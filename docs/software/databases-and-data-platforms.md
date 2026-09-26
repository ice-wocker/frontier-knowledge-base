# 数据库与数据平台

> 最后更新：2026-09-26 ｜ 领域：数据库与数据平台 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

2025–2026 年数据领域的核心变化有两个：**AI 原生（AI-native）成为数据库的一等设计目标**，以及**湖仓一体与开放表格式的融合**。向量检索从独立数据库下沉为通用能力，几乎所有主流数据平台都开始提供 MCP（Model Context Protocol）服务器以直连 AI Agent（[Data Platform Native AI Agent Tooling in 2026](https://tuts.alexmercedcoder.dev/2026/2026-05-31-data-platform-ai-agent-tooling/)）。与此同时，交易型（OLTP）与分析型（OLAP）系统加速收敛，DuckDB、ClickHouse 等系统开始向「数据库即服务器」演进。

## 2025–2026 最新进展

### 1. PostgreSQL 生态

PostgreSQL 18 引入了全新的**异步 I/O（AIO）子系统**，允许并发发出多个 I/O 请求而非顺序等待，支持顺序扫描、位图堆扫描与 VACUUM；在 Linux 上可使用 `io_uring`，其它平台提供基于 worker 的实现（`io_method` 可选 `worker`、`io_uring`、`sync`），官方基准显示某些场景性能提升最高约 3 倍（[PostgreSQL 18 Press Kit](https://www.postgresql.org/about/press/presskit18/)、[PostgreSQL 18 Beta 1 Released!](https://www.postgresql.org/about/news/postgresql-18-beta-1-released-3070/)、[Resource Consumption](https://www.postgresql.org/docs/current/runtime-config-resource.html)）。Postgres 生态已成为 AI 时代最活跃的底座：DynamoDB、ClickHouse 等非 Postgres 系统也在向该生态靠拢。

### 2. 分布式 SQL

- **CockroachDB** v26.2 于 2026-04-27 发布，通过 `distributed_merge.mode` 为 `IMPORT` 操作提供分布式合并（两阶段：先写本地 SST，再由协调者合并摄取）（[What's New in v26.2 — CockroachDB](https://www.cockroachlabs.com/docs/releases/v26.2)）。
- **YugabyteDB** v2026.1 STS 系列引入**多租户资源治理（Resource Governance for Multitenancy）**，基于 Linux cgroups 在争用时公平分配 CPU，并可为数据库配置 CPU 上限（[What's new in the YugabyteDB v2026.1 STS release series](https://docs.yugabyte.com/stable/releases/ybdb-releases/v2026.1/)）。
- **TiDB** 为 MySQL 兼容的分布式 SQL，基于 TiKV 存储、通过 TiFlash 提供 HTAP 分析路径，无需手工分片（[TiDB vs CockroachDB (2026) Comparison Guide](https://www.pingcap.com/compare/cockroachdb-vs-tidb/)）。三者的取舍集中在兼容生态（Postgres vs MySQL）、多区域一致性与延迟、以及乐观/悲观并发控制策略上（[TiDB vs YugabyteDB (2026)](https://www.pingcap.com/compare/yugabytedb-vs-tidb/)）。

### 3. 云原生数据库

- **Amazon Aurora DSQL** 为无服务器分布式 SQL，宣称最高 99.999% 可用性（[Amazon Aurora DSQL features](https://aws.amazon.com/rds/aurora/dsql/faqs/)）；Aurora Serverless 性能提升最高 30% 并增强扩缩能力（[Amazon Aurora 资源](https://aws.amazon.com/cn/rds/aurora/resources/)）。
- **Neon** 于 2025 年 5 月加入 Databricks（2025-05-14 宣布收购意向），其无服务器 Postgres 架构成为 **Lakebase Postgres** 的基础，可运行于 Neon 与 Databricks 两处（[Databricks Agrees to Acquire Neon](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems)、[Neon and Lakebase](https://neon.com/docs/introduction/neon-and-lakebase)）。Lakebase 定位为面向 AI 应用与 Agent 的「运营型数据库」新类别，将运营数据引入湖仓并支持持续自动扩缩（[Databricks Launches Lakebase](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps)）。
- **PlanetScale** 主打高并发 MySQL 兼容；其公开基准对比中声称相对 Neon Lakebase 最高快 1.4 倍、相对 Supabase 最高快 3.4 倍（[PlanetScale Benchmarks](https://planetscale.com/benchmarks)）。

### 4. 向量数据库

向量检索成为 RAG 的基础设施，代表系统包括 pgvector、Pinecone、Weaviate、Qdrant、Milvus 2.6、Chroma、LanceDB。一项针对七个系统的系统性实证评测（涵盖 FAISS、Qdrant、Milvus、Weaviate、Chroma、pgvector、LanceDB）联合考察了检索质量、延迟、吞吐与资源占用（[A Comprehensive Empirical Evaluation of Vector Database Systems for ANN Search](https://arxiv.org/pdf/2608.12812)）。工程实践中，pgvector 因与 Postgres 原生集成、成本最低而适合关系+向量混合场景，Pinecone 主打托管与极致规模，Weaviate 内置 GraphQL 与模块化能力（[Vector Database Comparison 2026](https://bytepane.com/faq/vector-database-comparison-2026-pgvector-pinecone-weaviate-qdrant-chroma-milvus-rag/)）。值得关注的是 **Amazon DynamoDB 于 2026-08-05 正式支持原生向量搜索**，单数毫秒延迟、99%+ 召回，可扩展至数万亿向量且无需复制到独立向量库（[Amazon DynamoDB now supports real-time vector search](https://aws.amazon.com/blogs/aws/amazon-dynamodb-now-supports-real-time-vector-search-at-any-scale/)）。

### 5. OLAP 与实时分析

- **ClickHouse**：在 ClickBench 上于 43 条查询中赢得或并列 32 条，热缓存中位延迟 148 ms（[The fastest OLAP databases in 2026](https://clickhouse.com/resources/engineering/fastest-olap-databases)）；Open House 2026 宣布 ClickHouse Postgres 进入公测，事务吞吐较 AWS RDS 高 5 倍以上，多阶段分布式查询将 TPC-H SF100 从 117.6 秒降至 54.7 秒（[Open House 2026 Day 1](https://clickhouse.com/blog/open-house-2026-day-1)）。
- **DuckDB**：v2.0 代号「Cyanoptera」，预计 2026 年秋季发布，亮点包括 DuckDB 作为服务器、触发器、`VARIANT` 类型、异步 I/O、新 SQL 解析器与新存储格式（[A Preview of DuckDB v2.0](https://www.duckdb.org/2026/08/17/duckdb-20-highlights)）。
- **StarRocks**：采用 MPP 架构、全向量化执行引擎与支持实时更新的列式存储，秒级加载实现近实时分析（[StarRocks](https://docs.starrocks.io/docs/introduction/StarRocks_intro/)）。

### 6. 流处理

- **Apache Kafka 4.2.0** 于 2026-02-20 发布，带来生产可用的 share groups、Kafka Streams rebalance GA 与安全增强（[Apache Kafka — Confluent Blog](https://www.confluent.io/ko-kr/blog/category/apache-kafka/)）。
- **Redpanda Streaming 26.1**（2026-03-31 GA）宣称推出业界首个「可适应流引擎」，可在 topic 级别平衡性能、安全与效率，无需维护多套专用集群（[Redpanda Streaming 26.1](https://www.redpanda.com/press/redpanda-streaming-26-1-introduces-industrys-first-adaptable-streaming-engine)）。Redpanda 是 Kafka API 兼容替代，官方称延迟较 Kafka 低最高 10 倍（[Platform capabilities — Redpanda](https://www.redpanda.com/data-streaming/platform-capabilities)）。

### 7. 湖仓一体与开放表格式

三大开放表格式各有侧重：**Apache Iceberg** 源自 Netflix 并于 2018 年捐赠给 ASF，以引擎无关的元数据规范、不可变快照、隐藏分区与 REST catalog 规范构建了最广的目录与厂商生态；**Delta Lake** 由 Databricks 创建；**Apache Hudi** 侧重流式摄取与索引（[What is an Open Table Format?](https://hudi.apache.org/blog/2026/07/14/what-is-an-open-table-format/)）。**Apache XTable（孵化中）** 可在 Hudi、Iceberg、Delta Lake 之间翻译表元数据而无需复制或重写数据文件，典型模式是用 Hudi 摄取、以 Iceberg 暴露给下游引擎（[Apache Hudi vs Apache Iceberg for Streaming Ingestion](https://hudi.apache.org/blog/2026/08/11/hudi-vs-iceberg-for-streaming-ingestion/)）。Databricks 的 Unity Catalog 已开源并归属 LF AI & Data Foundation（[What is an open lakehouse?](https://www.databricks.com/fr/blog/what-open-lakehouse-open-data-standards-explained)）。

### 8. NoSQL 与缓存

许可之争重塑了缓存格局：**Redis 8** 起提供三许可（RSALv2、SSPLv1 与 OSI 认可的 AGPLv3）（[Licenses — Redis](https://redis.io/legal/licenses/)）；**Valkey** 由 Linux Foundation 支持、采用宽松的 BSD 3-Clause，定位为永久开源的高性能键值存储（[Valkey](https://valkey.io/)、[What is Valkey?](https://redis.io/blog/what-is-valkey/)）。

### 9. 数据库 AI 化趋势

Google Cloud 在 Next '26 发布 **Agentic Data Cloud**，并推出 Database Onboarding Agent 与 Database Observability Agent 两个 AI 数据库代理，覆盖 Day 0 配置与 Day 1/2 监控运维（[Introducing Database Operations Agents](https://cloud.google.com/blog/products/databases/deep-dive-on-new-ai-powered-database-agents)、[What's new with Databases](https://cloud.google.com/blog/products/databases/whats-new-for-google-cloud-databases-at-next26)）。MCP 成为 AI Agent 与企业数据之间的默认桥梁，Weaviate v1.37 等已内置 MCP Server（[Vector Database News April 2026](https://ranksquire.com/2026/05/01/vector-database-news-april-2026/)）。

## 核心技术与关键概念

- **异步 I/O（AIO）**：以 `io_uring`/worker 提升 Postgres 吞吐。
- **HTAP**：TiDB 以 TiFlash 列式副本同时服务事务与分析。
- **开放表格式 + REST Catalog**：Iceberg/Delta/Hudi 与 XTable 实现跨引擎互操作。
- **向量索引与 ANN**：HNSW、Sparse-BM25 等支撑近似最近邻检索与混合搜索。
- **MCP（Model Context Protocol）**：AI Agent 连接数据库的工具协议。
- **Serverless / 分支（Branching）**：Neon 以 copy-on-write 提供数据库分支能力。

## 代表性项目/平台

| 类别 | 项目/平台 | 官方链接 |
|---|---|---|
| 关系型 | PostgreSQL | https://www.postgresql.org/ |
| 分布式 SQL | CockroachDB / TiDB / YugabyteDB | https://www.cockroachlabs.com/、https://www.pingcap.com/、https://www.yugabyte.com/ |
| 云原生 | Aurora / Spanner / Neon / PlanetScale | https://aws.amazon.com/rds/aurora/、https://cloud.google.com/spanner、https://neon.com/、https://planetscale.com/ |
| OLAP | ClickHouse / DuckDB / StarRocks | https://clickhouse.com/、https://duckdb.org/、https://www.starrocks.io/ |
| 流处理 | Kafka / Flink / Redpanda | https://kafka.apache.org/、https://flink.apache.org/、https://www.redpanda.com/ |
| 湖仓 | Iceberg / Delta Lake / Hudi / XTable | https://iceberg.apache.org/、https://delta.io/、https://hudi.apache.org/、https://xtable.apache.org/ |
| NoSQL/缓存 | DynamoDB / Redis / Valkey | https://aws.amazon.com/dynamodb/、https://redis.io/、https://valkey.io/ |
| 向量 | pgvector / Pinecone / Weaviate / Qdrant / Milvus | https://github.com/pgvector/pgvector、https://www.pinecone.io/、https://weaviate.io/、https://qdrant.tech/、https://milvus.io/ |

## 版本与生态数据

| 项目 | 版本/数据 | 来源 |
|---|---|---|
| PostgreSQL | 18（AIO，最高 3x 提升） | postgresql.org |
| CockroachDB | v26.2（2026-04-27） | cockroachlabs.com |
| YugabyteDB | v2026.1 STS（资源治理 EA） | docs.yugabyte.com |
| ClickHouse | ClickBench 43 条查询赢/并列 32 条，中位 148ms | clickhouse.com |
| DuckDB | v2.0 预览（2026 秋） | duckdb.org |
| Kafka | 4.2.0（2026-02-20） | confluent.io |
| Redpanda | Streaming 26.1（2026-03-31 GA） | redpanda.com |
| DynamoDB | 原生向量搜索 GA（2026-08-05） | aws.amazon.com |
| Redis | 8+ 三许可（含 AGPLv3） | redis.io |
| Valkey | BSD 3-Clause / Linux Foundation | valkey.io |

## 趋势与争议

1. **向量能力下沉到通用数据库**：DynamoDB 原生向量搜索、pgvector 流行，正在挤压独立向量数据库的生存空间；向量库转向混合搜索、GPU 加速与 MCP 集成寻找差异化。
2. **OLTP/OLAP 边界消融**：Lakebase、ClickHouse Postgres、TiFlash 等都在打通运营与分析数据，但一致性模型与运维复杂度仍是主要权衡。
3. **许可与开源的博弈**：Redis 的三许可 vs Valkey 的 BSD，反映基础设施软件「开源可持续性」的持续争议。
4. **AI Agent 重塑数据库运维**：从 MCP 集成到自主数据库代理，DBA 工作正被 AI 部分接管，但也带来权限、审计与数据安全的新风险。

## 参考来源

1. [PostgreSQL 18 Press Kit](https://www.postgresql.org/about/press/presskit18/)
2. [PostgreSQL: PostgreSQL 18 Press Kit（中文）](https://www.postgresql.org/about/press/presskit18/zh/)
3. [PostgreSQL 18 Beta 1 Released!](https://www.postgresql.org/about/news/postgresql-18-beta-1-released-3070/)
4. [Resource Consumption — PostgreSQL](https://www.postgresql.org/docs/current/runtime-config-resource.html)
5. [What's New in v26.2 — CockroachDB](https://www.cockroachlabs.com/docs/releases/v26.2)
6. [What's new in the YugabyteDB v2026.1 STS release series](https://docs.yugabyte.com/stable/releases/ybdb-releases/v2026.1/)
7. [TiDB vs CockroachDB (2026) Comparison Guide for Platform Teams](https://www.pingcap.com/compare/cockroachdb-vs-tidb/)
8. [TiDB vs YugabyteDB (2026) Comparison Guide for Platform Teams](https://www.pingcap.com/compare/yugabytedb-vs-tidb/)
9. [Serverless distributed SQL database with active-active high availability – Amazon Aurora DSQL](https://aws.amazon.com/rds/aurora/dsql/faqs/)
10. [Amazon Aurora 资源](https://aws.amazon.com/cn/rds/aurora/resources/)
11. [Databricks Agrees to Acquire Neon](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems)
12. [Neon and Lakebase](https://neon.com/docs/introduction/neon-and-lakebase)
13. [Databricks Launches Lakebase](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps)
14. [PlanetScale Benchmarks](https://planetscale.com/benchmarks)
15. [A Comprehensive Empirical Evaluation of Vector Database Systems for ANN Search](https://arxiv.org/pdf/2608.12812)
16. [Vector Database Comparison 2026](https://bytepane.com/faq/vector-database-comparison-2026-pgvector-pinecone-weaviate-qdrant-chroma-milvus-rag/)
17. [Amazon DynamoDB now supports real-time vector search at any scale](https://aws.amazon.com/blogs/aws/amazon-dynamodb-now-supports-real-time-vector-search-at-any-scale/)
18. [The fastest OLAP databases in 2026 (ranked by ClickBench)](https://clickhouse.com/resources/engineering/fastest-olap-databases)
19. [Open House 2026 Day 1 — ClickHouse](https://clickhouse.com/blog/open-house-2026-day-1)
20. [A Preview of DuckDB v2.0](https://www.duckdb.org/2026/08/17/duckdb-20-highlights)
21. [StarRocks — Database Features](https://docs.starrocks.io/docs/introduction/Features)
22. [Apache Kafka — Confluent Blog](https://www.confluent.io/ko-kr/blog/category/apache-kafka/)
23. [Redpanda Streaming 26.1 Introduces Industry's First Adaptable Streaming Engine](https://www.redpanda.com/press/redpanda-streaming-26-1-introduces-industrys-first-adaptable-streaming-engine)
24. [Features and capabilities — Redpanda](https://www.redpanda.com/data-streaming/platform-capabilities)
25. [What is an Open Table Format? — Apache Hudi](https://hudi.apache.org/blog/2026/07/14/what-is-an-open-table-format/)
26. [Apache Hudi vs Apache Iceberg for Streaming Ingestion](https://hudi.apache.org/blog/2026/08/11/hudi-vs-iceberg-for-streaming-ingestion/)
27. [What is an open lakehouse? Open data standards explained](https://www.databricks.com/fr/blog/what-open-lakehouse-open-data-standards-explained)
28. [Licenses — Redis](https://redis.io/legal/licenses/)
29. [What is Valkey? — Redis](https://redis.io/blog/what-is-valkey/)
30. [Valkey](https://valkey.io/)
31. [Introducing Database Operations Agents — Google Cloud](https://cloud.google.com/blog/products/databases/deep-dive-on-new-ai-powered-database-agents)
32. [What's new with Databases: Powering the agentic future](https://cloud.google.com/blog/products/databases/whats-new-for-google-cloud-databases-at-next26)
33. [Vector Database News April 2026: MCP Arrives](https://ranksquire.com/2026/05/01/vector-database-news-april-2026/)
34. [Data Platform Native AI Agent Tooling in 2026](https://tuts.alexmercedcoder.dev/2026/2026-05-31-data-platform-ai-agent-tooling/)