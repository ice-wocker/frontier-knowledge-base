# 软件供应链安全

> 最后更新：2026-09-26 ｜ 领域：安全 · 供应链与构建环境 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

软件供应链安全关注代码从源码、依赖、构建、打包到分发全链路被篡改的风险。SLSA（Supply-chain Levels for Software Artifacts，读作 "salsa"）是由产业共识建立、可增量采纳的供应链安全指南：生产方据此加固自身链路，消费方据此判断软件包是否可信（[About SLSA](https://slsa.dev/spec/v1.1/about)）。SLSA 官方将典型威胁案例指向 SolarWinds 与 Codecov 事件，并强调风险不只存在于代码本身，而分布在从源码到构建、打包、分发的每个环节——任何环节的弱点都会动摇"你运行的代码就是你扫描过的代码"这一前提（同上）。

SLSA v1.1 当前只包含 Build 一条 track，覆盖 Build Level 1–3，更高等级留待后续版本；Build track 的核心是 provenance（来源证明），描述"谁构建了产物、用了什么流程、输入是什么"，级别越高对构建过程、provenance 与产物被篡改的防护越强（[SLSA specification v1.1](https://slsa.dev/spec/v1.1/)、[SLSA Build Track](https://slsa.dev/spec/v1.1-rc1/zonepage)）。历史上，MOVEit、GoAnywhere 等被广泛部署的托管文件传输工具遭攻陷，确立了「攻陷一个被广泛部署的工具、同时勒索其整个客户群」的攻击模板（[2026 Ransomware Attack Analysis: Trends & Defenses](https://nohack.net/latest-ransomware-attack-analysis-2026/)）。

## 最新进展（2025–2026）

**npm 生态蠕虫化攻击。** 2025 年 9 月，被 StepSecurity 命名为 Shai-Hulud 的攻击成为 npm registry 上首个可自我复制的蠕虫，初始入侵集中在中招维护者账号与 `@ctrl/tinycolor` 等包（[Supply Chain Attacks in 2025/2026](https://www.softscheck.com/en/blog/supply-chain-attacks/)）。其链路为：受害者执行 `npm install` → `postinstall` 脚本自动触发 → 窃取 npm token、GitHub PAT 及 AWS/GCP/Azure 云凭据 → 外泄并在受害者账号下创建名为 "Shai-Hulud" 的公开仓库 → 利用窃得的发布 token 感染下游包，在大约 48–72 小时内把影响从少数包扩散到数百个包（[The Shai-Hulud npm Supply Chain Attack Explained](https://safeguard.sh/resources/blog/the-shai-hulud-npm-supply-chain-attack-explained)）。Socket、StepSecurity、Aikido、Wiz 等厂商在不同阶段共记录超过 500 个被投毒包版本；2025 年 11 月的第二波 "The Second Coming" 进一步加入可在失败条件下擦除开发者主目录的破坏逻辑，并尝试在受害者仓库内注册恶意自托管 GitHub Actions runner 以获取持久化（同上）。该事件不映射为单一 CVE：恶意发布通常按包/版本逐个发布 GHSA，个别咨询的 CVSS 落在 9.0–9.8（Critical），且不会进入 CISA KEV 目录——这正是只依赖 CVE/KEV 优先级流程的组织反应迟缓的原因（同上）。

**SLSA 自身的边界被公开讨论。** SLSA 官方博客以 "Mini Shai-Hulud" 为例指出：当攻击者代码在构建平台内部运行时，产出的 attestation 与合法包"无法区分"，因为 attestation 只是构建平台观测结果的记录——观测准确，但构建已被攻陷；SLSA Build L3 正是通过要求构建平台保证隔离（除声明参数外，任何外部影响都不得改变构建）来应对这一问题（[Mini Shai-Hulud: Where SLSA's Boundaries Fall](https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do)）。

**SBOM 从最佳实践变为法定义务。** 欧盟《网络韧性法案》（Cyber Resilience Act，CRA，Regulation (EU) 2024/2847）要求制造商为所有带数字元素的产品维护软件物料清单（SBOM），使用通用的机器可读格式、至少覆盖顶层依赖，实践上通常采用 SPDX 或 CycloneDX（[EU Cyber Resilience Act: Overview, Requirements, and Timelines](https://www.docker.com/blog/eu-cyber-resilience-act-overview/)、[CRA guide for software developers](https://www.cyberresilienceact.eu/guide-software.html)）。CRA 于 2024 年 12 月 10 日生效，报告义务自 2026 年 9 月（生效后 21 个月）适用，大部分义务自 2027 年 12 月 11 日（36 个月）适用（[CRA FAQ](https://www.cyberresilienceact.eu/ja/faq.html)）。2026 年 8 月 13 日，ETSI 就 17 项 CRA 产品标准草案（EN 304 6xx 系列）启动公开征询，覆盖浏览器、密码管理器、杀毒软件、VPN、智能家居助手、联网玩具、可穿戴等 Class I/II 品类（[ETSI: 17 Draft CRA Product Standards](https://www.cyberresilienceact.eu/news/etsi-17-cra-product-standards-public-enquiry-13-august-2026.html)）。SBOM 的最小元素清单也在更新：澳大利亚 ACSC 发布 2026 版最小元素，新增 SBOM 作者签名、数据格式名称与版本、生成上下文、工具名称与版本、组件哈希值与算法、组件许可证等字段（[2026 Minimum Elements for a Software Bill of Materials (SBOM)](https://www.cyber.gov.au/business-government/supplier-cyber-risk-management/managing-cyber-supply-chains/2026-minimum-elements-for-a-software-bill-of-materials)）。

**签名与透明度日志成为默认。** Sigstore 生态的 in-toto attestation 已被 Homebrew（2024 年 5 月）、PyPI（2024 年 11 月）、Maven Central（2025 年 1 月）、NVIDIA NGC 的模型签名（2025 年 7 月）等采纳（[Sigstore Blog](https://blog.sigstore.dev/)）。其核心组件为 Cosign（签名/验签 CLI）、Fulcio（短时证书）、Rekor（透明度日志）；keyless 模式下 Cosign 通过 OIDC 身份获取临时密钥与证书，并用 CI 流水线自身的 OIDC token 证明"是哪条工作流产出了该产物"（[Image Signing with Cosign and Sigstore](https://safeguard.sh/resources/blog/image-signing-with-cosign-sigstore)）。Cosign v3 与基于 tile 的 Rekor v2 已发布（[Sigstore 项目概况](https://rywalker.com/research/sigstore)）。

**资金与威胁情报口径。** 2026 年 3 月 17 日，Linux Foundation 宣布来自 Anthropic、AWS、GitHub、Google、Google DeepMind、Microsoft、OpenAI 合计 1250 万美元的资助，由 Alpha-Omega 与 OpenSSF 管理；Alpha-Omega 自 2022 年 2 月成立以来已累计投入约 1400 万美元支持 LLVM、Java、PHP、Jenkins、Airflow 等项目（[Google | OpenSSF](https://openssf.org/tag/google/)、[Scorecard | OpenSSF](https://openssf.org/tag/scorecard/)）。ATT&CK v19.2（2026 年 8 月 6 日）作为首次 Agile 发布，新增 TeamPCP（G1056）、ShinyHunters（G1057）两个组织，以及 Shai-Hulud（S9008）、Mini Shai-Hulud（S9043）、CanisterWorm（S9042）、TeamPCP Cloud Stealer（S9041）等与 CI/CD 供应链攻击相关的软件条目（[Updates - August 2026](https://attack.mitre.org/resources/updates/)）。

## 核心技术与关键概念

- **SLSA 的 tracks 与 levels**：track 聚焦供应链的某个侧面（当前仅 Build），level 表示逐级加固的安全实践；SLSA 0 指尚未达到任何等级（[About SLSA](https://slsa.dev/spec/v1.1/about)）。
- **provenance 与 attestation**：provenance 记录构建主体、流程与输入；attestation 是这类可验证声明的载体，配套还有 VSA（Verification Summary Attestation）格式（[SLSA specification v1.1](https://slsa.dev/spec/v1.1/)）。
- **SBOM 与 ML-BOM**：SBOM 描述软件库集合或 Docker 镜像，通常是静态的、绑定到某个产品版本，列出 Go modules、PIP、Gem、NPM、DEB、RPM 等组件（[SBOM et OBOM](https://www.ossir.org/paris/supports/2026/JSSI/CoreUpdate-JSSI2026-SBOM.pdf)）；对 AI 场景还需覆盖模型、数据集与插件，OWASP 将其列为 LLM 供应链风险（[Supply Chain Vulnerabilities](https://learn.microsoft.com/pl-pl/security/zero-trust/catalog-ai-attack-techniques/supply-chain-vulnerabilities)）。
- **keyless 签名与透明度日志**：以 OIDC 身份绑定短时证书、把签名事件写入 Rekor，避免长期私钥（[Image Signing with Cosign and Sigstore](https://safeguard.sh/resources/blog/image-signing-with-cosign-sigstore)）。
- **构建环境安全**：hermetic build（隔离的 CI 环境）、构建后立即用 trivy/grype 扫描、用 cosign 做 keyless 签名、把 SBOM 与扫描结果作为可验证 attestation 附加（[Supply Chain Security 2026](https://dev.to/saaro_net/supply-chain-security-2026-sbom-sigstoreslsa-and-admission-control-as-devops-standard-3lbl)）。
- **依赖侧防护**：lockfile 固定版本、CI 中 `npm install --ignore-scripts` 或 `.npmrc` 设 `ignore-scripts=true`、要求硬件密钥 2FA 与短时/最小权限发布 token、审计 lockfile 与 IOC 列表、排查非预期的 "Shai-Hulud" 仓库与 Actions/自托管 runner 注册（[The Shai-Hulud npm Supply Chain Attack Explained](https://safeguard.sh/resources/blog/the-shai-hulud-npm-supply-chain-attack-explained)）。
- **开发环节的经典教训**：XZ Utils 后门（CVE-2024-3094）暴露了维护者倦怠被社工利用、以及恶意代码从未提交进 git、只存在于发布 tarball 的结构性盲区；Andres Freund 因 SSH 登录慢约 500ms 与异常 CPU 占用而发现异常（[The XZ Utils Backdoor: How a Supply Chain Attack Hid Outside Git](https://manuelfedele.github.io/it/posts/xz-utils-backdoor-the-git-tarball-gap/)）。相关研究对其攻击路径与缓解技术进行了系统梳理（[On the critical path to implant backdoors... Early learnings from XZ](https://arxiv.org/pdf/2404.08987v1)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **SLSA**（[slsa.dev](https://slsa.dev/)）：供应链安全规范与等级体系，可映射到 NIST SSDF（[About SLSA](https://slsa.dev/spec/v1.1/about)）。
- **OpenSSF / Alpha-Omega**（[openssf.org](https://openssf.org/tag/linux-foundation/)）：OpenSSF 提供 Scorecard 等工具，Alpha-Omega 资助关键开源项目。
- **Sigstore**（[blog.sigstore.dev](https://blog.sigstore.dev/)）：Cosign、Fulcio、Rekor，被 npm、PyPI、Homebrew、GitHub Artifact Attestations 使用（[Sigstore 项目概况](https://rywalker.com/research/sigstore)）。
- **检测与响应厂商**：Socket、StepSecurity、Aikido、Wiz 在 Shai-Hulud 事件中提供 IOC 与清单（[The Shai-Hulud npm Supply Chain Attack Explained](https://safeguard.sh/resources/blog/the-shai-hulud-npm-supply-chain-attack-explained)）；Safeguard 等提供 SBOM 生成、可达性分析与自动修复 PR（同上）。

## 关键数据与评测结果（附来源）

| 数据 | 数值 | 来源 |
| --- | --- | --- |
| Shai-Hulud 受影响包版本 | 500+ | [Safeguard](https://safeguard.sh/resources/blog/the-shai-hulud-npm-supply-chain-attack-explained) |
| 蠕虫扩散时间 | 约 48–72 小时 | 同上 |
| 个案 CVSS | 9.0–9.8（Critical） | 同上 |
| CRA 报告义务适用 | 2026 年 9 月 | [CRA FAQ](https://www.cyberresilienceact.eu/ja/faq.html) |
| CRA 大部分义务适用 | 2027-12-11 | 同上 |
| OpenSSF/Alpha-Omega 新增资助 | 1250 万美元（2026-03-17） | [OpenSSF](https://openssf.org/tag/google/) |
| Alpha-Omega 累计投入 | 约 1400 万美元（2022 年起） | [OpenSSF Scorecard](https://openssf.org/tag/scorecard/) |

## 趋势与争议

- **框架的边界**：SLSA 明确不覆盖代码质量、生产者主观恶意，以及"产物与其传递依赖"的单一等级——递归评估依赖是消费方自己的责任（[About SLSA](https://slsa.dev/spec/v1.1/about)）。Mini Shai-Hulud 进一步说明：若构建平台本身被攻陷，attestation 虽真实却不可信，必须依赖平台隔离保证（[SLSA Blog](https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do)）。
- **合规与成本**：CRA 未强制 SBOM 格式，实践上集中在 SPDX/CycloneDX，并建议 SBOM 只涵盖包与依赖元数据，避免把密钥与个人数据写入其中（[Docker](https://www.docker.com/blog/eu-cyber-resilience-act-overview/)）。
- **检测口径的错配**：恶意发布不进入 CVE/KEV 体系，EPSS 也无法刻画"你已信任的包被其维护者账号替换"的概率，促使组织把 SBOM 生成、可达性分析与发布行为异常监测纳入常态化流程（[Safeguard](https://safeguard.sh/resources/blog/the-shai-hulud-npm-supply-chain-attack-explained)）。
- **护栏 vs 可用性**：禁用生命周期脚本、固定版本、keyless 签名都会带来"破坏合法构建脚本"或"迁移工作量"的取舍，需要在 CI 中配套白名单与准入控制（[Supply Chain Security 2026](https://dev.to/saaro_net/supply-chain-security-2026-sbom-sigstoreslsa-and-admission-control-as-devops-standard-3lbl)）。

## 参考来源

- [About SLSA（slsa.dev）](https://slsa.dev/spec/v1.1/about)
- [SLSA specification v1.1](https://slsa.dev/spec/v1.1/)
- [SLSA Build Track（v1.1-rc1 页面）](https://slsa.dev/spec/v1.1-rc1/zonepage)
- [SLSA • Supply-chain Levels for Software Artifacts](https://slsa.dev/)
- [Mini Shai-Hulud: Where SLSA's Boundaries Fall](https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do)
- [Supply Chain Attacks in 2025/2026: What Happened and How to Prevent It](https://www.softscheck.com/en/blog/supply-chain-attacks/)
- [The Shai-Hulud npm Supply Chain Attack Explained](https://safeguard.sh/resources/blog/the-shai-hulud-npm-supply-chain-attack-explained)
- [EU Cyber Resilience Act: Overview, Requirements, and Timelines（Docker）](https://www.docker.com/blog/eu-cyber-resilience-act-overview/)
- [CRA guide for software developers](https://www.cyberresilienceact.eu/guide-software.html)
- [Cyber Resilience Act FAQ（时间表）](https://www.cyberresilienceact.eu/ja/faq.html)
- [ETSI: On 13 August 2026, ETSI Opened the Public Enquiry on 17 Draft CRA Product Standards](https://www.cyberresilienceact.eu/news/etsi-17-cra-product-standards-public-enquiry-13-august-2026.html)
- [2026 Minimum Elements for a Software Bill of Materials (SBOM)（ACSC）](https://www.cyber.gov.au/business-government/supplier-cyber-risk-management/managing-cyber-supply-chains/2026-minimum-elements-for-a-software-bill-of-materials)
- [SBOM et OBOM : comment générer des inventaires logiciels pertinents（OSSIR）](https://www.ossir.org/paris/supports/2026/JSSI/CoreUpdate-JSSI2026-SBOM.pdf)
- [Sigstore Blog](https://blog.sigstore.dev/)
- [Image Signing with Cosign and Sigstore](https://safeguard.sh/resources/blog/image-signing-with-cosign-sigstore)
- [Sigstore 项目概况（rywalker.com）](https://rywalker.com/research/sigstore)
- [Supply Chain Security 2026: SBOM, Sigstore/SLSA, and Admission Control as DevOps Standard](https://dev.to/saaro_net/supply-chain-security-2026-sbom-sigstoreslsa-and-admission-control-as-devops-standard-3lbl)
- [Supply Chain Vulnerabilities（Microsoft Learn, AI attack techniques）](https://learn.microsoft.com/pl-pl/security/zero-trust/catalog-ai-attack-techniques/supply-chain-vulnerabilities)
- [The XZ Utils Backdoor: How a Supply Chain Attack Hid Outside Git](https://manuelfedele.github.io/it/posts/xz-utils-backdoor-the-git-tarball-gap/)
- [On the critical path to implant backdoors... Early learnings from XZ（arXiv）](https://arxiv.org/pdf/2404.08987v1)
- [OpenSSF：Linux Foundation 1250 万美元资助](https://openssf.org/tag/google/)
- [OpenSSF：Alpha-Omega 与 Scorecard](https://openssf.org/tag/scorecard/)
- [MITRE ATT&CK Updates - August 2026](https://attack.mitre.org/resources/updates/)