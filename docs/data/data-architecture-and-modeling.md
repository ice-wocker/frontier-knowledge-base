# 数据架构与建模

> 最后更新：2026-09-26 ｜ 领域：数据·工程与架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

数据架构与建模关注两件事：数据在系统间如何分层与流动（架构），以及数据以何种结构被组织与表达（建模）。经典的三条建模流派——Inmon 的 3NF 自顶向下、Kimball 的维度建模（星型/雪花）与 Data Vault 2.0 的企业级整合模型——至今仍是架构选型的坐标系，但在列式引擎与湖仓普及后，其物理落地形态已发生显著变化。

## 最新进展（2025–2026）

**Medallion（奖章）分层成为湖仓默认范式。** Medallion 架构用三层组织湖仓数据：bronze（原始数据）、silver（清洗与富化数据）、gold（面向业务的特选数据），层级越高代表数据质量越高（[Understand medallion architecture for Fabric with OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-medallion-lakehouse-architecture)、[What is medallion architecture?](https://cloud.google.com/discover/what-is-medallion-architecture)）。其设计遵循 ACID 原则以保障数据的准确性与可靠性：数据从原始形式开始，原始副本被保留为可信事实源（[在 Fabric 中实现 Medallion Lakehouse 体系结构](https://learn.microsoft.com/zh-cn/fabric/onelake/onelake-medallion-lakehouse-architecture)）。gold 层常采用星型 schema 或为快速读取优化的表，因其已预聚合与预计算，在仪表盘中加载很快（[What is medallion architecture?](https://cloud.google.com/discover/what-is-medallion-architecture)）。

**开放表格式成为 2026 湖仓的地基。** 架构演进的判断是：2026 湖仓的基础不再是专有存储格式，而是 Apache Iceberg、Apache Hudi、Delta Lake 等开放表格式，它们带来事务、schema 演进、时间旅行等数据库式能力（[The Future-Proof Modern Data Stack for 2026](https://ansivus.com/blog/the-future-proof-modern-data-stack-for-2026-key-components-architectures)）。

**语义层与指标层兴起。** 架构从「指标目录」转向「可组合分析（composable analytics）」。开放式语义层如 Cube 以 cube（事实）与 view（连接）在 JS/YAML 中声明度量、维度与连接，并对外暴露 Postgres 兼容 SQL、REST、GraphQL 与 MCP 端点，使 AI agent 能像查询 Postgres 一样查询语义指标（[Composable Analytics Beats Metric Catalogs](https://tuts.alexmercedcoder.dev/2026/2026-06-08-composable-analytics-semantic-layers-expressiveness/)）。dbt 则被广泛视为转换层事实标准，将 SQL 转换变为版本控制、可测试、可文档化的代码（[AI-Ready Data Architecture in 2026](https://addepto.com/blog/modern-data-architecture-cost-effective-innovations-for-2026/)）。

## 核心技术与关键概念

**三层数仓分层。** 传统数仓以 Inmon 的 3NF 集成核心 + 面向部门的集市组织；云数仓时代演化为 staging/raw → integrated/cleansed → mart/serving 的分层，并与 Medallion 的 bronze/silver/gold 一一对应。silver 层负责标准化、去重与校验，schema 采用业务标准命名与类型，主键唯一，更新策略多为 SCD Type 1（原地更新）或 Type 2（保留历史）（[Medallion Architecture: Bronze, Silver, Gold Layers](https://nitinkc.github.io/DataWarehouseLearnings/03-medallion-architecture/)）。

**维度建模（Kimball）。** 核心要素包括事实表的粒度（grain）、一致性维度（conformed dimension）与缓慢变化维 SCD（Type 1/2/3），面向分析师与 OLAP 的简洁性是其最大优势（[Architektury datových skladů: Inmon, Kimball a Data Vault](https://www.keymaker.cz/architektury-datovych-skladu-inmon-kimball-a-data-vault-komparace/)）。

**Data Vault 2.0。** 为应对企业整合挑战而生，三大结构件为：Hub（以自然业务键标识的核心业务概念，不可变）、Link（Hub 间关系）、Satellite（描述性属性，含历史、记录来源、加载日期）。业务逻辑被上移到 business vault，信息集市（information marts）则以经典 Kimball 星型对外服务——business vault 是增量的，叠加在 raw vault 之上而不修改它（[Data Vault 2.0](https://datavidhya.com/learn/data-modeling-and-warehouse/modern-approaches/data-vault/)、[Why data warehouses fail](https://blackthorn-vision.com/blog/why-data-warehouses-fail-and-how-to-design-one-that-doesnt/)）。

**自动化建模。** Data Vault 2.0 的落地借助 dbt 包自动化：AutomateDV（原 dbtvault）与 datavault4dbt 提供标准 Data Vault 2.0 特性，从元数据（表名与映射）生成并运行 ETL 代码，且利用 dbt 并行加载能力（[Manage enterprise-scale complexity with confidence](https://www.getdbt.com/product/data-vault)、[AutomateDV](https://dbtvault.readthedocs.io)）。

**粒度与一致性维度。** 无论采用哪种流派，维度建模的基本功都在于确定事实表的粒度（grain）——即一行事实代表什么业务事件。粒度过粗会丢失分析细节，过细则导致事实表急剧膨胀。一致性维度（conformed dimension）是跨多个事实表共享的维度定义，它保证不同业务过程的数据可按同一口径对齐，是「单一事实版本」得以成立的前提。缓慢变化维（SCD）则记录维度属性随时间的变化：Type 1 直接覆盖、不保留历史；Type 2 新增版本行并标注有效期；Type 3 以附加列记录前后值。选择哪种 SCD 取决于审计与分析需求，Type 2 在需要追溯历史归属（如客户所属区域变更）的场景中更为常见（[Architektury datových skladů](https://www.keymaker.cz/architektury-datovych-skladu-inmon-kimball-a-data-vault-komparace/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Medallion 架构**（https://learn.microsoft.com/en-us/fabric/onelake/onelake-medallion-lakehouse-architecture）— 湖仓三层分层范式。
- **dbt**（https://www.getdbt.com/）— 转换层与语义/指标层。
- **AutomateDV / dbtvault**（https://dbtvault.com）— Data Vault 2.0 自动化 dbt 包。
- **Cube**（https://cube.dev/）— 开放式可组合语义层。
- **Apache Iceberg / Delta Lake / Apache Hudi** — 开放表格式底座（详见湖仓文件）。

## 关键数据与评测结果（附来源）

- Medallion 三层为 bronze/silver/gold，层级越高数据质量越高（[Microsoft Learn](https://learn.microsoft.com/en-us/fabric/onelake/onelake-medallion-lakehouse-architecture)）。
- silver 层更新策略以 SCD Type 1/Type 2 为主（[Medallion Architecture](https://nitinkc.github.io/DataWarehouseLearnings/03-medallion-architecture/)）。
- Data Vault 三大结构件为 Hub、Link、Satellite，business vault 为增量叠加层（[Data Vault 2.0](https://datavidhya.com/learn/data-modeling-and-warehouse/modern-approaches/data-vault/)）。

## 趋势与争议

**流派之辩：经典方法论是否过时。** 一种 2026 年的观点认为，列式引擎普及后，Inmon 的 3NF 自顶向下与 Kimball 作为物理模式（星型 schema）已显过时，但「维度建模作为一种思考方式」依然有效；Data Vault 2.0 对中型组织而言过于繁重，仅在大型企业中仍然适用（[DWH в 2026: четыре зоны вместо Inmon, Kimball и Data Vault 2.0](https://habr.com/en/articles/1035136/)）。此论断属单一来源观点，与主流厂商文档并列呈现。

**选型取决于主导风险。** 中立建议是：若主导风险是 BI 交付缓慢，倾向 Kimball；若是企业级不一致，倾向 Inmon；若是来源波动与可审计性，倾向 Data Vault（[Kimball vs Inmon vs Data Vault 2.0](https://talkingschema.ai/blog/compare-inmon-kimball-datavault)）。

**规范化与建模之争仍在延续。** 湖仓范式下 bronze/silver 层常保留较高规范化以控制冗余，gold/集市层则反规范化以便分析；而 Data Vault 的软件工程化（可自动加载、可审计）与 Kimball 的易用性之间，仍是企业架构需要权衡的核心张力。

**架构演进的三条现实路径。** 综合 2026 年的多方资料，数据架构演进大致沿三条路径展开：其一，以开放表格式为地基的 Lakehouse，把事务与性能叠加到对象存储之上，成为云时代默认底座；其二，Data Mesh 主张按领域拆分数据产品的所有权与责任，缓解中心化数据团队的瓶颈；其三，以语义/指标层为核心的可组合分析，把度量定义从物理表解耦，供 BI 与 AI agent 统一消费。三条路径并非互斥，实践中常见的组合是以 Lakehouse 承载存储、以领域所有权组织治理、以语义层对外提供一致指标。需要注意的是，Data Vault 的落地高度依赖自动化工具（如 AutomateDV、datavault4dbt），若缺乏自动化，其 Hub/Link/Satellite 的建模与加载成本会显著抬高，这也是「Data Vault 对中型组织过于繁重」这一判断的重要背景。

## 参考来源

- [Understand medallion lakehouse architecture for Fabric with OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-medallion-lakehouse-architecture)
- [What is medallion architecture?](https://cloud.google.com/discover/what-is-medallion-architecture)
- [在 Fabric 中实现 Medallion Lakehouse 体系结构](https://learn.microsoft.com/zh-cn/fabric/onelake/onelake-medallion-lakehouse-architecture)
- [Medallion Architecture: Bronze, Silver, Gold Layers](https://nitinkc.github.io/DataWarehouseLearnings/03-medallion-architecture/)
- [DWH в 2026: четыре зоны вместо Inmon, Kimball и Data Vault 2.0](https://habr.com/en/articles/1035136/)
- [Kimball vs Inmon vs Data Vault 2.0: Data Warehouse Architecture Guide](https://talkingschema.ai/blog/compare-inmon-kimball-datavault)
- [Architektury datových skladů: Inmon, Kimball a Data Vault – komparace](https://www.keymaker.cz/architektury-datovych-skladu-inmon-kimball-a-data-vault-komparace/)
- [Data Vault 2.0 — Scalable, Auditable Warehouse Architecture](https://datavidhya.com/learn/data-modeling-and-warehouse/modern-approaches/data-vault/)
- [Why data warehouses fail and how to design one that doesn't](https://blackthorn-vision.com/blog/why-data-warehouses-fail-and-how-to-design-one-that-doesnt/)
- [Manage enterprise-scale complexity with confidence (dbt Data Vault)](https://www.getdbt.com/product/data-vault)
- [AutomateDV | Data Vault Automation Tool](https://dbtvault.com)
- [AutomateDV Docs](https://dbtvault.readthedocs.io)
- [The Future-Proof Modern Data Stack for 2026](https://ansivus.com/blog/the-future-proof-modern-data-stack-for-2026-key-components-architectures)
- [Composable Analytics Beats Metric Catalogs](https://tuts.alexmercedcoder.dev/2026/2026-06-08-composable-analytics-semantic-layers-expressiveness/)
- [AI-Ready Data Architecture in 2026: Lakehouse, Fabric, Mesh](https://addepto.com/blog/modern-data-architecture-cost-effective-innovations-for-2026/)