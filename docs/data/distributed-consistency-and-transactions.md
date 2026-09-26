# 分布式一致性与事务

> 最后更新：2026-09-26 ｜ 领域：数据·分布式、治理与分析 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

分布式一致性与事务研究的是：当数据被复制到多台机器、跨多个区域甚至多个云之后，如何让系统对外表现出一致的读写语义，并在网络分区、节点故障、时钟漂移等条件下保持事务的 ACID 属性。经典理论框架包括 CAP 定理与 PACELC 扩展：CAP 只描述发生分区（P）时在可用性（A）与一致性（C）之间的取舍；PACELC 进一步指出，在没有分区的正常情况下，系统还要在延迟（L）与一致性（C）之间取舍（[Beyond CAP](https://thecodeforge.io/system-design/cap-theorem/)、[Distributed Transactions](https://people.cs.rutgers.edu/~pxk/classes/417/notes/transactions.html)）。按 PACELC 分类，Cassandra、DynamoDB 属于 PA/EL（分区时保可用、平时保低延迟、最终一致），而 Spanner、etcd、CockroachDB 属于 PC/EC（分区时保一致、平时也保一致，代价是延迟）（[Beyond CAP](https://thecodeforge.io/system-design/cap-theorem/)）。

## 最新进展（2025–2026）

**共识协议持续演进。** Raft 仍是工业界主流共识算法，但学术与工程侧出现了大量增强：Rafture 提出带"分发后裁剪"的纠删码 Raft，允许系统在分发完成后调整存储成本，且保证用 F+1 个分片即可重建（[Rafture](https://arxiv.org/html/2603.24761v1)）；TRM-Raft 通过链上信任与声誉模型（B-TRM）非侵入式增强 Raft，使其具备拜占庭容错，并在领导者选举与日志复制中嵌入声誉信号（[TRM-Raft](https://arxiv.org/html/2607.08666v1)）。EPaxos* 则通过重写故障恢复流程，修正了原始 EPaxos 的缺陷，同时保持无故障路径的性能特征（[Making Democracy Work](https://arxiv.org/html/2511.02743v3)）。

**无领导者共识进入生产实验。** Cloudflare 于 2026 年 7 月公开了 Meerkat 的细节：这是一个基于 EPFL 2023 年发表的 QuePaxa 算法的全球一致键值服务实验。与 Raft 不同，QuePaxa 允许所有副本同时接受写入，避免领导者故障或网络退化导致的停滞（[Meerkat](https://blog.sied.ar/2026/07/meerkat-el-nuevo-algoritmo-de-consenso-global-de-cloudflare-para-clave-valor-fuerte.html)）。工业界的另一条路线是继续优化 Raft 选举，例如基于节点优先级的领导者选举以降低高负载下的写延迟（[Improved Raft Protocol](https://dl.acm.org/doi/pdf/10.1145/3701047.3701055)）。

**可下载的全球分布式数据库。** Google 于 2026 年 4 月 23 日发布 Spanner Omni 预览，把 Spanner 从纯云服务扩展到客户自有数据中心、其他云甚至笔记本上运行；其关键点是使用**基于软件的 TrueTime** 在任何环境提供全局事务一致性，并支持关系、键值、图、向量等多模型与跨模型 ACID 事务（[Announcing Spanner Omni](https://cloud.google.com/blog/products/databases/introducing-spanner-omni/?hl=en)、[Spanner Omni overview](https://docs.cloud.google.com/spanner-omni/overview)）。

**分布式 SQL 阵营的版本动态。** CockroachDB v26.2（2026-04-27）通过 `distributed_merge.mode` 为 `IMPORT` 操作提供分布式合并，分两阶段执行——先写本地 SST，再由协调者合并摄取（[What's New in v26.2 — CockroachDB](https://www.cockroachlabs.com/docs/releases/v26.2)）。YugabyteDB v2026.1 STS 系列引入面向多租户的资源治理（Resource Governance for Multitenancy），基于 Linux cgroups 在资源争用时公平分配 CPU，并可为数据库配置 CPU 上限（[What's new in the YugabyteDB v2026.1 STS release series](https://docs.yugabyte.com/stable/releases/ybdb-releases/v2026.1/)）。TiDB 为 MySQL 兼容的分布式 SQL，基于 TiKV 存储、通过 TiFlash 提供 HTAP 分析路径且无需手工分片；三者的取舍集中在兼容生态（Postgres vs MySQL）、多区域一致性与延迟、以及乐观/悲观并发控制策略上（[TiDB vs CockroachDB (2026) Comparison Guide](https://www.pingcap.com/compare/cockroachdb-vs-tidb/)、[TiDB vs YugabyteDB (2026)](https://www.pingcap.com/compare/yugabytedb-vs-tidb/)）。

**云原生数据库的形态演进。** Amazon Aurora DSQL 为无服务器分布式 SQL，宣称最高 99.999% 可用性；Aurora Serverless 亦带来最高 30% 的性能提升并增强扩缩能力（[Amazon Aurora DSQL features](https://aws.amazon.com/rds/aurora/dsql/faqs/)、[Amazon Aurora 资源](https://aws.amazon.com/cn/rds/aurora/resources/)）。Neon 于 2025-05-14 宣布被 Databricks 收购，其无服务器 Postgres 架构成为 Lakebase Postgres 的基础，可运行于 Neon 与 Databricks 两处（Neon 以 copy-on-write 提供数据库分支能力）；Lakebase 被定位为面向 AI 应用与 Agent 的「运营型数据库」新类别，把运营数据引入湖仓并支持持续自动扩缩（[Databricks Agrees to Acquire Neon](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems)、[Neon and Lakebase](https://neon.com/docs/introduction/neon-and-lakebase)、[Databricks Launches Lakebase](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps)）。PlanetScale 主打高并发 MySQL 兼容，其公开基准声称相对 Neon Lakebase 最高快 1.4 倍、相对 Supabase 最高快 3.4 倍（[PlanetScale Benchmarks](https://planetscale.com/benchmarks)）。

## 核心技术与关键概念

**一致性模型与隔离级别。** 从线性一致性（linearizability）到可串行化（serializability），再到 Spanner 提供的外部一致性（external consistency，即严格可串行化）：若事务 T1 在真实时间上先于 T2 提交，则 T1 的提交时间戳必须小于 T2 的开始时间；在未指定隔离级别时，Spanner 默认提供这一最强保证（[True Time and external consistency](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency)）。Spanner 的实现基础是 TrueTime——一个返回带边界时间区间 `[earliest, latest]` 的 API，真实时间保证落在区间内（[Distributed Databases](https://people.cs.rutgers.edu/~pxk/classes/417/notes/distributed-databases.html)），从而让不同机器能对事务顺序达成一致（[Life of Spanner Reads & Writes](https://docs.cloud.google.com/spanner/docs/whitepapers/life-of-reads-and-writes)）。

**时钟问题。** 分布式系统无法依赖物理时钟的精确同步。Lamport 逻辑时钟通过单调计数器维护 happens-before 关系；向量时钟可捕捉并发；混合逻辑时钟（HLC）在物理时钟基础上加入逻辑分量，是在工程中被广泛采用的折中（[Clock Synchronization](https://cosmiclearn.com/dbint/clock-synchronization.php)）。

**分布式事务与 2PC。** 当事务跨越多个分片（例如多个 Paxos Group / Tablet）时，通常由两阶段提交（2PC）协调：一个 Paxos Group 的 Leader 担任 Coordinator，其余为 Participant；Prepare 阶段在 Lock Table 上写入并达成组内一致，Commit 阶段完成提交，由此把 2PC 与共识协议结合（[数据库内核月报](http://mysql.taobao.org/monthly/2026/02/01/)）。Spanner 的跨区域事务则需要 2PC 配合 TrueTime 时间戳（[CockroachDB vs Google Spanner](https://www.cockroachlabs.com/compare/cockroachdb-vs-google-spanner/)）。

**服务化层面的工程改进。** Spanner 客户端在 2025 年 8 月的更新中加入了对读写事务的多路复用会话（multiplexed session）支持，并支持设置读锁模式（read lock mode）（[Spanner release notes](https://docs.cloud.google.com/spanner/docs/release-notes?authuser=8)）。这类改动表明强一致数据库正把"降低连接与锁开销"作为提升可用性的工程重点，而不仅是在算法层做取舍。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Google Spanner / Spanner Omni**：全球分布式、强一致、多模型数据库；Spanner Omni 支持容器化部署在自有 Kubernetes 基础设施上（[Spanner Omni overview](https://docs.cloud.google.com/spanner-omni/overview)）。
- **CockroachDB**：通过 Raft 在各表、Range、区域间实现可串行化隔离，从架构上即支持完全分布式的多行多表 ACID 事务；官方对比文档指出 Spanner 走 2PC + TrueTime，而 CockroachDB 直接用分布式共识（[CockroachDB vs Google Spanner](https://www.cockroachlabs.com/compare/cockroachdb-vs-google-spanner/)）。
- **YugabyteDB**：v2026.1 STS 系列在 xCluster 复制、DDL 队列错误处理等方面继续迭代（[YugabyteDB v2026.1](https://docs.yugabyte.com/stable/releases/ybdb-releases/v2026.1/)）。
- **TiDB**：8.5.0 起将加速建表（表创建加速）转为 GA，并让 PD follower 也能处理 Region 请求以降低 PD Leader 的 CPU 压力（[TiDB 8.5.0 Release Notes](https://docs.pingcap.com/tidb/dev/release-8.5.0/)）。
- **学术原型 K2**：基于 TrueTime 时钟优化多区域数据存储的分布式事务，支持严格可串行化的通用事务（[K2](https://arxiv.org/html/2504.01460)）。

## 关键数据与评测结果（附来源）

- CockroachDB 官方对比指出其可串行化事务在表、Range、区域层面通过 Raft 达成一致，而 Spanner 的跨区域事务需要 2PC 与 TrueTime 时间戳配合（[CockroachDB vs Google Spanner](https://www.cockroachlabs.com/compare/cockroachdb-vs-google-spanner/)）。
- K2 论文明确其提供严格可串行化（strict serializability），即隔离层面可串行化、实时序层面线性一致（[K2](https://arxiv.org/html/2504.01460)）。
- 基于节点优先级选举的改进 Raft，在仿真中降低了高负载与不稳定网络下的平均写延迟（[Improved Raft Protocol](https://dl.acm.org/doi/pdf/10.1145/3701047.3701055)）。

## 趋势与争议

其一，**共识协议正从"领导者中心"向"无领导者/并行接受写"扩展**，QuePaxa/Meerkat 类方案与 EPaxos 修复版表明该方向已从理论走向工程验证，但在生产环境中对故障恢复复杂性的容忍度仍是争议点（[Meerkat](https://blog.sied.ar/2026/07/meerkat-el-nuevo-algoritmo-de-consenso-global-de-cloudflare-para-clave-valor-fuerte.html)、[Making Democracy Work](https://arxiv.org/html/2511.02743v3)）。其二，**强一致的落地成本结构正在改变**：Spanner Omni 用软件 TrueTime 替代专用原子钟/GPS 硬件，把"跨区域强一致"从云专属能力推向本地部署，但软件时钟的误差边界能否在多云异构网络下维持同等保证，尚无统一口径。其三，**CAP 的表述本身持续被修正**：多篇 2026 年的技术文章强调 CAP 只覆盖分区这一少数场景，把 PACELC 作为更完整的选型框架（[Beyond CAP](https://readllm.com/docs/tech/latest/beyond-cap-how-spanner-and-cockroachdb-are-redefining-distributed-databases-in-2026/)、[Beyond CAP: PACELC](https://uplatz.com/blog/eventual-consistency-or-probabilistic-reconciliation-deconstructing-the-core-trade-offs-of-decentralized-ledgers/)）。其四，**2PC 是否"过时"仍存在分歧**：一部分观点认为 2PC 在单机/同区仍是最优解，另一部分认为其阻塞特性在跨区域场景必须与共识协议深度结合（[数据库内核月报](http://mysql.taobao.org/monthly/2026/02/01/)）。

## 参考来源

1. [Beyond CAP — Why Cassandra Returned Stale Data at 3 AM](https://thecodeforge.io/system-design/cap-theorem/)
2. [Distributed Transactions — Rutgers CS417](https://people.cs.rutgers.edu/~pxk/classes/417/notes/transactions.html)
3. [Rafture: Erasure-coded Raft with Post-Dissemination Pruning](https://arxiv.org/html/2603.24761v1)
4. [TRM-Raft: A Byzantine-Resistant Raft Consensus via Integrated Trust and Reputation Model](https://arxiv.org/html/2607.08666v1)
5. [Making Democracy Work: Fixing and Simplifying Egalitarian Paxos](https://arxiv.org/html/2511.02743v3)
6. [Meerkat: el nuevo algoritmo de consenso global de Cloudflare](https://blog.sied.ar/2026/07/meerkat-el-nuevo-algoritmo-de-consenso-global-de-cloudflare-para-clave-valor-fuerte.html)
7. [The Study of a Distributed Networking Method Based on an Improved Raft Protocol](https://dl.acm.org/doi/pdf/10.1145/3701047.3701055)
8. [CockroachDB vs Google Spanner](https://www.cockroachlabs.com/compare/cockroachdb-vs-google-spanner/)
9. [Beyond CAP: How Spanner and CockroachDB Are Redefining Distributed Databases in 2026](https://readllm.com/docs/tech/latest/beyond-cap-how-spanner-and-cockroachdb-are-redefining-distributed-databases-in-2026/)
10. [Spanner: True Time and external consistency](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency)
11. [Life of Spanner Reads & Writes](https://docs.cloud.google.com/spanner/docs/whitepapers/life-of-reads-and-writes)
12. [Distributed Databases — Rutgers CS417](https://people.cs.rutgers.edu/~pxk/classes/417/notes/distributed-databases.html)
13. [Clock Synchronization: TrueTime, Vector Clocks, & Hybrid Logical Clocks](https://cosmiclearn.com/dbint/clock-synchronization.php)
14. [K2: On Optimizing Distributed Transactions in a Multi-region Data Store with TrueTime Clocks](https://arxiv.org/html/2504.01460)
15. [Announcing Spanner Omni](https://cloud.google.com/blog/products/databases/introducing-spanner-omni/?hl=en)
16. [Spanner Omni overview](https://docs.cloud.google.com/spanner-omni/overview)
17. [数据库内核月报（2PC 与 Paxos Group）](http://mysql.taobao.org/monthly/2026/02/01/)
18. [What's new in the YugabyteDB v2026.1 STS release series](https://docs.yugabyte.com/stable/releases/ybdb-releases/v2026.1/)
19. [TiDB 8.5.0 Release Notes](https://docs.pingcap.com/tidb/dev/release-8.5.0/)
20. [Spanner release notes](https://docs.cloud.google.com/spanner/docs/release-notes?authuser=8)
21. [Eventual Consistency or Probabilistic Reconciliation? PACELC](https://uplatz.com/blog/eventual-consistency-or-probabilistic-reconciliation-deconstructing-the-core-trade-offs-of-decentralized-ledgers/)
22. [What's New in v26.2 — CockroachDB](https://www.cockroachlabs.com/docs/releases/v26.2)
23. [TiDB vs CockroachDB (2026) Comparison Guide for Platform Teams](https://www.pingcap.com/compare/cockroachdb-vs-tidb/)
24. [TiDB vs YugabyteDB (2026) Comparison Guide for Platform Teams](https://www.pingcap.com/compare/yugabytedb-vs-tidb/)
25. [Serverless distributed SQL database with active-active high availability – Amazon Aurora DSQL](https://aws.amazon.com/rds/aurora/dsql/faqs/)
26. [Amazon Aurora 资源](https://aws.amazon.com/cn/rds/aurora/resources/)
27. [Databricks Agrees to Acquire Neon](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems)
28. [Neon and Lakebase](https://neon.com/docs/introduction/neon-and-lakebase)
29. [Databricks Launches Lakebase, a New Class of Operational Database for AI Apps](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps)
30. [PlanetScale Benchmarks](https://planetscale.com/benchmarks)