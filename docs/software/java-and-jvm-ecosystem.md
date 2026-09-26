# Java 与 JVM 生态

> 最后更新：2026-09-26 ｜ 领域：软件·语言与运行时 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

Java 是一门面向对象的静态类型语言，依托 JVM（Java Virtual Machine）实现「一次编写，到处运行」。JVM 通过字节码、即时编译（JIT，C1/C2）与多种垃圾回收器在吞吐、延迟与内存之间提供可调权衡，并支持 Kotlin、Scala、Groovy、Clojure 等多语言运行。Java 拥有规模巨大的企业级生态（Spring、Jakarta EE、Apache 生态）与稳定的 LTS 发布节奏（JDK 21、JDK 25），长期作为交易型系统的「骨干」语言（[Java Trends of 2026](https://keyholesoftware.com/java-trends-2026/)）。

## 最新进展（2025–2026）

1. **JDK 25 LTS（2025-09-16 发布）。** Oracle 公布的特性包括：JEP 519 紧凑对象头（在 64 位架构上将对象头缩减到 64 位，提升部署密度与数据局部性）、JEP 514 AOT 命令行易用性、JEP 513 灵活的构造器体（允许在显式调用构造器前做输入校验与安全计算）（[Oracle Releases Java 25](https://www.oracle.com/tr/news/announcement/oracle-releases-java-25-2025-09-16/)）。第三方总结指出，启用 `-XX:+UseCompactObjectHeaders` 后小对象内存占用可显著下降（[JDK 25 新特性极简总结](https://cloud.tencent.com/developer/article/2589586)）。

2. **JDK 25 性能改进。** OpenJDK 团队总结称，JEP 521 使 Generational Shenandoah 转为正式产品特性；ZGC 重整页分配（以 Mapped Cache 取代 Page Cache）以改善未用内存管理（[Performance Improvements in JDK 25](https://inside.java/2025/10/20/jdk-25-performance-improvements/)）。Red Hat 表示其 OpenJDK 25 LTS 构建随 RHEL 10.1 提供，支持至 2030 年 12 月，并强调启动更快、内存占用更低（[OpenJDK 25 now available in Red Hat Enterprise Linux 10.1](https://developers.redhat.com/articles/2025/12/04/openjdk-25-now-available-red-hat-enterprise-linux-10-1)）。

3. **虚拟线程与并发。** 虚拟线程在 Java 21 定型，Java 24 移除了部分限制；虚拟线程由 JVM 管理、成本远低于操作系统线程，适合 I/O 密集的微服务与请求-响应负载（[Reasons to move to Java 25](https://learn.microsoft.com/en-us/java/openjdk/reasons-to-move-to-java-25)）。JDK 26 的待办项中包含「允许在常见类初始化路径上抢占虚拟线程」的改进（[OpenJDK Quality Outreach update](https://mail.openjdk.org/archives/list/quality-discuss@openjdk.org/message/6X46TJDUJM2LL23HZCSQAFWRXQDGZSNA/attachment/2/attachment.html)）。

4. **发布节奏。** JDK 26 计划于 2026 年 3 月 17 日正式可用（[OpenJDK Quality Outreach update](https://mail.openjdk.org/archives/list/quality-discuss@openjdk.org/message/6X46TJDUJM2LL23HZCSQAFWRXQDGZSNA/attachment/2/attachment.html)）。

5. **Project Valhalla 落地。** OpenJDK 官方称，JEP 401（Value Objects，预览）与 JEP 539（JVM 中严格字段初始化，预览）已集成，将包含在 JDK 28 中，并已提供基于 JDK 28 的早期访问构建（[Project Valhalla](https://openjdk.org/projects/valhalla/)、[JEP 401: Value Objects (Preview)](https://openjdk.org/jeps/401)）。第三方解读补充：Oracle 工程师 Lois Foltan 在 2026 年 6 月确认该特性进入 OpenJDK 主线，目标为 2027 年 3 月的 JDK 28，作为预览特性（[Project Valhalla's Value Classes Are Finally Real](https://www.javacodegeeks.com/2026/08/project-valhallas-value-classes-are-finally-real.html)）。

6. **ZGC 后续与 GraalVM。** 已有 JEP 草案提出 ZGC 自适应堆大小（`-XX:+ZAdaptiveHeapSizing`，在 JDK 28 默认关闭，计划后续版本默认开启）（[JEP draft: Automatic Heap Sizing for ZGC](http://openjdk.org/jeps/8377305)）与 ZGC 更快启动/预热（[JEP draft: Faster Startup and Warmup with ZGC](http://openjdk.org/jeps/8329758)）。GraalVM 25.2.4 为基于 OpenJDK 25.0 的创新版本（[GraalVM 25.2.4 Release Notes](https://www.graalvm.org/release-notes/25.2/)）。

7. **框架与生态。** Spring Boot 4 与 GraalVM 24 对齐并继续强化 Native Image 支持，要求 Kotlin 至少 2.2（[Spring Boot 4 im Xperten-Check](https://www.itsonix.eu/de/blog/20260623-spring-boot-4-im-xperten-check)）。JVM 生态开始面向 AI Agent 扩展，例如 Koog 从 Kotlin Agent 框架发展为提供完整惯用 Java API（[Java in April 2026](https://techlife.blog/posts/java-ecosystem-april-2026/)）。

## 核心技术与关键概念

- **字节码与 JIT。** JVM 执行字节码，热点代码由 C1（快启动、低优化）与 C2（高优化）分层编译，配合去优化（deoptimization）。
- **垃圾回收器谱系。** G1（默认、均衡）、ZGC（并发、亚毫秒停顿、停顿与堆大小无关，代价是更高内存与 CPU）、Shenandoah（JDK 25 转正的分代模式，内存开销更低）（[The JVM Garbage Collector Decision in 2026](https://www.javacodegeeks.com/2026/04/the-jvm-garbage-collector-decision-in-2026-g1-vs-zgc-vs-shenandoah-for-real-workloads.html)、[ZGC Overview](https://wiki.openjdk.org/spaces/zgc/overview)）。
- **虚拟线程与结构化并发。** 轻量线程与 `StructuredTaskScope` 简化 thread-per-request 风格的并发。
- **Project Panama（FFM API）。** 通过 `java.lang.foreign` 安全调用本地代码，替代部分 JNI 场景。
- **Project Valhalla。** 值类/值对象旨在消除对象身份开销，配合泛型特化改善内存布局；JEP 539 严格字段初始化配合其语义（[Project Valhalla](https://openjdk.org/projects/valhalla/)）。
- **GraalVM 与 Native Image。** AOT 编译为原生可执行文件，降低启动时间与内存占用，适合微服务（[Oracle GraalVM solution brief](https://www.oracle.com/a/ocom/docs/graalvm-enterprise-modern-app-solution-brief.pdf)）。
- **模块系统与生态语言。** JPMS 模块化；Kotlin（JVM 兼容、渐进采用）、Scala（函数式与效应库）、Groovy 等。

## 代表性项目 / 公司 / 产品（附官方链接）

- Oracle Java / OpenJDK — [oracle.com/java](https://www.oracle.com/java/)
- Project Valhalla — [openjdk.org/projects/valhalla](https://openjdk.org/projects/valhalla/)
- GraalVM — [graalvm.org](https://www.graalvm.org/)
- Spring — [spring.io](https://spring.io/)
- Kotlin（JetBrains）— [kotlinlang.org](https://kotlinlang.org/)
- ZGC 项目页 — [wiki.openjdk.org/spaces/zgc](https://wiki.openjdk.org/spaces/zgc/overview)

## 关键数据与评测结果（附来源）

- 2025 年 Stack Overflow 开发者调查显示，Java 使用率约 29.4%，Kotlin 约 10.8%（[Technology](https://survey.stackoverflow.co/2025/technology)）。
- 关于语言分工，分析指出 Java 主要用于交易型系统，Python 用于数据、ML 与自动化；Kotlin 在 Android 与现代后端上升但极少取代既有 Java 企业系统；Go 与 Rust 更多出现在新微服务、云基础设施与性能关键路径，而非替代既有 Java 系统（[Java Trends of 2026](https://keyholesoftware.com/java-trends-2026/)）。
- Red Hat 声明其 OpenJDK 25 LTS 支持至 2030 年 12 月（[OpenJDK 25 now available in RHEL 10.1](https://developers.redhat.com/articles/2025/12/04/openjdk-25-now-available-red-hat-enterprise-linux-10-1)）。

## 趋势与争议

- **升级节奏压力。** 六个月的 feature release 与两年一次的 LTS，使企业需在安全更新与升级成本之间权衡；JDK 25 作为新 LTS 成为主流迁移目标。
- **Valhalla 时间线。** 值类自提出以来多次推迟，早期访问构建自 JDK 26 基线起提供，正式进入主线并计划在 JDK 28 预览，社区对其性能收益与迁移影响持续关注（[Project Valhalla's Value Classes Are Finally Real](https://www.javacodegeeks.com/2026/08/project-valhallas-value-classes-are-finally-real.html)）。
- **Native Image 权衡。** 更快启动与更低内存的代价是构建复杂度、反射配置与峰值吞吐差异。
- **Kotlin 与 Java 的关系。** Kotlin 在 Android 与现代后端扩张，但企业存量 Java 系统的迁移成本使其长期共存（[Java Trends of 2026](https://keyholesoftware.com/java-trends-2026/)）。
- **AI 时代的 JVM 定位。** 围绕 Agent 的 Java 化框架（如 Koog 的 Java API 与 Spring AI 的集成层定位）正在形成，但生态成熟度仍待观察（[Java in April 2026](https://techlife.blog/posts/java-ecosystem-april-2026/)）。

## 参考来源

1. [Oracle Releases Java 25](https://www.oracle.com/tr/news/announcement/oracle-releases-java-25-2025-09-16/)
2. [Performance Improvements in JDK 25](https://inside.java/2025/10/20/jdk-25-performance-improvements/)
3. [OpenJDK 25 now available in Red Hat Enterprise Linux 10.1](https://developers.redhat.com/articles/2025/12/04/openjdk-25-now-available-red-hat-enterprise-linux-10-1)
4. [JDK 25 新特性极简总结](https://cloud.tencent.com/developer/article/2589586)
5. [Reasons to move to Java 25（Microsoft）](https://learn.microsoft.com/en-us/java/openjdk/reasons-to-move-to-java-25)
6. [OpenJDK Quality Outreach update（JDK 26 GA 与虚拟线程抢占）](https://mail.openjdk.org/archives/list/quality-discuss@openjdk.org/message/6X46TJDUJM2LL23HZCSQAFWRXQDGZSNA/attachment/2/attachment.html)
7. [Project Valhalla（OpenJDK）](https://openjdk.org/projects/valhalla/)
8. [JEP 401: Value Objects (Preview)](https://openjdk.org/jeps/401)
9. [Project Valhalla's Value Classes Are Finally Real](https://www.javacodegeeks.com/2026/08/project-valhallas-value-classes-are-finally-real.html)
10. [JEP draft: Automatic Heap Sizing for ZGC](http://openjdk.org/jeps/8377305)
11. [JEP draft: Faster Startup and Warmup with ZGC](http://openjdk.org/jeps/8329758)
12. [GraalVM 25.2.4 Release Notes](https://www.graalvm.org/release-notes/25.2/)
13. [Spring Boot 4 im Xperten-Check](https://www.itsonix.eu/de/blog/20260623-spring-boot-4-im-xperten-check)
14. [Java in April 2026: Leyden Grows Up, Spring Gets Smarter](https://techlife.blog/posts/java-ecosystem-april-2026/)
15. [The JVM Garbage Collector Decision in 2026: G1 vs ZGC vs Shenandoah](https://www.javacodegeeks.com/2026/04/the-jvm-garbage-collector-decision-in-2026-g1-vs-zgc-vs-shenandoah-for-real-workloads.html)
16. [ZGC Overview（OpenJDK Wiki）](https://wiki.openjdk.org/spaces/zgc/overview)
17. [Oracle Solution brief: Java and GraalVM](https://www.oracle.com/a/ocom/docs/graalvm-enterprise-modern-app-solution-brief.pdf)
18. [Java Trends of 2026](https://keyholesoftware.com/java-trends-2026/)
19. [Stack Overflow Developer Survey 2025 — Technology](https://survey.stackoverflow.co/2025/technology)