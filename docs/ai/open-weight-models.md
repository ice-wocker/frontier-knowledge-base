# 开放权重（开源）模型生态

> 最后更新：2026-09-26 ｜ 领域：人工智能 / 开放权重模型与本地部署 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 一、概述

「开放权重（open-weight）」指模型参数可公开下载、可自行部署与微调，区别于仅提供 API 的闭源模型。2025–2026 年，开放权重阵营从「追赶者」变为「半壁江山」：一方面，Meta Llama、阿里 Qwen、DeepSeek、Google Gemma、Mistral、微软 Phi、OpenAI gpt-oss、智谱 GLM、MiniMax、月之暗面 Kimi 等构成庞大的模型矩阵；另一方面，中国开源模型在 OpenRouter 等平台上的调用量持续领先。有分析称，截至 2026 年 3 月，OpenRouter 月度榜单前五名中有三席为中国模型，MiniMax、Kimi、DeepSeek 正成为全球开发者的优先选项，其优势可归纳为「开源、活跃、价格」三要素（[事关AI，中国首次超越美国 — 中新网](http://www.chinanews.com.cn/cj/2026/03-06/10582565.shtml)）。

Mozilla 于 2026 年 9 月发布的 **State of Open Source AI** 报告认为，开放权重模型已从「实验性替代品」转变为全球 AI 基础设施的关键支柱，驱动力来自性能快速提升、运营成本显著下降，以及企业对模型部署「主权与控制权」的空前需求（[Mozilla State of Open Source AI Report 2026](https://blognewstweets.com/mozilla-state-of-open-source-ai-report-2026-open-weight-models-move-from-experimentation-to-global-enterprise-dominance/)）。

需要澄清一个术语混淆：多数所谓「开源模型」实为**开放权重**，其许可证并非都通过 OSI 认证，例如 Llama 4 采用自定义的社区许可证，因而被明确指为「open-weight 但不是 OSI 认可的开源」（[Llama 4 — The Planet Tools](https://theplanettools.ai/tools/llama-4)）。更严格地说，真正的开源 LLM 应同时公开权重、架构，理想情况下还包括训练代码；而现实中多数模型仅公开权重，训练数据与训练代码通常不公开（[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)）。

## 二、2025–2026 最新进展

- **DeepSeek V4**：2026 年 4 月 24 日发布并开源 DeepSeek-V4 Preview，官方称其开启「高性价比 1M 上下文时代」，含 **V4-Pro（1.6T 总参数 / 49B 激活）** 与 **V4-Flash（284B / 13B 激活）** 两个 MoE 变体（[DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)）。模型卡明确开放仓库中的权重与代码采用 **MIT 许可证**（[DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)）。该系列建立在 token-wise compression 与 **DeepSeek Sparse Attention** 之上（[Open-Weights LLM Release History and Timeline](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html)）。2026 年 9 月 10 日又发布 **DeepSeek-V4.1-Flash**，具备原生多模态视觉理解能力，官方称 GPQA Diamond 达 90% 以上（[DeepSeek API 更新日志](https://api-docs.deepseek.com/zh-cn/updates/)）。此前的 DeepSeek V3.2 为 685B 总参数 / 37B 激活、MIT 相关许可（另有来源记为 671B/37B）（[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)、[React-ing to Grace Hopper 200](https://arxiv.org/pdf/2604.17187)）。
- **阿里 Qwen**：Qwen3.5 全系开放权重采用 **Apache 2.0** 许可，支持 201 种语言（[Qwen 3.5](https://qwen3lm.com/qwen3.5/)）。旗舰 **Qwen3.8-2.4T-A95B** 于 2026 年 8 月开源，稀疏 MoE 架构拥有 2.4T 总参数、每步约 95B 激活，搭配混合注意力与 1M 上下文（[qwen3.8-2.4t-a95b Model Info](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-2-4t-a95b)）。阿里云称其已开源 460 多个模型，衍生出 30 万以上衍生模型、累计下载超 30 亿次（[Alibaba Unveils Qwen3.8-27B and Releases Weights of Qwen3.8 Flagship Model](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463)）。近期版本还包括 Qwen3.5（2026-02-16，Apache-2.0，旗舰 397B 总参数 / 17B 激活，另有 27B 稠密版在 SWE-bench Verified 上以 72.4 追平 GPT-5 mini）（[Provider Landscape 2026-07](https://raw.githubusercontent.com/glamworks/glamfire/HEAD/research/25-provider-landscape-2026-07.md)）。
- **Google Gemma 4**：2026 年 3 月 31 日发布 Gemma 4（含 E2B/E4B 等移动优先型号），4 月 16 日推出 MTP 版本，6 月 3 日发布 **Gemma 4 12B Unified**（统一、无编码器的多模态模型），并衍生 DiffusionGemma 与 Gemma 4 QAT 量化版本；官方以 **Apache 2.0** 发布权重（[Gemma 版本 — Google AI for Developers](https://ai.google.dev/gemma/docs/releases)、[Gemma 4: Byte for byte, the most capable open models](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)）。
- **OpenAI gpt-oss**：OpenAI 于 2025 年 8 月 5 日发布 **gpt-oss-120b / gpt-oss-20b**，采用 **Apache 2.0** 许可，参数结构分别为 117B/5.1B 与 21B/3.6B，上下文 128K token（[Open-Weight AI Models 2026](https://www.progressiverobot.com/2026/08/13/open-weight-ai-models-2026/)）。官方帮助文档说明 Apache 2.0 允许广泛使用、修改与再分发（含商业用途，但受其 gpt-oss 使用政策约束），且这两个模型**不通过 OpenAI API 提供**（[OpenAI open-weight models (gpt-oss)](https://help.openai.com/fr-fr/articles/11870455-openai-open-weight-models-gpt-oss)）。
- **Mistral 与 MiniMax**：Mistral Large 3（2025 年 12 月）为 675B/41B MoE、256K 上下文、Apache 2.0（[Open-Weight AI Models 2026](https://www.progressiverobot.com/2026/08/13/open-weight-ai-models-2026/)）。MiniMax M2.5 于 2026 年 2 月 13 日全球开源并支持本地化部署（[MiniMax M2.5宣布全球开源并支持本地化部署 — 经济参考网](http://jjckb.xinhuanet.com/20260213/f083116f8a184cb4919d6b783df219ea/c.html)）；M3 于 2026 年 6 月发布；多模态生成模型 **MiniMax H3** 亦宣布开源（[MiniMax H3来了 — 上观新闻](http://m.toutiao.com/group/7668511907879354880/)）。
- **智谱 GLM 与月之暗面 Kimi**：GLM 系列以 MIT 许可密集迭代（GLM-5、GLM-5.1、GLM-5.2），GLM-5.1 为 754B 总参数 / 40B 激活（[React-ing to Grace Hopper 200](https://arxiv.org/pdf/2604.17187)、[Best Open-Source LLMs — aiwiki](https://aiwiki.ai/wiki/best_open_source_llms)）。月之暗面侧，Kimi K2.5 为 1T 总参数 / 32B 激活、MIT 许可（[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)），2026 年 9 月 21 日，月之暗面确认 **Kimi K3** 接入 Amazon Bedrock，全球企业开发者可直接调用（[北美云分成破冰，Kimi K3落地亚马逊Bedrock — 每日经济新闻](http://m.toutiao.com/group/7687957605545558562/)）。
- **小米 MiMo**：小米推出 **MiMo-V2-Flash**（309B/15B，MIT 许可）及 MiMo-V2.5 / V2.5-Pro（Apache-2.0），进入开放权重前沿阵营（[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)、[Best Open-Source LLM 2026 — Codersera](https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/)）。

## 三、核心技术与关键概念

### 1. 许可证类型

| 许可证 | 代表模型 | 特点 |
| --- | --- | --- |
| **Apache 2.0** | Qwen 3.5/3.8、Gemma 4、Mistral Large 3、gpt-oss、MiMo-V2.5 | 宽松，允许自由商用、修改、分发（通常要求署名） |
| **MIT** | DeepSeek V4、GLM-5/5.1/5.2、Kimi K2.5/K2.6、MiMo-V2-Flash | 宽松，开放仓库权重与代码，限制最少 |
| **Llama 社区许可** | Meta Llama 4 | 自定义商业许可，非 OSI 开源 |
| **Gemma Terms of Use** | Google Gemma（早期版本） | 允许多数用途，但限制损害 Google 产品的用途 |
| **无标准许可** | DeepSeek V3.2（部分口径） | 公开发布权重但无标准开源许可，商用需先审查 |

许可维度可拆解为四项：是否允许商用、是否允许微调、是否允许再分发、以及限制条款（[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)）。据 2026 年汇总，Mistral Large 3、Qwen3.5、Gemma 4 为 Apache-2.0，GLM-5.2、DeepSeek V4、Kimi K2.6 为 MIT 或 Modified MIT（[Best Open-Source LLMs — aiwiki](https://aiwiki.ai/wiki/best_open_source_llms)）。

**Llama 4 社区许可**的关键条款：月活超过 **7 亿** 的产品需向 Meta 单独申请许可（由其酌情授予）；衍生 AI 模型名称须含「Llama」；分发须显著标注「Built with Llama」并保留版权声明；可接受使用政策排除军事等用途（[Llama 4 许可说明](https://theplanettools.ai/tools/llama-4)、[Meta AI — aiwiki](https://aiwiki.ai/wiki/meta_ai)）。Llama 4 于 2025 年 4 月 5 日发布，为原生生多模态模型，Scout 版本上下文窗口达 **1000 万 token**，知识截止于 2024 年 8 月（[Llama 4](https://howaiworks.ai/models/llama)）。注：另有中文来源称 Llama 4 采用 Apache 2.0，与多数英文来源不符，本库以官方社区许可口径为准，读者引用时需交叉核对（[Meta Llama 4 全系列深度解析](https://blog.csdn.net/zsh_1314520/article/details/161386672)）。

### 2. 蒸馏与能力差距

**蒸馏（distillation）** 指用更强模型的输出训练另一个模型，是行业标准技术，在中国 AI 产业尤为普遍。据 Interconnects 分析，蒸馏大约能把中国公司相对美国前沿的差距缩小 **1–2 个月**（[The current balance of power in open models](https://www.interconnects.ai/p/the-current-balance-of-power-in-open)）。2026 年 2 月，Anthropic 披露三家中国实验室（DeepSeek、Moonshot、MiniMax）的「工业化规模」蒸馏活动，称其通过约 **24,000 个欺诈账号**产生了超过 **1600 万次交互**，以抽取 Claude 的推理、编码与智能体能力；Anthropic 与 OpenAI 随后将此类抽取定性为国家安全关切（[Everyone's Watching the Wrong Benchmark — Gradient](https://www.gradient.com/blog/posts/open-vs-closed-model-gap/)）。围绕此事的争论在于：闭源 API 本身可被系统性「挖矿」，而开放权重则让蒸馏变得「无需服务条款」即可进行（[What Is AI Distillation?](https://www.explainx.ai/blog/what-is-ai-distillation-knowledge-transfer-fable-5-2026)、[In Defense of Open Models — IDC](https://www.idc.com/resource-center/blog/in-defense-of-open-models-kimi-k3-distillation-and-the-future-of-intelligence/)）。

### 3. 本地部署与量化

**llama.cpp**（MIT 许可，GitHub 星标 85,000+）是本地推理生态的基石：纯 C/C++、无外部依赖，可在 NVIDIA CUDA、AMD ROCm、Apple Metal、纯 CPU 乃至 Raspberry Pi 上运行 **GGUF** 量化模型（[The Complete Guide to Local LLM Inference Tools in July 2026](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)）。典型量化档位的质量/体积权衡（以 7B 模型为例）：F16 14GB（基准）、Q8_0 8.5GB（约 99% 质量）、Q4_K_M 5.0GB（约 97%）、Q3_K_M 4.1GB（约 94%）（[Running LLMs Locally in 2026](https://technologypulse.app/2026-04-28-local-llm-guide-2026/)）。**Ollama** 与 **LM Studio** 则封装了 GGUF 的选择与运行，降低使用门槛（[GGUF Quantization Benchmarks](https://vucense.com/dev-corner/gguf-quantization-explained-q4-k-m-vs-q8-0-vs-f16-2026/)）。

工具选型上，**GGUF**（Q4_K_M、Q5_K_M、Q6_K、Q8_0 等「K-quants」按层混合位深，单文件自包含）最适合 CPU、消费级 GPU 与 Apple Silicon，是通用且可移植的默认；**AWQ（INT4）** 与 GPTQ 面向 GPU 服务，在多数基准中 AWQ 的质量保持略优于 GPTQ（[Running LLMs Locally in 2026 — DEV](https://dev.to/daviducolo/running-llms-locally-in-2026-the-complete-guide-to-benefits-trade-offs-and-getting-started-32k)）。在吞吐与多用户服务场景，**vLLM** 支持最广的格式范围（safetensors、GPTQ、AWQ、FP8、NVFP4、bitsandbytes），在 NVIDIA 硬件上 GPU 优化的量化格式（如 AWQ）通常比 GGUF 吞吐更高，但生产环境仅支持 Linux 且需要独立 NVIDIA/AMD GPU，配置复杂度高于 Ollama（[Local LLM Inference in 2026](https://blog.starmorph.com/blog/local-llm-inference-tools-guide)）。

### 4. 开放权重 vs 闭源：主权、合规与成本

选择开放权重的常见动机有三：**数据主权**（提示、文档与输出不离开自有服务器，无跨境传输与第三方保留策略）、**合规**（对受 HIPAA 约束的医疗数据、PCI-DSS/SOC 2 约束的金融数据，自托管可让 PHI 留在合规范畴内；在欧盟 AI Act 语境下，本地部署便于保留审计痕迹）（[Open-Weight vs. Closed-Source AI Models in 2026](https://www.sabaoon.dev/blog/open-weight-vs-closed-source-ai-2026)、[Open-Source AI Deployment for Enterprises (2026 Guide)](https://www.fleeceai.agency/blog/open-source-ai-deployment-for-enterprises)），以及**成本可预测**（没有按 token 计费，高并发重复负载的边际成本低）（[Best Open-Weights AI Models for Business in 2026](https://www.layer3labs.io/open-weights/best-open-weights-ai-models)）。相应地，自托管也意味着企业需自行承担硬件、运维与安全责任。

### 5. 许可与能力的「口径之争」

「开放权重已追平闭源」这一判断高度依赖所选的基准与版本：同一族模型在不同评测快照中的排名可能不一致。例如 DeepSeek-V4-Pro 在 SWE-bench 上为 80.6%、LiveCodeBench 93.5%、原生 1M 上下文（[Best Open Source AI Models in 2026](https://felloai.com/pt/best-open-source-ai-models/)），而 GLM-5.2 在开源模型中 GPQA Diamond 最高（91.2%），Kimi K2.6 以 90.5% 紧随（[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)）。因此引用任何「领先」结论时都应同时标注基准、版本与时间。

### 6. 「完全开放」模型：OLMo 3 与训练流程透明化

「开放权重」之外还有一类更彻底的路线：**完全开放（fully open）**，即不仅公开权重，还公开训练数据、代码、中间 checkpoint 与训练流程。代表是 Allen Institute for AI（Ai2）的 **OLMo 3**：2025 年 11 月 20 日发布，包含 7B 与 32B 两个参数规模的稠密 decoder-only Transformer，每个规模各有 Base、Think、Instruct、RL Zero 四个后训练变体，其中 32B Think 被称为首个「完全开放的 32B 思考模型」（[Ai2 Announces Olmo 3 Family of Open Frontier Language Models](https://www.hpcwire.com/bigdatawire/this-just-in/ai2-announces-olmo-3-family-of-open-frontier-language-models/)、[Ai2 Introduces Olmo 3 — MarkTechPost](https://www.marktechpost.com/2025/11/20/allen-institute-for-ai-ai2-introduces-olmo-3-an-open-source-7b-and-32b-llm-family-built-on-the-dolma-3-and-dolci-stack/)）。其预训练使用全新的 **Dolma 3** 数据集，约 9.3 万亿 token，来源涵盖网页、经 olmOCR 处理的科学论文 PDF、代码仓库与数学题（[Completely Breaking Down the AI Black Box: Ai2 Releases Olmo 3](https://www.communeify.com/en/blog/ai2-olmo-3-ai-black-box-breakthrough-full-transparency/)）。这类项目价值在于可复现与可审计，与商业「开放权重」形成对照。

### 7. 开放权重的安全风险：护栏移除（abliteration）

开放权重带来便利的同时也带来一类结构性风险：**护栏可被后训练移除**。一项由 University of Waterloo 与 FAR.AI 合作的 **TamperBench** 基准测试发现，21 个热门开放权重模型（包括经过防御加固的版本）全部可借微调或激活编辑（activation editing）攻击剥除其安全调优（[TamperBench: All 21 Tested Open-Weight LLMs Had Guardrails Stripped](https://www.pyramidledger.com/blog/tamperbench-all-21-tested-open-weight-llms-had-guardrails-stripped)）。Anthropic CEO 亦对立法者表示，开源模型构成系统性安全风险，理由是任何拥有适度 GPU 资源的行为者都能微调移除 RLHF 与 Constitutional AI 对齐层，且研究多次显示用不到 1000 条恶意样本即可显著削弱安全对齐，从而把「越狱」从提示工程问题变成无防御对策的模型修改问题（[Anthropic CEO: Open-Source AI Models Pose Systemic Safety Risk](https://gridthegrey.com/posts/first-look-anthropic-ceo-warns-lawmakers-open-source-ai-poses-safety-control/)）。西点军校 CTC 的评论称之为 **abliteration 问题**：由于开放权重模型的护栏很可能对所有人可移除，模型一旦发布就可能「不可逆」，因此建议在开源前做 abliteration 抗性测试（[Guardrails Under Test: Terrorist Misuse of AI Models and the Open-Weight 'Abliteration' Problem](https://ctc.westpoint.edu/feature-commentary-guardrails-under-test-terrorist-misuse-of-ai-models-and-the-open-weight-abliteration-problem/)）。相关研究进一步表明，现有开放权重安全防护对 **abliteration** 与 **prefilling** 两类低成本、非梯度优化攻击同样脆弱（[Open-Weight LLM Fine-Tuning Defenses are Susceptible to Simple Attacks](https://arxiv.org/html/2605.26526v1)）。也有观点认为，抗移除设计无法根除滥用，但能显著抬高攻击成本、改变滥用经济学（[What Does Safe AI Mean for Open-Weight LLMs When Fine-Tuning Strips Guardrails?](https://aitechinspire.com/what-does-safe-ai-mean-for-open-weight-llms-when-fine-tuning-strips-guardrails/)）。

## 四、代表性项目 / 产品

| 模型系列 | 开发者 | 代表版本 | 官方链接 |
| --- | --- | --- | --- |
| Llama | Meta | Llama 4（Scout / Maverick） | https://www.llama.com/ |
| DeepSeek | 深度求索 | V4-Pro / V4-Flash / V4.1-Flash | https://api-docs.deepseek.com/news/news260424 |
| Qwen | 阿里巴巴 | Qwen3.8 / Qwen3.5 / Qwen3-VL / Qwen3-Omni | https://qwen.ai/ |
| Gemma | Google DeepMind | Gemma 4 | https://deepmind.google/models/gemma/ |
| Mistral | Mistral AI | Mistral Large 3 | https://mistral.ai/ |
| gpt-oss | OpenAI | gpt-oss-120b / 20b | https://openai.com/index/introducing-gpt-oss/ |
| GLM | 智谱 AI | GLM-5.3 Flash / GLM-5.2 / GLM-5.1 | https://www.zhipuai.cn/ |
| MiniMax | MiniMax | M2.5 / M3 / H3 | https://www.minimax.io/ |
| Kimi | 月之暗面 | Kimi K3 / K2.6 / K2.5 | https://www.moonshot.cn/ |
| MiMo | 小米 | MiMo-V2-Flash | https://github.com/XiaomiMiMo |
| Phi | 微软 | Phi 系列 | https://azure.microsoft.com/en-us/products/phi |

## 五、关键数据与评测结果

**Onyx 开放 LLM 排行榜快照（更新于 2026-03-12）**：

| 模型 | 提供方 | 许可 | 参数（总/激活） | SWE-bench | GPQA Diamond | AIME 2025 | HumanEval | Arena Elo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kimi K2.5 | Moonshot | MIT | 1T / 32B | 76.8% | 87.6% | 96.1% | 99.0% | 1,447 |
| GLM-5 | Zhipu AI | MIT | 744B / 40B | 77.8% | 86.0% | 84.0% | 90.0% | 1,451 |
| Qwen 3.5 | Qwen | Apache 2.0 | 397B / 17B | 76.4% | 88.4% | N/A | N/A | N/A |
| MiMo-V2-Flash | Xiaomi | MIT | 309B / 15B | 73.4% | 83.7% | 94.1% | 84.8% | 1,401 |
| DeepSeek V3.2 | DeepSeek | 无标准许可 | 685B / 37B | 67.8% | 79.9% | 89.3% | N/A | 1,421 |
| GPT-oss 120B | OpenAI | Apache 2.0 | 117B / 5.1B | 62.4% | 80.9% | 97.9% | 88.3% | 1,354 |

（数据来源：[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)；该快照中「无单一赢家」——Kimi K2.5 领先 HumanEval 与 AIME，GLM-5 领先 SWE-bench，Qwen 3.5 领先 GPQA Diamond。）

- **调用量**：中国 AI 大模型调用量连续十九周领跑，环比增长 **379%**；某周榜单中 GPT-5.6 Luna 以 12.9 万亿 Token 居第二、智谱 GLM-5.3 Flash 以 12.4 万亿 Token 升至第三、DeepSeek-V4-Flash（0731 正式版）同以 12.4 万亿 Token 居第四（[每日经济新闻](http://m.toutiao.com/group/7682613135580086825/)）。
- **性价比**：中信建投研报称国产模型 MiniMax M2.5 性能比肩 Claude Opus 4.6，但价格仅为其 **1/6–1/20**（[中新网](http://www.chinanews.com.cn/cj/2026/03-06/10582565.shtml)）。
- **能力差距**：有分析给出开放权重模型达到闭源基准分数的 **91%**，且推理成本低 **8–12 倍**（[Open Source Models Closed the Gap](https://arjunjaggi.com/blog/open-source-models-closed-the-gap)）。
- **DeepSeek V4.1-Flash**：官方称 GPQA Diamond 达 **90% 以上**（[DeepSeek API 更新日志](https://api-docs.deepseek.com/zh-cn/updates/)）；DeepSeek V4-Pro 在 SWE-Bench Verified 为 80.6、LiveCodeBench 93.5（[Best Open Source AI Models in 2026](https://felloai.com/pt/best-open-source-ai-models/)）。
- **Qwen3.8-2.4T-A95B 核心基准**：GPQA Diamond 92.6、PaperBench 93.0、OSWorld 86.1、BabyVision 82.0（[阿里云百炼模型信息](https://help.aliyun.com/zh/model-studio/qwen3-8-2-4t-a95b)）；另有来源记为 SWE-bench Pro 67.7、Terminal Bench 2.1 86.6、DeepSWE 1.1 56.6，API 定价约输入 $2.00 / 输出 $6.00 每百万 token（[Open-Weight AI Models 2026](https://www.progressiverobot.com/2026/08/13/open-weight-ai-models-2026/)）。
- **代码模型横向对比**：在一项以 GH200 为硬件、用五个开放权重代码模型构建同一 React Native 应用的研究中，GLM-5.1（754B/40B 激活，MIT）取得 58.4% 的 state-of-the-art；Kimi-K2.5（1T/32B）、DeepSeek-V3.2（671B/37B）、Qwen3-Coder-480B（480B/35B）彼此仅相差几个基准点，且该研究指出 SWE-Bench 排名未能预测哪个模型真正完成交付（[React-ing to Grace Hopper 200](https://arxiv.org/pdf/2604.17187)）。

**生态规模与份额（多口径并列）**：

- **Hugging Face 下载格局**：一份 Hub 生态分析显示，领跑者不是 Meta、Google 或 OpenAI，而是阿里 Qwen——其头部模型合计约 **3.994 亿次下载**，占 top-1000 流量的 **18.5%**，约为 Google 的 4 倍；top 模型中 **71.5%** 采用宽松开源许可，仅 **Apache 2.0** 就占 **49%**；前 5 家组织合计占约 **46%**（[Hugging Face Hub State 2026: Qwen Leads, Apache 2.0 Wins](https://zentor.ai/blog/huggingface-hub-state-2026)）。
- **Qwen 生态规模**：另一口径称 Qwen 在 Hugging Face 的累计下载已超 **10 亿次**，带 Qwen 标签的衍生模型超过 **20 万**、微调超过 **11.3 万**，超过 Google 与 Meta 基座模型家族之和；平台上约 **40%** 的新 LLM 衍生模型基于 Qwen；过去一年中国约占 Hub 全部下载量的 **41%**（[Hugging Face's 2026 Open-Model Report: Qwen Hits 3B Downloads](https://www.chinaon.ai/stories/huggingface-2026-open-model-report-qwen-3b-downloads-chinese-models-tokenusage-august2026.html)）。
- **推理用量**：在 OpenRouter 上，开放模型每周生成的 token 量从 2025 年 9 月的约 **1 万亿**增至 2026 年 9 月的约 **80 万亿**；同期中国模型在该平台的份额从约 **70%** 升至 **80% 以上**；面向编码的智能体平台 OpenCode 有 **95% 以上**的推理流量直接路由到中国开放权重模型（[China Leads Open AI Models With 3.2B Downloads, Congress Told](https://www.aibreakingwire.com/news/china-leads-open-ai-models-with-32b-downloads-congress-told)）。
- **下载模型规模变化**：据 Hugging Face《State of Open Source on Hugging Face: Spring 2026》（2026-03-17 发布），被下载开放模型的平均规模从 2023 年的 827M 参数增至 2025 年的 **20.8B** 参数，中位数从 326M 变为 **406M**（[Open Source AI Model Download Statistics 2026](https://commandlinux.com/statistics/open-source-ai-model-downloads/)）。

## 六、趋势与争议

1. **开源 vs 闭源的边界之争**：支持者认为开放权重降低推理成本、增强数字主权与可审计性（Google 称 Apache 2.0 发布 Gemma 4 是「巨大里程碑」，赋予开发者数字主权）（[Gemma 4 韩文博客](https://blog.google/intl/ko-kr/company-news/technology/gemma-4-kr/)）；反对者（如 Anthropic、OpenAI）担忧滥用与知识产权问题。Mozilla 报告则从产业侧指出，主权与控制权需求正推动开放权重进入企业主流部署（[Mozilla State of Open Source AI Report 2026](https://blognewstweets.com/mozilla-state-of-open-source-ai-report-2026-open-weight-models-move-from-experimentation-to-global-enterprise-dominance/)）。
2. **蒸馏的合法性与安全叙事**：IDC 指出闭源厂商本就控制着被「蒸馏」系统的访问权、条款与自动化行为模式，把开放模型一律限制并不合理（[In Defense of Open Models](https://www.idc.com/resource-center/blog/in-defense-of-open-models-kimi-k3-distillation-and-the-future-of-intelligence/)）。开放权重使蒸馏「无需服务条款」即可进行，这一特性既是其生态优势，也成为安全争议焦点（[What Is AI Distillation?](https://www.explainx.ai/blog/what-is-ai-distillation-knowledge-transfer-fable-5-2026)）。
3. **许可证合规风险**：Llama 社区许可的 7 亿 MAU 门槛、命名与署名要求，使「开源」在法务上并非无约束；同类风险也存在于各家的自定义许可（如 Gemma Terms of Use、部分无标准许可的权重发布），企业采用前需评估（[Llama 4 许可说明](https://theplanettools.ai/tools/llama-4)、[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)）。
4. **中国模型的全球博弈**：模型出海伴随云厂商分成等商业机制变化，分析师提醒当多个同质化中国模型供应商竞争同一分销渠道时，议价地位可能反转（[每日经济新闻](http://m.toutiao.com/group/7687957605545558562/)）。
5. **部署门槛与「本地」的现实边界**：多数前沿开放权重模型仍需企业级硬件（如 4×H100 80GB 或同等）才能全精度推理；真正可在单卡运行的替代品有限，例如 GPT-oss 120B（1×H100）与 DeepSeek R1 蒸馏版（DS-R1-Distill-Qwen-32B、DS-R1-Distill-Llama-70B，可跑在单张 RTX 4090 或 H100）（[Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)）。这使「开放权重＝人人可本地运行」的叙事需要更细的硬件前提。
6. **「开放即不可逆」的安全争论**：TamperBench 等研究表明护栏可被微调/激活编辑剥离，西点 CTC 由此提出开放权重一旦发布可能「不可逆」，主张在开源前进行 abliteration 抗性测试；而开放阵营则强调可审计性与防滥用设计能改变攻击经济学（[TamperBench](https://www.pyramidledger.com/blog/tamperbench-all-21-tested-open-weight-llms-had-guardrails-stripped)、[Guardrails Under Test — West Point CTC](https://ctc.westpoint.edu/feature-commentary-guardrails-under-test-terrorist-misuse-of-ai-models-and-the-open-weight-abliteration-problem/)、[What Does Safe AI Mean for Open-Weight LLMs](https://aitechinspire.com/what-does-safe-ai-mean-for-open-weight-llms-when-fine-tuning-strips-guardrails/)）。这一争论把「开放 vs 闭源」从商业模式问题推向安全治理问题。
7. **生态汇聚与单点依赖**：Hugging Face 与 OpenRouter 的多份统计都显示 Qwen 生态与部分中国实验室已形成高度集中的下载与用量份额（[Hugging Face Hub State 2026](https://zentor.ai/blog/huggingface-hub-state-2026)、[China Leads Open AI Models](https://www.aibreakingwire.com/news/china-leads-open-ai-models-with-32b-downloads-congress-told)）。集中化在降低使用门槛的同时，也带来供应链与治理上的单点依赖风险。

## 参考来源

1. [Open-Weight AI Models 2026: Complete Guide to the Best](https://www.progressiverobot.com/2026/08/13/open-weight-ai-models-2026/)
2. [Open-Weights LLM Release History and Timeline](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html)
3. [DeepSeek V4 Preview Release — DeepSeek API Docs](https://api-docs.deepseek.com/news/news260424)
4. [DeepSeek V4 Technical Documentation (Model Card)](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)
5. [DeepSeek API 更新日志（V4.1-Flash）](https://api-docs.deepseek.com/zh-cn/updates/)
6. [Build with DeepSeek V4 Using NVIDIA Blackwell](https://developer.nvidia.com/blog/build-with-deepseek-v4-using-nvidia-blackwell-and-gpu-accelerated-endpoints)
7. [Qwen 3.5: The Next Generation of Open AI](https://qwen3lm.com/qwen3.5/)
8. [qwen3.8-2.4t-a95b Model Info — Alibaba Cloud Model Studio](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-2-4t-a95b)
9. [Alibaba Unveils Qwen3.8-27B and Releases Weights of Qwen3.8 Flagship Model](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463)
10. [qwen3.8-2.4t-a95b 模型信息 — 阿里云百炼](https://help.aliyun.com/zh/model-studio/qwen3-8-2-4t-a95b)
11. [Gemma 版本 — Google AI for Developers](https://ai.google.dev/gemma/docs/releases)
12. [Gemma 4: Byte for byte, the most capable open models — Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
13. [Gemma 4 — Google DeepMind](https://deepmind.google/models/gemma/gemma-4/)
14. [Gemma 4 소개 (Apache 2.0) — Google Blog](https://blog.google/intl/ko-kr/company-news/technology/gemma-4-kr/)
15. [Llama 4 — howaiworks.ai](https://howaiworks.ai/models/llama)
16. [Llama 4 License 说明 — The Planet Tools](https://theplanettools.ai/tools/llama-4)
17. [Meta AI — aiwiki.ai](https://aiwiki.ai/wiki/meta_ai)
18. [Meta Llama 4 全系列深度解析 — CSDN](https://blog.csdn.net/zsh_1314520/article/details/161386672)
19. [MiniMax M2.5宣布全球开源并支持本地化部署 — 经济参考网](http://jjckb.xinhuanet.com/20260213/f083116f8a184cb4919d6b783df219ea/c.html)
20. [MiniMax H3来了 — 上观新闻](http://m.toutiao.com/group/7668511907879354880/)
21. [中国AI大模型调用量连续十九周领跑 — 每日经济新闻](http://m.toutiao.com/group/7682613135580086825/)
22. [事关AI，中国首次超越美国 — 中新网](http://www.chinanews.com.cn/cj/2026/03-06/10582565.shtml)
23. [北美云分成破冰，Kimi K3落地亚马逊Bedrock — 每日经济新闻](http://m.toutiao.com/group/7687957605545558562/)
24. [The current balance of power in open models — Interconnects](https://www.interconnects.ai/p/the-current-balance-of-power-in-open)
25. [Everyone's Watching the Wrong Benchmark — Gradient](https://www.gradient.com/blog/posts/open-vs-closed-model-gap/)
26. [What Is AI Distillation? — ExplainX](https://www.explainx.ai/blog/what-is-ai-distillation-knowledge-transfer-fable-5-2026)
27. [In Defense of Open Models: Kimi K3, Distillation — IDC](https://www.idc.com/resource-center/blog/in-defense-of-open-models-kimi-k3-distillation-and-the-future-of-intelligence/)
28. [Open Source Models Closed the Gap](https://arjunjaggi.com/blog/open-source-models-closed-the-gap)
29. [The Complete Guide to Local LLM Inference Tools in July 2026](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)
30. [GGUF Quantization Benchmarks: Q4_K_M vs Q8_0 vs F16 (2026)](https://vucense.com/dev-corner/gguf-quantization-explained-q4-k-m-vs-q8-0-vs-f16-2026/)
31. [Running LLMs Locally in 2026: Ollama, LM Studio, llama.cpp](https://technologypulse.app/2026-04-28-local-llm-guide-2026/)
32. [GGUF - llama.cpp 的量化格式 — ModelScope](https://www.modelscope.cn/skills/@davila7/optimization-gguf)
33. [Best Open Source LLMs in 2026 — Onyx](https://onyx.app/insights/best-open-source-llms-2026)
34. [Onyx Open LLM Leaderboard](https://onyx.app/open-llm-leaderboard)
35. [Best Open-Source LLMs — aiwiki.ai](https://aiwiki.ai/wiki/best_open_source_llms)
36. [Best Open-Source LLM 2026: Llama 4, DeepSeek V4, Qwen, Kimi — Codersera](https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/)
37. [Best Open Source AI Models in 2026, Ranked and Compared — Fello AI](https://felloai.com/pt/best-open-source-ai-models/)
38. [React-ing to Grace Hopper 200: Five Open-Weights Coding Models](https://arxiv.org/pdf/2604.17187)
39. [Provider Landscape 2026-07 (Qwen family)](https://raw.githubusercontent.com/glamworks/glamfire/HEAD/research/25-provider-landscape-2026-07.md)
40. [OpenAI open-weight models (gpt-oss) — OpenAI Help](https://help.openai.com/fr-fr/articles/11870455-openai-open-weight-models-gpt-oss)
41. [Mozilla State of Open Source AI Report 2026](https://blognewstweets.com/mozilla-state-of-open-source-ai-report-2026-open-weight-models-move-from-experimentation-to-global-enterprise-dominance/)
42. [Open-Weight vs. Closed-Source AI Models in 2026 — Sabaoon](https://www.sabaoon.dev/blog/open-weight-vs-closed-source-ai-2026)
43. [Open-Source AI Deployment for Enterprises (2026 Guide) — Fleece AI](https://www.fleeceai.agency/blog/open-source-ai-deployment-for-enterprises)
44. [Best Open-Weights AI Models for Business in 2026 — Layer3 Labs](https://www.layer3labs.io/open-weights/best-open-weights-ai-models)
45. [Running LLMs Locally in 2026: Benefits, Trade-offs — DEV](https://dev.to/daviducolo/running-llms-locally-in-2026-the-complete-guide-to-benefits-trade-offs-and-getting-started-32k)
46. [Local LLM Inference in 2026: Tools, Hardware & Open-Weight Models — Starmorph](https://blog.starmorph.com/blog/local-llm-inference-tools-guide)
47. [Open Weights AI: Your Strategic Compliance Hedge — FluxHuman](https://fluxhuman.com/en/blog/open-weights-ai-your-strategic-compliance-hedge)
48. [Best Local & Open-Weight LLMs (2026) — AIToolTier](https://aitooltier.com/categories/ai-local-models)
49. [Ai2 Announces Olmo 3 Family of Open Frontier Language Models — HPCwire](https://www.hpcwire.com/bigdatawire/this-just-in/ai2-announces-olmo-3-family-of-open-frontier-language-models/)
50. [Allen Institute for AI (AI2) Introduces Olmo 3 — MarkTechPost](https://www.marktechpost.com/2025/11/20/allen-institute-for-ai-ai2-introduces-olmo-3-an-open-source-7b-and-32b-llm-family-built-on-the-dolma-3-and-dolci-stack/)
51. [Completely Breaking Down the AI Black Box: Ai2 Releases Olmo 3](https://www.communeify.com/en/blog/ai2-olmo-3-ai-black-box-breakthrough-full-transparency/)
52. [OLMo 3 — aiwiki.ai](https://aiwiki.ai/wiki/olmo_3)
53. [美艾伦AI研究所发布Olmo 3系列AI模型 — 中国科学院网信工作网](https://ecas.cas.cn/xxkw/kbcd/201115_148603/ml/xxhjsyjcss/202512/t20251229_5094404.html)
54. [TamperBench: All 21 Tested Open-Weight LLMs Had Guardrails Stripped](https://www.pyramidledger.com/blog/tamperbench-all-21-tested-open-weight-llms-had-guardrails-stripped)
55. [Anthropic CEO: Open-Source AI Models Pose Systemic Safety Risk](https://gridthegrey.com/posts/first-look-anthropic-ceo-warns-lawmakers-open-source-ai-poses-safety-control/)
56. [Guardrails Under Test: Terrorist Misuse of AI Models and the Open-Weight 'Abliteration' Problem — West Point CTC](https://ctc.westpoint.edu/feature-commentary-guardrails-under-test-terrorist-misuse-of-ai-models-and-the-open-weight-abliteration-problem/)
57. [Open-Weight LLM Fine-Tuning Defenses are Susceptible to Simple Attacks](https://arxiv.org/html/2605.26526v1)
58. [What Does Safe AI Mean for Open-Weight LLMs When Fine-Tuning Strips Guardrails?](https://aitechinspire.com/what-does-safe-ai-mean-for-open-weight-llms-when-fine-tuning-strips-guardrails/)
59. [Hugging Face Hub State 2026: Qwen Leads, Apache 2.0 Wins — Zentor](https://zentor.ai/blog/huggingface-hub-state-2026)
60. [Hugging Face's 2026 Open-Model Report: Qwen Hits 3B Downloads](https://www.chinaon.ai/stories/huggingface-2026-open-model-report-qwen-3b-downloads-chinese-models-tokenusage-august2026.html)
61. [China Leads Open AI Models With 3.2B Downloads, Congress Told](https://www.aibreakingwire.com/news/china-leads-open-ai-models-with-32b-downloads-congress-told)
62. [Open Source AI Model Download Statistics 2026 [Llama, Mistral And DeepSeek]](https://commandlinux.com/statistics/open-source-ai-model-downloads/)