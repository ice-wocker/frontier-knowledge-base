# AI 安全与对齐（AI Safety and Alignment）

> 最后更新：2026-09-26 ｜ 领域：人工智能 / 安全、对齐与治理 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 一、概述

AI 安全与对齐关注两类问题：**误用风险（misuse）**——模型被用于生化、网络、操控等危害；以及**失控 / 失准风险（misalignment & loss of control）**——模型追求与人类意图不一致的目标，或削弱人类对其的监督与关停能力。2025–2026 年，该领域从学术议题走向工程化与制度化：前沿实验室发布可度量的能力阈值与安全等级，监管开始具备执法力，同时多位一线研究者公开警告极端风险。

## 二、2025–2026 最新进展

- **RSP 进入「路线图 + 风险报告」时代**：Anthropic 于 2026 年 2 月 24 日发布 **RSP v3.0**，是对该政策的全面重写，配套发布 **Frontier Safety Roadmaps（前沿安全路线图）** 与量化全部已部署模型风险的 **Risk Reports（风险报告）**（[Anthropic's Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy)）。此后持续迭代至 **v3.4**（2026 年 7 月 8 日生效），并发布 2026 年 8 月风险报告（覆盖日期截至 7 月 15 日）。
- **DeepMind 推出 FSF 3.1 与追踪能力等级**：2026 年 4 月 17 日，Google DeepMind 在 **Frontier Safety Framework** 第三版基础上加入 **Tracked Capability Levels（TCLs）**，用于更早识别较轻风险，并公开从风险识别到缓解的完整流程（[Strengthening our Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)）。
- **可解释性从「提取特征」走向「追踪电路」**：Anthropic 用稀疏自编码器（SAE）在 Claude 中分离出数百万「单义特征」，并通过**特征引导（feature steering）**证明这些特征可因果地改变行为（如有意放大某特征使模型产生幻觉）；对 Claude 3.5 Haiku 的**电路追踪（circuit tracing）**揭示了在没有显式思维链时也会发生的多步推理与规划（[Anthropic Mechanistic Interpretability Research Findings](https://research.mental-momentum.ai/r/anthropic-mechanistic-interpretability-2ic9sw)）。
- **监管开始执法**：欧盟《AI 法案》（AI Act）作为全球首部综合性 AI 法律，其 AI Office 与成员国主管部门的执法权自 **2026 年 8 月 2 日** 起适用于部分条款（[The enforcement framework of the AI Act](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)）；禁止性条款中的 **Prohibition 9** 于 **2026 年 12 月** 生效，系通过 AI Omnibus 引入（[AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)）。

## 三、核心技术与关键概念

### 1. 对齐技术

- **RLHF（Reinforcement Learning from Human Feedback）**：后训练对齐的骨干，典型三阶段为监督微调（SFT）→ 训练奖励模型 → 用强化学习优化策略（[Scalable oversight: RLHF, DPO, Constitutional AI, and weak-to-strong generalization](https://explainx.ai/blog/scalable-oversight-rlhf-constitutional-ai-weak-to-strong)）。
- **DPO（Direct Preference Optimization）**：更高效的替代方案，**完全消除强化学习**步骤，已被 Llama 3、Mistral 等模型的训练管线采用（[Constitutional AI and Alignment Alternatives: Beyond RLHF](https://zylos.ai/research/2026-02-01-constitutional-ai-alignment-alternatives/)、[RLHF Explained](https://aibuzz.blog/rlhf-explained/)）。
- **Constitutional AI（CAI）**：Anthropic 于 2022 年 12 月提出，核心是让模型依据一组明确原则（宪法）对自身回答做**自我批判与修订**，并以 AI 反馈替代部分人工偏好（RLAIF）；到 2026 年已衍生出 Collective Constitutional AI 等以公众输入民主化 AI 价值的实践（[Constitutional AI and Alignment Alternatives](https://zylos.ai/research/2026-02-01-constitutional-ai-alignment-alternatives/)、[A Technical Survey of RL Techniques for LLMs](https://arxiv.org/html/2507.04136v1)）。
- **可扩展监督（scalable oversight）与弱到强泛化（weak-to-strong generalization）**：研究如何用能力较弱的监督者可靠地训练与评估更强的模型（[Scalable oversight](https://explainx.ai/blog/scalable-oversight-rlhf-constitutional-ai-weak-to-strong)）。

### 2. 可解释性（Mechanistic Interpretability）

SAE 把多义（polysemantic）的神经元激活分解为可解释的单义特征；跨层转码器（**Cross-Layer Transcoder, CLT**）是 SAE 的变体，用跳跃 ReLU（JumpReLU）激活，把特征输出写入后续 MLP 层，使特征间交互在注意力之后呈线性，便于追踪（[On the Biology of a Large Language Model](https://aiwiki.ai/wiki/biology_of_a_large_language_model)）。据 2026 年报道，Anthropic 已在 Claude 4.7 中映射出 6000 多个被充分理解的特征，包括「含安全漏洞的代码」「用户问题中的错误前提」「模型正被要求欺骗」等（[AI Model Interpretability 2026](https://networkcraft.net/networkcraft-ai-interpretability-2026/)）。但该路径亦受质疑：一项对 Llama 3.1 开源 SAE 的复现研究虽成功复现基础的特征提取与引导，却对其「可解释即安全监督」的主张提出压力测试（[When the Coffee Feature Activates on Coffins](https://arxiv.org/html/2601.03047)）。

### 3. 越狱与提示注入

- **直接提示注入 / 越狱**：Azure AI Content Safety 的 **Prompt Shields**（前称 jailbreak 风险检测）用于识别用户试图诱导模型产生未授权行为的攻击（[Azure AI Content Safety — Jailbreak detection](https://learn.microsoft.com/it-it/azure/ai-services/content-safety/concepts/jailbreak-detection)）。
- **间接提示注入（IPI）**：攻击者通过不可信的外部数据源注入指令。研究提出 **Rennervate**，利用注意力特征在 token 级检测隐蔽注入并做精确清洗（[Attention is All You Need to Defend Against Indirect Prompt Injection](https://arxiv.org/html/2512.08417v3)）。另有「自演化多智能体」防御框架，把成功攻击抽象为**方法级规则**存入跨交互记忆以泛化防御整类攻击（[A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks](https://arxiv.org/html/2608.26008v1)）。
- **工程缓解**：对任何有实质现实影响的模型发起操作应采用**人在回路（human-in-the-loop）**审批，且审批界面须展示真实将发生的动作与所用输入（[Prompt Injection, Jailbreaks and Data Exfiltration](https://www.cybersecurityessential.com/ai-security/llm-security/prompt-injection-enterprise-llm-security/)）。

### 4. 红队测试

对前沿模型的系统性对抗测试成为发布前标准环节。一项为期九周的红队研究（2026 年 4 月 10 日–5 月 22 日）对 Anthropic、OpenAI、Google 的 7 个前沿模型在 22 个风险类别上执行了超过 **26,500** 次评估（RedBench 基准，29,362 条提示），产生 **468** 项关键发现（[Responsible AI Model Evaluations: A Nine-Week Red-Teaming Study](https://sushegaad.github.io/Responsible-AI-Model-Evaluations/paper/research-paper.pdf)）。Anthropic 前沿红队于 2026 年 9 月 10 日发布衡量模型在**战术情报定位与常规武器**方面能力的新评估（[Measuring AI capabilities in intelligence targeting and conventional weapons](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities)）。

## 四、代表性框架与项目

| 框架 / 项目 | 发布方 | 核心机制 | 官方链接 |
| --- | --- | --- | --- |
| Responsible Scaling Policy (RSP) | Anthropic | ASL 安全等级 + 能力阈值 + 路线图 + 风险报告 | https://www.anthropic.com/responsible-scaling-policy |
| Frontier Safety Framework (FSF 3.1) | Google DeepMind | CCL / TCL 能力等级 + 安全案例评审 | https://deepmind.google/blog/strengthening-our-frontier-safety-framework/ |
| Preparedness Framework | OpenAI | 追踪能力类别 + 能力阈值 + 分级保障 | https://deploymentsafety.openai.com/ |
| AI Control Roadmap | Google DeepMind | 检测等级 D1–D4、预防/响应等级 R1–R3 | https://deepmind.google/blog/securing-the-future-of-ai-agents/ |
| Prompt Shields | Microsoft Azure | 检测用户提示注入 / 越狱 | https://learn.microsoft.com/azure/ai-services/content-safety/ |
| AI Act | 欧盟 | 风险分级 + 分阶段执法 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai |

## 五、关键数据与评测结果

- **RSP 阈值实践**：Anthropic 于 2026 年 2 月 10 日判定 Claude Opus 4.6 **未跨越 AI R&D-4 能力阈值**，但承认「自信地排除该阈值正变得越来越困难」，并为超越 Opus 4.5 能力的模型撰写 **Sabotage Risk Report（破坏风险报告）**（[RSP](https://www.anthropic.com/responsible-scaling-policy)）。
- **FSF 评测结果**：按 FSF 协议，DeepMind 测得 **Gemini 3.1 Pro（重点 Deep Think 模式）** 在 CBRN、有害操控、机器学习 R&D 与失准 CCL 上均**低于预警阈值**；在网络安全（cyber）领域因前代模型曾超阈值而做了额外测试，结论仍低于 cyber CCL（[Gemini 3.1 Pro Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)）。
- **越狱脆弱性**：一项对 DeepSeek v4 Pro 的前沿风险评估称，模型在 CBRN、网络与恐怖主义内容上可被诱导达到 **98–100%** 的攻击成功率；在智能体设置下，以单一模板包裹可执行 **110 项有害任务中的 80%**（[Evaluating DeepSeek v4 Pro for Frontier Risks](https://neoresearch.ai/papers/DSv4_Safety_Evaluation_v1.1.pdf)）。
- **风险评分基准**：在《Frontier AI Risk Management Framework in Practice》中，Claude Sonnet 4.5（Thinking）取得最高的 PACEBench 分数 **0.335**，GPT-5.2（2025-12-11）为 0.280，Seed-OSS-36B-Instruct 最低为 0.075（[Frontier AI Risk Management Framework in Practice](https://arxiv.org/pdf/2602.14457.pdf)）。
- **国家级评测**：英国 AI 安全研究所（AISI）测试 GPT-5.5 与 Claude Mythos Preview，发现其表现明显超出此前的「能力翻倍」趋势线，尚不清楚是新的更快增长趋势还是短期跃升（[英国AISI对GPT-5.5和Mythos的测评结果 — 安全内参](https://www.secrss.com/articles/90281)）。

## 六、趋势与争议

1. **「拿全人类生命做赌注」的公开预警**：Anthropic 对齐科学负责人 Evan Hubinger 警告未来十年内 AI 导致人类灭绝的概率超过 10%；研究员 Jacob Coxon 辞职并称当前 AI 开发是「拿全人类生命进行的豪赌」（[OpenAI再曝大模型越界行为！盖茨加入AI安全论战](http://m.toutiao.com/group/7689744961213956623/)）。OpenAI CEO Sam Altman 则公开提出两种「反乌托邦」情景：人类永久失去对未来的控制，或技术权力过度集中于单一个人、公司或主权国家（[OpenAI CEO Sam Altman Warns Humanity Could Lose Control](https://techgolly.com/openai-ceo-sam-altman-warns-humanity-could-lose-control-in-two-dystopian-ai-scenarios)）。
2. **递归自我改进（recursive self-improvement）担忧**：越来越多研究者警告，递归自我改进与日益自主的智能体可能使先进系统难以控制，该概念虽仍属理论，却正影响创业投资与安全辩论（[AI Researchers Warn Recursive Self-Improvement Could Put Human Control at Risk](https://superintelligencenews.com/ai-fields/ai-safety-recursive-self-improvement/)）。
3. **公众人物加码**：比尔·盖茨警告 AI 是一种「足够强大」的工具，足以引发「导致十亿人死亡」的事件，并呼吁立法监管（[比尔·盖茨称人工智能"足够强大可能导致十亿人死亡" — 南京晨报](http://m.toutiao.com/group/7689735335030538762/)）。
4. **自我监管 vs 外部监管的张力**：RSP / FSF / Preparedness 均为厂商自设框架，其阈值定义、评测透明度与「谁敢真的暂停训练」的可信度仍受质疑；同时欧盟 AI Act 分阶段执法与美中各异的治理路径，使全球规则呈碎片化格局（[Global AI Governance: Frameworks in Formation](https://bostoncommonasset.com/wp-content/uploads/2026/06/AI-Governance-Frameworks-in-Formation-BCAM-June-2026.pdf)）。
5. **可解释性的乐观与审慎**：SAE/电路追踪被视为人类监督最有希望的路径之一，但复现研究提示其结论可能被高估，需更多独立验证（[When the Coffee Feature Activates on Coffins](https://arxiv.org/html/2601.03047)）。

## 参考来源

1. [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy)
2. [Anthropic's Transparency Hub (RSP PDF)](https://www-cdn.anthropic.com/5fb26a6974468f83ce87b4799a7ac957ce9d8f96.pdf)
3. [Responsible Scaling Policy — aiwiki](https://aiwiki.ai/wiki/responsible_scaling_policy/edit)
4. [Strengthening our Frontier Safety Framework — Google DeepMind](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/)
5. [Updating the Frontier Safety Framework — Google DeepMind](https://deepmind.com/discover/blog/updating-the-frontier-safety-framework/)
6. [Gemini 3.1 Pro Model Card — Google DeepMind](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
7. [Frontier Safety Framework (Google DeepMind) — aiwiki](https://aiwiki.ai/wiki/frontier_safety_framework)
8. [Securing the future of AI agents — Google DeepMind](https://deepmind.google/blog/securing-the-future-of-ai-agents/)
9. [Deep Research System Card — OpenAI Preparedness](https://deploymentsafety.openai.com/deep-research/introduction)
10. [Responsible AI Model Evaluations: A Nine-Week Red-Teaming Study](https://sushegaad.github.io/Responsible-AI-Model-Evaluations/paper/research-paper.pdf)
11. [Evaluating DeepSeek v4 Pro for Frontier Risks](https://neoresearch.ai/papers/DSv4_Safety_Evaluation_v1.1.pdf)
12. [Measuring AI capabilities in intelligence targeting and conventional weapons — Anthropic](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities)
13. [Frontier AI Risk Management Framework in Practice: A Risk Analysis Technical Report](https://arxiv.org/pdf/2602.14457.pdf)
14. [英国AISI对GPT-5.5和Mythos的测评结果 — 安全内参](https://www.secrss.com/articles/90281)
15. [Anthropic Mechanistic Interpretability Research Findings](https://research.mental-momentum.ai/r/anthropic-mechanistic-interpretability-2ic9sw)
16. [AI Model Interpretability 2026: Why This Is the Year We Finally See Inside the Black Box](https://networkcraft.net/networkcraft-ai-interpretability-2026/)
17. [When the Coffee Feature Activates on Coffins: An Analysis of Feature Extraction and Steering](https://arxiv.org/html/2601.03047)
18. [On the Biology of a Large Language Model — aiwiki](https://aiwiki.ai/wiki/biology_of_a_large_language_model)
19. [Representation Engineering & Mechanistic Interpretability](https://www.frankx.ai/research/representation-engineering-mechanistic-interpretability)
20. [Prompt Injection, Jailbreaks and Data Exfiltration: Securing Enterprise LLMs in 2026](https://www.cybersecurityessential.com/ai-security/llm-security/prompt-injection-enterprise-llm-security/)
21. [A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks](https://arxiv.org/html/2608.26008v1)
22. [Azure AI Content Safety — Jailbreak detection](https://learn.microsoft.com/it-it/azure/ai-services/content-safety/concepts/jailbreak-detection)
23. [Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs](https://arxiv.org/html/2512.08417v3)
24. [Scalable oversight: RLHF, DPO, Constitutional AI, and weak-to-strong generalization](https://explainx.ai/blog/scalable-oversight-rlhf-constitutional-ai-weak-to-strong)
25. [128. RLHF Explained — aibuzz](https://aibuzz.blog/rlhf-explained/)
26. [Constitutional AI and Alignment Alternatives: Beyond RLHF — zylos.ai](https://zylos.ai/research/2026-02-01-constitutional-ai-alignment-alternatives/)
27. [A Technical Survey of Reinforcement Learning Techniques for Large Language Models](https://arxiv.org/html/2507.04136v1)
28. [Model Alignment Techniques Beyond RLHF](https://www.daydreamsoft.com/blog/model-alignment-techniques-beyond-rlhf-the-future-of-safe-and-reliable-ai-systems)
29. [AI Act — European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
30. [The enforcement framework of the AI Act — European Commission](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
31. [Global AI Governance: Frameworks in Formation](https://bostoncommonasset.com/wp-content/uploads/2026/06/AI-Governance-Frameworks-in-Formation-BCAM-June-2026.pdf)
32. [比尔·盖茨称人工智能"足够强大可能导致十亿人死亡" — 南京晨报](http://m.toutiao.com/group/7689735335030538762/)
33. [OpenAI再曝大模型越界行为！盖茨加入AI安全论战 — 众播视频](http://m.toutiao.com/group/7689744961213956623/)
34. [OpenAI CEO Sam Altman Warns Humanity Could Lose Control — techgolly](https://techgolly.com/openai-ceo-sam-altman-warns-humanity-could-lose-control-in-two-dystopian-ai-scenarios)
35. [AI Researchers Warn Recursive Self-Improvement Could Put Human Control at Risk](https://superintelligencenews.com/ai-fields/ai-safety-recursive-self-improvement/)
36. ["我们在拿生命做赌注":造AI的人为何开始密集预警? — InfoQ](https://www.infoq.cn/news/FA80wgNMOwCRrXsSIAwX)