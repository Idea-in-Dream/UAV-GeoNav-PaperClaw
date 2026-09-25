# Daily Reports

最近三天日报（最新在前）：

# [20260923](./202609/20260923.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日论文聚焦GNSS拒止环境下的定位与建图，涵盖无人机大范围几何地图定位、语义运动先验增强的立体视觉SLAM、稠密单目惯性SLAM的前馈初始化与位姿条件建图，以及基于虚幻引擎的卫星立体匹配合成数据集。整体趋势显示，研究者正通过多源先验融合与合成数据生成，提升复杂城市环境中定位与三维重建的鲁棒性和精度。

## ✨ 今日亮点

- 无人机几何地图定位应对GNSS拒止城市环境
- 语义运动先验提升立体视觉SLAM特征匹配
- 虚幻引擎合成卫星立体匹配高精度数据集

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260923] Large-Scale Geometric Map-Based Localization of UAVs in GNSS-Denied Urban Environments | Garth J.S. Terlizzi III, Fathian Kaveh | Department of Computer Science, Colorado School of Mines | 面向GNSS拒止城市环境，提出基于大规模几何地图的无人机跨视角检索与精细配准定位方法。 | [#154](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/154) |
| [20260923] Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM | Chatterjee Preeti, Lu Jin, Sun Jin, Suchendra M. Bhandarkar | School of Computing, University of Georgia | 利用层次化语义与运动先验改进立体视觉SLAM特征匹配，提升传统SLAM鲁棒性。 | [#155](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/155) |
| [20260923] DAVIO: Dense Monocular–Inertial SLAM with Feed-Forward Initialization and Pose-Conditioned Mapping | Mahmoud Jaafar, Movsesyan Arthur, Iumanov Mikhail, Kolyubin Sergey | Robotics (BE2 R) Lab, ITMO University, Saint Petersburg, Russia | 提出稠密单目惯性SLAM，采用前馈初始化与位姿条件建图，应对GNSS拒止场景。 | [#156](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/156) |
| [20260923] SatUnreal: A High-Precision Synthetic Dataset for Satellite Stereo Matching via Unreal Engine | Kim Han-Gyeol, Park JaeWan, Park Junmin, Kwon Darongsae | To address these issues, research on synthetic data utiliz- | 基于虚幻引擎构建高精度合成数据集，用于卫星立体匹配与DSM/DEM/TDOM基准测试。 | [#157](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/157) |

## 🔎 观察

- GNSS拒止定位与SLAM研究正从单一传感器向多源先验融合演进，语义与运动信息成为提升鲁棒性的关键。
- 合成数据集开始覆盖卫星立体匹配任务，有望缓解真实标注稀缺问题，但域差距仍需验证。

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

# [20260921](./202609/20260921.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文聚焦于神经渲染与SLAM的深度融合，以及面向遥感与无人机场景的几何感知方法。贝叶斯概率框架被引入3DGS-SLAM以量化不确定性，卫星高斯泼溅结合智能体实现可审计的城市DSM重建。同时，稀疏优化、可调空间尺度的隐式神经表示以及模拟视频传输下的多视图几何等研究，共同推动遥感AI在鲁棒性、可解释性和跨域适应方面的发展。

## ✨ 今日亮点

- 贝叶斯概率建模提升3DGS-SLAM不确定性量化能力
- 智能体卫星高斯泼溅实现可审计城市DSM重建
- 模拟视频传输下FPV无人机多视图几何新基准

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260921] BayesianGS-SLAM: Uncertainty-Aware Neural Rendering SLAM via Probabilistic Formulation | Kang Kyeongsu, Ha Seongbo, Lee Sibaek, Yu Hyeonwoo | Department of Intelligent Robotics, Sungkyunkwan University, Suwon, South Korea | 提出贝叶斯GS-SLAM，通过概率公式实现不确定性感知的神经渲染SLAM。 | [#141](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/141) |
| [20260921] Agentic Building-Aware Satellite Gaussian Splatting for Auditable Urban DSM Reconstruction | Sun Wentao, Xu Zhengsen, Chen Yiping, John S. Zelek, Li Jonathan | University of Waterloo, Department of Systems Design Engineering, Waterloo, Canada；University of Calgary, Department of Geomatics Engineering, Calgary, Canada；Sun Yat-sen University, School of Geospatial Engineering and Science, Zhuhai, China | 利用智能体建筑感知卫星高斯泼溅，实现可审计的城市DSM重建。 | [#142](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/142) |
| [20260921] SPARSER: Sparse Variable Projection by Exploiting Separable Structure in Robotic Perception | Nikolas R. Sanderson, Fishberg Andrew, Han Haoyu, Yang Heng, Jonathan P. How, Singh Hanumant, Everett Michael, Papalia Alan | Department of Naval Architecture and Marine Engineering, Unitypically require solving problems to high numerical；Institute of Experiential；accuracy (Triggs et al. 2000); and (iii) problems often Robotics, Northeastern University, Boston, MA, USA；problem sparsity to handle scale (Dellaert et al. 2017), Alan Papalia, Assistant Professor, Department of Naval Architecture and；adopt second-order methods (e.g., Levenberg–Marquardt) Marine Engineering at the University of Michigan | 提出SPARSER，利用可分离结构进行稀疏变量投影以加速机器人感知。 | [#143](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/143) |
| [20260921] MIND THE GAP: A GEOGRAPHIC IMPLICIT NEURAL REPRESENTATION WITH ADJUSTABLE SPATIAL SCALE | Corley Isaac, Rao Arjun, Rolf Esther, Klemmer Konstantin, Shelhamer Evan, Lehmann Nils, Rußwurm Marc, Mai Gengchen, Jacobs Nathan, Kerner Hannah | University of British Columbia；University of Colorado Boulder；University College London；Vector Institute；Technical University of Munich；University of Bonn；University of Texas at Austin；Washington University in Saint Louis；Arizona State University；research.taylorgeospatial.org/mind | 提出地理隐式神经表示，支持可调空间尺度的遥感场景建模。 | [#144](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/144) |
| [20260921] AnalogDepth: Multi-view Geometry from FPV drones under Analog Video Transmission | Amorim André, Pedro F. Proença | NOVA School of Science of Technology；NOVA School of Science and Technology, NOVA University Lisbon, Caparica, Portugal | 构建模拟视频传输下FPV无人机多视图几何数据集与基准。 | [#145](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/145) |

## 🔎 观察

- 神经渲染与SLAM结合正从静态重建走向概率化与不确定性量化。
- 遥感与无人机场景推动几何优化和隐式表示向可调尺度与鲁棒性发展。

---

Powered by OpenClaw🦞

---
