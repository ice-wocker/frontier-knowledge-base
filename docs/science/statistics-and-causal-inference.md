# 统计学与因果推断

> 最后更新：2026-09-26 ｜ 领域：科学·统计学与因果推断 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

统计学提供从有限样本推断总体、量化不确定性与设计实验的工具；因果推断则聚焦"干预的效果"而非单纯关联。Rubin 的潜在结果框架与 Pearl 的结构因果模型（含因果图与 do-演算）是两大主流语言。实践中广泛使用随机对照试验、目标试验模拟（target trial emulation）以及因果机器学习方法。2025–2026 年的显著变化是 LLM 与自动化的引入，以及碰撞偏误（collider bias）等经典陷阱被反复证实。

## 最新进展（2025–2026）

**目标试验模拟（TTE）成为观察性因果推断的标准框架。** 该框架主张两步走：先指定能回答因果问题的假想随机试验方案（目标试验），再尝试用观察性数据模拟该试验；其价值在于预防若干常见偏倚（[The target trial framework for causal inference from observational data: Why and when is it helpful?](https://pmc.ncbi.nlm.nih.gov/articles/PMC11936718/pdf/nihms-2063403.pdf)）。方法学综述进一步将其形式化为一系列必须明确规定的要素：合格标准、治疗策略与分配、结局、随访、因果对比与统计分析（[Target trial emulation: from observational data to causal inference](https://ebm.bmj.com/content/early/2026/07/23/bmjebm-2025-114080)）。

**TTE 的自动化与联邦化。** 有研究提出 LLM 驱动框架，用检索增强生成从真实试验方案中抽取五个核心 TTE 设计参数，并生成可在真实世界 EHR 数据上执行的表型管线，再由人工校验（[LLM-Driven Target Trial Emulation with Human-in-the-Loop Validation for Randomized Trial](https://www.medrxiv.org/content/10.64898/2026.04.09.26350523v1.full)）。FL-TTE 则把 TTE 扩展为多中心联邦学习框架，在不共享患者级数据的前提下完成联邦协议设计、联邦逆概率加权等步骤（[Federated target trial emulation using distributed observational data for treatment effect estimation](https://pmc.ncbi.nlm.nih.gov/articles/PMC12214564/)）。

**因果发现与 LLM 结合。** Causal Ensemble Agent（CEA）对异构因果发现专家做关系级线性意见池化，并仅在聚合置信度接近决策边界时调用 LLM 作为"元裁判"动态重赋权，而非让 LLM 直接推断因果关系（[Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting](https://arxiv.org/html/2606.10607v1)）。Tree-Query 把成对因果发现归约为关于后门路径、独立性与潜在混杂、因果方向的短序列查询，给出可解释判断与稳健性置信度，并对四类成对关系的渐近可识别性给出理论保证（[Step-by-Step Causality: Transparent Causal Discovery with Multi-Agent Tree-Query and Adversarial Confidence Estimation](https://arxiv.org/html/2601.10137v1)）。CDFM 则尝试构建"因果发现基础模型"，把未知因果机制视为潜变量以支持零样本结构推断（[CDFM: Towards a General-Purpose Causal Discovery Foundation Model](https://www.semanticscholar.org/paper/CDFM:-Towards-a-General-Purpose-Causal-Discovery-Qiao-Cai/91192ae14665f6af67d65be3756063cb470fe3f3)）。

**贝叶斯计算与新工具。** AI4BayesCode 将自然语言描述的贝叶斯模型翻译为可运行、经校验的 MCMC 采样器，通过把模型分解为模块化采样块减少从零实现复杂采样算法的需求（[AI4BayesCode: From Natural Language Descriptions to Validated Modular Stateful Bayesian Samplers](https://arxiv.org/html/2605.18476v1)）。"JAX à la Stan"提出按 Stan 设计范式在 JAX 中编写贝叶斯模型的方法，便于把既有教材与案例逐行迁移（[JAX à la Stan](https://bob-carpenter.github.io/dj-paper/)）。组合式摊销贝叶斯推断被扩展到大规模层次模型，用于缓解聚合大量数据点时的数值稳定性问题（[Compositional amortized inference for large-scale hierarchical Bayesian models](https://openreview.net/forum?id=N3XCVHZGW5)）。

**工业界因果机器学习。** DoWhy 等端到端因果推断库被广泛用于生产实践（[DoWhy | An end-to-end library for causal inference](https://petergtz.github.io/dowhy/v0.6/index.html)）。在促销优化场景中，双重稳健/去偏机器学习（DML）与成本感知优化结合，实现促销类型与折扣深度的个性化分配，以在效果与预算效率之间平衡（[Causal Machine Learning for Promotions: Industry Evidence and Applications](https://causal-machine-learning.github.io/kdd2025-workshop/papers/16.pdf)）。

## 核心概念与常见陷阱

- **潜在结果与反事实**：因果效应定义为同一单元在不同干预下的结果之差；观察数据中仅能观测到其中一个。
- **因果图（DAG）与识别准则**：后门准则、前门准则；用图判断应调整哪些协变量。
- **碰撞偏误**：碰撞变量是另外两个变量的共同结果（如 D → X ← Y）。两个原因在无条件时相互独立，但一旦对碰撞变量条件化便产生条件依赖，从而引入原本不存在的伪关联（[What Directed Acyclic Graphs (DAGs) Teach Us About Choosing Covariates](https://j1yoo.github.io/blog/2025/What_Directed_Acyclic_Graphs_Teach_Us_About_Choosing_Covariates/)）。有方法学文章系统指出，用探索性多变量回归识别"因果风险因素"存在碰撞偏误、多重检验与 p 值操纵等问题（[Factors associated with: problems of using exploratory multivariable regression to identify causal risk factors](https://pmc.ncbi.nlm.nih.gov/articles/PMC12574381/)）。尘肺/COVID 类研究也通过定量偏误分析（如 RHR）评估对住院或感染状态条件化带来的碰撞偏误（[Investigation of potential collider bias in estimating the association between long-term exposure to air pollution and COVID-19 mortality](https://pmc.ncbi.nlm.nih.gov/articles/PMC12040017/)）。
- **工具变量的假设依赖**：有研究显示把某合并用药作为协变量纳入两阶段最小二乘（2SLS）会引入碰撞偏误，可能制造非因果的存活获益关联（[Does Piperacillin-Tazobactam Increase Mortality Risk Compared With Cefepime? Collider Bias and the Importance of Assumptions in Instrumental Variable Analyses](https://academic.oup.com/cid/article/82/1/e17/8172143)）。

## 趋势与争议

1. **LLM 与因果推断的结合**：带来可解释性与自动化红利，但 LLM 判断可能引入不可验证的假设，故多采用"仅作裁判、不直接定因果"的设计。
2. **"调整更多协变量"未必更安全**：碰撞偏误的存在说明协变量选择必须由图或明确假设驱动。
3. **框架选择**：TTE 与 DAG/do-演算在医学、经济与社会科学的适用边界仍在讨论；不同学科口径差异明显。

## 参考来源

- [The target trial framework for causal inference from observational data: Why and when is it helpful?](https://pmc.ncbi.nlm.nih.gov/articles/PMC11936718/pdf/nihms-2063403.pdf)
- [Target trial emulation: from observational data to causal inference（BMJ EBM）](https://ebm.bmj.com/content/early/2026/07/23/bmjebm-2025-114080)
- [LLM-Driven Target Trial Emulation with Human-in-the-Loop Validation for Randomized Trial](https://www.medrxiv.org/content/10.64898/2026.04.09.26350523v1.full)
- [Federated target trial emulation using distributed observational data for treatment effect estimation](https://pmc.ncbi.nlm.nih.gov/articles/PMC12214564/)
- [Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting](https://arxiv.org/html/2606.10607v1)
- [Step-by-Step Causality: Transparent Causal Discovery with Multi-Agent Tree-Query and Adversarial Confidence Estimation](https://arxiv.org/html/2601.10137v1)
- [CDFM: Towards a General-Purpose Causal Discovery Foundation Model](https://www.semanticscholar.org/paper/CDFM:-Towards-a-General-Purpose-Causal-Discovery-Qiao-Cai/91192ae14665f6af67d65be3756063cb470fe3f3)
- [AI4BayesCode: From Natural Language Descriptions to Validated Modular Stateful Bayesian Samplers](https://arxiv.org/html/2605.18476v1)
- [JAX à la Stan](https://bob-carpenter.github.io/dj-paper/)
- [Compositional amortized inference for large-scale hierarchical Bayesian models](https://openreview.net/forum?id=N3XCVHZGW5)
- [DoWhy | An end-to-end library for causal inference](https://petergtz.github.io/dowhy/v0.6/index.html)
- [Causal Machine Learning for Promotions: Industry Evidence and Applications（KDD 2025 Workshop）](https://causal-machine-learning.github.io/kdd2025-workshop/papers/16.pdf)
- [What Directed Acyclic Graphs (DAGs) Teach Us About Choosing Covariates](https://j1yoo.github.io/blog/2025/What_Directed_Acyclic_Graphs_Teach_Us_About_Choosing_Covariates/)
- [Factors associated with: problems of using exploratory multivariable regression to identify causal risk factors](https://pmc.ncbi.nlm.nih.gov/articles/PMC12574381/)
- [Investigation of potential collider bias in estimating the association between long-term exposure to air pollution and COVID-19 mortality](https://pmc.ncbi.nlm.nih.gov/articles/PMC12040017/)
- [Does Piperacillin-Tazobactam Increase Mortality Risk Compared With Cefepime? Collider Bias and the Importance of Assumptions in Instrumental Variable Analyses](https://academic.oup.com/cid/article/82/1/e17/8172143)