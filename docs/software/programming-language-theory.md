# 编程语言理论与范式

> 最后更新：2026-09-26 ｜ 领域：软件·语言与运行时 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

编程语言理论（Programming Language Theory, PLT）研究语言的形式语义、类型系统、内存模型与编译实现，是系统软件与工程语言设计的理论基础。其核心议题包括：静态类型与动态类型的取舍、类型系统的表达力（泛型、子类型、依赖类型、线性/仿射类型）、内存管理方式（手动、所有权、垃圾回收）、并发内存模型，以及从源码到机器码的编译流水线。

2025–2026 年，这一领域最显著的外部驱动力来自两点：一是各国监管与安全机构推动的「内存安全」要求，直接改变了系统级语言的选择偏好；二是 AI 辅助编程的普及，对语言工具链性能、类型系统易用性与编译器速度提出了新需求。

## 最新进展（2025–2026）

1. **内存安全成为政策议题。** 相关安全架构资料显示，CISA 已要求关键基础设施软件供应商提交内存安全路线图，截止日期为 2026 年 1 月 1 日（[Security Architecture](https://coproduct-opensource.github.io/nucleus/architecture/security.html)）。回顾脉络：NSA 在 2022 年指南中将 Rust、C#、Go、Java、Python、Swift 列为内存安全语言，白宫 ONCD 2024 年报告称 C 与 C++ 对新软件而言「过于危险」，CISA 2023 年指南将 Rust 列为内存安全重写的首选底层语言（[Rust & Memory Safety: What NSA, CISA & White House Say (2026)](https://rustify.rs/articles/rust-memory-safety-nsa-cisa-2026)）。

2. **主流语言主动补足内存安全。** 微软在 C# 15 中启动「重新定义内存安全」的多版本计划，将 `unsafe` 上下文绑定到真正访问非托管内存的操作，而非仅凭指针类型的存在（[What's new in C# 15](https://learn.microsoft.com/en-us/dotNet/csharp/whats-new/csharp-15)）；微软同时说明 `unsafe` 关键字正被重新设计，改用新的安全注释风格向调用方声明「必须履行的安全义务」（[Improving C# Memory Safety](https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/)）。

3. **代数效应（algebraic effects）进入主流语言。** 2026 年开源的编译型语言 Cangjie（仓颉）原生支持 effect handlers，引入 `perform` 与 `resume` 关键字，将异常机制泛化（[Cangjie, a New Open-Source Compiled Language with Native Effect Handlers and Algebraic Data Types](https://www.infoq.com/news/2026/05/cangjie-effect-handlers-adt/)）；研究型语言 Effekt 长期实践词法效应处理器，其效应处理器被称为「异常处理器的加强版」（[Effekt Language](https://effekt-lang.org/)）。

4. **垃圾回收持续演进。** JDK 25（2025 年 9 月 GA）将 Generational Shenandoah 转为正式产品特性，并重整 ZGC 的页分配机制（[Performance Improvements in JDK 25](https://inside.java/2025/10/20/jdk-25-performance-improvements/)）；ZGC 自 JDK 21 起重新实现以支持分代，停顿时间与堆大小无关，可覆盖数百 MB 到 16TB 的堆（[ZGC Overview](https://wiki.openjdk.org/spaces/zgc/overview)）。业界分析指出，2026 年全分代化的 ZGC 可实现亚毫秒停顿，但内存开销高 15–30%、CPU 高 5–10%，而 Shenandoah 在 JDK 25 转正后在内存开销上更占优（[The JVM Garbage Collector Decision in 2026](https://www.javacodegeeks.com/2026/04/the-jvm-garbage-collector-decision-in-2026-g1-vs-zgc-vs-shenandoah-for-real-workloads.html)）。

5. **编译流水线与编译性能。** TypeScript 7.0 于 2026 年 7 月发布，将编译器与语言服务整体用 Go 重写为原生二进制，利用原生代码速度与共享内存多线程，全量构建常见提速约 8–12 倍（[Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)）。MLIR 继续扩展为多后端编译基础设施，2026 年出现了面向 agentic AI 的 dataflow dialect（[Tenth LLVM Performance Workshop at CGO](https://llvm.org/devmtg/2026-01/)）。

6. **新语言与运行时版本。** Mojo 发布 v1.0.0b1，统一 `fn` 与 `def`（[Mojo v1.0.0b1](https://www.mojolang.org/releases/v1.0.0b1/)）；Zig 最新版本 0.16.0，强调编译期代码执行、无隐式控制流与无隐式内存分配（[Zig 编程语言](https://ziglang.org/zh-CN/)）；Swift 6.4 以 Swift Build 作为 Swift Package Manager 默认构建系统，并推进跨平台子进程 API（[Swift 6.4 Released](https://www.swift.org/blog/swift-6.4-released/)）。

## 核心技术与关键概念

- **类型系统。** 静态与动态类型、结构化与名义类型、子类型、参数化多态与特设多态、依赖类型、线性与仿射类型（资源「恰好一次」或「至多一次」使用，是所有权模型的类型论根基）、渐进类型。
- **所有权与借用。** Rust 要求每个值有唯一所有者，所有权转移（move）后原变量失效，借用允许临时访问但不转移所有权，编译器保证借用不超出被引用数据的生命周期，从而在编译期消除 use-after-free、double-free 与数据竞争，且无运行时 GC 开销（[Memory-Safe Systems Programming: Rust vs C++20 vs Ada](https://drcodes.com/posts/memory-safe-systems-programming-rust-vs-c20-vs-ada)）。
- **内存模型。** 定义并发下读写的可见性与原子性；数据竞争自由（data-race freedom）是安全语言的重要目标。
- **垃圾回收。** 追踪式回收、标记-清除/复制/标记-整理、分代假设、并发与增量回收、区域回收。停顿时间、吞吐与内存开销构成典型三角权衡。
- **编译原理。** 词法/语法分析、AST、中间表示（SSA）、优化、寄存器分配、JIT 与 AOT 权衡；LLVM 与 MLIR 是主要编译基础设施，Cranelift 等后端面向快速编译场景。
- **效应系统。** 将「程序产生什么副作用」编码进类型，代数效应与处理器可把 I/O、状态、异常等统一建模并组合，支持多发射恢复（multi-shot resumptions）（[Flix](https://flix.dev/#/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- Rust — [rust-lang.org](https://www.rust-lang.org/)
- Effekt — [effekt-lang.org](https://effekt-lang.org/)
- Flix — [flix.dev](https://flix.dev/#/)
- Koka — [github.com/koka-lang/koka](https://github.com/koka-lang/koka)
- Zig — [ziglang.org](https://ziglang.org/)
- Mojo — [mojolang.org](https://www.mojolang.org/)
- LLVM / MLIR — [llvm.org](https://llvm.org/)
- Cangjie（仓颉）— 见 InfoQ 报道（[链接](https://www.infoq.com/news/2026/05/cangjie-effect-handlers-adt/)）

## 关键数据与评测结果（附来源）

- 2025 年 Stack Overflow 开发者调查（49,000+ 份回答，177 个国家）显示使用率：JavaScript 66%、HTML/CSS 61.9%、SQL 58.6%、Python 57.9%、Bash/Shell 48.7%、TypeScript 43.6%、Java 29.4%、Rust 14.8%；Rust 连续多年被评为「最受推崇」语言（[Technology](https://survey.stackoverflow.co/2025/technology)）。
- 与 2024 年相比，Python 使用率上升约 7 个百分点，Rust 与 Go 各上升约 2 个百分点（[Developers remain willing but reluctant to use AI: The 2025 Developer Survey results](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/)）。

## 趋势与争议

- **内存安全的立法化与采购化。** 政策要求与语言选择直接挂钩，争议在于「选用内存安全语言是否等价于安全软件」，以及重写既有 C/C++ 代码的成本、性能回退与生态风险。
- **GC vs 所有权。** 争论集中在可预测尾延迟、吞吐、开发效率与学习曲线之间的取舍；Rust 的采用常以「GC 停顿不可接受」的生产事故为触发点（[Rust's Enterprise Takeover](https://www.javacodegeeks.com/2026/02/rusts-enterprise-takeover-when-memory-safety-becomes-non-negotiable.html)）。
- **编译速度。** Rust 官方社区调研指出，从新手到专家、从嵌入式到 Web 开发者，均把编译时间视为显著的生产力障碍，有人对比「Java 约 100 毫秒，Rust 视改动为 5 秒到 1 分钟」（[What we heard about Rust's challenges](https://blog.rust-lang.org/2026/03/20/rust-challenges.md/)）。
- **效应系统的落地张力。** 学术界的表达力与工业界的可理解性、运行时性能之间仍存在矛盾。
- **AI 生成代码的反向需求。** 更强类型与形式化验证被用于约束生成代码的正确性，但相关工具链在安全关键领域仍不成熟（[What does it take to ship Rust in safety-critical?](https://blog.rust-lang.org/2026/01/14/what-does-it-take-to-ship-rust-in-safety-critical/)）。

## 参考来源

1. [Security Architecture（CISA memory-safety roadmap）](https://coproduct-opensource.github.io/nucleus/architecture/security.html)
2. [Rust & Memory Safety: What NSA, CISA & White House Say (2026)](https://rustify.rs/articles/rust-memory-safety-nsa-cisa-2026)
3. [What's new in C# 15](https://learn.microsoft.com/en-us/dotNet/csharp/whats-new/csharp-15)
4. [Improving C# Memory Safety](https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/)
5. [Cangjie, a New Open-Source Compiled Language with Native Effect Handlers and Algebraic Data Types](https://www.infoq.com/news/2026/05/cangjie-effect-handlers-adt/)
6. [Effekt Language](https://effekt-lang.org/)
7. [Flix](https://flix.dev/#/)
8. [Performance Improvements in JDK 25](https://inside.java/2025/10/20/jdk-25-performance-improvements/)
9. [ZGC Overview（OpenJDK Wiki）](https://wiki.openjdk.org/spaces/zgc/overview)
10. [The JVM Garbage Collector Decision in 2026: G1 vs ZGC vs Shenandoah](https://www.javacodegeeks.com/2026/04/the-jvm-garbage-collector-decision-in-2026-g1-vs-zgc-vs-shenandoah-for-real-workloads.html)
11. [Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
12. [Tenth LLVM Performance Workshop at CGO](https://llvm.org/devmtg/2026-01/)
13. [Mojo v1.0.0b1](https://www.mojolang.org/releases/v1.0.0b1/)
14. [Zig 编程语言](https://ziglang.org/zh-CN/)
15. [Swift 6.4 Released](https://www.swift.org/blog/swift-6.4-released/)
16. [Memory-Safe Systems Programming: Rust vs C++20 vs Ada](https://drcodes.com/posts/memory-safe-systems-programming-rust-vs-c20-vs-ada)
17. [Stack Overflow Developer Survey 2025 — Technology](https://survey.stackoverflow.co/2025/technology)
18. [Developers remain willing but reluctant to use AI: The 2025 Developer Survey results](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/)
19. [Rust's Enterprise Takeover: When Memory Safety Becomes Non-Negotiable](https://www.javacodegeeks.com/2026/02/rusts-enterprise-takeover-when-memory-safety-becomes-non-negotiable.html)
20. [What we heard about Rust's challenges, and how we can address them](https://blog.rust-lang.org/2026/03/20/rust-challenges.md/)
21. [What does it take to ship Rust in safety-critical?](https://blog.rust-lang.org/2026/01/14/what-does-it-take-to-ship-rust-in-safety-critical/)