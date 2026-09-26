# 身份与访问管理（IAM）

> 最后更新：2026-09-26 ｜ 领域：安全 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

身份与访问管理（Identity and Access Management，IAM）负责对「谁在什么条件下可以访问什么资源」进行认证、授权与治理。2025–2026 年，IAM 的主线有三条：OAuth 2.1 与 WebAuthn/Passkey 等现代认证规范持续落地；密码正在被 passkey 大规模替代；以及非人类身份（Non-Human Identity，NHI）与 AI 代理爆炸式增长带来的治理真空。

## 最新进展（2025–2026）

### OAuth 2.1 与元数据规范

OAuth 2.1 由 IETF OAuth 工作组以 Internet-Draft 形式推进，2025 年 5 月 28 日发布的 draft-ietf-oauth-v2-1-13 定位为 Standards Track，计划将 OAuth 2.0 与其多个安全扩展合并为一份规范（[The OAuth 2.1 Authorization Framework — draft-ietf-oauth-v2-1-13](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-13.html)）。其核心变化是把 PKCE、精确重定向 URI 匹配、禁止隐式流与资源所有者密码凭证流等最佳实践固化进主规范，但截至该版本仍为草案状态。

配套的元数据规范方面，RFC 9728（OAuth 2.0 Protected Resource Metadata）定义了受保护资源发布 `authorization_servers` 等参数的方式，用于指示可与之配合的授权服务器 issuer 标识（[OAuth 2.0 Protected Resource Metadata — RFC 9728](https://datatracker.ietf.org/doc/rfc9728/)）；RFC 8414 则建立了「OAuth Authorization Server Metadata」注册表。此外，身份链（identity chaining）等草案还在探索跨域 token exchange 的扩展参数（[draft-ietf-oauth-identity-chaining-06](https://www.ietf.org/archive/id/draft-ietf-oauth-identity-chaining-06.txt)）。

### Passkey 规模化

FIDO Alliance《The State of Passkeys 2026: Global Consumer and Workforce Report》给出关键数据：全球约有 50 亿个 passkey 处于活跃使用状态；90% 的消费者熟悉 passkey，75% 已在至少部分账户上启用；68% 的组织正在部署、试点或推广 passkey 用于员工认证（[The State of Passkeys 2026 — FIDO Alliance](https://fidoalliance.org/wp-content/uploads/2026/05/The-State-of-Passkeys-Global-Consumer-and-Workforce-Report-1.pdf)）。另一份汇总指出，passkey 认知率从 2023 年的 39% 升至 75%，48% 的 Top 100 网站已支持 passkey（较 2022 年翻倍以上），可使用 passkey 的账户总数超过 150 亿（[Password Statistics for 2026](https://www.swif.ai/blog/password-statistics)）。体验数据方面，FIDO 口径下 passkey 平均登录耗时 8.5 秒，而「密码 + 验证码」流程平均 31.2 秒（[Passkeys vs Passwords: 8.5s vs 31s Sign-In [2026]](https://shattered.io/passkeys-vs-passwords/)）。

### 非人类身份与 AI 代理

多方口径显示 NHI 数量远超人类用户：KPMG 的 2026 年报告称平均企业内非人类身份与人类之比为 80:1，CyberArk 给出的比例为 82:1（[Your AI Agents Outnumber Your Employees 80 to 1](https://www.xyzbytes.com/blog/non-human-identity-crisis-ai-agents)）；云安全联盟（CSA）白皮书称平均为 45:1，云原生环境可达 144:1（[The Non-Human Identity Governance Vacuum — CSA](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/)）。GitGuardian《State of Secrets Sprawl 2026》发现 2025 年仅在公开 GitHub 上就新增 2,865 万个硬编码密钥，同比增长 34%，其中不乏与 AI 相关的密钥（[Non-Human Identity and Credential Lifecycle Governance for AI Agent Fleets](https://zylos.ai/research/2026-07-05-nonhuman-identity-credential-governance-ai-agent-fleets)）。IDC 预计到 2028 年将有最多 13 亿个 AI 代理在运行。

Sophos《State of Identity Security 2026》（调查 5,000 名 IT 与安全负责人）发现，薄弱的非人类身份管理已成为泄露的第二大根本原因，出现在约 40% 的安全事件中；Gartner 也将「IAM 适应 AI 代理」列为其年度顶级网络安全趋势之一（[AI Agents Expose the Non-Human Identity Security Gap](https://www.cybrsecmedia.com/non-human-identities-and-ai-agents-just-made-the-gap-measurable/)）。可见性缺口显著：仅约 21% 的组织维护着活跃代理的实时登记表，仅约 28% 能将代理行为追溯到人类发起者（[xyzbytes](https://www.xyzbytes.com/blog/non-human-identity-crisis-ai-agents)）。

## 核心技术与关键概念

- **SSO 与联合身份**：SAML 2.0、OIDC 在企业内主导跨域单点登录。
- **OAuth 2.1 / OIDC**：授权与身份层规范，OAuth 2.1 整合安全最佳实践，OIDC 在 OAuth 之上提供身份断言。
- **FIDO2 / WebAuthn / Passkey**：基于公钥的钓鱼抗性认证，凭证绑定域名，私钥不出设备。
- **MFA / 持续认证**：零信任身份模型中，认证不是一次性事件，而是结合用户、设备、位置、网络与威胁上下文的持续判定。
- **PAM（特权访问管理）**：管理特权账户与会话，2026 年的主流能力包括即时（Just-in-Time）特权授予、自动化回收、零常驻特权与端点权限管理（[Top 10 Best Privileged Access Management (PAM) Tools in 2026](https://cyberpress.org/best-privileged-access-management-tools/)）。
- **CIEM / NHI 治理**：对服务账户、API key、OAuth token、机器证书与 AI 代理凭证进行生命周期治理。

PAM 的趋势是从常驻特权转向 JIT 与最小权限：多款 2026 年工具强调通过审批工作流授予限时特权并在到期后自动撤销，同时以异常检测识别可疑特权行为（[10 Best Privileged Access Management Tools of 2026](https://thectoclub.com/tools/best-privileged-access-management-solutions/)）。

## 代表性组织与标准

- **IETF OAuth 工作组**：维护 OAuth 2.1、RFC 9728、RFC 8414 等（[draft-ietf-oauth-v2-1-13](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-13.html)）。
- **FIDO Alliance**：WebAuthn/Passkey 标准与年度采纳报告（[FIDO Alliance](https://fidoalliance.org/wp-content/uploads/2026/05/The-State-of-Passkeys-Global-Consumer-and-Workforce-Report-1.pdf)）。
- **CSA / NIST**：非人类身份治理与零信任身份框架（[CSA 白皮书](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/)）。
- **PAM 厂商生态**：2026 年评测覆盖 Netwrix、HashiCorp Boundary、Britive、StrongDM 等（[Top 10 PAM Tools](https://cyberpress.org/best-privileged-access-management-tools/)）。

## 关键数据与评测结果

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 活跃 passkey 数量 | 约 50 亿 | [FIDO Alliance](https://fidoalliance.org/wp-content/uploads/2026/05/The-State-of-Passkeys-Global-Consumer-and-Workforce-Report-1.pdf) |
| 消费者 passkey 认知率 / 启用率 | 90% / 75% | [FIDO Alliance](https://fidoalliance.org/wp-content/uploads/2026/05/The-State-of-Passkeys-Global-Consumer-and-Workforce-Report-1.pdf) |
| 组织部署/试点 passkey 比例 | 68% | [FIDO Alliance](https://fidoalliance.org/wp-content/uploads/2026/05/The-State-of-Passkeys-Global-Consumer-and-Workforce-Report-1.pdf) |
| NHI 与人类身份比例 | 80:1（KPMG）/ 82:1（CyberArk）/ 45:1（CSA） | [xyzbytes](https://www.xyzbytes.com/blog/non-human-identity-crisis-ai-agents)、[CSA](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/) |
| 2025 年 GitHub 新增硬编码密钥 | 2,865 万个（+34% YoY） | [GitGuardian（zylos.ai 转引）](https://zylos.ai/research/2026-07-05-nonhuman-identity-credential-governance-ai-agent-fleets) |
| NHI 管理薄弱作为泄露根本原因占比 | 约 40% | [Sophos（cybrsecmedia 转引）](https://www.cybrsecmedia.com/non-human-identities-and-ai-agents-just-made-the-gap-measurable/) |

## 趋势与争议

- **密码退场速度**：passkey 已具规模，但供应链、遗留系统、跨设备迁移与账户恢复仍是障碍，且部分场景仍需密码作为回退，取代进程存在争议。
- **OAuth 2.1 定稿时点**：截至 draft-13 仍为草案，何时成为正式 RFC 尚不确定，企业实施应以草案要求为最低基线。
- **NHI 治理真空**：身份治理框架对机器的严格程度远低于对人类的严格程度，AI 代理的自主性与权限扩散放大了这一差距，如何为代理设定「人类责任人」尚无统一标准。
- **代理式身份的新风险**：AI 代理与静态服务账户不同，可自主决策并调用工具，一旦权限过大或被提示注入操纵，可能产生难以追溯的连锁操作。

## 参考来源

1. [The OAuth 2.1 Authorization Framework — draft-ietf-oauth-v2-1-13 (IETF)](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-13.html)
2. [OAuth 2.0 Protected Resource Metadata — RFC 9728 (IETF)](https://datatracker.ietf.org/doc/rfc9728/)
3. [draft-ietf-oauth-identity-chaining-06 (IETF)](https://www.ietf.org/archive/id/draft-ietf-oauth-identity-chaining-06.txt)
4. [draft-ietf-oauth-refresh-token-expiration-00 (IETF)](https://www.ietf.org/archive/id/draft-ietf-oauth-refresh-token-expiration-00.txt)
5. [The State of Passkeys 2026: Global Consumer and Workforce Report — FIDO Alliance](https://fidoalliance.org/wp-content/uploads/2026/05/The-State-of-Passkeys-Global-Consumer-and-Workforce-Report-1.pdf)
6. [Passkeys vs Passwords: 8.5s vs 31s Sign-In [2026] — Shattered](https://shattered.io/passkeys-vs-passwords/)
7. [Password Statistics for 2026: Reuse, Cracks, Breaches, and the Passkey Shift — SWIF](https://www.swif.ai/blog/password-statistics)
8. [Passkeys & FIDO2: Passwordless Authentication Explained — Cyberphinix](https://cyberphinix.de/en/blog/passkeys-fido2-explained/)
9. [Your AI Agents Outnumber Your Employees 80 to 1 — xyzbytes](https://www.xyzbytes.com/blog/non-human-identity-crisis-ai-agents)
10. [The Non-Human Identity Governance Vacuum — Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/)
11. [Non-Human Identity and Credential Lifecycle Governance for AI Agent Fleets — zylos.ai](https://zylos.ai/research/2026-07-05-nonhuman-identity-credential-governance-ai-agent-fleets)
12. [AI Agents Expose the Non-Human Identity Security Gap — CybrSecMedia](https://www.cybrsecmedia.com/non-human-identities-and-ai-agents-just-made-the-gap-measurable/)
13. [Top 10 Best Privileged Access Management (PAM) Tools in 2026 — CyberPress](https://cyberpress.org/best-privileged-access-management-tools/)
14. [10 Best Privileged Access Management Tools of 2026 — The CTO Club](https://thectoclub.com/tools/best-privileged-access-management-solutions/)