# 单仓与构建系统（Monorepo and Build Systems）

> 最后更新：2026-09-26 ｜ 领域：软件工程 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

单仓（monorepo）指把多个项目、服务、库放在同一个版本控制仓库中统一管理；构建系统则负责在这种规模下正确、增量、可缓存的构建与测试。单仓的优势在于共享依赖与协同变更（coordinated changes），但对「各自独立、技术栈异构」的团队未必合适，因此工具选择需要结合团队规模、项目复杂度与语言需求（[Monorepo in 2026: Turborepo vs Nx vs Bazel for Modern Development Teams](https://daily.dev/blog/monorepo-turborepo-vs-nx-vs-bazel-modern-development-teams)）。

规模化构建的核心机制是把任务建模为依赖图（DAG），据此确定执行顺序、识别可并行任务，并以内容寻址的方式做缓存与复用（[Incremental Build Systems for Large Codebases](https://awesome-repositories.com/q/incremental-build-system-for-large-codebases)）。增量构建带来的收益往往大于干净构建：把一次构建从 8 分钟降到 30 秒以内，会实质改变开发者的工作方式与反馈回路（[The Build System Wars — Bazel, Buck2, Pants, and Whether Your Monorepo Actually Needs One](https://tianpan.co/forum/t/the-build-system-wars-bazel-buck2-pants-and-whether-your-monorepo-actually-needs-one/615)）。

## 最新进展（2025–2026）

**1. Bazel 完成 WORKSPACE → Bzlmod 的迁移。** 官方路线图说明：Bazel 8 默认禁用 WORKSPACE 支持（仍可用 `--enable_workspace` 开启），Bazel 9 将移除 WORKSPACE 支持（[Bazel roadmap](https://bazel.build/versions/8.2.1/about/roadmap)）。Bzlmod 是新一代外部依赖管理系统，自动解析传递依赖，并以中央注册表（Bazel Central Registry）分发规则，是使用 Bazel 未来版本的必经迁移步骤（[Guía de migración de Bzlmod](https://bazel.google.cn/external/migration?hl=es)）。第三方整理称 Bazel 9（2026 年 1 月，LTS）已完全移除 `WORKSPACE`，外部依赖只能在 `MODULE.bazel` 中声明并自 BCR 解析（[Monorepos: Tooling & Build Systems](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-tooling/)）。

**2. 远程缓存/远程执行成为 CI 提速的主要来源。** 一项对 Bazel、Buck2、Pants 的对比评估显示：启用远程缓存后，各工具带来的 CI 用时下降幅度大致相当（Bazel −62%、Buck2 −65%、Pants −60%）——也就是说「远程缓存使 CI 时间减少约 60%，与所选工具无关」（[tianpan.co](https://tianpan.co/forum/t/the-build-system-wars-bazel-buck2-pants-and-whether-your-monorepo-actually-needs-one/615)）。Bazel 的远程执行通过 gRPC 协议在独立平台上执行 action，开源实现包括 bazel-buildfarm（[Adapting Bazel Rules for Remote Execution](https://bazel.build/remote/rules?hl=en)）。

**3. 缓存正确性成为竞争焦点。** Nx 采用按任务缓存、输入由插件与可组合的 `namedInputs` 推导，并以 Nx Cloud 的任务沙箱（task sandboxing）暴露未声明的读写，可选严格模式使任务失败；差异在于生效时机——Bazel 默认在每个 action 上强制执行沙箱，而 Nx 的沙箱是可选的（[Nx vs Bazel](https://nx.dev/docs/guides/comparisons/nx-vs-bazel)）。

**4. AI 集成进入构建工具路线图。** 2026 年的对比文章提到 Nx 正朝「面向自主 AI 智能体的基础设施」方向发展，计划在 2026 年第一季度推出供 IDE 集成的 MCP server、用于管理 LLM 上下文的 code mode，以及面向迁移与代码生成的专用智能体；Turborepo 尚未公布直接的 AI 集成（[Turborepo vs Nx в 2026](https://devtoolswatch.com/ru/turborepo-vs-nx-2026)）。

## 核心技术与关键概念

- **依赖图与受影响范围（affected）**：Nx 与 Turborepo 自动推导依赖图并提供 `affected` / `--filter` 能力；Bazel 使用显式的 BUILD 文件描述依赖（[Self-Hosted Monorepo Build Systems: Nx vs Turborepo vs Bazel Compared](https://www.pistack.xyz/posts/2026-06-16-self-hosted-monorepo-build-systems-nx-turborepo-bazel/)）。
- **远程缓存 vs 分布式执行**：远程缓存复用他人已产出的结果；分布式执行把 action 派发到执行农场。Nx 提供 Nx Agents，Turborepo 依赖 Vercel Remote Cache，Bazel 可对接任意的远程缓存/执行后端（[pistack.xyz](https://www.pistack.xyz/posts/2026-06-16-self-hosted-monorepo-build-systems-nx-turborepo-bazel/)）。
- **早期截断（early cutoff）**：Bazel 的 action key 使用依赖的「输出摘要」而非其 key，因此当上游改动（例如仅改注释）对编译产物字节无影响时，下游 action 仍能命中缓存；该机制要求构建产物可复现（[Monorepos: Scaling & Engineering](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-scaling/)）。
- **密封性（hermeticity）与可复现构建**：Bazel 强调密封构建环境；Buck2 同样采用规则化、密封构建，并用类 Starlark 语言描述（[Bazel alternatives for teams that want reproducible builds](https://www.codeables.dev/article/bazel-alternatives-for-teams-that-want-reproducible-builds-and)）。
- **缓存默认行为差异**：Turborepo 对注册的任务默认开启缓存，可用 `cache: false` 关闭（如 `dev` 任务），并且仅在任务声明了输出时才存储文件产物；Nx 需要更少的任务配置即可获得更深层的缓存能力（[Nx vs Turborepo](https://nx.dev/docs/guides/comparisons/nx-vs-turborepo)）。
- **可逆性作为选型准则**：有观点建议从「最可逆」的一步开始——先采用 workspaces + Turborepo；相较之下，Bazel/Buck2/Pants 需要自建并保障远程缓存与执行农场，学习曲线陡峭且切换成本高、可逆性低（[andrewaltimit.github.io](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-tooling/)）。
- **集中式依赖版本管理**：Nx 22 支持 pnpm catalogs，提供集中定义与引用依赖版本的机制，以缓解大型单仓中同一包版本漂移的问题（[Nx 22 Release: Expanding the build platform](https://nx.dev/blog/nx-22-release)）。
- **多语言支持方式**：Bazel 通过 rule sets 支持 Go、Java/Kotlin、C++、Python、JS/TS、Rust 等多种语言；相比之下 Nx 与 Turborepo 的优势集中在 JavaScript/TypeScript 世界（[Monorepos: Tooling & Build Systems](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-tooling/)、[daily.dev](https://daily.dev/blog/monorepo-turborepo-vs-nx-vs-bazel-modern-development-teams)）。
- **选型的三维矩阵**：可运维面（是否需要自建并保障远程缓存/执行农场）、学习曲线（package.json 脚本 / 工具自有项目模型 / Starlark 与密封性与工具链规则）、可逆性（高 / 中 / 低）是区分「workspaces + Turborepo」「Nx/moon/Rush」「Bazel/Buck2/Pants」三档方案的主要维度（[andrewaltimit.github.io](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-tooling/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

| 工具 | 定位 | 官方/来源链接 |
| --- | --- | --- |
| Bazel | 多语言、密封、可远程执行的构建系统（源自 Google Blaze） | [bazel.build](https://bazel.build/remote/rules?hl=en) |
| Nx | JS/TS 优先、支持多语言的单仓任务图与缓存平台 | [nx.dev](https://nx.dev/docs/guides/comparisons/nx-vs-turborepo) |
| Turborepo | 轻量任务编排与缓存（Vercel） | [nx.dev 对比页](https://nx.dev/docs/guides/comparisons/nx-vs-turborepo) |
| Buck2 | Meta 开源的下一代构建系统 | [codeables.dev](https://www.codeables.dev/article/bazel-alternatives-for-teams-that-want-reproducible-builds-and) |
| Pants | 多语言单仓构建与缓存 | [tianpan.co](https://tianpan.co/forum/t/the-build-system-wars-bazel-buck2-pants-and-whether-your-monorepo-actually-needs-one/615) |
| bazel-buildfarm | 开源分布式远程执行平台 | [bazel.build](https://bazel.build/remote/rules?hl=en) |

## 关键数据与评测结果（附来源）

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 远程缓存带来的 CI 用时下降（Bazel / Buck2 / Pants） | −62% / −65% / −60% | [tianpan.co](https://tianpan.co/forum/t/the-build-system-wars-bazel-buck2-pants-and-whether-your-monorepo-actually-needs-one/615) |
| 增量构建改善示例 | 8 分钟 → 30 秒以内 | [tianpan.co](https://tianpan.co/forum/t/the-build-system-wars-bazel-buck2-pants-and-whether-your-monorepo-actually-needs-one/615) |
| Google 主干仓库规模 | 约 20 亿行代码、约 10 亿个文件、每天约 40,000 次提交、25,000+ 工程师 | [Decoding Monorepos 2026: Tools and CI/CD](https://sesamedisk.com/monorepo-tools-ci-cd-2026/) |
| Google3 仓库规模 | 超过 86 TB、约 20 亿行代码 | [Monorepos vs Polyrepos](https://esb1995.com/en/courses/devops-engineering/lessons/VG3aJYQr) |
| Google 单仓源码文件数 | 超过 900 万个源文件（内部构建系统名为 Blaze） | [How Does Google Keep a Monorepo With Billions of Lines Maintainable?](https://www.mrcomputerscience.com/how-does-google-keep-a-monorepo-with-billions-of-lines-maintainable/) |
| Bazel 9 的 WORKSPACE 移除 | 完全移除，改用 `MODULE.bazel`（Bzlmod） | [andrewaltimit.github.io](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-tooling/) |

关于 Google 单仓规模的公开数字口径不一（文件数从「约 10 亿个文件」到「超过 900 万个源文件」），差异源于是否把生成物、测试数据等计入统计，此处并列呈现。

## 趋势与争议

- **单仓 vs 多仓**：单仓在共享依赖与协同变更上有优势，但可能不适合高度自治的团队与异构技术栈；是否采用应先判断组织协作模式（[daily.dev](https://daily.dev/blog/monorepo-turborepo-vs-nx-vs-bazel-modern-development-teams)）。
- **是否真的需要 Bazel 级工具**：评估文章指出「远程缓存带来的约 60% CI 提速与工具无关」，因此引入 Bazel 的收益未必来自其独有机制，而更多来自「有远程缓存」这件事本身；同时 Bazel 的学习曲线与不可逆性构成显著成本（[tianpan.co](https://tianpan.co/forum/t/the-build-system-wars-bazel-buck2-pants-and-whether-your-monorepo-actually-needs-one/615)、[andrewaltimit.github.io](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-tooling/)）。
- **密封性的强制执行时机**：Bazel 默认对每个 action 强制，Nx 为可选沙箱；严格性强可换来缓存正确性，但会增加配置与调试负担（[Nx vs Bazel](https://nx.dev/docs/guides/comparisons/nx-vs-bazel)）。
- **迁移成本**：Bzlmod 迁移被官方描述为「使用未来 Bazel 版本的必经步骤」，并建议使用迁移工具辅助；对作为他人依赖的项目，迁移还会解锁下游项目的迁移（[bazel.google.cn](https://bazel.google.cn/external/migration?hl=es)）。
- **AI 与构建工具的融合**：构建工具开始向上延伸到「为 AI 智能体提供上下文与迁移能力」，但其实际收益目前缺少公开的量化评测（[devtoolswatch.com](https://devtoolswatch.com/ru/turborepo-vs-nx-2026)）。

## 参考来源

1. [Self-Hosted Monorepo Build Systems: Nx vs Turborepo vs Bazel Compared](https://www.pistack.xyz/posts/2026-06-16-self-hosted-monorepo-build-systems-nx-turborepo-bazel/)
2. [Nx vs Turborepo](https://nx.dev/docs/guides/comparisons/nx-vs-turborepo)
3. [Nx vs Turborepo（adopting-nx 指南）](https://nx.dev/docs/guides/adopting-nx/nx-vs-turborepo)
4. [Nx vs Turborepo（KB）](https://nx.dev/docs/kb/nx-vs-turborepo)
5. [Nx vs Bazel](https://nx.dev/docs/guides/comparisons/nx-vs-bazel)
6. [Monorepo in 2026: Turborepo vs Nx vs Bazel for Modern Development Teams](https://daily.dev/blog/monorepo-turborepo-vs-nx-vs-bazel-modern-development-teams)
7. [Nx 22 Release: Expanding the build platform](https://nx.dev/blog/nx-22-release)
8. [Turborepo vs Nx в 2026: какой инструмент для монорепо выбрать](https://devtoolswatch.com/ru/turborepo-vs-nx-2026)
9. [Monorepos: Tooling & Build Systems](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-tooling/)
10. [Monorepos: Scaling & Engineering](https://andrewaltimit.github.io/Documentation/docs/advanced/monorepo-scaling/)
11. [Bazel roadmap](https://bazel.build/versions/8.2.1/about/roadmap)
12. [Guía de migración de Bzlmod](https://bazel.google.cn/external/migration?hl=es)
13. [Adapting Bazel Rules for Remote Execution](https://bazel.build/remote/rules?hl=en)
14. [The Build System Wars — Bazel, Buck2, Pants, and Whether Your Monorepo Actually Needs One](https://tianpan.co/forum/t/the-build-system-wars-bazel-buck2-pants-and-whether-your-monorepo-actually-needs-one/615)
15. [Incremental Build Systems for Large Codebases](https://awesome-repositories.com/q/incremental-build-system-for-large-codebases)
16. [Bazel alternatives for teams that want reproducible builds and caching without Bazel-level complexity](https://www.codeables.dev/article/bazel-alternatives-for-teams-that-want-reproducible-builds-and)
17. [Decoding Monorepos 2026: Tools and CI/CD](https://sesamedisk.com/monorepo-tools-ci-cd-2026/)
18. [Monorepos vs Polyrepos](https://esb1995.com/en/courses/devops-engineering/lessons/VG3aJYQr)
19. [How Does Google Keep a Monorepo With Billions of Lines Maintainable?](https://www.mrcomputerscience.com/how-does-google-keep-a-monorepo-with-billions-of-lines-maintainable/)