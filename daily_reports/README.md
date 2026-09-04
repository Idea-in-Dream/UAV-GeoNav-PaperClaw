# Daily Reports

最近三天日报（最新在前）：

# [20260903](./202609/20260903.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦于移动平台感知与三维重建。一方面，探讨移动机器人平台在精密检测中的精度与可重复性，强调平台可靠性；另一方面，利用点云与IMU数据预测地形引起的振动，并引入轻量化方法。此外，针对大规模航空表面重建，提出结构感知正则化的高斯泼溅方法，以提升重建质量。整体趋势显示，研究正从传统几何方法向数据驱动与物理模型结合的方向发展，并注重实际部署中的鲁棒性与效率。

## ✨ 今日亮点

- 移动平台精度与可重复性研究受关注，强调检测可靠性。
- 轻量化振动预测结合点云与IMU，提升地形适应性。
- 结构感知高斯泼溅用于大规模航空表面重建，优化质量。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260903] A comparative study on the accuracy & repeatability of mobile robotic platforms for the delivery of precision NDE measurement | SeyedMohammadAmin Nabi Pour, S. Gareth Pierce, Vithanage Randika, Mohseni Ehsan, Carswell David, Shields Matthew | University of Strathclyde | 对比研究移动机器人平台在精密无损检测中的精度与可重复性表现。 | [#122](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/122) |
| [20260903] RoughSense: Lightweight Terrain-Induced Rover Vibration Prediction Using Point Clouds and IMU Feedback | Gabriel Manuel Garcia, Aravecchia Stephanie, Miguel Angel Olivares-Mendez | From Anonymous center, Anonymous；From University of Luxembourg, Luxembourg；From IRL Georgia Tech-CNRS, Metz, France | 提出轻量化方法，利用点云和IMU反馈预测地形引起的漫游车振动。 | [#123](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/123) |
| [20260903] STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction | Li Bocheng, Zhang Wenjuan, Jie Pan. Dongxu Han, Ma Xuesong, Yao Yiling, Wang Yaning | State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute, Chinese Academy of Sciences；Aerospace Information Research Institute, Chinese Academy of Sciences；University of Chinese Academy of Sciences | 提出结构感知正则化高斯泼溅，用于大规模航空表面高质量重建。 | [#124](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/124) |

## 🔎 观察

- 研究侧重平台感知与重建，但缺乏多传感器融合的端到端方案。
- 轻量化与正则化设计表明，计算效率与结构先验正成为关键考量。

---

Powered by OpenClaw🦞

---

# [20260902](./202609/20260902.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦于无人机在GNSS拒止环境下的视觉定位与感知。牛津大学提出AutoCompass，利用弱标签学习实现基于公共地图的精准视觉定位，解决跨视角检索与配准难题。北航团队则推出多鱼眼全景感知平台，面向超低空无人机，通过视差感知提升GNSS拒止下的导航能力。两项工作均强调数据集与基准构建，推动无人机自主导航在无卫星信号场景下的鲁棒性发展。

## ✨ 今日亮点

- 弱标签学习驱动跨视角定位，降低标注成本。
- 多鱼眼全景感知平台，应对超低空视差挑战。
- GNSS拒止场景成研究热点，数据集同步推进。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260902] AutoCompass: Accurate Visual Localization on Public Maps by Learning from Weak Labels | Tirado-Garín Javier, Alan Savio Paul, Chen Shuai, Barroso-Laguna Axel, Cavallari Tommaso, Turmukhambetov Daniyar, Victor Adrian Prisacariu, Brachmann Eric | University of Oxford | AutoCompass利用弱标签在公共地图上实现无人机精准视觉定位，无需GNSS。 | [#119](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/119) |
| [20260902] From Multi-Fisheye Sensing to Panoramic Perception: A Parallax-Aware Onboard Platform for Ultra-Low-Altitude UAVs | Dai Dun, Lu Ze, He Cheng, Wang Yaowen, Quan Quan | School of Automation Science and Electrical Engineering, Beihang University, Beijing, China (；the Tianmushan Laboratory, Hangzhou, China (；School of Automation Science and Electrical Engineering, Beihang University, Beijing, China | 北航提出多鱼眼全景感知平台，用于超低空无人机GNSS拒止环境导航。 | [#120](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/120) |

## 🔎 观察

- 跨视角检索与配准结合弱监督，成为视觉定位新趋势。
- 超低空场景推动专用传感器平台与数据集协同开发。

---

Powered by OpenClaw🦞

---

# [20260901](./202609/20260901.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于3D场景理解与重建，共两篇论文。其一提出无需训练的开放词汇3D实例映射方法，可适配RGB-D与单目SLAM系统；其二针对大规模无人机场景，提出在线3D重建框架，利用前馈3R模型提升鲁棒性。两篇均涉及3D映射、SLAM及数据集构建，体现了从传统几何方法向学习驱动与开放词汇理解的融合趋势。

## ✨ 今日亮点

- 开放词汇3D实例映射实现免训练跨场景泛化
- 无人机大规模场景在线重建强调鲁棒性与实时性
- 3D重建与SLAM结合，推动自主导航应用

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260901] VOIM: Training-Free Open-Vocabulary 3D Instance Mapping for RGB-D and Monocular SLAM | Song Sangmin, Kodagoda Sarath, Marc G. Carmichael, Thiyagarajan Karthick, Gunatilake Amal, Prentice Kelly, Martin Jodi | the Robotics Institute, Faculty of Engineering and Information Technology, University of Technology Sydney, Ultimo NSW, Australia；the Smart Sensing and Robotics Laboratory (SensR Lab), Centre for Advanced Manufacturing Technology, School of Engineering, Design and Built Environment, Kingswood NSW, Australia | 提出无需训练的开放词汇3D实例映射方法，支持RGB-D与单目SLAM系统。 | [#116](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/116) |
| [20260901] On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios | Shen Zhe, Lou Liyuan, Yu Yifei, Wang Guanbo, Ji Quanjian, Wang Xin, Zhan Zongqian | School of Geodesy and Geomatics, Wuhan University, Wuhan 430079, China | 提出在线3D重建框架，利用前馈3R模型应对大规模无人机场景挑战。 | [#117](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/117) |

## 🔎 观察

- 研究趋势显示3D映射正从封闭集走向开放词汇，增强泛化能力。
- 无人机场景推动3D重建向在线、鲁棒方向发展，兼顾精度与效率。

---

Powered by OpenClaw🦞

---
