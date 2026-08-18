#!/usr/bin/env python3
from __future__ import annotations

"""
从 arXiv 拉取今天+昨天提交的论文，先按遥感关键词 OR 初筛，
再用 LLM 筛选“遥感 x 基础模型/计算机视觉/人工智能交叉”论文，
最后去重（已存在于 GitHub issues 的 arXiv id）并调用现有流程更新/创建 issue。
"""

import re
import json
from datetime import datetime
from pathlib import Path

from clients.arxiv_client import fetch_recent_candidates, has_remote_sensing_signal
from clients.llm_client import call_llm
from paper_processor import process_paper
from pipeline_config import get_repo, load_config
from services.filter_assets import load_ai_signal_patterns, render_filter_prompt
from services.digest_builder import extract_author, extract_institution, is_invalid_digest_field, is_invalid_digest_institution
from services.issue_index import canonical_arxiv_id, ensure_index, lookup_issue, update_index_from_issue, save_index
from services.labels import normalize_paper_labels

CONFIG = load_config()
AI_MATCH_PATTERNS = load_ai_signal_patterns()
OBVIOUS_EXCLUSION_PATTERNS = [
    re.compile(r"(?i)\btracking\b"),
    re.compile(r"(?i)\bdetection\b"),
    re.compile(r"(?i)\bsegmentation\b"),
    re.compile(r"(?i)\b(?:path|trajectory|motion) planning\b"),
    re.compile(r"(?i)\b(?:obstacle|collision) avoidance\b"),
    re.compile(r"(?i)\b(?:in[- ]flight actuation|reconfigurable intelligent surface|wireless beamforming)\b"),
]
EXPLICIT_GEO_OUTPUT_PATTERNS = [
    re.compile(r"(?i)\b(?:geo[- ]?locali[sz]ation|geolocation|cross[- ]view locali[sz]ation)\b"),
    re.compile(r"(?i)\b(?:map matching|map registration|map alignment|UAV[- ]to[- ]satellite)\b"),
    re.compile(r"(?i)\b(?:absolute|global) (?:position|pose|locali[sz]ation)\b"),
    re.compile(r"(?i)\b(?:latitude|longitude|geographic coordinates?)\b"),
    re.compile(r"(?i)\b(?:6[- ]?DoF|camera pose)\b.{0,100}\b(?:map|satellite|georeferenced)\b"),
]
TRADITIONAL_LOCALIZATION_TITLE_PATTERN = re.compile(
    r"(?i)\b(?:visual[- ]inertial odometry|visual[- ]inertial navigation|VIO|"
    r"visual odometry|VO|SLAM|simultaneous locali[sz]ation and mapping)\b"
)
UAV_PLATFORM_PATTERN = re.compile(
    r"(?i)\b(?:UAVs?|drones?|quadrotors?|micro aerial vehicles?|MAVs?|aerial|airborne)\b"
)
NON_AERIAL_PLATFORM_PATTERN = re.compile(
    r"(?i)\b(?:humanoid|biped(?:al)?|legged robot|autonomous driv(?:ing|er)|"
    r"self[- ]driving|road vehicles?|wheel odometry|underwater|AUVs?|"
    r"marine robots?|endoscop(?:e|ic)|surgical robots?)\b"
)
NEGATED_OUTPUT_PREFIX_PATTERN = re.compile(
    r"(?i)(?:(?:does?|do|did|is|are|was|were|can|could|will|would)\s+not|"
    r"rather than|instead of|fails? to)\b.{0,80}$|\bwithout\s*$"
)


def has_ai_signal(text: str) -> bool:
    return any(pattern.search(text) for pattern in AI_MATCH_PATTERNS)


def has_explicit_geo_output(text: str) -> bool:
    """Require positive geo-output evidence instead of negated comparison wording."""
    for pattern in EXPLICIT_GEO_OUTPUT_PATTERNS:
        for match in pattern.finditer(text):
            prefix = text[max(0, match.start() - 100) : match.start()]
            clause_prefix = re.split(r"[.;\n]", prefix)[-1]
            if NEGATED_OUTPUT_PREFIX_PATTERN.search(clause_prefix):
                continue
            return True
    return False


def obvious_common_false_positive(candidate: dict) -> str | None:
    title = candidate["title"]
    text = f"{title}\n{candidate['abstract']}"
    non_aerial_platform = NON_AERIAL_PLATFORM_PATTERN.search(text)
    if non_aerial_platform and not UAV_PLATFORM_PATTERN.search(text):
        return f"明确面向非空中专用平台 {non_aerial_platform.group(0)}，且没有无人机迁移证据"
    matched_task = None
    for pattern in OBVIOUS_EXCLUSION_PATTERNS:
        matched_task = pattern.search(text)
        if matched_task:
            break
    if not matched_task:
        return None
    if has_explicit_geo_output(text):
        return None
    # SLAM/VO/VIO 论文常在摘要中描述 feature tracking、detection 或 segmentation
    # 子模块。标题明确以里程计/建图为主任务时，即使未写 UAV，
    # 也不应被普通检测、分割、跟踪门禁误伤。
    if TRADITIONAL_LOCALIZATION_TITLE_PATTERN.search(title):
        return None
    return f"明显属于普通{matched_task.group(0)}，且标题摘要没有地图绝对定位或地理坐标输出证据"


def keyword_fallback(candidates, reason: str):
    """Conservative title+abstract fallback used when LLM is unavailable."""
    out_items = []
    for candidate in candidates:
        text = f"{candidate['title']}\n{candidate['abstract']}"
        if not (has_remote_sensing_signal(text) and has_ai_signal(text)):
            continue
        safety_reason = obvious_common_false_positive(candidate)
        if safety_reason:
            print(f"  [安全门禁] 关键词回退排除 {candidate['arxiv_id']}: {safety_reason}")
            continue
        enriched = dict(candidate)
        enriched["filter_status"] = "needs_review"
        enriched["filter_labels"] = ["Needs-Review"]
        enriched["filter_reason"] = reason
        out_items.append(enriched)
    return out_items


def _extract_json_payload(raw_output: str):
    code_block = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_output)
    if code_block:
        json_str = code_block.group(1).strip()
    else:
        match = re.search(r"\{[\s\S]*\}|\[[\s\S]*\]", raw_output)
        json_str = match.group(0) if match else raw_output
    return json.loads(json_str)


def _parse_decision_items(items, default_status: str) -> dict[str, dict]:
    decisions: dict[str, dict] = {}
    if not isinstance(items, list):
        return decisions
    for item in items:
        if isinstance(item, str):
            arxiv_id = item.strip()
            labels: list[str] = []
            reason = ""
        elif isinstance(item, dict):
            arxiv_id = str(item.get("arxiv_id", "")).strip()
            labels = normalize_paper_labels(item.get("labels") or [])
            reason = str(item.get("reason", "")).strip()
        else:
            continue
        if not arxiv_id:
            continue
        if default_status == "needs_review" and "Needs-Review" not in labels:
            labels.append("Needs-Review")
        decisions[arxiv_id] = {
            "status": default_status,
            "labels": labels,
            "reason": reason,
        }
    return decisions


def _parse_llm_decisions(raw_output: str) -> tuple[dict[str, dict], bool]:
    """Parse structured decisions and retain compatibility with legacy ID arrays."""
    payload = _extract_json_payload(raw_output)
    if isinstance(payload, list):
        return _parse_decision_items(payload, "keep"), True
    if not isinstance(payload, dict):
        raise ValueError("LLM output must be a JSON object or array")

    decisions: dict[str, dict] = {}
    for status in ("keep", "needs_review", "exclude"):
        for arxiv_id, decision in _parse_decision_items(payload.get(status), status).items():
            if arxiv_id in decisions:
                raise ValueError(f"duplicate decision for {arxiv_id}")
            decisions[arxiv_id] = decision
    return decisions, False


def _match_id(cid: str, keep_set: set[str]) -> bool:
    cid_base = canonical_arxiv_id(cid)
    return any(cid_base == canonical_arxiv_id(item) for item in keep_set)


def _find_decision(arxiv_id: str, decisions: dict[str, dict]) -> dict | None:
    for decision_id, decision in decisions.items():
        if _match_id(arxiv_id, {decision_id}):
            return decision
    return None


def _llm_cross_filter_batch(candidates):
    if not candidates:
        return []

    payload = []
    for i, c in enumerate(candidates, 1):
        payload.append(f"[{i}] id={c['arxiv_id']} | title={c['title']} | abstract={c['abstract'][:2400]}")

    prompt = render_filter_prompt(payload)

    decisions = None
    legacy_array = False
    last_llm_error = None
    for attempt in range(2):
        try:
            out = call_llm(prompt, max_tokens=5000, timeout=240, thinking="disabled").strip()
        except Exception as exc:
            last_llm_error = exc
            print(f"  [LLM 请求] 第 {attempt + 1} 次失败: {exc}")
            if attempt == 0:
                print("  [LLM 请求] 重试中...")
            continue
        try:
            decisions, legacy_array = _parse_llm_decisions(out)
            break
        except Exception as exc:
            last_llm_error = exc
            print(f"  [LLM 解析] 第 {attempt + 1} 次失败: {exc}")
            if attempt == 0:
                print(f"  [LLM 解析] 原始输出: {out[:200]}")
                print("  [LLM 解析] 重试中...")

    if decisions is not None:
        result = []
        for candidate in candidates:
            decision = _find_decision(candidate["arxiv_id"], decisions)
            if decision is None:
                if legacy_array:
                    continue
                decision = {
                    "status": "needs_review",
                    "labels": ["Needs-Review"],
                    "reason": "LLM 未覆盖该候选，按保守策略保留待复核",
                }
            if decision["status"] == "exclude":
                continue
            safety_reason = obvious_common_false_positive(candidate)
            if safety_reason:
                print(f"  [安全门禁] 排除 {candidate['arxiv_id']}: {safety_reason}")
                continue
            enriched = dict(candidate)
            enriched["filter_status"] = decision["status"]
            enriched["filter_labels"] = normalize_paper_labels(decision.get("labels") or [])
            enriched["filter_reason"] = decision.get("reason", "")
            if decision["status"] == "needs_review" and "Needs-Review" not in enriched["filter_labels"]:
                enriched["filter_labels"].append("Needs-Review")
            result.append(enriched)
        print(f"  [LLM 解析] 成功，命中 {len(result)} 篇")
        return result

    # 两次都失败，降级到关键词交叉筛选
    print(f"  [LLM 降级] 两次均失败，改用关键词交叉筛选: {last_llm_error}")
    out_items = keyword_fallback(candidates, "LLM 请求或输出失败，关键词回退命中，需人工复核")
    print(f"  [关键词降级] 命中 {len(out_items)} 篇")
    return out_items


def llm_cross_filter(candidates, batch_size: int = 20):
    """Use title + abstract in bounded batches so every candidate can be classified."""
    selected = []
    for start in range(0, len(candidates), batch_size):
        batch = candidates[start : start + batch_size]
        print(f"  [LLM 批次] {start + 1}-{start + len(batch)}/{len(candidates)}")
        selected.extend(_llm_cross_filter_batch(batch))
    return selected


def compact_item(item: dict[str, object]) -> dict[str, object]:
    return {
        "arxiv_id": item["arxiv_id"],
        "published": item["published"],
        "title": item["title"],
        "filter_status": item.get("filter_status", ""),
        "filter_labels": item.get("filter_labels", []),
        "filter_reason": item.get("filter_reason", ""),
    }


def issue_has_valid_metadata(issue) -> bool:
    body = issue.body or ""
    authors = extract_author(body)
    institution = extract_institution(body)
    return (
        not is_invalid_digest_field(authors)
        and "et al." not in authors
        and not is_invalid_digest_institution(institution)
    )


def load_existing_issue_map(repo, index: dict[str, dict], arxiv_ids: list[str]) -> dict[str, object]:
    issue_map: dict[str, object] = {}
    for arxiv_id in arxiv_ids:
        issue = lookup_issue(repo, index, arxiv_id)
        if issue is not None:
            issue_map[arxiv_id] = issue
    return issue_map


def main(dry_run=False, days_back=2, stats_out: str | None = None, target_date: str | None = None):
    if not CONFIG.github_token and not dry_run:
        raise RuntimeError("Missing required environment variable: GITHUB_TOKEN")
    if not CONFIG.llm_api_key and not dry_run:
        raise RuntimeError("Missing required environment variable: LLM_API_KEY")

    repo = get_repo(CONFIG) if CONFIG.github_token else None
    index = ensure_index(repo) if repo is not None else {}

    if target_date:
        print(f"[1/5] 拉取指定日期 {target_date} 候选...")
        cands = fetch_recent_candidates(max_results=500, days_back=days_back, target_date=target_date)
    else:
        print(f"[1/5] 拉取最近 {days_back} 天候选...")
        cands = fetch_recent_candidates(max_results=500, days_back=days_back)
    cand_count = len(cands)
    print(f"  候选数: {cand_count}")

    print("[2/5] LLM 交叉筛选...")
    if CONFIG.llm_api_key:
        selected = llm_cross_filter(cands)
    else:
        print("  [DRY RUN] 未配置 LLM_API_KEY，使用标题+摘要关键词回退并统一标记 Needs-Review")
        selected = keyword_fallback(cands, "dry-run 未配置 LLM，关键词回退命中，需人工复核")
    selected_count = len(selected)
    print(f"  入选数: {selected_count}")

    print("[3/5] 读取 issue 去重...")
    selected_arxiv_ids = [x["arxiv_id"] for x in selected]
    existing_issue_map = load_existing_issue_map(repo, index, selected_arxiv_ids) if repo is not None else {}
    todo = []
    keep = []
    refresh = []
    for item in selected:
        issue = existing_issue_map.get(item["arxiv_id"])
        if issue is None:
            todo.append({"candidate": item, "issue_number": None, "reason": "missing"})
            continue
        if issue_has_valid_metadata(issue):
            keep.append(item)
        else:
            refresh.append(item)
            todo.append({"candidate": item, "issue_number": issue.number, "reason": "stale_metadata"})

    existing_count = len(keep)
    refresh_count = len(refresh)
    todo_count = len(todo)
    print(f"  已合格: {existing_count}，待刷新: {refresh_count}，待处理总数: {todo_count}")

    stats = {
        "date": target_date or datetime.now().strftime("%Y%m%d"),
        "candidate_count": cand_count,
        "llm_selected_count": selected_count,
        "existing_count": existing_count,
        "refresh_count": refresh_count,
        "todo_count": todo_count,
        "candidate_arxiv_ids": [x["arxiv_id"] for x in cands],
        "selected_arxiv_ids": [x["arxiv_id"] for x in selected],
        "existing_arxiv_ids": [x["arxiv_id"] for x in keep],
        "refresh_arxiv_ids": [x["arxiv_id"] for x in refresh],
        "todo_arxiv_ids": [x["candidate"]["arxiv_id"] for x in todo],
        "candidate_items": [compact_item(x) for x in cands],
        "selected_items": [compact_item(x) for x in selected],
        "successful_selected_arxiv_ids": [x["arxiv_id"] for x in keep],
        "successful_selected_items": [compact_item(x) for x in keep],
        "failed_arxiv_ids": [],
        "failed_items": [],
        "todo_items": [
            {
                **compact_item(x["candidate"]),
                "issue_number": x["issue_number"],
                "reason": x["reason"],
            }
            for x in todo
        ],
    }
    if stats_out:
        Path(stats_out).parent.mkdir(parents=True, exist_ok=True)
        Path(stats_out).write_text(json.dumps(stats, ensure_ascii=False), encoding="utf-8")

    if dry_run:
        print("[DRY RUN] 列表如下:")
        for x in todo:
            item = x["candidate"]
            print(
                f"  - {item['arxiv_id']} | {item['published']} | issue={x['issue_number'] or '-'} | "
                f"reason={x['reason']} | {item['title'][:90]}"
            )
        return

    print("[4/5] 提交 issue（不重复）...")
    for task in todo:
        aid = task["candidate"]["arxiv_id"]
        issue_number = task["issue_number"]
        print(f"  -> 处理 {aid} | issue={issue_number or '-'} | reason={task['reason']}")
        candidate = task["candidate"]
        result, error_msg = process_paper(
            aid,
            issue_number=issue_number,
            target_date=target_date,
            filter_labels=candidate.get("filter_labels"),
            needs_review=candidate.get("filter_status") == "needs_review",
        )
        if result is not None and hasattr(result, "number"):
            update_index_from_issue(index, aid, result)
        if result is None:
            stats["failed_arxiv_ids"].append(aid)
            stats["failed_items"].append(
                {
                    **compact_item(task["candidate"]),
                    "issue_number": issue_number,
                    "reason": task["reason"],
                    "error": error_msg or "未知错误",
                }
            )
        else:
            stats["successful_selected_arxiv_ids"].append(aid)
            stats["successful_selected_items"].append(compact_item(task["candidate"]))

        if stats_out:
            Path(stats_out).write_text(json.dumps(stats, ensure_ascii=False), encoding="utf-8")

    save_index(repo, index)
    print("[5/5] 完成")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--days", type=int, default=2, help="抓取最近 N 天的论文（默认2天）")
    parser.add_argument("--date", dest="date", help="抓取指定日期（YYYYMMDD）")
    parser.add_argument("--stats-out", dest="stats_out", help="输出统计 JSON 文件路径")
    args = parser.parse_args()

    main(dry_run=args.dry_run, days_back=args.days, stats_out=args.stats_out, target_date=args.date)
