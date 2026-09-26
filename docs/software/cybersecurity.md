# 网络安全前沿

> 最后更新：2026-09-26 ｜ 领域：网络安全 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

2025–2026 年网络安全呈现「攻击面收敛于 AI 与供应链、防御重心转向身份与零信任」的双向挤压。一方面，勒索软件持续以制造业与供应链为目标，攻击者借助 AI 自动化恶意代码开发与赎金定价；另一方面，API 与 AI Agent 成为新的高危暴露面，行业开始发布面向 Agentic 应用的风险清单。防御侧，Passkey/无密码成为身份安全主线，后量子密码（PQC）迁移从标准发布进入落地执行阶段。

## 2025–2026 最新进展

### 1. 主要攻击面与事件趋势

**勒索软件**：制造业仍是首要目标。2026 年前七个月针对制造业的勒索事件同比增长 40%，中型制造商因处于大型企业生产线关键位置而成为重点猎物（[Ransomware Attacks on Manufacturers Rise as Supply Chain Threats Escalate](https://www.news4hackers.com/ransomware-attacks-on-manufacturers-rise-as-supply-chain-threats-escalate/)、[Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grows](https://radar.offseq.com/threat/ransomware-attacks-on-manufacturers-surge-as-supply-chain-risk-grows-225032fe881f2abc)）。2025 年 9 月捷豹路虎（Jaguar Land Rover）英国工厂一度停产成为标志性案例；物流环节同样脆弱，如 2025 年英国冷链物流商 Peter Green Chilled 遭攻击后无法处理新订单（[Black Kite's 2026 Manufacturing & Distribution Ransomware Report](https://www.unite.ai/black-kites-2026-manufacturing-distribution-ransomware-report-manufacturing-remains-ransomwares-top-target/)）。

**供应链与第三方风险**：MOVEit、GoAnywhere 事件确立了「攻陷广泛部署的工具、同时勒索整个客户群」的模板；2026 年第一季度出现针对企业备份与恢复平台的漏洞利用，被专门用于在加密前先破坏备份完整性，从而消除企业的首要恢复手段（[2026 Ransomware Attack Analysis: Trends & Defenses](https://nohack.net/latest-ransomware-attack-analysis-2026/)）。

**API 安全**：根据 Akamai《2026 互联网现状》报告，受访组织平均每天遭遇 258 次 API 攻击（2025 年数据），较 2024 年的 121 次增长 113%（[API Security Statistics 2026](https://axis-intelligence.com/api-security-statistics/)、[Apps, APIs, and DDoS 2026 — Akamai](https://www.akamai.com/site/en/documents/state-of-the-internet/2026/app-api-ddos-security-report-2026.pdf)）。2026 年已出现 AI 相关的高危案例，如 LiteLLM（CVE-2026-42208）预认证 RCE 在公开后 36 小时内即被大规模利用（[API Security Guide 2026](https://chs.us/guides/api-security/)）。

**云配置错误**：CSPM 持续监控云基础设施的错误配置与合规违规，因云环境遵循责任共担模型——厂商负责基础设施安全，客户须自行保障配置安全（[What is CSPM?](https://prowler.com/cloud-security-glossary/what-is-cspm)、[What is CSPM — Wiz](https://www.wiz.io/academy/cloud-security/what-is-cloud-security-posture-management-cspm)）。

### 2. 零信任架构

零信任架构（ZTA）以 NIST SP 800-207 为权威定义，强调保护资源本身而非网络分段，网络位置不再被视为安全姿态的核心要素；NIST SP 800-207A 进一步给出多云云原生应用的访问控制模型（[NIST Special Publication 800-207 Zero Trust Architecture](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)、[Search | CSRC](https://csrc.nist.gov/publications/sp800)）。美国联邦机构依据第 14028 号行政令须采用该框架；据 Gartner，2026 年将有 10% 的大型企业拥有成熟零信任计划，而 2023 年这一比例不足 1%（[Zero Trust Architecture: NIST 800-207 Implementation Guide](https://securitycomplianceguide.com/blog/zero-trust-nist-800-207-guide/)）。浏览器成为零信任新战场，CrowdStrike Falcon Secure Access 被 Frost & Sullivan 评为 2026 年零信任浏览器安全全球技术领导者（[Falcon Secure Access Sets the Standard for Zero Trust Browser Security](https://www.crowdstrike.com/en-us/blog/falcon-secure-access-sets-standard-for-zero-trust-security-browser/)）。

### 3. 身份安全与 Passkey/无密码

Passkey 采用加速：FIDO Alliance 估计全球已有约 50 亿个 passkey 在使用（2026 年 5 月数据），微软 OneDrive、Xbox、Copilot 等每天有数亿用户以 passkey 登录（[World Passkey Day: Advancing passwordless authentication](https://www.microsoft.com/en-us/security/blog/2026/05/07/world-passkey-day-advancing-passwordless-authentication/)）。RSA 称 2026 年 87% 的企业正在部署或试点 passkey，两年前仅 53%；无密码认证市场 2025 年规模达 241 亿美元，预计 2030 年增至 557 亿美元（[Why Passkeys Are the Future of Passwordless Authentication](https://www.rsa.com/resources/blog/passwordless/why-passkeys-are-the-future-of-passwordless-authentication/)）。Passkey 基于 FIDO 标准，采用源绑定公钥加密并要求本地用户交互，使其极难被钓鱼重放（[Microsoft Entra ID 中的 FIDO2 密钥身份验证方法](https://learn.microsoft.com/zh-cn/entra/identity/authentication/concept-authentication-passkeys-fido2)）。日本 Mercari 约 2300 万月活用户中已有近 1300 万账户使用 passkey，登录成功率显著高于短信 OTP（[Forging the Path to Enterprise Passkeys](https://fidoalliance.org/forging-the-path-to-enterprise-passkeys-a-collaborative-discussion-by-fido-board-members/)）。

### 4. 后量子密码迁移

NIST 于 2024-08-13 最终确定首批三个 PQC 标准：**FIPS 203（ML-KEM）** 用于密钥封装、**FIPS 204（ML-DSA）** 用于数字签名、**FIPS 205（SLH-DSA）** 用于无状态哈希签名；2025 年 3 月 NIST 又选定 HQC 作为备份密钥封装算法（[Post-Quantum Cryptography Explained: Why 2026 Is the Year It Matters](https://krazytech.com/technical-papers/post-quantum-cryptography)、[The 2026 executive order on post-quantum cryptography](https://qramm.org/learn/2026-executive-order-pqc.html)）。美国已通过行政令（M-26-15）要求联邦系统迁移至 NIST 批准的 PQC 标准，并要求迁移计划与 NIST IR 8547 对齐（[美国后量子密码迁移行政令解读](https://www.secrss.com/articles/91993)）。NIST NCCoE 的 PQC 迁移项目聚焦「密码可见性与风险管理」（构建并维护全面的密码清单）与互操作性/基准测试两条工作线（[FAQ about Post-Quantum Cryptography — NIST](https://pages.nist.gov/nccoe-migration-post-quantum-cryptography/FAQ/index.html)）。ML-KEM 正被纳入 ISO/IEC 18033-2，ML-DSA 与 SLH-DSA 拟标准化为 ISO/IEC 14888-5/6（[Migration to Post-Quantum Cryptography — NIST](https://csrc.nist.gov/csrc/media/presentations/2026/mpts2026-3b1/images-media/mpts2026-3b1-slides-nist-pqc-moody.pdf)）。

### 5. CNAPP / CSPM 与云安全

**CNAPP（Cloud-Native Application Protection Platform）** 将 CSPM、CWPP、CIEM、API 安全与云检测响应（CDR）整合为统一平台，能力涵盖 API 发现与清单、API 威胁防护（如实时阻断注入与未授权访问）、工作负载漂移检测与连通性映射（[什么是 CNAPP? — Palo Alto Networks](https://www.paloaltonetworks.cn/cyberpedia/what-is-a-cloud-native-application-protection-platform)、[What is a CNAPP? — Microsoft](https://www.microsoft.com/en-us/security/business/security-101/what-is-cnapp)）。以 Microsoft Defender for Cloud 为例，其三大组件为 CSPM（检查并改进云资源安全态势）、DevSecOps（跨多云与多流水线的代码级安全）与 CWPP（保护 VM、容器、存储、数据库与服务器等工作负载）（[What is Microsoft Defender for Cloud?](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)）。

### 6. EDR / XDR 与终端、浏览器安全

终端安全向 AI 驱动演进：Microsoft Defender for Endpoint 提供基于行为、云端与 ML 的下一代防护、EDR、漏洞管理，以及「自动攻击中断」——通过实时隔离失陷设备、禁用失陷账户来阻止横向移动，配合预测性防护（predictive shielding）主动保护高价值资产（[Windows 上的 Microsoft Defender for Endpoint](https://learn.microsoft.com/zh-cn/defender-endpoint/microsoft-defender-endpoint-windows)）。Microsoft Defender XDR 自 2026-09-23 起向符合条件的 M365 E5/E7 客户提供预览版 Integrated SOC（ISOC），将 XDR、SIEM、威胁情报、自动化与 AI 融为一体（[What's new in Microsoft Defender XDR](https://learn.microsoft.com/hi-in/defender-xdr/whats-new)）。Sophos Endpoint（Intercept X）等同样提供 EDR/XDR 能力（[Sophos Endpoint](https://assets.sophos.com/X24WTUEQ/at/8cssp49fv8gjk55vxgw6n/sophos-endpoint-br.pdf)）。

### 7. AI 带来的新型攻击与 AI 防御

**攻击侧**：威胁行为者已把 AI 用于自动化攻击链；微软观察到针对 Azure AI 模型部署的「越狱（jailbreak）」尝试，并使用 **Prompt Shields**（统一 API，检测用户提示攻击与间接攻击 XPIA）进行检测与阻断（[AI as tradecraft: How threat actors operationalize AI](https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/)）。针对深度伪造与 AI 生成钓鱼，仅靠安全意识培训已不足，需结合高风险请求的带外验证、抗钓鱼 MFA 与深度伪造检测（[AI Cybersecurity: Defending Against AI-Powered Attacks](https://blog.eduonix.com/2026/09/ai-cybersecurity-defending-against-ai-powered-attacks/)）。欧盟《AI 法案》（EU AI Act）于 2026 年 8 月进入全面适用，其第 50 条要求对面向公众传播的深度伪造与 AI 生成文本进行强制标注（[Défense contre les Attaques IA Générées](https://ayinedjimi-consultants.fr/static/pdf/ia-defense-attaques-ia-generees-2026.pdf)）。

**防御侧**：业界建议将提示、检索文档、工具响应等外部内容一律视为不可信输入，对直接/间接提示注入、投毒、对抗输入、模型窃取与不安全集成进行测试，并校验模型输入输出（[Cloud Security 2026: When AI is the Weapon and the Target](https://cloudsecurityalliance.org/blog/2026/09/17/cloud-security-2026-when-ai-is-the-weapon-and-the-target)）。OWASP 提供了 LLM Top 10 控制项，NIST AI RMF 用于持续跟踪风险（[2026 and the Rise of AI-Based Cyberattacks](https://innovirtuoso.com/ai/2026-and-the-rise-of-ai-based-cyberattacks-threat-models-real-risks-and-a-zero-trust-playbook-for-resilience/)）。2026 年新增的 **OWASP Top 10 for Agentic Applications** 列出 Agent 目标劫持（ASI01）、工具滥用（ASI02）、身份与权限滥用（ASI03）、Agentic 供应链漏洞（ASI04）、意外代码执行（ASI05）等风险（[Apps, APIs, and DDoS 2026 — Akamai](https://www.akamai.com/site/en/documents/state-of-the-internet/2026/app-api-ddos-security-report-2026.pdf)）。

### 8. 漏洞披露与权威清单

**OWASP Top 10:2025**（第 8 版）突出系统性根因弱点，完整列表为：A01 失效的访问控制、A02 安全配置错误、A03 软件供应链失效、A04 加密机制失效、A05 注入、A06 不安全设计、A07 认证失效、A08 软件或数据完整性失效、A09 安全日志记录和告警失效、A10 异常条件处理不当（[OWASP Top 10:2025 引言](https://owasp.org/Top10/2025/zh-Hant/0x00_2025-Introduction/)、[OWASP IMPACT REPORT 2025](https://owasp.org/assets/files/OWASP_Impact_Report_2025.pdf)）。其新版将「软件供应链失效」与「异常条件处理不当」列为新增重点，反映现代应用的构建与攻击方式（[OWASP IMPACT REPORT 2025](https://owasp.org/assets/files/OWASP_Impact_Report_2025.pdf)）。API 侧对应 **OWASP API Top 10**，涵盖失效认证（API2）、对象属性级授权失效（API3）、无限制资源消耗（API4）、功能级授权失效（API5）、敏感业务流滥用（API6）等（[OWASP API Top 10 (2026)](https://vulnerabbit.com/blog/02-02-2026_owasp_api_top10)）。**CISA KEV（Known Exploited Vulnerabilities）** 目录持续收录已被在野利用的漏洞并给出整改期限，例如 2026 年 9 月收录的 Cisco ISE 特权 API 误用（CVE-2026-76460）与 Google Pixel 授权不当（CVE-2026-58704）（[CISA Known Exploited Vulnerabilities (KEV)](https://cvefeed.io/cisakev/cisa-known-exploited-vulnerability-catalog)）；Linux 内核 IPv6 提权漏洞 CVE-2026-53362 亦被列入 KEV（[Under attack. Patch these first.](https://premierepc.com/security-briefs/known-exploited)）。

## 核心技术与关键概念

- **零信任（ZTA）**：以资源为中心、持续验证、最小权限。
- **CNAPP / CSPM / CWPP / CDR**：云安全的融合平台能力。
- **Passkey / FIDO2**：源绑定公钥、抗钓鱼的免密码认证。
- **PQC（ML-KEM/ML-DSA/SLH-DSA）**：抗量子计算的密码算法族。
- **Prompt Injection（直接/间接）**：针对 LLM 与 Agent 的输入操纵攻击。
- **CISA KEV**：在野利用漏洞的权威清单与整改基线。

## 代表性框架/项目与标准

| 类别 | 项目/标准 | 官方链接 |
|---|---|---|
| 应用安全清单 | OWASP Top 10:2025 / API Top 10 / Agentic Top 10 | https://owasp.org/Top10/ |
| 零信任 | NIST SP 800-207 / 800-207A | https://csrc.nist.gov/pubs/sp/800/207/final |
| 后量子密码 | NIST FIPS 203/204/205 | https://csrc.nist.gov/projects/post-quantum-cryptography |
| 漏洞目录 | CISA KEV | https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| 身份 | FIDO2 / WebAuthn / Passkey | https://fidoalliance.org/ |
| 云安全 | CNAPP（CSPM+CWPP+CIEM+CDR） | https://www.paloaltonetworks.com/cyberpedia/what-is-a-cloud-native-application-protection-platform |
| 终端 | EDR / XDR | https://learn.microsoft.com/defender-endpoint/ |

## 版本与生态数据

| 指标 | 数据 | 来源 |
|---|---|---|
| 制造业勒索事件 | 2026 年前 7 个月同比 +40% | News4Hackers / OffSeq |
| 日均 API 攻击 | 258 次/组织（2025），较 2024 的 121 次 +113% | Akamai 2026 |
| Passkey 全球使用量 | 约 50 亿（FIDO Alliance 估计） | Microsoft Security Blog |
| 企业 passkey 部署/试点 | 87%（2026）对比 53%（两年前） | RSA |
| 无密码市场 | 2025 年 241 亿美元 → 2030 年 557 亿美元 | RSA |
| 成熟零信任企业占比 | 2026 年预计 10%（2023 年 <1%） | Gartner（转引） |
| PQC 标准 | FIPS 203/204/205（2024-08-13 定稿） | NIST |
| OWASP Top 10:2025 | 第 8 版，新增 A03、A10 | owasp.org |

## 趋势与争议

1. **AI 既是武器也是目标**：攻击者用 AI 自动化攻击链，企业又需保护 AI 系统自身；OWASP Agentic Top 10 的出现标志着 Agent 安全进入标准化视野。
2. **零信任从理念到基线**：NIST SP 800-207 提供厂商无关定义，但成熟落地比例仍低，身份与浏览器成为新前线。
3. **PQC 迁移的紧迫性与「先存后解」风险**：标准已就绪，但企业密码清单缺失与互操作性挑战使迁移周期拉长，攻击者可能先截获密文等待量子算力成熟后再解密。
4. **供应链信任的边界**：即使拥有合法签名与证明，攻击者仍可窃取构建环境凭证生成「有效但恶意」的制品，说明完整性证明不能替代运行时防护。
5. **合规压力的上升**：EU AI Act 第 50 条的深度伪造标注义务与企业级 AI 治理要求，正把技术防护与法律合规绑定。

## 参考来源

1. [Ransomware Attacks on Manufacturers Rise as Supply Chain Threats Escalate](https://www.news4hackers.com/ransomware-attacks-on-manufacturers-rise-as-supply-chain-threats-escalate/)
2. [Ransomware Attacks on Manufacturers Surge as Supply Chain Risk Grows](https://radar.offseq.com/threat/ransomware-attacks-on-manufacturers-surge-as-supply-chain-risk-grows-225032fe881f2abc)
3. [Black Kite's 2026 Manufacturing & Distribution Ransomware Report](https://www.unite.ai/black-kites-2026-manufacturing-distribution-ransomware-report-manufacturing-remains-ransomwares-top-target/)
4. [2026 Ransomware Attack Analysis: Trends & Defenses](https://nohack.net/latest-ransomware-attack-analysis-2026/)
5. [API Security Statistics 2026: Exploited Auth Flaws Doubled, Attacks Per Org Up 113%](https://axis-intelligence.com/api-security-statistics/)
6. [Apps, APIs, and DDoS 2026 — Akamai](https://www.akamai.com/site/en/documents/state-of-the-internet/2026/app-api-ddos-security-report-2026.pdf)
7. [API Security Guide 2026](https://chs.us/guides/api-security/)
8. [What is CSPM? Cloud Security Posture Management Explained](https://prowler.com/cloud-security-glossary/what-is-cspm)
9. [What is CSPM (Cloud Security Posture Management)? — Wiz](https://www.wiz.io/academy/cloud-security/what-is-cloud-security-posture-management-cspm)
10. [NIST Special Publication 800-207 Zero Trust Architecture](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)
11. [Search | CSRC — SP 800-207A](https://csrc.nist.gov/publications/sp800)
12. [Zero Trust Architecture: NIST 800-207 Implementation Guide](https://securitycomplianceguide.com/blog/zero-trust-nist-800-207-guide/)
13. [Falcon Secure Access Sets the Standard for Zero Trust Browser Security](https://www.crowdstrike.com/en-us/blog/falcon-secure-access-sets-standard-for-zero-trust-security-browser/)
14. [World Passkey Day: Advancing passwordless authentication](https://www.microsoft.com/en-us/security/blog/2026/05/07/world-passkey-day-advancing-passwordless-authentication/)
15. [Why Passkeys Are the Future of Passwordless Authentication](https://www.rsa.com/resources/blog/passwordless/why-passkeys-are-the-future-of-passwordless-authentication/)
16. [Microsoft Entra ID 中的 FIDO2 密钥身份验证方法](https://learn.microsoft.com/zh-cn/entra/identity/authentication/concept-authentication-passkeys-fido2)
17. [Forging the Path to Enterprise Passkeys: A Collaborative Discussion by FIDO Board Members](https://fidoalliance.org/forging-the-path-to-enterprise-passkeys-a-collaborative-discussion-by-fido-board-members/)
18. [Post-Quantum Cryptography Explained: Why 2026 Is the Year It Matters](https://krazytech.com/technical-papers/post-quantum-cryptography)
19. [The 2026 executive order on post-quantum cryptography](https://qramm.org/learn/2026-executive-order-pqc.html)
20. [美国后量子密码迁移行政令解读](https://www.secrss.com/articles/91993)
21. [FAQ about Post-Quantum Cryptography — NIST NCCoE](https://pages.nist.gov/nccoe-migration-post-quantum-cryptography/FAQ/index.html)
22. [Migration to Post-Quantum Cryptography — NIST](https://csrc.nist.gov/csrc/media/presentations/2026/mpts2026-3b1/images-media/mpts2026-3b1-slides-nist-pqc-moody.pdf)
23. [什么是 CNAPP? — Palo Alto Networks](https://www.paloaltonetworks.cn/cyberpedia/what-is-a-cloud-native-application-protection-platform)
24. [What is a CNAPP? — Microsoft](https://www.microsoft.com/en-us/security/business/security-101/what-is-cnapp)
25. [What is Microsoft Defender for Cloud?](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
26. [Windows 上的 Microsoft Defender for Endpoint](https://learn.microsoft.com/zh-cn/defender-endpoint/microsoft-defender-endpoint-windows)
27. [What's new in Microsoft Defender XDR](https://learn.microsoft.com/hi-in/defender-xdr/whats-new)
28. [Sophos Endpoint](https://assets.sophos.com/X24WTUEQ/at/8cssp49fv8gjk55vxgw6n/sophos-endpoint-br.pdf)
29. [AI as tradecraft: How threat actors operationalize AI](https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/)
30. [AI Cybersecurity: Defending Against AI-Powered Attacks](https://blog.eduonix.com/2026/09/ai-cybersecurity-defending-against-ai-powered-attacks/)
31. [Défense contre les Attaques IA Générées: Stratégies](https://ayinedjimi-consultants.fr/static/pdf/ia-defense-attaques-ia-generees-2026.pdf)
32. [Cloud Security 2026: When AI is the Weapon and the Target](https://cloudsecurityalliance.org/blog/2026/09/17/cloud-security-2026-when-ai-is-the-weapon-and-the-target)
33. [2026 and the Rise of AI-Based Cyberattacks](https://innovirtuoso.com/ai/2026-and-the-rise-of-ai-based-cyberattacks-threat-models-real-risks-and-a-zero-trust-playbook-for-resilience/)
34. [OWASP Top 10:2025 引言](https://owasp.org/Top10/2025/zh-Hant/0x00_2025-Introduction/)
35. [OWASP IMPACT REPORT 2025](https://owasp.org/assets/files/OWASP_Impact_Report_2025.pdf)
36. [OWASP API Top 10 (2026)](https://vulnerabbit.com/blog/02-02-2026_owasp_api_top10)
37. [CISA Known Exploited Vulnerabilities (KEV)](https://cvefeed.io/cisakev/cisa-known-exploited-vulnerability-catalog)
38. [Under attack. Patch these first.](https://premierepc.com/security-briefs/known-exploited)