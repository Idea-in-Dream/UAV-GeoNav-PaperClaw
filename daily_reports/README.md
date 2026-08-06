# Daily Reports

最近三天日报（最新在前）：

# [20260804](./202608/20260804.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 0 篇。

当日未检索到符合条件并纳入日报的论文。

## 🔎 观察

- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。
- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。

---

Powered by OpenClaw🦞

---

# [20260722](./202607/20260722.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦无人机跨视角地理定位，提出两项新框架与基准。RIM框架通过检索匹配实现跨域全局定位，应对GNSS拒止环境；OffNadirLoc基准则针对大倾斜视角下的定位挑战，两者均公开代码与数据集，推动无人机-卫星视觉定位的鲁棒性与可复现性研究。

## ✨ 今日亮点

- 提出检索-匹配一体化框架，提升跨域定位精度
- 发布大倾斜视角基准，填补现有数据集空白
- 两项工作均开源，促进算法对比与复现

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260722] RIM: A Retrieval-In-Matching Framework for Cross-Domain Global Visual Localization of UAVs | Li Xin, Duan Siyuan, Wang Shang, Mao Zhimin, Hu Bingliang, Zhang Geng | Key Laboratory of Spectral Imaging Technology CAS, Xi’an Institute of Optics and；Precision Mechanics, Chinese Academy of Sciences, Xi’an, 710119, China；University of Chinese Academy of Sciences, Beijing, 100049, China | RIM框架结合检索与匹配，实现无人机跨域全局定位，应对GNSS拒止环境。 | [#1](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/1) |
| [20260722] OffNadirLoc: Benchmark and Framework for Challenging UAV-to-Satellite Geo-Localization under Large Off-Nadir Views | Qiao Qian, Liu Wenye, Liu Ting, Shu Jiuhe, Wang Peng | School of Computer Science, Northwestern Polytechnical University | OffNadirLoc基准聚焦大倾斜视角，提供新数据集与评估框架，提升定位鲁棒性。 | [#2](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/2) |

## 🔎 观察

- 跨视角定位研究正从常规视角向极端视角扩展，挑战更贴近实际飞行场景。
- 开源代码与基准成为标配，推动领域内可复现性和公平对比。

---

Powered by OpenClaw🦞

---

# [20260716](./202607/20260716.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦无人机与智能反射面（RIS）及无线感知技术的融合。两项工作分别探索了无人机搭载RIS的实时飞行控制，以及基于条件生成学习的无线点云成像用于目标感知与跟踪。研究均强调可复现性，并涉及GNSS拒止环境下的定位与目标地理定位，显示出无人机自主导航与感知技术的交叉发展趋势。

## ✨ 今日亮点

- 无人机RIS实时控制提升通信可靠性
- 条件生成学习实现无线点云感知
- 两项研究均注重可复现性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260716] LIVE-RIS: Real-Time In-Flight Actuation of UAV-Mounted RIS | Müller David, Weinberger Kevin, Sezgin Aydin, Mönnigmann Martin | the chair of Automatic Control and Systems Theory, Department of Mechanical Engineering, Ruhr-Universität Bochum,, Bochum, Germany；the chair of Digital Communication Systems, Department of Electrical Engineering, Ruhr-Universität Bochum,, Bochum, Germany | 提出LIVE-RIS系统，实现无人机搭载RIS的实时飞行驱动控制。 | [#21](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/21) |
| [20260716] Conditional Generative Learning Enabled Wireless UAV Sensing and Tracking via Point Cloud Imaging | Dai Xinhong, Gao Yuan, Jiang Hao, Yuan Xiaojun, Wang Xin | Key Laboratory for Information Science of Electromagnetic Waves (MoE), College of Future Information Technology, Fudan University, Shanghai, China. (；the National Key Laboratory of Wireless Communications, the University of Electronic Science and Technology of China, Chengdu, China ( | 利用条件生成学习，通过点云成像实现无线无人机感知与跟踪。 | [#22](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/22) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Trajectory-aware Cross-view Geo-localization with Sequential Observations | [2607.15491v1](https://arxiv.org/abs/2607.15491v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 研究趋势偏向将硬件控制与AI感知结合，提升无人机在复杂环境下的自主性。
- 可复现性成为重要考量，但两项工作均需进一步评审验证。

---

Powered by OpenClaw🦞

---
