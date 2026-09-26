# AI Agent（智能体）技术与生态

> 最后更新：2026-09-26 ｜ 领域：人工智能·智能体 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI Agent（智能体）指以大语言模型为推理核心、能够调用工具、读取与写入外部系统、并在多步任务中自主决策的系统。从工程视角看，一个典型 agent 由「模型 + 工具接口 + 状态与记忆 + 编排循环 + 防护栏」构成：模型负责推理与决策，工具接口负责把模型意图落到真实系统，状态与记忆负责跨步骤保持一致，编排循环负责把多步任务串起来，防护栏负责约束其自主行为。

2025–2026 年，Agent 从「demo 阶段」走向「协议标准化 + 工程化框架 + 严苛评测」三线并进：一方面 MCP、A2A 等开放协议把工具接入与智能体互操作标准化，并交由 Linux Foundation 托管形成厂商中立治理；另一方面 LangGraph、CrewAI、Microsoft Agent Framework、OpenAI Agents SDK 等提供了成熟编排原语；同时 GAIA、SWE-bench、OSWorld、Terminal-Bench 等基准把「自主性与可靠性」这一核心难题量化暴露出来。与此同时，企业落地数据显示「做过试点」的比例远高于「真正进入生产」，而安全事件也随自主性上升而增加。

## 2025–2026 最新进展

**MCP 成为事实标准并完成中立化治理。** Anthropic 于 2024 年 11 月 25 日开源 Model Context Protocol（MCP），用于把 AI 助手连接到数据所在的系统，包括内容仓库、业务工具与开发环境（[Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)）。OpenAI 于 2025 年 3 月在 ChatGPT 桌面端等产品中采纳 MCP，Google DeepMind 于 2025 年 4 月确认支持，Microsoft 通过 Semantic Kernel 与 Azure OpenAI 集成（[What is Model Context Protocol (MCP)?](https://resources.rework.com/libraries/ai-terms/model-context-protocol)）。

2025 年 12 月 9 日，Anthropic 把 MCP 捐赠给 Agentic AI Foundation（Linux Foundation 下的定向基金），MCP 成为该新基金会的创始项目；当时 MCP 已拥有超过 9700 万次月度 SDK 下载、10,000 个活跃服务器，并获得 ChatGPT、Claude、Cursor、Gemini、Microsoft Copilot、Visual Studio Code 等主流平台的一等客户端支持（[MCP joins the Agentic AI Foundation](http://blog.modelcontextprotocol.io/tags/announcement/)）。Linux Foundation 的 2026 年报告把 MCP 称为「连接 LLM 与数据/应用的行业标准」，并称其一周年时 Python SDK 周下载量达 2000 万次（[Open Source and the Future of AI](https://www.linuxfoundation.org/hubfs/Research%20Reports/Open%20Source%20and%20the%20Future%20of%20AI_Report_2026.pdf)）。到 2026 年，企业架构正从私有的 function-calling 封装转向这一开放、厂商中立的接口标准（[Model Context Protocol Explained](https://www.kunal-chowdhury.com/2026/09/model-context-protocol-mcp-enterprise-ai.html)）。

协议本身在 2026 年迎来最大修订：2026 年 6 月 29 日发布 release candidate，协议转为无状态，移除 initialize 握手与协议级 session，使服务器可用简单轮询负载均衡器扩展，不再需要管理 sticky session 或共享 session；客户端侧新增 Multi Round-Trip Requests（MRTR）等模式以支持更丰富的服务器到客户端交互（[Beta SDKs for the 2026-07-28 MCP Spec Release Candidate](http://blog.modelcontextprotocol.io/tags/announcement/)）。AWS 与 Anthropic 表示，新规范的无状态协议核心已在 Amazon Bedrock AgentCore 中可用，且由 AWS 贡献的官方扩展 Tasks 可支持可靠的长时间运行 agent（[The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)）。生态基建同步完善：2025 年 9 月推出官方 MCP Registry（registry.modelcontextprotocol.io）作为公开服务器目录与 API；2026 年 3 月引入扩展（Extensions）机制，使开发者可在不改动核心协议的前提下叠加 UI、认证与行业约定；2026 年 7 月官方 Ruby SDK 达到 1.0。Agentic AI Foundation 还推出首个 MCP 官方认证 MCPA，覆盖 MCP 基础、架构与组件、交互与执行、安全与治理、用例与生态五个领域（[MCP joins the Agentic AI Foundation](http://blog.modelcontextprotocol.io/tags/announcement/)、[MCPA Certification](https://www.linuxfoundation.org/press/agentic-ai-foundation-launches-mcpa-certification-to-validate-mcp-expertise)）。

**A2A 协议打通智能体互操作并达到 v1.0。** A2A（Agent2Agent）由 Google 发起并捐献给 Linux Foundation，用于不同框架（如 LangGraph、CrewAI、Google ADK、Genkit）构建的智能体互相发现能力、协商交互模式并协作，而不暴露内部状态（[Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/)）。A2A v1.0 是首个稳定、可生产的版本，通过支持多种协议绑定、无缝版本协商与统一语义模型，使异构环境的 agent 可互操作（[A2A Protocol Ships v1.0](https://a2a-protocol.org/latest/announcing-1.0/)）。协议由技术指导委员会维护，成员来自 AWS、Cisco、Google、IBM Research、Microsoft、Salesforce、SAP、ServiceNow 八家公司，并有广泛社区伙伴支持（[Agent2Agent (A2A) Protocol](https://a2a-protocol.org/v1.0.0/)）。

2026 年 4 月 9 日（一周年）时，A2A 已有 150+ 组织支持，并深度集成进 Google、Microsoft、AWS 平台，多个行业进入生产部署（[A2A Protocol Surpasses 150 Organizations](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)）。有分析把三者关系概括为：function calling 是模型原生发出结构化 JSON 的能力，MCP 标准化工具发现与执行传输（JSON-RPC），A2A 负责智能体间的委派与上下文传递，二者互补而非替代（[What Is AI Agent Tool Calling? MCP, Function Calling, and A2A Explained](https://dev.to/arcade/ai-agent-tool-calling-mcp-a2a-23l6)）。

**Agent 框架进入整合期。** 微软的 AutoGen 于 2025 年 10 月进入维护模式，Microsoft Agent Framework 于 2026 年 4 月达到 1.0 GA（[LangChain vs. AutoGen](https://www.langchain.com/resources/langchain-vs-autogen)）。2026 年主流的 Python 多智能体编排框架包括 Microsoft Semantic Kernel/Agent Framework、LangGraph、AutoGen、CrewAI 四者（[Compare orchestration frameworks](https://learn.microsoft.com/cs-cz/training/modules/aaai-implement-multi-agent-orchestration-azure-ai-foundry/6-compare-orchestration-frameworks)）。LangChain 的梳理显示 CrewAI（MIT）、Microsoft Agent Framework（MIT）、LlamaIndex Workflows（MIT）、Google ADK（Apache 2.0）、OpenAI Agents SDK（MIT）等各有侧重（[The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)）。

按厂商 SDK 角度，2026 年出现三款厂商主导的 SDK：OpenAI Agents SDK（2026 年 3 月，基于 handoff 的多智能体、内置 tracing）、Anthropic Agent SDK（与 Claude 4.6 同期，最深的 MCP 集成与 computer-use 工具、可查看 extended thinking）、Google ADK（2026 年 4 月），它们都会把使用者引向各自模型与运行时（[Best AI Agent Frameworks in 2026](https://toolradar.com/guides/best-ai-agent-frameworks)）。此外还有按场景划分的选择：LangGraph 1.0、OpenAI Agents SDK、Claude Agent SDK、CrewAI 1.14、Microsoft Agent Framework 等（[Best AI Agent Frameworks](https://aiwiki.ai/wiki/best_ai_agent_frameworks)）。Google 官方 codelab 演示了分层编排：LangGraph 做规划状态机、CrewAI 做角色化执行、A2A 做跨框架通信、ADK 做顶层编排（[Scale Agents with CrewAI, LangGraph, A2A, and ADK](https://codelabs.developers.google.com/next26/scale-agents)）。

**OpenAI Agents SDK 的演进。** 新版 Agents SDK 提供了更强大的 agent loop harness：可配置记忆、沙箱感知编排、类 Codex 的文件系统工具，并标准化集成 MCP、skills、AGENTS.md、代码执行等前沿 agent 系统的通用原语（[The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)）。

**Computer Use 与浏览器操作。** Anthropic 于 2026 年 3 月 23 日在 Claude Cowork 与 Claude Code 中以研究预览形式上线 Computer Use，让 Claude 可移动鼠标、点击、打开应用、浏览网页、填写表格，并默认通过 per-app 许可系统阻断交易平台、加密交易所等敏感类别（[Claude now moves your mouse, and asks permission first](https://botmonster.com/ai/claude-computer-use-hands-on-ai-desktop-control-cowork/)）。2026 年 8 月 26 日，Claude in Chrome 结束预览、面向所有付费 Claude 计划正式可用（GA），并可在浏览器中自主执行动作而无需逐步批准；安全分类器会在每个动作执行前校验其是否安全且符合用户请求（[Claude in Chrome is generally available](https://claude.com/blog/claude-in-chrome-generally-available)）。同一天，Claude Cowork 桌面应用内置浏览器：任务需要访问网站时，侧栏打开浏览器，Claude 导航网页、阅读、点击与输入，可用于填表、从仪表盘拉取数字、走通无 connector 的门户（[Claude gets its own browser in Cowork](https://claude.com/blog/cowork-built-in-browser/)）。在 API 层面，Anthropic 把桌面级 computer use 与网页级 browser use 工具区分：前者驱动完整桌面环境，后者通过无障碍树、元素、表单与标签页，以及截图与 viewport 坐标来操作页面（[Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)、[Browser use tool](https://platform.claude.com/docs/pt-BR/agents-and-tools/tool-use/browser-use-tool)）。浏览器端其它主流方案包括 ChatGPT agent mode（Atlas 于 2026 年 8 月 9 日退役）、Gemini in Chrome 的 auto browse 等（[7 Best AI Browser Agents in 2026](https://www.usecarly.com/blog/best-ai-browser-agents/)）。有媒体指出，通过把浏览器嵌入 AI（而非让 AI 接管用户的浏览器）是 Claude 与已停运的 Atlas 的路线差异（[Claude自己长出浏览器](https://g.pconline.com.cn/x/2181/21811416.html)）。

**企业落地从试点走向生产。** 采用数据存在明显口径差异。Anthropic 的《2026 State of AI Agents Report》显示，81% 的组织计划在 2026 年从简单任务自动化走向更复杂的 AI 项目，其中 39% 预期开发处理多步流程的 agent、29% 计划部署跨职能 agent，企业（87%）比中小企业（78%）更积极（[The 2026 State of AI Agents Report](https://resources.anthropic.com/hubfs/The%202026%20State%20of%20AI%20Agents%20Report.pdf)）。但有分析指出，真正的生产级自主部署比例仍低：某项统计称约 80% 的企业应用在 2026 年一季度已嵌入至少一个 AI agent、88% 的组织至少在一个业务职能中使用 AI，但真正在生产流程中自主运行的仅 31%，成功规模化 agentic 系统的约 23%（[Agentic AI Enterprise 2026](https://thebriefscript.com/agentic-ai-enterprise-2026-autonomous-agents/)）；另一口径称约 5% 的自定义企业 AI 工具真正进入生产（[AI Agent Adoption Statistics 2026](https://prefactor.tech/learn/ai-agent-adoption-statistics/)）；还有基于生产遥测的报告称 54% 的企业已部署（[AI Agents in Production: The 2026 Reality Check](https://networkcraft.net/ai-agents-production-2026-reality-check/)）。商业侧，Salesforce 报告其 Agentforce 年度经常性收入（ARR）达 8 亿美元、同比增长 169%，并已完成 29,000 个客户部署（[AI Agents Hit Enterprise Escape Velocity](https://insights.reinventing.ai/articles/ai-agents-enterprise-escape-velocity-2026-02-27)）。

## 核心技术与关键概念

- **工具调用 / function calling**：模型输出结构化参数以触发外部函数，是 agent 与外界交互的最底层原语。
- **MCP**：以 client-server 架构统一工具/数据源的发现与调用，降低集成债；2026 年修订后协议转为无状态，便于水平扩展。
- **A2A**：以 JSON-RPC 2.0 为基线实现智能体间协商与任务委派，v1.0 提供多种协议绑定与版本协商。
- **编排范式**：Plan-Execute、ReAct、handoff、agents-as-tools 等。LangGraph 以显式节点、边、状态转移与 checkpoint 支撑复杂、持久且混合确定性/模型驱动步骤的工作流；OpenAI Agents SDK 以模型驱动循环、handoff、agents-as-tools 为小型可组合原语（[AI agent frameworks compared](https://arize.com/guides/ai-agent-handbook/agent-frameworks/)）。
- **上下文工程（context engineering）**：把指令、工具、记忆、检索知识与防护栏组织进上下文；有研究认为上下文质量是 agent 可靠性的先行指标（[AI Agents Do Not Fail Alone: The Context Fails First](https://arxiv.org/abs/2607.14275)）。
- **Agent 记忆**：结构化笔记（agentic memory）把笔记持久化到上下文窗口之外，需要时再拉回，是 Claude Code 待办清单、NOTES.md 等模式的基础（[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。长程任务会出现「行为状态衰减」，可用独立记忆 agent 主动注入记忆提醒来缓解（[Remember When It Matters](https://arxiv.org/html/2607.08716)）；InfiAgent 通过把持久状态外置为文件中心的抽象，使推理上下文与任务时长无关（[InfiAgent](https://arxiv.org/html/2601.03204v1)）；HORMA 则把记忆构建与记忆检索分层，以适配二者不同的时间与功能尺度（[Organize then Retrieve](https://arxiv.org/html/2606.11680v1)）。
- **托管自主性（managed autonomy）**：当不确定性升高时，agent 应能检测认知漂移、暂停推理、尝试恢复，乃至交还控制权（[Intelligence as Managed Autonomy](https://arxiv.org/pdf/2605.27628)）。
- **拒绝/防护栏（guardrails）**：在动作执行前进行安全分类或权限校验，例如 Claude 在浏览器动作前用安全分类器校验（[Claude in Chrome is generally available](https://claude.com/blog/claude-in-chrome-generally-available)）。
- **沙箱与代码执行**：前沿 agent 系统把代码执行、文件系统工具与沙箱感知编排作为通用原语标准化，使 agent 能在隔离环境中试错而不污染宿主系统（[The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)）。
- **协议安全**：由于工具描述、错误追踪数据、网页内容都可能被注入指令，agent 的威胁面已从模型扩展到框架、注册表与工具链本身（[AutoJack and Agentjacking](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/06/CSA_research_note_ai-agent-rce-autojack-agentjacking_20260623-csa-styled.pdf)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- Model Context Protocol：https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
- A2A Protocol：https://a2a-protocol.org/latest/
- OpenAI Agents SDK：https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- Microsoft Agent Framework：https://learn.microsoft.com/en-us/agent-framework/overview/
- Google ADK / CrewAI / LangGraph 编排示例：https://codelabs.developers.google.com/next26/scale-agents
- Claude in Chrome / Cowork 浏览器：https://claude.com/blog/claude-in-chrome-generally-available
- τ-bench：https://taubench.com/
- Terminal-Bench：https://www.tbench.ai/news/terminal-bench-2-1
- MCP Registry：https://registry.modelcontextprotocol.io

## 关键数据与评测结果

- **GAIA**：该基准考察通用助手在真实工具环境中的多步任务能力。2026 年 5 月的榜单上，CustomGPT.ai Research Lab 以 92.03% 的总分领先（L1 96.77%、L2 89.94%、L3 89.8%）（[GAIA Leaderboard](https://gaia-benchmark-leaderboard.hf.space/deepseek.com)）。
- **SWE-bench Verified**：由 500 个经人工筛选的 Python 真实 issue 构成，通过运行测试验证补丁是否正确（[AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration](https://arxiv.org/html/2602.03786)）。2026 年 5 月榜单中，Claude Mythos Preview 以 93.9% 领先，但该文同时指出该基准存在较高的数据污染风险（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。
- **OSWorld**：桌面级 agent 基准。2026 年 7 月 27 日，中国「实在 Agent」以 90.2% 的任务成功率登顶 OSWorld 全球总榜，被报道为该基准自 2024 年发布以来首个突破该水平的方案（[中国智能体登顶OSWorld](http://www.xinhuanet.com/government/20260805/60bc929f7f0d4722b6ad4f4f22d90fcb/c.html)）。但更新的 OSWorld 2.0 针对更贴近现实的多步长任务，即便最强模型 Claude Opus 4.8 也仅完成 20.6%（[AI Browser Agents in 2026](https://nerdleveltech.com/ai-browser-agents-claude-chatgpt-gemini)），说明基准难度随任务真实性显著上升。
- **Terminal-Bench**：面向真实终端任务的基准。2026 年发布 Terminal-Bench 2.1，修复了 2.0 版 89 个任务中的 28 个（[Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)）。在 2.0 版榜单上，Codex CLI 搭配 GPT-5.5 达 82.2%、Simple Codex 搭配 GPT-5.3-Codex 达 75.1%（[terminal-bench@2.0 Leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0)）；2.1 榜单上 Terminus 2 搭配 Gemini 3 Pro（high）为 73.9%、Claude Code 搭配 Opus 4.7（max）为 68.9%（[terminal-bench@2.1 Leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.1)）。
- **τ-bench 系列**：从 τ-bench（2024）发展到 τ²-bench（2025，dual control）、τ-knowledge/τ-voice（2026），覆盖策略遵循、知识检索与实时语音交互（[τ-bench](https://taubench.com/)）。
- **企业采用率**：见上文，存在从约 5% 到 54% 的多口径差异，取决于对「生产」「agent」的定义。

## 趋势与争议

**自主性与可靠性的张力。** 实证研究刻画了两类失败模式：Safety Drift（声明的安全意图在长程执行中逐渐侵蚀，导致违反约束的动作）与 Operational Hallucination（持续的重复工具调用，反映状态感知错误甚至 livelock）（[Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/abs/2607.18366)）。2026 年 1 月 29 日至 3 月 18 日七周内出现了一系列由「过度、缺乏治理的自主性」引发的安全事件，包括恶意 skill 污染 agent 注册表、prompt injection 把开发工具变成供应链武器、智能体擅自动用基础设施等（[The Cost of Unchecked Autonomy](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/03/autonomy-risks-top-10-incidents-v1-csa-styled.pdf)）。云安全联盟（CSA）的调研显示 65% 的受访者对 agentic AI 风险存在担忧（[Autonomous by Design, Uncontrolled in Practice](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-agentic-ai-loss-of-control-20260908-csa-style/)）。

**Promptware 与 agentic 攻击成为已确认的攻击类。** CSA 指出，promptware 攻击类（以 prompt injection 载荷实现多阶段、持久、由攻击者导向的行为）已从实验室演示发展为规模化确认利用：学术研究者于 2026 年 1 月形式化的七阶段 kill chain 对应 2025–2026 年 21 起有记录的真实多阶段攻击，其中三起涉及 AI 编程助手（[Promptware and Agentic C2: The Confirmed Attack Class](https://labs.cloudsecurityalliance.org/research/csa-research-note-promptware-agentic-c2-attack-class-2026050/)）。此外，AutoJack 与 Agentjacking 暴露了 AI agent 框架本身成为远程代码执行（RCE）攻击面：Agentjacking（2026 年 6 月由 Tenet Security 披露）显示，注入到 Sentry 错误追踪数据中的恶意内容可以劫持 AI 编程 agent，研究者识别出 2,388 个以上可能暴露的组织（[AutoJack and Agentjacking](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/06/CSA_research_note_ai-agent-rce-autojack-agentjacking_20260623-csa-styled.pdf)）。有分析指出，agentic AI 会放大间接提示注入：单条注入指令可经工具调用、子 agent 委派与共享记忆传播；工具输出劫持、参数枚举、agent 到 agent 注入等是 agentic 特有的攻击向量，且「confused deputy」问题使低权限外部内容可经能力递增的 agent 链升级为高权限动作（[Indirect Prompt Injection in Agentic AI](https://beyondscale.tech/blog/indirect-prompt-injection-agentic-ai-enterprise-guide)）。OpenAI 也指出，现实中最有效的提示注入已更像社会工程学，而非简单的提示词覆盖（[优化 AI 智能体设计：提升对提示注入的免疫力](https://openai.com/zh-Hans-CN/index/designing-agents-to-resist-prompt-injection/)）。

**浏览器/桌面 agent 的能力边界。** 尽管榜单分数走高，但 CAPTCHA、双因素认证、敏感操作授权等仍是一致的短板（[Best AI Browser Agents 2026](https://thebestaitools.co/best-ai-tools/best-ai-browser-agents-that-browse-the-web-for-you/)）；厂商也普遍提示用户需对 agent 操作保持监督（[7 Best AI Browser Agents in 2026](https://www.usecarly.com/blog/best-ai-browser-agents/)）。

**协议标准化带来的新问题。** 协议连接层虽已基本解决，但智能体间通信的开放性也让人类监督变得不透明，成为治理难点（[The Cost of Unchecked Autonomy](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/03/autonomy-risks-top-10-incidents-v1-csa-styled.pdf)）。

**评测口径与污染隐忧。** 不同基准的分数高度依赖推理协议、工具可用性与评测实现，跨来源直接比较容易失真；同时 SWE-bench 等被广泛引用的 agent 基准也被指出存在较高的数据污染风险（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。此外，「agent」「自主」「生产」等概念缺乏统一定义，导致企业采用率出现从约 5% 到 54% 的宽幅差异，引用时需注意口径（[AI Agent Adoption Statistics 2026](https://prefactor.tech/learn/ai-agent-adoption-statistics/)、[AI Agents in Production: The 2026 Reality Check](https://networkcraft.net/ai-agents-production-2026-reality-check/)）。

## 参考来源

1. [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
2. [What is Model Context Protocol (MCP)?](https://resources.rework.com/libraries/ai-terms/model-context-protocol)
3. [Tool use in AI agents](https://atlan.com/know/ai-agent/ai-agent-tool-use/)
4. [Model Context Protocol Explained](https://www.kunal-chowdhury.com/2026/09/model-context-protocol-mcp-enterprise-ai.html)
5. [MCP joins the Agentic AI Foundation](http://blog.modelcontextprotocol.io/tags/announcement/)
6. [Agentic AI Foundation Launches MCPA Certification](https://www.linuxfoundation.org/press/agentic-ai-foundation-launches-mcpa-certification-to-validate-mcp-expertise)
7. [The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
8. [Open Source and the Future of AI (Linux Foundation 2026)](https://www.linuxfoundation.org/hubfs/Research%20Reports/Open%20Source%20and%20the%20Future%20of%20AI_Report_2026.pdf)
9. [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/)
10. [A2A Protocol v1.0.0](https://a2a-protocol.org/v1.0.0/)
11. [A2A Protocol Ships v1.0](https://a2a-protocol.org/latest/announcing-1.0/)
12. [A2A Protocol Surpasses 150 Organizations](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
13. [What Is AI Agent Tool Calling? MCP, Function Calling, and A2A Explained](https://dev.to/arcade/ai-agent-tool-calling-mcp-a2a-23l6)
14. [LangChain vs. AutoGen](https://www.langchain.com/resources/langchain-vs-autogen)
15. [Compare orchestration frameworks](https://learn.microsoft.com/cs-cz/training/modules/aaai-implement-multi-agent-orchestration-azure-ai-foundry/6-compare-orchestration-frameworks)
16. [The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)
17. [Best AI Agent Frameworks in 2026 (ToolRadar)](https://toolradar.com/guides/best-ai-agent-frameworks)
18. [Best AI Agent Frameworks (aiwiki)](https://aiwiki.ai/wiki/best_ai_agent_frameworks)
19. [AI agent frameworks compared (Arize)](https://arize.com/guides/ai-agent-handbook/agent-frameworks/)
20. [Scale Agents with CrewAI, LangGraph, A2A, and ADK](https://codelabs.developers.google.com/next26/scale-agents)
21. [The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
22. [Claude now moves your mouse, and asks permission first](https://botmonster.com/ai/claude-computer-use-hands-on-ai-desktop-control-cowork/)
23. [Claude in Chrome is generally available](https://claude.com/blog/claude-in-chrome-generally-available)
24. [Claude gets its own browser in Cowork](https://claude.com/blog/cowork-built-in-browser/)
25. [Computer use tool - Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)
26. [Browser use tool - Claude Platform Docs](https://platform.claude.com/docs/pt-BR/agents-and-tools/tool-use/browser-use-tool)
27. [Claude自己长出浏览器（太平洋科技）](https://g.pconline.com.cn/x/2181/21811416.html)
28. [7 Best AI Browser Agents in 2026](https://www.usecarly.com/blog/best-ai-browser-agents/)
29. [Best AI Browser Agents That Browse the Web for You in 2026](https://thebestaitools.co/best-ai-tools/best-ai-browser-agents-that-browse-the-web-for-you/)
30. [The 2026 State of AI Agents Report](https://resources.anthropic.com/hubfs/The%202026%20State%20of%20AI%20Agents%20Report.pdf)
31. [Agentic AI Enterprise 2026: From Pilots to Production](https://thebriefscript.com/agentic-ai-enterprise-2026-autonomous-agents/)
32. [AI Agent Adoption Statistics 2026](https://prefactor.tech/learn/ai-agent-adoption-statistics/)
33. [AI Agents in Production: The 2026 Reality Check](https://networkcraft.net/ai-agents-production-2026-reality-check/)
34. [AI Agents Hit Enterprise Escape Velocity](https://insights.reinventing.ai/articles/ai-agents-enterprise-escape-velocity-2026-02-27)
35. [AI Agents Do Not Fail Alone: The Context Fails First](https://arxiv.org/abs/2607.14275)
36. [Intelligence as Managed Autonomy](https://arxiv.org/pdf/2605.27628)
37. [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
38. [Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents](https://arxiv.org/html/2607.08716)
39. [InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents](https://arxiv.org/html/2601.03204v1)
40. [Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents](https://arxiv.org/html/2606.11680v1)
41. [Model Context Protocol 文档](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro)
42. [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/)
43. [GAIA Leaderboard](https://gaia-benchmark-leaderboard.hf.space/deepseek.com)
44. [AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration](https://arxiv.org/html/2602.03786)
45. [AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)
46. [中国智能体登顶OSWorld，90.2%成功率反超海外巨头](http://www.xinhuanet.com/government/20260805/60bc929f7f0d4722b6ad4f4f22d90fcb/c.html)
47. [AI Browser Agents in 2026: Claude, ChatGPT Work, and Gemini](https://nerdleveltech.com/ai-browser-agents-claude-chatgpt-gemini)
48. [Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)
49. [terminal-bench@2.0 Leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0)
50. [terminal-bench@2.1 Leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.1)
51. [τ-bench](https://taubench.com/)
52. [Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/abs/2607.18366)
53. [The Cost of Unchecked Autonomy](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/03/autonomy-risks-top-10-incidents-v1-csa-styled.pdf)
54. [Autonomous by Design, Uncontrolled in Practice](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-agentic-ai-loss-of-control-20260908-csa-style/)
55. [Promptware and Agentic C2: The Confirmed Attack Class](https://labs.cloudsecurityalliance.org/research/csa-research-note-promptware-agentic-c2-attack-class-2026050/)
56. [AutoJack and Agentjacking: AI Agent Frameworks as a New RCE Attack Surface](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/06/CSA_research_note_ai-agent-rce-autojack-agentjacking_20260623-csa-styled.pdf)
57. [Indirect Prompt Injection in Agentic AI: Enterprise Guide](https://beyondscale.tech/blog/indirect-prompt-injection-agentic-ai-enterprise-guide)
58. [优化 AI 智能体设计：提升对"提示注入"的免疫力（OpenAI）](https://openai.com/zh-Hans-CN/index/designing-agents-to-resist-prompt-injection/)