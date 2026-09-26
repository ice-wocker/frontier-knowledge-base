# 大模型评测基准（Benchmarks）

> 最后更新：2026-09-26 ｜ 领域：人工智能·模型评测 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

评测基准（benchmark）是衡量大模型能力的标尺，也是厂商发布时的「成绩单」。一个基准通常由三要素定义：任务与数据（题目从哪来、如何标注）、评测协议（模型能否用工具、思考多少、允许几次尝试）与判定方式（精确匹配、测试通过、人类偏好投票）。理解基准时必须同时看这三者，否则分数难以解读。

2025–2026 年，基准生态呈现两条主线：一是经典知识类基准（MMLU 系列）快速饱和，失去区分度；二是新基准不断向「更难、更真实、更抗污染」演进——从 GPQA Diamond、AIME/MATH 到 Humanity's Last Exam（HLE）、ARC-AGI-2/3，再到 agent 化的 SWE-bench Verified、LiveCodeBench、τ-bench、Terminal-Bench。与此同时，数据污染（contamination）与刷榜（leaderboard gaming）成为普遍且可量化的系统性问题，单一聚合指数与「厂商自报分数」的可比性也持续受到质疑。

在实践中，解读一个基准分数至少需要同时追问四个问题：题目是否可能出现在训练数据中（污染）、评测时模型被允许使用哪些工具与多少思考预算（推理协议）、模型是否被针对该基准专门优化（过拟合/刷榜）、以及分数由谁复跑验证（厂商自报还是独立评估）。2025–2026 年的多起争议恰好分布在这四个维度上：从 MMLU 被测得的高污染率，到 ARC-AGI-3 上因评测脚手架不同而出现的悬殊分数，再到聚合指数改版引发的排名漂移。因此，本文件在列出分数时尽量并列多来源与多口径，并注明模型配置与是否使用工具。

## 2025–2026 最新进展

**知识基准饱和。** MMLU（Massive Multitask Language Understanding）由 Dan Hendrycks 等人于 2020 年 9 月提出、2021 年在 ICLR 发表，包含 57 个学科共 15,908 道题（[MMLU](https://aiwiki.ai/wiki/mmlu)、[Measuring Massive Multitask Language Understanding](https://arxiv.org/html/2009.03300v2)）。其分数从 GPT-3（2020）的 43.9% 升到 GPT-4（2023）的 86.4%、o1 的 91.8%（[From BERT to Frontier Agents](https://arxiv.org/pdf/2608.13675)），到 2026 年前沿模型已挤在 90% 出头的窄带内，差距不足两个百分点，落在 15,908 题测试的测量噪声内，被判定「已饱和、不再能区分前沿模型」（[MMLU, MMLU-Pro, and MMMU](https://benchmarkingagents.com/mmlu/)）。作为继任者，MMLU-Pro 通过增加选项、去除琐碎与噪声题，使准确率相对 MMLU 下降 16%–33%，并把对提示风格的敏感性从 4%–5% 降到约 2%（[MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/pdf/2406.01574v1)）。截至 2026 年 5 月，MMLU-Pro 前沿分数为 86%–89%，强开源模型为 81%–84%，呈现收敛（[MMLU-Pro: The Discriminating Successor to MMLU](https://benchmarkingagents.com/mmlu-pro/)）。

**面向高难推理的新基准。** GPQA Diamond 考察研究生级、经「Google-Proof」设计的科学问题，2026 年的前沿分数已进入 90% 以上：有追踪显示 Gemini 3.1 Pro 为 94.3%、Claude Opus 4.7 为 94.2%、Claude Mythos 5 为 94.1%（[GPQA Diamond](https://www.demandsphere.com/research/demandsphere-radar/ai-frontier-model-tracker/benchmarks/gpqa-diamond/)）；另一榜单列出 Gemini 3.1 Pro Preview（high）94.6%、Gemini 3.6 Flash（high）94.4%、GPT 5.5 Pre Release（xhigh）94.1%、Grok 4.6（high）94.0%（[GPQA Diamond Leaderboard](https://llmrun.dev/benchmark/gpqa-diamond?show=all)）；AIWiki 则记录截至 2026 年 9 月 3 日 GPT-6 Astra（xhigh）达 96.3%、Gemini 3.8 Flash（high）95.3%（[GPQA Diamond](https://aiwiki.ai/wiki/gpqa_diamond/edit)）。这些差距已很小，说明 GPQA Diamond 也趋于饱和，但其绝对难度仍高于 MMLU。AIME 方面，Gemma 4 31B 在 AIME 2026 上厂商自报 89.2%（[Gemma 4 31B](https://hokai.io/hub/models/gemma-4-31b)），GPT-5.4 Pro 在 OTIS Mock AIME 上为 96.1%（[Best Chatgpt Model for Math in 2026](https://www.cometapi.com/best-chatgpt-model-for-math-in-2026/)）。

**Agent 化与真实任务基准兴起。** SWE-bench 把评测对象从「回答问题」转向「修复真实 GitHub issue」，其 Verified 子集（500 题）成为编程 agent 的事实标准（[SWE-bench Verified](https://www.swebench.com/verified)）。2026 年 5 月，SWE-bench 官方发布 ProgramBench，用于评测模型能否从零编写有意义的软件工件（[SWE-bench](https://www.swebench.com/)）。为对抗污染，SWE-bench-Live 自 2026 年 8 月起强化提交校验：每个提交必须提供 agent 的 rollout 轨迹，以确认只向 agent 提供了问题描述与 Docker 镜像，避免 ground truth 泄漏，通过校验的提交才标注「Verified」（[SWE-bench-Live](https://swe-bench-live.github.io/)）。此外还有面向竞赛编程的 LiveCodeBench、面向工具-用户交互的 τ-bench、面向终端任务的 Terminal-Bench 等，共同把「自主性与可靠性」量化。

**评测从「答案」转向「过程与可靠性」。** 新一代 agent 基准不再只看最终答案，而是考核长程执行中的过程可靠性：SWE-bench 依赖运行真实测试来判定补丁是否正确，Terminal-Bench 需要修复任务自身缺陷以维持有效性，SWE-bench-Live 则要求提交 agent 轨迹来防止作弊。这种「过程化」趋势使评测更贴近真实部署场景，但也更依赖评测基础设施与人工维护，评测成本与维护负担显著上升，且任务质量（如不可解或泄漏的题目）会直接影响可比性（[SWE-bench-Live](https://swe-bench-live.github.io/)、[Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)）。

## 核心基准详解

### Humanity's Last Exam（HLE）

由 Center for AI Safety（CAIS）与 Scale AI 于 2025 年 1 月联合发布，定位「人类知识前沿的多模态基准」，旨在成为同类最后的闭式学术基准；2025 年 4 月 3 日定稿为 2,500 道题，由数学、物理、化学、生物、计算机、古典语言、历史、哲学等研究生级领域专家贡献（[Humanity's Last Exam](https://scale.com/leaderboard/humanitys_last_exam)、[Humanity's Last Exam: The Knowledge Benchmark Built to Last](https://benchmarkingagents.com/hle-humanitys-last-exam/)）。2025 年 10 月 8 日又推出可持续提交题目的动态分支 HLE-Rolling（[Humanity's Last Exam: The AI Benchmark for LLM Reasoning](https://intuitionlabs.ai/pdfs/humanity-s-last-exam-the-ai-benchmark-for-llm-reasoning.pdf)）。

HLE 的设计目标是把「闭式、可自动判定的学术知识」推到人类前沿，从而在饱和之前留出足够的区分空间；其 2,500 题规模与跨 100+ 学科的覆盖，使其更接近「知识广度与深度」的联合测试，而非单一学科能力。由于题目多来自最新研究或专家冷知识，模型能否作答高度依赖训练数据覆盖与检索能力，因此「有无工具」会带来显著分数差异（见上表 46.9% 对 64.7%）。（[Humanity's Last Exam](https://aiwiki.ai/wiki/humanity_s_last_exam/edit)）

**前沿分数（多口径并列）。** 2026 年 9 月，Claude Fable 5.1 以 65%、Claude Opus 5 64.7%、Claude Mythos 5 64.5% 领先（[Humanity's Last Exam (HLE)](https://benchlm.ai/benchmarks/hle)）；在 Artificial Analysis 的 AA-HLE 变体上，Claude Opus 5.5 以 61.4% 居首（[Artificial Analysis Humanity's Last Exam (AA-HLE)](https://benchlm.ai/benchmarks/aahle)）。另一份汇总给出 2026 年 5 月的对比表：HLE 前沿模型为 46.9%（无工具）、64.7%（有工具，实验室自报），人类专家约 90%，覆盖 100+ 学科（[Humanity's Last Exam](https://aiwiki.ai/wiki/humanity_s_last_exam/edit)）；一项面向 agentic AI 的报告则记录 2026 年 5 月 Claude Opus 4.7 以 54.7%（带工具）领先，Kimi K2.6 为 54.0%，并指出 HLE 发布时（2025 年 1 月）前沿模型仅有个位数分数（[The Jagged Topographic Frontier](https://rayuzwyshyn.net/UCRiverside2026/DeepResearchModelsPresentation/OriginalReports/Benchmarking_Agentic_AI_SynthesisUzwyshyn.pdf)）。HLE 是少数「最高分仍低于 65%」的基准之一（[HLE](https://benchgecko.ai/benchmark/hle)）。

### ARC-AGI 1/2/3

ARC-AGI 由 François Chollet 于 2019 年的论文《On the Measure of Intelligence》提出，用「抽象与推理语料」衡量流体智力，即在新任务上的技能获取效率（[ARC-AGI Series](https://arcprize.org/arc-agi)、[ARC-AGI-1](https://arcprize.org/arc-agi/1/)）。ARC-AGI-2 于 2025 年推出，是该框架最直接的落地（[ARC-AGI-2](https://aiwiki.ai/wiki/arc_agi_2/edit)）。

ARC-AGI 系列的特殊之处在于刻意避开语言与记忆，只测量「在新任务上获取技能」的效率，因此对训练数据污染的抵抗力更强，也更难靠单纯扩大规模直接碾压。ARC-AGI-3 的高难度与对交互式环境的要求，使其成为 2026 年「AGI 进度」讨论的焦点，但也正因评测协议复杂，不同 harness 的结果差异极大，解读时需格外谨慎。

**前沿分数（多口径并列）。** 2026 年 9 月，GPT-6 Astra 在 ARC-AGI-2 上达 95%、GPT-5.6 Sol 92.5%、Claude Opus 5 90.4%（[ARC-AGI v2](https://llm-stats.com/benchmarks/arc-agi-v2)）。ARC Prize 官方结果页列出 2026 年 9 月 22 日 GPT-6 Luna 在 ARC-AGI-1/2/3 上分别为 86.7%、59.3%、0.59%，Claude Opus 5.5 为 98.5%、93.3%（[Results](https://arcprize.org/results)）。另一汇总记录 Claude Fable 5.1 的系统卡首次给出 ARC-AGI-2 90%、ARC-AGI-1 97.5%（max effort，半私有验证集）（[Every frontier AI model on every major benchmark](https://mungomash.com/ai/benchmarks/)）。在 ARC-AGI-1 上，跨模型集成方案公开 SOTA 达 94.5%，Claude Opus 4.6 以 93.0% 接近，且成本远低（[The ARC of Progress towards AGI](https://arxiv.org/html/2603.13372v1)）。

ARC-AGI-3 是 2026 年的新前沿，难度骤升：半私有集上 Anthropic Claude Opus 4.6（max reasoning）仅 0.50%、Google Gemini 3.1 Pro（preview）0.40%、OpenAI GPT 5.4（high reasoning）0.20%、xAI Grok 4.20（beta）0.10%（[ARC-AGI 3](https://aiwiki.ai/wiki/arc-agi_3)）。但 ARC Prize 关于 GPT-6 Astra 的分析给出了差异极大的结果：在标准 harness 下 medium reasoning 为 38.6%、low 为 17.5%、none 为 35.2%；而换用 provider adapter harness 后分别达 98.4%、98.0%、96.7%（[OpenAI's GPT-6 Astra on ARC-AGI-3](https://arcprize.org/blog/astra)）。这说明 harness（评测脚手架）本身对分数的影响可能远大于模型代际差异。

### GPQA Diamond

研究生级、经「Google-Proof」设计的科学问答基准，多选题形式，人类专家约 81%、MMLU 人类约 89.8%（[Humanity's Last Exam](https://aiwiki.ai/wiki/humanity_s_last_exam/edit)）。2026 年前沿分数大多在 94%–96% 区间（见上文多口径来源），已接近饱和。另有榜单把 Muse Spark（Meta）列为 86%、Qwen3.5-397B MoE 为 78.2%、Llama-Nemotron Ultra 253B 为 70.5%（[GPQA Diamond: 2026 AI Leaderboard](https://aitooltier.com/benchmarks/gpqa-diamond)），可看出开源与非前沿闭源模型仍有明显差距。Epoch AI 指出，主要实验室自报的分数一般落在独立复跑评估的置信区间内（[GPQA Diamond](https://aiwiki.ai/wiki/gpqa_diamond/edit)）。

### SWE-bench Verified

面向自主软件工程的基准，要求 agent 生成能通过测试、解决真实 GitHub issue 的补丁；Verified 子集经人工筛选剔除问题样本，共 500 个任务，由人工标注者确认问题描述清晰、测试补丁正确、在给定信息下可解（[SWE-bench Verified](https://www.swebench.com/verified)）。2026 年 5 月，Claude Mythos Preview 以 93.9% 领先，但同一报道明确指出该基准存在较高的数据污染风险（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。开源侧，Live-SWE-agent 公示其 SWE-bench Verified 结果为 45.8%（Claude 4.5 Sonnet，2025-11-15）（[Live-SWE-agent](https://live-swe-agent.github.io/)）。

### LiveCodeBench / LiveCodeBench Pro

为对抗污染而设计：持续从 LeetCode、AtCoder、Codeforces 收集新题并按时间窗口评测，同时覆盖代码自修复、执行与测试输出预测等能力（[LiveCodeBench](https://livecodebench.github.io/)、[LiveCodeBench: Holistic and Contamination Free Evaluation](https://arxiv.org/pdf/2403.07974)）。LiveCodeBench Pro 聚焦竞赛题，2026 年 5 月由 Gemini 3.1 Pro 以 2887 Elo 领先（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。在按截断日期滚动的 pass-rate 上，DeepSeek-R1-0528 为 73.3%、o4-mini 为 72.8%、Qwen3-235B-A22B 为 70.7%（[Coding task router](https://www.codesota.com/code-generation)）。其「按发布时间切片」的设计恰好暴露了污染：模型在训练截止日之后发布的题目上「明显更差」，并在截止边界出现骤降，是记忆早期题目的典型特征（[A benchmark is not a control](https://vamshij.com/writing/a-benchmark-is-not-a-control/)）。

### LMArena（Chatbot Arena）

以人类两两盲测投票生成 Elo 分数，是最贴近用户主观偏好的榜单。2026 年 9 月，Claude Fable 5.1（max）以约 1507.58 的 Elo 位居榜首，Claude Opus 5（max）1504.96 次之（[AI Model Leaderboard — Elo Rankings (2026)](https://prompeteer.ai/leaderboard)）；8 月的榜单显示 Fable 5 分数在 1506–1525 区间、Opus 5 约 1522、GPT-5.6 Sol 约 1514（[LMArena Leaderboard, August 2026](https://www.swfte.com/lmarena)、[LMArena.ai, Top Models August 2026](https://www.swfte.com/it/ai/lmarena-ai)）。另有榜单以 Claude Opus 4.6 为 1,503、Gemini 3.1 Pro 为 1,494 分列前二（[Arena Elo Benchmark](https://lmmarketcap.com/zh/benchmarks/arena_elo)）。该榜单同时提供价格与上下文信息，便于做性价比分析（[Text Arena 🏆 Overall](https://lmarena-ai-chatbot-arena.static.hf.space/index.html)）。

需要指出，人类偏好投票衡量的是「用户主观偏好」，会受回答风格、长度与呈现方式影响，与能力型基准（GPQA Diamond、HLE）的排名并不总是一致，因此两类榜单应互补解读，而非互相替代。

### τ-bench 与 Terminal-Bench

τ-bench 面向「工具-智能体-用户」交互与策略遵循，已从 τ-bench（2024）演进到 τ²-bench（2025，dual control）、τ-knowledge/τ-voice（2026，知识检索与实时语音）（[τ-bench](https://taubench.com/)）；其 v1.0.1 于 2026 年 7 月修复了 banking_knowledge 域的任务错误，并明确旧版结果与新版本不可直接比较（[tau2-bench README](https://raw.githubusercontent.com/sierra-research/tau2-bench/main/README.md)）。Terminal-Bench 2.1 于 2026 年修复了 2.0 版 89 个任务中的 28 个（[Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)）；其 4.0 版本被厂商用作编程/agent 能力指标，如 Grok 4.7 报告 Terminal-Bench 4.0 得 38.0%（[Grok 4.7 — SpaceXAI's September 2026 Grok Flagship](https://ai-tldr.dev/models/grok-4-7/)）。

### Artificial Analysis Intelligence Index

该指数把多个基准聚合成单一分数，v4.3 版本在 2026 年由 Claude Fable 5.1 与 GPT-6 Astra 领跑、GLM-5.3 与 Kimi K3 领先开源权重（[Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)）。有报道指出，六个实验室已有模型在 Intelligence Index 上超过 50：Anthropic（Claude Fable 5，60）、OpenAI（GPT-5.6 Sol max，59）、Moonshot AI（Kimi K3，57）、SpaceXAI（Grok 4.5 high，54）、Z AI（GLM-5.2 max，51）与 Meta（Muse Spark）（[Four frontier launches in eight days](https://artificialanalysis.ai/articles/four-frontier-launches-in-eight-days-six-labs-now-field-a-model-above-50-on-the-artificial-analysis-intelligence-index)）。值得注意的是，指数版本更新本身会移动排名：有分析记录 v4.2 在重定价与调整私有测试集后，使 GPT-6 Astra「在没有新模型发布的情况下」上升四分（[Artificial Analysis Intelligence Index v4.2](https://pick-right.com/news/artificial-analysis-intelligence-index-v4-2-astra-repriced-private-test-sets-2026-09-07/)）。

## 关键数据速览（附来源）

下列数据仅汇总前文已引用的多口径结果，供快速对照；详细出处见各段就地标注与文末参考来源。

- **知识类**：MMLU 前沿约 90% 出头且已饱和（[MMLU, MMLU-Pro, and MMMU](https://benchmarkingagents.com/mmlu/)）；MMLU-Pro 前沿 86%–89%、强开源 81%–84%（[MMLU-Pro](https://benchmarkingagents.com/mmlu-pro/)）。
- **科学问答**：GPQA Diamond 前沿约 94%–96%，人类专家约 81%（[GPQA Diamond](https://aiwiki.ai/wiki/gpqa_diamond/edit)、[Humanity's Last Exam](https://aiwiki.ai/wiki/humanity_s_last_exam/edit)）。
- **抽象推理**：ARC-AGI-2 前沿约 90%–95%（部分口径），ARC-AGI-1 接近或超过 90%（[ARC-AGI v2](https://llm-stats.com/benchmarks/arc-agi-v2)、[Results](https://arcprize.org/results)）；ARC-AGI-3 半私有集普遍极低（0.1%–0.5%），但换用 provider adapter harness 后可升至 96% 以上（[ARC-AGI 3](https://aiwiki.ai/wiki/arc-agi_3)、[OpenAI's GPT-6 Astra on ARC-AGI-3](https://arcprize.org/blog/astra)）。
- **知识前沿**：HLE 前沿约 47%（无工具）至 65%（有工具），人类专家约 90%（[Humanity's Last Exam](https://aiwiki.ai/wiki/humanity_s_last_exam/edit)、[HLE](https://benchlm.ai/benchmarks/hle)）。
- **软件工程**：SWE-bench Verified 前沿约 90% 以上（存在污染争议），Live-SWE-agent 自报 45.8%（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)、[Live-SWE-agent](https://live-swe-agent.github.io/)）。
- **人类偏好**：LMArena Elo 前沿约 1500–1525（[AI Model Leaderboard — Elo Rankings (2026)](https://prompeteer.ai/leaderboard)、[LMArena Leaderboard, August 2026](https://www.swfte.com/lmarena)）。

需要强调，各基准的「前沿」随定义与时间快速变化，且同一模型在不同 harness、工具配置与 effort 下的分数差别可能很大，引用时必须注明版本、日期与配置。

## 趋势与争议

**污染（contamination）可测量且严重。** 对 MMLU 的抽样检测发现整体污染率约 13.8%，STEM 达 18.1%，哲学最高达 66.7%（[Are Large Language Models Truly Smarter Than Humans?](https://arxiv.org/html/2603.16197)）。一项跨 4,590 个「模型—问题」对的大规模测量发现整体污染率为 57.3%，全部 17 个模型都显示污染证据，开源权重模型（Llama、Mistral、DeepSeek、Qwen）系统性地更高（74%–79%），闭源 API 模型为 40%–64%，受污染最重的是维基百科衍生基准（如 HotpotQA、QuAC）（[Measuring Benchmark Data Contamination in Frontier Language Models at Scale](https://ne2ne.com/static/papers/contamination_paper.pdf)）。检测方法也在进步：ZCP 通过零 CoT 截断与同构扰动数据集区分「记忆」与「真实推理」，并提出「Contamination Confidence」度量（[The Illusion of Reasoning](https://arxiv.org/html/2605.21856v1)）；DVD 方法则在 Omni-MATH、SuperGPQA 上构建变体污染基准，优于困惑度、Min-k%、编辑距离与嵌入相似度等基线（[DVD: A Robust Method for Detecting Variant Contamination](https://arxiv.org/html/2601.04895v1)）。更棘手的是「软污染」：78% 的 CodeForces 题目与 50% 的 ZebraLogic 题目在训练数据中存在语义重复，且用语义重复样本微调能带来与精确重复相当的约 20% 提升，作者据此认为「近期能力提升被这种软污染所混淆」（[Do AI Benchmarks Still Matter?](https://awesomeagents.ai/leaderboards/do-ai-benchmarks-still-matter/)）。针对前沿模型的规模化测量亦显示高记忆率，例如 Claude Opus 4.5 在被测集合上记忆率约 55.9%（[Measuring Benchmark Data Contamination](https://ne2ne.com/static/papers/contamination_paper.pdf)）。

**刷榜与饱和。** HumanEval 已被判定饱和并「退出前沿区分器行列」（集群在 93%–95%）（[AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)）。MMLU 亦被建议「仅在与 2024 年前模型做历史对比时引用」（[MMLU, MMLU-Pro, and MMMU](https://benchmarkingagents.com/mmlu/)）。ARC-AGI 的高分也引发「过拟合担忧」（[Gemini benchmark gains, ARC overfit concerns](https://zeronoise.ai/posts/gemini-benchmark-gains-arc-overfit-concerns-and-rising-pressure-on-trust-deepfakes-peer-review-robots-b00cnyy42p/download/pdf)）。

**基准的可持续性成为设计目标。** 面对饱和与污染的双重压力，基准社区的方向是「持续更新、动态出题、公开评测协议」：LiveCodeBench 按发布时间切片持续收集新题，HLE 推出可滚动提交题目的分支，SWE-bench-Live 则要求提交 agent 轨迹以杜绝泄漏。这些机制共同的目标，是让基准在污染与过拟合面前尽可能长时间保持有效性（[LiveCodeBench](https://livecodebench.github.io/)、[Humanity's Last Exam](https://intuitionlabs.ai/pdfs/humanity-s-last-exam-the-ai-benchmark-for-llm-reasoning.pdf)、[SWE-bench-Live](https://swe-bench-live.github.io/)）。

**评测脚手架与「科技公司自报」的风险。** ARC-AGI-3 上标准 harness 与 provider adapter harness 的巨大差异表明，同一模型在不同评测脚手架下分数可以天差地别（[OpenAI's GPT-6 Astra on ARC-AGI-3](https://arcprize.org/blog/astra)）。业界共识是：不同基准的分数高度依赖推理协议、工具可用性与评测实现，跨来源直接比较易失真（[Test-Time Scaling in Reasoning LLMs](https://www.alphaxiv.org/abs/2608.04001)）；多份榜单聚合页也强调「每个分数都引用实验室发布或独立复跑」（[Every frontier AI model on every major benchmark](https://mungomash.com/ai/benchmarks/)）。因此，阅读榜单时应同时记录模型版本、effort/工具配置、harness 与数据版本。

**「单一分数」的诱惑与陷阱。** 把多个基准聚合成单一指数便于传播与横向比较，但指数对基准集合、权重与版本高度敏感：改版本身即可在没有新模型发布的情况下移动排名，因此指数更适合作为「概览入口」而非「精确结论」（[Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)、[Artificial Analysis Intelligence Index v4.2](https://pick-right.com/news/artificial-analysis-intelligence-index-v4-2-astra-repriced-private-test-sets-2026-09-07/)）。这也解释了为何同一时期不同榜单的「第一名」会不一致。

## 参考来源

1. [MMLU](https://aiwiki.ai/wiki/mmlu)
2. [Measuring Massive Multitask Language Understanding](https://arxiv.org/html/2009.03300v2)
3. [From BERT to Frontier Agents](https://arxiv.org/pdf/2608.13675)
4. [MMLU, MMLU-Pro, and MMMU](https://benchmarkingagents.com/mmlu/)
5. [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/pdf/2406.01574v1)
6. [MMLU-Pro: The Discriminating Successor to MMLU](https://benchmarkingagents.com/mmlu-pro/)
7. [GPQA Diamond (DemandSphere AI Frontier Model Tracker)](https://www.demandsphere.com/research/demandsphere-radar/ai-frontier-model-tracker/benchmarks/gpqa-diamond/)
8. [GPQA Diamond Leaderboard (llmrun)](https://llmrun.dev/benchmark/gpqa-diamond?show=all)
9. [GPQA Diamond (aiwiki)](https://aiwiki.ai/wiki/gpqa_diamond/edit)
10. [GPQA Diamond: 2026 AI Leaderboard](https://aitooltier.com/benchmarks/gpqa-diamond)
11. [Gemma 4 31B](https://hokai.io/hub/models/gemma-4-31b)
12. [Best Chatgpt Model for Math in 2026](https://www.cometapi.com/best-chatgpt-model-for-math-in-2026/)
13. [Humanity's Last Exam](https://scale.com/leaderboard/humanitys_last_exam)
14. [Humanity's Last Exam: The Knowledge Benchmark Built to Last](https://benchmarkingagents.com/hle-humanitys-last-exam/)
15. [Humanity's Last Exam: The AI Benchmark for LLM Reasoning](https://intuitionlabs.ai/pdfs/humanity-s-last-exam-the-ai-benchmark-for-llm-reasoning.pdf)
16. [Humanity's Last Exam (HLE)](https://benchlm.ai/benchmarks/hle)
17. [Artificial Analysis Humanity's Last Exam (AA-HLE)](https://benchlm.ai/benchmarks/aahle)
18. [Humanity's Last Exam (aiwiki)](https://aiwiki.ai/wiki/humanity_s_last_exam/edit)
19. [The Jagged Topographic Frontier](https://rayuzwyshyn.net/UCRiverside2026/DeepResearchModelsPresentation/OriginalReports/Benchmarking_Agentic_AI_SynthesisUzwyshyn.pdf)
20. [HLE](https://benchgecko.ai/benchmark/hle)
21. [ARC-AGI Series](https://arcprize.org/arc-agi)
22. [ARC-AGI-1](https://arcprize.org/arc-agi/1/)
23. [ARC-AGI-2](https://aiwiki.ai/wiki/arc_agi_2/edit)
24. [ARC-AGI v2](https://llm-stats.com/benchmarks/arc-agi-v2)
25. [Results (ARC Prize)](https://arcprize.org/results)
26. [Every frontier AI model on every major benchmark](https://mungomash.com/ai/benchmarks/)
27. [The ARC of Progress towards AGI](https://arxiv.org/html/2603.13372v1)
28. [ARC-AGI 3](https://aiwiki.ai/wiki/arc-agi_3)
29. [OpenAI's GPT-6 Astra on ARC-AGI-3](https://arcprize.org/blog/astra)
30. [SWE-bench](https://www.swebench.com/)
31. [SWE-bench Verified](https://www.swebench.com/verified)
32. [SWE-bench-Live](https://swe-bench-live.github.io/)
33. [Live-SWE-agent](https://live-swe-agent.github.io/)
34. [LiveCodeBench](https://livecodebench.github.io/)
35. [LiveCodeBench: Holistic and Contamination Free Evaluation](https://arxiv.org/pdf/2403.07974)
36. [Coding task router](https://www.codesota.com/code-generation)
37. [A benchmark is not a control](https://vamshij.com/writing/a-benchmark-is-not-a-control/)
38. [AI Model Leaderboard — Elo Rankings (2026)](https://prompeteer.ai/leaderboard)
39. [LMArena Leaderboard, August 2026](https://www.swfte.com/lmarena)
40. [LMArena.ai, Top Models August 2026](https://www.swfte.com/it/ai/lmarena-ai)
41. [Arena Elo Benchmark](https://lmmarketcap.com/zh/benchmarks/arena_elo)
42. [Text Arena 🏆 Overall](https://lmarena-ai-chatbot-arena.static.hf.space/index.html)
43. [τ-bench](https://taubench.com/)
44. [tau2-bench README](https://raw.githubusercontent.com/sierra-research/tau2-bench/main/README.md)
45. [Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1)
46. [Grok 4.7 — SpaceXAI's September 2026 Grok Flagship](https://ai-tldr.dev/models/grok-4-7/)
47. [Announcing the Artificial Analysis Intelligence Index v4.3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-3)
48. [Four frontier launches in eight days](https://artificialanalysis.ai/articles/four-frontier-launches-in-eight-days-six-labs-now-field-a-model-above-50-on-the-artificial-analysis-intelligence-index)
49. [Artificial Analysis Intelligence Index v4.2](https://pick-right.com/news/artificial-analysis-intelligence-index-v4-2-astra-repriced-private-test-sets-2026-09-07/)
50. [Are Large Language Models Truly Smarter Than Humans?](https://arxiv.org/html/2603.16197)
51. [Measuring Benchmark Data Contamination in Frontier Language Models at Scale](https://ne2ne.com/static/papers/contamination_paper.pdf)
52. [The Illusion of Reasoning: Exposing Evasive Data Contamination in LLMs via Zero-CoT Truncation](https://arxiv.org/html/2605.21856v1)
53. [DVD: A Robust Method for Detecting Variant Contamination](https://arxiv.org/html/2601.04895v1)
54. [Do AI Benchmarks Still Matter?](https://awesomeagents.ai/leaderboards/do-ai-benchmarks-still-matter/)
55. [AI Agent Benchmark Roundup May 2026](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)
56. [Gemini benchmark gains, ARC overfit concerns](https://zeronoise.ai/posts/gemini-benchmark-gains-arc-overfit-concerns-and-rising-pressure-on-trust-deepfakes-peer-review-robots-b00cnyy42p/download/pdf)
57. [Test-Time Scaling in Reasoning LLMs](https://www.alphaxiv.org/abs/2608.04001)
58. [AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration](https://arxiv.org/html/2602.03786)