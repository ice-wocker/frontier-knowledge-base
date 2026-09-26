# Transformer 架构原理

> 最后更新：2026-09-26 ｜ 领域：AI·基础原理 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

Transformer 由 Vaswani 等人在 2017 年论文《Attention Is All You Need》中提出，是此后所有主流大语言模型的基础架构（[The History of AI](https://99aiskills.com/en/courses/ai-fundamentals/lesson/history-of-ai)）。现代 LLM 的骨架可概括为"注意力 + FFN 的堆叠块"模式：GPT-4、Claude、Llama 4、DeepSeek-R1、Qwen3 等共享一批趋同的设计选择（[What Changed? How Modern LLMs Evolved Beyond the Original Transformer](https://llm.learnbeneficial.com/blog/llm/modern-llm-architectures/)）。

## 最新进展（2025–2026）

现代 LLM 相对原始 Transformer 的演进，集中在若干组件级的标准化上：

| 组件 | 原始 Transformer | 现代 LLM |
| --- | --- | --- |
| 位置编码 | 正弦式（Sinusoidal） | RoPE（旋转位置编码） |
| 归一化 | LayerNorm | RMSNorm |
| 注意力头 | MHA（多头） | GQA / MLA |
| 激活函数 | ReLU | SwiGLU |
| FFN 结构 | 单一大 FFN | MoE（稀疏混合专家） |

上述选择在 GPT-4、Claude、Llama 4、DeepSeek-R1、Qwen3 中基本一致（[What Changed? How Modern LLMs Evolved Beyond the Original Transformer](https://llm.learnbeneficial.com/blog/llm/modern-llm-architectures/)）。一个具体案例是 Supernova 架构，它组合使用 RoPE 做位置编码、GQA（3:1 压缩比）降低显存带宽需求、RMSNorm 提升计算效率、SwiGLU 改善梯度流，并称这些组件协同可最大化每参数的效率（[Supernova: Achieving More with Less in Transformer Architectures](https://arxiv.org/html/2507.15773v1)）。

2025–2026 年的两个显著走向是：（1）注意力机制向"混合"与"稀疏/线性替代"演进，以缓解长序列的二次复杂度；（2）FFN 层大规模稀疏化（MoE）以在固定推理算力下扩大参数池。代表案例包括 NVIDIA 的 Nemotron 3 Super——采用 Mamba-MoE 混合架构，512 个专家、top-22 路由（k=22），以 sigmoid 路由打分配合专家偏置，并用无辅助损失的负载均衡策略在 120.6B 参数上保证专家利用均衡（[Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)）；以及 MiniCPM-SALA，一个 9B 参数混合架构，按 1:3 比例交织稀疏注意力（InfLLM-V2）与线性注意力（Lightning Attention），并采用混合位置编码（HyPE）兼顾效率与长上下文性能（[MiniCPM-SALA: Hybridizing Sparse and Linear Attention for Efficient Long-Context Modeling](https://arxiv.org/html/2602.11761)）。

## 核心技术与关键概念

### 自注意力与多头注意力

自注意力（Self-Attention）的核心计算为 softmax(QKᵀ/√d_k)·V，其中 Query 表示"我在找什么"，Key/Value 由序列中各 token 生成（[KV-Caching in LLMs](https://saeedmehrang.github.io/blogs/language-modeling/llm-2025-overview/kv-caching/)）。多头注意力（Multi-Head Attention, MHA）将其并行化为多个子空间，使模型可从不同表示子空间同时关注信息。现代模型为降低推理显存与带宽，普遍改用 GQA（Grouped Query Attention，多个查询头共享同一组 K/V）或 MLA（Multi-head Latent Attention），在效率与表示能力之间取舍（[What Changed? How Modern LLMs Evolved](https://llm.learnbeneficial.com/blog/llm/modern-llm-architectures/)、[Supernova](https://arxiv.org/html/2507.15773v1)）。

### 位置编码与上下文扩展（RoPE / YaRN）

原始 Transformer 使用正弦式位置编码，现代模型转向 RoPE（Rotary Positional Embeddings），以更高效地编码位置（[Supernova](https://arxiv.org/html/2507.15773v1)）。RoPE 把位置信息编码为对 Q/K 的旋转，但当推理序列超出训练时的最大长度时，旋转角度会落在训练未见过的范围，导致注意力权重失真、性能下降（[Rotary Position Embeddings (RoPE) and Context Extension](https://calwoo.github.io/notes/concepts/deep-learning-engineering/rotary-embeddings/index.html)）。

YaRN（Yet another RoPE extensioN method）是系统化解决该问题的代表方法，其核心包括"NTK-by-parts"（按波长把维度分成三段分别处理）与"温度缩放"（对 softmax 前的 logits 施加全局温度，实践中通过把 √(1/t) 乘入 RoPE 的 cos/sin 缓存实现）（[YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/html/2309.00071v3)、[Long Context RoPE YaRN MLA Tutorial](https://wanshuiyin.github.io/ARIS-in-AI-Offer/tutorials/long_context_rope_yarn_mla_tutorial_en.html)）。YaRN 通过选择性重标定旋转频率与注意力幅度来外推上下文，仅插值编码全局结构的低频维度、保留负责局部次序的高频分量（[Analysing Extrapolation Capabilities of Modern Positional Embeddings](https://openreview.net/attachment?id=mEGr7Fm54B&name=pdf)）。

### 层归一化：Post-LN / Pre-LN / RMSNorm

归一化位置的演进尤为关键：

- **Post-LN（原始 Transformer）**：`output = LayerNorm(x + SubLayer(x))`，在残差相加之后归一化，可约束隐状态方差，但在深层模型中可能削弱梯度信号（[Peri-LN: Revisiting Normalization Layer in the Transformer Architecture](https://arxiv.org/pdf/2502.02732)、[Layer Normalisation in Transformers](https://learnixo.io/blog/ta-layer-norm)）。
- **Pre-LN（GPT、LLaMA 等现代默认）**：`output = x + SubLayer(LayerNorm(x))`，在子层之前归一化，保持残差路径"干净"，使深层训练更稳定；有资料指出 Post-LN 在没有 warmup 技巧时超过约 12 层即难以训练，而所有 50 层以上的现代 LLM 都采用 pre-norm（[Layer Normalisation in Transformers](https://learnixo.io/blog/ta-layer-norm)、[Layer Normalization](https://zeroentropy.dev/concepts/layer-normalization/)）。Pre-norm 被认为通过提供更干净的恒等路径稳定优化，带来更可预测的大规模训练轨迹（[Architectural Evolution And Component Standardisation In Modern Large Language Models](https://www.opsatscale.com/data-ai/architectural-evolution-modern-llms/)）。
- **RMSNorm**：与 LayerNorm 相比，RMSNorm(x) = (x / rms(x)) · γ 只做缩放、不居中、不除以标准差，因而计算更省（[how-to-train-your-gpt](http://raw.githubusercontent.com/raiyanyahya/how-to-train-your-gpt/master/chapters/06_transformer_block.md)）。

### FFN、SwiGLU 与 MoE

FFN 层方面，激活函数从 ReLU 转向门控线性单元，主流为 SwiGLU（Swish-Gated Linear Unit），被认为可改善参数效率与梯度流（[Architectural Evolution And Component Standardisation](https://www.opsatscale.com/data-ai/architectural-evolution-modern-llms/)、[Supernova](https://arxiv.org/html/2507.15773v1)）。

在超大模型中，单一稠密 FFN 常被稀疏 MoE 取代：以"许多更小的专家网络"替换一个大 FFN，每个 token 只激活少量专家，从而在扩大知识容量的同时付出线性级别的算力（[Mixture-of-Experts (MoE) in DeepSeek](https://www.manning.com/preview/build-a-deepseek-model-from-scratch/chapter-4)）。以 DeepSeek-V3 为例，其主模型参数达 671B，但每个 token 的激活路径仅约 37B 参数，由一个学习到的路由器为每个 token 选择专家（[Mixture of Experts DeepSeek: How MoE Models Work](https://codeforgeek.com/mixture-of-experts-deepseek/)）。NVIDIA 的说明指出，在 DeepSeek-R1、gpt-oss-120B 等 MoE 模型中，token 先经过与稠密架构相同的自注意力块，随后才由门控网络选择专家子集并逐层路由（[What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/?lv=true)）。DeepSeek-V3 的专家路由可用"专家中心嵌入"与输入表示的相似度来理解（[Unpacking DeepSeek-V3: From Architectural Renovations to Technical Innovations](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.175744930.06343205/v1)）。

### 注意力效率变体：滑动窗口、线性与混合

密集全连接注意力的复杂度随序列长度二次增长，因而出现多种高效替代（[Efficient Transformers: Sparse Attention and Linear Attention](https://kindatechnical.com/natural-language-processing/topic-2-lesson-9.html)）：

- **滑动窗口注意力（SWA）**：每个 token 只关注固定大小的邻近窗口，复杂度 O(n·w)，Longformer、Mistral 等采用；实践中常与"全局 token"（如序列开头的若干 token）结合（[Efficient Transformers](https://kindatechnical.com/natural-language-processing/topic-2-lesson-9.html)、[Alleviating Forgetfulness of Linear Attention](https://publications.idiap.ch/attachments/reports/2025/He_Idiap-RR-01-2026.pdf)）。SWAA 提出一套即插即用配方，让全注意力模型无需昂贵预训练即可适配 SWA，并通过保留"汇聚（sink）token"、交织全注意力与 SWA 层等方式缓解结构性缺陷（[SWAA: Sliding Window Attention Adaptation](https://arxiv.org/html/2512.10411v5)）。
- **线性/稀疏混合**：Power-based Partial Attention（PPA）把注意力复杂度参数化为 O(L^(1+p))，p=0 即线性复杂度的滑动窗口、p=1 即全注意力，用以系统研究"注意力缩放行为"对性能的影响（[Power-based Partial Attention](https://arxiv.org/html/2601.17334)）。InfoMamba 则用"概念瓶颈线性滤波层"替代 token 级自注意力，并耦合选择性递归流，属于无注意力的混合 Mamba-Transformer 设计（[InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model](https://arxiv.org/html/2603.18031v1)）。

### KV cache

KV cache 是 Transformer 推理的基础优化：自回归生成时，已计算过的 token 的 Key/Value 不再变化，只有新 token 的 Query 是新的，因此缓存 K/V 可消除对历史表示的重复计算（[KV-Caching in LLMs](https://saeedmehrang.github.io/blogs/language-modeling/llm-2025-overview/kv-caching/)）。但其显存占用随上下文长度线性增长，当上下文从数千扩展到百万 token 时，会成为 GPU 显存容量、显存带宽与吞吐的首要瓶颈（[KV Cache Optimization Strategies for Scalable and Efficient LLM Inference](https://arxiv.org/html/2603.20397)）。

2025–2026 年的应对手段包括量化与压缩：

- **KV 量化**：AWS 指出，把存储元素从 FP16（2 字节）压到 FP8（1 字节）或 INT4（0.5 字节），可将每 token 的 KV 体积降低 50–75%（[Accelerate inference with KV cache tiering on AWS](https://aws.amazon.com/blogs/storage/accelerate-inference-with-kv-cache-tiering-on-aws/)）。KV Pareto 工作系统比较了 int8/int4/int2 及混合精度（k8v8、k8v4、k8v2、k4v4、k4v2、k2v2）等方案（[KV Pareto: Systems-Level Optimization of KV Cache and Model Compression for Long Context Inference](https://aclanthology.org/anthology-files/pdf/eacl/2026.eacl-industry.9.pdf)）。
- **面向 MLA 的量化**：SnapMLA 指出 MLA 中 RoPE 分量对均匀量化高度敏感（FP8 量化会使 RoPE 分量的 MSE 上升一个数量级），因而提出"RoPE 感知"策略：仅对内容分量做 FP8 量化、把 RoPE 分量保留为 BF16（[SnapMLA: Efficient Long-Context MLA Decoding via Hardware-Aware FP8 Quantized Pipelining](https://arxiv.org/pdf/2602.10718.pdf)）。
- **剪枝与稀疏**：SWAN 以离线正交矩阵旋转并剪枝 KV cache，无需重建即可直接参与注意力计算，在每 token 节省 50–60% 显存的激进设置下仍接近未压缩基线（[SWAN: Sparse Winnowed Attention](https://arxiv.org/html/2511.18936)）；RaBitQCache 用随机旋转二进制量化与高吞吐 binary-INT4 运算估计注意力权重（[RaBitQCache: Rotated Binary Quantization for KVCache](https://arxiv.org/html/2606.31519)）。
- **产品级量化**：NVIDIA 的 NVFP4 KV cache 量化相较 FP8 可将显存占用降低最多 50%，在 LiveCodeBench、MMLU-PRO、MBPP、RULER 64K 等基准上精度损失小于 1%（[Optimizing Inference for Long Context and Large Batch Sizes with NVFP4 KV Cache](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache)）。

### 三种变体

按注意力掩码与用途，可分为：

- **Encoder-only**：双向注意力，适合理解类任务与嵌入，历史上以 BERT 系为代表（[How Does Tokenization Work?](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)）。
- **Decoder-only**：因果掩码，自回归生成，是当代生成式 LLM 的主流形态（[What Changed? How Modern LLMs Evolved](https://llm.learnbeneficial.com/blog/llm/modern-llm-architectures/)）。
- **Encoder-Decoder**：用于序列到序列任务，如翻译，历史上以 T5、原始 Transformer 为代表（[How Does Tokenization Work?](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)）。

## 趋势与争议

- **组件趋同 vs 架构创新**：多数前沿模型的组件选择已高度收敛，但注意力变体（GQA/MLA）、FFN 稀疏化（MoE）与位置外推仍是活跃创新点（[What Changed? How Modern LLMs Evolved](https://llm.learnbeneficial.com/blog/llm/modern-llm-architectures/)）。2026 年混合架构（Mamba + 注意力 + MoE）与稀疏/线性注意力的组合方案明显增多（[Nemotron 3 Super](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)、[MiniCPM-SALA](https://arxiv.org/html/2602.11761)）。
- **归一化位置的再审视**：有研究（Peri-LN）重新探讨归一化层在 Transformer 中的放置，说明"pre-norm 一统天下"并非没有争议（[Peri-LN](https://arxiv.org/pdf/2502.02732)）。
- **长上下文显存墙**：KV cache 的线性增长是长上下文部署的核心矛盾，量化与压缩在节省显存与保持精度之间持续权衡；MLA 等架构本身也引入了对量化更敏感的分量，进一步增加调优难度（[KV Cache Optimization Strategies](https://arxiv.org/html/2603.20397)、[SnapMLA](https://arxiv.org/pdf/2602.10718.pdf)、[NVFP4 KV Cache](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache)）。
- **混合架构的取舍**：线性/SSM 方案带来线性复杂度，但常被认为在保留高频结构细节上不及注意力，混合设计因此成为折中路径（[A Lightweight Hybrid Mamba Transformer for Image Super-Resolution](https://xplorestaging.ieee.org/document/11609999)）。

## 参考来源

- [What Changed? How Modern LLMs Evolved Beyond the Original Transformer](https://llm.learnbeneficial.com/blog/llm/modern-llm-architectures/)
- [The History of AI](https://99aiskills.com/en/courses/ai-fundamentals/lesson/history-of-ai)
- [Supernova: Achieving More with Less in Transformer Architectures](https://arxiv.org/html/2507.15773v1)
- [Architectural Evolution And Component Standardisation In Modern Large Language Models](https://www.opsatscale.com/data-ai/architectural-evolution-modern-llms/)
- [Peri-LN: Revisiting Normalization Layer in the Transformer Architecture](https://arxiv.org/pdf/2502.02732)
- [Layer Normalisation in Transformers](https://learnixo.io/blog/ta-layer-norm)
- [Layer Normalization](https://zeroentropy.dev/concepts/layer-normalization/)
- [how-to-train-your-gpt (chapters/06_transformer_block.md)](http://raw.githubusercontent.com/raiyanyahya/how-to-train-your-gpt/master/chapters/06_transformer_block.md)
- [KV-Caching in LLMs: The Optimization That Makes Inference Practical](https://saeedmehrang.github.io/blogs/language-modeling/llm-2025-overview/kv-caching/)
- [KV Cache Optimization Strategies for Scalable and Efficient LLM Inference](https://arxiv.org/html/2603.20397)
- [Optimizing Inference for Long Context and Large Batch Sizes with NVFP4 KV Cache](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache)
- [SWAN: Sparse Winnowed Attention](https://arxiv.org/html/2511.18936)
- [How Does Tokenization Work? Byte-Pair Encoding in Plain English](https://ai-tldr.dev/learn/llm-fundamentals/tokens-and-tokenization/how-tokenization-works/)
- [Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)
- [MiniCPM-SALA: Hybridizing Sparse and Linear Attention for Efficient Long-Context Modeling](https://arxiv.org/html/2602.11761)
- [Rotary Position Embeddings (RoPE) and Context Extension](https://calwoo.github.io/notes/concepts/deep-learning-engineering/rotary-embeddings/index.html)
- [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/html/2309.00071v3)
- [Long Context RoPE YaRN MLA Tutorial](https://wanshuiyin.github.io/ARIS-in-AI-Offer/tutorials/long_context_rope_yarn_mla_tutorial_en.html)
- [Analysing Extrapolation Capabilities of Modern Positional Embeddings in Vision Transformers](https://openreview.net/attachment?id=mEGr7Fm54B&name=pdf)
- [Mixture-of-Experts (MoE) in DeepSeek](https://www.manning.com/preview/build-a-deepseek-model-from-scratch/chapter-4)
- [Mixture of Experts DeepSeek: How MoE Models Work](https://codeforgeek.com/mixture-of-experts-deepseek/)
- [What Is Mixture of Experts? (NVIDIA)](https://www.nvidia.com/en-us/glossary/mixture-of-experts/?lv=true)
- [Unpacking DeepSeek-V3: From Architectural Renovations to Technical Innovations](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.175744930.06343205/v1)
- [Efficient Transformers: Sparse Attention and Linear Attention](https://kindatechnical.com/natural-language-processing/topic-2-lesson-9.html)
- [Alleviating Forgetfulness of Linear Attention by Hybrid Sparse Attention](https://publications.idiap.ch/attachments/reports/2025/He_Idiap-RR-01-2026.pdf)
- [SWAA: Sliding Window Attention Adaptation](https://arxiv.org/html/2512.10411v5)
- [Power-based Partial Attention: Bridging Linear-Complexity and Full Attention](https://arxiv.org/html/2601.17334)
- [InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model](https://arxiv.org/html/2603.18031v1)
- [Accelerate inference with KV cache tiering on AWS](https://aws.amazon.com/blogs/storage/accelerate-inference-with-kv-cache-tiering-on-aws/)
- [KV Pareto: Systems-Level Optimization of KV Cache and Model Compression](https://aclanthology.org/anthology-files/pdf/eacl/2026.eacl-industry.9.pdf)
- [SnapMLA: Efficient Long-Context MLA Decoding via Hardware-Aware FP8 Quantized Pipelining](https://arxiv.org/pdf/2602.10718.pdf)
- [RaBitQCache: Rotated Binary Quantization for KVCache](https://arxiv.org/html/2606.31519)
- [A Lightweight Hybrid Mamba Transformer for Image Super-Resolution](https://xplorestaging.ieee.org/document/11609999)