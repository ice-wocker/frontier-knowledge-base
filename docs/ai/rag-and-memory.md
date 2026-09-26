# RAG 与上下文工程（Context Engineering）与智能体记忆

> 最后更新：2026-09-26 ｜ 领域：人工智能 / 检索增强生成、上下文工程与记忆 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 一、概述

检索增强生成（Retrieval-Augmented Generation, RAG）曾长期被简化为「向量检索 + 拼接进提示词」的标准模式。Pinecone 自称是该范式的开创者与向量数据库品类定义者，并称其平台上有 80 万以上活跃开发者与 9000 多家付费客户（[Pinecone Nexus: The Knowledge Engine for Agents](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)）。但到 2025–2026 年，业界共识已转向：RAG 只是「上下文工程（context engineering）」这一更大工程学科中的一个检索手段，真正的准确率来自源数据治理、冲突消解、权限控制与综合（[Context Engineering vs RAG](https://getunblocked.com/blog/context-engineering-vs-rag/)）。

Anthropic 在 2025 年 9 月 29 日发布的工程博客中对这一转向给出了权威表述：构建 LLM 应用正从「为提示词寻找恰当词句」转向回答「什么样的上下文配置最可能产生我们期望的模型行为」（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。同一时期 Mei 等人的综述论文为上下文工程提供了学术骨架（[Beyond RAG: The Rise of Context Engineering](https://www.prateek-sharma.com/blog/beyond-rag-context-engineering/)）。

## 二、2025–2026 最新进展

- **从「检索」走向「知识编译」**：Pinecone 于 2026 年 5 月发布 Pinecone Nexus，将其定位为「知识引擎（knowledge engine）而非检索系统」，核心是**上下文编译器（context compiler）**与**可组合检索器（composable retriever）**，并推出声明式查询语言 **KnowQL**（含 intent、filter、provenance、output shape、confidence、budget 六个原语）（[Pinecone Nexus](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)）。
- **GraphRAG 的成本革命**：微软研究院提出的 LazyGraphRAG 把索引成本降到与向量 RAG 相同，仅为完整 GraphRAG 的 **0.1%**，同时在与向量 RAG 相当的查询成本下，在 local queries 上优于长上下文向量 RAG 与 GraphRAG DRIFT search（[LazyGraphRAG: Setting a new standard for quality and cost](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)）。GraphRAG 1.0 于 2024 年 12 月发布以改善开发者易用性（[Moving to GraphRAG 1.0](https://www.microsoft.com/en-us/research/blog/moving-to-graphrag-1-0-streamlining-ergonomics-for-developers-and-users/)）。
- **Agentic RAG 与混合图检索**：Qdrant 与 Neo4j 等组合出「图 + 向量」的混合检索，由 Agentic AI 编排；Data Graphs 构建的架构在知识图谱写入时实时嵌入非结构化属性，用 Qdrant 与图引擎作为互补检索层（[Build a GraphRAG Agent with Neo4j and Qdrant](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/)、[How Data Graphs Built a True Hybrid Graph RAG Platform](https://qdrant.tech/blog/case-study-datagraphs/)）。
- **智能体记忆独立成层**：Mem0、Letta（原 MemGPT）、Zep 等记忆中间件快速成熟，把记忆从「检索片段」提升为可管理、可衰减、可治理的独立组件。

## 三、核心技术与关键概念

### 1. 向量数据库

主流选择与定位（2026）：Qdrant 用 Rust 实现，以**单机低延迟与过滤式 ANN**见长；Milvus 2.5 面向**十亿级规模**，提供磁盘与 GPU 索引；Weaviate 内置混合检索与生成模块；Chroma 是面向原型与**智能体记忆**的最简 Python 方案；pgvector 0.8 适合「Postgres 已在运行你数据」的场景（[Open source vector databases: Qdrant vs Milvus vs Weaviate](https://botmonster.com/ai/open-source-vector-databases-qdrant-milvus-weaviate/)）。Milvus 采用存算分离的云原生架构，构建于 Faiss、HNSW、DiskANN、SCANN 等向量检索库之上，可支撑**超过 100 亿向量的集合**（[Milvus Architecture Overview](https://milvus.io/docs/architecture_overview.md)、[Comparing Milvus with Alternatives](https://milvus-io-dev.zilliz.cc/docs/v2.5.x/comparison.md)）。

### 2. 混合检索与重排序

纯向量检索会漏掉精确匹配，纯 BM25 关键词检索会漏掉语义相似性，因此生产系统普遍采用**混合检索**：数据显示混合检索相比纯稠密检索可带来约 **17% 的召回提升**，p50 延迟增加不到 **6ms**（[How to Build a Production-Ready RAG Pipeline in 2026](https://metafiedlab.com/blog/how-to-build-a-production-ready-rag-pipeline-in-2026/)）。典型流水线先用快速混合检索召回 **50–100** 个候选（约 10ms），再用交叉编码器（cross-encoder）对前 **20–30** 个做重排序（约 50–80ms），最终选取前 **5–8** 个送入 LLM 上下文（[RAG Pipeline Architecture: Chunking Strategies, Hybrid Search, Reranking, and Evaluation Frameworks](https://lucioduran.com/blog/rag-pipeline-architecture-chunking-reranking-evaluation)）。双编码器（bi-encoder）快而不精、交叉编码器准而慢，二者互补是该架构的核心权衡。

### 3. 长上下文 vs RAG

Gemini 是首个支持 **100 万 token** 上下文的模型（[Long context | Gemini API](https://developers.generativeai.google.com/gemini-api/docs/long-context)）。有中文技术分析称，截至 2025–2026 年，Gemini、Claude、GPT-5 系列等前沿模型上下文已进入百万 token 区间，其中 Claude Sonnet 4.6 支持最多 1M token（[RAG vs Long Context](https://ai-tldr.dev/learn/rag/rag-fundamentals/rag-vs-long-context/)）。但长上下文并不等于长上下文可用：学术研究《Retrieval Augmented Generation or Long-Context LLMs?》系统比较了二者并提出混合方案，指出长上下文 LLM 易受无关内容干扰、且可能丢失中段信息（[RAG or Long-Context LLMs? A Comprehensive Study and Hybrid Approach](https://arxiv.org/html/2407.16833v2)）。成本与延迟差距尤为悬殊：一项实验显示全上下文方案单次查询约 10 美分、耗时约 45 秒，而 RAG 约 0.008 美分、约 1 秒，成本比约 **1250 倍**、延迟比约 **45 倍**（[Lost in the Middle, 1,250x Cost: The Limits of Long-Context vs RAG](https://www.bestaiweb.ai/lost-in-the-middle-1-250x-cost-and-the-hard-technical-limits-of-long-context-vs-rag/)）。

### 4. 上下文工程（Context Engineering）

Anthropic 认为上下文是有限资源，并援引 Chroma 的「**context rot（上下文腐化）**」研究：随着上下文 token 增多，模型准确回忆信息的能力下降；LLM 与人一样拥有「**注意力预算**」，源于 Transformer 每个 token 需与其余 token 两两交互（n² 关系），上下文越长注意力越被摊薄（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、[Context Rot](https://research.trychroma.com/context-rot)）。其应对策略包括：

- **精炼高信号 token**：系统提示词「处于恰当高度」（既不过度硬编码 if-else，也非含糊过度概括），工具集保持最小可用、避免功能重叠，示例用少量多样、代表性强的 canonical examples。
- **Just-in-time 检索**：让智能体持有轻量标识符（文件路径、存储查询、网页链接），在运行时用工具动态加载数据；Claude Code 即采用此混合模式——`CLAUDE.md` 预先注入，而 `glob`/`grep` 支持即时的按需检索，绕过陈旧索引问题。
- **长任务技术**：**compaction（压缩）**（把接近上限的对话摘要后重启新上下文窗口）、**结构化笔记（structured note-taking）**、**多智能体架构（multi-agent architectures）**。

### 5. Chunking 策略

一项针对学术文本的检索增强评估研究比较了固定长度（fixed-sized）、递归（recursive）与基于聚类的 chunking 策略，并报告各类策略在忠实度（faithfulness）指标计算中约 42%–47% 出现失败（评测器超时或返回非法值），说明分块策略与评估稳定性仍是尚未收敛的问题（[Evaluating Chunking Strategies for RAG on Academic Texts](https://arxiv.org/html/2607.01852)）。另有研究采用「重叠语义分块 + 父文档元数据」并结合 BM25 与 BGE 稠密向量做二级混合检索（[DS@GT ARC at LongEval](https://arxiv.org/html/2607.14400v1)）。

### 6. 智能体记忆架构

记忆系统已成为独立技术层。**MemGPT**（现 Letta）提出操作系统式记忆层级：**core memory**（常驻上下文窗口，类比 CPU 寄存器）、**working memory**（容量有限的近期上下文）、**archival memory**（不进提示词、按需检索，类比磁盘）（[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/pdf/2310.08560.pdf)、[Mem0 vs Letta vs Zep](https://dev.to/plur9/mem0-vs-letta-vs-zep-which-should-you-use-for-agent-memory-1n8m)）。**Mem0** 采用两级架构：向量库做相似度检索，外加可选的图记忆层（Mem0ᵍ，把记忆表示为有向带标签图），并采用「单遍 ADD-only 抽取」与「多信号检索（语义相似 + 关键词匹配 + 实体匹配三路并行融合）」提升效果（[AI Agent Memory 2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026)、[How AI Agents Remember: Memory Architectures That Work](https://groundy.com/articles/how-ai-agents-remember-memory-architectures-that/)）。此外还有 MemMachine（保留 ground-truth 的长期记忆，先做句子级切分再索引）与 AgentMemBench（面向长期记忆管理策略的系统性基准）（[MemMachine](https://arxiv.org/pdf/2604.04853)、[AgentMemBench](https://arxiv.org/pdf/2608.00009)）。

### 7. 评估

**RAGAS** 是主流开源 RAG 评估框架，核心指标包括 **Faithfulness**（回答是否忠于检索上下文）、**AnswerRelevancy**（回答与问题的相关性）、**AnswerCorrectness**（与参考答案的吻合度）与 Context Recall 等，0.4 版起将指标迁移到 collections 体系（[RAGAS Metrics](https://docs.ragas.io/en/v0.3.0/references/metrics/)、[Migration from v0.3 to v0.4](https://docs.ragas.io/en/v0.4.1/howtos/migrations/migrate_from_v03_to_v04/)）。实践中，Faithfulness 低于 0.85 意味着「自信的错误答案」正在触达用户；而高 Faithfulness 叠加低 Context Recall 则表示系统在准确概括不完整的信息（[RAG Evaluation with RAGAS](https://dev.to/michael_pham018/rag-evaluation-with-ragas-faithfulness-context-recall-and-answer-relevance-5cb)）。新的诊断式框架（如 RAGVue）也在尝试对评估结果做可解释分解（[RAGVue](https://arxiv.org/html/2601.04196)）。

## 四、代表性项目 / 产品

| 项目 / 产品 | 定位 | 官方链接 |
| --- | --- | --- |
| Pinecone Nexus / KnowQL | Agentic 知识引擎与声明式查询语言 | https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/ |
| Microsoft GraphRAG / LazyGraphRAG | 知识图谱式全局检索 | https://www.microsoft.com/en-us/research/project/graphrag/ |
| Milvus | 云原生十亿级向量数据库 | https://milvus.io/docs/architecture_overview.md |
| Qdrant | Rust 高性能向量数据库（GraphRAG 混合检索） | https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/ |
| RAGAS | 开源 RAG 评估框架 | https://docs.ragas.io/ |
| Mem0 / Letta / Zep | 智能体记忆中间件 | https://mem0.ai/ |

## 五、关键数据与评测结果

- 混合检索相较纯稠密检索召回提升约 **17%**，p50 延迟增加 <6ms（[来源](https://metafiedlab.com/blog/how-to-build-a-production-ready-rag-pipeline-in-2026/)）。
- LazyGraphRAG 索引成本为完整 GraphRAG 的 **0.1%**，与向量 RAG 持平（[来源](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)）。
- 长上下文 vs RAG 的成本比约 **1250×**、延迟比约 **45×**（单模型单语料实验）（[来源](https://www.bestaiweb.ai/lost-in-the-middle-1-250x-cost-and-the-hard-technical-limits-of-long-context-vs-rag/)）。
- Pinecone 宣称 Nexus 可带来任务完成率 **>90%**、完成时间快 **30×**、token 消耗最多降低 **90%**（厂商自述数据）（[来源](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)）。
- 学术文本 chunking 研究中 Faithfulness 计算失败率达 **42%–47%**（[来源](https://arxiv.org/html/2607.01852)）。

## 六、趋势与争议

1. **「长上下文会不会杀死 RAG」仍是核心争论**。结论趋于折中：长上下文在单次、小语料、需要全局理解的场景更强，RAG 在成本、延迟、可治理性上仍占优，混合（先检索再长上下文推理）被普遍推荐（[RAG or Long-Context LLMs?](https://arxiv.org/html/2407.16833v2)、[Context Engineering vs RAG](https://getunblocked.com/blog/context-engineering-vs-rag/)）。
2. **从「检索」到「工程 + 治理」**：InfoWorld 2025 年的分析指出多数企业 RAG 失败源于上下文质量而非检索召回（[来源](https://getunblocked.com/blog/context-engineering-vs-rag/)）；Pinecone、Glean、LangChain 分别从知识层、平台层、基础设施层回应可靠性问题，但「谁来做上下文管理」仍有分歧（[Context engineering done right](https://www.k-ai.ai/en/news/context-engineering-clean-corpus-upstream-layer/)）。
3. **厂商基准的客观性存疑**：有分析提醒「最好按基准」往往出自厂商自测，且不存在通用冠军，应按规模、DevOps 能力与延迟要求选型（[Одних векторов ИИ-агенту мало](https://dev.to/promptra-team/odnikh-viektorov-ii-aghientu-malo-ghibrid-i-graphrag-mieniaiut-rag-25o7)）。
4. **记忆的隐私与治理**：记忆持久化带来 PII 标记（如 Pinecone 在摄入时打标、集中规则控制 LLM 处理）与权限（ACL-aware filtering）问题，是智能体落地的重要风险点（[来源](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)）。

## 参考来源

1. [Effective context engineering for AI agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
2. [Context Rot — Chroma Research](https://research.trychroma.com/context-rot)
3. [Pinecone Nexus: The Knowledge Engine for Agents](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)
4. [LazyGraphRAG: Setting a new standard for quality and cost — Microsoft Research](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
5. [Moving to GraphRAG 1.0 — Microsoft Research](https://www.microsoft.com/en-us/research/blog/moving-to-graphrag-1-0-streamlining-ergonomics-for-developers-and-users/)
6. [Project GraphRAG — Microsoft Research](https://www.microsoft.com/en-us/research/project/graphrag/)
7. [KET-RAG: A Cost-Efficient Multi-Granular Indexing Framework for Graph-RAG](https://arxiv.org/pdf/2502.09304v2.pdf)
8. [Build a GraphRAG Agent with Neo4j and Qdrant](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/)
9. [How Data Graphs Built a True Hybrid Graph RAG Platform — Qdrant](https://qdrant.tech/blog/case-study-datagraphs/)
10. [Long context — Gemini API Docs](https://developers.generativeai.google.com/gemini-api/docs/long-context)
11. [RAG vs Long Context — ai-tldr.dev](https://ai-tldr.dev/learn/rag/rag-fundamentals/rag-vs-long-context/)
12. [Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach](https://arxiv.org/html/2407.16833v2)
13. [Lost in the Middle, 1,250x Cost: The Limits of Long-Context vs RAG](https://www.bestaiweb.ai/lost-in-the-middle-1-250x-cost-and-the-hard-technical-limits-of-long-context-vs-rag/)
14. [RAGAS Metrics — 官方文档](https://docs.ragas.io/en/v0.3.0/references/metrics/)
15. [RAGAS: Migration from v0.3 to v0.4](https://docs.ragas.io/en/v0.4.1/howtos/migrations/migrate_from_v03_to_v04/)
16. [RAG Evaluation with RAGAS: Faithfulness, Context Recall, and Answer Relevance](https://dev.to/michael_pham018/rag-evaluation-with-ragas-faithfulness-context-recall-and-answer-relevance-5cb)
17. [RAGVue: A Diagnostic View for Explainable and Automated Evaluation of RAG](https://arxiv.org/html/2601.04196)
18. [Milvus Architecture Overview](https://milvus.io/docs/architecture_overview.md)
19. [Comparing Milvus with Alternatives](https://milvus-io-dev.zilliz.cc/docs/v2.5.x/comparison.md)
20. [Open source vector databases: Qdrant vs Milvus vs Weaviate](https://botmonster.com/ai/open-source-vector-databases-qdrant-milvus-weaviate/)
21. [How to Build a Production-Ready RAG Pipeline in 2026](https://metafiedlab.com/blog/how-to-build-a-production-ready-rag-pipeline-in-2026/)
22. [RAG Pipeline Architecture: Chunking, Hybrid Search, Reranking, Evaluation](https://lucioduran.com/blog/rag-pipeline-architecture-chunking-reranking-evaluation)
23. [Evaluating Chunking Strategies for RAG on Academic Texts](https://arxiv.org/html/2607.01852)
24. [DS@GT ARC at LongEval: Citation Integrity and Factual Grounding in Scientific QA](https://arxiv.org/html/2607.14400v1)
25. [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/pdf/2310.08560.pdf)
26. [Mem0 vs Letta vs Zep: Which Should You Use for Agent Memory?](https://dev.to/plur9/mem0-vs-letta-vs-zep-which-should-you-use-for-agent-memory-1n8m)
27. [AI Agent Memory 2026: Progress Benchmark Report — Mem0](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
28. [How AI Agents Remember: Memory Architectures That Work](https://groundy.com/articles/how-ai-agents-remember-memory-architectures-that/)
29. [MemMachine: A Ground-Truth-Preserving Memory System](https://arxiv.org/pdf/2604.04853)
30. [AgentMemBench: A Systematic Benchmark for Long-Term Memory Management](https://arxiv.org/pdf/2608.00009)
31. [Beyond RAG: The Rise of Context Engineering](https://www.prateek-sharma.com/blog/beyond-rag-context-engineering/)
32. [Context Engineering vs RAG: When to Use Which Approach](https://getunblocked.com/blog/context-engineering-vs-rag/)
33. [Context engineering done right — k-ai.ai](https://www.k-ai.ai/en/news/context-engineering-clean-corpus-upstream-layer/)
34. [Одних векторов ИИ-агенту мало: гибрид и graphrag меняют RAG](https://dev.to/promptra-team/odnikh-viektorov-ii-aghientu-malo-ghibrid-i-graphrag-mieniaiut-rag-25o7)
35. [H-RAG at SemEval-2026 Task 8: Hierarchical Parent–Child Retrieval](https://arxiv.org/pdf/2605.00631.pdf)