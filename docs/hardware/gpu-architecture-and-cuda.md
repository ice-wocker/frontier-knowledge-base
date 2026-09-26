# GPU 架构深入与 CUDA

> 最后更新：2026-09-26 ｜ 领域：硬件·芯片与设计 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

GPU 最初为图形渲染设计，其核心思路是用大量相对简单的流多处理器（SM，Streaming Multiprocessor）并行执行同一段代码的不同数据（SIMT，Single Instruction Multiple Threads）。与 CPU 相比，GPU 把大部分晶体管预算投入到算术单元与高带宽显存，而不是分支预测与大容量缓存，因此在矩阵乘法、卷积、注意力这类高数据并行算力密集负载上具有数量级优势。

随着深度学习成为主流负载，GPU 的硬件演进方向明显被 AI 牵引：张量核心（Tensor Core）从 Volta 引入，逐步增加低精度格式支持；显存从 GDDR 转向 HBM；片间互连带宽成为与算力同等重要的指标。NVIDIA 在 GTC 2026 上把这一趋势总结为"七颗芯片共同构成一台系统"（CPU、GPU、NVLink 交换、SuperNIC、DPU 等），标志着竞争焦点从单芯片转向机架级系统（[NVIDIA GTC LIVE 2026 Highlights](https://images.nvidia.com/nvimages/gtc/pdf/GTC26_SanJose_Highlights_Final.pdf)）。

## 最新进展（2025–2026）

**Hopper 到 Blackwell：** Hopper 架构（H100）引入线程块集群（Thread Block Clusters）这一新层级，允许一个线程块读写同一集群内其他线程块的共享内存，即分布式共享内存（Distributed Shared Memory），并把 CUDA 线程组层次扩展为线程、线程块、线程块集群、网格四级（[NVIDIA Hopper Architecture In-Depth](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/)）。H100 SXM 拥有 132 个 SM、每 SM 128 个 FP32 核心，L2 缓存由 A100 的 40MB 提升到 50MB（[Tuning CUDA Applications for Hopper GPU Architecture](https://docs.nvidia.com/cuda/archive/12.5.1/hopper-tuning-guide/index.html)）。

Blackwell 的关键变化是第二代 Transformer Engine 与新精度格式：Blackwell Tensor Core 引入社区定义的微缩放（microscaling）格式，用于在保持精度的同时替换更大位宽（[NVIDIA Blackwell Architecture](https://www.nvidia.com/en-sg/data-center/technologies/blackwell-architecture/)）。系统层面，第五代 NVLink 提供每 GPU 1.8TB/s 双向吞吐，NVLink 域最多可扩展到 576 个 GPU；NVLink 交换芯片让单个 72-GPU 域（NVL72）拥有 130TB/s 的 GPU 带宽（[NVIDIA Corporation Introduces the NVIDIA Blackwell Platform](https://nvidianews.nvidia.com/_gallery/download_pdf/65f8a7843d633205563719fc/)）。GB200 Grace Blackwell Superchip 通过 NVLink-C2C 把两颗 Blackwell GPU 与一颗 Grace CPU 连成一体（[NVIDIA GB200 NVL72](https://www.nvidia.com/en-eu/data-center/gb200-nvl72/)）。

**Blackwell Ultra 与 GB300：** Blackwell Ultra 单芯片稠密 NVFP4 算力由 Blackwell 的 10 PFLOPS 提升到 15 PFLOPS，相对 Blackwell 提升 1.5 倍、相对 Hopper H100/H200 提升 7.5 倍（[Inside NVIDIA Blackwell Ultra: The Chip Powering the AI Factory Era](https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/)）。GB300 NVL72 配置 72 颗 Blackwell Ultra GPU 与 36 颗 Grace CPU，GPU 内存 20TB、带宽最高 576TB/s，FP4 Tensor Core 达 1440 PFLOPS｜1080 PFLOPS（[NVIDIA GB300 NVL72](https://www.nvidia.com/en-in/data-center/gb300-nvl72/)）。

**Rubin 平台（2026）：** NVIDIA 在 GTC 2026 发布以天文学家 Vera Rubin 命名的平台，包含机架级 Vera Rubin NVL72 与 HGX Rubin NVL8。Rubin GPU 采用第三代 Transformer Engine 并支持硬件加速的自适应压缩，提供 50 PFLOPS 的 NVFP4 推理算力，搭载 288GB HBM4、带宽 22TB/s（[NVIDIA GTC LIVE 2026 Highlights](https://images.nvidia.com/nvimages/gtc/pdf/GTC26_SanJose_Highlights_Final.pdf)、[NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-gb/data-center/vera-rubin-nvl72/)）。Vera Rubin NVL72 集成 72 颗 Rubin GPU、36 颗 Vera CPU、ConnectX-9 SuperNIC 与 BlueField-4 DPU，使用 NVLink 6 交换芯片并向外扩展 Quantum-X800 InfiniBand（[NVIDIA Vera Rubin Platform](https://www.nvidia.com/en-us/data-center/technologies/rubin/)）。HGX Rubin NVL8 集成 8 颗 Rubin GPU 与第六代 NVLink，官方称相比 HGX B200 提供最高 10 倍 token 工厂吞吐，并以 1/4 的 GPU 数量达到相当训练性能（[NVIDIA HGX Platform](https://www.nvidia.com/en-us/data-center/hgx/)）。

**CUDA 工具链：** CUDA 13.0 是新的大版本，遵循语义化版本并在 13.x 系列内保证 ABI 稳定，与 r580 及更新的驱动兼容（[CUDA Toolkit Release Notes, Release 13.0](https://docs.nvidia.com/cuda/archive/13.0.0/pdf/CUDA_Toolkit_Release_Notes.pdf)）。13.0 引入基于 tile 的编程模型，让开发者对整个数据块定义操作，由编译器负责线程分配与 Tensor Core 映射，并统一了 Arm 服务器与嵌入式平台的工具链（[What's New and Important in CUDA Toolkit 13.0](https://developer.nvidia.com/blog/whats-new-and-important-in-cuda-toolkit-13-0)）。CUDA 13.3（2026 年 5 月 27 日）在 C++ 中引入 CUDA Tile 编程，并把支持范围扩展到计算能力 9.0（Hopper）（[CUDA Toolkit 13.3 Release Notes](https://docs.nvidia.com/cuda/pdf/CUDA_Toolkit_Release_Notes.pdf)、[NVIDIA CUDA 13.3 通过 C++ 中的平铺式编程增强 GPU 开发](https://developer.nvidia.cn/blog/nvidia-cuda-13-3-enhances-gpu-development-with-tile-programming-in-c-compiler-autotuning-and-python-updates/)）。

## 核心技术与关键概念

- **SM 与 warp：** 每个 SM 包含多个 warp 调度器，以 32 线程为一个 warp 执行；同一 warp 内线程共享指令流，分支发散会串行化执行。Hopper 每个 SM 有 128 个 FP32 核心，Ampere 为 64 个（[NVIDIA Hopper Architecture In-Depth](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/)）。
- **存储层级：** 寄存器、共享内存/L1、L2、HBM。H100 的 L2 为 50MB 且支持持久化控制（[Tuning CUDA Applications for Hopper GPU Architecture](https://docs.nvidia.com/cuda/archive/12.5.1/hopper-tuning-guide/index.html)）。带宽与容量是 LLM 推理的主要瓶颈，因此 HBM 代际与容量成为 GPU 规格竞争的核心。
- **Tensor Core 精度谱系：** FP64、TF32、BF16/FP16、FP8/FP6、INT8、FP4/NVFP4。H100 SXM 的 TF32 Tensor Core 为 989 TFLOPS、BF16 为 1979 TFLOPS（官方标注含稀疏加速）（[NVIDIA H100 GPU](https://www.nvidia.com/en-us/data-center/h100/)）。Blackwell 起采用微缩放格式，Blackwell Ultra 进一步强化 NVFP4。
- **线程块集群与分布式共享内存：** 集群保证一组线程块同时调度到一组 SM 上，可跨 SM 直接读写共享内存，并协同驱动张量内存加速器（TMA）等异步单元（[NVIDIA Hopper 深入研究架构](https://developer.nvidia.cn/blog/nvidia-hopper-architecture-in-depth/)）。
- **NVLink / NVLink-C2C / NVSwitch：** 用于 GPU 间与 CPU-GPU 间高带宽一致性互连。第五代 NVLink 单 GPU 双向 1.8TB/s，NVLink 域最高 576 GPU；NVLink 交换芯片在 NVL72 内提供 130TB/s 聚合带宽并支持 SHARP FP8 聚合（[NVIDIA Corporation Introduces the NVIDIA Blackwell Platform](https://nvidianews.nvidia.com/_gallery/download_pdf/65f8a7843d633205563719fc/)）。
- **CUDA 编程模型与生态库：** CUDA 提供 C++/Python/Fortran 接口，配合 cuDNN、cuBLAS、NCCL、TensorRT 等库。有券商研究统计，截至 2025 年 NVIDIA 开发者计划已汇聚约 600 万名开发者，CUDA 生态涵盖超过 400 个库、600 个 AI 模型与 3700 个 GPU 加速应用，累计下载量突破 5300 万次（[计算机行业-CUDA：英伟达护城河的构筑、松动与国产突围](http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/industry/rptid/838403661197/index.phtml)）。第三方分析引用的 NVIDIA 财报口径则分别为 FY2025 约 590 万开发者（[5.9 Million Developers Keep Nvidia Winning](https://www.stratrix.com/moat-anatomy/cuda-as-a-moat-why-developers)）与 FY2026 10-K 口径超过 750 万开发者（[CUDA Ecosystem Lock-In](https://fundalyst.xyz/NVDA/platform_premium/cuda_moat)），口径差异明显。

## 代表性项目 / 公司 / 产品（附官方链接）

| 产品 | 关键特征 | 官方链接 |
| --- | --- | --- |
| NVIDIA H100（Hopper） | 132 SM，L2 50MB，第四代 Tensor Core，TF32 989 TFLOPS | [nvidia.com/en-us/data-center/h100](https://www.nvidia.com/en-us/data-center/h100/) |
| NVIDIA B200（Blackwell） | HGX 形态 180GB HBM3E、约 7.7TB/s；GB200 形态 186GB、8TB/s | [Lenovo SR680a V3 with B200 Product Guide](https://lenovopress.lenovo.com/lp2247.pdf)、[NVIDIA B200](https://aiwiki.ai/wiki/nvidia_b200) |
| NVIDIA GB200 NVL72 | 72-GPU NVLink 域，作为单一大 GPU，万亿参数实时推理快 30 倍 | [nvidia.com/en-eu/data-center/gb200-nvl72](https://www.nvidia.com/en-eu/data-center/gb200-nvl72/) |
| NVIDIA GB300 NVL72 | 72×Blackwell Ultra + 36×Grace，20TB GPU 内存，576TB/s | [nvidia.com/en-in/data-center/gb300-nvl72](https://www.nvidia.com/en-in/data-center/gb300-nvl72/) |
| NVIDIA Vera Rubin NVL72 | 72×Rubin + 36×Vera，NVLink 6，Quantum-X800 | [nvidia.com/en-us/data-center/technologies/rubin](https://www.nvidia.com/en-us/data-center/technologies/rubin/) |
| Google TPU7x（Ironwood） | 每 VM 4 颗芯片，每芯片 2 个 TensorCore + 4 个 SparseCore，Pod 最高 9216 芯片 | [TPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines)、[A developer's guide to training with Ironwood TPUs](https://cloud.google.com/blog/products/compute/training-large-models-on-ironwood-tpus) |

## 关键数据与评测结果（附来源）

- **单芯片 vs 系统口径差异：** NVIDIA 官方产品页对 HGX B200 标称 FP4 Tensor Core 144 PFLOPS｜72 PFLOPS，对 GB300 NVL72 标称 1440 PFLOPS｜1080 PFLOPS（[NVIDIA HGX](https://www.nvidia.com/ja-jp/data-center/hgx/)、[NVIDIA GB300 NVL72](https://www.nvidia.com/en-in/data-center/gb300-nvl72/)）。这两组数据均为多卡聚合值且存在稀疏/稠密两列口径，与开发者博客给出的单芯片 10→15 PFLOPS 表述并不完全对应，引用时需明确口径。
- **TPU 与 GPU 推理对比：** 一项测试用 16 块 TPU v7 Ironwood 对阵 16 块 NVIDIA GB200，双方均以 vLLM 运行同一模型（Kimi K3），TPU 达到每秒约 709 个 token，GB200 为每秒约 452 个，TPU 快约 57%（[谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)）。另有分析机构称 Ironwood 在与 B200/B300 的对比中，每美元性能最高领先约 50%（[Google's TPUv7 beats Nvidia on cost per token](https://aiinsiders.net/article/googles-tpuv7-beats-nvidia-on-cost-per-token-analyst-finds)）。
- **Blackwell 推理基准：** 在 SemiAnalysis InferenceMAX v1 基准中，Blackwell B200 配合 TensorRT-LLM 的表现被评价为早期吞吐显著低于当前最优水平（[NVIDIA Blackwell Leads on SemiAnalysis InferenceMAX v1 Benchmarks](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks)）。
- **软件生态成熟度：** 有分析指出 AMD ROCm 在 2025 年下载量增长 10 倍，vLLM CI 通过率从 37% 提升到 93%（[ROCm: CUDA를 넘을 수 있는가](https://hiveworks-invest.com/stocks/amd/rocm/)）。

## 趋势与争议

1. **算力指标口径混乱。** 稀疏与稠密、单芯片与整机架、不同精度（FP4/FP8/BF16）混用，导致跨厂商比较极易失真；NVIDIA 官方产品页与开发者博客之间也存在可比性问题。
2. **机架级系统成为竞争单位。** NVL72/NVL144 这类整机架方案把竞争从芯片扩展到供电、液冷、NVLink 交换与网络，单芯片算力优势需要系统级兑现。
3. **CUDA 锁定与替代路径。** CUDA 的开发者规模、库数量与框架集成构成护城河；AMD ROCm 通过 HIP 提供 CUDA 兼容层，TPU 则依赖 XLA/编译器路线，各方在"迁移成本"上的博弈仍在持续。
4. **自研加速器的成本压力。** Google 的 Ironwood 以编译器为中心的软硬协同路线，配合 ICI、光交换与 DCN 组网（[A developer's guide to training with Ironwood TPUs](https://cloud.google.com/blog/products/compute/training-large-models-on-ironwood-tpus)），对以 GPU 为中心的采购结构形成替代压力。
5. **功耗与散热。** 单芯片 1000W 级 TGP、整机架数百千瓦，使液冷与供电设计成为架构的一部分，而非配套工程。
6. **出口管制影响产品形态。** 有报道称在新出口限制下，NVIDIA 面向中国市场的产品会在 Blackwell 代放弃 HBM3E 而改用 GDDR7，并以 RTX Pro 6000 为基础（[Новости по тегу gddr7](https://3dnews.ru/tags/gddr7)）。

## 参考来源

1. [NVIDIA GTC LIVE 2026 Highlights](https://images.nvidia.com/nvimages/gtc/pdf/GTC26_SanJose_Highlights_Final.pdf)
2. [NVIDIA Hopper Architecture In-Depth](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/)
3. [NVIDIA Hopper 深入研究架构（中文）](https://developer.nvidia.cn/blog/nvidia-hopper-architecture-in-depth/)
4. [Tuning CUDA Applications for Hopper GPU Architecture](https://docs.nvidia.com/cuda/archive/12.5.1/hopper-tuning-guide/index.html)
5. [NVIDIA Blackwell Architecture](https://www.nvidia.com/en-sg/data-center/technologies/blackwell-architecture/)
6. [NVIDIA Corporation Introduces the NVIDIA Blackwell Platform](https://nvidianews.nvidia.com/_gallery/download_pdf/65f8a7843d633205563719fc/)
7. [NVIDIA GB200 NVL72](https://www.nvidia.com/en-eu/data-center/gb200-nvl72/)
8. [NVIDIA GB300 NVL72](https://www.nvidia.com/en-in/data-center/gb300-nvl72/)
9. [NVIDIA DGX GB300](https://www.nvidia.com/en-eu/data-center/dgx-gb300/)
10. [Inside NVIDIA Blackwell Ultra: The Chip Powering the AI Factory Era](https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/)
11. [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-gb/data-center/vera-rubin-nvl72/)
12. [NVIDIA Vera Rubin Platform](https://www.nvidia.com/en-us/data-center/technologies/rubin/)
13. [NVIDIA HGX Platform](https://www.nvidia.com/en-us/data-center/hgx/)
14. [NVIDIA DGX B300](https://www.nvidia.com/es-la/data-center/dgx-b300/)
15. [CUDA Toolkit Release Notes, Release 13.3](https://docs.nvidia.com/cuda/pdf/CUDA_Toolkit_Release_Notes.pdf)
16. [CUDA Toolkit Release Notes, Release 13.0](https://docs.nvidia.com/cuda/archive/13.0.0/pdf/CUDA_Toolkit_Release_Notes.pdf)
17. [What's New and Important in CUDA Toolkit 13.0](https://developer.nvidia.com/blog/whats-new-and-important-in-cuda-toolkit-13-0)
18. [NVIDIA CUDA 13.3 通过 C++ 中的平铺式编程增强 GPU 开发](https://developer.nvidia.cn/blog/nvidia-cuda-13-3-enhances-gpu-development-with-tile-programming-in-c-compiler-autotuning-and-python-updates/)
19. [NVIDIA H100 GPU](https://www.nvidia.com/en-us/data-center/h100/)
20. [Lenovo ThinkSystem SR680a V3 with B200 Product Guide](https://lenovopress.lenovo.com/lp2247.pdf)
21. [NVIDIA B200（aiwiki）](https://aiwiki.ai/wiki/nvidia_b200)
22. [TPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines)
23. [A developer's guide to training with Ironwood TPUs](https://cloud.google.com/blog/products/compute/training-large-models-on-ironwood-tpus)
24. [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)
25. [谷歌TPU跑Kimi比英伟达GPU快57%（量子位）](http://m.toutiao.com/group/7689737267351306792/)
26. [Google's TPUv7 beats Nvidia on cost per token, analyst finds](https://aiinsiders.net/article/googles-tpuv7-beats-nvidia-on-cost-per-token-analyst-finds)
27. [NVIDIA Blackwell Leads on SemiAnalysis InferenceMAX v1 Benchmarks](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks)
28. [计算机行业-CUDA：英伟达护城河的构筑、松动与国产突围](http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/industry/rptid/838403661197/index.phtml)
29. [5.9 Million Developers Keep Nvidia Winning](https://www.stratrix.com/moat-anatomy/cuda-as-a-moat-why-developers)
30. [CUDA Ecosystem Lock-In](https://fundalyst.xyz/NVDA/platform_premium/cuda_moat)
31. [ROCm: CUDA를 넘을 수 있는가](https://hiveworks-invest.com/stocks/amd/rocm/)
32. [Новости по тегу gddr7](https://3dnews.ru/tags/gddr7)