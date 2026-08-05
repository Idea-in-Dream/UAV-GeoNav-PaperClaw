#!/usr/bin/env python3
from __future__ import annotations

import re

from pipeline_config import get_repo, load_config
from services.labels import normalize_resource_labels
from services.paper_analysis import format_resource_links_md


RELATION_SECTION_PATTERN = re.compile(
    r"\n### 与 GeoVINS / NGPS / PiLoT v2 的关系\s*\n[\s\S]*?(?=\n### 对当前无人机定位项目的价值)",
)
RESOURCE_SECTION_PATTERN = re.compile(
    r"^### (?:代码链接|公开代码与资源)\s*$\n[\s\S]*?(?=^### |\Z)",
    re.MULTILINE,
)
OFFNADIRLOC_PROJECT_URL = "https://montalario.github.io/offnadirloc/"


def remove_obsolete_relation_section(body: str) -> str:
    return RELATION_SECTION_PATTERN.sub("\n", body or "")


def _offnadirloc_resource_section() -> str:
    return "\n".join(
        [
            "### 公开代码与资源",
            f"- 项目主页：[OffNadirLoc]({OFFNADIRLOC_PROJECT_URL})",
            "- 公开代码：尚未发布。项目页中的 `Code (coming soon)` 仍指向占位地址，不能作为代码仓库。",
            "- 数据集与模型：页面展示了数据集说明，但未提供可下载数据、代码或权重链接。",
            "",
        ]
    ) + "\n"


def repair_resource_section(title: str, body: str) -> str:
    match = RESOURCE_SECTION_PATTERN.search(body or "")
    if not match:
        return body

    if "OffNadirLoc" in (title or ""):
        replacement = _offnadirloc_resource_section()
    else:
        section = match.group(0).replace("### 代码链接", "### 公开代码与资源", 1)
        section = re.sub(
            r"^(### 公开代码与资源\s*)\n(?:代码链接与开放资源|公开代码与资源)\s*\n",
            r"\1\n",
            section,
        )
        replacement = format_resource_links_md(section).rstrip() + "\n\n"

    return body[: match.start()] + replacement + body[match.end():]


def extract_resource_section(body: str) -> str:
    match = RESOURCE_SECTION_PATTERN.search(body or "")
    return match.group(0) if match else ""


def repair_issue_body(title: str, body: str) -> str:
    repaired = remove_obsolete_relation_section(body)
    repaired = repair_resource_section(title, repaired)
    return re.sub(r"\n{3,}", "\n\n", repaired).rstrip() + "\n"


def repaired_labels(label_names: list[str], body: str) -> list[str]:
    return normalize_resource_labels(label_names, extract_resource_section(body))


def update_embedded_label_row(body: str, label_names: list[str]) -> str:
    date_labels = [label for label in label_names if re.fullmatch(r"\d{8}", label)]
    other_labels = [label for label in label_names if label not in date_labels]
    ordered = date_labels + other_labels
    replacement = f"| **标签** | {', '.join(ordered)} |"
    return re.sub(r"^\| \*\*标签\*\* \|.*\|$", replacement, body, count=1, flags=re.MULTILINE)


def main() -> None:
    repo = get_repo(load_config())
    updated = 0
    for issue in repo.get_issues(state="all"):
        if (issue.title or "").strip().startswith("日报 "):
            continue
        old_body = issue.body or ""
        new_body = repair_issue_body(issue.title or "", old_body)
        old_labels = [label.name for label in issue.labels]
        new_labels = repaired_labels(old_labels, new_body)
        new_body = update_embedded_label_row(new_body, new_labels)
        if new_body == old_body and new_labels == old_labels:
            print(f"UNCHANGED issue #{issue.number}")
            continue
        issue.edit(body=new_body, labels=new_labels)
        print(f"UPDATED issue #{issue.number}")
        updated += 1
    print(f"DONE updated={updated}")


if __name__ == "__main__":
    main()
