# 数学前沿

> 最后更新：2026-09-26 ｜ 领域：科学·数理与材料 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

数学前沿通常由三类事件标记：顶级奖项的颁发（菲尔兹奖等）、长期悬而未决猜想被证明或推翻，以及人工智能开始实质性介入数学研究与证明流程。2025–2026 年，这三条线索同时出现了值得记录的进展：三维 Kakeya 猜想被证明、ICM 2026 颁发新一届菲尔兹奖，以及多个 AI 系统在国际数学奥林匹克（IMO）与研究工作层面取得突破。

## 最新进展（2025–2026）

### 三维 Kakeya 猜想被证明

2025 年初，王虹（Hong Wang，纽约大学 Courant 数学科学研究所与 IHES）与 Joshua Zahl 在 arXiv 发表论文，证明了三维空间中的 Kakeya 猜想。在此之前，二维（n=2）情形早已被证明，而三维情形长期是该猜想最关键的开放环节。（[A Closer Look at Kakeya's Conjecture](https://www.polytechnique.edu/en/news/closer-look-kakeyas-conjecture)）

### 2026 年菲尔兹奖

2026 年 7 月 23 日，在美国费城举行的国际数学家大会（ICM 2026）开幕式上，国际数学联盟（IMU）公布了 2026 年菲尔兹奖得主，共四人：Yu Deng（邓煜）、Hong Wang（王虹）、John Pardon、Jacob Tsimerman。（[2026 Fields Medals](https://www.claymath.org/news/2026-fields-medals/)）（[Update: Chinese mathematicians Deng Yu, Wang Hong awarded Fields Medals](https://english.news.cn/20260724/93beba493cfd4385973e388bcef2782f/c.html)）据 Clay 数学研究所，邓煜的获奖理由涉及其在偏微分方程方面的工作；王虹是菲尔兹奖历史上第三位女性得主。（[2026 Fields Medals](https://www.claymath.org/news/2026-fields-medals/)）（[2026 Fields Medal: Meet the Four Laureates](https://impa.br/notices/2026-fields-medal-meet-the-four-laureates/?lang=en)）多家机构提到，邓煜、John Pardon 的部分数学训练分别与 MIT 相关。（[MIT Mathematics](https://math.mit.edu/?ref=list)）

### AI 与数学证明

- **IMO 与形式化证明**：Google DeepMind 的 AlphaProof 在 2024 年 IMO 上达到银牌水平，它把一个预训练语言模型与 AlphaZero 式强化学习结合，在 Lean 证明环境中运行，并用自动形式化的约 8000 万条自然语言题面来引导自对弈循环。（[AI for Mathematics — Proving, Formalizing & Conjecturing](https://jimmyresearch.com/modules/aifs-mathematics/)）2025 年，Harmonic 的 Aristotle 在 IMO 上达到金牌水平，字节跳动的 SEED Prover 达到银牌水平；值得注意的是，这些能够产出形式化证明的 AI 系统均使用 Lean。（[Lean: Machine-Checked Mathematics](https://leodemoura.github.io/static/shanghai2026/)）
- **AI 破解长期猜想**：2026 年 5 月，据英国《新科学家》报道（参考消息转载），OpenAI 开发的人工智能模型破解了一个困扰数学家 80 年的数学猜想，布里斯托尔大学数学家 Misha Rudnev 称其为「人工智能数学能力的震撼时刻」。（[AI破解困扰人类80年数学猜想](http://www.xinhuanet.com/liangzi/20260528/2f21ea4e942b4daba9a485e3b14c034f/c.html)）2026 年 8 月，据 ScienceDaily 转述，一位在 Anthropic 工作的数学家称使用 AI 模型（文中称 Claude Fable 5）找到一个异常简单的反例，推翻了雅可比猜想（Jacobian conjecture）：该猜想在三维及以上维度为假，而其原始的二维版本仍未解决。（[Claude Fable 5 AI finds a tiny formula that topples an 87-year-old math conjecture](https://sciencedaily.com/releases/2026/08/260804034634.htm)）
- **形式化证明搜索系统**：Google DeepMind 提出 AlphaProof Nexus，把通用语言模型与 Lean 证明助手组成智能体式循环，将每一步候选证明提交给 Lean 编译器，并利用编译错误信息引导下一次尝试，相关预印本于 2026 年 5 月发布在 arXiv。（[AlphaProof Nexus](https://aiwiki.ai/wiki/alphaproof_nexus)）

## 核心技术与关键概念

- **Kakeya 猜想（挂谷猜想）**：讨论在空间中转动单位线段所需的最小集合面积/测度问题，是调和分析与几何测度论的核心猜想之一。
- **雅可比猜想（Jacobian conjecture）**：关于多项式映射雅可比行列式为非零常数时是否可逆的代数几何猜想。
- **形式化数学与证明助手**：Lean 等系统把数学证明转化为机器可逐步检验的形式代码，使 AI 生成的证明可以被自动验证，是 AI 进入数学研究的关键基础设施。（[Lean: Machine-Checked Mathematics](https://leodemoura.github.io/static/shanghai2026/)）
- **自动形式化（autoformalization）**：把自然语言题面自动翻译为形式化陈述的过程，为强化学习提供训练素材。
- **千禧年大奖难题（Millennium Prize Problems）**：Clay 数学研究所设七道题、每题 100 万美元悬赏。黎曼假设（Riemann Hypothesis）仍是其中之一；其非平凡零点位于临界线上的假设至今未被证明，早期工作已借助 Odlyzko–Schönhage 算法计算验证了前 10¹³ 个零点。（[The Riemann Hypothesis](https://riemann-hypothesis.dev/)）

## 代表性项目 / 机构 / 产品

- **AlphaProof / AlphaProof Nexus**（Google DeepMind）：形式化数学证明搜索系统，与 Lean 深度集成。（[AI for Mathematics](https://jimmyresearch.com/modules/aifs-mathematics/)）（[AlphaProof Nexus](https://aiwiki.ai/wiki/alphaproof_nexus)）
- **Aristotle**（Harmonic）：2025 年 IMO 达到金牌水平的形式化证明系统。（[Lean: Machine-Checked Mathematics](https://leodemoura.github.io/static/shanghai2026/)）
- **SEED Prover**（字节跳动）：2025 年 IMO 达到银牌水平。（[Lean: Machine-Checked Mathematics](https://leodemoura.github.io/static/shanghai2026/)）
- **Lean**（Lean FRO / Leonardo de Moura）：被上述各 AI 系统共同采用的形式化证明平台。（[Lean: Machine-Checked Mathematics](https://leodemoura.github.io/static/shanghai2026/)）
- **Clay 数学研究所（Clay Mathematics Institute）**：千禧年难题与菲尔兹奖公告的权威来源之一。（[2026 Fields Medals](https://www.claymath.org/news/2026-fields-medals/)）
- **国际数学家大会（ICM 2026）**：2026 年 7 月在费城举行，颁发菲尔兹奖。

## 关键数据与评测结果（附来源）

| 事项 | 数据 | 来源 |
| --- | --- | --- |
| ICM 2026 菲尔兹奖人数 | 4 人（Yu Deng、Hong Wang、John Pardon、Jacob Tsimerman） | [Clay](https://www.claymath.org/news/2026-fields-medals/) |
| 王虹历史地位 | 第三位女性菲尔兹奖得主 | [IMPA](https://impa.br/notices/2026-fields-medal-meet-the-four-laureates/?lang=en) |
| AlphaProof IMO 成绩 | 2024 年银牌 | [jimmyresearch](https://jimmyresearch.com/modules/aifs-mathematics/) |
| AlphaProof 自动形式化规模 | 约 8000 万条自然语言题面 | [jimmyresearch](https://jimmyresearch.com/modules/aifs-mathematics/) |
| Aristotle / SEED Prover IMO 2025 | 金牌 / 银牌 | [leodemoura](https://leodemoura.github.io/static/shanghai2026/) |
| 黎曼假设已验证零点数 | 前 10¹³ 个 | [riemann-hypothesis.dev](https://riemann-hypothesis.dev/) |

## 趋势与争议

1. **AI 从「竞赛数学」走向「研究数学」**：从 IMO 到破解长期猜想，AI 的介入点正从解题扩展到提出反例与探索开放性猜想，但相关成果多为预印本或媒体转述，尚需学界同行评议与更广泛复现。
2. **形式化与非形式化的分歧**：机器可验证的形式化证明（Lean）提供了可靠性的客观标准，但成本高、覆盖有限；非形式化证明更贴近数学家日常工作，却难以自动验证。
3. **AI 成果的归因与署名争议**：当 AI 参与发现反例或证明时，人类数学家的贡献界定、成果署名与可信度评估成为新问题。
4. **千禧年难题仍开放**：黎曼假设等核心难题未解决，围绕其「无条件证明」偶有非主流论文出现，需以权威机构与同行评议为准。

## 参考来源

- [A Closer Look at Kakeya's Conjecture — École polytechnique](https://www.polytechnique.edu/en/news/closer-look-kakeyas-conjecture)
- [2026 Fields Medals — Clay Mathematics Institute](https://www.claymath.org/news/2026-fields-medals/)
- [Update: Chinese mathematicians Deng Yu, Wang Hong awarded Fields Medals — Xinhua](https://english.news.cn/20260724/93beba493cfd4385973e388bcef2782f/c.html)
- [2026 Fields Medal: Meet the Four Laureates — IMPA](https://impa.br/notices/2026-fields-medal-meet-the-four-laureates/?lang=en)
- [MIT Mathematics](https://math.mit.edu/?ref=list)
- [AI for Mathematics — Proving, Formalizing & Conjecturing](https://jimmyresearch.com/modules/aifs-mathematics/)
- [Lean: Machine-Checked Mathematics — Leonardo de Moura](https://leodemoura.github.io/static/shanghai2026/)
- [AlphaProof Nexus](https://aiwiki.ai/wiki/alphaproof_nexus)
- [AI破解困扰人类80年数学猜想 — 新华网](http://www.xinhuanet.com/liangzi/20260528/2f21ea4e942b4daba9a485e3b14c034f/c.html)
- [Claude Fable 5 AI finds a tiny formula that topples an 87-year-old math conjecture — ScienceDaily](https://sciencedaily.com/releases/2026/08/260804034634.htm)
- [The Riemann Hypothesis](https://riemann-hypothesis.dev/)