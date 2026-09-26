# 后训练与对齐方法

> 最后更新：2026-09-26 ｜ 领域：AI·基础原理 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

后训练（Post-training）指预训练之后、使模型具备指令遵循、偏好对齐与推理能力的一系列方法。一份 2025 年的后训练综述把 SFT、RLHF、DPO、GRPO 等技术放入统一脉络，指出 DPO（2023）通过直接依据人类偏好优化模型输出、绕过中间奖励建模来简化 RLHF，而 GRPO 最初是在其团队此前的 DeepSeekMath 工作中提出的（[A Survey on Post-training of Large Language Models](https://arxiv.org/html/2503.06072v3)）。经典 RLHF（Reinforcement Learning from Human Feedback）建立在对齐 LLM 与人类偏好的基础范式上，把模糊的伦理准则转化为可微的优化信号，通常包含监督微调（SFT）、奖励模型训练与强化学习优化三个阶段（[A Technical Survey of Reinforcement Learning Techniques for Large Language Models](https://arxiv.org/html/2507.04136)）。该框架是 InstructGPT 等指令遵循模型成功的关键（[Towards Efficient Online Exploration for RLHF](https://arxiv.org/pdf/2509.22633?)）。

## 最新进展（2025–2026）

2025–2026 年的重心从"对齐偏好"转向"训练推理"：

- **RLVR 与 GRPO**：可验证奖励强化学习（RLVR）让模型借助 SFT 与 RLVR 发展出强推理行为，且只需相对有限的监督数据；结合 cold-start 数据后，可在较低训练成本下达到此前模型的水平（[100 Days After DeepSeek-R1: A Survey on Replication Studies and More Directions for Reasoning Language Models](https://arxiv.org/html/2505.00551v1/)）。DeepSeek 官方称 DeepSeek-R1 在后训练阶段大规模使用强化学习，在仅有极少标注数据的情况下极大提升推理能力，在数学、代码、自然语言推理等任务上性能比肩 OpenAI o1 正式版（[DeepSeek-R1 发布，性能对标 OpenAI o1 正式版](https://api-docs.deepseek.com/zh-cn/news/news250120/)）。DeepSeek-R1 采用组相对策略优化（GRPO），省去与策略模型同规模的 critic 模型，改用一组输出的组内得分估计基线（[DeepSeek-R1](https://arxiv.org/pdf/2501.12948)）。可验证奖励（如数学答案正确性、代码通过单元测试）与格式奖励（如强制 ` thinking`、`<answer>` 标签）共同驱动长链式推理（[Sailing AI by the Stars: A Survey of Learning from Rewards](https://arxiv.org/html/2505.02686v1)）。
- **GRPO 的理论刻画**：有研究证明，带可验证奖励的 GRPO 可以写成一个 KL 正则化的对比损失（contrastive loss），其中对比项由同一 prompt 下成组采样得到的奖励差异构成（[Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification](https://arxiv.org/html/2503.06639v1)）。
- **拒绝采样的回归**：RAFT 等仅用正样本的拒绝采样基线，在早期训练阶段收敛更快，与 GRPO 的性能差距出人意料地小；但因其训练仅用正样本会导致策略熵迅速下降、限制探索，最终被 GRPO 超越（[A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce](https://arxiv.org/pdf/2504.11343.pdf)）。
- **Agentic RL 与更广的对齐视角**：一份综述梳理了面向 LLM 的 Agentic 强化学习图景，指出 DeepSeek 的成功带动了对 GRPO 的广泛研究，GRPO 通过组内评估范式缓解 PPO 大型 critic 的低效问题（[The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/pdf/2509.02547.pdf)）。另有综述把对齐扩展到文化、多模态与低延迟等维度，并把 DPO 描述为把 RLHF 对齐问题重构为分类任务、直接在人工排序答案的静态数据集上离线微调（[RLHF: A comprehensive Survey for Cultural, Multimodal and Low Latency Alignment Methods](https://arxiv.org/html/2511.03939)）。

## 核心技术与关键概念

### RLHF 三阶段

1. **SFT**：在人类示范数据上监督微调，得到基线指令模型（[A Technical Survey of RL Techniques for LLMs](https://arxiv.org/html/2507.04136)、[Towards Efficient Online Exploration for RLHF](https://arxiv.org/pdf/2509.22633?)）。
2. **奖励模型（Reward Model）**：基于成对偏好数据（Bradley-Terry 假设）训练，预测人类偏好（[Towards Efficient Online Exploration for RLHF](https://arxiv.org/pdf/2509.22633?)）。RLHF 将 MDP 扩展为包含成对偏好三元组 (p, y_A, y_B) 的数据（[Reinforcement Learning for Large Model: A Survey](https://arxiv.org/html/2508.08189v3)）。
3. **RL 优化**：以 RL 优化器（如 PPO）对模型采样并用奖励模型打分进行优化（[RLHF: A short introduction](https://simg.baai.ac.cn/paperfile/cdde5943-94af-4852-9187-361ead70a22b.pdf)）。

### 直接偏好优化家族（DPO/IPO/KTO/SimPO/ORPO）

DPO 类方法绕过显式奖励模型与 RL，直接在偏好数据上优化策略。DPO 把 RLHF 对齐问题重述为一个分类任务：在静态的人类排序答案集合上直接微调策略，把整个流程化为一次离线损失最小化（[RLHF: A comprehensive Survey for Cultural, Multimodal and Low Latency Alignment Methods](https://arxiv.org/html/2511.03939)）。2023–2024 年出现多个变体：

| 方法 | 作者/年份 | 核心创新 |
| --- | --- | --- |
| DPO | Rafailov 等 | 用偏好对直接优化，无需独立奖励模型 |
| IPO（Identity Preference Optimization） | Azar 等，2023 | 去掉 Bradley-Terry 假设，使用基于成对偏好概率的通用目标（ΨPO）；用平方损失替代 log-sigmoid，缓解 DPO 在确定性偏好下的过拟合 |
| KTO（Kahneman-Tversky Optimization） | Ethayarajh 等，ICML 2024 | 使用非成对的二元反馈（可取/不可取），基于前景理论 |
| SimPO（Simple Preference Optimization） | Meng 等，2024 | 目标为 −log σ(β·log πθ(yw,x) − β·log πθ(yl,x) − γ) |
| ORPO（Odds Ratio Preference Optimization） | Hong 等，2024 | 无参考模型的单体式偏好优化，在 SFT 损失上叠加 odds ratio 惩罚项，对不受青睐的生成风格施加小的惩罚即可实现对齐 |

前四行来自 [Direct Preference Optimization (DPO)](https://aiwiki.ai/wiki/direct_preference_optimization_dpo/edit)、[From RLHF to Direct Alignment: A Theoretical Unification](https://arxiv.org/pdf/2601.06108v1) 与 [The Differences Between Direct Alignment Algorithms are a Blur](https://arxiv.org/html/2502.01237v3)。ORPO 一行来自其原始论文，该文强调 SFT 本身在偏好对齐中的作用，认为对不受青睐的生成风格施加一个小的惩罚项即可，因而无需额外的偏好对齐阶段（[ORPO: Monolithic Preference Optimization without Reference Model](https://arxiv.org/pdf/2403.07691)）。

一项跨任务评测发现，标准对齐流程中 KTO 在除多任务理解外的所有任务上优于其他方法；各方法在推理任务上的表现则较为接近，说明无 RL 的算法对推理能力影响有限（[Insights into Alignment: Evaluating DPO and its Variants Across Multiple Tasks](https://arxiv.org/pdf/2404.14723v2)）。需注意该结论基于特定实验设置，尚不能推广为普适排序。

一份 2026 年的微调实践指南给出的选型建议是：有成对偏好数据、希望单次监督式训练且不引入奖励模型时用 DPO；需要显式奖励模型、在线采样与奖励塑形（通常用于安全关键的对齐）时，用带 PPO 的完整 RLHF；DPO 在 Hugging Face TRL 上更易实现、收敛更快，已成为多数微调栈中的默认偏好微调方法（[Fine-Tuning LLMs in 2026: LoRA, QLoRA, DPO, GRPO Compared](https://futureagi.com/blog/fine-tuning-llms-unlocking-peak-performance/)）。

### RLAIF

RLAIF（Reinforcement Learning from AI Feedback）在 Constitutional AI 中被提出，用 AI 生成的反馈替代人类对有害性的标注，以一套"宪法"原则指导自我批判与修订，使模型在人类与 AI 偏好的混合信号上学习无害行为（[Awesome LLM Post-training [2025 Update]](https://congchan.github.io/posts/awesome-large-language-model-llm-post-training-2025-update/)）。

### GRPO 与 RLVR

GRPO 对每个问题 q 采样一组输出 {o1, o2, …, oG}，用组内得分估计基线，从而省去 critic 模型、降低 RL 训练成本（[DeepSeek-R1](https://arxiv.org/pdf/2501.12948)）。在 DeepSeek 的实践中，推理数据使用基于规则的奖励，通用数据则使用奖励模型以捕捉人类偏好（[DeepSeek-R1 讲解](https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/ivanov_farhat_deepseek.pdf)）。

### 拒绝采样

拒绝采样（Rejection Sampling）从模型中为每个 prompt 采样 K 个输出，选取奖励最高的候选用于微调（[LLM 中的意图对齐](https://blog.csdn.net/weixin_46365033/article/details/144367905)）。实践上常用温度 0.7–1.0，每个 prompt 生成 10 至 30 个以上补全，补全过少会使训练有偏或噪声过大（[Rejection Sampling (RLHF Book)](https://rlhfbook.com/c/10-rejection-sampling)）。典型流程为：采样多个响应 → 用奖励模型打分 → 仅用高质量响应微调（[Xwin-LM: Strong and Scalable Alignment Practice for LLMs](https://arxiv.org/html/2405.20335v1)）。

## 关键数据与评测结果

- **GRPO 与 DPO 对 CoT 忠实性的影响**：一项评测比较 GRPO 与 DPO 提升链式思维（CoT）忠实性的能力，发现在更大模型上 GRPO 表现优于 DPO，Qwen2.5-14B-Instruct 在各评测指标上最好；两者都呈现"模型越大表现越好"的正相关，GRPO 提升的潜力更大（[Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs](https://arxiv.org/html/2512.22631)）。
- **对齐算法对内部特征几何的影响**：一项机制分析使用线性探针、稀疏自编码器与 crosscoder，发现不同目标以系统性不同的方式重塑内部特征几何：KTO 与 GRPO 倾向于通过建设性的特征共享与高显著特征的稀疏调用，增强偏好表示的可线性解码性；而 DPO 与 ORPO 常通过旋转与特征衰减等非建设性几何畸变降低可分性；PPO 与 SimPO 则大体保持可分性（[Mechanistic Analysis of Alignment Algorithms in Language Models](https://arxiv.org/pdf/2606.09850v1)）。
- **对齐税（alignment tax）**：一份 2026 年的实践总结指出，对齐后的模型常在推理类基准上损失约 10–20%，缓解手段包括回放缓冲区（replay buffer）与谨慎的数据混合（[Post-Training Playbook: SFT, LoRA, DPO, and GRPO from First Principles](https://gopikrishnatummala.com/posts/mlops/modern-post-training-peft-2026/)）。

## 趋势与争议

- **RL-free 对齐 vs RL 对齐**：DPO 系方法简单稳定、工程成本低，但在确定性偏好下可能过拟合、在推理任务上收益有限；RL/GRPO 系在推理与探索上更强，但训练更不稳定（[Insights into Alignment](https://arxiv.org/pdf/2404.14723v2)、[A Minimalist Approach to LLM Reasoning](https://arxiv.org/pdf/2504.11343.pdf)）。
- **可验证奖励的边界**：RLVR 依赖可自动判定的正确性信号，主要适用于数学、代码等域，难以直接迁移到开放式任务（[Sailing AI by the Stars](https://arxiv.org/html/2505.02686v1)）。
- **合成反馈的循环风险**：RLAIF 等 AI 反馈降低标注成本，但可能引入模型自身偏见（[Awesome LLM Post-training [2025 Update]](https://congchan.github.io/posts/awesome-large-language-model-llm-post-training-2025-update/)）。
- **对齐税与能力保持**：对齐信号在提升安全与偏好的同时可能损害推理表现，多来源数据指向约 10–20% 量级的下降，如何在对齐与能力之间取得平衡仍是开放问题（[Post-Training Playbook](https://gopikrishnatummala.com/posts/mlops/modern-post-training-peft-2026/)）。

## 参考来源

- [A Survey on Post-training of Large Language Models](https://arxiv.org/html/2503.06072v3)
- [A Technical Survey of Reinforcement Learning Techniques for Large Language Models](https://arxiv.org/html/2507.04136)
- [Towards Efficient Online Exploration for Reinforcement Learning with Human Feedback](https://arxiv.org/pdf/2509.22633?)
- [Reinforcement Learning for Large Model: A Survey](https://arxiv.org/html/2508.08189v3)
- [Reinforcement Learning from Human Feedback: A short introduction](https://simg.baai.ac.cn/paperfile/cdde5943-94af-4852-9187-361ead70a22b.pdf)
- [100 Days After DeepSeek-R1: A Survey on Replication Studies and More Directions for Reasoning Language Models](https://arxiv.org/html/2505.00551v1/)
- [DeepSeek-R1 发布，性能对标 OpenAI o1 正式版 | DeepSeek API Docs](https://api-docs.deepseek.com/zh-cn/news/news250120/)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948)
- [DeepSeek-R1 (CSC2541 presentation)](https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/ivanov_farhat_deepseek.pdf)
- [Sailing AI by the Stars: A Survey of Learning from Rewards](https://arxiv.org/html/2505.02686v1)
- [Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification](https://arxiv.org/html/2503.06639v1)
- [A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce](https://arxiv.org/pdf/2504.11343.pdf)
- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/pdf/2509.02547.pdf)
- [RLHF: A comprehensive Survey for Cultural, Multimodal and Low Latency Alignment Methods](https://arxiv.org/html/2511.03939)
- [Direct Preference Optimization (DPO)](https://aiwiki.ai/wiki/direct_preference_optimization_dpo/edit)
- [From RLHF to Direct Alignment: A Theoretical Unification of Preference Learning](https://arxiv.org/pdf/2601.06108v1)
- [The Differences Between Direct Alignment Algorithms are a Blur](https://arxiv.org/html/2502.01237v3)
- [ORPO: Monolithic Preference Optimization without Reference Model](https://arxiv.org/pdf/2403.07691)
- [Insights into Alignment: Evaluating DPO and its Variants Across Multiple Tasks](https://arxiv.org/pdf/2404.14723v2)
- [Fine-Tuning LLMs in 2026: LoRA, QLoRA, DPO, GRPO Compared](https://futureagi.com/blog/fine-tuning-llms-unlocking-peak-performance/)
- [Awesome Large Language Model (LLM) Post-training - [2025 Update]](https://congchan.github.io/posts/awesome-large-language-model-llm-post-training-2025-update/)
- [LLM 中的意图对齐](https://blog.csdn.net/weixin_46365033/article/details/144367905)
- [Rejection Sampling (RLHF Book)](https://rlhfbook.com/c/10-rejection-sampling)
- [Xwin-LM: Strong and Scalable Alignment Practice for LLMs](https://arxiv.org/html/2405.20335v1)
- [Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs](https://arxiv.org/html/2512.22631)
- [Mechanistic Analysis of Alignment Algorithms in Language Models](https://arxiv.org/pdf/2606.09850v1)
- [Post-Training Playbook: SFT, LoRA, DPO, and GRPO from First Principles](https://gopikrishnatummala.com/posts/mlops/modern-post-training-peft-2026/)