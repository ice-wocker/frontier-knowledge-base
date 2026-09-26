# 计算科学与仿真

> 最后更新：2026-09-26 ｜ 领域：科学·计算科学与仿真 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

计算科学以数值方法、算法与高性能计算（HPC）求解无法解析处理的数学模型，覆盖分子动力学、计算流体力学（CFD）、电子结构计算、数字孪生等方向。2025–2026 年最显著的趋势是"AI 与物理模型融合"：机器学习势函数、神经算子与代理模型被引入传统求解流程，同时 E 级（exascale）超算为大规模仿真提供了算力底座。

## 最新进展（2025–2026）

**E 级超算与算力格局。** TOP500 2025 年 11 月榜单显示，劳伦斯利弗莫尔国家实验室（LLNL）的 El Capitan 以 HPL 实测 1.809 EFlop/s 继续位居第一，并在 HPCG 榜单以 17.41 PFlop/s 居首；其同门系统 Tuolumne 以 208.1 PFlop/s 位列第 12（[El Capitan retains title as world's fastest supercomputer in latest Top500](https://www.llnl.gov/article/53596/el-capitan-retains-title-worlds-fastest-supercomputer-latest-top500-list)、[TOP500 November 2025](https://www.top500.org/lists/top500/2025/11/)）。欧洲首台 E 级系统 JUPITER Booster 以 1.23 EFlop/s 位列第四（[全球新一期TOP500超算公布 欧洲首台E级超算破局](https://ecas.cas.cn/xxkw/kbcd/201115_148603/ml/xxhjsyjcss/202512/t20251229_5094408.html)）。

**机器学习原子间势（MLIP）与分子动力学。** Allegro-FM 面向 E 级分子动力学，覆盖元素周期表 89 种元素，可用于结构关联、反应动力学、力学强度、断裂与固液溶解等任务，并展现出一定的涌现能力（[Allegro-FM: Toward an Equivariant Foundation Model for Exascale Molecular Dynamics Simulations](https://ar25.alcf.anl.gov/science/highlights/nakano)）。有工作把十亿参数级通用 MLIP 的训练部署到两台 E 级超算上，单精度峰值达 1.2/1.0 EFLOPS（理论峰值的 24%/35.5%），并行效率超 90%，把训练从数周压缩到数小时（[Breaking the Training Barrier of Billion-Parameter Universal Machine Learning Interatomic Potentials](https://arxiv.org/html/2604.15821)）。DPA4C 报告单张 H20 GPU 可同时模拟 1405 万原子，在 1024 张 V100 上扩展到 20.48 亿原子并保持 80% 以上效率（[10 Million Atoms on a Single GPU, 2.048 Billion Atoms on a Thousand GPUs](https://blogs.deepmodeling.com/DPA_2026_08_23/)）。另有研究通过压缩特征向量与中间张量的显存占用，把 MLIP 的 HBM 足迹降至现有方案的 3% 以下，以解锁多组分块体材料模拟（[Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential](https://arxiv.org/html/2608.16329v1)）。

**神经代理模型与算子。** SMART 用 Transformer 从几何点云直接预测气动物理量，不依赖仿真网格（[SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model](https://arxiv.org/html/2601.18707)）。PhysGuard 利用仿真数据上的经验 Fisher 信息矩阵识别"物理关键"参数方向，从而约束微调以保留物理结构，服务于神经算子的仿真到现实迁移（[PhysGuard: Fisher-Guided Gradient Projection for Sim-to-Real Neural PDE Surrogates](https://arxiv.org/html/2606.16602v1)）。针对受约束多物理场，cellular sheaf 神经算子被用于结构保持的代理建模，改善滚动行为、散度控制与谱误差（[Cellular Sheaf Neural Operators for Structure-Preserving Surrogate Modeling of Constrained PDEs](https://www.semanticscholar.org/paper/Cellular-Sheaf-Neural-Operators-for-Surrogate-of-Shikhman-Gilbertie/04030509aa65c7649b32b464270d135838af56e1)）。此外，"间接神经校正器"主张把学习到的校正项嵌入控制方程而非直接更新状态，以降低时间步长与 Lipschitz 常数带来的误差放大（[Indirect Neural Corrector](https://ge.in.tum.de/author/i15geadmin/)）。

**CFD 与数字孪生。** 出现面向非 CFD 专业的开源、云原生数字孪生框架，支持在线配置与执行 CFD 仿真，服务规划师、建筑师等终端用户（[AN OPEN-SOURCE FRAMEWORK FOR CFD-BASED DIGITAL TWINS: A CASE STUDY ON STORM WATER MANAGEMENT](https://research.utu.fi/converis/getfile?id=506414573&portal=true&v=1)）。NIST 基于高速吸收成像测量构建了原子层沉积（ALD）工艺中 MoCl5 瞬态输运的三维时变 CFD 数字孪生（[A CFD-Based Digital Twin Framework for Transient MoCl5 Transport in an Experimental Atomic Layer Deposition Process](https://www.nist.gov/publications/cfd-based-digital-twin-framework-transient-mocl5-transport-experimental-atomic-layer)）。商用侧，Cadence、西门子、新思与达索等正借助 CUDA-X 与 Blackwell GPU 把求解器加速一个数量级，并把实时结果集成进数字孪生（[计算流体动力学 (CFD) 仿真](https://www.nvidia.cn/use-cases/computational-fluid-dynamics-simulation/)）。

**电子结构计算。** DeePHF 结合神经网络与量子力学描述符，在保持 DFT 效率的同时逼近 CCSD(T) 精度（[A Deep Learning-Augmented Density Functional Framework for Reaction Modeling with Chemical Accuracy](https://pmc.ncbi.nlm.nih.gov/articles/PMC12381711/pdf/au5c00541.pdf)）。机器学习哈密顿量预测可达毫电子伏级精度（如 DeepH-E3 在石墨烯约 0.4 meV、HamGNN 在 QM9 约 1.5 meV），相较传统 DFT 加速 3–5 个数量级（[机器学习赋能电子结构计算: 进展、挑战与展望](https://wulixb.iphy.ac.cn/article/doi/10.7498/aps.75.20251253)）。NN-xTB 在 GMTKN55 基准上取得 4 kcal/mol 的 WTMAD-2，以接近半经验方法的成本达到类 DFT 精度（[Machine-Learning Adaptivity, DFT-Level Accuracy, and Semi-Empirical Quantum-Chemistry Speed with Neural-Network Extended Tight-Binding](https://chemrxiv.org/doi/pdf/10.26434/chemrxiv-2025-chlcc-v3)）。也有工作面向分子、固体与反应表面训练机器学习的交换—关联泛函（[Machine-learned exchange-correlation functionals for molecules, solids, and reactive surfaces](https://arxiv.org/html/2608.21525v1)）。

## 核心技术与关键概念

- **数值方法**：有限差分、有限元、有限体积、谱方法；离散化、稳定性与收敛性分析。
- **HPC 与并行**：MPI/OpenMP、GPU 加速、混合精度、通信与负载均衡；Rmax/Rpeak 与 HPCG 等基准口径。
- **多尺度与耦合**：从电子结构到连续介质的跨尺度方法、多物理场耦合。
- **代理模型与不确定性量化（UQ）**：神经算子、物理信息神经网络、仿真到现实的迁移。
- **数字孪生**：以观测锚定的物理模型 + 实时数据同化，服务于设计、运维与"假设"情景。

## 趋势与争议

1. **物理一致性 vs 数据拟合**：守恒律、长期滚动稳定性与纯数据驱动的精度之间存在张力，需专门的正则化或结构约束。
2. **泛化边界与可验证性**：AI 代理模型在训练分布外的可靠性缺乏统一评估标准。
3. **算力与能耗成本**：E 级规模的训练与仿真带来显著能耗与资源门槛，大模型与小足迹方案的路线之争仍在继续。

## 参考来源

- [El Capitan retains title as world's fastest supercomputer in latest Top500（LLNL）](https://www.llnl.gov/article/53596/el-capitan-retains-title-worlds-fastest-supercomputer-latest-top500-list)
- [TOP500 November 2025](https://www.top500.org/lists/top500/2025/11/)
- [全球新一期TOP500超算公布 欧洲首台E级超算破局](https://ecas.cas.cn/xxkw/kbcd/201115_148603/ml/xxhjsyjcss/202512/t20251229_5094408.html)
- [Allegro-FM: Toward an Equivariant Foundation Model for Exascale Molecular Dynamics Simulations（ALCF）](https://ar25.alcf.anl.gov/science/highlights/nakano)
- [Breaking the Training Barrier of Billion-Parameter Universal Machine Learning Interatomic Potentials](https://arxiv.org/html/2604.15821)
- [10 Million Atoms on a Single GPU, 2.048 Billion Atoms on a Thousand GPUs（DPA4C）](https://blogs.deepmodeling.com/DPA_2026_08_23/)
- [Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential](https://arxiv.org/html/2608.16329v1)
- [SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model](https://arxiv.org/html/2601.18707)
- [PhysGuard: Fisher-Guided Gradient Projection for Sim-to-Real Neural PDE Surrogates](https://arxiv.org/html/2606.16602v1)
- [Cellular Sheaf Neural Operators for Structure-Preserving Surrogate Modeling of Constrained PDEs](https://www.semanticscholar.org/paper/Cellular-Sheaf-Neural-Operators-for-Surrogate-of-Shikhman-Gilbertie/04030509aa65c7649b32b464270d135838af56e1)
- [Indirect Neural Corrector（TU Munich）](https://ge.in.tum.de/author/i15geadmin/)
- [AN OPEN-SOURCE FRAMEWORK FOR CFD-BASED DIGITAL TWINS](https://research.utu.fi/converis/getfile?id=506414573&portal=true&v=1)
- [A CFD-Based Digital Twin Framework for Transient MoCl5 Transport in an Experimental Atomic Layer Deposition Process（NIST）](https://www.nist.gov/publications/cfd-based-digital-twin-framework-transient-mocl5-transport-experimental-atomic-layer)
- [计算流体动力学 (CFD) 仿真（NVIDIA）](https://www.nvidia.cn/use-cases/computational-fluid-dynamics-simulation/)
- [A Deep Learning-Augmented Density Functional Framework for Reaction Modeling with Chemical Accuracy（DeePHF）](https://pmc.ncbi.nlm.nih.gov/articles/PMC12381711/pdf/au5c00541.pdf)
- [机器学习赋能电子结构计算: 进展、挑战与展望](https://wulixb.iphy.ac.cn/article/doi/10.7498/aps.75.20251253)
- [Machine-Learning Adaptivity, DFT-Level Accuracy, and Semi-Empirical Quantum-Chemistry Speed with Neural-Network Extended Tight-Binding（NN-xTB）](https://chemrxiv.org/doi/pdf/10.26434/chemrxiv-2025-chlcc-v3)
- [Machine-learned exchange-correlation functionals for molecules, solids, and reactive surfaces](https://arxiv.org/html/2608.21525v1)