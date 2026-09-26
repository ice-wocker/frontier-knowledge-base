# 领域驱动设计（DDD）

> 最后更新：2026-09-26 ｜ 领域：软件·架构与 API ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

领域驱动设计（Domain-Driven Design, DDD）由 Eric Evans 提出，核心是在复杂业务系统中以领域模型为中心，让软件结构与业务概念对齐。其战略设计关注限界上下文（bounded context）、通用语言（ubiquitous language）与上下文映射；战术设计关注实体、值对象、聚合（aggregate）、领域事件与领域服务。2025–2026 年，DDD 既是模块化单体与微服务划界的方法论基础，也因「贫血模型」反模式与「为 DDD 而 DDD」的过度设计争议而持续被讨论；事件风暴（Event Storming）成为最常用的发现工作坊。

## 最新进展（2025–2026）

### 限界上下文仍是划界核心

DDD 的战略模式被反复强调为「最重要的模式」：它强制把一个复杂领域拆成多个内聚的小边界，每个边界内有一套统一、自洽的语言与领域模型（[DDD:领域驱动设计](https://blog.csdn.net/weixin_46619605/article/details/155024617)）。典型例子是「Customer」：在 Sales 上下文里是一个处于转化中的 lead，在 Billing 里是一个有付款条款的账户，在 Support 里是一个有工单的人；强行建立单一 `Customer` 模型会退化为充满空字段与复杂判断的「上帝类」（[Domain-Driven Design in 2026: A Practical Guide](https://www.alekseialeinikov.com/en/blog/topics/architecture/domain-driven-design-2026-a-practical-guide)）。有资料强调，在大系统中不可能为整个组织建立单一一致模型，因此必须划分边界、让不同子域团队独立演进（[Domain Driven Design – how to implement and use it?](https://odysse.io/en/domain-driven-design-how-to-implement-and-use-it/)）。

### 事件风暴作为发现方法

事件风暴被描述为 DDD 首选的发现「强力工具」：低技术门槛的协作式工作坊，一群人围绕业务流程在长墙上用彩色便利贴建模；做法是一次聚焦一个业务流程，从过去时的领域事件（如 `Order Shipped`、`Payment Failed`）出发，再补上命令、参与者、策略、读模型、外部系统与聚合（[Discovering Domains and Contexts](https://software-architecture-guild.com/guide/architecture/domains/discovering-domains-and-contexts/)）。其颜色编码约定为：橙色=领域事件、蓝色=命令、黄色=参与者、粉色=热点等（[Event Storming & DDD](https://drcodes.com/posts/event-storming-ddd-master-microservices-decomposition)）。该方法由 Alberto Brandolini 提出并在 DDD 社区被公认为快速捕获方案设计、提升团队对领域理解的技术（[Event Storming — IBM Cloud Architecture](https://ibm-cloud-architecture.github.io/refarch-eda/methodology/event-storming/)）。实践中分为「大局事件风暴」（用于发现限界上下文）与「软件设计事件风暴」（聚焦单一上下文内部以定义聚合）（[Event Storming – The Complete Guide](https://www.qlerify.com/post/event-storming-the-complete-guide)）。

### DDD 与 AI/多智能体系统的结合

2025–2026 年出现把 DDD 与事件风暴用于设计多智能体 AI 系统的新实践：以领域事件、命令与聚合来结构化系统的业务行为，使协作式建模同样服务于 AI 系统的边界设计（[Designing Scalable Multi-Agent AI Systems: Leveraging DDD and Event Storming](https://dzone.com/articles/multi-agent-ai-ddd-event-storming)）。

## 核心技术与关键概念

- **限界上下文（Bounded Context）**：某一领域模型与语言保持一致的显式边界；同一词在不同上下文含义不同（[Domain-Driven Design in 2026](https://www.alekseialeinikov.com/en/blog/topics/architecture/domain-driven-design-2026-a-practical-guide)）。
- **通用语言（Ubiquitous Language）**：领域专家与开发者在同一上下文内共享的无歧义语言（[IBM Cloud Architecture — Event Storming](https://ibm-cloud-architecture.github.io/refarch-eda/methodology/event-storming/)）。
- **聚合（Aggregate）**：围绕一个或多个实体的一致性边界，其中只有一个实体是聚合根；外部只能通过根实体的标识引用，其他实体是根的子对象（[Microsoft — 使用战术 DDD 设计微服务](https://learn.microsoft.com/fr-fr/azure/architecture/microservices/model/tactical-domain-driven-design)）。
- **实体与值对象**：实体有身份标识与生命周期，值对象以属性定义、不可变。
- **领域事件（Domain Event）**：领域中专有名词、对专家有意义的「已发生事实」，是事件风暴与事件驱动架构的连接点（[IBM Cloud Architecture](https://ibm-cloud-architecture.github.io/refarch-eda/methodology/event-storming/)）。
- **富领域模型 vs 贫血模型**：业务逻辑应尽量封装在实体、值对象或领域服务中；在应用服务里堆积大量 `if-else` 判断的「贫血模型」是 DDD 极力避免的反模式（[2025 年 DDD 核心模式解析](https://blog.csdn.net/qq_21886255/article/details/153411519)）。
- **上下文映射**：描述限界上下文之间的关系模式（如共享内核、防腐层等），用于跨团队协作。

## 代表性项目 / 组织 / 产品

- **Eric Evans 与 DDD 社区**：DDD 方法论的提出者与持续演化者（[odysse.io](https://odysse.io/en/domain-driven-design-how-to-implement-and-use-it/)）。
- **Alberto Brandolini / Event Storming**：事件风暴方法的提出者（[IBM Cloud Architecture](https://ibm-cloud-architecture.github.io/refarch-eda/methodology/event-storming/)）。
- **Microsoft Azure Architecture Center**：提供战术 DDD 与微服务建模的官方指南（[Microsoft](https://learn.microsoft.com/fr-fr/azure/architecture/microservices/model/tactical-domain-driven-design)）。
- **Qlerify 等工具**：支撑事件风暴协作与在线建模的商业产品（[Qlerify](https://www.qlerify.com/post/event-storming-the-complete-guide)）。

## 关键数据与评测结果

DDD 属于方法论，缺乏统一量化指标。可核验的实践口径主要来自案例叙述：例如电商系统按 Sales、Billing、Support 等上下文拆分，以避免单一 `Product`/`Customer` 模型膨胀为「上帝类」（[2025 年 DDD 核心模式解析](https://blog.csdn.net/qq_21886255/article/details/153411519)）；多个资料一致主张用事件风暴在一次工作坊内完成领域发现与上下文划分（[Event Storming – The Complete Guide](https://www.qlerify.com/post/event-storming-the-complete-guide)；[Discovering Domains and Contexts](https://software-architecture-guild.com/guide/architecture/domains/discovering-domains-and-contexts/)）。

## 趋势与争议

- **贫血模型之争**：贫血模型被普遍称为「最常见且致命」的反模式——实体只有数据没有逻辑、封装被破坏、业务规则散落在服务层、规则变更需多处修改（[Anti-Patterns and Pitfalls](https://advanced-beginner.github.io/en/docs/ddd/concepts/anti-patterns/)）。批评集中在：实体通过公开 getter/setter 暴露数据、破坏封装，一致性难以保证，业务规则分散且内聚度低（[Rich Domains: How to Use DDD](https://www.telerik.com/blogs/rich-domains-how-use-ddd-create-more-sustainable-systems)）。
- **DDD 是否被过度使用**：社区反复讨论「DDD 何时值得投入、何时不值得」，以及它与微服务配合的边界——DDD 提供划界语言，但并非所有 CRUD 系统都需要战术模式全套（[Domain-Driven Design: Modeling Software Around the Business](https://dev.to/rhuturaj_takle/domain-driven-design-modeling-software-around-the-business-1h3)）。
- **方法论落地难**：限界上下文的划分是公认的难点，实践中依赖工作坊与领域专家深度参与；缺乏领域专家投入时，模型容易退化为技术分层（[Event Storming – The Complete Guide](https://www.qlerify.com/post/event-storming-the-complete-guide)）。
- **与模块化单体/微服务的配合**：DDD 的战略边界被用作模块化单体内部模块划分与微服务拆分的依据，强调边界应服务于业务必要性而非技术偏好（[The Modular Monolith 2026 Complete Guide](https://dev.to/x4nent/the-modular-monolith-2026-complete-guide-spring-modulith-archunit-fitness-functions-and-lessons-878)）。

## 参考来源

- [Domain Driven Design – how to implement and use it?](https://odysse.io/en/domain-driven-design-how-to-implement-and-use-it/)
- [Domain-Driven Design in Practice: Bounded Contexts and Aggregates](https://scopeforged.com/blog/domain-driven-design-practical)
- [Domain-Driven Design in 2026: A Practical Guide](https://www.alekseialeinikov.com/en/blog/topics/architecture/domain-driven-design-2026-a-practical-guide)
- [Utiliser le DDD tactique pour concevoir des microservices — Microsoft](https://learn.microsoft.com/fr-fr/azure/architecture/microservices/model/tactical-domain-driven-design)
- [DDD:领域驱动设计 — 驾驭复杂业务系统的架构艺术](https://blog.csdn.net/weixin_46619605/article/details/155024617)
- [2025 年领域驱动设计核心模式最新面试题全解析](https://blog.csdn.net/qq_21886255/article/details/153411519)
- [Event Storming — IBM Cloud Architecture](https://ibm-cloud-architecture.github.io/refarch-eda/methodology/event-storming/)
- [Event Storming – The Complete Guide](https://www.qlerify.com/post/event-storming-the-complete-guide)
- [Event Storming & DDD: Master Microservices Decomposition](https://drcodes.com/posts/event-storming-ddd-master-microservices-decomposition)
- [Discovering Domains and Contexts](https://software-architecture-guild.com/guide/architecture/domains/discovering-domains-and-contexts/)
- [Designing Scalable Multi-Agent AI Systems: Leveraging DDD and Event Storming](https://dzone.com/articles/multi-agent-ai-ddd-event-storming)
- [Anti-Patterns and Pitfalls — DDD](https://advanced-beginner.github.io/en/docs/ddd/concepts/anti-patterns/)
- [Rich Domains: How to Use DDD to Create More Sustainable Systems](https://www.telerik.com/blogs/rich-domains-how-use-ddd-create-more-sustainable-systems)
- [Domain-Driven Design: Modeling Software Around the Business](https://dev.to/rhuturaj_takle/domain-driven-design-modeling-software-around-the-business-1h3)
- [The Modular Monolith 2026 Complete Guide](https://dev.to/x4nent/the-modular-monolith-2026-complete-guide-spring-modulith-archunit-fitness-functions-and-lessons-878)