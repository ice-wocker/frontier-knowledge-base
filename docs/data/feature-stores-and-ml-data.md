# 特征平台与 ML 数据

> 最后更新：2026-09-26 ｜ 领域：数据·分布式、治理与分析 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

特征平台（Feature Platform）与特征存储（Feature Store）是机器学习工程中连接数据工程与模型训练/推理的中间层。其核心目标是：让特征可定义、可发现、可复用、可治理，并保证离线训练与在线推理使用同一套特征计算逻辑，从而避免训练-服务偏差（training-serving skew）。与之配套的还有 ML 数据工程实践，包括训练数据版本控制、数据血缘与可复现性。

## 最新进展（2025–2026）

**实时特征延迟进入亚秒级。** Databricks 展示了其 Feature Store 的实时新鲜度能力：来自 Kafka 的流式聚合现在能以 200ms p99 延迟到达在线特征存储，把特征滞后从分钟/小时级压缩到毫秒级。其关键是 Spark 实时模式（Spark Real-Time Mode, RTM），它连续处理行而不是等待微批，按事件更新滚动窗口聚合，并对检查点做摊销以降低有状态流处理的延迟；Lakebase 则提供高吞吐的在线服务能力（[How Databricks Feature Store serves features with sub-second freshness](https://www.databricks.com/blog/how-databricks-feature-store-serves-features-sub-second-freshness)）。

**开源与托管两条路线分化清晰。** Feast 定位为开源的、面向生产 AI 的特征存储，为训练与推理提供高规模结构化数据；从 Feast v0.65 起，其与 ScyllaDB 的集成更紧密，带来向量检索支持与更好的表现（[FEAST](https://feast.dev/)）。Tecton 则定位为全托管的特征平台，用于编排从转换到在线服务的完整特征生命周期，并承诺企业级 SLA（[Feature Platform | Tecton](https://www.tecton.ai/product/)）。第三方对比把两者的差异总结为"自管理的特征存储"与"托管的特征平台"：后者额外自动化批、流、实时的特征管道（[Choosing the Right Feature Store: Feast or Tecton?](https://resources.tecton.ai/hubfs/Choosing-Feature-Solution-Feast-or-Tecton.pdf)）。

**平台横向对比口径趋于统一。** 2026 年的对比表把主流平台并列：Feast v0.64.0（开源、与编排器无关，计算引擎支持本地 Python、Spark、dbt）、Tecton v0.9.3（托管企业 SaaS，Spark 与原生 Python 的 Rift Engine）、Hopsworks v4.1（一体化 AI Lakehouse 平台，使用 Spark、Flink、RonDB 计算）（[Evolving MLOps: Automated Model Retraining Pipelines with Feature Stores](https://www.shyankdev.com/blogs/evolving-mlops-retraining-pipelines-feature-stores)）。

**数据版本控制与合规管道。** 在 ML 数据侧，DVC（Data Version Control）与 lakeFS 成为两条主流路线。DVC 用 Git 式模型管理数据：实际数据存放于对象存储，Git 只跟踪指针，`dvc add` 计算内容哈希并写出仅含哈希与存储位置的 `.dvc` 文件（[Training Data Versioning](https://datavidhya.com/learn/ai-for-data-engineering/feature-stores-ml-infra/training-data-pipelines-versioning/)）。lakeFS 则在对象存储之上构建类 Git 仓库，提供 `branch`/`commit`/`merge`/`revert`（[Building Compliant and Reproducible ML Pipelines](https://lakefs.io/blog/building-compliant-ml-pipelines/)）；典型流程是先在独立分支上验证新语料，通过后再 merge 到 main，从而让生产环境在验证期间继续从旧分支服务（[Data versioning para LLMOps: DVC, lakeFS](https://blog.lo0.es/posts/data-versioning-dvc-lakefs/)）。

## 核心技术与关键概念

**离线存储与在线存储。** 特征存储通常由两个基础组件构成：离线存储（offline store）针对大规模、低成本的训练数据检索优化；在线存储（online store）针对在线服务的低延迟检索优化（[Feast Introduction](https://docs.feast.dev/v0.59-branch)）。Tecton 的表述是：在离线与在线环境之间存储一致的基线特征值，以防止训练-服务偏差（[Feature Platform | Tecton](https://www.tecton.ai/product/)）。

**逻辑与物理分离。** 平台的核心抽象是"以代码定义特征、以文件形式在 Git 仓库中管理"（Tecton），使特征定义可评审、可版本化（[Feature Platform | Tecton](https://www.tecton.ai/product/)）。在 Databricks 路线上，Feature Store 与 Unity Catalog、Delta Lake 紧耦合，提供自动血缘追踪与特征发现，并经 MLflow 记录实验（[How to Build Feature Stores for Production ML Systems 2026](https://iterathon.tech/blog/feature-store-implementation-production-ml-2026)）。

**训练-服务一致性与数据版本。** 保证一致性需要同一份特征转换逻辑同时用于训练与推理，并对训练数据集做版本固定。DVC 可用于实验跟踪（模型指标、参数、版本）、构建与运行 ML 管道、实现可复现性、数据与模型注册，以及通过 CML 做 CI/CD（[27 MLOps Tools for 2026](https://lakefs.io/blog/mlops-tools/)）。DVC 官方也强调与 Amazon SageMaker AI、MLflow 结合时的端到端血缘能力（[Data Version Control](https://dvc.org/)）。

**特征平台的三层职责。** 从工程视角看，特征平台通常承担三层职责：一是特征定义与版本化（以代码/文件形式纳入 Git 管理）（[Feature Platform | Tecton](https://www.tecton.ai/product/)）；二是离线与在线一致的物化（离线优化大规模低成本检索，在线优化低延迟检索）（[Feast Introduction](https://docs.feast.dev/v0.59-branch)）；三是治理与血缘（在 Databricks 路线中由 Unity Catalog 承载，自动追踪模型与特征版本的绑定关系）（[Top 10 Feature Store Platforms](https://www.scmgalaxy.com/tutorials/top-10-feature-store-platforms-features-pros-cons-comparison/)）。

**模型-特征血缘。** 在 Lakehouse 路线上，系统会自动追踪哪些模型绑定到哪些特征版本，并借由 Delta Lake 的 ACID 与时间旅行能力支持回溯（[Top 10 Feature Store Platforms](https://www.scmgalaxy.com/tutorials/top-10-feature-store-platforms-features-pros-cons-comparison/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Feast**：开源特征存储，293 位贡献者、1200 万+ 下载、5.5K Slack 成员（官方站点数据）；v0.65 起强化与 ScyllaDB 的集成以支持向量检索（[FEAST](https://feast.dev/)）。
- **Tecton**：全托管特征平台，覆盖转换、在线服务与 SLA（[Feature Platform | Tecton](https://www.tecton.ai/product/)）。
- **Databricks Feature Store**：与 Unity Catalog、Delta Lake、MLflow 深度集成，支持亚秒级特征新鲜度（[How Databricks Feature Store serves features with sub-second freshness](https://www.databricks.com/blog/how-databricks-feature-store-serves-features-sub-second-freshness)）。
- **Hopsworks**：面向协作 ML、治理与端到端工作流的特征平台，支持离线与在线特征使用（[Top 10 Feature Store Platforms](https://www.theaiops.com/top-10-feature-store-platforms-features-pros-cons-comparison/)）。
- **DVC / lakeFS**：数据版本控制工具，分别代表 Git 扩展式与对象存储之上的类 Git 仓库两种范式（[Data Version Control](https://dvc.org/)、[Building Compliant and Reproducible ML Pipelines](https://lakefs.io/blog/building-compliant-ml-pipelines/)）。

## 关键数据与评测结果（附来源）

- Databricks：Kafka 流式聚合到在线特征存储的 p99 延迟为 200ms（[Databricks Feature Store](https://www.databricks.com/blog/how-databricks-feature-store-serves-features-sub-second-freshness)）。
- Feast 官方站点数据：293 位贡献者、12M+ 下载、5.5K Slack 成员（[FEAST](https://feast.dev/)）。
- 2026 年对比表版本号：Feast v0.64.0、Tecton v0.9.3、Hopsworks v4.1（[Evolving MLOps](https://www.shyankdev.com/blogs/evolving-mlops-retraining-pipelines-feature-stores)）。
- 一项 2026 年的实施经验判断：特征存储对少于 10 个模型的团队属于过度设计，但在复杂流式用例中值得投入（[How to Build Feature Stores for Production ML Systems 2026](https://iterathon.tech/blog/feature-store-implementation-production-ml-2026)）。
- Databricks 成本以 DBU 消耗计，约 $0.07/DBU（同上来源）。

## 趋势与争议

其一，**"小团队是否需要特征存储"长期存在分歧**：一种观点认为在模型数量少时引入特征存储是过度工程；另一种观点认为只要有实时特征或跨团队复用需求，特征存储就是必需的基础设施（[How to Build Feature Stores for Production ML Systems 2026](https://iterathon.tech/blog/feature-store-implementation-production-ml-2026)）。其二，**开源与托管的取舍**：开源方案（Feast）避免厂商绑定但需要自建在线存储与管道运维；托管方案（Tecton）降低运维成本但引入平台依赖，且各家的能力边界（实时、向量、治理）差异明显（[Choosing the Right Feature Store](https://resources.tecton.ai/hubfs/Choosing-Feature-Solution-Feast-or-Tecton.pdf)）。其三，**LLM 时代特征存储的定位变化**：Feast 开始支持向量检索、Databricks 强调统一治理，说明特征平台正在向"AI/LLM 的结构化与向量数据服务层"扩展，但其与向量数据库的边界仍不清晰（[FEAST](https://feast.dev/)）。其四，**数据版本控制的工具碎片化**：DVC、lakeFS 与各云厂商原生版本能力并存，缺乏统一标准，跨工具的可复现性验证仍是难点（[27 MLOps Tools for 2026](https://lakefs.io/blog/mlops-tools/)）。

## 参考来源

1. [How Databricks Feature Store serves features with sub-second freshness](https://www.databricks.com/blog/how-databricks-feature-store-serves-features-with-sub-second-freshness)
2. [FEAST — open source feature store](https://feast.dev/)
3. [Feature Platform | Tecton](https://www.tecton.ai/product/)
4. [Choosing the Right Feature Store: Feast or Tecton?](https://resources.tecton.ai/hubfs/Choosing-Feature-Solution-Feast-or-Tecton.pdf)
5. [Evolving MLOps: Automated Model Retraining Pipelines with Feature Stores](https://www.shyankdev.com/blogs/evolving-mlops-retraining-pipelines-feature-stores)
6. [Feast Introduction — docs.feast.dev](https://docs.feast.dev/v0.59-branch)
7. [Training Data Versioning — DataVidhya](https://datavidhya.com/learn/ai-for-data-engineering/feature-stores-ml-infra/training-data-pipelines-versioning/)
8. [Building Compliant and Reproducible ML Pipelines — lakeFS](https://lakefs.io/blog/building-compliant-ml-pipelines/)
9. [Data versioning para LLMOps: DVC, lakeFS](https://blog.lo0.es/posts/data-versioning-dvc-lakefs/)
10. [27 MLOps Tools for 2026: Key Features & Benefits](https://lakefs.io/blog/mlops-tools/)
11. [Home – DVC (Data Version Control)](https://dvc.org/)
12. [How to Build Feature Stores for Production ML Systems 2026](https://iterathon.tech/blog/feature-store-implementation-production-ml-2026)
13. [Top 10 Feature Store Platforms: Features, Pros, Cons & Comparison](https://www.theaiops.com/top-10-feature-store-platforms-features-pros-cons-comparison/)
14. [Top 10 Feature Store Platforms — scmgalaxy](https://www.scmgalaxy.com/tutorials/top-10-feature-store-platforms-features-pros-cons-comparison/)