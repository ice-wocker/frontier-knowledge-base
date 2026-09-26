# 复杂系统与网络科学

> 最后更新：2026-09-26 ｜ 领域：科学·复杂系统与网络科学 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

复杂系统研究由大量异质单元通过非线性相互作用组成的系统如何涌现出宏观有序行为，网络科学则以图、超图与多层网络为语言刻画结构—功能关系。两者在临界性、同步、传播动力学与复杂经济学等方向高度交汇，2025–2026 年的一个共同趋势是把长期停留在结构层面的指标与真实的网络动力学打通。

## 最新进展（2025–2026）

**结构指标与动力学的打通。** 深圳大学吴宗泽、王向荣团队联合西班牙萨拉戈萨大学 Yamir Moreno 在 Nature Communications 发表研究，首次严格证明"有效图阻"（effective graph resistance）在物理上等价于图扩散过程中的累计热耗散量，为这一沿用二十余年、此前仅停留在电网络类比层面的指标赋予了清晰的物理内涵（[复杂网络有效图阻的动力学解释和物理内涵揭示](https://kjb.szu.edu.cn/info/1143/21343.htm)）。

**中心性与关键节点识别。** 有工作基于线性化网络系统的 Green 函数提出多维动力学中心性框架，把节点重要性与其在网络动力学中的响应联系起来（[Multidimensional dynamical centrality from Green functions in complex networks](https://arxiv.org/html/2609.29197v1)）。关键节点识别方面，出现基于曲率进行多尺度结构收缩的方法，而 CycRank 则提出利用环结构优化既有方法的选点策略（[Curvature-Based Multiscale Structural Contraction for Identifying Key Nodes in Complex Networks](https://www.semanticscholar.org/paper/Curvature-Based-Multiscale-Structural-Contraction-Zhang-Qu/c25b755d4077b1ce6f21561f9f6fe3c0ee7ca083)）。

**高阶相互作用与同步。** 超图上的 Kuramoto 模型成为热点。有研究显示高阶相互作用对同步的影响是非单调的：在成对耦合基础上加入微弱的高阶耦合会增强同步，同步度在某个小而**非零**的高阶耦合强度处达到最大（[When higher-order interactions enhance synchronization: the case of the Kuramoto model](https://arxiv.org/html/2508.10992v3)）。另有工作推导了含任意阶超边的自适应 Kuramoto 模型的精确序参量动力学（[Emergent synchrony in oscillator networks with adaptive arbitrary-order interactions](https://arxiv.org/html/2511.06766)），并给出二元与三元相互作用共存时的自洽分析框架与临界耦合强度（[Self-consistent analysis of the Kuramoto model with higher-order interactions](https://arxiv.org/html/2605.24701v1)）。还有研究提出在有向超图上通过 Dirac 谱编程实现可编程的拓扑簇同步（[Topological cluster synchronization via Dirac spectral programming on directed hypergraphs](https://arxiv.org/html/2512.14729v1)）。

**自组织临界性。** 有研究揭示由液滴注入与随机融合驱动的自组织临界性，液滴尺寸在面积分数接近临界值时呈指数约 1.5 的幂律分布，其尺寸动力学由与聚集系统簇尺寸类似的 Smoluchowski 方程支配（[Self-organized criticality driven by droplet influx and random fusion](https://arxiv.org/html/2502.06236v1)）。在临界性与学习的交叉上，PNAS 论文提出神经网络学习可被视为由最大熵原理与互信息约束共同塑造的非平衡过程，从而产生重尾的参数更新分布（[Heavy-tailed update distributions arise from information-driven self-organization in nonequilibrium learning](https://www.pnas.org/doi/10.1073/pnas.2523012122)）。此外，eigen microstate 理论被用于刻画 Kuramoto 模型相位涨落的凝聚与临界性，其有限尺寸标度与平均场近似的临界指数一致（[Condensation and criticality of eigen microstates of phase fluctuations in Kuramoto model](https://cpb.iphy.ac.cn/EN/article/downloadArticleFile.do?attachType=PDF&id=127946)）。

**多层网络与传播动力学。** 有工作提出多尺度推断框架，以同时重建微观单纯形相互作用与宏观元种群组织，并指出结构可识别性由跨层传播耦合与网络异质性共同决定（[Multiscale Reconstruction of Multiplex Networks with Higher-Order Interactions](https://arxiv.org/html/2609.17354v1)）。在传染病建模中，有研究用位移追踪矩阵数据构建有向加权流动网络，以随机元种群 SEIR 模型模拟乌干达 Bundibugyo 埃博拉病毒的输入与扩散（[Network-based modelling of Bundibugyo Ebola virus disease importation and spread in Uganda using Displacement Tracking Matrix flow data](https://www.medrxiv.org/content/10.64898/2026.06.22.26356210v2.full)）；也有工作把 Graph Transformer 与元种群 SIR 模型结合进行多区域疫情预测（[Multi-region infectious disease prediction modeling based on spatio-temporal graph neural network and the dynamic model](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012738)），并以物理—信息—社会三层耦合网络推导基本再生数与疫情阈值（[Epidemic dynamics in physical-information-social multilayer networks](https://arxiv.org/html/2506.00104v1)）。PNAS 另有研究重建了两种呼吸道病毒在美国都市区之间的早期空间扩散，指出人类流动只能部分解释推断出的传播路径，随机过程带来相当大的不确定性（[Reconstructing the early spatial spread of pandemic respiratory viruses in the United States](https://www.pnas.org/doi/full/10.1073/pnas.2518051123)）。

**复杂经济学。** Santa Fe Institute（SFI）长期推动的基于主体建模（ABM）正进入经济主流：2025 年有 SFI 工作组报告讨论 LLM 与 ABM 结合用于政策级经济模拟（[Emergent Behaviour Across Disciplines](https://anthonywest.co.uk/research/emergent-behaviour-cross-domain/summary)）。SFI Press 出版的《The Economy as an Evolving Complex System IV》指出，ABM 已不再局限于理论，政策制定者与央行已在用它模拟经济在压力下的表现（[New Book: The Economy as an Evolving Complex System IV](https://www.sfipress.org/news/new-book-the-economy-as-an-evolving-complex-system-iv)）。

## 核心概念

- **网络结构与指标**：度分布、小世界、模块结构、介数中心性、有效图阻。
- **多层与高阶网络**：多层/多重网络、超图、单纯复形，用于建模组与多体相互作用。
- **网络动力学**：同步（Kuramoto 及高阶推广）、级联失效、渗流、传播（SI/SIR 及元种群模型）。
- **涌现与自组织**：自组织临界性、幂律与标度、临界慢化。
- **非线性动力学**：分岔、混沌、稳定性与吸引子。
- **复杂经济学**：异质主体、有限理性、非均衡演化、ABM 与政策模拟。

## 趋势与争议

1. **结构指标的动力学可解释化**：有效图阻、中心性等指标正被赋予基于扩散或响应函数的物理含义。
2. **高阶相互作用效应非单调**：微弱高阶耦合可能增强同步、过强则抑制，说明"更多连接总更好"的直觉不成立。
3. **ABM 的主流化**：其可信度依赖与 LLM、真实数据的结合，但校准、验证与可复现性仍是争论焦点。
4. **传播建模的预测力**：人类流动只能部分解释传播路径，随机性与数据质量带来显著不确定性。

## 参考来源

- [复杂网络有效图阻的动力学解释和物理内涵揭示（深圳大学）](https://kjb.szu.edu.cn/info/1143/21343.htm)
- [Multidimensional dynamical centrality from Green functions in complex networks](https://arxiv.org/html/2609.29197v1)
- [Curvature-Based Multiscale Structural Contraction for Identifying Key Nodes in Complex Networks](https://www.semanticscholar.org/paper/Curvature-Based-Multiscale-Structural-Contraction-Zhang-Qu/c25b755d4077b1ce6f21561f9f6fe3c0ee7ca083)
- [When higher-order interactions enhance synchronization: the case of the Kuramoto model](https://arxiv.org/html/2508.10992v3)
- [Emergent synchrony in oscillator networks with adaptive arbitrary-order interactions](https://arxiv.org/html/2511.06766)
- [Self-consistent analysis of the Kuramoto model with higher-order interactions](https://arxiv.org/html/2605.24701v1)
- [Topological cluster synchronization via Dirac spectral programming on directed hypergraphs](https://arxiv.org/html/2512.14729v1)
- [Self-organized criticality driven by droplet influx and random fusion](https://arxiv.org/html/2502.06236v1)
- [Heavy-tailed update distributions arise from information-driven self-organization in nonequilibrium learning（PNAS）](https://www.pnas.org/doi/10.1073/pnas.2523012122)
- [Condensation and criticality of eigen microstates of phase fluctuations in Kuramoto model](https://cpb.iphy.ac.cn/EN/article/downloadArticleFile.do?attachType=PDF&id=127946)
- [Multiscale Reconstruction of Multiplex Networks with Higher-Order Interactions](https://arxiv.org/html/2609.17354v1)
- [Network-based modelling of Bundibugyo Ebola virus disease importation and spread in Uganda](https://www.medrxiv.org/content/10.64898/2026.06.22.26356210v2.full)
- [Multi-region infectious disease prediction modeling based on spatio-temporal graph neural network and the dynamic model（PLOS Comp Biol）](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012738)
- [Epidemic dynamics in physical-information-social multilayer networks](https://arxiv.org/html/2506.00104v1)
- [Reconstructing the early spatial spread of pandemic respiratory viruses in the United States（PNAS）](https://www.pnas.org/doi/full/10.1073/pnas.2518051123)
- [Emergent Behaviour Across Disciplines](https://anthonywest.co.uk/research/emergent-behaviour-cross-domain/summary)
- [New Book: The Economy as an Evolving Complex System IV（SFI Press）](https://www.sfipress.org/news/new-book-the-economy-as-an-evolving-complex-system-iv)