# Daily Reports

最近三天日报（最新在前）：

# [20260726](./202607/20260726.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦于多模态与安全合规性，涵盖无人机智能体基准、空地平台行人跟踪、越野导航规划、遥感图像生成及极化SAR分类。趋势显示，自监督学习、对比学习及新型架构（如Mamba）正推动遥感智能体在复杂环境下的感知与决策能力提升。

## ✨ 今日亮点

- 多模态无人机智能体安全策略基准发布
- 空地平台行人跟踪多线索融合框架提出
- 方向自适应Mamba用于极化SAR分类

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260726] MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents | Belal S. Alsinglawi, Wang Weizheng, Wu Junyi, Jiang Yi, Lin Lianhai, Debbah Merouane, Alsmadi Izzat | College of Technological Innovation, Zayed University, Abu Dhabi, United Arab Emirates (；School of Computer Science and Information Technology, The University of Adelaide, Adelaide, SA, Australia (；School of Computer Science and Engineering, University of Emergency Management, Beijing, China (e-mails；Department of Computer and Information Engineering, College of Computing and Mathematical Sciences, Khalifa University, Abu Dhabi, United Arab Emirates ( | 提出MulRobBench基准，评估多模态无人机智能体安全策略合规性。 | [#969](https://github.com/thinson/RS-PaperClaw/issues/969) |
| [20260726] Beyond Appearance: A Multi-cue Framework and Large-scale Benchmark for Pedestrian Association and Tracking on Mobile Aerial-Ground Platforms | Wu Ruiqi, Jiao Bingliang, Han Ruize, Yu Hangzheng, Jiang Xunkai, Wang Shining, Hu Yuanqi, Wang Wenxuan, Wang Peng | School of Computer Science, Northwestern Polytechnical University, Xi'an, China; Ningbo Institute, Northwestern Polytechnical University, Ningbo, China; and National Engineering Laboratory for Integrated Aero-Space-Ground-Ocean Big Data Application Technology, Xi'an, China (；the Shenzhen University of Advanced Technology, Shenzhen, China ( | 构建多线索框架与大规模基准，实现空地平台行人关联与跟踪。 | [#970](https://github.com/thinson/RS-PaperClaw/issues/970) |
| [20260726] Learning Traversability-Aware Global Planners for Long Horizon Off-Road Navigation | Viswanath Kasi, Jason M. Gregory, Kolhe Shaunak, Saripalli Srikanth | This research was developed with funding from the Defense Advanced；Research Projects Agency (DARPA) and DEVCOM Army Research Labo-；Texas A&M University, College Station, TX 77840, USA kasiv；DEVCOM Army Research laboratory, Adelphi, MD, USA | 自监督学习可通行性感知全局规划器，用于长时越野导航。 | [#971](https://github.com/thinson/RS-PaperClaw/issues/971) |
| [20260726] Contrastive Parameter Disentanglement for Multi-modal Remote Sensing Image Generation | Zhang Yu, Zhao Wenda, Tang Haojun, Wang Haipeng | School of Information and Communication Engineering, Dalian University of Technology, Dalian, China ( | 对比参数解耦方法，提升多模态遥感图像生成质量。 | [#972](https://github.com/thinson/RS-PaperClaw/issues/972) |
| [20260726] Direction-adaptive Mamba: Spatial-Frequency Dual-Domain Collaborative Learning for PolSAR Image Classification | Shi Junfei, Cheng Yu, Zhang Haojia, Hua Wenqiang, Li Junhuai, Gong Maoguo | Xidian University | 方向自适应Mamba实现空间-频率双域协同极化SAR分类。 | [#973](https://github.com/thinson/RS-PaperClaw/issues/973) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| WGDnet: Wishart-guided Geometric-aware Deep Network for PolSAR Image Classification | [2607.23638v1](https://arxiv.org/abs/2607.23638v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 多模态与安全合规性成为无人机智能体研究新焦点
- 自监督与对比学习在遥感导航和图像生成中应用增多

---

Powered by OpenClaw🦞

---

# [20260725](./202607/20260725.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于SAR基础模型预训练、轻量化地物分割、高光谱融合边缘部署及SAR图像生成。SARATR-X-v2提出尺度感知结构预训练方法，PriSAR利用3D几何先验引导扩散模型生成可控SAR图像，轻量CNN在DeepGlobe上验证了高效分割潜力，高光谱融合在树莓派上实现优化部署。

## ✨ 今日亮点

- SARATR-X-v2提出尺度感知结构预训练，提升SAR基础模型性能。
- PriSAR利用3D几何先验引导扩散模型，实现参数可控SAR图像生成。
- 轻量CNN在DeepGlobe上验证了高效地物分割的可行性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260725] SARATR-X-v2: Scale-Aware Structural Pre-Training for SAR Foundation Models | Li Weijie, Song Yafei, Liu Yongxiang, Peng Bowen, Zhou Jie, Xia Jingyuan, Yang Wei, Liu Tianpeng, Liu Zhen, Liu Li | College of Electronic Science and Technology, National University of Defense Technology, Changsha, China ( | SARATR-X-v2提出尺度感知结构预训练方法，用于SAR基础模型。 | [#964](https://github.com/thinson/RS-PaperClaw/issues/964) |
| [20260725] Optimized Embedded Implementation of Hyperspectral-Multispectral Image Fusion on Raspberry Pi | Salah Eddine Brezini, Bekhelifi Okba, Mezouar Oussama, Chams Eddine Choucha, Boukhacheba Sarra, Fethi Abdelatif Dali | Intelligent Systems Research Intelligent Systems Research Intelligent Systems Research；Laboratory (Laresi) Laboratory (Laresi) Laboratory (Laresi)；University of Science and University of Science and University of Science and；Advanced Data Science and Intelligent Systems Research Intelligent Systems Research；Cognitive Applications Laboratory Laboratory (Laresi) Laboratory (Laresi) | 高光谱与多光谱图像融合算法在树莓派上实现优化嵌入式部署。 | [#965](https://github.com/thinson/RS-PaperClaw/issues/965) |
| [20260725] When Less Is More: A Controlled Benchmark of Lightweight CNNs for Satellite Land-Cover Segmentation on DeepGlobe | Atiq Ur Rehman, Joseph Michael Donovan | University of South Dakota, Vermillion, USA；of Economics & Decision Sciences, University of South Dakota, Vermillion, SD, USA | 轻量CNN在DeepGlobe卫星图像地物分割任务中表现高效。 | [#966](https://github.com/thinson/RS-PaperClaw/issues/966) |
| [20260725] PriSAR: 3D Geometric-Prior-Guided Diffusion for Parameter-Controlled SAR Image Generation | Zhang Fan, Wu Xuanting, Ma Fei, Yin Qiang, Hu Yuxin | College of Information Science and Technology, Beijing University of Chemical Technology, Beijing 100029, China；Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing 100190, China | PriSAR利用3D几何先验引导扩散模型生成参数可控SAR图像。 | [#967](https://github.com/thinson/RS-PaperClaw/issues/967) |

## 🔎 观察

- SAR基础模型预训练正从通用掩码建模向尺度感知结构提取演进。
- 边缘计算与轻量化模型成为遥感应用落地的重要趋势。

---

Powered by OpenClaw🦞

---

# [20260724](./202607/20260724.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦于红外多帧超分、高光谱特征提取及遥感多模态大模型后训练。红外超分领域提出新基准与轻量化状态空间模型；高光谱分类引入整体多变量分解方法；多模态大模型则通过能力差距驱动后训练实现场景专业化，三者均注重效率与实用性。

## ✨ 今日亮点

- 红外多帧超分新基准与轻量化模型发布
- 高光谱图像整体多变量分解特征提取方法
- 能力差距驱动的遥感多模态大模型后训练

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260724] IR275K: A Benchmark for Infrared Multi-Frame Super-Resolution Toward Efficient Remote Sensing | Deng Jie, Wang Heyang, Wang Changxin, Shen Junkai, Chen Hongyi, He Zhiping, Qi Hongxing, Zhang Xudong, Wang Jianyu | Hangzhou Institute for Advanced Study, Hangzhou；Shanghai Institute of Technical Physics of the Chinese Academy of Sciences, Shanghai；University of Chinese Academy of Sciences, Beijing | 提出IR275K红外多帧超分基准及轻量化状态空间模型 | [#960](https://github.com/thinson/RS-PaperClaw/issues/960) |
| [20260724] Efficient Spatial-Spectral Feature Extraction in Hyperspectral Images via Holistic Multivariance Decomposition | Tuna Süha | \.Istanbul Technical University, \.Istanbul 34469, Türkiye | 整体多变量分解高效提取高光谱空间-光谱特征 | [#961](https://github.com/thinson/RS-PaperClaw/issues/961) |
| [20260724] Filling Before Advancing: Capability-Gap-Driven Post-Training for Scenario-Specialized Remote Sensing MLLMs | Zong Yuheng, Wang Minghua, Zhao Xin, Zhan Zhi-Hui, Plaza Antonio, Jon Atli Benediktsson | Institute of Robotics and Automatic Information System (IRAIS), the Tianjin Key Laboratory of Intelligent Robotics；(tjKLIR), Nankai University, Tianjin 300071, China；Hyperspectral Computing Laboratory, Department of Technology of Computers and Communications, Escuela Politécnica；University of Extremadura, Cáceres, Spain；Faculty of Electrical and Computer Engineering, University of Iceland, Reykjavík, Iceland | 能力差距驱动后训练实现遥感多模态大模型场景专业化 | [#962](https://github.com/thinson/RS-PaperClaw/issues/962) |

## 🔎 观察

- 红外与高光谱领域均追求轻量化与高效特征提取
- 多模态大模型后训练正从通用向场景专业化演进

---

Powered by OpenClaw🦞

---
