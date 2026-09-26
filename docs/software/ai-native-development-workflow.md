# AI 原生研发流程（AI-Native Development Workflow）

> 最后更新：2026-09-26 ｜ 领域：软件工程 · AI 原生研发 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI 原生研发流程指把大模型与智能体（agent）作为默认参与者，嵌入从需求、设计、编码、评审、测试、文档到部署与事故响应的软件开发生命周期（SDLC），而非仅在编辑器里提供补全。2025–2026 年的核心结论是：**AI 显著加速了“代码产出”这一环节，但能否转化为整体交付绩效，取决于下游工程基础（平台、测试、评审、可观测性）是否扎实**。DORA 2025 报告《State of AI-assisted Software Development》（2025 年 9 月发布）将其概括为“AI 是放大器”：它放大高效组织的优势，也放大薄弱组织的失序（[DORA 2025: Year in review](https://dora.dev/insights/dora-2025-year-in-review/)）。

## 最新进展（2025–2026）

**1. 采用率接近饱和，收益与信任脱节。** DORA 2025 指出约 90% 的技术从业者已在工作中使用 AI，逾 80% 认为提升了自身生产力，但仍有约 30% 对 AI 生成代码缺乏信任（[Balancing AI tensions](https://dora.dev/insights/balancing-ai-tensions/)、[90% of Developers Use AI: Google DORA 2025](https://www.adwaitx.com/google-dora-2025-90-percent-developers-use-ai/)）。DORA 同时发现“信任悖论”：24% 的受访者“非常/相当”信任 AI，30% 仅“略微/完全不”信任（[Inside our 2025 DORA report](https://blog.google/technology/developers/dora-report-2025/)）。

**2. 智能体原生地进入平台与流水线。** GitHub 于 2025 年推出 Agent HQ，把 Anthropic、OpenAI、Google、Cognition、xAI 等的编码智能体统一进 GitHub 与 VS Code，作为付费 Copilot 订阅的一部分；Claude 与 OpenAI Codex 随后进入公开预览（[Introducing Agent HQ](https://github.blog/news-insights/company-news/welcome-home-agents/)、[Pick your agent](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)）。GitHub 还发布面向并行智能体工作流的 Copilot 桌面应用技术预览，其动机之一是应对“工作流割裂、上下文切换过多、评审智能体生成代码耗时过多”等问题（[GitHub Copilot app](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/)、[GitHub Copilot Desktop App Targets Parallel Agentic Workflows](https://www.infoq.com/news/2026/06/github-copilot-app/)）。

**3. 落地建议偏向“分阶段、选低风险环节先行”。** 行业指南建议先从重复、可度量、低风险的流程起步，典型候选是测试生成、文档、事故摘要与 backlog 分析（[Agentic SDLC](https://www.dronahq.com/agentic-sdlc-guide)）。

**4. 代码评审自动化成为独立赛道。** 多家工具提供 PR 级 AI 评审（CodeRabbit、Greptile、Qodo/Cursor Bugbot 等）。Greptile 在其官方基准中称在 50 个开源 PR 上捕获 82% 的 bug，Bugbot 58%、Copilot 54%、CodeRabbit 44%、Graphite 6%（[Greptile AI Code Review Benchmarks](https://www.greptile.com/benchmarks)）。但存在明显口径冲突：一个独立对照基准将 Greptile 的捕获率下调至 45%；在 OpenSSF CVE Benchmark 上 DeepSource 达 84.51% F1、CodeRabbit 为 36.19% F1，说明准确率高度依赖缺陷类型（[Code review IA : 6 bots en PR](https://www.decodeur-ia.com/articles/comparatif-6-bots-code-review-ia-coderabbit-greptile-qodo-cursor-bugbot-copilot-graphite/)）。

## 核心技术与关键概念

- **全流程介入点**：需求澄清与拆解、架构与方案设计、代码生成与重构、依赖升级、测试生成、文档生成、评审、部署脚本与事故复盘。DORA 观察到一个关键现象：AI 降低了“启动新任务”的门槛，但把成本转移到后续的评审与验证环节（[Balancing AI tensions](https://dora.dev/insights/balancing-ai-tensions/)）。
- **上下文工程**：AI 建议质量与团队是否沉淀了业务上下文、架构约定与决策记录强相关；文档因此从“负担”转为性能杠杆（[L'IA comme amplificateur : la théorie DORA 2025](https://www.sfeir.com/articles/ia-amplificateur-theorie-dora-2025/)）。
- **决策记录（ADR）的 AI 化**：有研究提出 AI-ADR，在 Markdown Any Decision Records（MADR）模板上扩展 AI 专属字段（如可解释性等），以记录 AI 相关架构选择（[RAD-AI: Rethinking Architecture Documentation for AI-Augmented Ecosystems](https://arxiv.org/html/2603.28735v1)）。
- **多智能体编排**：把编码、评审、测试、修复拆给不同智能体并行执行，需要统一的会话状态、权限与观测面。

## 代表性项目 / 产品（附官方链接）

- **GitHub Agent HQ / Copilot app**：智能体统一的平台层（[github.blog](https://github.blog/news-insights/company-news/welcome-home-agents/)）。
- **CodeRabbit / Greptile**：AI 代码评审代表产品（[coderabbit.ai](https://www.coderabbit.ai/)、[greptile.com/benchmarks](https://www.greptile.com/benchmarks)）。
- **SWE-bench / ProgramBench**：衡量自动修复与从零构建程序能力的基准；SWE-bench 原始集含 2294 个来自 12 个 Python 仓库的真实 GitHub issue，2026 年 5 月新增 ProgramBench（[SWE-bench 官网](https://www.swebench.com/)）。

## 关键数据与评测结果（附来源）

| 指标 | 数据 | 来源 |
| --- | --- | --- |
| 技术从业者 AI 使用率 | 约 90% | [DORA / Google](https://www.adwaitx.com/google-dora-2025-90-percent-developers-use-ai/) |
| 对 AI 生成代码缺信任比例 | 约 30% | [DORA](https://dora.dev/insights/balancing-ai-tensions/) |
| SWE-bench Verified 最高分（某 harness） | 82.2%（GPT-5.5），高于当时榜单 SOTA 79.2% | [NVIDIA Developer Blog](https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/) |
| AI 生成代码平均漏洞率（形式化验证研究） | 55.8%（7 个模型），GPT-4o 62.4%、Gemini 2.5 Flash 48.4% | [Broken by Default (arXiv)](https://arxiv.org/html/2604.05292v1) |
| AI 工具归因 CVE 趋势 | 2026 年 1 月 6 个 → 2 月 15 个 → 3 月 35 个 | [CSA Research Note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/) |

## 趋势与争议

**趋势：** 一是评审与测试环节被自动化工具大量接管；二是文档与测试被重新定义为“给 AI 的上下文投资”（[Documentation Is the New Source Code](https://devblogs.microsoft.com/ise/documentation-is-the-new-source-code/)）；三是智能体权限、审计与人工把关成为平台标准能力。

**争议：** 其一，生产力增益的真实性存在强冲突口径。METR 于 2025 年 7 月的随机对照试验发现，经验丰富的开源开发者在自身仓库使用早期 2025 年 AI 工具时，完成时间反而增加 19%，而他们在任务前预计缩短 24%、任务后仍认为缩短 20%（[Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)）。这与 DORA 的自评口径互相矛盾，说明“感知生产力”与“客观度量”可能严重背离。其二，AI 提速是否以稳定性为代价：DORA 指出 AI 采用与交付不稳定相关，有分析引述 Cortex 与 Faros.ai 数据显示 PR 数上升同时每 PR 事故数与变更失败率上升（[The AI Code Quality Paradox](https://www.practicallogix.com/the-ai-code-quality-paradox-why-84-of-developers-use-ai-tools-but-only-29-trust-them/)）。其三，AI 生成代码的安全风险数据分歧较大：有研究给出 40%–62% 的漏洞率区间，且指出该比率并未随模型功能提升而下降，同时新增针对智能体层的间接提示注入与“slopsquatting”供应链攻击面（[Investigating the Security Risks and Vulnerabilities Introduced by AI Generated Code](https://jenerjournalarchive.com/wp-content/uploads/2026/07/investigating-the-security-risks-and-vulnerabilities-introduction-by-ai-generated-code-in-modern-web-development-environment.pdf)）。其四，AI 评审工具的“高捕获率”多为厂商自评，独立复现结果显著更低，需警惕假阳性成本（[CodeRabbit vs Qodo vs Greptile](https://baeseokjae.github.io/posts/coderabbit-vs-qodo-vs-greptile-2026/)）。

## 参考来源

- [DORA 2025: Year in review](https://dora.dev/insights/dora-2025-year-in-review/)
- [Balancing AI tensions: Moving from AI adoption to effective SDLC use (DORA)](https://dora.dev/insights/balancing-ai-tensions/)
- [How are developers using AI? Inside our 2025 DORA report (Google)](https://blog.google/technology/developers/dora-report-2025/)
- [90% of Developers Use AI: Google DORA 2025 Report](https://www.adwaitx.com/google-dora-2025-90-percent-developers-use-ai/)
- [Introducing Agent HQ: Any agent, any way you work (GitHub Blog)](https://github.blog/news-insights/company-news/welcome-home-agents/)
- [Pick your agent: Use Claude and Codex on Agent HQ (GitHub Blog)](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)
- [GitHub Copilot app: The agent-native desktop experience (GitHub Blog)](https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/)
- [GitHub Copilot Desktop App Targets Parallel Agentic Workflows (InfoQ)](https://www.infoq.com/news/2026/06/github-copilot-app/)
- [Agentic SDLC: A practical guide to AI-led software delivery in 2026](https://www.dronahq.com/agentic-sdlc-guide)
- [AI Code Reviews | CodeRabbit](https://www.coderabbit.ai/)
- [Greptile AI Code Review Benchmarks](https://www.greptile.com/benchmarks)
- [Code review IA : 6 bots en PR, 12 critères](https://www.decodeur-ia.com/articles/comparatif-6-bots-code-review-ia-coderabbit-greptile-qodo-cursor-bugbot-copilot-graphite/)
- [CodeRabbit vs Qodo vs Greptile: Best AI Code Review Tool 2026](https://baeseokjae.github.io/posts/coderabbit-vs-qodo-vs-greptile-2026/)
- [SWE-bench](https://www.swebench.com/)
- [Six Agent Harness Capabilities for Higher Model Performance (NVIDIA)](https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/)
- [Broken by Default: A Formal Verification Study (arXiv)](https://arxiv.org/html/2604.05292v1)
- [Vibe Coding's Security Debt: The AI-Generated CVE Surge (CSA)](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/)
- [Investigating the Security Risks and Vulnerabilities Introduced by AI Generated Code](https://jenerjournalarchive.com/wp-content/uploads/2026/07/investigating-the-security-risks-and-vulnerabilities-introduction-by-ai-generated-code-in-modern-web-development-environment.pdf)
- [Documentation Is the New Source Code (Microsoft ISE)](https://devblogs.microsoft.com/ise/documentation-is-the-new-source-code/)
- [RAD-AI: Rethinking Architecture Documentation for AI-Augmented Ecosystems (arXiv)](https://arxiv.org/html/2603.28735v1)
- [L'IA comme amplificateur : la théorie DORA 2025 décryptée (SFEIR)](https://www.sfeir.com/articles/ia-amplificateur-theorie-dora-2025/)
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity (METR)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [The AI Code Quality Paradox](https://www.practicallogix.com/the-ai-code-quality-paradox-why-84-of-developers-use-ai-tools-but-only-29-trust-them/)