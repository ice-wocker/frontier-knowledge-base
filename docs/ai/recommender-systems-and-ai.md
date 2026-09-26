# 推荐系统与 AI（Recommender Systems & AI）

> 最后更新：2026-09-26 ｜ 领域：AI·提示、Agent 与应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

推荐系统（Recommender Systems）从早期的协同过滤（Collaborative Filtering）与矩阵分解，演进到深度学习排序模型，再到当前以大语言模型（LLM）与生成式架构为核心的新范式。传统工业推荐是多级级联架构（召回 retrieval、粗排、精排 ranking、竞拍 auction），在工业界取得显著成功，但受限于语义鸿沟、阶段不一致与特征碎片化（[Generative Recommendation: A Survey of Models, Systems, and Industrial Advances](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176523089.94266134/v2)）。新兴的生成式推荐系统（Generative Recommender Systems, GRS）把推荐重构为序列生成任务，用 Transformer 架构与 token 化的物品表示统一建模（同上）。

## 最新进展（2025–2026）

过去一年，基于 LLM 的生成式推荐（GR）形成与判别式推荐明显不同的新范式，展现出替代"重度依赖复杂手工特征的传统推荐系统"的潜力（[GR-LLMs: Recent Advances in Generative Recommendation Based on Large Language Models](https://arxiv.org/html/2507.06507)）。综述将生成式推荐的优势归纳为三点：面向会话语义、可解释推荐与个性化内容创作等"天然生成型任务"具备根本优势；大规模训练范式下生成式架构受益于缩放定律，性能可随模型与数据规模可预测地提升；以及统一建模可缓解多阶段级联的不一致（[A Survey on Generative Recommendation: Data, Model, and Tasks](https://arxiv.org/html/2510.27157)）。

工业落地方面，2025 年出现一波生成式推荐模型浪潮（OneRec、MTGR、RankMixer、PinRec、LONGER 等）（[Generative Recommendation（博客）](http://xiahouzuoxin.github.io/posts/generativerecommendation/)）。快手 OneRec 采用 Encoder-Decoder 架构，引入基于奖励机制的偏好对齐方法，借助强化学习增强效果（[快手提出端到端生成式推荐系统 OneRec](https://blog.csdn.net/kuaishoutech/article/details/148798366)）；2025 年财报显示快手迭代端到端生成式推荐大模型并推出 OneRec-V2，持续提升推荐准确度（[Kuaishou Technology Announces Fourth Quarter and Full Year 2025 Financial Results](https://kuaishou.gcs-web.com/news-releases/news-release-details/kuaishou-technology-announces-fourth-quarter-and-full-year-2025)）。

2026 年的研究进一步把"生成式推荐"推进到三条新方向：其一"弯曲缩放曲线"（如 ULTRA-HSTU 的协同设计），其二统一长序列建模与特征交叉的扩展（如 HyFormer、OneTrans），其三把用户历史长度推向 1 万条以上作为全新的缩放轴（如抖音相关工作），代表性新模型包括 TokenMixer-Large、HyFormer、ULTRA-HSTU、GEMs 与"Make It Long, Keep It Fast"等（[Generative Recommendation（博客）](http://xiahouzuoxin.github.io/posts/generativerecommendation/)）。Google 的 PLUM 论文则把 Gemini 作为骨干模型适配到推荐域：用 RQ-VAE 对物品做 token 化，并在用户观看序列上做继续预训练（Continued Pre-Training, CPT），据称在 YouTube Shorts 的线上 A/B 中带来 +4.96% 的点击率（CTR）提升（[Generative Recommendation in Production](https://louiswang524.github.io/blog/generative-retrieval/)）。

## 核心技术与关键概念

**协同过滤到深度学习**：从基于用户—物品交互相似度的协同过滤，过渡到用神经网络建模交互序列与特征交叉的深度推荐（DLRM 类模型）。

**序列推荐**：直接建模用户行为序列。HSTU（Hierarchical Sequential Transducers）把推荐重构为对 action token 的生成式转换，用逐点门控替代 softmax、用逐元素门控替换 FFN，并把服务（M-FALCON）与稀疏性（stochastic length）设计进架构，被描述为"推荐领域第一条幂律缩放曲线"（[Generative Recommendation（博客）](http://xiahouzuoxin.github.io/posts/generativerecommendation/)）。HSTU 的论文证明生成式架构相比传统判别式模型可获得更优的缩放表现：直接处理完整用户历史、不依赖特征工程与采样，随资源增加展现更高性能上限与更好训练效率（[Generative Recommendation: A Survey](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176523089.94266134/v2)）。

**语义 ID（Semantic ID）与物品 token 化**：生成式推荐须先把物品离散化为可生成的 token 序列，常见做法是基于语义的 ID 设计。最新研究如 VaLiDRec 用变长、与 LLM 词表对齐的语义标识符（SID），通过 token 重要性估计、语义质量感知剪枝与冲突感知精修，让标识长度随物品语义复杂度自适应（[VaLiDRec](https://arxiv.org/html/2607.25209)）；面向会话语境的工作则提出"先生成、后匹配"的 intent-driven SID 生成范式（[Intent-Driven Semantic ID Generation](https://arxiv.org/html/2605.07613)）。

**大模型推荐（LLM4Rec）**：把用户—物品交互翻译成自然语言模板，把推荐重构为语言建模任务，用提示让 LLM 直接估计向用户 u 推荐物品 i 的似然，实现灵活的零样本个性化（[A Comprehensive Review on Harnessing Large Language Models to Overcome Recommender System Challenges](https://arxiv.org/html/2507.21117)）。LLM4Rec 同时带来规模、实时处理与数据隐私方面的新挑战（[LLM4Rec: A Comprehensive Survey](https://pdfs.semanticscholar.org/6944/4b6724b66f68004b6756b4cbdecac26c4d46.pdf)）。为兼顾语义深度与线上实时性，S-GRec 提出把高成本的语义推理与实时推断解耦，在训练阶段蒸馏进轻量、与业务对齐的生成器（[S-GRec](https://arxiv.org/html/2602.10606v3)）。

**冷启动**：系统必须在新用户无交互历史时回退到基于内容或基于流行度的信号，而不能硬失败（[Design a Recommendation System](https://www.datainterview.com/courses/machine-learning-system-design/case-recommendation-system)）。NVIDIA 的工程博客把冷启动与"严格延迟要求"列为生成式推荐在生产中必须面对的两大问题（[How Generative Recommenders Are Redefining RecSys at Scale](https://developer.nvidia.com/blog/how-generative-recommenders-are-redefining-recsys-at-scale/)）；也有工作提出 ColdRAG，用动态构建的知识图谱与 LLM 引导的多跳推理为冷启动检索与排序候选（[ColdRAG](https://openreview.net/attachment?id=JvRYUMIBwO&name=pdf)）。

**指标与 A/B**：排序质量常用 NDCG@K（带位置对数折扣、支持分级相关性）、Hit Rate@K、MAP/MRR；评分预测用 RMSE/MAE；二分类相关性用 AUC（[Recommendation System — AI Wiki](https://aiwiki.ai/wiki/recommendation_system)；[Recommendation Systems: Fundamentals and Core Concepts](https://www.chenk.top/en/recommendation-systems/01-fundamentals/)）。系统还需支持离线 A/B 评估与在线实验，允许不同模型变体服务不同用户分桶（[Design a Recommendation System](https://www.datainterview.com/courses/machine-learning-system-design/case-recommendation-system)）。

## 代表性项目 / 公司 / 产品

- **快手 OneRec / OneRec-V2**：端到端生成式推荐系统，在快手/快手极速版 App 上线（[OneRec Technical Report](https://arxiv.org/pdf/2506.13695v4)）；OneRec-V2 进一步引入 FP8 量化推断（[Quantized Inference for OneRec-V2](https://arxiv.org/html/2603.11486v1)）。
- **Meta HSTU**：生成式推荐的开创性架构，引入推荐领域的缩放定律证据（[Generative Recommendation: A Survey](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176523089.94266134/v2)）。
- **Google PLUM**：以 Gemini 为骨干、经 RQ-VAE 物品 token 化与 CPT 适配到 YouTube 推荐（[Generative Recommendation in Production](https://louiswang524.github.io/blog/generative-retrieval/)）。
- **美团 MTGR（Meituan Generative Recommendation）**：基于 HSTU 架构，保留原 DLRM 特征（含交叉特征），通过用户级压缩实现训练与推理加速（[Bending the Scaling Law Curve in Large-Scale Recommendation Systems](https://www.semanticscholar.org/paper/Bending-the-Scaling-Law-Curve-in-Large-Scale-Ding-Course/abda063ddc44a79f86650196daa45aab6f1728a1/figure/12)）。
- **Pinterest**：在冷启动与内容探索/去偏方向持续产出工业系统，如冷启动成本策略与 PinEqualizer 全漏斗内容探索去偏系统（[Warmer for Less](https://arxiv.org/html/2512.17277v1/)；[PinEqualizer](https://arxiv.org/html/2607.22518)）。

## 关键数据与评测结果

- **OneRec**：显著降低通信与存储开销，运营成本（OPEX）仅为传统推荐管线的 10.6%；在快手/快手极速版 App 处理 25% 的总 QPS，整体 App 停留时长分别提升 0.54% 与 1.24%（[OneRec Technical Report](https://arxiv.org/pdf/2506.13695v4)）。其 P-Score Reward 消融显示在 Kuaishou 场景下观看时长 +0.21%、App 停留 +0.26%、视频观看 +0.17%（[OneRec Technical Report v2](https://arxiv.org/html/2506.13695v2)）。
- **OneRec-V2**：在拥有 4 亿日活（DAU）的快手/快手极速版 App 上做在线 A/B 测试，App 停留时长分别提升 0.467% 与 0.741%，7 日用户留存（LT7）分别提升 0.069% 与 0.034%，并称在无"跷跷板效应"下平衡多目标（[OneRec-V2 Technical Report](https://arxiv.org/html/2508.20900)；[OneRec-V2 概览](https://www.alphaxiv.org/overview/2508.20900v4)）。
- **OneRec-V2 量化推断**：采用 FP8 训练后量化并配套优化推断基础设施，端到端推断延迟由 139ms 降至 70ms（-49%）、吞吐由 205 提升至 394 queries/sec（+92%），并称通过线上 A/B 确认核心指标零退化（[Quantized Inference for OneRec-V2](https://papers.lunadong.com/paper/9206)；[arXiv:2603.11486](https://arxiv.org/html/2603.11486v1)）。
- **HSTU 的上下文并行扩展**：论文引入支持 jagged tensor 的 HSTU attention 上下文并行，使用户交互序列长度支持提升 5.3 倍，与 DDP 结合时取得 1.55× 的缩放系数（[Scaling Generative Recommendations with Context Parallelism on HSTU](https://arxiv.org/pdf/2508.04711v1)）。
- **Pinterest 冷启动**：论文给出多策略在 grid-click 会话、save 会话等指标上的相对提升，其中 Homefeed 保存（Save）单项最高 +0.77%（[Warmer for Less](https://arxiv.org/html/2512.17277v1/)）。
- **SessionRec**：验证"下一会话预测"范式可持续展现缩放定律特征，随数据量增加性能持续提升，并认为单一生成模型可同时处理召回与排序，从而替代传统多模型级联（[SessionRec](https://arxiv.org/pdf/2502.10157.pdf)）。
- **Google PLUM**：在 YouTube Shorts 的线上 A/B 中报告 +4.96% CTR 提升（[Generative Recommendation in Production](https://louiswang524.github.io/blog/generative-retrieval/)）。

## 趋势与争议

一是**级联架构 vs 端到端生成**：支持者认为统一生成模型可消除多阶段不一致并受益于缩放定律（[A Survey on Generative Recommendation](https://arxiv.org/html/2510.27157)）；但工业界仍需在成本、实时性、多目标平衡上做取舍，OneRec 以性能优化把 OPEX 压到传统管线的约十分之一以证明可行性（[OneRec Technical Report](https://arxiv.org/pdf/2506.13695v4)）。二是**缩放定律是否稳定**：HSTU 之后，"弯曲缩放曲线"等研究显示大推荐模型的缩放行为需更细致刻画，2026 年出现 ULTRA-HSTU 等"协同设计"思路（[Bending the Scaling Law Curve](https://www.semanticscholar.org/paper/Bending-the-Scaling-Law-Curve-in-Large-Scale-Ding-Course/abda063ddc44a79f86650196daa45aab6f1728a1/figure/12)；[Generative Recommendation（博客）](http://xiahouzuoxin.github.io/posts/generativerecommendation/)）。三是**冷启动与偏差**：探索与去偏成为 Pinterest 等平台的重点工业课题（[PinEqualizer](https://arxiv.org/html/2607.22518)），NVIDIA 亦把冷启动与严格延迟列为生产痛点（[NVIDIA](https://developer.nvidia.com/blog/how-generative-recommenders-are-redefining-recsys-at-scale/)）。四是**隐私与实时性**：LLM4Rec 在规模、实时处理与数据隐私上带来新挑战（[LLM4Rec](https://pdfs.semanticscholar.org/6944/4b6724b66f68004b6756b4cbdecac26c4d46.pdf)），而把语义推理与线上推断解耦（如 S-GRec）是当前应对实时性的主流工程方向（[S-GRec](https://arxiv.org/html/2602.10606v3)）。

## 参考来源

1. [Generative Recommendation: A Survey of Models, Systems, and Industrial Advances](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176523089.94266134/v2)
2. [GR-LLMs: Recent Advances in Generative Recommendation Based on Large Language Models](https://arxiv.org/html/2507.06507)
3. [LLM4Rec: A Comprehensive Survey on the Integration of Large Language Models in Recommender Systems](https://pdfs.semanticscholar.org/6944/4b6724b66f68004b6756b4cbdecac26c4d46.pdf)
4. [A Survey on Generative Recommendation: Data, Model, and Tasks](https://arxiv.org/html/2510.27157)
5. [A Comprehensive Review on Harnessing Large Language Models to Overcome Recommender System Challenges](https://arxiv.org/html/2507.21117)
6. [Scaling Generative Recommendations with Context Parallelism on Hierarchical Sequential Transducers](https://arxiv.org/pdf/2508.04711v1)
7. [Generative Recommendation（博客）](http://xiahouzuoxin.github.io/posts/generativerecommendation/)
8. [SessionRec: Next Session Prediction Paradigm For Generative Sequential Recommendation](https://arxiv.org/pdf/2502.10157.pdf)
9. [Bending the Scaling Law Curve in Large-Scale Recommendation Systems](https://www.semanticscholar.org/paper/Bending-the-Scaling-Law-Curve-in-Large-Scale-Ding-Course/abda063ddc44a79f86650196daa45aab6f1728a1/figure/12)
10. [Warmer for Less: A Cost-Efficient Strategy for Cold-Start Recommendations at Pinterest](https://arxiv.org/html/2512.17277v1/)
11. [Recommendation System — AI Wiki](https://aiwiki.ai/wiki/recommendation_system)
12. [Recommendation Systems (1): Fundamentals and Core Concepts](https://www.chenk.top/en/recommendation-systems/01-fundamentals/)
13. [Design a Recommendation System](https://www.datainterview.com/courses/machine-learning-system-design/case-recommendation-system)
14. [PinEqualizer: Full Funnel Content Exploration and Debiasing System at Pinterest](https://arxiv.org/html/2607.22518)
15. [OneRec Technical Report](https://arxiv.org/pdf/2506.13695v4)
16. [OneRec Technical Report v2](https://arxiv.org/html/2506.13695v2)
17. [OneRec-V2 Technical Report](https://arxiv.org/html/2508.20900)
18. [OneRec-V2 概览 — alphaXiv](https://www.alphaxiv.org/overview/2508.20900v4)
19. [Kuaishou Technology Announces Fourth Quarter and Full Year 2025 Financial Results](https://kuaishou.gcs-web.com/news-releases/news-release-details/kuaishou-technology-announces-fourth-quarter-and-full-year-2025)
20. [快手提出端到端生成式推荐系统 OneRec — CSDN](https://blog.csdn.net/kuaishoutech/article/details/148798366)
21. [Quantized Inference for OneRec-V2 (arXiv:2603.11486)](https://arxiv.org/html/2603.11486v1)
22. [Quantized Inference for OneRec-V2 — Evaluation Highlights](https://papers.lunadong.com/paper/9206)
23. [Generative Recommendation in Production: HSTU, OneRec, and What Every Major Platform Is Building](https://louiswang524.github.io/blog/generative-retrieval/)
24. [VaLiDRec: Variable-Length LLM-Aligned Semantic IDs for Generative Recommendation](https://arxiv.org/html/2607.25209)
25. [Intent-Driven Semantic ID Generation for Grounded Conversational News Recommendation](https://arxiv.org/html/2605.07613)
26. [S-GRec: Personalized Semantic-Aware Generative Recommendation with Asymmetric Advantage](https://arxiv.org/html/2602.10606v3)
27. [How Generative Recommenders Are Redefining RecSys at Scale — NVIDIA](https://developer.nvidia.com/blog/how-generative-recommenders-are-redefining-recsys-at-scale/)
28. [ColdRAG: Adaptive Candidate Retrieval with Dynamic Knowledge Graph Construction for Cold-Start Recommendation](https://openreview.net/attachment?id=JvRYUMIBwO&name=pdf)