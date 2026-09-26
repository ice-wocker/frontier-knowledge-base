# 半导体制造前沿

> 最后更新：2026-09-26 ｜ 领域：半导体制造 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

半导体制造是所有前沿计算的物理基础。进入 2026 年，行业竞争围绕四条主线展开：**①先进制程从 FinFET 转向 GAA 环栅并逼近 2nm/1.4nm；②背面供电（BSPDN）成为新一代节点的"标配"；③High-NA EUV 光刻进入量产试用；④先进封装（CoWoS、SoIC、Chiplet）与 HBM 成为 AI 芯片真正的产能瓶颈**。与此同时，各国芯片法案补贴与出口管制持续重塑全球供应链地理格局。

## 2025–2026 最新进展

### 先进制程节点：2nm 正式量产
台积电 2nm（N2）技术已于 2025 年第四季度按计划进入量产，采用业界领先的第一代 nanosheet（纳米片）晶体管技术，在性能与功耗上实现完整节点级跃升（[TSMC 2nm Technology](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm)）。据台积电 2025 年年报，N2 良率良好，预计 2026 年快速爬坡；N2P 与 A16 作为 N2 家族延伸，量产时间均定于 2026 年下半年（[TSMC 2025 Annual Report](https://investor.tsmc.com/static/annualReports/2025/english/index.html)）。其中 A16 首次采用台积电称为"Super Power Rail（SPR）"的背面供电方案，最适合信号走线复杂、供电网络密集的 HPC 产品。

更前沿的节点节奏也已明确：A14（1.4nm 级，第二代 nanosheet）计划 2028 年量产；A13 作为 A14 家族延伸，通过约 97% 的光学微缩实现 6% 面积节省，设计规则与 A14 完全兼容，计划 2029 年量产（[TSMC Debuts A13 Technology](https://pr.tsmc.com/english/news/3302)、[TSMC A14 Technology](https://www.tsmc.com/japanese/dedicatedFoundry/technology/logic/l_A14)）。

Intel 方面，18A 是其首个在美国本土量产的 2nm 级节点，采用 RibbonFET 全环绕栅极晶体管与 PowerVia 背面供电技术（[Intel 18A Platform Brief](https://www.intel.de/content/dam/www/central-libraries/us/en/documents/2025-03/foundry-18a-platform-brief.pdf)）。2026 年 1 月 CES 上，Intel 发布第三代酷睿 Ultra 处理器（代号 Panther Lake），这是首款基于 Intel 18A 打造的计算平台，2026 年 1 月 27 日起商用上市（[CES 2026: Intel Core Ultra Series 3](https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a)、[Intel Unveils Panther Lake Architecture](https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a)）。Intel 的下一代 14A 节点节奏被明显提前：据 Intel CFO 表述，14A 将于 2026 年 10 月发布 0.9 版 PDK，2027 年下半年开始风险试产，2028 年进入大规模量产，其缺陷密度下降速度为 22nm 以来最快（[TrendForce: Intel CFO Says 14A Defect Reduction Fastest Since 22nm](https://www.trendforce.com/news/2026/09/01/news-intel-cfo-says-14a-defect-reduction-fastest-since-22nm-customer-talks-reportedly-grow-ahead-of-2028-ramp/)）。

三星（Samsung Foundry）2nm 节点 SF2 属于其第三代 GAA（MBCFET）技术，相较 3nm 工艺性能提升 12%、能效提升 25%、面积减少 5%（[Samsung Foundry Forum 2023](https://semiconductor.samsung.com/emea/news-events/news/samsung-electronics-unveils-foundry-vision-in-the-ai-era-at-samsung-foundry-forum-2023/)）。2026 年 9 月，三星位于美国得州泰勒（Taylor）的工厂已开始在 2nm 工艺上生产晶圆，进入特斯拉 AI5 芯片的原型生产阶段（[电子工程专辑：三星得州泰勒工厂提前启动特斯拉AI5芯片试生产](https://www.eet-china.com/news/202609208226.html)）。三星与 Broadcom 也已扩大战略合作，涵盖 HBM 供货与 2nm 及以下制程（[Samsung and Broadcom Expand Strategic Collaboration](https://news.samsung.com/global/samsung-electronics-and-broadcom-expand-strategic-collaboration-across-memory-and-foundry-technologies)）。

### High-NA EUV 光刻进入量产
ASML 的 High-NA EUV 取得关键里程碑：Intel Foundry 已在其 18A 部分层使用 ASML EXE High-NA EUV 系统，对代号 Panther Lake 的部分 Intel Core Ultra Series 3 处理器进入高量产制造（[ASML: High NA EUV reaches new readiness milestone](https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone)）。Intel 也是首家安装并通过第二代 TWINSCAN EXE:5200B 验收测试的公司，该机基于 EXE:5000，提升产能与套刻精度。Intel 披露，High-NA 在其产线累计已处理超过一百万片晶圆（[Intel Foundry and ASML Collaborate to Accelerate Industry Readiness for High NA EUV](https://www.intel.cn/content/www/us/en/newsroom/news/intel-foundry/intel-foundry-asml-accelerate-industry-readiness-for-high-na-euv.html)）。

据媒体报道，EXE:5200B 单台售价约 4 亿美元，分辨率约 8nm（[麻省理工科技评论中文站](https://www.mittrchina.com/news/detail/16551)）。ASML 在 2026 年第二季度电话会上表示，预计全年出货约 65 台 Low-NA EUV 系统，EUV 净系统销售额同比增长超 45%（[ASML Q2 2026 results](https://ourbrand.asml.com/asset/1fd3908a-0381-47b5-9b69-a3094f656651/2026_07_15-ASML-Transcript-investor-call-Q2-2026.pdf)）。

### 先进封装与 HBM：真正的瓶颈
AI 芯片的产能瓶颈已从晶圆制造转向先进封装。TSMC 的 CoWoS（Chip-on-Wafer-on-Substrate）产能从 2024 年下半年的约 3.5 万片/月，计划提升至 2026 年底的约 13 万片/月（[TSMC CoWoS/SoIC 产能战略](https://troy-technical.jp/ai%E9%9C%80%E8%A6%81%E3%81%AE%E6%80%A5%E5%A2%97%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%99%E3%82%8Btsmc%E3%81%AEcowos-soic%E7%94%9F%E7%94%A3%E8%83%BD%E5%8A%9B%E6%88%A6%E7%95%A5%EF%BC%9A2026%E5%B9%B4%E6%9C%AB/)）。卖方与行业媒体估计，2026 年底 CoWoS 月产能集中在 12–14 万片，而年需求接近百万片量级，NVIDIA 约占其中 60%（[TSMC CoWoS: A Full Guide](https://www.insidedeeptech.com/tsmc-cowos-packaging-full-guide/)）。另有报道称台积电计划到 2028 年将 CoWoS 产能翻倍至约 26 万片/月，并推出 14 倍光罩（14-reticle）方案以支持 10 颗计算 die 与 20 个 HBM 堆栈（[RCR Tech: TSMC reportedly plans to double CoWoS capacity by 2028](https://rcrtech.com/semiconductor-news/tsmc-double-cowos-capacity-by-2028/)）。

3D 堆叠方面，TSMC 的 SoIC 技术将扩展至最先进平台，A14-to-A14 SoIC 计划 2029 年量产，die-to-die I/O 密度相较 N2-on-N2 SoIC 提升 1.8 倍（[TSMC Debuts A13 Technology](https://pr.tsmc.com/english/news/3302)）。HBM 方面，三星已出货业界首个商用 HBM4，12 层堆叠容量 24–36GB，并计划引入 16 层堆叠扩展至最高 48GB；其数据 I/O 从 1,024 翻倍至 2,048（[Samsung Ships Industry-First Commercial HBM4](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing)）。SK hynix 展示了 16 层 48GB HBM4，并强调其 base die 由 TSMC 先进逻辑工艺制造（[SK hynix at TSMC Symposium 2026](https://news.skhynix.com/tsmc-technology-symposium-2026/)）。

### Chiplet 开放标准：UCIe 3.0
开放小芯片互连标准 UCIe 3.0 于 2025 年 8 月发布，将 UCIe-S/UCIe-A 数据速率翻倍至 48 GT/s 与 64 GT/s，并引入连续传输协议、运行时 TX 重校准、L2 优化等增强（[UCIe Specifications](https://www.uciexpress.org/specifications)、[Chiplet Summit 2026: UCIe Momentum](https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem)）。

### 补贴与供应链韧性
美国《芯片法案》（CHIPS Act）已落地多项大额直接补贴：Intel 约 78.6 亿美元（另通过 Secure Enclave 获 30 亿美元）、TSMC 亚利桑那 66 亿美元直接拨款 + 50 亿美元贷款担保、三星泰勒 47.45 亿美元、Micron 61.65 亿美元（[CRS 报告](https://www.everycrsreport.com/reports/R49031.html)、[CHIPS Act: $52B Semiconductor Investment](https://consumerelectronicsdaily.com/chip-supply/chips-act-semiconductor-investment/)）。2026 年 4 月美国国会听证材料显示，美政府以约 89 亿美元入股 Intel（含 57 亿美元未支付的芯片法案奖励与 32 亿美元 Secure Enclave 资金），并推动 Micron 承诺 2000 亿美元、TSMC 追加 1000 亿美元本土投资（[美国众议院听证备忘录](https://docs.house.gov/meetings/IF/IF17/20260415/119148/HHRG-119-IF17-20260415-SD002.pdf)）。

欧盟方面，《欧洲芯片法案》通过"芯片欧洲计划"提供最高 33 亿欧元，其中 Horizon Europe 与 Digital Europe 各 16.5 亿欧元；2026 年欧盟委员会还陆续批准德国多项国家援助，如 6.59 亿欧元支持四座新半导体设施、2.88 亿欧元支持 Carl Zeiss 等（[European Chips Act 预算](https://commission.europa.eu/strategy-and-policy/eu-budget/motion/focus/eu-budget-bolsters-europes-technological-leadership-european-chips-act_en)、[欧盟理事会文件](https://data.consilium.europa.eu/doc/document/ST-10094-2026-ADD-1/en/pdf)）。

## 核心技术与关键概念

- **GAA（Gate-All-Around）环栅晶体管**：用纳米片（nanosheet）沟道四面被栅极包裹，取代 FinFET 的三面接触，改善静电控制与漏电。台积电 N2/A14、Intel RibbonFET、三星 MBCFET 均属此类。
- **背面供电（BSPDN）**：把供电网络移到晶圆背面，释放正面走线空间、降低 IR drop。Intel 18A 的该技术名为 PowerVia，利用嵌入每个标准单元的 nano-TSV 供电（[Intel Foundry HPC/AI Brief](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2025-11/intel-foundry-hpc-ai-brief.pdf)）；台积电 A16 的对应方案为 Super Power Rail（SPR），采用背面直接接触方案（[IEEE: A16 Angstrom-Class CMOS](https://xplorestaging.ieee.org/document/11577475)）。业界普遍认为在 2nm 时代，BSPDN 已从"可选"变为"必需"（[BSPDN: The Structural Revolution](https://techmacroarchive.com/bspdn-2nm-foundry-revolution-2026/)）。
- **High-NA EUV**：数值孔径从 0.33 提升到 0.55，分辨率更高，可用更少曝光次数实现更小特征尺寸，但单台成本极高（约 4 亿美元）。
- **先进封装**：CoWoS 把逻辑 die 与 HBM 并排放在中介层上；SoIC 实现 die 垂直堆叠；Chiplet 通过 UCIe 等开放接口组合不同工艺的裸片。
- **HBM3E / HBM4**：HBM4 将单堆栈接口位宽从 1,024 bit 翻倍到 2,048 bit，容量从 12 层 36GB 向 16 层 48GB 演进。

## 关键数据

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| TSMC N2 量产 | 2025 Q4 进入量产，2026 快速爬坡 | [TSMC 2nm](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm) |
| TSMC N2P / A16 | 2026 下半年量产 | [TSMC 2025 Annual Report](https://investor.tsmc.com/static/annualReports/2025/english/index.html) |
| TSMC A14 / A13 | 2028 / 2029 量产 | [TSMC A14](https://www.tsmc.com/japanese/dedicatedFoundry/technology/logic/l_A14) |
| Intel 18A | 2025 Q4 风险量产，2026 大规模量产；Panther Lake 首发 | [CES 2026 Intel](https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a) |
| Intel 14A | 2027 H2 风险试产，2028 量产 | [TrendForce](https://www.trendforce.com/news/2026/09/01/news-intel-cfo-says-14a-defect-reduction-fastest-since-22nm-customer-talks-reportedly-grow-ahead-of-2028-ramp/) |
| ASML High-NA EXE:5200B | 单台约 4 亿美元，分辨率约 8nm | [麻省理工科技评论中文站](https://www.mittrchina.com/news/detail/16551) |
| TSMC CoWoS 产能 | 2026 年底约 13 万片/月 | [TSMC CoWoS/SoIC 产能战略](https://troy-technical.jp/ai%E9%9C%80%E8%A6%81%E3%81%AE%E6%80%A5%E5%A2%97%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%99%E3%82%8Btsmc%E3%81%AEcowos-soic%E7%94%9F%E7%94%A3%E8%83%BD%E5%8A%9B%E6%88%A6%E7%95%A5%EF%BC%9A2026%E5%B9%B4%E6%9C%AB/) |
| Samsung HBM4 | 12 层 24–36GB，规划 16 层 48GB | [Samsung HBM4](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing) |
| UCIe 3.0 | 2025 年 8 月发布，48/64 GT/s | [UCIe Specifications](https://www.uciexpress.org/specifications) |
| 美国 CHIPS 补贴 | Intel 78.6 亿、TSMC 66 亿、Samsung 47.45 亿、Micron 61.65 亿美元 | [CRS 报告](https://www.everycrsreport.com/reports/R49031.html) |

## 趋势与争议

1. **产能瓶颈从制程转向封装与 HBM**：即便台积电、Intel、三星的先进制程产能持续扩张，CoWoS 与 HBM 供给仍是 AI 芯片出货的硬约束。行业有分析将 2026 年形容为"AI 单点引爆需求、8 英寸成熟产能与先进封装同时卡住"的一年，涨价从个别品类外溢为全行业共识（[与非网：2026年芯片行情](https://m.eefocus.com/article/2085777.html)）。
2. **成熟制程过剩与价格战**：28nm 及以上成熟节点在前期投资潮后出现供给过剩。中国大陆厂商持续扩产，SMIC 2026 年 Q1 产能利用率达 93.5%，28nm 及以上逻辑代工出口价格上浮 8–12%（[SMIC Q1 2026](https://www.qishuai-cn.com/news/SMIC_Q1_2026_Utilization_at_93_5_28nm_Logic_Foundry_Export_Prices_Up_8_12_.html)）。成熟制程的供需与地缘博弈将持续。
3. **出口管制与技术自主**：受美方出口管制限制，中国大陆最先进的可量产节点约为 7nm 级（SMIC），因无法获取 ASML EUV 设备而受限；这也推动本土在成熟制程、特色工艺、Chiplet 与自主算力配套上的结构性机会。
4. **High-NA EUV 的成本门槛**：单台设备约 4 亿美元，且良率、套刻、产能仍处爬坡期，业界对"是否所有层都要用 High-NA"仍有争议，目前主要是 Intel 在 18A 部分层先行使用。
5. **补贴与"产能回流"的可持续性**：美国以股权入股 Intel、以政策撬动 TSMC/Micron 追加投资，引发对政府直接干预产业、以及长期产能过剩风险的讨论。

## 参考来源

1. [TSMC 2nm Technology](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm)
2. [TSMC 2026 Annual Shareholders' Meeting Agenda（PDF）](https://investor.tsmc.com/sites/ir/shareholders-meeting/2026-06-04/2026AGM_Agenda_wmn.pdf)
3. [TSMC 2025 Annual Report Website](https://investor.tsmc.com/static/annualReports/2025/english/index.html)
4. [TSMC 2025 Operational Highlights（PDF）](https://investor.tsmc.com/static/annualReports/2025/english/pdf/2025_tsmc_ar_e_ch5.pdf)
5. [TSMC Debuts A13 Technology at 2026 North America Technology Symposium](https://pr.tsmc.com/english/news/3302)
6. [TSMC A14 Technology](https://www.tsmc.com/japanese/dedicatedFoundry/technology/logic/l_A14)
7. [Intel 18A Process Node（PDF）](https://www.intel.de/content/dam/www/central-libraries/us/en/documents/2025-03/foundry-18a-platform-brief.pdf)
8. [Intel Foundry HPC/AI Platform Brief（PDF）](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2025-11/intel-foundry-hpc-ai-brief.pdf)
9. [Intel Foundry Process Roadmap（PDF）](https://download.intel.com/newsroom/2025/foundry/Intel-Foundry-Direct-Connect-Roadmap-Infographic.pdf)
10. [CES 2026: Intel Core Ultra Series 3 Debut as First Built on Intel 18A](https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a)
11. [Intel Unveils Panther Lake Architecture: First AI PC Platform Built on 18A](https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a)
12. [Intel Foundry and ASML Collaborate to Accelerate Industry Readiness for High NA EUV](https://www.intel.cn/content/www/us/en/newsroom/news/intel-foundry/intel-foundry-asml-accelerate-industry-readiness-for-high-na-euv.html)
13. [ASML: High NA EUV reaches new readiness milestone](https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone)
14. [ASML EUV lithography systems](https://www.asml.com/en/en/products/euv-lithography-systems)
15. [ASML Q2 2026 results transcript（PDF）](https://ourbrand.asml.com/asset/1fd3908a-0381-47b5-9b69-a3094f656651/2026_07_15-ASML-Transcript-investor-call-Q2-2026.pdf)
16. [ASML reports Q1 2026 results（PDF）](https://ourbrand.asml.com/asset/d7b914e6-fdd1-4262-b805-d80f3efcb39a/2026_04_15_Presentation-Investor-Relations-Q1-2026.pdf)
17. [麻省理工科技评论中文站：ASML 新一代光刻机 EXE:5200B](https://www.mittrchina.com/news/detail/16551)
18. [TSMC Debuts A13 Technology（中文）](https://pr.tsmc.com/schinese/news/3302)
19. [Samsung Ships Industry-First Commercial HBM4](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing)
20. [Samsung: The HBM4 Infographic](https://news.samsungsemiconductor.com/global/video-the-hbm4-infographic-key-specs-and-performance-leap/)
21. [SK hynix Presents Vision at TSMC Symposium 2026](https://news.skhynix.com/tsmc-technology-symposium-2026/)
22. [Samsung Foundry Vision in the AI Era（SF2）](https://semiconductor.samsung.com/emea/news-events/news/samsung-electronics-unveils-foundry-vision-in-the-ai-era-at-samsung-foundry-forum-2023/)
23. [电子工程专辑：三星得州泰勒工厂提前启动特斯拉AI5芯片试生产](https://www.eet-china.com/news/202609208226.html)
24. [Samsung Electronics and Broadcom Expand Strategic Collaboration](https://news.samsung.com/global/samsung-electronics-and-broadcom-expand-strategic-collaboration-across-memory-and-foundry-technologies)
25. [TSMC CoWoS: A Full Guide to the Packaging Line That Gates AI GPUs](https://www.insidedeeptech.com/tsmc-cowos-packaging-full-guide/)
26. [TSMC's CoWoS Packaging Capacity Grew 9x in Three Years](https://xenospectrum.com/en/cowos-packaging-bottleneck-nvidia/)
27. [RCR Tech: TSMC reportedly plans to double CoWoS capacity by 2028](https://rcrtech.com/semiconductor-news/tsmc-double-cowos-capacity-by-2028/)
28. [AI需要急増に対応するTSMCのCoWoS/SoIC生産能力戦略](https://troy-technical.jp/ai%E9%9C%80%E8%A6%81%E3%81%AE%E6%80%A5%E5%A2%97%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%99%E3%82%8Btsmc%E3%81%AEcowos-soic%E7%94%9F%E7%94%A3%E8%83%BD%E5%8A%9B%E6%88%A6%E7%95%A5%EF%BC%9A2026%E5%B9%B4%E6%9C%AB/)
29. [UCIe Specifications](https://www.uciexpress.org/specifications)
30. [Chiplet Summit 2026: UCIe Momentum Across a Growing Ecosystem](https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem)
31. [Introducing the UCIe 3.0 Specification（PDF）](https://www.uciexpress.org/_files/ugd/0c1418_b4744fe368c94e3e9c7eaa13ead632bf.pdf)
32. [IEEE: A16 Angstrom-Class CMOS Technology with Super Power Rail](https://xplorestaging.ieee.org/document/11577475)
33. [BSPDN: The Structural Revolution Saving 2nm AI Chip ROI in 2026](https://techmacroarchive.com/bspdn-2nm-foundry-revolution-2026/)
34. [Semiconductor Fabrication Facilities Funded by the CHIPS Act（CRS）](https://www.everycrsreport.com/reports/R49031.html)
35. [CHIPS Act: $52B Semiconductor Investment, Fab Buildout, and Export Controls](https://consumerelectronicsdaily.com/chip-supply/chips-act-semiconductor-investment/)
36. [TSMC, Intel, Samsung US Fab Investments: Policy Timeline](https://consumerelectronicsdaily.com/chip-supply/tsmc-intel-samsung-us-fab-investments/)
37. [美国众议院听证备忘录（2026-04-15，PDF）](https://docs.house.gov/meetings/IF/IF17/20260415/119148/HHRG-119-IF17-20260415-SD002.pdf)
38. [The EU budget bolsters Europe's technological leadership: the European Chips Act](https://commission.europa.eu/strategy-and-policy/eu-budget/motion/focus/eu-budget-bolsters-europes-technological-leadership-european-chips-act_en)
39. [欧盟理事会文件 ST-10094-2026（PDF）](https://data.consilium.europa.eu/doc/document/ST-10094-2026-ADD-1/en/pdf)
40. [欧委会批准德国6.59亿欧元半导体援助](https://germany.representation.ec.europa.eu/nachrichten-und-veranstaltungen/pressemitteilungen/vier-neue-halbleiteranlagen-kommission-genehmigt-beihilfe-deutschlands-hohe-von-659-millionen-euro-2026-07-14_es)
41. [欧委会批准德国2.88亿欧元半导体援助](https://germany.representation.ec.europa.eu/news/halbleiter-produktion-eu-kommission-genehmigt-beihilfe-deutschlands-hohe-von-288-millionen-euro-2026-05-20_de)
42. [与非网：满产、涨价、排队——2026年芯片行情](https://m.eefocus.com/article/2085777.html)
43. [SMIC Q1 2026 Utilization at 93.5%](https://www.qishuai-cn.com/news/SMIC_Q1_2026_Utilization_at_93_5_28nm_Logic_Foundry_Export_Prices_Up_8_12_.html)
44. [TrendForce: Intel CFO Says 14A Defect Reduction Fastest Since 22nm](https://www.trendforce.com/news/2026/09/01/news-intel-cfo-says-14a-defect-reduction-fastest-since-22nm-customer-talks-reportedly-grow-ahead-of-2028-ramp/)
45. [新浪财经：英特尔14A缺陷密度曲线系22nm以来最佳](https://finance.sina.com.cn/stock/t/2026-08-27/doc-inipuqhs0655612.shtml)