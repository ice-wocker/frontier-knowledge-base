# 合规与安全治理

> 最后更新：2026-09-26 ｜ 领域：安全 · 合规、标准与治理 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

安全合规与治理是把外部要求（法规、标准、行业规范）转化为可审计、可持续运行的内部控制的工程。企业常见的合规基线包括：ISO/IEC 27001（信息安全管理体系）、SOC 2（服务组织的控制鉴证）、NIST Cybersecurity Framework（风险管理框架）、PCI DSS（支付卡数据）、以及区域性法规如 GDPR、NIS2、DORA、欧盟《网络韧性法案》（CRA）与中国的网络安全等级保护制度。合规实践的关键不是逐框架重做，而是建立统一控制库以映射多个框架、降低证据收集开销——例如 ISO 27001 的组织、技术与人因控制可与 SOC 2 的五项信任服务准则（安全、可用性、处理完整性、保密性、隐私）良好对应（[ISO 27001 What Changed In 2026](https://www.konfirmity.com/blog/iso-27001-what-changed-in-2026)）。

治理侧的另一条主线是"监管条款本身也在被简化"：欧盟委员会在 2025 年 11 月与 2026 年 1 月提出针对 NIS2 的定向修订，目标是澄清适用范围、协调要求、对齐事件报告口径，并引入基于认证（修订后的 Cybersecurity Act，CSA2）的合规证明方式（[Navigating NIS2 Compliance March 2026（Deloitte PDF）](https://www.deloitte.com/content/dam/assets-zone2/be/en/docs/services/consulting/2026/be-deloitte-nis2-whitepaper-march-2026.pdf)）。

## 最新进展（2025–2026）

**ISO/IEC 27001 完成版本迁移。** ISO/IEC 27001:2013 的三年过渡窗口在 2025 年 10 月 31 日关闭，2013 版证书全部失效，新发与换发证书一律使用 ISO/IEC 27001:2022，其 Annex A 为四个主题（组织、人员、物理、技术）下的 93 项控制（[ISO 27001 What Changed In 2026](https://www.konfirmity.com/blog/iso-27001-what-changed-in-2026)、[SOC 2 vs ISO 27001](https://riskpublishing.com/soc-2-vs-iso-27001-which-security-certificatio/)）。2022 版把 Annex A 从 14 个章节 114 项控制重组为四主题 93 项，新增 11 项针对云安全与威胁情报的控制，并合并了若干冗余控制；核心要求位于第 4–10 章（[SOC 2 vs ISO 27001（securitycomplianceguide）](https://securitycomplianceguide.com/blog/soc-2-vs-iso-27001/)）。有整理指出截至 2026 年 3 月 NIS2 已进入实际执法阶段（[SOC 2 vs ISO 27001（strongcyber）](https://strongcybersolutions.com/soc-2-vs-iso-27001-which-should-you-pursue-first/)）。

**NIS2 的落地进度参差。** 成员国原定 2024 年 10 月 17 日前完成转化，但部分国家未按时通报完整转化措施，欧盟委员会已将爱尔兰、西班牙、法国与荷兰提交欧盟法院（[Commission refers Ireland, Spain, France and the Netherlands to the Court of Justice](https://digital-strategy.ec.europa.eu/en/news/commission-refers-ireland-spain-france-and-netherlands-court-justice-failing-transpose-rules)）。2026 年 1 月 20 日，委员会在新网络安全一揽子方案中提出对 NIS2 的定向修订以提高法律确定性（[NIS2-Richtlinie](https://digital-strategy.ec.europa.eu/de/policies/nis2-directive)）。国别节奏也不同：意大利要求组织在 2026 年 10 月前完成合规（过渡期），重大事件通知义务须在 9 个月内落实（[Deloitte NIS2 白皮书](https://www.deloitte.com/content/dam/assets-zone2/be/en/docs/services/consulting/2026/be-deloitte-nis2-whitepaper-march-2026.pdf)）。

**DORA 进入适用期并细化本地实施。** 欧盟《数字运营韧性法案》（DORA，Regulation (EU) 2022/2554）自 2025 年 1 月 17 日起适用，要求金融实体建立覆盖治理、资产清单、风险识别、保护、检测、响应、恢复与持续改进的 ICT 风险管理框架，并对重大 ICT 相关事件进行检测、分类与报告（[Digital operational resilience for the financial sector（EUR-Lex）](https://eur-lex.europa.eu/EN/legal-content/summary/digital-operational-resilience-for-the-financial-sector.html)、[Preparedness union strategy for the EU financial sector（COM:2026:119）](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=COM:2026:119:FIN)）。除微型企业外的金融实体须维护数字化运营韧性测试计划，并至少每三年开展一次基于风险画像的威胁导向渗透测试（TLPT），且测试方须经认证、具备专业能力与职业赔偿保险（[EUR-Lex](https://eur-lex.europa.eu/EN/legal-content/summary/digital-operational-resilience-for-the-financial-sector.html)）。第三方 ICT 服务商管理方面，RTS（Commission Delegated Regulation (EU) 2024/1531）要求政策明确对支撑关键或重要功能的服务商风险管理框架的保证水平，尽职调查需评估风险缓解与业务连续性措施、适当第三方认证等的使用（[Commission Delegated Regulation (EU) 2024/1531](https://ec.europa.eu/finance/docs/level-2-measures/dora-regulation-rts--2024-1531_en.pdf)）。2026 年 8 月 27 日，卢森堡 CSSF 就 DORA 适用于在卢设立的第三国分支机构发布公告（[CSSF](https://www.cssf.lu/fr/tic-et-cyber-risque-pour-les-entites-dora/)）。

**GDPR 执法规模跨过新台阶。** CMS GDPR Enforcement Tracker Report 2026 显示，截至 2026 年报告期，累计罚款首次突破 60 亿欧元，达到约 61.1 亿欧元（较 2025 年报告增加约 4.876 亿欧元）；2018–2026 年间的平均罚款约 228 万欧元，但均值仍被少数超大额罚款严重影响（[GDPR Enforcement Tracker Report 2026（CMS PDF）](https://cms.law/en/content/download/882763/file/Enforcement-Tracker-Report%202026_Executive%20Summary_f.pdf?v=9:.GDPR)）。2026 年 9 月 23 日，爱尔兰数据保护委员会就 Google 处理位置数据对其罚款 4.03 亿欧元（[The Irish Data Protection Commission fines Google 403 000 000 EUR](https://www.edpb.europa.eu/news/the-irish-data-protection-commission-fines-google-403-000-000-eur-following-inquiry-into_en)）；中文报道称该裁决于 2026 年 9 月 21 日宣布、罚款逾 4 亿欧元，涉及 2018 年 5 月 GDPR 生效至 2020 年 2 月调查启动期间的位置数据处理（[谷歌被欧盟开出逾4亿欧元"罚单"](https://m.gmw.cn/2026-09/22/content_1304566612.htm)）。同期还有 CNIL 对 EXTIA 罚款 30 万欧元、对 Hôpital Privé de la Loire 就健康数据泄露罚款等案例（[EDPB News](https://www.edpb.europa.eu/news_en)）。

**CRA、PCI DSS 与 CMMC 的时间线。** CRA（Regulation (EU) 2024/2847）于 2024 年 12 月 10 日生效，报告义务自 2026 年 9 月适用、大部分义务自 2027 年 12 月 11 日适用（[CRA FAQ](https://www.cyberresilienceact.eu/ja/faq.html)）。PCI DSS 方面，v4.0.1 自 2024 年 12 月 31 日起成为唯一有效版本，4.0 中的 51 项"未来生效"要求已于 2025 年 3 月 31 日全部强制，2026 年的所有评估均按 4.0.1 执行、无过渡宽限（[PCI DSS 4.0 compliance playbook](https://www.scrut.io/post/pci-dss-4-0-compliance-playbook)、[PCI DSS v4.0 & v4.0.1: Everything That Changed](https://ghost.securitywall.co/pci-dss-v4-changes-2026/)）。美国国防部方面，2026 年 7 月 13 日宣布立即暂停 CMMC Phase II 要求（原定 2026 年 11 月 10 日实施），Phase I 自评估要求保持不变，并将启动全面审查以对齐采办转型指令（[About CMMC（DoW CIO）](https://dowcio.war.gov/cmmc/About/)）；暂停强制第三方评估并不免除承包商保护 CUI、落实 NIST SP 800-171 Rev.2 控制以满足 CMMC Level 2 分数、并向分包商传递相应合同要求的既有义务（[What Defense Contractors Should Know About DOD's Suspension of CMMC Phase 2](https://www.lw.com/en/insights/what-defense-contractors-should-know-about-dod-suspension-of-cmmc-phase-2)）。

**框架侧与预算侧。** NIST CSF 2.0 于 2024 年发布，新增 Govern 功能、强化网络安全供应链风险管理，并扩展为一套便于落地的资源（[Celebrating Two Years of CSF 2.0!](https://www.nist.gov/blogs/cybersecurity-insights/celebrating-two-years-csf-20)）。2026 年 8 月，NIST 发布 SP 1353 ipd《使用人工智能进行 CSF 分析与报告的快速上手指南》初稿并公开征求意见（[Seeking Public Comment! Using AI for CSF 2.0 Analysis and Reporting](https://www.nist.gov/news-events/news/2026/08/seeking-public-comment-using-artificial-intelligence-cybersecurity)）。AI 治理方面，ISO/IEC 42001:2023 提供 AI 管理体系框架（[ISO/IEC 42001:2023](https://www.iso.org/fr/standard/42001)），已被部分企业的 AI 治理平台取得认证（[Fragmented Governance, Misread Mandate（CSA）](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-governance-fragmentation-20260908-csa-s/)）；EU AI Act 的高风险条款自 2026 年 8 月 2 日起可执行，违规罚款最高可达 1,500 万欧元或全球年营业额 3%，最严重的禁止性做法违规可达 3,500 万欧元或 7%（[EU AI Act 2026: The Complete ISO 42001 Compliance Blueprint](https://pecb.com.ua/en/eu-ai-act-iso-42001-compliance-guide-2026/)）。支出侧，Gartner 2Q26 预测（2026 年 6 月 25 日发布）显示 2026 年全球信息安全支出达 2,489 亿美元、按不变汇率增长 12.7%，到 2030 年达 3,726 亿美元（[Gartner's $248.9B security forecast](https://softwarestrategiesblog.com/category/zero-trust-security/)）；另有 Gartner 新闻稿称 2026 年将达 2,400 亿美元、同比增长 12.5%（[Gartner 预测 2026 年全球信息安全支出 2400 亿美元](https://www.gartner.com/cn/newsroom/press-releases/2025-sec-spending)）——两个口径存在差异，需分别标注来源。

**中国合规基线。** 《网络安全法》第 21 条明确"国家实行网络安全等级保护制度"，第 31 条规定对关键信息基础设施在等级保护制度基础上实行重点保护（[中华人民共和国网络安全法（公安部）](https://www.isccc.gov.cn/xxgk1/zcfg_3/flhxzfg/202603/t20260305_11199.htm)）。公安部对等级保护 2.0 的解读指出，2017 年《网络安全法》实施标志等级保护 2.0 正式启动（[网络安全等级保护2.0标准解读](https://www.mps.gov.cn:9080/n6557563/c7369073/content.html)）；《关键信息基础设施安全保护条例》界定了 CII 范围，并规定在国家网信部门统筹协调下、由国务院公安部门负责指导监督 CII 安全保护工作（[关键信息基础设施安全保护条例](http://xzfg.moj.gov.cn/front/law/detail?LawID=683)）。

## 核心技术与关键概念

- **统一控制库与框架映射**：以一套控制映射多个框架，减少重复取证（[Konfirmity](https://www.konfirmity.com/blog/iso-27001-what-changed-in-2026)）。
- **SOC 2 的五项信任服务准则**：安全、可用性、处理完整性、保密性、隐私（[Konfirmity](https://www.konfirmity.com/blog/iso-27001-what-changed-in-2026)）。
- **ISO 27001:2022 的结构**：核心要求在第 4–10 章（上下文、领导力、策划、支持、运行、绩效评价、改进），Annex A 为四主题 93 项控制（[securitycomplianceguide](https://securitycomplianceguide.com/blog/soc-2-vs-iso-27001/)）。
- **DORA 的四大支柱式要求**：ICT 风险管理框架、事件检测分类报告、数字化运营韧性测试（含 TLPT）、第三方 ICT 风险管理（[EUR-Lex](https://eur-lex.europa.eu/EN/legal-content/summary/digital-operational-resilience-for-the-financial-sector.html)、[COM:2026:119](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=COM:2026:119:FIN)）。
- **CSF 2.0 的 Govern 功能**：把治理、供应链风险与组织画像纳入框架核心（[NIST](https://www.nist.gov/blogs/cybersecurity-insights/celebrating-two-years-csf-20)）。
- **等级保护的制度位置**：作为《网络安全法》确立的基础性制度，并与 CII 重点保护衔接（[公安部](https://www.mps.gov.cn/n6557563/c7369120/content.html)）。
- **审计与证据**：以风险分析为前提设计控制与缓解措施，并以认证/鉴证报告作为对外证明（[EUR-Lex DORA](https://eur-lex.europa.eu/EN/legal-content/summary/digital-operational-resilience-for-the-financial-sector.html)、[VCA](https://www.vehicle-certification-agency.gov.uk/connected-and-automated-vehicles/cyber-security-and-software-updating/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **标准与框架**：ISO/IEC 27001:2022（[ISO](https://www.iso.org/fr/standard/42001)）、ISO/IEC 42001:2023 AI 管理体系（同上）、NIST CSF 2.0（[NIST](https://www.nist.gov/cyberframework)）、AICPA SOC 2（[Konfirmity](https://www.konfirmity.com/blog/iso-27001-what-changed-in-2026)）、PCI DSS 4.0.1（[PCI SSC](https://www.pcisecuritystandards.org/pdfs/pci_lifecycle_for_changes_to_dss_and_padss.pdf)）、CMMC（[DoW CIO](https://dowcio.war.gov/cmmc/About/)）。
- **法规与监管机构**：EU NIS2（[EC](https://digital-strategy.ec.europa.eu/de/policies/nis2-directive)）、DORA（[EIOPA](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en)）、CRA（[EC](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)）、GDPR 与 EDPB（[EDPB](https://www.edpb.europa.eu/news_en)）、中国网信办/公安部（[CAC](https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm)）。
- **合规工具与生态**：统一控制库与映射工具（[Konfirmity](https://www.konfirmity.com/blog/iso-27001-what-changed-in-2026)）、GDPR 罚款追踪（[CMS](https://cms.law/en/content/download/882763/file/Enforcement-Tracker-Report%202026_Executive%20Summary_f.pdf?v=9:.GDPR)）。

## 关键数据与评测结果（附来源）

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| ISO 27001:2013 过渡截止 | 2025-10-31（证书失效） | [riskpublishing](https://riskpublishing.com/soc-2-vs-iso-27001-which-security-certificatio/) |
| ISO 27001:2022 Annex A 控制数 | 93 项 / 四主题（新增 11 项） | [securitycomplianceguide](https://securitycomplianceguide.com/blog/soc-2-vs-iso-27001/) |
| GDPR 累计罚款 | 约 61.1 亿欧元（首次破 60 亿） | [CMS Report 2026](https://cms.law/en/content/download/882763/file/Enforcement-Tracker-Report%202026_Executive%20Summary_f.pdf?v=9:.GDPR) |
| GDPR 平均罚款（2018–2026） | 约 228 万欧元 | 同上 |
| Google 位置数据罚款 | 4.03 亿欧元（2026-09-23） | [EDPB](https://www.edpb.europa.eu/news/the-irish-data-protection-commission-fines-google-403-000-000-eur-following-inquiry-into_en) |
| NIS2 转化截止 | 2024-10-17（四国被诉） | [EC](https://digital-strategy.ec.europa.eu/en/news/commission-refers-ireland-spain-france-and-netherlands-court-justice-failing-transpose-rules) |
| DORA 适用起始 | 2025-01-17 | [EIOPA](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) |
| PCI DSS 未来生效要求强制日 | 2025-03-31（共 51 项） | [Scrut](https://www.scrut.io/post/pci-dss-4-0-compliance-playbook) |
| CMMC Phase II | 2026-07-13 暂停（原定 2026-11-10） | [DoW CIO](https://dowcio.war.gov/cmmc/About/) |
| 2026 全球信息安全支出 | 2,489 亿美元 / +12.7%（不变汇率，2Q26 预测） | [softwarestrategiesblog](https://softwarestrategiesblog.com/category/zero-trust-security/) |
| 2026 全球信息安全支出（另一口径） | 2,400 亿美元 / +12.5% | [Gartner 新闻稿](https://www.gartner.com/cn/newsroom/press-releases/2025-sec-spending) |

## 趋势与争议

- **合规不等于安全，但合规在加速**：CRA、NIS2、DORA、CMMC、PCI DSS 4.0.1 等在同一时期集中生效或收紧，组织面临多重时间线叠加（[CRA FAQ](https://www.cyberresilienceact.eu/ja/faq.html)、[Deloitte NIS2](https://www.deloitte.com/content/dam/assets-zone2/be/en/docs/services/consulting/2026/be-deloitte-nis2-whitepaper-march-2026.pdf)）。
- **监管自身在"简化"**：NIS2 的定向修订与 Digital Omnibus 均以降低合规复杂度和提升法律确定性为目标，同时也引发对义务被稀释的讨论（[EC NIS2](https://digital-strategy.ec.europa.eu/de/policies/nis2-directive)、[EDPB-EDPS JOINT OPINION 2/2026](https://www.edpb.europa.eu/system/files/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf)）。
- **政策反复带来规划不确定性**：CMMC Phase II 的暂停表明强制第三方评估的节奏可能随政策调整而变化，但底层控制义务未随之取消（[DoW CIO](https://dowcio.war.gov/cmmc/About/)、[Latham & Watkins](https://www.lw.com/en/insights/what-defense-contractors-should-know-about-dod-suspension-of-cmmc-phase-2)）。
- **AI 治理的框架错位**：ISO/IEC 42001 与 EU AI Act 的适用对象与义务结构不同，存在"治理碎片化、授权被误读"的风险，需要有意识地做义务映射（[CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-governance-fragmentation-20260908-csa-s/)、[PECB](https://pecb.com.ua/en/eu-ai-act-iso-42001-compliance-guide-2026/)）。
- **预测与统计口径差异**：Gartner 同一年的安全支出存在 2,489 亿与 2,400 亿美元两种表述，分别发布于不同材料，引用时须注明来源与口径（[softwarestrategiesblog](https://softwarestrategiesblog.com/category/zero-trust-security/)、[Gartner](https://www.gartner.com/cn/newsroom/press-releases/2025-sec-spending)）。

## 参考来源

- [ISO 27001 What Changed In 2026（Konfirmity）](https://www.konfirmity.com/blog/iso-27001-what-changed-in-2026)
- [SOC 2 vs ISO 27001: Which Security Certification to Pursue（riskpublishing）](https://riskpublishing.com/soc-2-vs-iso-27001-which-security-certificatio/)
- [SOC 2 vs ISO 27001（securitycomplianceguide）](https://securitycomplianceguide.com/blog/soc-2-vs-iso-27001/)
- [SOC 2 vs ISO 27001: Which Should You Pursue First?（strongcyber）](https://strongcybersolutions.com/soc-2-vs-iso-27001-which-should-you-pursue-first/)
- [The State of Compliance 2026: A CISO's Guide](https://www.cybersecurityessential.com/state-of/state-of-compliance/)
- [Navigating NIS2 Compliance March 2026（Deloitte PDF）](https://www.deloitte.com/content/dam/assets-zone2/be/en/docs/services/consulting/2026/be-deloitte-nis2-whitepaper-march-2026.pdf)
- [NIS2-Richtlinie（European Commission）](https://digital-strategy.ec.europa.eu/de/policies/nis2-directive)
- [Commission refers Ireland, Spain, France and the Netherlands to the Court of Justice](https://digital-strategy.ec.europa.eu/en/news/commission-refers-ireland-spain-france-and-netherlands-court-justice-failing-transpose-rules)
- [Digital operational resilience for the financial sector（EUR-Lex）](https://eur-lex.europa.eu/EN/legal-content/summary/digital-operational-resilience-for-the-financial-sector.html)
- [Digital Operational Resilience Act (DORA)（EIOPA）](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en)
- [Preparedness union strategy for the EU financial sector（COM:2026:119）](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=COM:2026:119:FIN)
- [Commission Delegated Regulation (EU) 2024/1531（DORA RTS）](https://ec.europa.eu/finance/docs/level-2-measures/dora-regulation-rts--2024-1531_en.pdf)
- [CSSF：TIC et cyber-risque – pour les entités DORA](https://www.cssf.lu/fr/tic-et-cyber-risque-pour-les-entites-dora/)
- [GDPR Enforcement Tracker Report 2026（CMS PDF）](https://cms.law/en/content/download/882763/file/Enforcement-Tracker-Report%202026_Executive%20Summary_f.pdf?v=9:.GDPR)
- [The Irish Data Protection Commission fines Google 403 000 000 EUR（EDPB）](https://www.edpb.europa.eu/news/the-irish-data-protection-commission-fines-google-403-000-000-eur-following-inquiry-into_en)
- [谷歌被欧盟开出逾4亿欧元"罚单"（光明网）](https://m.gmw.cn/2026-09/22/content_1304566612.htm)
- [EDPB News](https://www.edpb.europa.eu/news_en)
- [Cyber Resilience Act FAQ（时间表）](https://www.cyberresilienceact.eu/ja/faq.html)
- [Cyber Resilience Act（European Commission）](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
- [PCI DSS 4.0 compliance playbook（Scrut）](https://www.scrut.io/post/pci-dss-4-0-compliance-playbook)
- [PCI DSS v4.0 & v4.0.1: Everything That Changed](https://ghost.securitywall.co/pci-dss-v4-changes-2026/)
- [PCI Security Standards Council: Lifecycle for Changes to PCI DSS and PA-DSS](https://www.pcisecuritystandards.org/pdfs/pci_lifecycle_for_changes_to_dss_and_padss.pdf)
- [About CMMC（Department of War CIO）](https://dowcio.war.gov/cmmc/About/)
- [What Defense Contractors Should Know About DOD's Suspension of CMMC Phase 2（Latham & Watkins）](https://www.lw.com/en/insights/what-defense-contractors-should-know-about-dod-suspension-of-cmmc-phase-2)
- [Celebrating Two Years of CSF 2.0!（NIST）](https://www.nist.gov/blogs/cybersecurity-insights/celebrating-two-years-csf-20)
- [Seeking Public Comment! Using AI for Cybersecurity Framework 2.0 Analysis and Reporting（NIST）](https://www.nist.gov/news-events/news/2026/08/seeking-public-comment-using-artificial-intelligence-cybersecurity)
- [Cybersecurity Framework（NIST）](https://www.nist.gov/cyberframework)
- [ISO/IEC 42001:2023（ISO）](https://www.iso.org/fr/standard/42001)
- [Fragmented Governance, Misread Mandate: ISO 42001 and the EU AI Act（CSA）](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-governance-fragmentation-20260908-csa-s/)
- [EU AI Act 2026: The Complete ISO 42001 Compliance Blueprint（PECB）](https://pecb.com.ua/en/eu-ai-act-iso-42001-compliance-guide-2026/)
- [Gartner's $248.9B security forecast（softwarestrategiesblog）](https://softwarestrategiesblog.com/category/zero-trust-security/)
- [Gartner 预测 2026 年全球终端用户信息安全支出将达到 2400 亿美元](https://www.gartner.com/cn/newsroom/press-releases/2025-sec-spending)
- [中华人民共和国网络安全法（公安部）](https://www.isccc.gov.cn/xxgk1/zcfg_3/flhxzfg/202603/t20260305_11199.htm)
- [中华人民共和国网络安全法（中央网信办）](https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm)
- [落实网络安全等级保护制度和关键信息基础设施安全保护制度解读（公安部）](https://www.mps.gov.cn/n6557563/c7369120/content.html)
- [网络安全等级保护2.0标准解读（公安部）](https://www.mps.gov.cn:9080/n6557563/c7369073/content.html)
- [关键信息基础设施安全保护条例（司法部）](http://xzfg.moj.gov.cn/front/law/detail?LawID=683)