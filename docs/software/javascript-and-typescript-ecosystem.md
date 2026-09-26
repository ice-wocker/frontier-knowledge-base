# JavaScript 与 TypeScript 生态

> 最后更新：2026-09-26 ｜ 领域：软件·语言与运行时 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

JavaScript（正式标准为 ECMAScript）是 Web 平台的通用语言，也是全球使用率最高的编程语言；TypeScript 在其之上增加静态类型系统，已成为现代前端与 Node.js 后端开发的行业标准。生态的核心议题包括：标准演进（TC39 提案流程）、模块系统（ESM 与 CommonJS 的互操作）、运行时竞争（Node.js、Deno、Bun）、包管理与构建工具链。2025–2026 年最重大的事件是 TypeScript 编译器被整体改用 Go 重写为原生二进制，使大型项目全量构建提速约 8–12 倍（[Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)）。

## 最新进展（2025–2026）

1. **TypeScript 7.0（2026-07-08 发布）。** 微软将编译器与工具链从 TypeScript/Node.js 实现迁移为 Go 编写的原生二进制，在保持结构、逻辑与结果兼容的前提下引入原生代码速度与共享内存多线程，常见提速 8–12 倍（[Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)）。该原生预览（`@typescript/native-preview`、`tsgo`）此前已通过 npm 与 VS Code 插件形式开放（[Announcing TypeScript Native Previews](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)）。Visual Studio 2026 的 Insiders 版本已默认启用 TypeScript 7 Beta（[TypeScript 7 Beta Now Enabled by Default](https://devblogs.microsoft.com/visualstudio/typescript-7-beta-now-enabled-by-default-in-visual-studio-2026-18-6-insiders-3/)）。

2. **TypeScript 7 的兼容性变化。** 官方在《Progress on TypeScript 7 – December 2025》中说明，JavaScript 类型检查（部分依赖 JSDoc 注解）被从头重写；为简化内部实现，削减了部分复杂或较少使用的模式支持，例如 TypeScript 7.0 不再识别 `@enum` 相关模式（[Progress on TypeScript 7 – December 2025](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)）。

3. **Node.js 版本演进。** Node.js 24（Current 阶段采用 V8 13.6）进入 LTS（[Node.js 24.0.0](https://nodejs.org/uk/blog/release/v24.0.0)）；24.x 持续发布安全补丁，如 24.17.0（2026-06-18）与 24.21.0（2026-09-08）（[Node.js 24.17.0 (LTS)](https://nodejs.org/zh-tw/blog/release/v24.17.0)、[Node.js 24.21.0 (LTS)](https://nodejs.org/uk/blog/release/v24.21.0)）。Node.js 25（2025）升级 V8 至 14.1，带来 `JSON.stringify` 性能改进与内置 `Uint8Array` 的 base64/hex 转换，并扩展权限模型（新增 `--allow-net` 等）（[Node.js 25.0.0](https://nodejs.org/pt-br/blog/release/v25.0.0)）。

4. **Node.js 26。** Node.js 26 默认启用 Temporal API，升级 V8 至 14.6、Undici 至 8.0，并包含若干弃用与移除（[Node.js 26.0.0](https://nodejs.org/zh-cn/blog/release/v26.0.0)）；26.1.0 引入实验性 `node:ffi` 模块，用于从 JavaScript 加载动态库并调用原生符号（[Node.js 26.1.0](https://nodejs.org/en/blog/release/v26.1.0)）。此外，Node.js 自 v27 起将版本号与首次 Current 发布的日历年份对齐（[Trip report: Node.js collaboration summit 2026 London](https://nodejs.org/fr/blog/events/collab-summit-2026-london)）。

5. **原生 TypeScript 支持。** Node.js 默认直接执行仅包含「可擦除（erasable）」TypeScript 语法的文件，将类型语法替换为空白且不做类型检查，可用 `--no-strip-types` 关闭；Node 会忽略 `tsconfig.json`（[Modules: TypeScript](https://nodejs.org/download/release/latest-v26.x/docs/api/typescript.html)）。`--experimental-strip-types` 在 Node 24 稳定，`require(esm)` 互操作同样在 v24 稳定（[Node.js vs Bun vs Deno 2 in 2026](https://dev.to/moksh/nodejs-vs-bun-vs-deno-2-in-2026-which-javascript-runtime-should-you-actually-use-260e)）。

6. **运行时竞争。** 第三方评测称 Bun 在 2026 年已达到约 95% 的 npm 生态兼容度，剩余约 5% 主要是原生 C++ 插件（如 `sharp`、`node-canvas` 存在兼容毛刺）（[Bun vs Deno vs Node.js: which JavaScript runtime actually wins in 2026?](https://botmonster.com/web-dev/bun-vs-deno-vs-nodejs-javascript-runtime-2026/)）；其安装速度比 npm 快 10–25 倍、比 pnpm 快 3–5 倍，Deno 2 已实现 npm 兼容（`deno run npm:express`）（[Bun vs Deno 2 vs Node 22: JavaScript Runtimes in 2026](https://www.pkgpulse.com/blog/bun-vs-deno-2-vs-node-22-javascript-runtimes-2026)）。Deno 亦集成了 Go 编写的原生 TypeScript 编译器（tsgo），在理解 Deno 模块解析的前提下比 `tsc` 快约 10 倍（[Deno 文档：TypeScript](https://deno.zhcndoc.com/runtime/fundamentals/typescript.md)）。

## 核心技术与关键概念

- **ECMAScript 与 TC39。** 标准由 TC39 通过六阶段流程推进，每两个月开会评审提案（[TC39 — Specifying JavaScript](https://tc39.es/)）。处于 Stage 3 的提案包括正则表达式缓冲边界等（[Regular Expression Buffer Boundaries for ECMAScript](https://tc39.es/proposal-regexp-buffer-boundaries/)）。
- **模块系统。** ESM（`import`/`export`）与 CommonJS（`require`）并存；`require(esm)` 互操作在 Node 24 稳定，缓解长期的双模块摩擦（[Node.js vs Bun vs Deno 2 in 2026](https://dev.to/moksh/nodejs-vs-bun-vs-deno-2-in-2026-which-javascript-runtime-should-you-actually-use-260e)）。
- **TypeScript 类型系统。** 结构化类型、泛型、条件类型与类型推断；编译期做类型检查、运行时擦除类型。
- **类型擦除（type stripping）。** 仅支持「可擦除语法」——枚举、命名空间等需要代码生成的语法不被原生运行时接受，这使 TypeScript 的「可移植性」成为焦点（[Modules: TypeScript](https://nodejs.org/download/release/latest-v26.x/docs/api/typescript.html)）。
- **引擎。** Node.js/Deno 基于 V8，Bun 基于 JavaScriptCore；Temporal API 等新标准逐步进入默认（[Node.js 26.0.0](https://nodejs.org/zh-cn/blog/release/v26.0.0)）。
- **工具链。** `tsc`/`tsgo` 做类型检查，esbuild/SWC/Vite 做转译与打包，包管理由 npm/pnpm/yarn/Bun 竞争。

## 代表性项目 / 公司 / 产品（附官方链接）

- TypeScript — [typescriptlang.org](https://www.typescriptlang.org/)
- Node.js — [nodejs.org](https://nodejs.org/)
- Deno — [deno.com](https://deno.com/)
- Bun — [bun.sh](https://bun.sh/)
- TC39（ECMAScript 标准）— [tc39.es](https://tc39.es/)
- npm — [npmjs.com](https://www.npmjs.com/)

## 关键数据与评测结果（附来源）

- 2025 年 Stack Overflow 开发者调查显示，JavaScript 使用率约 66%，HTML/CSS 约 61.9%，TypeScript 约 43.6%（TypeScript 已成为 Web 领域的事实标准）（[Technology](https://survey.stackoverflow.co/2025/technology)）。
- TypeScript 7 性能：官方称提速通常在 8–12 倍区间，Visual Studio 团队称大型代码库编译时间改进最高可达 10 倍并显著降低内存占用（[Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)、[TypeScript 7 Beta Enabled by Default](https://devblogs.microsoft.com/visualstudio/typescript-7-beta-now-enabled-by-default-in-visual-studio-2026-18-6-insiders-3/)）。
- 包安装速度（第三方评测口径）：Bun 比 npm 快 10–25 倍、比 pnpm 快 3–5 倍（[Bun vs Deno 2 vs Node 22](https://www.pkgpulse.com/blog/bun-vs-deno-2-vs-node-22-javascript-runtimes-2026)）。

## 趋势与争议

- **原生重写的兼容性风险。** TypeScript 7 削减部分 JSDoc 与特殊模式支持（如不再识别 `@enum`），对依赖这些模式的旧代码库构成迁移风险（[Progress on TypeScript 7 – December 2025](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)）。
- **类型检查与转译分离。** 原生运行时只做类型擦除、不做类型检查，工具链因此趋向「转译器 + 独立类型检查器」的分工（[Modules: TypeScript](https://nodejs.org/download/release/latest-v26.x/docs/api/typescript.html)）。
- **运行时竞争与生态兼容。** Bun/Deno 以速度与「内置一切」争夺市场，但原生插件兼容度仍是短板（[Bun vs Deno vs Node.js](https://botmonster.com/web-dev/bun-vs-deno-vs-nodejs-javascript-runtime-2026/)）。
- **发布与维护可持续性。** Node.js 将版本号与年份对齐，官方称此举反映志愿者维护现状并旨在保持项目长期可持续（[Trip report: Node.js collaboration summit 2026 London](https://nodejs.org/fr/blog/events/collab-summit-2026-london)）。
- **CSS/构建生态的边界扩展。** TC39 对类成员访问修饰等提案的讨论（如轻量受保护字段）显示语言层仍在吸纳工程实践需求（[TC39 Discourse](https://es.discourse.group/latest)）。

## 参考来源

1. [Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)
2. [Announcing TypeScript Native Previews](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)
3. [Progress on TypeScript 7 – December 2025](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/)
4. [TypeScript 7 Beta Now Enabled by Default in Visual Studio 2026 18.6 Insiders 3](https://devblogs.microsoft.com/visualstudio/typescript-7-beta-now-enabled-by-default-in-visual-studio-2026-18-6-insiders-3/)
5. [Node.js 24.0.0 (Current)](https://nodejs.org/uk/blog/release/v24.0.0)
6. [Node.js 24.17.0 (LTS)](https://nodejs.org/zh-tw/blog/release/v24.17.0)
7. [Node.js 24.21.0 (LTS)](https://nodejs.org/uk/blog/release/v24.21.0)
8. [Node.js 25.0.0 (Current)](https://nodejs.org/pt-br/blog/release/v25.0.0)
9. [Node.js 26.0.0 (Current)](https://nodejs.org/zh-cn/blog/release/v26.0.0)
10. [Node.js 26.1.0 (Current)](https://nodejs.org/en/blog/release/v26.1.0)
11. [Modules: TypeScript（Node.js 文档）](https://nodejs.org/download/release/latest-v26.x/docs/api/typescript.html)
12. [Trip report: Node.js collaboration summit (2026 London)](https://nodejs.org/fr/blog/events/collab-summit-2026-london)
13. [Bun vs Deno vs Node.js: which JavaScript runtime actually wins in 2026?](https://botmonster.com/web-dev/bun-vs-deno-vs-nodejs-javascript-runtime-2026/)
14. [Bun vs Deno 2 vs Node 22: JavaScript Runtimes in 2026](https://www.pkgpulse.com/blog/bun-vs-deno-2-vs-node-22-javascript-runtimes-2026)
15. [Deno 文档：TypeScript](https://deno.zhcndoc.com/runtime/fundamentals/typescript.md)
16. [Node.js vs Bun vs Deno 2 in 2026](https://dev.to/moksh/nodejs-vs-bun-vs-deno-2-in-2026-which-javascript-runtime-should-you-actually-use-260e)
17. [TC39 — Specifying JavaScript](https://tc39.es/)
18. [Regular Expression Buffer Boundaries for ECMAScript](https://tc39.es/proposal-regexp-buffer-boundaries/)
19. [TC39 Discourse — Latest topics](https://es.discourse.group/latest)
20. [Stack Overflow Developer Survey 2025 — Technology](https://survey.stackoverflow.co/2025/technology)