# Daily Reports

最近三天日报（最新在前）：

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

# [20260723](./202607/20260723.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦于多模态与多任务融合，涵盖无人机单目深度估计、高光谱影像分类基准、大模型对抗攻击及显著目标检测。深度估计强调视角泛化，高光谱领域推出大规模基准数据集，同时大模型安全性与光谱-空间协同网络成为新热点。

## ✨ 今日亮点

- 无人机单目深度估计实现任意高度、俯仰、翻滚及视场角泛化
- 发布大规模高空间分辨率高光谱影像分类基准数据集
- 提出针对遥感大语言模型的可迁移定向对抗攻击方法

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260723] DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV | Ling Tong, Diao Wenhui, Feng Yingchao, Bi Hanbo, Hou Zhongyan, Sun Xian | Accordingly, research on low-altitude remote sensing imagery；mation Research Institute, Chinese Academy of Sciences, Beijing 100190；China, also with the School of Electronic, Electrical and Communication；Engineering, University of Chinese Academy of Sciences, Beijing 100190；China, also with the University of Chinese Academy of Sciences, Beijing；China, and also with the Key Laboratory of Target Cognition；stitute, Chinese Academy of Sciences, Beijing 100190, China ( | 提出DAPM方法，实现无人机任意视角下的单目深度估计 | [#955](https://github.com/thinson/RS-PaperClaw/issues/955) |
| [20260723] HyperImageNet: A Large-Scale High-Spatial Resolution Hyperspectral Imagery Classification Benchmark | Zeng Chuguang, Li Jingtao, Liu Yinhe, Zhong Yanfei | Wuhan University Wuhan University Wuhan University Wuhan University | HyperImageNet发布大规模高空间分辨率高光谱分类基准 | [#956](https://github.com/thinson/RS-PaperClaw/issues/956) |
| [20260723] GeoThreat: Transferable Targeted Adversarial Attacks on Large Vision-Language Models for Remote Sensing Image Interpretation | Fu Yimin, Bai Yuefeng, Pan Baicheng, Liu Zhunga, Michael K. Ng | Department of Mathematics, Hong Kong Baptist University, Hong Kong, China (；School of Automation, Northwestern Polytechnical University, Xi'an,, China ( | GeoThreat实现针对遥感大模型的可迁移定向对抗攻击 | [#957](https://github.com/thinson/RS-PaperClaw/issues/957) |
| [20260723] Spectral-Spatial Synergistic Guided Network for Hyperspectral Salient Object Detection | Peng Yanyan, Xu Tingfa, Xiao Yao, Liu Peifu, Bai Shuyan, Xu Fengxiang, Li Jianan | Chongqing Innovation Center, Beijing Institute of Technology, Chongqing, China；School of Optics and Photonics, Beijing Institute of Technology, Beijing, China (；School of Optics and Photonics, Beijing Institute of Technology, Beijing, China；the Key Laboratory of Photoelectronic Imaging Technology and System, Ministry of Education of China, Beijing, China ( | 提出光谱-空间协同引导网络用于高光谱显著目标检测 | [#958](https://github.com/thinson/RS-PaperClaw/issues/958) |

## 🔎 观察

- 高光谱遥感从分类向显著目标检测等细粒度任务拓展
- 大模型安全性与视角泛化能力成为遥感AI研究新焦点

---

Powered by OpenClaw🦞

---
