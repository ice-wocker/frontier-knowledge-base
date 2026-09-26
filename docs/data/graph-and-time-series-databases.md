# 图数据库与时序数据库

> 最后更新：2026-09-26 ｜ 领域：数据·分布式、治理与分析 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

图数据库与时序数据库是两类为特定数据形态优化的专用数据库。图数据库以节点、边、属性为基本模型，擅长多跳关系遍历、路径查找与连接数据分析，典型产品有 Neo4j、Amazon Neptune、TigerGraph、Stardog 等。时序数据库（TSDB）以时间戳为核心索引维度，针对高吞吐写入、时间窗口聚合、降采样与保留策略优化，典型产品有 InfluxDB、TimescaleDB、QuestDB、ClickHouse 等。近年来两者共同的新驱动力都来自 AI：图库被用作 GraphRAG 与 Agent 的知识层，时序库则承载可观测性、IoT 与实时分析负载。

## 最新进展（2025–2026）

**GQL 成为首个新 ISO 数据库查询语言。** ISO/IEC 39075:2024 GQL 于 2024 年 4 月 11 日获批，是自 1987 年 SQL 以来第一个新的 ISO 数据库语言标准，Cypher 是其主要的输入方言（[Cypher Query Language](https://www.bestaiweb.ai/glossary/cypher-query-language/)）。GQL 采用了 Cypher 的大量查询构造语义（如 `MATCH/RETURN` 形式），因此 Cypher 现已支持大多数 GQL 强制特性及相当一部分可选特性（[GQL conformance](https://www.neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/)）。

**Neo4j 切换到 Cypher 25。** 从 Neo4j 2026.02 起，分布式 neo4j.conf 显式设置 `db.query.default_language=CYPHER_25`（此前默认为 CYPHER_5），新部署的新建数据库默认使用 Cypher 25；版本仍可在 `CREATE DATABASE` 中显式指定，并可通过 `ALTER DATABASE` 随时变更（[Release Notes: Neo4j 2026.02.2](https://neo4j.com/release-notes/database/neo4j-2026-02-2/)）。Neo4j 2026.04 的 GQL 一致性文档也持续更新（[GQL conformance](https://www.neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/)）。

**Neo4j 押注生成式 AI 与图智能。** Neo4j 于 2025 年 10 月 2 日宣布投入 1 亿美元强化其作为"智能体系统默认知识层"的定位，资金用于产品创新（含两款新的 Agent 化产品）以及面向 AI 原生公司的初创扶持计划，计划在 12 个月内支持全球 1000 家初创企业（[Neo4j Invests $100M in GenAI](https://www.businesswire.com/news/home/20251002109386/en/Neo4j-Invests-%24100M-in-GenAI-Launches-New-Agentic-AI-Offerings)）。2026 年 Neo4j 宣布收购 GraphAware，推出基于开放标准的智能分析方案，作为 Palantir Gotham 的替代，并称这是其 1 亿美元 AI 路线图的关键里程碑（[Neo4j Acquires GraphAware](https://neo4j.com/press-releases/neo4j-acquires-graphaware/?hl=en-US)）。公司发展历程中还包括 Aura Graph Analytics（零 ETL 图分析）与面向 100TB+ 规模的 Infinigraph（[Pioneers of Graph Technology](https://neo4j.com/company/)）。

**时序库的引擎重构。** TimescaleDB 推出 Hypercore 混合行列引擎：热数据以行格式服务快速写入与更新，冷数据自动迁移到压缩列存，官方口径下的旧批评（"所有数据都要解压回行"）已不再完全成立（[6 Best Time-Series Databases in 2026](https://basekick.net/blog/best-time-series-databases-2026)）。InfluxDB 进入 3.x 世代（InfluxDB 3 Core 等），QuestDB 则持续以列存与向量化执行主打开销比。

## 核心技术与关键概念

**图模型与查询语言。** 属性图（property graph）与 RDF 是两种主要数据模型。Cypher 使用类 ASCII 图形语法描述图模式，例如 `(node)-[:RELATIONSHIP]->(node)`，直观表达遍历、模式匹配与路径查找，其设计已被 ISO 标准化为 GQL（[Neo4j](https://www.modern-datatools.com/tools/neo4j)）。Neo4j 与 ISO 委员会的其他成员共同推动了 GQL 标准，标准定义了处理属性图的数据结构与基本操作（[Neo4j 欢迎全新的 GQL 国际标准](https://neo4j.ac.cn/press-releases/gql-standard/)）。

**时序模型与引擎设计。** TSDB 的关键在于高持续写入吞吐与并发负载下的稳定查询延迟。QuestDB 自述在 ClickBench 类 OLAP 工作负载上表现较强，并给出对比数据：相对 InfluxDB 3 Core 写入快 12–36 倍、复杂分析查询快 43–418 倍；相对 TimescaleDB 写入快 6–13 倍、复杂查询快 16–20 倍（[Comparing InfluxDB, TimescaleDB, and QuestDB](https://questdb.com/blog/comparing-influxdb-timescaledb-questdb-time-series-databases/)）。

**品类边界的扩张。** 两类专用库都在向通用引擎的边界扩张：图平台开始提供零 ETL 的图分析（Neo4j Aura Graph Analytics）与面向统一事务/分析负载的大规模图引擎（Infinigraph，官方称支持 100TB+ 规模）（[Pioneers of Graph Technology](https://neo4j.com/company/)）；时序侧的代表如 QuestDB 在 ClickBench 类 OLAP 负载上追求与列存分析引擎竞争的能力（[Comparing InfluxDB, TimescaleDB, and QuestDB](https://questdb.com/blog/comparing-influxdb-timescaledb-questdb-time-series-databases/)）。这意味着"专用数据库"的护城河正从数据模型转向执行引擎与生态集成。

**选型取舍。** 当团队需要在同一数据库中同时获得事务与分析能力时，TimescaleDB 的 PostgreSQL 底座是明显优势——不必同时运行两个数据库（[6 Best Time-Series Databases in 2026](https://basekick.net/blog/best-time-series-databases-2026)）。这类"扩展通用数据库"与"专用时序引擎"之间的取舍，是 TSDB 选型的核心议题。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Neo4j**：图智能平台，2026 年主线版本采用 Cypher 25、推进 GQL 一致性，并通过 1 亿美元 GenAI 投资布局 Agent 知识层（[Release Notes: Neo4j 2026.02.2](https://neo4j.com/release-notes/database/neo4j-2026-02-2/)、[Neo4j Press Releases](https://neo4j.com/press-releases/)）。
- **GraphAware（被 Neo4j 收购）**：由 Neo4j 收购后成为其开放标准智能分析方案的组成部分（[Neo4j Acquires GraphAware](https://neo4j.com/press-releases/neo4j-acquires-graphaware/?hl=en-US)）。
- **QuestDB / InfluxDB / TimescaleDB / ClickHouse**：主流时序方案，官方与第三方对比中覆盖吞吐与复杂查询两个维度（[The Best Time-Series Databases in 2026](https://questdb.com/blog/best-time-series-databases/)）。
- **知识图谱平台**：MarketsandMarkets 列出的主要玩家包括 IBM、Oracle、Microsoft、AWS、Neo4j、Progress Software、TigerGraph、Stardog、Franz Inc 等（[Artificial Intelligence (AI) Market Research Reports](https://www.marketsandmarkets.com/artificial-intelligence-ai-market-research-270.html)）。

## 关键数据与评测结果（附来源）

**图数据库市场规模（多口径并列）：**
- 2026 年市场规模 45.0 亿美元，2026–2033 CAGR 18%，2033 年约 200 亿美元（[Graph Database Market](https://www.coherentmarketinsights.com/industry-reports/graph-database-market)）。
- 2025 年 34.2 亿美元、2026 年 43.2 亿美元，2034 年 282.7 亿美元，2026–2034 CAGR 26.45%（[Graph Database Market — Straits Research](https://straitsresearch.com/report/graph-database-market)）。
- 2025 年 35.2 亿美元、2026 年 44.4 亿美元，2035 年 356.4 亿美元，CAGR 25.08%（[Graph Database Market — Market Research Future](https://www.marketresearchfuture.com/reports/graph-database-market-21397)）。
- 2026 年约 36.0 亿美元（援引 Fortune Business Insights）（[Statistics](https://hydradb.com/blog/statistics-building-memory-layers)）。
- 知识图谱市场：2026 年 19.0 亿美元 → 2032 年 98.8 亿美元，CAGR 31.6%（[AI Market Research Reports](https://www.marketsandmarkets.com/artificial-intelligence-ai-market-research-270.html)）。

**时序数据库基准（第三方与厂商口径）：**
- 吞吐对比表（批量插入 / 单条插入）：QuestDB ≈1,500,000 / 250,000 points/s；InfluxDB 3 Core ≈1,000,000 / 180,000；TimescaleDB ≈500,000 / 50,000（[InfluxDB vs QuestDB vs TimescaleDB 2026](https://www.pistack.xyz/posts/influxdb-vs-questdb-vs-timescaledb-self-hosted-time-series-database-guide-2026/)）。
- QuestDB 自述相对 InfluxDB 1.x/2.x 写入快至 34 倍、相对 3 Core 快至 27 倍、重双重 groupby 查询快至 159 倍；相对 TimescaleDB 写入快至 8 倍、复杂查询快至 72 倍（[The Best Time-Series Databases in 2026](https://questdb.com/blog/best-time-series-databases/)）。

## 趋势与争议

其一，**基准数据的可信度争议**：TSDB 的对比数字主要来自厂商自身（如 QuestDB 博客）或第三方博客，测试方法、数据模型与硬件配置差异大，不同来源给出的倍数从"6–13 倍"到"12–36 倍"不等，横向比较需谨慎（[Comparing InfluxDB, TimescaleDB, and QuestDB](https://questdb.com/blog/comparing-influxdb-timescaledb-questdb-time-series-databases/)、[The Best Time-Series Databases in 2026](https://questdb.com/blog/best-time-series-databases/)）。其二，**图数据库市场规模的统计口径分歧显著**：2026 年规模在 35.2 亿–45.0 亿美元之间，CAGR 在 18%–26.45% 之间，同一年的估计值差异接近 10 亿美元，反映定义（是否含图分析服务、知识图谱）与覆盖厂商不同（[Straits Research](https://straitsresearch.com/report/graph-database-market)、[Coherent Market Insights](https://www.coherentmarketinsights.com/industry-reports/graph-database-market)）。其三，**GQL 标准化与实际迁移的时滞**：GQL 于 2024 年获批，但厂商一致性进度不同，Neo4j 到 2026 年仍在推进渐进式一致性，用户需要同时理解 Cypher 版本（5 与 25）与 GQL 的差异（[GQL conformance](https://www.neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/)）。其四，**AI 需求的两面性**：图库受益于 GraphRAG 与 Agent 知识层需求，但也面临"向量数据库 + 传统关系库"组合的替代压力；时序库受益于 IoT 与可观测性，但数据量增长同时推高存储成本。市场驱动方面，有分析预测到 2030 年全球活跃 IoT 设备将超过 290 亿台（[Time Series Database Market Research Report 2034](https://marketintelo.com/report/time-series-database-market)），2025 年 IoT 设备出货已超过 154 亿台（[Time Series Databases Software Market](https://dataintelo.com/report/global-time-series-databases-software-market)）。

## 参考来源

1. [GQL conformance — Neo4j Cypher Manual](https://www.neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/)
2. [Release Notes: Neo4j 2026.02.2](https://neo4j.com/release-notes/database/neo4j-2026-02-2/)
3. [Neo4j 欢迎全新的 GQL 国际标准](https://neo4j.ac.cn/press-releases/gql-standard/)
4. [Cypher Query Language（ISO/IEC 39075:2024 说明）](https://www.bestaiweb.ai/glossary/cypher-query-language/)
5. [Neo4j — modern-datatools](https://www.modern-datatools.com/tools/neo4j)
6. [Neo4j Invests $100M in GenAI, Launches New Agentic AI Offerings](https://www.businesswire.com/news/home/20251002109386/en/Neo4j-Invests-%24100M-in-GenAI-Launches-New-Agentic-AI-Offerings)
7. [Neo4j Acquires GraphAware](https://neo4j.com/press-releases/neo4j-acquires-graphaware/?hl=en-US)
8. [Neo4j Press releases](https://neo4j.com/press-releases/)
9. [Pioneers of Graph Technology — Neo4j company](https://neo4j.com/company/)
10. [Graph Database Market Size and Share Analysis — Coherent Market Insights](https://www.coherentmarketinsights.com/industry-reports/graph-database-market)
11. [Graph Database Market — Straits Research](https://straitsresearch.com/report/graph-database-market)
12. [Graph Database Market — Market Research Future](https://www.marketresearchfuture.com/reports/graph-database-market-21397)
13. [Artificial Intelligence (AI) Market Research Reports — MarketsandMarkets](https://www.marketsandmarkets.com/artificial-intelligence-ai-market-research-270.html)
14. [Statistics — building memory layers](https://hydradb.com/blog/statistics-building-memory-layers)
15. [The Best Time-Series Databases in 2026 (and How to Choose) — QuestDB](https://questdb.com/blog/best-time-series-databases/)
16. [Comparing InfluxDB, TimescaleDB, and QuestDB Time-Series Databases](https://questdb.com/blog/comparing-influxdb-timescaledb-questdb-time-series-databases/)
17. [InfluxDB vs QuestDB vs TimescaleDB: Best Time-Series Database 2026](https://www.pistack.xyz/posts/influxdb-vs-questdb-vs-timescaledb-self-hosted-time-series-database-guide-2026/)
18. [6 Best Time-Series Databases in 2026: An Honest Comparison](https://basekick.net/blog/best-time-series-databases-2026)
19. [Time Series Database Market Research Report 2034 — MarketIntelo](https://marketintelo.com/report/time-series-database-market)
20. [Time Series Databases Software Market — DataIntelo](https://dataintelo.com/report/global-time-series-databases-software-market)