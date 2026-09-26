# AI 搜索与深度研究（AI Search & Deep Research）

> 最后更新：2026-09-26 ｜ 领域：AI·提示、Agent 与应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI 搜索（AI Search）指以对话式界面替代或补充传统关键词检索的产品形态，典型代表包括 ChatGPT Search、Google AI Overviews、Perplexity 等；深度研究（Deep Research）则是其中的"重模式"分支：Agent 自主制定研究计划、反复检索、识别知识缺口并再次检索，最终产出多页带引用的报告（[Build with Gemini Deep Research](https://goo.gle/deep-research-agent)）。Google 把 Deep Research 描述为"在用户监督下"工作：用户输入问题后，它先生成多步研究计划供用户修改或批准，随后像人一样浏览网页——搜索、发现有价值的信息，再基于所学发起新的搜索（[Try Deep Research and our new experimental model in Gemini](https://blog.google/products-and-platforms/products/gemini/google-gemini-deep-research/)）。

到 2026 年，AI 搜索进一步从"生成答案"转向"可执行 Agent"：Google 把信息 Agent 与生成式 UI 引入 Search，OpenAI 推出内置 ChatGPT 的 Atlas 浏览器，Perplexity 以 Comet 浏览器与实时引用为特色，浏览器本身成为新的分发入口（[A new era for AI Search](https://blog.google/products-and-platforms/products/search/search-io-2026/)；[ChatGPT Atlas - 发行说明](https://help.openai.com/zh-hans-cn/articles/12591856-chatgpt-atlas-release-notes)）。

## 最新进展（2025–2026）

Google 在 2025 年 3 月宣布升级 Deep Research，采用 Gemini 2.0 Flash Thinking Experimental，增强从规划、搜索到推理、分析与报告的全流程能力，产出更详细、更有洞察的多页报告（[New Gemini app features, available to try at no cost](https://blog.google/products/gemini/new-gemini-app-features-march-2025/)）。随后 Deep Research 向所有用户开放，并新增 Audio Overviews，可把报告转成类似播客的 AI 语音讨论（[6 tips to get the most out of Gemini Deep Research](https://blog.google/products-and-platforms/products/gemini/tips-how-to-use-deep-research/)）。当前版本的 Gemini Deep Research 以 Gemini 3 Pro 作为推理核心，官方称其"最具事实性"，并针对降低幻觉与提升报告质量做了专门训练，同时通过规模化多步强化学习提升搜索能力（[Build with Gemini Deep Research](https://goo.gle/deep-research-agent)）。

2026 年，深度研究成为各大厂商的标配功能：Google Gemini 提供 Deep Research 与 Deep Research Max；Perplexity、ChatGPT、Claude、Grok 均提供各自的深度研究模式，激活方式、运行时长与典型引用来源数量差异明显（[AI Search and Deep Research Tools Compared](https://felloai.com/ai-search-deep-research-comparison/)）。同期出现的还有"思考时间"更长的变体，如 Gemini 的 Deep Think 采用并行思考技术，可同时生成并权衡多个想法（[Try Deep Think in the Gemini app](https://blog.google/products-and-platforms/products/gemini/gemini-2-5-deep-think/)）。

2026 年 5 月 19 日 Google I/O 上，Search 被升级为以 Gemini 3.5 Flash 作为 AI Mode 的全球默认模型，并推出 25 年来最大的搜索框改版：搜索框可动态展开、支持以文本、图片、文件、视频或 Chrome 标签作为输入；同时引入"信息 Agent"，在后台 7×24 运行，跨网页（博客、新闻、社交帖子）与实时数据（金融、购物、体育）监控变化并推送综合更新（[A new era for AI Search](https://blog.google/products-and-platforms/products/search/search-io-2026/)）。官方称 AI Mode 上线一年月活已超过 10 亿、查询量每季度翻倍以上，并把 Personal Intelligence 扩展至近 200 个国家与地区、98 种语言；此外还加入 agentic booking/calling 及由 Antigravity 与 Gemini 3.5 Flash 驱动的"生成式 UI"与自定义 mini app（同上）。

浏览器入口方面：OpenAI 推出 ChatGPT Atlas，Plus、Pro 与 Business 用户可启用智能体模式，让 ChatGPT 端到端完成任务（如研究饮食计划、生成食材清单、把杂货加入购物车），官方强调关键操作前会征求用户许可（[ChatGPT Atlas - 发行说明](https://help.openai.com/zh-hans-cn/articles/12591856-chatgpt-atlas-release-notes)；[Introducing ChatGPT Atlas](https://openai.com/ko-KR/index/introducing-chatgpt-atlas/)）。Perplexity 的 Comet 浏览器于 2026 年 3 月 23 日从 $200/月改为完全免费，首周登上 iOS App Store 总榜第 3，随后因安全争议排名回落；截至 2026 年中期，Comet 占全球浏览器约 1.9% 份额、月用户增长约 11.5%（[AI Browser Agents Comparison 2026](https://baeseokjae.github.io/posts/ai-browser-agents-comparison-2026/)）。

## 核心技术与关键概念

**检索与合成**：Deep Research 的循环可概括为"制定计划 → 查询 → 阅读结果 → 识别知识缺口 → 再搜索"，即迭代式规划而非一次性检索（[Build with Gemini Deep Research](https://goo.gle/deep-research-agent)）。

**引用与事实性**：降低幻觉、保证引用可溯源是核心目标。官方强调推理核心专门为"减少幻觉、最大化报告质量"训练（同上）。

**运行形态差异**：不同产品在搜索模式与深度研究模式间切换。Gemini 的 Deep Research 运行 5 至 15 分钟以上、涉及数百页来源；Claude 走"网页搜索开关 + Claude Research（Agent 式浏览）"路线，典型耗时从数秒到数分钟、来源数量通常少于 Perplexity 或 ChatGPT（[AI Search and Deep Research Tools Compared](https://felloai.com/ai-search-deep-research-comparison/)）。

**实时性与来源发现**：Perplexity 以"引用优先、实时网页"为特色，适合快速查证与发现最新来源；Gemini 偏重结构化、覆盖面广的解释型回答；Grok 在实时信息上有优势（[I tested ChatGPT's Deep Research against Gemini, Perplexity, and Grok AI](https://geekchamp.com/i-tested-chatgpts-deep-research-against-gemini-perplexity-and-grok-ai-to-see-which-is-best/)）。在响应形态上，Perplexity Pro 典型响应为秒级、引用为行内编号可点击；ChatGPT Search 为秒级至不到一分钟、引用置于答案末尾或侧栏；Gemini Deep Research 为分钟级"报告作业"、引用集中在报告末尾（[Perplexity Pro vs ChatGPT Search vs Gemini Deep Research 2026](https://smartaitoolsreview.com/blog/perplexity-pro-vs-chatgpt-search-vs-gemini-deep-research-2026)）。

**GEO（生成式引擎优化）**：指通过结构化内容、schema 与品牌权威信号，使内容被 ChatGPT、Perplexity、Google AI Overviews、Gemini、Claude 等引擎引用为来源，其目标由传统 SEO 的"排名链接"转向"被 AI 摘要引用"（[GEO in 2026](https://aithinkerlab.com/generative-engine-optimization-2026/)；[What is Generative Engine Optimisation](https://www.langoor.com/blog/what-is-generative-engine-optimisation)）。普林斯顿大学、Georgia Tech 与 IIT Delhi 的 Aggarwal 等（KDD 2024）研究证明，针对性的 GEO 方法可将内容在 AI 答案中的可见度提升最多 40%，"加入统计数据"等手法效果尤为显著（[GEO in 2026](https://aithinkerlab.com/generative-engine-optimization-2026/)；[Reicht klassisches SEO 2026 noch aus?](https://www.drweb.de/generative-engine-optimization-geo/)）。

## 代表性项目 / 产品

- **Google Gemini Deep Research**：由 Gemini 3 Pro 驱动的长时程上下文收集与综合 Agent，提供多步研究计划确认流程（[Build with Gemini Deep Research](https://goo.gle/deep-research-agent)）。
- **Google Search / AI Mode**：以 Gemini 3.5 Flash 为默认模型，引入信息 Agent、agentic booking/calling 与生成式 UI（[A new era for AI Search](https://blog.google/products-and-platforms/products/search/search-io-2026/)）。
- **ChatGPT Deep Research 与 ChatGPT Atlas**：Deep Research 以多步分析、长报告与多来源权衡见长（[I tested ChatGPT's Deep Research…](https://geekchamp.com/i-tested-chatgpts-deep-research-against-gemini-perplexity-and-grok-ai-to-see-which-is-best/)）；Atlas 浏览器内置智能体模式，可在用户许可下执行端到端任务（[ChatGPT Atlas - 发行说明](https://help.openai.com/zh-hans-cn/articles/12591856-chatgpt-atlas-release-notes)）。
- **Perplexity 与 Comet**：以快速事实查证与当前来源发现见长，被评价为"更快、更透明，且是唯一具实质意义的免费选项"（[Best AI for deep research (2026)](https://nesyona.com/articles/perplexity-vs-claude-vs-chatgpt-deep-research-2026)）；Comet 浏览器 2026 年转为免费（[AI Browser Agents Comparison 2026](https://baeseokjae.github.io/posts/ai-browser-agents-comparison-2026/)）。
- **Claude Research**：适合对自有文档做推理、以及长文档与谨慎推理的场景（[AI Search and Deep Research Tools Compared](https://felloai.com/ai-search-deep-research-comparison/)）。

## 关键数据与评测结果

- **DRACO 排行榜**（2026 年 2 月口径）：Gemini Deep Research 59.0%、OpenAI Deep Research (o3) 52.1%、Claude Opus 4.5（标准模型 + 网页搜索 + 代码执行，非深度研究 Agent）46.7%（[DRACO Leaderboard](https://leaderboard.steel.dev/leaderboards/draco)）。
- **LiveResearchBench**（用户视角深度研究在线基准）平均分：Grok-4 Deep Research 69.4、Gemini Deep Research 66.4、Manus 66.3，分项含呈现与组织、事实与逻辑一致性、覆盖与全面性、引用关联（[LiveResearchBench](https://arxiv.org/html/2510.14240v2/)）。
- **多产品的定性排名**（第三方打分）：Perplexity 86、ChatGPT 70、Claude 67、Gemini 65，作者称 Perplexity 以"快、透明、唯一有意义免费"领先，ChatGPT 拥有最长最全面的报告（[Best AI for deep research (2026)](https://nesyona.com/articles/perplexity-vs-claude-vs-chatgpt-deep-research-2026)）。
- **AI 搜索流量份额（多口径，需谨慎）**：一份来源称 2026 年 1 月 ChatGPT 约占全球 AI 聊天助手流量的 60.7%，较 2025 年 1 月的 86.7% 下降 22 个百分点；Google Gemini 约 15%、Microsoft Copilot 约 13.2%（[AI Search Statistics 2026](https://aibusinessweekly.net/p/ai-search-statistics-2026-market-share-zero-click-geo)）。另一来源给出不同数字：ChatGPT 约 60.7%、Gemini 约 21.5%、Copilot 13.2%、Perplexity 5.8%、Claude 4.1%（[KI News](https://reneki.de/news/ki-news/)）；第三份 GEO 指南则给出 ChatGPT 53.7%（同比 +37%）、Gemini 26.7%（+640%）、Claude 7.95%（+300%）的"AI 份额"（[GEO-Guide](https://www.seowerk.de/wp-content/uploads/GEO-Guide-Strategie-Status-quo-7-Juli-2026_seowerk.pdf)）。三者在 Gemini 份额上明显不一致，此处并列呈现。
- **Perplexity 流量口径**：有来源称 Perplexity 在 2026 年 5 月仅占全球 AI 聊天助手网页流量约 1.3%（Momentic 2026 年 7 月报告，引用 Similarweb 数据），位列主要平台第六；但在 Cloudflare 的每日"自愿导航"排名中仅次于 ChatGPT 与 Claude、位居第三，作者指出网页流量口径显著低估了其实际使用（[Perplexity AI Statistics 2026](https://aibusinessweekly.net/p/perplexity-ai-statistics)）。
- **用户规模口径**：有来源称 Google AI Overviews 覆盖超过 20 亿月活、出现在约一半搜索中；ChatGPT 达到 10 亿月活；Perplexity 至 2026 年中期增长至 4500 万 MAU、估值 200 亿美元，同时 Google 仍掌握超过 90% 的搜索量，AI 搜索是快速增长的楔子而非替代品（[AI Search 2026](https://valueaddvc.com/blog/ai-search-2026-perplexity-vs-chatgpt-search-vs-google-ai-overviews-compared)）。
- **Zero-click 现象**：SparkToro 与 Similarweb 的 2026 年 6 月分析称 68.01% 的美国 Google 搜索不再产生任何外链点击（[GEO: How To Build Visibility In The AI Era](https://www.webspero.com/blog/generative-engine-optimization-how-to-build-visibility-in-the-ai-era/)）；另一来源给出 69%，并称在带 AI Overviews 的查询中该比例升至 83%（[Reicht klassisches SEO 2026 noch aus?](https://www.drweb.de/generative-engine-optimization-geo/)）。

## 趋势与争议

一是**份额口径混乱**：上述多个第三方来源对 Gemini 份额、Perplexity 用户规模的统计差异明显，且多基于流量估算而非统一口径，使用时需交叉核验（对比 [AI Search Statistics 2026](https://aibusinessweekly.net/p/ai-search-statistics-2026-market-share-zero-click-geo) 与 [KI News](https://reneki.de/news/ki-news/)）。二是**"答案引擎"对内容生态的冲击**：AI Overviews 与对话式搜索催生 zero-click 现象与 GEO（生成式引擎优化）议题（[GEO: How To Build Visibility In The AI Era](https://www.webspero.com/blog/generative-engine-optimization-how-to-build-visibility-in-the-ai-era/)；[AI Search Statistics 2026](https://aibusinessweekly.net/p/ai-search-statistics-2026-market-share-zero-click-geo)）。三是**浏览器成为新入口**：Atlas 与 Comet 把"搜索"扩展为可执行任务的 Agent 环境，Comet 曾因安全争议排名回落，提示浏览式 Agent 的安全与信任问题尚未解决（[AI Browser Agents Comparison 2026](https://baeseokjae.github.io/posts/ai-browser-agents-comparison-2026/)）。四是**准确率与事实性**：有统计称 Perplexity 的引用错误率最低（约 37%），而部分引擎据称高达 90%，此类数据来自第三方评测，需谨慎对待（[AI Search Platform Comparison 2026](https://pressonify.ai/okf/article/ai-search-platform-comparison-2026.md)）。五是**模型生命周期**：OpenAI 已于 2026 年 2 月 13 日在 ChatGPT 中停用 GPT-4o 等模型（仍可通过 API 使用），说明搜索/研究产品底层模型的迭代节奏很快（[停用 GPT-4o 和其他 ChatGPT 模型](https://help.openai.com/zh-hans-cn/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)）。

## 参考来源

1. [Build with Gemini Deep Research](https://goo.gle/deep-research-agent)
2. [Try Deep Research and our new experimental model in Gemini](https://blog.google/products-and-platforms/products/gemini/google-gemini-deep-research/)
3. [New Gemini app features, available to try at no cost (March 2025)](https://blog.google/products/gemini/new-gemini-app-features-march-2025/)
4. [6 tips to get the most out of Gemini Deep Research](https://blog.google/products-and-platforms/products/gemini/tips-how-to-use-deep-research/)
5. [Try Deep Think in the Gemini app](https://blog.google/products-and-platforms/products/gemini/gemini-2-5-deep-think/)
6. [AI Search and Deep Research Tools Compared (2026)](https://felloai.com/ai-search-deep-research-comparison/)
7. [Best AI for deep research (2026): Perplexity vs Claude vs ChatGPT vs Gemini](https://nesyona.com/articles/perplexity-vs-claude-vs-chatgpt-deep-research-2026)
8. [I tested ChatGPT's Deep Research against Gemini, Perplexity, and Grok AI](https://geekchamp.com/i-tested-chatgpts-deep-research-against-gemini-perplexity-and-grok-ai-to-see-which-is-best/)
9. [DRACO Leaderboard](https://leaderboard.steel.dev/leaderboards/draco)
10. [LiveResearchBench: A Live Benchmark for User-Centric Deep Research in the Wild](https://arxiv.org/html/2510.14240v2/)
11. [AI Search Statistics 2026: Market Share, Zero-Click & GEO](https://aibusinessweekly.net/p/ai-search-statistics-2026-market-share-zero-click-geo)
12. [KI News](https://reneki.de/news/ki-news/)
13. [AI Search 2026: Perplexity vs ChatGPT Search vs Google AI Overviews Compared](https://valueaddvc.com/blog/ai-search-2026-perplexity-vs-chatgpt-search-vs-google-ai-overviews-compared)
14. [AI Search Platform Comparison 2026](https://pressonify.ai/okf/article/ai-search-platform-comparison-2026.md)
15. [停用 GPT-4o 和其他 ChatGPT 模型 — OpenAI Help Center](https://help.openai.com/zh-hans-cn/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)
16. [A new era for AI Search — Google Blog](https://blog.google/products-and-platforms/products/search/search-io-2026/)
17. [ChatGPT Atlas - 发行说明 — OpenAI Help Center](https://help.openai.com/zh-hans-cn/articles/12591856-chatgpt-atlas-release-notes)
18. [Introducing ChatGPT Atlas — OpenAI](https://openai.com/ko-KR/index/introducing-chatgpt-atlas/)
19. [AI Browser Agents Comparison 2026: Comet vs Browser-Use vs Operator](https://baeseokjae.github.io/posts/ai-browser-agents-comparison-2026/)
20. [Perplexity Pro vs ChatGPT Search vs Gemini Deep Research: AI Search Compared (2026)](https://smartaitoolsreview.com/blog/perplexity-pro-vs-chatgpt-search-vs-gemini-deep-research-2026)
21. [Generative Engine Optimization (GEO) in 2026](https://aithinkerlab.com/generative-engine-optimization-2026/)
22. [Reicht klassisches SEO 2026 noch aus? — drweb.de](https://www.drweb.de/generative-engine-optimization-geo/)
23. [What is Generative Engine Optimisation (GEO)?](https://www.langoor.com/blog/what-is-generative-engine-optimisation)
24. [GEO-Guide: Was wir sicher über Generative Engine Optimization wissen](https://www.seowerk.de/wp-content/uploads/GEO-Guide-Strategie-Status-quo-7-Juli-2026_seowerk.pdf)
25. [Perplexity AI Statistics 2026: Users, Revenue & Growth](https://aibusinessweekly.net/p/perplexity-ai-statistics)
26. [Generative Engine Optimization: How To Build Visibility In The AI Era](https://www.webspero.com/blog/generative-engine-optimization-how-to-build-visibility-in-the-ai-era/)