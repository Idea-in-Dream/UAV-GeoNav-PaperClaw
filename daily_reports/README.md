# Daily Reports

最近三天日报（最新在前）：

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
