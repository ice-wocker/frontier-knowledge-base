# 大模型评测基准（Benchmarks）

> 最后更新：2026-09-26 ｜ 领域：人工智能·模型评测 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

评测基准（benchmark）是衡量大模型能力的标尺，也是厂商发布时的"成绩单"。2025–2026 年，基准生态呈现两条主线：一是经典知识类基准（MMLU 系列）快速饱和，失去区分度；二是新基准不断向"更难、更真实、更抗污染"演进——从 GPQA Diamond、AIME/MATH 到 Humanity's Last Exam（HLE）、ARC-AGI-2，再到 agent 化的 SWE-bench Verified、LiveCodeBench、τ-bench、Terminal-Bench。与此同时，数据污染（contamination）与刷榜（leaderboard gaming）成为普遍且可量化的系统性问题。

## 2025–2026 最新进展

**知识基准饱和。** MMLU（Massive Multitask Language Understanding）由 Dan Hendrycks 等人于 2020 年 9 月提出、2021 年在 ICLR 发表，包含 57 个学科共 15,908 道题（[MMLU](https://aiwiki.ai/wiki/mmlu)、[Measuring Massive Multitask Language Understanding](https://arxiv.org/html/2009.03300v2)）。其分数从 GPT-3（2020）的 43.9% 升到 GPT-4（2023）的 86.4%、o1 的 91.8%（[From BERT to Frontier Agents](https://arxiv.org/pdf/2608.13675)），到 2026 年前沿模型已挤在 90% 出头的窄带内，差距不足两个百分点，落在 15,908 题测试的测量噪声内，被判定"已饱和、不再能区分前沿模型"（[MMLU, MMLU-Pro, and MMMU](https://benchmarkingagents.com/mmlu/)）。作为继任者，MMLU-Pro 通过增加选项、去除琐碎与噪声题，使准确率相对 MMLU 下降 16%–33%，并把对提示风格的敏感性从 4%–5% 降到约 2%（[MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/pdf/2406.01574v1)）。截至 2026 年 5 月，MMLU-Pro 前沿分数为 86%–89%，强开源模型为 81%–84%，呈现收敛（[MMLU-Pro: The Discriminating Successor to MMLU](https://benchmarkingagents.com/mmlu-pro/)）。

**面向高难推理的新基准。** GPQA Diamond 在 2026 年 9 月的前沿分数为：GPT-6 Astra 96.0、Gemini 3.8 Flash 95.3、Claude Fable 5.1 与 Claude Opus 5 均 93.7（[Frontier AI Benchmarks Compared: Opus 5.5, GPT-6 & More](https://aitoolsreview.co.uk/insights/frontier-ai-benchmarks-september-2026)）；更早的一代中，Gemini 3 Pro 为 91.9%、GPT-5 Pro 88.4%、Claude Opus 4.5 87.0%（[Gemini 3 Pro vs Claude Opus 4.5 vs GPT-5](https://www.getmaxim.ai/articles/gemini-3-pro-vs-claude-opus-4-5-vs-gpt-5-the-ultimate-frontier-model-comparison/)）。AIME 方面，Gemma 4 31B 在 AIME 2026 上厂商自报 89.2%（[Gemma 4 31B](https://hokai.io/hub/models/gemma-4-31b)），GPT-5.4 Pro 在 OTIS Mock AIME 上为 96.1%（[Best Chatgpt Model for Math in 2026](https://www.cometapi.com/best-chatgpt-model-for-math-in-2026/)）。

## 核心基准详解

### Humanity's Last Exam（HLE）

由 Center for AI Safety（CAIS）与 Scale AI 于 2025 年 1 月联合发布，定位"人类知识前沿的多模态基准"，旨在成为同类最后的闭式学术基准；2025 年 4 月 3 日定稿为 2,500 道题，由数学、物理、化学、生物、计算机、古典语言、历史、哲学等研究生级领域专家贡献（[Humanity's Last Exam](https://scale.com/leaderboard/humanitys_last_exam)、[Humanity's Last Exam: The Knowledge Benchmark Built to Last](https://benchmarkingagents.com/hle-humanitys-last-exam/)）。2025 年 10 月 8 日又推出可持续提交题目的动态分支 HLE-Rolling（[Humanity's Last Exam: The AI Benchmark for LLM Reasoning](https://intuitionlabs.ai/pdfs/humanity-s-last-exam-the-ai-benchmark-for-llm-reasoning.pdf)）。**前沿分数**：2026 年 9 月，Claude Fable 5.1 以 65%、Claude Opus 5 64.7%、Claude Mythos 5 64.5% 领先（[Humanity's Last Exam (HLE)](https://benchlm.ai/benchmarks/hle)）；在 Artificial Analysis 的 AA-HLE 变体上，Claude Opus 5.5 以 61.4% 居首（[Artificial Analysis Humanity's Last Exam (AA-HLE)](https://benchlm.ai/benchmarks/aahle)）。HLE 是少数"最高分仍低于 65%"的基准之一（[HLE](https://benchgecko.ai/benchmark/hle)）。

### ARC-AGI 1/2/3

ARC-AGI 由 François Chollet 于 2019 年的论文《On the Measure of Intelligence》提出，用"抽象与推理语料"衡量流体智力，即在新任务上的技能获取效率（[ARC-AGI Series](https://arcprize.org/arc-agi)、[ARC-AGI-1](https://arcprize.org/arc-agi/1/)）。ARC-AGI-2 于 2025 年推出，是该框架最直接的落地（[ARC-AGI-2](https://aiwiki.ai/wiki/arc_agi_2/edit)）。**前沿分数**：2026 年 9 月，GPT-6 Astra 在 ARC-AGI-2 上达 95%、GPT-5.6 Sol 92.5%、Claude Opus 5 90.4%（[ARC-AGI v2](https://llm-stats.com/benchmarks/arc-agi-v2)）；而 GPT-5.2 仅为 52.9%，可见代际跃升之剧烈。ARC Prize 官方结果页列出 2026 年 9 月 22 日 GPT-6 Luna 在 ARC-AGI-1/2/3 上分别为 86.7%、59.3%、0.59%，Claude Opus 5.5 为 98.5%、93.3%（[Results](https://arcprize.org/results)）。在 ARC-AGI-1 上，跨模型集成方案公开 SOTA 达 94.5%，Claude Opus 4.6 以 93.0% 接近，且成本远低（[The ARC of Progress towards AGI](https://arxiv.org/html/2603.13372v1)）。

### SWE-bench Verified

面向自主软件工程的基准，要求 agent 生成能通过测试、解决真实 GitHub issue 的补丁；Verified 子集经人工筛选剔除问题样本，共 500 个任务（[AOrchestra](https://arxiv.org/html/2602.03786)）。2026 年 5 月，Claude Mythos Preview 以 93.9% 领先，但同一报道明确指出该基准存在较高的数据污染风险（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。

### LiveCodeBench / LiveCodeBench Pro

为对抗污染而设计：持续从 LeetCode、AtCoder、Codeforces 收集新题并按时间窗口评测，同时覆盖代码自修复、执行与测试输出预测等能力（[LiveCodeBench](https://livecodebench.github.io/)、[LiveCodeBench: Holistic and Contamination Free Evaluation](https://arxiv.org/pdf/2403.07974)）。LiveCodeBench Pro 聚焦竞赛题，2026 年 5 月由 Gemini 3.1 Pro 以 2887 Elo 领先（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。其"按发布时间切片"的设计恰好暴露了污染：模型在训练截止日之后发布的题目上"明显更差"，并在截止边界出现骤降，是记忆早期题目的典型特征（[A benchmark is not a control](https://vamshij.com/writing/a-benchmark-is-not-a-control/)）。

### LMArena（Chatbot Arena）

以人类两两盲测投票生成 Elo 分数，是最贴近用户主观偏好的榜单。2026 年 9 月，Claude Fable 5.1 以约 1507.58 的 Elo 位居榜首（[AI Model Leaderboard — Elo Rankings (2026)](https://prompeteer.ai/leaderboard)）；8 月的榜单显示 Fable 5 分数在 1506–1525 区间（[LMArena Leaderboard, August 2026](https://www.swfte.com/lmarena)）。该榜单同时提供价格与上下文信息，便于做性价比分析（[Text Arena 🏆 Overall](https://lmarena-ai-chatbot-arena.static.hf.space/index.html)）。

### τ-bench 与 Terminal-Bench

τ-bench 面向"工具-智能体-用户"交互与策略遵循，已从 τ-bench（2024）演进到 τ²-bench（2025，dual control）、τ-knowledge/τ-voice（2026，知识检索与实时语音）（[τ-bench](https://taubench.com/)）；其 v1.0.1 于 2026 年 7 月修复了 banking_knowledge 域的任务错误，并明确旧版结果与新版本不可直接比较（[tau2-bench README](https://raw.githubusercontent.com/sierra-research/tau2-bench/main/README.md)）。Terminal-Bench 2.1 于 2026 年修复了 2.0 版 89 个任务中的 28 个（[Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)）；其 4.0 版本被厂商用作编程/agent 能力指标，如 Grok 4.7 报告 Terminal-Bench 4.0 得 38.0%（[Grok 4.7 — SpaceXAI's September 2026 Grok Flagship](https://ai-tldr.dev/models/grok-4-7/)）。

## 趋势与争议

**污染（contamination）可测量且严重。** 对 MMLU 的抽样检测发现整体污染率约 13.8%，STEM 达 18.1%，哲学最高达 66.7%（[Are Large Language Models Truly Smarter Than Humans?](https://arxiv.org/html/2603.16197)）；另有研究在 15+ 模型、6 个多选题基准上测得污染率 1%–45%（[The Leaderboard Illusion](https://infinitigrid.com/blog/the-leaderboard-illusion)）。更棘手的是"软污染"：78% 的 CodeForces 题目与 50% 的 ZebraLogic 题目在训练数据中存在语义重复，且用语义重复样本微调能带来与精确重复相当的约 20% 提升，作者据此认为"近期能力提升被这种软污染所混淆"（[Do AI Benchmarks Still Matter?](https://awesomeagents.ai/leaderboards/do-ai-benchmarks-still-matter/)）。针对前沿模型的规模化测量亦显示高记忆率，例如 Claude Opus 4.5 在被测集合上记忆率约 55.9%（[Measuring Benchmark Data Contamination in Frontier Language Models at Scale](https://ne2ne.com/static/papers/contamination_paper.pdf)）。

**刷榜与饱和。** HumanEval 已被判定饱和并"退出前沿区分器行列"（集群在 93%–95%）（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。MMLU 亦被建议"仅在与 2024 年前模型做历史对比时引用"（[MMLU, MMLU-Pro, and MMMU](https://benchmarkingagents.com/mmlu/)）。ARC-AGI 的高分也引发"过拟合担忧"（[Gemini benchmark gains, ARC overfit concerns](https://zeronoise.ai/posts/gemini-benchmark-gains-arc-overfit-concerns-and-rising-pressure-on-trust-deepfakes-peer-review-robots-b00cnyy42p/download/pdf)）。

**单一指数与"科技公司自报"的风险。** Artificial Analysis Intelligence Index v4.3 把多个基准聚合成单一分数，2026 年由 Claude Fable 5.1 与 GPT-6 Astra 领跑、GLM-5.3 与 Kimi K3 领先开源权重（[Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)）。但业界共识是：不同基准的分数高度依赖推理协议、工具可用性与评测实现，跨来源直接比较易失真（[Test-Time Scaling in Reasoning LLMs](https://www.alphaxiv.org/abs/2608.04001)）；多份榜单聚合页也强调"每个分数都引用实验室发布或独立复跑"（[Every frontier AI model on every major benchmark](https://mungomash.com/ai/benchmarks/)）。

## 参考来源

1. [MMLU](https://aiwiki.ai/wiki/mmlu)
2. [Measuring Massive Multitask Language Understanding](https://arxiv.org/html/2009.03300v2)
3. [From BERT to Frontier Agents](https://arxiv.org/pdf/2608.13675)
4. [MMLU, MMLU-Pro, and MMMU](https://benchmarkingagents.com/mmlu/)
5. [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/pdf/2406.01574v1)
6. [MMLU-Pro: The Discriminating Successor to MMLU](https://benchmarkingagents.com/mmlu-pro/)
7. [Frontier AI Benchmarks Compared: Opus 5.5, GPT-6 & More](https://aitoolsreview.co.uk/insights/frontier-ai-benchmarks-september-2026)
8. [Gemini 3 Pro vs Claude Opus 4.5 vs GPT-5](https://www.getmaxim.ai/articles/gemini-3-pro-vs-claude-opus-4-5-vs-gpt-5-the-ultimate-frontier-model-comparison/)
9. [Gemma 4 31B](https://hokai.io/hub/models/gemma-4-31b)
10. [Best Chatgpt Model for Math in 2026](https://www.cometapi.com/best-chatgpt-model-for-math-in-2026/)
11. [Humanity's Last Exam](https://scale.com/leaderboard/humanitys_last_exam)
12. [Humanity's Last Exam: The Knowledge Benchmark Built to Last](https://benchmarkingagents.com/hle-humanitys-last-exam/)
13. [Humanity's Last Exam: The AI Benchmark for LLM Reasoning](https://intuitionlabs.ai/pdfs/humanity-s-last-exam-the-ai-benchmark-for-llm-reasoning.pdf)
14. [Humanity's Last Exam (HLE)](https://benchlm.ai/benchmarks/hle)
15. [Artificial Analysis Humanity's Last Exam (AA-HLE)](https://benchlm.ai/benchmarks/aahle)
16. [HLE](https://benchgecko.ai/benchmark/hle)
17. [ARC-AGI Series](https://arcprize.org/arc-agi)
18. [ARC-AGI-1](https://arcprize.org/arc-agi/1/)
19. [ARC-AGI-2](https://aiwiki.ai/wiki/arc_agi_2/edit)
20. [ARC-AGI v2](https://llm-stats.com/benchmarks/arc-agi-v2)
21. [Results](https://arcprize.org/results)
22. [The ARC of Progress towards AGI](https://arxiv.org/html/2603.13372v1)
23. [AOrchestra](https://arxiv.org/html/2602.03786)
24. [AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)
25. [LiveCodeBench](https://livecodebench.github.io/)
26. [LiveCodeBench: Holistic and Contamination Free Evaluation](https://arxiv.org/pdf/2403.07974)
27. [A benchmark is not a control](https://vamshij.com/writing/a-benchmark-is-not-a-control/)
28. [AI Model Leaderboard — Elo Rankings (2026)](https://prompeteer.ai/leaderboard)
29. [LMArena Leaderboard, August 2026](https://www.swfte.com/lmarena)
30. [Text Arena 🏆 Overall](https://lmarena-ai-chatbot-arena.static.hf.space/index.html)
31. [τ-bench](https://taubench.com/)
32. [tau2-bench README](https://raw.githubusercontent.com/sierra-research/tau2-bench/main/README.md)
33. [Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)
34. [Grok 4.7 — SpaceXAI's September 2026 Grok Flagship](https://ai-tldr.dev/models/grok-4-7/)
35. [Are Large Language Models Truly Smarter Than Humans?](https://arxiv.org/html/2603.16197)
36. [The Leaderboard Illusion](https://infinitigrid.com/blog/the-leaderboard-illusion)
37. [Do AI Benchmarks Still Matter?](https://awesomeagents.ai/leaderboards/do-ai-benchmarks-still-matter/)
38. [Measuring Benchmark Data Contamination in Frontier Language Models at Scale](https://ne2ne.com/static/papers/contamination_paper.pdf)
39. [Gemini benchmark gains, ARC overfit concerns](https://zeronoise.ai/posts/gemini-benchmark-gains-arc-overfit-concerns-and-rising-pressure-on-trust-deepfakes-peer-review-robots-b00cnyy42p/download/pdf)
40. [Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)
41. [Every frontier AI model on every major benchmark](https://mungomash.com/ai/benchmarks/)
42. [Test-Time Scaling in Reasoning LLMs](https://www.alphaxiv.org/abs/2608.04001)