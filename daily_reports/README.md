# Daily Reports

最近三天日报（最新在前）：

# [20260915](./202609/20260915.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日论文聚焦于SLAM与三维重建的轻量化、语义化与多源融合。PanoGS-SLAM将全景相机与3D高斯泼溅结合，拓展了SLAM的感知视野；HuMemSLAM受人类视觉认知启发，提升语义位置识别的鲁棒性；TIO-Former面向纳米无人机，以超轻量流式因果Transformer实现ToF-惯性里程计；HLC-GS则利用风险图引导的高度层一致性高斯泼溅，从光学卫星影像重建DSM。整体趋势显示，研究者正致力于在资源受限平台上提升定位与建图的精度和鲁棒性。

## ✨ 今日亮点

- 全景3D高斯泼溅SLAM拓展了视觉SLAM的感知范围与重建能力
- 人类视觉记忆机制被引入语义位置识别以增强鲁棒性
- 超轻量流式Transformer为纳米无人机提供新型ToF-惯性里程计方案

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260915] PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM | Mao Yongqi, Shi Hao, Zhang Yufan, Yi Zhonghua, Guo Xiangfei, Wang Kaiwei | Zhejiang University；National University of Defense Technology | 提出全景3D高斯泼溅SLAM系统，利用全景相机提升建图与定位的视野覆盖。 | [#136](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/136) |
| [20260915] HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM | Adebambo Mayowa, Donnelly Sebastian, Amaritei Armand, Bradley Andrew, Rast Alexander | Research in human visual cognition suggests that recog-；School of Engineering, Computing & Mathematics, Oxford Brookes；University, Oxford, UK；University, Oxford, UK. 2) HuMemSLAM, the integration of HuMem-VPR with | 受人类视觉认知启发，设计高效语义位置识别模块以增强视觉SLAM鲁棒性。 | [#137](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/137) |
| [20260915] TIO-Former: Ultra-Lightweight 6-Directional ToF-Inertial Odometry for Nano-UAVs via a Streaming Causal Transformer | Liu Yang, He Yifan, Zhao Wenhao, Mo Xiangyu, Xu Yang, Wei Hao, Ma Mingze, Li Huan, Wu Yifan, Dai Zipeng, Zhou Xin, Gao Fei | Zhejiang University, Hangzhou, China | 面向纳米无人机，提出超轻量流式因果Transformer实现6方向ToF-惯性里程计。 | [#138](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/138) |
| [20260915] HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery | Yang Jie, Pi Yingdong, Luo Qiyan, Wang Xiaoyu, Wen Lekang, Wang Mi | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；Hubei Luojia Laboratory；School of Computer Science, Wuhan University | 利用风险图引导高度层一致性高斯泼溅，从光学卫星影像重建DSM。 | [#139](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/139) |

## 🔎 观察

- 轻量化与语义化成为SLAM研究主线，纳米无人机与全景感知等新平台推动算法适配。
- 3D高斯泼溅持续向遥感与SLAM渗透，但跨模态融合与实时性仍是待验证的关键。

---

Powered by OpenClaw🦞

---

# [20260911](./202609/20260911.md)
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

# [20260910](./202609/20260910.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日候选论文聚焦农业机器人视觉定位与建图。该研究面向温室番茄采摘场景，针对被叶片遮挡的隐藏果实检测难题，提出结合分层定位与GLOMAP的视觉SLAM方案。方法融合传统SLAM、视觉里程计与精细配准，旨在为机器人提供稳定位姿估计，从而辅助发现隐蔽目标。整体趋势显示，SLAM技术正从通用导航向特定农业场景的精细感知任务延伸，强调在复杂植被环境下的鲁棒性与实用性。

## ✨ 今日亮点

- 面向温室采摘，用视觉SLAM检测被遮挡的隐藏番茄
- 融合分层定位与GLOMAP，提升复杂植被环境位姿估计
- 方法涉及精细配准、传统SLAM与视觉里程计多模块

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260910] Visual-SLAM for the detection of hidden tomatoes in greenhouses by Hierarchical Localization and GLOMAPfor robotized harvesting | Cañadas-Aránega Fernando, José C. Moreno, José L. Blanco-Claraco, Rodríguez Francisco | Department of Informatics, CIESOL, ceiA3, Universidad de Almería；Department of Engineering, CIESOL, ceiA3, Universidad de Almería | 提出结合分层定位与GLOMAP的视觉SLAM，用于温室机器人采摘中检测被遮挡的隐藏番茄。 | [#133](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/133) |

## 🔎 观察

- 农业场景SLAM正从导航定位转向服务精细感知，隐藏目标检测成为新切入点。
- 传统SLAM与学习型建图结合，或成复杂植被环境下鲁棒定位的务实路径。

---

Powered by OpenClaw🦞

---
