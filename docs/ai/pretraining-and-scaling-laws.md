# 预训练与缩放定律

> 最后更新：2026-09-26 ｜ 领域：AI·基础原理 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

预训练是 LLM 通过海量文本以自监督方式学习通用语言能力的基础阶段。其核心工程问题是"算力—数据—参数"三者的最优配比，以及如何在超大规模下保持训练稳定、并保证数据质量。缩放定律（Scaling Laws）为这一配比提供了经验性数学指引。

## 最新进展（2025–2026）

2025–2026 年，业界对缩放定律的实践从"纯训练算力最优"转向"面向部署的产品最优"：

- **超配数据的"过度训练"（over-training）**成为主流。以 Llama 3 为例，8B 模型在约 15 万亿 token 上训练，远超 Chinchilla 针对 8B 规模建议的约 1600 亿 token（接近 100 倍）；70B 模型同样在 15 万亿 token 上训练，token/参数比约 214，是 Chinchilla 最优比 20 的 10 倍以上（[The Llama 3 herd](https://vibeengines.com/paper/llama-3)、[Scaling laws & compute economics](https://wes.today/series/training/train-from-scratch/training-loop/scaling-laws/)）。
- 这一选择的经济逻辑是：模型训练一次、服务数以亿次计，牺牲一些训练算力换取更小更便宜的推理模型，长期更划算（[The Llama 3 herd](https://vibeengines.com/paper/llama-3)）。
- 数据规模持续膨胀：LLMOrbit 的整理显示 Gopher 约 1.4T token、Chinchilla 约 1.4T、Llama 2 约 2.0T、Llama 3 约 15T、Gemini 1.5 达 12T 以上；训练成本也从 GPT-3 的约 330 万美元升至 DeepSeek-V3 的 1.1 亿美元以上，5 年间膨胀约 100 倍（[LLMOrbit: A Circular Taxonomy of Large Language Models](https://arxiv.org/html/2601.14053v1)）。
- **缩放定律本身被扩展**：研究者开始把"数据质量""数据边界"等此前被忽略的变量纳入模型，提出质量感知缩放定律与"计算—数据"统一缩放定律（见下文）。

## 核心技术与关键概念

### Kaplan 定律与 Chinchilla 之争

早期 Kaplan 等人的缩放定律建议将大部分算力投入模型参数量。2022 年 DeepMind 的论文《Training Compute-Optimal Large Language Models》（即 Chinchilla 论文）对此提出挑战：作者训练了 400 多个不同规模/数据配比的模型，认为在固定算力预算下，模型规模与数据应大致同比例增长，最优 token/参数比约为 20:1（即 10B 参数模型约需 200B token）（[Chinchilla Scaling Laws: Compute-Optimal LLM Training](https://mbrenndoerfer.com/writing/chinchilla-scaling-laws-compute-optimal-llm-training)、[What Are AI Scaling Laws?](https://ai-tldr.dev/learn/llm-fundamentals/llm-basics/what-are-scaling-laws/)）。据此，团队训练了 67B 参数的 Chinchilla，以相近算力预算超越了更大的模型（[Resolving Discrepancies in Compute-Optimal Scaling of Language Models](https://arxiv.org/html/2406.19146)）。

具体对比上，Gopher 为 280B 参数、约 300B token（每参数约 1.1 token）；Chinchilla 为 70B 参数、1.4T token（每参数约 20 token）（[Chinchilla Optimality](https://sungeuns.github.io/foundation-model-engineering/ko/chapter-8/chinchilla-optimality/)）。

后续研究指出 Kaplan 与 Hoffmann（Chinchilla）之间存在方法论差异，并尝试调和这两种结论（[Resolving Discrepancies in Compute-Optimal Scaling](https://arxiv.org/html/2406.19146)）。Chinchilla 的核心结论 D = 20N 被广泛引用，但实践中 FLOPs 往往并非首要约束，模型常被训练远超过 Chinchilla 时长（[Scaling Inference-Efficient Language Models](https://arxiv.org/html/2501.18107v2)）。

### 质量感知与"计算—数据"缩放定律（2025–2026）

Chinchilla 框架只考虑模型规模与数据量，未形式化数据质量。2025 年有研究引入无量纲的"数据质量参数 Q"，提出质量感知缩放定律，把损失建模为模型规模、数据量与数据质量的联合函数（[Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining](https://arxiv.org/html/2510.03313v2)）。一项被 ICLR 2026 收录的研究构建了 QualityPajama（含 23 个不同质量干预的数据集），训练 2000 多个模型系统测量"过滤 / 去重 / LLM 改写"如何重塑神经缩放定律的全部五个参数，发现数据干预会同时改变缩放系数与指数（而架构改动主要影响系数）（[How Text Quality Interventions Reshape Neural Scaling Laws for LLMs](https://en.papernotes.org/ICLR2026/llm_pretraining/how_text_quality_interventions_reshape_neural_scaling_laws_for_llms_empirical_st/)）。

针对"高质量数据有限"的现实，另一项工作提出"计算—数据"（CD）缩放定律：经典 compute-optimal 假设数据可随算力自由增长，而 data-optimal 假设语料固定、算力可无限增加；CD 缩放通过引入"词元有效性函数 η"统一两种极端情形（[Bridging Compute- and Data-Optimal Pretraining](https://arxiv.org/html/2607.25271)、[Bridging Compute- and Data-Optimal Pretraining（智源社区）](https://hub-assets-cache.baai.ac.cn/paper/dfa80101-fc41-4978-a663-545916b98835)）。

### 数据清洗与去重

预训练数据的质量决定模型上限。典型流水线包括：

- **精确去重（exact dedup）**：对文档做哈希，每个哈希仅保留一份（[Building Nemotron-CC](https://developer.nvidia.com/blog/?p=99540)）。
- **模糊去重（fuzzy dedup）**：通过 MinHash 签名 + 局部敏感哈希（LSH）检测高 Jaccard 相似度的近重复文档（[Building Nemotron-CC](https://developer.nvidia.com/blog/?p=99540)）。也有流水线先做模糊去重、再做精确子串去重（[CCI4.0](https://arxiv.org/html/2506.07463)）。
- **重复内容过滤**：既做跨语料的全局去重，也过滤单文档内部的高重复片段，防止模型学到退化、重复的语言模式并稳定训练分布（[Blu-WERP](https://arxiv.org/html/2511.18054)）。
- **质量与安全过滤**：移除仇恨言论、PII 与有毒内容，这一阶段被认为是最难的（[Data Collection and Cleaning for LLM Pretraining at Web Scale: The 2026 Pipeline Guide](https://rioworld.org/data-collection-and-cleaning-for-llm-pretraining-at-web-scale-the-2026-pipeline-guide)）。有报告称 Dolma 的段落级去重可将下游表现提升 7.3%，但预处理时间增至 3.2 倍；SimHash 64 位指纹已成为标准做法（[同上](https://rioworld.org/data-collection-and-cleaning-for-llm-pretraining-at-web-scale-the-2026-pipeline-guide)）。需要说明的是，此类具体增益数字来自不同实验设置，口径差异较大，引用时需核对原始报告。

### 数据墙与合成数据

研究界普遍担忧高质量公开文本即将耗尽：多项工作引用 Villalobos 等人（2022）的估计，认为可获得的高质量公开文本可能在 2026–2028 年间被耗尽，预训练因而进入"数据墙"（data wall）区间——从"吞吐能力问题"转变为"控制问题"，即在每一步优化中该让哪些 token 塑造模型（[OPUS: Towards Efficient and Principled Data Selection in LLM Pre-training in Every Iteration](https://arxiv.org/html/2602.05400v2)）。LLMOrbit 亦把"数据稀缺（预计 2026–2028 年高质量文本耗尽）"列为持续缩放面临的首要瓶颈（[LLMOrbit](https://arxiv.org/html/2601.14053v1)）。有分析进一步把预训练的"三重缩放墙"概括为：成本指数级增长、数据存量有限、以及每一点增量收益都要求指数级投入（[Scaling Walls, Data Exhaustion, and the Technical Limits of Pre-Training in 2026](https://www.bestaiweb.ai/scaling-walls-data-exhaustion-and-the-technical-limits-of-pre-training-in-2026/)）。

合成数据被视为延缓数据墙的路径之一：SynPro 通过"改写"与"重排版"把同一份有机数据呈现为多样形式，并用强化学习以质量、忠实度与数据影响力为奖励进行优化，报告称其解锁的有效 token 量是简单重复的 5.2 倍、是当时最优网页改写基线 RePro 的 3.0 倍（[Generating Pretraining Tokens from Organic Data for Data-Bound Scaling](https://arxiv.org/html/2605.17849)）。但合成数据并非免费午餐：一项系统研究指出，在 TXBK 混合中约 33% 合成数据的效果稳定优于 67%，且随模型变大，合成数据的相对收益会减弱（[Demystifying Synthetic Data in LLM Pre-training](https://proxy.stardusted.uk/default/https/arxiv.org/pdf/2510.01631)）；另有研究系统考察了提示设计、生成器模型与源数据对合成预训练数据质量的影响（[How Can We Synthesize High-Quality Pretraining Data?](https://arxiv.org/html/2604.13977v1)）。

### 训练不稳定与损失尖峰

超大规模预训练普遍遭遇梯度不稳定与损失尖峰（loss spike），可能引发灾难性发散，迫使团队回滚 checkpoint 并跳过数据批次（[ZClip: Adaptive Spike Mitigation for LLM Pre-Training](https://arxiv.org/html/2504.02507v1)）。常见成因包括：学习率过高、梯度爆炸、数值溢出/下溢（尤其在长序列或低精度下），以及大集群中 GPU 显存或网络的静默数据损坏（比特翻转）（[Training Stability: Diagnosing and Fixing Loss Spikes](https://kindatechnical.com/advanced-llm-topics/lesson-16-training-stability-diagnosing-and-fixing-loss-spikes.html)）。缓解手段包括：

- **梯度裁剪**：传统固定阈值或范数法效果有限，2025 年出现自适应方案，如 AdaGC（按张量的自适应梯度裁剪，对优化器无关、内存开销可忽略）（[AdaGC](https://arxiv.org/html/2502.11034v3)）、ZClip（动态调整裁剪阈值）（[ZClip](https://arxiv.org/html/2504.02507v1)）。
- **输出层与激活的不稳定性**：大学习率下训练末期的输出 logit 发散，常用 z-loss 缓解，但有研究认为 z-loss 只是治标，并提出输出嵌入中心化（output embedding centering）以治本（[Output Embedding Centering for Stable LLM Pretraining](https://arxiv.org/html/2601.02031v1)）；此外有研究提出 PowLU 激活函数，以有理幂函数实现自适应非线性，在尖峰区间维持稳定训练（[PowLU: An Activation Function for Stable Pre-Training of LLMs](https://arxiv.org/html/2605.25704)）。
- **运维层面**：以 NaN/Inf 计数等信号监控训练健康度（[Training Stability, Loss Spikes & Debugging Large Runs](https://prakashkagitha.github.io/llm-stack-book/03-pretraining/11-training-stability.html)）。

### 算力—数据—参数权衡

综合来看，配比决策需同时考虑三方面：训练算力预算（Chinchilla 视角）、部署推理成本（产品视角，倾向于宁小勿大、宁训久勿训短）以及数据可得性（数据墙视角）。Llama 3 报告拟合出最优训练 token 数随算力预算的幂律关系 N⋆(C) = AC^α，并得到 (α, A) = (0.53, 0.29)（[The Llama 3 Herd of Models](https://arxiv.org/pdf/2407.21783)）。

## 趋势与争议

- **compute-optimal 与 product-optimal 的分野**：Chinchilla 只优化训练算力，而实际部署需要权衡训练与推理的总成本，这使"过度训练"成为理性选择（[Scaling laws & compute economics](https://wes.today/series/training/train-from-scratch/training-loop/scaling-laws/)）。
- **数据墙隐忧**：高质量公开文本增长有限，去重与质量过滤会进一步缩减可用数据，推动合成数据与多模态数据的使用；但合成数据的收益随规模递减，且存在模型崩塌等风险（[OPUS](https://arxiv.org/html/2602.05400v2)、[Demystifying Synthetic Data](https://proxy.stardusted.uk/default/https/arxiv.org/pdf/2510.01631)）。
- **缩放定律的"指数 vs 系数"之争**：新研究显示数据质量干预会同时改变缩放系数与指数，意味着简单外推经典幂律可能低估数据质量的杠杆作用（[How Text Quality Interventions Reshape Neural Scaling Laws](https://en.papernotes.org/ICLR2026/llm_pretraining/how_text_quality_interventions_reshape_neural_scaling_laws_for_llms_empirical_st/)）。
- **数据配比不透明**：各厂商的领域配比（代码/数学/多语种权重）多为商业机密，不同来源口径不一，横向比较困难。

## 参考来源

- [The Llama 3 herd](https://vibeengines.com/paper/llama-3)
- [Scaling laws & compute economics](https://wes.today/series/training/train-from-scratch/training-loop/scaling-laws/)
- [LLMOrbit: A Circular Taxonomy of Large Language Models](https://arxiv.org/html/2601.14053v1)
- [Chinchilla Scaling Laws: Compute-Optimal LLM Training](https://mbrenndoerfer.com/writing/chinchilla-scaling-laws-compute-optimal-llm-training)
- [What Are AI Scaling Laws? Why Bigger Models Got Smarter](https://ai-tldr.dev/learn/llm-fundamentals/llm-basics/what-are-scaling-laws/)
- [Resolving Discrepancies in Compute-Optimal Scaling of Language Models](https://arxiv.org/html/2406.19146)
- [Chinchilla Optimality](https://sungeuns.github.io/foundation-model-engineering/ko/chapter-8/chinchilla-optimality/)
- [Scaling Inference-Efficient Language Models](https://arxiv.org/html/2501.18107v2)
- [The Llama 3 Herd of Models](https://arxiv.org/pdf/2407.21783)
- [Building Nemotron-CC, A High-Quality Trillion Token Dataset](https://developer.nvidia.com/blog/?p=99540)
- [CCI4.0: A Bilingual Pretraining Dataset](https://arxiv.org/html/2506.07463)
- [Blu-WERP (Web Extraction and Refinement Pipeline)](https://arxiv.org/html/2511.18054)
- [Data Collection and Cleaning for LLM Pretraining at Web Scale: The 2026 Pipeline Guide](https://rioworld.org/data-collection-and-cleaning-for-llm-pretraining-at-web-scale-the-2026-pipeline-guide)
- [ZClip: Adaptive Spike Mitigation for LLM Pre-Training](https://arxiv.org/html/2504.02507v1)
- [AdaGC: Enhancing LLM Pretraining Stability via Adaptive Gradient Clipping](https://arxiv.org/html/2502.11034v3)
- [Output Embedding Centering for Stable LLM Pretraining](https://arxiv.org/html/2601.02031v1)
- [Training Stability, Loss Spikes & Debugging Large Runs](https://prakashkagitha.github.io/llm-stack-book/03-pretraining/11-training-stability.html)
- [Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining](https://arxiv.org/html/2510.03313v2)
- [How Text Quality Interventions Reshape Neural Scaling Laws for LLMs](https://en.papernotes.org/ICLR2026/llm_pretraining/how_text_quality_interventions_reshape_neural_scaling_laws_for_llms_empirical_st/)
- [Bridging Compute- and Data-Optimal Pretraining](https://arxiv.org/html/2607.25271)
- [Bridging Compute- and Data-Optimal Pretraining（智源社区）](https://hub-assets-cache.baai.ac.cn/paper/dfa80101-fc41-4978-a663-545916b98835)
- [OPUS: Towards Efficient and Principled Data Selection in LLM Pre-training in Every Iteration](https://arxiv.org/html/2602.05400v2)
- [Scaling Walls, Data Exhaustion, and the Technical Limits of Pre-Training in 2026](https://www.bestaiweb.ai/scaling-walls-data-exhaustion-and-the-technical-limits-of-pre-training-in-2026/)
- [Generating Pretraining Tokens from Organic Data for Data-Bound Scaling](https://arxiv.org/html/2605.17849)
- [Demystifying Synthetic Data in LLM Pre-training](https://proxy.stardusted.uk/default/https/arxiv.org/pdf/2510.01631)
- [How Can We Synthesize High-Quality Pretraining Data?](https://arxiv.org/html/2604.13977v1)
- [Training Stability: Diagnosing and Fixing Loss Spikes](https://kindatechnical.com/advanced-llm-topics/lesson-16-training-stability-diagnosing-and-fixing-loss-spikes.html)
- [PowLU: An Activation Function for Stable Pre-Training of LLMs](https://arxiv.org/html/2605.25704)