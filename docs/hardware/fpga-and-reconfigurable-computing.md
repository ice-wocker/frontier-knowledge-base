# FPGA 与可重构计算（FPGA and Reconfigurable Computing）

> 最后更新：2026-09-26 ｜ 领域：硬件·计算架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

FPGA（Field Programmable Gate Array，现场可编程门阵列）是一类可在出厂后重复编程的集成电路，其核心价值在于把硬件逻辑与数据通路按需定制，同时在需求变化时无需重新流片即可更新功能。与 ASIC（专用集成电路）相比，FPGA 单位成本更高、峰值能效通常不及定制电路，但具备上市快、可迭代、小批量经济的优势，因此在网络加速、金融交易、原型验证、航空航天与国防、通信等领域长期占据稳固位置。近两年 AI 推理与高速网络的可编程加速需求，使 FPGA 与自适应 SoC（adaptive SoC）重新受到关注。

## 最新进展（2025–2026）

- **Altera 独立**：Intel 于 2025 年 4 月 14 日宣布将 Altera 业务 51% 股权出售给 Silver Lake，交易对 Altera 估值 87.5 亿美元，使其成为最大的纯 FPGA（pure-play）半导体方案公司（[Intel Announces Strategic Investment by Silver Lake in Altera](https://www.altera.com/newsroom/news/press-release/altera-investment-silver-lake)）。交易完成后 Intel 保留 49% 股权（[Altera Closes Silver Lake Investment to Become World's Largest Pure-play FPGA Solutions Provider](https://www.altera.com/newsroom/news/press-release/altera-silver-lake)）。
- **产品迭代**：Altera 于 2026 年 8 月 11 日随 Quartus Prime Pro Edition 26.1 扩展其 Agilex FPGA 组合的 DDR5/LPDDR5/LPDDR5X 内存支持，强调更高带宽、更大灵活性与供应韧性（[Altera Expands DDR5 Memory Support Across Agilex FPGA Portfolio](https://www.altera.com/newsroom/ddr5-memory-support)）；并于 2026 年 6 月 8 日在 IMS2026 宣布下一代宽带 Agilex 9 Direct RF-Series SoC FPGA 进入工程样品阶段，面向航空航天、国防与先进通信（[Altera Introduces Next-Generation Agilex 9 Direct RF-Series SoC FPGA](https://www.altera.com/newsroom/agilex-9-agrw039)）。
- **面向 AI 的高端 FPGA**：AMD 于 2025 年推出 Versal Premium VP1902，被称为当时全球最大 FPGA，具备 420 万逻辑单元与 8 TFLOPS AI 性能，面向网络与云（[Worldwide High-End FPGA Market 2026](https://pmarketresearch.com/worldwide-high-end-fpga-market-research/)）。

## 核心技术与关键概念

- **可编程资源**：查找表（LUT）实现组合逻辑；DSP 块用于乘加等算术运算；块存储器（BRAM）是主要专用存储资源，实现为同步双端口存储，数据位宽可达 72 位，Xilinx 7 系列每个 BRAM 为 36 Kib，可配置为单个 36 Kib 或拆分为两个独立 18 Kib，读写独立时钟支持跨时钟域安全传输；更高密度需求可由 AMD UltraScale+ 引入的 UltraRAM 满足（[FPGA Development: Architecture, Tools, and Design Flow](https://www.wevolver.com/article/fpga-development-architecture-tools-and-design-flow)）。
- **高层次综合（HLS）**：以 C/C++ 描述算法，由工具综合为 RTL。AMD Vitis HLS 将顶层函数参数综合为 RTL I/O 端口并自动实现接口协议，C 中的数组可映射到 BRAM、LUTRAM、URAM 等存储资源，循环可保持卷绕（rolled）或流水化（pipelined）以提升性能，并提供时延、启动间隔等性能指标（[AMD Vitis HLS](https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vitis/vitis-hls.html)）。工具链演进方面，Vitis 统一 IDE（新 GUI）成为默认，经典 IDE 已弃用（[Novidades na Plataforma de software AMD Vitis](https://www.amd.com/pt/products/software/adaptive-socs-and-fpgas/vitis/vitis-whats-new.html)）。
- **FPGA vs ASIC 权衡**：FPGA 可重构、上市周期短、适合算法快速演进与小批量场景；ASIC 在量产规模下单位成本与能效更优，但流片成本高、迭代慢。
- **面向 AI 与 DSP 的工具链演进**：AMD Vitis 平台扩展了 AI 引擎（AIE）与 HDL 模块库，新增 FFT（含原生浮点 SSR=32/64）以及可更少占用 DSP58 资源的复数乘法器等（[Novidades na Plataforma de software AMD Vitis](https://www.amd.com/pt/products/software/adaptive-socs-and-fpgas/vitis/vitis-whats-new.html)）。
- **自适应 SoC / AI 引擎**：将 FPGA 可编程逻辑与硬核处理器、AI 引擎（AIE）阵列集成，用于在可编程平台上承载 AI 推理。

## 代表性项目 / 公司 / 产品（附官方链接）

- **AMD**：通过收购 Xilinx 成为 FPGA 与自适应计算的主要提供商，产品包括 Versal 自适应 SoC、Alveo 加速卡、Kria SOM；其 Embedded 业务部门包含嵌入式 CPU、APU 与 FPGA（[AMD Reports Second Quarter 2026 Financial Results](https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results)）。
- **Altera**：独立后的纯 FPGA 公司，产品线含 Agilex 系列（[Altera Newsroom](https://www.altera.com/newsroom)）。
- **Bittware / 加速卡生态**：面向低延迟交易的 FPGA NIC，如 LMS ÜberNIC，将整个网络协议栈放入加速硬件，基于 PCIe 5.0 + CXL（[LMS ÜberNIC](https://www.bittware.com/zh/products/lms-ubernic/)）。

## 关键数据与评测结果（附来源）

- **市场份额**：有分析称 AMD（Xilinx）以约 51% 份额领先，四大美国厂商合计占全球市场 90% 以上；2025 年 Silver Lake 以 87.5 亿美元收购 Intel Altera 51% 股权后，Altera 成为全球最大独立 FPGA 公司，同时国产替代进入关键窗口（[A New Shift in Computing Power: FPGAs Regain Industry Influence in AI Inference](https://en.ic2035.com/news_details_1/2060261211354619904.html)）。在 2026 年上半年全球 FPGA 企业市占率榜单中，复旦微电位列全球第四（[2026 年上半年全球 FPGA 企业市场占有率 - 复旦微电全球第四](https://www.myzaker.com/article/6aa8c3878e9f0913fb085e27)）。
- **应用结构**：一份报告给出的 FPGA 芯片应用分布为电信 34.75%、数据中心 25.33%、汽车 19.86%、工业 10.11%（[Field Programmable Gate Array Chip Market](https://pmarketresearch.com/it/field-programmable-gate-array-chip-market/)）。按产品类型，SRAM FPGA 占 81.07%、Flash FPGA 占 11.34%、反熔丝（Antifuse）FPGA 占 7.08%（[Global Field-Programmable Gate Array (FPGA) Market 2026](https://pmarketresearch.com/worldwide-field-programmable-gate-array-fpga-market-research/)）。
- **主要玩家**：AMD、Intel、Lattice Semiconductor、Microchip、Achronix、QuickLogic、Efinix、GOWIN、Flex Logix、Renesas 等（[Field Programmable Gate Array (FPGA) Market](https://www.strategicmarketresearch.com/market-report/field-programmable-gate-array-market)）。
- **AMD Embedded 收入**：AMD 2026 年第二季度 Embedded 业务营收 9.77 亿美元、同比增长 19%，主要因多终端市场需求走强（[AMD Reports Second Quarter 2026 Financial Results](https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results)）；该业务（主要为 Xilinx 系列）经营利润 3.86 亿美元，上年同期为 2.75 亿美元（[From PCs to AI Accelerators: Advanced Micro Devices (AMD) Shares](https://www.openbookanalytics.com/news/insights/from-pcs-to-ai-accelerators-advanced-micro-devices-amd-shares)）。AMD 在 2023 年报中称 Embedded 业务营收 53 亿美元、同比增长 17%，并维持「业界第一大 FPGA 与自适应计算方案提供商」定位（[AMD 2023 Annual Report on Form 10-K](https://ir.amd.com/financial-information/sec-filings/content/0001193125-24-076535/0001193125-24-076535.pdf)）。
- **市场规模（多口径）**：有报告称 2026 年 FPGA 市场规模 110.2 亿美元，到 2031 年达 172.3 亿美元，CAGR 9.35%（[Field Programmable Gate Array (FPGA) Market](https://www.mordorintelligence.com/industry-reports/field-programmable-gate-array-fpga-market)）；另有报告给出 2025 年 117.3 亿美元、2034 年 193.4 亿美元、CAGR 10.5%（[Field-Programmable Gate Arrays (FPGA) Market Research Report 2034](https://researchintelo.com/report/field-programmable-gate-arrays-fpga-market)）。高端 FPGA 细分口径亦有差异：一份报告称 2025 年高端 FPGA 市场为 62.5 亿美元（[Worldwide High-End FPGA Market 2026](https://pmarketresearch.com/worldwide-high-end-fpga-market-research/)），另一份称 2025 年为 78 亿美元、2034 年达 172 亿美元、CAGR 9.2%（[High End FPGA Market](https://dataintelo.com/report/global-high-end-fpga-market)）。

## 趋势与争议

- **AI 加速的定位**：FPGA 被广泛用于 SmartNIC（智能网卡），实现网络数据包处理与 AI 推理融合；以实时金融风控为例，网卡上的 FPGA 可就地完成 AI 模型判断，无需把数据搬到主机 CPU/GPU 内存，从而降低端到端时延并卸载主机负担（[FPGA在人工智能领域的应用前景分析](https://www.eet-china.com/mp/a524652.html)）。
- **数据中心与网络场景**：Agilex 7 M 系列针对 AI 内存带宽敏感场景优化，在数据中心面向生成式 AI 模型加速，在网络领域用于下一代防火墙的高性能数据通路与深度缓存（[Agilex 7 FPGA: A Programmable Platform Leading AI and Data Center Computing Power](http://www.mjdic.com/news-read-id-5676.html)）。
- **金融低延迟应用**：FPGA 在算法交易与衍生品定价（如蒙特卡洛）中通过把计算映射到硬件并最小化与主机 CPU 的通信来降低时延（[Algorithmic Trading: A brief, computational finance case study on data centre FPGAs](https://arxiv.org/pdf/1607.05069v1)）；Intel 与生态伙伴提供 FPGA 加速库用于量化金融（[Accelerating Quantitative Finance with FPGA-based Acceleration cards](https://www.intel.cn/content/dam/www/public/us/en/documents/solution-briefs/accelerating-quantitative-finance-fpga-brief.pdf)）。
- **AI 推理中的定位回升**：有分析认为 FPGA 在 AI 推理领域重新获得行业影响力，同时国产替代进入关键窗口（[A New Shift in Computing Power: FPGAs Regain Industry Influence in AI Inference](https://en.ic2035.com/news_details_1/2060261211354619904.html)）。
- **国产替代**：有分析指出随着海外厂商格局调整（Altera 独立、AMD 主导），国产 FPGA 替代进入关键窗口，2026 年上半年复旦微电已位列全球市占率第四（[A New Shift in Computing Power](https://en.ic2035.com/news_details_1/2060261211354619904.html)、[2026 年上半年全球 FPGA 企业市场占有率](https://www.myzaker.com/article/6aa8c3878e9f0913fb085e27)）。
- **市场争议**：FPGA 市场规模统计口径差异较大（是否含自适应 SoC、高端与整体口径不同），引用时需区分来源与范围；同时 AI ASIC 与 GPU 的强势也在挤压 FPGA 在部分推理场景的空间。

## 参考来源

- [Intel Announces Strategic Investment by Silver Lake in Altera](https://www.altera.com/newsroom/news/press-release/altera-investment-silver-lake)
- [Altera Closes Silver Lake Investment to Become World's Largest Pure-play FPGA Solutions Provider](https://www.altera.com/newsroom/news/press-release/altera-silver-lake)
- [Altera Expands DDR5 Memory Support Across Agilex FPGA Portfolio](https://www.altera.com/newsroom/ddr5-memory-support)
- [Altera Introduces Next-Generation Agilex 9 Direct RF-Series SoC FPGA](https://www.altera.com/newsroom/agilex-9-agrw039)
- [Worldwide High-End FPGA Market 2026](https://pmarketresearch.com/worldwide-high-end-fpga-market-research/)
- [FPGA Development: Architecture, Tools, and Design Flow](https://www.wevolver.com/article/fpga-development-architecture-tools-and-design-flow)
- [AMD Vitis HLS](https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vitis/vitis-hls.html)
- [Novidades na Plataforma de software AMD Vitis](https://www.amd.com/pt/products/software/adaptive-socs-and-fpgas/vitis/vitis-whats-new.html)
- [AMD Reports Second Quarter 2026 Financial Results](https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results)
- [From PCs to AI Accelerators: Advanced Micro Devices (AMD) Shares](https://www.openbookanalytics.com/news/insights/from-pcs-to-ai-accelerators-advanced-micro-devices-amd-shares)
- [AMD 2023 Annual Report on Form 10-K](https://ir.amd.com/financial-information/sec-filings/content/0001193125-24-076535/0001193125-24-076535.pdf)
- [A New Shift in Computing Power: FPGAs Regain Industry Influence in AI Inference](https://en.ic2035.com/news_details_1/2060261211354619904.html)
- [2026 年上半年全球 FPGA 企业市场占有率 - 复旦微电全球第四](https://www.myzaker.com/article/6aa8c3878e9f0913fb085e27)
- [Field Programmable Gate Array Chip Market](https://pmarketresearch.com/it/field-programmable-gate-array-chip-market/)
- [Global Field-Programmable Gate Array (FPGA) Market 2026](https://pmarketresearch.com/worldwide-field-programmable-gate-array-fpga-market-research/)
- [Field Programmable Gate Array (FPGA) Market (Strategic Market Research)](https://www.strategicmarketresearch.com/market-report/field-programmable-gate-array-market)
- [LMS ÜberNIC](https://www.bittware.com/zh/products/lms-ubernic/)
- [Field Programmable Gate Array (FPGA) Market](https://www.mordorintelligence.com/industry-reports/field-programmable-gate-array-fpga-market)
- [Field-Programmable Gate Arrays (FPGA) Market Research Report 2034](https://researchintelo.com/report/field-programmable-gate-arrays-fpga-market)
- [High End FPGA Market](https://dataintelo.com/report/global-high-end-fpga-market)
- [FPGA在人工智能领域的应用前景分析](https://www.eet-china.com/mp/a524652.html)
- [Agilex 7 FPGA: A Programmable Platform Leading AI and Data Center Computing Power](http://www.mjdic.com/news-read-id-5676.html)
- [Algorithmic Trading: A brief, computational finance case study on data centre FPGAs](https://arxiv.org/pdf/1607.05069v1)
- [Accelerating Quantitative Finance with FPGA-based Acceleration cards](https://www.intel.cn/content/dam/www/public/us/en/documents/solution-briefs/accelerating-quantitative-finance-fpga-brief.pdf)