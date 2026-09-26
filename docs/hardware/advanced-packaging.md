# 先进封装

> 最后更新：2026-09-26 ｜ 领域：硬件·芯片与设计 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

当制程微缩的收益趋缓、单芯片面积受光罩尺寸与良率限制时，先进封装成为继续提升系统算力的主要路径。其核心思路是把多个裸片（die）通过硅中介层（interposer）、重布线层（RDL）、硅桥（bridge）或直接混合键合集成在一个封装内，从而在逼近单芯片的互连密度下实现异构集成——例如把逻辑计算 die 与多颗 HBM 堆叠放在一起，或把不同制程节点、不同功能的芯粒（chiplet）组合成一颗"系统级芯片"。

2.5D 封装（die 并排在中介层上）与 3D 封装（die 垂直堆叠）是两条主线。关键工艺要素包括 TSV（硅通孔）、微凸点（micro-bump）、混合键合（hybrid bonding）、翘曲控制与封装级热管理。AI 加速器是当前先进封装需求最集中、产能最紧张的应用，因此 CoWoS 等产能指标已成为观察 AI 算力供给的重要先行变量。

## 最新进展（2025–2026）

**CoWoS 产能快速扩张，仍是核心瓶颈。** 台积电计划把 CoWoS 月产能从 2024 年下半年的约 3.5 万片提升到 2026 年底的约 13 万片，接近 4 倍增长，以应对 NVIDIA、Google 等主要客户的紧急订单（[AI需要の急増に対応するTSMCのCoWoS/SoIC生産能力戦略](https://troy-technical.jp/ai%E9%9C%80%E8%A6%81%E3%81%AE%E6%80%A5%E5%A2%97%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%99%E3%82%8Btsmc%E3%81%AEcowos-soic%E7%94%9F%E7%94%A3%E8%83%BD%E5%8A%9B%E6%88%A6%E7%95%A5%EF%BC%9A2026%E5%B9%B4%E6%9C%AB/)、[TSMC、先端パッケージング能力を4倍に拡大](https://troy-technical.jp/tsmc%E3%80%81%E5%85%88%E7%AB%AF%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%83%B3%E3%82%B0%E8%83%BD%E5%8A%9B%E3%82%924%E5%80%8D%E3%81%AB%E6%8B%A1%E5%A4%A7%EF%BC%9A2026%E5%B9%B4%E6%9C%AB%E3%81%BE/)）。据 TrendForce 口径，2026 年底台积电 CoWoS 月产能预计约 12 万至 14 万片，2027 年有望提升至约 20 万片；产能结构向 CoWoS-L 倾斜，DIGITIMES 预计 2026 年第四季度 CoWoS-L 占台积电 CoWoS 产能比重将升至约 75%（[CoWoS紧缺持续，先进封装供给格局重塑](https://finance.sina.com.cn/roll/2026-09-17/doc-inisckrz4080792.shtml)）。另有统计指出先进封装占台积电 2026 年 600 亿至 640 亿美元资本开支的 10%–20%，5.5 倍光罩尺寸的 CoWoS-L 在 2026 年 8 月于多个 AI 客户产品上实现 98%–99% 的量产良率（[TSMC（VentureAtlas）](https://www.ventureatlas.org/company/tsmc)）。行业估算还显示 NVIDIA 在 2026 年约占台积电先进封装产能的 60%（[NVIDIAがTSMC先端パッケージの60%を抑えた2026年](https://qiita.com/plasmon/items/f49d99469a0f9ca520bf)）。

**CoWoS 技术分层。** 台积电 CoWoS 家族包含三种技术：CoWoS-S（硅中介层）、CoWoS-R（RDL 中介层，2023 年起量产，最小 4µm 间距）与 CoWoS-L（RDL 中介层叠加嵌入式局部硅互连 LSI 桥与嵌入式深沟槽电容 eDTC），首个 3.5 倍光罩尺寸的 CoWoS-L 已量产，5.5 倍版本 2026 年进入量产（[TSMC CoWoS：A Full Guide to the Packaging Line That Gates AI GPUs](https://www.insidedeeptech.com/tsmc-cowos-packaging-full-guide/)、[CoWoS（TSMC 3DFabric）](https://3dfabric.tsmc.com/chinese/dedicatedFoundry/technology/cowos.htm)、[HPC Platform – TSMC 3DFabric](https://www.tsmc.com/schinese/dedicatedFoundry/technology/platform_HPC_tech_WLSI)）。CoWoS-L 的混合中介层方案是 NVIDIA B200/GB200 及后续加速器的共同基础（[CoWoS-L이란?](https://www.vlsi.kr/ko/cowos-liran-rdl-inteopojeoe-lsi-beurisjireul-bageun-5-retikeul-ai-gasoggi-paekiji/)）。

**SoIC 3D 堆叠规模仍小。** SoIC 是台积电面向 3D 芯片堆叠的前端晶圆键合技术（[IC-Link Joins TSMC 3DFabric Alliance](https://www.techtimes.com/articles/327952/20260923/ic-link-joins-tsmc-3dfabric-alliance-showcases-cowos-asic-co-design-oip-forum-today.htm)）。行业报告估计 2026 年台积电 SoIC 月产能约在 1 万至 1.5 万片区间，约为 CoWoS 产能的一成，并预期 NVIDIA Rubin Ultra 与 Feynman 等后续产品会更多采用（[NVIDIAがTSMC先端パッケージの60%を抑えた2026年](https://qiita.com/plasmon/items/f49d99469a0f9ca520bf)）。需要说明，该数字来自多个行业报告的区间估计，并非台积电官方公布值。

**面板级封装与玻璃基板成为下一代方向。** 台积电推出 CoPoS（Chip-on-Panel-on-Substrate），基于 310×310mm 方形面板，与晶圆形态的 CoWoS 不同，后续将引入玻璃芯基板；计划 2026 年在子公司 VisEra 建立试点线、2027 年试产、2028 年下半年量产（[Intel and TSMC Push Panel-Level Packaging as Market Sets to Expand Tenfold](https://www.thelec.net/news/articleView.html?idxno=11912)、[Intel and TSMC Pile In as Glass Substrates and Panel Packaging Head for 10x Growth](https://www.c114pro.com/chip/175754.html)）。另有报道称台积电已在龙潭厂建置采用玻璃基板的 CoPoS 试验线，并在台湾与美国规划量产线，预计 2028 年正式量产；力成早在 2024 年即量产全自动 FOPLP 产线（[DIGITIMES：台厂2030年前玻璃基板封装优势难被撼动](https://www.eet-china.com/mp/a525600.html)）。玻璃基板市场被预测将从 2024 年的 6.5 亿美元增长到 2030 年的 80 亿美元，约 12 倍；采用玻璃芯基板可降低约 30% 成本并把晶圆利用率提升到 90% 以上（[ガラス基板が有機ABFの25年を終わらせる](https://xenospectrum.com/glass-panel-level-packaging-tsmc-intel-2030/)、[TSMC et Intel accélèrent sur les nouveaux boîtiers](https://topcpu.net/fr/news/tsmc-intel-advanced-packaging-glass-substrates-panel-level-2030)）。Counterpoint 预计东亚（台湾、日本、中国）将占面板级封装产能的 84.8%（[Intel and TSMC Pile In as Glass Substrates and Panel Packaging Head for 10x Growth](https://www.c114pro.com/chip/175754.html)）。

**Intel 的封装技术组合。** Intel Foundry 提供 EMIB（嵌入式多裸片互连桥，2.5D）、EMIB-T（支持从一个封装技术迁移到另一个技术而几乎无需重新设计，并支持垂直供电以降低直流与交流噪声，2026 年支持超过 8 倍光罩尺寸、2028 年支持 12 倍）以及 Foveros 系列：Foveros 2.5D 把芯粒堆叠在无源基底 die 上，Foveros Direct 3D 堆叠在有源基底 die 上并采用混合键合互连，铜-铜凸点间距小于 5µm（[Accelerating AI and HPC with advanced process and packaging technologies](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2025-11/intel-foundry-hpc-ai-brief.pdf)）。Intel 在亚利桑那投资超过 320 亿美元建设两座新晶圆厂并改造 Fab 42 以支持 Intel 18A，该基地同时承载 EMIB、Foveros、Foveros Omni 与 Foveros Direct 技术（[Intel Arizona: The Silicon Desert](https://download.intel.com/newsroom/2024/corporate/Intel-Arizona-The-Silicon-desert.pdf)）。

**混合键合凸点间距持续缩小。** UCIe 联盟材料显示，混合键合（hybrid bonding）的凸点间距正从 9µm 向 1µm 以下演进，3D 集成由此从"边缘连接"转向全面积连接，带宽密度显著提升（[Introducing the UCIe 3.0 Specification](https://www.uciexpress.org/_files/ugd/0c1418_b4744fe368c94e3e9c7eaa13ead632bf.pdf)）。

**载板与材料侧瓶颈。** ABF 载板供应紧张成为封装产能的并行约束：据 SemiAnalysis 报告，2026 年六家主要 ABF 基板供应商产能已全部预定，交期由 2025 年初的约 6 至 8 个月拉长到 12 至 14 个月（[新浪财经：ABF载板相关报道](https://finance.sina.com.cn/wm/2026-08-29/doc-inipxyyv8793330.shtml.md)）；揖斐电与欣兴电子计划合计投资超过 8000 亿日元扩充 AI 服务器用 ABF 基板产能（[IbidenとUnimicron、AIサーバー向けABF基板生産能力を大幅増強へ](https://troy-technical.jp/ibiden%e3%81%a8unimicron%e3%80%81ai%e3%82%b5%e3%83%bc%e3%83%90%e3%83%bc%e5%90%91%e3%81%91abf%e5%9f%ba%e6%9d%bf%e7%94%9f%e7%94%a3%e8%83%bd%e5%8a%9b%e3%82%92%e5%a4%a7%e5%b9%85%e5%a2%97%e5%bc%b7%e3%81%b8/)。

## 核心技术与关键概念

- **中介层与桥接：** 硅中介层（CoWoS-S）提供最高互连密度但成本高、受光罩尺寸限制；RDL 中介层（CoWoS-R）以聚合物/铜布线换取更低成本与更快交付；CoWoS-L 在 RDL 中嵌入 LSI 硅桥，仅在需要高密度互连处使用硅，从而在良率与成本之间取得平衡（[TSMC CoWoS 指南](https://www.insidedeeptech.com/tsmc-cowos-packaging-full-guide/)）。
- **TSV 与凸点：** TSV 为 3D 堆叠与中介层提供垂直通路；微凸点与 C4 凸点决定 IO 密度。Intel EMIB 通过在中介层中加入 TSV 改善供电与信号布线（[Intel Foundry ADG Platform Brief](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2026-02/intel-foundry-adg-platform-brief.pdf)）。
- **混合键合：** 铜-铜直接键合，无需焊料，实现亚 5µm 甚至亚 1µm 间距，是 3D 堆叠与高带宽内存、BV-NAND 的关键工艺（[Intel Foundry HPC/AI Brief](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2025-11/intel-foundry-hpc-ai-brief.pdf)、[UCIe 3.0](https://www.uciexpress.org/_files/ugd/0c1418_b4744fe368c94e3e9c7eaa13ead632bf.pdf)）。
- **Chiplet 与 UCIe：** UCIe 3.0（2025 年 8 月发布）把 UCIe-S 与 UCIe-A 数据率翻倍至 48/64 GT/s，并增加自动协商与高级管理能力（[UCIe Webinars](https://www.uciexpress.org/webinars)、[The Growing Chiplet Ecosystem](https://www.uciexpress.org/post/the-growing-chiplet-ecosystem-collaboration-innovation-and-the-next-wave-of-ucie-adoption)）。
- **面板级封装（FOPLP）：** 以方形面板替代圆形晶圆，提升面积利用率。晶圆利用率可从面板化配合玻璃芯提升到 90% 以上（[topcpu.net](https://topcpu.net/fr/news/tsmc-intel-advanced-packaging-glass-substrates-panel-level-2030)）。
- **供电与热管理：** 单封装需要以约 1V 电压供应上千安培电流，成为 AI 多芯片封装的独立工程挑战（[DIGITIMES Biz Focus](https://www.digitimes.com/biz/index.php?cat=558&pg=1)）。垂直供电（如 EMIB-T）与局部深沟槽电容（eDTC）是应对手段。

## 代表性项目 / 公司 / 产品（附官方链接）

| 厂商 | 技术 | 链接 |
| --- | --- | --- |
| TSMC | CoWoS-S / CoWoS-R / CoWoS-L、SoIC、CoPoS | [TSMC 3DFabric CoWoS](https://3dfabric.tsmc.com/chinese/dedicatedFoundry/technology/cowos.htm)、[HPC Platform](https://www.tsmc.com/schinese/dedicatedFoundry/technology/platform_HPC_tech_WLSI) |
| Intel | EMIB、EMIB-T、Foveros、Foveros Direct、玻璃基板 | [Intel Foundry HPC/AI Brief](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2025-11/intel-foundry-hpc-ai-brief.pdf) |
| AMD / 日月光 / 力成 | FOPLP 面板级封装产线 | [DIGITIMES 报道](https://www.eet-china.com/mp/a525600.html) |
| 载板供应商 | 揖斐电、欣兴电子、新光电气、AT&S、南亚电路板 | [WorldNL](https://worldnl.com/the-state-of-abf-substrates-in-data-center-silicon-in-2026-solving-the-supply-crunch-and-material-wa-493583.html) |
| UCIe 联盟 | Chiplet 互连标准 | [uciexpress.org](https://www.uciexpress.org/specifications) |

## 关键数据与评测结果（附来源）

- CoWoS 月产能：2024 年底约 3.5 万片 → 2026 年底约 13 万片（约 4 倍）（[troy-technical](https://troy-technical.jp/tsmc%E3%80%81%E5%85%88%E7%AB%AF%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%83%B3%E3%82%B0%E8%83%BD%E5%8A%9B%E3%82%924%E5%80%8D%E3%81%AB%E6%8B%A1%E5%A4%A7%EF%BC%9A2026%E5%B9%B4%E6%9C%AB%E3%81%BE/)）；TrendForce 口径为 2026 年底 12 万–14 万片、2027 年约 20 万片（[新浪财经](https://finance.sina.com.cn/roll/2026-09-17/doc-inisckrz4080792.shtml)）。
- CoWoS-L 占比：预计 2026 年 Q4 升至约 75%（[新浪财经](https://finance.sina.com.cn/roll/2026-09-17/doc-inisckrz4080792.shtml)）。
- CoWoS-L 良率：5.5 倍光罩尺寸产品 2026 年 8 月于多个 AI 客户产品实现 98%–99% 量产良率（[VentureAtlas](https://www.ventureatlas.org/company/tsmc)）。
- SoIC 月产能：2026 年业界估计 1 万–1.5 万片（非官方）（[qiita](https://qiita.com/plasmon/items/f49d99469a0f9ca520bf)）。
- 玻璃基板市场：2024 年 6.5 亿美元 → 2030 年 80 亿美元（[xenospectrum](https://xenospectrum.com/glass-panel-level-packaging-tsmc-intel-2030/)）。
- ABF 载板交期：12–14 个月（2026），对比 2025 年初 6–8 个月（[新浪财经](https://finance.sina.com.cn/wm/2026-08-29/doc-inipxyyv8793330.shtml.md)）。
- Intel EMIB-T 光罩尺寸支持：2026 年 > 8 倍、2028 年 12 倍（[Intel Foundry HPC/AI Brief](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2025-11/intel-foundry-hpc-ai-brief.pdf)）。

## 趋势与争议

1. **CoWoS 仍是 AI 算力供给的决胜变量。** 尽管产能接近翻两番，CoWoS 依然供不应求，且产能结构从 CoWoS-S 转向 CoWoS-L；由于客户高度集中（NVIDIA 约占六成），产能分配直接决定各家加速器的出货节奏（[qiita](https://qiita.com/plasmon/items/f49d99469a0f9ca520bf)）。
2. **面板级与玻璃基板的时间表风险。** CoPoS 量产目标普遍定在 2028 年，2026–2027 年为试点与试产阶段；玻璃基板成本优势（约 30%）与尺寸稳定性优势明确，但量产良率与设备成熟度仍待验证（[thelec](https://www.thelec.net/news/articleView.html?idxno=11912)）。
3. **2.5D 与 3D 的分工。** SoIC 等 3D 堆叠产能远小于 CoWoS，短期内 2.5D 仍是 HBM 集成的主流方案；3D 堆叠的散热与测试访问（KGD）问题限制了其在大功率逻辑+HBM 组合上的快速替代。
4. **封装成为材料与设备的联合瓶颈。** ABF 载板交期延长、玻璃载板产能爬坡、混合键合设备与材料供应，共同构成封装扩产的约束，意味着"晶圆厂产能"不再是唯一瓶颈（[新浪财经](https://finance.sina.com.cn/wm/2026-08-29/doc-inipxyyv8793330.shtml.md)）。
5. **标准竞争加剧。** UCIe 作为开放标准快速迭代，但厂商私有互连（如 NVLink、Infinity Fabric）在带宽密度上仍有优势，形成"开放标准降低门槛、私有方案追求性能"的并行格局。
6. **供电与热设计内生化。** 千安培级供电与千瓦级散热使封装设计必须与芯片架构、基板与冷却方案同步规划，而非后端工程。

## 参考来源

1. [AI需要の急増に対応するTSMCのCoWoS/SoIC生産能力戦略：2026年末までに月産13万枚を目指す](https://troy-technical.jp/ai%E9%9C%80%E8%A6%81%E3%81%AE%E6%80%A5%E5%A2%97%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%99%E3%82%8Btsmc%E3%81%AEcowos-soic%E7%94%9F%E7%94%A3%E8%83%BD%E5%8A%9B%E6%88%A6%E7%95%A5%EF%BC%9A2026%E5%B9%B4%E6%9C%AB/)
2. [TSMC、先端パッケージング能力を4倍に拡大：2026年末までに月産13万枚のCoWoSウェーハを達成](https://troy-technical.jp/tsmc%E3%80%81%E5%85%88%E7%AB%AF%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%83%B3%E3%82%B0%E8%83%BD%E5%8A%9B%E3%82%924%E5%80%8D%E3%81%AB%E6%8B%A1%E5%A4%A7%EF%BC%9A2026%E5%B9%B4%E6%9C%AB%E3%81%BE/)
3. [CoWoS紧缺持续，先进封装供给格局重塑（新浪财经）](https://finance.sina.com.cn/roll/2026-09-17/doc-inisckrz4080792.shtml)
4. [TSMC（VentureAtlas）](https://www.ventureatlas.org/company/tsmc)
5. [NVIDIAがTSMC先端パッケージの60%を抑えた2026年](https://qiita.com/plasmon/items/f49d99469a0f9ca520bf)
6. [TSMC CoWoS: A Full Guide to the Packaging Line That Gates AI GPUs](https://www.insidedeeptech.com/tsmc-cowos-packaging-full-guide/)
7. [CoWoS®（TSMC 3DFabric）](https://3dfabric.tsmc.com/chinese/dedicatedFoundry/technology/cowos.htm)
8. [HPC Platform – TSMC 3DFabric®](https://www.tsmc.com/schinese/dedicatedFoundry/technology/platform_HPC_tech_WLSI)
9. [CoWoS-L이란? RDL 인터포저에 LSI 브릿지를 박은 5+ 레티클 AI 가속기 패키지](https://www.vlsi.kr/ko/cowos-liran-rdl-inteopojeoe-lsi-beurisjireul-bageun-5-retikeul-ai-gasoggi-paekiji/)
10. [IC-Link Joins TSMC 3DFabric Alliance](https://www.techtimes.com/articles/327952/20260923/ic-link-joins-tsmc-3dfabric-alliance-showcases-cowos-asic-co-design-oip-forum-today.htm)
11. [Intel and TSMC Push Panel-Level Packaging as Market Sets to Expand Tenfold（TheElec）](https://www.thelec.net/news/articleView.html?idxno=11912)
12. [Intel and TSMC Pile In as Glass Substrates and Panel Packaging Head for 10x Growth](https://www.c114pro.com/chip/175754.html)
13. [DIGITIMES：台厂2030年前玻璃基板封装优势难被撼动](https://www.eet-china.com/mp/a525600.html)
14. [ガラス基板が有機ABFの25年を終わらせる](https://xenospectrum.com/glass-panel-level-packaging-tsmc-intel-2030/)
15. [TSMC et Intel accélèrent sur les nouveaux boîtiers](https://topcpu.net/fr/news/tsmc-intel-advanced-packaging-glass-substrates-panel-level-2030)
16. [Accelerating AI and HPC with advanced process and packaging technologies（Intel Foundry）](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2025-11/intel-foundry-hpc-ai-brief.pdf)
17. [Intel Foundry ADG Platform Brief](https://www.intel.cn/content/dam/www/central-libraries/us/en/documents/2026-02/intel-foundry-adg-platform-brief.pdf)
18. [Intel Arizona: The Silicon Desert](https://download.intel.com/newsroom/2024/corporate/Intel-Arizona-The-Silicon-desert.pdf)
19. [Introducing the UCIe 3.0 Specification](https://www.uciexpress.org/_files/ugd/0c1418_b4744fe368c94e3e9c7eaa13ead632bf.pdf)
20. [UCIe Webinars（UCIe 3.0 发布）](https://www.uciexpress.org/webinars)
21. [The Growing Chiplet Ecosystem](https://www.uciexpress.org/post/the-growing-chiplet-ecosystem-collaboration-innovation-and-the-next-wave-of-ucie-adoption)
22. [UCIe Specifications](https://www.uciexpress.org/specifications)
23. [新浪财经：ABF载板供应链已无余量相关报道](https://finance.sina.com.cn/wm/2026-08-29/doc-inipxyyv8793330.shtml.md)
24. [IbidenとUnimicron、AIサーバー向けABF基板生産能力を大幅増強へ](https://troy-technical.jp/ibiden%e3%81%a8unimicron%e3%80%81ai%e3%82%b5%e3%83%bc%e3%83%90%e3%83%bc%e5%90%91%e3%81%91abf%e5%9f%ba%e6%9d%bf%e7%94%9f%e7%94%a3%e8%83%bd%e5%8a%9b%e3%82%92%e5%a4%a7%e5%b9%85%e5%a2%97%e5%bc%b7%e3%81%b8/)
25. [The state of ABF substrates in data center silicon in 2026](https://worldnl.com/the-state-of-abf-substrates-in-data-center-silicon-in-2026-solving-the-supply-crunch-and-material-wa-493583.html)
26. [DIGITIMES Biz Focus - News highlights](https://www.digitimes.com/biz/index.php?cat=558&pg=1)