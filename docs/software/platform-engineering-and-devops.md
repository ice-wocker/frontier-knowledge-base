# 平台工程与 DevOps

> 最后更新：2026-09-26 ｜ 领域：平台工程与 DevOps ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

2025–2026 年，DevOps 的重心从「工具链拼接」转向**平台工程（Platform Engineering）**与**AI 辅助运维**。平台工程的核心是把内部平台当作产品来经营，用「黄金路径（golden paths）」替代临时脚本与一次性自动化（[Platform engineering: how internal developer platforms reshape software delivery](https://www.future-of-software.com/platform-engineering-in-2026-what-it-actually-costs-and-what-it-actually-delivers)）。与此同时，DORA 报告揭示了 AI 带来的「生产力悖论」：个体产出显著提升，但组织级交付指标并未同步改善。

## 2025–2026 最新进展

### 1. 平台工程与 IDP

**Backstage** 由 Spotify 于 2020 年开源并捐赠给 CNCF（2022-03-15 进入孵化阶段），已成为 IDP 事实标准（[Backstage — CNCF](https://www.cncf.io/projects/backstage/)）。CNCF 2025 年度报告显示，Backstage 自 2024 年以来贡献量翻倍以上，是领先的开源 IDP（[CNCF 2025 ANNUAL REPORT](https://www.cncf.io/wp-content/uploads/2026/03/cncf_ar25_033126a.pdf)）。据行业梳理，其插件市场已列出 200 多个插件、宣称被 3000 多家组织采用，架构为 React 前端 + 后端目录（[Platform Engineering in 2026: The IDP Maturity Report](https://www.agency.codercops.com/blog/platform-engineering-internal-developer-platforms-2026)）。CNCF 与 SlashData 于 2026-03-24 联合发布的报告将 Backstage、Helm、kro 置于「adopt」位置，其中 Helm 获得最高的可靠性成熟度评分——94% 的开发者给出四星或五星（[CNCF and SlashData Report Finds Platform Engineering Tools Maturing](https://www.cncf.io/announcements/2026/03/24/cncf-and-slashdata-report-finds-platform-engineering-tools-maturing-as-organizations-prepare-for-ai-driven-infrastructure/)）。除 Backstage 外，**Port** 等平台也在探索将 AI Copilot 嵌入门户以增强自助服务（[Internal Developer Portals 2.0](https://it-stud.io/internal-developer-portals-2-0-how-ai-copilots-inside-backstage-and-port-are-transforming-developer-self-service)）。

### 2. CI/CD

CI/CD 市场呈两强格局：**GitHub Actions** 以最低摩擦、最丰富生态与按量计价见长，是开源项目与中小团队默认选择；**GitLab CI/CD** 则以一体化 DevOps 平台、内置安全扫描与自托管合规能力取胜，适合受监管行业（[Best CI/CD Platforms 2026: GitHub Actions vs GitLab CI/CD](https://ai.gravitydevops.com/articles/best-cicd-platforms-2026)、[GitHub Actions vs GitLab CI/CD: Complete CI/CD Comparison (2026)](https://dev.to/_d7eb1c1703182e3ce1782/github-actions-vs-gitlab-cicd-complete-cicd-comparison-2026-48ac)）。**Dagger** 以「可移植、可调试、随处运行」为卖点（[Best CI/CD Tools 2026](https://thesoftwarescout.com/best-ci-cd-tools-2026-complete-guide-to-continuous-integration-deployment)），**Tekton** 则是 Kubernetes 原生的流水线框架。

### 3. IaC（基础设施即代码）

**Terraform** 仍是主流，但 2023 年 8 月的许可证变更催生了 **OpenTofu**——由 Linux Foundation 治理、与 Terraform 1.5.x API 兼容、沿用 HCL 语法与同一批 provider/module（[Best Terraform Alternatives in 2026](https://www.pulumi.com/blog/best-terraform-alternatives/)、[Best Infrastructure as Code Tools in 2026](https://saaspedia.dev/posts/best-iac-tools)）。**Pulumi** 支持用通用编程语言（含类、对象、继承）定义基础设施（[Pulumi](https://www.pulumi.com/)）；**Crossplane** 将 Kubernetes 作为通用控制平面，已于 2025-11-06 从 CNCF 毕业（[CNCF Announces Graduation of Crossplane](https://www.cncf.io/search/Crossplane/)）。其它选项包括 AWS CDK、Bicep、Google Cloud Infrastructure Manager 等（[Best Infrastructure as Code (IaC) Tools for 2026](https://www.pulumi.com/blog/infrastructure-as-code-tools/)。

### 4. 可观测性

**OpenTelemetry** 于 2026-05-11 从 CNCF 毕业，拥有超过 24,000 名贡献者，是活跃度第二高的 CNCF 项目，标志着可观测性从孤立工具选择升级为战略支柱（[OpenTelemetry — CNCF](https://www.cncf.io/projects/opentelemetry/)）。**Grafana Labs** 在 GrafanaCON 2026（2026-04-21）发布 **Grafana 13**，为 Alloy 引入 OpenTelemetry engine mode（可用标准 OTel Collector YAML 配置并保留 Prometheus 能力），并推出处于公开预览的 AI Observability 以监控 Agent 工作负载（[Grafana Labs Launches Grafana 13 at GrafanaCON 2026](https://grafana.com/press/2026/04/21/grafana-labs-launches-grafana-13-at-grafanacon-2026-makes-open-observability-easier-to-run-at-scale/)、[GrafanaCON 2026 announcements](https://grafana.com/blog/grafanacon-2026-announcements/)）。Grafana Labs 的 2026 可观测性调研显示，多数组织已在使用 OpenTelemetry 或正在向其迁移（[Grafana Labs Launches Grafana 13](https://grafana.com/press/2026/04/21/grafana-labs-launches-grafana-13-at-grafanacon-2026-makes-open-observability-easier-to-run-at-scale/)）。

### 5. SRE 与错误预算

SRE 以 SLO/错误预算约束发布节奏仍是核心方法论。2026 年的新变量是 **AI SRE Agent**：AWS DevOps Agent、Azure SRE Agent 以及 Dynatrace（2026-07-27 发布自主 SRE agents）等产品可自主诊断并提出或执行缓解措施（[Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/)、[Overview of Azure SRE Agent](https://learn.microsoft.com/sr-latn-rs/azure/sre-agent/overview)、[AI SRE Agents in 2026: What They Can Really Do](https://nerdleveltech.com/ai-sre-agents-autonomous-incident-remediation)）。实践中，Agent 已能独立调查，但修复动作通常仍需人工审批与安全策略约束（[AI-Powered Incident Response: Cut MTTR 60% with LLMs (2026)](https://squareops.com/blog/ai-powered-incident-response-reduce-mttr-sre/)）。

### 6. 供应链安全

**SLSA** 已发布 v1.2 规范，其「软件证明（attestation）」模型用于向自动化策略引擎提供关于制品来源与构建过程的认证元数据（[Software attestations — SLSA v1.2](https://slsa.dev/spec/v1.2/attestation-model)）。**Sigstore/Cosign** 提供无需管理密钥的 keyless 签名；**SBOM + SLSA + Sigstore** 组合被视为纵深防御（[Supply Chain Security: SBOM, SLSA et Sigstore en 2026](https://ayinedjimi-consultants.fr/static/pdf/supply-chain-security-sbom-slsa-sigstore.pdf)）。CNCF TAG Security 的《Software Supply Chain Best Practices v2》建议使用签名证明、生成并分发 SBOM，并验证安全元数据（[SOFTWARE SUPPLY CHAIN BEST PRACTICES V2](https://tag-security.cncf.io/community/working-groups/supply-chain-security/supply-chain-security-paper-v2/Software_Supply_Chain_Practices_whitepaper_v2.pdf)）。值得注意的是，2026 年的 **Mini Shai-Hulud** 攻击表明 SLSA 的边界：攻击者从 runner 内存中提取合法 OIDC token、经 Sigstore Fulcio 签名，生成的证明仍「如实」报告了构建者与仓库，说明**有效的证明并不等于可信的意图**（[Mini Shai-Hulud: Where SLSA's Boundaries Fall](https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do)）。

### 7. AI 辅助 DevOps 与 DORA 数据

DORA 的《State of AI-assisted Software Development》报告显示，90% 的技术从业者已在工作中使用 AI，超过 80% 认为 AI 提升了生产力（[Balancing AI tensions — DORA](https://dora.dev/insights/balancing-ai-tensions/)）。但早期研究（2024）曾指出 25% 的 AI 采用度提升反而伴随约 1.5% 的交付吞吐下降与 7.2% 的稳定性下降，原因是 AI 加速生成代码导致批次变大、评审更慢（[Impact of Generative AI in Software Development — DORA](https://dora.dev/ai/gen-ai-report/report/)）。2025 年报告进一步刻画为「生产力悖论」：个体产出提升约 21%、每人合并的 PR 数增加约 98%，但组织级交付指标基本持平（[AI in the SDLC: The Productivity Paradox](https://stratofactory.com/wp-content/uploads/2026/06/AI_in_the_SDLC_Research_by_Stratofactory.pdf)）。DORA 2026 以「J 曲线」解释这一现象：AI 采用先带来学习成本与「验证税」导致的短期回落，随后才可能进入指数增长（[What the DORA 2026 J-Curve Actually Says](http://revelara.ai/blog/dora-2026-j-curve-reliability-vibe-coding/)）。此外，AI Agent 工作负载也带来新的安全面，如 CI/CD 中的「Shadow AI」（[Shadow AI in CI/CD — CNCF](https://www.cncf.io/blog/2026/08/07/shadow-ai-in-ci-cd-threat-modeling-the-path-from-developer-laptop-to-kubernetes/)）。

## 核心技术与关键概念

- **IDP / Golden Paths**：Service Catalog、Software Templates、TechDocs 与插件生态构成开发者门户。
- **IaC**：声明式定义基础设施，HCL（Terraform/OpenTofu）与通用编程语言（Pulumi）两条路线。
- **OpenTelemetry / Prometheus**：厂商中立的遥测采集标准与指标系统。
- **SLO / 错误预算**：以可靠性目标约束发布速度的 SRE 方法论。
- **SLSA / SBOM / Sigstore**：供应链完整性的三层防护。
- **Agentic SRE**：AI Agent 参与告警分诊、根因分析与受控修复。

## 代表性项目/平台

| 类别 | 项目/平台 | 官方链接 |
|---|---|---|
| IDP | Backstage / Port | https://backstage.io/、https://www.port.io/ |
| CI/CD | GitHub Actions / GitLab CI / Dagger / Tekton | https://github.com/features/actions、https://about.gitlab.com/、https://dagger.io/、https://tekton.dev/ |
| IaC | Terraform / OpenTofu / Pulumi / Crossplane | https://www.terraform.io/、https://opentofu.org/、https://www.pulumi.com/、https://www.crossplane.io/ |
| 可观测性 | OpenTelemetry / Prometheus / Grafana | https://opentelemetry.io/、https://prometheus.io/、https://grafana.com/ |
| 供应链安全 | SLSA / Sigstore / in-toto | https://slsa.dev/、https://www.sigstore.dev/、https://in-toto.io/ |
| GitOps | Argo CD / Flux | https://argo-cd.readthedocs.io/、https://fluxcd.io/ |

## 版本与生态数据

| 项目/指标 | 数据 | 来源 |
|---|---|---|
| OpenTelemetry | 2026-05-11 CNCF 毕业；24,000+ 贡献者 | cncf.io |
| Grafana | Grafana 13（2026-04-21 发布） | grafana.com |
| Helm | 94% 开发者给出四/五星可靠性评分 | CNCF/SlashData 2026 |
| Backstage | CNCF 孵化；贡献量较 2024 翻倍以上 | CNCF 2025 年报 |
| SLSA | v1.2 规范（attestation 模型） | slsa.dev |
| DORA（2024） | AI 采用 +25% → 吞吐 -1.5%、稳定性 -7.2% | dora.dev |
| DORA（2025） | AI 使用者占比 90%；PR/人 +98% | dora.dev |
| CNCF 项目数（2025） | 毕业 34、孵化 36、沙箱 144 | CNCF 2025 年报 |

## 趋势与争议

1. **平台工程的「产品化」**：平台团队需要像产品团队一样拥有路线图与 SLO，避免 IDP 沦为「又一个门户」。
2. **AI 的价值被高估还是被延迟**：DORA 的 J 曲线与 2025 年「生产力悖论」表明，AI 的收益取决于流程、评审与信任机制的配套变革。
3. **Agent 自主修复的安全边界**：AI SRE Agent 虽能大幅降低 MTTR，但「目标锁定（goal lock）」与越权修复是主要风险，需要明确「安全动作面」。
4. **供应链证明的信任假设**：Mini Shai-Hulud 攻击说明仅靠签名与证明不足以防御，构建环境的隔离与运行时防护同样关键。

## 参考来源

1. [Platform engineering: how internal developer platforms reshape software delivery](https://www.future-of-software.com/platform-engineering-in-2026-what-it-actually-costs-and-what-it-actually-delivers)
2. [Backstage — CNCF](https://www.cncf.io/projects/backstage/)
3. [CNCF 2025 ANNUAL REPORT](https://www.cncf.io/wp-content/uploads/2026/03/cncf_ar25_033126a.pdf)
4. [Platform Engineering in 2026: The Internal Developer Platform Maturity Report](https://www.agency.codercops.com/blog/platform-engineering-internal-developer-platforms-2026)
5. [CNCF and SlashData Report Finds Platform Engineering Tools Maturing](https://www.cncf.io/announcements/2026/03/24/cncf-and-slashdata-report-finds-platform-engineering-tools-maturing-as-organizations-prepare-for-ai-driven-infrastructure/)
6. [Internal Developer Portals 2.0: How AI Copilots Inside Backstage and Port Are Transforming Developer Self-Service](https://it-stud.io/internal-developer-portals-2-0-how-ai-copilots-inside-backstage-and-port-are-transforming-developer-self-service)
7. [Best CI/CD Platforms 2026: GitHub Actions vs GitLab CI/CD](https://ai.gravitydevops.com/articles/best-cicd-platforms-2026)
8. [GitHub Actions vs GitLab CI/CD: Complete CI/CD Comparison (2026)](https://dev.to/_d7eb1c1703182e3ce1782/github-actions-vs-gitlab-cicd-complete-cicd-comparison-2026-48ac)
9. [Best CI/CD Tools 2026: 9 Pipelines Ranked by Speed, Price & DX](https://thesoftwarescout.com/best-ci-cd-tools-2026-complete-guide-to-continuous-integration-deployment)
10. [Best Terraform Alternatives in 2026](https://www.pulumi.com/blog/best-terraform-alternatives/)
11. [Best Infrastructure as Code Tools in 2026 — Compared by a Practicing SRE](https://saaspedia.dev/posts/best-iac-tools)
12. [Best Infrastructure as Code (IaC) Tools for 2026](https://www.pulumi.com/blog/infrastructure-as-code-tools/)
13. [Pulumi - Infrastructure as Code in Any Programming Language](https://www.pulumi.com/)
14. [Cloud Native Computing Foundation Announces Graduation of Crossplane](https://www.cncf.io/search/Crossplane/)
15. [OpenTelemetry — CNCF](https://www.cncf.io/projects/opentelemetry/)
16. [Grafana Labs Launches Grafana 13 at GrafanaCON 2026](https://grafana.com/press/2026/04/21/grafana-labs-launches-grafana-13-at-grafanacon-2026-makes-open-observability-easier-to-run-at-scale/)
17. [GrafanaCON 2026 announcements: A guide to all the latest news](https://grafana.com/blog/grafanacon-2026-announcements/)
18. [Leverage Agentic AI for Autonomous Incident Response with AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/)
19. [Overview of Azure SRE Agent](https://learn.microsoft.com/sr-latn-rs/azure/sre-agent/overview)
20. [AI SRE Agents in 2026: What They Can Really Do](https://nerdleveltech.com/ai-sre-agents-autonomous-incident-remediation)
21. [AI-Powered Incident Response: Cut MTTR 60% with LLMs (2026)](https://squareops.com/blog/ai-powered-incident-response-reduce-mttr-sre/)
22. [Software attestations — SLSA v1.2](https://slsa.dev/spec/v1.2/attestation-model)
23. [Supply Chain Security: SBOM, SLSA et Sigstore en 2026](https://ayinedjimi-consultants.fr/static/pdf/supply-chain-security-sbom-slsa-sigstore.pdf)
24. [SOFTWARE SUPPLY CHAIN BEST PRACTICES V2 — CNCF TAG Security](https://tag-security.cncf.io/community/working-groups/supply-chain-security/supply-chain-security-paper-v2/Software_Supply_Chain_Practices_whitepaper_v2.pdf)
25. [Mini Shai-Hulud: Where SLSA's Boundaries Fall](https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do)
26. [Balancing AI tensions: Moving from AI adoption to effective SDLC use — DORA](https://dora.dev/insights/balancing-ai-tensions/)
27. [Impact of Generative AI in Software Development — DORA](https://dora.dev/ai/gen-ai-report/report/)
28. [AI in the SDLC: The Productivity Paradox](https://stratofactory.com/wp-content/uploads/2026/06/AI_in_the_SDLC_Research_by_Stratofactory.pdf)
29. [What the DORA 2026 J-Curve Actually Says About Reliability and Vibe Coding](http://revelara.ai/blog/dora-2026-j-curve-reliability-vibe-coding/)
30. [Shadow AI in CI/CD: Threat-modeling the path from developer laptop to Kubernetes](https://www.cncf.io/blog/2026/08/07/shadow-ai-in-ci-cd-threat-modeling-the-path-from-developer-laptop-to-kubernetes/)