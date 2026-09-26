# 检索深入：稀疏、稠密、混合检索与向量搜索（Retrieval & Vector Search）

> 最后更新：2026-09-26 ｜ 领域：AI·提示、Agent 与应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

现代检索栈（尤其是 RAG 场景）通常由三层构成：候选召回（稀疏词法检索、稠密语义检索或两者混合）、重排序（reranking）与向量索引（ANN）。TREC RAG 2025 的参赛报告把混合检索系统描述为"融合稀疏检索、稠密语义匹配与交叉编码器重排"，并指出该组合在多数指标上取得最佳表现（[NITATREC at TREC RAG 2025](https://trec.nist.gov/pubs/trec34/papers/NIT%20Agartala.rag.pdf)）。一项面向文本—表格文档的基准研究也给出相同的工程结论：以混合检索（BM25 + 稠密，RRF 融合）为基线，加交叉编码器重排带来最大单次质量提升，再在索引时加入 contextual retrieval 可获得稳定但中等的增益（[From BM25 to Corrective RAG](https://arxiv.org/pdf/2604.01733)）。

## 最新进展（2025–2026）

**混合检索成为默认基线**。企业内网结构化数据的研究采用 all-mpnet-base-v2 稠密检索与 BM25 稀疏检索，按 0.6 : 0.4 的权重融合，以兼顾语义深度与词法准确性，并配合结构感知分块（文本按递归字符分块、约 700 token）（[Advancing Retrieval-Augmented Generation for Structured Enterprise and Internal Data](https://arxiv.org/pdf/2507.12425)）。科学 RAG 的实证研究比较了三种系统——稠密（BGE-M3 + 向量搜索）、稀疏（BM25）与混合（RRF 融合），结论是混合检索比仅稀疏或仅稠密都更鲁棒（[SciRet](https://arxiv.org/html/2608.03860v1)）。多跳检索评测数据集 StratRAG 也采用混合评分：把 BM25 与稠密分数各自 min-max 归一化到 [0,1] 后等权（α=0.5）相加，编码器使用 all-MiniLM-L6-v2（[StratRAG: A Multi-Hop Retrieval Evaluation Dataset](https://arxiv.org/html/2604.22757)）。

**ColBERT 与延迟交互（late interaction）**继续演进。ColBERT 用 BERT 分别编码查询与文档，通过 token 级向量的细粒度交互（MaxSim：对每个查询 token 取最近的文档 token 并求和）计算相似度，文档多向量表示可离线预计算（[Incorporating Token Importance in Multi-Vector Retrieval](https://arxiv.org/html/2511.16106)）。围绕延迟交互模型的训练与检索工具链也在完善，如 PyLate 提供 MaxSim 评分与重排 API（[PyLate](https://arxiv.org/html/2508.03555v1/)）。2026 年出现若干面向效率与效果的改进：Col-Bandit 把重排建模为"有限总体 Top-K 识别"问题，用带不确定性上界的查询时剪枝只揭示必要的 (document, query token) MaxSim 条目（[Col-Bandit](https://arxiv.org/html/2602.02827v1/)）；PLAID-PRF 在 PLAID 索引上引入伪相关反馈的质心式 token（[PLAID-PRF](https://arxiv.org/html/2607.18626v1)）；ColBERT-AW 则用属性感知的查询 token 加权增强延迟交互效果（[ColBERT-AW](https://www.semanticscholar.org/paper/ColBERT-AW:-Enhancing-Late-Interaction-Retrieval-An-Lee/75cfde2dc6d88d3a7bf02c4d2f8ef9d309977e7d)）。TREC 2025 的多阶段层级检索管线把 ColBERTv2.0 作为延迟交互模型与 Contriever 等双编码器组合使用（[Single-Turn LLM Reformulation Powered Multi-Stage Hybrid Re-Ranking](https://trec.nist.gov/pubs/trec34/papers/mst.tot.pdf)）。

**向量数据库与索引工程优化**。Pinterest 的 Manas 平台从内存占用的 HNSW 演进到量化 SPANN：据报告，乘积量化（PQ）可把 HNSW 索引压缩约 74%、IVF 索引压缩约 93%，召回落在 70–80% 区间；标量量化（SQ）可把 HNSW 索引压缩约 59%、IVF 约 75%，且在各负载下稳定保持 90% 以上召回（[From Memory-Hungry HNSW to Quantized SPANN — InfoQ](https://www.infoq.com/news/2026/09/pinterest-search/)）。厂商层面的索引竞争也在加剧，Qdrant 于 2026 年 7 月发布基准称其在吞吐、延迟与算力上优于 Elastic 的磁盘索引 DiskBBQ（[Qdrant Beats Elastic's DiskBBQ](https://qdrant.tech/blog/benchmark-elastic-diskbbq/)）。

**GraphRAG 与图增强的混合检索**。工程界把 GraphRAG 描述为向量库之外的"知识图谱层"：检索变成两阶段操作——先用向量库找到语义相关的文本片段，再用知识图谱探索并验证这些片段中所提实体之间的关系（[GraphRAG Is the Future of Enterprise Knowledge Management](https://ragaboutit.com/graphrag-is-the-future-of-enterprise-knowledge-management/)）。由于图遍历的单次查询成本高于向量检索、且在单跳事实检索上表现更弱，生产实现通常引入 hybrid router，按查询类型在"图遍历（关系型问题）"与"向量检索（事实型问题）"之间路由（[GraphRAG 2026](https://ayinedjimi-consultants.fr/static/pdf/knowledge-graph-rag-graphrag-2026.pdf)；[Your Agent's Memory Problem Is a Retrieval Architecture Problem](https://www.falkordb.com/blog/ai-agent-memory-retrieval-architecture/)）。Towards Practical GraphRAG 则用 RRF 融合稠密向量检索与 1-hop 图遍历结果，以兼顾语义相似与结构关系（[Towards Practical GraphRAG](https://arxiv.org/html/2507.03226v3)）。

## 核心技术与关键概念

**稀疏检索（BM25）**：基于词频与逆文档频率的词法匹配，对精确术语与专有名词强，但缺乏语义泛化。

**稠密检索**：用嵌入向量做语义相似度，需配套 ANN 索引。常用嵌入模型包括 BGE-M3，MTEB 多语言榜单中亦有 gemini-embedding-001、Qwen3-Embedding-8B 等（见下文评测）。

**学习型稀疏检索（SPLADE）**：SPLADE 通过预训练语言模型的 MLM 头直接学习高维稀疏表示，实现查询与文档的联合词项扩展与重新加权，并配以稀疏正则化；后续版本（如 SPLADE-v3）强调更强的难负样本挖掘与蒸馏损失（[Mistral-SPLADE: LLMs for better Learned Sparse Retrieval](https://arxiv.org/pdf/2408.11119.pdf)）。在 SemEval-2026 的多轮 RAG 任务中，参赛系统常用 SPLADE-v3 作为稀疏召回以增强实体中心与精确匹配类查询的词法锚定，再与稠密召回经 RRF 融合（[Sifei at SemEval-2026 Task 8](https://arxiv.org/pdf/2606.28352v1)；[IIMAS-RAG at SemEval-2026 Task 8](https://aclanthology.org/2026.semeval-1.345.pdf)）。

**混合检索与融合**：常见做法是 RRF（Reciprocal Rank Fusion）融合 BM25 与稠密的排名列表，或按权重线性融合（[From BM25 to Corrective RAG](https://arxiv.org/pdf/2604.01733)；[Advancing RAG…](https://arxiv.org/pdf/2507.12425)）。

**重排序**：交叉编码器（cross-encoder）对候选做逐对精排，质量提升最大，但其分数缺乏可解释性，难以据此设定过滤阈值（[A Model and Package for German ColBERT](https://arxiv.org/pdf/2504.20083v1.pdf)）。

**延迟交互与多向量**：延迟交互模型（COLBERT、XTR）把文档表示为 token 级向量集合，通过 MaxSim 让每个查询 token 与每个文档 token 交互，效果接近 SOTA，但穷举检索在算力上不可行，因此常被用作重排而非全量召回（[Multivector Reranking in the Era of Strong First-Stage Retrievers](https://arxiv.org/pdf/2601.05200.pdf)）。

**ANN 索引**：核心概念为 HNSW（分层的可导航小世界图，主流 ANN 索引，参数 M、efConstruction、efSearch）、IVF（倒排文件，先聚类再搜索，参数 nlist、nprobe）与量化（PQ 乘积量化、SQ 标量量化、BQ 二值量化，用于压缩向量降低内存）；评测关注 Recall、QPS、延迟（[Vector Database Selection in Practice](https://www.toolsku.com/en/blog/distributed-vector-database-comparison-2026/)）。

**嵌入微调与评测**：MTEB（Massive Text Embedding Benchmark）是主流评测框架，覆盖检索、重排、对分类、聚类、分类与语义相似度等任务类型，并有按语言划分的子榜（[MTEB Benchmark Overview](https://mteb-leaderboard.hf.space/)）；MMTEB 把评测扩展到多语言（[MMTEB](https://arxiv.org/html/2502.13595)）。2026 年出现的 MTEB(LLM) 则专门评测把 LLM 直接当嵌入模型用于推理密集型检索的表现（[The Embedder's Dilemma](https://arxiv.org/html/2608.12875v1)）。

## 代表性项目 / 产品

- **向量数据库**：FAISS 是优化库（IVF、HNSW、PQ，可选 GPU），无内置持久化；Qdrant 基于 Rust、强调过滤与水平扩展；Milvus 为存算分离的分布式数据库，支持 IVF/HNSW/DiskANN；Weaviate 结合 HNSW 与内置向量化及知识图谱式对象存储；Chroma 面向 RAG 快速原型；LanceDB 用磁盘列式格式与 IVF-PQ 索引实现快速、省内存的构建（[A Comprehensive Empirical Evaluation of Vector Database Systems for ANN Search](https://arxiv.org/pdf/2608.12812)）。
- **pgvector / Pinecone 等**：工程参数上，Qdrant 默认 SQ、支持 BQ/PQ；Milvus 支持 SQ8、fp16、SQ4；pgvector 提供 halfvec 与二值量化；Pinecone 为托管二值量化（[Enterprise Vector Database 2026: Qdrant vs Milvus vs pgvector vs Pinecone](https://dev.to/devrudals/enterprise-vector-database-2026-qdrant-vs-milvus-vs-pgvector-vs-pinecone-16a0)）。
- **嵌入模型**：Qwen3-Embedding 系列提供多种尺寸，官方称 8B 版本在 MTEB 多语言榜单排名第一（截至 2025 年 6 月 5 日，分数 70.58）（[Qwen 3 Embedding](https://www.kaggle.com/models/qwen-lm/qwen-3-embedding/transformers/8b/1)）。

## 关键数据与评测结果

- **两阶段管线的量化增益**：在文本—表格文档基准中，"混合检索 + 神经重排（Hybrid + Cohere Rerank）"的 Recall@5 达 0.816，显著高于单独混合 RRF（0.695，+17.4%）、BM25（0.644，+26.7%）与稠密检索（0.587，+39.0%）（[From BM25 to Corrective RAG](https://arxiv.org/pdf/2604.01733)）。
- **图索引的吞吐/内存权衡**：一项在同一条件下比较 HNSW、DiskANN、RoarGraph、ACORN 等的实验给出 HNSW（M=16）约 35,000 QPS、构建 120s、内存 256MB；HNSW（M=32）约 50,000 QPS、构建 210s、内存 480MB；HNSW + SQ-8bit 约 85,000 QPS、内存 64MB（[グラフ型ベクトル検索の包括的実験評価](https://0h-n0.github.io/posts/paper-2501-04702/)）。
- **MTEB 领先模型（多口径）**：一份 2026 年 4 月榜单给出 Gemini Embedding 001（MTEB 平均 68.32、检索 67.71、3072 维、最大 8192 token）与 NVIDIA NV-Embed-v2（72.31*，4096 维）排列前列（[Embedding Model Leaderboard: MTEB Rankings April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)）；另一份榜单给出 KaLM-Embedding-Gemma3-12B 平均 72.32（3840 维、11.76B）与 Qwen3-Embedding-8B 平均 70.58（4096 维、Apache-2.0）（[MTEB leaderboard — Codesota](https://www.codesota.com/benchmarks/mteb)）；专注 LLM 做嵌入的 MTEB(LLM) 上，Gemini 3.1 Pro 以均分 77.6 领先，Octen-8B 77.2、Qwen3-E-8B 紧随（[The Embedder's Dilemma](https://arxiv.org/html/2608.12875v1)）。另有更新至 2026 年 7 月的榜单给出 Harrier-OSS-v1-27B（v2 分数 74.3）与 KaLM-Embedding-Gemma3-12B（v2 分数 72.32）等条目（[Best Embedding Models 2025: MTEB Scores & Leaderboard](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)）。上述榜单版本（MTEB v1 English / Multilingual / MMTEB / MTEB(LLM)）不同，分数不可直接横向比较。
- **大规模向量检索**：阿里云 PolarDB 基于 DINOv2 的 100 亿条 1024 维向量数据集，对比 IVF-PQ 与 HNSW-DiskMode 两类索引，用于高吞吐写入与高精度实时查询的选型（[性能测试报告：百亿级 DINO 向量数据集 — 阿里云](https://help.aliyun.com/zh/polardb/polardb-for-mysql/user-guide/performance-testing-based-on-a-dino-dataset-with-tens-of-billions-vectors)）。
- **量化权衡**：Pinterest 数据显示 PQ 量化把 HNSW 索引降至 32 GB（约压缩 74%），但 Recall@100 从 93.72% 降至 77.25%；SQ 则把索引降至更低比特并稳定保持 90% 以上召回（[InfoQ](https://www.infoq.com/news/2026/09/pinterest-search/)）。
- **融合 + 重排的增益**：在 WSDM CUP 多语言检索任务上，Naver Labs Europe 用 RRF（k=50）把一阶段融合结果与其重排结果再融合，nDCG@20 由 0.517 提升到 0.548（重排器为 Qwen3 Reranker 4B）（[Naver Labs Europe @ WSDM CUP](https://arxiv.org/pdf/2602.20986)）。
- **混合检索一致性**：多项研究（TREC RAG 2025、SciRet、企业结构化数据）均报告混合检索在多数指标上优于单一稀疏或稠密检索（[NITATREC](https://trec.nist.gov/pubs/trec34/papers/NIT%20Agartala.rag.pdf)；[SciRet](https://arxiv.org/html/2608.03860v1)；[Advancing RAG…](https://arxiv.org/pdf/2507.12425)）。

## 趋势与争议

一是**"混合 + 重排"是否已足够**：多项 2025–2026 研究把混合检索 + 交叉编码器重排视作性价比最高的组合，但重排带来延迟与算力开销，且交叉编码器分数不可解释、阈值难定（[From BM25 to Corrective RAG](https://arxiv.org/pdf/2604.01733)；[German ColBERT](https://arxiv.org/pdf/2504.20083v1.pdf)）。二是**多向量 vs 单向量**：ColBERT 式延迟交互保留了 token 级细粒度，代价是存储与 MaxSim 计算更重，因此常被用作重排而非全量召回，并催生查询时剪枝（Col-Bandit）等降本手段（[Multivector Reranking](https://arxiv.org/pdf/2601.05200.pdf)；[Col-Bandit](https://arxiv.org/html/2602.02827v1/)）。三是**索引与内存的权衡**：量化能显著降低内存，但召回损失明显，需要按场景选择 SQ/ BQ/ PQ（[InfoQ](https://www.infoq.com/news/2026/09/pinterest-search/)），厂商基准（如 Qdrant 对 Elastic DiskBBQ）也需谨慎看待，因由各自发布（[Qdrant](https://qdrant.tech/blog/benchmark-elastic-diskbbq/)）。四是**榜单口径陷阱**：MTEB 存在 English v1、Multilingual、MMTEB、MTEB(LLM) 等多个版本与子榜，模型分数与排名会随口径变化，选型时需对齐同一榜单（对比 [MTEB — AI Wiki](https://aiwiki.ai/wiki/mteb) 与 [Embedding Model Leaderboard](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)）。

## 参考来源

1. [NITATREC at TREC RAG 2025: Exploring Sparse, Dense, and Hybrid Retrieval](https://trec.nist.gov/pubs/trec34/papers/NIT%20Agartala.rag.pdf)
2. [From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents](https://arxiv.org/pdf/2604.01733)
3. [Advancing Retrieval-Augmented Generation for Structured Enterprise and Internal Data](https://arxiv.org/pdf/2507.12425)
4. [SciRet: A Compute-Aware Empirical Study of Retrieval and Reranking for Scientific RAG](https://arxiv.org/html/2608.03860v1)
5. [Incorporating Token Importance in Multi-Vector Retrieval](https://arxiv.org/html/2511.16106)
6. [PyLate: Flexible Training and Retrieval for Late Interaction Models](https://arxiv.org/html/2508.03555v1/)
7. [Single-Turn LLM Reformulation Powered Multi-Stage Hybrid Re-Ranking (TREC 2025)](https://trec.nist.gov/pubs/trec34/papers/mst.tot.pdf)
8. [From Memory-Hungry HNSW to Quantized SPANN: Pinterest's Manas Platform — InfoQ](https://www.infoq.com/news/2026/09/pinterest-search/)
9. [A Comprehensive Empirical Evaluation of Vector Database Systems for ANN Search](https://arxiv.org/pdf/2608.12812)
10. [性能测试报告：百亿级 DINO 向量数据集 — 阿里云 PolarDB](https://help.aliyun.com/zh/polardb/polardb-for-mysql/user-guide/performance-testing-based-on-a-dino-dataset-with-tens-of-billions-vectors)
11. [Enterprise Vector Database 2026: Qdrant vs Milvus vs pgvector vs Pinecone](https://dev.to/devrudals/enterprise-vector-database-2026-qdrant-vs-milvus-vs-pgvector-vs-pinecone-16a0)
12. [Vector Database Selection in Practice: Deep Comparison of 5 Distributed Vector Databases](https://www.toolsku.com/en/blog/distributed-vector-database-comparison-2026/)
13. [MTEB (Massive Text Embedding Benchmark) — AI Wiki](https://aiwiki.ai/wiki/mteb)
14. [Best Embedding Models 2025: MTEB Scores & Leaderboard](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)
15. [MTEB Benchmark Overview — Hugging Face Space](https://mteb-leaderboard.hf.space/)
16. [MMTEB: Massive Multilingual Text Embedding Benchmark](https://arxiv.org/html/2502.13595)
17. [Qwen 3 Embedding](https://www.kaggle.com/models/qwen-lm/qwen-3-embedding/transformers/8b/1)
18. [A Model and Package for German ColBERT](https://arxiv.org/pdf/2504.20083v1.pdf)
19. [StratRAG: A Multi-Hop Retrieval Evaluation Dataset](https://arxiv.org/html/2604.22757)
20. [Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval](https://arxiv.org/html/2602.02827v1/)
21. [PLAID-PRF: Pseudo-Relevance Feedback with Centroid-like Tokens in PLAID](https://arxiv.org/html/2607.18626v1)
22. [Multivector Reranking in the Era of Strong First-Stage Retrievers](https://arxiv.org/pdf/2601.05200.pdf)
23. [ColBERT-AW: Enhancing Late Interaction Retrieval With Attribute-Aware Query Token Weighting](https://www.semanticscholar.org/paper/ColBERT-AW:-Enhancing-Late-Interaction-Retrieval-An-Lee/75cfde2dc6d88d3a7bf02c4d2f8ef9d309977e7d)
24. [Qdrant Beats Elastic's DiskBBQ at 2x Throughput](https://qdrant.tech/blog/benchmark-elastic-diskbbq/)
25. [Embedding Model Leaderboard: MTEB Rankings April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)
26. [The Embedder's Dilemma: LLMs Are Better, but at What Cost?](https://arxiv.org/html/2608.12875v1)
27. [MTEB leaderboard — Codesota](https://www.codesota.com/benchmarks/mteb)
28. [グラフ型ベクトル検索の包括的実験評価（HNSW・DiskANN・RoarGraph・ACORN）](https://0h-n0.github.io/posts/paper-2501-04702/)
29. [Mistral-SPLADE: LLMs for better Learned Sparse Retrieval](https://arxiv.org/pdf/2408.11119.pdf)
30. [Sifei at SemEval-2026 Task 8: Hybrid Retrieval and Query Rewriting for Multi-Turn RAG](https://arxiv.org/pdf/2606.28352v1)
31. [IIMAS-RAG at SemEval-2026 Task 8: Hybrid Sparse-Dense Retrieval and Answerability-Conditioned Generation](https://aclanthology.org/2026.semeval-1.345.pdf)
32. [Naver Labs Europe @ WSDM CUP | Multilingual Retrieval](https://arxiv.org/pdf/2602.20986)
33. [GraphRAG Is the Future of Enterprise Knowledge Management](https://ragaboutit.com/graphrag-is-the-future-of-enterprise-knowledge-management/)
34. [GraphRAG 2026 : Knowledge Graphs, Neo4j et Architecture RAG](https://ayinedjimi-consultants.fr/static/pdf/knowledge-graph-rag-graphrag-2026.pdf)
35. [Your Agent's Memory Problem Is a Retrieval Architecture Problem — FalkorDB](https://www.falkordb.com/blog/ai-agent-memory-retrieval-architecture/)
36. [Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale](https://arxiv.org/html/2507.03226v3)