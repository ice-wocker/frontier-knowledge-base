# 缓存与存储策略（Caching and Storage Strategies）

> 最后更新：2026-09-26 ｜ 领域：软件工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

缓存的本质是在更快的介质上保存数据的副本，以降低延迟、减少对下游（数据库、源站）的压力。它同时引入三个必须面对的问题：一致性（副本何时过期）、容量（保存什么、淘汰什么）与可靠性（缓存故障时系统如何降级）。

在架构层面，缓存通常按层级组织：进程内缓存（L1，节点本地、微秒级、无网络开销）、分布式缓存（L2，集群共享、毫秒级）、数据库/源站作为唯一事实来源（[Application-Level Caching](https://adamdjellouli.com/articles/backend_engineers_guide/05_caching/07_application_level_caching)）。本地缓存的劣势是受实例内存限制、且各实例各持一份副本，若管理不当会导致数据不一致（[Mastering Advanced Caching: Redis, Caffeine, and Multi-Layer Architectures](https://codewithyoha.com/blogs/mastering-advanced-caching-redis-caffeine-and-multi-layer-architectures)）。

## 最新进展（2025–2026）

**1. Redis 8 正式发布，引入面向 AI 的数据类型。** Redis 8 GA 版本带来了 30 多项性能改进以及新的「vector set」（向量集合）数据类型（beta），用于高维向量相似度检索，适用于语义搜索与推荐等 AI 场景；该类型由 Redis 原作者 Salvatore Sanfilippo 开发，设计上受有序集合（sorted set）启发（[Redis 8 is now GA](https://redis.io:8443/blog/redis-8-ga/)）。官方文档说明 vector set 目前处于 beta，API 与行为可能在未来版本中变化（[Redis 8.0](https://redis.io/docs/latest/develop/whats-new/8-0/)）。Redis 8 还整合了此前分层的能力，包括支持水平与垂直扩展的 Redis Search、可查询 JSON 文档类型、时序、五种概率型数据结构（Bloom、Cuckoo、Count-min sketch、Top-k、t-digest）（[Redis Open Source 8.0 release notes](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.0-release-notes/)）。

**2. Valkey 持续迭代并强调效率与一致性。** Linux Foundation 于 2026 年 5 月 19 日宣布 Valkey 9.1 正式可用（GA），该版本聚焦更高的效率与模块化，以在生产环境中提供更高可靠性与一致性，并包含来自 80 多位贡献者在安全、可观测性、性能、效率与工具方面的改进（[Valkey Enhances Efficiency, Security, and Modular Performance with 9.1 Release](https://www.linuxfoundation.org/press/valkey-enhances-efficiency-security-and-modular-performance-with-9.1-release-and-new-ecosystem-integrations)）。Valkey 9.0 引入了原子 slot 迁移、Hash 字段级过期与集群模式下的多数据库支持，并宣称单集群可达每秒 10 亿次操作；8.1 则带来额外 27% 的内存节省（小键值对约 16 字节时可节省最多 41%）（[Valkey Meets Laravel: Bridging Open Source Communities at Laracon India 2026](https://valkey.io/blog/valkey-at-laracon-india-2026/)）。官方版本页显示 8.x 系列的最新版本为 8.1.10（发布日期 2026-09-01）（[Valkey](https://valkey.io/)）。

**3. CDN 边缘缓存向分层缓存与更大容量演进。** Cloudflare 的 Cache Reserve 通过长期保存长尾内容来提高缓存命中率并降低回源与出口（egress）成本（[Cloudflare Cache Reserve](https://www.cloudflare.com/products/cache-reserve/)）。其分层缓存（Tiered Caching）机制在本地 PoP 未命中时向上层缓存拓扑查询，Smart Tiered Caching 与 Regional Tiered Cache 通过集中连接提高命中率、降低全局回源负载；Enterprise 客户还可自定义分层拓扑（[Designing a distributed web performance architecture](https://developers.cloudflare.com/reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/)）。

**4. 多层缓存（Caffeine + Redis）成为主流实践。** Spring Boot 等技术栈的多级缓存方案以 Caffeine 作为进程内 L1（亚微秒读取、无网络）、Redis 作为 L2 回退与一致性层，从而在热数据上获得亚毫秒级读取（[Spring Boot Caching: Multi-Level Cache with Caffeine + Redis](https://blog.devops-monk.com/2026/05/spring-boot-caching-caffeine-redis/)）。

## 核心技术与关键概念

- **缓存穿透 / 击穿 / 雪崩**：缓存击穿（stampede，又称 thundering herd）指热点 key 过期瞬间，大量并发请求同时未命中并涌向数据库重新生成（[Redis 缓存层架构指南](https://redis.io:8443/blog/cache-layer-architecture-guide.md)）。
- **击穿的三种防御**：请求合并（request coalescing，仅第一个未命中请求去取数据，其余等待其结果）、TTL 抖动（jitter）、分布式锁/互斥（仅一个请求回源，其余等待或读旧值）（[Redis 缓存层架构指南](https://redis.io:8443/blog/cache-layer-architecture-guide.md)、[Caching Strategies 2026: Redis, Valkey, CDN, and Application Caching](https://calmops.com/devops/caching-strategies-redis-cdn-application-cache/)）。
- **原子加载（atomic loading）**：Caffeine 的 `LoadingCache.get()` 保证未命中时只有一个线程执行 loader、其余等待，从机制上消除击穿；`refreshAfterWrite` 与 `expireAfterWrite` 语义不同，前者在返回旧值的同时异步刷新（[Caching KMS data keys in multi-thread environments](https://aws.amazon.com/blogs/security/caching-kms-data-keys-in-multi-thread-environments-per-tenant-encryption-for-event-driven-systems-at-scale/)）。
- **失效策略**：Valkey 与 Redis 原生支持基于过期的失效（设置 TTL 后由服务端移除）；更精确的失效需客户端协调。两者均通过 RESP3 协议的客户端追踪（client tracking）支持客户端缓存，服务端会在被追踪的 key 变化时通知客户端；而「代际（generation）整体递增」式失效会一次使大量条目同时失效，等于人为触发一次惊群，因此代际应限定在真正同时变化的数据范围内（[What is Cache Invalidation?](https://redisson.pro/glossary/cache-invalidation.html)）。
- **常见错误**：把 TTL 作为唯一策略会导致读到旧数据与惊群（[Two Hard Things: Naming Things & Cache Invalidation — Valkey Edition](https://almalinux.org/files/2026/aldg/aldg-2026-valkey-luna-rojas.pdf)）。
- **CDN 命中率诊断**：Cloudflare 提供 cache status 分类（如 Dynamic 表示资源本身不可缓存、Revalidated 表示回源校验），据此可定位可优化项（[Cache performance](https://developers.cloudflare.com/cache/performance-review/cache-performance)）。
- **TTL 抖动的具体实现**：以基础 TTL 叠加随机偏移（例如基础 3600 秒、抖动 ±600 秒）来避免大量 key 在同一时刻集体过期（[Two Hard Things: Naming Things & Cache Invalidation — Valkey Edition](https://almalinux.org/files/2026/aldg/aldg-2026-valkey-luna-rojas.pdf)）。
- **层次与责任划分**：进程内缓存作为 L1（超快、节点本地），分布式缓存作为 L2（快速、集群级），数据库作为唯一事实来源；命中顺序通常为 L1 → L2 → 源站（[Application-Level Caching](https://adamdjellouli.com/articles/backend_engineers_guide/05_caching/07_application_level_caching)）。
- **分层 TTL 设计**：多级缓存实践中，L1 常设置较短 TTL（例如 5–10 分钟）并叠加随机偏移，L2 保存全量业务数据，热 key 不设过期、冷 key 用短 TTL 加随机偏移，以兼顾一致性域与防雪崩（[Prevent Cache Avalanche with Multi-Level Caffeine + Redis](https://www.besthub.dev/articles/prevent-cache-avalanche-with-multi-level-caffeine-redis-high-availability-design-d3d0dee62adf)）。

## 代表性项目 / 公司 / 产品（附官方链接）

| 项目 / 产品 | 定位 | 链接 |
| --- | --- | --- |
| Redis 8 | 内存数据平台，含 vector set、Search、JSON、时序与概率结构 | [redis.io](https://redis.io:8443/blog/redis-8-ga/) |
| Valkey | Linux Foundation 下的开源键值数据库，9.1 已 GA | [linuxfoundation.org](https://www.linuxfoundation.org/press/valkey-enhances-efficiency-security-and-modular-performance-with-9.1-release-and-new-ecosystem-integrations) |
| Cloudflare Cache Reserve / Tiered Cache | CDN 边缘缓存与分层缓存 | [cloudflare.com](https://www.cloudflare.com/products/cache-reserve/) |
| Caffeine | JVM 进程内高性能缓存库 | [AWS Security Blog](https://aws.amazon.com/blogs/security/caching-kms-data-keys-in-multi-thread-environments-per-tenant-encryption-for-event-driven-systems-at-scale/) |
| Memcached | 经典分布式内存缓存 | [Application-Level Caching](https://adamdjellouli.com/articles/backend_engineers_guide/05_caching/07_application_level_caching) |
| Redisson | 基于 Redis/Valkey 的客户端与失效协调 | [redisson.pro](https://redisson.pro/glossary/cache-invalidation.html) |

## 关键数据与评测结果（附来源）

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| Redis 8 性能改进项 | 30+ 项 | [redis.io](https://redis.io:8443/blog/redis-8-ga/) |
| Valkey 8.1 额外内存节省 | 27%（小键值对最多 41%） | [valkey.io](https://valkey.io/blog/valkey-at-laracon-india-2026/) |
| Valkey 9.0 单集群吞吐 | 最多 10 亿次操作/秒 | [valkey.io](https://valkey.io/blog/valkey-at-laracon-india-2026/) |
| Valkey 8.x 最新版本 | 8.1.10（2026-09-01） | [valkey.io](https://valkey.io/) |
| Cloudflare vs CloudFront 命中率（第三方估算） | 90–98% vs 85–95% | [Cloudflare vs AWS 2026](https://alloq.digital/en/blog/cloudflare-vs-aws/) |

需注意，Cloudflare 与 CloudFront 的命中率对比来自第三方博客，属估算口径，官方文档未给出可直接比较的数字。

## 趋势与争议

- **分发版本与许可争议的后续影响**：Redis 8 起提供三许可——RSALv2、SSPLv1 与 OSI 认可的 AGPLv3（[Licenses — Redis](https://redis.io/legal/licenses/)）；Valkey 由 Linux Foundation 支持、采用宽松的 BSD 3-Clause，定位为永久开源的高性能键值存储（[Valkey](https://valkey.io/)、[What is Valkey?](https://redis.io/blog/what-is-valkey/)）。Redis 与 Valkey 形成并存生态，Valkey 以 Linux Foundation 治理与「更省内存/更低基础设施成本」为卖点（[linuxfoundation.org](https://www.linuxfoundation.org/press/valkey-enhances-efficiency-security-and-modular-performance-with-9.1-release-and-new-ecosystem-integrations)）；Redis 则通过原生数据类型与 AI 相关能力（vector set）强化差异化（[redis.io](https://redis.io:8443/blog/redis-8-ga/)）。
- **「缓存即数据库」的边界**：Redis 8 引入更多数据结构与查询能力，使缓存层与数据层职责边界更模糊，其 beta 状态也提示 API 仍可能变化（[redis.io](https://redis.io/docs/latest/develop/whats-new/8-0/)）。
- **一致性成本**：客户端追踪、代际失效与分布式锁都能提升一致性精度，但分别引入协议依赖、惊群与额外延迟，不存在零成本的「精确失效」（[redisson.pro](https://redisson.pro/glossary/cache-invalidation.html)、[calmops.com](https://calmops.com/devops/caching-strategies-redis-cdn-application-cache/)）。
- **本地缓存的一致性风险**：多实例各自持有 L1 副本会造成一致性难题，因此多层方案通常把一致性职责交给 L2，并对 L1 采用短 TTL + 抖动（[codewithyoha.com](https://codewithyoha.com/blogs/mastering-advanced-caching-redis-caffeine-and-multi-layer-architectures)、[besthub.dev](https://www.besthub.dev/articles/prevent-cache-avalanche-with-multi-level-caffeine-redis-high-availability-design-d3d0dee62adf)）。
- **CDN 命中率并非越高越好**：对高度动态的内容，缓存可能带来陈旧风险，官方文档将部分资源默认标记为不可缓存即出于此考量（[developers.cloudflare.com](https://developers.cloudflare.com/cache/performance-review/cache-performance)）。

## 参考来源

1. [Redis 缓存层架构指南（Cache layer architecture guide）](https://redis.io:8443/blog/cache-layer-architecture-guide.md)
2. [Caching Strategies 2026: Redis, Valkey, CDN, and Application Caching](https://calmops.com/devops/caching-strategies-redis-cdn-application-cache/)
3. [What is Cache Invalidation?](https://redisson.pro/glossary/cache-invalidation.html)
4. [Two Hard Things: Naming Things & Cache Invalidation — Valkey Edition](https://almalinux.org/files/2026/aldg/aldg-2026-valkey-luna-rojas.pdf)
5. [DB 앞단 캐싱 전략 — Redis 캐시 레이어와 무효화](https://clang-engineer.github.io/posts/db/2026-07-03-caching-strategy-redis/)
6. [Redis 8 is now GA, loaded with new features and more than 30 performance improvements](https://redis.io:8443/blog/redis-8-ga/)
7. [Announcing vector sets: a new Redis data type for vector similarity](https://redis.io/blog/announcing-vector-sets-a-new-redis-data-type-for-vector-similarity.md)
8. [Redis 8.0（What's new）](https://redis.io/docs/latest/develop/whats-new/8-0/)
9. [Redis Open Source 8.0 release notes](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.0-release-notes/)
10. [Valkey Enhances Efficiency, Security, and Modular Performance with 9.1 Release and New Ecosystem Integrations](https://www.linuxfoundation.org/press/valkey-enhances-efficiency-security-and-modular-performance-with-9.1-release-and-new-ecosystem-integrations)
11. [Valkey Meets Laravel: Bridging Open Source Communities at Laracon India 2026](https://valkey.io/blog/valkey-at-laracon-india-2026/)
12. [Valkey（官方版本页）](https://valkey.io/)
13. [Valkey Blog](https://valkey.io/blog/)
14. [Cloudflare Cache Reserve](https://www.cloudflare.com/products/cache-reserve/)
15. [Cloudflare — Cache performance](https://developers.cloudflare.com/cache/performance-review/cache-performance)
16. [Designing a distributed web performance architecture](https://developers.cloudflare.com/reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/)
17. [Cloudflare vs AWS 2026: CDN, Security & Pricing Compared](https://alloq.digital/en/blog/cloudflare-vs-aws/)
18. [Mastering Advanced Caching: Redis, Caffeine, and Multi-Layer Architectures](https://codewithyoha.com/blogs/mastering-advanced-caching-redis-caffeine-and-multi-layer-architectures)
19. [Application-Level Caching](https://adamdjellouli.com/articles/backend_engineers_guide/05_caching/07_application_level_caching)
20. [Spring Boot Caching: Multi-Level Cache with Caffeine + Redis](https://blog.devops-monk.com/2026/05/spring-boot-caching-caffeine-redis/)
21. [Prevent Cache Avalanche with Multi-Level Caffeine + Redis: High-Availability Design](https://www.besthub.dev/articles/prevent-cache-avalanche-with-multi-level-caffeine-redis-high-availability-design-d3d0dee62adf)
22. [Caching KMS data keys in multi-thread environments](https://aws.amazon.com/blogs/security/caching-kms-data-keys-in-multi-thread-environments-per-tenant-encryption-for-event-driven-systems-at-scale/)
23. [Licenses — Redis](https://redis.io/legal/licenses/)
24. [What is Valkey? — Redis](https://redis.io/blog/what-is-valkey/)