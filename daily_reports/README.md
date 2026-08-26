# Daily Reports

最近三天日报（最新在前）：

# [20260825](./202608/20260825.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域聚焦于视觉惯性里程计（VIO）的鲁棒性与精度提升。研究提出KLTNet，通过稀疏特征跟踪网络改进单目VIO性能，结合传统几何与深度学习，旨在应对复杂环境下的跟踪丢失问题。该工作体现了将学习型特征与经典SLAM框架融合的趋势，以增强系统在挑战性场景中的适应能力。

## ✨ 今日亮点

- 提出KLTNet稀疏特征跟踪网络，提升VIO鲁棒性。
- 融合深度学习与经典SLAM，增强复杂环境适应性。
- 开源代码，促进视觉惯性里程计研究复现。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260825] KLTNet: Learning Sparse Feature Tracking for Robust and Accurate Monocular Visual-Inertial Odometry | Jin Renbiao, Zou Danping, Yu Wenxian | Shanghai Jiao Tong University, Shanghai, China. ( | KLTNet通过稀疏特征跟踪学习，显著提升单目视觉惯性里程计的鲁棒性和精度。 | [#105](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/105) |

## 🔎 观察

- 学习型特征跟踪正成为VIO领域提升鲁棒性的重要方向。
- 传统几何与深度学习结合仍是当前遥感定位技术的主流范式。

---

Powered by OpenClaw🦞

---

# [20260824](./202608/20260824.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 4 篇。

今日研究聚焦于复杂环境下的自主导航与三维重建。强化学习用于宏动作拓扑导航，以应对噪声定位；Isaac Sim平台支持高保真自动驾驶仿真；SuperMap系统结合时空SLAM与视觉语言导航；SiZeUp通过深度序数损失实现航拍图像快速三维代理生成。整体趋势显示，多传感器融合与跨模态学习成为提升系统鲁棒性的关键。

## ✨ 今日亮点

- 强化学习提升噪声定位下的导航鲁棒性
- 高保真仿真平台加速自动驾驶算法验证
- 视觉语言导航与SLAM融合成新热点

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260824] Macro-Action Topological Navigation under Noisy Localization using Reinforcement Learning | Hakenes Simon, Glasmachers Tobias | Institute of Neural Computation, Ruhr University Bochum, Germany | 利用强化学习在噪声定位下实现宏动作拓扑导航，提升鲁棒性 | [#100](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/100) |
| [20260824] RoboRacer Arena: Scaling High-Fidelity Autonomous Racing in Isaac Sim | Clement Mihaela-Larisa, Poks Agnes, Bartocci Ezio | research using 1:10-scale autonomous vehicles, but the variety；AIT Austrian Institute of Technology, Vienna, Austria | RoboRacer Arena在Isaac Sim中构建高保真自动驾驶赛车仿真环境 | [#101](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/101) |
| [20260824] SuperMap: A Spatio-Temporal SLAM System for Visual-Language Navigation | Zhao Shibo, Chen Guofei, Zhu Honghao, Li Zhiheng, Yao Changwei, Zantout Nader, Kim Seungchan, Wang Wenshan, Zhang Ji, Scherer Sebastian | The Robotics Institute, Carnegie Mellon University | SuperMap提出时空SLAM系统，融合视觉语言实现导航 | [#102](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/102) |
| [20260824] SiZeUp: Fast 3D Proxy from Aerial Images via Depth Ordinal Loss | Zhou Wenjun, Li Yunshan, Zhu Qiaoyu, Xiong Weidan, Zhang Hao, Cohen-Or Daniel, Huang Hui | WENJUN ZHOU, Shenzhen University, China；YUNSHAN LI, Shenzhen University, China；QIAOYU ZHU, Shenzhen University, China；WEIDAN XIONG, Shenzhen University, China；HAO ZHANG, Simon Fraser University, Canada；DANIEL COHEN-OR, Shenzhen University, China；HUI HUANG∗, Shenzhen University, China；Authors’ Contact Information: Wenjun Zhou, CSSE, Shenzhen University, China, Cohen-Or, and Hui Huang. 2026. SiZeUp: Fast 3 D Proxy from Aerial Images；dan Xiong, Shenzhen University, China；Fraser University, Canada；Visual Media and Multidimensional Intelligence, CSSE, Shenzhen University, China | SiZeUp采用深度序数损失，从航拍图像快速生成三维代理 | [#103](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/103) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Spotter: Efficient Urban Visual Localization via Geo-Referenced Facade Landmarks in GPS-Degraded Environments | [2608.23290v1](https://arxiv.org/abs/2608.23290v1) | 质检未通过: 单位为空或无效; 图片数量不足（至少1张） |


## 🔎 观察

- 多篇论文强调仿真环境与真实场景的差距，推动高保真模拟器发展
- 视觉语言模型与SLAM结合，预示多模态导航成为未来方向

---

Powered by OpenClaw🦞

---

# [20260823](./202608/20260823.md)
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
