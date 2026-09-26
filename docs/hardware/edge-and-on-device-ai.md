# 端侧 AI

> 最后更新：2026-09-26 ｜ 领域：端侧 AI ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

端侧 AI（On-Device AI）指在手机、PC、可穿戴、车载等终端本地完成模型推理，而非依赖云端。2025–2026 年，随着小参数模型（1B–9B 级）质量跃升、NPU 算力进入 40–85 TOPS 区间、以及量化与推理框架成熟，端侧大模型从"演示"走向"系统级集成"：Apple Intelligence 与 Siri AI、Google Gemini Nano/Gemma、高通骁龙与联发科天玑的 NPU 均把"本地大模型"作为核心卖点。端侧 AI 的核心价值是**低延迟、离线可用、隐私不出设备、以及降低云端 token 成本**，主要约束则是**内存带宽与容量**。

## 2025–2026 最新进展

### Apple：Apple Intelligence 与 Siri AI
2026 年 6 月，Apple 发布由 AI 从头重构的 **Siri AI**，其底层为新一代 **Apple Foundation Models**，同时运行在设备端与采用 Private Cloud Compute 的服务器上（[Apple introduces Siri AI](https://www.apple.com/uk/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)）。2026 年 9 月，下一代 Apple Intelligence 正式推送：新能力由新一代 Apple Foundation Models 驱动，且这些模型是"与 Google 及其 Gemini 模型合作定制"，用于深度集成的 Apple Intelligence 体验，并可运行于设备端与 Private Cloud Compute（[The next generation of Apple Intelligence is available today](https://images.apple.com/hk/en/newsroom/2026/09/next-generation-of-apple-intelligence-available-today/)）。该系统随 iOS 27、iPadOS 27、macOS 27、watchOS 27、visionOS 27 提供，覆盖 iPhone 16 及更新机型、iPhone 15 Pro、M1 及更新的 iPad/Mac、Apple Vision Pro、Apple Watch Series 9 及更新等。据行业报道，Apple 的端侧模型 AFM Core 为约 30 亿参数的稠密模型，而算力更高的 AFM Core Advanced 支持表达性语音合成与口述准确率提升，需更高端硬件（如 iPhone 17 Pro、iPhone Air、iPhone 18）（[GPTS24: Apple Launches Siri AI in iOS 27](https://www.gpts24.com/en/news/apple-launches-siri-ai-in-ios-27-powered-by-gemini-refined-foundation-models)）。

### Google：Gemini Nano 与 Gemma
Google 的端侧路线由 **Gemini Nano** 与开源 **Gemma** 双线构成。Gemini Nano 是 Google 最面向设备的模型，Nano-1 与 Nano-2 分别约 18 亿与 32.5 亿参数，在设备端（联网或离线）提供快速响应（[Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/pdf/2312.11805.pdf)、[Gemini Nano](https://deepmind.google/models/gemini/nano/)）。开发者通过 ML Kit Gen AI APIs 集成，这些 API 基于 AICore、由 Gemini Nano 驱动，所有 App 共享设备上的同一个 Gemini Nano 模型，避免各自打包（[Overview of the ML Kit Gen AI APIs](https://developers.google.com/ml-kit/genai/)）。Pixel 10 系列搭载第五代自研 Tensor G5 芯片（[Google Tensor: the brains behind Pixel phones](https://store.google.com/ideas/articles/google-tensor-pixel-smartphone/)）。

Gemma 侧，面向端侧的 **Gemma 3n** 提供 E2B 与 E4B 两种规格，具备多模态理解（音频/文本/图像/视频），采用嵌套结构，拥有 4B 活跃内存占用、含 2B 活跃内存子模型（[Gemma 3n](https://deepmind.google/models/gemma/gemma-3n/)）。2026 年 3 月 31 日，Google 发布 **Gemma 4**，提供 E2B、E4B、31B、26B A4B 四种规格；此前还发布了 Gemma 3 270M 等超小模型（[Gemma 版本](https://ai.google.dev/gemma/docs/releases)、[Gemma](https://deepmind.google/models/gemma/)）。Google 的移动端推理运行时为 **LiteRT-LM**，官方基准显示 Gemma-3n-E2B（约 2965MB）在 Samsung S24 Ultra 上 GPU 预填充可达 816 tk/s（[Lite RT-LM Overview](https://developers.google.com/edge/litert-lm/overview)）。

### 高通骁龙：X2 Elite 的 80/85 TOPS NPU
高通于 2025 年 9 月发布 **Snapdragon X2 Elite** 系列。其 Hexagon NPU 提供最高 **85 TOPS（INT8）** 的算力，并在 Sensing Hub 上配备双 Micro NPU；内存支持 LPDDR5x（[Snapdragon X2 Elite Product Brief](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-X2-Elite-Product-Brief.pdf)、[Snapdragon X2 Elite](https://www.qualcomm.com/laptops/products/snapdragon-x2-elite)）。高通称其为笔记本电脑上全球最快的 NPU，支持 80 TOPS AI 处理能力，可在 Windows 11 AI+ PC 上支持并发 AI 体验，且不接电源也可使用（[高通新闻稿](https://www.qualcomm.cn/news/releases/2025/09/releases-2025-09-24-2)）。

### 联发科天玑：NPU 990
联发科 **Dimensity 9500** 集成超性能 AI 处理器 **NPU 990**，性能相较上一代翻倍，配备第二代生成式 AI 引擎 2.0，峰值性能下功耗降低 56%，token 生成速度提升 2 倍以上；并新增业界首个基于 CIM（存内计算）的"Super Efficient NPU"用于常开 AI 应用（[MediaTek Dimensity 9500](https://www.mediatek.com/products/smartphones/mediatek-dimensity-9500)、[D9500 Infographic](https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Infographics/D9500%20Infographic-%2019th%20September.pdf)）。

### 小型模型生态
2026 年端侧可用的小模型已相当丰富。据对比评测，按 4-bit（Q4_K_M）量化后的内存占用约为：Phi-4 Mini（3.8B）约 2.7GB、Gemma 3 4B 约 2.9GB、Llama 3.2 3B 约 2.2GB、Qwen3 1.7B 约 1.1GB、SmolLM2 1.7B 约 1.1GB、Gemma 3 1B 约 720MB（[Best Mobile LLM Models in 2026](https://www.promptquorum.com/power-local-llm/mobile-llm-models-phi4-gemma-smollm)）。另一横向对比列出 Gemma 4 E2B（~2B 有效参数，PLE 架构）、Phi-4 mini（3.8B Dense）、Qwen3 14B、Qwen3 30B-A3B（30B 总参/3B 激活，MoE）（[Lightweight Local LLM Comparison 2026](https://zendevy.com/en/ai/local-llm-lightweight-comparison-2026/)）。此外 Qwen 3.5 Small（2026 年 3 月发布，含 0.8B/2B/4B/9B）被视为 2026 年端侧综合最佳选择之一（[Best On-Device AI Models in 2026](https://andrew.ooo/answers/best-on-device-ai-models-2026/)）。Meta 的 Llama 3.2 1B/3B 专门针对端侧硬件优化，与 Arm、Qualcomm、MediaTek 合作实现首日适配（[AI Wiki: Llama 3.2](https://aiwiki.ai/wiki/llama_3_2/raw)）。

### 端侧推理框架
- **llama.cpp**：以 GGUF 格式与高效量化著称，是本地推理的事实标准之一，广泛用于把模型压缩到移动端可运行（[Optimizing LLMs Using Quantization For Mobile Execution](https://arxiv.org/pdf/2512.06490)）。
- **MLX**：Apple Silicon 专属框架，在 Apple 硬件上性能领先（[On-Device AI Inference](https://cloudrps.com/blog/on-device-ai-inference-edge-models-architecture/)）。
- **ExecuTorch**：Meta 推出的 PyTorch 原生端侧部署框架，可从 MCU 扩展到带专用加速器的 SoC，支持量化与可插拔后端（XNNPACK、CoreML、Vulkan 等）（[ExecuTorch 论文](https://arxiv.org/pdf/2605.08195)）。PyTorch 还推出 ExecuTorch MLX Delegate，让 PyTorch 模型在 Apple Silicon GPU 上带着 MLX 加速运行，支持 BF16/FP16/FP32/2/4/8-bit affine/NVFP4 量化（[PyTorch: Running PyTorch Models on Apple Silicon GPUs with the ExecuTorch MLX Delegate](https://pytorch.org/blog/running-pytorch-models-on-apple-silicon-gpus-with-the-executorch-mlx-delegate/)）。
- **ONNX Runtime Mobile**：跨平台、面向 NPU 的企业级方案，官方教程支持在骁龙 NPU 上运行 Phi-3.5 mini 与 Llama 3.2 3B（[ONNX Runtime: Run SLMs on Snapdragon devices with NPUs](https://onnxruntime.ai/docs/genai/tutorials/snapdragon.html)）。
- **LiteRT-LM**：Google 的移动优先运行时（[Lite RT-LM Overview](https://developers.google.com/edge/litert-lm/overview)）。
- **ncnn**：腾讯优图 2017 年开源的移动端神经网络推理框架，无第三方运行时依赖，支持 CPU 与 Vulkan GPU 后端，并提供 pnnx 转换工具（[ncnn on PyPI](https://pypi.org/project/ncnn/)）。

一份 2026 年的运行时综述把常见选择归纳为：llama.cpp/Ollama（通用本地方案）、TensorRT Edge-LLM、ExecuTorch（移动与 MCU）、vLLM（边缘服务器多用户）、MLX（Apple Silicon）、LiteRT-LM（Android/iOS 上的 Gemma 级模型）（[The Edge LLM Runtime Stack 2026](https://edgeaistack.ai/blog/edge-llm-runtime-stack-2026/)）。

### 边缘 AI 芯片厂商
- **Hailo**：Hailo-10H 边缘 AI 加速器已量产，具备生成式 AI 能力，典型功耗仅 2.5W，通过 AEC-Q100 Grade 2 车规认证，面向 2026 年开始量产的汽车设计（[Hailo-10H GA](https://hailo.ai/company-overview/newsroom/news/hailo-announces-general-availability-of-hailo-10h-edge-ai-accelerator-with-generative-ai-capabilities/)）。
- **Ambarella**：2026 年 1 月 CES 发布 CV7 边缘 AI 视觉 SoC，性能提升超 2.5 倍；2026 年 9 月 15 日又发布首款独立 AI 加速器 X7，可为任意主机处理器增加物理 AI 能力（[Ambarella 与 ZEDEDA 合作](https://www.ambarella.com/news/ambarella-and-zededa-partner-to-bring-cloud-orchestrated-ai-to-billions-of-devices-at-the-physical-edge/)、[Ambarella Launches X7](https://www.ambarella.com.tw/news/ambarella-launches-x7-its-first-standalone-ai-accelerator-to-add-physical-ai-to-any-host-processor/)）。
- 其他厂商还包括 Syntiant（超低功耗语音/传感器推理）、Kneron（智能家居、IP 摄像头）、NXP（Ara-240 视觉 AI）、BrainChip（Akida 神经形态）等（[Global AI Hardware Landscape 2026](https://www.geniatech.com/ai-hardware-2025/)）。

## 核心技术与关键概念

- **端侧大模型与 NPU 算力**：主流旗舰 NPU 算力已进入 40–85 TOPS 区间（如骁龙 X2 Elite 的 80/85 TOPS、天玑 9500 的 NPU 990），足以流畅运行 3B–9B 级模型。
- **量化**：4-bit 量化是端侧主流，可大幅压缩模型体积。一项针对 Llama 3.2 3B 的研究显示，使用 4-bit PTQ 并转为 GGUF 格式后模型体积减少 68.66%（[Optimizing LLMs Using Quantization For Mobile Execution](https://arxiv.org/pdf/2512.06490)）。常见方案包括 4/6/8-bit、affine 量化与 NVFP4。
- **内存瓶颈**：端侧 LLM 的主要约束是内存容量与带宽——模型权重（尤其是堆叠的 Transformer 层）占据大部分内存预算；例如 Qwen3-Reranker-0.6B 中 28 层 Transformer 占总权重内存的 70% 以上（[On-device Semantic Selection（arXiv）](https://arxiv.org/html/2510.15620v2)）。
- **端侧 RAG**：通过本地嵌入模型 + 向量检索让小模型获得私有知识。移动端的分块策略需比服务器更保守（建议单块不超过 256 token），因为要在 6–8GB 共享内存中与系统、App 争抢空间（[On-Device RAG for Android](https://mvpfactory.io/blog/on-device-rag-for-android-running-embedding-models-vector-search-in-sqlite-and)）。在 NPU 上，静态图会限制最大上下文长度，需要比 CPU/GPU 更小的分块（如索引时 1000 字符 vs 2500 字符）（[Energy-Efficient On-Device RAG on a Mobile NPU](https://arxiv.org/html/2606.11257v1)）。
- **隐私优势**：端侧推理使数据不出设备，离线可用，符合 GDPR/CCPA 等合规要求；Apple 的 Private Cloud Compute 则试图在必须上云时也保持隐私承诺（[Apple Siri AI](https://www.apple.com/uk/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)）。
- **混合推理（模型路由）**：日常辅助任务用小模型、复杂推理用云端大模型，可显著降低 token 成本。行业观点认为这种"按任务选模型"的策略可让企业 AI token 消耗降低 80% 以上（[中国电子报：AMD大中华区市场营销副总裁纪朝晖访谈](http://m.toutiao.com/group/7689737596750152192/)）。

## 关键数据

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 骁龙 X2 Elite Hexagon NPU | 最高 85 TOPS（INT8） | [Qualcomm 产品简介](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-X2-Elite-Product-Brief.pdf) |
| 天玑 9500 NPU 990 | 性能翻倍、峰值功耗降 56%、token 生成快 2 倍 | [MediaTek Dimensity 9500](https://www.mediatek.com/products/smartphones/mediatek-dimensity-9500) |
| Gemma 3n E2B 体积 | 约 2965MB；S24 Ultra GPU 预填充 816 tk/s | [LiteRT-LM Overview](https://developers.google.com/edge/litert-lm/overview) |
| Gemini Nano | Nano-1 约 1.8B、Nano-2 约 3.25B 参数 | [Gemini 论文](https://arxiv.org/pdf/2312.11805.pdf) |
| Phi-4 Mini（3.8B）Q4_K_M | 约 2.7GB 内存，手机端约 13–18 tk/s | [Best Mobile LLM Models 2026](https://www.promptquorum.com/power-local-llm/mobile-llm-models-phi4-gemma-smollm) |
| Llama 3.2 3B 4-bit 量化 | 模型体积减少 68.66% | [Optimizing LLMs Using Quantization（arXiv）](https://arxiv.org/pdf/2512.06490) |
| Hailo-10H | 典型功耗 2.5W，AEC-Q100 Grade 2 车规 | [Hailo-10H GA](https://hailo.ai/company-overview/newsroom/news/hailo-announces-general-availability-of-hailo-10h-edge-ai-accelerator-with-generative-ai-capabilities/) |
| 混合推理 token 节省 | 可降低 80% 以上 | [中国电子报](http://m.toutiao.com/group/7689737596750152192/) |

## 趋势与争议

1. **隐私 vs 能力**：端侧模型参数小、上下文有限（Gemini Nano 等场景上下文常被限制在几千 token），难以胜任复杂推理；Apple 与 Google 均以"端侧 + 私有云"的混合架构折中，如何在隐私承诺与模型能力间平衡仍是核心议题。
2. **内存是真正的天花板**：与数据中心受限于算力不同，端侧主要受限于内存容量与带宽，模型权重占用、量化精度损失、KV cache 增长共同构成瓶颈。NPU 的静态图特性还限制了上下文灵活性。
3. **模型碎片化与工具链**：端侧要面对 Arm/x86、Apple/Android/Windows、不同 NPU 后端（Hexagon、CoreML、XNNPACK、Vulkan、QNN）的碎片化，推理框架（ExecuTorch、ONNX Runtime、LiteRT）之间的兼容性成为工程痛点。
4. **"端侧 AI 是否被过度营销"**：厂商强调 TOPS 数字，但实际体验更取决于内存带宽、软件栈与应用生态；TOPS 与真实 token 吞吐并不线性相关。
5. **成本与能耗经济学**：把日常任务放在端侧、只在复杂推理时调用云端，是企业降低 AI 成本的重要路径，也推动了 AI PC 与"智能体主机"的产品形态。

## 参考来源

1. [Apple introduces Siri AI, a profoundly more capable and personal assistant](https://www.apple.com/uk/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)
2. [The next generation of Apple Intelligence is available today（Apple HK）](https://images.apple.com/hk/en/newsroom/2026/09/next-generation-of-apple-intelligence-available-today/)
3. [Apple accelerates app development with new intelligence frameworks and advanced tools](https://images.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/)
4. [GPTS24: Apple Launches Siri AI in iOS 27 Powered by Gemini-Refined Foundation Models](https://www.gpts24.com/en/news/apple-launches-siri-ai-in-ios-27-powered-by-gemini-refined-foundation-models)
5. [Gemma 3n（Google DeepMind）](https://deepmind.google/models/gemma/gemma-3n/)
6. [Gemma 版本（Google AI for Developers）](https://ai.google.dev/gemma/docs/releases)
7. [Gemma（Google DeepMind）](https://deepmind.google/models/gemma/)
8. [Lite RT-LM Overview](https://developers.google.com/edge/litert-lm/overview)
9. [Overview of the ML Kit Gen AI APIs](https://developers.google.com/ml-kit/genai/)
10. [Gemini Nano（Google DeepMind）](https://deepmind.google/models/gemini/nano/)
11. [Gemini: A Family of Highly Capable Multimodal Models（arXiv）](https://arxiv.org/pdf/2312.11805.pdf)
12. [Google Tensor: the brains behind Pixel phones](https://store.google.com/ideas/articles/google-tensor-pixel-smartphone/)
13. [Snapdragon X2 Elite Product Brief（PDF）](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Snapdragon-X2-Elite-Product-Brief.pdf)
14. [Qualcomm Snapdragon X2 Elite](https://www.qualcomm.com/laptops/products/snapdragon-x2-elite)
15. [高通：全新骁龙X2 Elite Extreme和骁龙X2 Elite](https://www.qualcomm.cn/news/releases/2025/09/releases-2025-09-24-2)
16. [MediaTek Dimensity 9500](https://www.mediatek.com/products/smartphones/mediatek-dimensity-9500)
17. [MediaTek Dimensity 9500（中文）](https://www.mediatek.com/zh-cn/products/smartphones/mediatek-dimensity-9500)
18. [MediaTek Dimensity flagship chip comparison（PDF）](https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Infographics/D9500%20Infographic-%2019th%20September.pdf)
19. [Best Mobile LLM Models in 2026: Phi-4 Mini vs Gemma 3 vs SmolLM](https://www.promptquorum.com/power-local-llm/mobile-llm-models-phi4-gemma-smollm)
20. [Lightweight Local LLM Comparison 2026](https://zendevy.com/en/ai/local-llm-lightweight-comparison-2026/)
21. [Best On-Device AI Models in 2026](https://andrew.ooo/answers/best-on-device-ai-models-2026/)
22. [EXECUTORCH — A Unified PyTorch Solution to Run AI Models On-Device（arXiv）](https://arxiv.org/pdf/2605.08195)
23. [Running PyTorch Models on Apple Silicon GPUs with the ExecuTorch MLX Delegate](https://pytorch.org/blog/running-pytorch-models-on-apple-silicon-gpus-with-the-executorch-mlx-delegate/)
24. [The Edge LLM Runtime Stack 2026](https://edgeaistack.ai/blog/edge-llm-runtime-stack-2026/)
25. [On-Device AI Inference: Running LLMs Locally with llama.cpp, MLX, and ExecuTorch](https://cloudrps.com/blog/on-device-ai-inference-edge-models-architecture/)
26. [ONNX Runtime: Run SLMs on Snapdragon devices with NPUs](https://onnxruntime.ai/docs/genai/tutorials/snapdragon.html)
27. [ncnn（PyPI）](https://pypi.org/project/ncnn/)
28. [Hailo Announces General Availability of Hailo-10H Edge AI Accelerator](https://hailo.ai/company-overview/newsroom/news/hailo-announces-general-availability-of-hailo-10h-edge-ai-accelerator-with-generative-ai-capabilities/)
29. [Ambarella Launches X7, Its First Standalone AI Accelerator](https://www.ambarella.com.tw/news/ambarella-launches-x7-its-first-standalone-ai-accelerator-to-add-physical-ai-to-any-host-processor/)
30. [Ambarella and ZEDEDA Partner to Bring Cloud-Orchestrated AI to the Physical Edge](https://www.ambarella.com/news/ambarella-and-zededa-partner-to-bring-cloud-orchestrated-ai-to-billions-of-devices-at-the-physical-edge/)
31. [Global AI Hardware Landscape 2026](https://www.geniatech.com/ai-hardware-2025/)
32. [Energy-Efficient On-Device RAG on a Mobile NPU（arXiv）](https://arxiv.org/html/2606.11257v1)
33. [On-Device RAG for Android: Embedding Models, Vector Search in SQLite](https://mvpfactory.io/blog/on-device-rag-for-android-running-embedding-models-vector-search-in-sqlite-and)
34. [On-device Semantic Selection Made Low Latency and Memory Efficient（arXiv）](https://arxiv.org/html/2510.15620v2)
35. [Optimizing LLMs Using Quantization For Mobile Execution（arXiv）](https://arxiv.org/pdf/2512.06490)
36. [AI Wiki: Llama 3.2](https://aiwiki.ai/wiki/llama_3_2/raw)
37. [中国电子报：AMD大中华区市场营销副总裁纪朝晖访谈](http://m.toutiao.com/group/7689737596750152192/)