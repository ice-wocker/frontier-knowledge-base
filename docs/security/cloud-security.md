# 云安全

> 最后更新：2026-09-26 ｜ 领域：安全 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

云安全（Cloud Security）围绕云上身份、配置、工作负载、数据与基础设施即代码（IaC）的风险展开。2025–2026 年的主线是「平台整合」与「身份风险前置」：Gartner 提出的 CNAPP（Cloud-Native Application Protection Platform）成为事实上的采购框架，而 IAM 过度授权、暴露的服务主体凭证与 AI 网关类组件的供应链风险，成为多起真实事件的核心成因。

## 最新进展（2025–2026）

### CNAPP 成为统一平台

Gartner 预测 80% 的企业将整合到 CNAPP——一个在单一数据模型下集成 CSPM（云安全态势管理）、CWPP（云工作负载保护）、CIEM（云基础设施权限管理）与 DSPM（数据安全态势管理）的统一平台，其核心价值主张是攻击路径关联分析（[CSPM vs CWPP: Choosing the Right Cloud Security Tool in 2026](https://cipherssecurity.com/cspm-vs-cwpp-cloud-security-2026/)）。另有分析指出，Gartner 的目标是让企业平均云原生安全厂商数量从 2022 年的 10 家降至 3 家或更少，并预计 CNAPP 细分市场到 2028 年规模达 250 亿美元（[CNAPP in 2026: Why CSPM, CWPP, CIEM, and KSPM Are All Collapsing Into One Platform](https://netguardia.com/security-operations/cloud-security/cnapp-in-2026-why-cspm-cwpp-ciem-and-kspm-are-all-collapsing-into-one-platform/)）。

按 Forrester 在 CWS 报告中的界定，完整的云工作负载安全 = CSPM + CIEM + 云工作负载保护 + IaC 安全 + 容器运行时保护 + 检测与响应，且这些能力应整合到单一平台；即 CWPP 已演进为 CNAPP（[一文读懂：HIDS、EDR、CWPP 到底有什么区别？（2026 版）](https://cloud.tencent.com/developer/article/2750759)）。CNAPP 通常还包含 KSPM（Kubernetes 安全态势）与 IaC 扫描（[CNAPP Explained: Cloud-Native Application Protection Platforms](https://www.graphnodesoftware.com/guides/cnapp-cloud-application-security)）。

### 容器与 Kubernetes 风险

2025 年披露了多个影响容器生态的高危漏洞：CVE-2025-23266（被称为「NVIDIAScape」，CVSS 9.0）利用 NVIDIA Container Toolkit 的 OCI `createContainer` 钩子，可从容器镜像继承环境变量并以容器文件系统权限执行，攻击者可在镜像中设置 `LD_PRELOAD` 实现逃逸（[Kubernetes AI Workload Security: Hardening LLM Infrastructure](https://beyondscale.tech/blog/kubernetes-ai-workload-security)）。另一个是 runC 的 CVE-2025-52565，攻击者可在容器初始化期间将 `/dev/null` 替换为符号链接，使 runC 将攻击者控制的路径以读写方式 bind-mount 进容器，从而写入 `/proc` 并实现完整容器逃逸（[Kubernetes and Container Security: Attacks, Misconfigurations, and Defenses](https://hivesecurity.gitlab.io/blog/kubernetes-container-security-attacks-and-defenses/)）。

学术综述将风险归因于共享宿主内核漏洞与粗粒度 RBAC 权限等根因，前者导致从容器边界突破到宿主机命令执行，后者导致横向移动与未授权挖矿（[KUBERNETES IN CYBERSECURITY: Architecture, Vulnerabilities, and Defense-in-Depth Hardening Frameworks](https://www.in-academy.uz/index.php/SI/article/download/50038/21437/23915)）。Kubernetes 项目通过安全响应委员会（SRC）维护官方 CVE 列表，并提供 JSON/RSS 订阅源以便程序化获取（[官方 CVE 订阅源 — Kubernetes](https://kubernetes.io/zh-cn/docs/reference/issues-security/official-cve-feed/)）。

### 云 IAM 与凭证暴露

Intruder 的 2026 Cloud Security Index 扫描约 3,000 家组织的错误配置数据，发现 80% 至 98% 的云账户存在弱 IAM 控制或缺失日志（因云厂商而异）；CloudSEK 则追踪到一起经由流行 AI 网关库（LiteLLM）的供应链攻击，暴露了云凭证、SSH 密钥与 Kubernetes token，影响超过 2 个项目（[Cloud IAM Fails Hit 98%, LiteLLM Breach Hits 434K [2026]](https://shattered.io/cloud-iam-misconfiguration-litellm-breach-2026/)）。

微软披露的 Storm-3168 案例显示了「代理式云攻击」：被攻陷的服务主体的 client ID、client secret 与 tenant ID 曾以明文出现在公开 GitHub issue 中，虽然后来被编辑删除，但仍可通过公开编辑历史获取；微软强调，删除或遮蔽已暴露的密钥不会使其失效，任何公开发布过的凭证都应视为已泄密并立即吊销或轮换（[Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)）。

## 核心技术与关键概念

- **CSPM**：持续评估云资源配置与合规基线（CIS、等保等），发现公开存储桶、开放安全组、缺失加密等。
- **CWPP**：面向工作负载的运行时保护，覆盖主机、容器、Serverless。
- **CIEM**：管理「哪个身份在什么条件下可以访问哪些云资源」，解决过度授权与权限升级链（[CSPM vs CWPP in 2026](https://cipherssecurity.com/cspm-vs-cwpp-cloud-security-2026/)）。
- **CIEM 与权限升级链**：攻击者先通过钓鱼、泄露凭证或 token 窃取获得低权限账户，再枚举 IAM 权限并串联出提升路径（[Cloud Security Threats 2026: What You Must Know](https://cybknow.com/cloud-security-threats-2026/)）。
- **KSPM**：Kubernetes 配置与 RBAC 态势管理。
- **IaC 扫描**：在 Terraform、CloudFormation 等模板阶段发现错误配置，左移风险。
- **DSPM**：发现与分类敏感数据、评估数据流与访问风险。

云安全的实际风险更多来自配置、身份、访问、API、SaaS 集成、Kubernetes、CI/CD 管线与第三方依赖，而非「云」本身（[Cloud Security Statistics 2026: IAM, Breaches & Risk](https://deepstrike.io/blog/cloud-security-statistics)）。

## 代表性厂商 / 平台

- **CNAPP 玩家**：2026 年多份评测对比了整合 CSPM/CWPP/CIEM/KSPM/DSPM 的平台（[Top 10 Best CNAPP Platforms in 2026](https://cybersecuritynews.com/best-cnapp-platforms/amp/)）。
- **Kubernetes 官方**：SRC 维护 CVE 列表与安全公告（[Kubernetes Issues and Security](https://kubernetes.io/docs/reference/issues-security/_print/)）。
- **云厂商与安全厂商**：Microsoft 安全博客持续披露云攻击案例与防护建议。

## 关键数据与评测结果

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 存在弱 IAM/缺失日志的云账户比例 | 80%–98% | [Intruder 2026 Cloud Security Index（shattered.io 转引）](https://shattered.io/cloud-iam-misconfiguration-litellm-breach-2026/) |
| 企业预期整合到 CNAPP 的比例 | 80%（Gartner 预测） | [cipherssecurity](https://cipherssecurity.com/cspm-vs-cwpp-cloud-security-2026/) |
| 企业使用云原生安全厂商数目标（Gartner） | 从 10 家降至 ≤3 家 | [netguardia](https://netguardia.com/security-operations/cloud-security/cnapp-in-2026-why-cspm-cwpp-ciem-and-kspm-are-all-collapsing-into-one-platform/) |
| CNAPP 细分市场规模预测（2028） | 250 亿美元 | [netguardia](https://netguardia.com/security-operations/cloud-security/cnapp-in-2026-why-cspm-cwpp-ciem-and-kspm-are-all-collapsing-into-one-platform/) |
| NVIDIA Container Toolkit 逃逸漏洞 | CVE-2025-23266，CVSS 9.0 | [beyondscale.tech](https://beyondscale.tech/blog/kubernetes-ai-workload-security) |

## 趋势与争议

- **平台 vs 单点工具**：整合带来的攻击路径关联能力与「单一供应商锁定」风险并存，不同报告对整合速度的预期差异较大（Gartner 给出 2028 目标，实际落地进度仍有争议）。
- **身份安全成为云安全主战场**：服务主体、CIEM、非人类身份（NHI）治理被反复强调，与身份与访问管理领域高度重叠。
- **AI 基础设施带来的新工作负载风险**：AI 网关、模型推理容器、GPU 共享引入了新的供应链与逃逸面，容器安全与 AI 供应链安全的边界趋于模糊。
- **凭证「删而不废」的认知误区**：多起事件表明公开发布过的密钥即使被隐藏仍有效，凭证轮换与吊销流程成为审计重点。

## 参考来源

1. [CSPM vs CWPP: Choosing the Right Cloud Security Tool in 2026 — Ciphers Security](https://cipherssecurity.com/cspm-vs-cwpp-cloud-security-2026/)
2. [CNAPP in 2026: Why CSPM, CWPP, CIEM, and KSPM Are All Collapsing Into One Platform — NetGuardia](https://netguardia.com/security-operations/cloud-security/cnapp-in-2026-why-cspm-cwpp-ciem-and-kspm-are-all-collapsing-into-one-platform/)
3. [一文读懂：HIDS、EDR、CWPP 到底有什么区别？（2026 版）— 腾讯云](https://cloud.tencent.com/developer/article/2750759)
4. [CNAPP Explained: Cloud-Native Application Protection Platforms — Graphnode](https://www.graphnodesoftware.com/guides/cnapp-cloud-application-security)
5. [Top 10 Best CNAPP (Cloud-Native Application Protection) Platforms in 2026 — Cybersecurity News](https://cybersecuritynews.com/best-cnapp-platforms/amp/)
6. [Kubernetes AI Workload Security: Hardening LLM Infrastructure — BeyondScale](https://beyondscale.tech/blog/kubernetes-ai-workload-security)
7. [Kubernetes and Container Security: Attacks, Misconfigurations, and Defenses — Hive Security](https://hivesecurity.gitlab.io/blog/kubernetes-container-security-attacks-and-defenses/)
8. [KUBERNETES IN CYBERSECURITY: Architecture, Vulnerabilities, and Defense-in-Depth Hardening Frameworks](https://www.in-academy.uz/index.php/SI/article/download/50038/21437/23915)
9. [官方 CVE 订阅源 — Kubernetes](https://kubernetes.io/zh-cn/docs/reference/issues-security/official-cve-feed/)
10. [Kubernetes Issues and Security — Kubernetes](https://kubernetes.io/docs/reference/issues-security/_print/)
11. [Cloud IAM Fails Hit 98%, LiteLLM Breach Hits 434K [2026] — Shattered](https://shattered.io/cloud-iam-misconfiguration-litellm-breach-2026/)
12. [Cloud Security Threats 2026: What You Must Know — CybKnow](https://cybknow.com/cloud-security-threats-2026/)
13. [Storm-3168: Agentic-driven cloud attacks using compromised service principals — Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)
14. [Cloud Security Statistics 2026: IAM, Breaches & Risk — DeepStrike](https://deepstrike.io/blog/cloud-security-statistics)