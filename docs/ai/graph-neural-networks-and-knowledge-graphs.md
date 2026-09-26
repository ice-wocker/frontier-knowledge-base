# 图学习与知识图谱

> 最后更新：2026-09-26 ｜ 领域：AI·生成与多模态 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

图学习（Graph Learning）以图神经网络（GNN）与图 Transformer 为核心，处理节点、边与整图的表示学习；知识图谱（Knowledge Graph，KG）则以实体—关系—实体三元组刻画结构化知识。2025–2026 年最活跃的交汇点是 **GraphRAG**：用 LLM 从非结构化文本抽取实体与关系构建知识图谱，再以图结构增强检索与推理，缓解传统向量 RAG 的结构信息缺失与 token 低效问题。同时，图基础模型（Graph Foundation Model，GFM）成为研究热点，但其相对调优良好的 GNN 是否具备普遍优势仍存争议。代表性新方向包括以强化学习驱动 Agent 化的 GraphRAG（Graph-R1）、以 GNN 引导跨分块图增强（CrossAug），以及多模态知识图谱抽取（MegaRAG）（[Graph-R1](https://en.papernotes.org/ICML2026/information_retrieval/graph-r1_towards_agentic_graphrag_framework_via_end-to-end_reinforcement_learnin/)、[CrossAug](https://arxiv.org/html/2605.28004)、[MegaRAG](https://en.papernotes.org/ACL2026/graph_learning/)）。

## 最新进展（2025–2026）

- **GraphRAG 走向强化学习与 Agent 化**：Graph-R1（ICML 2026）把 GraphRAG 重构为端到端强化学习框架，由「知识超图环境 + 多轮 think–query–retrieve–answer 智能体 + 结果导向奖励」构成（[Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning](https://en.papernotes.org/ICML2026/information_retrieval/graph-r1_towards_agentic_graphrag_framework_via_end-to-end_reinforcement_learnin/)）。
- **GNN 回到 GraphRAG 管线核心**：CrossAug 提出以 GNN 引导的跨分块图增强方法，用自监督图损坏模块定位分块局部抽取失败的位置，并据此补全关系结构（[Beyond Chunk-Local Extraction: Cross-Chunk Graph Augmentation for GraphRAG](https://arxiv.org/html/2605.28004)）。剑桥的 GraphNeuralRAG 报告探讨把 GNN 置于 GraphRAG 管线核心的机遇与挑战，覆盖多跳问答与扰动建模（[GraphNeuralRAG](https://www.cst.cam.ac.uk/seminars/list/245977)）。
- **可解释性**：Ex-GraphRAG 用多变量图神经加性网络（M-GNAN）替换 GNN 编码器，对编码器输出做跨节点与特征组的精确分解，从而审计证据路由，并在 STaRK-Prime 上匹配黑盒性能（[Ex-GraphRAG: Interpretable Evidence Routing for Graph-Augmented LLMs](https://arxiv.org/html/2605.21994)）。
- **多模态知识图谱**：MegaRAG（ACL 2026）用多模态大模型（MLLM）对长文档逐页并行抽取实体关系，合并为多模态知识图谱（MMKG），并以子图引导的精修补全跨模态、跨页关系，配合双路径检索与两阶段答案生成，报告称显著优于 GraphRAG/LightRAG/VisRAG（[Graph Learning（ACL 2026）](https://en.papernotes.org/ACL2026/graph_learning/)）。
- **多模态图基模型基准**：有工作提出首个系统化形式化多模态图学习范式的基准，涵盖 19 个多模态数据集、7 个应用域、8 种模拟策略、6 类下游任务与 57 个实现于模块化 API 的 SOTA 方法（[Toward Federated Multimodal Graph Foundation Models](https://www.semanticscholar.org/paper/Toward-Federated-Multimodal-Graph-Foundation-A-Li-Fu/b7195e171c64d69cf851266d4a53a0f6d02ae32a)）。
- **图基础模型（GFM）**：一项对 9 个近期 GFM 在节点属性预测任务上的公平复评发现，其中只有基于 Prior-data Fitted Networks 范式的最新模型能超过调优良好的 GNN 基线，但推理成本更高（[A Fair Evaluation of Graph Foundation Models for Node Property Prediction](https://arxiv.org/html/2606.24509)）。此外出现面向图数据的「通用基础模型」尝试，并在生物网络（如 SagePPI、ogbn-proteins、StringGO、Fold-PPI）上评测（[Toward a universal foundation model for graph-structured data](https://arxiv.org/html/2604.06391v1)）；Structure-Centric GFM（SCGFM）用几何基与 Gromov–Wasserstein 距离对齐异构图拓扑（[Structure-Centric Graph Foundation Model via Geometric Bases](https://openreview.net/forum?id=iMrOO18AoP)）；RAG-GFM 则以检索增强缓解图基础模型的内存瓶颈，用双视角对齐与上下文增强在五个基准上优于 13 个基线（[Overcoming In-Memory Bottlenecks in Graph Foundation Models via Retrieval-Augmented Generation](https://arxiv.org/html/2601.15124v1)）。

## 核心技术与关键概念

- **GraphRAG**：Microsoft Research 于 2024 年提出，用 LLM 从非结构化文本抽取实体、关系与事件构建知识图谱，并利用社区聚类生成多层知识摘要来增强 LLM（[GraphRAG 实践](https://developer.cloud.tencent.com/article/2713121)）。
- **知识图谱 + 多跳推理**：GraphRAG 直接遍历图的节点和边，为查询汇集事实及其关系网络，实现结构化的多跳推理，提供经过整理的事实而非简单文档堆叠（[Knowledge Graphs Meet LLMs: The Enterprise Reasoning Stack](https://aiconference.london/knowledge-graphs-meet-llms-the-enterprise-reasoning-stack-20260917-07)）。
- **本体工程**：企业级图落地通常遵循五层架构——数据摄取与质量保证、领域本体工程、知识图谱构建与填充、GraphRAG 增强、下游应用使能（[A Five-Layer Reference Architecture for First-Party Enterprise Knowledge Graphs](https://media.sciltp.com/articles/2608004839/2608004839.pdf)）。
- **图基与拓扑对齐**：面向 GFM 的工作用几何基、Gromov–Wasserstein 距离与结构感知特征重编码来统一异构拓扑与不兼容特征维度（[SCGFM](https://openreview.net/forum?id=iMrOO18AoP)）。
- **应用：药物与生物**：GNN 在计算药物发现中被用于分子生成、分子性质预测与药物—药物相互作用预测，以分子结构图建模与靶点结合（[Recent Developments in GNNs for Drug Discovery](https://arxiv.org/html/2506.01302v1)）。有综述指出 GNN 已在分子性质预测、药物重定位、毒性评估与相互作用分析上取得突破，并以生成式 GNN 增强虚拟筛选与新分子设计（[Graph neural networks driven acceleration in drug discovery](https://pmc.ncbi.nlm.nih.gov/articles/PMC12750157/)）。
- **基于结构的推理**：借助 AlphaFold 预测结构，GNN 可进行结构导向的机器学习；例如有工作以 AlphaFold 预测结构为输入、用 GNN 处理结构信息来预测 PROTAC 介导的蛋白降解性（[Structure-Aware Prediction of PROTAC-Mediated Protein Degradability](https://arxiv.org/html/2606.04021v1)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- Microsoft Research：GraphRAG 方法。
- 学术前沿：Graph-R1（ICML 2026）、CrossAug、Ex-GraphRAG、MegaRAG（ACL 2026）、GraphNeuralRAG 等（见参考来源）。
- 企业实践：面向制造、临床与客户体验等领域的第一方企业知识图谱参考架构（[A Five-Layer Reference Architecture](https://media.sciltp.com/articles/2608004839/2608004839.pdf)）。
- 生物医药：GNN 在分子性质预测、分子生成、药物重定位与相互作用分析上形成应用集群（[Graph neural networks driven acceleration in drug discovery](https://pmc.ncbi.nlm.nih.gov/articles/PMC12750157/)）。

## 关键数据与评测结果（附来源）

- 有厂商博客称 GraphRAG 在企业领域达 80% 准确率、而传统向量 RAG 为 51%，并称在企业基准上有 3.4 倍提升（[Knowledge Graphs for Enterprise AI — Replacing RAG with Structured Reasoning](https://stage.trantorinc.com/blog/knowledge-graphs-enterprise-ai)）——该数据来自商业博客，仅作转述。
- GFM 复评：9 个 GFM 中仅 PFN 范式的最新模型在节点属性预测上优于调优 GNN，但推理成本更高（[A Fair Evaluation of Graph Foundation Models](https://arxiv.org/html/2606.24509)）。
- RAG-GFM：在五个基准图数据集的跨域节点与图分类上优于 13 个 SOTA 基线（[RAG-GFM](https://arxiv.org/html/2601.15124v1)）。
- 在生物医药方向，GNN 已被广泛用于分子性质预测、分子生成与药物—药物相互作用预测（[Recent Developments in GNNs for Drug Discovery](https://arxiv.org/html/2506.01302v1)），并借助 AlphaFold 预测结构实现规模化结构导向的机器学习（[Structure-Aware Prediction of PROTAC-Mediated Protein Degradability via Graph Neural Networks](https://arxiv.org/html/2606.04021v1)）。

## 趋势与争议

- **GraphRAG vs 向量 RAG**：图结构增强在可解释性与多跳推理上具备优势，但也带来图谱构建成本与本体维护负担；部分「高提升」数据来自厂商自述，需谨慎对待（[Knowledge Graphs for Enterprise AI](https://stage.trantorinc.com/blog/knowledge-graphs-enterprise-ai)）。
- **GFM 是否必要**：公平复评显示，多数图基础模型未必优于调优良好的领域 GNN，且推理开销更大，说明「基础模型化」在图领域尚无定论（[A Fair Evaluation of Graph Foundation Models](https://arxiv.org/html/2606.24509)）。
- **分块抽取的固有缺陷**：GraphRAG 的实体关系抽取常在分块边界处失败，GNN 引导的跨分块增强是对此的直接回应（[Cross-Chunk Graph Augmentation for GraphRAG](https://arxiv.org/html/2605.28004)）。
- **可解释性与审计**：随着 GraphRAG 用于企业关键场景，证据路由的可审计性成为新焦点（[Ex-GraphRAG](https://arxiv.org/html/2605.21994)）。

## 参考来源

- [Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning（ICML 2026）](https://en.papernotes.org/ICML2026/information_retrieval/graph-r1_towards_agentic_graphrag_framework_via_end-to-end_reinforcement_learnin/)
- [Beyond Chunk-Local Extraction: Cross-Chunk Graph Augmentation for GraphRAG](https://arxiv.org/html/2605.28004)
- [Ex-GraphRAG: Interpretable Evidence Routing for Graph-Augmented LLMs](https://arxiv.org/html/2605.21994)
- [GraphNeuralRAG: On the Opportunities and Challenges of GNNs for GraphRAG](https://www.cst.cam.ac.uk/seminars/list/245977)
- [Graph Learning（ACL 2026，MegaRAG）](https://en.papernotes.org/ACL2026/graph_learning/)
- [A Fair Evaluation of Graph Foundation Models for Node Property Prediction](https://arxiv.org/html/2606.24509)
- [Toward a universal foundation model for graph-structured data](https://arxiv.org/html/2604.06391v1)
- [Toward Federated Multimodal Graph Foundation Models](https://www.semanticscholar.org/paper/Toward-Federated-Multimodal-Graph-Foundation-A-Li-Fu/b7195e171c64d69cf851266d4a53a0f6d02ae32a)
- [Structure-Centric Graph Foundation Model via Geometric Bases](https://openreview.net/forum?id=iMrOO18AoP)
- [Overcoming In-Memory Bottlenecks in Graph Foundation Models via Retrieval-Augmented Generation](https://arxiv.org/html/2601.15124v1)
- [GraphRAG 实践：企业知识库从文本检索到知识图谱推理的架构升级路径](https://developer.cloud.tencent.com/article/2713121)
- [Knowledge Graphs Meet LLMs: The Enterprise Reasoning Stack](https://aiconference.london/knowledge-graphs-meet-llms-the-enterprise-reasoning-stack-20260917-07)
- [A Five-Layer Reference Architecture for First-Party Enterprise Knowledge Graphs](https://media.sciltp.com/articles/2608004839/2608004839.pdf)
- [Knowledge Graphs for Enterprise AI — Replacing RAG with Structured Reasoning](https://stage.trantorinc.com/blog/knowledge-graphs-enterprise-ai)
- [Recent Developments in GNNs for Drug Discovery](https://arxiv.org/html/2506.01302v1)
- [Graph neural networks driven acceleration in drug discovery](https://pmc.ncbi.nlm.nih.gov/articles/PMC12750157/)
- [Structure-Aware Prediction of PROTAC-Mediated Protein Degradability via Graph Neural Networks](https://arxiv.org/html/2606.04021v1)