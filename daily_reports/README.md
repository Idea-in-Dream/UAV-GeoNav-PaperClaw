# Daily Reports

最近三天日报（最新在前）：

# [20260804](./202608/20260804.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 12 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于基础模型与数据集的构建，涵盖全球尺度密集匹配、洪水合成、3D语义场景补全及地球嵌入表示。多篇论文强调可复现性并公开代码，推动领域标准化。研究趋势显示从单一任务向多模态、物理约束与地理先验融合的方向发展。

## ✨ 今日亮点

- 全球尺度密集匹配基础模型LoRetta发布，含大规模数据集。
- FlowForm结合流体物理与拓扑一致性合成卫星洪水图像。
- Earth Embeddings探索地球观测数据的通用嵌入表示。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260804] LoRetta: A Foundation Model and Extensive Dataset for Global-Scale Remote Sensing Dense Image Matching | Yu Siwei, Guo Han, Shi Zhenwei, Zou Zhengxia | Department of Aerospace Intelligent Science and Technology, School of Astronautics, Beihang University, Beijing, China；the Key Laboratory of Spacecraft Design Optimization and Dynamic Simulation Technologies, Ministry of Education ( | LoRetta提出全球尺度遥感密集匹配基础模型及配套数据集，代码开源。 | [#53](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/53) |
| [20260804] FlowForm: Synergizing Fluid Physics with Topological Consistency for Satellite Flood Synthesis | Weihui Zhang, Ruizhi Wang, Hongye Xu, Huiqiong Wang, Li Sun, Mingli Song | Zhejiang University, Zhejiang, China | FlowForm利用流体物理与拓扑一致性约束，提升卫星洪水图像合成质量。 | [#54](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/54) |
| [20260804] Geospatial-Prior Guidance for 3D Semantic Scene Completion | Wang Meng, Zhang Shougao, He Wenzhe, Li Ruihui, Hu Nan, Tang Zhuo, Li Kenli | College of Computer Science and Electronic Engineering, Hunan University, Hunan, China | Geospatial-Prior Guidance利用地理先验引导3D语义场景补全，增强空间一致性。 | [#55](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/55) |
| [20260804] Earth Embeddings | Adam J. Stewart, Fang Heng, Isaac A. Corley, Xiao Xiang Zhu | Chair of Data Science in Earth Observation, Technical University of Munich, Munich, Germany；KTH Royal Institute of Technology, Stockholm, Sweden | Earth Embeddings研究地球观测数据的嵌入方法，旨在提升下游任务泛化能力。 | [#56](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/56) |

## 🔎 观察

- 今日论文多强调可复现性，公开代码与数据集成为标配，利于领域内比较与复现。
- 物理模型与地理先验的引入，显示遥感AI正从纯数据驱动向知识融合方向演进。

---

Powered by OpenClaw🦞

---

# [20260803](./202608/20260803.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 0 篇。

当日未检索到符合条件并纳入日报的论文。

## 🔎 观察

- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。
- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。

---

Powered by OpenClaw🦞

---

# [20260802](./202608/20260802.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦跨视角地理定位与高精地图构建。两项工作分别提出模仿人类驾驶的在线高精地图构建方法，以及基于稀疏混合专家的多尺度跨视角定位框架，均注重效率与精度平衡，推动无人机-卫星匹配及自动驾驶应用。

## ✨ 今日亮点

- 跨视角定位与高精地图构建成热点
- 稀疏混合专家提升多尺度检索效率
- 模仿驾驶行为优化在线地图生成

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260802] Driver2Map: Imitating Human Driving for Online High-Definition Map Construction | Yin Pan, Xia Runtian, Kuang Weisong, Li Kaiyu, Zhao Cong, Cao Xiangyong | Xi’an Jiaotong University | Driver2Map通过模仿人类驾驶行为，实现高效在线高精地图构建。 | [#49](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/49) |
| [20260802] One Query, Many Scales: Sparse Mixture-of-Experts for Efficient Hierarchical Cross-View Geo-Localization | Fan Ruijie, Ye Junyan, Zhu Qi, Li Weijia | Tsinghua Shenzhen International Graduate School, Tsinghua University；School of Geospatial Engineering and Science, Sun Yat-sen University | 提出稀疏混合专家模型，实现多尺度高效跨视角地理定位。 | [#50](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/50) |

## 🔎 观察

- 研究趋向于将驾驶认知融入地图生成，提升实时性。
- 稀疏专家机制在跨视角检索中展现计算效率优势。

---

Powered by OpenClaw🦞

---
