# 分布式训练与并行策略

> 最后更新：2026-09-26 ｜ 领域：AI·训练与推理工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

当模型参数、激活值与优化器状态总量远超单卡显存时，训练必须切分到多卡、多节点。分布式训练的核心就是把"计算、显存、通信"三者重新分配，主流切分维度包括：

- **数据并行（DP, Data Parallel）**：每卡持有完整模型副本，切分数据批次，反向传播后做梯度同步（AllReduce）。
- **张量并行（TP, Tensor Parallel）**：把单层内的矩阵乘按行/列切分到多卡，通信频繁，通常限定在节点内 NVLink 域。
- **流水并行（PP, Pipeline Parallel）**：把不同层分配到不同 stage，stage 之间用点对点传递激活与梯度，以 micro-batch 填满流水线（[Parallelism strategies for distributed training](https://rocm.docs.amd.com/projects/primus/en/latest/04-technical-guides/parallelism-strategies.html)）。
- **专家并行（EP, Expert Parallel）**：MoE 模型把不同专家放到不同设备，靠 all-to-all 路由 token。
- **序列并行 / 上下文并行（SP / CP）**：沿序列维度切分激活，用于长序列与长上下文训练。

**流水线气泡**是 PP 的固有代价：当某个 stage 等待输入而其他 stage 在计算时会产生空闲时间，所有并行策略的组合目标本质上是在通信量、显存占用与气泡之间取平衡（[Parallelism strategies for distributed training](https://rocm.docs.amd.com/projects/primus/en/latest/04-technical-guides/parallelism-strategies.html)）。

## 最新进展（2025–2026）

**框架侧向"自动化并行"演进。** PyTorch Conference North America 2026 上介绍的 DeepSpeed AutoTP、AutoSP、AutoEP，可在不重写代码的前提下为现有模型实现（包括大量 Hugging Face 模型）引入张量、序列与专家并行，并可与 ZeRO 组合用于大稠密模型、长上下文训练与 MoE 负载（[Open Research, Tooling & Optimization at PyTorch Conference North America 2026](https://pytorch.org/blog/open-research-tooling-optimization-at-pytorch-conference-north-america-2026/)）。

**Megatron Core 把 MoE 并行做成完整组合。** 其 MoE 功能页列出的能力包括：专家利用率优化的负载均衡损失、与 3D 并行集成的专家并行、EP + DP + TP + PP + SP 的完整并行组合、面向长序列 MoE 训练的上下文并行（CP）、用于大模型高效训练的并行折叠（Parallel Folding）异构映射，以及 MoE 专用分布式优化器（ZeRO-1 等价物）（[Mixture of Experts — Megatron Core](https://docs.nvidia.com/megatron-core/developer-guide/0.16.0/user-guide/features/moe.html)）。2026 年 1 月的开发版进一步加入流水线感知的细粒度激活卸载、Qwen3-Next 与 DeepSeek-V3.2（含 MTP）支持、Muon 与逐层分布式优化器，以及细粒度作用域的 CUDA Graph 支持（[Mixture of Experts — Megatron Core (nightly)](https://docs.nvidia.com/megatron-core/developer-guide/nightly/user-guide/features/moe.html)）。

**MoE 训练的显存效率成为独立研究方向。** 有工作提出"多并行组合（Mixture-of-Parallelisms）"以构建面向 MoE 的显存高效训练栈，并给出统一形式化：ZeRO-1 只切分优化器状态，ZeRO-2 额外切分梯度，ZeRO-3 再切分参数，各 rank 的持久状态量随并行度 W 递减（[Mixture-of-Parallelisms: Towards Memory-Efficient Training Stack for Mixture-of-Experts Models](https://arxiv.org/html/2607.01844)）。

## 核心技术与关键概念

**ZeRO 与 FSDP。** ZeRO（Zero Redundancy Optimizer）通过三级切分消除数据并行中的状态冗余；ZeRO-3 切分权重、梯度与优化器状态，使显存节省随数据并行度线性增长，并可通过 ZeRO-Infinity 卸载到 CPU 与 NVMe（[Zero Redundancy Optimizer](https://www.deepspeed.ai/tutorials/zero/)）。FSDP 是其在 PyTorch 中的实现：每卡只持有每个张量的 1/N，在计算某层前通过 AllGather 临时重建完整参数，反向传播后用 ReduceScatter 把梯度分片回各自的 owner（[A Practitioner's Guide to Distributed Training Parallelism](https://harsh-agarwal.github.io/distributed-training-parallelism/)）。

**3D 并行。** DeepSpeed 把数据并行、模型并行与流水并行的组合称为 3D 并行，宣称可为参数规模达万亿级的模型提供系统支持，并在 1.5B 到千亿级模型区间实现最高 10 倍加速（[Training Overview and Features](https://www.deepspeed.ai/training/)）。对 GPT-2/GPT-3 类架构，DeepSpeed 与 Megatron 已提供可直接复用的 3D 并行训练管线（[Training your large model with DeepSpeed](https://www.deepspeed.ai/tutorials/large-models-w-deepspeed/)、[Megatron-LM GPT2](https://www.deepspeed.ai/tutorials/megatron/)）。

**通信压缩。** 梯度同步在 ZeRO 模式下的开销尤为突出，压缩方法分为稀疏化、量化与低秩三类（[Taming Latency and Bandwidth: A Theoretical Framework and Adaptive Algorithm for Communication-Constrained Training](https://arxiv.org/html/2507.17346v2)）。量化方向中，1-bit Adam 把梯度压缩为单比特符号，相对 FP32 实现最高 32 倍压缩；QSGD 等方案以精度换带宽（[A Comprehensive Survey on Distributed Deep Learning Training](https://www.preprints.org/frontend/manuscript/0fd43cee939026cabc34cb2d3ed1821e/download_pub)）。

## 关键数据与评测结果

**梯度压缩的实测收益。** GIFT 提出几何感知的低精度梯度通信，在 64 台 GH200 超级芯片上把梯度通信量降低 75.0%，整体预训练时间减少 7.6%（[GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining](https://arxiv.org/html/2607.07494v1)）。EDGC 则以梯度熵的演化趋势动态调整压缩率，同时兼顾压缩效率与误差（[EDGC: Entropy-driven Dynamic Gradient Compression for Efficient LLM Training](https://arxiv.org/html/2511.10333v1)）。TAGC 针对 Transformer 结构做逐层选择性压缩与动态稀疏化，扩展了无损同态压缩方法以适配分片模型（[TAGC: Optimizing Gradient Communication in Distributed Transformer Training](https://dl.acm.org/doi/epdf/10.1145/3721146.3721946)）。

**容错与检查点（Checkpoint）的效率成为瓶颈。** FFTrainer 利用富余网络带宽快速存取状态以避免回滚，相比既有检查点方案把恢复时间最多降低 98%，并把 GPU 利用率损失最多减少 68%，且不影响正常训练（[FFTrainer: Fast Failover in Large-Language Model Training with Almost-Free State Management](https://arxiv.org/html/2512.03644)）。Amber 提出选择性增量检查点，只保留更新幅度显著的参数，实验识别出 2% 为有效经验阈值，可同时降低检查点耗时与存储开销（[Amber: Towards Fast and Space-Efficient Incremental Checkpointing in Large Language Model Training](https://dl.acm.org/doi/pdf/10.1145/3754598.3754606)）。TierCheck 采用三层式检查点：Tier-1 本地易失内存用于快速恢复，Tier-2 邻居节点易失内存异步复制以容忍单节点故障，Tier-3 远程持久存储用于持久化迁移（[TierCheck: Tiered Checkpointing for Fault Tolerance in Large Language Model Training](https://arxiv.org/html/2605.17821v1)）。DeadPool 则通过热替换（hot-swapping）在运行时不终止整个作业地把故障节点替换为备用节点，依赖关键路径外的内存检查点与通信子重建协议（[DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](https://arxiv.org/html/2607.01646v1)）。相关综述同时提到 MoEvement 相比当时最优方案把检查点开销与恢复开销分别最多降低 4 倍与 31 倍，端到端训练最多加速 8 倍（[TierCheck (Semantic Scholar)](https://www.semanticscholar.org/paper/TierCheck:-Tiered-Checkpointing-for-Fault-Tolerance-Han-Jiang/da2b798ec767a6ebbe3ba168a3b0cf077ee8fcb1)）。

## 代表性项目 / 公司 / 产品

- **Megatron-LM / Megatron Core**（NVIDIA）：张量并行与流水并行的工业参考实现，支持 EP、CP、SP 全组合与多种前沿 MoE 模型。
- **DeepSpeed**（Microsoft）：ZeRO、ZeRO-Infinity 与 3D 并行主力实现，2026 年新增 AutoTP / AutoSP / AutoEP。
- **PyTorch FSDP**：原生分片数据并行，是多数开源训练栈的默认选项。
- **Primus / ROCm**：AMD 生态下的并行策略实现与文档。

## 趋势与争议

1. **自动化 vs 手写切分**：AutoTP/AutoSP/AutoEP 降低了并行门槛，但在极端规模下手工调优的并行映射（如 Parallel Folding 的异构映射）通常仍有性能优势，二者并存。
2. **容错的成本被重新审视**：随着集群规模上升，故障成为常态而非异常，检查点不再只是"保险"，而是决定有效训练算力利用率（ETTR）的一等指标。
3. **压缩比与精度的张力**：激进压缩（如 1-bit）在受限网络下收益明显，但在高带宽 NVLink 集群中收益递减，需按互联条件选择策略。
4. **MoE 并行组合的复杂度**：EP 与 CP、SP 的自由组合带来大量可行配置，配置空间本身成为工程负担。

## 参考来源

1. [Parallelism strategies for distributed training (ROCm)](https://rocm.docs.amd.com/projects/primus/en/latest/04-technical-guides/parallelism-strategies.html)
2. [Mixture of Experts — Megatron Core 0.16.0](https://docs.nvidia.com/megatron-core/developer-guide/0.16.0/user-guide/features/moe.html)
3. [Mixture of Experts — Megatron Core (nightly)](https://docs.nvidia.com/megatron-core/developer-guide/nightly/user-guide/features/moe.html)
4. [Mixture-of-Parallelisms: Towards Memory-Efficient Training Stack for Mixture-of-Experts Models](https://arxiv.org/html/2607.01844)
5. [Open Research, Tooling & Optimization at PyTorch Conference North America 2026](https://pytorch.org/blog/open-research-tooling-optimization-at-pytorch-conference-north-america-2026/)
6. [Zero Redundancy Optimizer — DeepSpeed](https://www.deepspeed.ai/tutorials/zero/)
7. [A Practitioner's Guide to Distributed Training Parallelism](https://harsh-agarwal.github.io/distributed-training-parallelism/)
8. [Training Overview and Features — DeepSpeed](https://www.deepspeed.ai/training/)
9. [Training your large model with DeepSpeed](https://www.deepspeed.ai/tutorials/large-models-w-deepspeed/)
10. [Megatron-LM GPT2 — DeepSpeed](https://www.deepspeed.ai/tutorials/megatron/)
11. [Taming Latency and Bandwidth: A Theoretical Framework and Adaptive Algorithm for Communication-Constrained Training](https://arxiv.org/html/2507.17346v2)
12. [A Comprehensive Survey on Distributed Deep Learning Training](https://www.preprints.org/frontend/manuscript/0fd43cee939026cabc34cb2d3ed1821e/download_pub)
13. [GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining](https://arxiv.org/html/2607.07494v1)
14. [EDGC: Entropy-driven Dynamic Gradient Compression for Efficient LLM Training](https://arxiv.org/html/2511.10333v1)
15. [TAGC: Optimizing Gradient Communication in Distributed Transformer Training](https://dl.acm.org/doi/epdf/10.1145/3721146.3721946)
16. [FFTrainer: Fast Failover in Large-Language Model Training](https://arxiv.org/html/2512.03644)
17. [Amber: Towards Fast and Space-Efficient Incremental Checkpointing](https://dl.acm.org/doi/pdf/10.1145/3754598.3754606)
18. [TierCheck: Tiered Checkpointing for Fault Tolerance in Large Language Model Training](https://arxiv.org/html/2605.17821v1)
19. [DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint](https://arxiv.org/html/2607.01646v1)
20. [TierCheck (Semantic Scholar)](https://www.semanticscholar.org/paper/TierCheck:-Tiered-Checkpointing-for-Fault-Tolerance-Han-Jiang/da2b798ec767a6ebbe3ba168a3b0cf077ee8fcb1)