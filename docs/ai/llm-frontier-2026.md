# 通用大模型前沿格局（2025–2026）

> 最后更新：2026-09-26 ｜ 领域：人工智能·大语言模型 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

截至 2026 年 9 月，通用大模型（frontier LLM）的竞争格局已从"单一旗舰迭代"演变为"多厂商、多层次、按月刷新"的密集竞赛。头部厂商包括 OpenAI、Anthropic、Google DeepMind、xAI（后并入 SpaceX 体系）、Meta，以及中国的 DeepSeek、阿里云 Qwen、月之暗面 Kimi、字节跳动豆包、智谱 GLM 等。共同趋势是：旗舰模型普遍走向混合专家（MoE）稀疏架构、原生多模态、百万 token 级上下文窗口，以及把"思考（thinking）"能力内建为可按档位调节的推理模式，而非外挂的提示技巧。

进入 2026 年下半年，格局又出现两个新特征：其一是**分层发布**，同一厂商同时推出面向不同负载的多个型号（如 OpenAI 的 GPT-6 Sol 与 Luna），厂商公开建议按任务复杂度在多档模型间路由，而非只用单一旗舰（[GPT-6 Luna vs Gemini 3.8 Flash vs Claude Opus 5.5](https://www.sentisight.ai/gpt-6-luna-vs-gemini-3-8-flash-vs-claude-opus-5-5/)）；其二是**开放权重阵营的实质性逼近**，Kimi K3、GLM-5.2、DeepSeek V4 等以 MIT 系许可开放权重，在部分榜单上已与闭源旗舰同处第一梯队。与此同时，API 定价持续下探，前沿能力的获取门槛显著降低。

从发布事件的密度看，2026 年 9 月尤为集中：OpenAI 于 9 月 3 日发布 GPT-6 Astra，Anthropic 与 OpenAI 于 9 月 22 日几乎同日推出 Claude Opus 5.5 与 GPT-6 Sol/Luna，xAI 则于 9 月 21 日发布 Grok 4.7（[GPT-6 Sol与Claude Opus 5.5同日开打，谁是「性价比之王」-36氪](https://m.36kr.com/p/3995195771588745)）。

## 2025–2026 最新进展

### OpenAI GPT 系列

OpenAI 于 2025 年 12 月 11 日发布 GPT-5.2，被视为针对 Gemini 3 的市场反击，主打专业知识工作，即编程、数据分析与复杂推理（[Strategic Analysis of Frontier AI Models: GPT-5.2 vs. Gemini 3](https://ironcrestsoftware.com/assets/pdfs/ai-model-comparison-chatgpt-vs-gemini.pdf)）。随后 GPT-5.5 于 2026 年 4 月 23 日推出（[GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1 Pro: The Frontier Model Showdown](https://dev.to/om_shree_0709/gpt-55-vs-claude-opus-47-vs-gemini-31-pro-the-frontier-model-showdown-4mji)），其官方对比表显示在 GDPval（胜或平）达 84.9%、OSWorld-Verified 达 78.7%、Toolathlon 达 55.6%（[Presentamos GPT‑5.5](https://openai.com/es-ES/index/introducing-gpt-5-5/)）。2026 年 6 月 26 日，OpenAI 开始对 GPT-5.6 系列（代号 Sol）进行有限预览，强调更强的网络安全能力与分层防护（[预览 GPT‑5.6 Sol：新一代模型](https://openai.com/zh-Hans-CN/index/previewing-gpt-5-6-sol/)）。

关于 GPT-6，OpenAI 官方研究索引给出两条时间线：一条标注"研究 2026 年 9 月 3 日 GPT-6 Astra：新一代智能"，另一条标注"产品 2026 年 9 月 22 日 隆重推出 GPT-6 Sol 和 Luna"（[OpenAI 研究](https://openai.com/zh-Hans-CN/research/index/)）；而 OpenAI 中文页面对 Astra 的发布页则为《GPT-6 Astra：新一代智能》（[GPT-6 Astra：新一代智能](https://openai.com/zh-Hans-CN/index/gpt-6-astra/)）。由于不同页面口径存在差异，Astra 的准确首发日期应以官方索引与其新闻页为准，不宜单一采信。Astra 被描述为"迄今智能程度最高、最符合人类意图的模型，在计算机操作、编程、网络安全和科学领域具备前沿能力"（[OpenAI 研究](https://openai.com/zh-Hans-CN/research/index/)）。据 NVIDIA CEO 黄仁勋 9 月 6 日透露，GPT-6 Astra 的训练动用了约 10 万块 Grace Blackwell 系列 GPU，并计划再追加 40 万块用于后续阶段（[GPT-6 Astra : 100 000 GPU Nvidia pour entraîner le modèle](https://overclocking.com/gpt-6-astra-100000-gpu-nvidia-prix-ram/)）。

多个第三方来源把 Astra 的发布时间记为 2026 年 9 月 3 日：ThursdAI 的记录称 OpenAI 在直播中发布 GPT-6 Astra，总裁 Greg Brockman 对记者表示"欢迎来到 AGI 时代"，并报告 ARC-AGI-3 为 99.9、FrontierMath Tier 4 为 97.6%（[Frontier Models](https://thursdai.news/topics/frontier-models)）；howaiworks 给出 97.6%（FrontierMath Tier 4 v2）与 ExploitBench 100%（[OpenAI Launches GPT-6 Astra With Record Benchmarks](https://howaiworks.ai/blog/openai-gpt-6-astra-launch-2026)）。DataCamp 补充称，Astra 在 FrontierMath Tier 4 v2 得 97.6%，高于 Claude Fable 5.1 与 Fable 5 的 87.8% 及 Claude Opus 5 的 73.2%，OpenAI 把这一水平描述为"饱和"（[GPT-6 Astra: Features, Benchmarks, and Pricing](https://www.datacamp.com/ko/blog/gpt-6-astra)）。需注意一个重要的口径警示：ARC-AGI-3 的高分是在 OpenAI 自有 Provider Adapter 测试框架下取得，该框架会在请求间保留推理状态；独立报道指出在标准公开 ARC-AGI 框架下分数明显更低（[GPT-6 Astra Review: Benchmarks, Pricing, Safety](https://aitoolsreview.co.uk/insights/gpt-6-astra-review)）。至于 9 月 22 日的分层发布，36氪 报道称 GPT-6 Sol 与 GPT-6 Luna 脱胎于 GPT-6 Astra 底座，重点是把 Astra 的核心推理与多模态优势下放（[GPT-6 Sol与Claude Opus 5.5同日开打，谁是「性价比之王」-36氪](https://m.36kr.com/p/3995195771588745)）。

### Anthropic Claude 系列

Anthropic 的旗舰迭代尤为密集。Claude Opus 4.8 于 2026 年 5 月 28 日发布，定位严肃编程与 AI agent，配备 100 万 token 上下文窗口（[Claude Opus \ Anthropic](https://www.anthropic.com/claude/opus)）。2026 年 6 月 25 日，Anthropic 同时推出 Claude Fable 5（面向全体客户的最强模型）与 Claude Mythos 5（仅限 Project Glasswing 参与者），两者默认支持 100 万 token 上下文、128k 最大输出，并采用"always-on adaptive thinking"（[Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)）。Fable 5.1 与 Mythos 5.1 共享同一底层模型，Fable 侧保留针对网络安全与生物领域的更精确防护（[Claude Mythos 5](https://www.anthropic.com/claude/mythos)）。

2026 年 9 月 22 日，Claude Opus 5.5 发布，面向长时间运行的 agentic 编程与知识工作，100 万 token 上下文、128k 最大输出，定价为输入 $4/百万 token、输出 $20/百万 token（[Claude Opus 5.5 - Claude Platform Docs](https://platform.claude.com/docs/en/models/opus-5-5/overview)）。据 Anthropic 官方，Opus 5.5 在默认 effort（medium）下即可超过 Opus 5 在 max effort 的水平，成本约为其五分之一，并以约 40% 的成本追平 GPT-6 Astra（[Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)）。同期 Claude Opus 4.1 正式退役（[Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)）。关于安全分流机制，第三方报道提到当生产防护被触发时，部分任务会被改由较早模型完成：网络安全类任务交给 Opus 4.8，生物与"前沿 LLM 开发"类请求交给 Opus 5，常规的 bug 查找与修复仍在 Opus 5.5 上执行（[GPT-6 Luna vs Gemini 3.8 Flash vs Claude Opus 5.5](https://www.sentisight.ai/gpt-6-luna-vs-gemini-3-8-flash-vs-claude-opus-5-5/)）。

### Google Gemini 系列

Google 于 2025 年末发布 Gemini 3 系列后，Gemini 3.1 Pro 于 2026 年 3 月 13 日登陆 VS Code 与 IntelliJ 的 Gemini Code Assist（[Gemini for Google Cloud release notes](https://docs.cloud.google.com/gemini/docs/release-notes)）。2026 年 7 月 21 日，Google 推出 Gemini 3.6 Flash、3.5 Flash-Lite 与 3.5 Flash Cyber，主打面向大规模 agent 的效率、延迟与可靠性，并透露 Gemini 3.5 Pro 正在与合作方测试（[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)）。Gemini 3.8 Flash 与 Flash-Lite TTS 也已进入正式可用（GA）阶段（[版本说明 | Gemini API](https://ai.google.dev/gemini-api/docs/changelog)）。定价方面，Gemini 3.1 Pro Preview 输入 $2、输出 $12（每百万 token），Gemini 3.8 Flash 输入 $0.75（[Agent Platform Pricing | Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)）。

### xAI Grok

xAI 的 Grok 4.5 于 2026 年 7 月 8 日发布，是首个基于 V9（1.5 万亿参数）基座构建的旗舰，并且是与 Cursor 协同训练而非事后适配编程；其 API 定价为输入 $2、输出 $6（每百万 token）（[xAI and Grok](https://aiproplaybook.com/learn/module-4/section-4-4)、[Release Notes](https://releases.sh/xai/release-notes)）。此后 Grok 4.6 于 2026 年 8 月 12 日、Grok 4.7 于 2026 年 9 月 21 日相继发布；Grok 4.7 保持 $2/$6 定价，上下文 500K，在 DeepSWE v1.1 得 71.0%、CursorBench 4.0 得 46.3%、Terminal-Bench 4.0 得 38.0%（[Grok 4.7 Drops, OpenAI Cracks Math](https://dev.to/trillioniar_s_14a3c313e14/grok-47-drops-openai-cracks-math-and-trump-wants-an-ai-force-september-22-2026-3657)、[Grok 4.7 — SpaceXAI's September 2026 Grok Flagship](https://ai-tldr.dev/models/grok-4-7/)）。备受期待的 Grok 5 被推迟至 2026 年，候选方案为约 6 万亿参数的 MoE 模型，运行于 Colossus 2（[Grok 5: Release Date & All We Know So Far](https://felloai.com/all-we-know-so-far-about-grok-5/)）。在更早的 HLE-Diamond 榜单上，Grok 4.7 报告 25.4%（[Introducing HLE-Diamond](https://lastexam.ai/blog/hle-diamond)）。

### Meta Llama

Meta 于 2026 年 9 月 3 日发布 Llama 4 Maverick 2，取消了此前对月活超 7 亿运营者的商业授权限制，并即时上线 HuggingFace（[Meta "Llama 4 Maverick 2" — All Commercial Restrictions Lifted](https://slide.miraipage.net/ainews/06498a9f-6fb0-415d-947e-f8edbadb0bf2)）。Llama 4 系列采用 MoE 架构，面向多模态理解、多语言与代码任务优化（[Meta Llama 4 Maverick](http://docs.oracle.com/it-it/iaas/Content/generative-ai/meta-llama-4-maverick.htm)）。相较 OpenAI/Anthropic 的闭源旗舰，Meta 仍以开放权重为差异化路线。

### DeepSeek

DeepSeek 于 2025 年 12 月 1 日发布 V3.2 与 V3.2-Speciale，后者在 IMO 2025、CMO 2025、ICPC World Finals 2025 与 IOI 2025 上均达到金牌水平，成绩分别相当于人类选手第二名与第十名（[DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://www.deepseek.com/en/news/deepseek-v3-2/)）。2026 年 4 月 24 日发布 DeepSeek V4（含 V4-Pro、V4-Flash），沿用 DeepSeekMoE 与多 token 预测（MTP），并引入混合注意力（CSA+HCA）、流形约束超连接（mHC）与 Muon 优化器（[DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)）。2026 年 9 月 10 日发布 DeepSeek-V4.1-Flash，为新架构族中最小尺寸、具备原生多模态视觉理解，GPQA Diamond 达 90.9（[Change Log | DeepSeek API Docs](https://api-docs.deepseek.com/updates/)）。定价上，V4-Pro 为缓存未命中输入 $0.435、输出 $0.87 每百万 token，V4-Flash 为 $0.14/$0.28（[DeepSeek V4 Pro: specifications, pricing, benchmarks](https://deepseek-v4.io/deepseek-v4-pro)）。需要澄清的是，外界长期传闻的"DeepSeek R2"从未发布（[DeepSeek R2: The Most Anticipated Model That Never Shipped](https://theplanettools.ai/blog/deepseek-r2-never-shipped-what-deepseek-released-instead-2026)）。第三方评测把 DeepSeek V4 Pro 的 DeepSeekMoE 配置记为总参 1.6T、激活约 49B，并指出其自托管需要严肃的硬件投入（[DeepSeek V4 and V4 Flash vs. Kimi K3](https://softmaxdata.com/blog/deepseek-v4-glm-5-2-kimi-2-6-and/)、[DeepSeek V4 vs GLM-5.2 vs Kimi K3: Which to Deploy](https://andrew.ooo/answers/deepseek-v4-vs-glm-5-2-vs-kimi-k3-which-open-model-to-deploy-july-2026/)）。

### 阿里 Qwen

阿里巴巴于 2026 年 2 月 16 日开源 Qwen3.5 系列首款模型 Qwen3.5-397B-A17B（又称 Qwen3.5-Plus），为原生多模态基础模型，覆盖推理、编程、agent 与多模态理解（[Alibaba Open-Sources Qwen3.5](https://home.alibabagroup.com/en-US/document-1960233590314762240)、[Qwen3.5: Towards Native Multimodal Agents](https://qwen.ai/blog?id=qwen3.5)）。其 API 定价为输入 ¥1.2、输出 ¥7.2 每百万 token（128k 输入以内）（[qwen3.5-397b-a17b 模型信息](https://help.aliyun.com/zh/model-studio/qwen3-5-397b-a17b)）。此后 Qwen 快速迭代出 3.5-Plus、3.6-Plus、3.7-Plus 与 3.7-Max 等，均带"Thinking"开关，Qwen3.8-Max 则保留 low/medium/extra high 三档推理强度（[Qwen Code Weekly Update](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-08-27/)）。需注意，截至 2026 年年中，阿里最强的编程模型 Qwen3.7-Max 为 DashScope 上的 API-only 模型（$2.50 / $7.50 每百万 token），并未公开权重；可自托管的最强 Qwen 为更小尺寸版本（[GLM-5.2 vs DeepSeek V4 vs Qwen3](https://www.developersdigest.tech/blog/glm-5-2-vs-deepseek-v4-vs-qwen3-open-weights-coding-showdown)）。

### 月之暗面 Kimi

Moonshot AI 于 2026 年 7 月 16 日发布 Kimi K3，为 2.8 万亿参数模型，基于 KDA 混合线性注意力（Kimi Delta Attention）与注意力残差技术，原生支持视觉理解，上下文 100 万 token，号称全球首个开源的 3 万亿级模型（[Kimi K3：智能的新前沿](https://www.kimi.com/news/kimi-k3)）。2026 年 7 月 27 日，K3 完整权重按承诺上传 HuggingFace，采用需对大型"模型即服务"业务单独签约的 Kimi K3 License（[moonshotai/Kimi-K3](https://simonwillison.net/2026/Jul/27/kimi-k3/)）。K3 在 8 项真实 agentic 基准中的 4 项排名第一（[Kimi K3](https://k3-kimi.com/)），API 定价约输入 $3、输出 $15 每百万 token（[Qwen 3.8 Max vs. Kimi K3](https://www.theaitechpulse.com/qwen-3-8-max-vs-kimi-k3-2026)）。2026 年 9 月 11 日，Kimi K2.8 预览版上线（[What's New | Kimi Code Docs](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)）。

### 字节豆包

字节跳动 Seed 团队于 2026 年 6 月 23 日发布 Seed 2.1 系列，面向真实生产力场景（[Seed2.1 正式发布，深入 AI 生产力](https://research.doubao.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity)）。Doubao-Seed-2.1-pro 上下文窗口与最大输出均为 256k，最大思维链长度 256k，定价为输入 ¥6、输出 ¥30 每百万 token（[AI Hub-豆包大模型API服务平台](https://ai.volcengine.com/model)）。2026 年 9 月 16 日，Doubao-Seed-2.1-pro 升级至 0915 版本并全量上线火山方舟，强化 agent 专业任务交付、多模态编程与 3D/专业图文理解，同时进一步降低综合使用成本（[豆包大模型2.1 Pro更新](http://kw.beijing.gov.cn/xwdt/kcyx/xwdtyqqy/202609/t20260917_4867742.html)）。

### 其他：智谱 GLM

智谱于 2026 年 6 月 16–17 日上线并开源 GLM-5.2，主打长程任务，支持真正可用的 100 万 token 上下文，基于 7440 亿参数 MoE（每 token 约激活 400 亿参数），以 MIT 许可开放权重（[Z.ai - GLM-5.2上线并开源](https://www.zhipuai.cn/zh/research/161)、[Zhipu AI](https://aiwiki.ai/wiki/zhipu_ai)）。第三方汇总则把 GLM-5.2 记为约 7530 亿总参数、400 亿激活（[Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2](https://deepinfra.ai/blog/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2)），两处口径略有差异。

### 开放权重阵营横向对比

2026 年年中，开放权重前沿模型的规模与许可已形成明确梯队（[Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2](https://deepinfra.ai/blog/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2)）：

| 模型 | 总参数 / 激活 | 上下文 | 许可 | 权重状态 |
| --- | --- | --- | --- | --- |
| Kimi K3 | 2.8T / 约 50B | 1M | 改良 MIT | 2026-07-27 上线 |
| DeepSeek V4 Pro | 1.6T / 约 49B | 1M | MIT | 已上线 |
| GLM-5.2 | 约 753B / 约 40B | 1M | MIT | 已上线 |

三者的 Artificial Analysis Intelligence Index 分别约为 57（Kimi K3，总榜第 4）、44（DeepSeek V4 Pro，Max reasoning）与 51（GLM-5.2）（[Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2](https://deepinfra.ai/blog/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2)）。Kimi K3 在 Terminal-Bench 2.1 上厂商自报 88.3%（[Top 5 Open Weight Models That Matter to Developers in 2026](https://cline.bot/blog/best-open-weight-models-that-matter-in-2026)）。

不同来源的规格口径并不统一。MarkTechPost 在 2026 年 7 月 18 日的对比表中，把 Kimi K3 的激活参数标注为"未披露（16/896 专家）"、模态记为 Text + vision + video；DeepSeek V4 Pro 为总参 1.6T、激活 49B、1M 上下文（最大输出 384K）；GLM-5.2 为总参 744B（Artificial Analysis 口径 753B）、激活约 40B、1M 上下文（最大输出 131K）（[Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2 — MarkTechPost](https://www.marktechpost.com/2026/07/18/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2-open-trillion-scale-moe-models-compared-on-benchmarks-license-and-serving-cost/)）。自托管门槛方面，第三方给出 Kimi K3 需多节点 H100/MI300（≥8 卡、vLLM 或 SGLang），GLM-5.2 可单节点 8×H100 或 4×MI300 运行（[Qwen 3.8 Max vs GLM 5.2 vs Kimi K3 vs DeepSeek V4 Flash (2026)](https://a2aprotocol.ai/insights/qwen-38-max-vs-glm-52-vs-kimi-k3-vs-deepseek-v4-flash)）；一份面向落地选型的对比则总结 Kimi K3"能力最强但体量巨大、API 更贵且为自定义许可"，GLM-5.2"独立编程测试成绩领先、MIT 许可，但自托管仍需严肃硬件"（[DeepSeek V4 and V4 Flash vs. Kimi K3](https://softmaxdata.com/blog/deepseek-v4-glm-5-2-kimi-2-6-and/)）。

## 核心技术与关键概念

- **混合专家（MoE）稀疏架构**：通过门控网络为每个 token 选择少量专家，以较低激活算力换更大总参数量，已成为 Kimi K3、DeepSeek V4、GLM-5.2、Llama 4 等的共同选择（[What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)）。
- **超长上下文**：100 万 token 已成为前沿旗舰的默认门槛（Claude Opus 5.5、Kimi K3、GLM-5.2 等），部分 Gemini 版本可扩展至 1M–2M。
- **内建思考/推理档位**：Anthropic 的 adaptive thinking + effort、Qwen 的 Thinking 开关、Gemini 的 Deep Think，都把推理深度做成可调参数。
- **原生多模态**：Qwen3.5、Kimi K3、DeepSeek-V4.1-Flash 均在预训练阶段融合视觉，而非后期拼接。
- **分层发布与模型路由**：厂商同时提供能力/成本梯度明显的多个型号，主张按负载路由而非单模型通吃（[GPT-6 Luna vs Gemini 3.8 Flash vs Claude Opus 5.5](https://www.sentisight.ai/gpt-6-luna-vs-gemini-3-8-flash-vs-claude-opus-5-5/)）。
- **测试时计算（test-time compute）成为第三条扩展维度**：在预训练与后训练之外，通过更长的推理链、多路径探索与自我校验，在推理时投入更多算力以换取复杂任务上的提升（[Test-Time Compute: How Reasoning Models Are Changing AI Agent Architecture in 2026](https://skillgen.io/test-time-compute-ai-agents-2026)）。但该策略并非普适：有研究评估 14 个推理模型后指出，增加测试时计算并不稳定提升准确率，且在闭卷知识密集型任务上往往带来更多幻觉（[Test-Time Scaling in Reasoning Models Is Not Effective for Knowledge-Intensive Tasks Yet](https://arxiv.org/html/2509.06861v3)）；另有研究观察到大推理模型的输出长度扩展系数随参数量变化很弱，即"更大的模型未必更省 token"（[Scaling of Capability and Efficiency at Inference Time in Large Reasoning Models](https://arxiv.org/pdf/2609.27166)）。

## 代表性项目/产品（带官方链接）

- OpenAI GPT-6 Astra：https://openai.com/zh-Hans-CN/index/gpt-6-astra/
- Anthropic Claude Opus 5.5：https://platform.claude.com/docs/en/models/opus-5-5/overview
- Google Gemini API 更新日志：https://ai.google.dev/gemini-api/docs/changelog
- xAI 发布说明：https://releases.sh/xai/release-notes
- DeepSeek API 更新日志：https://api-docs.deepseek.com/updates/
- 阿里 Qwen3.5：https://qwen.ai/blog?id=qwen3.5
- 月之暗面 Kimi K3：https://www.kimi.com/news/kimi-k3
- 字节豆包大模型：https://ai.volcengine.com/model
- 智谱 GLM-5.2：https://www.zhipuai.cn/zh/research/161

## 关键数据与评测结果

- **LMArena（人类偏好）**：Claude Fable 5 / Opus 系列位居前列，Fable 5 分数约 1506–1531（[LMArena Leaderboard, August 2026](https://www.swfte.com/lmarena)、[AI Model Leaderboard — Elo Rankings (2026)](https://prompeteer.ai/leaderboard)）。
- **Artificial Analysis Intelligence Index v4.3**：Claude Fable 5.1 与 GPT-6 Astra 领跑，开放权重模型中 GLM-5.3 Flash、Kimi K3、Qwen3.8 2.4T A95B、DeepSeek V4 Pro 领先（[Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)）。Claude Opus 5.5 在 max effort 下取得 58 分，为当时最高（[Claude Opus 5.5 takes the top spot on the Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/claude-opus-5-5)）。需要强调，Artificial Analysis 的分值随版本与口径变化，不同来源给出的数字差异明显：v4.3 官方文章称 Claude Fable 5.1（max with fallback）与 GPT-6 Astra（max）同为 53，其后为 Claude Opus 5（max，51）、Claude Fable 5（50）、Muse Spark 1.3（48）（[Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)）；OfficeChai 的报道则称 Fable 5.1 以 66 分登顶、Claude Opus 5 为 63（[Claude Fable 5.1 Scores Tops Artificial Analysis Intelligence Index With Score Of 66](https://officechai.com/ai/claude-fable-5-1-scores-tops-artificial-analysis-intelligence-index-with-score-of-66-beats-opus-5-by-3-points/)）；BenchLM 收录的快照又给出 GPT-5.6 Terra 57.6、Claude Fable 5.1 53.4、DeepSeek V4 Pro 0813 53.2、GPT-6 Astra 52.7（[Artificial Analysis Intelligence Index — BenchLM](https://benchlm.ai/benchmarks/artificialanalysis)）；datalearner 的镜像则列出 Claude Fable 5.1 为 47、Grok 4.6（high）为 44（[Artificial Analysis Intelligence Index — datalearner](https://www.datalearner.com/en/leaderboards/external/aa-quality-index)）。这些数字不可直接横向比较。
- **Opus 5.5 vs GPT-6 Astra**：据 Anthropic，Opus 5.5 在 Terminal-Bench 4.0 达 66.4%；在双方唯一可公平对比的 AutomationBench 上，Opus 5.5 为 40.0%、GPT-6 Sol（xhigh）为 33.2%（[Frontier AI Benchmarks Compared: Opus 5.5, GPT-6 & More](https://aitoolsreview.co.uk/insights/frontier-ai-benchmarks-september-2026)）。OpenAI 另报告 Astra 未由 Anthropic 覆盖的指标：GPQA Diamond 96.0%、ARC-AGI-2 95%（[Claude Opus 5.5: Specs, Benchmarks, Pricing](https://kingy.ai/blog/claude-opus-5-5-specs-benchmarks-pricing-comparison/)）。Astra 发布时官方自报的另外两项为 FrontierMath Tier 4 v2 97.6% 与 ExploitBench 100%（[OpenAI Launches GPT-6 Astra With Record Benchmarks](https://howaiworks.ai/blog/openai-gpt-6-astra-launch-2026)）。
- **能力维度对比（2026 年 7 月）**：编程由 Claude Opus 4.7 在 SWE-bench 上领先约 2.9%，数学由 GPT-5.5 Pro 在 FrontierMath 上领先约 2.5%，长任务由 Claude Opus 系列领先约 2 倍 METR horizon（[GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1: The Ultimate July 2026 Comparison](https://q4km.ai/blog/gpt-55-vs-claude-opus-vs-gemini-july-2026.html)）。
- **ARC-AGI-2 / ARC-AGI-3**：GPT-6 Astra 报告 ARC-AGI-2 达 95%（[Abstraction and Reasoning Corpus for AGI v2 (ARC-AGI-2)](https://benchlm.ai/benchmarks/arc-agi-2)）；发布报道称其在 ARC-AGI-3 上自报 98.6%–99.9%，但该成绩基于 OpenAI 自定义 harness，标准框架下明显更低（[GPT-6 Astra Review: Benchmarks, Pricing, Safety](https://aitoolsreview.co.uk/insights/gpt-6-astra-review)、[Frontier Models](https://thursdai.news/topics/frontier-models)）。
- **HLE-Diamond（新变体）**：Claude Opus 5.5 60.6%、Claude Fable 5.1 55.0%、Claude Opus 5 51.3%、Gemini 3.8 Flash 38.6%、GPT-6 Sol 34.3%、GPT-5.6 Sol 33.8%、Grok 4.7 25.4%（[Introducing HLE-Diamond](https://lastexam.ai/blog/hle-diamond)）。
- **API 价格（2026 年 9 月）**：前沿 token 价格指数降至 16（以 2023 年 3 月为基准 100 计，下跌约 84%），21 个活跃样本的旗舰模型中位价为混合 $6.00/百万 token（[LLM API Pricing Trends — BenchLM](https://benchlm.ai/llm-pricing-trends)）。截至 2026 年 9 月 15 日，BenchLM 总榜前十中最便宜的是 Gemini 3.8 Flash，输入 $0.75、输出 $3.75 每百万 token（[LLM Pricing Statistics (2026) — BenchLM](https://benchlm.ai/stats/llm-pricing)）。据 2026 年 9 月的对照表，GPT-6 Astra 列表价为输入 $10 / 输出 $50（缓存读取约 $1）、Claude Fable 5.1 为 $10/$50（缓存 $0.25）、Claude Opus 5 为 $5/$25（缓存 $0.50）（[LLM API Pricing Comparison, September 2026](https://dev.to/gil_5296961bf2e126cf43cb4b/llm-api-pricing-comparison-september-2026-the-new-ceiling-the-cache-read-war-and-the-promo-1ni4)）。另一份对比指出，同期前沿模型的列表价跨度可达约两个数量级，DeepSeek V4 最低（输入 $0.435/百万 token），Claude Opus 4.7 最高（$5.00），而实际最便宜者取决于缓存命中率与输入输出比（[The 2026 LLM API Pricing Comparison](https://dev.to/dylanfoster1/the-2026-llm-api-pricing-comparison-gpt-55-claude-sonnet-46-gemini-35-flash-and-deepseek-v4-4g4)）。

## 趋势与争议

一是**迭代节奏空前加快**：同一厂商在数周内连发旗舰或改版（Grok 4.5→4.6→4.7；Claude Opus 4.8→Fable 5→Opus 5.5），用户与评测机构难以持续跟踪。二是**基准可信度受质疑**：ARC-AGI 等出现"过拟合担忧"，GPT-6 Astra 的 ARC-AGI-3 高分被指依赖自定义测试框架、与标准框架结果不一致（[GPT-6 Astra Review: Benchmarks, Pricing, Safety](https://aitoolsreview.co.uk/insights/gpt-6-astra-review)、[Gemini benchmark gains, ARC overfit concerns](https://zeronoise.ai/posts/gemini-benchmark-gains-arc-overfit-concerns-and-rising-pressure-on-trust-deepfakes-peer-review-robots-b00cnyy42p/download/pdf)）；而 MMLU 等老基准已被多家模型刷至饱和。三是**降本与"降价内卷"**：前沿 token 价格大幅下探，前沿价格指数较 2023 年 3 月下跌约 84%，DeepSeek V4 Pro 借 MoE 效率实现约 75% 降价（[LLM API Pricing Trends — BenchLM](https://benchlm.ai/llm-pricing-trends)、[4 Best Frontier AI Models](https://www.theaitechpulse.com/4-best-frontier-ai-models)）；高盛研究指出，具备前沿性能与多模态能力的模型仍保有较强定价能力，但低端 API 市场已进入价格战，预计 2026 年下半年低端 API 价格约每百万 token $0.1–0.2，部分资金充裕的中国厂商可能短期以零甚至负毛利率补贴（[大模型价格战持续升温 — 观察者网](http://m.toutiao.com/group/7689773875676135971/)）。四是**开源与闭源的分层**：Kimi K3、GLM-5.2、Qwen3.5 以开放权重冲击前沿，但许可证对大规模商用设限（如 Kimi K3 License 要求大型 MaaS 业务单独签约），围绕"open weights vs. open source"的界定仍存争议（[Kimi K3 Open Weights](https://nodemini.com/en/blog/2026-kimi-k3-open-weights-release-july-27.html)、[moonshotai/Kimi-K3](https://simonwillison.net/2026/Jul/27/kimi-k3/)）。五是**同一模型的"档位化"与跨厂路由成为采购常态**：分析建议企业按任务同时路由 2–3 档模型，以兼顾成本与能力上限（[GPT-6 Luna vs Gemini 3.8 Flash vs Claude Opus 5.5](https://www.sentisight.ai/gpt-6-luna-vs-gemini-3-8-flash-vs-claude-opus-5-5/)）。六是**监管进入可执行阶段**：欧盟 AI Act 于 2024 年 8 月 1 日生效，其中通用人工智能（GPAI）模型的义务自 2025 年 8 月 2 日起适用，而 AI Office 与成员国主管机关的执法权限自 2026 年 8 月 2 日起开始适用，同日部分透明度等条款也进入可执行状态（[AI Act — European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)、[FAQ — EU AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/faq)）。

## 参考来源

1. [Strategic Analysis of Frontier AI Models: GPT-5.2 vs. Gemini 3](https://ironcrestsoftware.com/assets/pdfs/ai-model-comparison-chatgpt-vs-gemini.pdf)
2. [GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1 Pro: The Frontier Model Showdown](https://dev.to/om_shree_0709/gpt-55-vs-claude-opus-47-vs-gemini-31-pro-the-frontier-model-showdown-4mji)
3. [Presentamos GPT‑5.5](https://openai.com/es-ES/index/introducing-gpt-5-5/)
4. [预览 GPT‑5.6 Sol：新一代模型](https://openai.com/zh-Hans-CN/index/previewing-gpt-5-6-sol/)
5. [GPT-6 Astra：新一代智能](https://openai.com/zh-Hans-CN/index/gpt-6-astra/)
6. [OpenAI 研究（发布时间索引）](https://openai.com/zh-Hans-CN/research/index/)
7. [GPT-6 Astra : 100 000 GPU Nvidia pour entraîner le modèle](https://overclocking.com/gpt-6-astra-100000-gpu-nvidia-prix-ram/)
8. [Claude Opus \ Anthropic](https://www.anthropic.com/claude/opus)
9. [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
10. [Claude Mythos 5](https://www.anthropic.com/claude/mythos)
11. [Claude Opus 5.5 - Claude Platform Docs](https://platform.claude.com/docs/en/models/opus-5-5/overview)
12. [Introducing Claude Opus 5.5 \ Anthropic](https://www.anthropic.com/claude-opus-5-5)
13. [Gemini for Google Cloud release notes](https://docs.cloud.google.com/gemini/docs/release-notes)
14. [Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)
15. [版本说明 | Gemini API](https://ai.google.dev/gemini-api/docs/changelog)
16. [Agent Platform Pricing | Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)
17. [xAI and Grok](https://aiproplaybook.com/learn/module-4/section-4-4)
18. [Release Notes](https://releases.sh/xai/release-notes)
19. [Grok 4.7 Drops, OpenAI Cracks Math](https://dev.to/trillioniar_s_14a3c313e14/grok-47-drops-openai-cracks-math-and-trump-wants-an-ai-force-september-22-2026-3657)
20. [Grok 4.7 — SpaceXAI's September 2026 Grok Flagship](https://ai-tldr.dev/models/grok-4-7/)
21. [Grok 5: Release Date & All We Know So Far](https://felloai.com/all-we-know-so-far-about-grok-5/)
22. [Meta "Llama 4 Maverick 2" — All Commercial Restrictions Lifted](https://slide.miraipage.net/ainews/06498a9f-6fb0-415d-947e-f8edbadb0bf2)
23. [Meta Llama 4 Maverick](http://docs.oracle.com/it-it/iaas/Content/generative-ai/meta-llama-4-maverick.htm)
24. [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://www.deepseek.com/en/news/deepseek-v3-2/)
25. [DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)
26. [Change Log | DeepSeek API Docs](https://api-docs.deepseek.com/updates/)
27. [DeepSeek V4 Pro: specifications, pricing, benchmarks](https://deepseek-v4.io/deepseek-v4-pro)
28. [DeepSeek R2: The Most Anticipated Model That Never Shipped](https://theplanettools.ai/blog/deepseek-r2-never-shipped-what-deepseek-released-instead-2026)
29. [Alibaba Open-Sources Qwen3.5](https://home.alibabagroup.com/en-US/document-1960233590314762240)
30. [Qwen3.5: Towards Native Multimodal Agents](https://qwen.ai/blog?id=qwen3.5)
31. [qwen3.5-397b-a17b 模型信息](https://help.aliyun.com/zh/model-studio/qwen3-5-397b-a17b)
32. [Qwen Code Weekly Update](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-08-27/)
33. [GLM-5.2 vs DeepSeek V4 vs Qwen3: The Open-Weights Coding Model Showdown (2026)](https://www.developersdigest.tech/blog/glm-5-2-vs-deepseek-v4-vs-qwen3-open-weights-coding-showdown)
34. [Kimi K3：智能的新前沿](https://www.kimi.com/news/kimi-k3)
35. [moonshotai/Kimi-K3](https://simonwillison.net/2026/Jul/27/kimi-k3/)
36. [Kimi K3](https://k3-kimi.com/)
37. [Qwen 3.8 Max vs. Kimi K3](https://www.theaitechpulse.com/qwen-3-8-max-vs-kimi-k3-2026)
38. [What's New | Kimi Code Docs](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)
39. [Seed2.1 正式发布，深入 AI 生产力](https://research.doubao.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity)
40. [AI Hub-豆包大模型API服务平台](https://ai.volcengine.com/model)
41. [豆包大模型2.1 Pro更新](http://kw.beijing.gov.cn/xwdt/kcyx/xwdtyqqy/202609/t20260917_4867742.html)
42. [Z.ai - GLM-5.2上线并开源](https://www.zhipuai.cn/zh/research/161)
43. [Zhipu AI](https://aiwiki.ai/wiki/zhipu_ai)
44. [Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2: Open-Weight AI Model Comparison](https://deepinfra.ai/blog/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2)
45. [Top 5 Open Weight Models That Matter to Developers in 2026](https://cline.bot/blog/best-open-weight-models-that-matter-in-2026)
46. [What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)
47. [GPT-6 Luna vs Gemini 3.8 Flash vs Claude Opus 5.5: Which Tier Fits Your Workload?](https://www.sentisight.ai/gpt-6-luna-vs-gemini-3-8-flash-vs-claude-opus-5-5/)
48. [Frontier AI Benchmarks Compared: Opus 5.5, GPT-6 & More (September 2026)](https://aitoolsreview.co.uk/insights/frontier-ai-benchmarks-september-2026)
49. [Claude Opus 5.5: Specs, Benchmarks, Pricing and How It Stacks Up](https://kingy.ai/blog/claude-opus-5-5-specs-benchmarks-pricing-comparison/)
50. [Introducing HLE-Diamond | Humanity's Last Exam](https://lastexam.ai/blog/hle-diamond)
51. [LMArena Leaderboard, August 2026](https://www.swfte.com/lmarena)
52. [AI Model Leaderboard — Elo Rankings (2026)](https://prompeteer.ai/leaderboard)
53. [Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)
54. [Claude Opus 5.5 takes the top spot on the Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/claude-opus-5-5)
55. [GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1: The Ultimate July 2026 Comparison](https://q4km.ai/blog/gpt-55-vs-claude-opus-vs-gemini-july-2026.html)
56. [Abstraction and Reasoning Corpus for AGI v2 (ARC-AGI-2)](https://benchlm.ai/benchmarks/arc-agi-2)
57. [Gemini benchmark gains, ARC overfit concerns](https://zeronoise.ai/posts/gemini-benchmark-gains-arc-overfit-concerns-and-rising-pressure-on-trust-deepfakes-peer-review-robots-b00cnyy42p/download/pdf)
58. [4 Best Frontier AI Models](https://www.theaitechpulse.com/4-best-frontier-ai-models)
59. [Kimi K3 Open Weights](https://nodemini.com/en/blog/2026-kimi-k3-open-weights-release-july-27.html)
60. [GPT-6 Sol与Claude Opus 5.5同日开打，谁是「性价比之王」-36氪](https://m.36kr.com/p/3995195771588745)
61. [Frontier Models — ThursdAI](https://thursdai.news/topics/frontier-models)
62. [OpenAI Launches GPT-6 Astra With Record Benchmarks — howaiworks](https://howaiworks.ai/blog/openai-gpt-6-astra-launch-2026)
63. [GPT-6 Astra: Features, Benchmarks, and Pricing — DataCamp](https://www.datacamp.com/ko/blog/gpt-6-astra)
64. [GPT-6 Astra Review: Benchmarks, Pricing, Safety — aitoolsreview](https://aitoolsreview.co.uk/insights/gpt-6-astra-review)
65. [Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2: Open Trillion-Scale MoE Models Compared — MarkTechPost](https://www.marktechpost.com/2026/07/18/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2-open-trillion-scale-moe-models-compared-on-benchmarks-license-and-serving-cost/)
66. [Qwen 3.8 Max vs GLM 5.2 vs Kimi K3 vs DeepSeek V4 Flash (2026) — a2aprotocol](https://a2aprotocol.ai/insights/qwen-38-max-vs-glm-52-vs-kimi-k3-vs-deepseek-v4-flash)
67. [DeepSeek V4 and V4 Flash vs. Kimi K3 — softmaxdata](https://softmaxdata.com/blog/deepseek-v4-glm-5-2-kimi-2-6-and/)
68. [DeepSeek V4 vs GLM-5.2 vs Kimi K3: Which to Deploy — andrew.ooo](https://andrew.ooo/answers/deepseek-v4-vs-glm-5-2-vs-kimi-k3-which-open-model-to-deploy-july-2026/)
69. [Artificial Analysis Intelligence Index — datalearner](https://www.datalearner.com/en/leaderboards/external/aa-quality-index)
70. [Claude Fable 5.1 Scores Tops Artificial Analysis Intelligence Index With Score Of 66 — OfficeChai](https://officechai.com/ai/claude-fable-5-1-scores-tops-artificial-analysis-intelligence-index-with-score-of-66-beats-opus-5-by-3-points/)
71. [Artificial Analysis Intelligence Index — BenchLM](https://benchlm.ai/benchmarks/artificialanalysis)
72. [LLM API Pricing Trends — BenchLM](https://benchlm.ai/llm-pricing-trends)
73. [LLM Pricing Statistics (2026) — BenchLM](https://benchlm.ai/stats/llm-pricing)
74. [LLM API Pricing Comparison, September 2026 — DEV](https://dev.to/gil_5296961bf2e126cf43cb4b/llm-api-pricing-comparison-september-2026-the-new-ceiling-the-cache-read-war-and-the-promo-1ni4)
75. [The 2026 LLM API Pricing Comparison — DEV](https://dev.to/dylanfoster1/the-2026-llm-api-pricing-comparison-gpt-55-claude-sonnet-46-gemini-35-flash-and-deepseek-v4-4g4)
76. [大模型价格战持续升温，智谱市值跌至3000亿港元 — 观察者网](http://m.toutiao.com/group/7689773875676135971/)
77. [AI Act — European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
78. [Frequently Asked Questions — EU AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/faq)
79. [Test-Time Scaling in Reasoning Models Is Not Effective for Knowledge-Intensive Tasks Yet — arXiv 2509.06861](https://arxiv.org/html/2509.06861v3)
80. [Scaling of Capability and Efficiency at Inference Time in Large Reasoning Models — arXiv 2609.27166](https://arxiv.org/pdf/2609.27166)
81. [Test-Time Compute: How Reasoning Models Are Changing AI Agent Architecture in 2026 — skillgen](https://skillgen.io/test-time-compute-ai-agents-2026)