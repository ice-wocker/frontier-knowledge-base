# 攻防安全与漏洞赏金

> 最后更新：2026-09-26 ｜ 领域：安全 · 攻防演练与漏洞经济 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

攻防安全（offensive security）涵盖渗透测试、红队演练、漏洞挖掘与协调披露（CVD）、漏洞赏金计划以及漏洞交易市场。其经济逻辑在 2025–2026 年发生明显位移：Verizon《2026 DBIR》显示，漏洞利用首次成为最常见的初始访问向量，占比从上一年的 20% 升至 31%，而凭据滥用降至 13%（[2026 Data Breach Investigations Report](https://www.verizon.com/business/resources/T158/reports/2026-dbir-data-breach-investigations-report.pdf)）。分析认为这反映了攻击者经济学的可测变化——利用一个未修补的、面向互联网的缺陷变得更快、更便宜（[AI-Accelerated Exploitation and Asymmetric Vulnerability Velocity（CSA）](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/ai-accelerated-exploitation-systemic-risk-v1-csa-styled.pdf)）。

## 最新进展（2025–2026）

**漏洞数量压垮了传统跟踪体系。** CSA 白皮书给出 2025 年的数字：NIST 当年发布约 48,185 条 CVE，较 2020 年增长 263%；2020 年时 21 人的 NVD 团队每年需富化约 18,000 条（[The NVD Infrastructure Crisis: AI Discovery Overwhelms Tracking](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_whitepaper_NVD_infrastructure_crisis_AI_vulnerability_discovery_20260504-csa-styled.pdf)）。2026 年 4 月 15 日，NIST 正式将 NVD 转为基于风险的分诊模型，约 29,000 条积压 CVE 被重新分类为 "Not Scheduled"，此后仅 CISA KEV 目录内的 CVE 等被纳入优先富化范围（[NVD Enrichment Triage: Enterprise Vulnerability Programs Must Adapt（CSA）](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_nist-nvd-enrichment-policy-change_20260419-csa-styled-1.pdf)）。中文报道同样指出 2025 年处理近 42,000 条 CVE 后，积压未处理总量仍超过 3 万条（[NIST突然宣布：漏洞太多，处理不过来了](https://www.secrss.com/articles/89561)）。NVD 官方仪表盘（抓取时点）显示当年新增接收 CVE 约 7.07 万条、完成分析约 3.69 万条（[NVD Dashboard](https://nvd.nist.gov/general/nvd-dashboard)）。

**AI 开始自主发现真实漏洞。** Google Project Zero 于 2024 年 10 月公布、11 月正式披露 Big Sleep（其前身为 Naptime 研究框架）在 SQLite 中发现真实的内存破坏漏洞——意义不在漏洞本身，而在于 LLM 代理通过"假设生成—代码检查—验证"的循环自主完成了发现（[The Collapsing Exploit Window（CSA）](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_whitepaper_collapsing_exploit_window_systemic_risk_20260423-csa-styled.pdf)）。这是 AI 代理首次在广泛部署的真实软件中找出可利用的、此前未知的内存安全缺陷，但它是防御性工具，由 Google 研究者运行，漏洞在进入正式版本前已被修复（[AI-Built Zero-Day: Google Catches First Real-World Exploit](https://nerdleveltech.com/ai-built-zero-day-google-gtig-first-real-world-exploit)）。据 2026 年 9 月的报道，Big Sleep 已累计发现 20 个开源漏洞（[Google's AI 'Big Sleep' Finds 20 Open-Source Vulnerabilities](https://ai-damn.com/google-s-ai-big-sleep-finds-20-open-source-vulnerabilities-1754367618012)）。

**自主渗透系统的基准表现。** XBOW 于 2025 年 6 月成为首个登上 HackerOne 美国排行榜第一的自主系统，超过所有人类参与者（[Taking the Top Hacker in the US to New Heights: XBOW Raises $75M Series B](https://xbow.com/blog/series-b)）。其后续披露称，两年间其代理在 HackerOne 上提交 1,060 个以上漏洞、执行 48 步利用链、17 分钟攻破密码学实现，并在 28 分钟内完成相当于首席渗透测试师 40 小时评估的工作量，全程无需人工介入（[We Ran 1,060 Autonomous Attacks](https://xbow.com/blog/we-ran-1060-autonomous-attacks)）。

**赏金经济规模。** HackerOne《Hacker-Powered Security Report 2025》基于 58 万余个已验证漏洞、当年 8,100 万美元赏金支出与 1,950 个企业项目的数据，强调"韧性来自执行而非覆盖率"——清晰的范围、快速分诊与有竞争力的奖励能挖出更多严重缺陷（[Hacker-Powered Security Report 2025](https://www.hackerone.com/report/hacker-powered-security)）。平台的支付口径需分别引用：HackerOne 市场支出为 8,100 万美元，而 Microsoft 仅自家产品就支付超过 2,000 万美元，两者统计范围与日历不同（[Bug Bounty Program Payouts by Platform Statistics 2026](https://commandlinux.com/statistics/bug-bounty-program-payouts-by-platform/)）。中高危被接受报告的平均报酬大致在 500–5,000 美元，大型项目严重漏洞可达 5 万至 10 万美元以上；Microsoft 2025 年的 Zero Day Quest 在 HackerOne 上运行，单次活动为云与 AI 漏洞支付超过 160 万美元（[Top 5 Bug Bounty Platforms for Security Researchers in 2026](https://guptadeepak.com/top-5-bug-bounty-platforms-for-security-researchers-in-2026/)）。

## 核心技术与关键概念

- **渗透测试与自动化**：完整自主的 AI 渗透测试可在真实生产系统上运行，且能构建多步利用链（[XBOW](https://xbow.com/blog/we-ran-1060-autonomous-attacks)）。
- **协调漏洞披露（CVD）**：赏金平台为报告方提供渠道，目录页可见各项目的奖励区间与响应状态（[HackerOne Directory](https://hackerone.com/directory/programs)）。
- **评分与优先级体系**：CVSS、EPSS、CISA KEV 各有适用边界；同一 CVE 可同时出现 NVD 9.9、厂商 7.0、CVSS v4 6.3 三种评分，直接取最高值会丢弃最重要的信息——分歧本身（[When One CVE Has Three Scores, Taking the Highest Is Not Caution](https://safeguard.sh/resources/blog/severity-inflation-when-scanners-disagree)）。
- **可利用性的前提条件**：一个 CVE 若仅在特定操作系统、开发服务器与可访问端口同时满足时才可利用，则"版本匹配"并不等于"可利用"；把每条咨询的前置条件列清楚，才能把 lockfile 差异转化为有效论证（[The Version String Is Not the Vulnerability](https://safeguard.sh/resources/blog/exploitability-preconditions-beyond-the-version-string)）。
- **"未证实"不等于"无漏洞"**：可利用性并非布尔值，把不确定性直接折叠为否定会掩盖开发者的下一步动作（["Not Demonstrated" Is Not "Not Vulnerable"](https://safeguard.sh/resources/blog/not-demonstrated-is-not-not-vulnerable)）。
- **补丁与遏制窗口**：对面向互联网资产的关键 CVE（CVSS ≥ 7.0）可采用 24 小时补丁 SLA 与免 CAB 预授权补丁，并辅以 AI 驱动的自动遏制（[Ransomware en 24 heures](https://ayinedjimi-consultants.fr/articles/ransomware-24h-fin-reponse-lente-securite)、[Unit 42 Global IR Report 2026](https://start.paloaltonetworks.com/rs/531-OCS-018/images/Unit42-Global-Incident-Response-Report.pdf?version=0)）。
- **自主渗透测试的评测口径**：自主代理可在真实生产系统上持续运行并直接向平台提交结果，其披露的能力指标（利用链长度、攻破耗时、与人类评估的对照）需结合具体的测试范围与时间盒来理解，不同厂商的对照条件并不统一（[XBOW](https://xbow.com/blog/we-ran-1060-autonomous-attacks)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **赏金平台**：HackerOne（[hackerone.com](https://www.hackerone.com/report/hacker-powered-security)）、Bugcrowd 等；平台目录可见 AI 相关项目（如 Nebius AI VDP）（[HackerOne Directory](https://hackerone.com/directory/programs)）。
- **厂商项目**：Microsoft Zero Day Quest（云与 AI 方向，[guptadeepak 汇总](https://guptadeepak.com/top-5-bug-bounty-platforms-for-security-researchers-in-2026/)）。
- **AI 攻防产品**：XBOW（自主渗透测试，[xbow.com](https://xbow.com/blog/series-b)）、Google Big Sleep（防御性自主漏洞发现，[CSA](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_whitepaper_collapsing_exploit_window_systemic_risk_20260423-csa-styled.pdf)）。
- **数据与标准**：NVD（[nvd.nist.gov](https://nvd.nist.gov/general/nvd-dashboard)）、CISA KEV、CVSS/EPSS（[Safeguard 分析](https://safeguard.sh/resources/blog/severity-inflation-when-scanners-disagree)）。

## 关键数据与评测结果（附来源）

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| Verizon DBIR 漏洞利用初始向量占比 | 31%（上年 20%） | [Verizon DBIR 2026](https://www.verizon.com/business/resources/T158/reports/2026-dbir-data-breach-investigations-report.pdf) |
| 2025 年 NIST 发布 CVE 数 | 约 48,185 条（较 2020 年 +263%） | [CSA](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_whitepaper_NVD_infrastructure_crisis_AI_vulnerability_discovery_20260504-csa-styled.pdf) |
| NVD 重新分类为 Not Scheduled 的积压 CVE | 约 29,000 条 | [CSA](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_nist-nvd-enrichment-policy-change_20260419-csa-styled-1.pdf) |
| 2025 年 KEV 漏洞完全修复比例 | 26% | [Verizon DBIR 2026](https://www.verizon.com/business/resources/T158/reports/2026-dbir-data-breach-investigations-report.pdf) |
| HackerOne 2025 年赏金支出 | 8,100 万美元 | [HackerOne](https://www.hackerone.com/report/hacker-powered-security) |
| HackerOne 已验证漏洞基数 | 58 万+ | 同上 |
| Microsoft Zero Day Quest 单次支出 | 160 万美元以上 | [guptadeepak](https://guptadeepak.com/top-5-bug-bounty-platforms-for-security-researchers-in-2026/) |
| XBOW 提交漏洞数 | 1,060+ | [XBOW](https://xbow.com/blog/we-ran-1060-autonomous-attacks) |
| Big Sleep 发现开源漏洞数 | 20（2026 年 9 月报道） | [ai-damn](https://ai-damn.com/google-s-ai-big-sleep-finds-20-open-source-vulnerabilities-1754367618012) |

## 趋势与争议

- **"利用窗口"坍塌**：AI 自主发现把补丁周期从数月压缩到数小时，防御方与攻击方在漏洞发现上的速度差成为系统性风险（[CSA](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_whitepaper_collapsing_exploit_window_systemic_risk_20260423-csa-styled.pdf)）。
- **跟踪基础设施危机**：CVE 增速超出 NVD 富化能力，NVD 转向 CISA KEV 优先的风险分诊（[CSA](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_nist-nvd-enrichment-policy-change_20260419-csa-styled-1.pdf)），而仅依赖 CVE/KEV 的组织对恶意发布类攻击反应迟缓（[Safeguard](https://safeguard.sh/resources/blog/the-shai-hulud-npm-supply-chain-attack-explained)）。
- **自主系统 vs 人类黑客**：XBOW 称其 AI 已在 HackerOne 美国榜登顶并可比肩首席渗透测试师，但这类对比的评测条件（范围、时间盒、目标类型）在各家披露中并不统一（[XBOW](https://xbow.com/blog/series-b)、[XBOW](https://xbow.com/blog/we-ran-1060-autonomous-attacks)）。
- **评分与优先级的分歧**：厂商、NVD 与 CVSS v4 的分数不一致时如何取舍，以及"版本匹配"与"实际可利用"之间的差距，仍是漏洞管理实践中的主要争议（[Safeguard](https://safeguard.sh/resources/blog/severity-inflation-when-scanners-disagree)、[Safeguard](https://safeguard.sh/resources/blog/exploitability-preconditions-beyond-the-version-string)）。
- **赏金支出口径**：市场支出与厂商自付支出、以及各平台不同的统计日历，使"总赏金"数字难以直接比较（[commandlinux](https://commandlinux.com/statistics/bug-bounty-program-payouts-by-platform/)）。

## 参考来源

- [2026 Data Breach Investigations Report（Verizon PDF）](https://www.verizon.com/business/resources/T158/reports/2026-dbir-data-breach-investigations-report.pdf)
- [AI-Accelerated Exploitation and Asymmetric Vulnerability Velocity（CSA PDF）](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/ai-accelerated-exploitation-systemic-risk-v1-csa-styled.pdf)
- [The NVD Infrastructure Crisis: AI Discovery Overwhelms Tracking（CSA PDF）](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_whitepaper_NVD_infrastructure_crisis_AI_vulnerability_discovery_20260504-csa-styled.pdf)
- [NVD Enrichment Triage: Enterprise Vulnerability Programs Must Adapt（CSA PDF）](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_nist-nvd-enrichment-policy-change_20260419-csa-styled-1.pdf)
- [The Collapsing Exploit Window: Systemic Consequences of AI-Autonomous Vulnerability Discovery at Scale（CSA PDF）](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_whitepaper_collapsing_exploit_window_systemic_risk_20260423-csa-styled.pdf)
- [NVD Dashboard](https://nvd.nist.gov/general/nvd-dashboard)
- [NIST突然宣布：漏洞太多，处理不过来了（安全内参）](https://www.secrss.com/articles/89561)
- [AI-Built Zero-Day: Google Catches First Real-World Exploit](https://nerdleveltech.com/ai-built-zero-day-google-gtig-first-real-world-exploit)
- [Google's AI 'Big Sleep' Finds 20 Open-Source Vulnerabilities](https://ai-damn.com/google-s-ai-big-sleep-finds-20-open-source-vulnerabilities-1754367618012)
- [Taking the Top Hacker in the US to New Heights: XBOW Raises $75M Series B](https://xbow.com/blog/series-b)
- [We Ran 1,060 Autonomous Attacks. Here's What the Industry Gets Wrong.](https://xbow.com/blog/we-ran-1060-autonomous-attacks)
- [Hacker-Powered Security Report 2025（HackerOne）](https://www.hackerone.com/report/hacker-powered-security)
- [HackerOne Directory（Programs）](https://hackerone.com/directory/programs)
- [Bug Bounty Program Payouts by Platform Statistics 2026](https://commandlinux.com/statistics/bug-bounty-program-payouts-by-platform/)
- [Top 5 Bug Bounty Platforms for Security Researchers in 2026](https://guptadeepak.com/top-5-bug-bounty-platforms-for-security-researchers-in-2026/)
- [When One CVE Has Three Scores, Taking the Highest Is Not Caution](https://safeguard.sh/resources/blog/severity-inflation-when-scanners-disagree)
- [The Version String Is Not the Vulnerability](https://safeguard.sh/resources/blog/exploitability-preconditions-beyond-the-version-string)
- ["Not Demonstrated" Is Not "Not Vulnerable"](https://safeguard.sh/resources/blog/not-demonstrated-is-not-not-vulnerable)
- [Ransomware en 24 heures : la fin du luxe de la réponse lente](https://ayinedjimi-consultants.fr/articles/ransomware-24h-fin-reponse-lente-securite)
- [The Global Incident Response Report 2026（Unit 42 PDF）](https://start.paloaltonetworks.com/rs/531-OCS-018/images/Unit42-Global-Incident-Response-Report.pdf?version=0)
- [The Shai-Hulud npm Supply Chain Attack Explained](https://safeguard.sh/resources/blog/the-shai-hulud-npm-supply-chain-attack-explained)