# AI 发展史与关键里程碑

> 最后更新：2026-09-26 ｜ 领域：AI·基础原理 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

人工智能（Artificial Intelligence, AI）作为一个被正式命名的学科，通常以 1956 年在美国达特茅斯学院（Dartmouth College）举办的暑期研讨会为起点，正是在这次会议上 "artificial intelligence" 一词被采纳，该领域被组织为一个正式的研究计划（[History of Artificial Intelligence](https://aiwiki.ai/wiki/history_of_artificial_intelligence)、[Artificial Intelligence](https://aiwiki.ai/wiki/artificial_intelligence)）。其思想根基更早：包括形式逻辑、1943 年提出的第一个神经元的数学模型，以及 Alan Turing 1950 年提出的机器智能测试（即图灵测试）（[Artificial Intelligence](https://aiwiki.ai/wiki/artificial_intelligence)、[History of Artificial Intelligence](https://aiwiki.ai/wiki/history_of_artificial_intelligence)）。

此后近七十年，AI 在符号主义、专家系统与连接主义之间多次更替范式，并经历过两次资金与关注度急剧下降的"AI 寒冬"：第一次约为 1974–1980 年，第二次约为 1987 年至 1990 年代中期。两次寒冬的成因高度相似——某个特定技术路线被过度乐观地投资，随后遭遇其支持者未曾言明的基础性局限，最终政府与商业资助方撤资（[History of Artificial Intelligence: Complete Timeline 1943-2026](https://aibusinessweekly.net/p/history-of-artificial-intelligence)）。

## 最新进展（2025–2026）

2025–2026 年是生成式 AI 从"对话"走向"推理"与"系统工程"的阶段。

- **DeepSeek-R1（2025 年 1 月）**：以强化学习激励推理能力（RLVR 路线），在数学与代码基准上大幅提升。据其技术报告，DeepSeek-R1 在 AIME 2024 上达到 79.8% Pass@1，略超 OpenAI-o1-1217；在 MATH-500 上达到 97.3%，与 OpenAI-o1-1217 相当（[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948)）。第三方梳理称该模型于 2025 年 1 月 20 日发布、以 MIT 许可开放权重，在数学、代码与推理上追平 OpenAI o1，其发布还引发了一轮全球科技股抛售（[DeepSeek-R1](https://theairankings.com/deepseek/deepseek-r1/)）。上线初期热度极高：第三方机构数据显示"上线 21 天，日活用户 2215 万"（[2025人工智能破壁时刻｜DeepSeek火爆一年间-新华网](https://www.news.cn/digital/20251211/80f702c6c7934ba58497c508d46aeb1c/c.html)），光明网的一篇综述也把 DeepSeek 列为中国大模型发展的重要里程碑（[人工智能的技术发展与未来展望](https://news.gmw.cn/2026-01/24/content_38555703.htm)）。有观点认为，DeepSeek-R1 证明纯 RL 在可验证奖励任务上能产生 o1 级推理能力、无需人工编写 CoT 数据，并开启了 2026 年一批衍生推理模型（QwQ、GLM-Zero、Kimi-Thinking 等）（[DeepSeek-R1](https://llms3.com/node/deepseek-r1)）。
- **GPT-5 世代**：OpenAI 的 GPT-5 于 2025 年 8 月 7 日发布，是一个统一系统，通过实时路由器在"快速模型"与"深度推理模型（GPT-5 thinking）"之间分配思考预算（[OpenAI GPT Model Release Timeline](https://hidekazu-konishi.com/entry/openai_gpt_model_release_timeline.html)）。此后迭代加快：GPT-5.1（2025 年 11 月）、GPT-5.2（2025 年 12 月）相继推出（[OpenAI GPT Model Release Timeline](https://hidekazu-konishi.com/entry/openai_gpt_model_release_timeline.html)）。另有资料称 GPT-5 相较 GPT-4o 减少约 45% 的事实性错误，ChatGPT 内上下文为 256k，API 为 400k（[ChatGPT](https://aiwiki.ai/wiki/chatgpt/edit)）。
- **2026 年的多款前沿模型**：据多家时间线整理，2026 年 9 月初 72 小时内三家实验室接连发布旗舰模型——Anthropic 的 Claude Fable 5.1 与 Mythos 5.1、Google 的 Gemini 3.8 Flash 与 3.8 Flash Cyber、OpenAI 的 GPT-6 Astra（[Three Frontier Models in 72 Hours: What Changed in September 2026](https://esso.dev/blog-posts/three-frontier-models-in-72-hours-what-changed-in-september-2026)）。其中 OpenAI 于 2026 年 9 月 3 日发布 GPT-6 Astra，并披露其为首个在其 Preparedness Framework 下达到"Critical"网络安全等级的模型；该等级被定义为能在无人类逐步引导的情况下识别并开发针对真实加固系统的可用零日漏洞，据称该模型在预发布评测中取得 100% 的利用（Exploit）得分（[News — The History of Artificial Intelligence](https://aihistoryproject.org/news)）；9 月 22 日又推出 GPT-6 家族中更低价的 GPT-6 Sol 与 GPT-6 Luna，Sol 定价 $2/$10 每百万 token（约为前代一半），Luna 面向高并发快速任务、定价 $0.10/$0.50（[AI models released in 2026](https://llmgateway.io/timeline/2026)、[AI Timeline](https://www.aicodex.to/timeline)）。Google 的 Gemini 3.8 Flash 于 2026 年 9 月 2 日发布（[AI models released in 2026](https://llmgateway.io/timeline/2026)），其 Gemini API 版本说明亦记录 2026 年 9 月 22 日 Gemini 3.8 Flash TTS 与 Flash-Lite TTS 正式发布（[版本说明 | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/changelog?hl=zh-cn)）。

- **2026 年的政策与产业节点**：据一份时间线整理，2026 年 6 月 2 日签署了与前沿 AI 相关的行政令（Executive Order 14409），同期 Anthropic 在一轮 650 亿美元融资后向 SEC 保密提交了 S-1 草案，并可能最早于 2026 年 10 月上市（[The Road to AGI](https://ai-timeline.org/)）；另一份时间线整理则列出 2026 年 9 月 OpenAI 开始推送 GPT-6 Astra、并扩展到面向计算机使用、编程、科学与专业工作的新一代模型等事件（[2026](https://shawnhack.com/timeline/2026)）。需说明的是，这类条目多来自第三方时间线汇编，具体表述与细节应以官方公告为准。

## 核心脉络与关键里程碑

从符号主义到深度学习的复兴，关键节点如下。

- **1950**：Alan Turing 发表关于机器智能测试的论文，为 AI 提供哲学与概念奠基（[Artificial Intelligence](https://aiwiki.ai/wiki/artificial_intelligence)）。
- **1956**：达特茅斯会议，AI 正式成为一门学科（[History of Artificial Intelligence](https://aiwiki.ai/wiki/history_of_artificial_intelligence)）。
- **1974–1980 与 1987–1990 年代中期的两次寒冬对照**：第一次由对开放式符号 AI 的期望落空触发，第二次则由专家系统狂热退潮触发；两次的共同点是某条技术路线被过度投资、遭遇支持者未曾言明的基础局限后，政府与商业资助方撤资（[History of Artificial Intelligence: Complete Timeline 1943-2026](https://aibusinessweekly.net/p/history-of-artificial-intelligence)、[Expert Systems and the First AI Winter](https://www.geschichte-der-informatik.de/articles/expert_systems_and_the_first_ai_winter/)）。
- **1970 年代**：对开放式符号 AI 的期望落空，Lighthill 报告与随之而来的资助削减引发第一次寒冬（[Expert Systems and the First AI Winter](https://www.geschichte-der-informatik.de/articles/expert_systems_and_the_first_ai_winter/)）。研究界转而收窄目标、在界定清晰的封闭领域中求生存，从而催生了"专家系统"这一路线（[Expert Systems Boom and Second AI Winter (1980–1993)](https://theepochzero.show/applied_ai/introduction_to_ai_and_history/10_expert_systems_boom_and_second_ai_winter_1980_1993/)）。
- **1980 年代**：专家系统繁荣，XCON、MYCIN 等系统被宣传为可为各行业节省巨额成本（[The Boom and Bust of Expert Systems During the 1980s](https://robotsauthority.com/the-boom-and-bust-of-expert-systems-during-the-1980s/)）。但专家系统"脆弱（brittle）"——在训练领域内表现良好，一旦越出边界便不可预测地失败（[Expert Systems and the First AI Winter](https://www.geschichte-der-informatik.de/articles/expert_systems_and_the_first_ai_winter/)）；其开发与维护成本高昂、难以适配，最终随 1987–1993 年的崩溃进入第二次寒冬（[Implications for AI Research: Applying Lessons from the Expert Systems Boom and Bust to the Current Large-Language Model Boom](https://ojs.aaai.org/index.php/AAAI/article/download/41334/45295)）。该时期还伴随美国 Strategic Computing Initiative 与日本 Fifth Generation Project 等政府资助计划，它们与"在知识中蕴含力量"的信念共同推动了专家系统与专用 Lisp 机器的繁荣（[Implications for AI Research](https://ojs.aaai.org/index.php/AAAI/article/download/41334/45295)）。
- **2012**：AlexNet 在 ImageNet 图像分类竞赛中夺冠，top-5 错误率约 15.3%，比上一年冠军下降约十个百分点；其成功要素包括 GPU、大规模数据集、深层卷积、ReLU、数据增强与 dropout，被广泛视为深度学习成为计算机视觉主流方向的转折点（[图文详情——科普中国资源服务](https://cloud.kepuchina.cn/h5/detail?id=7479623085172092928)、[A Milestone History of Artificial Intelligence](https://theagiclock.com/articles/milestone-history-of-artificial-intelligence/)）。
- **2013**：word2vec 以向量表示词语，推动词嵌入成为主流（[A Milestone History of Artificial Intelligence](https://theagiclock.com/articles/milestone-history-of-artificial-intelligence/)）。
- **2016**：Google 的 AlphaGo 击败围棋世界冠军李世石（Lee Sedol），攻下此前被认为对计算机过于复杂的棋类（[Artificial Intelligence](https://aiwiki.ai/wiki/artificial_intelligence)、[The History of AI](https://99aiskills.com/en/courses/ai-fundamentals/lesson/history-of-ai)）。
- **2017**：Google 研究者发表论文《Attention Is All You Need》，提出 Transformer 架构，成为此后所有主流大语言模型的基础（[The History of AI](https://99aiskills.com/en/courses/ai-fundamentals/lesson/history-of-ai)、[Artificial Intelligence](https://aiwiki.ai/wiki/artificial_intelligence)）。
- **2018**：GPT-1 于该年 6 月发布（[GPT-5 History Timeline & OpenAI Evolution (2015–2026)](https://aitimeline.in/gpt-5-history-timeline-openai-evolution-1334/)）。
- **2020**：GPT-3 发布，AlphaFold 2 解决蛋白质折叠问题（[Artificial Intelligence](https://aiwiki.ai/wiki/artificial_intelligence)）。
- **2022 年 11 月 30 日**：ChatGPT 发布，开启生成式 AI 的大众化浪潮（[GPT-5 History Timeline & OpenAI Evolution (2015–2026)](https://aitimeline.in/gpt-5-history-timeline-openai-evolution-1334/)）。
- **2023 年末起的模型节奏**：有整理指出 Google 的年度节奏大致为 Gemini 1.0（2023 年末）、2.0（2024 年末）、3.0（2025 年末）（[Every AI Model Coming in 2026–2027 — Father of AI](https://www.fatherofai.in/blog/every-ai-model-coming-2026-2027-release-calendar/)）。

## 趋势与争议

- **规模化到推理时计算**：从"更大模型"转向"更多思考时间"，GPT-5 的智能路由器与 DeepSeek-R1 的 RLVR 是两条代表性路线（[OpenAI GPT Model Release Timeline](https://hidekazu-konishi.com/entry/openai_gpt_model_release_timeline.html)、[DeepSeek-R1](https://arxiv.org/pdf/2501.12948)）。
- **开源与闭源并进**：DeepSeek 等开放权重模型的出现，使中美在大模型上的追赶周期缩短，也引发关于技术路线是否趋同的讨论（[人工智能的技术发展与未来展望](https://news.gmw.cn/2026-01/24/content_38555703.htm)）。
- **"寒冬"叙事本身存在争议**：有观点（CACM 评论）认为所谓"1970 年代第一次 AI 寒冬"并未真正发生，真正的寒冬是 1980 年代以专家系统为中心的政府资助泡沫破裂后、长达二十年的低迷（[How the AI Boom Went Bust](https://cacm.acm.org/opinion/how-the-ai-boom-went-bust/)）。学界已开始系统地把"专家系统狂热—崩盘"的历史教训对照当前 LLM 热潮（[Implications for AI Research](https://ojs.aaai.org/index.php/AAAI/article/download/41334/45295)）。
- **用户规模量级变化**：有资料称截至 2026 年 ChatGPT 的月活约 10 亿、周活约 9 亿（[GPT-5 History Timeline & OpenAI Evolution (2015–2026)](https://aitimeline.in/gpt-5-history-timeline-openai-evolution-1334/)）；不同来源口径不一，引用时需谨慎核对。
- **历史周期律的警示**：此前的 AI 寒冬表明，"过度承诺—基础局限—撤资"的循环可能重演；当前对推理与 Agent 的预期管理，成为行业反复讨论的话题（[History of Artificial Intelligence: Complete Timeline 1943-2026](https://aibusinessweekly.net/p/history-of-artificial-intelligence)）。
- **"封闭域有效"与"开放世界泛化"的鸿沟**：专家系统的核心教训并不在算法优劣，而在于它们只在界定清晰的领域内可靠、越界即失效；这一区分被反复用来审视当前 LLM 的能力边界与部署前提（[Expert Systems and the First AI Winter](https://www.geschichte-der-informatik.de/articles/expert_systems_and_the_first_ai_winter/)、[The Boom and Bust of Expert Systems During the 1980s](https://robotsauthority.com/the-boom-and-bust-of-expert-systems-during-the-1980s/)）。

## 参考来源

- [History of Artificial Intelligence](https://aiwiki.ai/wiki/history_of_artificial_intelligence)
- [History of Artificial Intelligence: Complete Timeline 1943-2026](https://aibusinessweekly.net/p/history-of-artificial-intelligence)
- [Artificial Intelligence](https://aiwiki.ai/wiki/artificial_intelligence)
- [A Milestone History of Artificial Intelligence](https://theagiclock.com/articles/milestone-history-of-artificial-intelligence/)
- [The History of AI](https://99aiskills.com/en/courses/ai-fundamentals/lesson/history-of-ai)
- [图文详情——科普中国资源服务](https://cloud.kepuchina.cn/h5/detail?id=7479623085172092928)
- [人工智能的技术发展与未来展望——光明网](https://news.gmw.cn/2026-01/24/content_38555703.htm)
- [ChatGPT](https://aiwiki.ai/wiki/chatgpt/edit)
- [GPT-5 History Timeline & OpenAI Evolution (2015–2026)](https://aitimeline.in/gpt-5-history-timeline-openai-evolution-1334/)
- [OpenAI GPT Model Release Timeline](https://hidekazu-konishi.com/entry/openai_gpt_model_release_timeline.html)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948)
- [Expert Systems and the First AI Winter](https://www.geschichte-der-informatik.de/articles/expert_systems_and_the_first_ai_winter/)
- [Expert Systems Boom and Second AI Winter (1980–1993)](https://theepochzero.show/applied_ai/introduction_to_ai_and_history/10_expert_systems_boom_and_second_ai_winter_1980_1993/)
- [The Boom and Bust of Expert Systems During the 1980s](https://robotsauthority.com/the-boom-and-bust-of-expert-systems-during-the-1980s/)
- [How the AI Boom Went Bust (CACM)](https://cacm.acm.org/opinion/how-the-ai-boom-went-bust/)
- [Implications for AI Research: Lessons from the Expert Systems Boom and Bust](https://ojs.aaai.org/index.php/AAAI/article/download/41334/45295)
- [2025人工智能破壁时刻｜DeepSeek火爆一年间-新华网](https://www.news.cn/digital/20251211/80f702c6c7934ba58497c508d46aeb1c/c.html)
- [DeepSeek-R1 (The AI Rankings)](https://theairankings.com/deepseek/deepseek-r1/)
- [DeepSeek-R1 (llms3.com)](https://llms3.com/node/deepseek-r1)
- [Three Frontier Models in 72 Hours: What Changed in September 2026](https://esso.dev/blog-posts/three-frontier-models-in-72-hours-what-changed-in-september-2026)
- [News — The History of Artificial Intelligence](https://aihistoryproject.org/news)
- [AI models released in 2026 (LLM Gateway)](https://llmgateway.io/timeline/2026)
- [AI Timeline](https://www.aicodex.to/timeline)
- [版本说明 | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/changelog?hl=zh-cn)
- [Every AI Model Coming in 2026–2027 — Father of AI](https://www.fatherofai.in/blog/every-ai-model-coming-2026-2027-release-calendar/)