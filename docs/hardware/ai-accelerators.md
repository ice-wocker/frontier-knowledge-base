# AI 芯片与加速器

> 最后更新：2026-09-26 ｜ 领域：AI 硬件 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI 加速器是支撑大模型训练与推理的物理底座。2024–2026 年，这一市场从" NVIDIA 一家独大"演变为"多极竞争 + 大厂自研"：NVIDIA 保持数据中心 GPU 绝对主导，但 AMD Instinct、Google TPU、AWS Trainium、华为昇腾、寒武纪，以及 Microsoft Maia、Meta MTIA 等自研芯片快速上量。产品演进的共同主线是**低精度算力（FP8/FP4/MXFP4）的持续翻倍、HBM 容量与带宽的军备竞赛，以及从"单芯片"走向"机架级/超节点级系统"**。

## 2025–2026 最新进展

### NVIDIA：从 Blackwell Ultra 到 Rubin
NVIDIA 的数据中心 GPU 路线遵循年度迭代节奏。Hopper 架构的 H200 于 2024 年成为首款提供 141GB HBM3e、4.8 TB/s 带宽的 GPU（[NVIDIA H200 GPU](https://www.nvidia.com/en-us/data-center/h200/)）。

Blackwell Ultra（GB300 NVL72）于 2025 年出货，单 GPU 配备 288GB HBM3e，相比前代提供 1.5 倍更大的 HBM 容量（[NVIDIA GB300 NVL72](https://www.nvidia.com/en-in/data-center/gb300-nvl72/)）。Blackwell Ultra 采用双芯片（dual-reticle）设计，以 10 TB/s 的 NV-HBI 互连两个 die，共 2080 亿晶体管，基于 TSMC 4NP 工艺，HBM3E 容量达 288GB、带宽 8 TB/s，可让 300B 以上参数模型完整驻留片上（[Inside NVIDIA Blackwell Ultra](https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/)）。相较 HGX H100，GB300 NVL72 可提供约 70 倍的 AI FLOPS（[NVIDIA Blackwell Ultra for the Era of AI Reasoning](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-for-the-era-of-ai-reasoning/)）。

2026 年 3 月，NVIDIA 正式发布 **Vera Rubin** 平台。Rubin GPU 采用 HBM4，带宽最高达 22 TB/s、容量 288GB，支持数万亿参数模型与高并发推理而无需卸载 KV cache；NVLink 6 提供 3600 GB/s 的 scale-up 带宽；单 GPU 提供 50 PFLOPS 的 NVFP4 推理算力、35 PFLOPS 的 NVFP4 训练算力、17.5 PFLOPS 的 FP8/FP6 训练算力（[Inside NVIDIA Rubin GPU Architecture](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)、[NVIDIA HGX Platform](https://www.nvidia.com/en-us/data-center/hgx/)）。Rubin 已进入全面量产，相关产品将于 2026 年下半年由合作伙伴供货（[NVIDIA Newsroom](https://nvidianews.nvidia.com/_gallery/download_pdf/695c39b23d633240d175d8e6/)）。

NVIDIA 进一步把竞争维度拉高到"机架级超级计算机"。Vera Rubin POD 整合五类机架系统、40 个机架、约 2 万颗 die、1152 颗 Rubin GPU，总算力 60 exaflops、总 scale-up 带宽 10 PB/s（[NVIDIA Vera Rubin POD](https://developer.nvidia.com/blog/?p=113993)）。其中 **Vera Rubin NVL72** 集成 72 颗 Rubin GPU 与 36 颗 Vera CPU，训练性能功耗比是 Blackwell 的 4 倍、推理性能功耗比达 10 倍。平台还引入了 SM 级低延迟推理加速器 NVIDIA Groq 3 LPX（每机架 256 颗 LPU），以及 BlueField-4 STX + CMX 上下文存储、Spectrum-6 SPX 网络等组件。后续路线图上还有 Vera Rubin Ultra NVL576 与 Kyber NVL144（面向 Feynman 时代）。

### AMD：MI350 到 MI400「Helios」
AMD 在 2025 年推出 Instinct MI350 系列，MI350X/MI355X 配备 288GB HBM3E、8 TB/s 带宽，支持 MXFP6/MXFP4 数据类型（[AMD Instinct MI350 Series](https://www.amd.com/en/products/accelerators/instinct/mi350.html)、[AMD Instinct MI355X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html)）。2026 年 Advancing AI 大会上，AMD 发布 MI400 系列与 AMD Helios 机架级方案：Helios 单机架集成 72 颗 MI455X GPU，配备 4,600 CPU 核心、2.9 ExaFlops FP4 算力、31TB HBM 容量和 260 TB/s scale-up 带宽（[ADVANCING AI 2026](https://newsroom.amd.com/documents/2026/07/2a710b7d-c107-4639-8855-fa9366f83967.pdf)）。AMD 称 Helios 每美元推理 token 数比竞争对手高最多 30%（[AAI 2026 新闻稿](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)）。Helios 参考设计已在 2026 年下半年进入量产部署，MI430X 预计 2027 年推出（[AMD Instinct MI400 Series](https://www.amd.com/en/products/accelerators/instinct/mi400.html)）。此外 AMD 与 Anthropic 达成战略合作，将部署最多 2GW 的 MI450 系列，首个 GW 于 2027 年上半年开始（[AMD and Anthropic 新闻稿](https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/)）。

### Google TPU：Ironwood（v7）与第八代双芯片
Google 第七代 TPU（TPU7x，代号 Ironwood）是首个 Ironwood 家族产品，面向大规模训练与推理，单 Pod 可达 9216 颗芯片，已于 2026 年 3 月 31 日 GA（[TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)、[Cloud TPU release notes](https://docs.cloud.google.com/tpu/docs/release-notes)）。据 Google 实测，Ironwood 相较 TPU v5p 的碳排放效率（CCI）提升 3.7 倍（[AI infrastructure efficiency: Ironwood TPUs](https://cloud.google.com/blog/topics/systems/ironwood-tpus-deliver-37x-carbon-efficiency-gains/)）。

2026 年 Cloud Next 大会上，Google 发布**第八代 TPU，并首次拆分为两款芯片**：面向训练的 TPU 8t 与面向推理的 TPU 8i。TPU 8t 单 superpod 可扩展至 9600 颗 TPU、2 PB 共享高带宽内存，处理能力约为前代 3 倍；TPU 8i 则针对高速推理与内存墙问题设计（[Our eighth generation TPUs](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)、[Cloud Next '26](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)）。

### AWS：Trainium3 与 Trn3 UltraServers
AWS 第四代 AI 芯片 Trainium3 于 2025 年 12 月 re:Invent 正式发布，是 AWS 首款 3nm AI 芯片。单颗 Trainium3 提供 2.52 PFLOPS 的 FP8 算力，内存容量提升 1.5 倍；Trn3 UltraServers 单系统最多集成 144 颗芯片，提供相较 Trn2 UltraServer 最高 4.4 倍的算力与 4 倍能效，支持 MXFP8/MXFP4 数据类型（[Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)、[Trainium3 UltraServers now available](https://www.aboutamazon.com/news/aws/trainium-3-ultraserver-faster-ai-training-lower-cost)）。客户包括 Anthropic 等（[AWS re:Invent 2025 汇总](https://www.aboutamazon.com/news/aws/aws-re-invent-2025-ai-news-updates)）。

### Intel Gaudi
Intel 的 Gaudi 3 在 2025 年扩大供货，推出标准 PCIe Gen5 形态的 Gaudi 3 PCIe 卡（HL-338），面向 LLM、多模态与企业 RAG 等负载（[Intel Gaudi 3 PCIe Product Brief](https://cdrdv2-public.intel.com/817488/Gaudi%203%20PCIe%20Product%20Brief_RB_1_V6.pdf)、[Intel®Gaudi® 3](https://habana.ai/products/gaudi3/)）。

### 华为昇腾
华为在 2025 年公开昇腾未来三年路线图：2026 年 Q1 推出面向推理 Prefill 与推荐场景的昇腾 950PR（采用自研 HBM），2026 年 Q4 推出面向推理 Decode 与训练的昇腾 950DT（[华为公布昇腾AI芯片未来3年迭代路线图](https://www.peopleapp.com/column/30050308165-500007097808)）。2026 年 9 月 17 日华为全联接大会 2026 上，华为轮值董事长汪涛表示，昇腾 910C 超节点已部署超 1000 套，昇腾 950 超节点已规模商用，昇腾 960 芯片研发进度超预期（[中国青年网](http://t.m.youth.cn/transfer/index/url/news.youth.cn/jsxw/202609/t20260917_16874687.htm)）。华为随后更新路线图：960DT 提前至 2027 年 Q1、960PR 提前至 2027 年 Q3，并首次引入 NPO 方案（[每日经济新闻](http://m.toutiao.com/group/7686424720039805480/)）。

### 寒武纪
寒武纪 2025 年营业收入 64.97 亿元，同比增长 453.21%；归母净利润 20.59 亿元，实现扭亏为盈（[证券时报](https://www.stcn.com/article/detail/3991331.html)）。2026 年 Q1 营收 28.85 亿元、同比增长 159.56%，主要由思元 590 芯片出货驱动（[雪球：寒武纪 2026 一季报](https://xueqiu.com/9957756617/386778759)）。

### 大厂自研：Microsoft Maia 与 Meta MTIA
Microsoft 于 2026 年 1 月发布第二代自研推理加速器 **Maia 200**：基于 TSMC 3nm，原生 FP8/FP4 tensor core，216GB HBM3e（7 TB/s）、272MB 片上 SRAM、1400 亿+晶体管，单芯片 FP4 算力超 10 PFLOPS、FP8 超 5 PFLOPS，750W TDP；搭载 2.8 TB/s scale-up 带宽，可扩展至 6144 颗加速器集群，性能/美元比现有 fleet 提升 30%（[Maia 200: The AI accelerator built for inference](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)、[Maia 200: Software-defined dataflow](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/maia-200-software-defined-dataflow-and-all-ethernet-networking-for-efficient-inf/4548198)）。

Meta 于 2026 年 3 月宣布将在两年内部署四代新 MTIA 芯片，覆盖排序推荐与 GenAI 负载，坚持以推理优先、快速迭代、基于行业标准的策略（[Expanding Meta's Custom Silicon](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/)）；并于 2026 年 4 月与 Broadcom 合作共同开发定制 AI 芯片，涉及芯片设计、先进封装与网络（[Meta Partners With Broadcom](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/)）。

## 核心技术与关键概念

- **低精度算力**：FP8 已成为主流训练/推理精度，FP4（NVIDIA NVFP4、AMD MXFP4、AWS MXFP4）进一步压低内存占用与能耗。NVIDIA Rubin 的 NVFP4 推理算力达 50 PFLOPS（[Inside NVIDIA Rubin GPU Architecture](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)）。
- **HBM 容量与带宽**：从 H100 的 80GB HBM3（3.35 TB/s）→ H200 的 141GB HBM3e（4.8 TB/s）→ Blackwell Ultra 的 288GB HBM3e（8 TB/s，[NVIDIA H200 GPU](https://www.nvidia.com/en-us/data-center/h200/)）→ Rubin 的 288GB HBM4（22 TB/s）。HBM4 将单 stack 接口从 1024 bit 提升到 2048 bit。
- **训练 vs 推理芯片**：训练侧强调高算力与高带宽 scale-up（NVL72/NVL576）；推理侧强调低延迟与长上下文 KV cache 管理，出现专用低延迟加速器（如 NVIDIA Groq 3 LPX）与专用推理芯片（Maia 200）。
- **机架级系统与互联**：NVLink 6（3600 GB/s/GPU）、AMD Helios 的 260 TB/s scale-up、Microsoft 基于以太网的 Maia 传输协议，说明竞争已从单芯片转向整机架。
- **散热与供电**：Vera Rubin NVL72 采用 45°C 温水液冷，并引入 Intelligent Power Smoothing（每 GPU 400 J 机架级储能），可在同一电力预算下多部署约 10% 的 NVL72 机架（[NVIDIA Vera Rubin POD](https://developer.nvidia.com/blog/?p=113993)）。

## 关键数据

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| NVIDIA GB300 NVL72 vs Hopper | 吞吐/MW 最高 50 倍，token 成本最高低 35 倍 | [NVIDIA 数据中心深度学习性能](https://resources.nvidia.com/en-us-inference-contact-us/deep-learning-perfor) |
| NVIDIA Rubin GPU（单卡） | NVFP4 推理 50 PFLOPS / 训练 35 PFLOPS | [NVIDIA HGX Platform](https://www.nvidia.com/en-us/data-center/hgx/) |
| NVIDIA Vera Rubin POD | 1152 GPU、60 exaflops、10 PB/s | [NVIDIA Vera Rubin POD](https://developer.nvidia.com/blog/?p=113993) |
| AMD MI455X（Helios 72 卡） | 2.9 ExaFlops FP4、31TB HBM、260 TB/s | [ADVANCING AI 2026](https://newsroom.amd.com/documents/2026/07/2a710b7d-c107-4639-8855-fa9366f83967.pdf) |
| Google TPU 8t | superpod 9600 TPU、2 PB 共享 HBM、约 3 倍算力 | [Cloud Next '26](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/) |
| AWS Trainium3 | 2.52 PFLOPS FP8/芯片，Trn3 系统算力 4.4 倍 | [AWS whats-new](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/) |
| Microsoft Maia 200 | FP4 >10 PFLOPS、216GB HBM3e@7TB/s、750W | [Microsoft Maia 200](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/) |
| SK hynix HBM4 | 2026-02-12 量产，11.7 Gb/s pin speed | [HBM 全指南](https://www.insidedeeptech.com/high-bandwidth-memory-hbm-full-guide/) |
| Micron HBM4 | 36GB 12H 量产，>2.8 TB/s，能效提升 20% | [Micron 新闻稿](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin) |
| 寒武纪 2025 营收 | 64.97 亿元，同比 +453.21% | [证券时报](https://www.stcn.com/article/detail/3991331.html) |

## 趋势与争议

1. **出口管制重塑市场**：2025 年 4 月美国政府要求 H20 出口中国需许可证，NVIDIA 因此在 2026 财年第一季度计提 45 亿美元费用（[NVIDIA SEC 文件](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)）。2025 年 12 月 8 日美方宣布允许 H20 出口，随后 BIS 于 2026 年 1 月发布规则，对 NVIDIA H200、AMD MI325X 及类似芯片的对华出口按"逐案审查"处理（[BIS 新闻稿](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)、[Federal Register](https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities)）。管制与反制催生了中国国产替代加速，也带来供应链与合规不确定性。
2. **自研芯片对 NVIDIA 的挤压**：Google、AWS、Microsoft、Meta 均在推进自研，推理场景成为自研芯片最容易切入的环节——推理对通用生态（CUDA）依赖更低，而对成本与能效更敏感。
3. **算力泡沫争议**：NVIDIA 与 OpenAI 达成的最高 1000 亿美元、至少 10GW 数据中心合作（首个 GW 于 2026 年下半年部署于 Vera Rubin 平台）引发对算力投资可持续性的讨论（[NVIDIA Newsroom](https://nvidianews.nvidia.com/_gallery/download_pdf/68d173273d633288cb44040b/)）。
4. **HBM 产能瓶颈**：HBM4 量产节奏（SK hynix、Micron、Samsung）直接制约高端 GPU 出货，成为行业关键瓶颈。

## 参考来源

1. [NVIDIA Vera Rubin POD: Seven Chips, Five Rack-Scale Systems, One AI Supercomputer](https://developer.nvidia.com/blog/?p=113993)
2. [Inside NVIDIA Rubin GPU Architecture: Powering the Era of Agentic AI](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)
3. [NVIDIA HGX Platform](https://www.nvidia.com/en-us/data-center/hgx/)
4. [Inside NVIDIA Blackwell Ultra: The Chip Powering the AI Factory Era](https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/)
5. [NVIDIA GB300 NVL72](https://www.nvidia.com/en-in/data-center/gb300-nvl72/)
6. [NVIDIA H200 GPU](https://www.nvidia.com/en-us/data-center/h200/)
7. [NVIDIA Blackwell Ultra for the Era of AI Reasoning](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-for-the-era-of-ai-reasoning/)
8. [NVIDIA Data Center Deep Learning Product Performance](https://resources.nvidia.com/en-us-inference-contact-us/deep-learning-perfor)
9. [NVIDIA Newsroom（Rubin 量产公告）](https://nvidianews.nvidia.com/_gallery/download_pdf/695c39b23d633240d175d8e6/)
10. [NVIDIA Newsroom（OpenAI 合作公告）](https://nvidianews.nvidia.com/_gallery/download_pdf/68d173273d633288cb44040b/)
11. [AMD Instinct™ MI400 Series GPUs](https://www.amd.com/en/products/accelerators/instinct/mi400.html)
12. [AAI 2026: AMD Delivers Full-Stack Compute for the Agentic AI Era](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)
13. [ADVANCING AI 2026（PDF）](https://newsroom.amd.com/documents/2026/07/2a710b7d-c107-4639-8855-fa9366f83967.pdf)
14. [AMD and Anthropic Announce Strategic Partnership](https://newsroom.amd.com/news/amd-anthropic-strategic-partnership/)
15. [AMD Instinct™ MI350 Series GPUs](https://www.amd.com/en/products/accelerators/instinct/mi350.html)
16. [AMD Instinct™ MI355X GPUs](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html)
17. [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x)
18. [Cloud TPU release notes](https://docs.cloud.google.com/tpu/docs/release-notes)
19. [AI infrastructure efficiency: Ironwood TPUs deliver 3.7x carbon efficiency gains](https://cloud.google.com/blog/topics/systems/ironwood-tpus-deliver-37x-carbon-efficiency-gains/)
20. [Our eighth generation TPUs: two chips for the agentic era](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
21. [Cloud Next '26: Momentum and innovation at Google scale](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)
22. [What's next in Google AI infrastructure: Scaling for the agentic era](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26)
23. [Announcing Amazon EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)
24. [Trainium3 UltraServers now available](https://www.aboutamazon.com/news/aws/trainium-3-ultraserver-faster-ai-training-lower-cost)
25. [Frontier agents, Trainium chips, and Amazon Nova: key announcements from AWS re:Invent 2025](https://www.aboutamazon.com/news/aws/aws-re-invent-2025-ai-news-updates)
26. [Intel Gaudi 3 AI Accelerators now available as a PCIe Card（PDF）](https://cdrdv2-public.intel.com/817488/Gaudi%203%20PCIe%20Product%20Brief_RB_1_V6.pdf)
27. [Intel®Gaudi® 3（Habana）](https://habana.ai/products/gaudi3/)
28. [华为汪涛：昇腾超节点部署超1000套，昇腾960芯片研发进度超预期（中国青年网）](http://t.m.youth.cn/transfer/index/url/news.youth.cn/jsxw/202609/t20260917_16874687.htm)
29. [华为公布昇腾AI芯片未来3年迭代路线图（人民日报客户端）](https://www.peopleapp.com/column/30050308165-500007097808)
30. [华为更新昇腾路线图：960DT上市比原计划提前三个季度（每日经济新闻）](http://m.toutiao.com/group/7686424720039805480/)
31. [科创板首家万亿市值公司诞生 寒武纪凭什么（证券时报）](https://www.stcn.com/article/detail/3991331.html)
32. [寒武纪2026年一季报核心数据（雪球）](https://xueqiu.com/9957756617/386778759)
33. [Maia 200: The AI accelerator built for inference](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)
34. [Maia 200: Software-defined dataflow and all-Ethernet networking](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/maia-200-software-defined-dataflow-and-all-ethernet-networking-for-efficient-inf/4548198)
35. [Expanding Meta's Custom Silicon to Power Our AI Workloads](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/)
36. [Meta Partners With Broadcom to Co-Develop Custom AI Silicon](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/)
37. [Micron in High-Volume Production of HBM4 Designed for NVIDIA Vera Rubin](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)
38. [High Bandwidth Memory (HBM): A Full Guide](https://www.insidedeeptech.com/high-bandwidth-memory-hbm-full-guide/)
39. [Department of Commerce Revises License Review Policy for Semiconductors Exported to China](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)
40. [Revision to License Review Policy for Advanced Computing Commodities（Federal Register）](https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities)
41. [NVIDIA SEC 文件（10-Q，2026-01-25）](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)