# Daily Reports

最近三天日报（最新在前）：

# [20260924](./202609/20260924.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦于GNSS拒止环境下的LiDAR-惯性里程计，FMCW多普勒LiDAR与IMU融合成为提升定位鲁棒性的新方向。该工作针对传统SLAM在无卫星信号场景中的漂移问题，利用调频连续波雷达的测速能力增强状态估计。整体趋势显示，多传感器紧耦合与新型测距体制正推动无人系统导航向更高自主性发展。

## ✨ 今日亮点

- FMCW多普勒LiDAR为GNSS拒止导航提供新观测维度
- LiDAR-惯性紧耦合方案提升位姿估计鲁棒性
- 澳门大学团队探索新型雷达体制在SLAM中的应用

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260924] FMCW-LIO: A Doppler LiDAR-Inertial Odometry | Zhao Mingle, Wang Jiahao, Gao Tianxiao, Xu Chengzhong, Kong Hui | University of Macau | 提出FMCW-LIO，利用多普勒LiDAR与IMU紧耦合，在GNSS拒止下实现鲁棒里程计。 | [#159](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/159) |

## 🔎 观察

- 多普勒测速信息可有效约束LiDAR-惯性里程计中的尺度与漂移误差。
- 新型FMCW雷达体制正从感知向导航定位延伸，值得持续关注。

---

Powered by OpenClaw🦞

---

# [20260923](./202609/20260923.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日论文聚焦GNSS拒止环境下的定位与建图，涵盖无人机大范围几何地图定位、立体视觉SLAM语义运动先验、单目惯性SLAM前馈初始化与位姿条件建图，以及卫星立体匹配合成数据集。研究趋势显示：多源先验融合（语义、运动、几何）成为提升鲁棒性的关键，同时合成数据被用于缓解真实标注稀缺问题。整体上，视觉与惯性、地图与学习的结合正推动拒止环境自主导航向高精度、可扩展方向发展。

## ✨ 今日亮点

- 无人机城市定位利用几何地图与跨视角检索实现GNSS拒止下大范围定位
- SLAM研究引入语义-运动层次先验，提升立体视觉特征匹配鲁棒性
- 单目惯性SLAM通过前馈初始化与位姿条件建图增强稠密重建能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260923] Large-Scale Geometric Map-Based Localization of UAVs in GNSS-Denied Urban Environments | Garth J.S. Terlizzi III, Fathian Kaveh | Department of Computer Science, Colorado School of Mines | 面向GNSS拒止城市环境，提出基于大规模几何地图的无人机定位，结合跨视角检索与精细配准实现目标地理定位。 | [#154](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/154) |
| [20260923] Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM | Chatterjee Preeti, Lu Jin, Sun Jin, Suchendra M. Bhandarkar | School of Computing, University of Georgia | 提出KYS-SLAM，利用层次化语义-运动先验改进立体视觉SLAM中的特征匹配，提升传统SLAM鲁棒性。 | [#155](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/155) |
| [20260923] DAVIO: Dense Monocular–Inertial SLAM with Feed-Forward Initialization and Pose-Conditioned Mapping | Mahmoud Jaafar, Movsesyan Arthur, Iumanov Mikhail, Kolyubin Sergey | Robotics (BE2 R) Lab, ITMO University, Saint Petersburg, Russia | 提出DAVIO，稠密单目惯性SLAM，采用前馈初始化与位姿条件建图，面向GNSS拒止场景。 | [#156](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/156) |
| [20260923] SatUnreal: A High-Precision Synthetic Dataset for Satellite Stereo Matching via Unreal Engine | Kim Han-Gyeol, Park JaeWan, Park Junmin, Kwon Darongsae | To address these issues, research on synthetic data utiliz- | 发布SatUnreal，基于虚幻引擎的高精度合成数据集，用于卫星立体匹配与DSM/DEM/TDOM基准测试。 | [#157](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/157) |

## 🔎 观察

- 多篇工作强调先验知识（语义、运动、几何）与SLAM/定位融合，反映拒止环境下对鲁棒性的迫切需求。
- 合成数据集与真实场景定位并行推进，显示数据稀缺仍是卫星与无人机视觉任务的关键瓶颈。

---

Powered by OpenClaw🦞

---

# [20260922](./202609/20260922.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 5 篇。

今日论文聚焦点云配准、SLAM跟踪与里程计评估。Unsigned Distance Maps被用于2D点云配准，Dual Covariance Gaussian Splatting SLAM通过解耦渲染与配准提升实时跟踪鲁棒性。同时，单目无人机导航引入动作条件潜在世界模型，而两篇工作分别质疑里程计评分规范并报告MOLA-LIO在COMFORT基准上的表现，反映出社区对评估标准与基准测试的重视。

## ✨ 今日亮点

- 无符号距离图被引入2D点云配准，拓展传统SLAM前端思路。
- 双协方差高斯泼溅SLAM解耦渲染与配准，提升实时跟踪鲁棒性。
- 两篇工作关注里程计评分与基准测试，推动评估规范化。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260922] Unsigned Distance Maps on 2D Point Cloud Registration | Ricardo B. Sousa, Grisetti Giorgio, Héber Miguel Sobreira, Carlos André Silva, António Paulo Moreira | Faculty of Engineering, University of Porto (FEUP). R. Dr. Roberto Frias, 4200-465 Porto, Portugal；INESC TEC -- Institute for Systems and Computer Engineering, Technology and Science. R. Dr. Roberto Frias, 4200-465 Porto, Portugal；Sapienza University of Rome. Piazzale Aldo Moro 5 | 提出基于无符号距离图的2D点云配准方法，面向传统SLAM与视觉里程计。 | [#147](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/147) |
| [20260922] Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking | Edward Beng Wai Tan, Lam Siew-Kei | College of Computing and Data Science, Nanyang Technological University, Singapore | 双协方差高斯泼溅SLAM解耦渲染与配准，实现鲁棒实时跟踪。 | [#148](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/148) |
| [20260922] SKYTOPIA: MONOCULAR DRONE NAVIGATION WITH ACTION-CONDITIONED LATENT WORLD MODELS | Zhang Yuhang, Zhang Rangya, Shang Yujing, Yu Zhuoyuan, Wang Weiying, Yang Steven, Yan Qingsong, Yan Chao, Feroskhan Mir | Nanyang Technological University, Singapore；Independent Researcher；Anonymous Institution | 单目无人机导航采用动作条件潜在世界模型，面向GNSS拒止环境。 | [#149](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/149) |
| [20260922] You Should Be Properly Scoring Your Odometry | Rønning Ola, Saqib Usama, Wasowski Andrzej | Software Quality Research Group, IT University of Copenhagen, Denmark | 指出里程计评分应更规范，避免评估偏差影响方法比较。 | [#150](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/150) |
| [20260922] MOLA LiDAR-Inertial Odometry (MOLA-LIO) on the COMFORT Localization Benchmark | Jose Luis Blanco-Claraco | Engineering Department；University of Almerı́a, Spain；Affiliation type Academia (University of Almerı́a) | 在COMFORT基准上评估MOLA-LIO，报告激光惯性里程计定位表现。 | [#151](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/151) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| TM-APR: Thermal Temporal-Memory Localization via Analytic Online Adaptation | [2609.26766v1](https://arxiv.org/abs/2609.26766v1) | 质检未通过: 单位为空或无效 |
| ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards | [2609.26315v1](https://arxiv.org/abs/2609.26315v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 点云配准与SLAM跟踪仍是核心，高斯泼溅与距离图代表不同技术路线。
- 评估规范与基准测试受关注，反映领域对可复现比较的迫切需求。

---

Powered by OpenClaw🦞

---
