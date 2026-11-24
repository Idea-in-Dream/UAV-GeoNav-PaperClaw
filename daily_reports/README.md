# Daily Reports

最近三天日报（最新在前）：

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

# [20261120](./202611/20261120.md)
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

# [20261119](./202611/20261119.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦于视觉惯性里程计与地理定位的鲁棒性与效率提升。AnyVIO提出跨平台前馈流式VIO，强调泛化部署；序列到空间方法利用视觉语言蒸馏构建显式空间信念以支持主动地理定位；立体VO结合几何前馈模型实现密集度量建图；AeroBelief则关注预算约束下的证据引导航空感知验证。整体趋势显示，研究者正从单一模块优化转向跨平台、跨模态的闭环系统设计，并重视实际部署中的资源约束与验证效率。

## ✨ 今日亮点

- AnyVIO实现跨平台前馈流式VIO，提升GNSS拒止环境下的泛化能力。
- 视觉语言蒸馏构建显式空间信念，推动主动地理定位从序列到空间推理。
- AeroBelief引入预算化首动作验证，优化证据引导的航空感知决策效率。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261119] AnyVIO: Feed-Forward Streaming Visual-Inertial Odometry Across Platforms | Atekha Omoruyi, Greiff Marcus, Zhang Ray, Carlone Luca | MIT；TRI | 提出跨平台前馈流式VIO框架AnyVIO，在GNSS拒止环境下实现无需重训练的泛化部署。 | [#279](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/279) |
| [20261119] From Sequence to Space: Explicit Spatial Belief with Vision-Language Distillation for Active Geo-Localization | Xu Ziyang, Han Peng, Zhou Hai | National Space Science Center, Chinese Academy of Sciences, Beijing 100190, China；University of Chinese Academy of Sciences, Beijing 101408, China | 利用视觉语言蒸馏构建显式空间信念，将序列观测转化为空间表示以支持主动地理定位。 | [#280](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/280) |
| [20261119] Stereo Visual Odometry with In-the-Loop Geometric Feed-Forward Models Towards Dense Metric Mapping | Fahira Afzal Maken, Sagun Man Singh Shrestha, Vanderfeen Edward, Lucas Carvalho de Lima, Li Rongxin, Sun Changming, Ramezani Milad | School of Electrical Engineering and Robotics, Queensland University of Technology (QUT), Brisbane, Australia | 将几何前馈模型嵌入立体视觉里程计闭环，面向密集度量建图提升几何一致性。 | [#281](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/281) |
| [20261119] AeroBelief: Budgeted First-Action Verification for Evidence-Guided Aerial Sensing | Li Tianren, Li Dongbo, Chen Hongkai, Liu Jie, Xing Guoliang | Harbin Institute of Technology China；The Chinese University of Hong Kong China | 提出预算化首动作验证策略，在有限感知预算下证据引导地优化航空目标定位决策。 | [#282](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/282) |

## 🔎 观察

- VIO研究正从精度竞赛转向跨平台泛化与流式部署，强调实际场景中的即插即用能力。
- 地理定位与航空感知开始引入显式空间信念和预算约束，反映从被动感知向主动决策的范式迁移。

---

Powered by OpenClaw🦞

---
