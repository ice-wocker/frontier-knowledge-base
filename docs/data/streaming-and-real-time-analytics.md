# 流处理与实时分析

> 最后更新：2026-09-26 ｜ 领域：数据·工程与架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

流处理与实时分析面向「数据到达即处理」的场景，用持续计算代替按周期批处理，把延迟从分钟/小时级压缩到秒级。技术栈通常由三部分构成：消息与事件日志（Kafka 等）、流计算引擎（Flink、Spark Structured Streaming）、以及实时消费端（实时数仓、物化视图、流式数据库）。CDC（Change Data Capture，变更数据捕获）是实时链路的重要入口，通过读取数据库事务日志捕获行级变更并向下游传播。

从架构演进看，实时分析经历了三个阶段：早期以「流计算引擎 + 消息队列」为主，工程师需自行管理作业与 offset；随后出现「实时数仓」，由 Flink/Spark 把流数据写入 OLAP 引擎供交互分析；当前则向「流式数据库」演进——用 SQL 直接定义增量物化视图，把作业编排、状态管理与 offset 记账下沉到系统内部。这一演进的驱动力是降低运维复杂度：传统 Flink 作业的状态调优、checkpoint 与版本升级都需要专门技能，而流式数据库把这些问题封装为数据库语义。与此同时，Kafka 作为事实上的事件骨干，其在 4.0 中完成向 KRaft 的迁移，也从基础设施层面降低了实时链路的运维门槛。

## 最新进展（2025–2026）

**Kafka 4.0：告别 ZooKeeper。** Apache Kafka 4.0 是第一个完全无需 Apache ZooKeeper 的主要版本，默认以 KRaft 模式运行，简化部署与管理，消除了维护独立 ZooKeeper 集群的复杂度，显著降低运维开销并增强可扩展性（[Apache Kafka 4.0.0 Release Announcement](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/)）。Kafka 4.0 仅支持 KRaft 模式，ZooKeeper 模式已被移除；broker 升级到 4.0.0 及以上需要处于 KRaft 模式，且软件与元数据版本至少为 3.3.x，较旧集群建议先升级到 3.9.x（[Upgrading](https://kafka.apache.org/40/getting-started/upgrade/)）。该版本亦被 Confluent 年度回顾列为 2025 年 Kafka 社区最大亮点（[2025 - The year gone by](https://developer.confluent.io/newsletter/2025-the-year-gone-by/)）。后续 4.0.2 为 bugfix 版本，发布于 2026 年 3 月 16 日，包含 KIP-1252（修正 ZooKeeper 与 KRaft 模式间的行为不一致）（[Posts in 2026](https://kafka.apache.org/blog/)）。

**Flink 与湖仓进一步融合。** 动态 Iceberg Sink 已正式成为 Apache Iceberg 项目的一部分，支持 Iceberg 1.10.0 及以上、Flink 1.20/2.0/2.1，使 Kafka 摄取可直接落入湖仓（[From Stream to Lakehouse: Kafka Ingestion with the Flink Dynamic Iceberg Sink](https://flink.apache.org/2025/11/11/from-stream-to-lakehouse-kafka-ingestion-with-the-flink-dynamic-iceberg-sink/)）。Confluent Cloud 推出的 Materialized Tables 从「管理临时语句」转向持久化、数据库式对象，用单条 SQL 自动完成 offset 记账与作业编排，并通过 CREATE OR ALTER 原地演进查询，Flink 在底层负责 offset 记账与作业迁移，终结了手工迁移周期（[New in Confluent Cloud](https://www.confluent.io/ko-kr/blog/2026-q2-confluent-cloud-launch/)）。

**流式数据库走向 AI-ready。** RisingWave 3.0 定位为面向 agentic AI 的实时数据平台，引入 Apache Iceberg V3 支持以强化实时湖仓架构、原生 pgvector 摄取以服务 AI 与语义搜索、WebSocket 与 HTTP 连接器实现低延迟事件摄取与动作执行、exactly-once 交付，以及以 DataFusion 作为默认分析引擎（[Announcing RisingWave 3.0](https://risingwave.com/blog/announcing-risingwave-3-0-the-real-time-data-platform-for-agentic-ai/)）。

**Kafka 4.2 与 Redpanda 的能力竞赛。** Apache Kafka 4.2.0 于 2026-02-20 发布，带来生产可用的 share groups、Kafka Streams rebalance GA 与安全增强（[Apache Kafka — Confluent Blog](https://www.confluent.io/ko-kr/blog/category/apache-kafka/)）。Redpanda Streaming 26.1（2026-03-31 GA）宣称推出业界首个「可适应流引擎」，可在 topic 级别平衡性能、安全与效率而无需维护多套专用集群；Redpanda 是 Kafka API 兼容替代，官方称延迟较 Kafka 低最高 10 倍（[Redpanda Streaming 26.1](https://www.redpanda.com/press/redpanda-streaming-26-1-introduces-industrys-first-adaptable-streaming-engine)、[Platform capabilities — Redpanda](https://www.redpanda.com/data-streaming/platform-capabilities)）。

## 核心技术与关键概念

**CDC。** CDC 从事务日志捕获行级变更并流向下游；主流工具有开源的 Debezium（覆盖 PostgreSQL、MySQL、MongoDB、SQL Server、Oracle，输出到 Kafka topic，数据库支持最广）与流式数据库 RisingWave（原生 PostgreSQL、MySQL，无需 Kafka/Debezium 中间件，直接产出物化视图、Iceberg、Kafka）（[Data Integration for Streaming: Tools, Patterns, and Best Practices (2026)](https://risingwave.com/blog/data-integration-streaming-tools-patterns-2026/)）。RisingWave 可原生读取 PostgreSQL、MySQL、MongoDB 的变更日志而无需中间件，流程为 CREATE SOURCE → CREATE MATERIALIZED VIEW 实时变换 → 查询物化视图或 CREATE SINK 推送下游（[Change Data Capture (CDC) — Complete Guide](https://www.risingwave.com/guides/change-data-capture-guide/)）。

**增量物化视图。** 流式数据库中的物化视图并非按计划刷新的静态快照，而是随新 CDC 事件到达自动更新的增量维护查询结果；源库一行 insert/update/delete 会在毫秒级传播到物化视图（[PostgreSQL CDC to Streaming SQL](https://risingwave.com/blog/postgresql-cdc-streaming-sql-tutorial/)）。

**批与流的质量控制差异。** 批量与流式在数据质量上的关键差异为：检查时机（加载后 vs 持续实时）、坏数据影响（污染可重跑的批次 vs 立即传播给在线消费者）、补救方式（删坏行重跑转换 vs DLQ+回放或补偿事件）、schema 演进（协调式低频 vs 持续且需向后兼容）、延迟容忍（T+1 小时级 vs 秒到分钟级）（[Data Quality in Streaming Pipelines](https://streamkap.com/resources-and-guides/data-quality-streaming-pipelines)）。

**Flink vs Materialize 等选型维度。** 流式数据库对比涉及编程接口（PostgreSQL 兼容 SQL + UDF vs 仅 SQL）、原生 CDC 源（内置 vs 需 Debezium+Kafka Connect）、连接器生态（50+ vs 较少）与 Iceberg 集成（原生 MoR/CoW/compaction/REST catalog vs 不支持）（[RisingWave vs Materialize](https://www.risingwave.com/risingwave-vs-materialize/)）。

**有状态处理、水位线与精确一次。** 与批处理不同，流处理的难点在于「状态」与「时间」。有状态算子（如聚合、连接、去重）需要在跨事件之间维护中间状态，其状态通常以 changelog 方式持久化到外部存储以支持故障恢复。事件时间（event time）与处理时间（processing time）的割裂引出水位线（watermark）机制：水位线用来估计「某时间点之前的事件已基本到齐」，从而决定何时触发窗口计算与何时丢弃迟到数据。精确一次（exactly-once）语义则要求源端可回放（如 Kafka offset 或 CDC LSN）、算子状态可快照、sink 端支持幂等或事务提交三者配合，RisingWave 3.0 即在交付语义上强调 exactly-once（[Announcing RisingWave 3.0](https://risingwave.com/blog/announcing-risingwave-3-0-the-real-time-data-platform-for-agentic-ai/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Apache Kafka**（https://kafka.apache.org/）— 事件日志，4.0 起纯 KRaft。
- **Apache Flink**（https://flink.apache.org/）— 流计算引擎，动态 Iceberg Sink。
- **Spark Structured Streaming**（https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html）— 微批流处理。
- **RisingWave**（https://risingwave.com/）— 流式数据库，原生 CDC + 增量物化视图。
- **Materialize**（https://materialize.com/）— 流式 SQL 数据库。
- **Debezium**（https://debezium.io/）— 开源 CDC。
- **Confluent Cloud**（https://www.confluent.io/）— 托管 Kafka 与 Flink、Materialized Tables。

## 关键数据与评测结果（附来源）

- Kafka 4.0 为首个无 ZooKeeper 的主要版本，升级需 KRaft 模式且元数据版本 ≥ 3.3.x（[Upgrading](https://kafka.apache.org/40/getting-started/upgrade/)）。
- 动态 Iceberg Sink 支持 Iceberg ≥ 1.10.0、Flink 1.20/2.0/2.1（[Flink Blog](https://flink.apache.org/2025/11/11/from-stream-to-lakehouse-kafka-ingestion-with-the-flink-dynamic-iceberg-sink/)）。
- RisingWave 提供 50+ 原生 source/sink 连接器（[RisingWave vs Materialize](https://www.risingwave.com/risingwave-vs-materialize/)）。
- 流式链路的端到端延迟可低至毫秒级（CDC 事件传播到物化视图）（[PostgreSQL CDC to Streaming SQL](https://risingwave.com/blog/postgresql-cdc-streaming-sql-tutorial/)）。

## 趋势与争议

**延迟与成本的权衡仍是主线。** 流式降低延迟，但引入 schema 持续演进、exactly-once 语义、DLQ 与回放等额外复杂度。Confluent 强调按吞吐而非数据变更量计费的流式优先架构可降低 TCO，此为厂商观点，需与自身成本模型对照。

**「真正的流」与「微批」的路线分歧。** Flink 代表逐事件处理，Spark Structured Streaming 以微批实现近似实时，二者在状态管理、乱序处理与延迟上取舍不同。

**流式数据库与湖仓的边界模糊。** 动态 Iceberg Sink、Materialized Tables（偏移记账与作业迁移自动化）让流处理与湖仓从「两套系统」走向统一，厂商生态（Confluent、RisingWave、Materialize）围绕「谁的 catalog/格式/引擎做控制面」展开竞争。

## 参考来源

- [Apache Kafka 4.0.0 Release Announcement](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/)
- [Upgrading (Kafka 4.0)](https://kafka.apache.org/40/getting-started/upgrade/)
- [2025 - The year gone by (Confluent)](https://developer.confluent.io/newsletter/2025-the-year-gone-by/)
- [Posts in 2026 (Kafka Blog)](https://kafka.apache.org/blog/)
- [From Stream to Lakehouse: Kafka Ingestion with the Flink Dynamic Iceberg Sink](https://flink.apache.org/2025/11/11/from-stream-to-lakehouse-kafka-ingestion-with-the-flink-dynamic-iceberg-sink/)
- [New in Confluent Cloud: Making Data, Pipelines, and Ops Accessible for AI-Ready Streaming](https://www.confluent.io/ko-kr/blog/2026-q2-confluent-cloud-launch/)
- [Announcing RisingWave 3.0: The Real-Time Data Platform for Agentic AI](https://risingwave.com/blog/announcing-risingwave-3-0-the-real-time-data-platform-for-agentic-ai/)
- [RisingWave vs Materialize Comparison](https://www.risingwave.com/risingwave-vs-materialize/)
- [Data Integration for Streaming: Tools, Patterns, and Best Practices (2026)](https://risingwave.com/blog/data-integration-streaming-tools-patterns-2026/)
- [Change Data Capture (CDC) — Complete Guide](https://www.risingwave.com/guides/change-data-capture-guide/)
- [PostgreSQL CDC to Streaming SQL: A Complete Tutorial](https://risingwave.com/blog/postgresql-cdc-streaming-sql-tutorial/)
- [Data Quality in Streaming Pipelines: A Practical Framework](https://streamkap.com/resources-and-guides/data-quality-streaming-pipelines)
- [Apache Kafka — Confluent Blog](https://www.confluent.io/ko-kr/blog/category/apache-kafka/)
- [Redpanda Streaming 26.1 Introduces Industry's First Adaptable Streaming Engine](https://www.redpanda.com/press/redpanda-streaming-26-1-introduces-industrys-first-adaptable-streaming-engine)
- [Platform capabilities — Redpanda Data Streaming](https://www.redpanda.com/data-streaming/platform-capabilities)