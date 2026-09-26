# AI 基础设施与算力

> 最后更新：2026-09-26 ｜ 领域：人工智能·基础设施与算力 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI 基础设施是前沿模型的物理底座，涵盖超大规模训练集群、GPU/TPU 互联网络、训练与推理软件栈、模型架构效率技术（MoE、量化、KV cache 优化）、以及数据中心的电力与散热。2025–2026 年，随着旗舰模型训练规模迈入"十万卡级"，基础设施的主旋律从"堆算力"转向"每瓦性能"与"每 token 成本"：一方面互联带宽、液冷与供电成为集群扩展的硬约束；另一方面推理侧通过 MoE 稀疏化、低精度量化与 KV cache 优化，把单位 token 成本压到历史最低。

## 2025–2026 最新进展

**十万卡级训练集群落地。** xAI 的 Memphis Colossus 集群以 100,000 块 NVIDIA H100 GPU 起步，用 122 天建成，随后又在 92 天内翻倍到 200,000 块，供电规模约 250 MW，网络采用 Spectrum-X 以太网（[xAI's Memphis Colossus: Anatomie eines 100.000-GPU-Supercomputers](https://introl.com/de/blog/xai-memphis-colossus-100000-gpu-supercomputer-infrastructure)）。据 NVIDIA CEO 黄仁勋 2026 年 9 月 6 日透露，GPT-6 Astra 的训练动用了约 10 万块 Grace Blackwell 系列 GPU，并计划再投入 40 万块用于后续阶段（[GPT-6 Astra : 100 000 GPU Nvidia pour entraîner le modèle](https://overclocking.com/gpt-6-astra-100000-gpu-nvidia-prix-ram/)）。中国方面，2026 年 7 月 10 日中科曙光宣布首个全国产十万卡 AI 超集群"曙光 8000（登峰）"落成并接入国家超算互联网，标志算力基础设施从万卡级迈向十万卡级部署（[全国产十万卡AI超集群落成并接入国家超算互联网](https://tech.gmw.cn/2026-07/10/content_38879178.htm)）。

**互联网络进入 260 TB/s 机架时代。** NVIDIA 的第六代 NVLink 为每个 GPU 提供 3.6 TB/s 带宽，单个 Vera Rubin NVL72 机架总带宽达 260 TB/s，支持大规模 MoE 与长上下文负载；其 scale-up 域可扩展至 1152 块 GPU，并引入共封装光学（co-packaged optics）（[NVIDIA NVLink: The Scale-Up Network for AI Factories](https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories)、[NVIDIA Vera Rubin](https://blogs.nvidia.com/blog/vera-rubin/)）。scale-out 侧，Spectrum-X 以太网以 Spectrum-6 102.4T 交换机、1.6T ConnectX-9 SuperNIC 与自适应路由构成（[NVIDIA Vera Rubin](https://blogs.nvidia.com/blog/vera-rubin/)）。NVLink 6 还增加了控制面弹性、部分填充机架运行与热插拔等可靠性特性（[NVIDIA NVLink and NVLink Switch](https://www.nvidia.com/en-sg/data-center/nvlink/)）。基于 Rubin 的 DGX SuperPOD 也沿用了同样的互联指标（[NVIDIA DGX SuperPOD](https://blogs.nvidia.cn/blog/dgx-superpod-rubin/)）。

**自研加速器规模化。** Google 第七代 TPU "Ironwood"（TPU7x）每个 pod 集成 9,216 块液冷芯片，提供 42.5 ExaFlops，单芯片性能是上一代 Trillium 的约 4 倍，已普遍可用（[Tensor Processing Units](https://cloud.google.com/tpu)）。AWS 的第四代 AI 芯片 Trainium3（首款 3nm AWS AI 芯片）驱动 EC2 Trn3 UltraServers，每芯片提供 2.52 PFLOPs FP8 算力，内存容量比前代提升 1.5 倍（[Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)）。一项对比测试显示，16 块 TPU v7 Ironwood 对 16 块 NVIDIA GB200 运行 Kimi K3，双方均用 vLLM，TPU 达到 709 token/s、GB200 为 452 token/s，前者快约 57%（[谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)）。

## 核心技术与关键概念

**MoE（混合专家）架构。** MoE 由专家子网络、专家稀疏性、门控网络与输出组合四要素构成，每 token 只激活少量专家，从而在控制算力的同时扩大总参数量（[What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)）。该领域的系统性问题包括 Top-k 路由、共享专家、细粒度专家、token 分发、设备放置、all-to-all 通信与计算-通信重叠等，与光互连带宽直接耦合（[The Evolution of Mixture-of-Experts Architectures in Large Language Models](https://arxiv.org/pdf/2608.08650)）。在万卡级 MoE 训练中，Megatron Core 等框架专门处理专家并行与负载均衡（[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/html/2603.07685v2)）。

**训练框架与并行策略。** PyTorch 仍是绝对主流，90% 以上已发表的大模型（Llama、Mistral、GPT 等）使用 PyTorch，生态成熟度领先 3–5 年；JAX 的 `pjit` 分片在大规模下是真实优势，但"JAX 在规模上更快"并非保证（[PyTorch vs JAX: Which Framework Wins Multi-Node GPU Training](https://markaicode.com/vs/pytorch-vs-jax/)、[PyTorch vs JAX: which deep learning framework should you choose?](https://theneuralbase.com/compare/pytorch-vs-jax/)）。工程实践中，8–100+ GPU 规模常采用 Megatron-LM 的 TP+PP+DP（三维并行），TPU 侧则用 JAX + Flax 的 pmap/mesh（[Frameworks de Treinamento Distribuído](https://compendium.koder.dev/ia/08-referencia/07-frameworks/treinamento-distribuido/)）。

**推理框架三强。** TensorRT-LLM 在 H100 上的稠密模型吞吐较 vLLM 高 15%–25%，但需编译；vLLM 部署最简、支持 400+ 模型架构与最广硬件；SGLang 凭借 RadixAttention 与专家并行（EP），在大 MoE（如 DeepSeek-R1/V3）与高并发场景表现最佳（[vLLM vs SGLang vs TensorRT-LLM](https://inferenceengineering.tech/learn/vllm-vs-sglang-vs-tensorrt-llm/)）。具体到 Llama 3.3 70B FP8 单卡 H100，TensorRT-LLM 单请求高约 8%、50 并发高约 13%，代价是近半小时的编译（[TensorRT-LLM vs vLLM vs SGLang: H100 Benchmark 2026](https://markaicode.com/benchmarks/cuda-llama-33-h100-throughput-benchmark/)）。vLLM 在 Qwen3.5 上实现了每 GPU 25,000 token/s 的总吞吐（[vLLM Reaches 25K Total TPS/GPU on Qwen3.5](https://vllm.ai/blog/2026-08-06-qwen35-25k-tps)），并通过 WideEP 与 NVFP4 GEMM 等针对 Blackwell 的精度优化持续提升大 MoE 服务能力（[Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)）。

**KV cache 优化与量化。** KV cache 量化是长上下文与高并发的关键：FP8/INT8 可把显存减半，INT4 进一步压缩但可能引入质量损失（[KV Cache & PagedAttention Complete Guide (2026)](https://localaimaster.com/blog/kv-cache-paged-attention-guide)）。NVIDIA 的 NVFP4 KV cache 相较 FP8 可将显存占用再降约 50%，但需要 Blackwell 硬件（[使用 NVFP4 KV 缓存优化大批次与长上下文推理](https://developer.nvidia.cn/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/)）。面向 context-heavy agent，UltraQuant 以 4-bit KV 缓存在生产级 Claude Code 轨迹回放上实现 2.71×（MiniMax-M2.5）至 4.38×（Qwen3 系列）的吞吐提升（[UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/html/2606.20474)）。

**蒸馏**：通过把大模型的推理/能力迁移到小模型，配合量化压缩部署成本，是推理降本的重要一环（[Inference-Time Distillation](https://arxiv.org/html/2512.02543v2)）。

## 代表性项目/产品（带官方链接）

- NVIDIA NVLink / Spectrum-X：https://www.nvidia.com/en-sg/data-center/nvlink/
- NVIDIA Vera Rubin 平台：https://blogs.nvidia.com/blog/vera-rubin/
- Google TPU（Ironwood）：https://cloud.google.com/tpu
- AWS Trainium：https://aws.amazon.com/ai/machine-learning/trainium/
- vLLM：https://vllm.ai/blog/2026-08-06-qwen35-25k-tps
- NVIDIA 推理平台（TensorRT-LLM / Dynamo）：https://www.nvidia.com/en-gb/solutions/ai/inference/

## 关键数据与评测结果

- **推理成本持续下探**：BenchLM Token Price Index 显示，截至 2026 年 9 月，前沿 LLM token 价格较 2023 年 3 月低约 84%（指数 16，基准 100）（[LLM Pricing Statistics (2026)](https://benchlm.ai/stats/llm-pricing)）。据数据服务商 Silicon Data，其按使用量加权的大模型 token 支出指数首次跌破每百万 token 1 美元，报 0.97 美元（[新浪财经](https://finance.sina.com.cn/roll/2026-09-03/doc-iniqpqxy7000038.shtml.md)）。
- **单位 token 成本**：据 SemiAnalysis InferenceX（2026 年 4 月），GB300 NVL72 在 116 TPS/user 交互性下可达每百万 token $0.123；NVIDIA B200 在 GPT-OSS-120B 上达到每百万 token 两美分的生产基准（[NVIDIA Inference Platform](https://www.nvidia.com/en-gb/solutions/ai/inference/)、[cloud accelerator pricing](https://perspectives.nvidia.com/cloud-accelerator-pricing-llm-inference-scale-2026)）。
- **液冷渗透率**：TrendForce 预测 AI 芯片的液冷渗透率 2026 年将达 53%（2025 年为 33%），并进一步升至 59%（[AI Data Center Liquid Cooling Adoption to Hit 53% in 2026](https://infotechlead.com/data-center/ai-data-center-liquid-cooling-adoption-to-hit-53-in-2026-as-nvidia-amd-google-drive-demand-97794)）。浸没式相变液冷可支持 150 kW/机架以上的功率密度；冷板式可捕获服务器约 80% 的热量（[Why Liquid Cooling is No Longer Optional for 2026 AI Workloads](https://inveniatech.com/data-center/why-liquid-cooling-is-no-longer-optional-for-2026-ai-workloads/)）。
- **液冷市场**：赛迪顾问数据显示，2025 年中国液冷数据中心市场规模达 159.8 亿元、同比增长 45.2%，预计 2026 年达 232.5 亿元；中金公司预测 2026 年全球智算中心液冷市场规模有望突破 1147 亿元、同比增长 273%（[算力火爆带热液冷赛道](http://finance.people.com.cn/n1/2026/0921/c1004-40802433.html)）。浸没式液冷可将机房 PUE 压至约 1.04，综合节电 15%–20%（[从一块芯片到一座机房](http://m.toutiao.com/group/7689727179181146675/)）。
- **云厂商资本开支**：2026 年 Alphabet 指引 1950–2050 亿美元，Microsoft 约 1900 亿美元，Meta 1250–1450 亿美元（[Hyperscaler](https://aiwiki.ai/wiki/hyperscaler/edit)）。四大云厂商 2026 年 AI capex 合计预计约 7000 亿美元，较 2025 年增长 60%–70%（[Reshaping the Nasdaq-100](https://www.nasdaq.com/docs/global-indexes/ndx-quarterly-macro-research-ai-capex)）。

## 趋势与争议

**电力与电网成为新瓶颈。** 高密度 AI 机架要求协调可用电网电力、设施设计、部署周期与长期运营效率；液冷之所以成为主流答案，是因为它能让人在有限电力下"榨出"更多算力（[Data center power density](https://blog.se.com/datacenter/2026/07/28/data-center-power-density-planning-liquid-cooled-ai-data-centers-around-grid-and-power-constraints/)）。

**资本开支的可持续性争议。** 有测算指出，大型科技公司已把约 96% 的现金流投入资本开支，长期债务合计升至约 3419 亿美元（Alphabet 982 亿、Amazon 1289 亿、Meta 837 亿、Microsoft 311 亿）（[AI Capex 2026: Big Tech Now Spends 96% of Its Cash Flow](https://www.simianx.ai/stories/ai-capex-2026-big-tech-now-spends-96-of-its-cash-flow)）。一旦 AI 需求放缓，约 7000 亿美元 capex 的回报节奏将受到审视（[What an AI slowdown does to $700 billion in AI capex](https://financetracked.com/ai-capex-slowdown)）。

**互联路线的分化。** NVLink 代表封闭但高带宽的 scale-up 路线（并借 NVLink Fusion 向半定制开放），以太网阵营（Spectrum-X、Ultra Ethernet）则在 scale-out 上争夺开放生态（[NVIDIA Vera Rubin](https://blogs.nvidia.com/blog/vera-rubin/)）。同时，自研加速器（TPU Ironwood、Trainium3）在特定负载上对通用 GPU 形成价格/能效竞争（[Tensor Processing Units](https://cloud.google.com/tpu)、[Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)）。

## 参考来源

1. [xAI's Memphis Colossus: Anatomie eines 100.000-GPU-Supercomputers](https://introl.com/de/blog/xai-memphis-colossus-100000-gpu-supercomputer-infrastructure)
2. [GPT-6 Astra : 100 000 GPU Nvidia pour entraîner le modèle](https://overclocking.com/gpt-6-astra-100000-gpu-nvidia-prix-ram/)
3. [全国产十万卡AI超集群落成并接入国家超算互联网](https://tech.gmw.cn/2026-07/10/content_38879178.htm)
4. [NVIDIA NVLink: The Scale-Up Network for AI Factories](https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories)
5. [NVIDIA Vera Rubin](https://blogs.nvidia.com/blog/vera-rubin/)
6. [NVIDIA NVLink and NVLink Switch](https://www.nvidia.com/en-sg/data-center/nvlink/)
7. [NVIDIA DGX SuperPOD](https://blogs.nvidia.cn/blog/dgx-superpod-rubin/)
8. [Tensor Processing Units](https://cloud.google.com/tpu)
9. [Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)
10. [谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)
11. [What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)
12. [The Evolution of Mixture-of-Experts Architectures in Large Language Models](https://arxiv.org/pdf/2608.08650)
13. [Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/html/2603.07685v2)
14. [PyTorch vs JAX: Which Framework Wins Multi-Node GPU Training](https://markaicode.com/vs/pytorch-vs-jax/)
15. [PyTorch vs JAX: which deep learning framework should you choose?](https://theneuralbase.com/compare/pytorch-vs-jax/)
16. [Frameworks de Treinamento Distribuído](https://compendium.koder.dev/ia/08-referencia/07-frameworks/treinamento-distribuido/)
17. [vLLM vs SGLang vs TensorRT-LLM](https://inferenceengineering.tech/learn/vllm-vs-sglang-vs-tensorrt-llm/)
18. [TensorRT-LLM vs vLLM vs SGLang: H100 Benchmark 2026](https://markaicode.com/benchmarks/cuda-llama-33-h100-throughput-benchmark/)
19. [vLLM Reaches 25K Total TPS/GPU on Qwen3.5](https://vllm.ai/blog/2026-08-06-qwen35-25k-tps)
20. [Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)
21. [KV Cache & PagedAttention Complete Guide (2026)](https://localaimaster.com/blog/kv-cache-paged-attention-guide)
22. [使用 NVFP4 KV 缓存优化大批次与长上下文推理](https://developer.nvidia.cn/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/)
23. [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/html/2606.20474)
24. [Inference-Time Distillation](https://arxiv.org/html/2512.02543v2)
25. [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/)
26. [NVIDIA Inference Platform](https://www.nvidia.com/en-gb/solutions/ai/inference/)
27. [LLM Pricing Statistics (2026)](https://benchlm.ai/stats/llm-pricing)
28. [新浪财经：LLM token 支出指数跌破 1 美元](https://finance.sina.com.cn/roll/2026-09-03/doc-iniqpqxy7000038.shtml.md)
29. [cloud accelerator pricing](https://perspectives.nvidia.com/cloud-accelerator-pricing-llm-inference-scale-2026)
30. [AI Data Center Liquid Cooling Adoption to Hit 53% in 2026](https://infotechlead.com/data-center/ai-data-center-liquid-cooling-adoption-to-hit-53-in-2026-as-nvidia-amd-google-drive-demand-97794)
31. [Why Liquid Cooling is No Longer Optional for 2026 AI Workloads](https://inveniatech.com/data-center/why-liquid-cooling-is-no-longer-optional-for-2026-ai-workloads/)
32. [算力火爆带热液冷赛道](http://finance.people.com.cn/n1/2026/0921/c1004-40802433.html)
33. [从一块芯片到一座机房](http://m.toutiao.com/group/7689727179181146675/)
34. [Hyperscaler](https://aiwiki.ai/wiki/hyperscaler/edit)
35. [Reshaping the Nasdaq-100](https://www.nasdaq.com/docs/global-indexes/ndx-quarterly-macro-research-ai-capex)
36. [Data center power density](https://blog.se.com/datacenter/2026/07/28/data-center-power-density-planning-liquid-cooled-ai-data-centers-around-grid-and-power-constraints/)
37. [AI Capex 2026: Big Tech Now Spends 96% of Its Cash Flow](https://www.simianx.ai/stories/ai-capex-2026-big-tech-now-spends-96-of-its-cash-flow)
38. [What an AI slowdown does to $700 billion in AI capex](https://financetracked.com/ai-capex-slowdown)