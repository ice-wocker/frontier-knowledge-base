# AI 与 LLM 安全

> 最后更新：2026-09-26 ｜ 领域：安全 · AI/LLM 攻防 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

LLM 应用的安全问题源于一个结构性事实：模型无法在上下文窗口内对"数据"与"指令"做硬性隔离（[OWASP Top 10 for LLM Applications 2025 解读](https://secportal.io/blog/owasp-top-10-for-llm-applications-explained)）。因此，攻击者只要能把自然语言指令送入模型可见的通道——用户输入、检索到的文档、工具返回、网页、附件——就可能覆盖开发者写入的系统提示。OWASP 将这类风险列为 LLM01: Prompt Injection，并明确指出这些输入"不需要对人可见或可读"，只要被模型解析即可（[OWASP-Top-10-for-LLMs-v2025.pdf](https://owasp.github.io/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)）。

## 最新进展（2025–2026）

**OWASP 榜单两代并存。** 2025 版为 LLM01 Prompt Injection、LLM02 Sensitive Information Disclosure、LLM03 Supply Chain、LLM04 Data and Model Poisoning、LLM05 Improper Output Handling 等（[OWASP LLM Top 10: A Builder's Map](https://dev.to/coppersundev/owasp-llm-top-10-a-builders-map-5b2a)）。2026 版（v1.0，日期为 2026 年 8 月 3 日）排序为：LLM01 Prompt Injection、LLM02 Sensitive Information Disclosure、LLM03 Excessive Agency、LLM04 Supply Chain、LLM05 Data and Model Poisoning、LLM06 Unbounded Consumption、LLM07 Misinformation、LLM08 Hidden Context Exposure、LLM09 Vector and Embedding Weaknesses、LLM10 Improper Output Handling（[CSA：OWASP's 2026 LLM Top 10](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/09/CSA_research_note_owasp_genai_top10_2026_agent_control_standard_20260904-csa-styled.pdf)、[OWASP GenAI LLM Top 10 2026 概览](https://owasp.org/www-project-top-10-for-large-language-model-applications/)）。相比 2025 版，最显著的变化是 Excessive Agency 从 LLM06 升至 LLM03（[OWASP LLM Top 10 2026 对照](https://altaysec.com.tr/arastirmalar/owasp-llm-top10-2026-turkce)）。一个第三方整理指出 2026 版为 v1.0（[OWASP LLM Top 10 (2026): Official List and What Changed](https://www.respan.ai/articles/owasp-llm-top-10)）。

**间接提示注入进入实战。** 2026 年 4 月下旬，Google Security 与 Forcepoint X-Labs 相继发布分析，确认攻击者已在开放网络中埋入隐藏指令以劫持浏览型 AI 代理、编码助手与企业 copilot；Palo Alto Networks Unit 42 亦有相关观测（[CSA：Indirect Prompt Injection Goes Operational](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_indirect_prompt_injection_in_the_wild_20260426-csa-styled.pdf)）。2026 年 7 月，Noma Security 披露 GitLost：利用公开 GitHub issue 中嵌入的隐蔽指令，诱使 GitHub 的 Agentic Workflow（按 `issues.assigned` 事件触发）在公开评论中泄露私有仓库数据（[Indirect Prompt Injection Exploits GitHub's AI Agent](https://www.infoq.com/news/2026/07/gitlost-github-prompt-injection/)）。Zenity 则公开了针对 Claude 与 ChatGPT/Atlas 代理式浏览器能力的零点击注入手法，攻击面涵盖邮件与 X 帖子，无需受害者主动交互（[Claude and ChatGPT Hijacked via Zero-Click Prompt Injection](https://gridthegrey.com/posts/claude-and-chatgpt-hijacked-via-zero-click-prompt-injection/)）。

**防御范式转向"抗社工"。** OpenAI 在其官方文章中表示，现实中效果最好的注入攻击越来越像社会工程而非简单的提示覆盖，因此防御重心应从"识别恶意字符串"转向抵抗误导与操纵性内容（[Designing AI agents to resist prompt injection](https://openai.com/index/designing-agents-to-resist-prompt-injection/)）。研究者进一步提出 Agent Data Injection（ADI）：不把不可信数据当作指令，而是伪造模型依赖的、被当作可信锚点的元数据（如评论作者/角色、邮件 sender、Web UI 元素标识、工具调用历史），使代理在执行用户原始任务的同时作用于伪造元数据（[Agent Data Injection (ADI)](https://www.howardism.dev/articles/agent-data-injection)）。

**Agent 与工具链成为主战场。** MCP（Model Context Protocol）相关的工具投毒（Tool Poisoning Attack，由 Invariant Labs 首次识别）利用模型对工具描述文本的天然信任触发未授权行为；多工具阈值投毒等新手法（如 ShareLock）被陆续提出（[ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP](https://arxiv.org/html/2606.27027)）。协议层亦被质疑：对 MCP STDIO 设计缺陷的分析指出，攻击者若能写或影响 MCP 配置文件，可在无需模型参与的情况下获得主机上的任意代码执行路径，影响范围被估计覆盖 20 万以上 AI 部署（[CSA：MCP STDIO Design Flaw Enables Systemic AI Supply Chain RCE](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_mcp_rce_design_vulnerability_20260423-csa-styled.pdf)）。由于基础协议规范未强制认证与授权，大量部署在未验证调用方身份的情况下接受连接或工具调用，OWASP MCP Top 10 将认证/授权不足列为 MCP07:2025（[CSA：Poisoned Foundations: The AI Developer Toolchain Attack Surface](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/06/ai-dev-toolchain-supply-chain-attack-surface-v1.0-csa-styled.pdf)）。OWASP 的 Agent Memory Guard 项目则聚焦记忆投毒——持久化代理记忆可被运行时篡改并跨会话延续，不同于模型权重（[OWASP Agent Memory Guard](https://owasp.org/www-project-agent-memory-guard/)）。

**模型与数据供应链。** 2026 年 5 月 10 日，攻击者注册 Hugging Face 组织 `Open-OSS` 并发布仿冒的 `privacy-filter` 仓库，模仿合法模型 `OpenCSS/privacy-filter`（[Defending Against Fake HuggingFace Repository Attacks](https://www.systemshardening.com/articles/ai-landscape/huggingface-fake-repo-attack-defence/)）。评论普遍指出，最直接的防御是放弃 Pickle、强制使用 safetensors——该格式只能存储张量数据，结构上无法在执行加载时运行任意代码；但仍需注意恶意元数据字段、导致解析器崩溃的损坏张量，以及"良性 safetensors + 恶意 pickle 或加载代码并存"的仓库（[The Open-OSS Malware Attack and the ML Supply Chain Crisis](https://mlhive.com/2026/05/open-oss-malware-machine-learning-supply-chain)、[AI Red Teaming Guide: Supply Chain](https://philocyber.com/en/resources/ai-red-teaming-guide/supply-chain)）。

**规模与数据。** Zscaler ThreatLabz 的 2026 AI 威胁报告（2026 年 6 月 17 日）称，员工全年向 AI 工具上传企业数据 18,033 TB，同比增长 93%；仅 ChatGPT 就产生 4.1 亿次 DLP 策略违规，同比增 99%（[Reading the Zscaler ThreatLabz Numbers](https://www.deepinspect.ai/blog/enterprise-ai-data-exposure-zscaler-2026-threat-report)）。Orca Security 的《2026 State of AI Security》称 51.5% 组织已用 AI 构建自定义应用，但 80% 的 SageMaker 部署仍启用全部五项核心不安全默认配置，81% 拥有 AI 包的组织至少存在一个已知高危漏洞，公开利用代码覆盖 50.1% 的告警（高于此前的 0.2%）（[2026 STATE OF AI SECURITY REPORT](https://orca.security/wp-content/uploads/2026/07/2026-State-of-AI-Security-Report.pdf)）。转引的行业数据还包括：生产环境中成功攻击平均 42 秒完成、90% 泄露敏感数据（Pillar Security），提示注入攻击同比上升 340%（OWASP, Q1 2026），13% 的组织已因 AI 模型或应用被入侵，其中 97% 缺乏基础 AI 访问控制（IBM）（[OrcaRouter Releases AI Threat Report 2026](https://kakacomputer.com/orcarouter-releases-ai-threat-report-2026-and-makes-its-security-controls-free-amid-rise-in-prompt-injection-attacks/)）。

## 核心技术与关键概念

- **直接注入 vs 间接注入**：前者由用户输入触发，后者把指令藏进模型会读取的外部内容（检索文档、工具响应、网页、附件）（[OWASP 2025 解读](https://secportal.io/blog/owasp-top-10-for-llm-applications-explained)）。
- **Excessive Agency（过度自主）**：代理可自主调用工具、执行 shell 命令、发起未受检 API 调用，是 2026 榜单中上升最快的风险（[CSA 2026 榜单](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/09/CSA_research_note_owasp_genai_top10_2026_agent_control_standard_20260904-csa-styled.pdf)）。
- **缓解措施（OWASP 官方口径）**：实施最小权限与专用 API token、把高风险操作的执行放在代码中而非交给模型、对特权操作引入 human-in-the-loop、对外部内容做隔离与标注（segregate and identify external content）（[OWASP-Top-10-for-LLMs-v2025.pdf](https://owasp.github.io/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)）。
- **提示层防护**：避免向用户暴露原始提示、用严格模板/分隔符区分用户输入与系统指令、生成后做安全内容过滤、支持模型级指令锁定、训练与微调数据严格消毒（[OWASP Community: Prompt Injection](https://community.owasp.org/attacks/PromptInjection)）。
- **Agentic Skill 生态防护**：要求所有已发布 skill 具备 ed25519 等密码学签名并拒绝未签名内容；把 skill 输出一律当作不可信数据、保留 provenance、在每一跳重建指令/数据边界（[OWASP Agentic Skills Top 10](https://owasp.github.io/www-project-agentic-skills-top-10/assets/publications/ast10-top10-whitepaper-2.pdf)）。
- **红蓝紫队闭环**：红队使用自主代理、prompt fuzzing、记忆投毒；蓝队监控运行时行为与异常；紫队关联攻击与告警、调优检测规则并自动改进护栏，强调持续安全而非一次性测试（[AI Security Solutions Landscape For AI and Agentic Red Teaming](https://genai.owasp.org/download/54018/?tmstv=1775767894)）。
- **评测基准**：AgentDojo 是一个动态评测框架，用于衡量在不可信数据上执行工具的代理的效用与对抗鲁棒性，包含 97 个跨领域真实任务；它由 US AISI 在与 UK AISI 的联合红队演练中扩展，并曾用于展示 Claude 3.5 Sonnet (new) 对提示注入的脆弱性（[AgentDojo（Inspect Evals）](https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentdojo/index.html)、[AgentDojo 官网](https://agentdojo.spylab.ai/)）。2026 年 6 月 19 日发布的 AutoDojo 指出静态基准只回放固定注入池，可能高估防御效果（[AutoDojo](https://www.llm-hacking.com/hacks/auto-dojo-adaptive-ipi-task-specification.md/)）。LlamaFirewall 等开源护栏系统以 AgentDojo 评估分层防御（[LlamaFirewall（arXiv）](https://arxiv.org/html/2505.03574)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **OWASP GenAI Security Project**（[owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/)）：LLM Top 10、Agentic Skills Top 10、Agent Memory Guard、MCP Top 10、AI Security Solutions Landscape。
- **商用/AI 防火墙**：Akamai Firewall for AI（实时检测提示注入、数据外泄与有害内容，入站过滤 + 出站净化）、Radware LLM Firewall（模型无关的 prompt 级检查）等被收录于 OWASP 解决方案分类（[Prompt Security | OWASP](https://genai.owasp.org/solution-taxonomy/prompt-security/)）。
- **开源护栏**：LlamaFirewall（[arXiv](https://arxiv.org/html/2505.03574)）、PromptArmor（[arXiv](https://arxiv.org/html/2507.15219)）。
- **模型托管安全**：Hugging Face 的 safetensors 格式与 SHA256 完整性校验被广泛推荐为防 Pickle 载荷的基础措施（[Open-OSS 分析](https://mlhive.com/2026/05/open-oss-malware-machine-learning-supply-chain)）。

## 关键数据与评测结果（附来源）

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 企业向 AI 工具上传数据 | 18,033 TB/年（+93%） | [Zscaler 2026 AI Threat Report 解读](https://www.deepinspect.ai/blog/enterprise-ai-data-exposure-zscaler-2026-threat-report) |
| ChatGPT DLP 违规 | 4.1 亿次（+99% YoY） | 同上 |
| SageMaker 不安全默认全开比例 | 80% | [Orca 2026 State of AI Security](https://orca.security/wp-content/uploads/2026/07/2026-State-of-AI-Security-Report.pdf) |
| 含高危漏洞的 AI 包组织占比 | 81% | 同上 |
| 提示注入攻击同比增幅 | 340%（OWASP, Q1 2026） | [OrcaRouter AI Threat Report 2026](https://kakacomputer.com/orcarouter-releases-ai-threat-report-2026-and-makes-its-security-controls-free-amid-rise-in-prompt-injection-attacks/) |
| 因 AI 被入侵的组织占比 | 13%（其中 97% 缺基础访问控制，IBM） | 同上 |
| AgentDojo 任务数 | 97 | [LlamaFirewall（arXiv）](https://arxiv.org/html/2505.03574) |

## 趋势与争议

- **"检测恶意字符串"路线被质疑**：OpenAI 认为真实攻击更接近社工，防御需能抵抗误导性叙述而非仅做模式匹配（[OpenAI](https://openai.com/index/designing-agents-to-resist-prompt-injection/)）；ADR/ADI 类工作则指出，让模型"仍然完成用户任务但作用于伪造元数据"更难被察觉（[ADI](https://www.howardism.dev/articles/agent-data-injection)）。
- **基准可靠性争议**：静态注入池可能导致防御被高估，需要自适应评测（[AutoDojo](https://www.llm-hacking.com/hacks/auto-dojo-adaptive-ipi-task-specification.md/)）。
- **协议与生态的信任缺口**：MCP 规范未强制认证、skill 生态缺少签名强制，都会把单点工具链缺陷放大为系统性 RCE 或供应链风险（[CSA MCP STDIO](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_mcp_rce_design_vulnerability_20260423-csa-styled.pdf)、[OWASP Agentic Skills Top 10](https://owasp.github.io/www-project-agentic-skills-top-10/assets/publications/ast10-top10-whitepaper-2.pdf)）。
- **榜单版本分歧**：2025 与 2026 两版 OWASP 榜单并存，官方建议对照阅读而非二选一（[OWASP LLM Top 10 (2026)](https://www.respan.ai/articles/owasp-llm-top-10)）。

## 参考来源

- [OWASP Top 10 for LLM Applications 2025（PDF）](https://owasp.github.io/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)
- [OWASP Top 10 for Large Language Model Applications（官网）](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP Top 10 for LLM Applications (2025): A Practical Guide](https://secportal.io/blog/owasp-top-10-for-llm-applications-explained)
- [OWASP LLM Top 10: A Builder's Map](https://dev.to/coppersundev/owasp-llm-top-10-a-builders-map-5b2a)
- [OWASP LLM Top 10 (2026): Official List and What Changed](https://www.respan.ai/articles/owasp-llm-top-10)
- [OWASP LLM Top 10 2026（对照表）](https://altaysec.com.tr/arastirmalar/owasp-llm-top10-2026-turkce)
- [CSA：OWASP's 2026 LLM Top 10 and New Agent Control Standard](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/09/CSA_research_note_owasp_genai_top10_2026_agent_control_standard_20260904-csa-styled.pdf)
- [CSA：Indirect Prompt Injection Goes Operational In-the-Wild Campaigns](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_indirect_prompt_injection_in_the_wild_20260426-csa-styled.pdf)
- [Indirect Prompt Injection Exploits GitHub's AI Agent to Leak Private Repository Data（InfoQ）](https://www.infoq.com/news/2026/07/gitlost-github-prompt-injection/)
- [Claude and ChatGPT Hijacked via Zero-Click Prompt Injection](https://gridthegrey.com/posts/claude-and-chatgpt-hijacked-via-zero-click-prompt-injection/)
- [Designing AI agents to resist prompt injection（OpenAI）](https://openai.com/index/designing-agents-to-resist-prompt-injection/)
- [Agent Data Injection (ADI)](https://www.howardism.dev/articles/agent-data-injection)
- [OWASP Community: Prompt Injection](https://community.owasp.org/attacks/PromptInjection)
- [OWASP Agentic Skills Top 10（PDF）](https://owasp.github.io/www-project-agentic-skills-top-10/assets/publications/ast10-top10-whitepaper-2.pdf)
- [OWASP Agent Memory Guard](https://owasp.org/www-project-agent-memory-guard/)
- [OWASP Prompt Security 解决方案分类](https://genai.owasp.org/solution-taxonomy/prompt-security/)
- [OWASP：AI Security Solutions Landscape For AI and Agentic Red Teaming](https://genai.owasp.org/download/54018/?tmstv=1775767894)
- [CSA：MCP STDIO Design Flaw Enables Systemic AI Supply Chain RCE](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_mcp_rce_design_vulnerability_20260423-csa-styled.pdf)
- [CSA：Poisoned Foundations: The AI Developer Toolchain Attack Surface](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/06/ai-dev-toolchain-supply-chain-attack-surface-v1.0-csa-styled.pdf)
- [ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP（arXiv）](https://arxiv.org/html/2606.27027)
- [Defending Against Fake HuggingFace Repository Attacks](https://www.systemshardening.com/articles/ai-landscape/huggingface-fake-repo-attack-defence/)
- [The Open-OSS Malware Attack and the Machine Learning Supply Chain Crisis](https://mlhive.com/2026/05/open-oss-malware-machine-learning-supply-chain)
- [AI Red Teaming Guide: Supply Chain](https://philocyber.com/en/resources/ai-red-teaming-guide/supply-chain)
- [AgentDojo（Inspect Evals 文档）](https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentdojo/index.html)
- [AgentDojo 官网](https://agentdojo.spylab.ai/)
- [AutoDojo: why 'action-open' agent tasks quietly break prompt-injection defenses](https://www.llm-hacking.com/hacks/auto-dojo-adaptive-ipi-task-specification.md/)
- [LlamaFirewall: An open source guardrail system（arXiv）](https://arxiv.org/html/2505.03574)
- [PromptArmor: Simple yet Effective Prompt Injection Defenses（arXiv）](https://arxiv.org/html/2507.15219)
- [Reading the Zscaler ThreatLabz Numbers as an Inline-Enforcement Problem](https://www.deepinspect.ai/blog/enterprise-ai-data-exposure-zscaler-2026-threat-report)
- [Orca Security：2026 State of AI Security Report](https://orca.security/wp-content/uploads/2026/07/2026-State-of-AI-Security-Report.pdf)
- [OrcaRouter Releases AI Threat Report 2026](https://kakacomputer.com/orcarouter-releases-ai-threat-report-2026-and-makes-its-security-controls-free-amid-rise-in-prompt-injection-attacks/)