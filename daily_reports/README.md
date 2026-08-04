# Daily Reports

最近三天日报（最新在前）：

# [20260801](./202608/20260801.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于多领域交叉应用：统计部门探索负责任AI与算法采纳以优化方法论，农业遥感利用基础模型实现免训练作物制图，图像处理领域提出新型去阴影网络。整体趋势显示，AI技术正从单一任务向复杂场景、多模态融合及实际业务落地演进。

## ✨ 今日亮点

- 统计部门探索负责任AI与算法采纳，推动遥感数据融入官方统计。
- 免训练作物制图方法结合SAM与物候信息，提升时空泛化能力。
- 新型去阴影网络利用CIELAB统计，增强边界可靠性与色彩恢复。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260801] Responsible AI and Algorithmic Adoption in Methodology Development for National Statistical Offices | Tam Siu-Ming | in methodology research and development, including harnessing big data, satellite imagery, and transactional sources to improve or redesign data collection instruments | 统计部门方法论开发中负责任AI与算法采纳，利用卫星影像等大数据改进数据采集。 | [#1016](https://github.com/thinson/RS-PaperClaw/issues/1016) |
| [20260801] PhenoStitch: Training-Free Panoptic Crop Mapping from Satellite Image Time Series | Li Xuechen | University of Minnesota | PhenoStitch提出免训练泛在作物制图，结合SAM与物候信息实现时序影像全景分割。 | [#1017](https://github.com/thinson/RS-PaperClaw/issues/1017) |
| [20260801] BRIC-Net: Boundary-Reliable Illumination-Color Interaction for Remote Sensing Image Deshadowing | Lu Wei, Liu Yi, Si-Bao | MOE Key Lab of ICSP, IMIS Lab of Anhui, Anhui Provincial Key Lab of Multimodal Cognitive Computation, Zenmorn-AHU；AI Joint Lab, School of Computer Science and Technology, Anhui University, Hefei 230601, China；derives reliability-aware guidance from CIELAB statistics | BRIC-Net通过边界可靠光照-颜色交互，提升遥感图像去阴影的亮度恢复与色彩校正。 | [#1018](https://github.com/thinson/RS-PaperClaw/issues/1018) |

## 🔎 观察

- 基础模型（如SAM）在遥感时序分析中应用增多，但免训练策略仍依赖物候先验。
- 统计业务与遥感AI结合，强调算法可解释性与负责任部署，或成未来重要方向。

---

Powered by OpenClaw🦞

---

# [20260731](./202607/20260731.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦于少样本学习与图像编辑两大方向。少样本分割与场景分类方法不断涌现，旨在降低标注成本并提升泛化能力。同时，基于视觉语言模型的卫星图像编辑、无人机地雷检测数据集及高光谱分类的量子启发方法也取得进展，展示了多模态融合与跨域适应在遥感应用中的潜力。

## ✨ 今日亮点

- 少样本遥感分割与分类方法成热点，强调训练自由与局部一致性。
- 视觉语言模型引入卫星图像编辑，实现掩码条件化编辑。
- 高光谱分类探索量子态表示，创新密度矩阵学习框架。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260731] SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation | Talha Muhammad, Muhammad Ahmed Amer | Independent Researcher | SatEdit利用视觉语言模型生成掩码，实现卫星图像的掩码条件化编辑。 | [#1010](https://github.com/thinson/RS-PaperClaw/issues/1010) |
| [20260731] Training-Free Entity-Level Few-Shot Segmentation of Remote Sensing Images with Advection Refinement | Bai Xueting, Ni Huan | School of Remote Sensing and Geomatics Engineering, Nanjing University of Information Science and Technology | 提出无需训练的地物级少样本分割方法，结合平流细化提升精度。 | [#1011](https://github.com/thinson/RS-PaperClaw/issues/1011) |
| [20260731] Locally Consistent Transductive Information Maximization for Few-Shot Remote Sensing Scene Classification | Karim El Khoury, Gérin Benoît, Macq Benoît, Christophe De Vleeschouwer | ICTEAM, UCLouvain, Louvain-la-Neuve, Belgium | 采用局部一致转导信息最大化，改进少样本遥感场景分类性能。 | [#1012](https://github.com/thinson/RS-PaperClaw/issues/1012) |
| [20260731] SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark for UAV/UGV-Based SUrface LANDmine Detection Under Domain Shift | Lekhak Sagar, Prasanna Reddy Pulakurthi, Joshi Lalit, Bhatta Ramesh, Emmett J. Ientilucci | the Rochester Institute of Technology, Rochester, NY, USA；Thapathali Campus, Institute of Engineering, Tribhuvan University, Kathmandu, Nepal | 发布SULAND v2数据集，用于无人机/地面机器人地雷检测的域偏移基准。 | [#1013](https://github.com/thinson/RS-PaperClaw/issues/1013) |
| [20260731] LegoQ: Density-Matrix Representation Learning with Spectral-Spatial State Transitions for Hyperspectral Classification | Cao Weijia, Yang Xiaofei, Wang Fu, Zhou Yicong, Zhou Xiang | Sun Yat-sen University；University of Macau | LegoQ通过密度矩阵表示学习光谱-空间状态转换，实现高光谱分类。 | [#1014](https://github.com/thinson/RS-PaperClaw/issues/1014) |

## 🔎 观察

- 少样本学习在遥感领域持续深化，从分类扩展到分割，且强调无需训练。
- 量子启发模型开始应用于高光谱分类，显示跨学科融合趋势。

---

Powered by OpenClaw🦞

---

# [20260730](./202607/20260730.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 12 篇；最终纳入日报 12 篇。

今日研究聚焦多模态融合与高效特征学习，涵盖洪水监测、农田分割、图像复原等应用。CLIP与SAR结合提升变化检测效率，Mamba与多尺度卷积推动高光谱分类，4D重建与无人机感知拓展动态场景理解。整体趋势强调跨模态协同与轻量化设计，以应对复杂遥感任务。

## ✨ 今日亮点

- 多模态融合成主流，文本-图像、SAR-光学协同应用广泛
- 高效特征学习受关注，Mamba与低秩专家网络兴起
- 动态场景理解深化，4D重建与状态转移模型涌现

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260730] Finding Change in Satellite Archives from Text: How to Combine Before-and-After Images Efficiently | Roy Simon, Bong Mark, Beltrame Giovanni | Polytechnique Montréal | 利用文本检索卫星影像变化，提出高效前后时相融合方法 | [#997](https://github.com/thinson/RS-PaperClaw/issues/997) |
| [20260730] Large scale cross-regional remote sensing flood monitoring framework for operative mapping and impact analysis | Novikov Ilya, Illarionova Svetlana, Dzharkinov Ruslan, Smirnova Maria, Abdullin Ayrat, Korotkova Anna, Ulianova Mariia, Shadrin Dmitrii, Burnaev Evgeny | Skolkovo Institute of Science and Technology, Moscow, 121205, Russia；Trofimuk Institute of Petroleum Geology and Geophysics SB RAS；King Fahd University of Petroleum and Minerals, Dhahran, 31261；Tyumen Industrial University, Tyumen, 625000, Russia；Huawei Russian Research Institute, Moscow, Russia | 构建跨区域SAR洪水监测框架，实现快速制图与影响分析 | [#998](https://github.com/thinson/RS-PaperClaw/issues/998) |
| [20260730] AdaAnchor4D: Anchor-Conditioned Spatiotemporal Feature Aggregation for Monocular UAV 4D Reconstruction | Xu Peiyi, Zhang Junpeng, Li Guanbin, Shang Ronghua, Feng Mingtao, Dong Le, Dong Weisheng, Shi Guangming, Feng Jie | Xidian University, Xi’an, China；Sun Yat-sen University, Guangzhou, China | 提出锚点条件时空聚合，提升单目无人机4D重建精度 | [#999](https://github.com/thinson/RS-PaperClaw/issues/999) |
| [20260730] MSCM-net: A hyperspectral image classiffcation method based on multi-scale convolution and Mamba | Chen Jianjun, Wang Linlin, Chang Lifang, Huo Limin, Song Shujiang, Zhao Yanjia, Shao Mingwei | Research highlight 1；Research highlight 2；Research highlight 3；Research highlight 4；Research highlight 5 | 结合多尺度卷积与Mamba，增强高光谱图像分类性能 | [#1000](https://github.com/thinson/RS-PaperClaw/issues/1000) |
| [20260730] Space2Ground 2.0: A Multi-Source Dataset and Framework for Agricultural Monitoring through Fusion of Street-Level and Satellite Imagery | Tsardanidis Iason, Koukos Alkiviadis, Choumos George, Sitokontantinou Vasileios, Kontoes Charalampos | Operational Unit BEYOND Centre, IAASARS, National Observatory of Athens, Athens, Greece；Artificial Intelligence Group, Wageningen University \& Research, The Netherlands – | 融合街景与卫星影像，构建农业监测多源数据集与框架 | [#1001](https://github.com/thinson/RS-PaperClaw/issues/1001) |
| [20260730] Think with Extra-Image: A Farmland Segmentation Agent Driven by Spatio-Temporal Information Gain | Wu Haiyang, Mu Weiliang, Du Zhuofei, Zhong Dandan, Shi Kaijie, Li Haifeng, Tao Chao | Central South University, Changsha, China | 利用时空信息增益驱动智能体，优化农田分割决策 | [#1002](https://github.com/thinson/RS-PaperClaw/issues/1002) |
| [20260730] Meteosat Third Generation imagery improves CNN-based SSI retrieval | Pribõtkin Gordei, Post Piia, Toll Velle | Institute of Computer Science；University of Tartu；Centre for Climate Research, Institute of Physics | 第三代气象卫星影像提升CNN太阳辐照度反演精度 | [#1003](https://github.com/thinson/RS-PaperClaw/issues/1003) |
| [20260730] FootprintNet: State-Transition-Guided Dynamic Footprint Learning for Multi-temporal Remote Sensing Change Detection | Zhang Haotian, Chen Hao, Guo Han, Zou Zhengxia, Shi Zhenwei | Beihang University 1, Shanghai Artificial Intelligence Laboratory 2 | 状态转移引导足迹学习，改善多时相建筑变化检测 | [#1004](https://github.com/thinson/RS-PaperClaw/issues/1004) |
| [20260730] CoRE-UIR: Prior-guided common and residual experts for efficient all-in-one remote sensing image restoration | Zhang Zaiyan, Yuan Qiangqiang, Li Jie, Lihe Ziyang, Wan Yu, Chen Yuzeng, Su Xin, Zhang Liangpei | a School of Geodesy and Geomatics, Wuhan University, Wuhan 430079, Hubei, China；b School of Artificial Intelligence, Wuhan University, Wuhan 430072, Hubei, China；c State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan 430079, Hubei, China；Universal Image Restoration), a prior-guided global-local framework centered on the Common-and- | 先验引导的通用与残差专家网络，实现高效一体化复原 | [#1005](https://github.com/thinson/RS-PaperClaw/issues/1005) |
| [20260730] Learning to Understand Body Language from Flight through Robust 3D Avatar Placing | Costea Dragos, Marcu Alina, Lazar Cristina, Leordeanu Marius | National University of Science and Technology “Politehnica” Bucharest, Romania；“Simion Stoilow” Institute of Mathematics of the Romanian Academy；NORCE Norwegian Research Centre AS | 通过3D虚拟人放置，从飞行中学习理解人体动作意图 | [#1006](https://github.com/thinson/RS-PaperClaw/issues/1006) |
| [20260730] Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation | Lee Dohun, Yoo Kyeonghyun, Kim Seokmin, Lee Byongho, Oh Seungjoo, Kim Hwangnam | Department of Electrical and Electronic Engineering, Korea University, Seoul, Republic of Korea；Department of Smart Mobility Engineering, Inha University, Incheon, Republic of Korea | 跨实体骨架迁移，实现无人机中继编队3D协同规划 | [#1007](https://github.com/thinson/RS-PaperClaw/issues/1007) |
| [20260730] A Systems Engineering Framework for Vision-Language-Enabled UAV Triage and Disaster Response | Saha Swapnil, Bhuvan Rajanasiriyur Jagadeesha, Patnaik Karishma, Majumdar Neelakshi | University of Arkansas, Fayetteville, Arkansas, 72701, USA；University of Michigan-Dearborn, Dearborn, Michigan, 48128, USA；Graduate Research Assistant, Department of Mechanical Engineering；Graduate Research Assistant, Department of Electrical and Computer Engineering；Assistant Professor, Department of Electrical and Computer Engineering；Assistant Professor, Department of Mechanical Engineering | 系统工程框架集成视觉语言模型，支持无人机灾后响应 | [#1008](https://github.com/thinson/RS-PaperClaw/issues/1008) |

## 🔎 观察

- 多模态融合从数据级向任务级演进，文本与SAR等异构信息协同增强解译能力
- 轻量化与高效架构（如Mamba、低秩）成为遥感深度学习新趋势，平衡精度与计算

---

Powered by OpenClaw🦞

---
