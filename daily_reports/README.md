# Daily Reports

最近三天日报（最新在前）：

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

# [20261118](./202611/20261118.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文聚焦空中机器人与视觉导航的交叉方向，涵盖实时SLAM、跨视角检索、视觉语言导航及自改进框架。研究趋势显示，三维重建与多模态大模型正加速融合，面向复杂环境下的自主导航与定位任务。同时，双帧记忆、递归自改进等策略被引入以提升泛化与迭代能力，数据集与基准建设亦受关注。

## ✨ 今日亮点

- Facet-SLAM提出实时三角面片泼溅SLAM，推动三维重建效率。
- 跨视角检索引入双向槽注意力，聚合结构-细节谱信息。
- 多篇工作探索视觉语言导航在无人机复杂环境中的落地。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261118] Facet-SLAM: Real-Time Triangle Splatting SLAM | Edward Beng Wai Tan, Lam Siew-Kei | College of Computing and Data Science, Nanyang Technological University, Singapore | 提出Facet-SLAM，利用三角面片泼溅实现实时SLAM，兼顾重建质量与效率。 | [#273](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/273) |
| [20261118] One Affinity, Two Axes: Bidirectional Slot Attention for Iterative Aggregation across the Structure--Detail Spectrum in Visual Retrieval | Wang Zihang, Zhu Wenkai, Kong Lingdong, Yan Teng, Liang Alan, Li Shuyuan, Chen Xieyuanli, Kong Dong, Zong Guanyu | Southeast University；National University of Singapore；The Hong Kong University of Science and Technology (Guangzhou)；Shanghai Innovation Institute；Shandong University of Science and Technology；National University of Defense Technology | 设计双向槽注意力机制，在视觉检索中迭代聚合结构与细节特征。 | [#274](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/274) |
| [20261118] A Hierarchical Onboard Vision-Language-Navigation Framework for Aerial Robots in Complex Environments | Wu Yuze, Zhu Mo, Li Xingxing, Du Yuheng, Wang Zhaoqi, Fan Yuxin, Li Wenjun, Hoi Kenghou, Han Zhichao, Zhou Xin, Gao Fei | State Key Laboratory of Industrial Control Technology, Zhejiang University, Hangzhou 310027, China | 构建分层机载视觉-语言-导航框架，面向复杂环境下的空中机器人。 | [#275](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/275) |
| [20261118] Allocentric Memory, Egocentric Acting: A Dual-Frame VLA for Urban Aerial Navigation | Xu Haotian, Hu Yue, Zhu Zhengqiu, Feng Tuo, Wang Wenguan, Yin Quanjun | National Key Laboratory of Digital Intelligent Modeling and Simulation；College of Systems Engineering, National University of Defense Technology；Zhejiang University | 提出双帧VLA框架，结合异中心记忆与自我中心行动用于城市空中导航。 | [#276](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/276) |
| [20261118] AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation | Wu Shiwei, Pan Yuwen, Li Zhi, Li Yaowen, Zhou Yan, Xu Xuemiao, Liu Yu | SIGS, Tsinghua University；Department of Electronic Engineering, Tsinghua University；Foshan University；South China University of Technology | 提出AeroRSI递归自改进方法，提升空中视觉语言导航的持续学习能力。 | [#277](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/277) |

## 🔎 观察

- 三维泼溅与SLAM结合成为实时重建新方向，但需关注动态场景下的鲁棒性。
- 视觉语言导航正从地面向空中迁移，双帧记忆与自改进策略或成关键。

---

Powered by OpenClaw🦞

---
