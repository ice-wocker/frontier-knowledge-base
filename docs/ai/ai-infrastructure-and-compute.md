# AI 基础设施与算力

> 最后更新：2026-09-26 ｜ 领域：人工智能·基础设施与算力 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI 基础设施是前沿模型的物理底座，涵盖超大规模训练集群、GPU/TPU 互联网络、训练与推理软件栈、模型架构效率技术（MoE、量化、KV cache 优化）、以及数据中心的电力与散热。2025–2026 年，随着旗舰模型训练规模迈入"十万卡级"，基础设施的主旋律从"堆算力"转向"每瓦性能"与"每 token 成本"：一方面互联带宽、液冷与供电成为集群扩展的硬约束；另一方面推理侧通过 MoE 稀疏化、低精度量化与 KV cache 优化，把单位 token 成本压到历史最低。

能源维度上存在多套口径。有统计称全球数据中心用电 2022 年约 340 TWh（约占全球 1.3%）、2024 年约 460 TWh（约 1.7%）、2026 年预计约 620 TWh（约 2.3%）、2030 年或达约 980 TWh（约 3.5%）（[AIデータセンターのエネルギー危機完全解説2026](https://labmemo.com/smr-data-center-energy-ai-explained-2026/)）；而援引 Gartner 2026 年 6 月报告的说法是，2026 年全球数据中心耗电约 565 TWh、同比增长 26%，其中 AI 优化服务器约 175 TWh（同比增 84%）（[AI Data Center Energy Crisis 2026](https://andrew.ooo/answers/ai-data-center-energy-crisis-colossus-stargate-power-july-2026/)）。两套数字差异明显，引用时须注明来源与统计边界。

## 2025–2026 最新进展

**十万卡级训练集群落地。** xAI 的 Memphis Colossus 集群以 100,000 块 NVIDIA H100 GPU 起步，用 122 天建成，随后又在 92 天内翻倍到 200,000 块，供电规模约 250 MW，网络采用 Spectrum-X 以太网（[xAI's Memphis Colossus: Anatomie eines 100.000-GPU-Supercomputers](https://introl.com/de/blog/xai-memphis-colossus-100000-gpu-supercomputer-infrastructure)）。据 NVIDIA CEO 黄仁勋 2026 年 9 月 6 日透露，GPT-6 Astra 的训练动用了约 10 万块 Grace Blackwell 系列 GPU，并计划再投入 40 万块用于后续阶段（[GPT-6 Astra : 100 000 GPU Nvidia pour entraîner le modèle](https://overclocking.com/gpt-6-astra-100000-gpu-nvidia-prix-ram/)）。中国方面，2026 年 7 月 10 日中科曙光宣布首个全国产十万卡 AI 超集群"曙光 8000（登峰）"落成并接入国家超算互联网，标志算力基础设施从万卡级迈向十万卡级部署（[全国产十万卡AI超集群落成并接入国家超算互联网](https://tech.gmw.cn/2026-07/10/content_38879178.htm)）。

**吉瓦级"AI 工厂"与史上最大规模资本开支。** OpenAI 主导的 Stargate 已演变为全球性 AI 基础设施网络：截至 2026 年 9 月 18 日，OpenAI 称已锁定超过 10 GW 算力，并另签约 8 IT-GW 的 PORTS-Pike 协议，但其中大部分容量尚未投入运营（[Stargate Project Tracker](https://www.stargate.how/)）。Oracle 与 OpenAI 的约 3000 亿美元、为期五年的云合同构成 Stargate 核心，预计电力需求达 4.5 GW（[Oracle's $300 Billion OpenAI Gamble](https://www.webanditnews.com/2026/09/15/oracles-300-billion-openai-gamble-the-massive-bet-reshaping-ai-infrastructure/)）。Stargate Nevada 首期约 5 GW 于 2026 年 7 月通电，1A 期资本开支估计 650–750 亿美元，由 SoftBank 与 Oracle 主要出资（[OpenAI's Stargate Nevada Just Went Live](https://datavook.com/post/openai-stargate-nevada-data-center-live-july-2026)）；密歇根 Saline Township 园区投资约 160 亿美元、供电 1.4 GW（[OpenAI Stargate - Saline Township Campus](https://servercountry.org/data/projects/openai-stargate-saline-township-campus/)）。

**HBM4 进入量产，内存带宽再翻倍。** Samsung 称其 HBM4 提供 11.7 Gbps 的稳定处理速度，超过 8 Gbps 行业标准约 46%，较上代 HBM3E 的 9.6 Gbps 提升 1.22 倍，并可增强至 13 Gbps（[Samsung Ships Industry-First Commercial HBM4](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)）。SK hynix 的 HBM4 将 IO 扩展至 2K，实现超过 2.8 TB/s 带宽，采用逻辑代工工艺后能效提升约 40%，并通过 Advanced MR-MUF 实现最高 16 层堆叠（[SK hynix HBM4](https://product.skhynix.com/products/dram/hbm/hbm4.go)）。Micron 的 HBM4 36GB 12H 已进入高量产，专为 NVIDIA Vera Rubin 设计，带宽超 2.8 TB/s、能效提升 20%（[Micron in High-Volume Production of HBM4](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)）；Samsung 并在 NVIDIA GTC 2026 展示面向 Vera Rubin 的 HBM4E（[Samsung Unveils HBM4E at NVIDIA GTC 2026](https://news.samsungsemiconductor.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/)）。

**互联网络进入 260 TB/s 机架时代。** NVIDIA 的第六代 NVLink 为每个 GPU 提供 3.6 TB/s 带宽，单个 Vera Rubin NVL72 机架总带宽达 260 TB/s，支持大规模 MoE 与长上下文负载；其 scale-up 域可扩展至 1152 块 GPU，并引入共封装光学（co-packaged optics）（[NVIDIA NVLink: The Scale-Up Network for AI Factories](https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories)、[NVIDIA Vera Rubin](https://blogs.nvidia.com/blog/vera-rubin/)）。scale-out 侧，Spectrum-X 以太网以 Spectrum-6 102.4T 交换机、1.6T ConnectX-9 SuperNIC 与自适应路由构成（[NVIDIA Vera Rubin](https://blogs.nvidia.com/blog/vera-rubin/)）。NVLink 6 还增加了控制面弹性、部分填充机架运行与热插拔等可靠性特性（[NVIDIA NVLink and NVLink Switch](https://www.nvidia.com/en-sg/data-center/nvlink/)）。基于 Rubin 的 DGX SuperPOD 也沿用了同样的互联指标（[NVIDIA DGX SuperPOD](https://blogs.nvidia.cn/blog/dgx-superpod-rubin/)）。Vera Rubin NVL72 单机架提供最多 3,600 PFLOPS NVFP4 算力、20.7 TB HBM4 与 1.6 PB/s 内存带宽（[How the NVIDIA Vera Rubin Platform is Solving Agentic AI's Scale-Up Problem](https://developer.nvidia.com/blog/how-the-nvidia-vera-rubin-platform-is-solving-agentic-ais-scale-up-problem/)）。

**推理侧走向"解耦 + 异构"。** NVIDIA Rubin CPX 是 Rubin 家族中专为上下文处理（prefill）设计的成员：上下文阶段是计算受限、解码阶段是内存带宽受限，二者解耦后可分别优化，Rubin CPX 负责摄取与处理百万 token 级 prompt，标准 Rubin GPU 负责 decode（[NVIDIA Rubin CPX](https://nvnexus.com/product/nvidia-rubin-cpx/)、[NVIDIA Rubin CPX Accelerates Inference Performance](https://resources.nvidia.com/en-us-inference-infrastructure/nvidia-rubin-cpx-accelerates)）。NVIDIA 与 Groq 相关的 Groq 3 LPX 加速器采用确定性执行模型与编译器调度的芯片间通信，与 Vera Rubin NVL72 组合支持 prefill-decode 解耦、attention-FFN 解耦（AFD）与外部 drafter 投机解码（[How NVIDIA Groq 3 LPX Unlocks Ultrafast Interactivity at Long Context](https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/)）。Vera Rubin 在延迟预算收紧时由 NVIDIA Dynamo 编排异构解码回路（[How the NVIDIA Vera Rubin Platform is Solving Agentic AI's Scale-Up Problem](https://developer.nvidia.com/blog/how-the-nvidia-vera-rubin-platform-is-solving-agentic-ais-scale-up-problem/)）。

**自研加速器规模化。** Google 第七代 TPU "Ironwood"（TPU7x）每个 pod 集成 9,216 块液冷芯片，单芯片 BF16 峰值 2,307 TFLOPs、FP8 4,614 TFLOPs、HBM 192 GiB，整 pod 提供约 42.5 ExaFlops（[TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)、[Tensor Processing Units](https://cloud.google.com/tpu)）。Google 随后公布第八代 TPU，采用双芯片设计、提供 121 ExaFlops 算力并整合更快的存储访问（[第 8 世代 TPU：エージェンティック時代に向けた 2 つのチップ](https://cloud.google.com/blog/ja/products/infrastructure/eighth-generation-tpu-agentic-era)）。AWS 的第四代 AI 芯片 Trainium3（首款 3nm AWS AI 芯片）驱动 EC2 Trn3 UltraServers，每芯片提供 2.52 PFLOPs FP8 算力，内存容量比前代提升 1.5 倍（[Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)）。一项对比测试显示，16 块 TPU v7 Ironwood 对 16 块 NVIDIA GB200 运行 Kimi K3，双方均用 vLLM，TPU 达到 709 token/s、GB200 为 452 token/s，前者快约 57%（[谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)）。

## 核心技术与关键概念

**MoE（混合专家）架构。** MoE 由专家子网络、专家稀疏性、门控网络与输出组合四要素构成，每 token 只激活少量专家，从而在控制算力的同时扩大总参数量（[What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)）。该领域的系统性问题包括 Top-k 路由、共享专家、细粒度专家、token 分发、设备放置、all-to-all 通信与计算-通信重叠等，与光互连带宽直接耦合（[The Evolution of Mixture-of-Experts Architectures in Large Language Models](https://arxiv.org/pdf/2608.08650)）。在万卡级 MoE 训练中，Megatron Core 等框架专门处理专家并行与负载均衡（[Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/html/2603.07685v2)）。

**训练框架与并行策略。** PyTorch 仍是绝对主流，90% 以上已发表的大模型（Llama、Mistral、GPT 等）使用 PyTorch，生态成熟度领先 3–5 年；JAX 的 `pjit` 分片在大规模下是真实优势，但"JAX 在规模上更快"并非保证（[PyTorch vs JAX: Which Framework Wins Multi-Node GPU Training](https://markaicode.com/vs/pytorch-vs-jax/)、[PyTorch vs JAX: which deep learning framework should you choose?](https://theneuralbase.com/compare/pytorch-vs-jax/)）。工程实践中，8–100+ GPU 规模常采用 Megatron-LM 的 TP+PP+DP（三维并行），TPU 侧则用 JAX + Flax 的 pmap/mesh（[Frameworks de Treinamento Distribuído](https://compendium.koder.dev/ia/08-referencia/07-frameworks/treinamento-distribuido/)）。

**推理框架三强。** TensorRT-LLM 在 H100 上的稠密模型吞吐较 vLLM 高 15%–25%，但需编译；vLLM 部署最简、支持 400+ 模型架构与最广硬件；SGLang 凭借 RadixAttention 与专家并行（EP），在大 MoE（如 DeepSeek-R1/V3）与高并发场景表现最佳（[vLLM vs SGLang vs TensorRT-LLM](https://inferenceengineering.tech/learn/vllm-vs-sglang-vs-tensorrt-llm/)）。具体到 Llama 3.3 70B FP8 单卡 H100，TensorRT-LLM 单请求高约 8%、50 并发高约 13%，代价是近半小时的编译（[TensorRT-LLM vs vLLM vs SGLang: H100 Benchmark 2026](https://markaicode.com/benchmarks/cuda-llama-33-h100-throughput-benchmark/)）。vLLM 在 Qwen3.5 上实现了每 GPU 25,000 token/s 的总吞吐（[vLLM Reaches 25K Total TPS/GPU on Qwen3.5](https://vllm.ai/blog/2026-08-06-qwen35-25k-tps)），并通过 WideEP 与 NVFP4 GEMM 等针对 Blackwell 的精度优化持续提升大 MoE 服务能力（[Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)）。

**KV cache 优化与量化。** KV cache 量化是长上下文与高并发的关键：FP8/INT8 可把显存减半，INT4 进一步压缩但可能引入质量损失（[KV Cache & PagedAttention Complete Guide (2026)](https://localaimaster.com/blog/kv-cache-paged-attention-guide)）。NVIDIA 的 NVFP4 KV cache 相较 FP8 可将显存占用再降约 50%，但需要 Blackwell 硬件（[使用 NVFP4 KV 缓存优化大批次与长上下文推理](https://developer.nvidia.cn/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/)）。面向 context-heavy agent，UltraQuant 以 4-bit KV 缓存在生产级 Claude Code 轨迹回放上实现 2.71×（MiniMax-M2.5）至 4.38×（Qwen3 系列）的吞吐提升（[UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/html/2606.20474)）。

**蒸馏**：通过把大模型的推理/能力迁移到小模型，配合量化压缩部署成本，是推理降本的重要一环（[Inference-Time Distillation](https://arxiv.org/html/2512.02543v2)）。

**数据中心散热路线。** 当前主流分冷板式、浸没式、喷淋式三大技术路线：冷板式支撑 50–120 kW/机架，浸没式可支撑 100–250 kW/机架的更高功率密度（[Direct-to-Chip vs. Immersion Cooling](https://www.soeteckpower.com/direct-to-chip-vs-immersion-cooling-which-is-right-for-your-ai-data-center/)）。Open Compute Project 的 ORv3 48V 规范把直接芯片（direct-to-chip，D2C）液冷视为 30 kW 以上机架的基线，Microsoft 自 2025 年 7 月起在 Azure 园区批量部署 D2C（[Architecting Hybrid Cooling Layers](https://www.computeforecast.com/long-reads/hybrid-cooling-mixed-density-data-hall-architecture/)）。据 2026 年市场数据，D2C 约占液冷采用量的 43%，是部署最广的方案（[Liquid Cooling for GPU Clusters](https://gainam.com/insights/liquid-cooling-gpu-clusters)）。

**液冷方案的成本结构差异。** 液冷路线的选择不仅取决于散热能力，也取决于流体成本与改造难度：一套 500 机架的 D2C 部署约需 5,000–15,000 升冷却液，而同等规模浸没式部署最低需 250,000–500,000 升介电液，流体资本开支指数约为 D2C 的 3–5 倍（[Direct-to-Chip vs. Immersion Cooling: Fluid Types](https://alliancechemical.com/blogs/articles/direct-to-chip-vs-immersion-cooling-fluid-types)）。在中国市场，冷板式在存量机房改造中占比超 85%，而浸没式可支撑单柜 100 kW 至 250 kW 超高功率密度、PUE 低至 1.03–1.05，被视为新建智算中心的核心方案（[算力火爆带热液冷赛道](http://news.qq.com/rain/a/20260921A024E500)）。

## 代表性项目/公司/产品（附官方链接）

- NVIDIA NVLink / Spectrum-X：https://www.nvidia.com/en-sg/data-center/nvlink/
- NVIDIA Vera Rubin 平台：https://blogs.nvidia.com/blog/vera-rubin/
- NVIDIA HGX 平台（Rubin / Blackwell Ultra）：https://www.nvidia.com/en-us/data-center/hgx/
- NVIDIA GB300 NVL72：https://www.nvidia.com/en-eu/data-center/gb300-nvl72/
- Google TPU（Ironwood / TPU7x）：https://cloud.google.com/tpu
- AWS Trainium：https://aws.amazon.com/ai/machine-learning/trainium/
- vLLM：https://vllm.ai/blog/2026-08-06-qwen35-25k-tps
- NVIDIA 推理平台（TensorRT-LLM / Dynamo）：https://www.nvidia.com/en-gb/solutions/ai/inference/
- SK hynix HBM4：https://product.skhynix.com/products/dram/hbm/hbm4.go
- CoreWeave（GPU 云）：https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/

## 关键数据与评测结果

- **推理成本持续下探**：BenchLM Token Price Index 显示，截至 2026 年 9 月，前沿 LLM token 价格较 2023 年 3 月低约 84%（指数 16，基准 100）（[LLM Pricing Statistics (2026)](https://benchlm.ai/stats/llm-pricing)）。据数据服务商 Silicon Data，其按使用量加权的大模型 token 支出指数首次跌破每百万 token 1 美元，报 0.97 美元（[新浪财经](https://finance.sina.com.cn/roll/2026-09-03/doc-iniqpqxy7000038.shtml.md)）。另有来源称，从 GPT-4 时代到 GPT-5 时代前沿 API 单价下降约 10 倍，而面向人的准入价格反而向每月 200 美元上限攀升（[Token prices fall as access tiers rise](https://www.usagepricing.com/blueprint/trends/token-price-deflation)）。
- **单位 token 成本**：据 SemiAnalysis InferenceX（2026 年 4 月），GB300 NVL72 在 116 TPS/user 交互性下可达每百万 token $0.123；NVIDIA B200 在 GPT-OSS-120B 上达到每百万 token 两美分的生产基准（[NVIDIA Inference Platform](https://www.nvidia.com/en-gb/solutions/ai/inference/)、[cloud accelerator pricing](https://perspectives.nvidia.com/cloud-accelerator-pricing-llm-inference-scale-2026)）。
- **机架级规格**：NVIDIA GB300 NVL72 集成 72 块 Blackwell Ultra GPU 与 36 块 Grace CPU，FP8/FP6 Tensor Core 算力 720 PFLOPS、INT8 24 POPS、FP16/BF16 360 PFLOPS，机内 NVLink 带宽 130 TB/s（[NVIDIA GB300 NVL72](https://www.nvidia.com/en-eu/data-center/gb300-nvl72/)、[NVIDIA Inference Platform](https://www.nvidia.com/en-gb/solutions/ai/inference/)）。NVIDIA HGX Vera Rubin NVL8 平台则由 8 块 Rubin SXM 搭配单路 Vera CPU（88 个 Arm 兼容的自定义 Olympus 核心）构成，NVFP4 推理算力 400 PFLOPS、NVFP4 训练 280 PFLOPS、FP8/FP6 训练 140 PFLOPS，CPU 侧配 1.5 TB LPDDR5X、带宽 1.2 TB/s（[NVIDIA HGX Platform](https://www.nvidia.com/en-us/data-center/hgx/)）。
- **GPU 云（neocloud）财务与积压订单**：CoreWeave 2026 年 Q2 营收 25.8 亿美元、同比增 112%，净亏损 6.26 亿美元，营收积压（backlog）约 1040 亿美元（[Best GPU Neoclouds 2026](https://www.marktechpost.com/2026/08/23/best-gpu-neoclouds-2026/)），并把 2026 全年营收指引上调至 124 亿–132 亿美元（[CoreWeave Raises 2026 Revenue Forecast](https://www.ainvest.com/news/coreweave-raises-2026-revenue-forecast-12-4b-13-2b-massive-backlog-2609/)）；另一口径显示其 Q1 2026 积压为 994 亿美元，并与 Meta 签下 210 亿美元、与 Anthropic 签下多年协议（[CoreWeave Reports Strong First Quarter 2026 Results](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/)）。Nebius 2026 年 Q2 营收 5.82 亿美元、同比增 454%、ARR 约 30 亿美元（[Best GPU Neoclouds 2026](https://www.marktechpost.com/2026/08/23/best-gpu-neoclouds-2026/)）。
- **液冷渗透率**：TrendForce 预测 AI 芯片的液冷渗透率 2026 年将达 53%（2025 年为 33%），并进一步升至 59%（[AI Data Center Liquid Cooling Adoption to Hit 53% in 2026](https://infotechlead.com/data-center/ai-data-center-liquid-cooling-adoption-to-hit-53-in-2026-as-nvidia-amd-google-drive-demand-97794)）。浸没式相变液冷可支持 150 kW/机架以上的功率密度；冷板式可捕获服务器约 80% 的热量（[Why Liquid Cooling is No Longer Optional for 2026 AI Workloads](https://inveniatech.com/data-center/why-liquid-cooling-is-no-longer-optional-for-2026-ai-workloads/)）。
- **能效 PUE**：Uptime Institute《2026 全球数据中心调查》给出行业平均 PUE 为 1.52，延续七年的相对停滞（[Uptime Institute Global Data Center Survey 2026](https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/UptimeInstitute.GlobalDataCenterSurvey.2026.pdf)）。而分技术路线看，先进风冷 PUE 约 1.45–1.60、直接芯片 1.10–1.20、单相浸没 1.03–1.08（[Data Center Cooling Economics](https://www.adamsilvaconsulting.com/insights/data-center-cooling-economics-2026)）。浸没式可将机房 PUE 压至约 1.04，综合节电 15%–20%（[从一块芯片到一座机房](http://m.toutiao.com/group/7689727179181146675/)）。
- **液冷市场**：赛迪顾问数据显示，2025 年中国液冷数据中心市场规模达 159.8 亿元、同比增长 45.2%，预计 2026 年达 232.5 亿元；中金公司预测 2026 年全球智算中心液冷市场规模有望突破 1147 亿元、同比增长 273%（[算力火爆带热液冷赛道](http://finance.people.com.cn/n1/2026/0921/c1004-40802433.html)）。
- **厂商级散热方案**：有整机方案（KAYTUS AI Compute Pod）宣称单机架冷却能力最高 130 kW、PUE 低至 1.1，并实现制冷与 IT 负载的秒级同步、制冷能效提升逾 10%（[KAYTUS AI Compute Pod Wins 2026 iF Design Award and Red Dot Award](https://www.businesswire.com/news/home/20260428825343/en/KAYTUS-AI-Compute-Pod-Wins-2026-iF-Design-Award-and-Red-Dot-Award-Setting-a-New-Standard-for-AI-Data-Center)）。
- **neocloud 的电力与合同化**：截至 2026 年 8 月，CoreWeave 活跃电力约 1.5 GW（51 个数据中心）、合同电力约 4.2 GW、积压约 1290 亿美元；Nebius 目标合同电力 5.0 GW，并累计与 Microsoft（约 170 亿美元）及 Meta（最高约 270 亿美元）签约（[The Oil of the AI Age? Compute Futures and the Neocloud Economy](https://img1.wsimg.com/blobby/go/5cb80fa7-f4af-43e6-8296-0ff3a28585b3/downloads/8c72e824-e164-454a-a6c0-087d523b16c7/Compute_Futures_and_Neocloud_Economics.pdf?ver=1788548072389)）。
- **成本下降曲线**：Andreessen Horowitz 的 "LLMflation" 分析显示，达到 GPT-3（2021 年 11 月）性能水平（MMLU 42 分，当时定价每百万 token 60 美元）的模型，到 2024 年末在 Together.ai 托管下每百万 token 仅需 0.06 美元（[LLM Cost Per Million Tokens: 2026 Inference Pricing Benchmark](https://gpusmith.com/articles/en/pdfs/llm-cost-per-million-tokens-benchmark.pdf)）。
- **云厂商资本开支**：2026 年 Alphabet 指引 1950–2050 亿美元，Microsoft 约 1900 亿美元，Meta 1250–1450 亿美元（[Hyperscaler](https://aiwiki.ai/wiki/hyperscaler/edit)）。另有统计口径称 Amazon 约 2000 亿美元、Google 约 1950 亿–2050 亿美元，四家合计推动约 7000 亿美元的基础设施竞赛（[AI Data Centre Investment Ranking 2026](https://infotechlead.com/data-center/ai-data-centre-investment-ranking-2026-amazon-google-microsoft-and-meta-lead-700-billion-infrastructure-race-98172)、[Amazon, Google, Microsoft and Meta Lead $700 Billion 2026 AI Infrastructure Race](https://jannikhansen.com/en/news/amazon-google-microsoft-and-meta-lead-700-billion-2026-ai-infrastructure-race)）。高盛则把资本开支分为三阶段：2023–2025 年约 6330 亿美元（年均约 2110 亿美元）、2026–2027 年约 1.73 万亿美元（年均约 8630 亿美元）、2028–2030 年进一步扩张（[高盛测算:"AI第二阶段"的"资本缺口"要怎么补?](http://m.toutiao.com/group/7689687631352857123/)）。

## 趋势与争议

**电力与电网成为新瓶颈。** 高密度 AI 机架要求协调可用电网电力、设施设计、部署周期与长期运营效率；液冷之所以成为主流答案，是因为它能让人在有限电力下"榨出"更多算力（[Data center power density](https://blog.se.com/datacenter/2026/07/28/data-center-power-density-planning-liquid-cooled-ai-data-centers-around-grid-and-power-constraints/)）。据 IEA 口径，数据中心用电约 40% 来自天然气、约 15% 来自煤电、核能约占 20%（[Powering AI's future: The case for nuclear energy in data centers](https://www.techtarget.com/it-infrastructure/feature/Powering-AIs-future-The-case-for-nuclear-energy-in-data-centers)）。为锁定长期电力，Meta 于 2026 年 1 月签署最多 6.6 GW 核电协议（含与 Constellation 的 1.1 GW、20 年 PPA 及与 TerraPower、Oklo 的远期协议），Amazon 与 Talen Energy 就 Susquehanna 核电（1.9 GW）达成 200 亿美元安排（[AI Data Center Energy Consumption Statistics 2026](https://axis-intelligence.com/ai-data-center-energy-consumption-statistics/)）。近期的电力缓解仍主要依赖燃气、燃料电池与电网效率提升（[AI Power Demand: Grid Bottleneck 2026](https://informedclearly.com/en/ai/62373/ai-power-demand-grid-bottleneck-2026)）。

**资本开支的可持续性争议。** 有测算指出，大型科技公司已把约 96% 的现金流投入资本开支，长期债务合计升至约 3419 亿美元（Alphabet 982 亿、Amazon 1289 亿、Meta 837 亿、Microsoft 311 亿）（[AI Capex 2026: Big Tech Now Spends 96% of Its Cash Flow](https://www.simianx.ai/stories/ai-capex-2026-big-tech-now-spends-96-of-its-cash-flow)）。一旦 AI 需求放缓，约 7000 亿美元 capex 的回报节奏将受到审视（[What an AI slowdown does to $700 billion in AI capex](https://financetracked.com/ai-capex-slowdown)）。

**互联路线的分化。** NVLink 代表封闭但高带宽的 scale-up 路线（并借 NVLink Fusion 向半定制开放），以太网阵营（Spectrum-X、Ultra Ethernet）则在 scale-out 上争夺开放生态（[NVIDIA Vera Rubin](https://blogs.nvidia.com/blog/vera-rubin/)）。同时，自研加速器（TPU Ironwood、Trainium3）在特定负载上对通用 GPU 形成价格/能效竞争（[Tensor Processing Units](https://cloud.google.com/tpu)、[Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)）。

**推理需求的结构性上移。** 随着 Agent、长上下文与推理模型的普及，算力需求曲线正从训练侧向推理侧延伸，算力供给持续紧张（[高盛测算:"AI第二阶段"的"资本缺口"要怎么补?](http://m.toutiao.com/group/7689687631352857123/)）。这也解释了为何 prefill/decode 解耦、KV cache 量化与更低价的 API 档位成为 2026 年基础设施优化的重点（[Token prices fall as access tiers rise](https://www.usagepricing.com/blueprint/trends/token-price-deflation)）。

**出口管制与算力地缘。** 美国商务部 BIS 于 2026 年 1 月修订对华半导体出口许可政策，将 Nvidia H200、AMD MI325X 等芯片的审查从"推定拒绝"改为"逐案审查"（[Department of Commerce Revises License Review Policy](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)、[Revision to License Review Policy for Advanced Computing Commodities](https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities)）；同月 Trump 政府宣布对符合条件的对华出口芯片加征 25% 关税，但政策松动未立即转化为商业现实，H200 重返中国市场后收入占比不足 1%（[英伟达H200芯片重返中国市场收入占比不足1%](https://www.eet-china.com/news/202608288257.html)）。NVIDIA 在 2025 年 4 月因 H20 出口需许可而计提 45 亿美元费用（[NVIDIA 10-K filing](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)）。

## 参考来源

1. [AIデータセンターのエネルギー危機完全解説2026](https://labmemo.com/smr-data-center-energy-ai-explained-2026/)
2. [AI Data Center Energy Crisis 2026: Colossus, Stargate, and the Race for Power](https://andrew.ooo/answers/ai-data-center-energy-crisis-colossus-stargate-power-july-2026/)
3. [xAI's Memphis Colossus: Anatomie eines 100.000-GPU-Supercomputers](https://introl.com/de/blog/xai-memphis-colossus-100000-gpu-supercomputer-infrastructure)
4. [GPT-6 Astra : 100 000 GPU Nvidia pour entraîner le modèle](https://overclocking.com/gpt-6-astra-100000-gpu-nvidia-prix-ram/)
5. [全国产十万卡AI超集群落成并接入国家超算互联网](https://tech.gmw.cn/2026-07/10/content_38879178.htm)
6. [Stargate Project Tracker](https://www.stargate.how/)
7. [Oracle's $300 Billion OpenAI Gamble](https://www.webanditnews.com/2026/09/15/oracles-300-billion-openai-gamble-the-massive-bet-reshaping-ai-infrastructure/)
8. [OpenAI's Stargate Nevada Just Went Live](https://datavook.com/post/openai-stargate-nevada-data-center-live-july-2026)
9. [OpenAI Stargate - Saline Township Campus](https://servercountry.org/data/projects/openai-stargate-saline-township-campus/)
10. [Samsung Ships Industry-First Commercial HBM4](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)
11. [SK hynix HBM4](https://product.skhynix.com/products/dram/hbm/hbm4.go)
12. [Micron in High-Volume Production of HBM4 Designed for NVIDIA Vera Rubin](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)
13. [Samsung Unveils HBM4E at NVIDIA GTC 2026](https://news.samsungsemiconductor.com/global/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/)
14. [NVIDIA NVLink: The Scale-Up Network for AI Factories](https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories)
15. [NVIDIA Vera Rubin](https://blogs.nvidia.com/blog/vera-rubin/)
16. [NVIDIA NVLink and NVLink Switch](https://www.nvidia.com/en-sg/data-center/nvlink/)
17. [NVIDIA DGX SuperPOD](https://blogs.nvidia.cn/blog/dgx-superpod-rubin/)
18. [How the NVIDIA Vera Rubin Platform is Solving Agentic AI's Scale-Up Problem](https://developer.nvidia.com/blog/how-the-nvidia-vera-rubin-platform-is-solving-agentic-ais-scale-up-problem/)
19. [NVIDIA Rubin CPX](https://nvnexus.com/product/nvidia-rubin-cpx/)
20. [NVIDIA Rubin CPX Accelerates Inference Performance and Efficiency](https://resources.nvidia.com/en-us-inference-infrastructure/nvidia-rubin-cpx-accelerates)
21. [How NVIDIA Groq 3 LPX Unlocks Ultrafast Interactivity at Long Context](https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/)
22. [TPU7x (Ironwood) — Google Cloud Docs](https://docs.cloud.google.com/tpu/docs/tpu7x)
23. [Tensor Processing Units — Google Cloud](https://cloud.google.com/tpu)
24. [第 8 世代 TPU：エージェンティック時代に向けた 2 つのチップ](https://cloud.google.com/blog/ja/products/infrastructure/eighth-generation-tpu-agentic-era)
25. [Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)
26. [谷歌TPU跑Kimi比英伟达GPU快57%](http://m.toutiao.com/group/7689737267351306792/)
27. [What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)
28. [The Evolution of Mixture-of-Experts Architectures in Large Language Models](https://arxiv.org/pdf/2608.08650)
29. [Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/html/2603.07685v2)
30. [PyTorch vs JAX: Which Framework Wins Multi-Node GPU Training](https://markaicode.com/vs/pytorch-vs-jax/)
31. [PyTorch vs JAX: which deep learning framework should you choose?](https://theneuralbase.com/compare/pytorch-vs-jax/)
32. [Frameworks de Treinamento Distribuído](https://compendium.koder.dev/ia/08-referencia/07-frameworks/treinamento-distribuido/)
33. [vLLM vs SGLang vs TensorRT-LLM](https://inferenceengineering.tech/learn/vllm-vs-sglang-vs-tensorrt-llm/)
34. [TensorRT-LLM vs vLLM vs SGLang: H100 Benchmark 2026](https://markaicode.com/benchmarks/cuda-llama-33-h100-throughput-benchmark/)
35. [vLLM Reaches 25K Total TPS/GPU on Qwen3.5](https://vllm.ai/blog/2026-08-06-qwen35-25k-tps)
36. [Driving vLLM WideEP and Large-Scale Serving Toward Maturity on Blackwell](https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html)
37. [KV Cache & PagedAttention Complete Guide (2026)](https://localaimaster.com/blog/kv-cache-paged-attention-guide)
38. [使用 NVFP4 KV 缓存优化大批次与长上下文推理](https://developer.nvidia.cn/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/)
39. [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/html/2606.20474)
40. [Inference-Time Distillation](https://arxiv.org/html/2512.02543v2)
41. [Direct-to-Chip vs. Immersion Cooling: Which is Right for Your AI Data Center?](https://www.soeteckpower.com/direct-to-chip-vs-immersion-cooling-which-is-right-for-your-ai-data-center/)
42. [Architecting Hybrid Cooling Layers for Mixed-Density Data Halls](https://www.computeforecast.com/long-reads/hybrid-cooling-mixed-density-data-hall-architecture/)
43. [Liquid Cooling for GPU Clusters: The Direct-to-Chip Decision Framework](https://gainam.com/insights/liquid-cooling-gpu-clusters)
44. [NVIDIA HGX Platform](https://www.nvidia.com/en-us/data-center/hgx/)
45. [NVIDIA GB300 NVL72](https://www.nvidia.com/en-eu/data-center/gb300-nvl72/)
46. [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/)
47. [NVIDIA Inference Platform](https://www.nvidia.com/en-gb/solutions/ai/inference/)
48. [LLM Pricing Statistics (2026)](https://benchlm.ai/stats/llm-pricing)
49. [新浪财经：AI token 价格创新低](https://finance.sina.com.cn/roll/2026-09-03/doc-iniqpqxy7000038.shtml.md)
50. [Token prices fall as access tiers rise](https://www.usagepricing.com/blueprint/trends/token-price-deflation)
51. [cloud accelerator pricing](https://perspectives.nvidia.com/cloud-accelerator-pricing-llm-inference-scale-2026)
52. [Best GPU Neoclouds 2026](https://www.marktechpost.com/2026/08/23/best-gpu-neoclouds-2026/)
53. [CoreWeave Raises 2026 Revenue Forecast to $12.4B–$13.2B](https://www.ainvest.com/news/coreweave-raises-2026-revenue-forecast-12-4b-13-2b-massive-backlog-2609/)
54. [CoreWeave Reports Strong First Quarter 2026 Results](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/)
55. [AI Data Center Liquid Cooling Adoption to Hit 53% in 2026](https://infotechlead.com/data-center/ai-data-center-liquid-cooling-adoption-to-hit-53-in-2026-as-nvidia-amd-google-drive-demand-97794)
56. [Why Liquid Cooling is No Longer Optional for 2026 AI Workloads](https://inveniatech.com/data-center/why-liquid-cooling-is-no-longer-optional-for-2026-ai-workloads/)
57. [Uptime Institute Global Data Center Survey 2026](https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/UptimeInstitute.GlobalDataCenterSurvey.2026.pdf)
58. [Data Center Cooling Economics: Liquid vs Air vs Immersion in 2026](https://www.adamsilvaconsulting.com/insights/data-center-cooling-economics-2026)
59. [算力火爆带热液冷赛道](http://finance.people.com.cn/n1/2026/0921/c1004-40802433.html)
60. [从一块芯片到一座机房](http://m.toutiao.com/group/7689727179181146675/)
61. [Hyperscaler](https://aiwiki.ai/wiki/hyperscaler/edit)
62. [AI Data Centre Investment Ranking 2026](https://infotechlead.com/data-center/ai-data-centre-investment-ranking-2026-amazon-google-microsoft-and-meta-lead-700-billion-infrastructure-race-98172)
63. [Amazon, Google, Microsoft and Meta Lead $700 Billion 2026 AI Infrastructure Race](https://jannikhansen.com/en/news/amazon-google-microsoft-and-meta-lead-700-billion-2026-ai-infrastructure-race)
64. [高盛测算:"AI第二阶段"的"资本缺口"要怎么补?](http://m.toutiao.com/group/7689687631352857123/)
65. [Data center power density](https://blog.se.com/datacenter/2026/07/28/data-center-power-density-planning-liquid-cooled-ai-data-centers-around-grid-and-power-constraints/)
66. [Powering AI's future: The case for nuclear energy in data centers](https://www.techtarget.com/it-infrastructure/feature/Powering-AIs-future-The-case-for-nuclear-energy-in-data-centers)
67. [AI Data Center Energy Consumption Statistics 2026](https://axis-intelligence.com/ai-data-center-energy-consumption-statistics/)
68. [AI Power Demand: Grid Bottleneck 2026](https://informedclearly.com/en/ai/62373/ai-power-demand-grid-bottleneck-2026)
69. [AI Capex 2026: Big Tech Now Spends 96% of Its Cash Flow](https://www.simianx.ai/stories/ai-capex-2026-big-tech-now-spends-96-of-its-cash-flow)
70. [What an AI slowdown does to $700 billion in AI capex](https://financetracked.com/ai-capex-slowdown)
71. [Department of Commerce Revises License Review Policy for Semiconductors Exported to China](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)
72. [Revision to License Review Policy for Advanced Computing Commodities](https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities)
73. [英伟达H200芯片重返中国市场收入占比不足1%](https://www.eet-china.com/news/202608288257.html)
74. [NVIDIA 10-K filing (nvda-20260125)](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
75. [Direct-to-Chip vs. Immersion Cooling: Fluid Types, Chemistry, and Selection Rules](https://alliancechemical.com/blogs/articles/direct-to-chip-vs-immersion-cooling-fluid-types)
76. [算力火爆带热液冷赛道（腾讯新闻）](http://news.qq.com/rain/a/20260921A024E500)
77. [The Oil of the AI Age? Compute Futures and the Neocloud Economy](https://img1.wsimg.com/blobby/go/5cb80fa7-f4af-43e6-8296-0ff3a28585b3/downloads/8c72e824-e164-454a-a6c0-087d523b16c7/Compute_Futures_and_Neocloud_Economics.pdf?ver=1788548072389)
78. [LLM Cost Per Million Tokens: 2026 Inference Pricing Benchmark](https://gpusmith.com/articles/en/pdfs/llm-cost-per-million-tokens-benchmark.pdf)
79. [KAYTUS AI Compute Pod Wins 2026 iF Design Award and Red Dot Award](https://www.businesswire.com/news/home/20260428825343/en/KAYTUS-AI-Compute-Pod-Wins-2026-iF-Design-Award-and-Red-Dot-Award-Setting-a-New-Standard-for-AI-Data-Center)