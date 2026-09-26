# 应用安全

> 最后更新：2026-09-26 ｜ 领域：安全 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

应用安全（Application Security，AppSec）关注在软件设计、开发、测试与运行各阶段识别与消除应用层弱点。2025–2026 年，该领域出现两个显著变化：一是 OWASP Top 10 发布第 8 版（2025 版），首次将「软件供应链失败」单列为独立类别，并新增「异常条件处理不当」类别；二是 AI 生成代码大规模进入生产环境，使传统 SAST/DAST 的覆盖面与误报控制面临结构性挑战。

## 最新进展（2025–2026）

### OWASP Top 10:2025 发布

OWASP 官方页面确认 2025 版为第 8 版，其十大类别为（[The Ten Most Critical Web Application Security Risks](https://owasp.org/Top10/2025/0x00_2025-Introduction/)）：

- A01:2025 Broken Access Control（失效的访问控制）
- A02:2025 Security Misconfiguration（安全配置错误）
- A03:2025 Software Supply Chain Failures（软件供应链失败）
- A04:2025 Cryptographic Failures（加密失败）
- A05:2025 Injection（注入）
- A06:2025 Insecure Design（不安全设计）
- A07:2025 Authentication Failures（身份认证失败）
- A08:2025 Software or Data Integrity Failures（软件或数据完整性失败）
- A09:2025 Security Logging and Alerting Failures（安全日志与告警失败）
- A10:2025 Mishandling of Exceptional Conditions（异常条件处理不当）

其中 A01 失效的访问控制连续第四次（连续四版）位居第一，官方数据表明平均 3.73% 的受测应用存在该类别 40 个 CWE 中的至少一个弱点，2021 版的 SSRF（A10:2021）已被并入该类别（[OWASP Top 10:2025 引言（繁中）](https://owasp.org/Top10/2025/zh-Hant/0x00_2025-Introduction/)；[OWASP Top 10 2025 — Revised Version Released With Two New Categories](https://cybersecuritynews.com/owasp-top-10-2025/amp/)）。A02 安全配置错误由 2021 版的第 5 位升至第 2 位，影响约 3.00% 的应用。第三方解读指出，2025 版分析覆盖 589 个 CWE、来自 13 个组织、2.8 百万个应用的数据（[OWASP Top 10 - 2025](https://fixthevuln.com/owasp-top10.html)）。

### OWASP API Security Top 10

API 安全方面，2023 版仍为当前最新版本，OWASP 尚未发布更新（[OWASP API Security Top 10 Complete Guide [2026 Update]](https://cloudinsight.cc/en/blog/owasp-api-top-10)）。其十大类别为（[Table of Contents — OWASP API Security](https://owasp.org/API-Security/editions/2023/en/0x00-toc/)）：

1. API1:2023 Broken Object Level Authorization（BOLA）
2. API2:2023 Broken Authentication
3. API3:2023 Broken Object Property Level Authorization（BOPLA）
4. API4:2023 Unrestricted Resource Consumption
5. API5:2023 Broken Function Level Authorization
6. API6:2023 Unrestricted Access to Sensitive Business Flows
7. API7:2023 Server Side Request Forgery
8. API8:2023 Security Misconfiguration
9. API9:2023 Improper Inventory Management
10. API10:2023 Unsafe Consumption of APIs

OWASP 对 API1:2023 的解释是，攻击者可通过操纵请求中的对象 ID（顺序整数、UUID 或通用字符串）利用对象级授权缺陷，这类问题在 API 应用中极为常见，因为服务端通常不完整跟踪客户端状态，而依赖客户端传入的对象 ID 决定可访问的对象（[API1:2023 Broken Object Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)）。BOLA 已连续两个版本位居首位（[OWASP API Security Top 10 Explained With Code](https://cyberphinix.de/en/blog/owasp-api-security-top-10/)）。

### API 攻击规模与 AI 相关高危案例

2026 年的 API 威胁数据显示攻击强度显著上升：Akamai《2026 互联网现状》报告称，受访组织平均每天遭遇 258 次 API 攻击（2025 年数据），较 2024 年的 121 次增长 113%（[API Security Statistics 2026](https://axis-intelligence.com/api-security-statistics/)、[Apps, APIs, and DDoS 2026 — Akamai](https://www.akamai.com/site/en/documents/state-of-the-internet/2026/app-api-ddos-security-report-2026.pdf)）。2026 年已出现与 AI 组件相关的高危 API 案例：LiteLLM 的预认证远程代码执行（CVE-2026-42208）在公开披露后 36 小时内即被大规模利用（[API Security Guide 2026](https://chs.us/guides/api-security/)）。

### AI 生成代码带来的新挑战

多方报告给出 AI 生成代码存在安全缺陷的比例：Veracode 的 GenAI Code Security Report 称 45% 的 AI 生成代码含安全漏洞（[The #1 AppSec Blind Spot: Why AI Code Defeats Traditional SAST](https://www.softwareseni.com/the-1-appsec-blind-spot-why-ai-code-defeats-traditional-sast/)）；另有 2026 年工具评测引用「40% 的 AI 生成代码含安全漏洞」并强调 AppSec 平台若不覆盖 AI 资产、MCP 服务器与 AI 编码助手将留下关键缺口（[The 7 Best Application Security Tools for 2026](https://xygeni.io/blog/top-application-security-tools/)）。DX Research 在 2026 年 Q1 对 500+ 组织的分析称，27% 的生产代码已由 AI 生成。实践观察则指出，截至 2026 年中期，尚无自动化工具能可靠捕获授权逻辑缺陷、缺失限流或仅客户端的安全控制（[Scanning Vibe-Coded Apps: Why Traditional SAST/DAST Falls Short](https://simonroses.com/2026/05/scanning-vibe-coded-apps-why-traditional-sast-dast-falls-short-part-6/)）。

## 核心技术与关键概念

- **SAST（静态应用安全测试）**：在源码/字节码层面分析，可尽早发现编码缺陷，但对授权逻辑、运行时配置类问题覆盖有限。
- **DAST（动态应用安全测试）**：对运行中应用发起测试，能发现配置与运行时问题，但定位与修复成本较高。
- **IAST / RASP**：插桩式测试与运行时自保护，结合运行时上下文降低误报。
- **SCA（软件成分分析）**：识别第三方组件与依赖漏洞，与 OWASP Top 10:2025 新增的 A03 软件供应链失败直接相关。
- **ASPM（应用安全态势管理）**：跨工具聚合与去重、按可利用性排序，并集成到 CI/CD（[Application Security Market Size, Share, Driving Factors & Industry Outlook](https://www.marketsandmarkets.com/Market-Reports/application-security-market-110170194.html)）。
- **SDL（安全开发生命周期）**：将威胁建模、安全编码规范、代码评审、安全测试与发布门禁嵌入开发流程。

Gartner 与市场研究机构将安全测试工具视为应用安全市场中最大细分，覆盖 SAST、DAST、IAST、RASP、SCA 与 ASPM，并强调现代平台以 AI 按可利用性排序漏洞、集成 CI/CD 实现持续测试（[Application Security Market Size, Share, Driving Factors & Industry Outlook](https://www.marketsandmarkets.com/Market-Reports/application-security-market-110170194.html)）。

## 代表性项目 / 产品 / 组织

- **OWASP**：发布 Top 10（Web）、API Security Top 10 等事实标准（[OWASP Top 10:2025](https://owasp.org/Top10/2025/0x00_2025-Introduction/)）。
- **安全测试平台**：市场评测将 SAST/DAST/SCA/ASPM 工具纳入统一比较框架（[The 7 Best Application Security Tools for 2026](https://xygeni.io/blog/top-application-security-tools/)）。
- **Veracode / DX Research**：提供 AI 生成代码安全性的量化研究。

## 关键数据与评测结果

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| OWASP Top 10:2025 受测应用存在 A01 弱点比例 | 平均 3.73% | [OWASP](https://owasp.org/Top10/2025/0x00_2025-Introduction/) |
| A02 安全配置错误影响比例 | 约 3.00% | [cybersecuritynews](https://cybersecuritynews.com/owasp-top-10-2025/amp/) |
| 2025 版分析数据规模 | 589 个 CWE、13 个组织、280 万应用 | [fixthevuln](https://fixthevuln.com/owasp-top10.html) |
| AI 生成代码含漏洞比例 | 45%（Veracode） | [softwareseni](https://www.softwareseni.com/the-1-appsec-blind-spot-why-ai-code-defeats-traditional-sast/) |
| 生产代码中 AI 生成占比 | 27%（DX Research，2026 Q1） | [softwareseni](https://www.softwareseni.com/the-1-appsec-blind-spot-why-ai-code-defeats-traditional-sast/) |

## 趋势与争议

- **供应链失败独立成类**：A03 的设立反映开源依赖与构建管线风险已上升为应用层核心议题，与软件供应链安全（SLSA/SBOM）领域高度耦合。
- **传统 SAST/DAST 的有效性争议**：有观点认为模式匹配式扫描难以应对 AI 生成代码，AI 原生工具（神经符号分析、LLM 误报过滤）正在尝试补位，但对授权逻辑等复杂缺陷仍需人工介入，结论尚不统一。
- **API 安全重心**：BOLA/BOPLA 长期居首，说明对象级与属性级授权仍是 API 最大风险面，与 API 网关、身份体系的联动成为常见缓解方向。
- **市场整合**：ASPM 与 CNAPP、AI 资产治理的边界正在模糊，不同厂商对「应用安全平台」的范围定义口径不一。

## 参考来源

1. [The Ten Most Critical Web Application Security Risks — OWASP Top 10:2025](https://owasp.org/Top10/2025/0x00_2025-Introduction/)
2. [引言 — OWASP Top 10:2025（繁中）](https://owasp.org/Top10/2025/zh-Hant/0x00_2025-Introduction/)
3. [OWASP Top 10 2025 — Revised Version Released With Two New Categories](https://cybersecuritynews.com/owasp-top-10-2025/amp/)
4. [OWASP Top 10 - 2025 — FixTheVuln](https://fixthevuln.com/owasp-top10.html)
5. [OWASP Top 10 2025: what's changed and the 2026 data — Patrowl](https://patrowl.io/en/blog/owasp-top-10-2025-what-s-changed-and-the-2026-data)
6. [Table of Contents — OWASP API Security Top 10 2023](https://owasp.org/API-Security/editions/2023/en/0x00-toc/)
7. [API1:2023 Broken Object Level Authorization — OWASP](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)
8. [OWASP API Security Top 10 (2023) Explained With Code — Cyberphinix](https://cyberphinix.de/en/blog/owasp-api-security-top-10/)
9. [OWASP API Security Top 10 Complete Guide [2026 Update] — CloudInsight](https://cloudinsight.cc/en/blog/owasp-api-top-10)
10. [The 7 Best Application Security Tools for 2026, Ranked and Compared — Xygeni](https://xygeni.io/blog/top-application-security-tools/)
11. [The #1 AppSec Blind Spot: Why AI Code Defeats Traditional SAST — SoftwareSeni](https://www.softwareseni.com/the-1-appsec-blind-spot-why-ai-code-defeats-traditional-sast/)
12. [Scanning Vibe-Coded Apps: Why Traditional SAST/DAST Falls Short — Simon Roses](https://simonroses.com/2026/05/scanning-vibe-coded-apps-why-traditional-sast-dast-falls-short-part-6/)
13. [Application Security Market Size, Share, Driving Factors & Industry Outlook — MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/application-security-market-110170194.html)