<div align="center">
  <img src="./docs/logo-220.png" alt="UAV-GeoNav-PaperClaw" width="120" />

# UAV-GeoNav-PaperClaw

面向无人机定位、地图匹配与 GNSS 拒止导航的论文自动追踪仓库

**arXiv → 标题/摘要初筛 → LLM 二次筛选 → 中文论文 Issue → 每日汇总 → GitHub Pages**

</div>

本项目基于 [thinson/RS-PaperClaw](https://github.com/thinson/RS-PaperClaw) 改造，保留其 Python 流水线、GitHub Issues、GitHub Actions、日报归档与 Pages 前端。上游许可证与版权信息保留在 [`skills/rs-paper-pipeline/LICENSE`](./skills/rs-paper-pipeline/LICENSE)。

## 项目用途

系统每天自动从 arXiv 检索并分析以下方向：

- 无人机视觉定位、绝对定位与全局重定位；
- UAV-to-Satellite、跨视角检索、粗定位与精配准；
- 正射影像、TDOM、DSM、DEM 和 GIS 地图配准；
- 三维地理地图、3DGS、NeRF 地图定位；
- 地图辅助 VIO、SLAM、惯性导航和 GNSS 拒止导航；
- 无人机、四旋翼和 MAV 的传统 SLAM、视觉里程计（VO）与视觉惯性里程计（VIO）；
- 无人机自身定位与目标地理定位；
- 热红外无人机与卫星/地图的跨模态定位；
- 直接相关的数据集、基准、尺度恢复和复现资源。

普通遥感检测/分割/变化检测、纯 UAV 检测/跟踪/规划、没有空中平台应用证据的通用 SLAM/VO/VIO，以及仅卫星影像之间的配准会被排除。不确定条目会保留并标记 `Needs-Review`。

## 输出内容

每篇入选论文对应一个中文 GitHub Issue，包含：

- 论文标题、arXiv 链接、发表时间、作者和单位；
- 公开代码与资源、任务类型、地图类型、输入传感器、定位输出；
- 核心方法、实验精度、运行速度与硬件；
- 是否融合 VIO/IMU、复现难度；
- 对当前无人机定位项目的价值以及局限与风险。

同一 arXiv ID 的不同版本（如 `v1`、`v2`）会归一到同一 Issue，不会重复创建。

## 部署步骤

### 1. 创建目标仓库

推荐从本仓库复制或 fork，仓库名使用 `UAV-GeoNav-PaperClaw`，默认分支保持为 `main`。

在仓库设置中确认：

1. `Settings → Actions → General → Workflow permissions` 允许 GitHub Actions 读写仓库；
2. `Settings → Pages → Source` 选择 **GitHub Actions**；
3. Issues 功能已启用。

### 2. 配置 Secrets

进入 `Settings → Secrets and variables → Actions → Secrets`：

| 名称 | 必需 | 说明 |
|---|---:|---|
| `LLM_API_KEY` | 是 | OpenAI-compatible Chat Completions 接口密钥 |
| `UAV_GITHUB_TOKEN` | 否 | 默认使用内置 `GITHUB_TOKEN`；若组织策略禁止 Issues/Contents 写入，可配置具有目标仓库 `issues:write`、`contents:write` 权限的细粒度 PAT |
| `DINGTALK_WEBHOOK` | 否 | 钉钉通知 Webhook；不配置不影响论文追踪 |

不要把 Token、Key、Webhook 或个人信息写入 `.env.example`、工作流或代码。

### 3. 配置 Variables

进入 `Settings → Secrets and variables → Actions → Variables`：

| 名称 | 必需 | 推荐值/说明 |
|---|---:|---|
| `RS_GITHUB_REPO` | 否 | 默认自动使用当前仓库；跨仓库写入时设为 `OWNER/UAV-GeoNav-PaperClaw` |
| `LLM_MODEL` | 否 | 默认 `deepseek-v4-flash`；这是 DeepSeek 官方正式 API 模型别名，不是 Preview，当前对应 `DeepSeek-V4-Flash-0731` |
| `LLM_THINKING_MODE` | 否 | 全文结构化分析的 thinking 模式，`enabled`/`disabled`，默认 `enabled`；初筛、翻译、标签和日报始终关闭 |
| `LLM_API_URL` | 否 | 默认 `https://api.deepseek.com/chat/completions`，也可使用兼容接口 |
| `ARXIV_API_URL` | 否 | 默认 `https://export.arxiv.org/api/query` |
| `ARXIV_API_PROXY_PREFIX` | 否 | arXiv 返回 429/503 时使用的只读代理前缀；Actions 默认使用 AllOrigins |
| `ARXIV_USER_AGENT` | 否 | 建议包含仓库 URL 的自定义 User-Agent |
| `GITHUB_TIMEOUT` | 否 | 默认 `15` 秒 |
| `GITHUB_RETRY` | 否 | 默认 `2` 次 |
| `FEISHU_TARGET` | 否 | 飞书通知目标，需要同时配置可用的 `OPENCLAW_BIN` |
| `OPENCLAW_BIN` | 否 | OpenClaw 可执行文件路径，仅通知功能使用 |

### 4. 初始化标签

运行 `UAV GeoNav PaperClaw Manual` 工作流并选择 `doctor`，工作流会先自动创建所有静态标签。也可在本地执行：

```bash
cd skills/rs-paper-pipeline
python3 scripts/cli.py setup-labels
```

### 5. 首次运行

在 Actions 页面打开 `UAV GeoNav PaperClaw Manual`：

1. 点击 `Run workflow`；
2. `command` 选择 `run_no_notify`；
3. `date` 可留空，或填 arXiv 业务日期 `YYYYMMDD`；
4. 检查新建论文 Issues、`daily_reports/` 提交和 Pages 部署工作流。

## 本地运行

要求 Python 3.8+、`pdftoppm`、`pdftotext`；GitHub Actions 固定使用 Python 3.11。

```bash
cd skills/rs-paper-pipeline
./bootstrap.sh
cp .env.example .env
```

编辑 `.env`，至少填写：

```dotenv
GITHUB_TOKEN=YOUR_TOKEN
LLM_API_KEY=YOUR_LLM_KEY
RS_GITHUB_REPO=OWNER/UAV-GeoNav-PaperClaw
```

然后执行：

```bash
python3 scripts/cli.py doctor
python3 scripts/cli.py filter --dry-run --date 20260801
python3 scripts/cli.py run --date 20260801 --no-notify
```

`filter --dry-run` 会真实访问 arXiv、LLM 和 GitHub，但不会创建/更新论文 Issue；`run --no-notify` 会创建或更新 Issues、日报和索引，只跳过通知。

## 手动命令

```bash
cd skills/rs-paper-pipeline

# 环境检查
python3 scripts/cli.py doctor

# 初始化标签
python3 scripts/cli.py setup-labels

# 只看筛选结果
python3 scripts/cli.py filter --dry-run --date YYYYMMDD

# 完整运行且不通知
python3 scripts/cli.py run --date YYYYMMDD --no-notify

# 强制重跑已完成日期
python3 scripts/cli.py run --date YYYYMMDD --no-notify --force

# 回填日期区间；默认跳过已完成日期且不发送通知
python3 scripts/cli.py backfill --start YYYYMMDD --end YYYYMMDD

# 检查某天 Issue 集合差异
python3 scripts/cli.py reconcile --date YYYYMMDD --dry-run

# 重建 arXiv ID → Issue 索引
python3 scripts/cli.py rebuild-index
```

## 定时任务

`.github/workflows/rs-pipeline-schedule.yml` 使用：

```text
0 0 * * *
```

即每周 7 天 UTC 00:00（北京时间 08:00）运行一次，每次处理前一个自然日。GitHub Actions 可能因平台排队略有延迟。工作流会依次：

1. 安装 Python 与 Poppler；
2. 检查环境并初始化标签；
3. 从 arXiv 获取候选；
4. 执行关键词初筛和 LLM 二次筛选；
5. 创建或更新论文 Issue；
6. 创建或更新日报 Issue；
7. 同步 `daily_reports/YYYYMM/YYYYMMDD.md`；
8. 由 `deploy-pages.yml` 更新 GitHub Pages。定时/回填使用 `GITHUB_TOKEN` 提交日报时，Pages 通过 `workflow_run` 云端触发，不依赖本机在线。

历史区间回填使用 `.github/workflows/rs-pipeline-backfill.yml`。回填与每日定时任务共享写入并发锁，避免同时更新 Issues、索引和日报。本次 2026-07-06 至 2026-08-05 回填会强制按最新筛选规则重新评估，并自动收口旧日期的 Issue 集合。

## 如何调整关键词

编辑：

```text
skills/rs-paper-pipeline/scripts/config/filter_keywords.json
```

- `rs_query_terms`：发送给 arXiv 的检索词；
- `rs_signal_patterns`：标题与摘要的主题初筛正则；
- `candidate_priority_patterns`：候选超过上限时，优先保留定位与地图匹配强信号论文；
- `ai_signal_patterns`：LLM 异常时的保守回退信号。
- `candidate_limit_per_day`：每天送入 LLM 的候选上限，默认 50。

候选层采用宽召回策略，目标是每天约 10–50 篇；LLM 会阅读标题和摘要，排除普通检测、分割、跟踪等论文，并将证据不足的条目标记为 `Needs-Review`。

## 如何调整筛选标准

编辑：

```text
skills/rs-paper-pipeline/scripts/prompts/filter_cross_prompt.md
```

Prompt 要求 LLM 对每个候选返回 `keep`、`needs_review` 或 `exclude`，并只能使用配置好的无人机定位标签。筛选会把标题和摘要一起送给 LLM，不能只依赖标题关键词。

Issue 分析字段位于：

```text
skills/rs-paper-pipeline/scripts/prompts/summarize_prompt.md
```

标签名称、颜色和描述位于：

```text
skills/rs-paper-pipeline/scripts/config/labels.json
```

## GitHub Pages

`docs/index.html` 会在 GitHub Pages 环境中自动识别 `OWNER/REPO`，读取当前仓库的日报和 Issue。若在本地启动静态服务器，可显式传入仓库：

```text
http://localhost:8000/?repo=OWNER/UAV-GeoNav-PaperClaw
```

## 验证

运行单元与回归测试：

```bash
cd skills/rs-paper-pipeline
python3 -m unittest discover -s tests -v
```

回归集覆盖 GeoVINS、NGPS、PiLoT、PiLoT v2、AeroMap3D、RIM、Bearing-UAV、OffNadirLoc、Altitude-Adaptive Vision-Only Geo-Localization、无人机传统 SLAM/VO/VIO，并包含普通遥感目标检测和非无人机通用 SLAM 负例。

## 目录结构

```text
UAV-GeoNav-PaperClaw/
├── .github/workflows/                # 手动、每日定时与 Pages 部署
├── docs/                             # GitHub Pages 前端
├── daily_reports/                    # 每日 Markdown 汇总
├── papers/issue_index.json           # arXiv ID 去重索引
└── skills/rs-paper-pipeline/
    ├── scripts/cli.py
    ├── scripts/config/               # 关键词与标签
    ├── scripts/prompts/              # 筛选与结构化分析 Prompt
    ├── scripts/clients/              # arXiv、GitHub、LLM 客户端
    ├── scripts/services/             # 去重、标签、日报等服务
    └── tests/                        # 单元与目标论文回归测试
```
