# 芯片设计与 EDA

> 最后更新：2026-09-26 ｜ 领域：硬件·芯片与设计 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

一颗现代数字芯片从需求到可制造版图，典型流程为：架构定义 → RTL 设计（Verilog/SystemVerilog/VHDL）→ 功能验证 → 逻辑综合 → DFT（可测性设计）→ 布局布线（Place & Route）→ 签核（时序 STA、DRC、LVS、EM/IR）→ GDSII 交付 → 流片（tapeout）。全流程高度依赖电子设计自动化（EDA，Electronic Design Automation）工具，EDA 因此被视为集成电路产业链的战略基础支柱（[e公司：上市公司资讯第一平台](https://egs.stcn.com/quotation/stock-info/sh688206.html)）。

除工具外，可复用 IP（接口、CPU 核、SRAM 编译器）、工艺设计套件（PDK）与良率模型共同构成设计生态。随着制程微缩成本失控与 AI 芯片面积膨胀，Chiplet（芯粒）异构集成与器件间互连标准 UCIe 成为设计方法学的重要演进方向。

## 最新进展（2025–2026）

**市场高度集中且进一步集中。** SEMI 相关材料显示，EDA"三大厂"占行业收入约 90%，其中 Cadence-Synopsys Classic 在 2025 年约占 73%，相较 2020 年提升 6 个百分点、相较 2015 年提升 9 个百分点（[The State of EDA: A View from Wall Street](https://www.semi.org/sites/semi.org/files/2026-09/DAC%20presentation%20(July%202026)%207%20(1).pdf)）。不同机构口径有差异：有报告按 2025 年收入计，Synopsys 15.33%、Cadence 14.05%、Siemens 12.14%（[Electronic Design Automation (EDA) Market Report 2026](https://www.thebusinessresearchcompany.com/report/electronic-design-automation-eda-global-market-report)）；另有机构认为 Synopsys 与 Cadence 在 2025 年合计约 62%（[AI And HPC EDA Tools Market](https://www.mordorintelligence.com/industry-reports/ai-and-hpc-eda-tools-market)）；还有口径给出 Synopsys 约 32%、Cadence 约 30%、Siemens EDA 约 13%、合计约 75%（[Synopsys（checkthat.ai）](https://checkthat.ai/brands/synopsys)）。引用时必须注明统计口径与年份。

**并购重塑竞争格局。** Synopsys 于 2025 年完成对 Ansys 的 350 亿美元收购，把热、电磁、机械求解器打包进 3D-IC 签核流程；Keysight 随后收购被剥离的光子学与低功耗资产以扩展 PathWave 平台（[AI And HPC EDA Tools Market](https://www.mordorintelligence.com/industry-reports/ai-and-hpc-eda-tools-market)）。

**AI 进入设计闭环。** Synopsys 的 DSO.ai 用强化学习在超大解空间中自主搜索功耗/性能/面积（PPA）最优解，已与 Fusion Compiler 原生集成；Synopsys.ai Copilot 生成式 AI 能力于 2025 年 9 月扩展到领先设计解决方案，用于缩短开发周期（[What is AI-Driven Chip Design?](https://www.synopsys.com/glossary/what-is-ai-driven-chip-design.html)、[Synopsys 宣布扩展 AI 能力](https://www.synopsys.com/ko-kr/korean/press-releases/synopsys-announces-expanding-ai-capabilities.html)）。Cadence Cerebrus 以迁移学习见长，可把 7nm 项目学到的优化策略迁移到 5nm 新项目加速收敛；Google AlphaChip 用基于边的图神经网络做宏单元布局，证明了学习型方法可以超越人工专家（[The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design](https://arxiv.org/pdf/2512.23189v1)）。

**验证向"软硬件可变"演进。** 硬件辅助验证（HAV，含仿真加速与 FPGA 原型）已成为 AI 时代芯片设计的关键环节；Synopsys 提出"软件定义的硬件辅助验证"，并引入可在仿真加速与原型之间重配置的"EP-Ready"硬件（[From Future Vision To Running Hardware: Verification At DAC 2026](https://semiengineering.com/from-future-vision-to-running-hardware-verification-at-dac-2026/)、[Software-Defined Hardware-Assisted Verification](https://www.synopsys.com/blogs/chip-design/software-defined-hardware-assisted-verification.html)）。业界判断，仿真对今天最大的设计已不再充分，仿真加速与 FPGA 原型成为主流手段（[ASIC Verification in 2026: Key Challenges and Industry Trends](https://www.asicpro.com/2026/06/30/asic-verification-challenges-2026/)）。有市场研究称，面向 RISC-V 的仿真加速占 2026 年该市场收入的 22%（[Semiconductor Emulators Market](https://www.intelmarketresearch.com/semiconductor-emulators-market-21539)）。

**Chiplet 标准快速迭代。** UCIe（Universal Chiplet Interconnect Express）在三代内完成从 1.0 到 3.0 的演进，其 PPA 已可对标许多定制 die-to-die 实现（[The Growing Chiplet Ecosystem](https://www.uciexpress.org/post/the-growing-chiplet-ecosystem-collaboration-innovation-and-the-next-wave-of-ucie-adoption)）。UCIe 3.0 规范于 2025 年 8 月发布，把 UCIe-S 与 UCIe-A 的数据率翻倍到 48/64 GT/s（[UCIe Webinars](https://www.uciexpress.org/webinars)）。UCIe 2.0 引入可选的可管理性能力与 UCIe DFx 架构（UDA），在每个 chiplet 内建立用于测试、遥测与调试的管理网络（[UCIe Specifications](https://www.uciexpress.org/specifications)）；同时标准化了采用混合键合的 UCIe-3D，凸点间距由 9µm 向小于 1µm 演进（[Introducing the UCIe 3.0 Specification](https://www.uciexpress.org/_files/ugd/0c1418_b4744fe368c94e3e9c7eaa13ead632bf.pdf)）。

**地缘政治直接作用于 EDA。** 2025 年 5 月美国 BIS 一度要求 EDA 出口许可，同年 7 月解除限制，Synopsys、Cadence、Siemens EDA 确认恢复对中国客户的销售与支持（[US Lifts EDA Software Export Restrictions to China](https://www.axtekic.com/news/u.s.-lifts-eda-software-export-restrictions-to-china.html)、[Key chip firms say US export ban lifted](https://www.chinadailyasia.com/upload/main/pdf/2025/07/04/d2e8647cdb726b2a194ee476a35e8caa.pdf)）。2026 年 7 月 1 日起，BIS 把"云端 EDA 工具远程调用服务"纳入出口管辖，向中国实体提供此类服务需单独许可（[U.S. BIS Adds Cloud-Based EDA Remote Access to Export Licensing Review](https://www.qishuai-cn.com/news/U_S_BIS_Adds_Cloud_Based_EDA_Remote_Access_to_Export_Licensing_Review.html)）。此外，Cadence 因向实体清单实体非法出口 EDA 软硬件被 BIS 处以 9500 万美元罚款（[BIS News and Updates](https://www.bis.gov/news-updates?news=Enforcement)）。需要说明的是，也有中文报道称"新思科技已暂停在华销售"，该说法与前述"恢复销售"的报道口径冲突，未经官方确认（[概伦电子免费开放国产 EDA 平台，华大九天 6% 份额领跑本土市场](https://www.niutoushe.com/lives/sybwxdcbgc6553)）。

## 核心技术与关键概念

- **RTL 与验证方法学：** 以 SystemVerilog + UVM 为事实标准，覆盖定向测试、约束随机、覆盖率驱动验证与断言（SVA）；形式验证用于等价性检查与属性证明；功耗验证与安全验证（如 RISC-V 侧信道）成为新增重点。
- **硬件辅助验证：** 仿真加速器与 FPGA 原型支持在硅前运行真实软件栈、执行更长的测试场景，显著缩短复杂项目的验证时间并提前软件开发（[ASIC Verification in 2026](https://www.asicpro.com/2026/06/30/asic-verification-challenges-2026/)）。
- **工艺设计套件（PDK）与 IP：** PDK 决定设计规则、器件模型与签核 deck；IP 复用率决定 SoC 工程成本。领先节点 PDK 的完整商用许可，据行业估算在单项目 200 万至 1000 万美元区间（不含持续 EDA 工具成本、第三方 IP 与表征流片）（[2 nm Process Design Kit (PDK) Market](https://dataintelo.com/report/2-nm-process-design-kit-market)）。
- **Chiplet 与 UCIe：** UCIe 支持多协议、可管理性与自动协商等可选特性，可按需裁剪复杂度（[The Growing Chiplet Ecosystem](https://www.uciexpress.org/post/the-growing-chiplet-ecosystem-collaboration-innovation-and-the-next-wave-of-ucie-adoption)）。UCIe 的工程落地带来新的验证需求：需在 floorplan 前锁定 UCIe profile（Standard vs Advanced、数据率、模块宽度），提前建立 3D 电磁抽取流程，并在每个 interposer 版本上跑合规套件（[Chiplet UCIe Signal Integrity Simulation: 2026 Verification Guide](https://whychips.com/chiplet-ucie-signal-integrity-simulation-2026-verification-guide/)）。
- **设计成本结构：** 软件验证与确认环节已消耗先进节点设计预算的 40% 以上（[The $725 Million Design Tax Reshaping Semiconductor Competition](https://www.stanleylaman.com/signals-and-noise/the-two-tier-silicon-economy)）。

## 代表性项目 / 公司 / 产品（附官方链接）

| 类别 | 代表 | 说明与链接 |
| --- | --- | --- |
| EDA 三大厂 | Synopsys、Cadence、Siemens EDA | DSO.ai、Cerebrus 等 AI 驱动工具（[AI-Driven Chip Design](https://www.synopsys.com/glossary/what-is-ai-driven-chip-design.html)） |
| 收购整合 | Synopsys + Ansys、Keysight | 2025 年 350 亿美元收购案（[Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/ai-and-hpc-eda-tools-market)） |
| 开源 EDA | OpenROAD / OpenROAD Initiative | RTL-to-GDSII 24 小时内无人干预完成，被 500 余篇同行评审论文引用（[Google Joins the OpenROAD Initiative](https://openroadinitiative.org/google-joins-ori/)、[OpenROAD](https://openroad.org/)） |
| 开源流程 | OpenLane + SkyWater 130nm PDK | 学术项目常用完整 RTL-to-GDSII 流程（[Physical Design of UET-RVMCU](https://arxiv.org/html/2603.28709v1)） |
| 开源基准 | RosettaStone 2.0 | 覆盖 2D 与 F2F 混合键合 3D 设计的 RTL-to-GDS 参考流程（[Toward Sustainable and Transparent Benchmarking for Academic Physical Design Research](https://arxiv.org/html/2601.17520)） |
| 中国 EDA | 华大九天、概伦电子 | 华大九天自称市场份额居本土 EDA 企业首位，拥有 700 余家客户（[华大九天上半年营收同比增长12.95%](https://www.stcn.com/article/detail/4161614.html)） |

## 关键数据与评测结果（附来源）

- **流片与设计成本序列：** 有半导体机构数据被引用为 28nm 设计费用约 2800 万美元、16nm 约 9000 万美元、7nm 约 2.5 亿美元、3nm 约 5.8 亿美元、2nm 约 7.25 亿美元（[新浪财经相关报道](https://finance.sina.com.cn/wm/2026-09-19/doc-inisisqe9886721.shtml.md)）。以 IBS 数据为来源的分析同样给出 2nm 节点 7.25 亿美元的设计支出，并指出这是首次出现"设计成本增速超过制程收益"的节点（[The $725 Million Design Tax](https://www.stanleylaman.com/signals-and-noise/the-two-tier-silicon-economy)）。
- **AI ASIC 的 NRE：** 3nm AI 芯片的总设计 NRE 估计在 4 亿至 6 亿美元以上（含工程、EDA、IP 与验证），2nm 趋近 7.25 亿美元；3nm 掩膜组单独增加 1500 万美元以上（有估计为 3000 万至 5000 万美元）（[Cost Estimates for OpenAI's Chip Jalapeno](https://www.useluminix.com/reports/competitive-intelligence/cost-estimates-for-openai-s-chip-jalapeno)）。另一份 2026 年 1 月基准把先进 3nm ASIC 的 NRE 描述为"超过 5 亿美元"（[同前报告](https://www.useluminix.com/reports/competitive-intelligence/cost-estimates-for-openai-s-chip-jalapeno/source/1)）。
- **中国 EDA 份额：** 有报道称三大 EDA 公司占中国 EDA 市场约 70%，本土厂商中华大九天以约 6% 的市场占有率居首（[牛透社](https://www.niutoushe.com/lives/sybwxdcbgc6553)）。华大九天 2026 年上半年营收同比增长 12.95%，技术服务收入增长 53.88%，研发强度升至 72.61%，员工总数增至 1527 人（[华大九天2026年中报解读](https://4g.stockstar.com/detail/RB2026090600001485)、[华大九天上半年营收同比增长12.95%](https://www.stcn.com/article/detail/4161614.html)）。
- **开源 EDA 能力：** OpenROAD 官方声明可实现 24 小时以内无人干预的完整 RTL-to-GDSII 流程（[OpenROAD](https://openroad.org/)）。

## 趋势与争议

1. **AI 驱动设计的边界。** DSO.ai、Cerebrus、AlphaChip 已验证在 PPA 优化与宏布局上的收益，但"agentic EDA"仍处早期；有研究指出单次 agent 运行的算力成本仍是主要制约（[Agentic AI in EDA Market](https://mobilityforesights.com/product/agentic-ai-in-eda-market)）。
2. **先进节点成本与 Chiplet 复用。** 2nm 级 NRE 与掩膜成本推动设计方转向 chiplet 复用与成熟节点组合，UCIe 生态因此成为降低设计边际成本的关键路径。
3. **开源 EDA 的成熟度争议。** OpenROAD 主打无人干预与速度，但先进节点 PDK、模拟/混合信号与签核精度仍由商用工具主导；Google 以 Principal Member 身份加入 OpenROAD Initiative，被视为开源硅生态的重要背书（[Google Joins the OpenROAD Initiative](https://openroadinitiative.org/google-joins-ori/)）。
4. **出口管制与供应链分割。** 2025 年 EDA 出口许可的短暂实施与撤销、2026 年云端 EDA 纳入许可审查，使 EDA 从纯商业工具变为政策工具；这对跨国设计团队的工具访问方式与本地化替代节奏产生直接影响。
5. **验证成本占比过高。** 验证已占先进节点设计预算 40% 以上，硬件辅助验证与形式化方法的组合被视为主要缓解手段，但也带来更长的软件栈依赖与更高的设备采购成本。

## 参考来源

1. [e公司：上市公司资讯第一平台](https://egs.stcn.com/quotation/stock-info/sh688206.html)
2. [The State of EDA: A View from Wall Street（SEMI/DAC 2026）](https://www.semi.org/sites/semi.org/files/2026-09/DAC%20presentation%20(July%202026)%207%20(1).pdf)
3. [Electronic Design Automation (EDA) Market Report 2026](https://www.thebusinessresearchcompany.com/report/electronic-design-automation-eda-global-market-report)
4. [AI And HPC EDA Tools Market Size & Share Analysis](https://www.mordorintelligence.com/industry-reports/ai-and-hpc-eda-tools-market)
5. [Synopsys（checkthat.ai）](https://checkthat.ai/brands/synopsys)
6. [Agentic AI in EDA Market Size, Share, Forecast & Strategic Outlook](https://mobilityforesights.com/product/agentic-ai-in-eda-market)
7. [What is AI-Driven Chip Design?（Synopsys）](https://www.synopsys.com/glossary/what-is-ai-driven-chip-design.html)
8. [Synopsys 宣布扩展 AI 能力（2025-09-03）](https://www.synopsys.com/ko-kr/korean/press-releases/synopsys-announces-expanding-ai-capabilities.html)
9. [The Dawn of Agentic EDA: A Survey of Autonomous Digital Chip Design](https://arxiv.org/pdf/2512.23189v1)
10. [From Future Vision To Running Hardware: Verification At DAC 2026](https://semiengineering.com/from-future-vision-to-running-hardware-verification-at-dac-2026/)
11. [Software-Defined Hardware-Assisted Verification: A New Benchmark for AI-Era Chip Design](https://www.synopsys.com/blogs/chip-design/software-defined-hardware-assisted-verification.html)
12. [ASIC Verification in 2026: Key Challenges and Industry Trends](https://www.asicpro.com/2026/06/30/asic-verification-challenges-2026/)
13. [Semiconductor Emulators Market Growth Analysis](https://www.intelmarketresearch.com/semiconductor-emulators-market-21539)
14. [UCIe Specifications](https://www.uciexpress.org/specifications)
15. [UCIe Webinars（UCIe 3.0 发布）](https://www.uciexpress.org/webinars)
16. [Introducing the UCIe 3.0 Specification](https://www.uciexpress.org/_files/ugd/0c1418_b4744fe368c94e3e9c7eaa13ead632bf.pdf)
17. [The Growing Chiplet Ecosystem: Collaboration, Innovation, and the Next Wave of UCIe Adoption](https://www.uciexpress.org/post/the-growing-chiplet-ecosystem-collaboration-innovation-and-the-next-wave-of-ucie-adoption)
18. [Universal Chiplet Interconnect Express Statement of Support for the UCIe 2.0 Specification](https://www.uciexpress.org/_files/ugd/0c1418_74c8a7bba0714b489dd54ef658c1c968.pdf)
19. [Chiplet UCIe Signal Integrity Simulation: 2026 Verification Guide](https://whychips.com/chiplet-ucie-signal-integrity-simulation-2026-verification-guide/)
20. [Google Joins the OpenROAD Initiative as Principal Member](https://openroadinitiative.org/google-joins-ori/)
21. [OpenROAD](https://openroad.org/)
22. [Physical Design of UET-RVMCU](https://arxiv.org/html/2603.28709v1)
23. [Toward Sustainable and Transparent Benchmarking for Academic Physical Design Research](https://arxiv.org/html/2601.17520)
24. [新浪财经：芯片流片费用相关报道](https://finance.sina.com.cn/wm/2026-09-19/doc-inisisqe9886721.shtml.md)
25. [The $725 Million Design Tax Reshaping Semiconductor Competition](https://www.stanleylaman.com/signals-and-noise/the-two-tier-silicon-economy)
26. [Cost Estimates for OpenAI's Chip Jalapeno](https://www.useluminix.com/reports/competitive-intelligence/cost-estimates-for-openai-s-chip-jalapeno)
27. [Cost Estimates for OpenAI's Chip Jalapeno（来源页）](https://www.useluminix.com/reports/competitive-intelligence/cost-estimates-for-openai-s-chip-jalapeno/source/1)
28. [2 nm Process Design Kit (PDK) Market](https://dataintelo.com/report/2-nm-process-design-kit-market)
29. [U.S. Lifts EDA Software Export Restrictions to China](https://www.axtekic.com/news/u.s.-lifts-eda-software-export-restrictions-to-china.html)
30. [Key chip firms say US export ban lifted（China Daily Asia）](https://www.chinadailyasia.com/upload/main/pdf/2025/07/04/d2e8647cdb726b2a194ee476a35e8caa.pdf)
31. [U.S. BIS Adds Cloud-Based EDA Remote Access to Export Licensing Review](https://www.qishuai-cn.com/news/U_S_BIS_Adds_Cloud_Based_EDA_Remote_Access_to_Export_Licensing_Review.html)
32. [BIS News and Updates（Cadence 处罚）](https://www.bis.gov/news-updates?news=Enforcement)
33. [概伦电子免费开放国产 EDA 平台，华大九天 6% 份额领跑本土市场](https://www.niutoushe.com/lives/sybwxdcbgc6553)
34. [华大九天2026年中报解读](https://4g.stockstar.com/detail/RB2026090600001485)
35. [华大九天上半年营收同比增长12.95% 市场份额居本土EDA企业首位](https://www.stcn.com/article/detail/4161614.html)