# Daily Reports

最近三天日报（最新在前）：

# [20261110](./202611/20261110.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 20 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日论文聚焦SLAM与定位系统的鲁棒性与精度提升，涵盖3D高斯泼溅、毫米波雷达和视觉惯性里程计三个方向。研究趋势显示，多模态融合与在线校准成为提升系统适应性的关键手段，同时针对非理想参考系和稀疏角度地图的检测问题受到关注。整体工作强调在复杂场景下的实时性与可靠性，为遥感与自主导航应用提供技术支撑。

## ✨ 今日亮点

- 3D高斯泼溅SLAM引入全局外参校准与在线重定位，提升建图一致性。
- 毫米波雷达SLAM利用非相干积分角度图进行CFAR检测，增强稀疏场景感知。
- 视觉惯性里程计扩展至非惯性参考系，提升跨参考系定位适应性。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261110] GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM | Yang Yuchen, Ding Ming, Wu Xinyu, Wang Hesheng | Department of Software Engineering, Nanchang University, Nanchang, China | 提出GEMOR-GS，通过全局外参校准优化3D高斯泼溅SLAM建图，并实现在线重定位。 | [#251](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/251) |
| [20261110] CFAR Detection on Non-Coherently Integrated Angular Maps for mmWave Radio SLAM | Tosi Paolo, Kaltiokallio Ossi, Henninger Marcus, Mandelli Silvio, Valkama Mikko | Karlsruhe Institute of Technology (KIT)；Tampere University, Tampere, Finland | 针对毫米波雷达SLAM，在非相干积分角度图上应用CFAR检测，改善稀疏角度地图的鲁棒性。 | [#252](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/252) |
| [20261110] NIF-VIO: Visual--Inertial Odometry Across Inertial and Non-Inertial Reference Frames | Shu Zichao, Li Lijun, Li Zhuochen, Chen Zetao, Wang Jianyu | the Shanghai Institute of Technical Physics, Chinese Academy of Sciences, Shanghai, China；University of Chinese Academy of Sciences, Beijing, China (；the Advanced Display and Sensing Research Center, Yongjiang Laboratory, Ningbo, China；University of Nottingham Ningbo China, Ningbo, China (；the Advanced Display and Sensing Research Center, Yongjiang Laboratory, Ningbo, China ( | 提出NIF-VIO，使视觉惯性里程计能够跨惯性与非惯性参考系工作，扩展应用场景。 | [#253](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/253) |

## 🔎 观察

- 3D高斯泼溅SLAM正从离线建图转向在线重定位，外参校准成为提升长期一致性的必要环节。
- 毫米波雷达SLAM的检测方法开始借鉴雷达信号处理中的CFAR，表明跨领域方法迁移具有潜力。

---

Powered by OpenClaw🦞

---

# [20261109](./202611/20261109.md)
<!-- UAV_GEONAV_PAPERCLAW_REPORT -->

## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日论文聚焦视觉SLAM与跨视角地理定位的鲁棒性提升。V3DSAM与DPGS-SLAM分别从语义-几何回环验证和扩散先验角度增强动态场景下的建图一致性；鱼眼视觉里程计通过球面光束法平差引导无监督深度学习解决尺度问题。跨视角序列定位引入注意力引导特征融合与混合空间度量学习。此外，无人机SAR成像与航空重建诊断评估也拓展了遥感几何处理的应用边界。

## ✨ 今日亮点

- V3DSAM提出语义-几何回环验证与几何锚定持久实例建图，提升前馈稠密SLAM一致性。
- DPGS-SLAM利用扩散先验与来源感知机制，增强动态场景单目高斯泼溅SLAM鲁棒性。
- 跨视角序列定位结合注意力引导特征融合与混合空间度量学习，提升检索与配准精度。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261109] V3DSAM: Semantic-Geometric Loop Verification and Geometry-Anchored Persistent Instance Mapping for Feed-Forward Dense SLAM | Ye Maolin, Zhao Dongqing, Li Linyang, Xue Shuai, Liu Yuan, Wang Yiyuan, Li Wen | Information Engineering University | V3DSAM为前馈稠密SLAM引入语义-几何回环验证与几何锚定持久实例建图，增强长期一致性。 | [#244](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/244) |
| [20261109] Attention-Guided Sequence Feature Fusion and Mixed-Space Metric Learning for Cross-View Image Sequence Geo-Localization | Wu Nan, Yang Chunfang, Li Jiangshan, Luo Xiangyang | Information Engineering University, Zhengzhou,, China, and the Henan Key Laboratory of Cyberspace Situation Awareness, Zhengzhou,, China. (；College of Electronic Science and Technology, National University of Defense Technology, Changsha, China. ( | 该文提出注意力引导序列特征融合与混合空间度量学习，用于跨视角图像序列地理定位。 | [#245](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/245) |
| [20261109] DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing | Luo Yifan, Matsumaru Takafumi, Dutta Vibekananda, He Xin | the Graduate School of Information, Production and Systems, Waseda University, Kitakyushu, Fukuoka 808-, Japan (；the Faculty of Mechatronics, Warsaw University of Technology, 00-661 Warsaw, Poland ( | DPGS-SLAM结合扩散先验与来源感知，实现动态视觉感知下的单目高斯泼溅SLAM。 | [#246](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/246) |
| [20261109] Scale-Consistent Monocular Fisheye Visual Odometry via Spherical Bundle Adjustment-Guided Unsupervised Depth Learning | Luo Wanhui, Zhao Hongbo, Zhou Yi, Chen Qijun, Nie Yiming, Fan Rui | Department of Control Science \& Engineering, the College of Electronic \& Information Engineering, Tongji University, Shanghai, China (；the Shanghai Research Institute for Intelligent Autonomous Systems, Tongji University, Shanghai, China (；School of Artificial Intelligence and Robotics, Hunan University,, Changsha, China (；the Unmanned Systems Technology Research Center, Defense Innovation Institute, Academy of Military Science, Beijing, China ( | 该文通过球面光束法平差引导无监督深度学习，实现尺度一致的单目鱼眼视觉里程计。 | [#247](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/247) |
| [20261109] Bistatic UAV-Based 3D SAR Imaging Using Integrated Sensing and Communications Transceivers | Sneh Akanksha, Ayyagari Krishna, Nawani Vivaswan, Shobha Sundar Ram | the Indraprastha Institute of Information Technology, Delhi, New Delhi India；University College London, United Kingdom | 该文研究基于集成感知与通信收发机的双基地无人机三维SAR成像方法。 | [#248](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/248) |
| [20261109] GeoPilot: Diagnosis-Guided Interventions and Geometric Evaluation for Aerial Reconstruction | Yin Pengyu, Pan Jie, Tan Junxiang, Fu Mengqi, Cheng Kun, Liu Yifan | the Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；School of Electronic Engineering, reference support, and artifact identities; it does not introduce a Beijing University of Posts and Telecommunications, Beijing, China ( | GeoPilot提出诊断引导干预与几何评估框架，用于航空重建质量分析与优化。 | [#249](https://github.com/Idea-in-Dream/UAV-GeoNav-PaperClaw/issues/249) |

## 🔎 观察

- SLAM研究正从单一几何约束转向语义-几何联合验证与生成先验融合，以应对动态与稀疏场景。
- 跨视角定位与航空重建均强调序列特征融合与诊断评估，表明遥感几何处理更注重可解释性与鲁棒性。

---

Powered by OpenClaw🦞

---

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
