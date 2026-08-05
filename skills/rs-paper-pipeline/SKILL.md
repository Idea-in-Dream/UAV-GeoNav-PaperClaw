---
name: rs-paper-pipeline
description: Use this skill when operating or maintaining the RS-PaperClaw pipeline that fetches remote-sensing arXiv papers, creates per-paper issues, builds daily digests, reconciles issue sets, and syncs daily_reports back to the repository.
---

Operate this skill from `skills/rs-paper-pipeline/`.

## Required environment

- `GITHUB_TOKEN`
- `LLM_API_KEY`

Optional:

- `DINGTALK_WEBHOOK`
- `FEISHU_TARGET`
- `RS_GITHUB_REPO`
- `LLM_MODEL`
- `LLM_THINKING_MODE`
- `LLM_API_URL`

## Entry points

- environment check:
  - `python3 scripts/cli.py doctor`
- standard pipeline run:
  - `python3 scripts/cli.py run`
- historical replay without notify:
  - `python3 scripts/cli.py run --date YYYYMMDD --no-notify`
- filter preview:
  - `python3 scripts/cli.py filter --dry-run --date YYYYMMDD`
- reconcile issue set:
  - `python3 scripts/cli.py reconcile --date YYYYMMDD --dry-run`
  - `python3 scripts/cli.py reconcile --date YYYYMMDD`

## Filtering rules

Do not hardcode article-list rules in Python.

- remote-sensing query terms and regex live in `scripts/config/filter_keywords.json`
- the LLM cross-filter prompt lives in `scripts/prompts/filter_cross_prompt.md`

If filtering behavior changes, update those files first, then validate with `filter --dry-run`.
