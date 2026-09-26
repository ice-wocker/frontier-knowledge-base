# 通用大模型前沿格局（2025–2026）

> 最后更新：2026-09-26 ｜ 领域：人工智能·大语言模型 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

截至 2026 年 9 月，通用大模型（frontier LLM）的竞争格局已从"单一旗舰迭代"演变为"多厂商、多层次、按月刷新"的密集竞赛。头部厂商包括 OpenAI、Anthropic、Google DeepMind、xAI（后并入 SpaceX 体系）、Meta，以及中国的 DeepSeek、阿里云 Qwen、月之暗面 Kimi、字节跳动豆包、智谱 GLM 等。共同趋势是：旗舰模型普遍走向混合专家（MoE）稀疏架构、原生多模态、百万 token 级上下文窗口，以及把"思考（thinking）"能力内建为可按档位调节的推理模式，而非外挂的提示技巧。与此同时，API 定价持续下探，前沿能力的获取门槛显著降低。

## 2025–2026 最新进展

### OpenAI GPT 系列

OpenAI 于 2025 年 12 月 11 日发布 GPT-5.2，被视为针对 Gemini 3 的市场反击，主打专业知识工作，即编程、数据分析与复杂推理（[Strategic Analysis of Frontier AI Models: GPT-5.2 vs. Gemini 3](https://ironcrestsoftware.com/assets/pdfs/ai-model-comparison-chatgpt-vs-gemini.pdf)）。随后 GPT-5.5 于 2026 年 4 月 23 日推出（[GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1 Pro: The Frontier Model Showdown](https://dev.to/om_shree_0709/gpt-55-vs-claude-opus-47-vs-gemini-31-pro-the-frontier-model-showdown-4mji)），其官方对比表显示在 GDPval（胜或平）达 84.9%、OSWorld-Verified 达 78.7%、Toolathlon 达 55.6%（[Presentamos GPT‑5.5](https://openai.com/es-ES/index/introducing-gpt-5-5/)）。2026 年 6 月 26 日，OpenAI 开始对 GPT-5.6 系列（代号 Sol）进行有限预览，强调更强的网络安全能力与分层防护（[预览 GPT‑5.6 Sol：新一代模型](https://openai.com/zh-Hans-CN/index/previewing-gpt-5-6-sol/)）。2026 年 9 月 22 日，OpenAI 正式发布 GPT-6 Astra，称为"新一代智能"（[GPT-6 Astra：新一代智能](https://openai.com/zh-Hans-CN/index/gpt-6-astra/)）。据 NVIDIA CEO 黄仁勋 9 月 6 日透露，GPT-6 Astra 的训练动用了约 10 万块 Grace Blackwell 系列 GPU，并计划再追加 40 万块用于后续阶段（[GPT-6 Astra : 100 000 GPU Nvidia pour entraîner le modèle](https://overclocking.com/gpt-6-astra-100000-gpu-nvidia-prix-ram/)）。

### Anthropic Claude 系列

Anthropic 的旗舰迭代尤为密集。Claude Opus 4.8 于 2026 年 5 月 28 日发布，定位严肃编程与 AI agent，配备 100 万 token 上下文窗口（[Claude Opus \ Anthropic](https://www.anthropic.com/claude/opus)）。2026 年 6 月 25 日，Anthropic 同时推出 Claude Fable 5（面向全体客户的最强模型）与 Claude Mythos 5（仅限 Project Glasswing 参与者），两者默认支持 100 万 token 上下文、128k 最大输出，并采用"always-on adaptive thinking"（[Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)）。Fable 5.1 与 Mythos 5.1 共享同一底层模型，Fable 侧保留针对网络安全与生物领域的更精确防护（[Claude Mythos 5](https://www.anthropic.com/claude/mythos)）。2026 年 9 月 22 日，Claude Opus 5.5 发布，面向长时间运行的 agentic 编程与知识工作，100 万 token 上下文、128k 最大输出，定价为输入 $4/百万 token、输出 $20/百万 token（[Claude Opus 5.5 - Claude Platform Docs](https://platform.claude.com/docs/en/models/opus-5-5/overview)）。同期 Claude Opus 4.1 正式退役（[Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)）。

### Google Gemini 系列

Google 于 2025 年末发布 Gemini 3 系列后，Gemini 3.1 Pro 于 2026 年 3 月 13 日登陆 VS Code 与 IntelliJ 的 Gemini Code Assist（[Gemini for Google Cloud release notes](https://docs.cloud.google.com/gemini/docs/release-notes)）。2026 年 7 月 21 日，Google 推出 Gemini 3.6 Flash、3.5 Flash-Lite 与 3.5 Flash Cyber，主打面向大规模 agent 的效率、延迟与可靠性，并透露 Gemini 3.5 Pro 正在与合作方测试（[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)）。Gemini 3.8 Flash 与 Flash-Lite TTS 也已进入正式可用（GA）阶段（[版本说明 | Gemini API](https://ai.google.dev/gemini-api/docs/changelog)）。定价方面，Gemini 3.1 Pro Preview 输入 $2、输出 $12（每百万 token），Gemini 3.8 Flash 输入 $0.75（[Agent Platform Pricing | Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)）。

### xAI Grok

xAI 的 Grok 4.5 于 2026 年 7 月 8 日发布，是首个基于 V9（1.5 万亿参数）基座构建的旗舰，并且是与 Cursor 协同训练而非事后适配编程；其 API 定价为输入 $2、输出 $6（每百万 token）（[xAI and Grok](https://aiproplaybook.com/learn/module-4/section-4-4)、[Release Notes](https://releases.sh/xai/release-notes)）。此后 Grok 4.6 于 2026 年 8 月 12 日、Grok 4.7 于 2026 年 9 月 21 日相继发布；Grok 4.7 保持 $2/$6 定价，上下文 500K，在 DeepSWE v1.1 得 71.0%、CursorBench 4.0 得 46.3%、Terminal-Bench 4.0 得 38.0%（[Grok 4.7 Drops, OpenAI Cracks Math](https://dev.to/trillioniar_s_14a3c313e14/grok-47-drops-openai-cracks-math-and-trump-wants-an-ai-force-september-22-2026-3657)、[Grok 4.7 — SpaceXAI's September 2026 Grok Flagship](https://ai-tldr.dev/models/grok-4-7/)）。备受期待的 Grok 5 被推迟至 2026 年，候选方案为约 6 万亿参数的 MoE 模型，运行于 Colossus 2（[Grok 5: Release Date & All We Know So Far](https://felloai.com/all-we-know-so-far-about-grok-5/)）。

### Meta Llama

Meta 于 2026 年 9 月 3 日发布 Llama 4 Maverick 2，取消了此前对月活超 7 亿运营者的商业授权限制，并即时上线 HuggingFace（[Meta "Llama 4 Maverick 2" — All Commercial Restrictions Lifted](https://slide.miraipage.net/ainews/06498a9f-6fb0-415d-947e-f8edbadb0bf2)）。Llama 4 系列采用 MoE 架构，面向多模态理解、多语言与代码任务优化（[Meta Llama 4 Maverick](http://docs.oracle.com/it-it/iaas/Content/generative-ai/meta-llama-4-maverick.htm)）。相较 OpenAI/Anthropic 的闭源旗舰，Meta 仍以开放权重为差异化路线。

### DeepSeek

DeepSeek 于 2025 年 12 月 1 日发布 V3.2 与 V3.2-Speciale，后者在 IMO 2025、CMO 2025、ICPC World Finals 2025 与 IOI 2025 上均达到金牌水平，成绩分别相当于人类选手第二名与第十名（[DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://www.deepseek.com/en/news/deepseek-v3-2/)）。2026 年 4 月 24 日发布 DeepSeek V4（含 V4-Pro、V4-Flash），沿用 DeepSeekMoE 与多 token 预测（MTP），并引入混合注意力（CSA+HCA）、流形约束超连接（mHC）与 Muon 优化器（[DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)）。2026 年 9 月 10 日发布 DeepSeek-V4.1-Flash，为新架构族中最小尺寸、具备原生多模态视觉理解，GPQA Diamond 达 90.9（[Change Log | DeepSeek API Docs](https://api-docs.deepseek.com/updates/)）。定价上，V4-Pro 为缓存未命中输入 $0.435、输出 $0.87 每百万 token，V4-Flash 为 $0.14/$0.28（[DeepSeek V4 Pro: specifications, pricing, benchmarks](https://deepseek-v4.io/deepseek-v4-pro)）。需要澄清的是，外界长期传闻的"DeepSeek R2"从未发布（[DeepSeek R2: The Most Anticipated Model That Never Shipped](https://theplanettools.ai/blog/deepseek-r2-never-shipped-what-deepseek-released-instead-2026)）。

### 阿里 Qwen

阿里巴巴于 2026 年 2 月 16 日开源 Qwen3.5 系列首款模型 Qwen3.5-397B-A17B（又称 Qwen3.5-Plus），为原生多模态基础模型，覆盖推理、编程、agent 与多模态理解（[Alibaba Open-Sources Qwen3.5](https://home.alibabagroup.com/en-US/document-1960233590314762240)、[Qwen3.5: Towards Native Multimodal Agents](https://qwen.ai/blog?id=qwen3.5)）。其 API 定价为输入 ¥1.2、输出 ¥7.2 每百万 token（128k 输入以内）（[qwen3.5-397b-a17b 模型信息](https://help.aliyun.com/zh/model-studio/qwen3-5-397b-a17b)）。此后 Qwen 快速迭代出 3.5-Plus、3.6-Plus、3.7-Plus 与 3.7-Max 等，均带"Thinking"开关，Qwen3.8-Max 则保留 low/medium/extra high 三档推理强度（[Qwen Code Weekly Update](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-08-27/)）。

### 月之暗面 Kimi

Moonshot AI 于 2026 年 7 月 16 日发布 Kimi K3，为 2.8 万亿参数模型，基于 KDA 混合线性注意力（Kimi Delta Attention）与注意力残差技术，原生支持视觉理解，上下文 100 万 token，号称全球首个开源的 3 万亿级模型（[Kimi K3：智能的新前沿](https://www.kimi.com/news/kimi-k3)）。2026 年 7 月 27 日，K3 完整权重按承诺上传 HuggingFace，采用需对大型"模型即服务"业务单独签约的 Kimi K3 License（[moonshotai/Kimi-K3](https://simonwillison.net/2026/Jul/27/kimi-k3/)）。K3 在 8 项真实 agentic 基准中的 4 项排名第一（[Kimi K3](https://k3-kimi.com/)），API 定价约输入 $3、输出 $15 每百万 token（[Qwen 3.8 Max vs. Kimi K3](https://www.theaitechpulse.com/qwen-3-8-max-vs-kimi-k3-2026)）。2026 年 9 月 11 日，Kimi K2.8 预览版上线（[What's New | Kimi Code Docs](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)）。

### 字节豆包

字节跳动 Seed 团队于 2026 年 6 月 23 日发布 Seed 2.1 系列，面向真实生产力场景（[Seed2.1 正式发布，深入 AI 生产力](https://research.doubao.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity)）。Doubao-Seed-2.1-pro 上下文窗口与最大输出均为 256k，最大思维链长度 256k，定价为输入 ¥6、输出 ¥30 每百万 token（[AI Hub-豆包大模型API服务平台](https://ai.volcengine.com/model)）。2026 年 9 月 16 日，Doubao-Seed-2.1-pro 升级至 0915 版本并全量上线火山方舟，强化 agent 专业任务交付、多模态编程与 3D/专业图文理解，同时进一步降低综合使用成本（[豆包大模型2.1 Pro更新](http://kw.beijing.gov.cn/xwdt/kcyx/xwdtyqqy/202609/t20260917_4867742.html)）。

### 其他：智谱 GLM

智谱于 2026 年 6 月 16–17 日上线并开源 GLM-5.2，主打长程任务，支持真正可用的 100 万 token 上下文，基于 7440 亿参数 MoE（每 token 约激活 400 亿参数），以 MIT 许可开放权重（[Z.ai - GLM-5.2上线并开源](https://www.zhipuai.cn/zh/research/161)、[Zhipu AI](https://aiwiki.ai/wiki/zhipu_ai)）。

## 核心技术与关键概念

- **混合专家（MoE）稀疏架构**：通过门控网络为每个 token 选择少量专家，以较低激活算力换更大总参数量，已成为 Kimi K3、DeepSeek V4、GLM-5.2、Llama 4 等的共同选择（[What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)）。
- **超长上下文**：100 万 token 已成为前沿旗舰的默认门槛（Claude Opus 5.5、Kimi K3、GLM-5.2 等），部分 Gemini 版本可扩展至 1M–2M。
- **内建思考/推理档位**：Anthropic 的 adaptive thinking + effort、Qwen 的 Thinking 开关、Gemini 的 Deep Think，都把推理深度做成可调参数。
- **原生多模态**：Qwen3.5、Kimi K3、DeepSeek-V4.1-Flash 均在预训练阶段融合视觉，而非后期拼接。

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
- **Artificial Analysis Intelligence Index v4.3**：Claude Fable 5.1 与 GPT-6 Astra 领跑，开放权重模型中 GLM-5.3 Flash、Kimi K3、Qwen3.8 2.4T A95B、DeepSeek V4 Pro 领先（[Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)）。Claude Opus 5.5 在 max effort 下取得 58 分，为当时最高（[Claude Opus 5.5 takes the top spot on the Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/claude-opus-5-5)）。
- **能力维度对比（2026 年 7 月）**：编程由 Claude Opus 4.7 在 SWE-bench 上领先约 2.9%，数学由 GPT-5.5 Pro 在 FrontierMath 上领先约 2.5%，长任务由 Claude Opus 系列领先约 2 倍 METR horizon（[GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1: The Ultimate July 2026 Comparison](https://q4km.ai/blog/gpt-55-vs-claude-opus-vs-gemini-july-2026.html)）。
- **ARC-AGI-2**：GPT-6 Astra 报告 95%（[Abstraction and Reasoning Corpus for AGI v2 (ARC-AGI-2)](https://benchlm.ai/benchmarks/arc-agi-2)）。

## 趋势与争议

一是**迭代节奏空前加快**：同一厂商在数周内连发旗舰或改版（Grok 4.5→4.6→4.7；Claude Opus 4.8→Fable 5→Opus 5.5），用户与评测机构难以持续跟踪。二是**基准可信度受质疑**：ARC-AGI 等出现"过拟合担忧"，而 MMLU 等老基准已被多家模型刷至饱和（[Gemini benchmark gains, ARC overfit concerns](https://zeronoise.ai/posts/gemini-benchmark-gains-arc-overfit-concerns-and-rising-pressure-on-trust-deepfakes-peer-review-robots-b00cnyy42p/download/pdf)）。三是**降本与"降价内卷"**：前沿 token 价格大幅下探，DeepSeek V4 Pro 借 MoE 效率实现约 75% 降价（[4 Best Frontier AI Models](https://www.theaitechpulse.com/4-best-frontier-ai-models)）。四是**开源与闭源的分层**：Kimi K3、GLM-5.2、Qwen3.5 以开放权重冲击前沿，但许可证对大规模商用设限，围绕"open weights vs. open source"的界定仍存争议（[Kimi K3 Open Weights](https://nodemini.com/en/blog/2026-kimi-k3-open-weights-release-july-27.html)）。

## 参考来源

1. [Strategic Analysis of Frontier AI Models: GPT-5.2 vs. Gemini 3](https://ironcrestsoftware.com/assets/pdfs/ai-model-comparison-chatgpt-vs-gemini.pdf)
2. [GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1 Pro: The Frontier Model Showdown](https://dev.to/om_shree_0709/gpt-55-vs-claude-opus-47-vs-gemini-31-pro-the-frontier-model-showdown-4mji)
3. [Presentamos GPT‑5.5](https://openai.com/es-ES/index/introducing-gpt-5-5/)
4. [预览 GPT‑5.6 Sol：新一代模型](https://openai.com/zh-Hans-CN/index/previewing-gpt-5-6-sol/)
5. [GPT-6 Astra：新一代智能](https://openai.com/zh-Hans-CN/index/gpt-6-astra/)
6. [GPT-6 Astra : 100 000 GPU Nvidia pour entraîner le modèle](https://overclocking.com/gpt-6-astra-100000-gpu-nvidia-prix-ram/)
7. [Claude Opus \ Anthropic](https://www.anthropic.com/claude/opus)
8. [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
9. [Claude Mythos 5](https://www.anthropic.com/claude/mythos)
10. [Claude Opus 5.5 - Claude Platform Docs](https://platform.claude.com/docs/en/models/opus-5-5/overview)
11. [Gemini for Google Cloud release notes](https://docs.cloud.google.com/gemini/docs/release-notes)
12. [Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)
13. [版本说明 | Gemini API](https://ai.google.dev/gemini-api/docs/changelog)
14. [Agent Platform Pricing | Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)
15. [xAI and Grok](https://aiproplaybook.com/learn/module-4/section-4-4)
16. [Release Notes](https://releases.sh/xai/release-notes)
17. [Grok 4.7 Drops, OpenAI Cracks Math](https://dev.to/trillioniar_s_14a3c313e14/grok-47-drops-openai-cracks-math-and-trump-wants-an-ai-force-september-22-2026-3657)
18. [Grok 4.7 — SpaceXAI's September 2026 Grok Flagship](https://ai-tldr.dev/models/grok-4-7/)
19. [Grok 5: Release Date & All We Know So Far](https://felloai.com/all-we-know-so-far-about-grok-5/)
20. [Meta "Llama 4 Maverick 2" — All Commercial Restrictions Lifted](https://slide.miraipage.net/ainews/06498a9f-6fb0-415d-947e-f8edbadb0bf2)
21. [Meta Llama 4 Maverick](http://docs.oracle.com/it-it/iaas/Content/generative-ai/meta-llama-4-maverick.htm)
22. [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://www.deepseek.com/en/news/deepseek-v3-2/)
23. [DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)
24. [Change Log | DeepSeek API Docs](https://api-docs.deepseek.com/updates/)
25. [DeepSeek V4 Pro: specifications, pricing, benchmarks](https://deepseek-v4.io/deepseek-v4-pro)
26. [DeepSeek R2: The Most Anticipated Model That Never Shipped](https://theplanettools.ai/blog/deepseek-r2-never-shipped-what-deepseek-released-instead-2026)
27. [Alibaba Open-Sources Qwen3.5](https://home.alibabagroup.com/en-US/document-1960233590314762240)
28. [Qwen3.5: Towards Native Multimodal Agents](https://qwen.ai/blog?id=qwen3.5)
29. [qwen3.5-397b-a17b 模型信息](https://help.aliyun.com/zh/model-studio/qwen3-5-397b-a17b)
30. [Qwen Code Weekly Update](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/weekly-update-2026-08-27/)
31. [Kimi K3：智能的新前沿](https://www.kimi.com/news/kimi-k3)
32. [moonshotai/Kimi-K3](https://simonwillison.net/2026/Jul/27/kimi-k3/)
33. [Kimi K3](https://k3-kimi.com/)
34. [Qwen 3.8 Max vs. Kimi K3](https://www.theaitechpulse.com/qwen-3-8-max-vs-kimi-k3-2026)
35. [What's New | Kimi Code Docs](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)
36. [Seed2.1 正式发布，深入 AI 生产力](https://research.doubao.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity)
37. [AI Hub-豆包大模型API服务平台](https://ai.volcengine.com/model)
38. [豆包大模型2.1 Pro更新](http://kw.beijing.gov.cn/xwdt/kcyx/xwdtyqqy/202609/t20260917_4867742.html)
39. [Z.ai - GLM-5.2上线并开源](https://www.zhipuai.cn/zh/research/161)
40. [Zhipu AI](https://aiwiki.ai/wiki/zhipu_ai)
41. [What Is Mixture of Experts?](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)
42. [LMArena Leaderboard, August 2026](https://www.swfte.com/lmarena)
43. [AI Model Leaderboard — Elo Rankings (2026)](https://prompeteer.ai/leaderboard)
44. [Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)
45. [Claude Opus 5.5 takes the top spot on the Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/claude-opus-5-5)
46. [GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1: The Ultimate July 2026 Comparison](https://q4km.ai/blog/gpt-55-vs-claude-opus-vs-gemini-july-2026.html)
47. [Abstraction and Reasoning Corpus for AGI v2 (ARC-AGI-2)](https://benchlm.ai/benchmarks/arc-agi-2)
48. [Gemini benchmark gains, ARC overfit concerns](https://zeronoise.ai/posts/gemini-benchmark-gains-arc-overfit-concerns-and-rising-pressure-on-trust-deepfakes-peer-review-robots-b00cnyy42p/download/pdf)
49. [4 Best Frontier AI Models](https://www.theaitechpulse.com/4-best-frontier-ai-models)
50. [Kimi K3 Open Weights](https://nodemini.com/en/blog/2026-kimi-k3-open-weights-release-july-27.html)