# Daily Reports

最近三天日报（最新在前）：

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

# [20260909](./202609/20260909.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究趋势聚焦于利用开放地图数据提升定位与里程计鲁棒性。一篇工作提出与里程计无关的漂移校正方法，通过将轨迹段匹配至OpenStreetMap车道中心线，实现无需依赖特定里程计模型的全局校正。该方向融合传统SLAM、视觉里程计与地图辅助定位，强调开放数据在长期导航中的价值，有望降低对高精地图的依赖，推动低成本、可扩展的定位方案发展。

## ✨ 今日亮点

- 利用OSM车道几何实现里程计无关的漂移校正
- 融合Map-Aided-VIO与传统SLAM、视觉里程计
- 开放地图数据降低对高精地图的依赖

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260909] Odometer-Agnostic Drift Correction Using OpenStreetMap Lane Geometry | Caballero Joaquin, Garcia-Fidalgo Emilio, Ortiz Alberto, Ralli Jarno | trajectory segments to OpenStreetMap (OSM) lane centerlines；and Computer Science, Institute of Artificial Intelligence, University of | 提出与里程计无关的漂移校正方法，将轨迹段匹配至OSM车道中心线以修正定位误差。 | [#131](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/131) |

## 🔎 观察

- 开放地图数据正成为SLAM漂移校正的轻量级替代方案，减少对高精地图的依赖。
- 里程计无关设计提升方法通用性，但匹配精度受OSM车道几何质量影响。

---

Powered by OpenClaw🦞

---
