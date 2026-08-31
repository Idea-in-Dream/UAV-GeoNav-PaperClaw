# RS-PaperClaw Runbook（可直接执行）

## 0. 环境
```bash
cd /path/to/RS-PaperClaw_pipeline
./bootstrap.sh
# 如 .env 是首次生成，编辑它并填入 GITHUB_TOKEN 和 LLM_API_KEY
```

如需代理，可在 `.env` 中设置：

```bash
RS_PROXY_URL=http://127.0.0.1:7897
```

如需通知，可在 `.env` 中任选一种：

```bash
# 飞书（依赖 openclaw）
FEISHU_TARGET=user:xxxx

# 钉钉机器人 webhook
DINGTALK_WEBHOOK=https://oapi.dingtalk.com/robot/send?access_token=xxxx
```

筛选规则文件默认从以下路径读取：

```bash
scripts/config/filter_keywords.json
scripts/prompts/filter_cross_prompt.md
```

如需覆盖路径，可在 `.env` 中设置：

```bash
RS_FILTER_KEYWORDS_FILE=scripts/config/filter_keywords.json
RS_FILTER_PROMPT_FILE=scripts/prompts/filter_cross_prompt.md
```

## 1) 运行默认日报（默认会推送）
```bash
python3 scripts/cli.py run
```

默认日期规则：

- GitHub 定时任务仅在周一至周五运行
- 周六、周日不自动更新论文
- 每次处理前一个自然日

## 2) 跑指定日期（默认不推送，适合追跑）
```bash
python3 scripts/cli.py run --date 20260312 --no-notify
```

## 3) 强制推送（仅在你确认需要时）
```bash
python3 scripts/cli.py run --date 20260312 --notify
```

## 4) 只做筛选，不跑日报
### 最近2天
```bash
python3 scripts/cli.py filter --days 2 --stats-out memory/rs_daily_stats_manual.json
```

### 指定日期
```bash
python3 scripts/cli.py filter --date 20260312 --stats-out memory/rs_daily_stats_20260312.json
```

## 4.1) 回填日期区间

```bash
python3 scripts/cli.py backfill --start 20260706 --end 20260805
```

默认不通知，并跳过已经完成且日报文件与 Digest Issue 一致的日期。失败日期会写入状态文件，其他日期继续执行；修复后可用同一命令恢复。

## 5) 只生成日报
```bash
python3 scripts/cli.py digest --date 20260312 --stats-json memory/rs_daily_stats_20260312.json
```

## 6) 同步日报 markdown 到仓库
```bash
python3 scripts/cli.py sync
```

## 6.1) 清理某天多余 issue 并重建日报
先预演：
```bash
python3 scripts/cli.py reconcile --date 20260317 --dry-run
```

确认无误后执行：
```bash
python3 scripts/cli.py reconcile --date 20260317
```

如只想清理 issue，不立即重建日报：
```bash
python3 scripts/cli.py reconcile --date 20260317 --skip-digest --skip-sync
```

## 6.2) 环境自检
```bash
python3 scripts/cli.py doctor
```

## 6.3) 只做筛选预演（不落 GitHub）
```bash
python3 scripts/cli.py filter --dry-run --date 20260312
```

## 7) 快速验收
```bash
# 看统计文件
cat memory/rs_daily_stats_20260312.json

# 看最近 issue（需代理）
curl -s "https://api.github.com/repos/thinson/RS-PaperClaw/issues?state=all&per_page=10" | python3 -c "import sys,json;d=json.load(sys.stdin);[print(f'#{x[\"number\"]}: {x[\"title\"]}') for x in d]"
```

## 8) 故障排查
- GitHub SSL EOF：先切 Clash 节点后重跑
- 历史追跑建议统一加 `--no-notify`，避免无关推送
- 如果筛选质量异常，先检查 `scripts/config/filter_keywords.json` 和 `scripts/prompts/filter_cross_prompt.md`
- 卡住进程：
```bash
ps -ef | grep daily_arxiv_cross_filter.py | grep -v grep
pkill -f daily_arxiv_cross_filter.py
```

## 9) GitHub Actions 部署
工作流文件已拆成两份：

```bash
.github/workflows/rs-pipeline-schedule.yml
.github/workflows/rs-pipeline-manual.yml
```

建议配置：

- Secret: `RS_GITHUB_TOKEN`
- Secret: `LLM_API_KEY`
- Secret: `DINGTALK_WEBHOOK`（如需通知）
- Variable: `RS_GITHUB_REPO`
- Variable: `LLM_MODEL`
- Variable: `LLM_THINKING_MODE`（默认 `enabled`，仅控制全文结构化分析）
- Variable: `LLM_API_URL`

行为说明：

- `rs-pipeline-schedule.yml`：北京时间每天 08:00 定时触发
- `rs-pipeline-manual.yml`：手动支持 `run / reconcile / doctor`
- 若无可用通知通道，定时任务会自动退到 `--no-notify`
- Actions 也会读取仓库内的筛选配置文件，不再把关键词和 prompt 写死在代码里
