# OLAP 与查询引擎

> 最后更新：2026-09-26 ｜ 领域：数据·工程与架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

OLAP（联机分析处理）与查询引擎面向大规模数据的分析与聚合查询，核心设计是列式存储加向量化执行：数据按列存储以提高压缩率与扫描效率，执行引擎以「批」（向量）为单位处理，而非逐行迭代。当前主流开源引擎包括 ClickHouse（实时 OLAP）、Apache Doris 与 StarRocks（实时数仓/湖仓查询）、DuckDB（嵌入式分析）与 Apache Druid（时序/交互分析），各自针对不同 workload 优化。

OLAP 与 OLTP 的设计目标根本不同：OLTP 面向高并发的单行读写与短事务，强调点查延迟与并发一致性，多采用行存 + B+ 树；OLAP 面向少量复杂查询扫描海量数据，强调吞吐与扫描效率，多采用列存 + 向量化。这一分野决定了二者的存储布局、索引策略与执行模型几乎不可通用。近年出现的 HTAP（混合事务分析处理）与「实时数仓」试图在同一系统内同时服务两类负载，但通常需要在写入路径（如主键模型、增量物化）与读取路径（列式 + 向量化）之间做大量工程折中，而非简单地把行存换成列存。

## 最新进展（2025–2026）

**ClickHouse 在 ClickBench 上持续领先。** 据 ClickHouse 发布的 2026 年「最快 OLAP 数据库」排行（以 ClickBench 为基准），ClickHouse 在 43 条查询中于 32 条上胜出或并列，热缓存中位延迟 148 ms，尾部延迟（Q28）9.6 s（[The fastest OLAP databases in 2026](https://clickhouse.com/resources/engineering/fastest-olap-databases)）。其 2026 列式数据库选型指南给出的建议是：实时 OLAP、面向客户的分析与 agentic analytics 选 ClickHouse；多 TB 的 BI 与数仓也选 ClickHouse；纯时序、以时间为主要访问维度选 QuestDB；高并发点查选 Pinot；单机/嵌入式选 DuckDB 或 ClickHouse（[Best columnar databases in 2026](https://clickhouse.com/resources/engineering/best-columnar-databases)）。需注意该排行与建议来自 ClickHouse 自身，为主观口径。

**Apache Doris 与 StarRocks 以多表关联与湖仓见长。** Apache Doris 官方基准页显示，在 13 条偏向宽表 join 与聚合的星型 schema 基准中，总耗时 30.1s（对比 Redshift 30.1s、Snowflake 32.9s、ClickHouse 82.2s）；在 TPC-H sf1000 总运行时间上，Doris 为 53.8s（Snowflake 102.5s、Redshift 120.6s、ClickHouse 279.0s）（[Apache Doris benchmarks](https://doris.incubator.apache.org/why-doris/benchmarks/)）。Doris 官方对比文档强调其相较 ClickHouse 的差异：具备强一致性主键存储模型支持同步更新与删除（ClickHouse 仅异步更新、更新后可读到旧值）、提供基于 Arrow-Flight 协议的高吞吐读取 API、并作为数据湖查询引擎支持 Hive/Hudi/Iceberg/Parquet（[Apache Doris vs ClickHouse](https://doris.apache.org/zh-CN/docs/3.x/gettingStarted/alternatives/alternative-to-clickhouse)）。StarRocks 官方 SSB-Flat 基准称，在 100 GB 数据集上其整体查询性能约为 ClickHouse 的 1.87 倍、Apache Druid 的 4.75 倍（[SSB Flat-table Benchmarking](https://docs.starrocks.io/docs/benchmarking/SSB_Benchmarking/)）。上述基准均为各厂商自测口径，互有冲突，应并列看待。

**DuckDB v2.0 走向分布式。** DuckDB 长期以快速、嵌入式、进程内列式数据库著称；v2.0 距 1.5 版累计超过 10000 次提交，是一次重大架构演进，将其运行边界扩展到分布式拓扑并稳定插件生态，同时不牺牲单二进制的简洁性，GA 计划于秋季发布（[Beyond Embedded: How DuckDB v2.0 Shifts Architecture toward Distributed Network Capabilities](https://www.infoq.com/news/2026/08/duckdb-v2-distributed/)）。v2.0 预览显示，行组裁剪被大幅扩展——min-max 索引（zone map）与 Parquet Bloom filter 现可跳过 struct、list、decimal、UUID、IN 过滤乃至函数谓词的数据（[A Preview of DuckDB v2.0](https://www.duckdb.org/2026/08/17/duckdb-20-highlights)）。生态侧，DuckDB 现随 dbt v2 内置发布，并支持直接查询 Hugging Face 数据集（[DuckDB](https://duckdb.org/)）。

## 核心技术与关键概念

**列式存储与压缩。** 列式布局让同列数据具有相似分布，从而获得高压缩率（如 ClickHouse 在 ClickBench 中压缩率约 1:…… 见来源原文），并利于只读取所需列。列存是 OLAP 引擎区别于 OLTP 行存的核心。

**向量化执行。** 以 DuckDB 为例，其执行引擎采用「Vector Volcano」模型：查询执行从物理计划根节点拉取第一个数据 chunk，chunk 是结果集/中间结果/基表的水平子集，节点递归拉取其子节点的 chunk；其向量运算库通过 C++ 模板为所有支持数据类型展开代码（[DuckDB: an Embeddable Analytical Database (SIGMOD 2019)](https://duckdb.org/pdf/SIGMOD2019-demo-duckdb.pdf)）。DuckDB 的循环以向量为单位，标准向量大小为 2048（STANDARD_VECTOR_SIZE），「对向量做紧凑循环」是其查询引擎的核心（[Design and Implementation of DuckDB Internals](https://blobs.duckdb.org/slides/DiDi-07.pdf)）。

**实时更新与湖仓查询。** 支持同步主键更新/删除（Doris 强一致主键模型）与异步更新（ClickHouse）是实时数仓的重要分野；能否作为湖仓查询引擎直接读取开放表格式，成为新一代 OLAP 的关键能力。

**MPP 与 join 优化。** 现代 OLAP 引擎多采用 MPP（大规模并行处理）架构：数据按分区分桶分布到多个节点，查询被拆分为算子片段并行执行，再通过 shuffle 汇总。多表关联（join）通常是分析查询的瓶颈，因此各家引擎在 join 顺序、runtime filter、向量化 hash join 与基于代价的优化器上投入巨大。Doris 的 Nereids 优化器基于 Cascades 框架、结合 RBO 与 CBO，正是为复杂 join 生成高效计划而设计（[Query Optimizer Introduction](https://doris.incubator.apache.org/docs/4.x/query-acceleration/optimization-technology-principle/query-optimizer/)）。此外，面向 AI/数据科学的集成能力（如 Arrow-Flight 高吞吐读取）正成为 OLAP 引擎的新竞争维度，用于把分析结果高效喂给训练与推理管道（[Apache Doris vs ClickHouse](https://doris.apache.org/zh-CN/docs/3.x/gettingStarted/alternatives/alternative-to-clickhouse)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **ClickHouse**（https://clickhouse.com/）— 实时 OLAP，亚秒级延迟。
- **Apache Doris**（https://doris.apache.org/）— 实时数仓，强一致主键模型、湖仓查询。
- **StarRocks**（https://www.starrocks.io/）— 高性能实时分析，多表关联优化。
- **DuckDB**（https://duckdb.org/）— 嵌入式分析数据库，v2.0 走向分布式。
- **Apache Druid**（https://druid.apache.org/）— 时序/交互式分析。
- **QuestDB**（https://questdb.io/）— 时序优先。
- **Apache Pinot**（https://pinot.apache.org/）— 高并发点查。

## 关键数据与评测结果（附来源）

- ClickBench：ClickHouse 43 条查询中 32 条胜出或并列，热缓存中位 148 ms（ClickHouse 自测，[来源](https://clickhouse.com/resources/engineering/fastest-olap-databases)）。
- Doris 星型 schema 基准总耗时 30.1s；TPC-H sf1000 总耗时 53.8s（Doris 官方，[来源](https://doris.incubator.apache.org/why-doris/benchmarks/)）。
- StarRocks SSB-Flat 100GB：整体性能约为 ClickHouse 1.87 倍、Druid 4.75 倍（StarRocks 官方，[来源](https://docs.starrocks.io/docs/benchmarking/SSB_Benchmarking/)）。
- DuckDB v2.0 距 1.5 版累计超过 10000 次提交，标准向量大小 2048（[InfoQ](https://www.infoq.com/news/2026/08/duckdb-v2-distributed/)、[DuckDB Slides](https://blobs.duckdb.org/slides/DiDi-07.pdf)）。

## 趋势与争议

**基准数据的厂商偏差。** 上述 ClickBench/TPC-H/SSB 结果均来自各厂商自测，同一对比如 Doris vs ClickHouse、StarRocks vs ClickHouse 的结论互相冲突（Doris 称远超 ClickHouse，ClickHouse 排行又称其领先），选择时不应采信单一结论，需以自身数据分布与查询模式做复现基准。

**实时更新能力的分野。** 强一致主键更新（Doris/StarRocks）对实时数仓的 upsert 场景更友好，ClickHouse 的异步更新在更新后可读到旧值，这是面向实时更新型业务时的关键差异（Doris 官方口径）。

**嵌入式 vs 分布式的边界移动。** DuckDB 长期以单机嵌入式定位，v2.0 向分布式拓扑扩展，与 ClickHouse/Doris 等分布式引擎的边界开始重叠，可能改变「小规模用 DuckDB、大规模用集群」的传统分工。

## 参考来源

- [The fastest OLAP databases in 2026 (ranked by ClickBench)](https://clickhouse.com/resources/engineering/fastest-olap-databases)
- [Best columnar databases in 2026](https://clickhouse.com/resources/engineering/best-columnar-databases)
- [Apache Doris benchmarks](https://doris.incubator.apache.org/why-doris/benchmarks/)
- [Apache Doris vs ClickHouse](https://doris.apache.org/zh-CN/docs/3.x/gettingStarted/alternatives/alternative-to-clickhouse)
- [SSB Flat-table Benchmarking (StarRocks)](https://docs.starrocks.io/docs/benchmarking/SSB_Benchmarking/)
- [Beyond Embedded: How DuckDB v2.0 Shifts Architecture toward Distributed Network Capabilities](https://www.infoq.com/news/2026/08/duckdb-v2-distributed/)
- [A Preview of DuckDB v2.0](https://www.duckdb.org/2026/08/17/duckdb-20-highlights)
- [Design and Implementation of DuckDB Internals: Vectorized Query Execution](https://blobs.duckdb.org/slides/DiDi-07.pdf)
- [DuckDB: an Embeddable Analytical Database (SIGMOD 2019)](https://duckdb.org/pdf/SIGMOD2019-demo-duckdb.pdf)
- [DuckDB – An in-process SQL OLAP database management system](https://duckdb.org/)