# Daily Reports

最近三天日报（最新在前）：

# [20261117](./202611/20261117.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日论文聚焦多模态SLAM与里程计的鲁棒性与资源效率。多智能体全景高斯泼溅SLAM通过球面回环提升大场景建图一致性；气压传感器阵列被用于重力向量估计，拓展了非视觉导航手段；退化隧道场景下的LiDAR-惯性-视觉融合里程计强调退化引导策略；资源感知的LiDAR-惯性里程计则关注计算受限平台。整体趋势显示，研究正从单一传感器向多源融合与场景自适应演进，同时兼顾嵌入式部署可行性。

## ✨ 今日亮点

- 多智能体全景高斯泼溅SLAM引入球面回环，提升跨会话建图精度。
- 分布式气压传感器阵列实现重力向量估计，为无视觉导航提供新思路。
- 退化引导的LiDAR-惯性-视觉融合里程计针对隧道场景增强鲁棒性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261117] CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure | Shao Qi, Cao Zhihao, Zhai Shuhao, Wu Taoyu, Li Zhuoxiao, Nguyen Anh, Hu Long, Li Xianzhi, Liang Hong, Huang Baoru, Li Liang | Harbin Engineering University, Harbin, China；University of Liverpool, Liverpool, cross-session multi-agent panoramic benchmarks demonstrate UK；the National racy and rendering quality among single-agent and multi-agent University of Singapore, Singapore；University of Macau, Macau, China；University of Liverpool, Liverpool, UK；Xi’an Jiaotong-Liverpool University, Suzhou, China；The Hong Kong University of Science and Technology I；University of Liverpool, Liverpool, Dense 3 D mapping of large indoor environments is essential UK；Imperial College London, London, UK；Huazhong University of Science and Technology, Wuhan, China | 提出多智能体全景高斯泼溅SLAM，利用球面回环实现跨会话大场景稠密建图与高质量渲染。 | [#268](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/268) |
| [20261117] Pressure Drop: Gravity Vector Estimation from a Distributed Barometric Pressure Sensor Array | Dubois William, Lauzon Nicolas, Laconte Johann, Pomerleau François | essential [1]. Although Simultaneous Localization and Mapping (SLAM) approaches can achieve strong performance [2], Previous research has shown that barometric pressure；Northern Robotics Laboratory, Université Laval, Québec；Université Clermont Auvergne, INRAE, UR TSCF, 63000, Clermont- ‚ An observability and configuration analysis of an array | 基于分布式气压传感器阵列估计重力向量，分析可观测性与配置，为SLAM提供辅助重力约束。 | [#269](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/269) |
| [20261117] DGV-DLIVO: Degeneracy-Guided Visual Fusion for Direct LiDAR-Inertial-Visual Odometry in Degenerate Tunnel Environments | Zhang Junrui | Department of Electronic and Information Engineering, Tongji University, Shanghai, 200092, China | 针对退化隧道环境，提出退化引导的LiDAR-惯性-视觉直接里程计，融合视觉信息增强定位鲁棒性。 | [#270](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/270) |
| [20261117] Pelorus: Resource-Aware Lidar-Inertial Odometry | Sieh Charlotte, Porrmann Mario | the Computer Engineering Group, Osnabrück University, Osnabrück, Germany ( | 提出资源感知的LiDAR-惯性里程计，面向计算受限平台优化资源分配与实时性能。 | [#271](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/271) |

## 🔎 观察

- 多智能体与跨会话SLAM成为大场景建图热点，球面回环设计有望解决全景相机视角冗余问题。
- 非视觉传感器（如气压阵列）与退化引导融合策略表明，研究正重视极端环境下的可观测性分析。

---

Powered by OpenClaw🦞

---

# [20261116](./202611/20261116.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 17 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日论文聚焦传统SLAM与视觉惯性里程计的系统优化与基准评测。Polygraph提出基于位姿图的大规模多会话轨迹优化方法，强调跨会话闭环与全局一致性；OrthoMark利用点锚定正交高度标记进行地点识别，探索3D地图配准新表征；sqrtVINS则针对Hilti-Trimble 2026挑战赛构建360视觉惯性SLAM系统，体现赛事驱动下的工程集成与数据集评测趋势。整体看，研究在传统SLAM框架内寻求多会话扩展、轻量表征与鲁棒系统设计。

## ✨ 今日亮点

- Polygraph以位姿图实现大规模多会话轨迹优化，提升全局一致性。
- OrthoMark提出点锚定正交高度标记，用于地点识别与3D配准。
- sqrtVINS面向Hilti-Trimble 2026挑战赛，集成360视觉惯性SLAM系统。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261116] Polygraph: Large-Scale Multi-Session Trajectory Optimization using Pose Graphs | Lukovic Petar, Tian Yi Lim, Pollefeys Marc, Speciale Pablo, Blum Hermann, Bauer Zuria | against it, as in ORB-SLAM3 Atlas [1], Maplab [2], [3], When a cluster closes, it is matched with every other session；Microsoft Spatial AI Lab, Zurich, Switzerland | 提出Polygraph，基于位姿图进行大规模多会话轨迹优化，通过跨会话匹配提升全局一致性。 | [#264](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/264) |
| [20261116] OrthoMark: Place Recognition with Point-Anchored Orthographic Height Mark | Li Haichuan | University of Turku | 提出OrthoMark，利用点锚定正交高度标记进行地点识别，服务于3D地图配准。 | [#265](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/265) |
| [20261116] sqrtVINS-Based 360 Visual-Inertial SLAM Systems: Hilti-Trimble SLAM Challenge 2026 Entry | Lee Jungwoo, Kim Hogyun, Choi Jiwon, Jeong Jinyong, Cho Younggun | Dept. of Electrical and Computer Engineering, Inha University, Incheon, South Korea | 基于sqrtVINS构建360视觉惯性SLAM系统，作为Hilti-Trimble 2026挑战赛参赛方案。 | [#266](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/266) |

## 🔎 观察

- 多会话SLAM正从单次建图转向全局位姿图优化，跨会话闭环与一致性维护成为关键。
- 赛事基准推动视觉惯性SLAM系统集成与鲁棒性验证，360感知与工程化评测受关注。

---

Powered by OpenClaw🦞

---

# [20261113](./202611/20261113.md)
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
