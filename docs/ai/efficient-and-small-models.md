# 小模型与高效模型

> 最后更新：2026-09-26 ｜ 领域：AI·训练与推理工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

小语言模型（Small Language Model, SLM）与"高效模型"指以极低推理成本换取可用智能的一类模型，通常具备三个特征之一或多个：**参数量小**（一般指 3B 以下）、**稀疏激活**（MoE 结构，总参数量大但每 token 只激活一小部分）、以及**面向端侧优化**（量化格式、低内存占用、CPU/移动 NPU 可运行）。

学术工作中对 SLM 的常见界定是"参数量通常少于 30 亿、已成为端侧部署的实用选择"，并列举了三类代表：Google DeepMind 的 Gemma 系列提供 1B 到 4B 参数、以针对边缘设备优化的量化格式发布；阿里巴巴 Qwen3 提供从 0.6B 起的尺寸；Microsoft 的 Phi-4 Mini 面向约 3B 量级（[Less Is More: Engineering Challenges of On-Device Small Language Model Integration in a Mobile Application](https://arxiv.org/pdf/2604.24636v2)）。相关趋势研究指出，过去数年参数量低于 4B 的语言模型数量急剧增加，且这些较新的模型正变得多模态，能力从文本扩展到图像到文本等任务（[Edge-First Language Model Inference: Models, Metrics, and Tradeoffs](https://arxiv.org/pdf/2505.16508.pdf)）。

小模型的价值不只是"便宜"：当任务边界明确（分类、抽取、路由、局部代码补全、端侧隐私敏感处理）时，一个 3B 级模型可以在手机上以每秒数十 token 的速度运行，从而绕过网络时延、隐私外发与 API 成本三大约束。

## 最新进展（2025–2026）

**Gemma 系列继续迭代，并走向本地设备。** Google 于 2025 年 3 月发布 Gemma 3，提供 1B、4B、12B、27B 四个尺寸，全部变体均为多模态（文本 + 图像），在消费级硬件上可运行（[The LLM Encyclopedia, July 11, 2026](https://stochasticsandbox.com/posts/llm-encyclopedia-2026-07-11/)）。2026 年 4 月，Google 发布 Gemma 4，官方定位为"迄今最智能的开放模型"（[Gemma 4: Byte for byte, the most capable open models](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)）。面向端侧，Google 推出 Gemma 3n，专为在手机、平板与笔记本上本地运行而设计，并与领先移动硬件厂商合作，架构上与下一代 Gemini Nano 共享，主打显著缩减的内存占用与"隐私优先、可离线"（[Gemma 3n — Google DeepMind](https://deepmind.google/models/gemma/gemma-3n/)）。Gemma 3n 的 E2B 与 E4B 变体原始参数量分别为 5B 与 8B，但借助架构创新可以在接近传统 2B 与 4B 模型的内存占用下运行，最低只需约 2GB（E2B）与 3GB（E4B）内存；其核心组件包括用于算力灵活性的 MatFormer 架构、用于内存效率的 Per-Layer Embeddings（PLE）与参数跳过（parameter skipping）（[Introducing Gemma 3n: The developer guide](https://googledevelopers.blogspot.sg/id/introducing-gemma-3n-developer-guide/)）。通过在运行时动态加载参数并缓存 PLE，可进一步降低运行内存（[Gemma 3n 型号概览 — Google AI for Developers](https://ai.google.dev/gemma/docs/gemma-3n?hl=zh-cn)）。Gemma 3n 已在 NVIDIA RTX 与 Jetson 平台上正式可用，并在文本与视觉之外加入音频能力（[Run Google DeepMind's Gemma 3n on NVIDIA Jetson and RTX](https://developer.nvidia.com/blog/run-google-deepminds-gemma-3n-on-nvidia-jetson-and-rtx/)）。

**小尺寸 MoE 成为"消费级甜点"。** Qwen3.6-35B-A3B 携带约 350 亿总参数但每 token 仅激活约 30 亿，在 agentic coding 套件上超过 Gemma 4-31B、并在多数视觉任务上追平 Claude Sonnet 4.5；20.9GB 的 Q4 量化可直接在 MacBook Pro M5 上运行（[Qwen3.6-35B-A3B: Alibaba's open-weight coding MoE](https://botmonster.com/ai/qwen-3-6-35b-a3b-open-weight-coding-moe/)）。官方博客确认其为全开源 MoE（35B 总参数 / 3B 激活），具备与更大模型相当的 agentic coding 能力以及较强的多模态感知与推理能力（[Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All](https://qwen.ai/blog?id=qwen3.6-35b-a3b)）；其 FP8 版本上下文长度为 262K，发布于 2026 年 4 月 14 日（[Qwen3.6 35B A3B FP8 — Together AI](https://www.together.ai/models/qwen3-6-35b-a3b-fp8)）。同代还有稠密的 Qwen3.6-27B，采用 Apache 2.0 许可、262K 上下文，Q4 下约 17GB，Qwen 团队称其在 SWE-bench Verified 上得 77.2，与 Sonnet 4.5 同级、比 Sonnet 4.6 的 79.6 低约 2 分（[Qwen 3.6 Complete Guide: 27B Dense, 35B-A3B MoE](https://insiderllm.com/pdfs/qwen-3-6-local-ai-guide.pdf)）。

**端侧工具链成熟。** vLLM 已把服务栈带到 Apple Silicon（vllm-metal），支持分页与连续批处理、批量 MTP 与 M5 prefill 加速（[Announcing vllm-metal: Concurrent Serving on Apple Silicon](https://vllm-project.github.io/2026/09/22/vllm-metal-v0-28-0.html)）。本地推理栈方面，GGUF 格式配合 llama.cpp、Ollama、LM Studio 是桌面与 CPU 场景的主流方案（[Model Quantization Guide: Foundations to Production Serving](https://slavadubrov.github.io/blog/2026/07/05/model-quantization-in-2026-from-foundations-to-production-serving/)）。芯片与模型侧，MediaTek 与阿里通义千问合作，在搭载天玑 9400 移动平台的设备上完成 Qwen3 模型部署，该平台集成第八代 AI 处理器 NPU 890 并支持主流大语言模型（[MediaTek 携手阿里通义千问在天玑移动平台完成 Qwen3 模型部署](https://developer.mediatek.com/ai/681dc0083648cc23f27eae09.html)）。

## 核心技术与关键概念

- **参数效率**：小模型的能力来自更高质量的数据配比与训练配方（如合成数据、课程学习），而非单纯堆参数；Phi 系列是"数据质量优先"的代表路线。Phi-4-Mini 是一个 3.8B 参数的稠密 decoder-only Transformer，采用分组查询注意力（GQA）、20 万词表与共享输入输出嵌入，在高质量 web 与合成数据上训练，在数学与代码等需要复杂推理的任务上宣称可匹配参数量约为其两倍的模型（[Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs](https://arxiv.org/html/2503.01743)）。
- **稀疏激活（MoE）**：以总参数换容量、以激活参数换成本。35B-A3B 这类配置让模型在显存占用接近 3B 稠密模型的同时保有更大知识容量，代价是需要全部专家参数常驻内存。
- **量化与格式**：端侧普遍使用 Q4_K_M、Q4_0、INT4 等格式；量化等级越高（B 数越小）内存占用越低、速度越快，但质量下降。例如 135M 的 SmolLM2 以 Q4_0 运行仅需约 150MB 内存（[SmolLM2 Model Sizes: 135M, 360M and 1.7B on Edge](https://www.ertas.ai/blog/smollm2-sub-3b-models-edge-mobile)）。
- **端侧运行时**：核心优化点包括 KV cache 分页/量化、投机解码（用更小模型起草）、以及把 NPU/GPU 的 prefill 加速与 CPU decode 结合。Google 的 Lite RT-LM 即为端侧运行时之一，其公开数据列出了不同设备上 CPU/GPU 的 prefill 与 decode 速度（[Lite RT-LM Overview](https://developers.google.com/edge/litert-lm/overview)）。
- **端云协同**：小模型处理高频、轻量、隐私敏感请求，复杂请求升级到云端大模型，是当前主流产品架构。

## 代表性项目 / 公司 / 产品（附官方链接）

| 系列 | 代表尺寸 | 定位与许可 |
| --- | --- | --- |
| Gemma（Google DeepMind） | Gemma 3：1B / 4B / 12B / 27B；Gemma 4（2026-04 发布）；Gemma 3n：E2B / E4B（原始 5B / 8B） | 开放权重，全尺寸多模态；Gemma 3n 面向手机/平板/笔记本本地运行（[Gemma 3n](https://deepmind.google/models/gemma/gemma-3n/)） |
| Phi（Microsoft） | Phi-4 Mini 3.8B / Phi-4 14B | 端侧推理质量优先（[Phi open model family](https://azure.microsoft.com/en-gb/products/phi)） |
| Qwen3 / Qwen3.5 / Qwen3.6（阿里巴巴） | 0.6B 起，小尺寸含 30B-A3B、35B-A3B MoE、27B 稠密 | 部分 Apache 2.0 |
| SmolLM2（Hugging Face） | 135M / 360M / 1.7B | 极小尺寸端侧 |
| gpt-oss（OpenAI） | 120B / 20B | 开放权重推理模型，默认 MXFP4 量化（[gpt-oss 介绍](https://openai.com/ko-KR/index/introducing-gpt-oss/)） |

（来源：[Less Is More](https://arxiv.org/pdf/2604.24636v2)、[Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)、[Gemma 3n](https://deepmind.google/models/gemma/gemma-3n/)、[The LLM Encyclopedia, July 11, 2026](https://stochasticsandbox.com/posts/llm-encyclopedia-2026-07-11/)、[Qwen 3.6 Complete Guide](https://insiderllm.com/pdfs/qwen-3-6-local-ai-guide.pdf)、[SmolLM2 Model Sizes](https://www.ertas.ai/blog/smollm2-sub-3b-models-edge-mobile)）

## 关键数据与评测结果

**端侧排行榜口径。** 一份 2026 年端侧/移动 LLM 排行榜给出：Gemma 3 4B 是最佳全能边缘模型，MMLU 43.6、IFEval 同类最佳，在 iPhone 16 Pro 上借助 Google AI Edge SDK 速度最快约 27 tok/s；Phi-4-Mini（3.8B）在推理质量上领先，GSM8K 88.6%、ARC-C 83.7%，在 MacBook 上约 22 tok/s（[Edge and Mobile LLM Leaderboard 2026: Phi, Gemma, Qwen](https://www.awesomeagents.ai/leaderboards/edge-mobile-llm-leaderboard/)）。

**手机实测口径（与上一条存在差异）。** 另一来源称 Phi-4 Mini（3.8B）可在 RAM 8GB 以上的高端手机上以实用速度运行，在 iPhone 17 Pro 上约 13–18 tok/s；SmolLM2 1.7B 在所有测试设备上最快；Qwen3 1.7B 多语言最佳（[2026년 모바일 LLM 최고 모델: Phi-4 Mini vs Gemma 3 vs SmolLM](https://www.promptquorum.com/ko/power-local-llm/mobile-llm-models-phi4-gemma-smollm)）。同一模型（Phi-4 Mini）在不同来源的 tok/s 分别为约 22（MacBook）与 13–18（iPhone 17 Pro），说明端侧数字与设备、量化等级、运行时强相关，不可直接横向比较。

**端侧机型实测（Gemma 4 E2B）。** Google 的 Lite RT-LM 文档列出，Gemma4-E2B（约 2.58GB）在 Samsung S26 Ultra 上 CPU decode 约 47 tk/s、GPU decode 约 52 tk/s；在 iPhone 17 Pro 上分别约 25 与 57 tk/s；在 MacBook Pro M4 Max 上分别约 42 与 160 tk/s（[Lite RT-LM Overview](https://developers.google.com/edge/litert-lm/overview)）。

**内存与设备门槛。** SmolLM2 方面：iPhone 12 及以后机型（4GB RAM）均可运行 Q4_K_M 的 SmolLM2 1.7B；更老的 3GB 机型只能运行 360M 或 135M 变体；iPhone 15 Pro 上 SmolLM2 135M（Q4_0）达 85 tok/s、分类时延 15ms、占用 150MB 内存（[SmolLM2 Model Sizes](https://www.ertas.ai/blog/smollm2-sub-3b-models-edge-mobile)）。另一份手机端指南给出：Phi-4-mini（3.8B）INT4 约 2.4GB、需 8GB 手机内存、在 Snapdragon 8 Elite 上约 30–40 tok/s；Qwen3 0.6B 约 0.4GB、需 6GB 内存、80+ tok/s；Llama 3.1 8B Q4 约 4.7GB、需 12GB 内存、约 10–15 tok/s（[Can You Run an LLM on a Phone? On-Device AI Explained](https://ai-tldr.dev/learn/local-open-models/running-models-locally/run-llms-on-a-phone/)）。一项手机应用集成研究给出的部署分层是：Gemma 4 E2B（约 2.6B、2.6GB）面向 ≥8GB RAM 的高端设备，具备更好的指令遵循但初始化更慢（约 10s）；Qwen3 0.6B（约 600M、614MB）面向更轻量的设备（[Less Is More](https://arxiv.org/pdf/2604.24636v2)）。

**CPU 与边缘开发板的对比口径。** 一项研究比较不同后端上端侧 LLM 的 prefill 性能，覆盖 Qwen2-0.5B、Llama-3.2-1B、Qwen2-1.5B、Llama-3.2-3B、Mistral-7B 与 Llama-3.2-8B 等模型，探讨 CPU 在何种条件下可超越 GPU（[Challenging GPU Dominance: When CPUs Outperform for On-Device LLM Inference](https://arxiv.org/html/2505.06461)）。在 Jetson Orin Nano 上，一份实测给出 gemma3:1b（Ollama）平均约 26.33 t/s、Qwen2.5-0.5B-Instruct（vLLM）约 15.18 t/s、Qwen3-0.6B-FP8（vLLM）约 12.81 t/s（[Why Your Jetson Orin Nano's 40 TOPS Goes Unused](https://ericxliu.me/posts/benchmarking-llms-on-jetson-orin-nano/)）。另有工作跨 8 类任务评测了 12 个 SLM（含 Llama-3.2-1B/3B、SmolLM2-135M/1.7B、gemma-3-1b/270m 等），以寻找微调基座模型（[We Benchmarked 12 Small Language Models Across 8 Tasks](https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/)）。

**Apple Silicon 实测配置。** 在 48GB 的 Mac Mini / Studio 上运行 Qwen3.5-35B-A3B 的 8bit 量化版本，占用 37GB 内存、约 83 tok/s，被描述为"智能 + 速度"的平衡点；32GB 或 36GB 机器上更合适的是 Qwen3.5-27B 4bit，占 15.3GB、约 39 tok/s（[rapid-mlx 0.5.0](https://pypi.org/project/rapid-mlx/0.5.0/)）。

**能力边界。** 一项本地模型的实地研究指出，Qwen3.6 35B-A3B、Qwen3.6 27B 与 Gemma 4 31B 在最长 280KB 的 prompt 上复现 20 行代码块的准确率均超过 95%，但"复现代码"不等于"代码生成"：在真实 PRD 上测试的三款编码模型中，只有稠密的 Qwen3.6 27B 产出了可用应用（[Local LLMs in 2026: a hardware-and-model field study](https://www.jacques.io/blog/gw-2026-local-coding-llm-comparisons)）。

## 趋势与争议

1. **"小模型够用"的边界不清**：检索/复现类任务表现已接近大模型，但开放式生成与长链推理仍有明显差距，选型应基于任务而非参数量。
2. **MoE vs 稠密之争**：小尺寸 MoE 在同一显存预算下给出更高总容量，但需要全部专家常驻内存、且对解码效率有额外系统要求；稠密模型在纯生成任务上被观察到更稳定。
3. **基准污染与口径混乱**：端侧 tok/s、MMLU、任务准确率的测量条件差异巨大，"最快""最强"结论高度依赖测试设置（例如同一 Phi-4 Mini 在不同来源、不同设备上的 tok/s 相差可达一倍以上）。
4. **许可与商用限制**：Gemma 与部分 Qwen 版本有自定义许可条款，Apache 2.0（如 Qwen3.6-27B）商用门槛更低。
5. **端云边界迁移**：随着端侧能力提升，越来越多功能从云端下沉，但隐私、模型更新与设备碎片化带来新的运维问题。

## 参考来源

1. [Less Is More: Engineering Challenges of On-Device Small Language Model Integration in a Mobile Application](https://arxiv.org/pdf/2604.24636v2)
2. [Edge-First Language Model Inference: Models, Metrics, and Tradeoffs](https://arxiv.org/pdf/2505.16508.pdf)
3. [Gemma 4: Byte for byte, the most capable open models](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
4. [Gemma 3n — Google DeepMind](https://deepmind.google/models/gemma/gemma-3n/)
5. [Introducing Gemma 3n: The developer guide](https://googledevelopers.blogspot.sg/id/introducing-gemma-3n-developer-guide/)
6. [Gemma 3n 型号概览 — Google AI for Developers](https://ai.google.dev/gemma/docs/gemma-3n?hl=zh-cn)
7. [Run Google DeepMind's Gemma 3n on NVIDIA Jetson and RTX](https://developer.nvidia.com/blog/run-google-deepminds-gemma-3n-on-nvidia-jetson-and-rtx/)
8. [Lite RT-LM Overview](https://developers.google.com/edge/litert-lm/overview)
9. [The LLM Encyclopedia, July 11, 2026](https://stochasticsandbox.com/posts/llm-encyclopedia-2026-07-11/)
10. [Qwen3.6-35B-A3B: Alibaba's open-weight coding MoE](https://botmonster.com/ai/qwen-3-6-35b-a3b-open-weight-coding-moe/)
11. [Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All](https://qwen.ai/blog?id=qwen3.6-35b-a3b)
12. [Qwen3.6 35B A3B FP8 — Together AI](https://www.together.ai/models/qwen3-6-35b-a3b-fp8)
13. [Qwen 3.6 Complete Guide: 27B Dense, 35B-A3B MoE, and Which to Use](https://insiderllm.com/pdfs/qwen-3-6-local-ai-guide.pdf)
14. [Announcing vllm-metal: Concurrent Serving on Apple Silicon](https://vllm-project.github.io/2026/09/22/vllm-metal-v0-28-0.html)
15. [Model Quantization Guide: Foundations to Production Serving](https://slavadubrov.github.io/blog/2026/07/05/model-quantization-in-2026-from-foundations-to-production-serving/)
16. [MediaTek 携手阿里通义千问在天玑移动平台完成 Qwen3 模型部署](https://developer.mediatek.com/ai/681dc0083648cc23f27eae09.html)
17. [Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs](https://arxiv.org/html/2503.01743)
18. [Phi open model family — Microsoft Azure](https://azure.microsoft.com/en-gb/products/phi)
19. [gpt-oss 介绍 — OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/)
20. [Edge and Mobile LLM Leaderboard 2026: Phi, Gemma, Qwen](https://www.awesomeagents.ai/leaderboards/edge-mobile-llm-leaderboard/)
21. [2026년 모바일 LLM 최고 모델: Phi-4 Mini vs Gemma 3 vs SmolLM](https://www.promptquorum.com/ko/power-local-llm/mobile-llm-models-phi4-gemma-smollm)
22. [SmolLM2 Model Sizes: 135M, 360M and 1.7B on Edge](https://www.ertas.ai/blog/smollm2-sub-3b-models-edge-mobile)
23. [Can You Run an LLM on a Phone? On-Device AI Explained](https://ai-tldr.dev/learn/local-open-models/running-models-locally/run-llms-on-a-phone/)
24. [Challenging GPU Dominance: When CPUs Outperform for On-Device LLM Inference](https://arxiv.org/html/2505.06461)
25. [Why Your Jetson Orin Nano's 40 TOPS Goes Unused (And What That Means for Edge AI)](https://ericxliu.me/posts/benchmarking-llms-on-jetson-orin-nano/)
26. [We Benchmarked 12 Small Language Models Across 8 Tasks to Find the Best Base Model for Fine-Tuning](https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/)
27. [rapid-mlx 0.5.0](https://pypi.org/project/rapid-mlx/0.5.0/)
28. [Local LLMs in 2026: a hardware-and-model field study](https://www.jacques.io/blog/gw-2026-local-coding-llm-comparisons)