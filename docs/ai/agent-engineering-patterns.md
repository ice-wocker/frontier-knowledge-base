# Agent 工程实践（Agent Engineering Patterns）

> 最后更新：2026-09-26 ｜ 领域：AI·提示、Agent 与应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

Agent 工程（Agent Engineering）指把大语言模型（LLM）从单轮文本补全扩展为能自主规划、调用工具、维护状态并多步完成任务的系统的实践体系。2026 年的业界共识是：决定 Agent 成败的往往不是更大的模型，而是如何拆分工作、如何管理上下文与记忆、如何评估与观测（[5 Key Concepts Behind Agentic AI Every Engineer Must Understand](https://www.kdnuggets.com/5-key-concepts-behind-agentic-ai-every-engineer-must-understand)）。一个标准做法是把工作拆给多个各有聚焦上下文的 Agent，并由一个编排者（orchestrator）统一协调，而非让单个 Agent 试图把一切塞进脑海（同上）。

## 最新进展（2025–2026）

2025–2026 年，Agent 架构讨论从"哪种框架"转向"哪种模式适配哪类任务"。2026 年的综述把主流架构归纳为八种模式：ReAct、Plan-and-Execute、反思式（Reflective）、多 Agent、记忆增强、RAG、自主循环等，并逐一给出强项、局限与适用场景（[The 8 AI Agent Architectures That Matter in 2026](https://www.nexusai-tech.com/ai-insights/8-ai-agent-architectures-2026-react-plan-execute-multi-agent-memory-rag-autonomous-loops)）。

记忆层在这一时期快速标准化。Letta（MemGPT 研究项目的生产化版本）提出三层记忆架构并推出基于 git 的 Context Repositories，用于编码 Agent 的程序化上下文管理与版本化（[Letta Research](https://www.letta.com/research/)）；Mem0 采用带时间戳的版本化记忆与 LLM 驱动的冲突消解，报告在 LoCoMo 上较 OpenAI Memory 提升约 26%（[Graph-Native Cognitive Memory for AI Agents](https://arxiv.org/html/2603.17244v1)）。

生产级 Agent 的内存设计也在工程化。2026 年有实践文章把长期记忆抽象为"五阶段流水线 + 四种设计模式"，其中 Checkpoint Memory（崩溃恢复）模式在每次关键动作后写入检查点，并区分三层存储——原始事件的 operational log、当前任务的 state、经整理的长期 lessons；该模式适合批处理、CI/CD 与无人值守自动化，并需要写入密集、低延迟的存储（如 Redis AOF、DynamoDB）（[Designing Persistent Memory for Production AI Agents: A Five-Stage Pipeline and Four Design Patterns](https://www.besthub.dev/articles/designing-persistent-memory-for-production-ai-agents-a-five-stage-pipeline-and-four-design-patterns-7663b00f231e)）。另有 Loop Engineering 指南把 Agent 记忆分为有限短期记忆（LLM 上下文窗口）与可扩展长期记忆（向量库、知识库、传统数据库），并由 Agent Orchestrator 持久化目标、计划与进度以支持恢复（[Agent Memory, State Management, and Persistent Data Storage](https://guidesfor.dev/loop-engineering-2026/agent-memory-state-management-persistent-data-storage/)）。

## 核心技术与关键概念

**ReAct**：以紧凑的"思考—工具—观察"循环逐步推进，下一步动作取决于上一次观察结果。适合路径未知、需要边跑边调工具（API、搜索、抓取）的任务；优点是可追溯、迭代快，但长程任务上要注意 token 漂移与成本膨胀（[The 8 AI Agent Architectures That Matter in 2026](https://www.nexusai-tech.com/ai-insights/8-ai-agent-architectures-2026-react-plan-execute-multi-agent-memory-rag-autonomous-loops)；[AI Agent Workflow Patterns (2026)](https://easygoingnerd.com/blog/ai-agent-workflow-patterns-2026/)）。

**Plan-and-Execute**：先显式分解出计划，再由独立循环逐步执行，必要时根据环境变化修订。适合流程确定、工具调用昂贵、分支因子大的任务；计划降低冗余探索、便于监控（可对比实际执行与计划），但上游数据中途变化会让计划过期，显得脆弱（[AI Agent Architecture 2026](https://dev.to/monuminu/ai-agent-architecture-2026-building-production-grade-systems-patterns-benchmarks-and-lessons-5d34)；[When to Choose ReAct vs Plan-and-Execute vs Multi-Agent](https://aiagents.codeguides.io/agent-architectures/when-to-choose-react-vs-plan-and-execute-vs-multi-agent/)）。在二 Agent 形态中，这被描述为 ReAct 的经典泛化："规划者—执行者"结构适合规划者用更强模型、执行者用更便宜模型的情形（[Multi-Agent AI Systems in 2026: Frameworks, Patterns, and Production Observability](https://futureagi.com/blog/multi-agent-systems-2025/)）。

**Reflexion / 反思式**：在生成后加入自我批判与修订环节，改进后续尝试（[AI Agent Workflow Patterns (2026)](https://easygoingnerd.com/blog/ai-agent-workflow-patterns-2026/)）。

**多 Agent 编排**：编排者 + 专家子 Agent。适合大而可切分的目标，能力最强也最昂贵；当存在真实角色边界（不同技能、模型或权限层级）时价值最大（[When to Choose ReAct vs Plan-and-Execute vs Multi-Agent](https://aiagents.codeguides.io/agent-architectures/when-to-choose-react-vs-plan-and-execute-vs-multi-agent/)）。业界常见的混合方式是"外层用计划、内层用 ReAct"，以兼顾可审计性与灵活性（同上）。2026 年的生产指南把多 Agent 编排归纳为五种核心模式——orchestrator/worker（编排者/工人）、pipeline（流水线）、fan-out/fan-in（扇出/扇入）、peer debate（对等辩论）、specialist routing（专家路由）（[Multi-Agent Orchestration Patterns: A Production Guide (2026)](https://www.explainx.ai/blog/multi-agent-orchestration-patterns-guide-2026)）。另有资料区分 Supervisor（协调者 + 专家）与 Hierarchical Supervisor（监督者只决定下一个该由哪个工人行动、自身不执行，常见于 CrewAI 的 hierarchical 流程与 OpenAI Agents SDK 的 handoffs）以及 Maker-Checker（一方产出、另一方打分或核验）（[Multi-Agent AI Systems in 2026](https://futureagi.com/blog/multi-agent-systems-2025/)）。工程上常建议让单个 Agent 拥有决策权与状态，工人近乎无状态、只处理单一任务，并把外部调用统一路由经过决策 Agent、按任务记录可关联的 trace（[Multi-Agent Orchestration in Production: The Patterns That Survive When the Demo Ends](https://www.future-of-software.com/multi-agent-orchestration-in-production-the-patterns-that-survive-when-the-demo-ends)）。

**记忆与状态**：Letta 的三层记忆借鉴计算机体系结构——最内层 Core Memory 常驻上下文（类比 RAM），保存用户名、偏好、当前任务状态；中层 Recall Memory 是过往对话的可检索归档；最外层 Archival Memory 是向量索引化的长期存储，通过 LLM 函数调用完成分页，让 Agent 自主决定记什么、忘什么（[MemGPT to Memory Standards](https://selina.ai/blog/memgpt-to-memory-standards-how-agent-operating-systems-became-the-default-architecture-for-ai-memory-in-2026)；[AI Agent Memory Architectures](https://zylos.ai/research/2026-04-05-ai-agent-memory-architectures-persistent-knowledge/)）。Mem0 把记忆抽取为事实存入向量库；Zep 构建于时序知识图谱（Graphiti）之上，跟踪事实随时间的变化（[Mem0 vs Letta vs Zep (2026)](https://aiworkflowlab.dev/article/agent-memory-mem0-vs-letta-vs-zep-2026)）。工程上，长期记忆常被拆为"向量化 + 语义分块 + 事实抽取"三环节：先做语义检索，再按保留自然边界的语义分块（通常优于固定长度切分），而后把关键事实与偏好抽取为结构化形式以支持精确匹配与范围查询（[Build AI agents with short-term & long-term memory in Redis](https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/)）。另有资料归纳出五种通用记忆模式——Buffer Memory（全量历史）、Sliding Window（最近 N 条）、Summary Memory（压缩摘要）、Vector Memory（语义检索）、Hybrid Memory（组合方案），复杂度递增（[AI Agent Memory Patterns: Building Stateful AI Applications with Long-Term Memory in 2026](https://crazyrouter.com/en/blog/ai-agent-memory-patterns-stateful-applications-guide-2026)）。跨会话持久化还有一种低成本做法是外部文件记忆：会话开始前读取一个或多个文件注入系统提示，会话结束或学到重要信息时写回文件，即所谓的 CLAUDE.md 模式（[AI Agent Memory Across Sessions (Agents 101, Part 3)](https://www.aibuilderclub.com/blog/ai-agents-101-part-3)）。

**工具设计**：工具 schema、错误返回与幂等性是可靠性的关键；Anthropic 的做法是让文件系统成为上下文的一部分，大文件由模型用 `grep`、`tail` 等命令按需加载（[Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)）。Anthropic 还指出最常见的失败模式之一是臃肿的工具集覆盖过多功能，导致"该用哪个工具"的决策点含糊；若人类工程师都无法确定某场景该用哪个工具，就不能指望 AI Agent 做得更好（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。一份工具定义规范建议包含清晰工具名（避免泛化命名如 `process_data`）、若干句说明"何时使用"而非仅"做什么"的描述、类型化输入 schema 与记录错误状态的输出 schema（[Tools for AI Agents — MLflow](https://www.mlflow.org/articles/tags/tools-for-ai-agents/)）。面向 Agent 的工具设计原则还包括：每个工具单一自然语言意图、用枚举替代自由文本字段、尽可能给出默认值、预校验参数以强制安全执行、内置失败指引告知模型下一步、明确记录副作用，并动态加载工具以避免上下文膨胀（[What Is AI Agent Tool Calling? MCP, Function Calling, and A2A Explained (2026)](https://dev.to/arcade/ai-agent-tool-calling-mcp-a2a-23l6)）。Anthropic 引入 programmatic tool calling（编程式工具调用），允许在代码中编排工具调用；OpenAI 的实践指南则建议对每个工具按只读/写、可逆性、所需账户权限与财务影响等维度打风险等级（低/中/高），并配 PII 过滤器与内容审核（[Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)；[A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)）。

**评估与可观测**：Agent 可观测指把每一步（LLM 调用、工具调用、检索、控制流决策）作为结构化 trace 捕获，因为失败通常藏在中间步骤而非最终答案里（[AI Agent Observability, Tracing & Evaluation with Langfuse](https://langfuse.com/blog/2024-07-ai-agent-observability-with-langfuse)）。Langfuse 把 tracing、监控、数据集、实验与评估连成一个闭环（[Langfuse](https://langfuse.com/)）；LangSmith 则覆盖 tracing、生产评估与管理部署全生命周期，并支持 OpenTelemetry 摄入与标注队列（Annotation Queues）把专家反馈沉淀为评测数据集（[LangSmith vs. Langfuse](https://www.langchain.com/articles/langsmith-vs-langfuse)；[LLM Observability Tools](https://www.langchain.com/articles/llm-observability-tools)）。

## 关键数据与评测结果

- **τ-bench 的 pass^k**：其核心创新是"Agent 在 k 次尝试中至少成功一次"的概率；在真实部署中可重试，因此比 Pass@1 更贴近实际可靠性。该指标会随 k 增大而下降（而非上升），τ-bench 原始论文发现 GPT-4o 在零售场景 pass^1 低于 50%、pass^8 低于 25%（[Tau-Bench: Customer-Service Agents Under Realistic Policy](https://benchmarkingagents.com/tau-bench/)；[Exploiting AI Agent Benchmarks](https://baeseokjae.github.io/posts/exploiting-ai-agent-benchmarks-2026/)）。τ-bench 官方定位为衡量 Agent 在文本与语音下与用户对话、调用工具、检索知识并遵循策略的能力，覆盖企业域，并已审计并修复 airline 与 retail 域中 50+ 个任务（修正期望动作、消歧等）；官方还推出 τ²-bench（考察编码 Agent 能否构建 τ-bench 所要评估的客服 Agent）及对应排行榜（[τ-bench](http://taubench.com/)）。
- **GAIA 与可靠性**：GAIA 分三个难度级别（Level 1 简单查找、Level 2 多步推理、Level 3 复杂多工具协同），验证集含 165 个任务；研究显示结果一致性通常随任务变难单调变化，而资源一致性（action cost 的可预测性）在复杂任务上普遍退化（[Towards a Science of AI Agent Reliability](https://arxiv.org/html/2602.16666)）。另有材料称截至 2026 年中期，GAIA 验证集领先系统总分已超过 92%，作者发布了面向动态/异步行为的 GAIA2（[GAIA Benchmark](https://aiwiki.ai/wiki/gaia_benchmark/raw)）。
- **多语言与终端 Agent 的新基准**：OmnilingualGAIA2 是 GAIA2 的机器翻译扩展（含部分人工专家校验），覆盖 5 种书写系统的 10 种目标语言并配本地化人工校准的多语言 verifier；评估七个前沿与开源权重 Agent 发现普遍存在 8.8–18.4 个 pass@3 百分点的跨语言差距（[OmnilingualGAIA2: Evaluating the Multilingual Gap in Frontier AI Agents](https://arxiv.org/html/2608.08775v2)）。TUA-Bench 面向通用终端使用 Agent，任务手工设计、在真实终端运行并由执行式评分协议评估；报告最强的前沿 Agent 即 Claude Code 配合 Claude Opus 4.8（max reasoning effort）取得 65.8% 总体成绩，两个赛道间仍有较大差距（[TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents](https://arxiv.org/html/2606.28480v1)）。
- **基准选择的分歧**：SWE-bench 评判可验证产物（代码补丁），GAIA 评判链式工具使用与浏览的精确答案，τ-bench 评判多轮对话中的策略遵循；多数排行榜用单次 pass@1 掩盖了可靠性问题，pass^k 是暴露该问题的关键锚点（[SWE-bench vs τ-bench vs GAIA](https://dreaming.press/posts/swe-bench-vs-tau-bench-vs-gaia.html)）。
- **评估维度示例**：一份 Agent 评估口径给出加权维度——上下文保持（20%，记住先前轮次、消解指代）、完整性（15%）、效率（10%，不做多余工具调用或冗余澄清）、个性（5%，语气简洁、避免谄媚）、错误恢复（5%，优雅处理缺失文件、空结果、歧义查询）（[Agent Eval Benchmark](https://amd-gaia.ai/docs/eval)）。

## 失败模式与工程建议

常见失败模式包括：长程任务中上下文漂移与 token 成本失控（ReAct）、计划中途过期（Plan-and-Execute）、多 Agent 通信开销与责任边界模糊、记忆写入噪声与冲突（如"囤积者"式从不遗忘）、以及工具调用不可重试导致的非幂等副作用（[Designing Persistent Memory for Production AI Agents](https://www.besthub.dev/articles/designing-persistent-memory-for-production-ai-agents-a-five-stage-pipeline-and-four-design-patterns-7663b00f231e)）。工程上普遍建议"从最简单的可行方案开始"，先用最小提示与最强模型测试，再针对失败模式补充指令并跟踪上下文使用与成功率等指标（[A Guide for Effective Context Engineering for AI Agents](https://www.marktechpost.com/2025/10/20/a-guide-for-effective-context-engineering-for-ai-agents/)）。评估上则建议不要只看单次通过率，而要用 pass^k 等一致性指标衡量可靠性（[Tau-Bench](https://benchmarkingagents.com/tau-bench/)）。对多 Agent 系统，还要注意流水线模式的通病：任一步骤失败会使整条流水线停止，因而重试与超时逻辑应建在流水线层而非单个节点内部（[Multi-Agent AI Systems: When One Agent Isn't Enough](https://www.kalviumlabs.ai/blog/multi-agent-ai-systems-when-one-agent-isnt-enough/)）。

## 趋势与争议

一是**"多 Agent"是否被过度使用**：支持者认为编排者 + 子 Agent 是解决上下文过载的标准方案（[5 Key Concepts](https://www.kdnuggets.com/5-key-concepts-behind-agentic-ai-every-engineer-must-understand)），批评者则指出它在成本与可靠性上代价高昂，仅在存在真实角色边界时才划算（[When to Choose ReAct vs Plan-and-Execute vs Multi-Agent](https://aiagents.codeguides.io/agent-architectures/when-to-choose-react-vs-plan-and-execute-vs-multi-agent/)）。二是**记忆架构尚无标准**：Mem0 的"事实 + 向量库"、Letta 的显式记忆块、Zep 的时序知识图谱路线并存，召回精度、延迟与运维成本各有取舍；外部文件记忆（CLAUDE.md 模式）则以极低复杂度作为起点（[Mem0 vs Letta vs Zep (2026)](https://aiworkflowlab.dev/article/agent-memory-mem0-vs-letta-vs-zep-2026)；[AI Agent Memory Across Sessions](https://www.aibuilderclub.com/blog/ai-agents-101-part-3)）。三是**评估可信度危机**：有观点认为 2026 年出现"Agent 评测信任危机"，基准被利用、单次指标失真，需要更诚实的可靠性报告方式（[Exploiting AI Agent Benchmarks](https://baeseokjae.github.io/posts/exploiting-ai-agent-benchmarks-2026/)）。四是**自改进多 Agent 的成熟度存疑**：让 Agent 观察自身输出、更新自身提示并自我改进的模式在 2026 年仍属研究级，生产使用有限、规模化可靠性尚未被证明（[Multi-Agent Systems 2026: Orchestration, Memory, Tooling, Reliability](https://ailearningguides.com/multi-agent-systems-2026/)）。

## 参考来源

1. [The 8 AI Agent Architectures That Matter in 2026](https://www.nexusai-tech.com/ai-insights/8-ai-agent-architectures-2026-react-plan-execute-multi-agent-memory-rag-autonomous-loops)
2. [AI Agent Workflow Patterns (2026): ReAct to Multi-Agent](https://easygoingnerd.com/blog/ai-agent-workflow-patterns-2026/)
3. [AI Agent Architecture 2026: Building Production-Grade Systems](https://dev.to/monuminu/ai-agent-architecture-2026-building-production-grade-systems-patterns-benchmarks-and-lessons-5d34)
4. [When to Choose ReAct vs Plan-and-Execute vs Multi-Agent](https://aiagents.codeguides.io/agent-architectures/when-to-choose-react-vs-plan-and-execute-vs-multi-agent/)
5. [5 Key Concepts Behind Agentic AI Every Engineer Must Understand](https://www.kdnuggets.com/5-key-concepts-behind-agentic-ai-every-engineer-must-understand)
6. [Letta Research](https://www.letta.com/research/)
7. [MemGPT to Memory Standards](https://selina.ai/blog/memgpt-to-memory-standards-how-agent-operating-systems-became-the-default-architecture-for-ai-memory-in-2026)
8. [AI Agent Memory Architectures: From Context Windows to Persistent Knowledge](https://zylos.ai/research/2026-04-05-ai-agent-memory-architectures-persistent-knowledge/)
9. [Graph-Native Cognitive Memory for AI Agents](https://arxiv.org/html/2603.17244v1)
10. [Mem0 vs Letta vs Zep: Agent Memory for Production AI Agents (2026)](https://aiworkflowlab.dev/article/agent-memory-mem0-vs-letta-vs-zep-2026)
11. [Building agents with the Claude Agent SDK — Anthropic](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
12. [A Guide for Effective Context Engineering for AI Agents — MarkTechPost](https://www.marktechpost.com/2025/10/20/a-guide-for-effective-context-engineering-for-ai-agents/)
13. [AI Agent Observability, Tracing & Evaluation with Langfuse](https://langfuse.com/blog/2024-07-ai-agent-observability-with-langfuse)
14. [Langfuse](https://langfuse.com/)
15. [LangSmith vs. Langfuse](https://www.langchain.com/articles/langsmith-vs-langfuse)
16. [LLM Observability Tools to Monitor & Eval Agents](https://www.langchain.com/articles/llm-observability-tools)
17. [Towards a Science of AI Agent Reliability](https://arxiv.org/html/2602.16666)
18. [Exploiting AI Agent Benchmarks: The 2026 Crisis of Trust in Agent Evaluation](https://baeseokjae.github.io/posts/exploiting-ai-agent-benchmarks-2026/)
19. [Tau-Bench: Customer-Service Agents Under Realistic Policy](https://benchmarkingagents.com/tau-bench/)
20. [τ-bench 官方网站](http://taubench.com/)
21. [GAIA Benchmark — AI Wiki](https://aiwiki.ai/wiki/gaia_benchmark/raw)
22. [SWE-bench vs τ-bench vs GAIA: Which Agent Benchmark Actually Predicts Production](https://dreaming.press/posts/swe-bench-vs-tau-bench-vs-gaia.html)
23. [Designing Persistent Memory for Production AI Agents: A Five-Stage Pipeline and Four Design Patterns](https://www.besthub.dev/articles/designing-persistent-memory-for-production-ai-agents-a-five-stage-pipeline-and-four-design-patterns-7663b00f231e)
24. [Agent Memory, State Management, and Persistent Data Storage](https://guidesfor.dev/loop-engineering-2026/agent-memory-state-management-persistent-data-storage/)
25. [Build AI agents with short-term & long-term memory in Redis](https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/)
26. [AI Agent Memory Patterns: Building Stateful AI Applications with Long-Term Memory in 2026](https://crazyrouter.com/en/blog/ai-agent-memory-patterns-stateful-applications-guide-2026)
27. [AI Agent Memory Across Sessions (Agents 101, Part 3)](https://www.aibuilderclub.com/blog/ai-agents-101-part-3)
28. [Multi-Agent Orchestration Patterns: A Production Guide (2026)](https://www.explainx.ai/blog/multi-agent-orchestration-patterns-guide-2026)
29. [Multi-Agent AI Systems in 2026: Frameworks, Patterns, and Production Observability](https://futureagi.com/blog/multi-agent-systems-2025/)
30. [Multi-Agent Orchestration in Production: The Patterns That Survive When the Demo Ends](https://www.future-of-software.com/multi-agent-orchestration-in-production-the-patterns-that-survive-when-the-demo-ends)
31. [Multi-Agent AI Systems: When One Agent Isn't Enough](https://www.kalviumlabs.ai/blog/multi-agent-ai-systems-when-one-agent-isnt-enough/)
32. [Multi-Agent Systems 2026: Orchestration, Memory, Tooling, Reliability](https://ailearningguides.com/multi-agent-systems-2026/)
33. [Tools for AI Agents — MLflow](https://www.mlflow.org/articles/tags/tools-for-ai-agents/)
34. [What Is AI Agent Tool Calling? MCP, Function Calling, and A2A Explained (2026)](https://dev.to/arcade/ai-agent-tool-calling-mcp-a2a-23l6)
35. [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)
36. [A practical guide to building agents — OpenAI](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
37. [Agent Eval Benchmark](https://amd-gaia.ai/docs/eval)
38. [OmnilingualGAIA2: Evaluating the Multilingual Gap in Frontier AI Agents](https://arxiv.org/html/2608.08775v2)
39. [TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents](https://arxiv.org/html/2606.28480v1)
40. [Effective context engineering for AI agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)