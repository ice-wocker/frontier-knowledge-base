# 量化与模型压缩

> 最后更新：2026-09-26 ｜ 领域：AI·训练与推理工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

量化（Quantization）把模型权重与激活值从高精度浮点（FP16/BF16/FP32）转换为低位宽表示（FP8/INT8/INT4/FP4，甚至 INT2），以换取更小的显存占用、更高的显存带宽利用率与更高的 Tensor Core 吞吐。它是当前大模型落地中最"性价比"最高的优化手段：通常只需少量校准数据，不需重训，即可在几乎无精度损失的前提下显著降低服务成本。

量化按作用对象分为三类：**权重-only 量化**（如 W4A16，只压权重、激活保持 FP16）、**权重—激活联合量化**（如 W8A8、W4A4，需硬件支持低精度矩阵乘）、以及 **KV cache 量化**（KV cache 量化把缓存中的 K/V 张量以 FP8、INT8、INT4 或 INT2 等更低位宽格式存储，区别于前缀缓存、PagedAttention 或卸载——后三者决定缓存是否复用、如何分配或放在哪里）（[Model Quantization Guide: Foundations to Production Serving](https://slavadubrov.github.io/blog/2026/07/05/model-quantization-in-2026-from-foundations-to-production-serving/)）。NVIDIA 在其部署工具中把常用格式归纳为若干档：FP8 block-wise 权重-only、FP8 逐通道权重 + 动态逐 token 激活、NVFP4（权重与激活的默认 FP4 量化）、INT8 SmoothQuant（逐通道权重、逐张量激活）以及 W4A16（AWQ 校准的 4 位权重-only，激活保持 FP16）（[Optimizing LLMs for Performance and Accuracy with Post-Training Quantization](https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization/)）。

## 最新进展（2025–2026）

**FP8 成为数据中心推理的默认精度。** 到 2026 年，FP8 已是 H100、H200、B200 上数据中心 LLM 推理的默认精度。FP8 有两种格式：**E4M3**（4 位指数、3 位尾数）用于权重与激活，**E5M2**（5 位指数、2 位尾数）用于训练期的梯度；E4M3 提供的动态范围足以覆盖主流推理负载（[Production LLM Inference — Part 2: Quantization and KV Cache](https://www.tekblueprint.org/blog/ai/llm-inference-quantization-kv-cache/)）。一项覆盖多种模型与任务的评测同样指出，FP8 是所有模型尺寸与任务上最可靠的量化方法；但在 405B 参数等超大模型上 SmoothQuant 会遇到问题（[Exploring the Trade-Offs: Quantization Methods, Task Difficulty, and Model Size in Large Language Models From Edge to Giant](https://earino.github.io/applied-deep-learning/week5/readings/lee2025_quantization_trade_offs.pdf)）。

**FP4 与 NVFP4 自 Blackwell 起进入生产。** NVFP4 的数据格式由 1 位符号、2 位指数、1 位尾数（E2M1）构成，可表示的数值幅度上限约为 ±6，采用层次化块缩放（hierarchical block scaling）把多个缩放因子组合以恢复高精度数值（[NVFP4 — Transformer Engine](https://docs.nvidia.com/deeplearning/transformer-engine-releases/release-2.17/user-guide/features/low_precision_training/nvfp4/nvfp4.html)）。与 MXFP4 相比，NVFP4 在每个 16 值块上使用一个共享的 FP8（E4M3）缩放因子，并再加一个更高层的 FP32 逐张量缩放因子；两个差异都很关键——更小的块（16 对 32）使单个离群值污染的值减半，更细的 E4M3 缩放则提供更细的调节档位（[Pushing Intelligence to 4-bit](https://research.nvidia.com/labs/eai/blogs/pushing-intelligence-to-4-bit/)）。NVFP4 与 INT4 不同，它保留浮点语义，拥有共享指数与紧凑尾数，因而动态范围更好；Blackwell Tensor Core 支持 FP16/FP8/FP4 的混合精度执行（[Quantize Models to NVFP4 with NVIDIA Model Optimizer](https://build.nvidia.com/station/nvfp4-quantization)）。NVFP4 相比 BF16 约有 3.5 倍更小的显存占用，适合高 batch、计算受限的负载（[Faster Diffusion on Blackwell: MXFP8 and NVFP4 with Diffusers and TorchAO](https://pytorch.org/blog/faster-diffusion-on-blackwell-mxfp8-and-nvfp4-with-diffusers-and-torchao/)）。

**低精度训练成为现实。** NVIDIA 在介绍 NVFP4 时指出，该格式自 Blackwell 架构起在芯片中实现，并在众多库中获得支持，可在保持与更高精度格式相当准确性的同时获得 4 位浮点的性能与能效优势（[NVFP4 加速 AI 训练与推理的三大方式](https://developer.nvidia.cn/blog/3-ways-nvfp4-accelerates-ai-training-and-inference/)）。Blackwell 是 NVIDIA 首个原生支持 FP4 的架构，借助 GB200 与 GB300 的 FP4 吞吐，可在保持训练所需精度、规模与并行性的前提下实现 4 位训练（[NVFP4 实现 16 位训练精度，4 位训练速度和效率](https://developer.nvidia.cn/blog/nvfp4-trains-with-precision-of-16-bit-and-speed-and-efficiency-of-4-bit/)）。NVIDIA Nemotron 3 Super 即以前述 NVFP4 完成预训练，并报告了稳定且准确的预训练表现（[Nemotron 3 Super Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)）。

## 核心技术与关键概念

**AWQ（Activation-aware Weight Quantization）** 基于"权重的重要性取决于激活分布"这一观察，对重要权重通道做逐通道缩放，以降低量化误差并实现高效低位宽量化；其缩放因子形式为 `s_j = max(|X_j|)^α / max(|W_j|)^(1-α)`，并对 α∈[0,1] 做网格搜索（[Model Quantization: Concepts, Methods, and Why It Matters](https://developer.nvidia.com/blog/model-quantization-concepts-methods-and-why-it-matters)、[Edge-ASR: Towards Low-Bit Quantization of Automatic Speech Recognition Models](https://arxiv.org/html/2507.07877v1/)）。AWQ 属于权重-only 的 W4A16 设计，在 4-bit 下可靠，低于 4-bit 时退化，此时向量量化码本方法 AQLM 与 QuIP# 更合适（[AWQ (Activation-aware Weight Quantization)](https://aiwiki.ai/wiki/awq/edit)）。

**GPTQ** 独立地对权重矩阵的每一行做量化，利用近似二阶信息（Hessian 矩阵）指导量化过程，以最小化量化引入的输出误差，从而在性能损失极小的前提下完成高效压缩（[Model Quantization: Concepts, Methods, and Why It Matters](https://developer.nvidia.com/blog/model-quantization-concepts-methods-and-why-it-matters)）。一份 2026 年的量化综述回顾了这一脉络，指出分组量化（group-wise quantization）此后成为主流方法：GPTQ 借助 Hessian 信息在逐层、逐组层面实现了准确的 INT3 或 INT4 量化，是首次对大规模模型实现高精度 PTQ 权重-only 量化（[A Survey of Quantization in LLM: Unlocking Potential Hardware Efficiency](https://jcst.ict.ac.cn/en/article/pdf/preview/10.1007/s11390-026-5979-1?issue=1&year=2026)）。

**SmoothQuant** 与 AWQ 共享逐通道缩放思想，但双向作用以支持 INT8 计算下的 W8A8 量化，与 AWQ 的权重-only 设计互补（[AWQ — aiwiki](https://aiwiki.ai/wiki/awq/edit)）。

**QLoRA 与 NF4**：只训练低秩矩阵 A、B 而冻结基座参数，同时对基座权重与 A、B 矩阵施加 NF4 量化，在保持高精度模型统计特性的同时大幅降低显存占用（[FedSODA: Federated Fine-tuning of LLMs via Similarity Group Pruning and Orchestrated Distillation Alignment](https://arxiv.org/html/2508.12727v1)）。

**蒸馏（Distillation）与剪枝（Pruning）**：蒸馏让学生模型匹配教师模型的输出（标签或思维链），LoRA 式蒸馏冻结预训练参数、在每层注入可训练低秩适配器（[Scaling Laws for Task-Specific LLM Distillation](https://arxiv.org/html/2606.24747)）；剪枝侧，EPTS 提出统一的多稀疏度框架，通过一次优化产出单一"弹性"模型，可覆盖多种稀疏配置，并用 Multi-Sparsity Hierarchy LoRA 实现从低稀疏到高稀疏组的知识继承（[EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression](https://arxiv.org/html/2606.25285)）。

## 关键数据与评测结果

**W8A8-FP 近乎无损，W8A8-INT 有轻微代价，W4A4 仍然困难。** 一份系统评测给出量化"精度—性能"对照：W8A8-FP 量化基本无损，在全部基准上保持未压缩模型的准确率，通常落在评测误差范围内；W8A8-INT 平均每任务仅退化约 1–3%，远低于此前报道的 10% 以上下降（[“Give Me BF16 or Give Me Death”? Accuracy-Performance Trade-Offs in LLM Quantization](https://arxiv.org/html/2411.02355v2/)）。另一来源则总结出更细的经验规律：AWQ 在权重-only 量化中通常优于 GPTQ，硬件支持使 FP8 更具优势；在小模型上 4 位量化可能导致显著精度下降（GPTQ 尤甚），但 70B 级模型通常能在量化后维持较好表现（[Exploring the Trade-Offs: Quantization Methods, Task Difficulty, and Model Size](https://earino.github.io/applied-deep-learning/week5/readings/lee2025_quantization_trade_offs.pdf)）。一项针对扩散型 LLM（dLLM）的后训练量化研究显示，把 LLaDA 量化到 W8A8 仅有轻微性能下降且对具体方法不敏感，但进一步降到 W4 仍具挑战（[Quantization Meets dLLMs: A Systematic Study of Post-training Quantization for Diffusion LLMs](https://arxiv.org/html/2508.14896v3)）。AWEQ 在 OPT-175B 上的 W8A8 设置下报告在 HellaSwag、WinoGrande、ARC-e 上达到当时的 SOTA 水平（[AWEQ: Post-Training Quantization with Activation-Weight Equalization for Large Language Models](https://arxiv.org/pdf/2311.01305v3.pdf)）。

**NVFP4 的吞吐收益。** NVIDIA 称 NVFP4 在 Blackwell Ultra GPU 上可提供最高约 15 petaFLOPS 的峰值稠密吞吐，是同架构 FP8 吞吐的 3 倍；在 MLPerf Training 中，配备 512 块 Blackwell Ultra GPU 的多套 GB300 NVL72 系统以 NVFP4 在 64.6 分钟内完成 Llama 3.1 405B 预训练基准，达到 1.9 倍加速（[3 Ways NVFP4 Accelerates AI Training and Inference](https://developer.nvidia.com/blog/3-ways-nvfp4-accelerates-ai-training-and-inference/)）。在图像生成侧，TensorRT 借助 FP4 为 Blackwell GeForce RTX 50 系列解锁更快的本地推理，FLUX transformer 通过后训练量化与量化感知训练被压到 FP4 权重，在 Image Reward、CLIP-IQA 等指标上恢复并匹配 BF16 精度；另一种替代方案是 SVDQuant（[NVIDIA TensorRT Unlocks FP4 Image Generation for NVIDIA Blackwell GeForce RTX 50 Series GPUs](https://developer.nvidia.com/blog/nvidia-tensorrt-unlocks-fp4-image-generation-for-nvidia-blackwell-geforce-rtx-50-series-gpus/)）。

**KV cache 量化的精度—上下文权衡。** vLLM 的 `--kv-cache-dtype fp8` 会对 KV cache 量化，并以 FP8（e4m3）执行整个注意力计算（即 QK 与 ScoreV 矩阵乘），把 KV cache 存储减半，从而在硬件成本不变时支持更高并发或更长上下文——前提是精度站得住（[The State of FP8 KV-Cache and Attention Quantization in vLLM](https://vllm-project.github.io/2026/04/22/fp8-kvcache.html)）。一项对 TurboQuant 的系统评测发现，退化集中在最长上下文（128k–256k），说明低位 KV cache 量化误差会随序列长度累积；结论是 TQ 的 k8v4 与 4bit-nc 对长上下文检索是安全的，而 k3v4-nc 与 3bit-nc 出现明显精度退化，FP8 与更高位宽的 TQ 变体表现相当且推理性能更好（[A First Comprehensive Study of TurboQuant: Accuracy and Performance](https://vllm-project.github.io/2026/05/11/turboquant.html)）。面向上下文密集的 Agent 场景，UltraQuant 提出了把 KV cache 压到每元素 4 位的方案，以码本格式存储键值并在运行时即时反量化（[UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/html/2606.20474)）。

**工程选型对照。** 一套 2026 年的实践指南给出映射关系：高吞吐服务若为计算受限，应从 FP8 或 INT8 W8A8 入手（工具包括 FP8 PTQ、SmoothQuant、TensorRT-LLM、vLLM），需考察吞吐、TTFT 与任务精度；长上下文或高并发把 GPU 占满时，应使用 KV cache 量化（vLLM、TensorRT-LLM 或 Transformers QuantizedCache），需考察长上下文检索、时延、安全与质量；本地 CPU / Apple Silicon / 桌面推理则使用带本地张量编码的 GGUF 文件（llama.cpp、Ollama、LM Studio），需考察 prompt 时延、内存占用与主观输出质量（[Model Quantization Guide](https://slavadubrov.github.io/blog/2026/07/05/model-quantization-in-2026-from-foundations-to-production-serving/)）。

## 趋势与争议

1. **精度格式的收敛与分裂**：数据中心侧向 FP8 收敛，超低精度侧出现 MXFP8 / MXFP4 / NVFP4 等多种块缩放格式并存，跨硬件迁移需重新量化。
2. **块缩放粒度的取舍**：块越小越能抑制离群值影响，但缩放元数据开销上升，NVFP4 选择 16 是精度与开销的折中。
3. **KV cache 量化的质量风险**：它直接作用于每一层的注意力键值，对长上下文检索与安全相关行为的影响需单独评测；多来源数据显示低位（3-bit 级）KV 量化的误差会随上下文长度累积，不能只看通用基准。
4. **4-bit 激活仍不成熟**：W4A4 在多数模型上仍明显掉点，权重-only 的 W4A16 与 W8A8 是当前更稳妥的生产选择；同时 W8A8-FP 与 W8A8-INT 在精度代价上也存在明显差异（近乎无损 vs 约 1–3% 退化）。
5. **压缩手段的组合问题**：量化、蒸馏、剪枝可叠加，但误差会累积，多来源数据表明其复合效果高度依赖具体模型与任务。

## 参考来源

1. [Model Quantization Guide: Foundations to Production Serving](https://slavadubrov.github.io/blog/2026/07/05/model-quantization-in-2026-from-foundations-to-production-serving/)
2. [Optimizing LLMs for Performance and Accuracy with Post-Training Quantization — NVIDIA](https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization/)
3. [Production LLM Inference — Part 2: Quantization and KV Cache](https://www.tekblueprint.org/blog/ai/llm-inference-quantization-kv-cache/)
4. [Exploring the Trade-Offs: Quantization Methods, Task Difficulty, and Model Size in Large Language Models From Edge to Giant](https://earino.github.io/applied-deep-learning/week5/readings/lee2025_quantization_trade_offs.pdf)
5. [NVFP4 — Transformer Engine](https://docs.nvidia.com/deeplearning/transformer-engine-releases/release-2.17/user-guide/features/low_precision_training/nvfp4/nvfp4.html)
6. [Using FP8 and FP4 with Transformer Engine](https://nvidia.github.io/TransformerEngine/examples/fp8_primer.html)
7. [Pushing Intelligence to 4-bit](https://research.nvidia.com/labs/eai/blogs/pushing-intelligence-to-4-bit/)
8. [Quantize Models to NVFP4 with NVIDIA Model Optimizer](https://build.nvidia.com/station/nvfp4-quantization)
9. [Faster Diffusion on Blackwell: MXFP8 and NVFP4 with Diffusers and TorchAO](https://pytorch.org/blog/faster-diffusion-on-blackwell-mxfp8-and-nvfp4-with-diffusers-and-torchao/)
10. [NVFP4 实现 16 位训练精度，4 位训练速度和效率 — NVIDIA 技术博客](https://developer.nvidia.cn/blog/nvfp4-trains-with-precision-of-16-bit-and-speed-and-efficiency-of-4-bit/)
11. [NVFP4 加速 AI 训练与推理的三大方式 — NVIDIA 技术博客](https://developer.nvidia.cn/blog/3-ways-nvfp4-accelerates-ai-training-and-inference/)
12. [Nemotron 3 Super Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)
13. [Model Quantization: Concepts, Methods, and Why It Matters](https://developer.nvidia.com/blog/model-quantization-concepts-methods-and-why-it-matters)
14. [Edge-ASR: Towards Low-Bit Quantization of Automatic Speech Recognition Models](https://arxiv.org/html/2507.07877v1/)
15. [AWQ (Activation-aware Weight Quantization) — aiwiki](https://aiwiki.ai/wiki/awq/edit)
16. [A Survey of Quantization in LLM: Unlocking Potential Hardware Efficiency](https://jcst.ict.ac.cn/en/article/pdf/preview/10.1007/s11390-026-5979-1?issue=1&year=2026)
17. [FedSODA: Federated Fine-tuning of LLMs via Similarity Group Pruning and Orchestrated Distillation Alignment](https://arxiv.org/html/2508.12727v1)
18. [Scaling Laws for Task-Specific LLM Distillation](https://arxiv.org/html/2606.24747)
19. [EPTS: Elastic Post-Training Sparsity for Efficient Large Language Model Compression](https://arxiv.org/html/2606.25285)
20. [“Give Me BF16 or Give Me Death”? Accuracy-Performance Trade-Offs in LLM Quantization](https://arxiv.org/html/2411.02355v2/)
21. [Quantization Meets dLLMs: A Systematic Study of Post-training Quantization for Diffusion LLMs](https://arxiv.org/html/2508.14896v3)
22. [AWEQ: Post-Training Quantization with Activation-Weight Equalization for Large Language Models](https://arxiv.org/pdf/2311.01305v3.pdf)
23. [NVIDIA TensorRT Unlocks FP4 Image Generation for NVIDIA Blackwell GeForce RTX 50 Series GPUs](https://developer.nvidia.com/blog/nvidia-tensorrt-unlocks-fp4-image-generation-for-nvidia-blackwell-geforce-rtx-50-series-gpus/)
24. [The State of FP8 KV-Cache and Attention Quantization in vLLM](https://vllm-project.github.io/2026/04/22/fp8-kvcache.html)
25. [A First Comprehensive Study of TurboQuant: Accuracy and Performance](https://vllm-project.github.io/2026/05/11/turboquant.html)
26. [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/html/2606.20474)
27. [Revision History — OpenReview](https://openreview.net/revisions?id=7dEx4gBd7A)