# RS-PaperClaw Pipeline Overview

## 1. 这是什么

这个目录本质上是一个从 OpenClaw 工作区抽出来的“遥感论文日报流水线”快照，不是一个从零整理好的通用仓库。

当前真正还在工作的主目标只有一个：

- 从 arXiv 拉取遥感相关论文
- 用 LLM 进一步筛选“遥感 x AI/基础模型/计算机视觉”交叉论文
- 为每篇论文生成结构化 GitHub Issue
- 汇总当天通过质检的论文，生成“日报 YYYYMMDD”
- 把日报同步回目标仓库的 `daily_reports/YYYYMM/YYYYMMDD.md`

目录里原先混入了很多与这个目标无关的脚本，例如科技新闻推送、签到提醒、图像生成、一次性修复脚本、旧版论文处理链路。清理后只保留现行主流程和必要文档。

## 2. 当前有效的数据流

主入口：

```bash
python3 scripts/cli.py run
```

执行链路：

1. `scripts/run_rs_daily_workday.py`
   负责总调度、代理注入、GitHub 连通性检查、锁文件、防重入、状态落盘、可选飞书通知。
   默认日期策略为每天处理前一个自然日，周一至周日一致。
2. `scripts/daily_arxiv_cross_filter.py`
   从 arXiv API 拉取候选论文，按遥感关键词初筛，再用 LLM 做二次交叉筛选，并跳过已存在于 GitHub Issues 的论文。
3. `scripts/paper_processor.py`
   单篇论文处理核心。负责：
   - 抓取论文元信息
   - 下载 PDF
   - 用 `pdftoppm` 生成预览图并上传
   - 调 LLM 做摘要翻译、标签提取、A1-A10 十问总结
   - 执行质量门禁
   - 创建或更新 GitHub Issue
4. `scripts/daily_digest_llm_upgrade.py`
   读取当天论文 issue，生成“日报 YYYYMMDD” issue。
5. `scripts/sync_daily_reports_to_repo.py`
   将日报 issue 内容同步到目标仓库 `daily_reports/` 目录，并维护 `README.md`。

## 3. 保留文件说明

- `RUNBOOK_RS_PIPELINE.md`
  运维执行手册，适合人工补跑和故障排查。
- `AGENT_GUIDE_RS_PIPELINE.md`
  面向其他 agent 的详细接手说明，重点覆盖执行顺序、状态文件、排障路径和人工介入边界。
- `PROJECT_OVERVIEW.md`
  当前目录的项目总览。
- `scripts/PIPELINE_SOP.md`
  单篇论文处理 SOP 和质量门禁说明。
- `scripts/run_rs_daily_workday.py`
  每日日报总入口。
- `scripts/daily_arxiv_cross_filter.py`
  候选论文抓取和交叉筛选。
- `scripts/paper_processor.py`
  单篇论文处理主引擎。
- `scripts/daily_digest_llm_upgrade.py`
  日报生成器。
- `scripts/sync_daily_reports_to_repo.py`
  日报同步器。
- `scripts/prompts/`
  `paper_processor.py` 使用的提示词模板。
- `scripts/config/filter_keywords.json`
  文章 list 筛选的关键词与 regex 配置。
- `scripts/prompts/filter_cross_prompt.md`
  文章 list 交叉筛选使用的 LLM prompt 模板。
- `.github/workflows/rs-pipeline-schedule.yml`
  GitHub Actions 定时主跑入口。
- `.github/workflows/rs-pipeline-manual.yml`
  GitHub Actions 手动运维入口。

当前代码结构已经拆成三层：

- `scripts/*.py`
  命令入口和主编排。
- `scripts/clients/`
  外部系统接入层，目前包括 GitHub、arXiv、LLM。
- `scripts/services/`
  业务逻辑层，目前包括论文分析和日报构建。
- `scripts/cli.py`
  统一命令入口。
- `scripts/doctor.py`
  环境自检入口。

## 4. 配置方式

项目根目录支持 `.env` 配置文件，示例见 `.env.example`。

推荐初始化方式：

```bash
./bootstrap.sh
python3 scripts/cli.py doctor
```

最少需要提供：

- `GITHUB_TOKEN`
- `LLM_API_KEY`

常用可选项：

- `RS_GITHUB_REPO`
- `LLM_MODEL`
- `LLM_THINKING_MODE`
- `LLM_API_URL`
- `RS_PROXY_URL`
- `RS_WORKSPACE`
- `OPENCLAW_BIN`
- `FEISHU_TARGET`
- `DINGTALK_WEBHOOK`
- `RS_FILTER_KEYWORDS_FILE`
- `RS_FILTER_PROMPT_FILE`

## 5. 运行时依赖

- Python 3
- `PyGithub`
- `pdftoppm`
- `pdftotext`
- 可访问 GitHub、arXiv、LLM API 的网络环境

Python 依赖可通过 `python3 -m pip install -r requirements.txt` 安装。

脚本里还依赖若干外部资源：

- GitHub 仓库：`thinson/RS-PaperClaw`
- 百炼兼容接口
- OpenClaw CLI（用于通知）

## 6. 目录特征和遗留问题

这个项目仍然保留了“运维脚本”风格，而不是“工程化包”风格，主要表现为：

- 主要入口依旧是脚本，不是 Python package CLI
- 依赖外部服务较多，运行成功高度依赖环境变量和网络

相比原始版本，当前已去掉硬编码 token，并改为从 `.env` 或环境变量读取；工作目录默认取当前仓库根目录，也可以通过 `RS_WORKSPACE` 覆盖。若 `RS_WORKSPACE` 指向的旧 OpenClaw 路径不存在，程序会自动回退到当前仓库根目录。

文章 list 的筛选规则也已经外置化：关键词、regex 和 LLM prompt 不再写死在代码里，默认从仓库文件读取，因此本地运行和 GitHub Actions 会使用同一套筛选定义。

因此它更像一套“可迁移的自动化流水线”，但还没有完全演进成标准化应用。

## 7. 推荐理解顺序

如果你以后继续接手这个目录，建议按下面顺序读：

1. `PROJECT_OVERVIEW.md`
2. `AGENT_GUIDE_RS_PIPELINE.md`
3. `RUNBOOK_RS_PIPELINE.md`
4. `scripts/cli.py`
5. `scripts/pipeline_config.py`
6. `scripts/run_rs_daily_workday.py`
7. `scripts/clients/`
8. `scripts/services/`
