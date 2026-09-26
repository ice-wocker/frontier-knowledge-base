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

**AI 加速器多极竞争（2025–2026）：** 数据中心加速器已从 NVIDIA 主导演变为"多极竞争 + 大厂自研"。AMD 在 2025 年推出 Instinct MI350 系列，MI350X/MI355X 配备 288GB HBM3E、8 TB/s 带宽，支持 MXFP6/MXFP4 数据类型（[AMD Instinct MI350 Series](https://www.amd.com/en/products/accelerators/instinct/mi350.html)、[AMD Instinct MI355X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html)）；2026 年 Advancing AI 大会发布 MI400 系列与机架级 AMD Helios，单机架集成 72 颗 MI455X GPU、4,600 CPU 核心、2.9 ExaFlops FP4 算力、31TB HBM 容量与 260 TB/s scale-up 带宽（[ADVANCING AI 2026（PDF）](https://newsroom.amd.com/documents/2026/07/2a710b7d-c107-4639-8855-fa9366f83967.pdf)），AMD 称 Helios 每美元推理 token 数比竞争对手高最多 30%（[AAI 2026 新闻稿](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)），Helios 参考设计已在 2026 年下半年进入量产部署、MI430X 预计 2027 年推出（[AMD Instinct MI400 Series](https://www.amd.com/en/products/accelerators/instinct/mi400.html)）。AMD 并与 Anthropic 达成战略合作，将部署最多 2GW 的 MI450 系列，首个 GW 于 2027 年上半年开始（[AMD and Anthropic 新闻稿](https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/)）。

**Google TPU：Ironwood 与第八代双芯片。** 第七代 TPU（TPU7x，代号 Ironwood）单 Pod 可达 9216 颗芯片，已于 2026 年 3 月 31 日 GA，Google 实测其相较 TPU v5p 的碳排放效率（CCI）提升 3.7 倍（[TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)、[Cloud TPU release notes](https://docs.cloud.google.com/tpu/docs/release-notes)、[Ironwood TPUs deliver 3.7x carbon efficiency gains](https://cloud.google.com/blog/topics/systems/ironwood-tpus-deliver-37x-carbon-efficiency-gains/)）。2026 年 Cloud Next 大会上，Google 发布第八代 TPU 并首次拆分为面向训练的 TPU 8t 与面向推理的 TPU 8i：TPU 8t 单 superpod 可扩展至 9600 颗 TPU、2 PB 共享高带宽内存、处理能力约为前代 3 倍（[Our eighth generation TPUs](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)、[Cloud Next '26](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)）。

**AWS Trainium3。** AWS 第四代 AI 芯片 Trainium3 于 2025 年 12 月 re:Invent 发布，是 AWS 首款 3nm AI 芯片，单颗提供 2.52 PFLOPS FP8 算力、内存容量提升 1.5 倍；Trn3 UltraServers 单系统最多集成 144 颗芯片，提供相较 Trn2 UltraServer 最高 4.4 倍算力与 4 倍能效，支持 MXFP8/MXFP4（[Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)、[Trainium3 UltraServers now available](https://www.aboutamazon.com/news/aws/trainium-3-ultraserver-faster-ai-training-lower-cost)）。

**Intel Gaudi 3。** Intel 的 Gaudi 3 在 2025 年扩大供货，推出标准 PCIe Gen5 形态的 Gaudi 3 PCIe 卡（HL-338），面向 LLM、多模态与企业 RAG 负载（[Intel Gaudi 3 PCIe Product Brief（PDF）](https://cdrdv2-public.intel.com/817488/Gaudi%203%20PCIe%20Product%20Brief_RB_1_V6.pdf)、[Intel®Gaudi® 3](https://habana.ai/products/gaudi3/)）。

**华为昇腾。** 华为 2025 年公开昇腾三年路线图：2026 年 Q1 推出面向推理 Prefill 与推荐场景的昇腾 950PR（采用自研 HBM），2026 年 Q4 推出面向推理 Decode 与训练的昇腾 950DT（[华为公布昇腾AI芯片未来3年迭代路线图](https://www.peopleapp.com/column/30050308165-500007097808)）。2026 年 9 月华为全联接大会 2026 上，轮值董事长汪涛表示昇腾 910C 超节点已部署超 1000 套、昇腾 950 超节点已规模商用、昇腾 960 研发进度超预期（[中国青年网](http://t.m.youth.cn/transfer/index/url/news.youth.cn/jsxw/202609/t20260917_16874687.htm)）；随后更新路线图，把 960DT 提前至 2027 年 Q1、960PR 提前至 2027 年 Q3，并首次引入 NPO 方案（[每日经济新闻](http://m.toutiao.com/group/7686424720039805480/)）。

**寒武纪。** 寒武纪 2025 年营业收入 64.97 亿元、同比增长 453.21%，归母净利润 20.59 亿元，实现扭亏为盈（[证券时报](https://www.stcn.com/article/detail/3991331.html)）；2026 年 Q1 营收 28.85 亿元、同比增长 159.56%，主要由思元 590 芯片出货驱动（[雪球：寒武纪 2026 一季报](https://xueqiu.com/9957756617/386778759)）。

**大厂自研：Microsoft Maia 与 Meta MTIA。** Microsoft 于 2026 年 1 月发布第二代自研推理加速器 Maia 200：基于 TSMC 3nm，原生 FP8/FP4 tensor core，216GB HBM3e（7 TB/s）、272MB 片上 SRAM、1400 亿+晶体管，单芯片 FP4 算力超 10 PFLOPS、FP8 超 5 PFLOPS，750W TDP；搭载 2.8 TB/s scale-up 带宽，可扩展至 6144 颗加速器集群，性能/美元比现有 fleet 提升 30%（[Maia 200: The AI accelerator built for inference](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)、[Maia 200: Software-defined dataflow](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/maia-200-software-defined-dataflow-and-all-ethernet-networking-for-efficient-inf/4548198)）。Meta 于 2026 年 3 月宣布两年内部署四代新 MTIA 芯片，覆盖排序推荐与 GenAI 负载（[Expanding Meta's Custom Silicon](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/)）；2026 年 4 月与 Broadcom 合作共同开发定制 AI 芯片，涉及芯片设计、先进封装与网络（[Meta Partners With Broadcom](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/)）。

**NVIDIA 机架级系统与散热。** Vera Rubin POD 整合五类机架系统、40 个机架、约 2 万颗 die、1152 颗 Rubin GPU，总算力 60 exaflops、总 scale-up 带宽 10 PB/s（[NVIDIA Vera Rubin POD](https://developer.nvidia.com/blog/?p=113993)）；其中 Vera Rubin NVL72 集成 72 颗 Rubin GPU 与 36 颗 Vera CPU，训练性能功耗比是 Blackwell 的 4 倍、推理性能功耗比达 10 倍，并引入 SM 级低延迟推理加速器 NVIDIA Groq 3 LPX（每机架 256 颗 LPU）、BlueField-4 STX 上下文存储与 Spectrum-6 SPX 网络。Vera Rubin NVL72 采用 45°C 温水液冷，并引入 Intelligent Power Smoothing（每 GPU 400 J 机架级储能），可在同一电力预算下多部署约 10% 的 NVL72 机架。Rubin GPU 单卡提供 50 PFLOPS NVFP4 推理、35 PFLOPS NVFP4 训练与 17.5 PFLOPS FP8/FP6 训练算力（[NVIDIA Vera Rubin POD](https://developer.nvidia.com/blog/?p=113993)、[NVIDIA HGX Platform](https://www.nvidia.com/en-us/data-center/hgx/)）。

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
| Google TPU 8t / 8i | 第八代拆分为训练（8t，9600 芯片 superpod、2 PB 共享 HBM）与推理（8i）双芯片 | [Our eighth generation TPUs](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/) |
| AMD Instinct MI350/MI355X | 288GB HBM3E、8 TB/s，支持 MXFP6/MXFP4 | [AMD MI350 Series](https://www.amd.com/en/products/accelerators/instinct/mi350.html) |
| AMD Helios（MI455X） | 72 颗 GPU，2.9 ExaFlops FP4、31TB HBM、260 TB/s scale-up | [ADVANCING AI 2026（PDF）](https://newsroom.amd.com/documents/2026/07/2a710b7d-c107-4639-8855-fa9366f83967.pdf) |
| AWS Trainium3 | 3nm，2.52 PFLOPS FP8/芯片，Trn3 UltraServer 144 芯片、4.4 倍算力 | [AWS whats-new](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/) |
| Intel Gaudi 3 PCIe（HL-338） | PCIe Gen5 卡形态，面向 LLM/多模态/RAG | [Intel Gaudi 3 PCIe（PDF）](https://cdrdv2-public.intel.com/817488/Gaudi%203%20PCIe%20Product%20Brief_RB_1_V6.pdf) |
| 华为昇腾 950PR / 950DT | 950PR（2026 Q1，自研 HBM）、950DT（2026 Q4） | [人民日报客户端](https://www.peopleapp.com/column/30050308165-500007097808) |
| Microsoft Maia 200 | FP4 >10 PFLOPS、216GB HBM3e@7TB/s、750W | [Microsoft Maia 200](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/) |
| Meta MTIA | 两年内部署四代，覆盖排序推荐与 GenAI；与 Broadcom 合作 | [Meta Custom Silicon](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/) |

## 关键数据与评测结果（附来源）

- **单芯片 vs 系统口径差异：** NVIDIA 官方产品页对 HGX B200 标称 FP4 Tensor Core 144 PFLOPS｜72 PFLOPS，对 GB300 NVL72 标称 1440 PFLOPS｜1080 PFLOPS（[NVIDIA HGX](https://www.nvidia.com/ja-jp/data-center/hgx/)、[NVIDIA GB300 NVL72](https://www.nvidia.com/en-in/data-center/gb300-nvl72/)）。这两组数据均为多卡聚合值且存在稀疏/稠密两列口径，与开发者博客给出的单芯片 10→15 PFLOPS 表述并不完全对应，引用时需明确口径。
- **TPU 与 GPU 推理对比：** 一项测试用 16 块 TPU v7 Ironwood 对阵 16 块 NVIDIA GB200，双方均以 vLLM 运行同一模型（Kimi K3），TPU 达到每秒约 709 个 token，GB200 为每秒约 452 个，TPU 快约 57%（[谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)）。另有分析机构称 Ironwood 在与 B200/B300 的对比中，每美元性能最高领先约 50%（[Google's TPUv7 beats Nvidia on cost per token](https://aiinsiders.net/article/googles-tpuv7-beats-nvidia-on-cost-per-token-analyst-finds)）。
- **Blackwell 推理基准：** 在 SemiAnalysis InferenceMAX v1 基准中，Blackwell B200 配合 TensorRT-LLM 的表现被评价为早期吞吐显著低于当前最优水平（[NVIDIA Blackwell Leads on SemiAnalysis InferenceMAX v1 Benchmarks](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks)）。
- **软件生态成熟度：** 有分析指出 AMD ROCm 在 2025 年下载量增长 10 倍，vLLM CI 通过率从 37% 提升到 93%（[ROCm: CUDA를 넘을 수 있는가](https://hiveworks-invest.com/stocks/amd/rocm/)）。
- **能效与成本对比：** NVIDIA 官方资料称 GB300 NVL72 相较 Hopper 平台吞吐/MW 最高 50 倍、token 成本最高低 35 倍（[NVIDIA 数据中心深度学习性能](https://resources.nvidia.com/en-us-inference-contact-us/deep-learning-perfor)）；AMD 称 Helios 每美元推理 token 数比竞争对手高最多 30%（[AAI 2026 新闻稿](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)）。
- **自研芯片关键指标：** Microsoft Maia 200 单芯片 FP4 算力超 10 PFLOPS、FP8 超 5 PFLOPS、216GB HBM3e@7TB/s、750W TDP、2.8 TB/s scale-up（[Microsoft Maia 200](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)）；AWS Trainium3 单颗 2.52 PFLOPS FP8（[AWS whats-new](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)）。
- **国产加速器业绩：** 寒武纪 2025 年营收 64.97 亿元（+453.21%）、2026 年 Q1 营收 28.85 亿元（+159.56%）（[证券时报](https://www.stcn.com/article/detail/3991331.html)、[雪球](https://xueqiu.com/9957756617/386778759)）。

## 趋势与争议

1. **算力指标口径混乱。** 稀疏与稠密、单芯片与整机架、不同精度（FP4/FP8/BF16）混用，导致跨厂商比较极易失真；NVIDIA 官方产品页与开发者博客之间也存在可比性问题。
2. **机架级系统成为竞争单位。** NVL72/NVL144 这类整机架方案把竞争从芯片扩展到供电、液冷、NVLink 交换与网络，单芯片算力优势需要系统级兑现。
3. **CUDA 锁定与替代路径。** CUDA 的开发者规模、库数量与框架集成构成护城河；AMD ROCm 通过 HIP 提供 CUDA 兼容层，TPU 则依赖 XLA/编译器路线，各方在"迁移成本"上的博弈仍在持续。
4. **自研加速器的成本压力。** Google 的 Ironwood 以编译器为中心的软硬协同路线，配合 ICI、光交换与 DCN 组网（[A developer's guide to training with Ironwood TPUs](https://cloud.google.com/blog/products/compute/training-large-models-on-ironwood-tpus)），对以 GPU 为中心的采购结构形成替代压力。
5. **功耗与散热。** 单芯片 1000W 级 TGP、整机架数百千瓦，使液冷与供电设计成为架构的一部分，而非配套工程。
6. **出口管制影响产品形态。** 有报道称在新出口限制下，NVIDIA 面向中国市场的产品会在 Blackwell 代放弃 HBM3E 而改用 GDDR7，并以 RTX Pro 6000 为基础（[Новости по тегу gddr7](https://3dnews.ru/tags/gddr7)）。
7. **出口管制重塑市场。** 2025 年 4 月美国政府要求 H20 出口中国需许可证，NVIDIA 因此在 2026 财年第一季度计提 45 亿美元费用（[NVIDIA SEC 文件（10-Q）](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)）；2025 年 12 月美方宣布允许 H20 出口，随后 BIS 于 2026 年 1 月发布规则，对 NVIDIA H200、AMD MI325X 及类似芯片的对华出口按"逐案审查"处理（[BIS 新闻稿](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)、[Federal Register](https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities)）。
8. **自研芯片对 NVIDIA 的挤压。** Google、AWS、Microsoft、Meta 均在推进自研，推理场景是自研芯片最容易切入的环节——推理对通用生态（CUDA）依赖更低，而对成本与能效更敏感；AMD 也以 Helios 机架级方案与 Anthropic 的 2GW 合作加入竞争。
9. **算力泡沫争议。** NVIDIA 与 OpenAI 达成的最高 1000 亿美元、至少 10GW 数据中心合作（首个 GW 于 2026 年下半年部署于 Vera Rubin 平台）引发对算力投资可持续性的讨论（[NVIDIA Newsroom（OpenAI 合作公告）](https://nvidianews.nvidia.com/_gallery/download_pdf/68d173273d633288cb44040b/)）。
10. **HBM 产能瓶颈。** HBM4 量产节奏（SK hynix、Micron、Samsung）直接制约高端 GPU 出货，成为行业关键瓶颈（[Micron 新闻稿](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)、[Samsung HBM4](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing)）。

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
33. [AMD Instinct™ MI350 Series GPUs](https://www.amd.com/en/products/accelerators/instinct/mi350.html)
34. [AMD Instinct™ MI355X GPUs](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html)
35. [AMD Instinct™ MI400 Series GPUs](https://www.amd.com/en/products/accelerators/instinct/mi400.html)
36. [ADVANCING AI 2026（PDF）](https://newsroom.amd.com/documents/2026/07/2a710b7d-c107-4639-8855-fa9366f83967.pdf)
37. [AAI 2026: AMD Delivers Full-Stack Compute for the Agentic AI Era](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)
38. [AMD and Anthropic Announce Strategic Partnership](https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/)
39. [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)
40. [Cloud TPU release notes](https://docs.cloud.google.com/tpu/docs/release-notes)
41. [AI infrastructure efficiency: Ironwood TPUs deliver 3.7x carbon efficiency gains](https://cloud.google.com/blog/topics/systems/ironwood-tpus-deliver-37x-carbon-efficiency-gains/)
42. [Our eighth generation TPUs: two chips for the agentic era](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
43. [Cloud Next '26: Momentum and innovation at Google scale](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)
44. [Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)
45. [Trainium3 UltraServers now available](https://www.aboutamazon.com/news/aws/trainium-3-ultraserver-faster-ai-training-lower-cost)
46. [Intel Gaudi 3 AI Accelerators now available as a PCIe Card（PDF）](https://cdrdv2-public.intel.com/817488/Gaudi%203%20PCIe%20Product%20Brief_RB_1_V6.pdf)
47. [Intel®Gaudi® 3（Habana）](https://habana.ai/products/gaudi3/)
48. [华为公布昇腾AI芯片未来3年迭代路线图（人民日报客户端）](https://www.peopleapp.com/column/30050308165-500007097808)
49. [华为汪涛：昇腾超节点部署超1000套，昇腾960芯片研发进度超预期（中国青年网）](http://t.m.youth.cn/transfer/index/url/news.youth.cn/jsxw/202609/t20260917_16874687.htm)
50. [华为更新昇腾路线图：960DT上市比原计划提前三个季度（每日经济新闻）](http://m.toutiao.com/group/7686424720039805480/)
51. [科创板首家万亿市值公司诞生 寒武纪凭什么（证券时报）](https://www.stcn.com/article/detail/3991331.html)
52. [寒武纪2026年一季报核心数据（雪球）](https://xueqiu.com/9957756617/386778759)
53. [Maia 200: The AI accelerator built for inference](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)
54. [Maia 200: Software-defined dataflow and all-Ethernet networking](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/maia-200-software-defined-dataflow-and-all-ethernet-networking-for-efficient-inf/4548198)
55. [Expanding Meta's Custom Silicon to Power Our AI Workloads](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/)
56. [Meta Partners With Broadcom to Co-Develop Custom AI Silicon](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/)
57. [NVIDIA Vera Rubin POD: Seven Chips, Five Rack-Scale Systems, One AI Supercomputer](https://developer.nvidia.com/blog/?p=113993)
58. [NVIDIA Data Center Deep Learning Product Performance](https://resources.nvidia.com/en-us-inference-contact-us/deep-learning-perfor)
59. [NVIDIA SEC 文件（10-Q，2026-01-25）](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
60. [Department of Commerce Revises License Review Policy for Semiconductors Exported to China](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)
61. [Revision to License Review Policy for Advanced Computing Commodities（Federal Register）](https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities)
62. [NVIDIA Newsroom（OpenAI 合作公告）](https://nvidianews.nvidia.com/_gallery/download_pdf/68d173273d633288cb44040b/)
63. [Micron in High-Volume Production of HBM4 Designed for NVIDIA Vera Rubin](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)
64. [Samsung Ships Industry-First Commercial HBM4](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing)