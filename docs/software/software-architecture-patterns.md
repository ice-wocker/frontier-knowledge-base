# 软件架构模式

> 最后更新：2026-09-26 ｜ 领域：软件·架构与 API ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

架构模式是对系统整体结构的可复用组织方式，决定依赖方向、边界划分、部署形态与演进路径。经典模式包括分层架构（Layered）、端口与适配器/六边形（Hexagonal / Ports and Adapters）、洋葱架构（Onion）与整洁架构（Clean）；部署形态上则有单体、模块化单体、微服务与 Serverless。2025–2026 年的主线是「回归务实」：模块化单体与显式的依赖倒置受到推崇，架构决策记录（ADR）在 AI 辅助开发时代重新获得重视。

## 最新进展（2025–2026）

### 模块化单体成为默认起点

多份资料指出，模块化单体已从「妥协方案」升级为推荐默认架构：它以单一部署单元运行，内部按清晰模块和强边界组织，保留单体的运维简单性而又不牺牲代码组织、模块化与可测试性（[The Microservices Backlash](https://www.devx.com/uncategorized/microservices-backlash-monoliths-comeback-2026/)）。有从业者提出「模块化单体 + 选择性服务抽取」的可演进架构，目标是降低当前运维负担，同时保留任一模块日后演进为独立服务的可能（[The Modular Monolith 2026 Complete Guide](https://dev.to/x4nent/the-modular-monolith-2026-complete-guide-spring-modulith-archunit-fitness-functions-and-lessons-878)）。在 .NET 实践中，关键做法是「按业务特性而非技术层拆分」，特性之间只依赖彼此契约、绝不依赖彼此实现，即以依赖倒置强制边界（[Modular Monolith in .NET: Enforcing Boundaries with Dependency Inversion](https://gaevoy.com/2026/06/30/modular-monolith-dotnet-enforcing-boundaries-dependency-inversion.html)）。

### 六边形/整洁架构与模块化单体合流

主流实践倾向「新项目先做六边形结构的模块化单体」：若规模需要，可将适配器抽取为独立微服务而不触碰领域核心，从而避免过早分布式化（[Hexagonal Architecture: Ports and Adapters](https://calmops.com/software-engineering/hexagonal-architecture-ports-adapters-pattern/)）。Thoughtworks 对六边形的解释强调它把核心业务逻辑与数据库、API、外部服务等基础设施分离，使结账等流程能在不真正扣款的情况下被完整测试，并更易隔离外部系统故障（[Hexagonal architecture explained through a practical example](https://www.thoughtworks.com/en-us/insights/blog/architecture/hexagonal-architecture-explained-practical-example)）。整洁架构与洋葱架构被描述为共享同一原则：依赖始终指向内层，业务逻辑不依赖框架、UI 与数据库（[From Spaghetti to Hexagons: A Practical Guide to Clean Java Architecture](https://javapro.io/2026/05/27/from-spaghetti-to-hexagons-a-practical-guide-to-clean-java-architecture/）；[Clean Architecture in ASP.NET Core](https://blog.ndepend.com/clean-architecture-for-asp-net-core-solution/)）。

### ADR 在 agentic 时代回归

有从业者观察到 ADR 出现「回归」，用于为 AI 辅助/agentic 工程团队锚定架构上下文；并提出以「ADR 覆盖率」衡量：目标覆盖 70–80% 的关键路径决策（数据模型、服务边界、认证、计费、受监管区域、曾出过事故的地方），低于 40% 属于危险区（[The ADR Comeback: Anchoring Agentic Engineering Teams](https://rickpollick.com/blog/adr-comeback-anchoring-agentic-engineering-teams)）。AWS 处方指南主张 ADR 一旦被接受或拒绝即应视为不可变文档，如需变更须新建 ADR 并走评审与批准流程（[AWS Prescriptive Guidance — ADR](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/architectural-decision-records/architectural-decision-records.pdf#best-practices)）。Microsoft 的 Azure Well-Architected 指南也建议对过去已知决策「回溯生成」ADR，并将其作为审计与事件响应的单一事实来源（[Mantenimiento de un registro de decisión de arquitectura](https://learn.microsoft.com/es-es/azure/well-architected/architect-role/architecture-decision-record)）。

## 核心技术与关键概念

- **分层架构**：自上而下的依赖，业务逻辑通常依赖数据访问层；实现简单但业务逻辑与持久化耦合，测试常需层层 mock（[Ports and Adapters (Hexagonal Architecture)](https://synchronium.github.io/software-architecture-wiki/styles/ports-and-adapters.html)）。
- **六边形 / 端口与适配器**：依赖向内，基础设施依赖业务逻辑；业务逻辑对基础设施无感知，可在隔离下测试（[synchronium](https://synchronium.github.io/software-architecture-wiki/styles/ports-and-adapters.html)）。
- **洋葱架构**：由 Jeffrey Palermo 于 2008 年提出，以同心层结构把领域逻辑置于中心、依赖向内流动，适合业务规则复杂的企业应用（[Onion Architecture](https://bytegoblin.io/blog/onion-architecture.mdx)）。
- **整洁架构**：常被描述为洋葱架构的别名，按 Domain / Application / UI / Infrastructure 四层组织，强调最小依赖（[Clean Architecture in ASP.NET Core](https://blog.ndepend.com/clean-architecture-for-asp-net-core-solution/)）。
- **模块化单体**：单部署单元 + 强内部边界 + 编译期边界强制（Go/Rust workspace、Java 模块等）（[The Microservices Backlash](https://www.devx.com/uncategorized/microservices-backlash-monoliths-comeback-2026/)）。
- **Serverless**：抽象基础设施、按需伸缩、按用量计费；适合不可预测的突发流量，但在持续高 CPU、超长执行、大内存常驻、严格冷启动与专用基础设施合规等场景不占优（[Serverless Architecture in 2026](https://topictrick.com/blog/serverless-architecture-2026)）。
- **ADR**：以简短文档记录「背景—决策—后果」，覆盖架构上重要的决策，作为审计与入职参考（[adr.github.io](https://adr.github.io/#existing-adr-templates)）。

## 代表性项目 / 组织 / 产品

- **Thoughtworks**：持续输出六边形架构等实践解读（[Thoughtworks](https://www.thoughtworks.com/en-us/insights/blog/architecture/hexagonal-architecture-explained-practical-example)）。
- **Spring Modulith / ArchUnit**：以模块与适应度函数在 Java 侧强制模块化单体边界（[dev.to](https://dev.to/x4nent/the-modular-monolith-2026-complete-guide-spring-modulith-archunit-fitness-functions-and-lessons-878)）。
- **adr.github.io**：ADR 社区，汇集模板与工具，并跟踪相关会议演讲（[adr.github.io](https://adr.github.io/#existing-adr-templates)）。
- **AWS / Microsoft 架构中心**：提供 ADR 与 Serverless 等模式的官方指南（[AWS ADR 指南](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/architectural-decision-records/architectural-decision-records.pdf#best-practices)）。

## 关键数据与评测结果

- **架构量化对比**：一份对比表给出部署单元（单体/模块化单体为 1，微服务数十至上百）、模块间延迟（纳秒级 vs 1–30+ 毫秒）、数据一致性（强 ACID vs 最终一致）、失败爆炸半径（整体 vs 隔离）等维度（[The Architectural Paradox](https://labs.relbis.com/blog/2026-05-03_monolith_vs_microservices/)）。
- **Serverless 适用边界**：资料给出「适用/不适用」清单——持续 CPU 利用率 > 50%、执行超 15 分钟、需跨请求大内存数据集、全用户亚 10ms 冷启动、要求专用基础设施合规等场景不建议使用 Serverless（[Serverless Architecture in 2026](https://topictrick.com/blog/serverless-architecture-2026)）。
- **ADR 覆盖率**：建议目标为 70–80%，低于 40% 视为危险区（二手经验数据）（[The ADR Comeback](https://rickpollick.com/blog/adr-comeback-anchoring-agentic-engineering-teams)）。

## 趋势与争议

- **单体回归是否「倒退」**：支持者认为复杂度应由业务必要性证明，模块化单体是可演进的务实起点；反对者担忧其扩展性与团队自治不足（[The Microservices Backlash](https://www.devx.com/uncategorized/microservices-backlash-monoliths-comeback-2026/)；[The Modular Monolith 2026 Complete Guide](https://dev.to/x4nent/the-modular-monolith-2026-complete-guide-spring-modulith-archunit-fitness-functions-and-lessons-878)）。
- **Serverless 的隐性成本**：冷启动、调试与可观测性困难、厂商锁定（如 Lambda 与 API Gateway/S3/DynamoDB 的深度耦合导致迁移昂贵）是主要争议点（[What is Serverless Architecture?](https://www.back4app.com/glossary/serverless-architecture/)；[A Technical Deep Dive for 2026](https://cloudconsultingfirms.com/insights/what-is-serverless-architecture/)）。
- **Serverless 架构反模式**：业界建议「Lambda 是胶水而非应用」、单一职责、默认异步（用 SQS/EventBridge 而非同步链）、用 Step Functions 编排状态机、为失败设计（DLQ、幂等、熔断）（[AWS Serverless Patterns and Anti-Patterns](https://dev.to/alpeshkumbhare/aws-serverless-patterns-and-anti-patterns-what-works-what-breaks-and-when-to-use-what-4k50)）。
- **模式与框架的独立性**：整洁/六边形/洋葱的共同主张是业务逻辑不依赖框架与数据库，但在实际项目中「形式化分层」与「过度抽象」的批评持续存在（[Clean Architecture in ASP.NET Core](https://blog.ndepend.com/clean-architecture-for-asp-net-core-solution/)）。

## 参考来源

- [The Microservices Backlash: When Monoliths Make a Comeback](https://www.devx.com/uncategorized/microservices-backlash-monoliths-comeback-2026/)
- [The Modular Monolith 2026 Complete Guide — Spring Modulith, ArchUnit](https://dev.to/x4nent/the-modular-monolith-2026-complete-guide-spring-modulith-archunit-fitness-functions-and-lessons-878)
- [Modular Monolith in .NET: Enforcing Boundaries with Dependency Inversion](https://gaevoy.com/2026/06/30/modular-monolith-dotnet-enforcing-boundaries-dependency-inversion.html)
- [Hexagonal Architecture: Ports and Adapters Pattern for Clean Software Design](https://calmops.com/software-engineering/hexagonal-architecture-ports-adapters-pattern/)
- [Hexagonal architecture explained through a practical example — Thoughtworks](https://www.thoughtworks.com/en-us/insights/blog/architecture/hexagonal-architecture-explained-practical-example)
- [Ports and Adapters (Hexagonal Architecture) — Software Architecture Wiki](https://synchronium.github.io/software-architecture-wiki/styles/ports-and-adapters.html)
- [Onion Architecture](https://bytegoblin.io/blog/onion-architecture.mdx)
- [.NET Architecture at Scale: Visual Guide to Modern Design Patterns](https://nitinksingh.com/posts/.net-architecture-at-scale-visual-guide-to-modern-design-patterns/)
- [Clean Architecture in ASP.NET Core](https://blog.ndepend.com/clean-architecture-for-asp-net-core-solution/)
- [From Spaghetti to Hexagons: A Practical Guide to Clean Java Architecture](https://javapro.io/2026/05/27/from-spaghetti-to-hexagons-a-practical-guide-to-clean-java-architecture/)
- [The ADR Comeback: Anchoring Agentic Engineering Teams With Architecture Decision Records](https://rickpollick.com/blog/adr-comeback-anchoring-agentic-engineering-teams)
- [AWS Prescriptive Guidance: Using architectural decision records](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/architectural-decision-records/architectural-decision-records.pdf#best-practices)
- [Microsoft Azure Well-Architected — Architecture decision record](https://learn.microsoft.com/es-es/azure/well-architected/architect-role/architecture-decision-record)
- [Architectural Decision Records — adr.github.io](https://adr.github.io/#existing-adr-templates)
- [The Architectural Paradox: Monolithic, Microservice, and Modular Monolithic Systems](https://labs.relbis.com/blog/2026-05-03_monolith_vs_microservices/)
- [Serverless Architecture in 2026: Beyond Functions](https://topictrick.com/blog/serverless-architecture-2026)
- [What is Serverless Architecture? A Practical Guide](https://middleware.io/blog/serverless-architecture/)
- [What is Serverless Architecture? — back4app glossary](https://www.back4app.com/glossary/serverless-architecture/)
- [What is Serverless Architecture? A Technical Deep Dive for 2026](https://cloudconsultingfirms.com/insights/what-is-serverless-architecture/)
- [AWS Serverless Patterns and Anti-Patterns](https://dev.to/alpeshkumbhare/aws-serverless-patterns-and-anti-patterns-what-works-what-breaks-and-when-to-use-what-4k50)