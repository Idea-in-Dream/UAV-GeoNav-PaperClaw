# RS-PaperClaw Agent Guide

这份文档写给“接手此目录的其他 agent”。

目标不是解释所有历史背景，而是让你在最短时间内：

- 理解这套流水线现在到底做什么
- 知道应该跑哪些命令
- 知道哪些文件是可信状态来源
- 知道什么时候需要人工介入
- 避免把非遥感论文混进日报

## 1. 先看什么

推荐阅读顺序：

1. `PROJECT_OVERVIEW.md`
2. `AGENT_GUIDE_RS_PIPELINE.md`
3. `RUNBOOK_RS_PIPELINE.md`
4. `scripts/cli.py`
5. `scripts/pipeline_config.py`
6. `scripts/run_rs_daily_workday.py`
7. `scripts/daily_arxiv_cross_filter.py`
8. `scripts/daily_digest_llm_upgrade.py`
9. `scripts/paper_processor.py`

## 2. 这套程序的真实边界

当前只做一件事：

- 从 arXiv 抓遥感相关论文
- 筛出“遥感 x AI / 基础模型 / 计算机视觉”交叉论文
- 为每篇论文创建或更新 GitHub issue
- 生成 `日报 YYYYMMDD`
- 把日报同步回目标仓库 `daily_reports/YYYYMM/YYYYMMDD.md`

不要把它当成一个通用论文系统，也不要默认它能处理新闻、博客、非遥感综述或任意 AI 论文。

## 3. 核心入口

统一入口：

```bash
python3 scripts/cli.py --help
```

最常用命令：

```bash
python3 scripts/cli.py doctor
python3 scripts/cli.py run
python3 scripts/cli.py run --date 20260316 --no-notify
python3 scripts/cli.py filter --dry-run --date 20260316
python3 scripts/cli.py digest --date 20260316 --stats-json memory/rs_daily_stats_20260316.json
python3 scripts/cli.py reconcile --date 20260316 --dry-run
python3 scripts/cli.py reconcile --date 20260316
python3 scripts/cli.py sync
```

命令语义：

- `doctor`：只检查环境，不访问完整业务链路
- `run`：标准总流程，包含 `filter -> digest -> sync -> 可选 notify`
- `filter`：只做候选抓取、交叉筛选、issue 去重、单篇处理
- `digest`：只重新生成日报 issue
- `reconcile`：按 stats 里的 `selected_arxiv_ids` 清理某天多余 issue，并可选重建日报与 sync
- `sync`：只把日报 markdown 同步回目标仓库

通知通道说明：

- 配了 `FEISHU_TARGET` 且本机存在可用 `openclaw` 时，会发飞书
- 配了 `DINGTALK_WEBHOOK` 时，会直接发钉钉机器人
- 两者都配置时，会同时尝试

筛选配置说明：

- arXiv 检索词、遥感信号 regex、AI 信号 regex 来自 `scripts/config/filter_keywords.json`
- LLM 交叉筛选 prompt 来自 `scripts/prompts/filter_cross_prompt.md`
- 如需临时切换配置文件，可通过 `RS_FILTER_KEYWORDS_FILE` 和 `RS_FILTER_PROMPT_FILE` 覆盖路径

## 4. 标准运行方式

### 4.1 运行默认日报

```bash
python3 scripts/cli.py run
```

默认行为：

- 如果不传 `--date`，脚本默认处理前一个自然日
- 定时任务每周 7 天运行，因此周末不再集中到周二补跑
- 自动模式默认允许通知

### 4.2 追跑历史日期

```bash
python3 scripts/cli.py run --date 20260316 --no-notify
```

这是最常用的追跑方式。除非用户明确要求，不要对历史追跑开启通知。

### 4.3 只验证筛选结果

```bash
python3 scripts/cli.py filter --dry-run --date 20260316
```

这个命令非常重要。遇到“筛选质量可疑”时，不要先重跑全流程，先看 dry-run。

## 5. 可信状态文件

本地状态主要看 `memory/`：

- `memory/pipeline_state/YYYYMMDD.json`
- `memory/rs_daily_stats_YYYYMMDD.json`

### 5.1 `pipeline_state`

这是总调度状态机。

关键字段：

- `step`
- `status`
- `reason`
- `failed_command`
- `stats_path`
- `daily_report_file`

常见状态：

- `precheck/failed`
- `filter/running`
- `filter/ok`
- `digest/ok`
- `sync/ok`
- `done/ok`

如果 `status=failed`，优先相信这里，不要先猜。

### 5.2 `rs_daily_stats`

这是当天筛选快照。

关键字段：

- `candidate_count`
- `llm_selected_count`
- `existing_count`
- `todo_count`
- `candidate_arxiv_ids`
- `selected_arxiv_ids`
- `existing_arxiv_ids`
- `todo_arxiv_ids`

这个文件现在不仅记录数量，也记录集合本身。后续 `digest` 会优先依赖 `selected_arxiv_ids`，所以它是“当天应该进日报的论文集合”的最重要本地依据。

## 6. 程序内部链路

### 6.1 `run_rs_daily_workday.py`

职责：

- 加锁防并发
- 做 GitHub 连通性检查
- 调 `filter`
- 调 `digest`
- 调 `sync`
- 记录状态文件

如果 `run` 行为异常，先看这里的状态落盘是否正确。

### 6.2 `daily_arxiv_cross_filter.py`

职责：

- 从 arXiv 拉候选
- 做遥感硬过滤
- 调 LLM 做交叉筛选
- 基于现有 GitHub issue 去重
- 对 `todo` 调 `paper_processor`

这个脚本已经做过两层收紧：

- 遥感信号必须能从标题或摘要中直接匹配到
- LLM 返回后还会再过一层本地遥感硬过滤
- 检索词和 prompt 都从文件读取，不要再把筛选规则散写回代码

因此，`selected` 理论上应该已经明显优于老版本，但仍可能存在“边界论文是否保留”的人工判断空间。

### 6.3 `paper_processor.py`

职责：

- 下载 PDF
- 生成本地预览图并上传 GitHub
- 做翻译、标签、十问总结
- 通过质量门禁后创建或更新 issue

如果单篇处理慢，通常卡在：

- PDF 下载
- PDF 转图片
- LLM 总结
- GitHub 上传图片

### 6.4 `daily_digest_llm_upgrade.py`

职责：

- 根据 open paper issues 生成日报内容
- 优先使用 stats 文件里的 `selected_arxiv_ids`
- 如果预期论文集合还没完整可见，会重试；仍不完整则直接失败

这一点很关键：程序现在不再允许“缺一篇但静默生成日报”。

## 7. 如何判断筛选是否出错

优先检查这三层：

1. `candidate_items`
2. `selected_items`
3. 目标仓库里打开的 `YYYYMMDD` 论文 issue

判断顺序：

- 如果 `candidate_items` 就已经明显脏，问题在遥感硬过滤
- 如果 `selected_items` 脏，问题在 LLM 交叉筛选或边界定义
- 如果 `selected_items` 是对的，但日报少篇，问题在 digest / issue 可见性

## 8. 遇到误入论文怎么处理

如果某一天已经有明显不相关的 issue 混进仓库，不要只重跑日报。

正确顺序：

1. 列出该日期当前打开的 issues
2. 关闭明显不相关项，并留一句说明 comment
3. 如有必要，重跑 `filter --dry-run --date YYYYMMDD` 验证新的集合
4. 重跑 `digest --date YYYYMMDD --stats-json ...`
5. 重跑 `sync`

不要跳过“关闭旧 issue”这一步，否则日报生成器仍可能把它们当成当天论文。

如果只是“上一版跑过一轮，现在要按最新 stats 自动收口”，优先用：

```bash
python3 scripts/cli.py reconcile --date YYYYMMDD --dry-run
python3 scripts/cli.py reconcile --date YYYYMMDD
```

这个命令会：

- 读取 `memory/rs_daily_stats_YYYYMMDD.json`
- 以其中的 `selected_arxiv_ids` 为准
- 对比目标仓库当天所有 open issues
- 自动关闭多余 issue
- 重建 digest
- 执行 sync

## 8.1 GitHub Actions

仓库已提供工作流：

```bash
.github/workflows/rs-pipeline-schedule.yml
.github/workflows/rs-pipeline-manual.yml
```

默认策略：

- `rs-pipeline-schedule.yml` 在北京时间每天 08:00 触发
- `rs-pipeline-manual.yml` 只负责手动运维
- 两个 workflow 都调用统一 CLI，不额外复制 Python 业务逻辑
- 默认走仓库内的筛选配置文件
- 无通知通道时自动退到 `--no-notify`
- 手动触发支持：
  - `run`
  - `reconcile`
  - `doctor`

## 9. 常见问题

### 9.1 GitHub SSL EOF

现象：

- `requests.exceptions.SSLError`
- `EOF occurred in violation of protocol`

处理：

- 先确认代理节点
- 再重跑命令
- 不要急着改代码

### 9.2 arXiv 429

现象：

- `HTTP Error 429`

处理：

- 等一段时间再试
- 优先用现有 `stats`、GitHub issue 集合做本地核对
- 不要连续高频重刷 `filter`

### 9.3 `preview_images=0`

优先检查：

- `pdftoppm` 是否存在
- PDF 是否下载成功
- 本地 `papers/figures/` 是否产出图片
- GitHub 图片上传是否成功

### 9.4 状态停在 `filter/running`

优先判断是不是“真的卡住”还是“正在跑很多单篇”。

方法：

- 看 `rs_daily_stats_YYYYMMDD.json` 是否已生成
- 看目标仓库当天 issue 是否在持续增加
- 如果在持续增加，说明只是批量处理慢

## 10. 给其他 agent 的执行建议

### 10.1 先验证，再大动作

顺序建议：

1. `doctor`
2. `filter --dry-run`
3. 看 `stats`
4. 再决定是否 `run`

### 10.2 不要手工改日报正文来“掩盖”问题

如果日报漏篇，修 `digest` 或修 issue 集合，不要直接改 markdown 文本。

### 10.3 不要默认所有带 UAV / satellite / SAR 的论文都应该进

边界论文很多，尤其是：

- 通用机器人 / 导航
- 通用 agent / LLM / tool use
- 农业视觉但没有遥感观测场景
- 纯时序 / 相似度 / 数据库 / 网络安全

必须看标题和摘要里是否有清晰的遥感场景、传感器或任务。

### 10.4 遇到“统计和日报数量不一致”时怎么做

这是重点排障顺序：

1. 看 `selected_arxiv_ids`
2. 看 open issues 是否完整覆盖这些 arXiv ID
3. 看日报正文里的 issue 列表是否与之对应

如果第 1 步和第 2 步不一致：

- 问题在 issue 创建或可见性

如果第 2 步和第 3 步不一致：

- 问题在 digest 收集逻辑

## 11. 这个目录里什么是核心文件

保留这些就够：

- `PROJECT_OVERVIEW.md`
- `AGENT_GUIDE_RS_PIPELINE.md`
- `RUNBOOK_RS_PIPELINE.md`
- `scripts/PIPELINE_SOP.md`
- `scripts/cli.py`
- `scripts/run_rs_daily_workday.py`
- `scripts/daily_arxiv_cross_filter.py`
- `scripts/paper_processor.py`
- `scripts/daily_digest_llm_upgrade.py`
- `scripts/sync_daily_reports_to_repo.py`
- `scripts/clients/`
- `scripts/services/`
- `scripts/prompts/`
- `.env.example`
- `requirements.txt`
- `bootstrap.sh`

`memory/` 和 `papers/` 是运行期目录，不是文档目录。

## 12. 最短上手路径

如果你是新 agent，直接按下面做：

```bash
python3 scripts/cli.py doctor
python3 scripts/cli.py filter --dry-run --date 20260316
cat memory/rs_daily_stats_20260316.json
python3 scripts/cli.py run --date 20260316 --no-notify
```

跑完后核对：

```bash
cat memory/pipeline_state/20260316.json
python3 scripts/cli.py digest --date 20260316 --stats-json memory/rs_daily_stats_20260316.json
python3 scripts/cli.py sync
```

如果你只能记住一句话：

先看 `stats`，再看 open issues，最后看 digest。
