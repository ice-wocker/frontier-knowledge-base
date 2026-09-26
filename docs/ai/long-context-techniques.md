# 长上下文技术：位置外推、稀疏注意力与状态空间模型

> 最后更新：2026-09-26 ｜ 领域：AI·训练与推理工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

长上下文（Long Context）指让大语言模型在一次前向计算中处理 128K、1M 乃至更长 token 序列的能力。其核心矛盾在于标准自注意力的计算与显存开销随序列长度呈二次增长，同时位置编码（Position Embedding）在超出预训练长度后出现分布外退化（extrapolation failure）。

工程上解决该矛盾的三条主线是：（1）**位置编码外推**，让基于 RoPE（Rotary Position Embedding）的模型在不重训或轻量微调下支持更长序列；（2）**稀疏 / 窗口化注意力**，把二次复杂度降为近似线性；（3）**线性注意力与状态空间模型（SSM）**，用固定大小的隐状态替代完整 KV cache。三条路线在 2025–2026 年出现明显的融合趋势，前沿模型普遍采用"局部注意力 + 稀疏全局召回 + SSM 层"的混合架构。

## 最新进展（2025–2026）

**位置外推方法持续迭代。** YaRN（Yet another RoPE extensioN）在其论文中系统整理了此前未公开发表的 NTK-aware、Dynamic NTK、NTK-by-parts 插值方法，并提出按维度波长决定插值强度，同时用温度校正（按 √log s 重新缩放注意力 logits）补偿 token 数增加带来的熵变化；该方法可将 LLaMA-2-7B 的上下文从 4K 扩展到 128K（[YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/html/2309.00071v3)、[LLM Engineering (6): Long Context — RoPE, YaRN, Sinks](https://www.chenk.top/en/llm-engineering/06-long-context/)）。综述《Thus Spake Long-Context Large Language Model》则汇总了 ReRoPE、Entropy-ABF 等后续方案，梳理了长上下文从位置编码、注意力结构到系统实现的完整技术栈（[Thus Spake Long-Context Large Language Model](https://arxiv.org/html/2502.17129v1)）。2026 年出现的 Jet-Long 提出 Dynamic Bifocal RoPE，在 7 个长度上平均将 RULER 分数从 42.93 提升到 52.94（2B 模型）、从 42.16 提升到 53.47（4B 模型）（[Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE](https://arxiv.org/html/2607.07740)）。

围绕 RoPE 的改进仍在继续。CoPE（Clipped RoPE）将既有 RoPE 扩展方法归纳为两类指导原则——一类是分布外（OOD）缓解，通过缩放 RoPE 频率以容纳未见位置；另一类是语义建模，认为用 RoPE 计算出的注意力分数应始终优先关注语义相似的 token；并据此提出 Clipped RoPE 作为可扩展的"免费午餐"（[CoPE: Clipped RoPE as A Scalable Free Lunch for Long Context LLMs](https://arxiv.org/pdf/2602.05258v1)）。Periodic RoPE（P-RoPE）则针对位置"耗尽"问题提出周期性位置编码，并与滑动窗口注意力（SWA）配合，由局部层捕捉每个窗口内的局部依赖与相对位置（[Periodic RoPE for Infinite Context LLMs](https://arxiv.org/pdf/2605.27980)）。在系统层面，流式窗口配合注意力汇（attention sink）短窗口 + 首部 token、以及 Ring Attention / Context Parallel 在设备间切分 KV 的方案，仍是长序列训练的常见组合（[Long Context Rope Yarn Mla Tutorial](https://wanshuiyin.github.io/ARIS-in-AI-Offer/tutorials/long_context_rope_yarn_mla_tutorial_en.html)）。

**稀疏注意力成为超长上下文的默认选择。** DeepSeek Sparse Attention（DSA）通过 Lightning Indexer 对历史位置打分，再用 token selector 保留被学习的可见前缀子集，被选中的 token 可以远在固定局部窗口之外；公开资料称 DeepSeek V3.2、GLM-5、GLM-5.2、Tencent Hy4-preview 均采用该模式（[DeepSeek Sparse Attention](https://sebastianraschka.com/llm-architecture-gallery/deepseek-sparse-attention/)）。针对 DSA 中 indexer 自身 O(L²) 打分开销与不规则访存导致的硬件效率问题，LongCat Sparse Attention 提出算法—硬件协同的流式感知分层跨层索引（[LongCat Sparse Attention](https://arxiv.org/html/2608.01662v1)）。DeepSeek-V4 相关工作则采用 Lookahead Sparse Attention，保留 128:1 压缩比的高度浓缩块以维持全局感知；该工作报告在 1M 上下文下每 decode token 计算降至基线的 0.30 倍、GPU KV cache 从 3.73 GB 缩至 0.37 GB（约 90% 缩减），并在 8×H20 的 PD 分离服务上带来 2.8× 聚合吞吐与 2.7× 并发提升（[FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention](https://arxiv.org/html/2606.09079v3)）。

**混合 SSM-Transformer 架构进入生产级。** NVIDIA 发布的 Nemotron 3 Super 是开放的 MoE 混合 Mamba-Transformer 模型，面向 agentic reasoning，并使用 LatentMoE 与多 token 预测（MTP）加速推理（[Nemotron 3 Super Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)）。第三方分析指出 Nemotron 3 这类混合架构只保留少量注意力层（如 6 层）即可在 1M 上下文取得 RULER-100 约 86.3% 的成绩（[Nemotron 3: How a Mamba-Transformer Hybrid Runs 1M Tokens](https://www.danilchenko.dev/posts/nemotron-3-mamba/)）。AI21 的 Jamba 系列是最早的规模化混合 Transformer-Mamba 模型之一，其 Jamba-1.5 在 RULER 的 13 项合成任务（含 8 种 needle-in-a-haystack 变体、变量跟踪与聚合任务）上做评测（[Jamba-1.5: Hybrid Transformer-Mamba Models at Scale](https://arxiv.org/pdf/2408.12570)）。Mamba 系列本身也持续演进：Mamba 使用选择性状态空间模型（selective SSM），以相对序列长度的线性时间处理序列，其 CUDA selective-scan 参考实现以 Apache 2.0 开源，后继版本包括 Mamba-2（2024）与 Mamba-3（2026）（[Mamba](https://aiwiki.ai/wiki/mamba)）。2Mamba 工作则指出线性注意力与 softmax 注意力之间仍存在精度差距，通过调整 A-mask 并提高隐状态阶数来缩小差距（[2Mamba2Furious: Linear in Complexity, Competitive in Accuracy](https://arxiv.org/html/2602.17363v1)）。针对混合模型的位置外推，Universal Position Interpolation（UPI）研究显示，Bamba-9B-v2 在结合 UPI 与 YaRN 后，64K 困惑度从 53.14 降至 18.59（[From Collapse to Control: Understanding and Extending Context Length in Emerging Hybrid Models via Universal Position Interpolation](https://en.papernotes.org/ICLR2026/llm_efficiency/from_collapse_to_control_understanding_and_extending_context_length_in_emerging_/)）。

## 核心技术与关键概念

- **RoPE 与位置外推**：RoPE 通过对 token 嵌入施加旋转矩阵同时编码相对与绝对位置信息（[An Evaluation of Context Length Extrapolation in Long Code](https://arxiv.org/pdf/2602.21800v1)）。NTK-aware 插值、位置插值（PI）、NTK-by-parts 与 YaRN 属于免训练或轻量微调的外推方案；实践中常配合少量长序列继续预训练。
- **窗口化与稀疏注意力**：以固定滑动窗口（如 512 token）承担局部建模，另设压缩分支与选择分支承担全局召回，再由一个 sigmoid 门控 MLP 按 query 位置对各分支出加权求和，端到端学习权重（[Sparse Attention Explained](https://www.danilchenko.dev/posts/sparse-attention-explained/)）。
- **线性注意力与 SSM**：以 O(N) 复杂度替代 O(N²)。研究显示 Mamba 与线性注意力 Transformer 存在惊人的结构相似性，其成功关键在于特定设计选择而非"线性注意力"标签本身（[Demystify Mamba in Vision: A Linear Attention Perspective](https://papers.nips.cc/paper_files/paper/2024/file/e618724ac897c6cf3fbfb273f8695d67-Paper-Conference.pdf)）。
- **注意力汇（attention sink）**：序列首部 token 会吸引大量注意力，是长上下文数值稳定性的重要处理对象；流式推理中通常保留首部若干 token（sink）加滑动窗口，窗口外 token 被丢弃但 sink 不可丢弃，否则困惑度会急剧上升（[Long Context Rope Yarn Mla Tutorial](https://wanshuiyin.github.io/ARIS-in-AI-Offer/tutorials/long_context_rope_yarn_mla_tutorial_en.html)）。
- **token 级压缩**：DeepSeek-V4 采用"token 维度压缩 + DSA 稀疏注意力"的组合来在超长上下文下降低计算与显存需求（[DeepSeek-V4 Preview: Entering the Era of Affordable Million-Token Context](https://www.deepseek.com/en/news/v4-preview/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **DeepSeek-V4 系列**：官方称 V4 拥有百万字超长上下文，并把 1M 上下文作为所有官方服务标配；V4-Pro 为 1.6T 总参数 / 49B 激活参数（[DeepSeek-V4 Preview: Entering the Era of Affordable Million-Token Context](https://www.deepseek.com/en/news/v4-preview/)、[DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)）。
- **NVIDIA Nemotron 3**：开放 MoE 混合 Mamba-Transformer 模型（[Nemotron 3 Super Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)）。
- **AI21 Jamba**：Transformer-Mamba 混合架构系列（[Jamba-1.5: Hybrid Transformer-Mamba Models at Scale](https://arxiv.org/pdf/2408.12570)）。
- **Mamba（Tri Dao、Albert Gu 等）**：选择性 SSM 与 select-scan CUDA 内核（[Mamba](https://aiwiki.ai/wiki/mamba)）。
- **FlashAttention / Ring Attention**：IO-aware 注意力与序列并行，是长上下文训练与推理的底层支撑。

## 关键数据与评测结果

**RULER** 是长上下文评测的事实标准之一，原始评测范围为 4K–128K。值得注意的是，2026 年的行业分析指出，尽管前沿模型已宣称 100 万 token 以上的上下文窗口，2024 年发现的"有效上下文缺口"在更长尺度上依然存在（[RULER benchmark](https://aiwiki.ai/wiki/ruler_benchmark/raw)）。有 2026 年的研究估算，前沿 LLM 实际可靠使用的上下文仅占标称窗口的约 50%–65%（同上来源）。

**混合架构的效率与质量数据。** 一项 SSM 与 Transformer 的系统对比研究称，在约 57K token 处，SSM 的首 token 时延（TTFT）可比 Transformer 快最多 4×（得益于线性复杂度），并称 SSM 可在 24 GB 消费级 GPU 上处理最多 220K token，约为优化后 Transformer 在不 offload 情况下的 4 倍（[Characterizing State Space Model and Transformer Inference](https://sapmitra.github.io/ssm-scope/)）。

**多语言长上下文评测**显示，随着上下文长度从 8K 增加到 128K，低资源语言与高资源语言之间的性能差距持续扩大；英文并非长上下文任务表现最好的语言（在 26 种语言中排名第 6），波兰语表现最佳（[One ruler to measure them all: Benchmarking multilingual long-context language models](https://arxiv.org/html/2503.01996v2)）。斯坦福 CRFM 的 HELM Long Context 也在 RULER 基础上加入了 HotPotQA 等基于短文的多跳问答任务进行评测（[HELM Long Context](https://crfm.stanford.edu/2025/09/29/helm-long-context.html)）。

**NIAH 类基准的局限**已被广泛讨论。Chroma 将经典 Needle-in-a-Haystack 设置沿 8 个输入长度、11 个 needle 位置扩展，LLM 判定与人工判定一致率超过 99%，结论是仅长度增加本身就会使可靠性下滑，且干扰段落会进一步伤害表现（[Context Rot: Why LLMs Degrade Long Before the Window Fills](https://www.datallmlab.com/blog/context-rot.html)）。多针 NIAH 的分数差异远大于单针：据 AI Wiki 汇总的在 1M token 处测试，Gemini 3 Deep Think 单针 99%、八针 89%，GPT-5.5 为 96% / 74%，Claude Opus 4.7 为 89% / 56%，DeepSeek V4-Pro 为 78% / 41%（[Needle in a Haystack](https://aiwiki.ai/wiki/needle_in_a_haystack/raw)）。

**DeepSeek-V4 的效率口径。** 官方论文称在 100 万 token 上下文下，DeepSeek-V4-Pro 单 token 推理 FLOPs 仅为 DeepSeek-V3.2 的 27%、KV cache 仅为 10%（[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/html/2606.19348)）。该口径出自官方论文，需与第三方复测区分。

## 趋势与争议

1. **标称窗口 vs 有效窗口**。多口径数据并存：Gemini 3.1 Pro 宣称 API 侧最高 2M token，Gemini 3 Pro 被报道达到 10M token（[ChatGPT vs Claude Context Window](https://aionx.co/ai-comparisons/chatgpt-claude-context-window/)、[Gemini vs. Claude in 2026](https://multiple.chat/gemini-vs-claude)）；Claude 标准窗口为 200K，Opus 4.6 提供 1M（[Claude vs Gemini (2026)](https://www.rohitprabhakar.com/blog/claude-vs-gemini/)）；DeepSeek 则宣称把 1M 作为官方服务标配（[DeepSeek-V4 Preview](https://www.deepseek.com/en/news/v4-preview/)）。但评测侧普遍认为有效可用长度显著低于标称值，二者口径不可直接比较。
2. **单一基准的误导性**。NIAH 只测词面检索，掩盖了推理能力随长度衰减的事实（[What Is Context Rot?](https://alphacorp.ai/blog/what-is-context-rot-why-bigger-ai-context-windows-make-models-worse)）。
3. **稀疏 vs 稠密的质量代价**。稀疏/线性架构带来吞吐优势，但在 <128K 的常规对话与 RAG 负载上，Transformer 在质量上仍占优，混合架构成为折中（[Mamba and State-Space Models Explained (2026)](https://localaimaster.com/blog/mamba-state-space-models-guide)）。
4. **扩展方式的可比性**。外推方法的效果高度依赖基座模型与续训数据，不同论文的 RULER 提升幅度（如 Jet-Long 为 +10 pp 量级）不宜跨模型直接比较。
5. **效率数字的归属**。DeepSeek-V4 的 27% FLOPs、10% KV cache 等收益口径来自官方论文与官方发布，与第三方在真实负载下的复测不可直接等同。

## 参考来源

1. [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/html/2309.00071v3)
2. [LLM Engineering (6): Long Context — RoPE, YaRN, Sinks](https://www.chenk.top/en/llm-engineering/06-long-context/)
3. [Thus Spake Long-Context Large Language Model](https://arxiv.org/html/2502.17129v1)
4. [Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE](https://arxiv.org/html/2607.07740)
5. [An Evaluation of Context Length Extrapolation in Long Code via Positional Embeddings and Efficient Attention](https://arxiv.org/pdf/2602.21800v1)
6. [DeepSeek Sparse Attention](https://sebastianraschka.com/llm-architecture-gallery/deepseek-sparse-attention/)
7. [LongCat Sparse Attention: Taming the Lightning via Streaming-aware Hierarchical Cross-Layer Indexing](https://arxiv.org/html/2608.01662v1)
8. [FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention](https://arxiv.org/html/2606.09079v3)
9. [Sparse Attention Explained](https://www.danilchenko.dev/posts/sparse-attention-explained/)
10. [Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)
11. [Mamba](https://aiwiki.ai/wiki/mamba)
12. [2Mamba2Furious: Linear in Complexity, Competitive in Accuracy](https://arxiv.org/html/2602.17363v1)
13. [Demystify Mamba in Vision: A Linear Attention Perspective](https://papers.nips.cc/paper_files/paper/2024/file/e618724ac897c6cf3fbfb273f8695d67-Paper-Conference.pdf)
14. [Mamba and State-Space Models Explained (2026)](https://localaimaster.com/blog/mamba-state-space-models-guide)
15. [RULER benchmark](https://aiwiki.ai/wiki/ruler_benchmark/raw)
16. [One ruler to measure them all: Benchmarking multilingual long-context language models](https://arxiv.org/html/2503.01996v2)
17. [HELM Long Context](https://crfm.stanford.edu/2025/09/29/helm-long-context.html)
18. [Context Rot: Why LLMs Degrade Long Before the Window Fills](https://www.datallmlab.com/blog/context-rot.html)
19. [Needle in a Haystack](https://aiwiki.ai/wiki/needle_in_a_haystack/raw)
20. [What Is Context Rot? Why Bigger AI Context Windows Make Models Worse](https://alphacorp.ai/blog/what-is-context-rot-why-bigger-ai-context-windows-make-models-worse)
21. [ChatGPT vs Claude Context Window: Which Handles More Text? (2026 Comparison)](https://aionx.co/ai-comparisons/chatgpt-claude-context-window/)
22. [Gemini vs. Claude in 2026](https://multiple.chat/gemini-vs-claude)
23. [Claude vs Gemini (2026): Which AI Is Better for Writing, Coding and Research?](https://www.rohitprabhakar.com/blog/claude-vs-gemini/)
24. [CoPE: Clipped RoPE as A Scalable Free Lunch for Long Context LLMs](https://arxiv.org/pdf/2602.05258v1)
25. [Periodic RoPE for Infinite Context LLMs](https://arxiv.org/pdf/2605.27980)
26. [DeepSeek-V4 Preview: Entering the Era of Affordable Million-Token Context](https://www.deepseek.com/en/news/v4-preview/)
27. [DeepSeek V4 Preview Release (API Docs)](https://api-docs.deepseek.com/news/news260424)
28. [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/html/2606.19348)
29. [Nemotron 3: How a Mamba-Transformer Hybrid Runs 1M Tokens](https://www.danilchenko.dev/posts/nemotron-3-mamba/)
30. [Characterizing State Space Model and Transformer Inference](https://sapmitra.github.io/ssm-scope/)
31. [Jamba-1.5: Hybrid Transformer-Mamba Models at Scale](https://arxiv.org/pdf/2408.12570)
32. [From Collapse to Control: Understanding and Extending Context Length in Emerging Hybrid Models via Universal Position Interpolation](https://en.papernotes.org/ICLR2026/llm_efficiency/from_collapse_to_control_understanding_and_extending_context_length_in_emerging_/)
33. [Long Context Rope Yarn Mla Tutorial](https://wanshuiyin.github.io/ARIS-in-AI-Offer/tutorials/long_context_rope_yarn_mla_tutorial_en.html)