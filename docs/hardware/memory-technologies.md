# 存储技术

> 最后更新：2026-09-26 ｜ 领域：硬件·芯片与设计 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

存储技术构成现代计算系统的数据层级：寄存器与 SRAM 靠近计算单元但容量小、成本高；DRAM 作为主存提供大容量与较高带宽；NAND Flash 与 SSD 提供持久化存储；外存与网络存储提供更大容量与更低成本。AI 工作负载同时挤压这一层级的顶点与中部——训练与推理需要巨量高带宽内存（HBM），而数据管道需要海量持久化容量，由此形成 2024–2026 年存储行业的结构性紧缺。

DRAM 侧主要产品线包括 DDR5（服务器/桌面）、LPDDR5X（移动与低功耗）、GDDR7（图形与部分加速器）与 HBM（高带宽内存）；NAND 侧以 3D NAND 为主，向更高层数堆叠与 QLC 演进；此外 CXL 内存、HBF（High Bandwidth Flash）与嵌入式新型存储（MRAM 等）构成层级中的新方向。

## 最新进展（2025–2026）

**AI 驱动的存储超级周期。** 2026 年第二季度一般型 DRAM 合约价格环比上涨 58%–63%，NAND Flash 合约价格环比上涨 70%–75%；有机构报告称 2026 年上半年全球存储芯片行业处于"15 年一遇的超级景气周期"，DRAM 与 NAND 合约价连续两个季度大幅上涨并完整传导至消费端（[国产存储上市了，内存为什么还这么贵？](http://m.ce.cn/bwzg/202608/t20260820_3158612.shtml)）。需求侧的量化依据是：单台 AI 服务器对 DRAM 的需求是普通服务器的 8 至 10 倍，而 HBM 对晶圆面积的消耗显著更高（[新浪财经：存储价格暴涨相关报道](https://finance.sina.com.cn/jjxw/2026-09-23/doc-inisuaap8659513.shtml.md)）。现货市场同样剧烈：据 RAM 价格指数，16Gb DDR5 颗粒现货价从 2025 年 9 月的约 6.84 美元升至 2025 年 12 月的约 27.20 美元（[RAM Prices Up 89%: AI Memory Crunch Hits Gaming](https://shattered.io/ram-prices-ai-memory-shortage-2026/)）。价格上涨的直接机制是三星与 SK 海力士把产能从消费类产品转向高毛利的 AI 相关器件，DDR5 RDIMM 需求已超过供给（[Crisis Global de Suministro de Memoria 2026–2027](https://blog.plds.es/?p=3558)）。

**HBM4 进入量产。** 三星宣布业界首个商用 HBM4 量产出货，稳定传输速率 11.7Gbps、最高可达 13Gbps，比 JEDEC 行业标准的 8Gbps 高出约 46%，相比前代 HBM3E 的最高 9.6Gbps 提升约 1.22 倍，并采用 4nm 逻辑基底芯片（base die）以最大化性能、可靠性与能效（[Samsung Ships Industry-First Commercial HBM4 With Ultimate Performance for AI Computing](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)）。SK 海力士的 HBM4 把 IO 扩展到 2K，实现超过 2.8TB/s 带宽，采用逻辑代工工艺后能效提升约 40%，并借助 Advanced MR-MUF 封装实现最高 16 层堆叠（[SK hynix HBM4](https://product.skhynix.com/products/dram/hbm/hbm4.go)）。美光 12 层堆叠 36GB HBM4 进入大规模量产，专为 NVIDIA Vera Rubin 平台设计，带宽超过 2.8TB/s、能效提升 20%，同期量产业界首款 PCIe Gen6 SSD 与 SOCAMM2（[Micron in High-Volume Production of HBM4 Designed for NVIDIA Vera Rubin](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)、[美光专为 NVIDIA Vera Rubin 打造的 HBM4 进入大规模量产阶段](https://micron.gcs-web.com/news-releases/news-release-details/meiguangzhuanwei-nvidia-vera-rubin-dazaode-hbm4)）。NVIDIA Rubin GPU 对应搭载 288GB HBM4、带宽 22TB/s（[NVIDIA GTC LIVE 2026 Highlights](https://images.nvidia.com/nvimages/gtc/pdf/GTC26_SanJose_Highlights_Final.pdf)）。

**3D NAND 冲击 400 层。** 三星在 FMS 2026 上公开业界首款垂直堆叠 400 层以上的第 10 代 V-NAND"V10 BV-NAND"，采用晶圆键合（BV，Bonded V-NAND）路线（[三星FMS 2026发布zHBM和zNAND-O概念产品，业界首款400层以上V10 BV-NAND亮相](https://www.eet-china.com/news/202608055083.html)、[삼성전자, FMS 2026서 차세대 3D 메모리 비전 제시](https://news.samsungsemiconductor.com/kr/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-fms-2026%EC%84%9C-%EC%B0%A8%EC%84%B8%EB%8C%80-3d-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EB%B9%84%EC%A0%84-%EC%A0%9C%EC%8B%9C/)）。另有报道称三星内部设计的 V10 层数在 430 层区间，使用 5.6 GT/s 接口，并首次在 cell-on-peripheral 架构中应用混合键合，技术细节在 2025 年 2 月的 ISSCC 上公布（[Kioxia NAND Flash Mass Production Accelerates: BiCS10](https://www.c114pro.com/chip/166763.html)）。竞争对手方面：Kioxia/SanDisk 的 BiCS10 为 332 层，采用 CBA（CMOS directly Bonded to Array）架构，计划 2026 年底至 2027 年初量产；SK 海力士第 9 代为 321 层、已完成开发（[Samsungが400層超V10 BV-NANDを発表｜FMS 2026](https://exa-technologies.jp/semicon-info/semiconductor-memory/samsung-400-layer-v10-bv-nand/)）。SK 海力士据报目标在 2026 年底实现 375 层 NAND 量产，而三星迄今最先进的商用产品仍是 2024 年 4 月开始量产的 286 层 NAND（[The Race to 400-Layer NAND](https://www.trendforce.com/news/2026/06/12/news-the-race-to-400-layer-nand-roadmaps-and-key-technologies-driving-samsung-sk-hynix-and-kioxia/)）。

**HBF：介于 HBM 与 SSD 之间的新层级。** SK 海力士与 Sandisk 于 2026 年 2 月启动 HBF（High Bandwidth Flash）标准化工作，并在 2026 年 8 月 3 日通过 OCP 发布首版 HBF 技术规范；规格包含最高 512GB 容量、3TB/s 带宽、对 UCIe 的支持，以及 2.5 倍能效改善的 375 层 4D NAND（[SK hynix Unveils First HBF Standard Specifications with Sandisk](https://news.skhynix.com/en/hbf-at-fms-2026/)、[Sandisk and SK hynix Advance Global Standardization of High Bandwidth Flash](https://www.sandisk.com/company/newsroom/press-releases/2026/2026-08-03-Sandisk-and-sk-hynix-advance-global-standardization-of-hbf)）。Sandisk 官方称 HBF 面向 AI 推理，容量可达 HBM 的 8–16 倍、带宽相近、成本相当，性能与"无限容量 HBM"的差距在 2.2% 以内（[SANDISK UNVEILS THE FUTURE OF MEMORY ARCHITECTURE FOR AI](https://documents.sandisk.com/content/dam/asset-library/en_us/assets/public/sandisk/collateral/company/Sandisk-HBF-Fact-Sheet.pdf)）；送样计划为 2026 年下半年，首批搭载 HBF 的 AI 推理设备样品预计 2027 年初可用（[Sandisk to Collaborate with SK hynix to Drive Standardization of High-Bandwidth Flash](https://www.sandisk.com/ar-sa/company/newsroom/press-releases/2025/2025-08-06-sandisk-to-collaborate-with-sk-hynix-to-drive-standardization-of-high-bandwidth-flash-memory-technology)）。

**CXL 内存推进不及预期。** CXL 4.0 规范于 2025 年发布，最大链路速率从 3.x 的 64 GT/s 提升到 128 GT/s（[Introducing the CXL 4.0 Specification](https://computeexpresslink.org/wp-content/uploads/2025/12/CXL_4.0-Webinar_December-2025_FINAL.pdf)）。落地方面，三星在 2025 年 10 月的 OCP 全球峰会上承诺交付下一代 CXL 3.1 模块，但据行业媒体报道九个月后仍未出货（[The AI Boom Created the Most Expensive Server Memory Market in History](https://liveinthefuture.org/stories/cxl-delay-stranded-memory-paradox)）。已有实际部署案例：Azure 推出首个搭载 Intel Xeon 6 与 CXL 内存的云 VM（私密预览），Meta 则用定制 CXL 2.0 芯片把旧 DDR4-2400 与新 DDR5-6400 混用于同一服务器（[Beyond the Memory Wall: How CXL Memory Pooling and Sharing Are Transforming AI Inference](https://computeexpresslink.org/wp-content/uploads/2026/09/CXL_FMS-2026-Panel-Presentation_FINAL.pdf)）。行业基准显示 CXL 内存池化可把机架 DRAM 总量降低 25%–30%，同时保留直连内存 90%–95% 的带宽（[同前](https://liveinthefuture.org/stories/cxl-delay-stranded-memory-paradox)）。

**图形显存与近存计算。** RTX 50 系列是首批采用 GDDR7 的消费级 GPU：RTX 5090 使用 512-bit、28Gbps GDDR7，带宽 1792 GB/s；RTX 5080 使用 256-bit、30Gbps，带宽 960 GB/s（[GDDR6 / GDDR6X / GDDR7 / HBM3 / HBM4 とは 2026年版](https://mypcrig.com/blog/gddr6-gddr7-hbm3-hbm4-gpu-memory-explained-2026/)、[GDDR6 vs GDDR7: A Technical Comparison](https://www.wevolver.com/article/gddr6-vs-gddr7-a-technical-comparison-of-graphics-memory)）。近存计算（PIM）方面，Samsung HBM2-PIM、SK hynix GDDR6-PIM 与 LPDDR5X-PIM 主要面向 GEMV 计算，适配 batch size 为 1 的解码阶段（[Processing in Memory: DRAM Is About to Do Math](https://ben3d.ca/blog/processing-in-memory)）。

**嵌入式新型存储（MRAM）。** 2026 年以来出现多个产业化信号：亚洲首个 8nm eMRAM 流片、搭载 SOT-MRAM 的无人机完成试飞、台积电 1 纳秒 SOT-MRAM 进展、全球首条 8 英寸磁性随机存储芯片产线在青岛建成（[MRAM产业化进入"临界点"](https://m.36kr.com/p/3806128847675144)）。三星的 eMRAM 路线图为 2024 年 14nm、2026 年 8nm、2027 年 5nm（[Developing the "Industry's Most Energy-Efficient" Next-Generation MRAM](https://semiconductor.samsung.com/us/news-events/tech-blog/developing-the-industrys-most-energy-efficient-next-generation-mram-selected-as-iedm-highlight-paper/)）；GlobalFoundries 表示车规 eMRAM 在 FDX 平台上具备"业界领先的 100 MHz 级访问时间"，已有主要客户完成流片（[Embedded MRAM（MRAM-Info）](https://www.mram-info.com/tags/embedded-mram)）。有分析认为 MRAM 市场到 2035 年可能达到 580 亿美元，主要替代微控制器中的嵌入式 Flash（[MRAM Finally Delivers on Decades of Promise](https://computers.sciencearray.com/mram-commercialization-magnetic-memory-breakthrough)）。

## 核心技术与关键概念

- **DRAM 单元与代际：** 1T1C（一晶体管一电容）结构，靠周期性刷新保持数据。DDR5 是服务器与桌面主流，LPDDR5X 面向低功耗与移动，GDDR7 面向图形与部分推理加速器，HBM 通过 TSV 与超宽 IO 换取数量级带宽。
- **HBM 的结构性代价：** HBM 需要大面积硅中介层与 TSV、堆叠良率损失高，对晶圆面积的单位容量消耗远高于普通 DRAM，因此 HBM 产能扩张会挤占通用 DRAM 供应——这是 2025–2026 年消费级内存涨价的重要传导机制（[新浪财经报道](https://finance.sina.com.cn/jjxw/2026-09-23/doc-inisuaap8659513.shtml.md)）。
- **HBM4 关键技术：** IO 位宽翻倍到 2K、逻辑基底芯片采用代工逻辑工艺、Advanced MR-MUF 或混合键合实现 12–16 层堆叠（[SK hynix HBM4](https://product.skhynix.com/products/dram/hbm/hbm4.go)、[Micron HBM4](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)）。
- **3D NAND 堆叠：** 通过增加层数提升密度，难点在于高深宽比刻蚀、层间应力控制与外围电路占比。BV-NAND（晶圆键合）与 CBA 架构把外围 CMOS 与存储阵列分开制造再键合，是突破 400 层的主要路径。
- **HBF 与 UCIe：** HBF 基于 NAND 存储技术，定位在 HBM 与 SSD 之间的新层级，并用 UCIe 作为互连接口（[SK hynix HBF](https://news.skhynix.com/en/hbf-at-fms-2026/)）。
- **CXL 协议：** 在 PCIe 物理层上实现缓存一致的内存语义，支持内存扩展、池化与共享；CXL 4.0 把链路速率翻倍（[CXL 4.0 Webinar](https://computeexpresslink.org/wp-content/uploads/2025/12/CXL_4.0-Webinar_December-2025_FINAL.pdf)）。
- **SSD 与接口代际：** PCIe Gen6 SSD 已进入量产，NVMe 与控制器能力决定随机读性能与写入放大（[Micron](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)）。

## 代表性项目 / 公司 / 产品（附官方链接）

| 厂商 | 代表产品 | 链接 |
| --- | --- | --- |
| Samsung | HBM4（11.7–13Gbps、4nm base die）、V10 BV-NAND（400 层以上） | [samsung.com](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/) |
| SK hynix | HBM4（>2.8TB/s、16 层堆叠）、HBF、375 层 4D NAND | [product.skhynix.com](https://product.skhynix.com/products/dram/hbm/hbm4.go)、[news.skhynix.com](https://news.skhynix.com/en/hbf-at-fms-2026/) |
| Micron | HBM4 36GB 12H、PCIe Gen6 SSD、SOCAMM2 | [investors.micron.com](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin) |
| Kioxia / SanDisk | BiCS10（332 层，CBA） | [c114pro](https://www.c114pro.com/chip/166763.html) |
| CXL 生态 | CXL Consortium、Azure、Meta | [computeexpresslink.org](https://computeexpresslink.org/wp-content/uploads/2026/09/CXL_FMS-2026-Panel-Presentation_FINAL.pdf) |
| MRAM | Samsung、GlobalFoundries、Everspin | [semiconductor.samsung.com](https://semiconductor.samsung.com/us/news-events/tech-blog/developing-the-industrys-most-energy-efficient-next-generation-mram-selected-as-iedm-highlight-paper/) |

## 关键数据与评测结果（附来源）

- 2026 年 Q2 合约价：一般型 DRAM 环比 +58%–63%，NAND Flash 环比 +70%–75%（[中国经济网](http://m.ce.cn/bwzg/202608/t20260820_3158612.shtml)）。
- 16Gb DDR5 现货：2025 年 9 月约 6.84 美元 → 2025 年 12 月约 27.20 美元（[RAM Prices Up 89%](https://shattered.io/ram-prices-ai-memory-shortage-2026/)）。
- HBM4 速率与带宽：三星 11.7Gbps（最高 13Gbps）；SK 海力士与美光均标称超过 2.8TB/s（[Samsung](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)、[Micron](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)）。
- NAND 层数：三星 V10 400 层以上（另有报道称 430 层区间）、Kioxia BiCS10 332 层、SK 海力士第 9 代 321 层、SK 海力士 375 层目标（[exa-technologies](https://exa-technologies.jp/semicon-info/semiconductor-memory/samsung-400-layer-v10-bv-nand/)、[TrendForce](https://www.trendforce.com/news/2026/06/12/news-the-race-to-400-layer-nand-roadmaps-and-key-technologies-driving-samsung-sk-hynix-and-kioxia/)）。
- HBF 规格：最高 512GB、3TB/s、UCIe 支持（[SK hynix](https://news.skhynix.com/en/hbf-at-fms-2026/)）。
- CXL 4.0 最大链路速率 128 GT/s，CXL 3.x 为 64 GT/s（[CXL 4.0 Webinar](https://computeexpresslink.org/wp-content/uploads/2025/12/CXL_4.0-Webinar_December-2025_FINAL.pdf)）。
- GDDR7 带宽：RTX 5090 达 1792 GB/s、RTX 5080 达 960 GB/s（[mypcrig](https://mypcrig.com/blog/gddr6-gddr7-hbm3-hbm4-gpu-memory-explained-2026/)）。

## 趋势与争议

1. **HBM 挤占通用 DRAM 的分配矛盾。** HBM 单位容量消耗的晶圆面积更高，且毛利更高，厂商优先分配产能给 HBM 与服务器 RDIMM，导致消费级 DDR5 与 NAND 价格上涨；这一"挤出效应"是当前存储价格结构性问题（[新浪财经](https://finance.sina.com.cn/jjxw/2026-09-23/doc-inisuaap8659513.shtml.md)）。
2. **HBF 的新层级之争。** HBF 声称以相近带宽提供 8–16 倍 HBM 容量，若在 2027 年如期送样，可能改变推理场景的内存层级划分；但目前仅有规范与样品计划，缺乏第三方独立评测（[Sandisk HBF Fact Sheet](https://documents.sandisk.com/content/dam/asset-library/en_us/assets/public/sandisk/collateral/company/Sandisk-HBF-Fact-Sheet.pdf)）。
3. **CXL 的推广悖论。** CXL 本可降低服务器内存成本，但在内存最昂贵的时期反而推进缓慢：厂商优先把产能投入 HBM 与高毛利模组，CXL 模块交付一再延期（[The AI Boom Created the Most Expensive Server Memory Market in History](https://liveinthefuture.org/stories/cxl-delay-stranded-memory-paradox)）。另有预测认为 CXL 3.0/3.1 的规模化 AI 池化应用要到 2026 下半年至 2027 年之后（[Guia de Planejamento de Infraestrutura CXL 4.0](https://introl.com/pt/blog/cxl-4-0-infrastructure-planning-guide-ai-memory-pooling-2025)）。
4. **3D NAND 的堆叠极限。** 400 层以上依赖晶圆键合与 CBA 分离制造，工艺复杂度与成本上升，层数提升的边际收益成为争议点；各厂商公布层数的统计方式（总层数 vs 有效层数）也不统一。
5. **新型存储的落地节奏。** MRAM 在嵌入式车规与 MCU 场景逐步替代嵌入式 Flash，但量产节点从 14nm 到 5nm 的推进需要长期验证；ReRAM/PCM 等方向在本轮检索中缺乏可确证的规模化量产数据。

## 参考来源

1. [国产存储上市了，内存为什么还这么贵？（中国经济网）](http://m.ce.cn/bwzg/202608/t20260820_3158612.shtml)
2. [新浪财经：存储价格暴涨核心驱动力相关报道](https://finance.sina.com.cn/jjxw/2026-09-23/doc-inisuaap8659513.shtml.md)
3. [RAM Prices Up 89%: AI Memory Crunch Hits Gaming [2026]](https://shattered.io/ram-prices-ai-memory-shortage-2026/)
4. [Why RAM Prices Are So High in 2026](https://tweaklibrary.com/why-ram-prices-are-so-high/)
5. [Crisis Global de Suministro de Memoria y Almacenamiento 2026–2027](https://blog.plds.es/?p=3558)
6. [Samsung Ships Industry-First Commercial HBM4](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)
7. [SK hynix HBM4](https://product.skhynix.com/products/dram/hbm/hbm4.go)
8. [Micron in High-Volume Production of HBM4 Designed for NVIDIA Vera Rubin](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)
9. [美光专为 NVIDIA Vera Rubin 打造的 HBM4 进入大规模量产阶段](https://micron.gcs-web.com/news-releases/news-release-details/meiguangzhuanwei-nvidia-vera-rubin-dazaode-hbm4)
10. [NVIDIA GTC LIVE 2026 Highlights](https://images.nvidia.com/nvimages/gtc/pdf/GTC26_SanJose_Highlights_Final.pdf)
11. [三星FMS 2026发布zHBM和zNAND-O概念产品](https://www.eet-china.com/news/202608055083.html)
12. [삼성전자, FMS 2026서 차세대 3D 메모리 비전 제시](https://news.samsungsemiconductor.com/kr/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-fms-2026%EC%84%9C-%EC%B0%A8%EC%84%B8%EB%8C%80-3d-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EB%B9%84%EC%A0%84-%EC%A0%9C%EC%8B%9C/)
13. [Samsungが400層超V10 BV-NANDを発表｜FMS 2026](https://exa-technologies.jp/semicon-info/semiconductor-memory/samsung-400-layer-v10-bv-nand/)
14. [Kioxia NAND Flash Mass Production Accelerates: BiCS10](https://www.c114pro.com/chip/166763.html)
15. [The Race to 400-Layer NAND: Roadmaps and Key Technologies](https://www.trendforce.com/news/2026/06/12/news-the-race-to-400-layer-nand-roadmaps-and-key-technologies-driving-samsung-sk-hynix-and-kioxia/)
16. [SK hynix Unveils First HBF Standard Specifications with Sandisk](https://news.skhynix.com/en/hbf-at-fms-2026/)
17. [Sandisk and SK hynix Advance Global Standardization of High Bandwidth Flash](https://www.sandisk.com/company/newsroom/press-releases/2026/2026-08-03-Sandisk-and-sk-hynix-advance-global-standardization-of-hbf)
18. [SANDISK UNVEILS THE FUTURE OF MEMORY ARCHITECTURE FOR AI（HBF Fact Sheet）](https://documents.sandisk.com/content/dam/asset-library/en_us/assets/public/sandisk/collateral/company/Sandisk-HBF-Fact-Sheet.pdf)
19. [Sandisk to Collaborate with SK hynix to Drive Standardization of High-Bandwidth Flash Memory](https://www.sandisk.com/ar-sa/company/newsroom/press-releases/2025/2025-08-06-sandisk-to-collaborate-with-sk-hynix-to-drive-standardization-of-high-bandwidth-flash-memory-technology)
20. [Introducing the CXL 4.0 Specification](https://computeexpresslink.org/wp-content/uploads/2025/12/CXL_4.0-Webinar_December-2025_FINAL.pdf)
21. [Beyond the Memory Wall: How CXL Memory Pooling and Sharing Are Transforming AI Inference](https://computeexpresslink.org/wp-content/uploads/2026/09/CXL_FMS-2026-Panel-Presentation_FINAL.pdf)
22. [The AI Boom Created the Most Expensive Server Memory Market in History](https://liveinthefuture.org/stories/cxl-delay-stranded-memory-paradox)
23. [Guia de Planejamento de Infraestrutura CXL 4.0](https://introl.com/pt/blog/cxl-4-0-infrastructure-planning-guide-ai-memory-pooling-2025)
24. [GDDR6 / GDDR6X / GDDR7 / HBM3 / HBM4 とは 2026年版](https://mypcrig.com/blog/gddr6-gddr7-hbm3-hbm4-gpu-memory-explained-2026/)
25. [GDDR6 vs GDDR7: A Technical Comparison of Graphics Memory](https://www.wevolver.com/article/gddr6-vs-gddr7-a-technical-comparison-of-graphics-memory)
26. [Processing in Memory: DRAM Is About to Do Math](https://ben3d.ca/blog/processing-in-memory)
27. [MRAM产业化进入"临界点"](https://m.36kr.com/p/3806128847675144)
28. [Embedded MRAM（MRAM-Info）](https://www.mram-info.com/tags/embedded-mram)
29. [Developing the "Industry's Most Energy-Efficient" Next-Generation MRAM](https://semiconductor.samsung.com/us/news-events/tech-blog/developing-the-industrys-most-energy-efficient-next-generation-mram-selected-as-iedm-highlight-paper/)
30. [MRAM Finally Delivers on Decades of Promise](https://computers.sciencearray.com/mram-commercialization-magnetic-memory-breakthrough)