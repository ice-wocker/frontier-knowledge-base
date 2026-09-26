# 化学与催化

> 最后更新：2026-09-26 ｜ 领域：科学·数理与材料 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

化学与催化前沿在 2025–2026 年的核心特征，是「AI 与自动化」对传统合成化学与催化研发流程的系统性渗透：从反应产率预测、逆设计催化剂，到由 AI 智能体自主规划并执行实验的闭环工作流，方法学层面出现大量新工具；与此同时，电催化与光催化在能源转化方向上持续产出高性能催化剂，金属有机框架（MOF）的基础性贡献则获得 2025 年诺贝尔化学奖的确认。

## 最新进展（2025–2026）

### 2025 年诺贝尔化学奖：金属有机框架

2025 年 10 月 8 日，瑞典皇家科学院决定将 2025 年诺贝尔化学奖授予 Susumu Kitagawa（京都大学）、Richard Robson（墨尔本大学）与 Omar M. Yaghi（加州大学伯克利分校），表彰他们「金属有机框架的开发」。诺奖委员会称，他们创造的分子构造「为化学留出了新的空间」。（[Press release: Nobel Prize in Chemistry 2025 — NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/press-release/)）（[三名科学家因金属有机框架研究获2025年诺贝尔化学奖 — 新华网](http://www.news.cn/20251008/5992987c39d14d4182092c32d546af4a/c.html)）MOF 是由金属节点与有机配体自组装形成的多孔晶体材料，在气体存储、分离、催化与能源领域应用广泛。（[Nobel Prize in Chemistry 2025 — NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/popular-information/)）

### AI 与计算化学

- **合成适用域（SynAD）框架**：清华大学的罗三中团队提出「合成适用域」（SynAD）框架，针对 AI 模型对未知反应预测失效的问题，通过距离度量算法定量评估产率预测的可靠性，可有效区分可预测与不可预测的反应，为 Ullmann 等反应的反应预测模型提供判别标准。（[清华大学基础分子科学中心 — 研究动态](https://cbms.chem.tsinghua.edu.cn/column/research)）
- **AI 智能体辅助催化剂设计**：有研究报告了 AI 智能体辅助的镍基催化剂设计策略，通过内置电场（BEF）增强生物质电氧化——将 5-羟甲基糠醛（HMF）氧化为 2,5-呋喃二甲酸（FDCA）；AI 智能体自主识别出 Mn 掺杂是构建 BEF、同时优化电子结构与界面微环境的手段。（[AI-Agent-Guided Design of Dual-Scale Modulated Nickel-Based Catalyst — ACS Nano](https://pubs.acs.org/doi/10.1021/acsnano.6c00124?goto=supporting-info)）
- **AI 引导的高通量催化剂发现**：有工作用 AI 引导高通量筛选，发现不含铱、钌的钯氧化物催化剂，用于耐久的酸性析氧反应，在超过 1000 小时运行中过电位保持在 0.5 V 以下。（[AI-guided high-throughput discovery of iridium- and ruthenium-free palladium-oxide catalysts — arXiv](https://arxiv.org/abs/2609.30133)）
- **高熵电催化剂的逆设计**：研究者提出基于主动学习的逆设计框架，结合条件生成对抗网络、原子图注意力网络、k 近邻与高通量 DFT 计算，降低高熵电催化剂（HEEC）设计所需的训练数据量，系统探索 Ni、Co、Fe 等组成空间。（[Boosting Screening of Nonequiatomic High-Entropy Electrocatalysts by Inverse Design via Active Graph Learning — ACS Catalysis](https://pubs.acs.org/doi/abs/10.1021/acscatal.5c05945)）
- **自主 AI 智能体用于 ORR 催化剂发现**：一篇综述指出，自主 AI 智能体正成为析氧/氧还原（ORR）催化剂发现的新角色，其将大语言模型、结构化知识图谱与机器人高通量实验整合，可自主设计、执行、分析并改进实验，成功关键在于从简单自动化转向高保真发现。（[Autonomous AI agents in ORR electrocatalyst discovery — RSC Materials Advances](https://pubs.rsc.org/es-mx/content/articlepdf/2026/ma/d6ma00429f?page=search)）

### 电催化与光催化

上述电催化方向集中体现了当前热点：酸性析氧反应（OER）、生物质电氧化（HMF→FDCA）、氧还原反应（ORR）等，均以「低贵金属/无贵金属 + 高耐久」为关键目标。（[arXiv 2609.30133](https://arxiv.org/abs/2609.30133)）（[ACS Nano](https://pubs.acs.org/doi/10.1021/acsnano.6c00124?goto=supporting-info)）相关研究普遍结合密度泛函理论（DFT）计算、主动学习与自动化实验。

## 核心技术与关键概念

- **金属有机框架（MOF）**：金属节点 + 有机配体自组装多孔晶体，具超高比表面积与结构可设计性。（[NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/press-release/)）
- **合成适用域（SynAD）**：衡量 AI 反应预测模型在其训练分布之外的可靠性，类似「域外检测」思想。（[清华 CBMS](https://cbms.chem.tsinghua.edu.cn/column/research)）
- **逆设计（inverse design）与主动学习**：给定目标性能反向搜索组成/结构，并用主动学习迭代减少所需标注数据。（[ACS Catalysis](https://pubs.acs.org/doi/abs/10.1021/acscatal.5c05945)）
- **内置电场（built-in electric field, BEF）**：通过掺杂等手段在催化剂内部构建电场，优化电子结构与界面微环境。（[ACS Nano](https://pubs.acs.org/doi/10.1021/acsnano.6c00124?goto=supporting-info)）
- **自主实验室 / 闭环工作流**：LLM + 知识图谱 + 机器人高通量实验，实现「设计-执行-分析-改进」自治循环。（[RSC Materials Advances](https://pubs.rsc.org/es-mx/content/articlepdf/2026/ma/d6ma00429f?page=search)）
- **电催化关键反应**：OER、ORR、HMF 氧化等，是能源转化与绿色合成的核心。（[arXiv](https://arxiv.org/abs/2609.30133)）

## 代表性项目 / 机构 / 产品

- **MOF 奠基三人组**（Kitagawa / Robson / Yaghi）：2025 年诺贝尔化学奖。（[NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/press-release/)）
- **清华大学罗三中团队**：SynAD 框架。（[清华 CBMS](https://cbms.chem.tsinghua.edu.cn/column/research)）
- **Pd 氧化物酸性 OER 催化剂**：AI 引导高通量发现。（[arXiv](https://arxiv.org/abs/2609.30133)）
- **高熵电催化剂主动学习逆设计框架**。（[ACS Catalysis](https://pubs.acs.org/doi/abs/10.1021/acscatal.5c05945)）

## 关键数据与评测结果（附来源）

| 事项 | 数据 | 来源 |
| --- | --- | --- |
| 2025 诺贝尔化学奖 | Kitagawa / Robson / Yaghi（MOF） | [NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/press-release/) |
| AI 催化剂耐久性 | 酸性 OER 过电位 <0.5 V，运行 >1000 h | [arXiv 2609.30133](https://arxiv.org/abs/2609.30133) |
| SynAD 目标 | 区分可预测/不可预测反应 | [清华 CBMS](https://cbms.chem.tsinghua.edu.cn/column/research) |
| HMF→FDCA | Ni 基催化剂 + 内置电场 | [ACS Nano](https://pubs.acs.org/doi/10.1021/acsnano.6c00124?goto=supporting-info) |

## 趋势与争议

1. **AI 预测的可靠边界**：SynAD 等工作表明，模型在训练分布外的反应预测可能失效，可靠性评估与域外检测成为必需。（[清华 CBMS](https://cbms.chem.tsinghua.edu.cn/column/research)）
2. **自动化与「高保真发现」**：业界强调自主实验室不能止步于简单自动化，需结合物理信息机器学习与稳健代理模型。（[RSC Materials Advances](https://pubs.rsc.org/es-mx/content/articlepdf/2026/ma/d6ma00429f?page=search)）
3. **贵金属依赖与耐久性**：电催化追求以非贵金属实现高耐久，是能源转化的成本与可持续性关键。
4. **计算与实验的融合程度**：DFT + 主动学习 + 机器人实验的闭环仍处早期，数据标准与可复现性有待完善。

## 参考来源

- [Press release: Nobel Prize in Chemistry 2025 — NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/press-release/)
- [Nobel Prize in Chemistry 2025 — Popular information — NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/popular-information/)
- [三名科学家因金属有机框架研究获2025年诺贝尔化学奖 — 新华网](http://www.news.cn/20251008/5992987c39d14d4182092c32d546af4a/c.html)
- [研究动态 — 清华大学基础分子科学中心](https://cbms.chem.tsinghua.edu.cn/column/research)
- [AI-Agent-Guided Design of Dual-Scale Modulated Nickel-Based Catalyst — ACS Nano](https://pubs.acs.org/doi/10.1021/acsnano.6c00124?goto=supporting-info)
- [AI-guided high-throughput discovery of iridium- and ruthenium-free palladium-oxide catalysts — arXiv](https://arxiv.org/abs/2609.30133)
- [Boosting Screening of Nonequiatomic High-Entropy Electrocatalysts by Inverse Design via Active Graph Learning — ACS Catalysis](https://pubs.acs.org/doi/abs/10.1021/acscatal.5c05945)
- [Autonomous AI agents in ORR electrocatalyst discovery — RSC Materials Advances](https://pubs.rsc.org/es-mx/content/articlepdf/2026/ma/d6ma00429f?page=search)