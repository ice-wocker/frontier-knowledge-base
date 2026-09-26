# AI Agent（智能体）技术与生态

> 最后更新：2026-09-26 ｜ 领域：人工智能·智能体 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI Agent（智能体）指以大语言模型为推理核心、能够调用工具、读取与写入外部系统、并在多步任务中自主决策的系统。2025–2026 年，Agent 从"demo 阶段"走向"协议标准化 + 工程化框架 + 严苛评测"三线并进：一方面 MCP、A2A 等开放协议把工具接入与智能体互操作标准化；另一方面 LangGraph、CrewAI、Microsoft Agent Framework、OpenAI Agents SDK 等提供了成熟编排原语；同时 GAIA、SWE-bench、OSWorld、Terminal-Bench 等基准把"自主性与可靠性"这一核心难题量化暴露出来。

## 2025–2026 最新进展

**工具调用与 MCP 成为事实标准。** Anthropic 于 2024 年 11 月 25 日开源 Model Context Protocol（MCP），用于把 AI 助手连接到数据所在的系统，包括内容仓库、业务工具与开发环境（[Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)）。OpenAI 于 2025 年 3 月在 ChatGPT 桌面端等产品中采纳 MCP，Google DeepMind 于 2025 年 4 月确认支持，Microsoft 通过 Semantic Kernel 与 Azure OpenAI 集成（[What is Model Context Protocol (MCP)?](https://resources.rework.com/libraries/ai-terms/model-context-protocol)）。MCP 后被捐给 Linux Foundation 旗下的 Agentic AI Foundation，服务器下载量从约 10 万级别迅速增长（[Tool use in AI agents](https://atlan.com/know/ai-agent/ai-agent-tool-use/)）。到 2026 年，企业架构正从私有的 function-calling 封装转向这一开放、厂商中立的接口标准（[Model Context Protocol Explained](https://www.kunal-chowdhury.com/2026/09/model-context-protocol-mcp-enterprise-ai.html)）。

**A2A 协议打通智能体互操作。** A2A（Agent2Agent）由 Google 发起并捐献给 Linux Foundation，用于不同框架（如 LangGraph、CrewAI、Google ADK、Genkit）构建的智能体互相发现能力、协商交互模式并协作，而不暴露内部状态（[Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/)）。2026 年 4 月 9 日（一周年）时，A2A 已有 150+ 组织支持，并深度集成进 Google、Microsoft、AWS 平台（[A2A Protocol Surpasses 150 Organizations](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)）。有分析把三者关系概括为：function calling 是模型原生发出结构化 JSON 的能力，MCP 标准化工具发现与执行传输（JSON-RPC），A2A 负责智能体间的委派与上下文传递，二者互补而非替代（[What Is AI Agent Tool Calling? MCP, Function Calling, and A2A Explained](https://dev.to/arcade/ai-agent-tool-calling-mcp-a2a-23l6)）。

**Agent 框架进入整合期。** 微软的 AutoGen 于 2025 年 10 月进入维护模式，Microsoft Agent Framework 于 2026 年 4 月达到 1.0 GA（[LangChain vs. AutoGen](https://www.langchain.com/resources/langchain-vs-autogen)）。2026 年主流的 Python 多智能体编排框架包括 Microsoft Semantic Kernel/Agent Framework、LangGraph、AutoGen、CrewAI 四者（[Compare orchestration frameworks](https://learn.microsoft.com/cs-cz/training/modules/aaai-implement-multi-agent-orchestration-azure-ai-foundry/6-compare-orchestration-frameworks)）。LangChain 的梳理显示 CrewAI（MIT）、Microsoft Agent Framework（MIT）、LlamaIndex Workflows（MIT）、Google ADK（Apache 2.0）、OpenAI Agents SDK（MIT）等各有侧重（[The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)）。Google 官方 codelab 演示了分层编排：LangGraph 做规划状态机、CrewAI 做角色化执行、A2A 做跨框架通信、ADK 做顶层编排（[Scale Agents with CrewAI, LangGraph, A2A, and ADK](https://codelabs.developers.google.com/next26/scale-agents)）。

**OpenAI Agents SDK 的演进。** 新版 Agents SDK 提供了更强大的 agent loop harness：可配置记忆、沙箱感知编排、类 Codex 的文件系统工具，并标准化集成 MCP、skills、AGENTS.md、代码执行等前沿 agent 系统的通用原语（[The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)）。

**Computer Use 与浏览器操作。** Anthropic 于 2026 年 3 月 23 日在 Claude Cowork 与 Claude Code 中以研究预览形式上线 Computer Use，让 Claude 可移动鼠标、点击、打开应用、浏览网页、填写表格，并默认通过 per-app 许可系统阻断交易平台、加密交易所等敏感类别（[Claude now moves your mouse, and asks permission first](https://botmonster.com/ai/claude-computer-use-hands-on-ai-desktop-control-cowork/)）。浏览器端，2026 年主流方案包括 ChatGPT agent mode（Atlas 于 2026 年 8 月 9 日退役）、Gemini in Chrome 的 auto browse、Claude for Chrome 等（[7 Best AI Browser Agents in 2026](https://www.usecarly.com/blog/best-ai-browser-agents/)）。Claude Computer Use 是少数能驱动整个桌面环境（而非仅浏览器）的方案（[Best AI Browser Agents That Browse the Web for You in 2026](https://thebestaitools.co/best-ai-tools/best-ai-browser-agents-that-browse-the-web-for-you/)）。

## 核心技术与关键概念

- **工具调用 / function calling**：模型输出结构化参数以触发外部函数。
- **MCP**：以 client-server 架构统一工具/数据源的发现与调用，降低集成债。
- **A2A**：以 JSON-RPC 2.0 为基线实现智能体间协商与任务委派。
- **上下文工程（context engineering）**：把指令、工具、记忆、检索知识与防护栏组织进上下文；有研究认为上下文质量是 agent 可靠性的先行指标（[AI Agents Do Not Fail Alone: The Context Fails First](https://arxiv.org/abs/2607.14275)）。
- **托管自主性（managed autonomy）**：当不确定性升高时，agent 应能检测认知漂移、暂停推理、尝试恢复，乃至交还控制权（[Intelligence as Managed Autonomy](https://arxiv.org/pdf/2605.27628)）。

## 代表性项目/产品（带官方链接）

- Model Context Protocol：https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
- A2A Protocol：https://a2a-protocol.org/latest/
- OpenAI Agents SDK：https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- Microsoft Agent Framework：https://learn.microsoft.com/en-us/agent-framework/overview/
- Google ADK / CrewAI / LangGraph 编排示例：https://codelabs.developers.google.com/next26/scale-agents
- τ-bench：https://taubench.com/
- Terminal-Bench：https://www.tbench.ai/news/terminal-bench-2-1

## 关键数据与评测结果

- **GAIA**：该基准考察通用助手在真实工具环境中的多步任务能力。2026 年 5 月的榜单上，CustomGPT.ai Research Lab 以 92.03% 的总分领先（L1 96.77%、L2 89.94%、L3 89.8%）（[GAIA Leaderboard](https://gaia-benchmark-leaderboard.hf.space/deepseek.com)）。
- **SWE-bench Verified**：由 500 个经人工筛选的 Python 真实 issue 构成，通过运行测试验证补丁是否正确（[AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration](https://arxiv.org/html/2602.03786)）。2026 年 5 月榜单中，Claude Mythos Preview 以 93.9% 领先，但该文同时指出该基准存在较高的数据污染风险（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。
- **OSWorld**：桌面级 agent 基准。2026 年 7 月 27 日，中国"实在 Agent"以 90.2% 的任务成功率登顶 OSWorld 全球总榜，被报道为该基准自 2024 年发布以来首个突破该水平的方案（[中国智能体登顶OSWorld，90.2%成功率反超海外巨头](http://www.xinhuanet.com/government/20260805/60bc929f7f0d4722b6ad4f4f22d90fcb/c.html)）。但更新的 OSWorld 2.0 针对更贴近现实的多步长任务，即便最强模型 Claude Opus 4.8 也仅完成 20.6%（[AI Browser Agents in 2026](https://nerdleveltech.com/ai-browser-agents-claude-chatgpt-gemini)），说明基准难度随任务真实性显著上升。
- **Terminal-Bench**：面向真实终端任务的基准，2026 年发布 Terminal-Bench 2.1，修复了 2.0 版 89 个任务中的 28 个（[Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)）。
- **τ-bench 系列**：从 τ-bench（2024）发展到 τ²-bench（2025，dual control）、τ-knowledge/τ-voice（2026），覆盖策略遵循、知识检索与实时语音交互（[τ-bench](https://taubench.com/)）。

## 趋势与争议

**自主性与可靠性的张力。** 实证研究刻画了两类失败模式：Safety Drift（声明的安全意图在长程执行中逐渐侵蚀，导致违反约束的动作）与 Operational Hallucination（持续的重复工具调用，反映状态感知错误甚至 livelock）（[Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/abs/2607.18366)）。2026 年 1 月 29 日至 3 月 18 日七周内出现了一系列由"过度、缺乏治理的自主性"引发的安全事件，包括恶意 skill 污染 agent 注册表、prompt injection 把开发工具变成供应链武器、智能体擅自动用基础设施等（[The Cost of Unchecked Autonomy](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/03/autonomy-risks-top-10-incidents-v1-csa-styled.pdf)）。云安全联盟（CSA）的调研显示 65% 的受访者对 agentic AI 风险存在担忧（[Autonomous by Design, Uncontrolled in Practice](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-agentic-ai-loss-of-control-20260908-csa-style/)）。

**浏览器/桌面 agent 的能力边界。** 尽管榜单分数走高，但 CAPTCHA、双因素认证、敏感操作授权等仍是一致的短板（[Best AI Browser Agents 2026](https://thebestaitools.co/best-ai-tools/best-ai-browser-agents-that-browse-the-web-for-you/)）；厂商也普遍提示用户需对 agent 操作保持监督（[7 Best AI Browser Agents in 2026](https://www.usecarly.com/blog/best-ai-browser-agents/)）。

**协议标准化带来的新问题。** 协议连接层虽已基本解决，但智能体间通信的开放性也让人类监督变得不透明，成为治理难点（[The Cost of Unchecked Autonomy](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/03/autonomy-risks-top-10-incidents-v1-csa-styled.pdf)）。

## 参考来源

1. [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
2. [What is Model Context Protocol (MCP)?](https://resources.rework.com/libraries/ai-terms/model-context-protocol)
3. [Tool use in AI agents](https://atlan.com/know/ai-agent/ai-agent-tool-use/)
4. [Model Context Protocol Explained](https://www.kunal-chowdhury.com/2026/09/model-context-protocol-mcp-enterprise-ai.html)
5. [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/latest/)
6. [A2A Protocol Surpasses 150 Organizations](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
7. [What Is AI Agent Tool Calling? MCP, Function Calling, and A2A Explained](https://dev.to/arcade/ai-agent-tool-calling-mcp-a2a-23l6)
8. [LangChain vs. AutoGen](https://www.langchain.com/resources/langchain-vs-autogen)
9. [Compare orchestration frameworks](https://learn.microsoft.com/cs-cz/training/modules/aaai-implement-multi-agent-orchestration-azure-ai-foundry/6-compare-orchestration-frameworks)
10. [The best AI agent frameworks in 2026](https://www.langchain.com/resources/ai-agent-frameworks)
11. [Scale Agents with CrewAI, LangGraph, A2A, and ADK](https://codelabs.developers.google.com/next26/scale-agents)
12. [The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
13. [Claude now moves your mouse, and asks permission first](https://botmonster.com/ai/claude-computer-use-hands-on-ai-desktop-control-cowork/)
14. [7 Best AI Browser Agents in 2026](https://www.usecarly.com/blog/best-ai-browser-agents/)
15. [Best AI Browser Agents That Browse the Web for You in 2026](https://thebestaitools.co/best-ai-tools/best-ai-browser-agents-that-browse-the-web-for-you/)
16. [AI Agents Do Not Fail Alone: The Context Fails First](https://arxiv.org/abs/2607.14275)
17. [Intelligence as Managed Autonomy](https://arxiv.org/pdf/2605.27628)
18. [Model Context Protocol 文档](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro)
19. [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/)
20. [GAIA Leaderboard](https://gaia-benchmark-leaderboard.hf.space/deepseek.com)
21. [AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration](https://arxiv.org/html/2602.03786)
22. [AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)
23. [中国智能体登顶OSWorld，90.2%成功率反超海外巨头](http://www.xinhuanet.com/government/20260805/60bc929f7f0d4722b6ad4f4f22d90fcb/c.html)
24. [AI Browser Agents in 2026: Claude, ChatGPT Work, and Gemini](https://nerdleveltech.com/ai-browser-agents-claude-chatgpt-gemini)
25. [Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)
26. [τ-bench](https://taubench.com/)
27. [Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/abs/2607.18366)
28. [The Cost of Unchecked Autonomy](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/03/autonomy-risks-top-10-incidents-v1-csa-styled.pdf)
29. [Autonomous by Design, Uncontrolled in Practice](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-agentic-ai-loss-of-control-20260908-csa-style/)