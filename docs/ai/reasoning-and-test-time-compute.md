# 推理模型与测试时计算（Test-Time Compute）

> 最后更新：2026-09-26 ｜ 领域：人工智能·推理模型 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

推理模型（reasoning model）与测试时计算（test-time compute，TTS）是 2024 年以来的核心范式转变：模型不再"一次性作答"，而是在给出最终答案前生成一段可见或隐藏的长链推理（chain of thought），并允许通过增加推理时的算力来换取更高的正确率。OpenAI 在 2024 年 9 月推出 o1，用大规模强化学习训练模型生成"长的内部思维链"（[Aprender a razonar con los LLM](https://openai.com/es-ES/index/learning-to-reason-with-llms/)），开启了这一路线。到 2026 年，思考能力已成为前沿旗舰的标准配置，并进一步演化为"可控推理深度"与"自适应推理"两条工程化主线。

## 2025–2026 最新进展

**OpenAI o 系列到 GPT-5/6 的延续。** 2025 年 4 月 16 日发布的 o3 与 o4-mini 系统卡显示，两者把推理与完整工具链（浏览、Python、图像与文件分析、图像生成、记忆等）结合，并首次让模型"在思维链中使用工具"来增强能力（[OpenAI o3 and o4-mini System Card](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)）。o3 在 ARC-AGI 上以高算力配置取得 87.5%，AIME 2025 取得 88.9%，GPQA Diamond 取得 87.7%（[Understanding and Benchmarking Artificial Intelligence: OpenAI's o3 Is Not AGI](https://arxiv.org/html/2501.07458v1/)、[OpenAI o3](https://aiwiki.ai/wiki/o3/edit)）。此后 GPT-5 系列与 GPT-6 Astra 均默认内置思考模式，并支持 effort 档位（[Claude vs ChatGPT vs Gemini](https://genai.club/blog/claude-vs-chatgpt-vs-gemini)）。

**DeepSeek-R1 与开源复现浪潮。** DeepSeek 于 2025 年初发布 R1 技术报告，证明可以仅用强化学习（无需人工监督推理轨迹）激励出长链推理行为（[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948)）。其发布后 100 天内催生大量复现研究（[100 Days After DeepSeek-R1: A Survey on Replication Studies](https://arxiv.org/html/2505.00551v1/)）。2025 年 12 月 1 日，DeepSeek V3.2-Speciale 在 IMO 2025、CMO 2025、ICPC World Finals 2025、IOI 2025 上均达金牌水平，被官方描述为"对标 Gemini-3.0-Pro"（[DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://www.deepseek.com/en/news/deepseek-v3-2/)）。

**Claude 的 extended/adaptive thinking。** Anthropic 在 Claude 4.7 时代以"Extended Thinking"参与推理竞争（[AI Reasoning Models Compared May 2026](https://www.web3aiblog.com/blog/ai-reasoning-models-compared-o3-claude-thinking-gemini-deep-think-deepseek-r1-may-2026)），并在后续新模型中把思考升级为默认开启的"自适应思考"，用 `effort` 参数控制思考深度，Claude Sonnet 5 的默认 effort 为 high（[Claude Sonnet 5 - Claude Platform Docs](https://platform.claude.com/docs/ru/models/sonnet-5/overview)）。

**Gemini Deep Think。** Google 把最强推理做成独立的 Deep Think 模式：Gemini 3.1 Deep Think 在 ARC-AGI-2 上达到 84.6%（经 ARC Prize 验证）、HLE 无工具 48.4%（[Gemini 3.1 Deep Think](https://deepmind.google/models/gemini/deep-think/)）。该模式被划分为数分钟级的"深推理档"，延迟 1–15 分钟，成本约为标准输出率的 3–5 倍（[Gemini 3.1 Pro Review](https://localaimaster.com/models/gemini-3-1-pro)）。

**Qwen 与 GLM 的推理开关。** Qwen 的推理模型提供两种模式：hybrid（按请求用 `enable_thinking` 开关思考）与 thinking-only（始终推理），输出以 `reasoning_content` 或 `reasoning_text` 返回（[Thinking](https://docs.qwencloud.com/developer-guides/text-generation/thinking)）。GLM 家族中 glm-5.3 为 thinking-only，glm-5.2/5.1/5/4.7/4.6 为默认开启思考的 hybrid（[Deep thinking](https://www.alibabacloud.com/help/en/model-studio/deep-thinking)）。

## 核心技术与关键概念

- **思维链（CoT）与长链推理**：让模型在作答前展开中间步骤；推理模型进一步把 CoT 拉长到数千乃至上万 token，并通过 RL 训练其"更有效的思考"。
- **RL / RLVR（Reinforcement Learning with Verifiable Rewards）**：用可自动判定的奖励（如数学答案对错）替代人工偏好，被称为 R1 之后的核心范式（[Reinforcement Learning with Verifiable Rewards for Small Search Agents](https://arxiv.org/html/2609.28765v1)）。
- **GRPO 与 DAPO 等算法**：GRPO 放弃与策略同规模的 critic，改用组内得分估计基线，显著节省 RL 成本（[DeepSeek-R1 技术报告](https://arxiv.org/pdf/2501.12948)）；后续出现 DAPO、GSPO 等改进（[Rewards as Labels: Revisiting RLVR from a Classification Perspective](https://arxiv.org/html/2602.05630)）。
- **过程奖励模型（PRM）**：相较只看最终答案的结果监督（ORM），过程监督对每个推理步骤单独打分，在 MATH 上显著更优，代表工作为 2023 年的《Let's Verify Step by Step》（arXiv:2305.20050，ICLR 2024）（[Process reward model (PRM)](https://aiwiki.ai/wiki/process_reward_model)、[Let's Verify Step by Step](https://papers.lunadong.com/paper/4718)）。
- **测试时扩展的两种形态**：平行扩展（采样多份候选用投票或验证器聚合）与顺序扩展（沿单一轨迹延长思考），以及二者的混合（[What, How, Where, and How Well? A Survey on Test-Time Scaling](https://arxiv.org/pdf/2503.24235v2)）。
- **budget forcing 与 s1**：通过强制模型"再想想"并控制思考 token 预算，实现可控的测试时扩展，在 AIME24 上取得最佳成绩（[s1: Simple test-time scaling](https://arxiv.org/pdf/2501.19393)）。
- **蒸馏**：把大模型的推理能力注入小模型，如 DeepSeek-R1-Distill-Qwen-1.5B/7B；也有推理时蒸馏以在无微调下节约成本（[Rewards as Labels](https://arxiv.org/html/2602.05630)、[Inference-Time Distillation](https://arxiv.org/html/2512.02543v2)）。

## 代表性项目/产品（带官方链接）

- OpenAI o3 / o4-mini 系统卡：https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf
- DeepSeek-R1 技术报告：https://arxiv.org/pdf/2501.12948
- Gemini 3.1 Deep Think：https://deepmind.google/models/gemini/deep-think/
- Claude 推理（effort / adaptive thinking）：https://platform.claude.com/docs/ru/models/sonnet-5/overview
- Qwen Thinking 开发文档：https://docs.qwencloud.com/developer-guides/text-generation/thinking
- GLM / Kimi 思考模式：https://www.alibabacloud.com/help/en/model-studio/deep-thinking
- s1: Simple test-time scaling：https://arxiv.org/pdf/2501.19393

## 关键数据与评测结果

- **o3**：ARC-AGI 高算力 87.5%，AIME 2025 88.9%，GPQA Diamond 87.7%（[OpenAI o3](https://aiwiki.ai/wiki/o3/edit)）；低算力半私有集 76%、高算力 88%（[OpenAI's O3: Features, O1 Comparison, Benchmarks](https://www.datacamp.com/pl/blog/o3-openai)）。
- **Gemini 3.1 Deep Think**：ARC-AGI-2 84.6%，HLE（无工具）48.4%（[Gemini 3.1 Deep Think](https://deepmind.google/models/gemini/deep-think/)）。
- **DeepSeek V3.2-Speciale**：IMO/CMO/ICPC/IOI 2025 金牌（[DeepSeek-V3.2](https://www.deepseek.com/en/news/deepseek-v3-2/)）。
- **错误的直觉：更多算力未必更好。** 一项对 beam search 扩展的研究发现，GPT-OSS-120B、Qwen3-32B 等长思维模型在扩大 beam 宽度后准确率不升反降，出现"逆算力扩展（inverse compute scaling）"（[The Art of Scaling Test-Time Compute for Large Language Models](https://arxiv.org/html/2512.02008)）。
- **多智能体推理的计算效率**：对 self-consistency、self-refinement、multi-agent debate、mixture-of-agents 的系统分析显示，不同 TTS 策略在 MMLU-Pro、BBH 上的"性能—算力"权衡差异显著，需按预算选择（[Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/html/2605.01566v1)）。

## 趋势与争议

**成本与延迟的权衡成为焦点。** 思考 token 按输出计费，属于"昂贵"的那一类——2026 年 7 月前沿输出价约 $25–30/百万 token，而输入约 $5/百万；一个难题可能消耗 1 万以上不可见推理 token，且成本分布有厚尾，99 分位查询的成本可达中位数的 100 倍（[Thinking Tokens: How Test-Time Compute Rewrote the AI Scaling Playbook](https://codelint.dev/blog/test-time-compute-reasoning-models)）。由此催生了 per-request 思考预算上限、effort 档位等控制手段。

**自适应推理深度。** 2025 年末至 2026 年一季度，CogRouter（2026 年 2 月）、ARES（2026 年 3 月）等方法证明，逐步动态调整推理深度的 agent 可在保持 SOTA 任务表现的同时减少 50–62% 的 token 消耗（[Adaptive Reasoning Depth in AI Agent Systems](https://zylos.ai/research/2026-04-13-adaptive-reasoning-depth-ai-agent-systems/)）。

**评测可复现性争议。** 有研究指出，"test-time scaling"一词覆盖了沿单轨迹延长、采样后投票/验证、部分状态搜索等结构截然不同的算法，若只报准确率而不说明推理协议、或把它们笼统归为"预算"，结果难以跨研究比较（[Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](https://www.alphaxiv.org/abs/2608.04001)）。此外，"蒸馏/压缩推理"方向（如 CRISP 最多减少 56% 推理长度同时提升准确率）也在挑战"越长越强"的假设（[CRISP: Compressed Reasoning via Iterative Self-Policy Distillation](https://www.alphaxiv.org/overview/2603.05433)）。

## 参考来源

1. [Aprender a razonar con los LLM](https://openai.com/es-ES/index/learning-to-reason-with-llms/)
2. [OpenAI o3 and o4-mini System Card](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)
3. [Understanding and Benchmarking Artificial Intelligence: OpenAI's o3 Is Not AGI](https://arxiv.org/html/2501.07458v1/)
4. [OpenAI o3](https://aiwiki.ai/wiki/o3/edit)
5. [OpenAI's O3: Features, O1 Comparison, Benchmarks & More](https://www.datacamp.com/pl/blog/o3-openai)
6. [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948)
7. [100 Days After DeepSeek-R1: A Survey on Replication Studies](https://arxiv.org/html/2505.00551v1/)
8. [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://www.deepseek.com/en/news/deepseek-v3-2/)
9. [AI Reasoning Models Compared May 2026](https://www.web3aiblog.com/blog/ai-reasoning-models-compared-o3-claude-thinking-gemini-deep-think-deepseek-r1-may-2026)
10. [Claude Sonnet 5 - Claude Platform Docs](https://platform.claude.com/docs/ru/models/sonnet-5/overview)
11. [Gemini 3.1 Deep Think](https://deepmind.google/models/gemini/deep-think/)
12. [Gemini 3.1 Pro Review](https://localaimaster.com/models/gemini-3-1-pro)
13. [Thinking](https://docs.qwencloud.com/developer-guides/text-generation/thinking)
14. [Deep thinking](https://www.alibabacloud.com/help/en/model-studio/deep-thinking)
15. [Reinforcement Learning with Verifiable Rewards for Small Search Agents](https://arxiv.org/html/2609.28765v1)
16. [Rewards as Labels: Revisiting RLVR from a Classification Perspective](https://arxiv.org/html/2602.05630)
17. [Process reward model (PRM)](https://aiwiki.ai/wiki/process_reward_model)
18. [Let's Verify Step by Step](https://papers.lunadong.com/paper/4718)
19. [What, How, Where, and How Well? A Survey on Test-Time Scaling](https://arxiv.org/pdf/2503.24235v2)
20. [s1: Simple test-time scaling](https://arxiv.org/pdf/2501.19393)
21. [Inference-Time Distillation](https://arxiv.org/html/2512.02543v2)
22. [The Art of Scaling Test-Time Compute for Large Language Models](https://arxiv.org/html/2512.02008)
23. [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/html/2605.01566v1)
24. [Thinking Tokens: How Test-Time Compute Rewrote the AI Scaling Playbook](https://codelint.dev/blog/test-time-compute-reasoning-models)
25. [Adaptive Reasoning Depth in AI Agent Systems](https://zylos.ai/research/2026-04-13-adaptive-reasoning-depth-ai-agent-systems/)
26. [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](https://www.alphaxiv.org/abs/2608.04001)
27. [CRISP: Compressed Reasoning via Iterative Self-Policy Distillation](https://www.alphaxiv.org/overview/2603.05433)
28. [Claude vs ChatGPT vs Gemini](https://genai.club/blog/claude-vs-chatgpt-vs-gemini)