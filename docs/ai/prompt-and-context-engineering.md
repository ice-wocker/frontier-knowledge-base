# 提示工程与上下文工程（Prompt & Context Engineering）

> 最后更新：2026-09-26 ｜ 领域：AI·提示、Agent 与应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

提示工程（Prompt Engineering）指通过设计输入文本、指令格式与示例来引导大语言模型（LLM）产生期望输出的方法体系；上下文工程（Context Engineering）则是范围更宽的概念，关注在推理时向模型提供的**全部**信息——系统提示、工具定义、记忆、检索结果、文件与 Skills 等——如何被组装、压缩与管理（[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)）。Anthropic 指出，当用户向 Claude 发送一条消息时，提示只是模型所获上下文的一小部分，大量上下文来自系统提示、Skills、CLAUDE.md 文件与记忆等来源；与一次性、可高度特化的提示不同，上下文会在许多请求间复用，因此不能写得同样具体（同上）。Anthropic 还强调，Agent 的文件与目录结构本身也是一种上下文工程形式（[Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)）。

Anthropic 官方将「上下文」定义为采样时纳入的 token 集合，而「工程」问题则是在 LLM 固有约束下优化这些 token 的效用，以稳定达成期望结果；其把上下文工程视为提示工程的"自然演进"，因为构建运行多轮推理的 Agent 时需要管理整个上下文状态（系统指令、工具、外部数据、消息历史等）（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。第三方指南进一步把上下文工程定义为"刻意设计进入 LLM 上下文窗口的一切——指令、记忆、工具结果与对话状态"（[Context Engineering for AI Agents 2026: The Complete Guide](https://tutorials.technology/tutorials/context-engineering-ai-agents-2026.html)）。

## 2025–2026 最新进展

2025 年 Anthropic 发布《Effective context engineering for AI agents》（Published Sep 29, 2025），建议把提示组织为明确分区（如 `<background_information>`、`<instructions>`、`## Tool guidance`、`## Output description`），并使用 XML 标签或 Markdown 标题分隔各区块，同时承认提示的具体格式正变得越来越不重要（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。同一日（2025-09-29）Anthropic 在 Claude Developer Platform 上推出 context editing（上下文编辑）与 memory tool（记忆工具），用于帮助开发者构建能处理长时任务、更有效的 Agent；Claude Sonnet 4.5 还增强了内置的上下文感知（context awareness），可全程跟踪可用 token 以更有效地管理上下文（[Managing context on the Claude Developer Platform](https://claude.com/blog/context-management)）。针对跨越多个上下文窗口的长任务，Anthropic 提出"两段式"方案：一个 initializer agent 在首次运行时搭建环境，另一个 coding agent 在每个会话中做增量推进，并为下一次会话留下清晰产物（[Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)）。

在生产实践中，2026 年的指南把"上下文"拆为系统上下文（system context：硬规则、工具使用策略、升级条件、输出 schema，且需版本化、不可在聊天界面里手工改生产指令）与任务上下文（task context：当前用户目标与工作流已知的结构化字段，如租户/用户 ID、产品标识、当前工作流节点、所需输出类型），并强调任务上下文应显式且类型化，而非只埋在自由文本对话里（[Context Engineering for Production AI Agents in 2026](https://dev.to/jasminshukla/context-engineering-for-production-ai-agents-in-2026-beyond-prompt-engineering-and-basic-rag-5564)）。另有工程实践强调"先盘点知识、再连接索引、检索前先消解冲突"：凡 Agent 无法触达的关键决策都可能变成未来的"自信错误答案"，故应把来源接入可检索存储并定义冲突规则（时效、来源权威性、人工覆盖）（[Context Engineering for AI Agents: Why the Build Is Easy and the Context Is Not (2026)](https://dev.to/shaam_ai/context-engineering-for-ai-agents-why-the-build-is-easy-and-the-context-is-not-2026-m4o)）。

在自动提示优化方面，DSPy 于 2025 年引入 **GEPA（Genetic-Pareto）反思式提示优化器**，该方法出自论文《GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning》，可自适应演化任意系统的文本组件（如提示），除标量分数外还允许指标返回文本反馈供语言模型参考（[dspy.GEPA: Reflective Prompt Optimizer](https://dspy.ai/api/optimizers/GEPA/overview/)）。GEPA 由独立 `gepa` 包提供，会捕获 DSPy 模块执行的完整 trace、定位需修改的部分，并维护一个候选程序种群，在验证集上打分后由 LLM 的"反思"步骤基于指标的逐预测器自然语言反馈提出指令修改；其 Pareto 前沿采样与反思式提案机制是它与 COPRO、MIPROv2 的关键区别，指标契约形如 `dspy.Prediction(score, feedback)`（[GEPA in depth](https://dspy.ai/diving-deeper/gepa-in-depth/)）。GEPA 已进入官方生态：OpenAI Cookbook（2025 年 11 月）以 GEPA 构建自主自愈工作流，Greptile 的《State of AI Coding 2025》报告也将其列为 AI 编码能力的关键进展，并称 GEPA 通过 trace 分析演化提示、以远少于强化学习的 rollout 次数达到相近表现（[Showcase — GEPA](https://gepa-ai.github.io/gepa/guides/use-cases/)）。DSPy 3.0 被描述为提示工程工作流的一次重大转变：开发者定义类型化 Signature（输入→输出及描述）、提供标注示例，框架自动为目标模型与任务编译优化提示（[Advanced Prompt Engineering Techniques Every Developer Should Know in 2026](https://baeseokjae.github.io/posts/prompt-engineering-techniques-2026/)）。

## 核心技术与关键概念

**思维链（Chain-of-Thought, CoT）**：鼓励模型在给出最终答案前生成中间推理步骤，只需提示模型"逐步思考"或提供分步示例；在数学、逻辑与分析类任务上尤为有效（[Prompt Engineering Fundamentals](https://yarmoluk.github.io/Digital-Transformation-with-AI-Spring-2026/chapters/04-prompt-engineering/)）。DSPy 等框架不再使用手写的固定 CoT 模板，而是按错误反馈、任务难度或所需推理类型动态增删、调整推理步骤（[Optimizing LLM Prompt Engineering with DSPy-Based Declarative Learning](https://arxiv.org/pdf/2604.04869)）。

**少样本提示（Few-shot）**：利用上下文学习（in-context learning），示例的质量、多样性与相关性显著影响效果；零样本提示适用于常见且定义明确的任务，清晰的指令与显式约束能提升结果（[Prompt Engineering Fundamentals](https://yarmoluk.github.io/Digital-Transformation-with-AI-Spring-2026/chapters/04-prompt-engineering/)）。

**自一致性（Self-Consistency）**：不再只运行一次提示，而是在较高温度下采样多条独立推理路径，再以多数投票决定最终答案，比信任单条思维链更可靠；代价是调用次数变为 N 倍，因此适合高价值、一次性的问题，而非高并发批量请求（[Advanced Prompt Engineering Techniques (2026)](https://aipromptshub.co/blog/advanced-prompt-engineering-techniques)；[What Is Self-Consistency?](https://ai-tldr.dev/learn/prompt-engineering/reasoning-techniques/self-consistency-prompting/)）。学术综述也将 Self-Consistency 描述为一种解码策略：先采样多条多样化推理路径，再通过多数投票聚合最终答案（[LLMs Can Generate a Better Answer by Aggregating Their Own Responses](https://arxiv.org/html/2503.04104)）。

**ReAct 与反思类提示**：ReAct 交替进行推理与动作；Self-Refine（Madaan et al., 2023）等则以"草稿—批判—修订"循环迭代改进输出（[SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://arxiv.org/pdf/2507.07441.pdf)）。多路径的响应式与反思式 Agent 框架（RR-MP）把多路径推理与反思结合，以提升科学推理准确率（[Enhancing LLM Reasoning with Multi-Path Collaborative Reactive and Reflection agents](https://arxiv.org/html/2501.00430v2)）。在线自校正方向还出现了"反思式置信度"（Reflective Confidence）等通过动态组装反射提示来纠正推理缺陷的工作（[REFLECTIVE CONFIDENCE: CORRECTING REASONING FLAWS VIA ONLINE SELF-CORRECTION](https://arxiv.org/pdf/2512.18605)）。

**系统提示设计**：系统提示用于建立持久的上下文与行为，精心设计的角色（persona）可带来一致的用户体验（[Prompt Engineering Fundamentals](https://yarmoluk.github.io/Digital-Transformation-with-AI-Spring-2026/chapters/04-prompt-engineering/)）。Anthropic 提出系统提示应处于"恰当高度"（right altitude）——既不能把复杂、脆弱的逻辑硬编码进提示（导致脆弱与维护困难），也不能只给模糊的高层指引，而应"具体到能有效引导行为，又灵活到能提供强启发式"（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。

**上下文的分层模型**：第三方资料把 Agent 上下文拆为五个层次——系统提示（角色、语气、硬约束）、仓库上下文（代码可读性，如 AGENTS.md、类型、测试）、工具面（MCP：Agent 能做什么）、记忆与会话（跨轮次与跨运行持久化的内容）、可观测性（可度量与改进的内容），并给出各自的常见失败模式（[Context Engineering for AI Agents: Building Context-Rich Environments](https://www.metacto.com/blogs/context-rich-environments-ai-agents)）。

**上下文的"相关性"与"充分性"原则**：一篇 2026 年的论文指出，上下文应遵循 Relevant（只给当前步骤必需的信息，过多上下文会造成 lost-in-the-middle 退化并增加成本）、Sufficient（须包含决策所需全部内容，否则 Agent 会幻觉、臆造）等原则，即"好的上下文不是'所有可用信息'，而是'决策所需的最小充分信息'"（[Context Engineering: From Prompts to Corporate Multi-Agent Architecture](https://arxiv.org/pdf/2603.09619v2)）。

**上下文压缩、即时检索与自动提示优化（DSPy）**：Anthropic 提出 long-horizon 任务的三种手段——compaction（把接近窗口上限的对话摘要后重启新窗口）、结构化笔记与多 Agent 架构，并推崇 "just in time" 检索（维护文件路径、存储查询、网页链接等轻量标识符，运行时用工具动态加载数据），CLAUDE.md 是先放上下文、glob/grep 是做即时导航的混合策略（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。DSPy 的优化器（原称 Teleprompters）可分两类——指令优化与少样本示例优化：`COPRO` 生成并精炼各步骤的新指令，用指标与训练集做坐标上升（爬山法）优化；`MIPROv2`（Multiprompt Instruction PRoposal Optimizer Version 2）可联合优化指令与少样本示例，做法是先自举少样本示例候选、基于任务不同动态提出指令，再用贝叶斯优化寻找最优组合（[DSPy Optimizers](https://dspy.ai/learn/optimization/optimizers/)；[dspy.MIPROv2](https://dspy.ai/api/optimizers/MIPROv2/)）。生产环境指南把 DSPy 的核心抽象归纳为 Signatures、Modules、Optimizers 三者（[Production Prompt Engineering in 2026](https://aiworkflowlab.dev/article/production-prompt-engineering-2026-structured-outputs-prompt-chaining-dspy)）。

## 代表性项目 / 工具

- **DSPy**：把 LLM 程序编译到指标上，用户给出示例与评分函数，框架自动调优提示直至质量收敛；官方示例 `dspy.GEPA(metric=..., auto="medium")` 与 `compile` 接口（[DSPy 官网](https://dspy.ai/)）。DSPy 是来自 Stanford NLP 的 Python 框架，用类型化签名与可组合模块替代脆弱的字符串提示，再用 MIPROv2 等优化器把程序编译为优化后的提示（或微调权重）（[DSPy 3.0 in Python: Programming (Not Prompting) LLMs in 2026](https://pythondatabench.com/article/dspy-3-python-programming-llms-2026)）。
- **GEPA**：DSPy 的反思驱动指令优化器，可由独立 `gepa` 包提供并支持自定义 reflection prompt 与自定义 proposer，例如可约束"生成的提示不超过 5000 字"（[Showcase — GEPA](https://gepa-ai.github.io/gepa/guides/use-cases/)；[Frequently Asked Questions — GEPA](https://gepa-ai.github.io/gepa/guides/faq/)）。
- **Anthropic 上下文工程实践**：以 Skills、CLAUDE.md、记忆与文件系统构成 Agent 的"上下文生态"，代码/日志等大文件通过 `grep`、`tail` 等由模型自主决定加载方式（[Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)）；平台侧提供 context editing 与 memory tool（[Managing context on the Claude Developer Platform](https://claude.com/blog/context-management)）。
- **Claude 5 时代的上下文工程规则**：官方博客公开了面向新一代模型调整提示与上下文组织的建议（[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)）。

## 关键数据与评测结果

- Self-Consistency 在数学推理与常识问答上取得成功，但应用到开放式任务时存在局限（[LLMs Can Generate a Better Answer by Aggregating Their Own Responses](https://arxiv.org/html/2503.04104)）。
- DSPy 优化器迭代时间线：MIPROv2 于 2024 年 6 月发布，用于同时优化指令与示例；GEPA 于 2025 年推出，支持基于反思的指令改进（[DSPy 官网](https://dspy.ai/)）。
- 大学课程材料将零样本、少样本、思维链与树状思维（Tree-of-Thought）、自一致性并列为难度递增的提示技术，指出进阶技术在提升效果的同时也增加成本（[Prompt Engineering Fundamentals](https://yarmoluk.github.io/Digital-Transformation-with-AI-Spring-2026/chapters/04-prompt-engineering/)）。
- 第三方指南称精心工程化的上下文窗口可把同一底层模型上的 Agent 任务完成率从约 30% 提升到约 90%（[Context Engineering for AI Agents 2026](https://tutorials.technology/tutorials/context-engineering-ai-agents-2026.html)，该数值为第三方口径，未见一手实验出处）。
- 关于"上下文退化"：needle-in-a-haystack 类基准揭示了 context rot（上下文中 token 越多，模型准确召回信息的能力越弱），且该特性在所有模型上均出现，只是退化斜率不同（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。

## 趋势与争议

一是**从"提示"到"上下文"的重心迁移**：业界共识逐渐转向认为 Agent 的质量更多取决于上下文如何被结构化与管理，而非模型本身；即便较弱的 LLM，配上恰当上下文也能表现良好，而再强的模型也无法弥补糟糕的上下文（[A Guide for Effective Context Engineering for AI Agents](https://www.marktechpost.com/2025/10/20/a-guide-for-effective-context-engineering-for-ai-agents/)）。二是**提示格式是否仍然重要的分歧**：Anthropic 一方面给出 XML/ Markdown 分区建议，另一方面也承认提示的具体格式正变得不那么关键（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。三是**自动化 vs 手工**：DSPy/GEPA 类自动优化器试图以指标驱动替代手工调参，但这要求高质量的训练集与评分函数，其效果高度依赖指标设计。四是**上下文长度策略的分歧**：一派主张等待更大窗口，另一派（如 Anthropic）认为任何规模的窗口在追求最强表现时都会遭遇上下文污染，因而更需要 compaction、结构化笔记与多 Agent 架构（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。五是**成本权衡**：自一致性、树状思维等技术的收益以成倍调用为代价，是否值得需结合实际任务度量（[Advanced Prompt Engineering Techniques (2026)](https://aipromptshub.co/blog/advanced-prompt-engineering-techniques)）。

## 参考来源

1. [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
2. [Effective context engineering for AI agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
3. [Building agents with the Claude Agent SDK — Anthropic](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
4. [A Guide for Effective Context Engineering for AI Agents — MarkTechPost](https://www.marktechpost.com/2025/10/20/a-guide-for-effective-context-engineering-for-ai-agents/)
5. [dspy.GEPA: Reflective Prompt Optimizer](https://dspy.ai/api/optimizers/GEPA/overview/)
6. [dspy.MIPROv2](https://dspy.ai/api/optimizers/MIPROv2/)
7. [DSPy Optimizers (formerly Teleprompters)](https://dspy.ai/learn/optimization/optimizers/)
8. [DSPy 官网](https://dspy.ai/)
9. [Prompt Engineering Fundamentals](https://yarmoluk.github.io/Digital-Transformation-with-AI-Spring-2026/chapters/04-prompt-engineering/)
10. [Advanced Prompt Engineering Techniques (2026)](https://aipromptshub.co/blog/advanced-prompt-engineering-techniques)
11. [What Is Self-Consistency? Sampling Multiple Answers and Voting](https://ai-tldr.dev/learn/prompt-engineering/reasoning-techniques/self-consistency-prompting/)
12. [LLMs Can Generate a Better Answer by Aggregating Their Own Responses](https://arxiv.org/html/2503.04104)
13. [Enhancing LLM Reasoning with Multi-Path Collaborative Reactive and Reflection agents](https://arxiv.org/html/2501.00430v2)
14. [REFLECTIVE CONFIDENCE: CORRECTING REASONING FLAWS VIA ONLINE SELF-CORRECTION](https://arxiv.org/pdf/2512.18605)
15. [SAND: Boosting LLM Agents with Self-Taught Action Deliberation](https://arxiv.org/pdf/2507.07441.pdf)
16. [University of Mannheim IE685 LLMs and Agents — Prompt Engineering](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Teaching/Large_Language_Models_and_Agents/FSS2026/IE685_LA_03_PromptEngineering.pdf)
17. [Managing context on the Claude Developer Platform](https://claude.com/blog/context-management)
18. [Effective harnesses for long-running agents — Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
19. [Context Engineering for AI Agents 2026: The Complete Guide](https://tutorials.technology/tutorials/context-engineering-ai-agents-2026.html)
20. [Context Engineering for AI Agents: Building Context-Rich Environments](https://www.metacto.com/blogs/context-rich-environments-ai-agents)
21. [Context Engineering for Production AI Agents in 2026](https://dev.to/jasminshukla/context-engineering-for-production-ai-agents-in-2026-beyond-prompt-engineering-and-basic-rag-5564)
22. [Context Engineering for AI Agents: Why the Build Is Easy and the Context Is Not (2026)](https://dev.to/shaam_ai/context-engineering-for-ai-agents-why-the-build-is-easy-and-the-context-is-not-2026-m4o)
23. [Context Engineering: From Prompts to Corporate Multi-Agent Architecture](https://arxiv.org/pdf/2603.09619v2)
24. [GEPA in depth — DSPy](https://dspy.ai/diving-deeper/gepa-in-depth/)
25. [Showcase — GEPA](https://gepa-ai.github.io/gepa/guides/use-cases/)
26. [Frequently Asked Questions — GEPA](https://gepa-ai.github.io/gepa/guides/faq/)
27. [Advanced Prompt Engineering Techniques Every Developer Should Know in 2026](https://baeseokjae.github.io/posts/prompt-engineering-techniques-2026/)
28. [Optimizing LLM Prompt Engineering with DSPy-Based Declarative Learning](https://arxiv.org/pdf/2604.04869)
29. [Production Prompt Engineering in 2026: Structured Outputs, Prompt Chaining, and DSPy Optimization](https://aiworkflowlab.dev/article/production-prompt-engineering-2026-structured-outputs-prompt-chaining-dspy)
30. [DSPy 3.0 in Python: Programming (Not Prompting) LLMs in 2026](https://pythondatabench.com/article/dspy-3-python-programming-llms-2026)