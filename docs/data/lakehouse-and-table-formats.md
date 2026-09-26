# 湖仓一体与表格式

> 最后更新：2026-09-26 ｜ 领域：数据·工程与架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

湖仓一体（Lakehouse）试图把数据湖的可扩展性、开放性与数据仓库的事务性和性能结合起来，其技术地基是开放表格式（Open Table Format）。开放表格式在 Parquet/ORC 等文件格式之上，用元数据层提供 ACID 事务、schema 演进、时间旅行与隐藏分区等数据库式能力。当前三大主流为 Apache Iceberg、Delta Lake 与 Apache Hudi，各自起源与治理归属不同，并通过 Catalog（目录）层实现多引擎共享与统一治理。

理解湖仓需要区分三个层次：底层是廉价、可扩展的对象存储（S3、Azure Blob、GCS）与其上的列式文件格式；中层是开放表格式，负责事务语义与元数据演进；上层是查询引擎与 Catalog，负责读取、写入与治理。与传统 Hive 表相比，开放表格式最大的改变是「元数据不再依赖目录约定」——表的分区、schema 与文件清单都由元数据显式管理，使 schema 演进、分区演进与原子提交成为可能，而不再需要重写或重命名整个目录。这也是湖仓能在同一份数据上同时支持批处理、流式写入与交互式分析的根本原因。需要强调的是，湖仓并非「数据湖 + 数据仓库」的简单叠加，其可行性完全取决于表格式与 Catalog 层能否提供足够强的事务与并发保证。

## 最新进展（2025–2026）

**Iceberg 以 REST Catalog 构建最广生态。** Iceberg 起源于 Netflix，2018 年捐赠给 Apache 软件基金会（ASF）。其设计中心是引擎无关的表元数据规范，具备不可变快照、隐藏分区（分区值由列变换派生）与明确的元数据演进；它有意把范围限定在格式与库，把表维护交给引擎与厂商，并通过 REST catalog 规范吸引到最广的 catalog 与厂商生态（[What is an Open Table Format?](https://hudi.apache.org/blog/2026/07/14/what-is-an-open-table-format/)）。

**Catalog 控制平面成为竞争焦点。** Apache Polaris 是面向 Iceberg 表的 catalog 实现，构建在开源 Iceberg REST 协议之上，可对不同 REST 兼容查询引擎提供集中、安全的读写访问（[Apache Polaris Documentation](https://polaris.apache.org/in-dev/unreleased/)）。REST Catalog 协议的关键价值在于：单一客户端实现可对接任意合规服务端；由于提交逻辑归服务端所有，还带来客户端侧 catalog 无法提供的能力（[REST Catalog Protocol](https://iceberg.apache.org/docs/nightly/rest-protocol/)）。2026 年的对比焦点落在 Polaris、Unity Catalog 与云端 REST catalog 之间：Catalog Commits（2026 GA）把写事务直接协调到 catalog 层，由 catalog 原子提交变更，消除 Spark 与 Flink 等多引擎并发写同表的竞态；Databricks 于 2026 年 4 月开源其 Business Semantics 层核心实现（[Choosing the Right Iceberg Control Plane](https://datalakehousehub.com/blog/2026-05-choosing-iceberg-control-plane/)）。

**Delta Lake 持续迭代。** Delta Lake 4.0 带来新的 catalog 集成、半结构化数据增强、更智能的变更跟踪与性能改进，其中「Drop Feature」允许在不截断全部历史的前提下移除表特性，便于表演进与更多客户端兼容（[Delta Lake 4.0](https://delta.io/blog/2025-09-25-delta-lake-40/)）。4.3 版本推进 UniForm：转换变为原子且增量，大提交在 Delta 事务内原子转换为 Iceberg 元数据，增量转换只重生成变更的日志区间；IcebergCompatV3（实验性）使使用 deletion vectors 的 Delta 表也能启用 UniForm（[Strengthening Catalog-Managed Delta Tables](https://delta.io/blog/2026-06-22-delta-4-3-release/)）。

**Hudi 强调 upsert 与流式。** Hudi 针对基于主键的持续更新优化，其索引可减少需重写的文件数，在频繁小更新的流式场景常优于替代方案（[Apache Iceberg vs Delta Lake vs Apache Hudi 2026](https://reintech.io/blog/apache-iceberg-vs-delta-lake-vs-apache-hudi-2026-table-format-comparison)）。

## 核心技术与关键概念

**开放表格式的能力矩阵。** 三者在 ACID、时间旅行上均支持；Iceberg 支持隐藏分区而 Delta/Hudi 不支持；schema 演进方面 Iceberg 与 Delta 完整支持、Hudi 相对受限（[Iceberg vs Delta Lake vs Hudi](https://blog.datalakehouse.help/iceberg/iceberg-open-table-format/)）。行级变更上，Iceberg 提供 COW、MOR 与 deletion vectors（V3），Delta 提供 COW + deletion vectors，Hudi 提供 COW + MOR 与记录索引 upsert；并发上 Iceberg 为乐观（指针交换）、Delta 为基于日志的乐观、Hudi 含非阻塞并发（NBCC）（[Apache Iceberg vs. Delta Lake vs. Hudi](https://e6data.com/blog/apache-iceberg-vs-delta-lake-vs-hudi)）。schema 演进上 Iceberg 按列 ID（完整安全），Delta 通过列映射（3.x），Hudi 为附加/兼容式（较受限）（同上）。

**Deletion Vectors 与 Liquid Clustering。** Deletion vectors 是加速表修改的存储优化，读取时通过应用删除向量记录的修改来解析当前表状态；所有 Apache Iceberg v3 表默认包含 deletion vectors（[Deletion vectors in Databricks](https://docs.databricks.com/gcp/en/delta/deletion-vectors)）。Liquid clustering 用基于聚类键的自动布局取代表分区与 ZORDER，可在不重写既有数据的前提下重新定义聚类键，适用于流式表与物化视图（[Use liquid clustering for tables](https://docs.databricks.com/aws/en/delta/clustering?language=SQL)）。

**锁定与集成风险。** Iceberg 工具集成最广（Spark、Flink、Trino、Hive、Snowflake、Athena、BigQuery 等），平台锁定风险低；Delta Lake 在 Databricks 内最强、外部持续增长，锁定风险较高；Hudi 集成覆盖 Spark、Flink、Hive、Presto、Trino（[Apache Iceberg vs Hudi vs Delta Lake](https://www.ksolves.com/blog/big-data/apache-iceberg-vs-hudi-vs-delta-lake)）。

**元数据、快照与表维护。** 开放表格式的关键在于把「表」从文件集合抽象为受元数据管理的实体。以 Iceberg 为例，每次写入生成一个新的不可变快照（snapshot），查询按快照解析出一致的文件清单，因而天然支持时间旅行与回滚；隐藏分区（hidden partitioning）让分区值由列变换自动派生，查询者无需感知分区列即可享受分区裁剪。Delta Lake 则用事务日志（_delta_log）记录每次提交的文件增删，其并发控制基于日志的乐观机制。由于这些格式不原地重写数据文件，生产环境必须配套表维护：包括快照过期（snapshot expiration）、小文件合并（compaction）与孤儿文件清理，否则元数据与文件数量会持续膨胀，拖慢查询并抬高存储成本。Catalog 层（Polaris、Unity Catalog、各云 REST catalog）在承担元数据集中管理的同时，也负责快照过期、文件合并等生命周期任务。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Apache Iceberg**（https://iceberg.apache.org/）— 引擎无关、REST Catalog 生态最广。
- **Delta Lake**（https://delta.io/）— Databricks 主导，UniForm、Liquid Clustering、Deletion Vectors。
- **Apache Hudi**（https://hudi.apache.org/）— Uber 起源，Onehouse 主导，upsert/流式强项。
- **Apache Polaris**（https://polaris.apache.org/）— Iceberg REST catalog 控制平面。
- **Unity Catalog**（https://www.databricks.com/product/unity-catalog）— 跨引擎治理与 catalog 管理。

## 关键数据与评测结果（附来源）

- Iceberg 2018 年捐赠 ASF；Delta Lake 由 Databricks 创建；Hudi 由 Uber 起源、Onehouse 主导（[What is an Open Table Format?](https://hudi.apache.org/blog/2026/07/14/what-is-an-open-table-format/)）。
- 治理归属：Iceberg/Hudi 为 ASF，Delta Lake 为 Linux Foundation（[Iceberg vs Delta Lake vs Hudi](https://blog.datalakehouse.help/iceberg/iceberg-open-table-format/)）。
- UniForm 在 4.3 版实现原子且增量转换，IcebergCompatV3 为实验性（[Delta Lake 4.3](https://delta.io/blog/2026-06-22-delta-4-3-release/)）。

## 趋势与争议

**版权与厂商博弈。** 生态竞争的核心从「表格式本身」转向「Catalog 控制平面」：开源 Polaris 与厂商托管 Unity Catalog、云端 REST catalog 之间的取舍，直接关系到多引擎互操作与锁定风险。Iceberg 凭借 REST 规范获得最广生态与最低锁定风险，而 Delta 通过 UniForm 向 Iceberg 元数据互转以缓解锁定担忧，形成「格式互操作」的竞争态势。

**功能口径冲突。** 关于 Hudi 的 schema 演进支持，不同来源表述为「部分支持」与「附加/兼容式（较受限）」，此处并列呈现，不做单一结论；关于 Iceberg 与 Delta 在并发写与 upsert 性能的优劣，各来源排名亦不完全一致，实际选型应依据自身 workload（CDC upsert、流式小更新等）做基准验证。

## 参考来源

- [What is an Open Table Format?](https://hudi.apache.org/blog/2026/07/14/what-is-an-open-table-format/)
- [Iceberg Open Table Format vs. Delta Lake vs. Apache Hudi](https://blog.datalakehouse.help/iceberg/iceberg-open-table-format/)
- [Apache Iceberg vs Delta Lake vs Apache Hudi 2026: Table Format Comparison](https://reintech.io/blog/apache-iceberg-vs-delta-lake-vs-apache-hudi-2026-table-format-comparison)
- [Apache Iceberg vs Hudi vs Delta Lake: How to Choose the Right Open Table Format](https://www.ksolves.com/blog/big-data/apache-iceberg-vs-hudi-vs-delta-lake)
- [Apache Iceberg vs. Delta Lake vs. Hudi](https://e6data.com/blog/apache-iceberg-vs-delta-lake-vs-hudi)
- [Apache Polaris Documentation](https://polaris.apache.org/in-dev/unreleased/)
- [Choosing the Right Iceberg Control Plane: Polaris vs. Unity Catalog vs. Cloud REST](https://datalakehousehub.com/blog/2026-05-choosing-iceberg-control-plane/)
- [REST Catalog Protocol (Apache Iceberg)](https://iceberg.apache.org/docs/nightly/rest-protocol/)
- [Strengthening Catalog-Managed Delta Tables with the Unity Catalog Delta APIs (Delta 4.3)](https://delta.io/blog/2026-06-22-delta-4-3-release/)
- [Delta Lake 4.0](https://delta.io/blog/2025-09-25-delta-lake-40/)
- [Delta Lake Liquid Clustering](https://delta.io/blog/liquid-clustering/)
- [Use liquid clustering for tables](https://docs.databricks.com/aws/en/delta/clustering?language=SQL)
- [Deletion vectors in Databricks](https://docs.databricks.com/gcp/en/delta/deletion-vectors)