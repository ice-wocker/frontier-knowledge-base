# 向量数据库与嵌入检索

> 最后更新：2026-09-26 ｜ 领域：数据·工程与架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

向量数据库与嵌入检索（embeddings）是 RAG（检索增强生成）与语义搜索的存储与检索底座。其基本流程是：用嵌入模型把文本、图像等非结构化数据编码为高维向量，建立近似最近邻（ANN）索引，在查询时按向量相似度（余弦/内积/欧氏距离）检索 Top-K 结果。系统由「嵌入模型 + 索引算法 + 向量数据库」三层构成，三者共同决定召回率、延迟与成本。

需要区分的是，「向量数据库」与「向量索引库」并不等同。向量索引库（如 FAISS、hnswlib）只提供 ANN 计算能力，不负责持久化、增删改、过滤、权限与多租户；而向量数据库在这些之上补齐了存储、并发、事务与运维能力。因此选型的第一个问题往往不是「哪个索引最快」，而是「需要多少运维能力」：已有 Postgres 的团队用 pgvector 扩展即可，追求极致性能可自托管 Qdrant，构建十亿级多租户平台则需要 Milvus 这类分布式系统或 Pinecone 这类全托管服务。此外，向量数据库的价值正被上游系统吸收——流式数据库（如 RisingWave 3.0 原生支持 pgvector 摄取）与湖仓（Milvus 3.0 的 lake-native）都在把向量能力内嵌，边界正在快速变化。

## 最新进展（2025–2026）

**向量数据库格局趋于分化。** 2026 年的产品对比显示，主流选择包括：Qdrant（Rust，2021，开源 + 云）、Pinecone（全托管 SaaS，2019，融资逾 1.38 亿美元）、Weaviate（Go，2019，开源 + 云）、Milvus（Go/C++，2019，开源，Zilliz Cloud）、pgvector（PostgreSQL 扩展，2021）（[The Best Vector Database in 2026](https://dev.to/darshit_01/the-best-vector-database-in-2026-qdrant-vs-pinecone-vs-weaviate-vs-milvus-vs-pgvector-3147)）。选型口径上，Pinecone 是运维负担最低的生产路径，Qdrant 是可自托管时的性能之选，Milvus 面向 1 亿+ 向量的多租户平台，Weaviate 则在「混合检索是产品本身而非功能」时被选用（[Vector DB Comparison](https://datavidhya.com/learn/ai-for-data-engineering/vector-databases-embeddings/vector-db-deep-dive/)）。

**Milvus 3.0 走向 lake-native。** 据 2026 企业视角对比，Milvus 3.0 为 lake-native 架构，适合十亿级自托管 workload；Pinecone 为完全托管、serverless、闭源；pgvector 是 Postgres 扩展，适合已在 Postgres 的团队；Qdrant 在搜索内部执行 payload 过滤，而非搜索前/后（[Top Vector Databases for Enterprise AI: 2026 Comparison](https://atlan.com/know/top-vector-databases-enterprise-ai/)）。

**量化成为规模化关键。** Pinterest 为应对 HNSW 的内存压力，在其 Manas 平台上对 1 亿条 GraphSAGE 嵌入实现标量量化（SQ）与乘积量化（PQ）以显著降低内存占用，并演进到量化版 SPANN（[From Memory-Hungry HNSW to Quantized SPANN](https://www.infoq.com/news/2026/09/pinterest-search/)）。

**嵌入模型榜单更新。** 2026 年 MTEB 相关排行中，Qwen3-Embedding-8B 以 70.6 位居前列（Apache 2.0、多语言），BGE-M3 为 63.2（MIT、568M 参数），Jina Embeddings v3 为 62.8，Nomic-embed-v2 为 61.4（137M 参数、紧凑）（[MTEB 2026](https://app.ailog.fr/fr/blog/news/rag-benchmark-mteb-2026)）。另一份 2026 年 4 月榜单列出 Nomic Embed v1.5 为 62.39（768 维、8192 token、$0.05/1M tokens）与 text-embedding-3-small 为 62.26（1536 维、8191 token、$0.02/1M tokens）（[Embedding Model Leaderboard: MTEB April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026)）。此外，NV-Embed-v2 在 MTEB English 上达 72.31（4096 维、32K 上下文），text-embedding-3-large 为 3072 维、8K 上下文、$0.13/1M tokens（[Best Embedding Models in 2026](https://futureagi.com/blog/best-embedding-models-2025/)）。

## 核心技术与关键概念

**索引算法：HNSW / IVF / PQ / DiskANN。** HNSW 是图索引，查询质量高但内存开销大；IVF 通过聚类划分桶以缩小搜索范围；PQ（乘积量化）把向量切成子向量并用码本聚类编码，可达 4–32 倍压缩，代价是召回率略降；DiskANN 采用「内存存 PQ 压缩向量 + SSD 存全精度向量与图边」的混合布局，先以内存中的压缩向量导航图、再用 SSD 上的全精度向量重排候选，可在十亿级索引上实现约 100 ms 查询（[Vector Indexing: HNSW, IVF, and DiskANN](https://npblue.com/ai/rag/vector-indexing)）。

**量化技术。** Milvus 支持标量量化（如 SQ8，把每个维度压成 8 bit，相比 32 位浮点可减少 75% 内存）与乘积量化（4–32 倍压缩），前者保留合理精度，后者压缩率更高、召回略降，适合内存受限场景（[Index Explained (Milvus)](https://milvus.io/docs/index-explained.md)）。

**过滤检索与混合检索。** pgvector 支持 HNSW、IVFFlat 索引与迭代扫描（0.8+）；Qdrant 使用可过滤 HNSW 链接；Weaviate 支持 ACORN 遍历；Pinecone 内置但不可调。压缩方面，pgvector 支持 halfvec/binary/sparse，Qdrant 支持标量/二值/TurboQuant，Weaviate 支持 PQ/SQ/BQ/RQ（[Vector Databases Compared](https://precisionaiacademy.com/blog/vector-database-comparison-2026)）。

**混合检索与重排序。** 纯稠密向量检索擅长语义相似，却可能在精确关键词、专有名词与稀有词上失败；因此在生产 RAG 中常采用混合检索：把 BM25 等稀疏检索与稠密向量检索的结果融合，再交由交叉编码器（cross-encoder）重排序模型对候选做精细打分。BGE-M3 这类模型的价值正在于「一模型同时输出稠密、稀疏与多向量表示」，减少维护多套检索管线的成本（[Best Embedding Models in 2026](https://futureagi.com/blog/best-embedding-models-2025/)）。过滤检索（filtered search）则是把结构化条件（权限、时间、租户）与向量相似度结合，其难点在于过滤会破坏图索引的连通性、导致召回下降，Qdrant 的「可过滤 HNSW 链接」与 pgvector 的迭代扫描正是针对该问题的工程解法（[Vector Databases Compared](https://precisionaiacademy.com/blog/vector-database-comparison-2026)）。

**规模化的核心约束。** 向量检索的规模化瓶颈往往不是算力而是内存：十亿级全精度浮点向量所需的 RAM 极其可观，因此生产系统普遍引入量化、磁盘索引（DiskANN）或将向量下沉到湖仓（Milvus 3.0 的 lake-native）。Pinterest 的实践进一步印证了这一点——其平台从内存密集的 HNSW 转向量化版 SPANN，以 SQ/PQ 大幅压缩内存占用（[From Memory-Hungry HNSW to Quantized SPANN](https://www.infoq.com/news/2026/09/pinterest-search/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Milvus**（https://milvus.io/）— 十亿级、lake-native（3.0）、Kubernetes 生产部署。
- **Qdrant**（https://qdrant.tech/）— Rust 实现、可过滤 HNSW、性能优先。
- **Weaviate**（https://weaviate.io/）— 混合检索优先。
- **Pinecone**（https://www.pinecone.io/）— 全托管 serverless。
- **pgvector**（https://github.com/pgvector/pgvector）— PostgreSQL 原生扩展。
- **BGE-M3 / Qwen3-Embedding / Nomic Embed**（https://huggingface.co/BAAI/bge-m3）— 开源嵌入模型代表。

## 关键数据与评测结果（附来源）

- 单节点性能（2026 对比）：Qdrant（HNSW，无量化）约 2100 QPS、p99 < 12 ms；Milvus（HNSW，CPU）约 1800 QPS、p99 < 15 ms，A10G 上 GPU CAGRA 约 4400 QPS；Weaviate（HNSW）约 1500 QPS（[Pinecone vs Weaviate vs Qdrant vs Milvus 2026](https://aiworkflowlab.dev/article/pinecone-vs-weaviate-vs-qdrant-vs-milvus-2026)）。
- SQ8 可减少 75% 内存；PQ 压缩比 4–32 倍（[Milvus Index Explained](https://milvus.io/docs/index-explained.md)）。
- DiskANN 在十亿级索引上可实现约 100 ms 查询（[Vector Indexing](https://npblue.com/ai/rag/vector-indexing)）。
- MTEB：Qwen3-Embedding-8B 70.6、BGE-M3 63.2、NV-Embed-v2 72.31（English）（[MTEB 2026](https://app.ailog.fr/fr/blog/news/rag-benchmark-mteb-2026)、[Best Embedding Models 2026](https://futureagi.com/blog/best-embedding-models-2025/)）。

## 趋势与争议

**嵌入模型的多口径冲突。** 不同来源的 MTEB 数值与榜首不一致（Qwen3-Embedding-8B 70.6 vs NV-Embed-v2 72.31 但后者为 English 子集），源于 MTEB 版本迭代、任务子集与维度设置的差异，不应跨口径直接比较。

**专用向量库 vs 通用数据库扩展。** pgvector 凭借「已在 Postgres 的团队无需新增系统」获得优势，而专用库在十亿级、多租户、极端并发下仍有性能与运维上的价值，形成「够用即合并、规模即专用」的分工。

**量化的精度-内存权衡。** SQ/PQ/TurboQuant 等量化显著降低内存成本，但引入召回损失，成为生产规模化的核心调优点；Pinterest 从 HNSW 转向量化 SPANN 的实践表明，内存而非算力往往是规模化瓶颈。

## 参考来源

- [The Best Vector Database in 2026: Qdrant vs Pinecone vs Weaviate vs Milvus vs pgvector](https://dev.to/darshit_01/the-best-vector-database-in-2026-qdrant-vs-pinecone-vs-weaviate-vs-milvus-vs-pgvector-3147)
- [Pinecone vs Weaviate vs Qdrant vs Milvus: Best Vector Database (2026)](https://aiworkflowlab.dev/article/pinecone-vs-weaviate-vs-qdrant-vs-milvus-2026)
- [Vector Databases Compared: pgvector, Qdrant, Weaviate, Pinecone](https://precisionaiacademy.com/blog/vector-database-comparison-2026)
- [Vector DB Comparison](https://datavidhya.com/learn/ai-for-data-engineering/vector-databases-embeddings/vector-db-deep-dive/)
- [Top Vector Databases for Enterprise AI: 2026 Comparison](https://atlan.com/know/top-vector-databases-enterprise-ai/)
- [Index Explained (Milvus)](https://milvus.io/docs/index-explained.md)
- [Vector Indexing: HNSW, IVF, and DiskANN for Fast ANN Search](https://npblue.com/ai/rag/vector-indexing)
- [From Memory-Hungry HNSW to Quantized SPANN: Pinterest's Manas Platform](https://www.infoq.com/news/2026/09/pinterest-search/)
- [MTEB 2026 : Etat des lieux du benchmark embeddings](https://app.ailog.fr/fr/blog/news/rag-benchmark-mteb-2026)
- [Embedding Model Leaderboard: MTEB Rankings April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026)
- [Best Embedding Models in 2026: NV-Embed-v2, BGE-M3, E5-mistral, Voyage 3 Compared](https://futureagi.com/blog/best-embedding-models-2025/)
- [Best Open-Weight Embedding Models 2026](https://presenc.ai/research/best-open-weight-embedding-models-2026)