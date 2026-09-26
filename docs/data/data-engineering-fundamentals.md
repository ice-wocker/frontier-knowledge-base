# 数据工程基础

> 最后更新：2026-09-26 ｜ 领域：数据·工程与架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

数据工程（Data Engineering）是围绕数据的采集、传输、转换、编排与质量保障构建可复用基础设施的工程学科。其核心目标是把分散在业务数据库、SaaS 系统、消息队列与日志中的原始数据，加工为可信、可分析、可被下游 BI、机器学习与 AI 应用消费的数据资产。现代数据栈通常被划分为六个层次：采集（ingestion）、处理（processing）、存储/数仓（warehousing）、转换（transformation）、编排（orchestration）与基础设施（infrastructure），业界普遍认为没有单一工具能覆盖全部六层，团队需要按场景组合选型（[Best Data Engineering Tools in 2026](https://estuary.dev/blog/data-engineering-tools/)）。

从处理范式看，批量（batch）与流式（streaming）是两条主线。批量管道按时间间隔收集并成组处理数据，典型延迟为分钟到小时级；流式管道则逐个事件连续处理，延迟以秒计（[Data Pipeline Best Practices](https://www.databricks.com/blog/data-pipeline-best-practices)）。选择哪条路线取决于下游 SLA：欺诈检测、实时个性化等场景需要流式，而历史报表与模型训练通常可以接受批量。

按采集方式，数据工程又可分为全量抽取、增量抽取与基于日志的 CDC。工程实践中的常见权衡在于：全量抽取实现简单但成本随数据量线性上升；增量与 CDC 虽更高效，却需要处理 schema 演进、乱序事件与初始快照的一致性。数据工程的另一条主线是「管道即代码」：把抽取、转换、编排全部纳入版本控制与 CI/CD，使数据资产的变更可评审、可回滚、可测试，这与软件工程的最佳实践趋同。随着数据量增长，团队普遍从「一次性脚本」演进到「声明式模型 + 编排调度」的组合，这正是 dbt 与编排器协同工作的价值所在。

## 最新进展（2025–2026）

**编排层：Airflow 3 代际更新与资产化范式。** 编排是调度、监控与管理管道执行的顶层。Apache Airflow 仍是最广泛部署的编排工具，其 3.0 版本被称为项目历史上最重大的发布，引入面向服务的架构（Service-Oriented Architecture）、稳定的 DAG 编写接口、事件驱动调度、基于 React 的现代化 UI 与高性能回填，其中 DAG Versioning 是历年社区调查中呼声最高的特性——DAG 会按启动时的版本完整运行，即便运行期间上传了新版本（[Apache Airflow 3 is Generally Available!](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/)、[Introducing Apache Airflow 3](https://www.astronomer.io/blog/intro-to-airflow-3/)）。据工具盘点，Airflow 3.0 发布于 2025 年 4 月，GitHub Star 约 37k；其 3.0.4 补丁版本发布于 2025-08-08（[Data Engineering Tools 2026](https://uvik.net/blog/data-engineering-tools/)、[Airflow Release Notes](https://airflow.apache.org/docs/apache-airflow/3.0.4/release_notes.html)）。

与之竞争的是以「资产为中心（asset-centric）」的 Dagster（约 13k Star）与 Pythonic、装饰器风格的 Prefect（约 19k Star）。Dagster 以数据资产而非任务为管道定义单位，在 ML 管道与复杂平台架构中越来越受偏好；Prefect 则主打更快的本地迭代体验（[Best Data Engineering Software 2026](https://dagster.io/learn/data-engineering-software)、[Airflow vs Prefect vs Dagster](https://www.alpsagility.com/modern-data-stack-orchestration-2026)）。另有 Kestra（约 26.6k Star，2026 年 3 月完成 2500 万美元 A 轮）等 YAML/多语言新秀加入竞争。

**批量与流式的成本再平衡。** 随着数据规模上升，传统批量 ELT 的成本模型开始承压：按数据变更量（如活跃行数）计费的模式在回填、schema 变更、嵌套数据展开时会产生成本尖峰；流式优先的架构则通过增量预处理降低批计算成本与重复抽取开销（[Why ELT Can't Keep Up](https://www.confluent.io/blog/why-batch-elt-breaks-at-scale/)）。

## 核心技术与关键概念

**ETL 与 ELT。** ETL（Extract-Transform-Load）在加载前于独立引擎完成转换，适合算力受限的传统数仓；ELT（Extract-Load-Transform）先将原始数据加载进云数仓/湖仓，再在目标端用 SQL 转换，成为云时代主流，其代表转换层工具是 dbt。

**编排与依赖管理。** 编排器（Airflow/Dagster/Prefect）位于栈顶，负责调度与依赖；典型流程为：编排器触发 Fivetran 完成从 API 抽取并加载到 Snowflake/BigQuery，确认后再触发 dbt 运行 SQL 模型，最后激活 ML 任务（[Airflow vs Prefect vs Dagster](https://www.alpsagility.com/modern-data-stack-orchestration-2026)）。Airflow 以 DAG（有向无环图）建模：任务为节点、依赖为边。

**数据质量（Data Quality）。** 数据质量分为批量与实时两个控制面，二者并非对立——批量提供广度与历史语境、成本更低，实时则能在坏事件污染下游仪表盘、模型或客户流程前将其拦截（[Real Time Data Quality 2026](https://www.digna.ai/real-time-data-quality)）。两者差异体现在检查时机（加载后 vs 持续进行）、坏数据影响（可重跑的批次 vs 立即传播给在线消费者）、补救方式（删行重跑 vs DLQ+回放/补偿事件）、schema 演进（协调式低频 vs 持续且需向后兼容）与延迟容忍（小时级 vs 秒到分钟级）（[Data Quality in Streaming Pipelines](https://streamkap.com/resources-and-guides/data-quality-streaming-pipelines)）。批量管道的主要风险是「静默不完整」——作业看似成功却丢分段，因此需要对比期望分区与观测分区（[Data Quality at Ingestion](https://unstructured.io/insights/data-quality-at-ingestion-a-framework-for-ai-ready-pipelines)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Apache Airflow**（https://airflow.apache.org/）— 编排的事实标准，DAG 中心设计，3.0 引入事件驱动与 DAG 版本化。
- **Dagster**（https://dagster.io/）— 资产中心、可观测性优先的编排。
- **Prefect**（https://www.prefect.io/）— Pythonic 装饰器式编排。
- **dbt**（https://www.getdbt.com/）— 转换层事实标准，将 SQL 转换为可版本控制、可测试、可文档化的代码。
- **Apache Kafka**（https://kafka.apache.org/）— 事件流采集与传输。
- **Fivetran**（https://www.fivetran.com/）— SaaS 连接器与托管采集。
- **Estuary**（https://estuary.dev/）— CDC 与批量采集。
- **Docker / Kubernetes**（https://kubernetes.io/）— 管道运行的基础设施底座。

## 关键数据与评测结果（附来源）

- Airflow GitHub Star 约 37k、Dagster 约 13k、Prefect 约 19k、Kestra 约 26.6k（2026 年盘点，[Data Engineering Tools 2026](https://uvik.net/blog/data-engineering-tools/)）。
- Airflow 3.0 于 2025 年 4 月发布；Airflow 3.0.4 补丁版本日期为 2025-08-08（[Airflow Release Notes](https://airflow.apache.org/docs/apache-airflow/3.0.4/release_notes.html)）。
- 批量管道典型延迟为分钟到小时，流式管道延迟以秒计（[Data Pipeline Best Practices](https://www.databricks.com/blog/data-pipeline-best-practices)）。

## 趋势与争议

其一，**编排的资产化与任务化之争**：Dagster 主张以数据资产为管道定义核心，更利于 ML 管道与平台治理；Airflow 的任务/DAG 模型则拥有最大存量生态，迁移成本高，社区实践上常见「新项目用 Dagster/Prefect、存量留在 Airflow」的混合格局。

其二，**本地开发体验的争论**：Prefect 阵营批评 Airflow 3 虽为史上最大发布，仍优先面向生产部署而非开发者快速迭代，并称迁移到 Prefect 可带来约 3 倍开发速度提升、成本下降超 50%，此为厂商口径，需与中立基准对照（[Airflow Local Development Sucks](https://www.prefect.io/blog/airflow-local-development)）。

其三，**批量 vs 流式的成本与复杂度权衡**：批量胜在成本可控、执行窗口可预测、回填明确；流式胜在低延迟，但引入 schema 演进持续兼容、DLQ 与回放等额外运维复杂度。

## 参考来源

- [Best Data Engineering Software: Top 12 Solutions in 2026](https://dagster.io/learn/data-engineering-software)
- [Data Engineering Tools 2026: 75+ Tools Across 14 Layers](https://uvik.net/blog/data-engineering-tools/)
- [Data Engineering 2026: Pipelines, Tools, and Career Guide](https://precisionaiacademy.com/blog/data-engineering-guide-2026)
- [Best Data Engineering Tools in 2026](https://estuary.dev/blog/data-engineering-tools/)
- [Airflow vs Prefect vs Dagster (and where dbt & Fivetran fit in 2026)](https://www.alpsagility.com/modern-data-stack-orchestration-2026)
- [Apache Airflow Release Notes 3.0.4](https://airflow.apache.org/docs/apache-airflow/3.0.4/release_notes.html)
- [Apache Airflow 3 is Generally Available!](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/)
- [Apache Airflow 3.0 Release Notes](https://airflow.apache.org/docs/apache-airflow/3.0.0/release_notes.html)
- [Introducing Apache Airflow 3](https://www.astronomer.io/blog/intro-to-airflow-3/)
- [Airflow Local Development Sucks](https://www.prefect.io/blog/airflow-local-development)
- [Real Time Data Quality: A Practical Guide for 2026](https://www.digna.ai/real-time-data-quality)
- [Data Quality at Ingestion: A Framework for AI-Ready Pipelines](https://unstructured.io/insights/data-quality-at-ingestion-a-framework-for-ai-ready-pipelines)
- [Data Pipeline Best Practices](https://www.databricks.com/blog/data-pipeline-best-practices)
- [Why ELT Can't Keep Up in the Era of High-Scale Data Engineering](https://www.confluent.io/blog/why-batch-elt-breaks-at-scale/)
- [Data Quality in Streaming Pipelines: A Practical Framework](https://streamkap.com/resources-and-guides/data-quality-streaming-pipelines)