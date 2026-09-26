# RAG 与上下文工程（Context Engineering）与智能体记忆

> 最后更新：2026-09-26 ｜ 领域：人工智能 / 检索增强生成、上下文工程与记忆 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 一、概述

检索增强生成（Retrieval-Augmented Generation, RAG）曾长期被简化为「向量检索 + 拼接进提示词」的标准模式。Pinecone 自称是该范式的开创者与向量数据库品类定义者，并称其平台上有 80 万以上活跃开发者与 9000 多家付费客户（[Pinecone Nexus: The Knowledge Engine for Agents](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)）。但到 2025–2026 年，业界共识已转向：RAG 只是「上下文工程（context engineering）」这一更大工程学科中的一个检索手段，真正的准确率来自源数据治理、冲突消解、权限控制与综合（[Context Engineering vs RAG](https://getunblocked.com/blog/context-engineering-vs-rag/)）。

Anthropic 在 2025 年 9 月 29 日发布的工程博客中对这一转向给出了权威表述：构建 LLM 应用正从「为提示词寻找恰当词句」转向回答「什么样的上下文配置最可能产生我们期望的模型行为」（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。同一时期 Mei 等人的综述论文为上下文工程提供了学术骨架（[Beyond RAG: The Rise of Context Engineering](https://www.prateek-sharma.com/blog/beyond-rag-context-engineering/)）。这一框架在 2026 年进一步固化：有分析认为，「上下文工程」已是提示工程的「生产级继任者」，2026 年多数输出质量的高低就取决于此（[Context Engineering in 2026: Provider-Agnostic Patterns After Claude 5](https://www.edenai.co/post/context-engineering-in-provider-agnostic-patterns-after-claude-5)）。

另一条与 RAG 并行演进的线索是「记忆」：到 2026 年，记忆已从「更长的提示词」升级为独立的架构层，被一些分析直接称为「新的 RAG」，即不再是可选优化而是生产系统的基础设施（[Memory Is the New RAG: Inside the Agent Memory Stack of 2026](https://www.xyzbytes.com/blog/ai-agent-memory-infrastructure-2026)）。本文因此同时覆盖检索、上下文工程与智能体记忆三条脉络。

## 二、2025–2026 最新进展

- **从「检索」走向「知识编译」**：Pinecone 于 2026 年 5 月发布 Pinecone Nexus，将其定位为「知识引擎（knowledge engine）而非检索系统」，核心是**上下文编译器（context compiler）**与**可组合检索器（composable retriever）**，并推出声明式查询语言 **KnowQL**（含 intent、filter、provenance、output shape、confidence、budget 六个原语）（[Pinecone Nexus](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)）。
- **系统提示词「大瘦身」**：2026 年 7 月 24 日，Anthropic 发布《The new rules of context engineering for Claude 5 generation models》，称已为最先进模型删减 Claude Code 超过 **80%** 的系统提示词且无可测量的性能损失，并把 `context` 视为跨请求复用的资产（系统提示、Skills、`CLAUDE.md`、memory 均属上下文来源）（[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)、[Anthropic's new context-engineering rules](https://ai-tldr.dev/releases/anthropic-context-engineering-claude-5-rules/)）。
- **Compaction 成为 API 原语**：Anthropic 把压缩（compaction）做成可调用的 API 能力，标识为 `compact_20260112`，由 token 阈值触发（最小 50K、默认 150K），用于治理会话内的上下文膨胀（[Anthropic Context Engineering](https://agentic-ai.readthedocs.io/en/latest/ContextEngineering/anthropic/)）。
- **GraphRAG 的成本革命**：微软研究院提出的 LazyGraphRAG 把索引成本降到与向量 RAG 相同，仅为完整 GraphRAG 的 **0.1%**，同时在与向量 RAG 相当的查询成本下，在 local queries 上优于长上下文向量 RAG 与 GraphRAG DRIFT search（[LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)）。GraphRAG 1.0 于 2024 年 12 月发布以改善开发者易用性（[Moving to GraphRAG 1.0](https://www.microsoft.com/en-us/research/blog/moving-to-graphrag-1-0-streamlining-ergonomics-for-developers-and-users/)）。
- **Agentic RAG 进入企业平台**：Google Research 与 Google Cloud 联合推出 agentic RAG 框架，思路是先拆解复杂企业问题、反复检索确认信息充足再生成（[RAG 还在说"我信息不够"?谷歌这套 Agentic RAG](https://blog.csdn.net/yanqianglifei/article/details/161802790)）。IBM 推出 agentic 检索框架 **OpenRAG**，运行于 watsonx.data 之上，强调治理、安全与混合检索（[Traditional RAG isn't enough: How to close the AI context gap with agentic RAG](https://www.ibm.com/campaign/guidebooks/context-gap-agentic-rag)）；微软 Azure Arc 的 Edge RAG 更名为 **Agentic Retrieval**，在边缘加入智能体编排层，支持多步会话与外部工具调用（[What's new in Agentic Retrieval in Foundry Local](https://learn.microsoft.com/fil-ph/azure/azure-arc/agents-tools-foundry-local/whats-new)）。微软 Azure AI Foundry 的文档进一步把 agentic retrieval 定义为「用模型把复杂输入拆成多个聚焦的子查询、并行执行并返回结构化 grounding 数据」，相比经典 RAG 增加了上下文感知的查询规划、并行执行与多轮对话中的指代保留（[Retrieval augmented generation (RAG) and indexes — Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation?view=foundry)）。
- **学术架构收敛为「渐进式证据获取」**：一项针对监管合规场景的研究把演进路径归纳为 naive RAG → 混合检索+重排 → agentic function-calling 检索 → 深度多智能体架构（含代码化工具合成与显式规划），并形式化为 **PEA-CAE（Progressive Evidence Acquisition with Cost-Aware Escalation）**：先用低成本高精度检索，仅在预期证据收益足以抵偿延迟时才升级为全文阅读（[From Naive RAG to Deep Agentic Retrieval](https://arxiv.org/abs/2607.24791v1)）。ACE-GraphRAG 则提出「表示—推理鸿沟」，在推理期加入上下文策略层，用「并行差分检索」从深度（事实）与广度（语义）两支补充证据（[ACE-GraphRAG](https://arxiv.org/abs/2608.01269v1)）。
- **智能体记忆独立成层**：Mem0、Letta（原 MemGPT）、Zep 等记忆中间件快速成熟，把记忆从「检索片段」提升为可管理、可衰减、可治理的独立组件。生产实践中，工具调用（retrieval、执行代码、查询数据库、抓取文档）负责把计划变成行动，而记忆负责让循环在多步之间保持连贯：短期记忆保存当前计划与中间结果，长期记忆则持久化用户偏好或此前已验证的事实（[From Static to Smart: Agentic RAG for Enterprise AI](https://unstructured.io/insights/from-static-to-smart-agentic-rag-for-enterprise-ai)）。

## 三、核心技术与关键概念

### 1. 向量数据库

主流选择与定位（2026）：Qdrant 用 Rust 实现，以**单机低延迟与过滤式 ANN**见长，把 payload 过滤放进检索内部（而非前置或后置）；Milvus 面向**十亿级规模**，3.0 版本转向「lake-native」以适配超大规模自托管；Weaviate 内置混合检索与生成模块；Chroma 是面向原型与**智能体记忆**的最简 Python 方案；pgvector 适合「Postgres 已在运行你数据」的中小规模场景；Pinecone 为全托管 serverless 方案（[Best Vector Database in 2026](https://www.layer3labs.io/comparisons/best-vector-databases)、[Top Vector Databases for Enterprise AI: 2026 Comparison](https://atlan.com/know/top-vector-databases-enterprise-ai/)）。

一项 2026 年企业级对比给出的实测（相同硬件）结论是：等召回率下 Qdrant 的 QPS 约为 Milvus 的 **5–6 倍**；托管方案月成本上 Qdrant Cloud 约 **$250–450**、Zilliz 约 **$600+**、Pinecone 约 **$1,300+**（10M×1536 向量口径），自托管单节点 Qdrant 最低（[Enterprise Vector Database 2026](https://dev.to/devrudals/enterprise-vector-database-2026-qdrant-vs-milvus-vs-pgvector-vs-pinecone-16a0)）。另一份对比给出 p50 延迟：Qdrant 9ms、Milvus 12ms、Weaviate 15ms、Pinecone 18ms；吞吐上限 Qdrant 约 1800 QPS、Milvus 约 1400、Weaviate 约 900、Pinecone 约 500（[Perbandingan Vector Database 2026](https://aiworkflowlab.dev/id/article/perbandingan-vector-database-2026-rag-produksi)）。此外还有分析认为 Pinecone 已通过补充混合检索与元数据过滤、价格下调而重新适配中端场景（[Best Vector Databases 2026](https://scored.tools/downloads/best-vector-databases-2026.pdf)）。各口径测试条件不同，不能直接横向定论。

一份学术实证评测在同一数据集上给出另一组口径：在 SIFT1M 上，FAISS 取得最高单节点吞吐（866 QPS）但缺乏数据库运维能力；Weaviate 的默认召回最佳（>99%）；Qdrant 在完整数据库中延迟最低（中位 4.55ms）；LanceDB 则以牺牲部分检索质量换取显著更快的索引构建（[A Comprehensive Empirical Evaluation of Vector Database Systems for ANN Search — arXiv 2608.12812](https://arxiv.org/pdf/2608.12812)）。AIMultiple 的开放源码基准（32 进程）则给出 Weaviate 8330、Milvus 5063、pgvector 4832、Qdrant 1859 QPS 的吞吐差异，并在混合检索上记录 nDCG 增益：LanceDB +0.063、Redis +0.049、Milvus +0.044、pgvector +0.037（[Vector Database Benchmark: 7 Open-Source Engines for RAG](https://aimultiple.com/open-source-vector-databases)）。在运维维度上，有分析对比多租户与负载下重建：Pinecone 依赖 serverless 后台构建、Qdrant 采用 LSM segment 合并、Milvus 通过对象存储解耦 IndexNode、pgvector 用 `CREATE INDEX CONCURRENTLY`（会争用 CPU/内存）（[Vector Databases for Production RAG (2026)](https://dev.to/locionic/vector-databases-for-production-rag-2026-pinecone-vs-qdrant-vs-milvus-vs-pgvector-4fim)）。

### 2. 混合检索与重排序

纯向量检索会漏掉精确匹配，纯 BM25 关键词检索会漏掉语义相似性，因此生产系统普遍采用**混合检索**：数据显示混合检索相比纯稠密检索可带来约 **17% 的召回提升**，p50 延迟增加不到 **6ms**（[How to Build a Production-Ready RAG Pipeline in 2026](https://metafiedlab.com/blog/how-to-build-a-production-ready-rag-pipeline-in-2026/)）。典型流水线先用快速混合检索召回 **50–100** 个候选（约 10ms），再用交叉编码器（cross-encoder）对前 **20–30** 个做重排序（约 50–80ms），最终选取前 **5–8** 个送入 LLM 上下文（[RAG Pipeline Architecture](https://lucioduran.com/blog/rag-pipeline-architecture-chunking-reranking-evaluation)）。双编码器（bi-encoder）快而不精、交叉编码器准而慢，二者互补是该架构的核心权衡。

### 3. 长上下文 vs RAG

Gemini 是首个支持 **100 万 token** 上下文的模型（[Long context | Gemini API](https://developers.generativeai.google/docs/long-context)）。有中文技术分析称，截至 2025–2026 年，前沿模型上下文已进入百万 token 区间，其中 Claude Sonnet 4.6 支持最多 1M token（[RAG vs Long Context](https://ai-tldr.dev/learn/rag/rag-fundamentals/rag-vs-long-context/)）。但长上下文并不等于可用：学术研究《Retrieval Augmented Generation or Long-Context LLMs?》系统比较了二者并提出混合方案，指出长上下文 LLM 易受无关内容干扰、且可能丢失中段信息（[RAG or Long-Context LLMs?](https://arxiv.org/html/2407.16833v2)）。

新证据进一步量化了这条权衡线：

- 「认知准确性的 token 税」研究用专家验证基准、3 个模型、972 个答案比较长上下文与语义 RAG：长上下文正确率最高（**73.1% vs 语义 RAG 的 65.4%**），但单查询 token 成本为后者的 **26 倍**（[The Token Tax of Epistemic Accuracy](https://arxiv.org/html/2606.20898)）。
- RULER 类基准显示，多数模型从 4K 扩到 128K 上下文时准确率下降 **15%–30%**，且失败并非随机：受 RoPE 顺序编码影响，位于长提示中部的信息被回忆的可靠性显著低于首尾（[2M-token context vs RAG in 2026](https://dev.to/mr_manushukla/2m-token-context-vs-rag-in-2026-cost-latency-and-when-each-actually-wins-5h1o)）。
- LongBench v2 中人类专家在限时下得 **53.7%**，最佳直答模型仅 **50.1%**；NoLiMa 中去除关键词重叠后，13 个长上下文模型有 **11 个**在 32K 时跌破其短上下文基线的一半（[Long-Context AI vs. RAG for Document Analysis Compared](https://intuitionlabs.ai/articles/long-context-ai-vs-retrieval-rag)）。
- 一份多针检索对比（1M 上下文）：Gemini 3 Deep Think 单针 99%/多针 89%、GPT-5.5 96%/74%、Claude Opus 4.7 89%/56%、DeepSeek V4-Pro 78%/41%（[Long context vs RAG en 2026](https://ianas.fr/blog/2026/05/20/long-context-vs-rag-quand-utiliser/)）。
- 成本/延迟实验（300 页文档）：Long Context 约 **$2.37 / 21.7s** 且在第 15–20 问后出现精度退化；模块化 RAG 约 **$0.028 / 8.1s** 且精度平稳（[RAG, поиск и LongContext](https://habr.com/ru/companies/bothub/articles/1081080/)）。

### 4. 上下文工程（Context Engineering）

Anthropic 认为上下文是有限资源，并援引 Chroma 的「**context rot（上下文腐化）**」研究：随着上下文 token 增多，模型准确回忆信息的能力下降；LLM 与人一样拥有「**注意力预算**」，源于 Transformer 每个 token 需与其余 token 两两交互（n² 关系），上下文越长注意力越被摊薄（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、[Context Rot](https://research.trychroma.com/context-rot)）。关于该研究的规模，第三方复述指出 Chroma 于 2025 年 7 月发布《Context Rot: How Increasing Input Tokens Impacts LLM Performance》，测试了 **18 个模型、194,480 次 LLM 调用**，发现每个模型都随输入变长而退化，且退化早于窗口填满；诱因包括输入长度、干扰项、目标事实与查询的匹配度以及周围文本的结构（[Context Rot: Why LLMs Degrade Long Before the Window Fills](https://www.datallmlab.com/blog/context-rot.html)）。有分析把退化幅度量化为「准确率从 95% 降到 60–70%」，并强调更大窗口并不能修复该问题、反而可能更糟（[Context Rot: Why AI Performance Degrades With More Information](https://usewire.io/blog/context-rot-why-ai-performance-degrades/)）；另有分析指出，即便标称 1M 窗口的模型，在 **50K token** 处已出现可测量的退化，Adobe Research 的 NoLiMa 基准（arXiv 2502.05167，ICML 2025）也记录了类似现象（[Claude Context Window Size (2026)](https://www.morphllm.com/claude-context-window)、[Context Rot: The Complete Guide](https://www.morphllm.com/context-rot)）。其应对策略包括：

- **精炼高信号 token**：系统提示词「处于恰当高度」（既不过度硬编码 if-else，也非含糊过度概括），工具集保持最小可用、避免功能重叠，示例用少量多样、代表性强的 canonical examples。
- **Just-in-time 检索**：让智能体持有轻量标识符（文件路径、存储查询、网页链接），在运行时用工具动态加载数据；Claude Code 即采用此混合模式——`CLAUDE.md` 预先注入，而 `glob`/`grep` 支持即时的按需检索，绕过陈旧索引问题。
- **长任务技术**：**compaction（压缩）**（把接近上限的对话摘要后重启新上下文窗口）、**结构化笔记（structured note-taking）**、**多智能体架构（multi-agent architectures）**。

在生产落地层面，有实践总结指出：以结构化形式（表格、JSON、项目符号列表）而非平铺文本呈现信息，通常能减少 token；长任务中应把短期工作记忆与长期持久记忆分离，按需从长期记忆拉取；组合上述手法的上下文工程方法被报告可降低约 **19% 的 token 用量**（[Context Engineering in Agentic RAG: Production Patterns That Cut Token Cost (2026)](https://sukruyusufkaya.com/en/blog/agentic-rag-baglam-muhendisligi-token-optimizasyonu-2026)）。记忆分类上，一种常见划分把智能体记忆分为**工作记忆**（当前任务的实时上下文窗口）、**语义记忆**（关于环境的事实与世界知识，按需检索，即经典 RAG 模式）、**情景记忆**（具体过往经验或任务实例的记录）与**程序性记忆**（[Context Engineering: System-Level Context Design for AI Agents](https://zylos.ai/research/2026-07-14-context-engineering-system-level-context-design-ai-agents/)）。

### 5. Chunking 策略

一项针对学术文本的检索增强评估研究比较了固定长度（fixed-sized）、递归（recursive）与基于聚类的 chunking 策略，并报告各类策略在忠实度（faithfulness）指标计算中约 42%–47% 出现失败（评测器超时或返回非法值），说明分块策略与评估稳定性仍是尚未收敛的问题（[Evaluating Chunking Strategies for RAG on Academic Texts](https://arxiv.org/html/2607.01852)）。另有研究采用「重叠语义分块 + 父文档元数据」并结合 BM25 与 BGE 稠密向量做二级混合检索（[DS@GT ARC at LongEval](https://arxiv.org/html/2607.14400v1)）。

2026 年的分块实践进一步收敛出几类主流策略（[Advanced RAG Chunking Techniques in 2026](https://futureagi.com/blog/advanced-chunking-techniques-for-rag/)、[Chunking strategies for RAG pipelines: A practical guide for 2026](https://www.dronahq.com/chunking-strategies/)）：

- **Late chunking（后置分块）**：由 Jina AI 于 2024 年提出（Gunther 等，arXiv 2409.04701），先以长上下文嵌入器嵌入整篇文档，再把 token 级嵌入按 chunk 做均值池化切分，使每个 chunk 向量自带全文语境，从而改善「指代缺失」问题。
- **Parent-child / 层级分块**：用较小的 child chunk（常见 100–200 token）做精准检索，命中后返回其所属的较大 parent chunk 供生成，从而解耦「检索精度」与「生成上下文」，是长企业文档中较有效但常被低估的策略。
- **Semantic chunking / Sentence-window retrieval**：前者按主题变化切分，后者在返回单句命中时附带其周围窗口，以兼顾精度与上下文。

### 6. 智能体记忆架构

记忆系统已成为独立技术层。**MemGPT**（现 Letta）提出操作系统式记忆层级：**core memory**（常驻上下文窗口，类比 CPU 寄存器）、**working memory**（容量有限的近期上下文）、**archival memory**（不进提示词、按需检索，类比磁盘）（[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/pdf/2310.08560.pdf)）。**Mem0** 采用两级架构：向量库做相似度检索，外加可选的图记忆层（Mem0ᵍ），并采用「单遍 ADD-only 抽取」与「多信号检索（语义相似 + 关键词匹配 + 实体匹配三路并行融合）」（[AI Agent Memory 2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026)、[How AI Agents Remember](https://groundy.com/articles/how-ai-agents-remember-memory-architectures-that/)）。

2026 年的记忆基准表现（各厂商/第三方口径并存）：Mem0 报告 LoCoMo **92.5%**、LongMemEval **94.4%**（当前算法，平均约 6900 token/查询），Zep 在 LongMemEval（GPT-4o）为 **71.2%**、LoCoMo 约 **80.32% @189ms**（[AI Agent Memory 2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026)）。Mem0 侧对比表称 LongMemEval 93.4 vs Zep 71.2、LoCoMo 91.6 vs 80.32，而 Zep 在自有 DMR 基准为 94.8、Mem0 未公开（[Zep vs Mem0](https://mem0.ai/blog/zep-vs-mem0-which-ai-memory-layer-should-you-choose)）；Zep 官方页面则给出 Zep 准确率 **90.2%**、检索 p50 **104ms** 对比 Mem0 **2,470ms**、上下文体积小 **35%**（4,408 vs 6,787 token）（[Agent memory built for production](https://www.getzep.com/mem0-alternative/)）。另一份 Mem0 侧的对比把 Letta 记为 LoCoMo 74.0、LongMemEval「未公布」，并在 BEAM 基准给出 Mem0 64.1/48.6（[Mem0 vs Letta](https://mem0.ai/compare/mem0-vs-letta)）。第三方复现则记录 Mem0 LoCoMo 92.5/LongMemEval 94.4、Zep LongMemEval 71.2、Supermemory LongMemEval-S 81.6，并给出 AutoMem 自测 LoCoMo 84.74%、LongMemEval 87.00%、recall@5 97.00%（[Agent Memory in 2026: An Honest Comparison](https://automem.ai/blog/agent-memory-in-2026-an-honest-comparison-of-mem0-zep-letta-and-the-rest)）。有分析指出，记忆中间件对比文档往往带有厂商立场，需交叉核验（[Agent Memory in 2026](https://automem.ai/blog/agent-memory-in-2026-an-honest-comparison-of-mem0-zep-letta-and-the-rest)）。评估上，业界通常用 LoCoMo（跨多会话长对话的记忆）与 LongMemEval（长历史下的长期记忆召回与推理）两个基准，因为记忆的失败模式是「时序性」的——必须在对的时间想起对的事实，而单轮基准无法覆盖（[LLM Evaluation Framework — Zep](https://www.getzep.com/ai-agents/llm-evaluation-framework/)）。此外还有 MemMachine（保留 ground-truth 的长期记忆）与 AgentMemBench（长期记忆管理基准）（[MemMachine](https://arxiv.org/pdf/2604.04853)、[AgentMemBench](https://arxiv.org/pdf/2608.00009)）。在成本维度上，有分析给出量级对比：记忆层在 LoCoMo 基准上每次调用约检索 **6,956 token**，而全上下文加载约 **26,000 token**（[Memory Is the New RAG](https://www.xyzbytes.com/blog/ai-agent-memory-infrastructure-2026)）。

### 7. 评估

**RAGAS** 是主流开源 RAG 评估框架，核心指标包括 **Faithfulness**（回答的每条声明是否都能由检索上下文支持，取值 0–1）、**AnswerRelevancy**、**AnswerCorrectness** 与 Context Recall 等，0.4 版起将指标迁移到 collections 体系（[RAGAS Faithfulness 指标](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/)、[Migration from v0.3 to v0.4](https://docs.ragas.io/en/v0.4.1/howtos/migrations/migrate_from_v03_to_v04/)）。实践中，Faithfulness 低于 0.85 意味着「自信的错误答案」正在触达用户；而高 Faithfulness 叠加低 Context Recall 则表示系统在准确概括不完整的信息（[RAG Evaluation with RAGAS](https://dev.to/michael_pham018/rag-evaluation-with-ragas-faithfulness-context-recall-and-answer-relevance-5cb)）。到 2026 年，四个核心指标（faithfulness、answer relevance、context precision、context recall）已成为事实标准，可用开源框架自动打分（[RAG Evaluation 2026: The Four Core Metrics and How to Read Them Diagnostically](https://dev.to/saaro_net/rag-evaluation-2026-the-four-core-metrics-and-how-to-read-them-diagnostically-1nk8)、[RAG Evaluation Explained: Top Metrics, Tools & Blindspots in 2026](https://atlan.com/know/how-to-evaluate-rag-systems-explained/)）。RAGAS 已在 ESG 等领域作为标准评估工具（结合 contextual recall/precision/relevance 等）（[Empirical Evaluation of Open-Source LLMs for RAG in ESG Domain](https://arxiv.org/abs/2609.15242)），RAGVue 等诊断式框架也在尝试对评估结果做可解释分解（[RAGVue](https://arxiv.org/html/2601.04196)）。

## 四、代表性项目 / 产品

| 项目 / 产品 | 定位 | 官方链接 |
| --- | --- | --- |
| Pinecone Nexus / KnowQL | Agentic 知识引擎与声明式查询语言 | https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/ |
| Microsoft GraphRAG / LazyGraphRAG | 知识图谱式全局检索 | https://www.microsoft.com/en-us/research/project/graphrag/ |
| IBM OpenRAG（watsonx.data） | 企业级 agentic 检索框架 | https://www.ibm.com/campaign/guidebooks/context-gap-agentic-rag |
| Milvus | 云原生十亿级向量数据库 | https://milvus.io/docs/architecture_overview.md |
| Qdrant | Rust 高性能向量数据库（GraphRAG 混合检索） | https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/ |
| RAGAS | 开源 RAG 评估框架 | https://docs.ragas.io/ |
| Mem0 / Letta / Zep | 智能体记忆中间件 | https://mem0.ai/ |

## 五、关键数据与评测结果

- 混合检索相较纯稠密检索召回提升约 **17%**，p50 延迟增加 <6ms（[来源](https://metafiedlab.com/blog/how-to-build-a-production-ready-rag-pipeline-in-2026/)）。
- LazyGraphRAG 索引成本为完整 GraphRAG 的 **0.1%**，与向量 RAG 持平；其做法是把昂贵的 LLM 摘要推迟到查询时，索引期只用轻量 NLP（NER 等）构图（[来源](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)、[How to Build GraphRAG Pipelines with Python](https://aiworkflowlab.dev/article/how-to-build-graphrag-pipelines-with-python-knowledge-graphs-for-smarter-retrieval)）。有分析给出成本示例：完整 GraphRAG 年成本约 $121,000，而 LazyGraphRAG 索引成本显著更低（[What is LazyGraphRAG?](https://www.articsledge.com/post/lazygraphrag-retrieval-augmented-generation)）；亦有总结称 LazyGraphRAG 的全局查询可在质量与完整 GraphRAG 相当的前提下把成本降至约 1/700（[Graph Rag — nemorize](https://nemorize.com/roadmaps/2026-modern-ai-search-rag-roadmap/lessons/graph-rag)）。
- 长上下文 RAG 正确率 **73.1% vs 65.4%**，但 token 成本 **26×**（[来源](https://arxiv.org/html/2606.20898)）；另有实验给出成本比约 **1250×**、延迟比约 **45×**（[来源](https://www.bestaiweb.ai/lost-in-the-middle-1-250x-cost-and-the-hard-technical-limits-of-long-context-vs-rag/)）。
- Anthropic 为 Claude 5 删减 Claude Code 系统提示词 **>80%**，无可测量性能损失（[来源](https://ai-tldr.dev/releases/anthropic-context-engineering-claude-5-rules/)）。
- Pinecone 宣称 Nexus 可带来任务完成率 **>90%**、完成时间快 **30×**、token 消耗最多降低 **90%**（厂商自述数据）（[来源](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)）。
- 学术文本 chunking 研究中 Faithfulness 计算失败率达 **42%–47%**（[来源](https://arxiv.org/html/2607.01852)）。
- 记忆系统基准（厂商/第三方口径并存）：Mem0 LoCoMo 92.5 / LongMemEval 94.4；Zep LongMemEval 71.2、LoCoMo ~80.3% @189ms（[来源](https://mem0.ai/blog/state-of-ai-agent-memory-2026)）。
- 上下文腐化研究规模：Chroma 于 2025 年 7 月用 **18 个模型、194,480 次调用**验证「随输入增长而退化」（[来源](https://www.datallmlab.com/blog/context-rot.html)）。
- 上下文工程组合手法被报告可降低约 **19% token 用量**（[来源](https://sukruyusufkaya.com/en/blog/agentic-rag-baglam-muhendisligi-token-optimizasyonu-2026)）。

## 六、趋势与争议

1. **「长上下文会不会杀死 RAG」仍是核心争论**。结论趋于折中：长上下文在单次、小语料、需要全局理解的场景更强，RAG 在成本、延迟、可治理性上仍占优，混合（先检索再长上下文推理）被普遍推荐（[RAG or Long-Context LLMs?](https://arxiv.org/html/2407.16833v2)、[Context Engineering vs RAG](https://getunblocked.com/blog/context-engineering-vs-rag/)）。但「token 税」与「lost in the middle」研究说明，长上下文的可用窗口远小于其标称窗口。
2. **从「检索」到「工程 + 治理」**：多数企业 RAG 失败源于上下文质量而非检索召回（[来源](https://getunblocked.com/blog/context-engineering-vs-rag/)）；Pinecone、Glean、LangChain 分别从知识层、平台层、基础设施层回应可靠性问题，但「谁来做上下文管理」仍有分歧（[Context engineering done right](https://www.k-ai.ai/en/news/context-engineering-clean-corpus-upstream-layer/)）。Anthropic 削减 80% 系统提示词的做法，反向印证「冗余上下文有害」。
3. **GraphRAG 从「昂贵」走向「可负担」**：LazyGraphRAG 把索引成本压到与向量 RAG 同量级后，行业建议把它作为默认起点，只在确有必要时才用完整 GraphRAG（[GraphRAG: when knowledge graphs beat vector search](https://datarekha.com/blog/graphrag-when-graphs-beat-vectors/)、[Graph Rag — nemorize](https://nemorize.com/roadmaps/2026-modern-ai-search-rag-roadmap/lessons/graph-rag)）。
4. **厂商基准的客观性存疑**：记忆与向量库对比多出自厂商自测或带立场内容，不存在通用冠军，应按规模、DevOps 能力与延迟要求选型（[Agent Memory in 2026](https://automem.ai/blog/agent-memory-in-2026-an-honest-comparison-of-mem0-zep-letta-and-the-rest)、[Vector Database Benchmark: 7 Open-Source Engines for RAG](https://aimultiple.com/open-source-vector-databases)）。
5. **记忆的隐私与治理**：记忆持久化带来 PII 标记与权限（ACL-aware filtering）问题，是智能体落地的重要风险点（[来源](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)）。
6. **架构复杂度本身成为成本**：PEA-CAE 等工作强调「成本感知升级」，即并非越复杂的 agentic 流程越好，而应在证据收益与延迟/成本间显式权衡（[From Naive RAG to Deep Agentic Retrieval](https://arxiv.org/abs/2607.24791v1)）。

## 参考来源

1. [Effective context engineering for AI agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
2. [Context Rot — Chroma Research](https://research.trychroma.com/context-rot)
3. [The new rules of context engineering for Claude 5 generation models — Claude](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
4. [Anthropic's new context-engineering rules — ai-tldr.dev](https://ai-tldr.dev/releases/anthropic-context-engineering-claude-5-rules/)
5. [Context Engineering in 2026: Provider-Agnostic Patterns After Claude 5 — edenai](https://www.edenai.co/post/context-engineering-in-provider-agnostic-patterns-after-claude-5)
6. [Anthropic Context Engineering — agentic-ai.readthedocs.io](https://agentic-ai.readthedocs.io/en/latest/ContextEngineering/anthropic/)
7. [Pinecone Nexus: The Knowledge Engine for Agents](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/)
8. [LazyGraphRAG: Setting a new standard for quality and cost — Microsoft Research](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)
9. [Moving to GraphRAG 1.0 — Microsoft Research](https://www.microsoft.com/en-us/research/blog/moving-to-graphrag-1-0-streamlining-ergonomics-for-developers-and-users/)
10. [Project GraphRAG — Microsoft Research](https://www.microsoft.com/en-us/research/project/graphrag/)
11. [Traditional RAG isn't enough: How to close the AI context gap with agentic RAG — IBM](https://www.ibm.com/campaign/guidebooks/context-gap-agentic-rag)
12. [What's new in Agentic Retrieval in Foundry Local — Microsoft Learn](https://learn.microsoft.com/fil-ph/azure/azure-arc/agents-tools-foundry-local/whats-new)
13. [RAG 还在说"我信息不够"?谷歌这套 Agentic RAG — CSDN](https://blog.csdn.net/yanqianglifei/article/details/161802790)
14. [From Naive RAG to Deep Agentic Retrieval — arXiv 2607.24791](https://arxiv.org/abs/2607.24791v1)
15. [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG — arXiv 2608.01269](https://arxiv.org/abs/2608.01269v1)
16. [KET-RAG: A Cost-Efficient Multi-Granular Indexing Framework for Graph-RAG](https://arxiv.org/pdf/2502.09304v2.pdf)
17. [Build a GraphRAG Agent with Neo4j and Qdrant](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/)
18. [How Data Graphs Built a True Hybrid Graph RAG Platform — Qdrant](https://qdrant.tech/blog/case-study-datagraphs/)
19. [Long context — Gemini API Docs](https://developers.generativeai.google/docs/long-context)
20. [RAG vs Long Context — ai-tldr.dev](https://ai-tldr.dev/learn/rag/rag-fundamentals/rag-vs-long-context/)
21. [Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach](https://arxiv.org/html/2407.16833v2)
22. [The Token Tax of Epistemic Accuracy — arXiv 2606.20898](https://arxiv.org/html/2606.20898)
23. [2M-token context vs RAG in 2026: cost, latency and when each actually wins](https://dev.to/mr_manushukla/2m-token-context-vs-rag-in-2026-cost-latency-and-when-each-actually-wins-5h1o)
24. [Long-Context AI vs. RAG for Document Analysis Compared — intuitionlabs](https://intuitionlabs.ai/articles/long-context-ai-vs-retrieval-rag)
25. [Long context vs RAG en 2026 : quand utiliser quoi ?](https://ianas.fr/blog/2026/05/20/long-context-vs-rag-quand-utiliser/)
26. [RAG, поиск и LongContext — Habr](https://habr.com/ru/companies/bothub/articles/1081080/)
27. [Lost in the Middle, 1,250x Cost: The Limits of Long-Context vs RAG](https://www.bestaiweb.ai/lost-in-the-middle-1-250x-cost-and-the-hard-technical-limits-of-long-context-vs-rag/)
28. [RAGAS Faithfulness 指标 — 官方文档](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/)
29. [RAGAS: Migration from v0.3 to v0.4](https://docs.ragas.io/en/v0.4.1/howtos/migrations/migrate_from_v03_to_v04/)
30. [RAG Evaluation with RAGAS: Faithfulness, Context Recall, and Answer Relevance](https://dev.to/michael_pham018/rag-evaluation-with-ragas-faithfulness-context-recall-and-answer-relevance-5cb)
31. [Empirical Evaluation of Open-Source LLMs for RAG in ESG Domain — arXiv 2609.15242](https://arxiv.org/abs/2609.15242)
32. [RAGVue: A Diagnostic View for Explainable and Automated Evaluation of RAG](https://arxiv.org/html/2601.04196)
33. [Milvus Architecture Overview](https://milvus.io/docs/architecture_overview.md)
34. [Comparing Milvus with Alternatives](https://milvus-io-dev.zilliz.cc/docs/v2.5.x/comparison.md)
35. [Best Vector Database in 2026: 6 Top Tools Ranked — layer3labs](https://www.layer3labs.io/comparisons/best-vector-databases)
36. [Top Vector Databases for Enterprise AI: 2026 Comparison — Atlan](https://atlan.com/know/top-vector-databases-enterprise-ai/)
37. [Enterprise Vector Database 2026: Qdrant vs Milvus vs pgvector vs Pinecone — DEV](https://dev.to/devrudals/enterprise-vector-database-2026-qdrant-vs-milvus-vs-pgvector-vs-pinecone-16a0)
38. [Perbandingan Vector Database 2026: Pinecone vs Qdrant vs Weaviate vs Milvus](https://aiworkflowlab.dev/id/article/perbandingan-vector-database-2026-rag-produksi)
39. [Best Vector Databases 2026: Top 8 Tools for AI Applications — scored.tools](https://scored.tools/downloads/best-vector-databases-2026.pdf)
40. [Open source vector databases: Qdrant vs Milvus vs Weaviate](https://botmonster.com/ai/open-source-vector-databases-qdrant-milvus-weaviate/)
41. [How to Build a Production-Ready RAG Pipeline in 2026](https://metafiedlab.com/blog/how-to-build-a-production-ready-rag-pipeline-in-2026/)
42. [RAG Pipeline Architecture: Chunking, Hybrid Search, Reranking, Evaluation](https://lucioduran.com/blog/rag-pipeline-architecture-chunking-reranking-evaluation)
43. [Evaluating Chunking Strategies for RAG on Academic Texts](https://arxiv.org/html/2607.01852)
44. [DS@GT ARC at LongEval: Citation Integrity and Factual Grounding in Scientific QA](https://arxiv.org/html/2607.14400v1)
45. [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/pdf/2310.08560.pdf)
46. [AI Agent Memory 2026: Progress Benchmark Report — Mem0](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
47. [Zep vs Mem0: Which AI Memory Layer Should You Choose? — Mem0](https://mem0.ai/blog/zep-vs-mem0-which-ai-memory-layer-should-you-choose)
48. [Agent memory built for production — Zep](https://www.getzep.com/mem0-alternative/)
49. [Agent Memory in 2026: An Honest Comparison of Mem0, Zep, Letta — automem.ai](https://automem.ai/blog/agent-memory-in-2026-an-honest-comparison-of-mem0-zep-letta-and-the-rest)
50. [Mem0 vs Letta vs Zep: Agent Memory for Production AI Agents (2026)](https://aiworkflowlab.dev/article/agent-memory-mem0-vs-letta-vs-zep-2026)
51. [Mem0 vs Letta vs Zep: Which Should You Use for Agent Memory?](https://dev.to/plur9/mem0-vs-letta-vs-zep-which-should-you-use-for-agent-memory-1n8m)
52. [How AI Agents Remember: Memory Architectures That Work](https://groundy.com/articles/how-ai-agents-remember-memory-architectures-that/)
53. [MemMachine: A Ground-Truth-Preserving Memory System](https://arxiv.org/pdf/2604.04853)
54. [AgentMemBench: A Systematic Benchmark for Long-Term Memory Management](https://arxiv.org/pdf/2608.00009)
55. [Beyond RAG: The Rise of Context Engineering](https://www.prateek-sharma.com/blog/beyond-rag-context-engineering/)
56. [Context Engineering vs RAG: When to Use Which Approach](https://getunblocked.com/blog/context-engineering-vs-rag/)
57. [Context engineering done right — k-ai.ai](https://www.k-ai.ai/en/news/context-engineering-clean-corpus-upstream-layer/)
58. [H-RAG at SemEval-2026 Task 8: Hierarchical Parent–Child Retrieval](https://arxiv.org/pdf/2605.00631.pdf)
59. [Memory Is the New RAG: Inside the Agent Memory Stack of 2026 — xyzbytes](https://www.xyzbytes.com/blog/ai-agent-memory-infrastructure-2026)
60. [From Static to Smart: Agentic RAG for Enterprise AI — Unstructured](https://unstructured.io/insights/from-static-to-smart-agentic-rag-for-enterprise-ai)
61. [Context Engineering in Agentic RAG: Production Patterns That Cut Token Cost (2026)](https://sukruyusufkaya.com/en/blog/agentic-rag-baglam-muhendisligi-token-optimizasyonu-2026)
62. [Retrieval augmented generation (RAG) and indexes — Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation?view=foundry)
63. [Context Engineering: System-Level Context Design for AI Agents — zylos.ai](https://zylos.ai/research/2026-07-14-context-engineering-system-level-context-design-ai-agents/)
64. [Mem0 vs Letta: Which AI Memory Platform Is Better for Production Agents? — Mem0](https://mem0.ai/compare/mem0-vs-letta)
65. [LLM Evaluation Framework: How to Evaluate LLM and Agent Applications — Zep](https://www.getzep.com/ai-agents/llm-evaluation-framework/)
66. [A Comprehensive Empirical Evaluation of Vector Database Systems for ANN Search — arXiv 2608.12812](https://arxiv.org/pdf/2608.12812)
67. [Vector Database Benchmark: 7 Open-Source Engines for RAG — AIMultiple](https://aimultiple.com/open-source-vector-databases)
68. [Vector Databases for Production RAG (2026): Pinecone vs Qdrant vs Milvus vs pgvector — DEV](https://dev.to/locionic/vector-databases-for-production-rag-2026-pinecone-vs-qdrant-vs-milvus-vs-pgvector-4fim)
69. [Context Rot: Why LLMs Degrade Long Before the Window Fills — datallmlab](https://www.datallmlab.com/blog/context-rot.html)
70. [Context Rot: The Complete Guide to Why LLMs Degrade as Context Grows — morphllm](https://www.morphllm.com/context-rot)
71. [Claude Context Window Size (2026): 1M Tokens on Opus 4.8 and Sonnet 5 — morphllm](https://www.morphllm.com/claude-context-window)
72. [Context Rot: Why AI Performance Degrades With More Information — usewire](https://usewire.io/blog/context-rot-why-ai-performance-degrades/)
73. [Advanced RAG Chunking Techniques in 2026: Late Chunking, Semantic, Parent-Child — futureagi](https://futureagi.com/blog/advanced-chunking-techniques-for-rag/)
74. [Chunking strategies for RAG pipelines: A practical guide for 2026 — DronaHQ](https://www.dronahq.com/chunking-strategies/)
75. [RAG Evaluation 2026: The Four Core Metrics and How to Read Them Diagnostically — DEV](https://dev.to/saaro_net/rag-evaluation-2026-the-four-core-metrics-and-how-to-read-them-diagnostically-1nk8)
76. [RAG Evaluation Explained: Top Metrics, Tools & Blindspots in 2026 — Atlan](https://atlan.com/know/how-to-evaluate-rag-systems-explained/)
77. [What is LazyGraphRAG? Microsoft's Game-Changing Answer to AI Data Retrieval Costs — articsledge](https://www.articsledge.com/post/lazygraphrag-retrieval-augmented-generation)
78. [How to Build GraphRAG Pipelines with Python: Knowledge Graphs for Smarter Retrieval — aiworkflowlab](https://aiworkflowlab.dev/article/how-to-build-graphrag-pipelines-with-python-knowledge-graphs-for-smarter-retrieval)
79. [GraphRAG: when knowledge graphs beat vector search — datarekha](https://datarekha.com/blog/graphrag-when-graphs-beat-vectors/)
80. [Graph Rag — nemorize](https://nemorize.com/roadmaps/2026-modern-ai-search-rag-roadmap/lessons/graph-rag)