# 并发与并行（Concurrency and Parallelism）

> 最后更新：2026-09-26 ｜ 领域：软件工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

并发（concurrency）指多个任务在时间上重叠推进，并行（parallelism）指多个任务在同一时刻真正同时执行。并发模型讨论的是「如何组织任务、如何共享状态、如何取消与传播错误」；并行则关心如何把工作切分到多核与多机上。

主流实现路线可分为几类：共享内存 + 线程/锁（Java、C++）、异步任务 + 事件循环（Rust async、JavaScript、Python asyncio）、协程（Go goroutine、Kotlin coroutines）、Actor 消息传递（Erlang/OTP、Akka/Pekko）、CSP 通道（Go channel）。2025–2026 年的主要变化是：结构化并发从语言实验走向标准化，虚拟线程/无栈协程大规摸进入生产，运行时（GC、调度器）也在为并发吞吐做专门优化。

## 最新进展（2025–2026）

**1. Java 结构化并发接近定稿。** JEP 525「Structured Concurrency (Sixth Preview)」的目标是简化并发编程：把一组运行在不同线程上的相关任务视为单个工作单元，从而简化错误处理与取消、提升可靠性与可观测性（[JEP 525: Structured Concurrency (Sixth Preview)](http://openjdk.org/jeps/525)）。该特性先在 JDK 19（JEP 428）、JDK 20（JEP 437）孵化，此后以预览形式迭代（[openjdk.org/jeps/525](http://openjdk.org/jeps/525)）。其 API 形态为 `StructuredTaskScope.open(...)` 配合 `scope.fork(...)` 与 `scope.join()`，使用方式接近同步代码（[结构化并发(JEP 525)终定稿!Java 26高并发代码](https://blog.csdn.net/HHX_01/article/details/159648429)）。

**2. 虚拟线程与结构化并发的定位被明确区分。** 按 JEP 444 的表述：虚拟线程提供「充裕的线程」，结构化并发则「正确地、稳健地协调」这些线程；二者互补而非竞争——虚拟线程消除了线程的成本，结构化并发消除了线程的风险（[Structured Concurrency: Why It Matters More Than Virtual Threads for Correctness](https://www.javacodegeeks.com/2026/04/structured-concurrency-why-it-matters-more-than-virtual-threads-for-correctness.html)）。在 API 选择上，扇出聚合（fan-out/collect）与「首个成功即返回」（hedging/racing）更适合用 `StructuredTaskScope` 与 `Joiner`，而无阻塞的异步流水线仍适合 `CompletableFuture`（[Structured Concurrency in Java: Why It's Better Than CompletableFuture](https://www.javacodegeeks.com/2026/03/structured-concurrency-in-java-why-its-better-than-completablefuture-and-what-it-still-cant-do.html)）。

**3. Go 1.26 默认启用新 GC 并改进并发相关开销。** Go 1.26 将此前在 1.25 中作为实验的 Green Tea 垃圾回收器默认启用，其设计通过更好的局部性与 CPU 可扩展性改善小对象的标记与扫描，官方预期在大量使用 GC 的真实程序中减少约 10%–40% 的 GC 开销（[Go 1.26 Release Notes](https://go.dev/doc/go1.26)）。同时，cgo 的基线开销降低约 30%，编译器在更多情形下可把切片的底层存储分配在栈上（[Go 1.26 is released](https://go.dev/blog/go1.26)）。后续版本的公开博客索引显示 Go 1.27 将加入泛型方法、`encoding/json/v2`、更快的内存分配与 goroutine 泄漏剖析（goroutine leak profiles）等（[Blog Index](https://go.dev/blog/all)）。

**4. Python 无 GIL 构建正式受支持。** 自 3.13 起 CPython 提供禁用全局解释器锁（GIL）的 free-threading 构建，使线程可在多核上真正并行；并非所有软件都能自动获益，但按线程化思路设计的程序在多核硬件上会更快（[Python support for free threading](https://docs.python.org/sv/3.14/howto/free-threading-python.html)）。Python 3.14 的发行说明列出 PEP 779——free-threaded Python 正式受支持（[What's new in Python 3.14](https://docs.python.org/3.16/whatsnew/3.14.html)）。此外，官方 macOS 与 Windows 二进制发行版现已包含实验性 JIT，可通过 `PYTHON_JIT=1` 测试，但官方不建议在生产中使用（[Python 3.14 有什么新变化](https://docs.python.org/zh-cn/3/whatsnew/3.14.html)）。

**5. Actor 模型路线继续获得工程验证。** Akka 侧发布的案例称其用 AI 迁移了 65 个开源项目，并强调单写者实体（single-writer entity）的价值：每个实体单线程处理、消息有序、请求间无共享可变状态，因而无需 `asyncio.Lock`、互斥量与「check-then-act」防御式判断（[We Ported 65 OSS Projects With AI](https://akka.io/blog/we-ported-65-oss-projects)）。

## 核心技术与关键概念

- **结构化并发**：以作用域限定任务生命周期，作用域结束即任务结束，从而获得清晰的错误传播与线程转储可观测性（[javacodegeeks.com](https://www.javacodegeeks.com/2026/03/structured-concurrency-in-java-why-its-better-than-completablefuture-and-what-it-still-cant-do.html)）。
- **虚拟线程（virtual threads）**：降低线程成本以支持大量并发阻塞式任务；对既有 WebFlux/Reactor 的团队，reactive 与虚拟线程以不同方式解决同一问题，而新项目若使用 Spring MVC 等命令式风格，虚拟线程通常更易调试（[Java Virtual Threads Deep Dive: Project Loom in Production (2026)](https://techoral.com/java/java-virtual-threads-deep-dive.html)）。
- **取消语义**：Rust async 中取消通过 drop future 实现，例如 Tokio 的 `oneshot::Receiver` 在 Drop 时向 Sender 发送关闭通知，从而实现自动撤销（[Tokio — Select](https://tokio.rs/tokio/tutorial/select)）；Tokio 的文档强调其利用所有权模型自动侦测「不再需要的计算」并撤销，无需用户显式调用 cancel（[Tokio 中文文档](https://tokio-cn.github.io/)）。
- **工作窃取调度**：Tokio 开箱提供多线程、工作窃取（work-stealing）调度器，启动运行时即利用全部 CPU 核心，在最小开销下可处理每秒数十万请求（[Tokio - An asynchronous Rust runtime](https://tokio.rs/)；[What is Tokio?](https://v0-1--tokio.netlify.app/docs/overview/)）。
- **抢占式调度与 reductions**：BEAM 虚拟机自行决定何时暂停并切换 Erlang/Elixir 进程，每个进程分配少量 reductions（计算单位），超出即被抢占，因此不会有单段代码饿死其他进程（[Why Developers Are Turning to Elixir for Scalable Apps](https://www.codowl.com/article/why-developers-are-turning-to-elixir-for-scalable-apps)）。
- **Actor 模型的无锁特性**：计算被组织为轻量、隔离、只通过消息通信的单元，没有共享状态、没有锁；JVM 上的代表实现是 Akka，其开源分支为 Apache Pekko（[What Is Reactive Architecture and Why It Matters](https://tms-outsource.com/blog/posts/reactive-architecture/)）。
- **背压（backpressure）**：Tokio 与 Akka 均把背压作为一等能力；Akka 强调流式处理端到端非阻塞、有背压，数据不在系统内无界缓冲（[akka.io](https://akka.io/blog/we-ported-65-oss-projects)）。

## 代表性项目 / 公司 / 产品（附官方链接）

| 项目 / 平台 | 模型 | 链接 |
| --- | --- | --- |
| OpenJDK Structured Concurrency（JEP 525） | 结构化并发（预览） | [openjdk.org/jeps/525](http://openjdk.org/jeps/525) |
| Java Virtual Threads（Project Loom） | 虚拟线程 | [techoral.com](https://techoral.com/java/java-virtual-threads-deep-dive.html) |
| Go runtime | goroutine、Green Tea GC | [go.dev](https://go.dev/doc/go1.26) |
| CPython free-threading | 无 GIL 多线程 | [docs.python.org](https://docs.python.org/sv/3.14/howto/free-threading-python.html) |
| Tokio | Rust 异步运行时、工作窃取 | [tokio.rs](https://tokio.rs/) |
| Erlang/OTP / Elixir | BEAM 抢占式调度、Actor | [codowl.com](https://www.codowl.com/article/why-developers-are-turning-to-elixir-for-scalable-apps) |
| Akka / Apache Pekko | JVM Actor 模型 | [tms-outsource.com](https://tms-outsource.com/blog/posts/reactive-architecture/) |

## 关键数据与评测结果（附来源）

- Go 1.26 官方预期 GC 开销降低约 10%–40%（重 GC 场景），cgo 基线开销降低约 30%（[go.dev/doc/go1.26](https://go.dev/doc/go1.26)、[go.dev/blog/go1.26](https://go.dev/blog/go1.26)）。
- 有第三方资料引述 Akka 在生产部署中达到每秒 140 万笔交易、9ms 延迟（[tms-outsource.com](https://tms-outsource.com/blog/posts/reactive-architecture/)）——该数字来自厂商转引的第三方博客，未附独立评测，引用时需注意口径。
- Tokio 官方称其应用可在最小开销下处理每秒数十万请求（[tokio.rs](https://tokio.rs/)）。
- 虚拟线程与固定线程池的基准结果因工作负载而异，公开文章中的典型生产发现按 I/O 密集型服务器场景对比（[techoral.com](https://techoral.com/java/java-virtual-threads-deep-dive.html)）。

## 趋势与争议

- **协程/虚拟线程 vs 异步回调**：命令式阻塞式写法（配虚拟线程）在可调试性上更优，而 reactive 在完全不阻塞线程的场景仍有优势；对既有 reactive 系统，迁移未必划算（[techoral.com](https://techoral.com/java/java-virtual-threads-deep-dive.html)）。
- **结构化并发是否应取代 CompletableFuture**：结构化并发在错误传播、取消与可观测性上更清晰，但无阻塞的异步流水线仍需要 `CompletableFuture` 一类工具，两者并非替代关系（[javacodegeeks.com](https://www.javacodegeeks.com/2026/03/structured-concurrency-in-java-why-its-better-than-completablefuture-and-what-it-still-cant-do.html)）。
- **语言层简化 vs 运行时复杂度**：无 GIL、Green Tea GC、虚拟线程等都在把复杂度下沉到运行时；收益依赖具体负载，官方也多以「预期」「因程序而异」表述（[docs.python.org](https://docs.python.org/sv/3.14/howto/free-threading-python.html)、[go.dev](https://go.dev/doc/go1.26)）。
- **生态兼容性**：free-threading 的收益受第三方 C 扩展是否支持无 GIL 构建制约（[docs.python.org](https://docs.python.org/fr/3.14/howto/free-threading-extensions.html)）。
- **Actor 模型的适配边界**：其无锁与顺序消息语义在实体级并发下收益明显，但需要改变数据建模方式（实体即单写者），并非对所有问题都适用（[akka.io](https://akka.io/blog/we-ported-65-oss-projects)）。

## 参考来源

1. [JEP 525: Structured Concurrency (Sixth Preview)](http://openjdk.org/jeps/525)
2. [Structured Concurrency: Why It Matters More Than Virtual Threads for Correctness](https://www.javacodegeeks.com/2026/04/structured-concurrency-why-it-matters-more-than-virtual-threads-for-correctness.html)
3. [Structured Concurrency in Java: Why It's Better Than CompletableFuture — and What It Still Can't Do](https://www.javacodegeeks.com/2026/03/structured-concurrency-in-java-why-its-better-than-completablefuture-and-what-it-still-cant-do.html)
4. [结构化并发(JEP 525)终定稿!Java 26高并发代码，再也不写线程池地狱](https://blog.csdn.net/HHX_01/article/details/159648429)
5. [Java Virtual Threads Deep Dive: Project Loom in Production (2026)](https://techoral.com/java/java-virtual-threads-deep-dive.html)
6. [Go 1.26 Release Notes](https://go.dev/doc/go1.26)
7. [Go 1.26 is released](https://go.dev/blog/go1.26)
8. [Go Blog Index](https://go.dev/blog/all)
9. [Go — Garbage collector (src/runtime/mgc.go)](https://go.dev/src/runtime/mgc.go)
10. [Go Release History](https://go.dev/doc/devel/release)
11. [Python support for free threading](https://docs.python.org/sv/3.14/howto/free-threading-python.html)
12. [What's new in Python 3.14](https://docs.python.org/3.16/whatsnew/3.14.html)
13. [Python 3.14 有什么新变化](https://docs.python.org/zh-cn/3/whatsnew/3.14.html)
14. [C API Extension Support for Free Threading](https://docs.python.org/fr/3.14/howto/free-threading-extensions.html)
15. [Tokio - An asynchronous Rust runtime](https://tokio.rs/)
16. [Tokio — Select（取消语义）](https://tokio.rs/tokio/tutorial/select)
17. [Tokio 中文文档](https://tokio-cn.github.io/)
18. [What is Tokio?](https://v0-1--tokio.netlify.app/docs/overview/)
19. [Why Developers Are Turning to Elixir for Scalable Apps](https://www.codowl.com/article/why-developers-are-turning-to-elixir-for-scalable-apps)
20. [What Is Reactive Architecture and Why It Matters](https://tms-outsource.com/blog/posts/reactive-architecture/)
21. [We Ported 65 OSS Projects With AI](https://akka.io/blog/we-ported-65-oss-projects)
22. [Actor模型在分布式并发系统中的原理剖析、优势及在Akka框架中的实践应用](https://blog.csdn.net/2301_77485708/article/details/157209331)