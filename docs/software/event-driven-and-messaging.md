# 事件驱动与消息系统

> 最后更新：2026-09-26 ｜ 领域：软件·架构与 API ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

事件驱动架构（EDA）以事件的产生、传输与消费组织系统，实现服务间的松耦合、异步与可扩展。其技术底座是消息与流平台（Kafka、Pulsar、NATS、RabbitMQ 等），上层常见模式包括事件溯源（Event Sourcing）、CQRS、发布/订阅与队列。2025–2026 年的关键动态包括：Apache Kafka 4.x 彻底转向 KRaft、交付语义与 Schema Registry 成为一致性与治理的核心手段，以及流式平台在吞吐、延迟与运维成本间的重新权衡。

## 最新进展（2025–2026）

### Kafka 4.x 全面进入 KRaft 时代

Apache Kafka 4.0 是首个完全不需要 Apache ZooKeeper 的主版本，默认以 KRaft 模式运行，消除了维护独立 ZooKeeper 集群的复杂度，显著降低运维开销并提升可扩展性（[Apache Kafka 4.0.0 Release Announcement](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/)）。升级文档明确：Kafka 4.0 仅支持 KRaft 模式，ZooKeeper 模式已移除（[Kafka 4.1 Upgrading](https://kafka.apache.org/41/getting-started/upgrade/)）。后续 4.0.1 于 2025 年 10 月发布（[Apache Kafka Blog](https://kafka.apache.org/blog/?trk=organization_guest_main-feed-card-text)），4.1 系列的兼容性文档更新至 2026 年，并要求用户使用 `--bootstrap-server` 与集群交互（[Kafka Compatibility](https://kafka.apache.org/41/getting-started/compatibility/)）。云厂商侧也在推进，例如 Amazon MSK 于 2026 年 8 月宣布支持就地 ZooKeeper 到 KRaft 集群升级（[Announcing in-place ZooKeeper-to-KRaft upgrades for Amazon MSK](https://aws.amazon.com.cdn.amazon.com/blogs/big-data/announcing-in-place-zookeeper-to-kraft-cluster-upgrades-for-amazon-msk/)）。

### 交付语义与 Schema Registry

Kafka 默认提供至少一次（at-least-once）交付；通过幂等生产者与事务 API，可让生产者向多个分区原子写入并在处理后提交偏移，从而在 Kafka Streams 中实现端到端精确一次（exactly-once）处理（[Kafka Core Concepts](https://kafka.apache.org/20/streams/core-concepts/)）。Confluent 文档指出，Kafka 默认保证至少一次，可在生产者禁用重试并在消费者手动提交偏移时实现至多一次（[Kafka Message Delivery Guarantees](https://docs.confluent.io/kafka/design/delivery-semantics.html)）。Schema Registry 提供集中式 schema 仓库，用于校验、序列化与反序列化，并在 schema 演进时保证兼容性，是数据治理、血缘与数据质量的关键组件（[Confluent Schema Registry](https://docs.confluent.io/platform/8.2/schema-registry/index.html)）。

### 消息平台格局

面向自托管场景的对比指出：NATS（JetStream）支持 NATS/MQTT/WebSocket 协议，RabbitMQ 基于 AMQP 0-9-1 并支持 MQTT/STOMP，Pulsar 支持自有协议、Kafka 协议与 MQTT；三者分别采用内置 JetStream、Quorum Queues 与 BookKeeper + 分层存储的持久化方案（[Self-Hosted Pub/Sub Platforms: NATS vs RabbitMQ vs Apache Pulsar](https://www.pistack.xyz/posts/2026-05-22-self-hosted-pubsub-platforms-nats-rabbitmq-apache-pulsar-guide/)）。Pulsar 的差异化在于以 Apache BookKeeper 分离计算与存储，使服务层与存储层可独立伸缩，并原生支持发布/订阅与队列两种模式、内置地理复制与多租户（[Best Apache Pulsar Alternatives in 2026](https://www.modern-datatools.com/alternatives/apache-pulsar)）。NATS 则以单二进制部署、亚毫秒级延迟见长，适合云、边缘与 IoT（[Best RabbitMQ Alternatives in 2026](https://www.modern-datatools.com/alternatives/rabbitmq)）。

## 核心技术与关键概念

- **事件 vs 命令**：事件是已发生的业务事实（过去时，如 `OrderPlaced`），命令是触发意图；建模时应写「意图导向」的事件而非「实现导向」的表更新（[CQRS and Event Sourcing: Practical Implementation Patterns 2026](https://calmops.com/software-engineering/cqrs-event-sourcing-practical-implementation/)）。
- **Event Sourcing**：不存储可变状态的当前快照，而是保存不可变事件序列，通过重放重建状态；配合快照应对长历史聚合（[Event Sourcing and CQRS](https://martinuke0.github.io/posts/2026-03-07-event-sourcing-and-cqrs-building-resilient-data-architectures-for-modern-distributed-systems/)）。
- **CQRS**：将命令（写）与查询（读）拆分为独立执行路径与数据表，读写各自优化，读模型通过异步投影更新，形成写读之间的最终一致窗口（[Event-Driven Architecture: CQRS and Event Sourcing in Practice](https://www.codesprintpro.com/blog/event-driven-cqrs-event-sourcing/)）。
- **Exactly-once**：通过幂等生产者 + 事务写入组合实现；并非所有连接器都支持 EOS，需确认其具备事务写入与幂等能力（[How to Transform Data and Manage Schemas in Kafka Connect](https://www.confluent.io/blog/kafka-connect-data-transformation-schema/)）。
- **Schema Registry 与兼容性**：集中管理 schema 并校验兼容性，支撑 schema 演进、数据血缘与审计（[Confluent Schema Registry](https://docs.confluent.io/platform/8.2/schema-registry/index.html)）。
- **投影幂等与事件版本化**：读侧投影应基于事件 ID 去重、保持幂等，并对事件做版本化与 upcaster 升级（[Event Sourcing and CQRS](https://martinuke0.github.io/posts/2026-03-07-event-sourcing-and-cqrs-building-resilient-data-architectures-for-modern-distributed-systems/)）。

## 代表性项目 / 组织 / 产品

- **Apache Kafka**：事件流平台的代表，4.x 起仅支持 KRaft（[Kafka 4.0.0 Release](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/)）。
- **Apache Pulsar**：以 BookKeeper 分离存算、支持多租户与地理复制（[modern-datatools](https://www.modern-datatools.com/alternatives/apache-pulsar)）。
- **NATS / NATS JetStream**：轻量、低延迟的消息系统（[pistack.xyz](https://www.pistack.xyz/posts/2026-05-22-self-hosted-pubsub-platforms-nats-rabbitmq-apache-pulsar-guide/)）。
- **RabbitMQ**：经典 AMQP 消息代理（[modern-datatools](https://www.modern-datatools.com/alternatives/rabbitmq)）。
- **Confluent Schema Registry**：Kafka 生态的 schema 治理组件（[Confluent](https://docs.confluent.io/platform/8.2/schema-registry/index.html)）。

## 关键数据与评测结果

- **架构性能对比（二手汇总）**：一份预印本给出的对比表列出 Apache Pulsar 峰值吞吐约 950,000、P95 延迟 22、P99 延迟 58；NATS JetStream 峰值吞吐约 800,000、P95 延迟 15、P99 延迟 38（[Next-Generation Event-Driven Architectures](https://arxiv.org/html/2510.04404v2)）。该数据为特定实验条件，不宜直接外推。
- **交付语义默认值**：Kafka 默认 at-least-once；exactly-once 需事务/幂等支持（[Kafka Message Delivery Guarantees](https://docs.confluent.io/kafka/design/delivery-semantics.html)）。

## 趋势与争议

- **运维简化 vs 功能完备**：KRaft 消除了 ZooKeeper 依赖，但也要求升级前达到 KRaft 生产就绪的版本门槛（[Kafka 4.1 Upgrading](https://kafka.apache.org/41/getting-started/upgrade/)）。
- **精确一次的成本**：EOS 提升一致性，但事务与幂等带来吞吐与复杂度代价，且受连接器支持度约束（[Kafka Connect Schema/EOS](https://www.confluent.io/blog/kafka-connect-data-transformation-schema/)）。
- **EDA 的复杂度税**：事件溯源 + CQRS 的组合被批评为增益伴随显著复杂度，实践建议包括事件建模谨慎、频繁快照、投影幂等与乐观并发控制（[Event Sourcing and CQRS](https://martinuke0.github.io/posts/2026-03-07-event-sourcing-and-cqrs-building-resilient-data-architectures-for-modern-distributed-systems/)）。
- **平台选型分歧**：Kafka 强在流处理生态，Pulsar 强在存算分离与多租户，NATS 强在极简与低延迟，RabbitMQ 强在成熟路由；「谁更好」取决于延迟、持久化与运维预算的优先级（[pistack.xyz](https://www.pistack.xyz/posts/2026-05-22-self-hosted-pubsub-platforms-nats-rabbitmq-apache-pulsar-guide/)）。

## 参考来源

- [Apache Kafka 4.0.0 Release Announcement](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/)
- [Apache Kafka 4.1 — Upgrading](https://kafka.apache.org/41/getting-started/upgrade/)
- [Apache Kafka 4.1 — Compatibility](https://kafka.apache.org/41/getting-started/compatibility/)
- [Apache Kafka Blog（4.0.1 发布）](https://kafka.apache.org/blog/?trk=organization_guest_main-feed-card-text)
- [Kafka Streams Core Concepts（exactly-once）](https://kafka.apache.org/20/streams/core-concepts/)
- [Kafka Message Delivery Guarantees — Confluent](https://docs.confluent.io/kafka/design/delivery-semantics.html)
- [Schema Registry for Confluent Platform](https://docs.confluent.io/platform/8.2/schema-registry/index.html)
- [How to Transform Data and Manage Schemas in Kafka Connect Pipelines](https://www.confluent.io/blog/kafka-connect-data-transformation-schema/)
- [Announcing in-place ZooKeeper-to-KRaft cluster upgrades for Amazon MSK](https://aws.amazon.com.cdn.amazon.com/blogs/big-data/announcing-in-place-zookeeper-to-kraft-cluster-upgrades-for-amazon-msk/)
- [Self-Hosted Pub/Sub Platforms: NATS vs RabbitMQ vs Apache Pulsar (2026 Guide)](https://www.pistack.xyz/posts/2026-05-22-self-hosted-pubsub-platforms-nats-rabbitmq-apache-pulsar-guide/)
- [Best Apache Pulsar Alternatives in 2026](https://www.modern-datatools.com/alternatives/apache-pulsar)
- [Best RabbitMQ Alternatives in 2026](https://www.modern-datatools.com/alternatives/rabbitmq)
- [Next-Generation Event-Driven Architectures: Performance, Scalability, and Intelligent Orchestration](https://arxiv.org/html/2510.04404v2)
- [Event-Driven Architecture: CQRS and Event Sourcing in Practice](https://www.codesprintpro.com/blog/event-driven-cqrs-event-sourcing/)
- [CQRS and Event Sourcing: Practical Implementation Patterns 2026](https://calmops.com/software-engineering/cqrs-event-sourcing-practical-implementation/)
- [Event Sourcing and CQRS: Building Resilient Data Architectures](https://martinuke0.github.io/posts/2026-03-07-event-sourcing-and-cqrs-building-resilient-data-architectures-for-modern-distributed-systems/)