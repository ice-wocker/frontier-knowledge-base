# 气候科学与地球系统

> 最后更新：2026-09-26 ｜ 领域：科学·地球系统与复杂系统 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

气候科学以地球系统为对象，涵盖大气、海洋、冰冻圈、陆地生物圈及其与人类活动的相互作用，通过观测、再分析、数值模式与统计归因来理解气候变化的成因与后果。当前该领域的三条主线是：耦合模式比较计划 CMIP7 的推进、以 AI 气象预报为代表的数据驱动方法崛起，以及临界点（tipping points）与极端事件归因研究的深化。

## 最新进展（2025–2026）

**观测与升温事实。** 世界气象组织（WMO）《2025 年全球气候状况》报告确认 2015–2025 年为有记录以来最热的 11 年，2025 年为有记录以来第二或第三热年份，全球平均地表温度较 1850–1900 年基准约高出 1.43°C（[地球气候摆动不定愈发失衡](https://wmo.int/zh-hans/news/media-centre/deqiuqihoubaidongbudingyufashiheng)）。WMO 同时指出，拉尼娜带来的短期降温并未逆转长期趋势，海洋增暖持续（[WMO confirms 2025 was one of warmest years on record](https://wmo.int/news/media-centre/wmo-confirms-2025-was-one-of-warmest-years-record)）。据 2025 年全球气候亮点报告，2023–2025 三年平均已超过工业化前 1.5°C，ERA5 为 1.52°C、JRA-3Q 为 1.50°C，为仪器记录期首次（[2025 GLOBAL CLIMATE HIGHLIGHTS](https://www.valleweather.com/GCH2025-full-report.pdf)）。

**CMIP7 与 IPCC AR7。** CMIP7 的 ScenarioMIP 给出了新的全球排放情景集合，与 CMIP6 情景相比有两个重要变化：21 世纪的最高排放情景低于此前情景集，而最低排放情景对应的升温预估也不相同（[CMIP7 scenarios explainer now live](https://www.wcrp-climate.org/news/science-highlights/2413-cmip7-scenarios-explainer-2026)）。配套数据发布基础设施正在换代：地球系统网格联盟下一代（ESGF-NG）计划于 2026 年 5 月启动并支持 CMIP 数据发布（[Update report for the WCRP Joint Scientific Committee: CMIP and WIP](https://www.wcrp-climate.org/documents/JSC/JSC47/Reports/JSC-47_reporting_CMIP_FINAL-PUBLIC.pdf)）。IPCC 第七次评估周期（AR7）中，三个工作组报告可能在 2028 年中期起陆续发布，综合报告预计 2029 年底发布；本周期唯一的特别报告《气候变化与城市》定于 2027 年 3 月通过（[IPCC Speeches](https://www.ipcc.ch/topic/speeches/)、[Leading scientists gather in India for final meeting to work on the Special Report on Climate Change and Cities](https://www.ipcc.ch/2026/08/03/srcities-lam4/)）。

**AI 气象预报。** Pangu-Weather、GraphCast、GenCast、ECMWF 的 AIFS 与 Microsoft 的 Aurora 等模型先后证明，基于历史再分析资料训练的数据驱动模型可在中期全球预报上比肩先进数值天气预报（NWP）（[Evaluating the Predictability of Selected Weather Extremes with Aurora, an AI Weather Forecast Model](https://www.preprints.org/manuscript/202606.1070)）。这些模型在架构上分属图神经网络、Transformer 与扩散模型，训练数据与预报时效也各不相同（[MAUSAM: An Observations-focused assessment of Global AI Weather Prediction Models During the South Asian Monsoon](https://arxiv.org/html/2509.01879)）。Aurora 为 3D Swin Transformer 编解码器架构，2025 年 5 月发表于 Nature，覆盖天气、空气质量、海浪与气旋路径（[Weather model comparison](https://aiwiki.ai/wiki/weather/edit)）。不过长时滚动的稳定性仍是关键问题，有基准研究指出不同模型在强噪声下逐步去噪的能力差异明显（[Can AI Weather Models Predict Beyond Two Weeks? A Quantitative Benchmark and Analysis of Long Rollouts](https://arxiv.org/html/2605.30184)）。

**地球系统数字孪生。** 欧盟 Destination Earth（DestinE）计划已进入第三阶段，由 ECMWF、EUMETSAT 与 ESA 共同实施（[Destination Earth moves into its third phase](https://destine.ecmwf.int/news/destination-earth-moves-into-its-third-phase/)）。其中气候变化适应数字孪生（Climate DT）在第二阶段（2024–2026）重点推进业务化，并加强 AI、不确定性量化与交互能力；遵循 HighResMIP 协议的升级模式模拟预计 2026 年初可用（[Climate Change Adaptation Digital Twin](https://destine.ecmwf.int/climate-change-adaptation-digital-twin-climate-dt/)）。

## 核心科学与关键概念

- **地球系统模式与情景集合**：CMIP 通过多模式集合量化内部变率与模式不确定性；情景（CMIP6 的 SSP 与新情景集）驱动政策相关的气候预估。
- **临界要素与级联**：大西洋经向翻转环流（AMOC）、亚马孙雨林、格陵兰与西南极冰盖等被列为可能发生不可逆转变的临界要素。
- **极端事件归因**：比较"有/无气候变化"两种反事实世界中的事件概率或强度。
- **数据驱动预报与再分析**：以 ERA5、JRA-3Q 等再分析产品为训练目标，ERA5 与 JRA-3Q 也是升温统计的重要口径来源。

## 关键进展：临界点与归因

临界点研究在 2025–2026 年倾向于用网络化框架刻画要素之间的相互作用。一项发表于 Earth System Dynamics 的风险评估框架发现，无论网络构建方式如何，AMOC 都具有最高的介数中心性（betweenness centrality），支持其作为级联主导中介者的判断（[A risk assessment framework for interacting tipping elements](https://esd.copernicus.org/articles/17/333/2026/esd-17-333-2026.html)）。另一项使用稀有事件算法的工作量化了从 AMOC 到亚马孙雨林的级联临界概率（[Quantification of the cascading tipping probability from the AMOC to the Amazon rainforest with a rare-event algorithm](https://pubs.aip.org/aip/cha/article-pdf/doi/10.1063/5.0288335/20917404/023146_1_5.0288335.pdf)）。关于西南极，有报道援引 Nature Climate Change（2026 年 2 月）与 The Cryosphere（2025 年 1 月）的研究称，Thwaites 与 Pine Island 冰川系统可能已对长期崩解"锁定"（[Climate Tipping Points — What Scientists Actually Know vs What Headlines Claim](https://osakawire.com/en/climate-tipping-points-what-scientists-actually-know/)）；此类表述属于二手转述，仍需以原始论文口径为准。

归因方面，World Weather Attribution 的 2025 年度报告指出，2025 年多数极端天气事件因气候变化而变得更可能或更强，同时强调证据基础不均衡：许多研究聚焦全球南方的强降雨，但观测数据缺口与主要面向全球北方开发的模式限制了结论的确定性（[Unequal evidence and impacts, limits to adaptation: Extreme Weather in 2025](https://www.worldweatherattribution.org/unequal-evidence-and-impacts-limits-to-adaptation-extreme-weather-in-2025/)）。方法学上，有研究提出"环流印记"归因方法，可分离动力学与非动力学（热力学等）贡献，并应用于 2025 年洛杉矶山火等事件（[Dynamically-Informed Extreme Event Attribution Using Circulation Imprints](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL116869)）。

## 趋势与争议

1. **AI 预报的定位**：数据驱动模型能否替代还是仅补充传统 NWP，以及如何保持物理一致性（质量/能量守恒）与长时稳定性，仍有争论。
2. **归因科学的公平性**：观测与模式资源分布不均，导致全球南方事件的归因证据相对薄弱。
3. **临界点表述落差**：公众传播中常出现"已越过临界点"的强断言，与文献中条件性、模型依赖的结论之间存在落差。
4. **口径并存**：升温幅度存在 ERA5 与 JRA-3Q 等多套数据集口径，需并列呈现而非取单一结论。

## 参考来源

- [地球气候摆动不定愈发失衡（WMO）](https://wmo.int/zh-hans/news/media-centre/deqiuqihoubaidongbudingyufashiheng)
- [WMO confirms 2025 was one of warmest years on record](https://wmo.int/news/media-centre/wmo-confirms-2025-was-one-of-warmest-years-record)
- [2025 GLOBAL CLIMATE HIGHLIGHTS](https://www.valleweather.com/GCH2025-full-report.pdf)
- [CMIP7 scenarios explainer now live（WCRP）](https://www.wcrp-climate.org/news/science-highlights/2413-cmip7-scenarios-explainer-2026)
- [Update report for the WCRP Joint Scientific Committee CMIP and WIP](https://www.wcrp-climate.org/documents/JSC/JSC47/Reports/JSC-47_reporting_CMIP_FINAL-PUBLIC.pdf)
- [IPCC Speeches](https://www.ipcc.ch/topic/speeches/)
- [Leading scientists gather in India for final meeting to work on the Special Report on Climate Change and Cities](https://www.ipcc.ch/2026/08/03/srcities-lam4/)
- [Evaluating the Predictability of Selected Weather Extremes with Aurora, an AI Weather Forecast Model](https://www.preprints.org/manuscript/202606.1070)
- [MAUSAM: An Observations-focused assessment of Global AI Weather Prediction Models During the South Asian Monsoon](https://arxiv.org/html/2509.01879)
- [Weather model comparison (Aurora)](https://aiwiki.ai/wiki/weather/edit)
- [Can AI Weather Models Predict Beyond Two Weeks? A Quantitative Benchmark and Analysis of Long Rollouts](https://arxiv.org/html/2605.30184)
- [Destination Earth moves into its third phase](https://destine.ecmwf.int/news/destination-earth-moves-into-its-third-phase/)
- [Climate Change Adaptation Digital Twin（DestinE）](https://destine.ecmwf.int/climate-change-adaptation-digital-twin-climate-dt/)
- [A risk assessment framework for interacting tipping elements（ESD）](https://esd.copernicus.org/articles/17/333/2026/esd-17-333-2026.html)
- [Quantification of the cascading tipping probability from the AMOC to the Amazon rainforest with a rare-event algorithm](https://pubs.aip.org/aip/cha/article-pdf/doi/10.1063/5.0288335/20917404/023146_1_5.0288335.pdf)
- [Climate Tipping Points — What Scientists Actually Know vs What Headlines Claim](https://osakawire.com/en/climate-tipping-points-what-scientists-actually-know/)
- [Unequal evidence and impacts, limits to adaptation: Extreme Weather in 2025（WWA）](https://www.worldweatherattribution.org/unequal-evidence-and-impacts-limits-to-adaptation-extreme-weather-in-2025/)
- [Dynamically-Informed Extreme Event Attribution Using Circulation Imprints（AGU）](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL116869)