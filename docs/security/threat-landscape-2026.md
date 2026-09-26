# 威胁态势 2026

> 最后更新：2026-09-26 ｜ 领域：安全 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

2025–2026 年的全球网络安全威胁态势呈现三个相互叠加的特征：勒索软件在「攻击量激增」与「赎金支付萎缩」之间背离，国家级 APT 活动向供应链与云基础设施纵深渗透，以及生成式 AI 被攻防双方同时武器化。权威年度报告给出的量化口径虽有差异，但方向高度一致——攻击数量与效率在上升，而防御方的成本结构正在被 AI 改写。

## 最新进展（2025–2026）

### 勒索软件：攻击量上升、支付额下降

Chainalysis《2026 Crypto Crime Report》显示，2025 年链上勒索赎金支付总额约 8.2 亿美元，同比下降约 8%，为连续第二年下降，而同期声称的攻击事件数量却上升了约 50%；与此同时，单笔赎金的中位数同比大幅上升 368%，接近 6 万美元（[Total Ransomware Payments Stagnate for Second Consecutive Year](https://www.chainalysis.com/blog/crypto-ransomware-2026/)）。Flashpoint 统计称，2026 年上半年全球已核实勒索受害者 6,256 家，较 2025 年上半年激增 45%（[Ransomware Operations, Multi-Extortion Cartels, and Financial Risk](https://flashpoint.io/resources/report/ransomware-operations-multi-extortion-cartels-and-financial-risk/)）。另有报告指出，2025 年被列于勒索泄露站点的企业约 7,300 至 7,800 家，同比增长约 45%–50%，而仅 28% 的受害者选择支付，为历史最低（[Cyber Threat Monitor](https://www.defconlevel.com/cyber-threats)）。

中国方面，新华网转引的报告显示，2025 年 7 月至 2026 年 6 月，全球活跃勒索病毒组织共 118 个，活跃度排名前 5 的组织发动的攻击占全部攻击的一半以上，集中度较高；同期共有 44 个勒索病毒组织向我国 164 个机构组织发动攻击（[报告显示：近一年来全球勒索病毒攻击事件同比增长四成](https://app.xinhuanet.com/news/article.html?articleId=2026090296ef5572cb224033bf74183b2347a0df)）。CYFIRMA 的月度跟踪则强调，勒索团伙越来越多地通过攻击面向互联网的 VPN 与远程接入设备取得特权立足点，并针对制造业及其依赖企业制造生产系统中断以加大勒索压力（[Tracking Ransomware: July 2026](https://www.cyfirma.com/research/tracking-ransomware-jul-2026/)）。

### 入侵入口的结构性变化

Verizon《2026 DBIR》（第 19 版，基于 2025 年数据）指出，软件漏洞利用以 31% 的占比首次超过被盗凭证，成为第一大入侵入口，这是 19 年来首次；报告认为 AI 让已知漏洞被武器化的时间窗口从「数月」压缩到「数小时」（[Vulnerability exploitation top breach entry point, 2026 industry-wide DBIR finds](https://www.verizon.com/about/news/breach-industry-wide-dbir-finds)）。同一份报告还给出多项变化：涉及第三方的泄露占比升至 48%（同比增长约 60%）；移动端社交工程成功率比传统邮件钓鱼高 40%；员工在工作场所使用未获批准「影子 AI」的比例从 15% 跃升至 45%；AI 机器人爬虫流量以每月约 21% 的速度增长，而人类流量几乎持平。

作为对照，上一版《2025 DBIR》统计的勒索软件出现率为 44%（同比增长 37%），漏洞利用向量增长 34%，被盗凭证占初始访问向量 22%，赎金支付中位数降至 11.5 万美元（[2025 Data Breach Investigations Report](https://www.verizon.com/business/resources/reports/2025-dbir-executive-summary.pdf)）。

### 权威成本与事件数据

IBM《2025 Cost of a Data Breach Report》显示，全球数据泄露平均成本五年来首次下降，从上一年的 488 万美元降至 444 万美元（下降 9%），回到 2023 年水平；美国平均成本则创下 1,022 万美元的纪录；全球泄露生命周期均值降至 241 天（[IBM Report: 13% Of Organizations Reported Breaches Of AI Models Or Applications](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls)）。报告同时披露，13% 的受访组织报告了 AI 模型或应用被攻破事件，其中 97% 表示缺乏适当的 AI 访问控制。

欧盟网络安全局（ENISA）《Threat Landscape 2025》基于 2024 年 7 月 1 日至 2025 年 6 月 30 日期间的 4,875 起事件分析，指出社交工程仍是首要入口，钓鱼（含 vishing、malspam、malvertising）约占 60% 的已观察案例，漏洞利用占 21.3%，僵尸网络占 9.9%，恶意应用占 8%（[ENISA Threat Landscape 2025](https://www.enisa.europa.eu/sites/default/files/2025-10/ENISA%20Threat%20Landscape%202025_0.pdf)；[EU consistently targeted by diverse yet convergent threat groups](https://www.enisa.europa.eu/news/etl-2025-eu-consistently-targeted-by-diverse-yet-convergent-threat-groups)）。ENISA 亦指出，勒索软件仍是短期影响最大的事件类型，地缘政治因素持续驱动针对欧盟关键实体的黑客行动主义 DDoS 活动（[Threat Landscape](https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape)）。

## 核心技术与关键概念

- **勒索软件即服务（RaaS）与多重勒索**：成熟平台持续降低攻击门槛，攻击者采用「先窃取、后加密」的多重勒索流程，即使受害者从备份恢复，数据公开威胁仍构成勒索杠杆（[Ransomware-as-a-Service 2026: The Modern Threat Ecosystem](https://acefortis.com/2026/08/07/ransomware-as-a-service-2026-the-modern-threat-ecosystem/)）。
- **AI 驱动的攻击流水线**：有报告称 Akira、Qilin、Scattered Spider 等团伙已将 AI 代理整合进攻击管道，用于规模化侦察（抓取 LinkedIn、GitHub、公司网站与招聘信息）与高度个性化的鱼叉钓鱼（[The State of Ransomware 2026](https://www.cybersecurityessential.com/state-of/state-of-ransomware/)）。
- **国家级 APT 的融合趋势**：间谍活动、供应链攻击、云利用与 OT 目标攻击出现收敛。Trend Micro 报告识别出供应链投毒案例：BlueNoroff 攻破 Axios 维护者账号，通过周下载量超 1 亿的软件包部署 RAT（[2026 H1 APT Report](http://www.trendmicro.com/vinfo/de/security/news/cybercrime-and-digital-threats/2026-h1-apt-report-how-apts-are-weaponizing-trust-in-the-age-of-ai)）。CYFIRMA 的季度 APT 报告指出，伊朗行为体集中于中东对手、关键基础设施、电信与政府，朝鲜行为体维持加密货币金融攻击并同时针对国防、航空航天与软件开发组织（[APT Quarterly Report: Apr to Jun 2026](https://www.cyfirma.com/research/apt-quarterly-report-apr-to-jun-2026/)）。
- **初始访问经纪（IAB）作为领先指标**：Chainalysis 认为 IAB 活动可作为勒索攻击的前瞻信号。

## 代表性机构 / 报告 / 平台

- **Verizon DBIR**：年度行业级泄露数据基准，2026 版聚焦 AI 对攻击速度的影响（[2026 DBIR](https://verizon.com/dbir)）。
- **IBM X-Force Cost of a Data Breach**：泄露成本与生命周期基准（[2025 Cost of a Data Breach Report](https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai)）。
- **ENISA Threat Landscape**：欧盟官方威胁态势年报，含 2026 版规划（[Threat Landscape](https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape)）。
- **Chainalysis Crypto Crime Report**：链上勒索支付与加密犯罪口径（[2026 Crypto Crime Report](https://www.chainalysis.com/blog/tag/2026-crypto-crime-report/)）。
- **区域评估**：美国新泽西州 NJCCIC《2026 Cyber Threat Assessment》评估国家级攻击者仍将是 2026 年及以后的首要威胁（[2026 Cyber Threat Assessment](https://www.cyber.nj.gov/threat-landscape/2026-cyber-threat-assessment)）。

## 关键数据与评测结果

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 2025 年链上勒索赎金总额 | 约 8.2 亿美元（同比 −8%） | [Chainalysis](https://www.chainalysis.com/blog/crypto-ransomware-2026/) |
| 2025 年勒索赎金中位数 | 约 6 万美元（同比 +368%） | [Chainalysis](https://www.chainalysis.com/blog/crypto-ransomware-2026/) |
| 2026 H1 已核实勒索受害者 | 6,256 家（同比 +45%） | [Flashpoint](https://flashpoint.io/resources/report/ransomware-operations-multi-extortion-cartels-and-financial-risk/) |
| 全球数据泄露平均成本（2025） | 444 万美元（同比 −9%） | [IBM](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls) |
| 漏洞利用作为首要入口（2026 DBIR） | 31% | [Verizon](https://www.verizon.com/about/news/breach-industry-wide-dbir-finds) |
| 钓鱼占已观察入侵案例（ENISA 2025） | 约 60% | [ENISA](https://www.enisa.europa.eu/sites/default/files/2025-10/ENISA%20Threat%20Landscape%202025_0.pdf) |

## 趋势与争议

- **「量增价跌」的分歧解读**：攻击量上升与支付额下降同时出现，各报告对原因存在不同口径——一方强调受害者拒付与执法打击，另一方强调单笔赎金中位数上升与勒索策略变化，尚无单一结论。
- **AI 的双面性**：DBIR 将 AI 视为加速漏洞利用与社交工程的因素；IBM 报告则将 AI 与自动化视为缩短泄露遏制时间、降低平均成本的原因之一，二者并不矛盾但需分别标注来源。
- **影子 AI 与数据外泄**：未授权 AI 工具使用比例一年内从 15% 升至 45%，成为非恶意数据泄露的第三大活动，构成新型治理风险。
- **国家级攻击与地缘政治绑定**：多份报告一致认为地缘政治持续塑造攻击目标选择，但对「国家级活动 vs 犯罪团伙」的归因与重叠程度仍有不同评估。

## 参考来源

1. [Total Ransomware Payments Stagnate for Second Consecutive Year, While Attacks Escalate — Chainalysis](https://www.chainalysis.com/blog/crypto-ransomware-2026/)
2. [2026 Crypto Crime Report — Chainalysis](https://www.chainalysis.com/blog/tag/2026-crypto-crime-report/)
3. [Ransomware Operations, Multi-Extortion Cartels, and Financial Risk — Flashpoint](https://flashpoint.io/resources/report/ransomware-operations-multi-extortion-cartels-and-financial-risk/)
4. [Cyber Threat Monitor — DEFCON Level](https://www.defconlevel.com/cyber-threats)
5. [报告显示：近一年来全球勒索病毒攻击事件同比增长四成 — 新华网](https://app.xinhuanet.com/news/article.html?articleId=2026090296ef5572cb224033bf74183b2347a0df)
6. [Tracking Ransomware: July 2026 — CYFIRMA](https://www.cyfirma.com/research/tracking-ransomware-jul-2026/)
7. [Vulnerability exploitation top breach entry point, 2026 industry-wide DBIR finds — Verizon](https://www.verizon.com/about/news/breach-industry-wide-dbir-finds)
8. [2025 Data Breach Investigations Report — Verizon](https://www.verizon.com/business/resources/reports/2025-dbir-executive-summary.pdf)
9. [IBM Report: 13% Of Organizations Reported Breaches Of AI Models Or Applications — IBM Newsroom](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls)
10. [2025 Cost of a Data Breach Report: Navigating the AI rush without sidelining security — IBM](https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai)
11. [ENISA Threat Landscape 2025 — ENISA](https://www.enisa.europa.eu/sites/default/files/2025-10/ENISA%20Threat%20Landscape%202025_0.pdf)
12. [EU consistently targeted by diverse yet convergent threat groups — ENISA](https://www.enisa.europa.eu/news/etl-2025-eu-consistently-targeted-by-diverse-yet-convergent-threat-groups)
13. [Threat Landscape — ENISA](https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape)
14. [2026 H1 APT Report — Trend Micro](http://www.trendmicro.com/vinfo/de/security/news/cybercrime-and-digital-threats/2026-h1-apt-report-how-apts-are-weaponizing-trust-in-the-age-of-ai)
15. [APT Quarterly Report: Apr to Jun 2026 — CYFIRMA](https://www.cyfirma.com/research/apt-quarterly-report-apr-to-jun-2026/)
16. [2026 Cyber Threat Assessment — NJCCIC](https://www.cyber.nj.gov/threat-landscape/2026-cyber-threat-assessment)
17. [Ransomware-as-a-Service 2026: The Modern Threat Ecosystem — AceFortis](https://acefortis.com/2026/08/07/ransomware-as-a-service-2026-the-modern-threat-ecosystem/)
18. [The State of Ransomware 2026 — Cybersecurity Essential](https://www.cybersecurityessential.com/state-of/state-of-ransomware/)