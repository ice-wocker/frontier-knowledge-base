# 推理优化与服务：从 PagedAttention 到分离式部署

> 最后更新：2026-09-26 ｜ 领域：AI·训练与推理工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

大语言模型推理服务（LLM Serving）的目标是在给定 GPU 预算下同时优化两个相互制约的指标：**吞吐量（throughput，tokens/s）**与**时延（latency，TTFT / TPOT）**。推理过程分为两个阶段——**prefill**（并行处理全部输入 token，计算密集）与 **decode**（逐 token 自回归生成，显存带宽密集）。两阶段的资源瓶颈不同，因此现代服务栈的优化路径也分为两条：面向 prefill 的批处理与算子效率优化，面向 decode 的 KV cache 管理与调度优化。

2023 年 vLLM 提出的 PagedAttention 是这一领域的转折点：它借鉴操作系统虚拟内存分页思想，以块（block）级别管理 KV cache，实现"近乎零浪费"的显存占用，并配合抢占式请求调度（[Efficient Memory Management for Large Language Model Serving with Paged Attention](https://export.arxiv.org/pdf/2309.06180v1)）。此后连续批处理（continuous batching）、chunked prefill、前缀缓存（prefix caching）、投机解码（speculative decoding）与 prefill/decode 分离部署（PD disaggregation）逐步成为标配。

## 最新进展（2025–2026）

**vLLM 进入 V1 引擎时代并持续重构执行核心。** 官方博客介绍了 Model Runner V2，用模块化模型逻辑、GPU 原生输入准备、稳定的持久化批处理与异步优先调度重写执行核心，同时保持 API 不变（[vLLM Blog](https://vllm.ai/blog)）。2026 年 9 月，vLLM 推出 vllm-metal，把分页、连续批处理的服务栈带到 Apple Silicon，宣称在并发 agent 负载下 TTFT 更平稳，支持批量 MTP 与 M5 prefill 加速；其实现保留 V1 的统一模型 step，将每个被调度 query token 打包为 `[total_q, H, D]` 并用 `cu_seqlens` 标记请求边界，在单次前向中完成混合 prefill/decode（[Announcing vllm-metal: Concurrent Serving on Apple Silicon](https://vllm-project.github.io/2026/09/22/vllm-metal-v0-28-0.html)）。

**分离式部署（PD Disaggregation）成为高吞吐场景主流。** 其动机是可以对 TTFT 与 ITL 分别调优，例如给 prefill 实例分配 TP、给 decode 实例分配 PP，互不干扰（[Disaggregated Prefilling (experimental)](https://docs.vllm.ai/en/stable/features/disagg_prefill/)）。在 Kimi K3 的 Day-0 支持中，vLLM 使用跨节点专家并行加数据并行，并以 PD 分离把 prefill 密集与 decode 密集负载放到不同副本；一个已验证拓扑是 TEP8 prefill 对 DEP16 decode，KV 传输使用 NIXL（[Kimi K3 Is Here: Efficient Day-0 Support on vLLM](https://vllm-project.github.io/2026/07/27/k3.html)）。该能力也被扩展到混合 SSM-attention 模型（如 Qwen3.5 的 Gated Delta Network 层），需要双描述符视图与逻辑—物理块映射来处理异构缓存布局（[vLLM Reaches 25K Total TPS/GPU on Qwen3.5](https://vllm.ai/blog/2026-08-06-qwen35-25k-tps)、[Disaggregated Serving for Hybrid SSM Models in vLLM](https://vllm.ai/blog)）。在 GB300 NVL72 集群上对 Qwen3.8-2.4T 做 PD 服务，vLLM 报告高吞吐场景下每 GPU 合计 5000 token/s 吞吐，低时延场景下每用户 180 个生成 token（[PD Serving of Qwen3.8-2.4T](https://vllm.ai/blog/2026-09-21-qwen38-pd-serving)）。

**PD 分离的工程细节向异构缓存延伸。** 对 Kimi K3 的优化总结指出，PD 分离与缓存 offload 需要同时传输 MLA KV 与 KDA 状态：MLA KV 在 TP rank 间被复制，而 KDA 状态按 head 与维度分片，Mamba 的 `align` block table 还可能稀疏且可变，因此"纯注意力"的传输假设不再适用（[Kimi K3 Performance Optimizations in vLLM: The Road to 2.8× Throughput](https://vllm.ai/blog/2026-09-13-kimi-k3-performance-optimization)）。在 AMD Instinct MI355X 上优化 MiniMax M3 的案例中，vLLM 通过把共享专家并入路由专家表、由 grouped GEMM 统一处理，去除了额外 launch 与中间流量，使输出吞吐在并发 1 时提升 30.2%、并发 128 时提升 5.6%（[Following the Bottleneck: Optimizing MiniMax M3 on AMD Instinct MI355X](https://vllm-project.github.io/2026/09/10/minimax-m3-mi355x.html)）。

**SGLang 以 RadixAttention 主打缓存复用，并向路由与多后端扩展。** SGLang 论文提出 RadixAttention，用基数树自动共享前缀，并称其吞吐比当时最接近的竞品高 4.4 倍（[Efficiently Programming Large Language Models using SGLang](https://arxiv.org/pdf/2312.07104v1)）。官方文档列出的核心能力包括 RadixAttention 前缀缓存、零开销 CPU 调度器、PD 分离、投机解码、连续批处理、paged attention、张量/流水/专家/数据并行、结构化输出、chunked prefill 与 FP4/FP8/INT4/AWQ/GPTQ 量化（[SGLang Documentation](https://sgl-project.github.io/)）。在路由层，llm-d Router 不再使用轮询，而是按前缀缓存局部性与当前负载对每个副本打分，把请求路由到最可能已持有其前缀的副本，以提升多轮与共享前缀负载下的 RadixAttention 命中率（[SGLang: llm-d](https://docs.sglang.io/docs/advanced_features/llm-d.md)）。面向 TPU 的 SGLang-JAX 支持 EAGLE/EAGLE3 投机解码，官方称可为兼容模型带来 20%–40% 吞吐提升且不影响输出质量（[SGLang TPU Documentation](https://docs.sglang.io/docs/hardware-platforms/tpu)）。

## 核心技术与关键概念

- **连续批处理 / iteration-level scheduling**：调度粒度从"整批"下沉到"单步 decode"。每一步检查请求队列，请求结束即释放 KV 块并在下一步插入新请求，消除静态批处理中的空槽浪费（[LLM Serving Optimization: Continuous Batching, PagedAttention, and Chunked Prefill](https://www.spheron.network/blog/llm-serving-optimization-continuous-batching-paged-attention/)）。
- **Chunked prefill**：把长 prompt 切成多个 chunk 与 decode 混合执行，平滑显存峰值并降低长请求对短请求的队头阻塞。
- **前缀缓存（prefix caching）**：对共享的系统提示或历史轮次复用已算好的 KV。SGLang v0.4.0 的前缀缓存在五轮对话上把首 token 时延从 210ms 降到 56ms（p50，单卡 A100），约 73%（[Best SGLang Production Practices](https://markaicode.com/best/best-sglang-production-practices/)）。
- **投机解码（speculative decoding）**：小模型起草、大模型单次前向验证多个候选 token，数学上保持与目标模型一致的输出分布。EAGLE-3 类方案在实测中给出约 2.1×–3.2× 加速且被描述为无损（[Self-Hosting vLLM on Cloud GPUs in 2026](https://dev.to/shubhanshu_shrimali/how-i-self-host-vllm-on-cloud-gpus-for-sub-180ms-inference-and-saved-45-on-costs-4cm5)）。研究侧，CARD 通过"查询—纠正"范式与缓存辅助实现最高 4.83× 加速，并相对 EAGLE-3 把目标模型计算量降低 6.86×，且无需微调起草或目标模型（[CARD: A Cache-Assisted Parallel Speculative Decoding Framework](https://arxiv.org/pdf/2508.04462v2)）；SpecExtend 则针对长序列场景，用跨模型检索（CMR）按目标模型注意力分数裁剪起草模型的 KV cache（[SpecExtend: A Drop-in Enhancement for Speculative Decoding of Long Sequences](https://arxiv.org/html/2505.20776v3)）。
- **关键指标定义**：TTFT 为请求发出到首个输出 token 的典型耗时；TPOT 为首 token 之后每 token 的典型耗时，ITL 为相邻 token 完成之间的典型时延，二者均忽略 TTFT（[Run benchmarking with trtllm-serve](https://nvidia.github.io/TensorRT-LLM/latest/commands/trtllm-serve/run-benchmark-with-trtllm-serve.html)）。
- **KV 传输与缓存卸载**：PD 分离通过 NIXL 等通道传输 KV；对混合架构还需额外传输 SSM/线性注意力状态，并处理 Mamba block table 的可变与稀疏问题（[Kimi K3 Performance Optimizations in vLLM](https://vllm.ai/blog/2026-09-13-kimi-k3-performance-optimization)）。

## 代表性项目 / 公司 / 产品

- **vLLM**：PagedAttention 与 V1 引擎，支持分布式、PD 分离、前缀缓存；官方提供 `vllm serve` 服务入口与基准脚本。
- **SGLang**：Berkeley LMSYS 团队出品，RadixAttention + 结构化输出（structured decoding），在高并发与多轮对话场景口碑突出；提供 `docs.sglang.io` 官方文档与多硬件后端。
- **TensorRT-LLM**：NVIDIA 官方推理栈，原生 FP8/FP4 与 Blackwell 优化，提供 `trtllm-serve` 与完整 benchmark 工具（[Overview — TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)）。
- **TGI / LMDeploy**：HF Text Generation Inference 与 LMDeploy（TurboMind C++ 内核）为其他主流选择。
- **llm-d Router**：基于前缀缓存感知的路由层，常与 SGLang 搭配（[SGLang: llm-d](https://docs.sglang.io/docs/advanced_features/llm-d.md)）。

## 关键数据与评测结果

不同引擎的对比较少呈"单点领先、非普适倍数"的特征。某 2026 年对比文章给出 H100 上 Llama 3.1 8B 的吞吐参考值：vLLM 约 12,500 tok/s，SGLang 约 16,200 tok/s，LMDeploy 约 16,100 tok/s，并称 SGLang 在多轮场景快 10%–20%（[vLLM vs SGLang vs LMDeploy: Fastest LLM Inference Engine in 2026?](https://dev.to/jaipalsingh/vllm-vs-sglang-vs-lmdeploy-fastest-llm-inference-engine-in-2026-5h04)）。另一来源指出，在单卡 H100 离线批推理 Llama 3.1 8B-Instruct、且 vLLM 0.11.0 显式启用 FlashInfer 后端的特定场景，AIMultiple 测得 SGLang 与 LMDeploy 领先约 29%，强调这是可复现的场景化数字而非普适倍数（[SGLang vs vLLM: Llama 3.1 8B H100 Throughput (2026)](https://markaicode.com/benchmarks/sglang-llama-31-h100-throughput-benchmark/)）。

**时延基准的一个实例。** AWS 在 SageMaker AI 的 G7 实例上对小型 LLM 的基准显示，中位 TTFT 约 118 ms（P99 为 286 ms），ITL 约 8.9 ms，输出吞吐约 408 tok/s（[Benchmarking small LLM inference on SageMaker AI: G7 vs G5 and G6](https://aws.amazon.com/blogs/machine-learning/benchmarking-small-llm-inference-on-sagemaker-ai-g7-vs-g5-and-g6/)）。在一份自托管网关对比中，Ollama 在单用户 TTFT 上约 45 ms、快于 vLLM 的约 82 ms，但默认配置下吞吐约 41 tok/s、P99 约 673 ms，明显低于同硬件的 vLLM（[Production Self-Hosted LLM Gateway: LiteLLM vs Ollama vs vLLM vs LocalAI (2026)](https://dev.to/devrudals/production-self-hosted-llm-gateway-litellm-vs-ollama-vs-vllm-vs-localai-2026-benchmark-tco--1bg5)）。

**成本侧**，NVIDIA 引用 SemiAnalysis InferenceX（截至 2026 年 4 月）称，Blackwell B200 在 GPT-OSS-120B 上配合最新 TensorRT-LLM 可达每 GPU 最高 60,000 token/s，约为 H200 的 4 倍，对应约 0.02 美元/百万 token（[NVIDIA Data Center Deep Learning Product Performance](https://developer.nvidia.com/deep-learning-performance-training-inference)）。一份 2026 年 TCO 分析给出更细口径：B200 NVL 上 70B 模型的输出成本约 0.14 美元/百万 token，H100 SXM5 约 0.78 美元/百万 token（约 5.6× 差距）；其表中 H100 SXM5 为 80GB/3.35 TB/s、700W、2.65 美元/小时，TTFT（4K prompt）约 182 ms、TPOT 约 28.5 ms（[AI Inference & Hardware Economics: 2026 Statistics & TCO Index](https://dev.to/abhishek_raajmishra_b2f2/ai-inference-hardware-economics-2026-statistics-tco-index-3idj)）。API 侧，某 2026 年速度对比列出 o3-mini 的 TTFT 约 350 ms、约 25 tok/s、输入 1.10 美元/百万 token，Claude Opus 4 约 500 ms、50 tok/s、5.00 美元/百万 token 等（[LLM Speed Comparison 2026](https://llmversus.com/llm/speed)）。中文市场方面，有报道称某厂商高峰时段每百万 token 缓存未命中输入为 2 元、输出 8 元，非高峰减半，并引述预测 2026 年下半年低端 API 价格约为每百万 token 0.1–0.2 美元（[大模型价格战持续升温](http://m.toutiao.com/group/7689773875676135971/)）。

跨硬件方面，有中文媒体报道称在 TPU 上运行 Kimi 并使用 DeepSeek 的推理框架，投机解码接受长度达到 6（每轮平均 6 个 token 通过验证），单步 decode 约 8.5ms；batch size 为 1 时 TPU 约 249 tok/s，GB200 约 127 tok/s（[谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)）。该口径为单一媒体报道，需谨慎对待。

## 趋势与争议

1. **架构趋同**：vLLM 与 SGLang 都在补齐对方的能力（vLLM 加入自动前缀缓存，SGLang 强化调度与并行），"谁更快"越来越取决于具体工作负载（长 prompt / 多轮 / 高并发 / 长输出）而非引擎本身。
2. **PD 分离的复杂度代价**：分离式部署提升 goodput 与可预测性，但引入 KV 传输网络开销、额外的故障域与运维复杂度，且对 SSM 混合架构需要处理异构缓存布局（MLA KV 复制、KDA 状态分片、Mamba block table 稀疏可变）。
3. **指标口径不统一**：吞吐是否包含 prefill、是否固定输出长度、是否开启前缀缓存，都会显著改变结论，跨来源数字不可直接比较。
4. **投机解码的非普遍收益**：在高 batch 的吞吐优先场景，验证开销可能超过收益；其价值主要体现在低 batch、低时延场景。不同实现给出的加速（2.1×–3.2×、CARD 的 4.83×、SGLang-JAX 的 20%–40%）分属不同模型与硬件，不可直接横比。
5. **成本数字的来源分层**：厂商官方（如 NVIDIA 引用的 InferenceX）与第三方 TCO 分析给出的美元/百万 token 口径不同（是否含 prefill、是否按吞吐峰值、是否含折旧），并列呈现而不合并结论。

## 参考来源

1. [Efficient Memory Management for Large Language Model Serving with Paged Attention](https://export.arxiv.org/pdf/2309.06180v1)
2. [vLLM Blog](https://vllm.ai/blog)
3. [Announcing vllm-metal: Concurrent Serving on Apple Silicon](https://vllm-project.github.io/2026/09/22/vllm-metal-v0-28-0.html)
4. [Disaggregated Prefilling (experimental) — vLLM Docs](https://docs.vllm.ai/en/stable/features/disagg_prefill/)
5. [Kimi K3 Is Here: Efficient Day-0 Support on vLLM](https://vllm-project.github.io/2026/07/27/k3.html)
6. [vLLM Reaches 25K Total TPS/GPU on Qwen3.5](https://vllm.ai/blog/2026-08-06-qwen35-25k-tps)
7. [PD Serving of Qwen3.8-2.4T](https://vllm.ai/blog/2026-09-21-qwen38-pd-serving)
8. [Efficiently Programming Large Language Models using SGLang](https://arxiv.org/pdf/2312.07104v1)
9. [When to Choose SGLang Over vLLM: Multi-Turn Conversations and KV Cache Reuse](https://www.runpod.io/blog/sglang-vs-vllm-kv-cache)
10. [LLM Serving Optimization: Continuous Batching, PagedAttention, and Chunked Prefill](https://www.spheron.network/blog/llm-serving-optimization-continuous-batching-paged-attention/)
11. [Best SGLang Production Practices: 4 Configs That Cut Latency by 60%](https://markaicode.com/best/best-sglang-production-practices/)
12. [CARD: A Cache-Assisted Parallel Speculative Decoding Framework](https://arxiv.org/pdf/2508.04462v2)
13. [SpecExtend: A Drop-in Enhancement for Speculative Decoding of Long Sequences](https://arxiv.org/html/2505.20776v3)
14. [Self-Hosting vLLM on Cloud GPUs in 2026](https://dev.to/shubhanshu_shrimali/how-i-self-host-vllm-on-cloud-gpus-for-sub-180ms-inference-and-saved-45-on-costs-4cm5)
15. [Run benchmarking with trtllm-serve](https://nvidia.github.io/TensorRT-LLM/latest/commands/trtllm-serve/run-benchmark-with-trtllm-serve.html)
16. [Overview — TensorRT-LLM Performance](https://nvidia.github.io/TensorRT-LLM/latest/developer-guide/perf-overview.html)
17. [vLLM vs SGLang vs LMDeploy: Fastest LLM Inference Engine in 2026?](https://dev.to/jaipalsingh/vllm-vs-sglang-vs-lmdeploy-fastest-llm-inference-engine-in-2026-5h04)
18. [SGLang vs vLLM: Llama 3.1 8B H100 Throughput (2026)](https://markaicode.com/benchmarks/sglang-llama-31-h100-throughput-benchmark/)
19. [NVIDIA Data Center Deep Learning Product Performance](https://developer.nvidia.com/deep-learning-performance-training-inference)
20. [谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)
21. [SGLang Documentation (SGLang Project)](https://sgl-project.github.io/)
22. [SGLang: llm-d Integration](https://docs.sglang.io/docs/advanced_features/llm-d.md)
23. [SGLang TPU Documentation](https://docs.sglang.io/docs/hardware-platforms/tpu)
24. [Kimi K3 Performance Optimizations in vLLM: The Road to 2.8× Throughput](https://vllm.ai/blog/2026-09-13-kimi-k3-performance-optimization)
25. [Following the Bottleneck: Optimizing MiniMax M3 on AMD Instinct MI355X](https://vllm-project.github.io/2026/09/10/minimax-m3-mi355x.html)
26. [AI Inference & Hardware Economics: 2026 Statistics & TCO Index](https://dev.to/abhishek_raajmishra_b2f2/ai-inference-hardware-economics-2026-statistics-tco-index-3idj)
27. [LLM Speed Comparison 2026](https://llmversus.com/llm/speed)
28. [Benchmarking small LLM inference on SageMaker AI: G7 vs G5 and G6](https://aws.amazon.com/blogs/machine-learning/benchmarking-small-llm-inference-on-sagemaker-ai-g7-vs-g5-and-g6/)
29. [Production Self-Hosted LLM Gateway: LiteLLM vs Ollama vs vLLM vs LocalAI (2026 Benchmark, TCO & Deployment Blueprint)](https://dev.to/devrudals/production-self-hosted-llm-gateway-litellm-vs-ollama-vs-vllm-vs-localai-2026-benchmark-tco--1bg5)
30. [大模型价格战持续升温，智谱市值跌至3000亿港元](http://m.toutiao.com/group/7689773875676135971/)