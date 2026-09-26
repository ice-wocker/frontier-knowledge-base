# MoE 稀疏架构

> 最后更新：2026-09-26 ｜ 领域：AI·基础原理 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

混合专家（Mixture of Experts, MoE）通过让网络的局部组件"条件性激活"来突破稠密模型的算力约束：一个 MoE 层拥有 N 个独立的 FFN（称为"专家"）以及一个决定每个 token 使用哪些专家的小型路由器网络；对任一 token，只有 k 个专家被激活，其余不参与计算，因此模型可拥有远超单次前向所需参数量的总参数（[Mixture of Experts (MoE) Models: Why They're Dominating 2025](https://www.generalcompute.com/blog/mixture-of-experts-moe-models-why-theyre-dominating-2025)）。这种设计常被称为"稀疏激活"。

在 DeepSeek-R1、gpt-oss-120B 等 MoE 大模型中，token 先经过与稠密架构相同的自注意力模块，随后门控网络（gating network）检查注意力输出、选取目标专家子集并据此路由每个 token；这种稀疏路由在连续的 MoE 层中重复，逐步塑造模型的内部表示，直至产生最终输出（[What Is Mixture of Experts? — NVIDIA Glossary](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)）。到 2025 年，MoE 已成为高效扩展大语言模型的主导架构，Mixtral 8x7B、DeepSeek-V2 等均以 MoE 在控制推理成本的前提下实现巨大参数量（[Product of Experts and Mixture of Experts](https://vinesmsuic.github.io/paper-poe-moe/)）。

## 最新进展（2025–2026）

- **DeepSeek-V3**：671B 总参数、每 token 激活 37B，采用 Multi-head Latent Attention（MLA）与 DeepSeekMoE 架构，并首创"无辅助损失"（auxiliary-loss-free）的负载均衡策略，以尽量减少为促进均衡而带来的性能下降（[DeepSeek-V3 Technical Report](https://arxiv.org/pdf/2412.19437)）。DeepSeek V3 共 61 层，其中 58 层包含 256 个路由专家（[The Architecture Revolution: MoE Is Changing AI Economics](https://aichronicle.co/the-architecture-revolution-how-mixture-of-experts-is-changing-ai-training-economics/)）。
- **DeepSeek-V4（2026）**：2026 年 4 月发布预览版本，包含两个 MoE 模型——V4-Pro 为 1.6T 总参数（49B 激活）、V4-Flash 为 284B 总参数（13B 激活），均支持 100 万 token 上下文；架构上保留 DeepSeekMoE 框架与多 token 预测（MTP）策略，并引入混合注意力（Compressed Sparse Attention 与 Heavily Compressed Attention 组合）、流形约束超连接（Manifold-Constrained Hyper-Connections, mHC）与 Muon 优化器（[DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-v4-model-card-EN.pdf)、[DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)）。NVIDIA 亦列出 V4-Pro 1.6T/49B 与 V4-Flash 284B/13B 的配置，最大输出长度经 DeepSeek API 可达 384K token（[Build with DeepSeek V4 Using NVIDIA Blackwell and GPU-Accelerated Endpoints](https://developer.nvidia.com/blog/build-with-deepseek-v4-using-nvidia-blackwell-and-gpu-accelerated-endpoints)）。
- **Llama 4（2025-04）**：Scout 为 17B 激活参数、16 个专家、109B 总参数，并把支持上下文从 Llama 3 的 128K 提升到最高 1000 万 token；Maverick 为 17B 激活参数、128 个专家、400B 总参数，两者原生多模态并支持 12 种语言（[Intel Data Center AI Solutions Support Llama 4 Release](https://www.intel.cn/content/www/us/en/developer/articles/technical/intel-ai-solutions-support-llama-4-release.html)、[The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes](https://sekunde.github.io/data/llama4.pdf)）。
- **gpt-oss（2025）**：OpenAI 的开放推理模型 gpt-oss-120b 与 gpt-oss-20b 面向桌面、笔记本与数据中心本地运行，权重在 Hugging Face 免费下载并默认做 MXFP4 量化，使 120B 模型可放入 80GB 内存、20B 版本仅需 16GB（[gpt-oss 介绍](https://openai.com/ko-KR/index/introducing-gpt-oss/)）。
- **细粒度专家与共享专家**：DeepSeekMoE 采用细粒度专家分解，将部分专家设为"共享专家"（始终激活），其余按 token 亲和度路由，以在不牺牲通用知识的前提下让专家发展专长（[The Architecture Revolution](https://aichronicle.co/the-architecture-revolution-how-mixture-of-experts-is-changing-ai-training-economics/)）。
- **路由器成为研究焦点**：2025 年出现 LASER 等即插即用的推理时路由算法，根据 gate 分数分布的形状自适应调整——当分数偏好明确时路由到最强专家，当分数较均匀时扩大候选集并路由到负载最低者，且无需重新训练即可接入现有 MoE 推理管线（[From Score Distributions to Balance: Plug-and-Play Mixture-of-Experts Routing](https://arxiv.org/html/2510.03293v1)）。
- **PyTorch 原生 MoE 训练栈**：NVIDIA NeMo Automodel 提供在 PyTorch 中以原生分布式并行训练大规模 MoE 的开源库，把完全分片数据并行（FSDP）、专家并行、流水并行与上下文并行，与 Transformer Engine kernel（如 CUDNN RMSNorm、CUDNN Linear、DotProductAttention）结合，并集成 Megatron-Core 的高级 token 路由与计算组件（[Democratizing Large-Scale Mixture-of-Experts Training with NVIDIA PyTorch Parallelism](https://developer.nvidia.com/blog/accelerating-large-scale-mixture-of-experts-training-in-pytorch)）。
- **MoE 推理服务优化**：针对 MoE 模型的推理分析指出，GB200 NVL72 的 NVLink 架构使每个输入 token 被动态路由到其所需专家所在的 GPU，配合 NVIDIA Dynamo 可分析 GPU 容量指标来决定如何服务请求或分配 GPU worker（[How NVIDIA GB200 NVL72 and NVIDIA Dynamo Boost Inference Performance for MoE Models](https://developer.nvidia.com/blog/how-nvidia-gb200-nvl72-and-nvidia-dynamo-boost-inference-performance-for-moe-models/)）。

## 核心技术与关键概念

### 路由机制

Top-K 路由是标准策略：路由器（线性层 + softmax）为每个 token 选出得分最高的 k 个专家并加权组合其输出（[Mixture of Experts (MoE) Explained](https://gurusup.com/blog/mixture-of-experts-moe-explained)、[Mixtral of Experts](https://arxiv.org/pdf/2401.04088v1)）。DeepSeek 的路由机制用一个线性层把隐藏维度映射到 n 个路由专家，以按语义内容对每个 token 分别路由——专家是在 token 级别而非序列（或查询）级别选择的（[DeepSeek Inference Theoretical Model](https://aleph-alpha.com/blog-assets/DeepSeek-Inference-Theoretical-Model_Deriving-the-performance-from-hardware-primitives_02092025.pdf)）。

- **Mixtral 8x7B**：每层由 8 个前馈专家组成，对每个 token 选择 2 个专家；架构与 Mistral 7B 相同，仅将 FFN 替换为专家集合（[Mixtral of Experts](https://arxiv.org/pdf/2401.04088v1)）。其总参数为 47B，但每 token 的激活计算量远小于同等总参数量的稠密模型（[Mixtral 8×7B 论文解读](https://hatohato.jp/ai/papers/20260429_jiang_mixtral.html)）。
- **DeepSeek-V3**：在 256 个细粒度专家中使用 top-8 路由（[Mixture of Experts (MoE) Explained](https://gurusup.com/blog/mixture-of-experts-moe-explained)）。

k 越大，每 token 计算越多、质量可能越好；k 越小越高效，但可能错过相关专家知识（[Mixture of Experts (MoE) Explained](https://gurusup.com/blog/mixture-of-experts-moe-explained)）。

路由器通过梯度下降学习，因此路由是可变的、训练中会漂移，可能不稳定；若不加约束，路由器常收敛到只使用 8 个专家中的 2–3 个（[MoE models: Mixtral, Llama 4, Qwen3](https://theneuralbase.com/transformer-architecture/learn/intermediate/moe-models-mixtral-llama-4-qwen3/)）。在对 Mixtral 的分析中，路由器显示出可测量的专长倾向，例如 Python 关键词倾向于某些专家、数学术语倾向于另一些专家，这种专长并非人工编程，而是从训练中涌现（[Chapter 30: Mixture of Experts](https://waylandz.com/llm-transformer-book-en/chapter-30-mixture-of-experts/)）。

### 负载均衡损失

为防止"路由坍缩"（routing collapse，即少数专家被过度使用），多数生产级 MoE 实现引入辅助的负载均衡损失，以保持专家使用均衡（[MoE models: Mixtral, Llama 4, Qwen3](https://theneuralbase.com/transformer-architecture/learn/intermediate/moe-models-mixtral-llama-4-qwen3/)）。DeepSeek-V3 则提出无辅助损失的均衡策略，转向用偏置项等方式调节负载，以避免辅助损失带来的性能退化（[DeepSeek-V3 Technical Report](https://arxiv.org/pdf/2412.19437)）。

### 专家并行与通信

MoE 训练依赖专家并行（Expert Parallelism, EP）：需要 all-to-all 集合通信把 token 分派到其被分配的专家所在设备，再收集结果（[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/html/2603.07685)）。每次 all-to-all 的每 GPU 发送量约为 T·K·h·(EP−1)/EP，其中 T 为本地 token 数、K 为 top-k、h 为隐藏维度，一次完整的 dispatch-and-combine 周期使通信量翻倍（[Scalable Training of MoE Models with Megatron Core](https://arxiv.org/html/2603.07685)）。EP 过程通常分为三个阶段：先按专家对 token 做重排（dispatching），再以 All-to-All 在设备间交换 token 数据，使每个设备只收到本地专家所需的 token，随后各设备对自己的 token 批次做专家计算（[MoE Parallel Folding: Heterogeneous Parallelism Mappings for Efficient Large-Scale MoE Model Training with Megatron Core](https://arxiv.org/pdf/2504.14960)）。该工作还提出"MoE Parallel Folding"，解耦注意力层与 MoE 层的并行方式，并使用五维混合并行（张量、专家、上下文、数据、流水并行）（[MoE Parallel Folding](https://arxiv.org/pdf/2504.14960)）。

工程上，NVIDIA Megatron Core 提供多种 token dispatcher：标准 alltoall 基于 NCCL 进行 token 交换，适合常规 EP 场景；FlexDispatcher 配 DeepEP 后端可在跨节点通信时去除冗余 token、把节点内/间通信融合为单个 kernel，适合跨节点 EP 与细粒度 MoE（如 DeepSeek-V3）（[Mixture of Experts (Megatron Core)](https://docs.nvidia.com/megatron-core/developer-guide/0.15.0/user-guide/features/moe.html)）。NVIDIA 的 Wide Expert Parallelism 在 NVL72 机架级系统上把专家分布到 8 个以上 GPU，以缓解 DeepSeek-R1（256 专家、671B 参数）等大模型的权重加载压力并提升 GroupGEMM 效率（[Scaling Large MoE Models with Wide Expert Parallelism on NVL72 Rack Scale Systems](https://developer.nvidia.com/blog/scaling-large-moe-models-with-wide-expert-parallelism-on-nvl72-rack-scale-systems)）。

## 关键数据与评测结果

| 模型 | 总参数 | 每 token 激活 | 路由配置 |
| --- | --- | --- | --- |
| Mixtral 8x7B | 47B | 每 token 仅激活所选 2 个专家（远低于总参数） | 8 专家，top-2 |
| DeepSeek-V3 | 671B | 37B | 256 路由专家，top-8（含共享专家） |
| DeepSeek-V4-Flash | 284B | 13B | DeepSeekMoE + MTP，1M 上下文 |
| DeepSeek-V4-Pro | 1.6T | 49B | DeepSeekMoE + MTP，1M 上下文 |
| Llama 4 Scout | 109B | 17B | 16 专家 |
| Llama 4 Maverick | 400B | 17B | 128 专家 |
| gpt-oss-120b | 120B | — | 默认 MXFP4 量化，可放入 80GB 内存 |

数据来源：[Mixtral of Experts](https://arxiv.org/pdf/2401.04088v1)、[Mixtral 8×7B 论文解读](https://hatohato.jp/ai/papers/20260429_jiang_mixtral.html)、[DeepSeek-V3 Technical Report](https://arxiv.org/pdf/2412.19437)、[DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-v4-model-card-EN.pdf)、[Intel Data Center AI Solutions Support Llama 4 Release](https://www.intel.cn/content/www/us/en/developer/articles/technical/intel-ai-solutions-support-llama-4-release.html)、[gpt-oss 介绍](https://openai.com/ko-KR/index/introducing-gpt-oss/)、[Mixture of Experts (MoE) Explained](https://gurusup.com/blog/mixture-of-experts-moe-explained)。Mixtral 8x7B 以稀疏 MoE 在开源模型中超越了当时的 GPT-3.5 与 LLaMA 2 70B（[Mixtral 8×7B 论文解读](https://hatohato.jp/ai/papers/20260429_jiang_mixtral.html)）。

## 趋势与争议

- **稀疏与稠密的取舍**：MoE 用更大的总参数换取更低的每 token 计算，但要求更高的显存容量与更复杂的通信/路由系统；稠密模型则在部署简单性上占优（[Mixture of Experts (MoE) Models](https://www.generalcompute.com/blog/mixture-of-experts-moe-models-why-theyre-dominating-2025)、[Scalable Training of MoE with Megatron Core](https://arxiv.org/html/2603.07685)）。由于每 token 只计算一部分参数，MoE 模型能以更低的推理算力达到与远大于其激活规模的稠密模型相近的基准表现，其代价是全部专家参数仍需可寻址（[Open Source LLMs: The Best Models You Can Run Yourself in 2026](https://www.aitooldiscovery.com/ai-infra/open-source-llm-models-explained)）。
- **通信墙**：跨节点 all-to-all 是 MoE 训练与推理的主要瓶颈，其延迟随设备数增长；在大规模训练中，通信时间可能超过计算时间而成为首要瓶颈，催生了分层 all-to-all、并行协同调度与 Wide-EP 等优化（[System for MOE Models](https://llmsystem.github.io/llmsystem2026spring/assets/files/llmsys-17-MoE-3aa3125f9ccdd4bb7109ef077fbe9260.pdf)、[Efficient MoE Pre-training at Scale on 1K AMD GPUs with TorchTitan](https://pytorch.org/blog/efficient-moe-pre-training-at-scale-with-torchtitan/)）。
- **负载均衡的两难**：辅助损失能稳定训练，但可能损害模型质量；无辅助损失的方案尝试在两者间取得平衡，仍是活跃争议点（[DeepSeek-V3 Technical Report](https://arxiv.org/pdf/2412.19437)）。
- **总参数与激活参数的口径差异**：模型报告的总参数与每 token 激活参数回答的是不同问题，两者应始终被分别标注，比较时不应混淆（[DeepSeek V4 architecture: MoE, 1M context, and verified specifications](https://deepseek-v4.io/architecture)）。
- **小尺寸 MoE 的兴起**：以 Qwen3.6-35B-A3B（35B 总参数 / 3B 激活）为代表的全开源 MoE，把"以激活参数换成本"的思路带到更小的部署规模，提供 agentic coding 与多模态感知能力（[Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All](https://qwen.ai/blog?id=qwen3.6-35b-a3b)）。

## 参考来源

- [Mixture of Experts (MoE) Models: Why They're Dominating 2025](https://www.generalcompute.com/blog/mixture-of-experts-moe-models-why-theyre-dominating-2025)
- [What Is Mixture of Experts? — NVIDIA Glossary](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)
- [Mixture of Experts (MoE) Explained: How Sparse Activation Powers AI at Scale](https://gurusup.com/blog/mixture-of-experts-moe-explained)
- [From Score Distributions to Balance: Plug-and-Play Mixture-of-Experts Routing](https://arxiv.org/html/2510.03293v1)
- [Product of Experts and Mixture of Experts](https://vinesmsuic.github.io/paper-poe-moe/)
- [The Architecture Revolution: MoE Is Changing AI Economics](https://aichronicle.co/the-architecture-revolution-how-mixture-of-experts-is-changing-ai-training-economics/)
- [DeepSeek-V3 Technical Report](https://arxiv.org/pdf/2412.19437)
- [DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-v4-model-card-EN.pdf)
- [DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)
- [Build with DeepSeek V4 Using NVIDIA Blackwell and GPU-Accelerated Endpoints](https://developer.nvidia.com/blog/build-with-deepseek-v4-using-nvidia-blackwell-and-gpu-accelerated-endpoints)
- [DeepSeek V4 architecture: MoE, 1M context, and verified specifications](https://deepseek-v4.io/architecture)
- [Intel Data Center AI Solutions Support Llama 4 Release](https://www.intel.cn/content/www/us/en/developer/articles/technical/intel-ai-solutions-support-llama-4-release.html)
- [The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes](https://sekunde.github.io/data/llama4.pdf)
- [gpt-oss 介绍 — OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/)
- [Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All](https://qwen.ai/blog?id=qwen3.6-35b-a3b)
- [DeepSeek V3 (NVIDIA Megatron Bridge)](https://docs.nvidia.com/nemo/megatron-bridge/0.4.2/models/llm/deepseek-v3.html)
- [Mixtral of Experts](https://arxiv.org/pdf/2401.04088v1)
- [Mixtral 8×7B 论文解读](https://hatohato.jp/ai/papers/20260429_jiang_mixtral.html)
- [MoE models: Mixtral, Llama 4, Qwen3](https://theneuralbase.com/transformer-architecture/learn/intermediate/moe-models-mixtral-llama-4-qwen3/)
- [Chapter 30: Mixture of Experts](https://waylandz.com/llm-transformer-book-en/chapter-30-mixture-of-experts/)
- [Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/html/2603.07685)
- [MoE Parallel Folding: Heterogeneous Parallelism Mappings for Efficient Large-Scale MoE Model Training with Megatron Core](https://arxiv.org/pdf/2504.14960)
- [Mixture of Experts (Megatron Core)](https://docs.nvidia.com/megatron-core/developer-guide/0.15.0/user-guide/features/moe.html)
- [Scaling Large MoE Models with Wide Expert Parallelism on NVL72 Rack Scale Systems](https://developer.nvidia.com/blog/scaling-large-moe-models-with-wide-expert-parallelism-on-nvl72-rack-scale-systems)
- [Democratizing Large-Scale Mixture-of-Experts Training with NVIDIA PyTorch Parallelism](https://developer.nvidia.com/blog/accelerating-large-scale-mixture-of-experts-training-in-pytorch)
- [How NVIDIA GB200 NVL72 and NVIDIA Dynamo Boost Inference Performance for MoE Models](https://developer.nvidia.com/blog/how-nvidia-gb200-nvl72-and-nvidia-dynamo-boost-inference-performance-for-moe-models/)
- [Open Source LLMs: The Best Models You Can Run Yourself in 2026](https://www.aitooldiscovery.com/ai-infra/open-source-llm-models-explained)
- [System for MOE Models](https://llmsystem.github.io/llmsystem2026spring/assets/files/llmsys-17-MoE-3aa3125f9ccdd4bb7109ef077fbe9260.pdf)
- [Efficient MoE Pre-training at Scale on 1K AMD GPUs with TorchTitan](https://pytorch.org/blog/efficient-moe-pre-training-at-scale-with-torchtitan/)