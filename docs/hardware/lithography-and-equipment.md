# 光刻与半导体设备

> 最后更新：2026-09-26 ｜ 领域：硬件·芯片与设计 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

半导体制造设备通常分为前道（晶圆制造）与后道（封装测试）两大类。前道核心环节包括光刻、刻蚀、薄膜沉积（CVD/PVD/ALD）、离子注入、扩散/退火、清洗、CMP 与量测/检测。其中光刻决定最小可分辨线宽与套刻精度，是技术门槛与资本密集度最高的环节，也是先进制程迭代的节奏控制器。

产业格局高度集中：ASML 是目前全球唯一实现 EUV（极紫外）光刻机量产供应的企业，其新一代 High-NA EUV（EXE 系列）采用 0.55 高数值孔径光学系统，分辨率达 8nm，官方规划用于 2nm 及以下先进逻辑与高密度存储芯片的大规模量产（[先进制程迭代加速 前道制造设备革新全面提速](https://epaper.cena.com.cn/pc/attachment/202603/20/2da929dc-3390-4a42-83fa-981be69f40fb.pdf)）。刻蚀与沉积则由 Lam Research、Applied Materials、Tokyo Electron 等主导，中国厂商在成熟制程环节加速替代。

## 最新进展（2025–2026）

**ASML 业绩与产能扩张。** ASML 2026 年第二季度实现总净销售额 93 亿欧元、净利润 29 亿欧元，并上调全年展望至 430 亿至 450 亿欧元总净销售额、54%–56% 毛利率（[ASML reports €9.3 billion total net sales and €2.9 billion net income in Q2 2026](https://ourbrand.asml.com/asset/9078cf4d-91fd-4dd9-a5d5-d1caab6dc046/2026_07_15_Presentation-Investor-Relations-Q2-2026.pdf)、[ASML Press releases & announcements](https://www.asml.com/en/news/press-releases)）。第三季度指引为总净销售额 110 亿至 120 亿欧元、毛利率 55%–57%、研发费用约 12 亿欧元（[同前投资者材料](https://ourbrand.asml.com/asset/9078cf4d-91fd-4dd9-a5d5-d1caab6dc046/2026_07_15_Presentation-Investor-Relations-Q2-2026.pdf)）。管理层表示 2026 年将出货约 65 台 Low-NA EUV 系统，EUV 净系统销售额同比增长超过 45%，需求由 DRAM 与先进逻辑共同驱动；并计划在 2026 年约 65 台的 NXE 产能基础上为 2027 年再增 30%，同时研究 2028 年再增 30%（[ASML Q2 2026 results investor call transcript](https://ourbrand.asml.com/asset/1fd3908a-0381-47b5-9b69-a3094f656651/2026_07_15-ASML-Transcript-investor-call-Q2-2026.pdf)、[ASML Interim Management Report 2026](https://ourbrand.asml.com/asset/468514ab-2a25-42be-a284-1560ebebcb6a/Statutory-Interim-Report-2026.pdf)）。此前 2025 年第四季度，ASML 净系统销售额为 76 亿欧元，其中 EUV 为 36 亿欧元并包含两台 High-NA 系统（[ASML Q4/FY 2025 results](https://ourbrand.asml.com/m/285dcba22c2bf203/original/2026_01_28-ASML-Transcript-investor-call-Q4-2025.pdf)）。

**High-NA EUV 进入量产验证阶段。** 2026 年 9 月，ASML 在 SEMICON Taiwan 披露全球 4 个客户的 10 台 High-NA EUV 系统已投运、另有 3 台在途，累计曝光超过 135 万片晶圆；通过认证的 EXE:5200B 达到每小时 135 片晶圆的量产吞吐量，机队可用率 84%（[百万片晶圆之后：英特尔与台积电，谁在改写光刻终局？](https://www.tmtpost.com/agent/ai-article/20252)）。ASML 官方声明称，Intel Foundry 已在其 Intel Core Ultra 系列 3（代号 Panther Lake）的部分产品上进入采用 EXE High-NA EUV 技术的高量产阶段，Intel Foundry 也是首家安装并通过第二代 TWINSCAN EXE:5200B 验收测试的公司，该机型基于 EXE:5000 提升了产能、套刻精度与光源性能（[High NA EUV reaches new readiness milestone with first high-volume Logic product](https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone)）。ASML 2026 年股东大会材料显示，2025 年底已出货 8 台 High-NA、其中 6 台在运行，公司给出的时间表是 2026 年底满足量产要求、客户导入集中在 2027–2028 年（[Intel Deploys High-NA EUV in Mass Production for the First Time](https://xenospectrum.com/en/intel-18a-high-na-euv-panther-lake-volume-production/)、[High-NA EUV (TWINSCAN EXE)](https://www.ventureatlas.org/product/asml-high-na-euv-twinscan-exe)）。吞吐量路线图上，EXE:5200C 目标 160 wph、EXE:5200D 175 wph、EXE:5400E 180 wph、规划中的 EXE:5600 超过 250 wph（[High-NA EUV (TWINSCAN EXE)](https://www.ventureatlas.org/product/asml-high-na-euv-twinscan-exe)）。

**刻蚀与沉积的设备创新。** Applied Materials 在 2026 财年第三季度财报中介绍，公司推出新的沉积与刻蚀系统以帮助客户在逻辑与存储上延续微缩，其中 Centris Spectral SiN ALD 利用微波等离子技术在挑战性 3D 结构中实现均匀氮化硅沉积，Producer Selectra Mo Etch 选择性去除钼（[Applied Materials Announces Third Quarter 2026 Results](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-third-quarter-2026-results)）。该季度总收入约 210 亿美元量级（重述口径），下季度指引约 102.5 亿美元（[Applied Materials Third Quarter Fiscal 2026 Earnings Presentation](https://appliedmaterials.gcs-web.com/static-files/9d5d182d-f060-4b22-a32c-4582257fdc9b)）。Lam Research 截至 2026 年 6 月 28 日的季度收入为 67.2 亿美元，滚动十二个月收入 232.3 亿美元（[Lam Research Reports Financial Results for the Quarter Ended June 28, 2026](https://investor.lamresearch.com/2026-07-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-June-28,-2026?asPDF=1)）。该公司把 2026 年晶圆制造设备（WFE）支出展望从 1350 亿–1400 亿美元上调到"1500 亿美元低位区间"，理由包括 AI 需求导致晶圆厂产能紧张，并预计到 2027 年将新增 8 至 10 座领先制程晶圆厂；同时指出环绕栅极（GAA）、背面供电与先进封装扩大了其可服务市场（[Lam Research Lifts 2026 WFE Outlook as AI Demand Strains Fab Capacity](https://www.marketbeat.com/instant-alerts/event-lam-research-lifts-2026-wfe-outlook-as-ai-demand-strains-fab-capacity-2026-09-11/)）。

**行业设备支出创纪录。** SEMI 2026 年 7 月发布的中期预测显示，2026 年全球半导体制造设备 OEM 总销售额将达 1659 亿美元，同比增长 23.2%，并预计增长延续至 2028 年、总额达 2290 亿美元以上（[Global Semiconductor Equipment Sales Forecast to Reach a Record $229 Billion in 2028](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports)、[SEMI报告：2028年全球半导体设备销售额预计创纪录](https://www.semi.org.cn/site/semi/article/88d23b6850284acb8ecc6f06c0a59828.html)）。需要注意口径变化：SEMI 2025 年 12 月的年终预测曾给出 2025 年 1330 亿美元、同比增长 13.7%，并预测 2027 年 1560 亿美元（[Global Semiconductor Equipment Sales Projected to Reach a Record of $156 Billion in 2027](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports)），与 2026 年 7 月的中期预测相比上修幅度显著，引用时应区分发布时间。

**中国设备的国产化推进。** 国内光刻机整机方面，上海微电子主推 90nm 成熟制程产品（SSX/SSA600 系列步进扫描投影光刻机），其 SSX600 系列（支持 90nm 及以下制程）出货量占国内光刻机市场份额超过 80%，但绝对销售额相比美日企业仍有差距（[放下"先进制程"执念，"成熟制程"引领半导体设备逆势狂欢](https://stcn.com/article/detail/3917099.html)）。另有报告称上海微电子 90nm 制程光刻机已实现稳定量产与规模出货，采用 KrF 光源，可满足 130nm 及以上成熟制程需求（[2026年中国光刻机报告下载：16亿市场规模与竞争格局演变](https://www.baogaobox.com/insights/260508000027273.html)）。刻蚀与薄膜设备方面，中微公司预计 2025 年营业收入约 123.85 亿元、同比增长约 36.62%，其中刻蚀设备约 98.32 亿元（+35.12%），LPCVD 与 ALD 等薄膜设备收入 5.06 亿元（+224.23%），归母净利润约 20.80 亿元（[中微公司预计2025年营收同比增长约37%](https://www.stcn.com/article/detail/3609771.html)）；2026 年上半年预计营收约 66.91 亿元、同比增长约 34.89%，归母净利润 27 亿至 29 亿元（[中微公司上半年净利润预增逾2.8倍](https://www.stcn.com/article/detail/4056714.html)）。北方华创 2024 年营收 298.38 亿元（+35.14%），2025 年前三季度营收 273.01 亿元（+32.97%）（[中微公司并购CMP设备公司，谁紧张了？](https://www.stcn.com/article/detail/3559589.html)）。关于国产浸没式 DUV 的产能，有海外单一媒体报道称 2026 年计划生产约 5 台浸没式 DUV 设备、2027 年提升至约 20 台并首批交付国内存储与晶圆厂，该信息仅有一处来源、未经官方确认，需谨慎对待（[Chinas Chipangriff auf ASML](https://www.deutschetageszeitung.de/Videos/4055-chinas-chipangriff-auf-asml.html?page=70)）。

**先进制程节点：2nm 量产与 GAA/背面供电。** 台积电 2nm（N2）已于 2025 年第四季度按计划进入量产，采用业界领先的第一代 nanosheet（纳米片）晶体管技术；据台积电 2025 年年报，N2 良率良好并预计 2026 年快速爬坡，N2P 与 A16 作为 N2 家族延伸、量产时间均定于 2026 年下半年，其中 A16 首次采用台积电称为"Super Power Rail（SPR）"的背面供电方案（[TSMC 2nm Technology](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm)、[TSMC 2025 Annual Report](https://investor.tsmc.com/static/annualReports/2025/english/index.html)）。更前沿的节点节奏为：A14（1.4nm 级，第二代 nanosheet）计划 2028 年量产；A13 通过约 97% 的光学微缩实现 6% 面积节省、设计规则与 A14 完全兼容，计划 2029 年量产（[TSMC Debuts A13 Technology](https://pr.tsmc.com/english/news/3302)、[TSMC A14 Technology](https://www.tsmc.com/japanese/dedicatedFoundry/technology/logic/l_A14)）。Intel 的 18A 是其首个在美国本土量产的 2nm 级节点，采用 RibbonFET 全环绕栅极晶体管与 PowerVia 背面供电（利用嵌入每个标准单元的 nano-TSV 供电）（[Intel 18A Platform Brief（PDF）](https://www.intel.de/content/dam/www/central-libraries/us/en/documents/2025-03/foundry-18a-platform-brief.pdf)、[Intel Foundry HPC/AI Brief（PDF）](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2025-11/intel-foundry-hpc-ai-brief.pdf)）；2026 年 1 月 CES 发布的第三代酷睿 Ultra（代号 Panther Lake）为首款基于 Intel 18A 的计算平台（[CES 2026: Intel Core Ultra Series 3](https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a)）。Intel 的 14A 计划 2026 年 10 月发布 0.9 版 PDK、2027 年下半年风险试产、2028 年大规模量产（[TrendForce: Intel CFO Says 14A Defect Reduction Fastest Since 22nm](https://www.trendforce.com/news/2026/09/01/news-intel-cfo-says-14a-defect-reduction-fastest-since-22nm-customer-talks-reportedly-grow-ahead-of-2028-ramp/)）。三星 2nm 节点 SF2 属其第三代 GAA（MBCFET）技术，相较 3nm 工艺性能提升 12%、能效提升 25%、面积减少 5%（[Samsung Foundry Forum 2023](https://semiconductor.samsung.com/emea/news-events/news/samsung-electronics-unveils-foundry-vision-in-the-ai-era-at-samsung-foundry-forum-2023/)）；2026 年 9 月其得州泰勒（Taylor）工厂已在 2nm 工艺上进入特斯拉 AI5 芯片的原型生产阶段（[电子工程专辑：三星得州泰勒工厂提前启动特斯拉AI5芯片试生产](https://www.eet-china.com/news/202609208226.html)）。

**产业补贴与政策。** 美国《芯片法案》（CHIPS Act）已落地多项大额直接补贴：Intel 约 78.6 亿美元（另通过 Secure Enclave 获 30 亿美元）、TSMC 亚利桑那 66 亿美元直接拨款 + 50 亿美元贷款担保、三星泰勒 47.45 亿美元、Micron 61.65 亿美元（[CRS 报告](https://www.everycrsreport.com/reports/R49031.html)、[CHIPS Act: $52B Semiconductor Investment](https://consumerelectronicsdaily.com/chip-supply/chips-act-semiconductor-investment/)）；2026 年 4 月美国国会听证材料显示，美政府以约 89 亿美元入股 Intel（含 57 亿美元未支付的芯片法案奖励与 32 亿美元 Secure Enclave 资金），并推动 Micron 承诺 2000 亿美元、TSMC 追加 1000 亿美元本土投资（[美国众议院听证备忘录（PDF）](https://docs.house.gov/meetings/IF/IF17/20260415/119148/HHRG-119-IF17-20260415-SD002.pdf)）。欧盟《欧洲芯片法案》通过"芯片欧洲计划"提供最高 33 亿欧元（Horizon Europe 与 Digital Europe 各 16.5 亿欧元），2026 年欧盟委员会还陆续批准德国多项国家援助，如 6.59 亿欧元支持四座新半导体设施、2.88 亿欧元支持 Carl Zeiss 等（[European Chips Act 预算](https://commission.europa.eu/strategy-and-policy/eu-budget/motion/focus/eu-budget-bolsters-europes-technological-leadership-european-chips-act_en)、[欧盟理事会文件（PDF）](https://data.consilium.europa.eu/doc/document/ST-10094-2026-ADD-1/en/pdf)、[欧委会批准德国6.59亿欧元半导体援助](https://germany.representation.ec.europa.eu/nachrichten-und-veranstaltungen/pressemitteilungen/vier-neue-halbleiteranlagen-kommission-genehmigt-beihilfe-deutschlands-hohe-von-659-millionen-euro-2026-07-14_es)、[欧委会批准德国2.88亿欧元半导体援助](https://germany.representation.ec.europa.eu/news/halbleiter-produktion-eu-kommission-genehmigt-beihilfe-deutschlands-hohe-von-288-millionen-euro-2026-05-20_de)）。

**成熟制程供需与地缘约束。** 28nm 及以上成熟节点在前期投资潮后出现供给过剩，中国大陆厂商持续扩产：SMIC 2026 年 Q1 产能利用率达 93.5%，28nm 及以上逻辑代工出口价格上浮 8–12%（[SMIC Q1 2026 Utilization at 93.5%](https://www.qishuai-cn.com/news/SMIC_Q1_2026_Utilization_at_93_5_28nm_Logic_Foundry_Export_Prices_Up_8_12_.html)）；行业有分析把 2026 年形容为"AI 单点引爆需求、8 英寸成熟产能与先进封装同时卡住"的一年，涨价从个别品类外溢为全行业共识（[与非网：满产、涨价、排队——2026年芯片行情](https://m.eefocus.com/article/2085777.html)）。受美方出口管制限制，中国大陆无法获取 ASML EUV 设备，其最先进的可量产节点约为 7nm 级（SMIC），这也推动了本土在成熟制程、特色工艺、Chiplet 与自主算力配套上的结构性机会（[Chinas Chipangriff auf ASML](https://www.deutschetageszeitung.de/Videos/4055-chinas-chipangriff-auf-asml.html?page=70)、[放下"先进制程"执念，"成熟制程"引领半导体设备逆势狂欢](https://stcn.com/article/detail/3917099.html)）。

## 核心技术与关键概念

- **光刻光源与路线：** 从 i-line、KrF、ArF 干式到 ArF 浸没式（193nm 加多重曝光），再到 EUV（13.5nm）。EUV 是唯一可支撑 7nm 以下单次曝光关键层的技术，High-NA（0.55 NA）通过更大数值孔径提升分辨率与成像对比度，可减少制程步骤、降低缺陷（[先进制程迭代加速 前道制造设备革新全面提速](https://epaper.cena.com.cn/pc/attachment/202603/20/2da929dc-3390-4a42-83fa-981be69f40fb.pdf)）。
- **套刻与产能指标：** High-NA 的商业化关键不只是分辨率，还包括套刻精度、吞吐量（wph）与机台可用率；ASML 披露的 135 wph 与 84% 可用率即为核心可量产性证据（[百万片晶圆之后](https://www.tmtpost.com/agent/ai-article/20252)）。
- **刻蚀与沉积：** 随着 GAA 晶体管、3D DRAM、钼等新金属化与高深宽比结构出现，选择性刻蚀与原子层沉积（ALD）的重要性上升。Lam Research 明确把 GAA 与背面供电视为增长机会（[Lam Research Lifts 2026 WFE Outlook](https://www.marketbeat.com/instant-alerts/event-lam-research-lifts-2026-wfe-outlook-as-ai-demand-strains-fab-capacity-2026-09-11/)）。中微公司称其超高深宽比刻蚀设备可在宽度仅为头发丝万分之一的沟槽中刻出深度为宽度 90 倍的结构，下一代产品面向 3D DRAM（[国产半导体设备企业迎来"黄金大年"](https://finance.sina.com.cn/jjxw/2026-07-05/doc-iniftwia8958459.shtml)）。
- **量测与检测：** 良率学习依赖缺陷检测与量测的精度与速度。AMAT 强调新系统可帮助客户快速区分关键缺陷与干扰信号（[Applied Materials Announces Third Quarter 2026 Results](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-third-quarter-2026-results)）。
- **供应格局与国产化分层：** 光刻由 ASML 独占 EUV；刻蚀由 Lam、TEL、AMAT 主导，中国厂商在部分环节国产化率已超 20%；ALD 由 TEL、AMAT 主导，北方华创、拓荆科技等跟进（[半导体产业与人工智能产业周期复苏及投资建议](https://m.book118.com/try_down/366125215230011013.pdf)）。

## 代表性项目 / 公司 / 产品（附官方链接）

| 公司 | 领域 | 链接 |
| --- | --- | --- |
| ASML | EUV/DUV 光刻机、量测 | [asml.com](https://www.asml.com/en/news/press-releases) |
| Applied Materials | 沉积、刻蚀、离子注入、量测 | [ir.appliedmaterials.com](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-third-quarter-2026-results) |
| Lam Research | 刻蚀、沉积、清洗 | [investor.lamresearch.com](https://investor.lamresearch.com/2026-07-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-June-28,-2026?asPDF=1) |
| 上海微电子装备（SMEE） | 90nm 步进扫描投影光刻机 | [放下"先进制程"执念](https://stcn.com/article/detail/3917099.html) |
| 中微公司（AMEC） | 刻蚀、LPCVD/ALD | [中微公司业绩公告报道](https://www.stcn.com/article/detail/4056714.html) |
| 北方华创 | 刻蚀、薄膜、炉管设备 | [中微公司并购CMP设备公司](https://www.stcn.com/article/detail/3559589.html) |

## 关键数据与评测结果（附来源）

- ASML 2026 年 Q2：总净销售额 93 亿欧元、净利润 29 亿欧元；全年展望 430–450 亿欧元（[ASML Q2 2026 投资者材料](https://ourbrand.asml.com/asset/9078cf4d-91fd-4dd9-a5d5-d1caab6dc046/2026_07_15_Presentation-Investor-Relations-Q2-2026.pdf)）。
- 2026 年 Low-NA EUV 出货计划约 65 台，EUV 净系统销售额同比增长逾 45%（[ASML Q2 2026 电话会记录](https://ourbrand.asml.com/asset/1fd3908a-0381-47b5-9b69-a3094f656651/2026_07_15-ASML-Transcript-investor-call-Q2-2026.pdf)）。
- High-NA：10 台投运、3 台在途、累计曝光超 135 万片晶圆、EXE:5200B 达 135 wph、可用率 84%（[百万片晶圆之后](https://www.tmtpost.com/agent/ai-article/20252)）。
- 2025 年全球半导体设备销售额 1330 亿美元（+13.7%，SEMI 2025 年 12 月口径）；2026 年预测 1659 亿美元（+23.2%，SEMI 2026 年 7 月口径）（[SEMI 年终预测](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports)、[SEMI 中期预测](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports)）。
- 2026 年 WFE 支出展望：由 1350 亿–1400 亿美元上调至 1500 亿美元低位区间（[Lam Research Lifts 2026 WFE Outlook](https://www.marketbeat.com/instant-alerts/event-lam-research-lifts-2026-wfe-outlook-as-ai-demand-strains-fab-capacity-2026-09-11/)）。

## 趋势与争议

1. **High-NA 的采用节奏。** ASML 官方时间表把客户量产导入放在 2027–2028 年，而 Intel 已在部分产品上使用 High-NA 进入高量产，二者的表述口径存在差异：前者指广泛量产导入，后者指局部 SKU。业界对 High-NA 是否会大范围取代 Low-NA 多重曝光仍有分歧，成本与机台可用率是关键变量。
2. **产能扩张与 DRAM 需求共振。** ASML 明确把 EUV 需求增长归因于 DRAM 与先进逻辑双轮驱动，存储厂商在 HBM 上的资本开支成为设备订单的重要来源。
3. **设备市场预测频繁上修。** SEMI 在半年内把 2026/2028 的预测大幅上调，说明 AI 相关投资对设备支出的拉动超出此前模型假设，但也意味着预测偏差风险上升。
4. **国产替代的分层现实。** 中国大陆在成熟制程设备上替代较快（刻蚀、清洗、部分薄膜环节），但高端光刻仍高度依赖进口；关于国产浸没式 DUV 进度的公开信息多为单一来源，缺乏官方确认。
5. **出口管制与供应链不确定性。** 先进设备出口限制改变了厂商的地域收入结构，也加速了中国设备厂商在成熟节点环节的市场份额提升。

## 参考来源

1. [先进制程迭代加速 前道制造设备革新全面提速](https://epaper.cena.com.cn/pc/attachment/202603/20/2da929dc-3390-4a42-83fa-981be69f40fb.pdf)
2. [ASML Press releases & announcements](https://www.asml.com/en/news/press-releases)
3. [ASML reports €9.3 billion total net sales and €2.9 billion net income in Q2 2026](https://ourbrand.asml.com/asset/9078cf4d-91fd-4dd9-a5d5-d1caab6dc046/2026_07_15_Presentation-Investor-Relations-Q2-2026.pdf)
4. [ASML Q2 2026 results（investor call transcript）](https://ourbrand.asml.com/asset/1fd3908a-0381-47b5-9b69-a3094f656651/2026_07_15-ASML-Transcript-investor-call-Q2-2026.pdf)
5. [ASML Statutory Interim Report 2026](https://ourbrand.asml.com/asset/468514ab-2a25-42be-a284-1560ebebcb6a/Statutory-Interim-Report-2026.pdf)
6. [ASML Q4/FY 2025 results transcript](https://ourbrand.asml.com/m/285dcba22c2bf203/original/2026_01_28-ASML-Transcript-investor-call-Q4-2025.pdf)
7. [High NA EUV reaches new readiness milestone with first high-volume Logic product](https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone)
8. [High-NA EUV (TWINSCAN EXE)（VentureAtlas）](https://www.ventureatlas.org/product/asml-high-na-euv-twinscan-exe)
9. [百万片晶圆之后：英特尔与台积电，谁在改写光刻终局？](https://www.tmtpost.com/agent/ai-article/20252)
10. [Intel Deploys High-NA EUV in Mass Production for the First Time](https://xenospectrum.com/en/intel-18a-high-na-euv-panther-lake-volume-production/)
11. [Applied Materials Announces Third Quarter 2026 Results](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-third-quarter-2026-results)
12. [Applied Materials Third Quarter Fiscal 2026 Earnings Presentation](https://appliedmaterials.gcs-web.com/static-files/9d5d182d-f060-4b22-a32c-4582257fdc9b)
13. [Lam Research Corporation Reports Financial Results for the Quarter Ended June 28, 2026](https://investor.lamresearch.com/2026-07-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-June-28,-2026?asPDF=1)
14. [Lam Research Lifts 2026 WFE Outlook as AI Demand Strains Fab Capacity](https://www.marketbeat.com/instant-alerts/event-lam-research-lifts-2026-wfe-outlook-as-ai-demand-strains-fab-capacity-2026-09-11/)
15. [Global Semiconductor Equipment Sales Forecast to Reach a Record $229 Billion in 2028, SEMI Reports](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports)
16. [SEMI报告：2028年全球半导体设备销售额预计创纪录](https://www.semi.org.cn/site/semi/article/88d23b6850284acb8ecc6f06c0a59828.html)
17. [Global Semiconductor Equipment Sales Projected to Reach a Record of $156 Billion in 2027, SEMI Reports](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports)
18. [放下"先进制程"执念，"成熟制程"引领半导体设备逆势狂欢](https://stcn.com/article/detail/3917099.html)
19. [2026年中国光刻机报告下载：16亿市场规模与竞争格局演变](https://www.baogaobox.com/insights/260508000027273.html)
20. [中微公司预计2025年营收同比增长约37%](https://www.stcn.com/article/detail/3609771.html)
21. [中微公司上半年净利润预增逾2.8倍](https://www.stcn.com/article/detail/4056714.html)
22. [中微公司并购CMP设备公司，谁紧张了？](https://www.stcn.com/article/detail/3559589.html)
23. [国产半导体设备企业迎来"黄金大年"](https://finance.sina.com.cn/jjxw/2026-07-05/doc-iniftwia8958459.shtml)
24. [半导体产业与人工智能产业周期复苏及投资建议](https://m.book118.com/try_down/366125215230011013.pdf)
25. [Chinas Chipangriff auf ASML](https://www.deutschetageszeitung.de/Videos/4055-chinas-chipangriff-auf-asml.html?page=70)