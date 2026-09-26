# 系统编程语言：C/C++ 与 Zig、Carbon 等

> 最后更新：2026-09-26 ｜ 领域：软件·架构与 API ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

系统编程语言指直接面向操作系统内核、嵌入式、编译器、数据库与高性能基础设施的语言家族，长期以 C 与 C++ 为核心。它们贴近硬件、可预测、运行时开销小，但也以手动内存管理与未定义行为（UB）著称。2025–2026 年，围绕「内存安全」的政策压力与技术演进成为该领域主线：一方面 C++ 通过标准库加固（hardening）、合约（contracts）与安全 profiles 做增量修补；另一方面 Rust 在 Linux 内核等关键场景获得正式地位，Zig、Carbon 等新语言继续探索不同的设计取舍。

## 最新进展（2025–2026）

### C++26 定稿与 C++29 启动

ISO C++ 委员会（WG21）在 2026 年 3 月完成了 C++26 的技术工作，并于同年 6 月投票将首批新特性纳入 C++29 工作草案。C++26 的关键语言改进包括编译期反射（reflection）与首轮内存安全加固，标准库方面新增 `std::simd` 与 `std::execution`（[CppCon 2026 综述](https://isocpp.org/blog/cgal/P1280)）。第三方梳理提到，C++26 经过多达二十余次修订，主要变更包含反射、中断五年后回归的合约，以及一系列消除 UB 的安全增强（[C++26 变更清单](https://programistamag.pl/wp-content/uploads/downloads/Programista_121_czym_zachwyci_cpp26_a.pdf)）。委员会同时披露，已在 C++29 草案中新增附录，系统性地处理 UB 并为 C++ 引入安全 profiles（[Standard C++ 标准化动态](https://isocpp.org/blog/rss/category/standardization)）。

### 内存安全：从工程议题上升为监管议题

多项检索资料一致指出，美国、欧盟、英国、德国、澳大利亚的网络安全机构已联合发声，呼吁停止在安全关键软件中使用 C/C++，并将其定性为国家安全问题（[Memory Safety Is Now a National Security Issue](https://www.aioapex.com/en/blog/memory-safety-is-now-a-national-security-issue-why-the-us-and-eu-want-developers-mq3ec9hn)）。有资料称美国 CISA 为软件厂商设定了 2026 年 1 月 1 日的期限，要求其发布「内存安全路线图」或转向内存安全语言（[The 2026 Memory Safety Mandate](https://techlife.blog/posts/memory-safety-modernization/)；[Why Everyone is Shifting from C/C++ to Rust](https://www.avidclan.com/blog/why-everyone-is-shifting-from-c-and-c-plus-to-rust)）。上述具体期限与备忘录编号在不同二手来源间存在差异，需谨慎对待。

C++ 社群对此作出回应。WG21 论文 P3081R2《Core safety profiles for C++26》提出默认禁止手动动态生命周期管理、保证空指针检查等规则（[P3081R2](https://open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3081r2.pdf)）；P3589R1 给出 profiles 的总体框架，强调类型与内存安全 profiles 应在所有实现中可用（[P3589R1](https://isocpp.org/files/papers/P3589R1.pdf)）。也有论文以「C++ 是否应成为内存安全语言」为题，主张 C++ 会「渐进地变得足够安全」，手段是标准库加固、合约与安全 profiles，而非彻底消除所有 UB（[P3874R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3874r1.pdf)）。此外有提案主张加固实现中的断言应采用「终止语义」（[P3878R1](https://isocpp.org/files/papers/P3878R1.html)）。

### Zig

Zig 保持高频发布节奏：0.15.1 的发布说明显示该版本包含来自 162 位贡献者的 647 次提交，并移除了已弃用字段（[Zig 0.15.1 Release Notes](https://ziglang.org/download/0.15.1/release-notes.html)）；官方下载页列出 0.16.0 于 2026 年 4 月 13 日发布（[Zig Releases](https://ziglang.org/it-IT/download/)）。官方 devlog 显示 2026 年 8 月 27 日的条目预告 0.17.0 将于数周内发布（[Zig Devlog 2026](https://ziglang.org/devlog/2026/)）。Zig 以「通用编程语言与工具链，用于维护健壮、最优、可复用的软件」自我定位（[Zig 0.16.0 Release Notes](https://ziglang.org/download/0.16.0/release-notes.html)）。

### Carbon

Carbon 由 Google 主导，目标是成为 C++ 的「后继语言」。官方文档明确其当前仍为实验性项目，团队正推进编译器与链接器工具链，并希望验证能否在 C++ 产业中取得临界规模的关注（[Carbon Language documentation](https://docs.carbon-lang.dev/)）。第三方报道称该项目已累积超过 5,200 次提交、33.7k stars，处于关键成熟阶段（[Carbon Programming Language 2026](https://www.programming-helper.com/tech/carbon-programming-language-2026-google-experimental-cpp-successor)）。

## 核心技术与关键概念

- **内存安全（memory safety）**：C/C++ 中大量漏洞源于越界、悬垂指针与 UB；安全 profiles 与标准库加固试图在保持兼容与性能的前提下削减这类风险（[P3874R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3874r1.pdf)）。
- **安全 profiles 与合约**：profiles 是可选的、保证可用的规则集合；合约用于表达前置/后置条件，二者共同构成 C++26 的安全基线（[P3589R1](https://isocpp.org/files/papers/P3589R1.pdf)）。
- **编译期反射**：C++26 引入反射，使编译期元编程从模板技巧转向语言原生能力（[CppCon 2026 综述](https://isocpp.org/blog/cgal/P1280)）。
- **Rust 的零成本安全**：所有权与借用检查在编译期消除整类内存错误，成为监管语境下 C/C++ 的主要替代叙事（[Memory Safety 国家议题](https://www.aioapex.com/en/blog/memory-safety-is-now-a-national-security-issue-why-the-us-and-eu-want-developers-mq3ec9hn)）。
- **Zig 的取舍**：不引入隐藏控制流、强调显式内存分配与构建系统一体化；Carbon 则强调与 C++ 的互操作与渐进迁移（[Zig 0.16.0](https://ziglang.org/download/0.16.0/release-notes.html)；[Carbon docs](https://docs.carbon-lang.dev/)）。

## 代表性项目 / 组织 / 产品

- **ISO C++ / WG21**：制定 C++ 标准的国际委员会，2026 年完成 C++26 并推进 C++29（[isocpp.org](https://isocpp.org/blog/rss/category/standardization)）。
- **Zig Software Foundation**：Zig 语言与工具链的官方组织（[ziglang.org](https://ziglang.org/devlog/2026/)）。
- **Google Carbon**：实验性 C++ 后继语言项目（[docs.carbon-lang.dev](https://docs.carbon-lang.dev/)）。
- **Linux 内核 Rust-for-Linux**：Rust 在系统层的代表落地项目（[rust-for-linux.com](https://rust-for-linux.com/print)）。

## 关键数据与评测结果

- **TIOBE 2026 年 9 月**：Python 以 17.76% 居首，C 以 10.28% 列第二，C++ 以 8.67% 列第三，Java 以 7.54% 列第四（[TIOBE 2026 年 9 月榜单](http://www.zaker.net/news/article_new.php?pk=6a9e2e2c8e9f0969d33c7ff0)）。
- **TIOBE 2026 年 7 月**：Rust 首次进入前 10；C 列第二（10.86%），C++ 以 9.12% 列第三，Java 8.03% 列第四（[TIOBE Index July 2026: Rust Enters Top 10](https://www.techrepublic.com/article/news-tiobe-july-2026-rust-enters-top-10/)）。
- **Linux 内核中的 Rust 状态**：官方内核文档仍将 Rust 支持描述为「实验性」，需通过 `CONFIG_RUST` 启用（[The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/translations/zh_CN/process/programming-language.html)）；但多家媒体报道称，2025 年底维护者峰会决定移除「实验性」标签，Linux 7.0（2026 年 4 月）中 Rust 驱动进入主线稳定分支（[Linux 7.0 Released: Rust Official](https://www.indiekings.com/2026/04/linux-70-released-rust-official-xfs.html)）。两方口径不同，以官方文档为准更稳妥。

## 趋势与争议

- **「修 C++」还是「换语言」**：WG21 一派主张以 profiles、加固、合约渐进提升安全性并保持向后兼容；监管与安全社群则倾向推动向 Rust 等内存安全语言迁移（[P3874R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3874r1.pdf)）。
- **迁移成本与既有资产**：C/C++ 承载了操作系统、数据库与海量遗留系统，整体重写的成本与风险巨大，「AI 自动翻译到 Rust」等设想仍停留在提案阶段（[NITRD 提案](https://files.nitrd.gov/90-fr-9088/Yaqub-Ali-AI-RFI-2025.pdf)）。
- **新语言的定位困境**：Carbon 仍处实验期，能否形成临界规模尚不确定；Zig 以不同哲学另辟蹊径，但生态与生态位仍在建设中（[Carbon docs](https://docs.carbon-lang.dev/)；[Zig Devlog](https://ziglang.org/devlog/2026/)）。
- **标准节奏争议**：C++ 每三年一版的节奏使重大安全能力分散在多轮标准中落地，社区对「改动是否足够快」存在持续讨论（[CppCon 2026 综述](https://isocpp.org/blog/cgal/P1280)）。

## 参考来源

- [CppCon 2026: Awaiters and Awaitables -- Mateusz Pusz](https://isocpp.org/blog/cgal/P1280)
- [Standard C++ Foundation — 标准化动态](https://isocpp.org/blog/rss/category/standardization)
- [C++26 – najważniejsze zmiany w języku](https://programistamag.pl/wp-content/uploads/downloads/Programista_121_czym_zachwyci_cpp26_a.pdf)
- [Core safety profiles for C++26 (P3081R2)](https://open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3081r2.pdf)
- [C++ Profiles: The Framework (P3589R1)](https://isocpp.org/files/papers/P3589R1.pdf)
- [Note to the C++ standards committee members (P3651R0)](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3651r0.pdf)
- [Should C++ be a memory-safe language? (P3874R1)](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3874r1.pdf)
- [Standard library hardening should not use the 'observe' semantic (P3878R1)](https://isocpp.org/files/papers/P3878R1.html)
- [Memory Safety Is Now a National Security Issue](https://www.aioapex.com/en/blog/memory-safety-is-now-a-national-security-issue-why-the-us-and-eu-want-developers-mq3ec9hn)
- [The 2026 Memory Safety Mandate](https://techlife.blog/posts/memory-safety-modernization/)
- [Why Everyone is Shifting from C/C++ to Rust](https://www.avidclan.com/blog/why-everyone-is-shifting-from-c-and-c-plus-to-rust)
- [Proposal: Leveraging AI to Translate Memory-Unsafe Languages into Rust (NITRD)](https://files.nitrd.gov/90-fr-9088/Yaqub-Ali-AI-RFI-2025.pdf)
- [Zig 0.15.1 Release Notes](https://ziglang.org/download/0.15.1/release-notes.html)
- [Zig 0.16.0 Release Notes](https://ziglang.org/download/0.16.0/release-notes.html)
- [Zig Releases（下载页）](https://ziglang.org/it-IT/download/)
- [Zig Devlog 2026](https://ziglang.org/devlog/2026/)
- [Carbon Language documentation](https://docs.carbon-lang.dev/)
- [Carbon Programming Language 2026: Google's Experimental Successor to C++](https://www.programming-helper.com/tech/carbon-programming-language-2026-google-experimental-cpp-successor)
- [Rust for Linux](https://rust-for-linux.com/print)
- [The Linux Kernel documentation — 程序设计语言](https://www.kernel.org/doc/html/latest/translations/zh_CN/process/programming-language.html)
- [Linux 7.0 Released: Rust Official, XFS Self-Healing & More](https://www.indiekings.com/2026/04/linux-70-released-rust-official-xfs.html)
- [TIOBE 2026 年 9 月编程语言排行榜](http://www.zaker.net/news/article_new.php?pk=6a9e2e2c8e9f0969d33c7ff0)
- [TIOBE Index July 2026: Rust Enters Top 10](https://www.techrepublic.com/article/news-tiobe-july-2026-rust-enters-top-10/)