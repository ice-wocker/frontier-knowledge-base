# 强化学习前沿

> 最后更新：2026-09-26 ｜ 领域：AI·前沿方向与风险 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

强化学习（Reinforcement Learning, RL）在 2025–2026 年重新成为大模型与具身智能的核心方法。最显著的变化是从「人类反馈强化学习」（RLHF）转向「可验证奖励强化学习」（RLVR，Reinforcement Learning with Verifiable Rewards）：在高难度数学或代码问题上，人类很难给出精准反馈，而 RLVR 用可自动验证的信号（如单元测试、标准答案）提供奖励（[双极进化与算力重构：2026 AI 行业深度展望（海外篇）](https://www.cdut.edu.cn/__local/0/04/B2/0A8B3667284C14584754964C019_491C571F_30ED92.pdf)）。RLVR 的流程可概括为「采样一个回答—验证—更新」三步，但其短板在于验证器几乎从不清净：单元测试只覆盖有限边界用例，人类与合成标签不完美，LLM judge（如 RLAIF）存在噪声且可被利用，这一在代码等更难领域尤为突出（[Rate or Fate? RLVεR: Reinforcement Learning with Verifiable Noisy Rewards](https://arxiv.org/pdf/2601.04411)）。

与此同时，世界模型（World Model）驱动的 RL、离线 RL 与多智能体/机器人 RL 也出现密集进展。

## 最新进展（2025–2026）

### RLVR 与 LLM 推理

DeepSeek-R1 是这一路线的标志性成果：它通过大规模 RL 后训练，在数学、代码与推理任务上达到与 OpenAI-o1 相当的水平，且标注数据需求极低，并以 MIT 许可开放模型权重（[DeepSeek-R1 Release](https://www.deepseek.com/en/news/deepseek-r1/)）。其技术报告指出，DeepSeek-R1-Zero 完全依靠 RL 自然涌现出多种推理行为，但存在可读性差、语言混用等问题；DeepSeek-R1 因此引入多阶段训练与冷启动数据，推理表现与 OpenAI-o1-1217 相当（[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948?categoryid=2849204&discountcode=CX19S)）。2025 年 5 月的 R1 更新中，AIME 2025 准确率由旧版 70% 提升至 87.5%，每题平均消耗 token 从 12K 增至 23K，显示推理深度增强（[DeepSeek-R1 更新，思考更深，推理更强](https://api-docs.deepseek.com/zh-cn/news/news250528/)）。

主流优化算法为 GRPO（Group Relative Policy Optimization），已被用于 DeepSeek-V3 与 R1 系列（[Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification](https://arxiv.org/html/2503.06639v1)）。也有研究尝试把可验证奖励从数学、代码扩展到更多领域，用模型充当验证器并由此定义二值或软奖励函数（[Crossing the Reward Bridge: Expanding RL with Verifiable Rewards Across Diverse Domains](https://arxiv.org/pdf/2503.23829.pdf)）。但 GRPO 式优化仍易出现崩溃，有研究从 token 级梯度动力学出发给出不稳定性分类，并提出只更新「赢家优势」的 WAPO 目标（[A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization](https://arxiv.org/pdf/2606.16154v1)）。

### 世界模型与想象式 RL

世界模型 RL 分为两支：一类学习隐空间压缩状态（Dreamer、MuZero、DayDreamer），样本效率极高但不可直接观看；另一类直接生成视频或 3D 场景（Genie 3、Sora、Cosmos、Marble），视觉效果强但难以检查（[World Models: The AI That Learned to Dream Before It Could Walk](https://dev.to/abdullahbinaqeel/world-models-the-ai-that-learned-to-dream-before-it-could-walk-3kam)）。Google DeepMind 的 Genie 3（2025 年 8 月）可由单条文本提示生成可交互、可导航的 3D 环境，达 24 fps，并能保持数分钟一致性（[World Models 讲义](https://dl4ds.github.io/sp2026/static_files/lectures/25_world_models.pdf)、[参考资料](https://world-models.io/llms.txt)）；Dreamer 4（2025 年 9 月）则展示了仅用离线数据解决 Minecraft 钻石任务的能力（[World Models 讲义](https://dl4ds.github.io/sp2026/static_files/lectures/25_world_models.pdf)）。据行业报道，NVIDIA 于 2026 年 2 月推出 DreamDojo/DreamZero，在 44,711 小时人类第一视角视频上预训练，经 Self Forcing 蒸馏后达到实时运行，并以与真实结果皮尔逊相关系数 r=0.995 评估机器人策略（[集大成者：DreamDojoDreamZero](http://dzb.cinn.cn/shtml/zggyb/20210324/vA3.shtml)）。

### 离线 RL 与真实机器人

真实世界 RL 的一大痛点是探索阶段的失败代价。FARL（Failure-Aware Offline-to-Online RL）引入基于世界模型的安全 critic 与离线恢复策略，并配套 FailureBench 基准，减少在线探索中的失败（[Failure-Aware RL: Reliable Offline-to-Online Reinforcement Learning with Self-Recovery for Real-World Manipulation](https://arxiv.org/html/2601.07821)）。将离线 RL 与跨本体（cross-embodiment）学习结合，可聚合不同形态机器人的异构轨迹以获取通用控制先验（[Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets](https://arxiv.org/html/2602.18025v1/)）。把不确定性与机器人世界模型结合，已能在 ANYmal D 与 Unitree G1 上离线训练并部署四足/人形运动策略（[Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots](https://arxiv.org/html/2504.16680v2)）。ROMBRL 提出「策略驱动的世界模型自适应」，用于鲁棒离线基于模型的 RL，相关工作在 ICML 2026 以海报形式发表（[ROMBRL — Policy-Driven World Model Adaptation for Robust Offline Model-based RL (ICML 2026)](https://agentic-intelligence-lab.org/2026/08/04/rombrl-post.html)）。Robo-ValueRL 则聚焦离线到在线 RL 中的可靠价值估计，并系统追踪其下游影响（[Robo-ValueRL: Reliable Value Estimation for Offline-to-Online Reinforcement Learning](https://www.semanticscholar.org/paper/Robo-ValueRL:-Reliable-Value-Estimation-for-Xia-Ren/9499b698bd2d53b119864cb75481b49844f768bb)）。

### 多智能体与机器人 RL

面向 LLM 多智能体系统的 RL 训练成为热点。MarsRL 通过 agentic 流水线并行与 agent 专属奖励，将 AIME2025 准确率从 86.5% 提升至 93.3%（[MarsRL: Advancing Multi-Agent Reasoning System via Reinforcement Learning with Agentic Pipeline Parallelism](https://arxiv.org/pdf/2511.11373)）；Dr. MAS 指出跨 agent 共享全局优势基线会放大梯度二阶矩并导致梯度爆炸，主张每个 agent 用自身均值方差归一化（[Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems](https://arxiv.org/html/2602.08847v1)）；MAGRPO 将 LLM 协作建模为合作型 MARL 问题（[LLM Collaboration with Multi-Agent Reinforcement Learning](https://arxiv.org/html/2508.04652v3/)）。在机器人侧，PPO 仍是人形运动控制主力：有工作用选择性 AMP（Adversarial Motion Prior）让单一人形机器人掌握走路、正步、跑步、爬梯、跳跃五种步态（[Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior](https://arxiv.org/html/2604.19102)），也有用 Mamba 编码器的端到端 RL 框架 HuMam（[HuMam: Humanoid Motion Control via End-to-End Deep Reinforcement Learning with Mamba](https://arxiv.org/html/2509.18046v2)）。Berkeley 团队的「Real-world humanoid locomotion with reinforcement learning」把控制问题形式化为 MDP，并用 RL 求解最优策略（[Real-world humanoid locomotion with reinforcement learning](https://people.eecs.berkeley.edu/~ilija/papers/scirobotics.adi9579.pdf)）；另有工作用双层优化实现自动奖励学习，让 DRL 在策略学习过程中自适应构造与优化奖励函数（[Deep Reinforcement Learning for Real-World Humanoid Robot Locomotion Control with Automatic Reward Learning](https://spj.science.org/doi/10.34133/research.1123?__cf_chl_f_tk=kjkJMLs8GK.Oe6oguyJpkgQlJR7_H.g2WTA5kWZGir0-1783326448-1.0.1.1-hc0V3kzEKLGTwLf3GTevK41EhOUtg7WFOrQena2Q8oQ)）。

## 核心技术与关键概念

- **RLVR**：以可验证信号替代人类偏好打分，主要适用于数学、代码等有客观答案的领域。
- **GRPO**：组内相对策略优化，无需价值网络，用同一 prompt 下多个采样结果的平均奖励作基线。
- **世界模型**：学习环境的压缩动力学或直接生成未来帧，用于想象式规划或策略评估。
- **离线 RL / offline-to-online**：先用已有数据集训练，再谨慎地在线微调，配合安全 critic 降低真实世界失败。
- **跨本体 RL**：聚合不同机器人形态的数据以获得通用控制先验。
- **多智能体 RL（MARL）**：把多 LLM 协作或协作机器人建模为合作博弈，难点在信用分配与训练稳定性。

## 代表性项目 / 公司 / 产品

- DeepSeek-R1 / R1-Zero / GRPO（DeepSeek）：开源推理模型与 RL 后训练范式（[DeepSeek-R1 Release](https://www.deepseek.com/en/news/deepseek-r1/)）。
- Genie 3（Google DeepMind）：交互式 3D 世界生成（[World Models 讲义](https://dl4ds.github.io/sp2026/static_files/lectures/25_world_models.pdf)）。
- Dreamer 4（Hafner 等）：离线数据下的想象式 RL（[World Models 讲义](https://dl4ds.github.io/sp2026/static_files/lectures/25_world_models.pdf)）。
- FARL / FailureBench、Uncertainty-Aware Robotic World Model：面向真实机器人的离线 MBRL（[FARL](https://arxiv.org/html/2601.07821)、[Uncertainty-Aware](https://arxiv.org/html/2504.16680v2)）。
- MarsRL、Dr. MAS、MAGRPO：多智能体 LLM 的 RL 训练框架（[MarsRL](https://arxiv.org/pdf/2511.11373)、[Dr. MAS](https://arxiv.org/html/2602.08847v1)、[MAGRPO](https://arxiv.org/html/2508.04652v3/)）。

## 关键数据与评测结果

| 事项 | 数据 | 来源 |
| --- | --- | --- |
| DeepSeek-R1 AIME 2025 准确率（2025-05 更新） | 70% → 87.5% | [DeepSeek API Docs](https://api-docs.deepseek.com/zh-cn/news/news250528/) |
| R1 每题平均 token | 12K → 23K | [DeepSeek API Docs](https://api-docs.deepseek.com/zh-cn/news/news250528/) |
| Genie 3 交互帧率 | 24 fps，一致性可达数分钟 | [World Models 讲义](https://dl4ds.github.io/sp2026/static_files/lectures/25_world_models.pdf) |
| MarsRL AIME2025 | 86.5% → 93.3% | [MarsRL](https://arxiv.org/pdf/2511.11373) |
| MarsRL BeyondAIME | 64.9% → 73.x% | [MarsRL](https://arxiv.org/pdf/2511.11373) |
| DreamDojo 策略评估相关性 | 与真实结果 r=0.995 | [中国工业新闻网电子报](http://dzb.cinn.cn/shtml/zggyb/20210324/vA3.shtml) |

## 趋势与争议

1. **验证器质量成为瓶颈**：RLVR 的扩张受限于奖励噪声，在困难领域尤甚（[RLVεR](https://arxiv.org/pdf/2601.04411)）。
2. **训练稳定性**：GRPO 式目标存在崩溃风险，学术界从梯度动力学、优势基线等角度提出改进（[WAPO](https://arxiv.org/pdf/2606.16154v1)、[Dr. MAS](https://arxiv.org/html/2602.08847v1)）。
3. **世界模型路线分歧**：隐空间模型样本高效却不可视，生成式世界模型可视却难验证（[World Models](https://dev.to/abdullahbinaqeel/world-models-the-ai-that-learned-to-dream-before-it-could-walk-3kam)）。
4. **真实世界探索仍有风险**：安全性 critic、恢复策略与不确定性惩罚等方案各自降低但未消除失败（[FARL](https://arxiv.org/html/2601.07821)、[Uncertainty-Aware](https://arxiv.org/html/2504.16680v2)）。
5. **多智能体信用分配**：跨 agent 的奖励归一化方式直接决定训练是否稳定，尚无统一结论（[Dr. MAS](https://arxiv.org/html/2602.08847v1)）。

## 参考来源

- [双极进化与算力重构：2026 AI 行业深度展望（海外篇）](https://www.cdut.edu.cn/__local/0/04/B2/0A8B3667284C14584754964C019_491C571F_30ED92.pdf)
- [Rate or Fate? RLVεR: Reinforcement Learning with Verifiable Noisy Rewards](https://arxiv.org/pdf/2601.04411)
- [DeepSeek-R1 Release](https://www.deepseek.com/en/news/deepseek-r1/)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948?categoryid=2849204&discountcode=CX19S)
- [DeepSeek-R1 更新，思考更深，推理更强 | DeepSeek API Docs](https://api-docs.deepseek.com/zh-cn/news/news250528/)
- [Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification](https://arxiv.org/html/2503.06639v1)
- [A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization](https://arxiv.org/pdf/2606.16154v1)
- [World Models: The AI That Learned to Dream Before It Could Walk](https://dev.to/abdullahbinaqeel/world-models-the-ai-that-learned-to-dream-before-it-could-walk-3kam)
- [World Models 讲义](https://dl4ds.github.io/sp2026/static_files/lectures/25_world_models.pdf)
- [参考资料（world-models.io）](https://world-models.io/llms.txt)
- [中国工业新闻网电子报：DreamDojoDreamZero](http://dzb.cinn.cn/shtml/zggyb/20210324/vA3.shtml)
- [Failure-Aware RL: Reliable Offline-to-Online Reinforcement Learning with Self-Recovery for Real-World Manipulation](https://arxiv.org/html/2601.07821)
- [Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets](https://arxiv.org/html/2602.18025v1/)
- [Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots](https://arxiv.org/html/2504.16680v2)
- [MarsRL: Advancing Multi-Agent Reasoning System via Reinforcement Learning with Agentic Pipeline Parallelism](https://arxiv.org/pdf/2511.11373)
- [Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems](https://arxiv.org/html/2602.08847v1)
- [LLM Collaboration with Multi-Agent Reinforcement Learning (MAGRPO)](https://arxiv.org/html/2508.04652v3/)
- [Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior](https://arxiv.org/html/2604.19102)
- [HuMam: Humanoid Motion Control via End-to-End Deep Reinforcement Learning with Mamba](https://arxiv.org/html/2509.18046v2)
- [Crossing the Reward Bridge: Expanding RL with Verifiable Rewards Across Diverse Domains](https://arxiv.org/pdf/2503.23829.pdf)
- [ROMBRL — Policy-Driven World Model Adaptation for Robust Offline Model-based RL (ICML 2026)](https://agentic-intelligence-lab.org/2026/08/04/rombrl-post.html)
- [Robo-ValueRL: Reliable Value Estimation for Offline-to-Online Reinforcement Learning](https://www.semanticscholar.org/paper/Robo-ValueRL:-Reliable-Value-Estimation-for-Xia-Ren/9499b698bd2d53b119864cb75481b49844f768bb)
- [Real-world humanoid locomotion with reinforcement learning](https://people.eecs.berkeley.edu/~ilija/papers/scirobotics.adi9579.pdf)
- [Deep Reinforcement Learning for Real-World Humanoid Robot Locomotion Control with Automatic Reward Learning](https://spj.science.org/doi/10.34133/research.1123?__cf_chl_f_tk=kjkJMLs8GK.Oe6oguyJpkgQlJR7_H.g2WTA5kWZGir0-1783326448-1.0.1.1-hc0V3kzEKLGTwLf3GTevK41EhOUtg7WFOrQena2Q8oQ)