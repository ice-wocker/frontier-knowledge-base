# GPU 编程与算子：CUDA、Triton 与 FlashAttention

> 最后更新：2026-09-26 ｜ 领域：AI·训练与推理工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

大模型的训练与推理性能，最终取决于 GPU 上算子（kernel）的实现质量。所谓"算子工程"，是围绕 NVIDIA GPU 的执行模型做三件事：**把数据搬运与计算重叠**、**减少 HBM 与片上存储之间的往返**、**消除 host 侧启动开销**。这三件事分别对应 FlashAttention 系列、算子融合（fusion）与 CUDA Graphs。

CUDA 的执行模型以线程束（warp）为调度单位，以线程块（block）映射到流式多处理器（SM），通过共享内存（shared memory / SMEM）与寄存器做片上暂存。Hopper 架构引入 TMA（Tensor Memory Accelerator）作为硬件异步拷贝引擎，可在不占用 SM 计算资源的情况下在 HBM 与 SMEM 之间搬运张量，并提供比 Ampere 更大的矩阵乘指令 WGMMA；H100 还具备专用 FP8 Tensor Core（[FlashAttention Complete Guide (2026)](https://localaimaster.com/blog/flash-attention-guide)）。到 Blackwell 世代，矩阵乘转向张量内存（TMEM）子系统与 TCGEN05 指令，SMEM 容量与 TMEM 容量进一步增大（[CUTLASS Overview](https://docs.nvidia.com/cutlass/latest/overview.html)）。

## 最新进展（2025–2026）

**FlashAttention-4：算法与流水线协同设计。** 论文《FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling》指出，Blackwell 代际上不对称的硬件扩展（张量核算力增速快于其他单元）要求重新设计流水线；该方法在 B200 上使用 BF16 时相对 cuDNN 9.13 最高快 1.3×、相对 Triton 最高快 2.7×，达到最高 1613 TFLOPs/s（约 71% 硬件利用率），并完全用嵌入 Python 的 CuTe-DSL 实现（[FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://arxiv.org/html/2603.05451)）。第三方技术分析复述了同一组数据（B200/HGX B200、BF16、1613 TFLOPs/s、71% 利用率、相对 cuDNN 9.13 的 1.3× 与相对 Triton 的 2.7×）（[FlashAttention-4 gives the NVIDIA Blackwell platform its most optimized attention kernel yet](https://lambda.ai/blog/flashattention-4-gives-the-nvidia-blackwell-platform-its-most-optimized-attention-kernel-yet)）。

**低精度与端到端块缩放注意力。** PyTorch 官方博客介绍把 FlashAttention-4 扩展为支持 MXFP8 的前向与反向，在 LLM 形状上达到 2.85 PF/s 前向、2 PF/s 反向；在其内部形状上前向 2.54 PF/s、反向 1.58 PF/s，相对 BF16 最高提升 1.6× 与 1.52×，并把量化融合进周边生产者以形成端到端块缩放注意力（[Low Precision Flash Attention 4: End-to-End Block-Scaled Attention for Blackwell](https://pytorch.org/blog/low-precision-flash-attention-4-end-to-end-block-scaled-attention-for-blackwell/)）。

**FlexAttention 接入 FA4 后端。** PyTorch 为 FlexAttention 增加 FlashAttention-4 后端，可自动生成 CuTeDSL 的 score/mask 修改函数并按自定义注意力变体 JIT 实例化 FA4；在 Hopper 与 Blackwell 上，计算受限工作负载相对既有 Triton 实现获得 1.2×–3.2× 性能提升（[FlexAttention + FlashAttention-4: Fast and Flexible](https://pytorch.org/blog/flexattention-flashattention-4-fast-and-flexible/)）。

**CUDA 工具链与 Python 绑定快速迭代。** CUDA 13.3 引入 C++ 层面的 tile programming、编译器自动调优与 Python 更新：CompileIQ 使用进化算法自动调优编译器配置，在 GEMM 与 attention 算子上带来最高 15% 加速；CCCL 3.3 增加 DLPack 与 mdspan 张量互操作；NVCC 提供完整 C++23 支持，并集成 nvprune 用于多架构产物管理（[NVIDIA CUDA 13.3 Enhances GPU Development](https://developer.nvidia.com/blog/nvidia-cuda-13-3-enhances-gpu-development-with-tile-programming-in-c-compiler-autotuning-and-python-updates)）。CUDA 13.4 进一步加入 Windows on Arm 支持、对共享 GPU 的更细粒度控制与 locality domains（[CUDA Toolkit 13.4 Adds Windows on Arm Support](https://developer.nvidia.com/blog/cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus)）。官方还发布了 CUDA Python 1.0，提供稳定的 API、统一的底层 1:1 cuda-python 绑定与 CUDA Pathfinder 组件定位能力（[CUDA Python 1.0: Stable APIs, One Foundation, Full Platform Access](https://developer.nvidia.com/blog/cuda-python-1-0-stable-apis-one-foundation-full-platform-access/)）。NVIDIA HPC SDK 26.9 支持 CUDA 13.x 与 12.x，其打包组件来自 CUDA 13.3U1 与 12.9U1（[NVIDIA HPC SDK Release Notes](https://docs.nvidia.com/hpc-sdk/release-notes/index.html)）。NVIDIA 另发布《The Modern CUDA Toolbox in Practice》，以逐步优化的方式演示现代 CUDA 工具箱的使用（[The Modern CUDA Toolbox in Practice](https://developer.nvidia.com/blog/the-modern-cuda-toolbox-in-practice-a-step-by-step-optimization-walkthrough/)）。

**Triton 生态从"替代写 kernel"走向"跨平台与后端对接"。** NVIDIA 与 OpenAI 合作推出 Triton-to-TileIR 桥接，让 Triton kernel 可以面向 NVIDIA 的 tile-based 编程模型编译而非直接生成 PTX，从而在保留 tile 级语义的同时利用 Tensor Core 能力与架构可移植性；可通过环境变量切换编译流水线，也可按 kernel 选择后端（[Advancing GPU Programming with the CUDA Tile IR Backend for OpenAI Triton](https://developer.nvidia.com/blog/advancing-gpu-programming-with-the-cuda-tile-ir-backend-for-openai-triton)）。Triton 本身是 OpenAI 开发的基于 Python 的 DSL，用高层 tile 模型与自动优化简化 GPU 编程，在自定义 tile 级算子上常能接近手工调优实现的性能（[Leveraging AI Ecosystem for Portable and Sustainable GPU Kernels in HPC](https://dl.acm.org/doi/pdf/10.1145/3815001.3815003)）。一份对 NVIDIA CUDA Tile 的评估显示，cuTile 的 tile 级 API（`ct.mma` 加自定义 epilogue）适合在 Blackwell 上写 cuBLAS 难以实现的融合 GEMM 变体，但在其测试中性能约为 cuBLAS 的 52%–79%，而裸 SIMT 实现则慢约 64–217×（[Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs](https://arxiv.org/html/2604.23466v2)）。

## 核心技术与关键概念

- **算子融合（fusion）**：把多个逐元素/激活/量化操作合并进单个 kernel，消除中间张量的读写。NVIDIA 用 CuTe DSL 构建的高级融合 MLP kernel 把 GroupGEMM 与 SwiGLU、GeGLU、sReLU 等 GLU 激活以及 MXFP8 / NVFP4 的量化与转置融合在一起，相比未融合路径获得 1.3×–2× 的 kernel 级加速，并实现无同步的 MoE 执行以支持整迭代 CUDA Graph（[Boosting MoE Training Throughput with Advanced Fusion Kernels](https://developer.nvidia.com/blog/boosting-moe-training-throughput-with-advanced-fusion-kernels)）。PyTorch 面向推荐系统推理的 in-kernel broadcast 优化把用户结果在 GEMM epilogue 内按索引加载并寄存器内相加，使延迟从 0.798 ms 降到 0.580 ms（27.4%），同时消除 0.87 GB 中间 DRAM 流量（[In-Kernel Broadcast Optimization: Co-Designing Kernels for RecSys Inference](https://pytorch.org/blog/in-kernel-broadcast-optimization-co-designing-kernels-for-recsys-inference/)）。
- **CUDA Graphs**：把一串 CUDA 操作捕获为图并以单次 API 调用回放，大幅削减 kernel 启动的 CPU 侧开销，减少 CPU-GPU 同步与驱动开销；TensorRT-LLM 通过 CUDA Graph padding 提高缓存图的命中率（[Architecture Overview — TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/overview.html)）。其代价是要求固定张量形状、确定性显存分配与静态控制流（[Hybrid JIT–CUDA Graph Optimization for Low-Latency Large Language Model Inference](https://arxiv.org/pdf/2604.23467)）。Foundry 通过模板化的 CUDA graph context 物化来消除冷启动瓶颈，集入 vLLM 后把冷启动时延最多降低 99%（[Foundry: Template-Based CUDA Graph Context Materialization](https://arxiv.org/html/2604.06664v1)）。TensorRT for RTX 的自适应推理也使用 CUDA Graphs 消除"入队受限"，例如每次推理迭代获得约 1.8ms（23%）的提升（[Adaptive Inference in NVIDIA TensorRT for RTX](https://developer.nvidia.com/blog/adaptive-inference-in-nvidia-tensorrt-for-rtx-enables-automatic-optimization)）。
- **计算—通信重叠**：Syncopate 面向多 GPU AI kernel，按 chunk 粒度自动实现计算与通信重叠，编译器据任务图识别满足数据依赖所需的最小同步点集合（[Syncopate: Efficient Multi-GPU AI Kernels via Automatic Chunk-Centric Compute-Communication Overlap](https://arxiv.org/html/2601.20595v4)）。
- **NCCL 集合通信**：NCCL 2.31.2 引入 Compute Fabric Transport（CFT）的 host 与 device API，并增强 Parallel Aggregated Tree（PAT）算法——对 ReduceScatter/AllGather 增加层级化 kernel，节点内使用 NVLS、跨节点使用 PAT，改善中小消息性能（[NCCL Release 2.31.2](https://docs.nvidia.com/deeplearning/nccl/release-notes/rel_2-31-2.html)）。
- **GEMM 与 tile programming**：以 cuTile（NVIDIA）与 Triton（OpenAI）为代表的 DSL 提供比手写 CUDA C++ 更可移植、更易维护的方案，同时性能接近手工调优，已被用于半导体制造图像处理等非 AI 负载（[The Case for Block-Based Programming With cuTile and Triton](https://www.nvidia.com/en-us/on-demand/session/gtc26-s81894/)）。但研究也指出 Triton 对 warp 级调度控制不足，难以实现细粒度的 MMA–激活重叠，这会限制某些融合场景的上限（[Tile-Level Activation Overlap for Efficient LLM Inference](https://arxiv.org/html/2607.02521)）。
- **运行时 API 演进**：CUDA 13.0 的 features archive 记录了若干执行与调度相关的新增能力，包括允许对内核中所有 block 的"调度而非完成"建立依赖的 launch completion events（用以为调度提供更紧的控制）、查询 MPS 是否运行的 API、返回内核函数名的驱动 API，以及在 libnvJitLink 中返回 nvJitLink 版本号的 API（[CUDA Features Archive Release 13.0](https://docs.nvidia.com/cuda/archive/13.0.2/pdf/CUDA_Features_Archive.pdf)）。这些接口反映了 CUDA 运行时在调度粒度与可观测性上的持续细化。

## 代表性项目 / 公司 / 产品

- **FlashAttention 系列**（Tri Dao 等）：IO-aware 注意力的事实标准，FA-2 / FA-3 / FA4 分别针对 Ampere、Hopper 与 Blackwell；FA4 以 CuTe-DSL（Python 嵌入）实现（[FlashAttention-4](https://arxiv.org/html/2603.05451)）。
- **Triton**（OpenAI）：Python DSL，广泛用于 Liger Kernel 等训练算子库，其 JIT 特性让调用方库更轻量、更可移植（[Liger Kernel: Efficient Triton Kernels for LLM Training](https://arxiv.org/pdf/2410.10989v3)）；TRITONMoE 则用纯 Triton 实现融合 MoE dispatch，全部 162 个测试在 AMD MI300X 上零改动通过（[Cross-Platform Fused MoE Dispatch in Triton](https://arxiv.org/pdf/2605.23911v1.pdf)）。AMD 侧还出现基于 TLX 的 GEMM + Activation 融合实现，并与 rocBLAS 等库做对比（[Optimizing GEMM + Activation on CDNA4 with TLX](https://www.amd.com/en/developer/resources/technical-articles/2026/optimizing-gemm-with-tlx.html)）。
- **NCCL / NVSHMEM**（NVIDIA）：集合通信与单边通信库；官方建议多数应用开发者直接使用这类通信库而非自行实现底层通信（[CUDA Toolkit 13.4](https://developer.nvidia.com/blog/cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus)）。
- **TensorRT-LLM**：把融合、量化、CUDA Graph 与插件化 attention 集成到统一插件体系。
- **CUTLASS / cuTe DSL**：NVIDIA 的模板化 GEMM/卷积库与设备端 DSL，其文档显示在 Blackwell SM100 上可接近理论峰值（[CUTLASS Overview](https://docs.nvidia.com/cutlass/latest/overview.html)）。

## 关键数据与评测结果

硬件—软件协同的端到端收益可观：NVIDIA 与 Sarvam AI 联合优化后，Sarvam 30B 主权模型在 Blackwell 上相对 H100 基线获得 4× 推理加速；该模型使用 128 专家的异构 MoE 架构，top-6 或 top-8 路由，基于 NVIDIA NeMo 框架从零训练（[How NVIDIA Extreme Hardware-Software Co-Design Delivered a Large Inference Boost](https://developer.nvidia.com/blog/how-nvidia-extreme-hardware-software-co-design-delivered-a-large-inference-boost-for-sarvam-ais-sovereign-models/)）。

FlashAttention-4 的注意力吞吐在不同精度下差异显著：B200 上 BF16 达 1613 TFLOPs/s（71% 利用率），MXFP8（FA4 MX8）在其内部形状上达 2.54 PF/s 前向 / 1.58 PF/s 反向，相对 BF16 有最高 1.6× / 1.52× 提升（[FlashAttention-4](https://arxiv.org/html/2603.05451)、[Low Precision Flash Attention 4](https://pytorch.org/blog/low-precision-flash-attention-4-end-to-end-block-scaled-attention-for-blackwell/)）。这些数字均来自论文与厂商/框架官方博客，属自评口径。

kernel 启动间隙的优化也存在不同技术路线：有报道指出 CUDA Graphs 与 NVIDIA PDL 技术能缩短 kernel 之间的交接间隙，但 kernel 边界依然存在，而 megakernel 方案直接消除了该边界（[谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)）。

## 趋势与争议

1. **CUDA C++ vs tile DSL**：Triton/cuTile 显著降低了算子开发门槛并改善可移植性，但在需要极致调度控制的场景（如 warp specialization、TMA 多阶段流水、细粒度 MMA–激活重叠）仍以手写 CUDA/CuTe 为主；cuTile 在实测中约为 cuBLAS 的 52%–79%，反映"可定制性"的性能代价（[Evaluating CUDA Tile](https://arxiv.org/html/2604.23466v2)）。
2. **架构代际迁移成本上升**：Blackwell 用 TCGEN05/TMEM 取代 WGMMA/SMEM，导致大量既有 kernel 需要结构性重写，算子库的架构适配成为持续负担；FA4 即为"算法—流水线协同设计"应对不对称硬件扩展的产物（[FlashAttention-4](https://arxiv.org/html/2603.05451)）。
3. **CUDA Graphs 的静态性约束**：捕获要求固定形状与静态控制流，与投机解码、动态批处理等动态负载存在张力，工程上依赖 padding 与模板化方案缓解。
4. **跨平台诉求增强**：TRITONMoE 在 AMD MI300X 上零改动通过测试、AMD 推进 TLX 融合算子，反映算子层对厂商无关性的需求正在上升。
5. **性能数据的口径差异**：注意力吞吐数字高度依赖精度（BF16/FP8/MXFP8）、形状与实现（FA4 vs cuDNN vs Triton），跨来源与跨精度不可直接比较。

## 参考来源

1. [FlashAttention Complete Guide (2026)](https://localaimaster.com/blog/flash-attention-guide)
2. [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](https://tridao.me/publications/flash3/flash3.pdf)
3. [FlashAttention-3: Fast and Accurate Attention With Asynchrony and Low Precision (NVIDIA GTC)](https://www.nvidia.com/en-us/on-demand/session/gtc25-S71368/)
4. [Flash Attention 3](https://aiwiki.ai/wiki/flash_attention_3)
5. [NVIDIA CUDA 13.3 Enhances GPU Development with Tile Programming in C++, Compiler Autotuning, and Python Updates](https://developer.nvidia.com/blog/nvidia-cuda-13-3-enhances-gpu-development-with-tile-programming-in-c-compiler-autotuning-and-python-updates)
6. [CUDA Toolkit 13.4 Adds Windows on Arm Support and Greater Control over Shared GPUs](https://developer.nvidia.com/blog/cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus)
7. [Advancing GPU Programming with the CUDA Tile IR Backend for OpenAI Triton](https://developer.nvidia.com/blog/advancing-gpu-programming-with-the-cuda-tile-ir-backend-for-openai-triton)
8. [Leveraging AI Ecosystem for Portable and Sustainable GPU Kernels in HPC](https://dl.acm.org/doi/pdf/10.1145/3815001.3815003)
9. [Boosting MoE Training Throughput with Advanced Fusion Kernels](https://developer.nvidia.com/blog/boosting-moe-training-throughput-with-advanced-fusion-kernels)
10. [Architecture Overview — TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/overview.html)
11. [Hybrid JIT–CUDA Graph Optimization for Low-Latency Large Language Model Inference](https://arxiv.org/pdf/2604.23467)
12. [Foundry: Template-Based CUDA Graph Context Materialization for Fast LLM Serving Cold Start](https://arxiv.org/html/2604.06664v1)
13. [Adaptive Inference in NVIDIA TensorRT for RTX Enables Automatic Optimization](https://developer.nvidia.com/blog/adaptive-inference-in-nvidia-tensorrt-for-rtx-enables-automatic-optimization)
14. [Syncopate: Efficient Multi-GPU AI Kernels via Automatic Chunk-Centric Compute-Communication Overlap](https://arxiv.org/html/2601.20595v4)
15. [NCCL Release 2.31.2](https://docs.nvidia.com/deeplearning/nccl/release-notes/rel_2-31-2.html)
16. [The Case for Block-Based Programming With cuTile and Triton](https://www.nvidia.com/en-us/on-demand/session/gtc26-s81894/)
17. [Liger Kernel: Efficient Triton Kernels for LLM Training](https://arxiv.org/pdf/2410.10989v3)
18. [Cross-Platform Fused MoE Dispatch in Triton](https://arxiv.org/pdf/2605.23911v1.pdf)
19. [How NVIDIA Extreme Hardware-Software Co-Design Delivered a Large Inference Boost for Sarvam AI's Sovereign Models](https://developer.nvidia.com/blog/how-nvidia-extreme-hardware-software-co-design-delivered-a-large-inference-boost-for-sarvam-ais-sovereign-models/)
20. [谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)
21. [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://arxiv.org/html/2603.05451)
22. [FlashAttention-4 gives the NVIDIA Blackwell platform its most optimized attention kernel yet (Lambda)](https://lambda.ai/blog/flashattention-4-gives-the-nvidia-blackwell-platform-its-most-optimized-attention-kernel-yet)
23. [Low Precision Flash Attention 4: End-to-End Block-Scaled Attention for Blackwell (PyTorch)](https://pytorch.org/blog/low-precision-flash-attention-4-end-to-end-block-scaled-attention-for-blackwell/)
24. [FlexAttention + FlashAttention-4: Fast and Flexible (PyTorch)](https://pytorch.org/blog/flexattention-flashattention-4-fast-and-flexible/)
25. [Evaluating CUDA Tile for AI Workloads on Hopper and Blackwell GPUs](https://arxiv.org/html/2604.23466v2)
26. [CUDA Python 1.0: Stable APIs, One Foundation, Full Platform Access](https://developer.nvidia.com/blog/cuda-python-1-0-stable-apis-one-foundation-full-platform-access/)
27. [NVIDIA HPC SDK Release Notes](https://docs.nvidia.com/hpc-sdk/release-notes/index.html)
28. [The Modern CUDA Toolbox in Practice: A Step-by-Step Optimization Walkthrough](https://developer.nvidia.com/blog/the-modern-cuda-toolbox-in-practice-a-step-by-step-optimization-walkthrough/)
29. [Optimizing GEMM + Activation on CDNA4 with TLX (AMD)](https://www.amd.com/en/developer/resources/technical-articles/2026/optimizing-gemm-with-tlx.html)
30. [Tile-Level Activation Overlap for Efficient LLM Inference](https://arxiv.org/html/2607.02521)
31. [In-Kernel Broadcast Optimization: Co-Designing Kernels for RecSys Inference (PyTorch)](https://pytorch.org/blog/in-kernel-broadcast-optimization-co-designing-kernels-for-recsys-inference/)
32. [CUTLASS Overview (NVIDIA)](https://docs.nvidia.com/cutlass/latest/overview.html)
33. [CUDA Features Archive Release 13.0](https://docs.nvidia.com/cuda/archive/13.0.2/pdf/CUDA_Features_Archive.pdf)