#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from functools import lru_cache

from pipeline_config import load_config


CONFIG = load_config()
LABELS_PATH = CONFIG.scripts_dir / "config" / "labels.json"
DATE_LABEL_PATTERN = re.compile(r"\d{8}")


@lru_cache(maxsize=1)
def load_label_definitions() -> dict[str, dict[str, str]]:
    if not LABELS_PATH.exists():
        raise RuntimeError(f"Missing labels config file: {LABELS_PATH}")
    data = json.loads(LABELS_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data:
        raise RuntimeError(f"Invalid labels config file: {LABELS_PATH}")
    return data


def allowed_paper_labels() -> set[str]:
    return set(load_label_definitions()) - {"日报"}


def normalize_paper_labels(labels: list[str] | tuple[str, ...] | None) -> list[str]:
    allowed = allowed_paper_labels()
    normalized: list[str] = []
    for raw in labels or []:
        name = str(raw).strip().strip("`[]\"'")
        if name in allowed and name not in normalized:
            normalized.append(name)
    return normalized


def has_confirmed_public_code(resource_answer: str) -> bool:
    text = " ".join((resource_answer or "").split())
    lowered = text.casefold()
    negative_markers = (
        "未发现公开代码",
        "无公开代码",
        "代码尚未公开",
        "代码暂未公开",
        "暂未发布",
        "尚未发布",
        "will be released",
        "coming soon",
        "占位地址",
        "placeholder",
    )
    if any(marker in lowered for marker in negative_markers):
        return False
    return bool(
        re.search(
            r"https?://(?:www\.)?(?:github\.com|gitlab\.com|bitbucket\.org|gitee\.com)/[^\s<>()（）]+",
            text,
            re.IGNORECASE,
        )
    )


def normalize_resource_labels(labels: list[str], resource_answer: str) -> list[str]:
    normalized = list(dict.fromkeys(labels))
    if not has_confirmed_public_code(resource_answer):
        normalized = [label for label in normalized if label != "Code-Available"]
    return normalized


def _definition_for(name: str) -> dict[str, str]:
    configured = load_label_definitions().get(name)
    if configured:
        return configured
    if DATE_LABEL_PATTERN.fullmatch(name):
        return {"color": "DDEEFF", "description": f"论文业务日期 {name}"}
    return {"color": "EDEDED", "description": "UAV GeoNav PaperClaw 自动标签"}


def ensure_repo_labels(repo, names: list[str] | tuple[str, ...] | set[str]) -> None:
    wanted = [name for name in dict.fromkeys(str(item).strip() for item in names) if name]
    if not wanted:
        return

    existing = {label.name for label in repo.get_labels()}
    for name in wanted:
        if name in existing:
            continue
        definition = _definition_for(name)
        try:
            repo.create_label(
                name=name,
                color=definition.get("color", "EDEDED").lstrip("#"),
                description=definition.get("description", "")[:100],
            )
        except Exception:
            # 并发工作流可能在本次请求前刚创建同名标签。
            refreshed = {label.name for label in repo.get_labels()}
            if name not in refreshed:
                raise
        existing.add(name)


def ensure_all_static_labels(repo) -> None:
    ensure_repo_labels(repo, list(load_label_definitions()))
