# Daily Reports

最近三天日报（最新在前）：

# [20260930](./202609/20260930.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日四篇论文聚焦于复杂环境下的定位与导航鲁棒性提升。研究趋势显示，多传感器融合与先验信息结合成为主流，如多相机视觉惯性SLAM引入楼层平面先验，以及几何语义约束的BEV学习缓解卫星地面定位歧义。同时，针对视觉不可靠场景，学习偏差动态与不确定性被用于提升VIO精度。此外，导航世界动作模型探索快速高效决策，反映出对实时性与泛化能力的双重关注。整体上，研究强调在GNSS拒止或视觉退化条件下，通过多模态约束与学习策略增强系统可靠性。

## ✨ 今日亮点

- 多相机视觉惯性SLAM融合楼层平面先验，提升室内定位鲁棒性。
- 几何语义约束的BEV学习有效缓解卫星地面定位歧义。
- 学习偏差动态与不确定性，增强视觉不可靠下的VIO性能。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260930] MVP-SLAM: Multi-Camera Visual-Inertial Floorplan-Prior SLAM | Bikandi-Noya Asier, Fernandez-Cortizas Miguel, Shaheer Muhammad, Voos Holger, Jose Luis Sanchez-Lopez | with the Automation and Robotics Research Group；Interdisciplinary Centre for Security, Reliability, and Trust (SnT), unexplored. A particular challenge for these systems is to find；associated with the Faculty of Science, Technology, and Medicine；University of Luxembourg, Luxembourg. {asier.bikandi | 提出多相机视觉惯性SLAM系统，利用楼层平面先验在GNSS拒止环境实现鲁棒定位。 | [#188](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/188) |
| [20260930] How to Reduce Localization Ambiguity? Geometry-Semantic Constrained BEV Representation Learning for Satellite-Ground Localization | Feng Junming, Xia Panwang, Wu Qiong, Lu Xudong, Jiao Zeyu, Lv Kun, Wu Zherong, Wan Yi, Ma Peifeng, Hsu Li-Ta, Zheng Zhi | The Hong Kong Polytechnic University, Hong Kong；Southern University of Science and Technology；Wuhan University, Wuhan, China；The Chinese University of Hong Kong, Hong Kong, China | 通过几何语义约束的BEV表示学习，降低卫星与地面跨视角定位的模糊性。 | [#189](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/189) |
| [20260930] LBDU-VIO: Learned Bias Dynamics and Uncertainty for Visual-Inertial Odometry with Unreliable Vision | Guo Qizhi, Lyu Junning, Lin Defu, He Shaoming | School of Aerospace Engineering and the Beijing Key Laboratory of UAV Autonomous Control, Beijing Institute of Technology, Beijing, China | 针对视觉不可靠场景，学习偏差动态与不确定性以提升视觉惯性里程计精度。 | [#190](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/190) |
| [20260930] DiffWAM: A Fast and Efficient Navigation World Action Model | Zhu Mo, Wu Yuze, Huang Xijie, Cui Xiao, Gao Fei, Zhou Xin | Zhejiang University | 提出快速高效的导航世界动作模型，用于视觉里程计与自主导航决策。 | [#191](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/191) |

## 🔎 观察

- 多源先验与学习约束结合，正成为解决定位歧义与退化问题的关键路径。
- 视觉不可靠条件下的VIO研究，从单纯滤波转向学习偏差与不确定性建模。

---

Powered by OpenClaw🦞

---

# [20260929](./202609/20260929.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日论文总体呈现出遥感与AI交叉深化趋势。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260929] Pow3R-SLAM: Real-Time RGB-D SLAM with 3D Reconstruction Priors | Kolios Christopher, Mehta Ishaan, Janjic Sasa, Bahoo Yeganeh, Saeedi Sajad | Toronto Metropolitan University, Toronto, Canada；University of Windsor, Windsor, Canada；University College London, London, United Kingdom | 聚焦Dataset-Benchmark、Traditional-SLAM，给出可复现的模型与评测方案。 | [#184](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/184) |
| [20260929] Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM | Kim Minseo, Kim Yina, Hwang Jinhwa, Alex Junho Lee | Department of Mechanical Systems Engineering, Sookmyung Women's University, 100 Cheongpa-ro 47-gil, Yongsan-gu, Seoul, Republic of Korea | 聚焦GNSS-Denied、Traditional-SLAM，给出可复现的模型与评测方案。 | [#185](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/185) |
| [20260929] SCCM: Spherically Consistent Coarse Matching for ERP Dense Feature Correspondence | Lee Gyeonggwan, Im Eunsoo, Hong Seunghwan, Suh Junghun | Kakao Mobility Corp., Seongnam, Republic of Korea Korea University, Seoul, Republic of Korea | 聚焦Dataset-Benchmark、Needs-Review，给出可复现的模型与评测方案。 | [#186](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/186) |

## 🔎 观察

- 基础模型与遥感任务结合持续增强，评测与推理能力成为关键。
- 多数工作关注算法有效性与泛化，而非硬件实现。

---

Powered by OpenClaw🦞

---

# [20260928](./202609/20260928.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦于复杂环境下的三维感知与定位。稀疏视角三维重建通过深度图渲染提升高斯泼溅的鲁棒性；林下无人机VIO数据集为GNSS拒止场景提供基准；边缘辅助多视角定位则探索任务导向通信与跨视角检索的结合。整体趋势显示，研究者正从单一模态向多源融合、从理想环境向真实复杂场景迁移，并强调可复现的基准建设。

## ✨ 今日亮点

- 稀疏视角3DGS结合深度图渲染，缓解重建退化问题
- 林下无人机VIO数据集填补GNSS拒止场景基准空白
- 任务导向通信与跨视角检索协同提升边缘定位精度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260928] Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering | Kang Jiaming, Zou Zhengxia, Shi Zhenwei | Beihang University | 提出基于深度图渲染的稀疏视角3D高斯泼溅方法，提升复杂场景重建质量。 | [#180](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/180) |
| [20260928] ForVis: An In-Field Dataset and Benchmark for VIO Using Under-Canopy UAV Flights in Forests | Kiani Arman, Ataei Masoud, Gyaase Elvis, Eiyike Jeffrey, Weiskittel Aaron, Chakraborty Prabuddha, Dhiman Vikas | Department of Electrical and Computer Engineering, University of Maine, Orono, ME 04469, USA | 发布林下无人机VIO飞行数据集与基准，面向GNSS拒止环境评估定位算法。 | [#181](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/181) |
| [20260928] Task-Oriented Communications for Edge-Assisted Multi-View Localization | Fang Zhengru, Lou Huanhuan, Hu Senkang, Tao Yihang, Li Zongdian, Deng Yiqin, Wang Jingjing, Fang Yuguang | Department of Electronic and Computer Engineering, The Hong Kong University of Science and Technology, Hong Kong (；the Hong Kong JC STEM Lab of Smart City and the Department of Computer Science, City University of Hong Kong, Hong Kong (；Zhejiang University, Hangzhou, China (；School of Data Science, Lingnan University, Tuen Mun, Hong Kong, China (；School of Cyber Science and Technology, Beihang University, Beijing, China ( | 研究边缘辅助多视角定位中的任务导向通信，融合跨视角检索与目标地理定位。 | [#182](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/182) |

## 🔎 观察

- 稀疏视角重建与林下VIO均指向真实复杂环境，表明鲁棒感知成为当前研究重点。
- 边缘辅助定位结合通信与检索，反映多源协同正从感知层向通信与决策层延伸。

---

Powered by OpenClaw🦞

---
