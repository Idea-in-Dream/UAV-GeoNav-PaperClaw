# RS Paper Pipeline

This directory contains the operational pipeline behind `RS-PaperClaw`.

It is responsible for:

1. fetching remote-sensing related arXiv candidates
2. filtering `remote sensing x AI/CV/foundation model` papers
3. generating or updating per-paper GitHub issues
4. generating daily digest issues
5. syncing digest markdown back to the repository
6. optionally sending notifications

## Structure

```text
skills/rs-paper-pipeline/
├── .env.example
├── .gitignore
├── AGENT_GUIDE_RS_PIPELINE.md
├── PROJECT_OVERVIEW.md
├── RUNBOOK_RS_PIPELINE.md
├── bootstrap.sh
├── requirements.txt
├── scripts/
│   ├── cli.py
│   ├── pipeline_config.py
│   ├── clients/
│   ├── services/
│   ├── config/filter_keywords.json
│   └── prompts/
└── SKILL.md
```

## Setup

```bash
cd skills/rs-paper-pipeline
./bootstrap.sh
```

Fill `.env` with at least:

- `GITHUB_TOKEN`
- `LLM_API_KEY`

Optional:

- `DINGTALK_WEBHOOK`
- `FEISHU_TARGET`
- `RS_GITHUB_REPO`
- `LLM_MODEL`
- `LLM_THINKING_MODE`（全文结构化分析默认 `enabled`）
- `LLM_API_URL`

## Main commands

```bash
cd skills/rs-paper-pipeline
python3 scripts/cli.py doctor
python3 scripts/cli.py run
python3 scripts/cli.py run --date 20260317 --no-notify
python3 scripts/cli.py filter --dry-run --date 20260317
python3 scripts/cli.py reconcile --date 20260317 --dry-run
```

## Customization

If you want to adapt this project into your own paper system, read:

- `CUSTOMIZATION_GUIDE.md`

That guide covers:

- how to change topic keywords and regex
- how to change the filter prompt
- how to point the pipeline to your own GitHub repository
- what each important `.env` variable does
- how to validate your customized setup safely

## Filter configuration

The article-list filtering rules are file-based, not hardcoded in Python:

- keywords and regex: `scripts/config/filter_keywords.json`
- LLM filter prompt: `scripts/prompts/filter_cross_prompt.md`

Both local runs and GitHub Actions read the same files.

## Automation

Repository-level workflows live at:

- `.github/workflows/rs-pipeline-schedule.yml`
- `.github/workflows/rs-pipeline-manual.yml`

Both workflows execute this skill project via the unified CLI.
