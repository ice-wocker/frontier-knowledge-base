# 开源许可与治理（Open Source Licensing and Governance）

> 最后更新：2026-09-26 ｜ 领域：软件 · 开源治理与法律合规 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

开源许可与治理研究的是三组相互纠缠的问题：代码以何种法律许可发布（许可证类型与兼容性）、项目由谁决策与维护（基金会、公司或社区治理）、以及使用方如何履行义务并控制风险（合规、SBOM、审计）。2025–2026 年，这一领域新增了两条主线：**AI 与开源的边界之争**（“开放权重是否等于开源”“用开源代码训练模型是否传播许可证义务”），以及**许可证“再开放化”与合规压力上升**。

## 最新进展（2025–2026）

**1. 许可证“回摆”：从 source-available 回到 OSI 认可的开源。** Redis 于 2024 年 3 月起在 Redis 7.4 及后续版本上改用 Redis Source Available License v2（RSALv2）与 SSPLv1 双许可，放弃此前的 BSD-3（[Redis Adopts Dual Source-Available Licensing](https://redis.io/blog/redis-adopts-dual-source-available-licensing/)）；随后 Redis 宣布自 Redis 8 起新增 OSI 认可的 AGPLv3 作为许可选项，使产品同时以 source-available 与 OSI 合规开源两种形态提供（[Redis is now available under the AGPLv3 open source license](https://redis.io/blog/agplv3/)、[Redis Licenses](https://redis.io/legal/licenses/)）。与之相对，HashiCorp 早在 2023 年即把产品许可从 Mozilla Public License v2.0（MPL 2.0）改为 Business Source License（BSL/BUSL）v1.1，API、SDK 与多数库仍保留 MPL 2.0（[HashiCorp adopts Business Source License](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license)）。

**2. “开放权重 ≠ 开源”成为公开争议。** 开源促进会（OSI）于 2024 年 10 月 28 日发布 **Open Source AI Definition（OSAID）1.0**，要求授予使用、研究、修改、分享四项自由，并公开数据信息、完整训练与运行代码，以及以合规条款提供模型参数（[Open-source AI (AI Wiki)](https://aiwiki.ai/wiki/open_source_ai)、[OSAID FAQ](https://opensource.org/ai/faq)）。由于 OSAID 未强制规定具体法律机制，围绕“开放权重（open weights）”是否等同于开源的争论持续发酵；2026 年 9 月媒体以《Open weights are not open source: Why AI's favorite label is under dispute》为题讨论该分歧（[OSI Press mentions](https://opensource.org/press-mentions)）。批评者认为，以 Llama 为代表的模型常被称为“开源”但不符合 OSI 定义（[The Open Source AI Lie](https://blog.serendeep.tech/blog/the-open-source-ai-lie)）。

**3. AI 训练与开源许可证的司法检验。** 历时较久的 GitHub Copilot 集体诉讼在 2026 年出现关键裁决：美国第九巡回法院就 Doe v. GitHub, Inc., No. 24-7700 作出判决（2026 年 9 月 16 日），被视为 AI 训练类案件中被告方的重要胜利（[Copyleft Currents](https://heathermeeker.com/)）。但“训练数据违反开源许可”与“许可证是否传播到模型”仍是被争议的问题，原告仍可继续就 Copilot 未经许可标注而复制他人代码的行为寻求禁令（[The Current State of the Theory that GPL Propagates to AI Models](https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/)）。中国司法层面，最高人民法院知识产权法庭在（2021）最高法知民终51号案中确立：开发者自身是否违反 GPLv2 与其对第三方是否享有著作权是两个独立问题，违反许可证产生的权利瑕疵不阻却对第三方侵权的救济（[数字法治｜人工智能时代开源治理的法律回应（上）](https://ipc.court.gov.cn/zh-cn/news/view-5767.html)）。

**4. 开源安全资金与治理投入上升。** Linux Foundation 宣布向 Alpha-Omega 与 OpenSSF 管理的一笔 1250 万美元集体投资，出资方包括 Anthropic、AWS、Google、Google DeepMind、GitHub、Microsoft 与 OpenAI，目标是增强开源生态的安全性、韧性与长期可持续性（[Linux Foundation（OpenSSF）](https://openssf.org/tag/linux-foundation/)）。据 OpenSSF 2025 年报，其技术顾问委员会（TAC）向 14 个 Technical Initiatives 拨款 663,248 美元（[OpenSSF 2025 Annual Report](https://openssf.org/wp-content/uploads/2025/12/2025_Annual_Report_1208.pdf)）。

## 核心技术与关键概念

- **许可证类型**：宽松型（MIT、Apache-2.0、BSD、MPL-2.0）与著佐权型（copyleft，如 GPLv2/v3、LGPL、AGPLv3）；此外是 source-available 类（BSL/BUSL、SSPL、RSALv2），后者并非 OSI 认可的开源许可。
- **兼容性**：GPLv2 与 GPLv3 不自动兼容，“GPL v2 only”代码不能与“GPL v3 or later”代码合并，否则可能违反其中一个或两个许可；不同许可证的署名要求也可能互相冲突（[2026 Open Source Security and Risk Analysis Report](https://www.blackduck.com/content/dam/black-duck/en-us/reports/rep-ossra.pdf)）。
- **SBOM**：软件物料清单是产品所含全部组件（含开源库、版本、许可证与已知漏洞）的机器可读清单；美国自 2021 年 5 月第 14028 号行政令起推动，NIST 与 NTIA 形成了 SBOM 最小元素规范（[License and Regulatory Risk in Open Source Components](https://safeguard.sh/resources/blog/license-and-regulatory-risk-in-open-source-components)）。
- **SPDX**：由 Linux Foundation 维护，2021 年被 ISO/IEC 5962 正式认可，擅长以机器可读形式表达复杂许可证表达式，用于合规、来源追溯与供应链风险分析（[OpenSSF October 2025](https://openssf.org/2025/10/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **OSI（Open Source Initiative）**：自 1998 年起维护开源定义，2024 年发布 OSAID 1.0（[opensource.org/ai/faq](https://opensource.org/ai/faq)）。
- **Linux Foundation 生态**：OpenSSF（开源安全）、Alpha-Omega、SPDX 等，承担资金归集与标准治理职能（[openssf.org](https://openssf.org/tag/linux-foundation/)）。
- **Redis / HashiCorp**：source-available 与再开放化两种路径的代表（[redis.io/legal/licenses](https://redis.io/legal/licenses/)、[hashicorp.com](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license)）。
- **Nous Research**：其开源 AI 智能体 Hermes 于 2026 年 7 月以至少 7500 万美元、15 亿美元估值完成融资，被视为开源 AI 项目的商业化案例（[Nous Research Raises $75M+ at $1.5B](https://valueaddvc.com/blog/nous-research-75m-1-5b-valuation-hermes-open-source-ai-agent-july-2026)）。

## 关键数据与评测结果（附来源）

| 事实 | 数据 | 来源 |
| --- | --- | --- |
| OSAID 1.0 发布时间 | 2024 年 10 月 28 日 | [AI Wiki](https://aiwiki.ai/wiki/open_source_ai) |
| Redis 8 起许可选项 | RSALv2 / SSPLv1 / AGPLv3 | [Redis Licenses](https://redis.io/legal/licenses/) |
| SPDX 国际标准 | ISO/IEC 5962:2021 | [OpenSSF](https://openssf.org/2025/10/) |
| OpenSSF 2025 技术倡议拨款 | 663,248 美元 / 14 个项目 | [OpenSSF 2025 Annual Report](https://openssf.org/wp-content/uploads/2025/12/2025_Annual_Report_1208.pdf) |
| AI 开源安全集体投资 | 1250 万美元 | [OpenSSF](https://openssf.org/tag/linux-foundation/) |

## 趋势与争议

**趋势：** 一是数字主权与合规要求推动 SBOM 与许可证扫描成为企业采购的常规门槛（[Open Source Compliance for Corporate Teams 2026](https://ossalt.com/guides/open-source-compliance-corporate-guide-2026)）；二是商业化模式集中于“open core（免费基础版 + 付费企业特性）”与“双许可（AGPL + 商业许可）”两类（[Open Source Funding Models & Sustainability 2026](https://ossalt.com/guides/open-source-funding-models-sustainability-2026)）；三是基金会支持提供基础设施与合法性，但很少直接补偿维护者（同上）。

**争议：** 其一，许可模式的正当性之争——source-available 是否“背叛开源”与企业是否应为上游付费，长期无共识。其二，AI 与开源的边界：OSAID 未规定法律机制，导致“开放权重”被广泛误用；训练数据与模型之间是否会“传播”许可证义务仍待司法明确。其三，合规风险的量级存在不同口径：有来源称 GPL 执法行动自 2022 年以来增加 220%（[Legal and Licensing Guide for Open-Source LLMs in 2026](https://ehga.org/legal-and-licensing-guide-for-open-source-llms-in)），该数字出自商业机构而非官方统计，应谨慎引用。其四，AI 生成代码的许可证来源不清，进一步放大了“什么是产品中真正包含的代码”这一治理难题（[The GPL Trap](https://blog.promise.legal/gpl-trap-open-source-license-compliance-startup/)）。

## 参考来源

- [Redis Licenses](https://redis.io/legal/licenses/)
- [Redis is now available under the AGPLv3 open source license](https://redis.io/blog/agplv3/)
- [Redis Adopts Dual Source-Available Licensing](https://redis.io/blog/redis-adopts-dual-source-available-licensing/)
- [HashiCorp adopts Business Source License](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license)
- [HashiCorp Licensing FAQ](https://www.hashicorp.com/fr/license-faq)
- [OSAID FAQ (Open Source Initiative)](https://opensource.org/ai/faq)
- [OSI Press mentions](https://opensource.org/press-mentions)
- [Open-source AI (AI Wiki)](https://aiwiki.ai/wiki/open_source_ai)
- [The Open Source AI Lie](https://blog.serendeep.tech/blog/the-open-source-ai-lie)
- [The Current State of the Theory that GPL Propagates to AI Models Trained on GPL Code](https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/)
- [Copyleft Currents (Heather Meeker)](https://heathermeeker.com/)
- [数字法治｜人工智能时代开源治理的法律回应（上）](https://ipc.court.gov.cn/zh-cn/news/view-5767.html)
- [2026 Open Source Security and Risk Analysis Report (Black Duck)](https://www.blackduck.com/content/dam/black-duck/en-us/reports/rep-ossra.pdf)
- [License and Regulatory Risk in Open Source Components](https://safeguard.sh/resources/blog/license-and-regulatory-risk-in-open-source-components)
- [Open Source Compliance for Corporate Teams 2026](https://ossalt.com/guides/open-source-compliance-corporate-guide-2026)
- [OpenSSF — Linux Foundation](https://openssf.org/tag/linux-foundation/)
- [OpenSSF October 2025](https://openssf.org/2025/10/)
- [OpenSSF 2025 Annual Report](https://openssf.org/wp-content/uploads/2025/12/2025_Annual_Report_1208.pdf)
- [Linux Foundation Annual Report 2025](https://www.linuxfoundation.org/hubfs/Publications/2025%20Linux%20Foundation%20Annual%20Report_121825a_lr.pdf)
- [Open Source Funding Models & Sustainability 2026](https://ossalt.com/guides/open-source-funding-models-sustainability-2026)
- [The GPL Trap](https://blog.promise.legal/gpl-trap-open-source-license-compliance-startup/)
- [Legal and Licensing Guide for Open-Source LLMs in 2026](https://ehga.org/legal-and-licensing-guide-for-open-source-llms-in)
- [Nous Research Raises $75M+ at $1.5B](https://valueaddvc.com/blog/nous-research-75m-1-5b-valuation-hermes-open-source-ai-agent-july-2026)