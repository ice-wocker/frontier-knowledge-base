# Agent 框架与工具链

> 最后更新：2026-09-26 ｜ 领域：AI·平台、工具与落地 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

Agent 框架与工具链指构建 LLM 智能体（agent）所需的软件分层：编排框架（LangGraph、CrewAI、AutoGen、OpenAI Agents SDK 等）、上下文与文档框架（LlamaIndex）、工具与上下文连接协议（Model Context Protocol, MCP），以及记忆、沙箱、可观测等基础设施。2025–2026 年，这一领域从「各家框架百花齐放」走向分层收敛：编排层出现少数主流选项，而连接层由 MCP 统一，客户端与工具之间的互操作性显著提升。

## 最新进展（2025–2026）

**MCP 成为事实标准并被基金会化。** Anthropic 将 Model Context Protocol（MCP）捐出并参与设立 Agentic AI Foundation，MCP 成为新基金会的创始项目。据其官方公告，MCP 已拥有超过 9,700 万次月度 SDK 下载、10,000 个以上活跃公共服务器，并获 ChatGPT、Claude、Cursor、Gemini、Microsoft Copilot、Visual Studio Code 等主流产品一等公民支持；基础设施侧则有 AWS、Cloudflare、Google Cloud、Microsoft Azure 提供部署支持（[Donating the Model Context Protocol and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)、[Announcement](http://blog.modelcontextprotocol.io/tags/announcement/)）。协议自身也在快速迭代：2026-07-28 规范被称为 MCP 自远程 MCP 发布以来最重要的一次修订，核心变化是"无状态协议核心"——MCP 从双向有状态协议转为请求/响应式无状态协议，每个请求自带协议版本、客户端身份与能力（携带于 `_meta`），可落在任意一台处于轮询负载均衡后的实例上；旧的 `initialize`/`initialized` 握手与 `Mcp-Session-Id` 头被退役（[The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)）。该版本还引入多项改动：Multi Round-Trip Requests（MRTR，以 `resultType: "input_required"` 支持工具调用中途向用户索取确认或缺失参数）、基于 HTTP 头的路由（`Mcp-Method`、`Mcp-Name`，便于网关/WAF 路由与限流）、可缓存的列表结果（`ttlMs`、`cacheScope`）、授权加固（RFC 9207 issuer 校验、从 Dynamic Client Registration 转向 Client ID Metadata Documents）、正式扩展框架（MCP Apps、Tasks、Enterprise Managed Authorization）以及带十二个月最短窗口的正式弃用政策；Tasks 从实验性核心移入 `io.modelcontextprotocol/tasks` 扩展，改用轮询式 `tasks/get` 与新 `tasks/update`（同上）。此前 2025 年 11 月规范已引入 Tasks 原语、OAuth 2.1 授权与 MCP Registry，并配套 TypeScript SDK v1.27、Python SDK v1.26（[Model Context Protocol Details](https://www.metavert.io/model-context-protocol-vs-mcp)）。第三方统计显示公共 MCP 服务器数量从 2025 年一季度的约 1,200 个增长到 2026 年 4 月的 9,400+ 个（[MCP Servers in 2026: Complete Model Context Protocol Guide](https://dev.to/nishilbhave/mcp-servers-in-2026-complete-model-context-protocol-guide-52le)）。该版本获得广泛生态支持：AWS 与 Anthropic 表示无状态核心已在 Amazon Bedrock AgentCore 可用，开发者可在标准可扩展基础设施上部署 MCP 服务器而无需管理会话或持久连接；Cloudflare 的 Agents SDK 自首日即支持该规范，并可在 Workers 中运行 MCP 服务器；Microsoft Foundry 以统一的 MCP 端点汇聚工具并集中治理、身份与可观测（[The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)）。

**编排框架形成分层格局。** 厂商维度上，LangGraph 来自 LangChain Inc.（MIT，Python + JS/TS），CrewAI 来自 crewAI Inc.（核心 MIT，另有企业版，仅 Python），OpenAI Agents SDK 来自 OpenAI（Apache 2.0 / MIT，Python + TypeScript），Microsoft Agent Framework 来自微软（MIT，.NET C# + Python），Claude Agent SDK 来自 Anthropic（代码 Apache 2.0 + Anthropic 商业条款，Python + TypeScript）（[AI Agent Framework Comparison (LangGraph/CrewAI/AutoGen)](https://blckalpaca.at/en/knowledge-base/ai-agents/ai-agent-frameworks-comparison)）。LangChain 官方的 2026 框架对比表把 LlamaIndex（Workflows，MIT）、Google ADK（Apache 2.0）、OpenAI Agents SDK（MIT）与部分开源的 Mastra 列为代表性选择，分别面向文档中心事件驱动的多 Agent 系统、GCP 原生团队、范围紧凑的助手与委派工作流、以及 TypeScript 团队（[The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)）。另有一份第三方评测给出"按用例最佳"清单：编排与状态图首选 LangGraph 1.0，最干净的多 Agent handoff 属 OpenAI Agents SDK，Anthropic 原生/编码/computer-use 场景属 Claude Agent SDK，快速角色化多 Agent 原型属 CrewAI 1.14，企业 .NET/Azure 栈属 Microsoft Agent Framework（[Best AI Agent Frameworks](https://aiwiki.ai/wiki/best_ai_agent_frameworks)）。

**LlamaIndex 从 RAG 框架转向 Agent 工作流。** 其官方定位已更新为「构建上下文感知 AI Agent 的开发者框架」，强调 memory、状态管理、human-in-the-loop、reflection 等可扩展构建块，以及 Python/TypeScript SDK 和「Day zero integrations」（[The developer-trusted framework for building context-aware AI agents](https://www.llamaindex.ai/llamaindex)）。Workflows 1.0 被定位为「面向 agentic 系统的轻量级框架」，支持类型化 Workflow State、Python 侧资源注入，以及通过 `llama-index-instrumentation` 接入 OpenTelemetry、Arize Phoenix 等可观测性后端（[Announcing Workflows 1.0](https://www.llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems)）。2026 年其又推出 LlamaAgents 开放预览，结合 LlamaParse 文档处理与 Agent Workflows，并用 CLI 工具 `llamactl` 生成模板与部署（[Announcing LlamaAgents Open Preview](https://www.llamaindex.ai/blog/llamaagents-build-serve-and-deploy-document-agents)）。

## 核心技术与关键概念

**编排范式**：以 LangGraph 为代表的状态化图编排，适合复杂有状态工作流；以 CrewAI 为代表的角色化「crew」多智能体模式，强调最快上手（约 20 行 Python 即可跑通原型）；以 OpenAI Agents SDK 为代表的多智能体工作流与委派（delegation）模式，并通过 LiteLLM 做到 provider-agnostic、支持 100+ 模型（[AI Agent Frameworks in Mid-2026](https://the-agent-report.com/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/)、[AI Agent Framework Comparison](https://blckalpaca.at/en/knowledge-base/ai-agents/ai-agent-frameworks-comparison)）。一份 2026 年的三方对比给出维度化差异：LangGraph 具备逐节点 checkpoint 的可持久化/可恢复能力、一等公民的 human-in-the-loop，并通过 LangChain 兼容任意模型；CrewAI 通过 Flows 支持恢复（粒度较粗），同样支持 human-in-the-loop；OpenAI Agents SDK 以 Sessions 承载记忆、无内置 checkpointing（[LangGraph vs CrewAI vs OpenAI Agents SDK: The 2026 Verdict](https://www.danilchenko.dev/posts/langgraph-vs-crewai/)）。多 Agent 系统层面，常见模式包括层级式 Supervisor（监督者只路由、自身不执行，常见于 CrewAI hierarchical 与 OpenAI Agents SDK handoffs）与 Maker-Checker（一方产出、另一方核验）（[Multi-Agent AI Systems in 2026](https://futureagi.com/blog/multi-agent-systems-2025/)）。

**工具连接协议（MCP）**：MCP 把「模型—工具—数据源」的接入从各家私有插件规范统一为开放协议，客户端与服务器解耦；配合 MCP Registry 做服务器发现，配合 OAuth 做授权，配合 Tasks 扩展支持长时任务（[The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)、[Model Context Protocol Details](https://www.metavert.io/model-context-protocol-vs-mcp)）。MCP Registry 是面向公开 MCP 服务器的开放目录与 API，用于提升可发现性与实现便利，已进入 preview 并可添加服务器（[Introducing the MCP Registry — Announcement](http://blog.modelcontextprotocol.io/tags/announcement/)）；官方注册表站点会列出各服务器的版本与更新时间（[Official MCP Registry](https://prod.registry.modelcontextprotocol.io/)）。SEP-2663（Tasks Extension）为最终（Final）状态的扩展轨道记录（[SEP-2663: Tasks Extension](https://modelcontextprotocol.io/seps/2663-tasks-extension)）。

**Agent SDK 的核心抽象**：OpenAI Agents SDK 以 Python 优先，强调 Agents as tools / Handoffs（在多 Agent 间协调与委派）、Guardrails（与执行并行做输入校验与安全检查、不过即快速失败，含 `inputGuardrails`/`outputGuardrails`）、Function tools（任意 Python 函数经自动 schema 生成与 Pydantic 校验变为工具）以及 MCP server 工具调用（[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)）。其 JS 版文档展示了 triage agent 通过 `handoffs: [bookingAgent, refundAgent]` 把请求转交专门 Agent 的写法（[Agents — OpenAI Agents SDK (JS)](https://openai.github.io/openai-agents-js/guides/agents/)）。

**记忆与状态**：LlamaIndex 把 memory、state management、human-in-the-loop、reflection 列为核心组件，LangGraph 则以图状态承载跨步骤记忆（[LlamaIndex](https://www.llamaindex.ai/llamaindex)、[LangChain resources](https://www.langchain.com/resources/ai-agent-frameworks)）。

**可观测与沙箱基建**：框架普遍通过 OpenTelemetry 打通 tracing；LlamaIndex Workflows 明确支持 OpenTelemetry 与 Arize Phoenix（[Workflows 1.0](https://www.llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems)）。LlamaAgents 提供本地应用服务器与云端部署（`llamactl`、LlamaCloud UI、headless API），构成部署型基建（[LlamaAgents Open Preview](https://www.llamaindex.ai/blog/llamaagents-build-serve-and-deploy-document-agents)）。

**TypeScript 侧**：LangChain 官方将 Mastra 列为面向 TypeScript 团队的生产级自定义 Agent 框架（部分开源），与 Vercel AI SDK 构成该语言生态的主要选择（[The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)、[Top AI Agent Frameworks in 2026](https://autogpt.net/top-ai-agent-frameworks/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **LangGraph（LangChain Inc.）**：状态化图编排，MIT，Python/JS（[https://www.langchain.com/resources/ai-agent-frameworks](https://www.langchain.com/resources/ai-agent-frameworks)）。
- **LangChain / LangSmith**：框架与可观测/评测平台（[https://www.langchain.com/](https://www.langchain.com/articles/llm-observability-tools)）。
- **CrewAI**：角色化多智能体，MIT 核心 + 企业版（[AI Agent Framework Comparison](https://blckalpaca.at/en/knowledge-base/ai-agents/ai-agent-frameworks-comparison)）。
- **AutoGen（微软）**：多智能体研究/原型框架（[Best AI Agent Frameworks in 2026](https://www.awesomeagents.ai/tools/best-ai-agent-frameworks-2026/)）。
- **Microsoft Agent Framework**：.NET C# + Python，MIT（[AI Agent Framework Comparison](https://blckalpaca.at/en/knowledge-base/ai-agents/ai-agent-frameworks-comparison)）。
- **OpenAI Agents SDK**：多智能体工作流 SDK，MIT（[The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)）。
- **Claude Agent SDK（Anthropic）**：Python/TypeScript（[AI Agent Framework Comparison](https://blckalpaca.at/en/knowledge-base/ai-agents/ai-agent-frameworks-comparison)）。
- **LlamaIndex / LlamaAgents**：文档中心 Agent 框架与工作流（[https://www.llamaindex.ai/llamaindex](https://www.llamaindex.ai/llamaindex)）。
- **Google ADK（Agent Development Kit）**：Apache 2.0，GCP 原生；支持自定义 Python 函数工具（FunctionTool）、内置工具（如 Google Search 的 AgentTool）、第三方工具（如 LangChain 的 LangchainTool）与 MCP 工具，可组合为多工具、含子 Agent 的结构（[The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)、[Build an AI Agent with Google ADK](https://codelabs.developers.google.com/build-ai-agent-google-adk)）。Google Cloud 的 Gemini Enterprise Agent Platform 亦以 ADK 作为开源开发/部署框架之一（[Build with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build)）。
- **MCP**：开放工具连接协议，Agentic AI Foundation 创始项目（[Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)）。

## 关键数据与评测结果（附来源）

- MCP：97M+ 月度 SDK 下载、10,000+ 活跃公共服务器（Anthropic 2026）（[Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)）。与此口径不同，2026-07-28 规范发布博客称 Tier 1 SDK 合计月下载接近 5 亿，其中 TypeScript 与 Python SDK 累计下载均突破 10 亿（[The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)）——两处数据口径与时间点不同，需分别看待。
- 公共 MCP 服务器：约 1,200（2025 Q1）→ 9,400+（2026 年 4 月）（第三方统计）（[MCP Servers in 2026](https://dev.to/nishilbhave/mcp-servers-in-2026-complete-model-context-protocol-guide-52le)）。
- OpenAI Agents SDK：v0.18、10.3M 下载，支持 100+ 模型（第三方统计）（[AI Agent Frameworks in Mid-2026](https://the-agent-report.com/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/)）。
- 社区热度（star 数）：AutoGen 约 57.4k、CrewAI 约 49.8k、LangGraph 约 30.3k、Agno 约 39k（第三方统计，不同来源数值不一）（[Best AI Agent Frameworks in 2026](https://www.awesomeagents.ai/tools/best-ai-agent-frameworks-2026/)、[AI Agent Frameworks in Mid-2026](https://the-agent-report.com/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/)）。
- MCP 迁移动因量化：一家托管数千 MCP 服务器的平台称其 mcp-use 的新 SDK v2 借助新的 client-server 拆分把包体积缩小约 83%，同时提速约 25%（[The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)，该数据为厂商自述）。

## 趋势与争议

**框架收敛与分层**：编排层竞争仍在（LangGraph、OpenAI Agents SDK、CrewAI、Microsoft Agent Framework、Claude Agent SDK、Google ADK、Mastra 等），而连接层由 MCP 统一，形成「多编排 + 单协议」的格局（[The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)）。

**框架选择的争议**：一派主张按语言与技术栈选择（TypeScript 看 Mastra vs Vercel AI SDK，Python 看 LangGraph vs OpenAI Agents SDK vs CrewAI，.NET 看 Microsoft Agent Framework）（[Top AI Agent Frameworks in 2026](https://autogpt.net/top-ai-agent-frameworks/)）；另一派担忧框架抽象过厚导致调试困难，倾向在 MCP 之上自建轻量编排。部分第三方统计将 AutoGen 标注为偏研究与原型（[Best AI Agent Frameworks in 2026](https://www.awesomeagents.ai/tools/best-ai-agent-frameworks-2026/)），此类定性来自第三方评测而非官方声明，需谨慎对待。

**协议演进风险**：MCP 2026-07-28 的大版本修订以破坏性变更为主（移除握手/会话、Tasks 迁为扩展、Roots/Sampling/Logging 及旧 HTTP+SSE 传输被弃用），官方承认这会带来迁移成本、尤其影响依赖 session identifier 的开发者，但通过正式弃用政策（十二个月窗口）与迁移说明降低风险（[The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)）。有分析认为，此举牺牲短期兼容换取可扩展性，是协议走向企业级基础设施的信号（同上）。

## 参考来源

- [Donating the Model Context Protocol and establishing the Agentic AI Foundation (Anthropic)](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [Announcement (Model Context Protocol Blog)](http://blog.modelcontextprotocol.io/tags/announcement/)
- [The 2026-07-28 Specification (Model Context Protocol Blog)](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [SEP-2663: Tasks Extension](https://modelcontextprotocol.io/seps/2663-tasks-extension)
- [Official MCP Registry](https://prod.registry.modelcontextprotocol.io/)
- [Model Context Protocol Details](https://www.metavert.io/model-context-protocol-vs-mcp)
- [MCP Servers in 2026: Complete Model Context Protocol Guide](https://dev.to/nishilbhave/mcp-servers-in-2026-complete-model-context-protocol-guide-52le)
- [AI Agent Framework Comparison (LangGraph/CrewAI/AutoGen)](https://blckalpaca.at/en/knowledge-base/ai-agents/ai-agent-frameworks-comparison)
- [AI Agent Frameworks in Mid-2026: The Complete Landscape](https://the-agent-report.com/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/)
- [The best AI agent frameworks in 2026 (LangChain)](https://www.langchain.com/resources/ai-agent-frameworks)
- [Best AI Agent Frameworks in 2026 - Dev Guide](https://www.awesomeagents.ai/tools/best-ai-agent-frameworks-2026/)
- [Best AI Agent Frameworks (AI Wiki)](https://aiwiki.ai/wiki/best_ai_agent_frameworks)
- [Top AI Agent Frameworks in 2026: 11 Frameworks Compared](https://autogpt.net/top-ai-agent-frameworks/)
- [LangGraph vs CrewAI vs OpenAI Agents SDK: The 2026 Verdict](https://www.danilchenko.dev/posts/langgraph-vs-crewai/)
- [Multi-Agent AI Systems in 2026: Frameworks, Patterns, and Production Observability](https://futureagi.com/blog/multi-agent-systems-2025/)
- [OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/)
- [Agents — OpenAI Agents SDK (JS)](https://openai.github.io/openai-agents-js/guides/agents/)
- [The developer-trusted framework for building context-aware AI agents (LlamaIndex)](https://www.llamaindex.ai/llamaindex)
- [Announcing Workflows 1.0: A Lightweight Framework for Agentic systems](https://www.llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems)
- [Announcing LlamaAgents Open Preview: Build, Serve & Deploy Document Agents](https://www.llamaindex.ai/blog/llamaagents-build-serve-and-deploy-document-agents)
- [Build an AI Agent with Google ADK](https://codelabs.developers.google.com/build-ai-agent-google-adk)
- [Build with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build)
- [LLM Observability Tools to Monitor & Eval Agents](https://www.langchain.com/articles/llm-observability-tools)