# 无人机定位论文标签 Prompt

根据论文标题和摘要选择标签。只允许从下列标签中选择：

UAV-Satellite, Orthophoto-Registration, DSM-DEM-TDOM, 3D-Map-Registration, 3DGS-NeRF, Map-Aided-VIO, GNSS-Denied, Cross-View-Retrieval, Fine-Registration, Target-Geolocation, Thermal-Localization, Dataset-Benchmark, Code-Available, Reproducible

规则：

1. 只输出逗号分隔的标签，不要解释；
2. 仅在标题或摘要有直接证据时选择；
3. 最多选择 6 个标签；
4. 无法判断时输出空字符串。

标题：{title}

摘要：{abstract}
