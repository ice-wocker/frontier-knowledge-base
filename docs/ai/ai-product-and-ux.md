# AI 产品与 UX

> 最后更新：2026-09-26 ｜ 领域：AI·前沿方向与风险 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

2025–2026 年，AI 产品的交互范式从「对话框」向「入口 + 智能体」演进：AI 助手不再只是插件，而成为承载任务执行、应用构建与持续工作的入口。与此同时，评测驱动迭代（Eval-Driven Development）成为产品工程的基本实践，定价模式也从按席位转向按用量与按结果。这一转变意味着 AI 助手开始覆盖从对话、写作到应用构建与后台任务的完整链路（[微软把 Office 三件套塞进 Copilot](http://m.toutiao.com/group/7689636358889751082/)）。

## 最新进展（2025–2026）

### 交互范式：chat / copilot / agent

微软于 2026 年 9 月 25 日发布新版 Copilot，新增 Home、Code、Autopilot 三项核心能力，意在把 AI 助手从对话工具扩展为可执行任务、构建应用和持续工作的智能代理。其中 Home 成为 Copilot 的新入口，整合 Chat 与 Cowork，并把 Word、Excel、PowerPoint 等 Office 能力直接融入；Code 采用与 GitHub Copilot 相同的技术，让用户用自然语言创建应用、仪表盘等；Autopilot 是此前 Scout AI 代理的升级版，被设计为持续运行的数字协作者，即使用户不在电脑前也能继续执行任务（[微软发布新版 Copilot，引入 Home、Code 和 Autopilot 三大 AI 功能](http://m.toutiao.com/group/7689446294707896883/)、[微软把 Office 三件套塞进 Copilot](http://m.toutiao.com/group/7689636358889751082/)）。

在官方 UX 指南中，微软明确 Copilot 的设计原则：对话优先（conversation-first）、渐进式复杂度（progressive complexity）、上下文保持（context preservation）、清晰而非重复（clarity over duplication），并要求应用支持 inline 模式（[User experience guidelines for MCP apps in declarative agents for Microsoft 365 Copilot](https://learn.microsoft.com/hr-hr/microsoft-365/copilot/extensibility/plugin-mcp-apps-ui-guidelines)）。面向产品团队的 Copilot 设计模式总结则认为 2026 年最高杠杆的模式是：幽灵文本补全（ghost-text completion）、内联动作菜单（Cmd-K 或斜杠命令）与选区锚定操作（selection-anchored actions）（[AI copilot UX design patterns for product teams in 2026](https://www.aydesign.ai/blog/ai-copilot-ux-design-patterns-2026)）。从采纳数据看，AI 编码 agent 的竞争格局仍在变化：调查显示 Claude Code 在 9 个月内实现约 6 倍增长，Google Antigravity 早期采纳迅速，而 GitHub Copilot 与「用于编码的 ChatGPT」的采用趋于平稳（[AI Coding Agent Adoption in 2026](https://codex.danielvaughan.com/2026/04/26/ai-coding-agent-adoption-2026-survey-data-codex-cli-positioning/)）。

### 信任与可控性

开发者对 AI 输出的信任出现下降：2026 年仅 29% 的开发者相信 AI 输出准确，低于 2024 年的 40%，46% 明确表示不信任（[AI Coding Assistant Statistics 2026](https://uvik.net/blog/ai-coding-assistant-statistics/)）。这要求产品在设计上强调可控性、可验证性与可回退，评测与红队也因此成为产品可控性的常规组成部分（[Eval-Driven Development: Why Evals Are the New Unit Tests for AI](https://www.xyzbytes.com/blog/eval-driven-development-new-tdd)）。

### 评测驱动迭代

Eval-Driven Development（EDD）指在设计提示词之前先写评测，用带标签数据集断言分数不低于阈值，并在 CI 中对每次变更做门禁；2026 年 EDD 已从前沿实践变为基线实践（[Eval-Driven Development for LLMs: A 2026 Guide](https://qaskills.sh/blog/eval-driven-development-llm-guide-2026)）。其成为基线的原因是：前沿模型每隔数周就会在你的提示之下发生变化，唯一能捕捉静默回归的机制，是在每个 PR 与每个抽样生产队列上运行的评测套件（[What Is Eval-Driven Development?](https://futureagi.com/glossary/eval-driven-development/)）。Anthropic 的指导是先用 eval 定义能力，再迭代直到 agent 通过（[Eval-Driven Development: Why Evals Are the New Unit Tests for AI](https://www.xyzbytes.com/blog/eval-driven-development-new-tdd)）。一个实践警告是「只评输出的评测会骗人」：仅按最终输出打分的 agent 通过率比全轨迹评测高 20–40%，会掩盖生产中最关键的失败；一个真实的评测闭环应包含来自生产失败的金标准数据集、可信的 grader 与 LLM judge 等部分（[Eval-Driven Development: Why Evals Are the New Unit Tests for AI](https://www.xyzbytes.com/blog/eval-driven-development-new-tdd)）。在更细的方法论中，评测驱动被概括为「定义—测试—诊断—修复」的可重复工程循环，用于替代「凭直觉逐条调提示」的做法（[When "Better" Prompts Hurt: Evaluation-Driven Iteration for LLM Applications](https://arxiv.org/pdf/2601.22025v1)）。

### 定价模式

2026 年 AI agent 定价收敛为四种：按席位订阅、按用量、按结果、混合（[AI Agent Development Cost in 2026: Pricing Models and Real Estimates](https://aimonk.com/ai-agent-pricing-models/)）。据 Futurum Research 调查，不足五分之一的企业买家仍偏好传统按用户定价，43% 更偏好按消费量定价（[AI Agent Development Cost in 2026](https://aimonk.com/ai-agent-pricing-models/)）。按结果定价的代表是 Salesforce Agentforce Help Agent，于 2026 年 6 月 25 日上线，采用每解决一次 2 美元的模型；Intercom Fin、HubSpot、Sierra AI 也在向同一结构收敛（[Outcome-Based AI Pricing Is Here](https://integrated.social/blog/outcome-based-ai-pricing-b2b-marketing-agentforce-2026/)）。按解决次数计价区间约 0.50–2.00 美元/次，失败尝试不收费（[AI Pricing Models: Per-Seat vs Per-Use vs Outcome (2026)](https://korixinc.com/learning-center/ai-pricing-models-2026)）。也有观点认为按结果定价是 2026 年最受关注、最接近「按价值付费」的模式（[AI Agent Pricing Models](https://pickaxe.co/post/ai-agent-pricing-models)）。

## 核心技术与关键概念

- **交互范式**：chat（对话）、copilot（嵌入既有工作流的协作）、agent（可自主执行任务）。
- **Inline / 选区锚定**：在用户所在位置提供操作，而非跳到独立聊天窗口。
- **渐进式复杂度**：默认轻量，仅在需要时展开。
- **EDD（评测驱动开发）**：先定义失败模式与评测，再迭代提示与模型，CI 门禁。
- **全轨迹评测**：不仅评最终输出，还评中间步骤，避免掩盖关键失败。
- **定价模式**：per-seat / usage-based / outcome-based / hybrid。

## 代表性项目 / 公司 / 产品

- Microsoft 365 Copilot：Home / Code / Autopilot 新入口（[界面快讯](http://m.toutiao.com/group/7689446294707896883/)）。
- Salesforce Agentforce：每解决一次 2 美元的结果定价（[integrated.social](https://integrated.social/blog/outcome-based-ai-pricing-b2b-marketing-agentforce-2026/)）。
- Intercom Fin / HubSpot / Sierra AI：收敛于按结果计费（[integrated.social](https://integrated.social/blog/outcome-based-ai-pricing-b2b-marketing-agentforce-2026/)、[korixinc](https://korixinc.com/learning-center/ai-pricing-models-2026)）。

## 关键数据与评测结果

| 事项 | 数据 | 来源 |
| --- | --- | --- |
| 开发者使用/计划使用 AI 工具 | 84%（Stack Overflow 2025 调查，2024 为 76%） | [AI Coding Statistics 2026](https://sqmagazine.co.uk/ai-coding-statistics/) |
| 每日使用 AI 工具的专业开发者 | 51% | [AI Coding Assistant Statistics 2026](https://uvik.net/blog/ai-coding-assistant-statistics/) |
| 常规使用 AI 工具的开发者（JetBrains 2025） | 85% | [AI Coding Statistics 2026](https://sqmagazine.co.uk/ai-coding-statistics/) |
| 信任 AI 输出准确的开发者 | 29%（2024 为 40%），46% 不信任 | [AI Coding Assistant Statistics 2026](https://uvik.net/blog/ai-coding-assistant-statistics/) |
| GitHub Copilot 用户数 | 约 2000 万（2026 年 7 月） | [AI Coding Assistant Statistics 2026](https://uvik.net/blog/ai-coding-assistant-statistics/) |
| Cursor ARR | 2026 年 2 月达 20 亿美元 | [AI for Coding & Software Development](https://aibuzz.blog/ai-for-coding-software-development/) |
| 企业买家偏好按消费量定价 | 43%；偏好按用户定价不足 1/5 | [AI Agent Development Cost in 2026](https://aimonk.com/ai-agent-pricing-models/) |
| Agentforce 结果定价 | 2 美元/解决 | [Outcome-Based AI Pricing](https://integrated.social/blog/outcome-based-ai-pricing-b2b-marketing-agentforce-2026/) |

## 趋势与争议

1. **入口之争**：AI 助手从插件升级为操作系统级入口，可能重塑既有应用分发与用户关系（[微软新版 Copilot](http://m.toutiao.com/group/7689636358889751082/)）。
2. **信任赤字**：能力提升的同时开发者信任下降，产品需以可控性与证据弥补（[AI Coding Assistant Statistics 2026](https://uvik.net/blog/ai-coding-assistant-statistics/)）。
3. **评测与产品耦合**：EDD 成为门禁，但「只评输出」会产生虚假达标（[Eval-Driven Development](https://www.xyzbytes.com/blog/eval-driven-development-new-tdd)）。
4. **定价不确定性**：按结果定价把失败成本转移给厂商，其可持续性取决于解决率与单位成本（[AI Pricing Models 2026](https://korixinc.com/learning-center/ai-pricing-models-2026)）。
5. **采纳成本与影子 AI**：有统计称影子 AI 事件使数据泄露平均成本增加约 67 万美元，且 47% 员工在组织禁用后仍使用个人 AI 账号（[AI for Coding & Software Development](https://aibuzz.blog/ai-for-coding-software-development/)）。
6. **持续运行代理的授权问题**：随着 Autopilot 类「持续运行的数字协作者」出现，产品需要处理用户不在场时的授权、审计与回退问题（[微软发布新版 Copilot](http://m.toutiao.com/group/7689446294707896883/)）。

## 参考来源

- [微软发布新版 Copilot，引入 Home、Code 和 Autopilot 三大 AI 功能（界面快讯）](http://m.toutiao.com/group/7689446294707896883/)
- [微软把 Office 三件套塞进 Copilot，AI 助手从"插件"变"入口"（华尔街见闻）](http://m.toutiao.com/group/7689636358889751082/)
- [User experience guidelines for MCP apps in declarative agents for Microsoft 365 Copilot](https://learn.microsoft.com/hr-hr/microsoft-365/copilot/extensibility/plugin-mcp-apps-ui-guidelines)
- [AI copilot UX design patterns for product teams in 2026](https://www.aydesign.ai/blog/ai-copilot-ux-design-patterns-2026)
- [AI Coding Assistant Statistics 2026: Adoption, Trust & Productivity](https://uvik.net/blog/ai-coding-assistant-statistics/)
- [AI Coding Statistics 2026: Adoption, Productivity and Market Data](https://sqmagazine.co.uk/ai-coding-statistics/)
- [AI for Coding & Software Development](https://aibuzz.blog/ai-for-coding-software-development/)
- [Eval-Driven Development for LLMs: A 2026 Guide](https://qaskills.sh/blog/eval-driven-development-llm-guide-2026)
- [Eval-Driven Development: Why Evals Are the New Unit Tests for AI](https://www.xyzbytes.com/blog/eval-driven-development-new-tdd)
- [What Is Eval-Driven Development?](https://futureagi.com/glossary/eval-driven-development/)
- [When "Better" Prompts Hurt: Evaluation-Driven Iteration for LLM Applications](https://arxiv.org/pdf/2601.22025v1)
- [AI Agent Development Cost in 2026: Pricing Models and Real Estimates](https://aimonk.com/ai-agent-pricing-models/)
- [Outcome-Based AI Pricing Is Here: Salesforce Agentforce's $2-Per-Resolution Model](https://integrated.social/blog/outcome-based-ai-pricing-b2b-marketing-agentforce-2026/)
- [AI Pricing Models: Per-Seat vs Per-Use vs Outcome (2026)](https://korixinc.com/learning-center/ai-pricing-models-2026)
- [AI Agent Pricing Models: Per-Seat, Usage-Based, and Outcome-Based Explained](https://pickaxe.co/post/ai-agent-pricing-models)
- [AI Coding Agent Adoption in 2026: What the Survey Data Actually Shows](https://codex.danielvaughan.com/2026/04/26/ai-coding-agent-adoption-2026-survey-data-codex-cli-positioning/)