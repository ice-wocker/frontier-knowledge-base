# 开源 AI 工具链

> 最后更新：2026-09-26 ｜ 领域：AI·平台、工具与落地 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

开源 AI 工具链涵盖模型与数据托管、训练与微调、推理与服务、本地运行、评测等环节。当前生态大致可分为几层：以 Hugging Face Hub 为核心的模型与数据集托管层；以 Transformers、PyTorch 等为代表的训练/微调框架层；以 vLLM、SGLang、TensorRT-LLM 为代表的高吞吐服务层；以 llama.cpp、Ollama、LM Studio 为代表的本地/端侧运行层。2025–2026 年的趋势是「本地运行质量快速逼近服务端」与「推理引擎按硬件分化为多条技术路线」。

## 最新进展（2025–2026）

**本地运行引擎的成熟。** 截至 2026 年 7 月的第三方统计显示，llama.cpp 采用 MIT 许可、GitHub 星标约 120,000，以 GGUF 格式著称，定位本地、CPU 与边缘推理；Ollama 同为 MIT 许可、星标约 176,000，以模型注册表（registry）与 CLI 为特色，面向本地桌面与开发者使用（[LLM inference engine](https://aiwiki.ai/wiki/inference_engine)）。Ollama 0.30 版本通过 llama.cpp 改进了性能与 GGUF 模型兼容性，并与之互补，在其 Apple Silicon 上的 MLX 引擎之外带来更广的硬件与模型支持；Ollama 官方博客还提到 Gemma 4 在 Apple Silicon 上通过多 token 预测（MTP）在 0.31 版本显著加速（[Blog · Ollama](https://ollama.com/blog)）。到 2026 年，GGUF 已成为本地/开放推理工具的默认交换格式，GGML 模型文件不再被支持（[llama.cpp и GGUF в 2026: low-level local runtime, hybrid CPU+GPU inference and current quantization reality](https://aisrc.ru/local-ai/llama-cpp-gguf)）。

**桌面 GUI 侧的竞争。** LM Studio 以桌面应用形态提供基于 Hugging Face 的搜索下载目录、聊天界面、逐模型加载设置与 Developer Mode；0.4.24 版本进一步加入面向 GGUF 的高级 llama.cpp 参数覆盖、提示词模板覆盖，以及默认支持视觉模型的加载期投机解码（speculative decoding）（[Ollama vs LM Studio 2026: Ollama Wins for Devs](https://dev.to/shaam_ai/ollama-vs-lm-studio-2026-ollama-wins-for-devs-p3l)）。其更新日志显示已支持 DFlash、DSpark 与 MTP assistant drafters，并要求 llama.cpp 引擎版本 2.29.1 或更高（[Changelog · LM Studio](https://lmstudio.ai/changelog/lmstudio)）。针对非技术与桌面用户，GPT4All 提供纯 CPU、零终端操作的本地 AI；mlx-lm 是 Mac 原生最快的推理路径，也是唯一可在 Apple Silicon 上本地微调的工具（[The Complete Guide to Local LLM Inference Tools in July 2026](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)）。

**服务端引擎的分工。** vLLM 官方称其为「面向所有人的简单、快速、低成本 LLM 推理与服务库」，最初由 UC Berkeley Sky Computing Lab 开发，现由 2,000+ 贡献者维护，是活跃度最高的开源 AI 项目之一（[vLLM](https://docs.vllm.ai/en/latest/index.html)）。其核心技术包括 PagedAttention 高效管理注意力 KV 内存、连续批处理（continuous batching）、CUDA/HIP graph 加速执行，以及 GPTQ、AWQ、SqueezeLLM、FP8 KV Cache 等量化支持（[vLLM Getting Started](https://docs.vllm.ai/_/downloads/en/v0.5.2/pdf/)）。vLLM 默认从 Hugging Face Hub 加载模型，可通过 `HF_HOME` 修改下载路径（[Supported Models](https://docs.vllm.ai/en/latest/models/supported_models/)）。2026 年 vLLM 进一步向新硬件与低精度扩展：官方博客介绍在 Blackwell 上推进 WideEP 与大规模服务成熟化，内容包括 NVFP4 GEMM、FP8 GEMM、NVFP4 MoE Dispatch 等低精度算子，RoPE+Quant 等 kernel 融合、通过权重卸载降低 prefill 开销以及 async scheduling 与 prefill/decode 分离等（[Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I)](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)）。vLLM 还新增了对 Apple Silicon 的并发服务支持：vllm-metal 把 vLLM 的调度器、paged KV cache 与 OpenAI 兼容服务器带到 Apple Silicon，由 MLX 与 Metal 负责执行，首个正式版本 v0.28.0 对齐上游版本号，引入批量 MTP、GGUF 与混合模型支持以及 M5 上更快的 prefill（[Announcing vllm-metal: Concurrent Serving on Apple Silicon](https://vllm-project.github.io/2026/09/22/vllm-metal-v0-28-0.html)）。

**生态的其他变化。** 有资料指出 Hugging Face TGI 自 2025 年 12 月起进入维护模式，采用 Apache 2.0 许可（星标约 11,000，已归档），早期以 Rust router 与连续批处理为特色（[LLM inference engine](https://aiwiki.ai/wiki/inference_engine)）。此外有社区文章称 GGUF 规范已成为 W3C 批准的推荐标准，使工具链可依赖稳定的二进制契约（[Open Source AI: What's New in September 2026](https://dev.to/vijay_vinoth_8e7abfd3f5b5/open-source-ai-whats-new-in-september-2026-2bah)）；不过另有资料称 GGUF 当前规范的结构版本为 v3，元数据键、支持的模型架构、量化类型与命令行参数仍会持续增加（[大模型量化从0到1(八): GGUF 格式彻底解剖——llama.cpp 生态的基石](https://blog.csdn.net/weixin_49520696/article/details/162737098)，未提及 W3C 推荐，两处说法需分别看待）。

**训练与框架层的更新。** 有报道称 Hugging Face 发布 Transformers 2.0，新增 200+ 模型（涵盖视觉-语言混合模型与指令微调 LLM）与 30 个新语言包（语言覆盖总数达 120），提供统一量化 API（8-bit 推理、精度损失低于 2%），并通过新的 `transformers-cloud` 扩展原生集成 AWS、GCP、Azure（[Hugging Face Unveils Transformers 2.0, Adding 200 Models and 30 Languages](https://dev.to/techpulse01239/hugging-face-unveils-transformers-20-adding-200-models-and-30-languages-4ep4)）。Hugging Face 依旧是最主要的开源权重分发中心，例如有模型以约 228 tok/s（Apple M5 Max）与约 116 tok/s（AMD Ryzen AI Max+ 395）在设备端运行，并受 llama.cpp、MLX、vLLM、SGLang 与 ONNX 支持（[Open-weight LLM releases](https://www.llm-releases.com/open-weight-models)）。

## 核心技术与关键概念

**模型分发与格式**：Hugging Face Hub 是事实上的模型分发中心，vLLM 等引擎默认从中拉取权重（[Supported Models](https://docs.vllm.ai/en/latest/models/supported_models/)）。GGUF 是 llama.cpp/Ollama 生态的模型格式，便于量化的本地加载；GGUF 让权重、tokenizer 信息与元数据一同携带，并可内嵌 chat-template 与运行时元数据，提升跨本地栈的可移植性（[llama.cpp и GGUF в 2026](https://aisrc.ru/local-ai/llama-cpp-gguf)、[大模型量化从0到1(八)](https://blog.csdn.net/weixin_49520696/article/details/162737098)）。

**量化**：本地运行依赖多种量化方案。llama.cpp 在 ROCm 上支持从 1.5-bit 到 8-bit 整数的多种量化，以加速推理并降低内存占用（[What is llama.cpp? — AMD ROCm docs](https://rocm.docs.amd.com/projects/llama-cpp/en/docs-25.08/what-is-llama-cpp.html)）。一篇针对 Llama-3.1-8B-Instruct 的统一评测系统性比较了 llama.cpp 的多种量化方案（[Which Quantization Should I Use? A Unified Evaluation of llama.cpp Quantization on Llama-3.1-8B-Instruct](https://arxiv.org/html/2601.14277)）。Ollama 上可观察到同一模型的不同量化档位对比——例如某 MoE 模型 MXFP4_MOE 为 7.0 GB、KLD vs BF16 为 0.166、Top-token match 84.2%；Q8_0 为 12.9 GB、KLD 0.016、Top-token match 95.2%；BF16 参考为 24.3 GB（[Mellum2 Instruct — MXFP4_MOE](https://ollama.com/JetBrains/mellum2-instruct-mxfp4_moe:latest)）。这些数据说明量化档位在体积与质量之间存在明确权衡。

**推理引擎关键技术**：PagedAttention、连续批处理、KV cache 量化与图执行（CUDA/HIP graph）是服务端引擎提升吞吐的核心（[vLLM Getting Started](https://docs.vllm.ai/_/downloads/en/v0.5.2/pdf/)）。量化方面，vLLM 支持动态 FP8 W8A8（无需校准数据，指定 `--quantization="fp8_per_tensor"` 即可把 BF16/FP16 模型动态量化为 FP8），并提供 block-wise 权重量化（`weight_block_size`）、online 激活缩放（`activation_scheme="dynamic"` 或 `"static"`）等参数（[FP8 W8A8 (vLLM)](https://docs.vllm.ai/en/latest/features/quantization/llm_compressor/fp8/)）。SGLang 的核心创新是 RadixAttention：不再在生成结束后丢弃 KV cache，而是把提示与生成结果的 KV cache 保留在一棵基数树（radix tree）中，实现高效的 prefix 搜索、复用、插入与驱逐，并配合 LRU 驱逐策略与缓存感知调度提升命中率（[Efficiently Programming Large Language Models using SGLang](https://arxiv.org/pdf/2312.07104v1.pdf)）。SGLang 面向请求共享公共前缀的场景（多轮对话、RAG、Agent 工作流），并通过 xGrammar 后端提供 JSON、regex、grammar 约束的结构化输出解码（[LLM Inference with SGLang](https://build.nvidia.com/station/sglang-inference/overview)）。

**训练与微调**：Transformers 库与 PyTorch 构成主流训练栈；Apple Silicon 上可用 mlx-lm 在本机进行推理与微调（[The Complete Guide to Local LLM Inference Tools in July 2026](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)）。

**评测与可观测**：MLflow 等平台提供 50+ 内置指标与 LLM judges，可用于开源模型的质量跟踪（[MLflow](https://mlflow.org/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Hugging Face / Transformers**：模型与数据集托管及训练库（[https://huggingface.co/](https://docs.vllm.ai/en/latest/models/supported_models/)）。
- **vLLM**：高吞吐推理服务引擎（[https://docs.vllm.ai/](https://docs.vllm.ai/en/latest/index.html)）；并扩展出 Apple Silicon 版本 vllm-metal（[vllm-metal](https://vllm-project.github.io/2026/09/22/vllm-metal-v0-28-0.html)）。
- **llama.cpp**：本地/CPU/边缘推理引擎，GGUF 格式，MIT（[LLM inference engine](https://aiwiki.ai/wiki/inference_engine)）。
- **Ollama**：本地模型注册表与 CLI，MIT（[https://ollama.com/blog](https://ollama.com/blog)）。
- **LM Studio**：桌面 GUI 与本地服务器（[https://lmstudio.ai/changelog/lmstudio](https://lmstudio.ai/changelog/lmstudio)）。
- **SGLang**：服务端推理引擎之一，RadixAttention + xGrammar 结构化输出（[LLM Inference with SGLang](https://build.nvidia.com/station/sglang-inference/overview)）。
- **Jan / GPT4All / mlx-lm / KoboldCpp**：本地运行与桌面替代选项（[The Complete Guide to Local LLM Inference Tools](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)；[Local LLM Inference in 2026: The Complete Guide to Tools, Hardware & Open-Weight Models](https://blog.starmorph.com/blog/local-llm-inference-tools-guide)）。
- **MLflow**：开源 AI 平台（[https://mlflow.org/](https://mlflow.org/)）。

## 关键数据与评测结果（附来源）

- llama.cpp GitHub 星标约 120,000、Ollama 约 176,000（2026 年 7 月，第三方统计）（[LLM inference engine](https://aiwiki.ai/wiki/inference_engine)）。另一份 2026 年统计口径不同：vLLM 31k+、MLX 24.6k、KoboldCpp 9.5k，而 LM Studio 为闭源未计（[Local LLM Inference in 2026](https://blog.starmorph.com/blog/local-llm-inference-tools-guide)）——同为第三方，数值与统计对象不一，需说明口径。
- Hugging Face TGI 星标约 11,000，2025 年 12 月起维护模式（第三方统计）（[LLM inference engine](https://aiwiki.ai/wiki/inference_engine)）。
- vLLM 由 2,000+ 贡献者维护（官方）（[vLLM](https://docs.vllm.ai/en/latest/index.html)）。
- Hugging Face 上可选的 GPTQ 量化模型超过 5,000 个（vLLM 文档）（[GPTQModel](https://docs.vllm.ai/en/latest/features/quantization/gptqmodel/)）。
- 量化档位对比示例：MXFP4_MOE 7.0 GB / KLD 0.166 / Top-token match 84.2%（Ollama 模型页）（[Mellum2 Instruct — MXFP4_MOE](https://ollama.com/JetBrains/mellum2-instruct-mxfp4_moe:latest)）。
- 性能对比口径：有第三方称 vLLM 通过 PagedAttention 在并发吞吐上约为 Ollama 的 16–20 倍，SGLang 的 RadixAttention 使 RAG 流水线约快 6 倍（[The Complete Guide to Local LLM Inference Tools in July 2026](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)，为第三方单一来源口径）。
- SGLang 在一项厂商合作优化中报告：在某 agentic 负载下，TopK-V2 把平均 kernel 延迟从 40.7 µs 降至 17.5 µs（80K ISL，2.33×），在 1M ISL 时从 372.1 µs 降至 36.6 µs（10.17×）（[Serving GLM5.2 NVFP4 Agentic Workload with SGLang](https://www.lmsys.org/blog/2026-07-13-glm52-optimization/)）。
- 开源权重再分发：一项研究称 2024 年 1 月至 2026 年 3 月间在 HuggingFace 上识别出 3,471 个原始"uncensored"模型，平均被重新打包 2.4 次；三个行为主体占全部 8,164 次压缩再分发的 52%，一旦量化并镜像到不同账户、格式与注册表（如 Ollama）后，即使上游移除这些模型仍能持续存在并更易被下游部署（[Uncensored Open-weight Models: Redistribution as the Persistence Layer](https://arxiv.org/html/2609.05241v1)）。

## 趋势与争议

**硬件路线分化**：服务端引擎出现按硬件分化的分支。vLLM 官方自 2026 年 1 月 20 日起在上游提供官方 Docker 镜像，此前 AMD 通过 Infinity hub 为 MI300X 提供预构建优化镜像（[Using Docker](https://docs.vllm.ai/en/latest/deployment/docker/)）；2026 年 vllm-metal 又把 vLLM 的能力带到 Apple Silicon，反映多硬件后端并行的趋势（[vllm-metal](https://vllm-project.github.io/2026/09/22/vllm-metal-v0-28-0.html)）。AMD 与 Moonshot AI 亦合作针对 AMD GPU 重构 agentic AI 服务栈（[Rebuilding Agentic AI from First Principles for AMD GPU](https://www.amd.com/en/developer/resources/technical-articles/2026/rebuilding-agentic-ai-for-amd-gpu.html)）。

**本地 vs 云**：本地运行在隐私、成本与离线可用性上有优势，但硬件内存约束与量化质量损失构成权衡；桌面工具（LM Studio）与 CLI 工具（Ollama）在易用性与可脚本化之间存在取舍（[Ollama vs LM Studio 2026](https://dev.to/shaam_ai/ollama-vs-lm-studio-2026-ollama-wins-for-devs-p3l)）。

**格式标准化**：社区称 GGUF 规范已获 W3C 推荐，若属实将降低模型与工具间的耦合（[Open Source AI: What's New in September 2026](https://dev.to/vijay_vinoth_8e7abfd3f5b5/open-source-ai-whats-new-in-september-2026-2bah)），但另有资料仅将其描述为仍在演进的 v3 结构规范（[大模型量化从0到1(八)](https://blog.csdn.net/weixin_49520696/article/details/162737098)），两处口径存在冲突。同时欧盟 AI Act 的「开源豁免」条款等监管因素也在影响开源工具的合规边界（[Open Source AI: What's New in September 2026](https://dev.to/vijay_vinoth_8e7abfd3f5b5/open-source-ai-whats-new-in-september-2026-2bah)）。

**开源权重的治理与再分发争议**：开放权重一旦量化、镜像到多个账户/格式/注册表后即难以被上游移除，这既降低了部署门槛，也引发对滥用治理与责任归属的讨论（[Uncensored Open-weight Models](https://arxiv.org/html/2609.05241v1)）。

## 参考来源

- [LLM inference engine](https://aiwiki.ai/wiki/inference_engine)
- [Blog · Ollama](https://ollama.com/blog)
- [llama.cpp и GGUF в 2026](https://aisrc.ru/local-ai/llama-cpp-gguf)
- [Ollama vs LM Studio 2026: Ollama Wins for Devs](https://dev.to/shaam_ai/ollama-vs-lm-studio-2026-ollama-wins-for-devs-p3l)
- [Changelog · LM Studio](https://lmstudio.ai/changelog/lmstudio)
- [The Complete Guide to Local LLM Inference Tools in July 2026: llama.cpp, Ollama, vLLM, SGLang, and Beyond](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)
- [Local LLM Inference in 2026: The Complete Guide to Tools, Hardware & Open-Weight Models](https://blog.starmorph.com/blog/local-llm-inference-tools-guide)
- [Open Source AI: What's New in September 2026](https://dev.to/vijay_vinoth_8e7abfd3f5b5/open-source-ai-whats-new-in-september-2026-2bah)
- [大模型量化从0到1(八): GGUF 格式彻底解剖](https://blog.csdn.net/weixin_49520696/article/details/162737098)
- [Which Quantization Should I Use? A Unified Evaluation of llama.cpp Quantization on Llama-3.1-8B-Instruct](https://arxiv.org/html/2601.14277)
- [What is llama.cpp? — AMD ROCm docs](https://rocm.docs.amd.com/projects/llama-cpp/en/docs-25.08/what-is-llama-cpp.html)
- [vLLM](https://docs.vllm.ai/en/latest/index.html)
- [vLLM Getting Started](https://docs.vllm.ai/_/downloads/en/v0.5.2/pdf/)
- [Supported Models (vLLM)](https://docs.vllm.ai/en/latest/models/supported_models/)
- [Using Docker (vLLM)](https://docs.vllm.ai/en/latest/deployment/docker/)
- [GPTQModel (vLLM)](https://docs.vllm.ai/en/latest/features/quantization/gptqmodel/)
- [FP8 W8A8 (vLLM)](https://docs.vllm.ai/en/latest/features/quantization/llm_compressor/fp8/)
- [Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell (Part I)](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)
- [Announcing vllm-metal: Concurrent Serving on Apple Silicon](https://vllm-project.github.io/2026/09/22/vllm-metal-v0-28-0.html)
- [LLM Inference with SGLang (NVIDIA)](https://build.nvidia.com/station/sglang-inference/overview)
- [Efficiently Programming Large Language Models using SGLang (RadixAttention)](https://arxiv.org/pdf/2312.07104v1.pdf)
- [Serving GLM5.2 NVFP4 Agentic Workload with SGLang](https://www.lmsys.org/blog/2026-07-13-glm52-optimization/)
- [Rebuilding Agentic AI from First Principles for AMD GPU](https://www.amd.com/en/developer/resources/technical-articles/2026/rebuilding-agentic-ai-for-amd-gpu.html)
- [Mellum2 Instruct — MXFP4_MOE (Ollama)](https://ollama.com/JetBrains/mellum2-instruct-mxfp4_moe:latest)
- [Hugging Face Unveils Transformers 2.0, Adding 200 Models and 30 Languages](https://dev.to/techpulse01239/hugging-face-unveils-transformers-20-adding-200-models-and-30-languages-4ep4)
- [Open-weight LLM releases](https://www.llm-releases.com/open-weight-models)
- [Uncensored Open-weight Models: Redistribution as the Persistence Layer](https://arxiv.org/html/2609.05241v1)
- [MLflow - Open Source AI Platform for Agents, LLMs & Models](https://mlflow.org/)