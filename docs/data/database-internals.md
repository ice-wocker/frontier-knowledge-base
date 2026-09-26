# 数据库内核

> 最后更新：2026-09-26 ｜ 领域：数据·工程与架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

数据库内核研究数据在磁盘与内存中如何组织、事务如何保证正确性、查询如何被优化与执行。核心组件包括存储引擎（B+ 树或 LSM-Tree）、事务与并发控制（MVCC、WAL）、以及查询处理层（解析、优化器、执行引擎）。不同引擎的取舍可以概括为「读优化 vs 写优化」以及「行存 vs 列存」两对基本张力，现代系统往往在此基础上叠加向量化执行、可组合的查询引擎与异步 I/O 等优化。

理解数据库内核有助于做出正确的工程决策：为什么事务型数据库在写入激增时会因 compaction 抖动而出现延迟毛刺？为什么分析查询有时会因优化器选错 join 顺序而慢上数十倍？为什么长期运行的事务会阻止 MVCC 的旧版本回收、导致表膨胀？这些问题的答案都指向内核机制。掌握存储引擎、事务与优化器三条主线，可以在容量规划、索引设计与故障排查时避免「凭经验调参」，转而依据机制定位根因。

## 最新进展（2025–2026）

**PostgreSQL 18：异步 I/O 与读性能跃升。** PostgreSQL 18 引入异步 I/O（AIO）子系统，可提升顺序扫描、位图堆扫描、vacuum 等操作的性能；官方称新 I/O 子系统在读存储时带来最高约 3 倍的性能提升（[PostgreSQL 18 Press Kit](https://www.postgresql.org/about/press/presskit18/)、[Release Notes](https://www.postgresql.org/docs/release/18.0/)）。该 AIO 子系统在 Linux 上可使用 `io_uring`，其它平台提供基于 worker 的实现，`io_method` 可选 `worker`、`io_uring`、`sync`（[Resource Consumption — PostgreSQL](https://www.postgresql.org/docs/current/runtime-config-resource.html)）。该版本还新增「skip scan」查找支持，并加入 uuidv7() 函数——为 UUID 提供更好的索引与读取性能，以及查询时计算的虚拟生成列（virtual generated columns）（[Release Notes](https://www.postgresql.org/docs/release/18.0/)、[Press Kit](https://www.postgresql.org/about/press/presskit18/)）。

**查询引擎走向可组合。** 过去「一个数据库一个单体查询引擎」的设计正在被拆解：Apache DataFusion 提供 Rust 编写的可嵌入、模块化执行引擎；Meta 的 Velox 提供可插入 Presto、Spark 等系统的高性能 C++ 执行内核；Substrait 提供跨语言计划表示格式，使查询计划可在不同引擎间流转而无需重新编译或解析；Apache Arrow 提供内存列式格式以消除组件间序列化开销（[Building Composable Query Engines with Rust Runtimes](https://tuts.alexmercedcoder.dev/2026/2026-05-24-composable-query-engines/)）。

**优化器的现代化。** Apache Doris 的查询优化器 Nereids 是基于 Cascades 框架构建的现代优化器，结合 RBO（基于规则）与 CBO（基于代价）为复杂查询生成高效执行计划（[Query Optimizer Introduction](https://doris.incubator.apache.org/docs/4.x/query-acceleration/optimization-technology-principle/query-optimizer/)）。Apache Calcite 则是 Java 查询规划框架，链路为 SQL parser → AST → logical plan → physical plan，本身不是执行引擎，而是产出 RelNode 树交由后端执行，被 Flink、Hive、Druid、Kylin、Phoenix 等广泛使用（[Calcite Internals](https://nmbr7.github.io/notes/database/calcite-internals/)）。

## 核心技术与关键概念

**B+ 树与 LSM-Tree。** B+ 树中数据始终有序、查找为 O(log n)，读取快；写入原地更新树，小写入快，但每次写入可能需要对目标页所在磁盘位置做随机 I/O。LSM-Tree 从不原地更新数据，先在内存缓冲所有写入，再按序批量顺序刷盘，写入始终是顺序的（快），代价是读取需跨多层搜索（[B-Tree vs LSM-Tree: Why InnoDB and RocksDB Make Different Trade-offs](https://ndlab.blog/posts/btree-vs-lsm-tree-innodb-rocksdb-2026)）。LSM-Tree 由 O'Neil 等人于 1996 年提出，是写密集型世界（时序库、事件存储、分布式 KV、分析摄入管道）的存储引擎，其核心洞见是磁盘顺序写远快于随机写（在 HDD 上常达约 100 倍）（[LSM Trees, MVCC, and Vectorized Execution](https://www.accelar.io/blog/lsm-tree-mvcc-database-internals)）。

**WAL 与写路径。** 写路径为：先追加写预写日志（WAL）以保证持久性（顺序追加，是最快的磁盘操作）；再插入内存有序结构（红黑树或跳表）；当 memtable 达到阈值（通常 64MB–256MB）时，刷盘为不可变的有序文件 SSTable（[B+- Trees, LSM Trees, WAL, and MVCC](https://codemia.io/courses/system_design_fundamentals/database_indexing_and_storage_mechanisms)）。

**MVCC。** 多数生产数据库在存储引擎之上叠加 MVCC，以在无锁情况下支持并发读写。MVCC 下更新不覆盖旧行，而是写入带更高事务 ID 的新版本；读者看到的是其事务开始前已提交的版本，旧版本最终由垃圾回收进程回收（PostgreSQL 为 VACUUM，RocksDB 为 compaction tombstone）（[Storage Engines](https://alivedise.github.io/backend-engineering-essentials/data-storage/storage-engines)）。

**优化器：规则与代价。** Calcite 的优化器是框架的核心，通过反复对关系表达式应用 planner 规则来优化查询，代价模型引导过程，规划引擎尝试生成语义等价但代价更低的替代表达式；优化器每个组件都可扩展——用户可添加关系算子、规则、代价模型与统计信息（[Apache Calcite: A Foundational Framework](https://arxiv.org/pdf/1802.10233.pdf)）。优化器通常先用 RBO 做确定性改写（谓词下推、列裁剪、常量折叠），再用 CBO 基于统计信息与代价模型选择 join 顺序、连接算法与并行度。统计信息（直方图、基数估计）的准确性直接决定计划质量，而基数估计误差是多表查询计划退化的首要来源。

**执行引擎：向量化与编译执行。** 执行层有两条主流路线：向量化执行（以批为单位处理，减少函数调用与分支开销，DuckDB 的 Vector Volcano 即属此类）与编译执行（把查询即时编译为机器码，如 HyPer 风格）。二者都在追求 CPU 缓存友好与 SIMD 利用。DuckDB 的循环以 2048 大小的向量为单位，是其引擎的核心（[Design and Implementation of DuckDB Internals](https://blobs.duckdb.org/slides/DiDi-07.pdf)）。此外，异步 I/O 正成为新一代内核降低读延迟的通用手段：PostgreSQL 18 的 AIO 子系统即通过并发发起 I/O 请求来掩盖存储延迟，官方称在读存储场景带来最高约 3 倍提升（[PostgreSQL 18 Press Kit](https://www.postgresql.org/about/press/presskit18/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **PostgreSQL**（https://www.postgresql.org/）— MVCC、B+ 树堆表，18 版引入 AIO。
- **RocksDB**（https://rocksdb.org/）— LSM-Tree 存储引擎，广泛用于 MySQL/Kafka Streams。
- **InnoDB**（https://dev.mysql.com/doc/refman/8.4/en/innodb-storage-engine.html）— B+ 树、MVCC。
- **Apache Calcite**（https://calcite.apache.org/）— 可扩展查询规划框架。
- **Apache DataFusion**（https://datafusion.apache.org/）— Rust 可嵌入执行引擎。
- **Velox**（https://facebookincubator.github.io/velox/）— Meta 的 C++ 执行内核。
- **Substrait / Apache Arrow**（https://substrait.io/、https://arrow.apache.org/）— 跨引擎计划与内存列式格式。

## 关键数据与评测结果（附来源）

- PostgreSQL 18 的新 I/O 子系统在读存储时性能提升最高约 3 倍（[PostgreSQL 18 Press Kit](https://www.postgresql.org/about/press/presskit18/)）。
- LSM-Tree 提出于 1996 年；HDD 上顺序写可比随机写快约 100 倍（[LSM Trees, MVCC, and Vectorized Execution](https://www.accelar.io/blog/lsm-tree-mvcc-database-internals)）。
- memtable 刷盘阈值通常为 64MB–256MB（[B+- Trees, LSM Trees, WAL, and MVCC](https://codemia.io/courses/system_design_fundamentals/database_indexing_and_storage_mechanisms)）。
- Nereids 基于 Cascades 框架，结合 RBO 与 CBO（[Doris Query Optimizer](https://doris.incubator.apache.org/docs/4.x/query-acceleration/optimization-technology-principle/query-optimizer/)）。

## 趋势与争议

**B+ 树 vs LSM-Tree 的持续取舍。** 二者并非优劣关系，而是读优化与写优化的分工：InnoDB 选择 B+ 树以服务读密集的事务型 workload，RocksDB 选择 LSM-Tree 以服务写密集与顺序写入场景；写放大的管理与 compaction 策略是 LSM-Tree 的主要工程难点。

**单体引擎 vs 可组合引擎。** 可组合路线（DataFusion/Velox/Substrait/Arrow）把优化、执行、内存格式解耦，降低复用成本，但也带来跨组件协调与性能开销；传统一体化引擎（如 Calcite + 自研执行）在调优深度上仍有优势，二者在 2026 年并存竞争。

**存储引擎选型的误区。** 将 LSM-Tree 与 B+ 树的基准直接跨 workload 比较（如点查 vs 范围扫描 vs 高写吞吐）常得出误导性结论；选型应基于读/写比例、延迟 SLA 与数据规模，而非单一引擎的绝对排名。

## 参考来源

- [LSM Trees, MVCC, and Vectorized Execution: The Internals That Determine Your Database Performance](https://www.accelar.io/blog/lsm-tree-mvcc-database-internals)
- [B+- Trees, LSM Trees, WAL, and MVCC](https://codemia.io/courses/system_design_fundamentals/database_indexing_and_storage_mechanisms)
- [Storage Engines [BEE-6005]](https://alivedise.github.io/backend-engineering-essentials/data-storage/storage-engines)
- [B-Tree vs LSM-Tree: Why InnoDB and RocksDB Make Different Trade-offs](https://ndlab.blog/posts/btree-vs-lsm-tree-innodb-rocksdb-2026)
- [Building Composable Query Engines with Rust Runtimes](https://tuts.alexmercedcoder.dev/2026/2026-05-24-composable-query-engines/)
- [Apache Calcite News](https://calcite.apache.org/news/)
- [Calcite Internals](https://nmbr7.github.io/notes/database/calcite-internals/)
- [Apache Doris Query Optimizer Introduction](https://doris.incubator.apache.org/docs/4.x/query-acceleration/optimization-technology-principle/query-optimizer/)
- [Apache Calcite: A Foundational Framework for Optimized Query Processing Over Heterogeneous Data Sources](https://arxiv.org/pdf/1802.10233.pdf)
- [PostgreSQL 18 Release Notes](https://www.postgresql.org/docs/release/18.0/)
- [PostgreSQL 18 Press Kit](https://www.postgresql.org/about/press/presskit18/)
- [Resource Consumption — PostgreSQL 18 Documentation](https://www.postgresql.org/docs/current/runtime-config-resource.html)