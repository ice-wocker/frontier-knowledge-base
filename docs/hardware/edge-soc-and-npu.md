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

## 核心技术与关键概念

- **NPU 与 AI Engine**：NPU 负责加速计算摄影、实时翻译、AI 助手、图像与视频编辑等任务，性能常以 TOPS 标称（[Processor architecture: Snapdragon vs the competition in 2026](https://en.androidsis.com/Snapdragon-processor-architecture-vs.-the-competition-in-2026/)）。
- **混合精度与传感中枢**：新一代 NPU 支持整数与浮点混合精度，并与低功耗传感中枢（如 Qualcomm Sensing Hub）配合，实现常开低功耗 AI（[Les SoC les plus rapides pour smartphones haut de gamme en 2026](https://fr.todoandroid.es/Les-SoC-les-plus-rapides-pour-smartphones-haut-de-gamme-en-2026/)）。
- **低比特端侧大模型**：MediaTek 的 BitNet 1.58-bit 方案通过极低比特量化降低端侧大模型的功耗与内存占用（见上）。
- **硬件矩阵加速**：Snapdragon 8 Elite Gen 5 的 CPU 内置硬件矩阵加速，与 Hexagon NPU 协同加速生成式 AI 工作负载（[Snapdragon 8 Elite Gen 5 Product Brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/images/company/news-media/media-center/press-kits/snapdragon-summit-2025-press-kit/day-2-/documents/Snapdragon8EliteGen5_ProductBrief.pdf)）。
- **统一内存与带宽**：Apple M5 将统一内存带宽提升至 153 GB/s（较 M4 提升近 30%），为端侧大模型提供更高内存吞吐（[Apple Newsroom](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/)）。
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

## 趋势与争议

1. **TOPS 可比性争议**：因各厂商在稀疏化、量化与系统级协同上的口径不同，单看 TOPS 并不能反映真实端侧体验（[AI On-Device Chips in 2026](https://skycrumbs.com/blog/ai-on-device-chips-2026)）。
2. **低比特化**：BitNet 1.58-bit 等极低比特大模型正被 SoC 直接支持，可显著降低端侧内存占用与推理功耗，成为端侧大模型落地的重要路径（见 MediaTek 资料）。Apple 方面则称 M5 的 AI 峰值 GPU 计算性能超过 M4 的 4 倍（[Apple Newsroom](https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/)）。
3. **端云协同**：agentic AI 常在端侧完成隐私敏感与低时延的前置处理、在云端完成重负载推理；Sensing Hub、Personal Knowledge Graph、Personal Scribe 等端侧能力被用于构建个性化上下文（[Qualcomm Mobile AI](https://www.qualcomm.com/smartphones/features/mobile-ai)）。
4. **跨平台与开放生态**：高通将 Hexagon NPU、Adreno GPU 等核心驱动向 Linux 上游合并，反映端侧 AI 平台正从单一操作系统向 Windows/Linux/Android 多系统扩展（[高通骁龙 X2 发布（ZAKER 科技）](http://m.toutiao.com/group/7689770879613420078/)）。
5. **算力口径与评测**：不同第三方对同一芯片的 TOPS 与跑分差异较大，端侧 AI 的真实体验更依赖系统级协同、内存带宽与软件栈优化（[AI On-Device Chips in 2026](https://skycrumbs.com/blog/ai-on-device-chips-2026)）。
6. **软件生态竞争**：高通开源 Hexagon-MLIR 并提供 QNN/SNPE，MediaTek 与 Apple 各自构建工具链，端侧 AI 的落地越来越依赖开发者工具与模型生态；同一硬件能否高效跑通主流模型，往往比峰值算力更关键（[Qualcomm Developer Blog](https://www.qualcomm.com/developer/blog/2026/02/build-faster-on-hexagon-npu-tritor-pytorch-with-hexagon-mlir-open-source)）。

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