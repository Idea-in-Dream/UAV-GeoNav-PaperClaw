# Daily Reports

最近三天日报（最新在前）：

# [20261126](./202611/20261126.md)
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
