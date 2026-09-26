# RISC-V 与开放硬件

> 最后更新：2026-09-26 ｜ 领域：硬件 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

RISC-V 是一套开放、免专利费的精简指令集架构（ISA），任何人可自由实现与扩展，被称为芯片界的"通用标准"，被视为突破芯片生态壁垒、发展自主可控算力的重要路线之一（[中国科学院启动下一代开源芯片与系统研发（中国科学院计算技术研究所）](http://www.ict.ac.cn/xwgg/mtwz/202603/t20260328_8178765.html)）。2025–2026 年，随着 RVA23 标准的落地、AI 相关扩展的推进以及开源芯片项目（如"香山""如意"）的发布，RISC-V 正从嵌入式走向应用级与 AI 加速场景。

## 最新进展（2025–2026）

- **RVA23 从标准走向量产**：RVA23 Profile 于 2024 年 10 月 21 日批准，对应用级处理器强制要求向量扩展（RVV）与虚拟化（Hypervisor）扩展，被视为解决软件碎片化、给 OS 厂商提供稳定支持目标的关键（[RVA23: From Ratification to Real-World Readiness](https://riscstar.com/blog/rva23-from-ratification-to-real-world-readiness/)、[Pervasive AI — RISC-V International](https://riscv.org/industries/automotive/pervasive-ai/)）。RISC-V International 表示矩阵（matrix）扩展仍在研发中，厂商亦可通过自定义扩展针对特定负载调优（[Pervasive AI](https://riscv.org/industries/automotive/pervasive-ai/)）。
- **NVIDIA 表态支持 RVA23**：RISC-V International 报道称，NVIDIA 表示若没有 RVA23，"不会考虑将 CUDA 移植到 RISC-V"；Canonical 也已将其 RISC-V 版 Ubuntu 的开发全面转向 RVA23（[NVIDIA on RVA23 — RISC-V International](https://riscv.org/blog/nvidia-cuda-rva23/)）。
- **量产芯片落地**：进迭时空（SpacemiT）K3 被称创造多项 RISC-V 全球纪录——全球首颗符合 RVA23 标准量产芯片、首颗支持 RVV 1024bit 向量位宽、首颗支持 FP8 原生推理、首颗支持完整虚拟化（RVH 1.0、AIA、IOMMU）的 RISC-V 芯片（[从 RVA23 标准落地到机器人运控实战：进迭时空 K3 卡位 RISC-V 端侧 AI（电子工程专辑）](https://www.eet-china.com/news/202608139657.html)）。
- **中国开源根社区成形**：2026 年 3 月 26 日，在 2026 中关村论坛年会"RISC-V 生态科技论坛"上，中国科学院正式发布"香山"开源高性能 RISC-V 处理器系统与"如意"RISC-V 原生操作系统，并启动下一代芯片与操作系统的联合研发；"香山"同步推出全球首个开源片上互连网络 IP（[【科技日报】"香山"配"如意"（中国科学院）](http://www.cas.cn/cm/202603/t20260330_5105393.shtml)、[【新华社】中国科学院启动下一代开源芯片与系统研发（中科院计算所）](http://www.ict.ac.cn/xwgg/mtwz/202603/t20260328_8178765.html)、[中国科学院正式发布 RISC-V 生态建设重要成果（科技日报）](http://www.stdaily.com/web/gdxw/2026-03/27/content_493813.html)）。
- **面向云端的大核**：进迭时空发布第三代 RISC-V 处理器核 X200，基于北京开源芯片研究院主导的"香山"开源生态与昆明湖 V2 架构，瞄准云计算与大芯片（[AI Agent 热潮下，谁来支撑大算力？进迭时空发布第三代 RISC-V 处理器核 X200（中国日报网）](http://tech.chinadaily.com.cn/a/202605/09/WS69fee676a310942cc49ab703.html)）。

## 核心技术与关键概念

- **基础 ISA 与扩展**：RISC-V 采用模块化设计，基础 ISA 之上通过标准扩展（如向量扩展 V、虚拟化扩展 H）与自定义扩展组合出不同定位的处理器。
- **Profile（配置档）机制**：RISC-V International 通过 Profile 固定某类系统的必选扩展集合。RVA23 为应用级 64 位 Profile，强制向量与虚拟化扩展；RVB23 共享同一 64 位基础但将两者设为可选，以换取更小、更低功耗的硅片（[Pervasive AI](https://riscv.org/industries/automotive/pervasive-ai/)、[Workload-Specific Silicon — RISC-V International](https://riscv.org/industries/automotive/workload-specific-silicon/)）。
- **AI 加速扩展**：向量扩展 RVA23 中为必选，矩阵（matrix）扩展在研发中，此外允许自定义扩展针对 AI 负载定制（[Pervasive AI](https://riscv.org/industries/automotive/pervasive-ai/)）。
- **软件栈**：开源 RVV 实现（如 Saturn Vector Unit）提供符合 RVV 1.0 的硬件；社区推进面向 RISC-V 的 AI 编译器（Buddy Compiler）与软件栈（RuyiAI），并推动 PyTorch 等框架的 RISC-V 支持（[RISC-V и приложения ИИ](https://www.injoit.org/index.php/j1/article/download/2463/2087)、[2026 Board of Directors Elections — RISC-V International](https://riscv.org/elections/)）。
- **车载应用**：满足 RVA23 的芯片可运行 Linux 级系统（如 Automotive Grade Linux 或 Android），用于数字座舱与车内智能助手（[Workload-Specific Silicon](https://riscv.org/industries/automotive/workload-specific-silicon/)）。

## 代表性项目 / 公司 / 组织

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| 香山（XiangShan） | 开源处理器系统 | 中科院计算所牵头，含全球首个开源片上互连网络 IP |
| 如意（Ruyi） | 原生操作系统 | 中科院软件所开发，与"香山"配套 |
| 进迭时空 K3 / X200 | 商业芯片 / 处理器核 | K3 为 RVA23 量产芯片；X200 面向云计算 |
| RISC-V International | 标准组织 | 维护 ISA 与 Profile，2026 年进行董事会选举 |
| Canonical | 软件厂商 | 将 RISC-V 版 Ubuntu 开发全面转向 RVA23 |
| NVIDIA | 芯片厂商 | 表态 RVA23 是其考虑将 CUDA 移植到 RISC-V 的前提 |

## 关键数据与评测结果

- 中国创业公司 EVAS 以 RISC-V 架构融资 2.95 亿美元，估值达 22.1 亿美元，其定位包含"绕开出口管制"以减少对美国贸易监管的暴露，理由是开放指令集可被任何人免版税使用、美国难以像限制 NVIDIA GPU 那样对 RISC-V 施加出口管制（[China Chip Startup EVAS Raises $295M on RISC-V Architecture Built for Export-Control Bypass](https://www.techtimes.com/articles/327750/20260920/china-chip-startup-evas-raises-295m-risc-v-architecture-built-for-export-control-bypass.htm)）。
- RISC-V 国际董事会成员背景显示，社区正推进面向 RISC-V 的 AI 系统软件与编译器（Buddy Compiler）、RuyiAI 软件栈及 PyTorch 的 RISC-V 支持（[2026 Board of Directors Elections](https://riscv.org/elections/)）。

## 趋势与争议

1. **地缘政治与出口管制争议**：美国部分国会议员以国家安全为由，主张对与中国实体在 RISC-V 技术上的合作实施出口许可；由于 RISC-V 开放且免版税，难以像 GPU 那样直接管制，被批评者认为此类管制"打错了算盘"（[对 RISC-V 出口管制？美国政客打错了算盘（光明网）](http://m.toutiao.com/group/7293507471606432292/)）。同时，美国国会亦持续审视半导体出口管制的有效性，2026 年提出 H.R. 8287《Semiconductor Controls Effectiveness Act of 2026》，要求就出口管制对相关国家半导体与 AI 发展的影响提交报告（[H.R. 8287](https://www.govinfo.gov/content/pkg/BILLS-119hr8287ih/pdf/BILLS-119hr8287ih.pdf)）。
2. **碎片化 vs 标准化**：RVA23 被视为缓解软件碎片化的关键一步，但矩阵等 AI 相关扩展尚未定稿，扩展生态仍在演进（见上）。
3. **从嵌入式走向应用级与 AI 加速**：随着 RVA23 芯片量产与开源根社区成形，RISC-V 的应用边界正从 MCU、嵌入式拓展到云计算、车载与端侧 AI。

## 参考来源

- [中国科学院启动下一代开源芯片与系统研发（中国科学院计算技术研究所）](http://www.ict.ac.cn/xwgg/mtwz/202603/t20260328_8178765.html)
- [【科技日报】"香山"配"如意"，开辟开源芯片产业落地新路径（中国科学院）](http://www.cas.cn/cm/202603/t20260330_5105393.shtml)
- [中国科学院正式发布 RISC-V 生态建设重要成果（科技日报）](http://www.stdaily.com/web/gdxw/2026-03/27/content_493813.html)
- [十年，中国辟出一条开源芯片产业落地之路（光明网）](http://tech.gmw.cn/2026-03/27/content_38673321.htm)
- [AI Agent 热潮下，谁来支撑大算力？进迭时空发布第三代 RISC-V 处理器核 X200（中国日报网）](http://tech.chinadaily.com.cn/a/202605/09/WS69fee676a310942cc49ab703.html)
- [从 RVA23 标准落地到机器人运控实战：进迭时空 K3 卡位 RISC-V 端侧 AI（电子工程专辑）](https://www.eet-china.com/news/202608139657.html)
- [RVA23: From Ratification to Real-World Readiness](https://riscstar.com/blog/rva23-from-ratification-to-real-world-readiness/)
- [NVIDIA on RVA23: "We Wouldn't Have Considered Porting CUDA to RISC-V Without It"](https://riscv.org/blog/nvidia-cuda-rva23/)
- [Pervasive AI — RISC-V International](https://riscv.org/industries/automotive/pervasive-ai/)
- [Workload-Specific Silicon — RISC-V International](https://riscv.org/industries/automotive/workload-specific-silicon/)
- [2026 Board of Directors Elections — RISC-V International](https://riscv.org/elections/)
- [RISC-V и приложения Искусственного Интеллекта](https://www.injoit.org/index.php/j1/article/download/2463/2087)
- [RISC-V Momentum in Silicon Valley AI Compute 2026](https://www.stanfordtechreview.com/articles/risc-v-momentum-in-silicon-valley-ai-compute-2026)
- [China Chip Startup EVAS Raises $295M on RISC-V Architecture Built for Export-Control Bypass（Tech Times）](https://www.techtimes.com/articles/327750/20260920/china-chip-startup-evas-raises-295m-risc-v-architecture-built-for-export-control-bypass.htm)
- [对 RISC-V 出口管制？美国政客打错了算盘（光明网）](http://m.toutiao.com/group/7293507471606432292/)
- [H.R. 8287: Semiconductor Controls Effectiveness Act of 2026](https://www.govinfo.gov/content/pkg/BILLS-119hr8287ih/pdf/BILLS-119hr8287ih.pdf)