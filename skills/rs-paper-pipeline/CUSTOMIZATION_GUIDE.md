# 自定义你的论文系统

这份文档面向想基于 `RS-PaperClaw` 改造自己论文系统的读者。

目标不是解释全部实现细节，而是告诉你最短路径：

1. 改抓取范围
2. 改筛选规则
3. 改提示词
4. 改推送和目标仓库
5. 用最小成本验证你的修改

---

## 1. 先明确哪些东西该改，哪些不要急着改

通常只需要先改这几类：

- `scripts/config/filter_keywords.json`
- `scripts/prompts/filter_cross_prompt.md`
- `.env` 里的目标仓库、模型、通知配置

不建议一上来就改这些：

- `paper_processor.py`
- `daily_digest_llm_upgrade.py`
- GitHub Actions 主逻辑

先把“抓什么论文、怎么筛、推到哪里”调对，系统就能工作。后面的摘要风格、单篇 issue 模板、日报文风再慢慢调。

---

## 2. 改你要追踪的论文主题

核心文件：

- `scripts/config/filter_keywords.json`

这个文件里有三组配置：

- `rs_query_terms`
  这是 arXiv 初始检索词，会直接影响候选池大小。
- `rs_signal_patterns`
  这是本地硬过滤 regex，用来判断标题或摘要里是否真的有“主题证据”。
- `candidate_priority_patterns`
  候选超过每日上限时，按这些强信号优先保留定位与地图匹配论文。
- `ai_signal_patterns`
  这是交叉筛选的第二组信号，用来保留“主题 x AI/CV/基础模型”交叉论文。
- `candidate_limit_per_day`
  这是每天送入 LLM 的候选上限，默认 50；候选层建议维持约 10–50 篇的宽召回。

### 2.1 如果你要做“遥感 x AI”

通常只需要继续维护当前这三组词，不用改结构。

### 2.2 如果你要改成别的主题

例如改成：

- 医学影像 x AI
- 机器人 x 大模型
- 3D Vision x Foundation Model

你应该这样改：

1. 先把 `rs_query_terms` 改成你的主题检索词
2. 再把 `rs_signal_patterns` 改成“必须出现的主题证据”
3. `ai_signal_patterns` 一般还能保留原有大部分内容

关键原则：

- `query_terms` 负责“多抓一些”
- `signal_patterns` 负责保留可能相关的主题语境，不替代 LLM 做最终相关性判断
- 普通检测、分割、跟踪等常见误命中由 LLM 根据标题和摘要排除
- 证据不足但可能相关的论文应保留并标记 `Needs-Review`

不要只改检索词、不改硬过滤。否则很容易把不相关论文抓进来。

### 2.3 一个实际判断标准

如果一篇论文不该进系统，那么它至少应该在下面一层被挡住：

- 抓取层没命中
- 本地主题硬过滤没命中
- LLM 交叉筛选没命中

如果这三层都挡不住，说明规则太松了。

---

## 3. 改筛选 prompt

核心文件：

- `scripts/prompts/filter_cross_prompt.md`

这个 prompt 决定 LLM 如何在候选论文里做二次筛选。

建议你只改三类内容：

- 主题定义
- 明确保留条件
- 明确排除条件

例如你可以改成：

- “必须出现医学影像场景词，如 CT、MRI、ultrasound”
- “若只是通用 NLP 或通用 agent，没有医学场景，一律排除”

### 3.1 prompt 改法建议

保留这种结构最稳：

1. 先写“要什么”
2. 再写“必须看见什么证据”
3. 最后写“哪些常见误伤要排除”
4. 返回格式永远要求严格 JSON

### 3.2 不要做的事

- 不要只写“请筛选相关论文”
- 不要把判断标准写得很文学化
- 不要允许返回解释性长文本

这个 prompt 是生产链路，不是聊天问答。

---

## 4. 其他 prompt 可以什么时候改

除了筛选 prompt，这个项目还有：

- `scripts/prompts/summarize_prompt.md`
- `scripts/prompts/translate_prompt.md`
- `scripts/prompts/tags_prompt.md`

它们分别影响：

- 单篇论文 10 问分析
- 中文摘要翻译
- 标签提取

如果你只是想“换主题”，通常先不要动它们。  
如果你想让 issue 风格更偏你的领域，再考虑微调这些 prompt。

---

## 5. 改配置项

核心文件：

- `.env`
- `.env.example`

最常见配置项如下。

### 5.1 必填

- `GITHUB_TOKEN`
  用来读写 issue、同步 `daily_reports/`
- `LLM_API_KEY`
  用来调用 LLM

### 5.2 常用可选项

- `RS_GITHUB_REPO`
  目标仓库，默认是 `thinson/RS-PaperClaw`
- `LLM_MODEL`
  使用的模型名
- `LLM_THINKING_MODE`
  全文结构化分析的 thinking 模式，可设为 `enabled` 或 `disabled`；初筛、翻译和标签固定关闭
- `LLM_API_URL`
  OpenAI-compatible Chat Completions 接口地址
- `GITHUB_TIMEOUT`
  GitHub API 超时秒数
- `GITHUB_RETRY`
  GitHub API 重试次数
- `ARXIV_API_URL`
  arXiv API 地址
- `ARXIV_USER_AGENT`
  请求 arXiv 时使用的 User-Agent

### 5.3 通知相关

- `DINGTALK_WEBHOOK`
  配了就可以发钉钉机器人
- `FEISHU_TARGET`
  配合可用 `openclaw` 时可发飞书
- `OPENCLAW_BIN`
  当 runner 或本机环境里 `openclaw` 不在 PATH 时可显式指定

### 5.4 网络相关

- `RS_PROXY_URL`
  本机需要代理时可设置

### 5.5 规则文件路径

- `RS_FILTER_KEYWORDS_FILE`
- `RS_FILTER_PROMPT_FILE`

默认已经指向仓库内文件。  
只有当你想做多套规则切换时，才建议覆盖这两个路径。

---

## 6. 如果你想把结果推到自己的仓库

只需要改：

- `RS_GITHUB_REPO=your-name/your-repo`

但前提是：

- `GITHUB_TOKEN` 对这个仓库有写权限
- 仓库允许创建 issue
- 仓库允许写入 `daily_reports/` 和 `papers/previews/`

建议直接 fork 一份，再改 `RS_GITHUB_REPO` 指向你的 fork。

---

## 7. 最小验证流程

改完不要立刻跑全量。

建议按这个顺序：

### 7.1 先做环境检查

```bash
cd skills/rs-paper-pipeline
python3 scripts/cli.py doctor
```

### 7.2 先看筛选结果

```bash
python3 scripts/cli.py filter --dry-run --date 20260317
```

你要重点看：

- 候选数是否离谱
- 筛中论文是否真的符合主题
- 有没有明显误伤

### 7.3 再跑单日但不通知

```bash
python3 scripts/cli.py run --date 20260317 --no-notify
```

### 7.4 如果之前跑脏了，再对账

```bash
python3 scripts/cli.py reconcile --date 20260317 --dry-run
python3 scripts/cli.py reconcile --date 20260317
```

---

## 8. GitHub Actions 怎么配合你的定制

仓库里当前有两个 workflow：

- `.github/workflows/rs-pipeline-schedule.yml`
- `.github/workflows/rs-pipeline-manual.yml`

它们都会读取仓库内的：

- `scripts/config/filter_keywords.json`
- `scripts/prompts/filter_cross_prompt.md`

所以你改完规则文件后：

- 本地运行会生效
- GitHub Actions 也会同步生效

不需要在 workflow 里再复制一份关键词或 prompt。

---

## 9. 常见坑

### 9.1 候选太少

通常是：

- `rs_query_terms` 太窄
- `rs_signal_patterns` 太苛刻

### 9.2 候选很多，但筛选很脏

通常是：

- 检索词太泛
- 主题硬过滤没写严
- prompt 里没写清楚排除条件

### 9.3 GitHub Actions 能跑，本地不行

通常是：

- 本地没配 `.env`
- 本地缺 `pdftoppm` / `pdftotext`
- 本地网络或代理有问题

### 9.4 reconcile 报没有 stats

现在已经支持自动重建 stats。  
如果还是异常，先单独跑一次：

```bash
python3 scripts/cli.py filter --dry-run --date YYYYMMDD
```

---

## 10. 推荐的改造顺序

如果你准备把它改造成自己的论文系统，推荐顺序是：

1. fork 仓库
2. 改 `RS_GITHUB_REPO`
3. 改 `filter_keywords.json`
4. 改 `filter_cross_prompt.md`
5. 本地跑 `filter --dry-run`
6. 本地跑 `run --date ... --no-notify`
7. 再启用 GitHub Actions
8. 最后再改摘要风格、标签和日报文风

这样最稳。
