# Daily Reports

最近三天日报（最新在前）：

# [20261125](./202611/20261125.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦于无GNSS环境下的空间感知与度量恢复。三项工作分别从协同高斯SLAM、视觉惯性锚定的度量升级以及双流视觉世界模型切入，体现了多传感器融合与几何一致性约束的深化趋势。同时，面向无人机动作条件建模的数据集与基准构建受到关注，表明该领域正从单一定位向可预测、可交互的场景理解延伸。

## ✨ 今日亮点

- 协同高斯SLAM引入传感器锚定与全局一致性约束，提升无GNSS重建鲁棒性。
- 视觉惯性锚定突破Sim(3)限制，实现前馈几何的度量尺度恢复。
- 双6-DoF视觉流融入动作条件世界模型，增强无人机场景动态预测能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261125] CADENCE: Sensor-GroundedWorld-Consistent Gaussian SLAM for Collaborative Mobile Reconstruction | Reshad Ul Karim, Samin Abrar, Md Rashad Al Hasan Rony | BRAC University, Dhaka, Bangladesh；AI Competence Center, Deutsche Telekom AG | 提出CADENCE，利用传感器锚定与全局一致性高斯SLAM实现协同移动重建，面向无GNSS场景。 | [#297](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/297) |
| [20261125] ProManO: Beyond Sim(3) for Metric Upgrade of Feed-Forward Geometry with Visual-Inertial Anchors | Hu Lingxiang, Zhao Zhenjun, Shao Qi, Naima Ait Oufroukh, Bonardi Fabien, Ghandour Raymond, Yuan Shenghai, Civera Javier, Huang Baoru | Université Paris-Saclay, Univ Évry, IBISC, France；University of Liverpool, UK；American University of the Middle East, Kuwait；Nanyang Technological University, Singapore | 提出ProManO，借助视觉惯性锚点将前馈几何从Sim(3)升级至度量尺度，提升定位精度。 | [#298](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/298) |
| [20261125] DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model | Li Zixuan, Huang Kangyao, Xu Meng, Tian Wan, Tang Xiaoyu, Sun Jinge, Yao Yingliang, Chen He, Meng Lingzhong, Xue Yunzhi, Chen Jingyu | University of International Business and Economics (uibe.edu.cn)；Tsinghua University (tsinghua.edu.cn)；Peking University (pku.edu.cn)；University of the Chinese Academy of Sciences (ucas.ac.cn)；QiYuanLab (qiyuanlab.com)；Beihang University (buaa.edu.cn)；Institute of Software, Chinese Academy of Sciences (iscas.ac.cn)；Institute of AI for Industries (iaii.ac.cn) | 提出DuoWM，将双6-DoF视觉流集成到动作条件无人机世界模型，并构建相关数据集基准。 | [#299](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/299) |

## 🔎 观察

- 无GNSS定位正从单一SLAM向多源锚定与度量恢复演进，几何一致性成为核心约束。
- 无人机世界模型开始强调动作条件与视觉流耦合，数据集与基准建设同步推进。

---

Powered by OpenClaw🦞

---

# [20261124](./202611/20261124.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文聚焦三维重建与定位导航的交叉领域。SLAM方向出现两项基于3DGS的改进工作，分别面向全向LiDAR-深度融合与在线建图的视角管理。基准评测方面，SpatialArena系统评估几何基础模型的空间能力，填补评测空白。无人机视觉里程计针对低空GNSS拒止场景提出鲁棒旋转估计方案。此外，毫米波雷达世界模型探索异构大语言模型在感知中的解耦应用，显示多模态融合趋势。

## ✨ 今日亮点

- GOLD-SLAM融合高斯泼溅与全向LiDAR-深度，拓展SLAM重建范式。
- SpatialArena建立几何基础模型空间能力评测基准，推动可复现比较。
- ROVO面向低空中高度无人机，实现GNSS拒止下鲁棒旋转视觉里程计。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261124] GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM | Zhang Weicong, Huang Yuan, Zheng Yu, Chenxiao Lin, Li Yingying, Fan Lilong, Zhuang Liangdong, Chen Yufan, Liu Ruiping, Zheng Junwei, Zhang Jiaming | Hunan University；Tsinghua University；Karlsruhe Institute of Technology；University of Oxford；InSAI Lab | 提出GOLD-SLAM，将高斯泼溅与全向LiDAR-深度结合，实现稠密建图与定位一体化。 | [#291](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/291) |
| [20261124] View Management with Gaussian Placement and Opacity Regularization for Online 3DGS | Dong Hwi Kim, Sangwon Park, Song Chaehyeon, Kim Ayoung | Seoul National University | 针对在线3DGS，设计高斯放置与不透明度正则化的视角管理策略，提升建图质量。 | [#292](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/292) |
| [20261124] SpatialArena: Where Do Geometric Foundation Models Stand? | Chen Yu, Yang Haosen, Su Ee Tan, Zhang Zhensong, Song Jifei, Deng Jiankang | MVP Lab \& Imperial College London | 构建SpatialArena基准，系统评测几何基础模型的空间理解与推理能力。 | [#293](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/293) |
| [20261124] ROVO: Robust Rotation-Only Visual Odometry for UAVs at Low and Moderate Altitudes | Song Xiaokai, Zhang Li, Teng Xichao, Pan Erting, Ye Yibin, Wang Kun, Liu Leqi, Dai Guangcheng | College of Aerospace Science and Engineering, National University of Defense Technology, Changsha 410000, China；Hunan Provincial Key Laboratory of Image Measurement and Vision Navigation；National University of Defense Technology, Changsha 410000, China；Hunan Institute of Advanced Technology, Changsha 410000, China | 提出ROVO，面向低空中高度无人机，在GNSS拒止下实现鲁棒纯旋转视觉里程计。 | [#294](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/294) |
| [20261124] PhysRF-WorldJEPA: Transforming Heterogeneous Large Language Models into Manifold-Decoupled Millimeter-Wave Radar World Models | Huang Yicheng, Ke Feng, Chen Linhan, Jiang Ziyi, Xiu Yin Zhang | School of Electronic and Information Engineering, South China University of Technology, Guangzhou, China | 将异构大语言模型转化为流形解耦的毫米波雷达世界模型，用于目标地理定位。 | [#295](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/295) |

## 🔎 观察

- 3DGS与SLAM结合持续升温，今日两项工作分别从传感器融合与在线视角管理切入优化。
- 几何基础模型评测开始体系化，SpatialArena的出现反映社区对可复现基准的迫切需求。

---

Powered by OpenClaw🦞

---

# [20261123](./202611/20261123.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦无人机在GNSS拒止环境下的定位与建图鲁棒性。跨视角地理定位方面，RigidAnchor通过迭代平面刚性对齐实现UAV与卫星影像的精细配准；定位评估方面，有工作提出参考位姿的地点重访一致性评测方法。同时，SLAM地图维护引入证据授权修订机制，决策语言模型的空间意识与地理偏差受到关注，热红外引导的低光图像增强也提供了统一基准。整体趋势显示，多源传感器融合与可复现基准建设并重，定位可靠性评估正从单一精度向一致性、可解释性延伸。

## ✨ 今日亮点

- RigidAnchor以迭代平面刚性对齐实现UAV-卫星跨视角精细配准，代码开源。
- 地点重访一致性评估为参考位姿质量提供可复现的基准测试思路。
- OmniSLAM提出证据授权修订持久对象地图，增强SLAM地图长期维护能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261123] RigidAnchor: Cross-View Geo-Localization for UAV via Iterative Planar Rigid Alignment | Wang Bo, Zhu Dekang, Li Jian, Meng Zhipeng, Wang Bo, Hu Dewen | National Innovation Institute of Defense Technology；College of Intelligence Science and Technology, National University of Defense Technology；School of Future Technology, National University of Defense Technology | 提出RigidAnchor，通过迭代平面刚性对齐实现GNSS拒止下UAV与卫星影像的跨视角精细配准，并开源代码。 | [#285](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/285) |
| [20261123] Place-Revisit Consistency Evaluation of Reference Poses | Huai Jianzhu, Zhang Yujia, Jozkow Grzegorz | State key Lab of Info Engineering in Surveying, Mapping and Remote Sensing (LIESMARS)；School of Instrument Science and Engineering, State Key Laboratory of Comprehensive PNT；Network and Equipment Technology, Southeast University, Nanjing, Jiangsu, China；UK-China Intelligent Mobility Research Centre, Southeast University, Nanjing, Jiangsu, China；Institute of Geodesy and Geoinformatics, Wroclaw University of Environmental and Life | 构建地点重访一致性评估方法，用于检验参考位姿的可靠性，强调可复现的基准测试流程。 | [#286](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/286) |
| [20261123] OmniSLAM: Evidence-Authorized Revision of Persistent Object Maps | Jie Haoxiang, Yan Yaoyuan, Heng Zhiyou, Li Liang, Li Zhaosong, Liu Lifeng | AI Lab, Country Garden Services；School of Mechanical Science and Engineering, Huazhong University of Science and Technology | 提出OmniSLAM，以证据授权方式修订持久对象地图，提升传统SLAM地图的长期一致性与可维护性。 | [#287](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/287) |
| [20261123] Seeing Is Locating: Spatial Awareness and Geographic Bias in Decision Language Models | Wongso Wilson, Hada Melino Muhammad, Lin Xiachong, Xue Hao, Flora D. Salim | University of New South Wales, Sydney, NSW, Australia；Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China；com/cruiseresearchgroup/GeoDecisions | 分析决策语言模型的空间意识与地理偏差，揭示其在定位相关决策中的系统性倾向。 | [#288](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/288) |
| [20261123] Thermal-Guided Low-Light UAV Image Enhancement: A Reliability-Aware Guidance Network and a Unified Benchmark | Zhao Zhicheng, Wang Yu, Xu Jiangong, Xu Lixiang, Li Chenglong, Tang Jin | School of Artificial Intelligence, Anhui University；Anhui Provincial Key Laboratory of Security Artificial Intelligence, Anhui University；Anhui Provincial Key Laboratory of Multimodal Cognitive Computation, Anhui University；School of Computer Science and Technology, Anhui University；School of Artificial Intelligence Engineering, Hefei Institute of Technology；State Key Laboratory of Opto-Electronic Information Acquisition and Protection Technology, Anhui University | 提出可靠性感知的热引导低光UAV图像增强网络，并构建统一基准以评估增强对下游任务的影响。 | [#289](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/289) |

## 🔎 观察

- 跨视角定位研究正从粗检索走向精细配准，刚性对齐与迭代优化成为提升UAV定位精度的可行路径。
- 多篇工作强调基准与可复现性，表明该领域对评估协议规范化和地图长期一致性的关注正在上升。

---

Powered by OpenClaw🦞

---
