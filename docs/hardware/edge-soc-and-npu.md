# 边缘 SoC 与 NPU

> 最后更新：2026-09-26 ｜ 领域：硬件 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

边缘 SoC（System-on-Chip）指把 CPU、GPU、NPU（Neural Processing Unit，神经网络处理单元）、ISP、DSP、内存控制器与基带等功能模块集成到单一芯片、面向智能手机、AI PC、平板、可穿戴与机器人等端侧设备的平台。随着端侧大模型兴起，NPU 算力（常以 TOPS，即每秒万亿次运算标称）成为衡量边缘 SoC 的关键指标之一。目前厂商主要围绕 NPU 算力、能效与软件工具链展开竞争，并逐步向 Android、Windows、Linux 等多操作系统扩展。需要注意的是，不同厂商对 TOPS 的统计口径与系统架构差异较大，直接横比 TOPS 数值容易产生误导（[AI On-Device Chips in 2026](https://skycrumbs.com/blog/ai-on-device-chips-2026)）。

## 最新进展（2025–2026）

**Qualcomm（高通）**：2025 年 9 月发布的 Snapdragon 8 Elite Gen 5 搭载新一代 Qualcomm Hexagon NPU，官方称 NPU 性能提升 37%、每瓦性能提升 16%；CPU 为定制设计并集成硬件矩阵加速以与 Hexagon NPU 协同，整体 SoC 功耗优化约 16%，CPU 能效最高提升 35%（[Snapdragon 8 Elite Gen 5 Product Brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/images/company/news-media/media-center/press-kits/snapdragon-summit-2025-press-kit/day-2-/documents/Snapdragon8EliteGen5_ProductBrief.pdf)、[Qualcomm Newsroom](https://www.qualcomm.com/news/releases/2025/09/snapdragon-8-elite-gen-5--the-world-s-fastest-mobile-system-on-a)）。高通同时公布该平台是首个在移动处理器上运行 GPT-OSS 的产品，端侧生成速度最高可达 220 TPS（[Qualcomm Mobile AI](https://www.qualcomm.com/smartphones/features/mobile-ai)）。面向次旗舰的 Snapdragon 8 Gen 5 则搭载"重构"的 Hexagon NPU，性能提升 46%（[Qualcomm Snapdragon 8 Gen 5](https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-gen-5-mobile-platform)）。此外，高通在 2026 年 2 月开源 Hexagon-MLIR，支持将 Triton 内核与 PyTorch 模型编译到 Hexagon NPU（[Qualcomm Developer Blog](https://www.qualcomm.com/developer/blog/2026/02/build-faster-on-hexagon-npu-tritor-pytorch-with-hexagon-mlir-open-source)）。

**MediaTek（联发科）**：2025 年 9 月发布天玑 9500（Dimensity 9500），采用"超性能 + 超能效"双 NPU 设计。官方称 NPU 990 峰值性能较上一代提升 111%，率先实现 4K 高清画质文生图，支持 BitNet 1.58-bit 大模型处理、峰值功耗最多降低 56%、大模型 token 生成速度最高提升 2 倍；另一颗超能效 NPU 被其称为业界首个基于 CIM（存内计算）的 NPU，面向常开（always-on）AI 场景（[MediaTek 新闻稿（中文）](https://corp.mediatek.cn/news-events/press-releases/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices)、[MediaTek Press Release](https://www.mediatek.com/press-room/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices)、[D9500 Infographic](https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Infographics/D9500%20Infographic-%2019th%20September.pdf)）。

**Apple**：2025 年 10 月发布 M5 芯片，配备更快的 16 核神经网络引擎，并在每个 GPU 核心内引入 Neural Accelerator，官方称 AI 峰值 GPU 计算性能超过 M4 的 4 倍；统一内存带宽提升近 30% 至 153 GB/s，CPU 多线程性能较 M4 最高提升 15%（[Apple Newsroom](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/)、[Apple 新闻稿（中文）](https://www.apple.com.cn/newsroom/2025/10/apple-unleashes-m5-a-big-leap-in-ai/)）。

**Huawei（华为）**：海思麒麟系列自麒麟 970 起集成基于自研达芬奇（Da Vinci）架构的 NPU；第三方逆向工程分析指出，麒麟 9030 的 NPU 由麒麟 9020 的"一个 Lite 核 + 一个 Tiny 核"改为"一个 Lite 核 + 两个 Tiny 核"，并出现明显布局变化（[海思麒麟 - 华为开发者联盟](https://developer.huawei.com/consumer/cn/blog/topic/03207954688624001)、[SemiAnalysis：海思麒麟 9030 逆向工程分析](https://www.eet-china.com/mp/a513132.html)）。

**AI PC 与 Windows on Arm 端侧平台**：Qualcomm 的 Snapdragon X 系列（X Elite / X Plus）被用于 Windows 笔记本与部分 Android 旗舰机，其中 Snapdragon X Elite 的 NPU 约 45 TOPS，官方与第三方描述其原始吞吐高于 M3、与 M4 相当，但由于整机系统架构差异，直接比较 TOPS 具有误导性（[AI On-Device Chips in 2026](https://skycrumbs.com/blog/ai-on-device-chips-2026)）。2026 年高通发布骁龙 X2，宣称支持三大操作系统、开启"智能体 PC"时代，并将为核心驱动（Hexagon NPU、Adreno GPU）提交上游合并请求；其对 Debian 的支持预计 2026 年底前启动，Ubuntu 认证由 Canonical 推进、目标 2027 年上半年完成，华硕计划推出运行 Ubuntu 的 Zenbook（[高通骁龙 X2 发布：支持三大系统，开启智能体 PC 时代（ZAKER 科技）](http://m.toutiao.com/group/7689770879613420078/)）。

**Qualcomm Snapdragon X2 Elite（80/85 TOPS NPU）**：高通于 2025 年 9 月发布 Snapdragon X2 Elite 系列，其 Hexagon NPU 提供最高 85 TOPS（INT8）的算力，并在 Sensing Hub 上配备双 Micro NPU，内存支持 LPDDR5x（[Snapdragon X2 Elite Product Brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-X2-Elite-Product-Brief.pdf)、[Snapdragon X2 Elite](https://www.qualcomm.com/laptops/products/snapdragon-x2-elite)）；高通称其为笔记本电脑上全球最快的 NPU，支持 80 TOPS AI 处理能力，可在 Windows 11 AI+ PC 上支持并发 AI 体验，且不接电源也可使用（[高通新闻稿](https://www.qualcomm.cn/news/releases/2025/09/releases-2025-09-24-2)）。

**端侧大模型与设备级 AI 体验（Apple / Google）**：2026 年 6 月，Apple 发布由 AI 从头重构的 Siri AI，其底层为新一代 Apple Foundation Models，同时运行在设备端与采用 Private Cloud Compute 的服务器上（[Apple introduces Siri AI](https://www.apple.com/uk/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)）。2026 年 9 月，下一代 Apple Intelligence 正式推送，新能力由新一代 Apple Foundation Models 驱动、这些模型是"与 Google 及其 Gemini 模型合作定制"，可运行于设备端与 Private Cloud Compute，并随 iOS 27、iPadOS 27、macOS 27、watchOS 27、visionOS 27 覆盖 iPhone 16 及更新机型、iPhone 15 Pro、M1 及更新的 iPad/Mac、Apple Vision Pro、Apple Watch Series 9 及更新等（[The next generation of Apple Intelligence is available today](https://images.apple.com/hk/en/newsroom/2026/09/next-generation-of-apple-intelligence-available-today/)）。据行业报道，Apple 端侧模型 AFM Core 为约 30 亿参数的稠密模型，而算力更高的 AFM Core Advanced 支持表达性语音合成与口述准确率提升、需更高端硬件（如 iPhone 17 Pro、iPhone Air、iPhone 18）（[GPTS24: Apple Launches Siri AI in iOS 27](https://www.gpts24.com/en/news/apple-launches-siri-ai-in-ios-27-powered-by-gemini-refined-foundation-models)）。Google 端侧路线由 Gemini Nano 与开源 Gemma 双线构成：Gemini Nano-1 与 Nano-2 分别约 18 亿与 32.5 亿参数，在设备端（联网或离线）提供快速响应（[Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/pdf/2312.11805.pdf)、[Gemini Nano](https://deepmind.google/models/gemini/nano/)）；开发者通过基于 AICore、由 Gemini Nano 驱动的 ML Kit Gen AI APIs 集成，所有 App 共享设备上的同一个 Gemini Nano 模型以避免各自打包，Pixel 10 系列搭载第五代自研 Tensor G5 芯片（[Overview of the ML Kit Gen AI APIs](https://developers.google.com/ml-kit/genai/)、[Google Tensor: the brains behind Pixel phones](https://store.google.com/ideas/articles/google-tensor-pixel-smartphone/)）。Gemma 侧，面向端侧的 Gemma 3n 提供 E2B 与 E4B 两种规格，具备音频/文本/图像/视频多模态理解，采用嵌套结构，拥有 4B 活跃内存占用、含 2B 活跃内存子模型（[Gemma 3n](https://deepmind.google/models/gemma/gemma-3n/)）；2026 年 3 月 31 日发布 Gemma 4，提供 E2B、E4B、31B、26B A4B 四种规格，此前还发布过 Gemma 3 270M 等超小模型（[Gemma 版本](https://ai.google.dev/gemma/docs/releases)、[Gemma](https://deepmind.google/models/gemma/)）。Google 的移动端推理运行时为 LiteRT-LM，官方基准显示 Gemma-3n-E2B（约 2965MB）在 Samsung S24 Ultra 上 GPU 预填充可达 816 tk/s（[Lite RT-LM Overview](https://developers.google.com/edge/litert-lm/overview)）。

**端侧小型模型生态**：2026 年端侧可用的小模型已相当丰富。据对比评测，按 4-bit（Q4_K_M）量化后的内存占用约为：Phi-4 Mini（3.8B）约 2.7GB、Gemma 3 4B 约 2.9GB、Llama 3.2 3B 约 2.2GB、Qwen3 1.7B 约 1.1GB、SmolLM2 1.7B 约 1.1GB、Gemma 3 1B 约 720MB（[Best Mobile LLM Models in 2026](https://www.promptquorum.com/power-local-llm/mobile-llm-models-phi4-gemma-smollm)）。另一横向对比列出 Gemma 4 E2B（~2B 有效参数，PLE 架构）、Phi-4 mini（3.8B Dense）、Qwen3 14B、Qwen3 30B-A3B（30B 总参/3B 激活，MoE）（[Lightweight Local LLM Comparison 2026](https://zendevy.com/en/ai/local-llm-lightweight-comparison-2026/)）；Qwen 3.5 Small（2026 年 3 月发布，含 0.8B/2B/4B/9B）被视为 2026 年端侧综合最佳选择之一（[Best On-Device AI Models in 2026](https://andrew.ooo/answers/best-on-device-ai-models-2026/)）。Meta 的 Llama 3.2 1B/3B 专门针对端侧硬件优化，与 Arm、Qualcomm、MediaTek 合作实现首日适配（[AI Wiki: Llama 3.2](https://aiwiki.ai/wiki/llama_3_2/raw)）。

**端侧推理框架**：llama.cpp 以 GGUF 格式与高效量化著称，是本地推理的事实标准之一，广泛用于把模型压缩到移动端可运行（[Optimizing LLMs Using Quantization For Mobile Execution](https://arxiv.org/pdf/2512.06490)）；MLX 是 Apple Silicon 专属框架，在 Apple 硬件上性能领先（[On-Device AI Inference](https://cloudrps.com/blog/on-device-ai-inference-edge-models-architecture/)）；ExecuTorch 是 Meta 推出的 PyTorch 原生端侧部署框架，可从 MCU 扩展到带专用加速器的 SoC，支持量化与可插拔后端（XNNPACK、CoreML、Vulkan 等）（[ExecuTorch 论文](https://arxiv.org/pdf/2605.08195)），其 ExecuTorch MLX Delegate 让 PyTorch 模型在 Apple Silicon GPU 上带着 MLX 加速运行，支持 BF16/FP16/FP32/2/4/8-bit affine/NVFP4 量化（[PyTorch: ExecuTorch MLX Delegate](https://pytorch.org/blog/running-pytorch-models-on-apple-silicon-gpus-with-the-executorch-mlx-delegate/)）；ONNX Runtime Mobile 是跨平台、面向 NPU 的企业级方案，官方教程支持在骁龙 NPU 上运行 Phi-3.5 mini 与 Llama 3.2 3B（[ONNX Runtime: Run SLMs on Snapdragon devices with NPUs](https://onnxruntime.ai/docs/genai/tutorials/snapdragon.html)）；LiteRT-LM 为 Google 的移动优先运行时；ncnn 为腾讯优图 2017 年开源的移动端神经网络推理框架，无第三方运行时依赖，支持 CPU 与 Vulkan GPU 后端，并提供 pnnx 转换工具（[ncnn on PyPI](https://pypi.org/project/ncnn/)）。一份 2026 年运行时综述把常见选择归纳为：llama.cpp/Ollama（通用本地方案）、TensorRT Edge-LLM、ExecuTorch（移动与 MCU）、vLLM（边缘服务器多用户）、MLX（Apple Silicon）、LiteRT-LM（Android/iOS 上的 Gemma 级模型）（[The Edge LLM Runtime Stack 2026](https://edgeaistack.ai/blog/edge-llm-runtime-stack-2026/)）。

**边缘 AI 芯片厂商**：Hailo-10H 边缘 AI 加速器已量产，具备生成式 AI 能力，典型功耗仅 2.5W，通过 AEC-Q100 Grade 2 车规认证，面向 2026 年开始量产的汽车设计（[Hailo-10H GA](https://hailo.ai/company-overview/newsroom/news/hailo-announces-general-availability-of-hailo-10h-edge-ai-accelerator-with-generative-ai-capabilities/)）；Ambarella 于 2026 年 1 月 CES 发布 CV7 边缘 AI 视觉 SoC（性能提升超 2.5 倍），2026 年 9 月 15 日又发布首款独立 AI 加速器 X7，可为任意主机处理器增加物理 AI 能力（[Ambarella and ZEDEDA Partner](https://www.ambarella.com/news/ambarella-and-zededa-partner-to-bring-cloud-orchestrated-ai-to-billions-of-devices-at-the-physical-edge/)、[Ambarella Launches X7](https://www.ambarella.com.tw/news/ambarella-launches-x7-its-first-standalone-ai-accelerator-to-add-physical-ai-to-any-host-processor/)）；其他厂商还包括 Syntiant（超低功耗语音/传感器推理）、Kneron（智能家居、IP 摄像头）、NXP（Ara-240 视觉 AI）、BrainChip（Akida 神经形态）等（[Global AI Hardware Landscape 2026](https://www.geniatech.com/ai-hardware-2025/)）。

## 核心技术与关键概念

- **NPU 与 AI Engine**：NPU 负责加速计算摄影、实时翻译、AI 助手、图像与视频编辑等任务，性能常以 TOPS 标称（[Processor architecture: Snapdragon vs the competition in 2026](https://en.androidsis.com/Snapdragon-processor-architecture-vs.-the-competition-in-2026/)）。
- **混合精度与传感中枢**：新一代 NPU 支持整数与浮点混合精度，并与低功耗传感中枢（如 Qualcomm Sensing Hub）配合，实现常开低功耗 AI（[Les SoC les plus rapides pour smartphones haut de gamme en 2026](https://fr.todoandroid.es/Les-SoC-les-plus-rapides-pour-smartphones-haut-de-gamme-en-2026/)）。
- **低比特端侧大模型**：MediaTek 的 BitNet 1.58-bit 方案通过极低比特量化降低端侧大模型的功耗与内存占用（见上）。
- **硬件矩阵加速**：Snapdragon 8 Elite Gen 5 的 CPU 内置硬件矩阵加速，与 Hexagon NPU 协同加速生成式 AI 工作负载（[Snapdragon 8 Elite Gen 5 Product Brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/images/company/news-media/media-center/press-kits/snapdragon-summit-2025-press-kit/day-2-/documents/Snapdragon8EliteGen5_ProductBrief.pdf)）。
- **统一内存与带宽**：Apple M5 将统一内存带宽提升至 153 GB/s（较 M4 提升近 30%），为端侧大模型提供更高内存吞吐（[Apple Newsroom](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/)）。
- **端侧大模型与 NPU 算力**：主流旗舰 NPU 算力已进入 40–85 TOPS 区间（如骁龙 X2 Elite 的 80/85 TOPS、天玑 9500 的 NPU 990），足以流畅运行 3B–9B 级模型。
- **量化与内存占用**：4-bit 量化是端侧主流，可大幅压缩模型体积——一项针对 Llama 3.2 3B 的研究显示，使用 4-bit PTQ 并转为 GGUF 格式后模型体积减少 68.66%（[Optimizing LLMs Using Quantization For Mobile Execution](https://arxiv.org/pdf/2512.06490)）；常见方案包括 4/6/8-bit、affine 量化与 NVFP4。
- **内存瓶颈**：端侧 LLM 的主要约束是内存容量与带宽——模型权重（尤其是堆叠的 Transformer 层）占据大部分内存预算；例如 Qwen3-Reranker-0.6B 中 28 层 Transformer 占总权重内存的 70% 以上（[On-device Semantic Selection（arXiv）](https://arxiv.org/html/2510.15620v2)）。
- **端侧 RAG**：通过本地嵌入模型 + 向量检索让小模型获得私有知识。移动端分块策略需比服务器更保守（建议单块不超过 256 token），因为要在 6–8GB 共享内存中与系统、App 争抢空间（[On-Device RAG for Android](https://mvpfactory.io/blog/on-device-rag-for-android-running-embedding-models-vector-search-in-sqlite-and)）；在 NPU 上静态图会限制最大上下文长度，需要比 CPU/GPU 更小的分块（如索引时 1000 字符 vs 2500 字符）（[Energy-Efficient On-Device RAG on a Mobile NPU](https://arxiv.org/html/2606.11257v1)）。
- **隐私优势**：端侧推理使数据不出设备、离线可用，符合 GDPR/CCPA 等合规要求；Apple 的 Private Cloud Compute 则试图在必须上云时也保持隐私承诺（[Apple introduces Siri AI](https://www.apple.com/uk/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)）。
- **混合推理（模型路由）**：日常辅助任务用小模型、复杂推理用云端大模型，可显著降低 token 成本；行业观点认为这种"按任务选模型"的策略可让企业 AI token 消耗降低 80% 以上（[中国电子报：AMD大中华区市场营销副总裁纪朝晖访谈](http://m.toutiao.com/group/7689737596750152192/)）。
- **软件工具链**：高通提供 Qualcomm AI Engine Direct SDK（可直连 Hexagon NPU）、Hexagon SDK 以及 QNN/SNPE 部署链路，可将 TensorFlow Lite 或 ONNX runtime 的工作负载委派给 Hexagon NPU（[Qualcomm AI Engine Direct SDK](https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk)、[NPU Utilization for Edge AI](https://soict.hust.edu.vn/wp-content/uploads/Qualcomm_NPU_EN.pdf)）。

## 代表性产品（附官方链接）

| 平台 | 厂商 | AI 引擎（官方口径） | 官方链接 |
| --- | --- | --- | --- |
| Snapdragon 8 Elite Gen 5 | Qualcomm | Hexagon NPU 性能 +37% | [链接](https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-elite-gen-5) |
| Snapdragon 8 Gen 5 | Qualcomm | Hexagon NPU 性能 +46% | [链接](https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-gen-5-mobile-platform) |
| Dimensity 9500 | MediaTek | NPU 990 双 NPU | [链接](https://www.mediatek.com/press-room/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices) |
| M5 | Apple | 16 核 Neural Engine + Neural Accelerator | [链接](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/) |

## 关键数据与评测结果

端侧 NPU 算力存在多种统计口径。高通方面称 Snapdragon 8 Elite Gen 5 的 CPU 为"20% 增强"的定制设计，并与 Hexagon NPU 协同实现 agentic AI（[Snapdragon 8 Elite Gen 5 Product Brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/images/company/news-media/media-center/press-kits/snapdragon-summit-2025-press-kit/day-2-/documents/Snapdragon8EliteGen5_ProductBrief.pdf)）。第三方汇总给出的代表性数字包括：Snapdragon X Elite NPU 约 45 TOPS；MediaTek Dimensity 9400 约 26 TOPS（APU 790）；Samsung Exynos 2400 约 32 TOPS；Intel Core Ultra Series 2 约 34 TOPS（[Best On-Device AI 2026](https://perspectiveai.xyz/best-on-device-ai-2026/)）。另一第三方汇总给出 Apple M5 的 16 核 Neural Engine 约 38 NPU TOPS、GPU 约 80 TOPS，Dimensity 9400+ 的 NPU 890 约 50 TOPS（[Edge Intelligence: AI Tablets 2026](https://www.theaitechpulse.com/best-ai-tablets-2026)）。一份 2026.Q2 的第三方 NPU 榜单显示，MediaTek Kompanio Ultra 910（NPU 890，TSMC N3E）标称约 50 TOPS、20W TDP（[Global NPU Leaderboard · 2026.Q2](https://aipc.computer/leaderboard)）。另有第三方报道称天玑 9500 的 NPU 990 算力"接近 100 TOPS"（[Los procesadores de móvil más potentes del mercado en 2026](https://noticias.compudemano.com/discusion/los-procesadores-de-movil-mas-potentes-del-mercado-en-2026.421596/)），并称其 30 亿参数 LLM 输出速度提升 100%（[Temui MediaTek Dimensity 9500](https://www.mediatek.com/id/tek-talk-blogs/meet-the-mediatek-dimensity-9500)）。上述数字来自不同评测与统计口径，不应直接横比。

**端侧 AI 关键数据（补充）**：骁龙 X2 Elite 的 Hexagon NPU 最高 85 TOPS（INT8）（[Qualcomm 产品简介](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-X2-Elite-Product-Brief.pdf)）；Gemma 3n-E2B 体积约 2965MB、在 S24 Ultra 上 GPU 预填充 816 tk/s（[LiteRT-LM Overview](https://developers.google.com/edge/litert-lm/overview)）；Phi-4 Mini（3.8B）在 Q4_K_M 量化下约 2.7GB 内存、手机端约 13–18 tk/s（[Best Mobile LLM Models 2026](https://www.promptquorum.com/power-local-llm/mobile-llm-models-phi4-gemma-smollm)）；Hailo-10H 典型功耗 2.5W、通过 AEC-Q100 Grade 2 车规（[Hailo-10H GA](https://hailo.ai/company-overview/newsroom/news/hailo-announces-general-availability-of-hailo-10h-edge-ai-accelerator-with-generative-ai-capabilities/)）；混合推理可将企业 AI token 消耗降低 80% 以上（[中国电子报](http://m.toutiao.com/group/7689737596750152192/)）。

## 趋势与争议

1. **TOPS 可比性争议**：因各厂商在稀疏化、量化与系统级协同上的口径不同，单看 TOPS 并不能反映真实端侧体验（[AI On-Device Chips in 2026](https://skycrumbs.com/blog/ai-on-device-chips-2026)）。
2. **低比特化**：BitNet 1.58-bit 等极低比特大模型正被 SoC 直接支持，可显著降低端侧内存占用与推理功耗，成为端侧大模型落地的重要路径（见 MediaTek 资料）。Apple 方面则称 M5 的 AI 峰值 GPU 计算性能超过 M4 的 4 倍（[Apple Newsroom](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/)）。
3. **端云协同**：agentic AI 常在端侧完成隐私敏感与低时延的前置处理、在云端完成重负载推理；Sensing Hub、Personal Knowledge Graph、Personal Scribe 等端侧能力被用于构建个性化上下文（[Qualcomm Mobile AI](https://www.qualcomm.com/smartphones/features/mobile-ai)）。
4. **跨平台与开放生态**：高通将 Hexagon NPU、Adreno GPU 等核心驱动向 Linux 上游合并，反映端侧 AI 平台正从单一操作系统向 Windows/Linux/Android 多系统扩展（[高通骁龙 X2 发布（ZAKER 科技）](http://m.toutiao.com/group/7689770879613420078/)）。
5. **算力口径与评测**：不同第三方对同一芯片的 TOPS 与跑分差异较大，端侧 AI 的真实体验更依赖系统级协同、内存带宽与软件栈优化（[AI On-Device Chips in 2026](https://skycrumbs.com/blog/ai-on-device-chips-2026)）。
6. **软件生态竞争**：高通开源 Hexagon-MLIR 并提供 QNN/SNPE，MediaTek 与 Apple 各自构建工具链，端侧 AI 的落地越来越依赖开发者工具与模型生态；同一硬件能否高效跑通主流模型，往往比峰值算力更关键（[Qualcomm Developer Blog](https://www.qualcomm.com/developer/blog/2026/02/build-faster-on-hexagon-npu-tritor-pytorch-with-hexagon-mlir-open-source)）。
7. **隐私 vs 能力**：端侧模型参数小、上下文有限（Gemini Nano 等场景上下文常被限制在几千 token），难以胜任复杂推理；Apple 与 Google 均以"端侧 + 私有云"的混合架构折中，如何在隐私承诺与模型能力间平衡仍是核心议题。
8. **内存是真正的天花板**：与数据中心受限于算力不同，端侧主要受限于内存容量与带宽，模型权重占用、量化精度损失、KV cache 增长共同构成瓶颈；NPU 的静态图特性还限制了上下文灵活性。
9. **模型碎片化与工具链**：端侧要面对 Arm/x86、Apple/Android/Windows、不同 NPU 后端（Hexagon、CoreML、XNNPACK、Vulkan、QNN）的碎片化，推理框架（ExecuTorch、ONNX Runtime、LiteRT）之间的兼容性成为工程痛点。
10. **"端侧 AI 是否被过度营销"**：厂商强调 TOPS 数字，但实际体验更取决于内存带宽、软件栈与应用生态；TOPS 与真实 token 吞吐并不线性相关。
11. **成本与能耗经济学**：把日常任务放在端侧、只在复杂推理时调用云端，是企业降低 AI 成本的重要路径，也推动了 AI PC 与"智能体主机"的产品形态。

## 参考来源

- [AI On-Device Chips in 2026: Snapdragon vs Apple Silicon](https://skycrumbs.com/blog/ai-on-device-chips-2026)
- [Best On-Device AI 2026](https://perspectiveai.xyz/best-on-device-ai-2026/)
- [Global NPU Leaderboard · 2026.Q2](https://aipc.computer/leaderboard)
- [Edge Intelligence: A Comparative Analysis of 2026 AI Tablets](https://www.theaitechpulse.com/best-ai-tablets-2026)
- [Processor architecture: Snapdragon vs the competition in 2026](https://en.androidsis.com/Snapdragon-processor-architecture-vs.-the-competition-in-2026/)
- [Les SoC les plus rapides pour smartphones haut de gamme en 2026](https://fr.todoandroid.es/Les-SoC-les-plus-rapides-pour-smartphones-haut-de-gamme-en-2026/)
- [The Snapdragon 8 Elite Gen 5 Mobile Platform — Product Brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/images/company/news-media/media-center/press-kits/snapdragon-summit-2025-press-kit/day-2-/documents/Snapdragon8EliteGen5_ProductBrief.pdf)
- [Snapdragon 8 Elite Gen 5, the World's Fastest Mobile System-on-a-chip](https://www.qualcomm.com/news/releases/2025/09/snapdragon-8-elite-gen-5--the-world-s-fastest-mobile-system-on-a)
- [Qualcomm Snapdragon 8 Elite Gen 5 Mobile Platform](https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-elite-gen-5)
- [Qualcomm Snapdragon 8 Gen 5 Mobile Platform](https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-gen-5-mobile-platform)
- [Qualcomm Mobile AI](https://www.qualcomm.com/smartphones/features/mobile-ai)
- [Qualcomm AI Engine Direct SDK](https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk)
- [Compile Triton & PyTorch for Hexagon NPU with Open Source Hexagon-MLIR](https://www.qualcomm.com/developer/blog/2026/02/build-faster-on-hexagon-npu-tritor-pytorch-with-hexagon-mlir-open-source)
- [NPU Utilization for Edge AI (Qualcomm)](https://soict.hust.edu.vn/wp-content/uploads/Qualcomm_NPU_EN.pdf)
- [MediaTek 发布天玑 9500（中文新闻稿）](https://corp.mediatek.cn/news-events/press-releases/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices)
- [MediaTek Dimensity 9500 Press Release](https://www.mediatek.com/press-room/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices)
- [MediaTek Dimensity 9500 Infographic](https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Infographics/D9500%20Infographic-%2019th%20September.pdf)
- [Apple unleashes M5, the next big leap in AI performance for Apple silicon](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/)
- [Apple 发布 M5 芯片，实现 AI 性能新跃升](https://www.apple.com.cn/newsroom/2025/10/apple-unleashes-m5-a-big-leap-in-ai/)
- [海思麒麟 - 华为开发者联盟](https://developer.huawei.com/consumer/cn/blog/topic/03207954688624001)
- [SemiAnalysis：海思麒麟 9030 及 N+3 工艺深度逆向工程分析](https://www.eet-china.com/mp/a513132.html)
- [高通骁龙 X2 发布：支持三大系统，开启智能体 PC 时代（ZAKER 科技）](http://m.toutiao.com/group/7689770879613420078/)
- [Los procesadores de móvil más potentes del mercado en 2026](https://noticias.compudemano.com/discusion/los-procesadores-de-movil-mas-potentes-del-mercado-en-2026.421596/)
- [Temui MediaTek Dimensity 9500](https://www.mediatek.com/id/tek-talk-blogs/meet-the-mediatek-dimensity-9500)
- [Apple introduces Siri AI, a profoundly more capable and personal assistant](https://www.apple.com/uk/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)
- [The next generation of Apple Intelligence is available today（Apple HK）](https://images.apple.com/hk/en/newsroom/2026/09/next-generation-of-apple-intelligence-available-today/)
- [Apple accelerates app development with new intelligence frameworks and advanced tools](https://images.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/)
- [GPTS24: Apple Launches Siri AI in iOS 27 Powered by Gemini-Refined Foundation Models](https://www.gpts24.com/en/news/apple-launches-siri-ai-in-ios-27-powered-by-gemini-refined-foundation-models)
- [Gemma 3n（Google DeepMind）](https://deepmind.google/models/gemma/gemma-3n/)
- [Gemma 版本（Google AI for Developers）](https://ai.google.dev/gemma/docs/releases)
- [Gemma（Google DeepMind）](https://deepmind.google/models/gemma/)
- [Lite RT-LM Overview](https://developers.google.com/edge/litert-lm/overview)
- [Overview of the ML Kit Gen AI APIs](https://developers.google.com/ml-kit/genai/)
- [Gemini Nano（Google DeepMind）](https://deepmind.google/models/gemini/nano/)
- [Gemini: A Family of Highly Capable Multimodal Models（arXiv）](https://arxiv.org/pdf/2312.11805.pdf)
- [Google Tensor: the brains behind Pixel phones](https://store.google.com/ideas/articles/google-tensor-pixel-smartphone/)
- [Snapdragon X2 Elite Product Brief（PDF）](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-X2-Elite-Product-Brief.pdf)
- [Qualcomm Snapdragon X2 Elite](https://www.qualcomm.com/laptops/products/snapdragon-x2-elite)
- [高通：全新骁龙X2 Elite Extreme和骁龙X2 Elite](https://www.qualcomm.cn/news/releases/2025/09/releases-2025-09-24-2)
- [Best Mobile LLM Models in 2026: Phi-4 Mini vs Gemma 3 vs SmolLM](https://www.promptquorum.com/power-local-llm/mobile-llm-models-phi4-gemma-smollm)
- [Lightweight Local LLM Comparison 2026](https://zendevy.com/en/ai/local-llm-lightweight-comparison-2026/)
- [Best On-Device AI Models in 2026](https://andrew.ooo/answers/best-on-device-ai-models-2026/)
- [EXECUTORCH — A Unified PyTorch Solution to Run AI Models On-Device（arXiv）](https://arxiv.org/pdf/2605.08195)
- [Running PyTorch Models on Apple Silicon GPUs with the ExecuTorch MLX Delegate](https://pytorch.org/blog/running-pytorch-models-on-apple-silicon-gpus-with-the-executorch-mlx-delegate/)
- [The Edge LLM Runtime Stack 2026](https://edgeaistack.ai/blog/edge-llm-runtime-stack-2026/)
- [On-Device AI Inference: Running LLMs Locally with llama.cpp, MLX, and ExecuTorch](https://cloudrps.com/blog/on-device-ai-inference-edge-models-architecture/)
- [ONNX Runtime: Run SLMs on Snapdragon devices with NPUs](https://onnxruntime.ai/docs/genai/tutorials/snapdragon.html)
- [ncnn（PyPI）](https://pypi.org/project/ncnn/)
- [Hailo Announces General Availability of Hailo-10H Edge AI Accelerator](https://hailo.ai/company-overview/newsroom/news/hailo-announces-general-availability-of-hailo-10h-edge-ai-accelerator-with-generative-ai-capabilities/)
- [Ambarella Launches X7, Its First Standalone AI Accelerator](https://www.ambarella.com.tw/news/ambarella-launches-x7-its-first-standalone-ai-accelerator-to-add-physical-ai-to-any-host-processor/)
- [Ambarella and ZEDEDA Partner to Bring Cloud-Orchestrated AI to the Physical Edge](https://www.ambarella.com/news/ambarella-and-zededa-partner-to-bring-cloud-orchestrated-ai-to-billions-of-devices-at-the-physical-edge/)
- [Global AI Hardware Landscape 2026](https://www.geniatech.com/ai-hardware-2025/)
- [Energy-Efficient On-Device RAG on a Mobile NPU（arXiv）](https://arxiv.org/html/2606.11257v1)
- [On-Device RAG for Android: Embedding Models, Vector Search in SQLite](https://mvpfactory.io/blog/on-device-rag-for-android-running-embedding-models-vector-search-in-sqlite-and)
- [On-device Semantic Selection Made Low Latency and Memory Efficient（arXiv）](https://arxiv.org/html/2510.15620v2)
- [Optimizing LLMs Using Quantization For Mobile Execution（arXiv）](https://arxiv.org/pdf/2512.06490)
- [AI Wiki: Llama 3.2](https://aiwiki.ai/wiki/llama_3_2/raw)
- [中国电子报：AMD大中华区市场营销副总裁纪朝晖访谈](http://m.toutiao.com/group/7689737596750152192/)