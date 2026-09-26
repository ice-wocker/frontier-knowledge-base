# 重构与遗留系统现代化（Refactoring and Legacy Modernization）

> 最后更新：2026-09-26 ｜ 领域：软件工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

重构指在不改变外部可观察行为的前提下改善代码内部结构；遗留系统现代化则把重构的粒度放大到系统级，目标是替换或改造长期运行、难以变更、技术栈过时的业务系统。两者共享同一前提：必须有办法判断「行为未变」。

Michael Feathers 在《Working Effectively with Legacy Code》中把遗留代码定义为「没有测试的代码」，而不论其年代；这一重新界定很重要，因为大量工程投入恰恰发生在无测试的代码上（[How to Refactor Legacy Code with AI Agents (2026)](https://getunblocked.com/blog/refactoring-legacy-code/)）。因此现代化的第一步通常是补建「特性化测试」（characterization tests）等安全网，再开始结构性改造。

## 最新进展（2025–2026）

**1. 绞杀者模式（Strangler Fig）成为 2026 年现代化的主流策略。** 该模式最初由 Martin Fowler 描述，做法是先选定要现代化的一块业务区域，以独立服务或应用构建现代版本并定义清晰的 API 边界，再由路由层逐步把流量切到新组件，旧模块在被替代后逐渐退役（[Legacy Modernization for the AI Era](https://aptibit.com/blog/legacy-modernization-enterprise-ai-era)）。2026 年的实践纪律明确倾向「绞杀者 + AI 加速」，而反对一次性替换整个遗留资产的大爆炸（big-bang）方案——后者制造了 2010 年代被广泛报道的大多数失败案例（[Legacy Modernization at AI Speed: The 6R Framework Meets GenAI Discipline](https://www.practicallogix.com/legacy-modernization-at-ai-speed-the-6r-framework-meets-genai-discipline)）。绞杀者模式的价值在于可以在每个功能点回滚，而不是把风险押在单一的多年度里程碑上（[Enterprise Software Modernization: Legacy System Migration Strategies for 2026](https://www.ainformat.com/detail/502)）。

**2. AI 辅助重构进入工程化阶段。** Martin Fowler 团队在为客户做现代化实验时，构建了名为 CodeConcise 的工具，把大语言模型与「从代码 AST 派生的知识图谱」结合；该组合在提取低层需求和构建高层说明两方面都取得了正向结果（[Martin Fowler — tagged by: legacy modernization](https://www.martinfowler.com/tags/legacy%20modernization.html)）。Fowler 还用「Research, Review, Rebuild」概括一种结构化工作流：由具备领域经验的工程师来准确解读需求、验证 AI 生成结果，从而让 AI 生成的代码在复杂的棕地项目中加速交付，同时避免代码库碎片化与技术债累积（[Research, Review, Rebuild](https://www.martinfowler.com/articles/research-review-rebuild.html)）。

**3. 厂商侧出现专用现代化产品。** Amazon Q Developer 的代码转换能力支持 Java 版本升级，例如从 Java 8 或 Java 11 升级到 Java 17 / Java 21（[Upgrading Java versions with Amazon Q Developer](https://docs.aws.amazon.com/en_en/amazonq/latest/qdeveloper-ug/code-transformation.html)）。针对主机（mainframe）场景，AWS Transform 的重构能力可自动把 COBOL 转换为 Java、把 JCL 转换为 Groovy 脚本，并以人类在环（human-in-the-loop）的顺序按业务域推进重构，声称保持功能等价（[Accelerate Your Mainframe Modernization Journey using AI Agents with AWS Transform](https://aws.amazon.com/blogs/migration-and-modernization/accelerate-your-mainframe-modernization-journey-using-ai-agents-with-aws-transform/)）。

**4. 技术债的量化数据持续累积。** Deloitte 的 2026 年全球技术领导力研究把技术债占 IT 年度支出的比例估在 21%–40%（[Technical Debt: The Cost That Never Makes the Agenda](https://www.liferay.com/b/technical-debt-the-cost-that-never-makes-the-agenda)）；JetBrains《State of Developer Ecosystem 2025》的数据称工程师每月因技术债损失 2–5 个工作日，相当于高达 25% 的工程预算（[Technical Debt: What It Costs and How to Pay It Down](https://dimitriadis.eu/en/articles/technische-schulden-was-sie-kosten-und-wie-man-sie-abbaut)）。

## 核心技术与关键概念

- **绞杀者模式（Strangler Fig）**：新旧系统并行运行，通过路由层渐进切流，最终置换旧系统；适用于大型、业务关键且不可接受一次性替换风险的系统（[Legacy System Modernisation with AI](https://www.moweb.com/blog/legacy-system-modernisation-ai-enterprise-upgrade)）。
- **大爆炸（big-bang）替换的失败模式**：试图在一个计划内现代化整个遗留资产；2026 年的现代化纪律明确规避该路径（[practicallogix.com](https://www.practicallogix.com/legacy-modernization-at-ai-speed-the-6r-framework-meets-genai-discipline)）。
- **6R 现代化框架**：与 GenAI 结合使用的经典迁移/改造决策框架（[practicallogix.com](https://www.practicallogix.com/legacy-modernization-at-ai-speed-the-6r-framework-meets-genai-discipline)）。
- **知识图谱 + LLM**：以 AST 派生的知识图谱补足 LLM 对大型代码库结构理解的不足，用于需求提取与代码解释（[martinfowler.com](https://www.martinfowler.com/tags/legacy%20modernization.html)）。
- **agentic programming（智能体式编程）**：Fowler 将其定义为人类提示 LLM 智能体生成代码、再评审其结果的新开发模式，并区别于「完全不看代码」的 vibe coding 与简单代码补全；其核心技能转向 harness engineering（围绕智能体的工程化脚手架）与领域专长（[Martin Fowler](https://martinfowler.spicytakes.org/)）。
- **技术债的口径差异**：不同研究给出的金额与占比口径不同，需并列看待（见下文与来源）。
- **「持续交付价值」而非「押注单一里程碑」**：绞杀者模式与 AI 加速结合后，企业能够持续交付价值，而不是把所有赌注压在单个多年度里程碑上（[practicallogix.com](https://www.practicallogix.com/legacy-modernization-at-ai-speed-the-6r-framework-meets-genai-discipline)）。
- **版本升级类转换的边界**：以 Amazon Q Developer 的 Java 升级为例，它只做使代码与目标 JDK 兼容所必需的最小改动，因此项目自身的库与依赖升级还需要额外的转换工作（[Amazon Q Developer を使用した Java バージョンのアップグレード](https://docs.aws.amazon.com/ja_jp/amazonq/latest/qdeveloper-ug/code-transformation.html)）。

## 代表性项目 / 公司 / 产品（附官方链接）

| 项目 / 产品 | 定位 | 链接 |
| --- | --- | --- |
| CodeConcise（Thoughtworks / Fowler 团队） | LLM + AST 知识图谱的遗留系统理解与现代化 | [martinfowler.com](https://www.martinfowler.com/tags/legacy%20modernization.html) |
| Amazon Q Developer | 代码转换，支持 Java 8/11/17 → 17/21 升级 | [AWS Docs](https://docs.aws.amazon.com/en_en/amazonq/latest/qdeveloper-ug/code-transformation.html) |
| AWS Transform | 主机现代化，COBOL→Java、JCL→Groovy | [AWS Blog](https://aws.amazon.com/blogs/migration-and-modernization/accelerate-your-mainframe-modernization-journey-using-ai-agents-with-aws-transform/) |
| Strangler Fig | 渐进式替换模式（Martin Fowler 提出） | [aptibit.com](https://aptibit.com/blog/legacy-modernization-enterprise-ai-era) |

## 关键数据与评测结果（附来源）

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 美国劣质软件质量的年度成本 | 2.41 万亿美元 | CISQ/Synopsys 报告，转引 [brights.io](https://brights.io/blog/technical-debt) |
| 累积技术债本金 | 1.52 万亿美元 | CISQ/Synopsys 报告，转引 [brights.io](https://brights.io/blog/technical-debt) |
| 全球技术债修复工作量 | 610 亿工作日（CAST 2025 对 100 亿行以上代码的分析） | [brights.io](https://brights.io/blog/technical-debt) |
| 技术债占 IT 年度支出比例 | 21%–40%（Deloitte 2026） | [liferay.com](https://www.liferay.com/b/technical-debt-the-cost-that-never-makes-the-agenda) |
| 工程师每月因技术债损失的时间 | 2–5 个工作日（JetBrains 2025） | [dimitriadis.eu](https://dimitriadis.eu/en/articles/technische-schulden-was-sie-kosten-und-wie-man-sie-abbaut) |
| 把技术债列为最大工作挫败感的开发者比例 | 62%（Stack Overflow 2024） | [dimitriadis.eu](https://dimitriadis.eu/en/articles/technische-schulden-was-sie-kosten-und-wie-man-sie-abbaut) |
| 大型企业累积技术债规模 | 1.5–2 万亿美元（HFS Research） | [xpert.digital](https://xpert.digital/en/when-ai-becomes-a-burden/) |
| 认为技术债已限制 AI 计划成效的高管比例 | 81%（IBM 分析） | [xpert.digital](https://xpert.digital/en/when-ai-becomes-a-burden/) |
| 2026 年遗留系统维护成本涨幅 | 18%–25% | [2026 Legacy System Maintenance Cost: Trends & Budget Guide](https://nextolive.com/blogs/2026-legacy-system-maintenance-cost-trends-budget-guide/) |

上述金额与占比来自不同机构、不同统计口径（软件质量成本、IT 支出占比、工程工时占比），彼此不可直接比较或加总。

## 趋势与争议

- **AI 加速 vs 理解力缺口**：AI 智能体重构的速度不是关键问题，关键在于「是否仍有人理解重构后的结果」；在无测试的遗留代码上引入智能体会放大风险（[getunblocked.com](https://getunblocked.com/blog/refactoring-legacy-code/)）。
- **知识图谱是否必要**：有观点认为引入 AST 知识图谱能显著弥补 LLM 对大型代码库结构理解的不足，但这也增加了工程复杂度与维护成本（[martinfowler.com](https://www.martinfowler.com/tags/legacy%20modernization.html)）。
- **AI 生成代码是否在加剧技术债**：一种观点认为，未经充分验证的 AI 生成代码库可能使技术债的增长呈指数级（[xpert.digital](https://xpert.digital/en/when-ai-becomes-a-burden/)）；同时也有实践者主张通过「Research, Review, Rebuild」这类带人工审查环节的工作流，让 AI 在棕地项目中净减少债务（[martinfowler.com](https://www.martinfowler.com/articles/research-review-rebuild.html)）。
- **重构安全网的获取方式争议**：是先补测试再重构，还是先借助 AI 生成理解性文档与知识图谱，再决定重构边界，目前尚无统一做法（[martinfowler.com](https://www.martinfowler.com/tags/legacy%20modernization.html)、[getunblocked.com](https://getunblocked.com/blog/refactoring-legacy-code/)）。
- **人机分工**：厂商的方案普遍强调「功能等价」与「人类在环」的顺序控制，暗示当前阶段全自动的端到端现代化尚非默认选项（[AWS Blog](https://aws.amazon.com/blogs/migration-and-modernization/accelerate-your-mainframe-modernization-journey-using-ai-agents-with-aws-transform/)）。

## 参考来源

1. [Legacy Modernization at AI Speed: The 6R Framework Meets GenAI Discipline](https://www.practicallogix.com/legacy-modernization-at-ai-speed-the-6r-framework-meets-genai-discipline)
2. [Enterprise Software Modernization: Legacy System Migration Strategies for 2026](https://www.ainformat.com/detail/502)
3. [Modernize Without Breaking: AI-Accelerated Refactoring](https://www.nalashaa.com/modernize-without-breaking-ai-refactoring/)
4. [Legacy System Modernisation with AI](https://www.moweb.com/blog/legacy-system-modernisation-ai-enterprise-upgrade)
5. [Legacy Modernization for the AI Era](https://aptibit.com/blog/legacy-modernization-enterprise-ai-era)
6. [Martin Fowler — tagged by: legacy modernization](https://www.martinfowler.com/tags/legacy%20modernization.html)
7. [Research, Review, Rebuild](https://www.martinfowler.com/articles/research-review-rebuild.html)
8. [Martin Fowler — agentic programming 摘要](https://martinfowler.spicytakes.org/)
9. [How to Refactor Legacy Code with AI Agents (2026)](https://getunblocked.com/blog/refactoring-legacy-code/)
10. [Technical Debt: Definition, Types, and Real Costs for Businesses](https://brights.io/blog/technical-debt)
11. [Technical Debt: The Cost That Never Makes the Agenda](https://www.liferay.com/b/technical-debt-the-cost-that-never-makes-the-agenda)
12. [Technical Debt: What It Costs and How to Pay It Down](https://dimitriadis.eu/en/articles/technische-schulden-was-sie-kosten-und-wie-man-sie-abbaut)
13. [The great AI illusion and the silent revolt of developers: When AI becomes a burden](https://xpert.digital/en/when-ai-becomes-a-burden/)
14. [2026 Legacy System Maintenance Cost: Trends & Budget Guide](https://nextolive.com/blogs/2026-legacy-system-maintenance-cost-trends-budget-guide/)
15. [Upgrading Java versions with Amazon Q Developer](https://docs.aws.amazon.com/en_en/amazonq/latest/qdeveloper-ug/code-transformation.html)
16. [Accelerate Your Mainframe Modernization Journey using AI Agents with AWS Transform](https://aws.amazon.com/blogs/migration-and-modernization/accelerate-your-mainframe-modernization-journey-using-ai-agents-with-aws-transform/)
17. [Martin Fowler — during: 2025](https://www.martinfowler.com/tags/2025.html)