# 搜索引擎与信息检索

> 最后更新：2026-09-26 ｜ 领域：数据·分布式、治理与分析 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

搜索引擎与信息检索（IR）技术负责把海量非结构化与半结构化内容组织为可检索、可排序的索引。核心技术包括倒排索引与 BM25 等词法评分模型、向量检索与近似最近邻（ANN）索引、以及把两者融合的混合检索（hybrid search）。在 RAG（检索增强生成）普及后，搜索引擎的角色从"给人看的结果列表"扩展到"为模型提供上下文"，检索质量直接决定生成质量。主流产品包括 Elasticsearch/Elastic Stack、OpenSearch、Vespa，以及可直接承载日志分析、语义检索与混合排序的多类引擎。

## 最新进展（2025–2026）

**Elastic 9.x 系列持续扩张，向量检索走向"开箱可用"。** Elastic 9.0 基于 Lucene 10 构建（[Elastic 9.0 及 8.18](https://www.elastic.co/kr/blog/whats-new-elastic-9-0-0)）；9.3 中 Elastic Agent Builder 正式 GA，并引入三个 Jina AI 模型（jina-embeddings-v3、jina-reranker-v2-base-multilingual、jina-reranker-v3）（[Elastic 9.3](https://www.elastic.co/blog/whats-new-elastic-9-3-0)）；9.5 带来列存能力与 VectorDB index mode，官方称向量检索"无需配置或索引调优即可工作"，并提供自动校准（auto-calibration），同时支持原生 Prometheus/PromQL（[Elastic 9.5](https://www.elastic.co/de/blog/whats-new-elastic-9-5-0)、[What's new — Elastic](https://www.elastic.co/whats-new)）。

**OpenSearch 3.x 上线 GPU 加速与 Agent 化能力。** OpenSearch 3.0 将 GPU 加速作为实验特性引入向量索引构建，官方基准显示索引速度提升 9.3 倍、成本降低 3.75 倍，把十亿级索引构建从"数天"缩短到"数小时"（[Announcing OpenSearch 3.0](https://opensearch.org/blog/unveiling-opensearch-3-0/)、[Performance progress in OpenSearch 3.0](https://opensearch.org/blog/opensearch-project-update-performance-progress-in-opensearch-3-0/)）。3.3.0（2025 年 10 月 14 日发布）重设计了 Discover 界面、以 Apache Calcite 作为默认 PPL 查询引擎，并将 agentic search 与 agentic memory API 转为 GA，同时用 Seismic 算法提升神经稀疏检索性能（[OpenSearch Version history](https://docs.opensearch.org/latest/version-history/)）。2026 路线图提出四大方向，包括 AMD GPU 支持以便本地部署、简化自建推理服务运行 Qwen3 模型、探索 GGUF 模型与 last token pooling（[The 2026 OpenSearch Roadmap](https://opensearch.org/blog/the-2026-opensearch-roadmap-four-pillars-for-ai-native-innovation/)）。

**混合检索成为 RAG 的最低可行基线。** 一项针对文本与表格混合文档的检索策略基准研究指出：通过 Reciprocal Rank Fusion（RRF）融合 BM25 与稠密检索，在所有指标与所有数据子集上都优于单一方法，其中在 TAT-DQA 上相对 BM25 的 Recall@5 提升 8.1 个百分点；作者因此建议把混合检索作为任何 RAG 部署的最低可行基线（[From BM25 to Corrective RAG](https://arxiv.org/pdf/2604.01733v1)）。SemEval-2026 Task 8（MTRAGEval）的多轮检索任务中，表现较好的系统普遍采用"查询改写 + 混合稀疏-稠密检索 + 交叉编码器重排序"的三段式管道，其中一套系统以 nDCG@5 = 0.531 在 38 个系统中排名第 8（[Caraman at SemEval-2026 Task 8](https://aclanthology.org/2026.semeval-1.225.pdf)），另一套使用 SPLADE 与 Voyage-3-large 经 RRF 融合（[IIMAS-RAG at SemEval-2026 Task 8](https://aclanthology.org/2026.semeval-1.345.pdf)）。

## 核心技术与关键概念

**倒排索引与 BM25。** BM25 仍是词法检索的基线，依赖在全语料上构建的倒排索引。研究指出 BM25 的价值在于精确术语匹配：生物医学查询常包含药物名、基因标识符、解剖缩写等，这些场景下词法精确性不可替代（[Benchmarking Retrieval Strategies for Biomedical RAG](https://arxiv.org/pdf/2605.02520)）。

**稠密向量检索与 ANN。** Elasticsearch 提供原生稠密向量检索（HNSW 索引）与 ELSER（Elastic Learned Sparse EncodeR，用于无需自建模型的语义检索）；OpenSearch 提供 k-NN 插件，支持 Faiss、NMSLIB、Lucene 多种后端（[OpenSearch vs Elasticsearch — 2026](https://devopsboys.com/blog/opensearch-vs-elasticsearch-2026)）。需要注意 OpenSearch 在 2.16 弃用 nmslib 并在新索引中移除（[OpenSearch vs Elasticsearch Compared (2026)](https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared)）。

**融合与重排序。** 混合检索通常用 RRF 或分数融合（ScoreFusion）合并多路结果。一份公开的 ADR 记录给出变体对比：BM25（稀疏）Recall@10 为 77.3%、QPS 57,174；稠密 flat（精确）Recall@10 仅 7.5%；ScoreFusion α=0.7 为 68.8%；RRF k=60 为 50.5%，三者的 QPS 均在 360 附近（[ADR-256 Hybrid Sparse-Dense Search](http://raw.githubusercontent.com/ruvnet/ruvector/HEAD/docs/adr/ADR-256-hybrid-sparse-dense-search.md)）。该结果表明融合参数（RRF 的 k、ScoreFusion 的 α）对召回影响巨大，需按语料调优。重排序阶段常用交叉编码器：生物医学 RAG 研究中，LangChain 的 EnsembleRetriever 以 BM25 权重 0.4、稠密检索权重 0.6 通过 RRF 组合（[Benchmarking Retrieval Strategies for Biomedical RAG](https://arxiv.org/pdf/2605.02520)）。

**晚交互（Late Interaction）与 ColBERT。** Vespa 自述为生产环境晚交互检索的源头引擎，提供原生 ColBERT embedder（把文本映射为多个上下文相关的 token 向量，质量优于压成单向量）以及后来被业界广泛采用的二值量化技巧（[Late Interaction in Vespa](https://frutik.github.io/awesome-search/Topics/Late-Interaction-in-Vespa)、[Embedding — Vespa](https://docs.vespa.ai/en/rag/embedding.html)）。与 Elasticsearch/OpenSearch/Qdrant 通过专用多向量字段与固定 MaxSim 函数实现不同，Vespa 在通用张量排序框架中表达晚交互——MaxSim 函数需用户以张量表达式书写（[Late Interaction in Vespa](https://frutik.github.io/awesome-search/Topics/Late-Interaction-in-Vespa)）。晚交互的存储成本较高，因此主要用于法律、监管、制药、金融等语料有界且单条价值高的垂直场景（[Late interaction, or why ColBERT keeps coming back](https://datarekha.com/blog/late-interaction-retrieval/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Elasticsearch / Elastic Stack**：9.x 系列，含原生向量检索、ELSER、Agent Builder、VectorDB index mode 与列存；集成 OpenAI、Azure OpenAI、Amazon Bedrock（[Elastic 9.5](https://www.elastic.co/de/blog/whats-new-elastic-9-5-0)、[OpenSearch vs Elasticsearch — 2026](https://devopsboys.com/blog/opensearch-vs-elasticsearch-2026)）。
- **OpenSearch**：k-NN 插件 + 多后端、神经搜索管道、ML Commons、GPU 加速向量索引构建（[OpenSearch vs Elasticsearch — 2026](https://devopsboys.com/blog/opensearch-vs-elasticsearch-2026)、[Announcing OpenSearch 3.0](https://opensearch.org/blog/unveiling-opensearch-3-0/)）。
- **Vespa**：原生 ColBERT embedder、张量排序框架下的晚交互、streaming mode 面向自然分片数据的低成本 RAG（[Embedding — Vespa](https://docs.vespa.ai/en/rag/embedding.html)、[RAG Blueprint](https://docs.vespa.ai/en/learn/tutorials/rag-blueprint.html)）。
- **Amazon OpenSearch Service**：托管服务，支持 GPU 加速向量索引、auto-optimize 与 vector ingestion；其 Optimized engine 结合列存分析与全文检索以提升性价比（[Amazon OpenSearch Service release notes](https://docs.amazonaws.cn/en_us/opensearch-service/latest/developerguide/release-notes.html)）。

## 关键数据与评测结果（附来源）

- Elastic 自测：在 2000 万文档语料上，Elasticsearch 在过滤式向量检索上的吞吐是 OpenSearch 的 8 倍，且在所有评估配置中 Recall@100 更高（[Elasticsearch vector search is up to 8x faster than OpenSearch](https://www.elastic.co/search-labs/fr/blog/opensearch-vs-elasticsearch-filtered-vector-search)）。
- OpenSearch 3.0 GPU 加速：向量索引构建速度提升 9.3 倍、成本降低 3.75 倍（[Announcing OpenSearch 3.0](https://opensearch.org/blog/unveiling-opensearch-3-0/)）。
- Elasticsearch 9.3 的 NVIDIA cuVS GPU 加速处于技术预览，最高可带来 12 倍索引加速；同时存在最大向量维度 4096 的限制（[OpenSearch vs Elasticsearch Compared (2026)](https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared)）。
- 第三方评测给出的语义负载区间：Elasticsearch 向量检索性能在大规模语义负载上比 OpenSearch 高 2–12 倍（[Elasticsearch vs OpenSearch for enterprise AI in 2026](https://www.sentientconcepts.com/post/elasticsearch-vs-opensearch)）。
- 混合检索基准：RRF 融合 BM25 + 稠密检索在 TAT-DQA 上 Recall@5 相对 BM25 提升 8.1pp（[From BM25 to Corrective RAG](https://arxiv.org/pdf/2604.01733v1)）；SemEval-2026 Task 8 中三段式管道 nDCG@5 = 0.531，38 个系统中第 8 名（[Caraman at SemEval-2026 Task 8](https://aclanthology.org/2026.semeval-1.225.pdf)）。

## 趋势与争议

其一，**厂商基准的可比性问题突出**：8 倍、12 倍、2–12 倍等结论分别来自 Elastic 自家 Search Labs、第三方博客与厂商对比文章，测试语料规模、过滤比例与召回口径不一致，不能直接横向比较（[Elasticsearch vector search](https://www.elastic.co/search-labs/fr/blog/opensearch-vs-elasticsearch-filtered-vector-search)、[OpenSearch vs Elasticsearch Compared (2026)](https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared)）。其二，**"混合检索是否总是更好"存在条件性**：公开的 ADR 数据显示 BM25 单独在 Recall@10 上（77.3%）显著优于 ScoreFusion（68.8%）与 RRF（50.5%），说明融合并不必然提升召回，与前述"混合检索优于单一方法"的结论存在冲突，可能源于语料与任务差异（[ADR-256](http://raw.githubusercontent.com/ruvnet/ruvector/HEAD/docs/adr/ADR-256-hybrid-sparse-dense-search.md)、[From BM25 to Corrective RAG](https://arxiv.org/pdf/2604.01733v1)）。其三，**晚交互的性价比争议**：ColBERT 类方案能带来召回提升，但索引体积与工程复杂度显著上升，只在语料有界、单条价值高的垂直场景被证明划算（[Late interaction, or why ColBERT keeps coming back](https://datarekha.com/blog/late-interaction-retrieval/)）。其四，**向量维度的硬约束**：Elasticsearch 4096 维上限可能随着更新一代嵌入模型维度上升而成为瓶颈（[OpenSearch vs Elasticsearch Compared (2026)](https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared)）。其五，**引擎边界模糊**：日志分析、全文检索与向量检索在同一引擎内融合（如 OpenSearch Optimized engine、Elastic 的列存与 VectorDB index mode），使得"搜索引擎 vs 向量数据库 vs OLAP"的品类划分逐渐失去意义（[Amazon OpenSearch Service release notes](https://docs.amazonaws.cn/en_us/opensearch-service/latest/developerguide/release-notes.html)、[Elastic 9.5](https://www.elastic.co/de/blog/whats-new-elastic-9-5-0)）。

## 参考来源

1. [Elasticsearch vector search is up to 8x faster than OpenSearch](https://www.elastic.co/search-labs/fr/blog/opensearch-vs-elasticsearch-filtered-vector-search)
2. [OpenSearch vs Elasticsearch — Which One to Use in 2026](https://devopsboys.com/blog/opensearch-vs-elasticsearch-2026)
3. [OpenSearch vs Elasticsearch Compared (2026): Performance, Cost, AI](https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared)
4. [Elasticsearch vs OpenSearch for enterprise AI in 2026](https://www.sentientconcepts.com/post/elasticsearch-vs-opensearch)
5. [Elastic 9.5: Columnar, VectorDB index mode & auto-calibration](https://www.elastic.co/de/blog/whats-new-elastic-9-5-0)
6. [Discover the latest from Elastic — What's new](https://www.elastic.co/whats-new)
7. [Elastic 9.3: Chat with your data, build custom AI agents](https://www.elastic.co/blog/whats-new-elastic-9-3-0)
8. [Elastic 9.0 및 8.18 release highlights](https://www.elastic.co/kr/blog/whats-new-elastic-9-0-0)
9. [OpenSearch Version history](https://docs.opensearch.org/latest/version-history/)
10. [Announcing OpenSearch 3.0](https://opensearch.org/blog/unveiling-opensearch-3-0/)
11. [OpenSearch Project update: Performance progress in OpenSearch 3.0](https://opensearch.org/blog/opensearch-project-update-performance-progress-in-opensearch-3-0/)
12. [The 2026 OpenSearch Roadmap: Four pillars for AI-native innovation](https://opensearch.org/blog/the-2026-opensearch-roadmap-four-pillars-for-ai-native-innovation/)
13. [Document history for Amazon OpenSearch Service](https://docs.amazonaws.cn/en_us/opensearch-service/latest/developerguide/release-notes.html)
14. [Embedding — Vespa Documentation](https://docs.vespa.ai/en/rag/embedding.html)
15. [RAG Blueprint — Vespa Documentation](https://docs.vespa.ai/en/learn/tutorials/rag-blueprint.html)
16. [Late Interaction in Vespa](https://frutik.github.io/awesome-search/Topics/Late-Interaction-in-Vespa)
17. [Late interaction, or why ColBERT keeps coming back](https://datarekha.com/blog/late-interaction-retrieval/)
18. [From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents](https://arxiv.org/pdf/2604.01733v1)
19. [Benchmarking Retrieval Strategies for Biomedical Retrieval-Augmented Generation](https://arxiv.org/pdf/2605.02520)
20. [Caraman at SemEval-2026 Task 8: Three-Stage Multi-Turn Retrieval](https://aclanthology.org/2026.semeval-1.225.pdf)
21. [IIMAS-RAG at SemEval-2026 Task 8: Hybrid Sparse-Dense Retrieval](https://aclanthology.org/2026.semeval-1.345.pdf)
22. [ADR-256 Hybrid Sparse-Dense Search](http://raw.githubusercontent.com/ruvnet/ruvector/HEAD/docs/adr/ADR-256-hybrid-sparse-dense-search.md)