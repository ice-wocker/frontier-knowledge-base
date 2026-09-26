# 网络安全与零信任

> 最后更新：2026-09-26 ｜ 领域：安全 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

网络安全与零信任（Network Security and Zero Trust）关注如何在网络层控制东西向与南北向流量、抵御大流量攻击，并以身份与上下文替代静态边界。2025–2026 年的关键变化是：零信任从概念框架走向可落地的参考实现，SASE/SSE 加速走向单供应商收敛，微隔离成为限制横向移动的主流控制，而 DDoS 攻击规模持续刷新纪录并呈现「超大流量 + 极短持续时间」特征。

## 最新进展（2025–2026）

### 零信任的参考实现

NIST SP 800-207《Zero Trust Architecture》将零信任定义为「从静态的、基于网络的边界转向以用户、资产和资源为中心」的范式，零信任假设不因资产或账户的物理/网络位置（如内网 vs 互联网）或资产所有权而授予隐式信任（[NIST Special Publication 800-207 Zero Trust Architecture](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)）。NIST 国家网络安全卓越中心（NCCoE）已与协作方在实验室环境中构建 19 个可互操作、基于开放标准的零信任实现（「builds」），覆盖增强身份治理（EIG）、软件定义边界（SDP）与微隔离等方法（[NIST Zero Trust Architecture — Introduction](https://pages.nist.gov/zero-trust-architecture/_sources/VolumeA/Introduction.rst)）。

其中，ZSO（Zero Trust Security Orchestrator）负责识别用户、设备、应用、位置、网络类型与威胁存在性，其自适应访问控制检查是零信任模型的基础，并提供基于安全移动端 MFA 的无摩擦单点登录体验（[NIST Zero Trust Architecture — Project Overview](https://pages.nist.gov/zero-trust-architecture/VolumeA/ProjectOverview.html)）。美国政府身份管理指南也将身份生命周期管理（ILM）与 ZTA、IGA 最佳实践对齐，强调「身份即新安全边界」，从静态的基于角色访问转向动态、上下文感知的授权（[Identity Lifecycle Management Playbook — IDManagement.gov](https://www.idmanagement.gov/playbooks/ilm/)）。NIST SP 800-207A 进一步给出多云、云原生应用的零信任访问控制模型（[Search | CSRC — SP 800-207A](https://csrc.nist.gov/publications/sp800)）。美国联邦机构依据第 14028 号行政令（Executive Order 14028）须采用该零信任框架（[Zero Trust Architecture: NIST 800-207 Implementation Guide](https://securitycomplianceguide.com/blog/zero-trust-nist-800-207-guide/)）。落地进度方面，据 Gartner，2026 年将有 10% 的大型企业拥有成熟零信任计划，而 2023 年这一比例不足 1%（[Zero Trust Architecture: NIST 800-207 Implementation Guide](https://securitycomplianceguide.com/blog/zero-trust-nist-800-207-guide/)）。浏览器成为零信任的新战场，CrowdStrike Falcon Secure Access 被 Frost & Sullivan 评为 2026 年零信任浏览器安全全球技术领导者（[Falcon Secure Access Sets the Standard for Zero Trust Browser Security](https://www.crowdstrike.com/en-us/blog/falcon-secure-access-sets-standard-for-zero-trust-security-browser/)）。

### SASE / SSE 的市场收敛

SASE（Secure Access Service Edge）将广域网与安全能力融合。市场研究显示，全球 SASE 市场 2025 年估值 107 亿美元，2026 年约 126 亿美元，预计 2036 年达约 766 亿美元，2026–2036 年 CAGR 为 19.7%（[Secure Access Service Edge (SASE) Market — Meticulous Research](https://www.meticulousresearch.com/product/secure-access-service-edge-market-6488/toc)）。SSE（Security Service Edge）作为 SASE 的安全侧，2025 年市场规模约 118.5 亿美元，2026 年约 146.5 亿美元，预计 2035 年达 685 亿美元，2026–2035 年 CAGR 为 22.8%（[Security Service Edge Market (2025-2035) — Emergen Research](https://www.emergenresearch.com/industry-report/security-service-edge-market)）。

趋势上，单供应商 SASE 正成为预期终态：Gartner 预测到 2028 年单供应商采用率达 50%，起初做 SSE 的厂商（如 Zscaler、Netskope）通过收购或合作补齐 SD-WAN，而起步于 SD-WAN 的厂商反向补齐安全（[SSE vs SASE: when each architecture fits your organisation — Jimber](https://jimber.io/blog/sse-vs-sase-when-each-architecture-fits-your-organisation/)）。另有口径称 Gartner 预计到 2026 年 80% 的企业将采用 SASE/ZTNA 策略（从当时的 20% 提升）（[Zscaler Company Overview — Luminix](https://www.useluminix.com/reports/company-overviews/zscaler-company-overview-zero-trust-security-platform-financials-and-market-position-2026/source/3)）。2026 年的 Gartner Magic Quadrant 中，有厂商连续第四年在 SSE 与 SASE 两个报告中同时获评领导者，反映传统防火墙厂商向 AI 原生安全平台转型（[Palo Alto Networks Secures Fourth Consecutive Double Leadership in 2026 Gartner MQ](https://skyportsystems.net/palo-alto-networks-secures-unprecedented-fourth-consecutive-double-leadership-in-2026-gartner-magic-quadrant-reports-for-sase-and-sse-platforms/)）。

### 微隔离与横向移动

微隔离（东-西向分段）通过限制已在内网的工作负载之间的流量，使单点被攻陷无法横向扩展。有资料指出超过 70% 的成功泄露涉及横向移动，而 CrowdStrike《2026 Global Threat Report》测得 eCrime 攻击者平均 breakout time 为 29 分钟（[What Is Microsegmentation? — Elisity](https://www.elisity.com/microsegmentation/what-is-microsegmentation)）。现代微隔离以「策略」而非重改网络拓扑来实现：定义哪些工作负载身份可以与哪些服务通信，由执行层负责落地（[Zero Trust Tools for Cloud Workloads: A How-To Guide — NetFoundry](https://netfoundry.io/for-agents/zero-trust-tools-for-cloud-workloads-a-how-to-guide/)）。Forrester 已发布专门的微隔离解决方案 Wave 评估，厂商在无代理分段、与交换机/防火墙原生集成方面持续投入（[Microsegmentation's Moment Is Now — Cisco Blogs](https://blogs.cisco.com/security/cisco-named-a-leader-in-the-forrester-wave-microsegmentation-solutions)）。

### DDoS 攻击规模

Cloudflare 报告称，其缓解过的最大规模 DDoS 攻击峰值达 22.2 Tbps 与 106 亿包/秒（Bpps），超过此前任何 DDoS 事件的两倍以上，该攻击为多向量组合且仅持续约 40 秒即造成显著影响（[The record-breaking DDoS attack mitigated by Cloudflare](https://assets-global.website-files.com/68062a5075f93e9a687abc30/68d53ecfce708f389f1fe440_81839581158.pdf)）。在 2025 年第四季度，超大规模攻击环比增加 40%，全年攻击规模增长超过 700%，其中一次达 31.4 Tbps、仅持续 35 秒（[DDoS threat report for 2025 Q4 — Cloudflare Radar](https://radar.cloudflare.com/reports/ddos-2025-q4)）。到 2026 年第二季度，Cloudflare 缓解了 805 次超过 1 Tbps 的网络层攻击，环比增长逾六倍；但同期 96.62% 的网络层攻击仍低于常规阈值，呈现「超大流量峰值 + 大量小规模攻击」并存的特征（[Cloudflare DDoS Threat Report H1 2026](https://blog.cloudflare.com/ddos-threat-report-2026-h1/)）。

## 核心技术与关键概念

- **零信任原则**：不授予隐式信任、持续验证、最小权限、假设已失陷。
- **ZTNA（零信任网络访问）**：以身份与上下文授权的应用级访问，替代传统 VPN 的全网可达。
- **SDP（软件定义边界）**：基于「黑云」模型的隐藏式访问通道。
- **微隔离**：基于工作负载身份的细粒度东西向控制，限制横向移动。
- **SASE / SSE**：将 SWG、CASB、ZTNA、FWaaS 与 SD-WAN 融合的云交付安全与网络架构。
- **DDoS 防护**：本地清洗、云清洗、anycast 分散与速率限制；应对多向量与超短时突发。
- **防火墙演进**：从状态检测下一代防火墙（NGFW）到云原生/虚拟化防火墙与 AI 原生平台。

## 代表性组织 / 厂商 / 平台

- **NIST NCCoE**：19 个可互操作零信任实现与 ZTA 指南（[NIST ZTA](https://pages.nist.gov/zero-trust-architecture/VolumeA/ProjectOverview.html)）。
- **Cloudflare**：DDoS 态势数据与缓解能力（[Cloudflare Radar](https://radar.cloudflare.com/reports/ddos-2025-q4)）。
- **SASE/SSE 厂商**：Zscaler、Netskope、Palo Alto Networks 等在 Gartner MQ 与 Forrester Wave 中被评估（[Palo Alto Networks 2026 Gartner MQ](https://skyportsystems.net/palo-alto-networks-secures-unprecedented-fourth-consecutive-double-leadership-in-2026-gartner-magic-quadrant-reports-for-sase-and-sse-platforms/)）。
- **Cisco / Forrester**：微隔离解决方案评估与无代理分段能力（[Cisco Blogs](https://blogs.cisco.com/security/cisco-named-a-leader-in-the-forrester-wave-microsegmentation-solutions)）。

## 关键数据与评测结果

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 最大已缓解 DDoS 攻击 | 22.2 Tbps / 106 亿 pps | [Cloudflare](https://assets-global.website-files.com/68062a5075f93e9a687abc30/68d53ecfce708f389f1fe440_81839581158.pdf) |
| 2025 Q4 最大攻击 | 31.4 Tbps（持续约 35 秒） | [Cloudflare Radar](https://radar.cloudflare.com/reports/ddos-2025-q4) |
| 2026 Q2 超过 1 Tbps 的网络层攻击次数 | 805 次（环比 +6 倍以上） | [Cloudflare H1 2026](https://blog.cloudflare.com/ddos-threat-report-2026-h1/) |
| 涉及横向移动的成功泄露比例 | 超过 70% | [Elisity](https://www.elisity.com/microsegmentation/what-is-microsegmentation) |
| SASE 市场 2025 → 2036 | 107 亿 → 约 766 亿美元 | [Meticulous Research](https://www.meticulousresearch.com/product/secure-access-service-edge-market-6488/toc) |
| 单供应商 SASE 采用率预测（2028） | 50%（Gartner） | [Jimber](https://jimber.io/blog/sse-vs-sase-when-each-architecture-fits-your-organisation/) |

## 趋势与争议

- **零信任落地程度之争**：NIST 已给出可落地的参考架构，但企业在身份治理、微隔离与持续验证上的成熟度差异较大，「零信任已实现」与「仍停留在概念」两种说法并存。
- **单供应商 vs 双供应商 SASE**：收敛可降低复杂度，但也带来锁定与功能短板风险；不同机构对收敛速度的预测差异较大。
- **DDoS 防御成本**：超大规模短时攻击对清洗带宽与弹性架构提出更高要求，攻击规模数字的统计口径（是否含放大流量、是否含应用层）在不同报告间不完全可比。
- **微隔离的实现路径**：基于代理 vs 无代理、网络层 vs 身份层存在取舍，无代理对各平台的一致性覆盖仍有争议。
- **与身份体系融合**：零信任网络访问与 IAM、设备信任、CIEM 的边界持续融合，产品定义尚未统一。

## 参考来源

1. [NIST Special Publication 800-207 Zero Trust Architecture — NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf)
2. [NIST Zero Trust Architecture — Executive Summary](https://pages.nist.gov/zero-trust-architecture/VolumeA/ExecutiveSummary.html)
3. [NIST Zero Trust Architecture — Introduction](https://pages.nist.gov/zero-trust-architecture/_sources/VolumeA/Introduction.rst)
4. [NIST Zero Trust Architecture — Project Overview](https://pages.nist.gov/zero-trust-architecture/VolumeA/ProjectOverview.html)
5. [Identity Lifecycle Management Playbook — IDManagement.gov](https://www.idmanagement.gov/playbooks/ilm/)
6. [Secure Access Service Edge (SASE) Market — Meticulous Research](https://www.meticulousresearch.com/product/secure-access-service-edge-market-6488/toc)
7. [Security Service Edge Market (2025-2035) — Emergen Research](https://www.emergenresearch.com/industry-report/security-service-edge-market)
8. [SSE vs SASE: when each architecture fits your organisation — Jimber](https://jimber.io/blog/sse-vs-sase-when-each-architecture-fits-your-organisation/)
9. [Zscaler Company Overview — Luminix](https://www.useluminix.com/reports/company-overviews/zscaler-company-overview-zero-trust-security-platform-financials-and-market-position-2026/source/3)
10. [Palo Alto Networks Secures Fourth Consecutive Double Leadership in 2026 Gartner MQ](https://skyportsystems.net/palo-alto-networks-secures-unprecedented-fourth-consecutive-double-leadership-in-2026-gartner-magic-quadrant-reports-for-sase-and-sse-platforms/)
11. [What Is Microsegmentation? — Elisity](https://www.elisity.com/microsegmentation/what-is-microsegmentation)
12. [Zero Trust Tools for Cloud Workloads: A How-To Guide — NetFoundry](https://netfoundry.io/for-agents/zero-trust-tools-for-cloud-workloads-a-how-to-guide/)
13. [Microsegmentation's Moment Is Now — Cisco Blogs](https://blogs.cisco.com/security/cisco-named-a-leader-in-the-forrester-wave-microsegmentation-solutions)
14. [The record-breaking DDoS attack mitigated by Cloudflare](https://assets-global.website-files.com/68062a5075f93e9a687abc30/68d53ecfce708f389f1fe440_81839581158.pdf)
15. [DDoS threat report for 2025 Q4 — Cloudflare Radar](https://radar.cloudflare.com/reports/ddos-2025-q4)
16. [Cloudflare DDoS Threat Report H1 2026](https://blog.cloudflare.com/ddos-threat-report-2026-h1/)
17. [Zero Trust Architecture: NIST 800-207 Implementation Guide](https://securitycomplianceguide.com/blog/zero-trust-nist-800-207-guide/)