# 合成数据与数据引擎

> 最后更新：2026-09-26 ｜ 领域：AI·前沿方向与风险 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

合成数据（Synthetic Data）指由模型而非人工生成、用于训练的数据。据 2026 年的行业总结，合成数据已成为几乎所有专用模型的默认监督来源：Tülu、OpenHermes、Llama-3-Instruct 等开放权重指令模型高度依赖合成数据，定制的 reranker、分类器与 embedder 也以合成语料为主，根本原因是人工标注是瓶颈，而 LLM 能大规模生产（[Synthetic Data Generation](https://zeroentropy.dev/concepts/synthetic-data-generation/)）。生成 1 万条样本从数周缩短到数小时，使合成数据成为 2024–2025 年多数微调项目的默认起点；整个「生成—训练—评测—迭代」的实验循环因此大幅加速（[What Is Synthetic Training Data? Using LLMs to Train LLMs](https://ai-tldr.dev/learn/fine-tuning/distillation-and-tools/synthetic-training-data/)）。

## 最新进展（2025–2026）

### 从 Self-Instruct 到自验证蒸馏

基础方法为 Self-Instruct：从少量种子指令出发，让强模型生成相似的新指令与答案，把几条样例扩展为数千条指令—答案对；Evol-Instruct 进一步「进化」已有样例，使其更复杂、更深入（[Fine-Tuning with Synthetic Data: Self-Instruct, Distillation, and the Model Collapse Risk](https://sukruyusufkaya.com/en/blog/sentetik-veri-ile-fine-tuning-2026)）。

2026 年的新进展强调「自我验证」与质量过滤。Self-Verified Distillation 让模型对种子问题生成候选解，用基于提示的自验证过滤，并通过「循环一致性—事实性」等多阶段级联筛选，再用自筛选数据集训练（[Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline](https://arxiv.org/abs/2605.26132)）。通义 DeepResearch 技术报告则给出端到端合成数据方案：通过随机游走构建高度互联的知识图谱，生成复杂、高不确定性、超人类水平的问答对，全流程无需人工干预（[Tongyi DeepResearch Technical Report](https://arxiv.org/html/2510.24701v1)）。

### 模型崩塌与缓解

模型崩塌（Model Collapse）最早由 Shumailov 等（2024）提出，指模型在多代训练于自身生成输出后性能显著下降（[What happens when generative AI models train recursively on each others' outputs?](https://arxiv.org/html/2505.21677)）。2025–2026 年研究细化了机理：

- **多模态下的崩塌特性**：在 VLM 与扩散模型中，崩塌会表现为视觉—语言对齐改善、图像描述任务方差增大；增加解码预算、提升模型多样性、用冻结模型重标注可有效缓解（[Multimodal Synthetic Data Finetuning and Model Collapse](https://dl.acm.org/doi/pdf/10.1145/3716553.3750806)）。多模态崩塌的特性与单模态不同，说明崩塌现象在不同模态下机制存在差异（[Multimodal Synthetic Data Finetuning and Model Collapse](https://dl.acm.org/doi/pdf/10.1145/3716553.3750806)）。
- **泛化到记忆的转变**：在扩散模型的迭代训练中，崩塌伴随从泛化到记忆的转变，直接驱动因素是每轮合成数据熵的下降，据此可提出基于熵的数据选择策略（[A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective](https://arxiv.org/html/2509.16499v3)）。
- **过度自信是驱动因素**：ForTIFAI 认为模型对自生成数据的过度自信是崩塌关键，提出置信度感知的损失函数 Truncated Cross Entropy（TCE），显著延缓递归训练中的崩塌（[ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models](https://arxiv.org/html/2509.08972v2)）。
- **数据比例的量化界**：有研究从 Fisher-Rao 视角推导，指出防止崩塌所需的有效数据比例与既有结论不同，并给出随维度增大仍非平凡的收缩与不变性界（[Preventing Model Collapse when Training LLMs with Synthetic Data](https://www.semanticscholar.org/paper/Preventing-Model-Collapse-when-Training-LLMs-with-Gharesifard-Tabuada/4058e948c1a787739eff1ce3cf821ab364bca3d8)）。

### 合成数据用于低资源与多语言

激活引导也被用于合成数据生成：有工作以「某语言平均激活减去其他语言平均激活」构造 steering vector，隔离语言身份，用于低资源语言生成（[Want Better Synthetic Data? Steer It](https://arxiv.org/html/2606.18389)）。

### 数据飞轮与验证管线

自蒸馏加验证的核心是「生成—过滤—训练」闭环：模型先对种子问题生成候选解，再用基于提示的自验证与多阶段级联（如循环一致性、事实性）筛选，最后在自筛选数据集上训练（[Self-Verified Distillation](https://arxiv.org/abs/2605.26132)）。典型合成数据管线覆盖指令扩增、答案生成、质量过滤与去重等环节，以便把少量种子快速扩展为数千条指令—答案对（[Fine-Tuning with Synthetic Data: Self-Instruct, Distillation, and the Model Collapse Risk](https://sukruyusufkaya.com/en/blog/sentetik-veri-ile-fine-tuning-2026)）。在 agent 场景中，通义的端到端方案先用随机游走构建高互联知识图谱，再生成复杂、高不确定性、超人类水平的问答对，全程无需人工干预（[Tongyi DeepResearch Technical Report](https://arxiv.org/html/2510.24701v1)）。

## 核心技术与关键概念

- **Self-Instruct / Evol-Instruct**：种子扩展与样例进化。
- **自蒸馏（self-distillation）**：模型以自身输出为监督，配合验证过滤。
- **验证与过滤（verification & filtering）**：循环一致性、事实性校验、多验证器级联。
- **数据飞轮（data flywheel）**：生成—训练—评测—再生成的正循环。
- **模型崩塌（model collapse）**：递归训练导致分布尾部丢失、多样性下降、记忆化。
- **熵与置信度监控**：用合成数据熵下降、模型置信度作为崩塌预警指标（[A Closer Look at Model Collapse](https://arxiv.org/html/2509.16499v3)、[ForTIFAI](https://arxiv.org/html/2509.08972v2)）。

从既有研究看，缓解模型崩塌的手段可归为三类：数据侧（熵选择、提高真实数据配比）、模型侧（提升模型多样性、用冻结模型重标注）与损失侧（置信度感知的损失设计）（[Multimodal Model Collapse](https://dl.acm.org/doi/pdf/10.1145/3716553.3750806)、[Entropy-based selection](https://arxiv.org/html/2509.16499v3)、[ForTIFAI](https://arxiv.org/html/2509.08972v2)）。

## 代表性项目 / 公司 / 产品

- Tülu、OpenHermes、Llama-3-Instruct：高度依赖合成数据的开放权重指令模型（[Synthetic Data Generation](https://zeroentropy.dev/concepts/synthetic-data-generation/)）。
- 通义 DeepResearch：端到端合成数据生成管线（[Tongyi DeepResearch Technical Report](https://arxiv.org/html/2510.24701v1)）。
- Self-Verified Distillation、ForTIFAI：自验证蒸馏与抗崩塌训练方法（[Self-Verified Distillation](https://arxiv.org/abs/2605.26132)、[ForTIFAI](https://arxiv.org/html/2509.08972v2)）。

## 关键数据与评测结果

| 事项 | 结论 | 来源 |
| --- | --- | --- |
| 生成 1 万条样本耗时 | 数小时（相比人工数周） | [What Is Synthetic Training Data?](https://ai-tldr.dev/learn/fine-tuning/distillation-and-tools/synthetic-training-data/) |
| 多模态崩塌缓解手段 | 增加解码预算、模型多样性、冻结模型重标注 | [Multimodal Model Collapse](https://dl.acm.org/doi/pdf/10.1145/3716553.3750806) |
| 崩塌驱动指标 | 合成数据熵下降 | [A Closer Look at Model Collapse](https://arxiv.org/html/2509.16499v3) |
| 抗崩塌损失 | Truncated Cross Entropy 显著延缓崩塌 | [ForTIFAI](https://arxiv.org/html/2509.08972v2) |

## 趋势与争议

1. **默认化**：合成数据成为专用模型的默认监督来源，但也带来同质化与偏差放大风险（[Synthetic Data Generation](https://zeroentropy.dev/concepts/synthetic-data-generation/)）。
2. **崩塌是否必然**：早期观点认为递归训练必然崩塌，新研究强调通过数据比例、熵选择、置信度损失与模型多样性可缓解，争议在于所需真实数据的比例（[Preventing Model Collapse](https://www.semanticscholar.org/paper/Preventing-Model-Collapse-when-Training-LLMs-with-Gharesifard-Tabuada/4058e948c1a787739eff1ce3cf821ab364bca3d8)、[ForTIFAI](https://arxiv.org/html/2509.08972v2)）。
3. **验证成本**：过滤与级联验证提升了质量，也引入额外算力与可能被利用的 judge 噪声（[Self-Verified Distillation](https://arxiv.org/abs/2605.26132)）。
4. **验证器噪声传导**：合成数据的最终质量高度依赖验证管线，而验证器（尤其是 LLM judge）本身存在噪声，这与 RLVR 面临的验证器问题同源（[Self-Verified Distillation](https://arxiv.org/abs/2605.26132)、[Rate or Fate? RLVεR](https://arxiv.org/pdf/2601.04411)）。
5. **合规**：合成数据的版权、来源标注与训练合规尚无统一标准，属行业持续讨论议题（本条未在上述检索结果中确认具体条款，暂不展开）。

## 参考来源

- [Synthetic Data Generation（zeroentropy.dev）](https://zeroentropy.dev/concepts/synthetic-data-generation/)
- [What Is Synthetic Training Data? Using LLMs to Train LLMs](https://ai-tldr.dev/learn/fine-tuning/distillation-and-tools/synthetic-training-data/)
- [Fine-Tuning with Synthetic Data: Self-Instruct, Distillation, and the Model Collapse Risk](https://sukruyusufkaya.com/en/blog/sentetik-veri-ile-fine-tuning-2026)
- [Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline](https://arxiv.org/abs/2605.26132)
- [Tongyi DeepResearch Technical Report](https://arxiv.org/html/2510.24701v1)
- [What happens when generative AI models train recursively on each others' outputs?](https://arxiv.org/html/2505.21677)
- [Multimodal Synthetic Data Finetuning and Model Collapse: Insights from VLMs and Diffusion Models](https://dl.acm.org/doi/pdf/10.1145/3716553.3750806)
- [A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective](https://arxiv.org/html/2509.16499v3)
- [ForTIFAI: Fending Off Recursive Training Induced Failure for AI Models](https://arxiv.org/html/2509.08972v2)
- [Preventing Model Collapse when Training LLMs with Synthetic Data](https://www.semanticscholar.org/paper/Preventing-Model-Collapse-when-Training-LLMs-with-Gharesifard-Tabuada/4058e948c1a787739eff1ce3cf821ab364bca3d8)
- [Want Better Synthetic Data? Steer It: Activation Steering for Low-Resource Language Generation](https://arxiv.org/html/2606.18389)
- [Rate or Fate? RLVεR: Reinforcement Learning with Verifiable Noisy Rewards](https://arxiv.org/pdf/2601.04411)