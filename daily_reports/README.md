# Daily Reports

最近三天日报（最新在前）：

# [20260821](./202608/20260821.md)
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

# [20260820](./202608/20260820.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于视觉定位与特征学习。RIPE++提出仅利用正样本对强化关键点学习，简化训练流程。另一项工作引入重力感知，实现基于仿射或旋转协变特征的绝对位姿估计，提升GNSS拒止环境下的定位鲁棒性。此外，地理隔离的自监督学习策略为大规模遥感数据训练提供新思路。整体趋势显示，结合几何先验与自监督方法正成为提升定位精度和泛化能力的关键。

## ✨ 今日亮点

- 关键点学习仅需正样本对，简化训练
- 重力先验提升部分标定位姿估计精度
- 地理隔离自监督学习增强特征泛化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260820] RIPE++: Reinforced Keypoint Learning from Positive Pairs Only | Künzel Johannes, Eisert Peter, Hilsmann Anna | Fraunhofer Heinrich-Hertz-Institute, HHI, Germany；Humboldt University Berlin, Germany | RIPE++仅用正样本对强化关键点学习，简化训练并提升匹配性能 | [#93](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/93) |
| [20260820] Gravity-aware partially calibrated absolute pose estimation from affine- or rotation-covariant features | Marcus Valtonen Örnhag, Jaenal Alberto, Adalbjörnsson Stefan | Ericsson Research, Lund, Sweden；University of Zaragoza, Spain | 重力感知方法利用仿射或旋转协变特征，实现部分标定绝对位姿估计 | [#94](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/94) |
| [20260820] Far from the Crowd: Scalable Self-Supervised Learning via Geographic Isolation | Daniele Rege Cambrin, Rossi Francesco, Varile Mattia | AIKO | 地理隔离自监督学习策略，提升大规模遥感数据特征学习的可扩展性 | [#95](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/95) |

## 🔎 观察

- 几何先验（如重力）与特征学习结合，成为GNSS拒止定位的重要趋势
- 自监督方法通过数据隔离策略，在减少标注依赖的同时增强模型泛化能力

---

Powered by OpenClaw🦞

---

# [20260819](./202608/20260819.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦无人机视觉定位与场景理解，涵盖终身场景记忆、主动地理定位、SLAM系统评估及视觉接地等方向。多篇论文提出新方法或基准，强调在GNSS拒止环境下的鲁棒性，并注重可复现性。趋势显示从传统SLAM向跨视角检索与多模态融合演进。

## ✨ 今日亮点

- 终身场景理解与动态记忆机制受关注
- 主动地理定位引入好奇心奖励塑造
- 无人机SLAM与视觉里程计评估成热点

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260819] LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding | Lee Yumin, Ju Hyoseok, Kim Giseop | Lee, H. Ju and G. Kim are with the Department of Robotics；by Basic Science Research Program through the National Research Foun- demanding and does not scale with prolonged deployment；), and by the Institute of Information & Communications posed, and session-indexed temporal queries are not directly | 提出波动感知时空记忆，用于终身场景理解，应对长期部署挑战。 | [#87](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/87) |
| [20260819] DynCur-Geo: Dynamic Curiosity Reward Shaping for Multimodal Active Geo-Localization | Sun Yiming, Zhang Yang, Zhu Pengfei | School of Automation, Southeast University, Nanjing 210096, China | 动态好奇心奖励塑造，提升多模态主动地理定位的探索效率。 | [#88](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/88) |
| [20260819] Evaluation of Monocular SLAM Systems on High-Altitude Nadir UAV Footage | Spagnolo Gašper, Dobrevski Matej, Skočaj Danijel | Faculty of Computer and Information Science, University of Ljubljana, Večna pot 113, Ljubljana, Slovenia | 系统评估单目SLAM在高空正射无人机视频中的性能表现。 | [#89](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/89) |
| [20260819] Evaluation of Image Matching Methods for Visual Odometry on UAVs | Spagnolo Gašper, Luka Čehovin Zajc, Dobrevski Matej | Faculty of Computer and Information Science, University of Ljubljana | 对比多种图像匹配方法在无人机视觉里程计中的适用性。 | [#90](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/90) |
| [20260819] GrabVG: Graph-Attentive Binding for Visual Grounding in UAV Imagery | Wang Chaowei, Di Yan, Sun Jingjun, Liu Baozhe, Tian Jiaxu, Li Yuheng, Guo Guangqian, Gao Shan | Northwestern Polytechnical University；Harbin Institute of Technology；The Hong Kong Polytechnic University | 提出图注意力绑定方法，用于无人机影像中的视觉接地任务。 | [#91](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/91) |

## 🔎 观察

- 研究重心从传统几何方法转向学习型跨视图检索与主动感知结合。
- 基准测试与可复现性成为无人机定位研究的重要关注点。

---

Powered by OpenClaw🦞

---
