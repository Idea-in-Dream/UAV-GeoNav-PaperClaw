# Daily Reports

最近三天日报（最新在前）：

# [20261106](./202611/20261106.md)
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

# [20261105](./202611/20261105.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦于多模态融合定位与建图在复杂环境下的鲁棒性提升。三篇论文分别从跨视角三维重建、视觉惯性里程计漂移抑制以及激光-惯性-视觉紧耦合里程计三个方向展开，体现了遥感与机器人感知领域对GNSS拒止场景下高精度定位的持续关注。跨视角地理定位与多传感器融合成为核心趋势，强调物理约束与按需特征管理以平衡精度与计算开销。

## ✨ 今日亮点

- 跨视角三维重建实现地面与卫星图像联合地理定位与相机中心估计。
- 按需视觉特征创建策略有效缓解GNSS拒止下视觉惯性里程计漂移。
- 物理解耦但紧耦合的LiDAR-惯性-视觉里程计提升多模态融合鲁棒性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261105] Georeferenced Cross-View 3D Reconstruction from Ground and Satellite Images | David G. Shatwell, Shah Mubarak | Institute of Artificial Intelligence, University of Central Florida；only the local scene geometry, but also localizing every camera center and 3 D | 提出地面与卫星图像联合三维重建方法，同时恢复局部场景几何并定位相机中心与三维点。 | [#239](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/239) |
| [20261105] Not Losing Your Way: Mitigating Visual-Inertial Odometry Drift through On-Demand Visual Feature Creation | D’Angelo Simone, Corrado Gianmarco, Esposito Federico, Scognamiglio Vincenzo, Ruggiero Fabio | PRISMA Lab, Department of Engineering and Information Technology, UAVs in GNSS-denied environments, whose effectiveness；University of Naples Federico II, Naples, Italy | 针对GNSS拒止环境，通过按需创建视觉特征抑制视觉惯性里程计漂移，提升定位持续性。 | [#240](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/240) |
| [20261105] FREE-LIVO: Physically Decoupled Yet Tightly Coupled LiDAR-Inertial-Visual Odometry | Tabata Reon, Koide Kenji, Oishi Shuji, Okawara Taku, Aoki Mizuho, Takanose Aoki, Yokozuka Masashi, Miura Jun | Active Intelligent Systems Lab., Toyohashi University of Technology, Japan | 提出物理解耦却紧耦合的LiDAR-惯性-视觉里程计框架，兼顾模态独立性与融合精度。 | [#241](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/241) |

## 🔎 观察

- 跨视角地理定位正从二维检索向三维几何重建演进，强调相机中心与场景结构的联合估计。
- 多传感器融合呈现“解耦设计、紧耦合优化”思路，以降低模态干扰并提升GNSS拒止下的鲁棒性。

---

Powered by OpenClaw🦞

---

# [20261104](./202611/20261104.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 3 篇。

今日研究聚焦于视觉SLAM与三维重建中的尺度一致性与鲁棒性问题。三篇论文分别从不同角度切入：基于VGGT的SLAM通过隐式语义与序列一致回环实现尺度锚定；METRIC-GS针对3D高斯泼溅提出选择性度量尺度估计；立体视觉惯性里程计则利用卡尔曼滤波地面高度估计应对反射干扰。整体趋势显示，研究者正致力于在复杂场景下提升几何估计的精度与稳定性，并注重代码开源与可复现性。

## ✨ 今日亮点

- VGGT-SLAM利用隐式语义与序列一致回环解决尺度漂移问题。
- METRIC-GS为3D高斯泼溅引入选择性度量尺度估计方法。
- 立体VIO通过卡尔曼滤波地面高度估计增强反射鲁棒性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261104] Scale Anchoring via Implicit Semantics and Sequence-Consistent Loop Closure for VGGT-Based SLAM | Jin Ziyi, Yu Kangjin, Wang Beichen, Jiang Can, Xia Zhongpu, Xu Jie | Anyverse Dynamics | 提出基于VGGT的SLAM系统，通过隐式语义和序列一致回环实现尺度锚定，提升轨迹精度。 | [#235](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/235) |
| [20261104] METRIC-GS: Selective Metric-Scale Estimation for 3D Gaussian Splatting | Yang Sooyeun, Jongseong Brad Choi | Department of Mechanical Engineering, SUNY Korea；Department of Mechanical Engineering, Stony Brook University；Department of Computer Science, SUNY Korea | 针对3D高斯泼溅提出选择性度量尺度估计方法，改善重建的尺度一致性。 | [#236](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/236) |
| [20261104] Reflection-Robust Stereo Visual-Inertial Odometry via Kalman-Filtered Ground-Height Estimation | Hwang Uihyun, Shin Sungjae, Kim Dongjae, Myung Hyun | School of Electrical Engineering, Korea Advanced Institute of Science and Technology, Daejeon, 34141, South Korea | 设计反射鲁棒的立体视觉惯性里程计，利用卡尔曼滤波地面高度估计抑制反射干扰。 | [#237](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/237) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| When to Ask for Help: Uncertainty-Triggered Aerial Refinement for Off-Road Navigation | [2611.06702v1](https://arxiv.org/abs/2611.06702v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 三篇工作均关注尺度或几何一致性，反映SLAM与三维重建对度量精度的持续需求。
- 方法上呈现多传感器融合与滤波估计结合的趋势，以应对复杂环境中的退化问题。

---

Powered by OpenClaw🦞

---
