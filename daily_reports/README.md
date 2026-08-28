# Daily Reports

最近三天日报（最新在前）：

# [20260827](./202608/20260827.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于多智能体协同重建与跨视角地理定位两大方向。CGS-SLAM通过协作高斯溅射实现多智能体同步定位与建图，提升复杂环境下的重建效率；UniGeo则利用多模态大语言模型，结合文本引导实现跨视角地理定位，增强检索精度。两者均涉及无人机与卫星数据融合，并配套开源数据集，推动三维视觉与地理空间智能的交叉发展。

## ✨ 今日亮点

- 多智能体协同高斯溅射SLAM实现高效联合重建
- 多模态大模型赋能文本引导跨视角地理定位
- 无人机与卫星数据融合趋势显著，开源数据集助力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260827] CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction | Jean-Daniel de Ambrogi, Chetouani Aladine, Nguyen Vincent, Chateigner Aurélien | Université Sorbonne Paris Nord, L2 TI, UR 3043, F-93430, Villetaneuse, France；Université d’Orléans, INSA CVL, LIFO, UR 4022, Orléans, France | CGS-SLAM提出协作高斯溅射SLAM，支持多智能体联合重建，提升GNSS拒止环境下的地图构建效率。 | [#109](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/109) |
| [20260827] UniGeo: A Multi-modal Large Language Model for Text-Guided Cross-View Geo-Localization | Wen Jiahao, Yu Hang, Zheng Zhedong | School of Computer Engineering and Science, Shanghai University, Shanghai, China (；the Faculty of Science and Technology, and Institute of Collaborative Innovation, University of Macau, Macau, China ( | UniGeo构建多模态大语言模型，利用文本引导跨视角地理定位，增强无人机与卫星图像匹配能力。 | [#110](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/110) |

## 🔎 观察

- 多智能体协作与多模态融合成为提升定位鲁棒性的关键路径
- 开源基准与数据集发布加速了遥感AI算法的可复现性研究

---

Powered by OpenClaw🦞

---

# [20260826](./202608/20260826.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域聚焦跨视角定位技术，一项大规模数据集研究成为亮点。该工作构建了开放、多样且规模庞大的基准，旨在推动细粒度跨视角检索与配准的进展。研究强调数据集的复现性与实用性，为无人机导航、城市感知等应用提供了关键支撑，反映出当前领域对高质量训练数据与标准化评估的迫切需求。

## ✨ 今日亮点

- 发布大规模跨视角定位数据集，强调开放与多样性。
- 聚焦细粒度检索与配准，推动定位精度提升。
- 提供可复现基准，促进算法公平对比与验证。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260826] OpenCVL: An Open, Diverse, and Large-Scale Dataset for Fine-Grained Cross-View Localization | Xia Zimin, Zaffar Mubariz, Fu Junsheng, Alahi Alexandre, Julian F. P. Kooij | Southern University of Science and Technology (SUSTech), China；Delft University of Technology, The Netherlands | 提出OpenCVL数据集，覆盖多场景跨视角图像，支持细粒度定位研究。 | [#107](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/107) |

## 🔎 观察

- 数据集构建成为跨视角定位研究的关键瓶颈，开放基准受重视。
- 细粒度配准需求上升，预示算法从粗检索向精定位演进。

---

Powered by OpenClaw🦞

---

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
