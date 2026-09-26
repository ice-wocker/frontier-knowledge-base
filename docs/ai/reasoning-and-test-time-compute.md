# 推理模型与测试时计算（Test-Time Compute）

> 最后更新：2026-09-26 ｜ 领域：人工智能·推理模型 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

推理模型（reasoning model）与测试时计算（test-time compute，TTS）是 2024 年以来的核心范式转变：模型不再「一次性作答」，而是在给出最终答案前生成一段可见或隐藏的长链推理（chain of thought），并允许通过增加推理时的算力来换取更高的正确率。OpenAI 在 2024 年 9 月推出 o1，用大规模强化学习训练模型生成「长的内部思维链」（[Aprender a razonar con los LLM](https://openai.com/es-ES/index/learning-to-reason-with-llms/)），开启了这一路线。

到 2026 年，思考能力已成为前沿旗舰的标准配置——OpenAI 的 GPT-5 于 2025 年 8 月发布时即被描述为「内置了思考能力」，并明确其面向所有人可用（[GPT-5 正式发布](https://openai.com/zh-Hans-CN/gpt-5/)）。这一范式进一步演化为两条工程化主线：一是「可控推理深度」，即用 effort 档位或 token 预算显式约束思考量；二是「自适应推理」，即由模型按任务难度动态决定思考多少。围绕这两条主线，评测、成本控制、训练算法（RLVR/GRPO 及其变体）与失败模式研究共同构成了 2025–2026 年的技术图景。

从系统角度看，测试时计算把「推理算力」从训练阶段部分解耦出来：训练时的规模定律回答「用多少算力训练」，测试时的扩展则回答「在单次推理中投入多少算力、以何种结构投入」。其直接后果是，同一个模型可通过对齐思考预算在「快速廉价」与「深思昂贵」之间连续滑动，而推理成本更多随任务难度而非请求数量变化。也正因如此，成本控制、延迟管理与评测口径成为 2026 年产品化落地的核心议题。

## 2025–2026 最新进展

**OpenAI o 系列到 GPT-5/6 的延续。** 2025 年 4 月 16 日发布的 o3 与 o4-mini 系统卡显示，两者把推理与完整工具链（浏览、Python、图像与文件分析、图像生成、记忆等）结合，并首次让模型「在思维链中使用工具」来增强能力（[OpenAI o3 and o4-mini System Card](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)）。o3 在 ARC-AGI 上以高算力配置取得 87.5%，AIME 2025 取得 88.9%，GPQA Diamond 取得 87.7%（[Understanding and Benchmarking Artificial Intelligence: OpenAI's o3 Is Not AGI](https://arxiv.org/html/2501.07458v1/)、[OpenAI o3](https://aiwiki.ai/wiki/o3/edit)）。2025 年 8 月，OpenAI 发布 GPT-5，内置思考能力（[GPT-5 正式发布](https://openai.com/zh-Hans-CN/gpt-5/)）；此后 GPT-5 系列与 GPT-6 Astra 均默认内置思考模式并支持 effort 档位（[Claude vs ChatGPT vs Gemini](https://genai.club/blog/claude-vs-chatgpt-vs-gemini)）。有分析指出，GPT-5.2 的 Thinking 模式在 agentic 编程任务（规划、执行、调试、验证）上表现突出，被视为「真正的结对程序员」（[Strategic Analysis of Frontier AI Models: GPT-5.2 vs. Gemini 3](https://ironcrestsoftware.com/assets/pdfs/ai-model-comparison-chatgpt-vs-gemini.pdf)）。

**DeepSeek-R1 与开源复现浪潮。** DeepSeek 于 2025 年初发布 R1 技术报告，证明可以仅用强化学习（无需人工监督推理轨迹）激励出长链推理行为（[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948)）。其发布后 100 天内催生大量复现研究（[100 Days After DeepSeek-R1: A Survey on Replication Studies](https://arxiv.org/html/2505.00551v1/)）。2025 年 12 月 1 日，DeepSeek V3.2-Speciale 在 IMO 2025、CMO 2025、ICPC World Finals 2025、IOI 2025 上均达金牌水平，被官方描述为「对标 Gemini-3.0-Pro」（[DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://www.deepseek.com/en/news/deepseek-v3-2/)）。开源阵营中，Kimi K3 等模型参数规模已达万亿级（[DeepSeek-V3.2 (Thinking) vs Kimi K3](https://llm-stats.com/models/compare/deepseek-reasoner-vs-kimi-k3)），Kimi-K2-Thinking 等推理模型在 MMLU、SWE-bench、MATH-500 上接近专有 SOTA（[Best Open Source LLMs in 2026](https://www.respan.ai/blog/best-open-source-llms)）。

**Claude 的 extended / adaptive thinking。** Anthropic 在 Claude 4.7 时代以「Extended Thinking」参与推理竞争（[AI Reasoning Models Compared May 2026](https://www.web3aiblog.com/blog/ai-reasoning-models-compared-o3-claude-thinking-gemini-deep-think-deepseek-r1-may-2026)），并在后续新模型中把思考升级为默认开启的「自适应思考」，用 `effort` 参数控制思考深度，Claude Sonnet 5 的默认 effort 为 high（[Claude Sonnet 5 - Claude Platform Docs](https://platform.claude.com/docs/ru/models/sonnet-5/overview)）。以 Claude Opus 4.6 为例，自适应思考意味着模型评估每个任务后决定投入多少推理，可用 low、medium、high、max 等级别微调「智能—速度—成本」的权衡，简单查询快速响应、复杂问题充分思考（[Anthropic Claude Opus 4.6: Is the Upgrade Worth It?](https://www.codecademy.com/article/anthropic-claude-opus-4-6)）。该 `effort` 参数被放在 `output_config` 对象中（而非 `thinking` 内），并接受 low、medium、high、xhigh 等取值（[Adaptive thinking](https://aiwiki.ai/wiki/adaptive_thinking)）。

**Gemini Deep Think。** Google 把最强推理做成独立的 Deep Think 模式：Gemini 3.1 Deep Think 在 ARC-AGI-2 上达到 84.6%（经 ARC Prize 验证）、HLE 无工具 48.4%（[Gemini 3.1 Deep Think](https://deepmind.google/models/gemini/deep-think/)）。该模式被划分为数分钟级的「深推理档」，延迟 1–15 分钟，成本约为标准输出率的 3–5 倍（[Gemini 3.1 Pro Review](https://localaimaster.com/models/gemini-3-1-pro)）。

**Qwen 与 GLM 的推理开关。** Qwen 的推理模型提供两种模式：hybrid（按请求用 `enable_thinking` 开关思考）与 thinking-only（始终推理），输出以 `reasoning_content` 或 `reasoning_text` 返回（[Thinking](https://docs.qwencloud.com/developer-guides/text-generation/thinking)）。GLM 家族中 glm-5.3 为 thinking-only，glm-5.2/5.1/5/4.7/4.6 为默认开启思考的 hybrid（[Deep thinking](https://www.alibabacloud.com/help/en/model-studio/deep-thinking)）。

**测试时扩展被系统化梳理。** 一项针对 test-time scaling 的综述从「扩展什么、如何扩展、在哪里扩展、效果如何」四个维度对该领域做了梳理，并把主流做法归纳为平行扩展（采样多份候选用投票或验证器聚合）、顺序扩展（沿单一轨迹延长思考）以及二者的混合（[What, How, Where, and How Well? A Survey on Test-Time Scaling](https://arxiv.org/pdf/2503.24235v2)）。在此基础上，s1 以 budget forcing 强制模型「再想想」并控制思考 token 预算，实现可控的测试时扩展，在 AIME24 上取得当时最佳成绩（[s1: Simple test-time scaling](https://arxiv.org/pdf/2501.19393)）。这些工作共同把「思考多少、怎么思考」从经验技巧变成可参数化的工程问题。

**多智能体推理与算力效率。** 对 self-consistency、self-refinement、multi-agent debate、mixture-of-agents 等策略的系统比较显示，不同测试时计算策略在 MMLU-Pro、BBH 等基准上的「性能—算力」帕累托前沿差异显著，应按预算选择最优策略而非默认使用最强配置（[Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/html/2605.01566v1)）。这说明「多智能体」并非总能换来更好的性价比，其收益高度依赖任务结构与预算区间。

**开源推理模型加速追赶。** 2026 年，开源权重的推理模型已在多个推理基准上接近专有前沿：例如 DeepSeek v3.2 在 SWE-Bench Verified 达 73.1%，MiniMax-M2.5 达 80.2%、GPQA-Diamond 85.2%，Kimi K2 Thinking 为 71.3%/85.7%，Kimi K2.5 为 76.8%/87.6%（[Best Open Source LLMs of May 2026](https://fireworks.ai/blog/best-open-source-llms-may-2026)）。与此同时，有研究发现 SWE-Bench 排名并不能预测某些真实软件工程任务的表现，说明单一基准的排序能力有限（[React-ing to Grace Hopper 200](https://arxiv.org/html/2604.17187)）。

**RL 训练算法的持续演进。** RLVR（Reinforcement Learning with Verifiable Rewards，以可自动判定的奖励训练）成为 R1 之后的主导范式，但研究开始系统揭示其奖励噪声问题：验证器（verifier）几乎从不「干净」——单元测试只探测有限边界情况，人类与合成标签并不完美，LLM judge（如 RLAIF）既有噪声又可能被利用，且这一问题在更难领域（尤其编程）更严重（[Rate or Fate? RLVR: Reinforcement Learning with Verifiable Noisy Rewards](https://arxiv.org/pdf/2601.04411v1)）。与此同时，对 GRPO 的理论分析不断深入：IBM 的研究证明，对可验证奖励做均值+方差校准会在损失中诱导出一个对比损失，其对比样本来自旧策略生成的合成数据（[RLVR: GRPO's Loss, Dynamics, and Success Amplification](https://research.ibm.com/publications/reinforcement-learning-with-verifiable-rewards-grpos-loss-dynamics-and-success-amplification)）；另有工作给出理论证明，GRPO 会隐式激励基座模型产生正确推理（[RLVR Implicitly Incentivizes Correct Reasoning in Base LLMs](https://arxiv.org/pdf/2506.14245v1.pdf)）。在此之上出现了多种改进：Off-Context GRPO 使用含特权指导的 rollout，但以重要性校正的目标把更新拉回原始无指导目标，避免未校正的引导训练失稳（[Off-Context GRPO](https://arxiv.org/html/2607.19313v1)）；SciencePRM 则在科学领域用过程级奖励到科学有效性的多个奖励层级来训练（[SciencePRM](https://cs224r.stanford.edu/projects/pdfs/Zijian%20(Carl)%20Ma%20submission_416288476/cs224r_final_report_2026.pdf)）。

## 核心技术与关键概念

- **思维链（CoT）与长链推理**：让模型在作答前展开中间步骤；推理模型进一步把 CoT 拉长到数千乃至上万 token，并通过 RL 训练其「更有效的思考」。
- **RL / RLVR（Reinforcement Learning with Verifiable Rewards）**：用可自动判定的奖励（如数学答案对错）替代人工偏好，被称为 R1 之后的核心范式（[Reinforcement Learning with Verifiable Rewards for Small Search Agents](https://arxiv.org/html/2609.28765v1)）。其关键局限是验证器本身存在噪声与可被利用的风险（[Rate or Fate?](https://arxiv.org/pdf/2601.04411v1)）。
- **GRPO 与 DAPO/GSPO 等算法**：GRPO 放弃与策略同规模的 critic，改用组内得分估计基线，显著节省 RL 成本（[DeepSeek-R1 技术报告](https://arxiv.org/pdf/2501.12948)）；后续出现 DAPO、GSPO 等改进（[Rewards as Labels: Revisiting RLVR from a Classification Perspective](https://arxiv.org/html/2602.05630)）。
- **过程奖励模型（PRM）**：相较只看最终答案的结果监督（ORM），过程监督对每个推理步骤单独打分，在 MATH 上显著更优，代表工作为 2023 年的《Let's Verify Step by Step》（arXiv:2305.20050，ICLR 2024）（[Process reward model (PRM)](https://aiwiki.ai/wiki/process_reward_model)、[Let's Verify Step by Step](https://papers.lunadong.com/paper/4718)）。
- **测试时扩展的两种形态**：平行扩展（采样多份候选用投票或验证器聚合）与顺序扩展（沿单一轨迹延长思考），以及二者的混合（[What, How, Where, and How Well? A Survey on Test-Time Scaling](https://arxiv.org/pdf/2503.24235v2)）。
- **budget forcing 与 s1**：通过强制模型「再想想」并控制思考 token 预算，实现可控的测试时扩展，在 AIME24 上取得最佳成绩（[s1: Simple test-time scaling](https://arxiv.org/pdf/2501.19393)）。
- **effort 档位 / 自适应思考**：用 low/medium/high/xhigh/max 等档位显式控制思考深度，或由模型按任务自行决定，是 2026 年产品化的主流控制手段（[Adaptive thinking](https://aiwiki.ai/wiki/adaptive_thinking)、[Anthropic Claude Opus 4.6](https://www.codecademy.com/article/anthropic-claude-opus-4-6)）。
- **蒸馏**：把大模型的推理能力注入小模型，如 DeepSeek-R1-Distill-Qwen-1.5B/7B；也有推理时蒸馏以在无微调下节约成本（[Rewards as Labels](https://arxiv.org/html/2602.05630)、[Inference-Time Distillation](https://arxiv.org/html/2512.02543v2)）。
- **自适应推理的预算分配**：把自适应推理建模为「不确定性下的计算投资」，预算应跟随推理的期望回报，而非仅凭感知难度决定（[Nice Fold or Hero Call: Learning Budget-Efficient Thinking for Adaptive Reasoning](https://arxiv.org/html/2605.11625)）。
- **验证器（verifier）与自一致性（self-consistency）**：平行扩展依赖对多份候选的聚合，既可用多数投票，也可用学得的验证器或过程奖励模型打分；验证器的质量直接决定聚合收益的上限，这也是 RLVR 噪声问题与测试时聚合问题的交汇点（[Rate or Fate?](https://arxiv.org/pdf/2601.04411v1)、[What, How, Where, and How Well?](https://arxiv.org/pdf/2503.24235v2)）。
- **部分状态搜索**：除「重采样候选」与「延长单轨迹」外，还可在部分推理状态上做搜索（search over partial states），其算法结构与前两者截然不同；若评测中不区分这些推理协议，结果将难以跨研究比较（[Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](https://www.alphaxiv.org/abs/2608.04001)）。
- **长链推理与压缩推理**：显式 CoT 会增加输出 token 与延迟，压缩/蒸馏方向的研究尝试在「减少推理长度」的同时保持甚至提升准确率（如 CRISP 最多减少 56% 推理长度），对「越长越强」的直觉提出挑战（[CRISP](https://www.alphaxiv.org/overview/2603.05433)）。
- **思考模式的开关与混合**：部分模型（Qwen、GLM）在同一权重上支持「按请求开启/关闭思考」的 hybrid 模式与「始终思考」的 thinking-only 模式，使同一模型可同时服务低延迟与高难度场景（[Thinking](https://docs.qwencloud.com/developer-guides/text-generation/thinking)、[Deep thinking](https://www.alibabacloud.com/help/en/model-studio/deep-thinking)）。
- **推理与工具 / agent 的结合**：o3 与 o4-mini 首次让模型在思维链中使用工具（浏览、Python 等），把「思考」与「行动」交织在一起，是推理模型与 agent 系统融合的重要标志，也为后续「边推理边调用工具」的 agent 产品奠定范式（[OpenAI o3 and o4-mini System Card](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)）。

## 代表性项目 / 产品（附官方链接）

- OpenAI o3 / o4-mini 系统卡：https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf
- OpenAI GPT-5（内置思考）：https://openai.com/zh-Hans-CN/gpt-5/
- DeepSeek-R1 技术报告：https://arxiv.org/pdf/2501.12948
- DeepSeek-V3.2：https://www.deepseek.com/en/news/deepseek-v3-2/
- Gemini 3.1 Deep Think：https://deepmind.google/models/gemini/deep-think/
- Claude 推理（effort / adaptive thinking）：https://platform.claude.com/docs/ru/models/sonnet-5/overview
- Qwen Thinking 开发文档：https://docs.qwencloud.com/developer-guides/text-generation/thinking
- GLM / Kimi 思考模式：https://www.alibabacloud.com/help/en/model-studio/deep-thinking
- s1: Simple test-time scaling：https://arxiv.org/pdf/2501.19393

## 关键数据与评测结果

- **o3**：ARC-AGI 高算力 87.5%，AIME 2025 88.9%，GPQA Diamond 87.7%（[OpenAI o3](https://aiwiki.ai/wiki/o3/edit)）；低算力半私有集 76%、高算力 88%（[OpenAI's O3: Features, O1 Comparison, Benchmarks](https://www.datacamp.com/pl/blog/o3-openai)）。
- **Gemini 3.1 Deep Think**：ARC-AGI-2 84.6%，HLE（无工具）48.4%（[Gemini 3.1 Deep Think](https://deepmind.google/models/gemini/deep-think/)）。
- **DeepSeek V3.2-Speciale**：IMO/CMO/ICPC/IOI 2025 金牌（[DeepSeek-V3.2](https://www.deepseek.com/en/news/deepseek-v3-2/)）。
- **开源推理模型**：Kimi-K2-Thinking 在 MMLU 93.1%、SWE-bench 89.7%、MATH-500 97.2%、IFEval 88.0%，被用于与「专有 SOTA」（94.5%/92.0%/98.1%/93.0%）对比，差距已在个位数百分点（[Best Open Source LLMs in 2026](https://www.respan.ai/blog/best-open-source-llms)）。
- **错误的直觉：更多算力未必更好。** 一项对 beam search 扩展的研究发现，GPT-OSS-120B、Qwen3-32B 等长思维模型在扩大 beam 宽度后准确率不升反降，出现「逆算力扩展（inverse compute scaling）」（[The Art of Scaling Test-Time Compute for Large Language Models](https://arxiv.org/html/2512.02008)）。
- **多智能体推理的计算效率**：对 self-consistency、self-refinement、multi-agent debate、mixture-of-agents 的系统分析显示，不同 TTS 策略在 MMLU-Pro、BBH 上的「性能—算力」权衡差异显著，需按预算选择（[Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/html/2605.01566v1)）。
- **成本参考**：Anthropic 的部分前沿模型具备 1M token 上下文、最高 128K 输出，输入/输出价分别为每百万 token 10 美元与 50 美元，缓存读取 0.25 美元（[Anthropic - promptfoo docs](https://www.promptfoo.dev/docs/providers/anthropic/)）。

## 趋势与争议

**成本与延迟的权衡成为焦点。** 思考 token 按输出计费，属于「昂贵」的那一类——2026 年 7 月前沿输出价约 $25–30/百万 token，而输入约 $5/百万；一个难题可能消耗 1 万以上不可见推理 token，且成本分布有厚尾，99 分位查询的成本可达中位数的 100 倍（[Thinking Tokens: How Test-Time Compute Rewrote the AI Scaling Playbook](https://codelint.dev/blog/test-time-compute-reasoning-models)）。由此催生了 per-request 思考预算上限、effort 档位等控制手段，厂商也把「自适应思考」作为默认策略以减少对简单任务的过度推理（[Anthropic Claude Opus 4.6](https://www.codecademy.com/article/anthropic-claude-opus-4-6)）。

**自适应推理深度。** 2025 年末至 2026 年一季度，CogRouter（2026 年 2 月）、ARES（2026 年 3 月）等方法证明，逐步动态调整推理深度的 agent 可在保持 SOTA 任务表现的同时减少 50–62% 的 token 消耗（[Adaptive Reasoning Depth in AI Agent Systems](https://zylos.ai/research/2026-04-13-adaptive-reasoning-depth-ai-agent-systems/)）。

**评测可复现性争议。** 有研究指出，「test-time scaling」一词覆盖了沿单轨迹延长、采样后投票/验证、部分状态搜索等结构截然不同的算法，若只报准确率而不说明推理协议、或把它们笼统归为「预算」，结果难以跨研究比较（[Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](https://www.alphaxiv.org/abs/2608.04001)）。此外，「蒸馏/压缩推理」方向（如 CRISP 最多减少 56% 推理长度同时提升准确率）也在挑战「越长越强」的假设（[CRISP: Compressed Reasoning via Iterative Self-Policy Distillation](https://www.alphaxiv.org/overview/2603.05433)）。

**RLVR 的奖励噪声与可持续性。** 随着研究深入，可验证奖励的「不干净」被反复强调：验证器覆盖不足、标签不完美、LLM judge 可被利用，都会使训练信号偏离真实目标，且在编程等稀疏反馈领域尤为突出（[Rate or Fate?](https://arxiv.org/pdf/2601.04411v1)）。这使得「如何设计更稳健的奖励与验证器」成为 RLVR 之后的关键议题。

**预训练算力与测试时算力的权衡。** 既然正确率可随测试时算力提升，就自然出现「更小的模型 + 更多思考」与「更大的模型 + 更少思考」之间的取舍；前者在可验证、可分解的任务上往往更划算，但其收益受制于验证器质量与推理延迟，且并非普遍成立（[What, How, Where, and How Well?](https://arxiv.org/pdf/2503.24235v2)、[The Art of Scaling Test-Time Compute for Large Language Models](https://arxiv.org/html/2512.02008)）。多份研究同时提示，「更多算力不一定更好」，需按任务与预算做帕累托选择（[Multi-Agent Reasoning Improves Compute Efficiency](https://arxiv.org/html/2605.01566v1)）。

**思考内容是否可见、可监督。** 推理模型的产品化还带来「思考是否对用户隐藏」的问题：Qwen 等以 `reasoning_content`/`reasoning_text` 字段返回思考内容（[Thinking](https://docs.qwencloud.com/developer-guides/text-generation/thinking)），而部分产品仅展示思考摘要。这在可调试性、可监督性、成本透明与安全审计之间形成张力，也影响用户对模型结论的信任方式。

## 参考来源

1. [Aprender a razonar con los LLM](https://openai.com/es-ES/index/learning-to-reason-with-llms/)
2. [GPT-5 正式发布（OpenAI）](https://openai.com/zh-Hans-CN/gpt-5/)
3. [OpenAI o3 and o4-mini System Card](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)
4. [Understanding and Benchmarking Artificial Intelligence: OpenAI's o3 Is Not AGI](https://arxiv.org/html/2501.07458v1/)
5. [OpenAI o3](https://aiwiki.ai/wiki/o3/edit)
6. [OpenAI's O3: Features, O1 Comparison, Benchmarks & More](https://www.datacamp.com/pl/blog/o3-openai)
7. [Strategic Analysis of Frontier AI Models: GPT-5.2 vs. Gemini 3 (January 2026)](https://ironcrestsoftware.com/assets/pdfs/ai-model-comparison-chatgpt-vs-gemini.pdf)
8. [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948)
9. [100 Days After DeepSeek-R1: A Survey on Replication Studies](https://arxiv.org/html/2505.00551v1/)
10. [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://www.deepseek.com/en/news/deepseek-v3-2/)
11. [DeepSeek-V3.2 (Thinking) vs Kimi K3](https://llm-stats.com/models/compare/deepseek-reasoner-vs-kimi-k3)
12. [Best Open Source LLMs in 2026](https://www.respan.ai/blog/best-open-source-llms)
13. [AI Reasoning Models Compared May 2026](https://www.web3aiblog.com/blog/ai-reasoning-models-compared-o3-claude-thinking-gemini-deep-think-deepseek-r1-may-2026)
14. [Claude Sonnet 5 - Claude Platform Docs](https://platform.claude.com/docs/ru/models/sonnet-5/overview)
15. [Anthropic Claude Opus 4.6: Is the Upgrade Worth It?](https://www.codecademy.com/article/anthropic-claude-opus-4-6)
16. [Adaptive thinking](https://aiwiki.ai/wiki/adaptive_thinking)
17. [Gemini 3.1 Deep Think](https://deepmind.google/models/gemini/deep-think/)
18. [Gemini 3.1 Pro Review](https://localaimaster.com/models/gemini-3-1-pro)
19. [Thinking (Qwen)](https://docs.qwencloud.com/developer-guides/text-generation/thinking)
20. [Deep thinking (Model Studio)](https://www.alibabacloud.com/help/en/model-studio/deep-thinking)
21. [Rate or Fate? RLVR: Reinforcement Learning with Verifiable Noisy Rewards](https://arxiv.org/pdf/2601.04411v1)
22. [RLVR: GRPO's Loss, Dynamics, and Success Amplification (IBM)](https://research.ibm.com/publications/reinforcement-learning-with-verifiable-rewards-grpos-loss-dynamics-and-success-amplification)
23. [RLVR Implicitly Incentivizes Correct Reasoning in Base LLMs](https://arxiv.org/pdf/2506.14245v1.pdf)
24. [Off-Context GRPO: Learning to Reason on Hard Problems using Privileged Information](https://arxiv.org/html/2607.19313v1)
25. [SciencePRM](https://cs224r.stanford.edu/projects/pdfs/Zijian%20(Carl)%20Ma%20submission_416288476/cs224r_final_report_2026.pdf)
26. [Reinforcement Learning with Verifiable Rewards for Small Search Agents](https://arxiv.org/html/2609.28765v1)
27. [Rewards as Labels: Revisiting RLVR from a Classification Perspective](https://arxiv.org/html/2602.05630)
28. [Process reward model (PRM)](https://aiwiki.ai/wiki/process_reward_model)
29. [Let's Verify Step by Step](https://papers.lunadong.com/paper/4718)
30. [What, How, Where, and How Well? A Survey on Test-Time Scaling](https://arxiv.org/pdf/2503.24235v2)
31. [s1: Simple test-time scaling](https://arxiv.org/pdf/2501.19393)
32. [Inference-Time Distillation](https://arxiv.org/html/2512.02543v2)
33. [Nice Fold or Hero Call: Learning Budget-Efficient Thinking for Adaptive Reasoning](https://arxiv.org/html/2605.11625)
34. [The Art of Scaling Test-Time Compute for Large Language Models](https://arxiv.org/html/2512.02008)
35. [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](https://arxiv.org/html/2605.01566v1)
36. [Anthropic - promptfoo docs](https://www.promptfoo.dev/docs/providers/anthropic/)
37. [Thinking Tokens: How Test-Time Compute Rewrote the AI Scaling Playbook](https://codelint.dev/blog/test-time-compute-reasoning-models)
38. [Adaptive Reasoning Depth in AI Agent Systems](https://zylos.ai/research/2026-04-13-adaptive-reasoning-depth-ai-agent-systems/)
39. [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](https://www.alphaxiv.org/abs/2608.04001)
40. [CRISP: Compressed Reasoning via Iterative Self-Policy Distillation](https://www.alphaxiv.org/overview/2603.05433)
41. [Claude vs ChatGPT vs Gemini](https://genai.club/blog/claude-vs-chatgpt-vs-gemini)
42. [Best Open Source LLMs of May 2026](https://fireworks.ai/blog/best-open-source-llms-may-2026)
43. [React-ing to Grace Hopper 200](https://arxiv.org/html/2604.17187)