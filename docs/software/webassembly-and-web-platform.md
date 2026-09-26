# WebAssembly 与 Web 平台

> 最后更新：2026-09-26 ｜ 领域：软件·平台与领域应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

WebAssembly（简称 Wasm）是一种可移植的二进制指令格式，最初为在浏览器中以接近原生速度运行高性能代码而设计，随后扩展到服务端、边缘计算、插件系统与嵌入式等场景。它以栈式虚拟机、线性内存模型和强类型静态校验为特征，可在不同硬件架构上高效执行（[WebAssembly: How It's Transforming Modern Web Development](https://arnav.au/2025/12/13/webassembly-is-reshaping-the-web/)）。

2025–2026 年，Wasm 生态的两条主线是**核心规范的能力扩张**（GC、尾调用、宽松 SIMD 等并入正式标准）与**组件模型（Component Model）/ WASI 的成熟**（异步原生化、可组合性、跨语言互操作）。下文分别展开。

## 最新进展（2025–2026）

- **Wasm 3.0 完成**：WebAssembly 官方于 2025 年 9 月 17 日发布「Wasm 3.0 Completed」，即核心标准新版本完成；该版本首次由新的 SpecTec 工具链产出规范文本，官方称其提高了规范可靠性，并已在多数主流浏览器中落地，Wasmtime 等独立引擎的支持也在推进中（[Wasm 3.0 Completed](https://webassembly.org/news/2025-09-17-wasm-3.0/)）。与此同时，核心规范的草案文本仍标注为 2.0 版本（Draft 2025-06-24），说明版本号口径存在并行，正文与规范文档的命名并不完全一致（[WebAssembly Specification Release 2.0 (Draft 2025-06-24)](https://webassembly.github.io/spec/core//_download/WebAssembly.pdf)）。
- **WASI 0.3.0 发布**：WASI Subgroup 投票通过并正式发布 WASI 0.3.0（2026 年 6 月 11 日），将此前位于 `wasi:io` 包中的异步能力下沉到组件模型本身，新增 `async func`、`stream`、`future` 等原生异步原语；Wasmtime 45 已运行候选版本，Wasmtime 46 默认启用 Component Model Async 并随附 WASI 0.3.0（[WASI 0.3 Launched](https://bytecodealliance.org/articles/WASI-0.3)）。
- **WASI 发布节奏**：WASI 0.3 补丁版每两个月在第二个周二发布；0.3.1（2026-08-11）已发布，0.3.2（2026-10-13）与 0.3.3（2026-12-08）为计划版本（[Roadmap](https://wasi.dev/roadmap/)）。WASI 0.3 被定义为「Stable, current」，0.2 为「Stable, superseded by 0.3」，0.1 为「Legacy」（[Releases](https://wasi.dev/releases/)）。
- **WasmGC 与尾调用进入 Baseline**：WasmGC（垃圾回收）与尾调用优化扩展自 2024 年 12 月 11 日起在三大浏览器引擎均已可用，成为 «Baseline Newly available» 特性（[Wasm GC and Wasm tail call optimizations are now Baseline Newly available](https://web.developers.google.cn/blog/wasmgc-wasm-tail-call-optimizations-baseline)）。
- **Web API 规范推进**：W3C 于 2025 年 10 月 15 日发布《WebAssembly Web API》候选推荐草案，定义 Wasm 与更广泛 Web 平台的集成方式（[WebAssembly Web API](https://www.w3.org/TR/2025/CRD-wasm-web-api-2-20251015/)）。
- **组件模型 1.0 路线**：Bytecode Alliance 提出组件模型走向稳定 1.0 的路线，在 2026 年 3 月巴塞罗那 Wasm I/O 上由 Luke Wagner 进一步阐述愿景；剩余工作规划在 WASI P3 发布之后，包括重构任务状态以便 Cranelift 优化掉同步适配器的开销（[The Road to Component Model 1.0](https://bytecodealliance.org/articles/the-road-to-component-model-1-0)）。

## 核心技术与关键概念

**WASI 版本谱系**：WASI 0.1 是受 POSIX 启发的模块级 API，运行时支持广泛；WASI 0.2 将 WASI 完全重建于组件模型与 WIT（WebAssembly Interface Type）接口描述语言之上，替换了 0.1 的类 C 的 WITX IDL，带来模块化、可虚拟化与跨语言互操作（[WASI 0.2](https://wasi.dev/releases/wasi-p2)）。WASI 0.3 则在此之上引入原生异步（[WASI 0.3](https://wasi.dev/releases/wasi-p3)）。

**组件模型与 WIT**：组件模型定义组件、接口与 world，引入 WIT 语言，规定组件与宿主之间的 canonical ABI，并提供组件的二进制与文本格式；它是 WASI Preview 2 系统接口的基础（[GitHub 组件模型 API 描述](https://raw.githubusercontent.com/api-evangelist/component-model/refs/heads/main/apis.yml)）。其核心价值在于：由一种语言（如 Rust）编译出的组件可与另一种语言（如 Go）编译的组件组合通信（[Releases](https://wasi.dev/releases/)）。

**核心语言扩展**：变更历史显示，尾调用扩展新增了 `return_call` 等控制指令；垃圾回收扩展引入了托管引用类型与新的堆类型形式（[Change History](https://webassembly.github.io/wide-arithmetic/core/appendix/changes.html)）。

**执行与内存模型**：Wasm 以紧凑二进制格式交付，加载与解析快于等价 JavaScript；其基于栈的虚拟机跨硬件高效执行；线性内存模型有助于避免传统 C/C++ 应用常见的缓冲区溢出漏洞，并遵循同源策略等 Web 安全标准（[WebAssembly: How It's Transforming Modern Web Development](https://arnav.au/2025/12/13/webassembly-is-reshaping-the-web/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Wasmtime**：组件模型的参考实现，支持运行实现 `wasi:cli/command` world 的组件、提供实现 `wasi:http/proxy` world 的服务，并可调用组件导出的函数（[Wasmtime](https://component-model.bytecodealliance.org/running-components/wasmtime.html)）。
- **Bytecode Alliance 生态实现**：包括 Wasmtime、Jco、wit-bindgen 语言绑定、cargo-component（Rust）、ComponentizeJS 与 Spin（Serverless Wasm），基本由 Bytecode Alliance 维护（[组件模型 API 描述](https://raw.githubusercontent.com/api-evangelist/component-model/refs/heads/main/apis.yml)）。
- **WasmEdge**：主打 AOT 编译器优化，官方称其为市场上最快的 WebAssembly 运行时之一，广泛用于边缘计算、汽车、Jamstack、Serverless、SaaS、服务网格乃至区块链应用（[Use Cases](https://wasmedge.org/docs/start/usage/use-cases/)）。据 2025 年 KubeCon NA 相关报道，WasmEdge 扩展了 GPU 支持（NVIDIA CUDA、AMD GPU、Apple Metal、Intel GPU 及专用 AI 处理器），并提供对 TensorRT、OpenVINO、Core ML 等推理引擎的多后端抽象（[WasmEdge at OSSummit Korea and KubeCon NA 2025](https://www.secondstate.io/articles/ossummit-korea-and-kubecon-na-2025/)）。
- **用户案例**：WasmEdge 用户名单中列出 ByteDance 用其运行服务网格代理与 sidecar 中的自定义逻辑、运行 Serverless 函数、以及作为 Ray 节点；Huawei Cloud 用于运行 Serverless 函数（[WasmEdge Users and Collaborators](https://wasmedge.org/docs/contribute/users/)）。

## 关键数据与评测结果（附来源）

- **与原生代码的差距**：一项使用 SPEC CPU 基准套件的评测显示，Wasm 目前比原生代码慢约 1.45–1.55 倍，差距归因于安全检查带来的指令开销与编译器代码生成次优；最关键的瓶颈常常是跨语言边界所需的数据编组（data marshaling）（[WebAssembly: A Systems-Level Analysis](https://uplatz.com/blog/webassembly-a-systems-level-analysis-of-performance-and-server-side-architectural-transformation/)）。
- **相对 JavaScript 的速度**：有资料援引 Mozilla 研究称，WebAssembly 可达到原生速度的约 95%，而 JavaScript 相对原生代码通常仅为 10–20%（[WebAssembly: How It's Transforming Modern Web Development](https://arnav.au/2025/12/13/webassembly-is-reshaping-the-web/)）。需注意上述数字为不同来源、不同基准口径下的结论，彼此并不直接可比。
- **场景化加速**：有行业博客给出的案例包括 4K 图像压缩由 800 ms 降至 78 ms；另一篇测度报告列出算法交易中移动平均计算由 JavaScript 150 ms 降至 Wasm 3 ms、复杂技术分析由 2.1 s 降至 45 ms（[Unlock WebGPU & WebAssembly](https://www.besthub.dev/articles/unlock-webgpu-webassembly-boost-3d-ai-and-video-performance-in-the-browser-dbdaf4910f38)、[WebAssembly : révolution du web performance 2025](https://aetherio.tech/articles/webassembly-revolution-performance-web-2025)）。此类数据来自第三方博客，口径与可复现性有限，仅作参考。
- **AR/VR 场景**：有研究指出，同一人脸识别算法以 Wasm 实现时的帧率约为 asm.js 版本的两倍、等价 JavaScript 算法的二十倍（[WebAssembly enables low latency interoperable AR/VR software](https://arxiv.org/pdf/2110.07128)）。

## 趋势与争议

**趋势**：一是「异步原生化」——WASI 0.3 把 async 从外部包下沉进组件模型，使跨语言异步组合成为标准能力；二是「组件模型 1.0」——社区目标是把组件模型稳定并形式化到 1.0，同时恢复同步适配器在引入组件模型异步之前的性能表现（[The Road to Component Model 1.0](https://bytecodealliance.org/articles/the-road-to-component-model-1-0)）；三是浏览器与服务端「双轨」——核心扩展（GC、尾调用）在浏览器进入 Baseline，而服务端依赖组件模型/WASI 推进。

**争议与分歧**：Wasm 的版本命名在「核心规范草案 2.0」与「Wasm 3.0 Completed」之间并存，容易造成混淆（[Wasm 3.0 Completed](https://webassembly.org/news/2025-09-17-wasm-3.0/)、[Spec 2.0 Draft](https://webassembly.github.io/spec/core//_download/WebAssembly.pdf)）；性能上，跨边界数据编组仍是主要瓶颈，Wasm 对 CPU 密集任务优势明显但对一般任务并非「万灵药」（[Systems-Level Analysis](https://uplatz.com/blog/webassembly-a-systems-level-analysis-of-performance-and-server-side-architectural-transformation/)）；此外 Wasm 相对原生仍有 1.45–1.55 倍差距，具体倍率随基准、引擎与优化程度而变，业界尚未形成统一定论。

## 参考来源

- [Wasm 3.0 Completed](https://webassembly.org/news/2025-09-17-wasm-3.0/)
- [WASI 0.3 Launched](https://bytecodealliance.org/articles/WASI-0.3)
- [WASI 0.3](https://wasi.dev/releases/wasi-p3)
- [WASI 0.2](https://wasi.dev/releases/wasi-p2)
- [WASI Releases](https://wasi.dev/releases/)
- [WASI Roadmap](https://wasi.dev/roadmap/)
- [The Road to Component Model 1.0](https://bytecodealliance.org/articles/the-road-to-component-model-1-0)
- [Wasmtime (Component Model docs)](https://component-model.bytecodealliance.org/running-components/wasmtime.html)
- [Wasm GC and Wasm tail call optimizations are now Baseline Newly available](https://web.developers.google.cn/blog/wasmgc-wasm-tail-call-optimizations-baseline)
- [WebAssembly Web API (W3C CR Draft 2025-10-15)](https://www.w3.org/TR/2025/CRD-wasm-web-api-2-20251015/)
- [WebAssembly Specification Release 2.0 (Draft 2025-06-24)](https://webassembly.github.io/spec/core//_download/WebAssembly.pdf)
- [WebAssembly Change History](https://webassembly.github.io/wide-arithmetic/core/appendix/changes.html)
- [WebAssembly: How It's Transforming Modern Web Development](https://arnav.au/2025/12/13/webassembly-is-reshaping-the-web/)
- [WebAssembly: A Systems-Level Analysis of Performance and Server-Side Architectural Transformation](https://uplatz.com/blog/webassembly-a-systems-level-analysis-of-performance-and-server-side-architectural-transformation/)
- [Components Model — API description](https://raw.githubusercontent.com/api-evangelist/component-model/refs/heads/main/apis.yml)
- [WasmEdge Use Cases](https://wasmedge.org/docs/start/usage/use-cases/)
- [WasmEdge Users and Collaborators](https://wasmedge.org/docs/contribute/users/)
- [WasmEdge at OSSummit Korea and KubeCon NA 2025](https://www.secondstate.io/articles/ossummit-korea-and-kubecon-na-2025/)
- [Unlock WebGPU & WebAssembly](https://www.besthub.dev/articles/unlock-webgpu-webassembly-boost-3d-ai-and-video-performance-in-the-browser-dbdaf4910f38)
- [WebAssembly : révolution du web performance 2025](https://aetherio.tech/articles/webassembly-revolution-performance-web-2025)
- [WebAssembly enables low latency interoperable AR/VR software](https://arxiv.org/pdf/2110.07128)