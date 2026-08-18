# Daily Reports

最近三天日报（最新在前）：

# [20260817](./202608/20260817.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于跨视角地理定位与GNSS拒止环境下的无人机导航。两项工作分别提出跨粒度对齐的跨视角视频定位方法，以及基于标记约束的位姿图校正技术，均强调在无卫星信号条件下的高精度定位，并配套开源数据集与基准，推动该领域可复现研究。

## ✨ 今日亮点

- 跨视角视频定位引入跨粒度对齐，提升检索与配准精度。
- GNSS拒止下利用标记约束校正位姿图，增强跨平台定位鲁棒性。
- 两项研究均发布数据集与基准，促进可复现性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260817] X$^2$Localizer: Cross-grained Alignment for Progressive Cross-view Video Geo-localization | Zeng Zichao, Fan Weijia, Chen Yufan, June Moh Goo, Zheng Junwei, Liu Ruiping, Peng Kunyu, Zhang Jiaming, Stiefelhagen Rainer, Boehm Jan | Hunan University；University of Alberta；Shenzhen University | 提出X$^2$Localizer，通过跨粒度对齐实现渐进式跨视角视频地理定位，并开源基准。 | [#82](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/82) |
| [20260817] Marker-Constrained Pose-Graph Correction for Cross-Platform Georeferencing in GNSS-Denied Environments | Giberna Marco, Jose Luis Sanchez Lopez, Voos Holger | Automation and Robotics Research Group, Interdisciplinary Centre for Security, Reliability；and Trust (SnT), University of Luxembourg；Faculty of Science, Technology and Medicine, University of Luxembourg, 4365 | 提出标记约束的位姿图校正方法，解决GNSS拒止环境下跨平台地理配准问题。 | [#83](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/83) |

## 🔎 观察

- 跨视角定位研究趋向于结合粗检索与细配准，以应对视角差异。
- GNSS拒止环境下的定位方案多依赖视觉与地图先验，强调多源融合。

---

Powered by OpenClaw🦞

---

# [20260816](./202608/20260816.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 0 篇。

当日未检索到符合条件并纳入日报的论文。

## 🔎 观察

- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。
- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。

---

Powered by OpenClaw🦞

---

# [20260815](./202608/20260815.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦SLAM技术，共两篇论文。其一结合事件相机与3D高斯泼溅，提出运动模糊鲁棒的SLAM系统，提升动态场景定位精度。其二提出自适应混合ICP的LiDAR SLAM方法，通过分类对应点并平衡残差，增强鲁棒性与效率。整体趋势显示，SLAM正融合多传感器与先进表示，以应对复杂环境挑战。

## ✨ 今日亮点

- 事件相机调制高斯泼溅，攻克运动模糊难题
- 自适应ICP分类点集，提升LiDAR SLAM鲁棒性
- SLAM融合多模态，迈向高动态场景应用

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260815] MotionGS-SLAM: Event-Modulated Gaussian Splatting for Motion-Blur Robust SLAM | Hu Zhiqiang, Huang Shouren, Ishikawa Masatoshi | the Research Institute for Science \& Technology, Tokyo University of Science | 提出事件调制高斯泼溅SLAM，利用事件相机应对运动模糊，提升定位鲁棒性。 | [#80](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/80) |
| [20260815] HP2-SLAM: Adaptive Hybrid ICP for Robust and Efficient LiDAR SLAM | Tran Nam, Tran Thu, Phan Hieu, Luu Thai, Nguyen Toan, William J. Beksi, Dang Tuan | Department of Electrical Engineering and Computer Science, Uni- with local neighborhood size. Correspondences are classified；Department into planar and non-planar sets, and the balance between；of Computer Science, University of Texas at Dallas, Richardson, TX, point-to-plane and point-to-point residuals emerges directly；Robotics Lab, University of Arkansas. ∗ | 提出自适应混合ICP的LiDAR SLAM，分类平面与非平面点，平衡残差提升效率。 | [#81](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/81) |

## 🔎 观察

- SLAM研究趋向多传感器融合，事件相机与激光雷达互补，增强极端场景适应性。
- 3D高斯泼溅开始应用于SLAM，预示实时高保真建图与定位的融合新方向。

---

Powered by OpenClaw🦞

---
