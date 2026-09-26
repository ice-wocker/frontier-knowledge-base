# 分词与嵌入

> 最后更新：2026-09-26 ｜ 领域：AI·基础原理 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

分词（Tokenization）把原始文本切分为模型可处理的 token 序列，嵌入（Embedding）则把 token 或整段文本映射为稠密向量。前者决定模型的"字母表"与词汇表规模，后者是检索、聚类、分类与 RAG 系统的语义基础。两者共同构成 LLM 的输入接口：分词器一旦随模型权重固化便难以更换，不同分词器的合并规则与词表规模不同，同一段文本会被编码成不同的 token 序列（[tiktoken vs SentencePiece vs Hugging Face Tokenizers](https://dreaming.press/posts/tiktoken-vs-sentencepiece-vs-huggingface-tokenizers.html)）。

## 最新进展（2025–2026）

- **字节级 BPE 成为事实标准**：到 2026 年，几乎所有大型生成式 LLM 都使用字节级 BPE（byte-level BPE）或某种 SentencePiece 方案（[What is Tokenization in LLMs? BPE, SentencePiece, tiktoken in 2026](https://futureagi.com/blog/what-is-tokenization-llms-2026/)）。字节级方案从 0–255 的字节开始建词表，保证任意 UTF-8 字符串都能被表示、不产生未知 token（unknown token），GPT-2、LLaMA 2、RoBERTa、Claude 等均采用该路线（[LLM Tokenization Methods Explained](https://codelint.dev/ai-tools/tokenization-guide)、[How Does Tokenization Work?](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)）。
- **SentencePiece 的 Unigram 分支被更多模型采用**：SentencePiece 本身不是一种算法，而是一套可训练 BPE 或 Unigram 模型的工具包，并把空格当作真实字符、以 `▁`（U+2581）标记，因此无需按语言做空白预切分；其中 Unigram 变体被 Gemma 系列采用（[What is Tokenization in LLMs?](https://futureagi.com/blog/what-is-tokenization-llms-2026/)、[How Does Tokenization Work?](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)）。WordPiece 则按"最大提升训练数据似然"的字节对进行合并，主要使用方为 BERT 系（[How Does Tokenization Work?](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)）。
- **嵌入评测细分与多模态化**：MTEB 已扩展出多语言（MMTEB）与多模态子榜，并按语言拆分出 MTEB(eng)、MTEB(Multilingual)、MTEB(cmn, v1)（中文）等独立榜单，各榜分别覆盖检索、重排序、聚类、分类与语义相似度等任务类型（[Available Benchmarks](https://docs.mteb.org/overview/available_benchmarks/)、[MTEB Leaderboard](https://mteb-leaderboard.hf.space/)）。

## 核心技术与关键概念

### 分词算法

| 算法 | 合并/切分策略 | 典型使用方 |
| --- | --- | --- |
| BPE（Byte-Pair Encoding） | 贪心合并高频字节对 | GPT-2/3/4、Claude 系 |
| SentencePiece | 基于原始字节的 Unigram 或 BPE，无空白预切分 | Llama、T5、Mistral、Gemini、Gemma |
| WordPiece | 按最大似然贪心切分 | BERT 及原始 Transformer 衍生 |
| Unigram（SentencePiece） | 从超大候选词表开始，按 EM 剪枝 | T5、mBART、XLM-R |

以上对照来自多份资料（[What is Tokenization in LLMs?](https://futureagi.com/blog/what-is-tokenization-llms-2026/)、[How Does Tokenization Work?](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)、[LLM Engineering (2): Tokenization Deep Dive](https://www.chenk.top/en/llm-engineering/02-tokenization/)、[LLM Tokenization Methods Explained](https://codelint.dev/ai-tools/tokenization-guide)）。当代聊天型 LLM 中，WordPiece 已较少见（[How Does Tokenization Work?](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)）。

**tiktoken** 是 OpenAI 于 2022 年 12 月开源的字节对编码分词库，用 Rust 编写、经 PyO3 提供 Python 绑定，可精确复现其模型的合并规则，编码速度约为同类实现的 3–6 倍（[tiktoken](https://aiwiki.ai/wiki/tiktoken)、[tiktoken vs SentencePiece vs Hugging Face Tokenizers](https://dreaming.press/posts/tiktoken-vs-sentencepiece-vs-huggingface-tokenizers.html)）。

**三大分词实现的关键差异**：tiktoken 是面向推理的 BPE 编码器，严格在 UTF-8 字节上操作、无需回退机制；SentencePiece 是 Google 的"语言无关"训练器，把文本当作原始字节流并支持 BPE 与 Unigram；Hugging Face `tokenizers` 则是 Rust 实现的完整流水线，可训练并运行上述各类算法（[tiktoken vs SentencePiece vs Hugging Face Tokenizers](https://dreaming.press/posts/tiktoken-vs-sentencepiece-vs-huggingface-tokenizers.html)、[How LLMs See the World: The Hidden Logic of Tokenization](https://plainenglish.io/artificial-intelligence/how-llms-see-the-world-the-hidden-logic-of-tokenization)）。由于 SentencePiece 先在 Unicode 码点上操作、对罕见字符回退到字节，因而对 CJK 等非英文文本压缩更好（[Tokenizer Learning](https://jianyuh.github.io/tokenizer/2025/12/06/Tokenizer.html)）。

### 上下文嵌入

早期的静态/类型级嵌入（如 Word2Vec、GloVe）为每个词分配一个固定向量，无法区分多义（[Contextualized Word Embeddings](https://www.artificial-intelligence-wiki.com/natural-language-processing/word-embeddings-and-representations/contextualized-word-embeddings/)）。上下文嵌入（contextual embeddings，如 ELMo、BERT、GPT）为同一词的每次出现生成不同向量，向量是整段输入序列的函数，从而区分"bank（银行）"与"bank（河岸）"等不同词义（[Lecture 12: Contextual embeddings](https://context-lab.com/llm-course/slides/week4/lecture12.pdf)、[A Survey on Contextual Embeddings](https://arxiv.org/pdf/2003.07278v2.pdf)）。

静态与上下文嵌入的典型对比：静态每种词一个向量、维度约 50–300、浅层模型；上下文嵌入每次出现一个向量、维度约 768–1024、深层模型（12–24 层以上）（[Word Embedding](https://aiwiki.ai/wiki/word_embedding)）。

### 嵌入模型与 MTEB

主流文本嵌入模型（含官方/公开来源）：

- **OpenAI text-embedding-3 系列**：text-embedding-3-small 默认 1536 维、text-embedding-3-large 默认 3072 维；官方公布的 MTEB 平均分中，ada v2 为 61.0、text-embedding-3-small 为 62.3、text-embedding-3-large 为 64.6（[New embedding models and API updates](https://openai.com/blog/new-embedding-models-and-api-updates)）。
- **BGE**（北京智源）：BGE 系列在发布时于对应规模上达到 SoTA，官方维护 MTEB 榜单（[bge](https://bge.baai.ac.cn/)）。第三方整理显示 BGE-M3（1024 维，MIT 许可）MTEB 约 63.0（[Best Embedding Models 2025: MTEB Scores & Leaderboard](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)）。
- **E5**：multilingual-e5 系列在 MMTEB 上表现稳健，例如 multilingual-e5-base 在 173 个模型对比中排名第 3，multilingual-e5-small 排名第 4（[MMTEB: Massive Multilingual Text Embedding Benchmark](https://arxiv.org/html/2502.13595v1)）。
- **Nomic**：nomic-embed 以仅 137M 参数实现长上下文文本嵌入，报告称其在 MTEB 与 LoCo 上超过 OpenAI text-embedding-ada 与 text-embedding-3-small（[Nomic Embed: Training a Reproducible Long Context Text Embedder](https://arxiv.org/html/2402.01613)）。第三方整理称 Nomic-embed-text-v1.5 MTEB 约 59.4、768 维（[Best Embedding Models 2025](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)）。
- **Cohere embed-v4**：第三方资料称其以 65.2 分居 MTEB 榜首，1024 维、$0.10/百万 token，支持 100 多种语言并可压缩到 256 或 512 维（[Embedding Model Comparison Guide 2025](https://artificial-intelligence-wiki.com/ai-development/ai-frameworks-and-libraries/embedding-model-comparison/)）。
- **Gemini Embedding 与 Qwen3 Embedding（2025–2026 新势力）**：Google 的 `gemini-embedding-001` 常居多语言 MTEB 榜单 API 类前列，其论文称在 MMTEB 的多语言、英文与代码评测上相对前代取得显著提升，尤擅分类、聚类与检索（[Gemini Embedding: Generalizable Embeddings from Gemini](https://arxiv.org/html/2503.07891)、[Top 10 Closed-Source and Open-Source Embedding Models (2026)](https://explainx.ai/blog/top-10-open-closed-source-embedding-models-2026)）。第三方榜单显示 Gemini Embedding 001 的 MTEB 平均分约 68.32、3072 维、最大 8192 token（[Embedding Model Leaderboard: MTEB Rankings April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)）。阿里巴巴 Qwen3 Embedding 系列覆盖 0.6B–8B 多种尺寸，官方称 8B 文本嵌入模型在 MTEB Multilingual 榜上以 70.58 分排名第一（截至 2025 年 6 月 5 日）、在 MTEB Code 榜达 80.68 分，超过此前的 Gemini-Embedding（[Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models](https://arxiv.org/pdf/2506.05176)、[Qwen 3 Embedding](https://www.kaggle.com/models/qwen-lm/qwen-3-embedding/transformers/8b/1)）。
- **NV-Embed-v2**：NVIDIA 的开源嵌入模型，第三方榜单记录其 MTEB 平均分约 72.31（口径含检索等子项）、4096 维、最大 32,768 token、Apache 2.0 许可（[Embedding Model Leaderboard: MTEB Rankings April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)、[Embedding Model Leaderboard 2026](https://aipromptshub.co/blog/embedding-model-leaderboard-2026)）。
- **EmbeddingGemma**：新一代轻量开源文本表示模型（[EmbeddingGemma: Powerful and Lightweight Text Representations](https://arxiv.org/html/2509.20354v2/)）。

**指令感知与可变维度**成为 2025–2026 的设计惯例：Qwen3 Embedding 支持 100 多种语言与编程语言，允许在所有维度上灵活定义向量，并以"指令 + 查询"拼接输入、文档保持不变的方式来让嵌入遵循任务指令（[Qwen3 Embedding](https://arxiv.org/pdf/2506.05176)、[Qwen3-Embedding-0.6B](https://deepinfra.com/Qwen/Qwen3-Embedding-0.6B)）；Qwen3-VL 系列进一步把统一表示学习扩展到图像、视频等多模态检索，其旗舰 Qwen3-VL-Embedding-8B 在 2026 年 1 月的 MMEB-V2 基准上取得 77.8 分，官方称超过当时榜单上的全部开源与闭源模型（[Qwen3-VL-Embedding and Qwen3-VL-Reranker](https://arxiv.org/pdf/2601.04720v2)、[Qwen3-VL-Embedding and Qwen3-VL-Reranker（官方博客）](https://qwen.ai/blog?id=qwen3-vl-embedding)）。

### 分词粒度与工程取舍

分词粒度直接牵动若干工程指标：词表越大，单 token 承载的信息越多、序列越短（利于降低注意力开销与 API 成本），但嵌入矩阵与输出层参数随之增大，且低频 token 训练不充分；词表越小，序列越碎、有效上下文越短，但泛化与词表利用率更好。字节级 BPE 通过"从字节起步"把词表外的组合问题转化为多 token 拼接，从根本上消除了 unknown token（[How Does Tokenization Work?](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)、[LLM Tokenization Methods Explained](https://codelint.dev/ai-tools/tokenization-guide)）。由于分词器随权重固化，更换分词器意味着需要重新训练或至少大规模继续训练，因此选型通常在建模型之前就已锁定（[tiktoken vs SentencePiece vs Hugging Face Tokenizers](https://dreaming.press/posts/tiktoken-vs-sentencepiece-vs-huggingface-tokenizers.html)）。

在检索与 RAG 场景中，嵌入模型的"最大输入 token 数"与"输出维度"是两项硬约束：维度决定向量存储与检索的显存/带宽开销，最大 token 数决定单次可编码的文档长度（超出通常需要截断或分块）。因此在选型时常需在质量、维度、长度、许可与价格之间权衡（[Embedding Model Leaderboard: MTEB Rankings April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)、[Top 10 Closed-Source and Open-Source Embedding Models (2026)](https://explainx.ai/blog/top-10-open-closed-source-embedding-models-2026)）。

## 关键数据与评测结果

MTEB（Massive Text Embedding Benchmark）覆盖分类、聚类、检索、重排序、配对分类与语义相似度等任务类型，并已拆分为 MTEB(eng)、MTEB(Multilingual) 等版本（英文 v1 榜单在 MTEB(eng, v1) 下仍可访问）（[Available Benchmarks](https://docs.mteb.org/overview/available_benchmarks/)）。榜单实时更新，官方入口为 Hugging Face Spaces 上的 MTEB leaderboard（[MTEB Leaderboard](https://mteb-leaderboard.hf.space/)）。

从公开榜单可提取若干可比的量化信息：Gemini Embedding 001 约 68.32 分、3072 维、最多 8192 token；NV-Embed-v2 约 72.31 分（含检索子项口径）、4096 维、最多 32,768 token、Apache 2.0 许可；OpenAI text-embedding-3-large 默认 3072 维、官方 MTEB 平均分 64.6（[Embedding Model Leaderboard: MTEB Rankings April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)、[Embedding Model Leaderboard 2026](https://aipromptshub.co/blog/embedding-model-leaderboard-2026)、[New embedding models and API updates](https://openai.com/blog/new-embedding-models-and-api-updates)）。这些数值来自不同榜单版本，仅作数量级参考。

需注意：不同来源的"MTEB 分数"常常基于不同榜单版本与任务集合（如上表同时出现 MTEB Multilingual v1 的 70.58 分与含检索子项的约 72.31 分），直接横向比较容易失真，引用时应标明口径（[Embedding Model Leaderboard 2026](https://aipromptshub.co/blog/embedding-model-leaderboard-2026)、[Best Embedding Models](https://www.madebyagents.com/models/embedding)）。

## 趋势与争议

- **分词与多语言公平性**：字节级 BPE 对非英文（尤其 CJK、Indic）的压缩效率不及针对码点设计的 SentencePiece，直接影响 token 成本与有效上下文长度（[Tokenizer Learning](https://jianyuh.github.io/tokenizer/2025/12/06/Tokenizer.html)）。一项针对现代分词器的跨语言分析报告称，相对英文各语言存在"token 税"，例如 gpt4o 平均约 1.75 倍、日语最高 3.41 倍，qwen2.5 平均约 1.90 倍、印地语最高 3.89 倍（[Cross-Lingual Tokenizer Equity](https://www.clawrxiv.io/abs/2603.00101)）；另有实测显示，用 OpenAI `o200k_base` 分词器，等效中文提示消耗的 token 是英文的 1.06–1.55 倍（平均 1.34 倍），而旧的 `cl100k_base` 下平均达 2.08 倍（[Is Chinese More Token-Efficient Than English? Tested](https://masonailab.com/en/insights/token-efficiency/)）。相关研究进一步指出，使用阿拉伯文、中文、西里尔等非拉丁文字的语言持续需要更多 token，Unicode 编码差异造成结构性偏差（[Non-English Speakers Pay More for Less](https://zenodo.org/records/20028344/files/Tokenization_preprint_V2.pdf?download=1)），并以 STRR 等指标量化切分退化（[Beyond Fertility: Analyzing STRR for Multilingual Tokenization Evaluation](https://arxiv.org/html/2510.09947)）。
- **嵌入维度可裁剪**：Matryoshka 式可变维度（如 text-embedding-3 的 dimensions 参数、Qwen3 Embedding 的全维度灵活定义）让存储与检索成本可调，成为工程常规（[Embeddings](https://openai-doc.ru/docs/embeddings)、[Qwen3 Embedding](https://arxiv.org/pdf/2506.05176)）。
- **榜单饱和与口径混乱**：MTEB 分数排名在不同整理文章中差异较大，反映评测版本迭代快、复现条件不一；多语言与多模态子榜的引入也使"单一总分"越来越难代表真实场景表现（[Best Embedding Models 2025](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)、[Embedding Model Comparison Guide 2025](https://artificial-intelligence-wiki.com/ai-development/ai-frameworks-and-libraries/embedding-model-comparison/)、[Available Benchmarks](https://docs.mteb.org/overview/available_benchmarks/)）。

## 参考来源

- [LLM Engineering (2): Tokenization Deep Dive](https://www.chenk.top/en/llm-engineering/02-tokenization/)
- [How Does Tokenization Work? Byte-Pair Encoding in Plain English](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)
- [tiktoken](https://aiwiki.ai/wiki/tiktoken)
- [What is Tokenization in LLMs? BPE, SentencePiece, tiktoken in 2026](https://futureagi.com/blog/what-is-tokenization-llms-2026/)
- [tiktoken vs SentencePiece vs Hugging Face Tokenizers](https://dreaming.press/posts/tiktoken-vs-sentencepiece-vs-huggingface-tokenizers.html)
- [LLM Tokenization Methods Explained](https://codelint.dev/ai-tools/tokenization-guide)
- [How LLMs See the World: The Hidden Logic of Tokenization](https://plainenglish.io/artificial-intelligence/how-llms-see-the-world-the-hidden-logic-of-tokenization)
- [Tokenizer Learning](https://jianyuh.github.io/tokenizer/2025/12/06/Tokenizer.html)
- [Lecture 12: Contextual embeddings](https://context-lab.com/llm-course/slides/week4/lecture12.pdf)
- [Word Embedding](https://aiwiki.ai/wiki/word_embedding)
- [Contextualized Word Embeddings](https://www.artificial-intelligence-wiki.com/natural-language-processing/word-embeddings-and-representations/contextualized-word-embeddings/)
- [A Survey on Contextual Embeddings](https://arxiv.org/pdf/2003.07278v2.pdf)
- [New embedding models and API updates (OpenAI)](https://openai.com/blog/new-embedding-models-and-api-updates)
- [Embeddings (OpenAI docs)](https://openai-doc.ru/docs/embeddings)
- [FAQ sur les embeddings (OpenAI Help)](https://help.openai.com/fr-ca/articles/6824809-faq-sur-les-embeddings)
- [bge (BAAI)](https://bge.baai.ac.cn/)
- [Best Embedding Models 2025: MTEB Scores & Leaderboard](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)
- [Embedding Model Comparison Guide 2025](https://artificial-intelligence-wiki.com/ai-development/ai-frameworks-and-libraries/embedding-model-comparison/)
- [Nomic Embed: Training a Reproducible Long Context Text Embedder](https://arxiv.org/html/2402.01613)
- [MMTEB: Massive Multilingual Text Embedding Benchmark](https://arxiv.org/html/2502.13595v1)
- [EmbeddingGemma: Powerful and Lightweight Text Representations](https://arxiv.org/html/2509.20354v2/)
- [Available Benchmarks (MTEB docs)](https://docs.mteb.org/overview/available_benchmarks/)
- [MTEB Leaderboard](https://mteb-leaderboard.hf.space/)
- [Gemini Embedding: Generalizable Embeddings from Gemini](https://arxiv.org/html/2503.07891)
- [Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models](https://arxiv.org/pdf/2506.05176)
- [Qwen 3 Embedding (Kaggle)](https://www.kaggle.com/models/qwen-lm/qwen-3-embedding/transformers/8b/1)
- [Qwen3-Embedding-0.6B (DeepInfra)](https://deepinfra.com/Qwen/Qwen3-Embedding-0.6B)
- [Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework](https://arxiv.org/pdf/2601.04720v2)
- [Qwen3-VL-Embedding and Qwen3-VL-Reranker（官方博客）](https://qwen.ai/blog?id=qwen3-vl-embedding)
- [Top 10 Closed-Source and Open-Source Embedding Models (2026)](https://explainx.ai/blog/top-10-open-closed-source-embedding-models-2026)
- [Embedding Model Leaderboard: MTEB Rankings April 2026](https://www.awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)
- [Embedding Model Leaderboard 2026: MTEB Rankings](https://aipromptshub.co/blog/embedding-model-leaderboard-2026)
- [Best Embedding Models](https://www.madebyagents.com/models/embedding)
- [Cross-Lingual Tokenizer Equity](https://www.clawrxiv.io/abs/2603.00101)
- [Is Chinese More Token-Efficient Than English? Tested](https://masonailab.com/en/insights/token-efficiency/)
- [Non-English Speakers Pay More for Less](https://zenodo.org/records/20028344/files/Tokenization_preprint_V2.pdf?download=1)
- [Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation](https://arxiv.org/html/2510.09947)