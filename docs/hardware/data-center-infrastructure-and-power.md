# 数据中心基础设施（Data Center Infrastructure and Power）

> 最后更新：2026-09-26 ｜ 领域：硬件·数据中心 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI 训练与推理把数据中心从「IT 房地产」变成「能源与热管理工程」。芯片功耗密度、单机柜功率、供电可得性与散热方式，共同构成本轮 AI 基础设施建设的主要约束。有观点指出，2026 年开发一个 AI 数据中心首先是一个电力、散热与人才问题，其次才是地产问题：建筑本身可 12–18 个月建成，但电网接入可能需 5–7 年，且 63% 的运营者把熟练劳动力短缺列为首要障碍（[Data Center Development for AI in 2026](https://gainam.com/insights/ai-data-center-development)）。

## 最新进展（2025–2026）

- **电力成为核心瓶颈**：IEA 预测到 2026 年 AI 数据中心将年耗电 1000 TWh，相当于日本全国用电量；而美国电网并网排队平均已达 5 年，积压约 2300 GW，历史完成率仅 14%（[650B Power Gap: AI Data Centers Collide with Grid Reality in 2026](https://informedclearly.com/en/ai/56053/ai-data-center-power-gap-grid-bottleneck-2026)）。IEA 指出数据中心通常 1–2 年建成，而配套电力设施扩容耗时更长；欧盟获得并网需 2–10 年，FLAP-D（法兰克福、伦敦、阿姆斯特丹、巴黎、都柏林）集群排队平均 7–10 年，估计全球约五分之一规划中的数据中心项目面临风险（[The new bottleneck for AI infrastructure is not silicon](https://vendor.energy/articles/ai-data-center-grid-bottleneck-europe/)）。
- **核电与表外供电**：截至 2026 年 5 月，超大规模厂商已宣布 13 个核电项目、合计逾 9.8 GW，包括 Microsoft 重启三里岛（835 MW）、Google 的 Kairos Power 机组（500 MW）、Amazon 对 X-energy 的投资（960 MW）（[Power Independence: Why Hyperscalers Are Bypassing the Grid to Fuel the AI Boom](https://informedclearly.com/en/ai/57103/hyperscalers-bypassing-grid-ai-boom-2026)）。三里岛重启项目配套 20 年购电协议（PPA）（[The 835 MW Nuclear AI Bet](https://www.unboxfuture.com/2026/09/the-835-mw-nuclear-ai-bet-inside.html)）。另有项目计划先用两台 GE Vernova 燃气轮机在 2030 年供应约 1 GW，再从 2032 年起增加最多 5 台 BWRX-300 SMR 的 1.5 GW（[GE Vernova](https://telborg.com/companies/ge-vernova)）。
- **液冷成为标配**：随着 GPU 芯片 TDP 突破 1000W，直接芯片（cold plate）液冷从可选项变为标准配置。厂商资料称直接芯片液冷换热效率比风冷高 10–20 倍，可支持 PUE 低于 1.15 与最高 100kW 的机柜密度（[Why Are Direct-to-Chip Liquid Cooling Servers Becoming Standard in 2026?](https://www.szwecent.com/why-are-direct-to-chip-liquid-cooling-servers-becoming-standard-in-2026/)）。Microsoft 自 2025 年 7 月起在 Azure 园区规模部署直接芯片液冷，并测试面向下一代系统的微流控方案；NVIDIA Blackwell（GB200/GB300）单卡功耗 1200–1400W，Vera Rubin 系统目标机柜功率约 600kW（[Direct-to-Chip Cooling Implementation: Reducing PUE Below 1.2](https://introl.com/blog/direct-to-chip-cooling-pue-below-12-implementation)）。

- **水资源约束**：欧盟委员会 2026 年《Cloud and AI Development Act》影响评估估计，2025 年欧盟境内数据中心消耗约 760 亿升水；大型数据中心冷却系统每天可能需数百万升淡水，实际用量取决于冷却方式、气候与区域水资源条件（[Green and resilient now](https://www.grundfos.com/content/dam/global/page-assets/products-and-services/products/documents/CBS-Data-centers-whitepaper-green-and-resilient-now.pdf)）。2026 年新研究显示单个数据中心每天取水量可高达 390 万加仑，满足美国未来数据中心需求可能需要最多 580 亿美元的额外供水系统容量（[How Much Water Do AI Data Centers Use?](https://infotechlead.com/data-center/how-much-water-do-ai-data-centers-use-58-billion-infrastructure-challenge-puts-cooling-in-focus-98412)）。传统冷却塔系统每年每兆瓦约耗水 260 万加仑，NVIDIA 称其 DSX 设计在有利气候下可将之降至接近零（[AI Data Center Water Use Is Not Solved](https://www.c114pro.com/cloud/174199.html)）；Google 的应对方案包括纯风冷、闭环液冷与把余热输出到市政电网（[AI's Hidden Thirst](https://www.ozonedailynews.com/tech/google-ai-data-center-water-consumption-cooling-2026)）。中国方面，业界提出「水能协同」；闭式干冷系统让冷却介质在管道内循环，可把蒸发耗水降到极低水平，北方地区全年大部分时间可依靠干冷器甚至新风系统散热（[报告:全球AI算力狂飙加剧水资源压力](https://www.cenews.com.cn/news.html?aid=1808573)）。

## 核心技术与关键概念

- **供电架构**：传统 54V 直流架构向 800 VDC 迁移，有资料称 800 VDC 可将端到端电力损耗降低 5%、铜用量减少 45%（[800VDC, Off-Grid Power, and the Decisions That Have to Come First](https://www.orbitalindustries.com/news/blog/800vdc-off-grid-power-and-the-decisions-that-have-to-come-first)）。
- **散热路线**：直接芯片液冷（冷板式）、浸没式液冷、相变液冷；据赛迪顾问《2025—2026年中国液冷数据中心市场报告》，2025 年中国液冷数据中心市场中冷板式液冷占比达 93.5%，仍将是未来 3–5 年主流方案，浸没式液冷将在单机柜功率超 200kW 的超高密度场景加速渗透（[算力火爆带热液冷赛道](https://www.cnii.com.cn/cyjs/202609/t20260921_761723.html)）。
- **PUE（Power Usage Effectiveness）**：衡量数据中心能效的核心指标，定义为本设施总能耗与 IT 设备能耗之比。
- **并网时序经济学**：有分析认为真正的约束是「送电日期」而非 GPU 配额，应按「兆瓦-年」而非「兆瓦」规划容量，规模更小但更早送电的站点在长期产出上可能更优（[AI Data Center Power Constraints: Capacity Planning When the Grid Sets the Ceiling](https://opennash.com/blog/ai-data-center-power-constraints-capacity-planning-when-the/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **核电/供电**：Microsoft 三里岛重启 + 20 年 PPA；Google Kairos Power；Amazon X-energy；GE Vernova 燃气轮机与 BWRX-300 SMR（各来源见上）。
- **液冷供应链**：直接芯片液冷系统 2025 年占据约 52.30% 的液冷市场份额，2026 年 AI 加速器单处理器功耗已超 1000 瓦（[Data Center Liquid Cooling Market](https://www.astuteanalytica.com/industry-report/data-center-liquid-cooling-market)）。
- **国内用电口径**：国家能源局数据显示 2025 年全国算力中心总用电量 1700 亿千瓦时，占全社会用电量 1.6%（[AI算力催热光模块新赛道](http://m.toutiao.com/group/7689742243267953187/)）。
- **人口/园区趋势**：有报道指出 NVIDIA 于 2026 年 8 月拟最高投入 30 亿美元入股电力基建企业 Lancium，以锁定数据中心电力资源（[行业大变天!黄仁勋大胆预判:半导体十年扩张 5-10 倍](http://m.toutiao.com/group/7689739753175941668/)）。

## 关键数据与评测结果（附来源）

- **机柜功率密度**：据 AFCOM《State of the Data Center Report 2026》，2026 年平均机柜密度达 27 kW，较 2025 年的 16 kW 大幅提升（[Data Center Direct-to-Chip Cooling Fluids Market](https://www.mordorintelligence.com/industry-reports/data-center-direct-to-chip-cooling-fluids-market)）。AI 服务器机柜功耗已从几年前的不足 10kW 上升到单柜 50–100kW（[SMRs for Data Centers](https://enkiai.com/data-center/microsoft-nuclear-on-site-power/)）。
- **PUE 行业均值**：Uptime Institute 全球数据中心调查显示，2025 年受访者年度 PUE 加权平均为 1.54，为连续第六年几乎停步（[Uptime Institute Global Data Center Survey 2025](https://uptimeinstitute.com/uptime_assets/cec7166957f7f529e48073bfcb5b0e99bf0dde906aa263aa7e834d33601db929-GA-2025-07-uptime-institute-global-data-center-survey-results-2025.pdf)）；2026 年行业平均 PUE 为 1.52，延续七年相对停滞趋势（[Uptime Institute Global Data Center Survey 2026](https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/UptimeInstitute.GlobalDataCenterSurvey.2026.pdf)）。受访者普遍把停滞归因于存量基础设施与地区性散热障碍（[Data centre efficiency flatlines for sixth year as AI power demands soar](https://thefreesheet.com/2026/01/19/data-centre-efficiency-flatlines-for-sixth-year-as-ai-power-demands-soar/)）。
- **超大规模 PUE**：行业目标是 1.05–1.2，头部企业如 Google 报告的全 fleet PUE 为 1.09（含季节性开销），部分最优站点可达 1.06–1.10（[Target PUE untuk Enterprise vs Hyperscale](https://aircontechindo.com/article/target-pue-untuk-enterprise-vs-hyperscale)）。
- **液冷市场**：直接芯片液冷市场 2025 年达 55.2 亿美元（[Direct-to-Chip Cooling Implementation](https://introl.com/blog/direct-to-chip-cooling-pue-below-12-implementation)）。

## 趋势与争议

- **电网并网 vs 自建发电**：美国 2024 年电网并网排队平均 55 个月，离网采购成为主要路径，但离网设备自身也存在多年排队（[800VDC, Off-Grid Power](https://www.orbitalindustries.com/news/blog/800vdc-off-grid-power-and-the-decisions-that-have-to-come-first)）。
- **电价与社会成本争议**：有报道指出数据中心需求已使部分区域居民电价上升，如 AEP Ohio 的 data-center rider 使家庭每月增加约 7.90 美元（[AI Nuclear Pivot: Hyperscalers Reshape Energy Markets 2026](https://informedclearly.com/en/ai/62451/ai-nuclear-hyperscalers-energy-markets-2026)）。
- **PUE 指标局限**：行业平均 PUE 多年停滞，说明在 AI 高功率密度下，单纯能效指标难以反映真实的水耗、碳排与选址外部性。

## 参考来源

- [Data Center Development for AI in 2026](https://gainam.com/insights/ai-data-center-development)
- [650B Power Gap: AI Data Centers Collide with Grid Reality in 2026](https://informedclearly.com/en/ai/56053/ai-data-center-power-gap-grid-bottleneck-2026)
- [The new bottleneck for AI infrastructure is not silicon](https://vendor.energy/articles/ai-data-center-grid-bottleneck-europe/)
- [Power Independence: Why Hyperscalers Are Bypassing the Grid to Fuel the AI Boom](https://informedclearly.com/en/ai/57103/hyperscalers-bypassing-grid-ai-boom-2026)
- [The 835 MW Nuclear AI Bet](https://www.unboxfuture.com/2026/09/the-835-mw-nuclear-ai-bet-inside.html)
- [GE Vernova](https://telborg.com/companies/ge-vernova)
- [SMRs for Data Centers, Microsoft's 10.5 GW Brookfield Plan](https://enkiai.com/data-center/microsoft-nuclear-on-site-power/)
- [Why Are Direct-to-Chip Liquid Cooling Servers Becoming Standard in 2026?](https://www.szwecent.com/why-are-direct-to-chip-liquid-cooling-servers-becoming-standard-in-2026/)
- [Direct-to-Chip Cooling Implementation: Reducing PUE Below 1.2](https://introl.com/blog/direct-to-chip-cooling-pue-below-12-implementation)
- [Green and resilient now: Report on fluid systems enabling water–energy coordination](https://www.grundfos.com/content/dam/global/page-assets/products-and-services/products/documents/CBS-Data-centers-whitepaper-green-and-resilient-now.pdf)
- [How Much Water Do AI Data Centers Use? $58 Billion Infrastructure Challenge Puts Cooling in Focus](https://infotechlead.com/data-center/how-much-water-do-ai-data-centers-use-58-billion-infrastructure-challenge-puts-cooling-in-focus-98412)
- [AI Data Center Water Use Is Not Solved: Nvidia's Cooling Fix Stops at the Walls](https://www.c114pro.com/cloud/174199.html)
- [AI's Hidden Thirst: How Google Is Engineering Its Way Out of the Data Center Water Crisis](https://www.ozonedailynews.com/tech/google-ai-data-center-water-consumption-cooling-2026)
- [报告:全球AI算力狂飙加剧水资源压力，"水能协同"成绿色算力竞争新赛道](https://www.cenews.com.cn/news.html?aid=1808573)
- [算力火爆带热液冷赛道](https://www.cnii.com.cn/cyjs/202609/t20260921_761723.html)
- [Data Center Liquid Cooling Market](https://www.astuteanalytica.com/industry-report/data-center-liquid-cooling-market)
- [Data Center Direct-to-Chip Cooling Fluids Market](https://www.mordorintelligence.com/industry-reports/data-center-direct-to-chip-cooling-fluids-market)
- [AI Data Center Power Constraints: Capacity Planning When the Grid Sets the Ceiling](https://opennash.com/blog/ai-data-center-power-constraints-capacity-planning-when-the/)
- [800VDC, Off-Grid Power, and the Decisions That Have to Come First](https://www.orbitalindustries.com/news/blog/800vdc-off-grid-power-and-the-decisions-that-have-to-come-first)
- [Uptime Institute Global Data Center Survey 2025](https://uptimeinstitute.com/uptime_assets/cec7166957f7f529e48073bfcb5b0e99bf0dde906aa263aa7e834d33601db929-GA-2025-07-uptime-institute-global-data-center-survey-results-2025.pdf)
- [Uptime Institute Global Data Center Survey 2026](https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/UptimeInstitute.GlobalDataCenterSurvey.2026.pdf)
- [Data centre efficiency flatlines for sixth year as AI power demands soar](https://thefreesheet.com/2026/01/19/data-centre-efficiency-flatlines-for-sixth-year-as-ai-power-demands-soar/)
- [Target PUE untuk Enterprise vs Hyperscale](https://aircontechindo.com/article/target-pue-untuk-enterprise-vs-hyperscale)
- [AI Nuclear Pivot: Hyperscalers Reshape Energy Markets 2026](https://informedclearly.com/en/ai/62451/ai-nuclear-hyperscalers-energy-markets-2026)
- [AI算力催热光模块新赛道](http://m.toutiao.com/group/7689742243267953187/)
- [行业大变天!黄仁勋大胆预判:半导体十年扩张 5-10 倍](http://m.toutiao.com/group/7689739753175941668/)