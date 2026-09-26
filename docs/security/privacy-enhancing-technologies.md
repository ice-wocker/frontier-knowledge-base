# 隐私增强技术（PETs）

> 最后更新：2026-09-26 ｜ 领域：安全 · 隐私保护与密码学应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

隐私增强技术（Privacy-Enhancing Technologies, PETs）指在保留数据可用价值的前提下，降低个人数据暴露面的一类技术集合，通常包括差分隐私（Differential Privacy, DP）、联邦学习（Federated Learning, FL）、同态加密（Homomorphic Encryption, HE）、安全多方计算（Secure Multi-Party Computation, SMPC）、可信执行环境（TEE）以及私有集合求交（Private Set Intersection, PSI）等。这些技术既可单独使用，也常被组合进数据洁净室（Data Clean Room）中：洁净室通常配套阈值抑制（如导出要求 k≥50）、私有集合运算与安全多方计算，用于跨方受众扩展、抑制与私密归因/增效实验（[Data Clean Rooms, Smarter AI, Safer Growth](https://petronellatech.com/blog/data-clean-rooms-smarter-ai-safer-growth/)）。

差分隐私的核心价值在于：即使攻击者掌握辅助信息，其形式化保证依然成立，从而克服传统匿名化的根本局限（[Differential Privacy 2026: How Enterprise Data Science Is Adopting Mathematical Privacy Guarantees](https://www.programming-helper.com/tech/differential-privacy-2026-enterprise-data-science-ai)）。

## 最新进展（2025–2026）

**同态加密走向可用。** Google 推出开源的 HEIR（Homomorphic Encryption Intermediate Representation）编译器工具链，可以把在明文上运行的预训练 AI 模型转换为在加密输入上运行；其愿景是让非密码学专家也能"一键"把加密推理用于生产（[How Google is Making Private AI Practical with Homomorphic Encryption](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/)）。HEIR 是一个基于 MLIR、以 Apache 2.0 许可开源的编译器，可把预训练模型转换为 FHE 模型，使服务器在密文上推理、永远看不到明文结果（[Google Just Open-Sourced the Compiler for Encrypted AI](https://reptile.haus/journal/homomorphic-encryption-private-ai-heir-business-guide-2026/)）。代价仍然显著：FHE 比明文慢约 1,000 倍，ML 推理甚至可能落后五个数量级，因此更适配欺诈评分、合规、推荐等批处理场景，而非交互式推理（[Google Just Made AI on Encrypted Data Practical](https://lindleylabs.com/blog/google-just-made-ai-on-encrypted-data-practical)；[reptile.haus](https://reptile.haus/journal/homomorphic-encryption-private-ai-heir-business-guide-2026/)）。同期研究显示，自动化算法搜索（如将 AlphaEvolve 用于 TPU 上的 FHE 优化）在 24 小时内发现实现级优化，使 TFHE bootstrap 延迟降低 2.5 倍，CKKS 的旋转与乘法延迟分别降低 1.31 倍与 1.18 倍（[Adapting AlphaEvolve to Optimize Fully Homomorphic Encryption on TPUs（arXiv）](https://arxiv.org/html/2605.14718)）。

**联邦学习与差分隐私、安全聚合深度结合。** 2026 年的研究主线是把 LDP 与安全聚合（如全阈值加法秘密共享）联合使用：DDP-SA 提出客户端本地差分隐私加秘密共享的两阶段保护，兼顾端到端隐私与可计算性（[DDP-SA（arXiv）](https://arxiv.org/html/2604.07125v1)）。针对梯度泄露的 Joint-DP-FL 结合邻域差分隐私、梯度裁剪与高斯噪声注入，在多个模型和图像数据集上降低了代表性梯度泄露攻击的成功率（[Privacy-Preserving Against Gradients Leakage Attacks via Joint Differential Privacy in Federated Learning](https://xplorestaging.ieee.org/document/11456084)）。噪声累积是 DP-FL 的核心难题：FedDecouple 通过"阶段解耦"让客户端只上传干净梯度、由两台辅助服务器处理加噪，以缓解聚合时的方差累积（[FedDecouple（MDPI）](https://www.mdpi.com/2227-7390/14/17/3086)）。面向量子威胁，ZKFL-PQ 提出三层协议，混合 ML-KEM（FIPS 203）等后量子组件以应对"先收集后解密"（HNDL）风险（[Zero-Knowledge Federated Learning with Lattice-Based Hybrid Encryption（arXiv）](https://arxiv.org/html/2603.03398)）。

**差分隐私已大规模落地，但实现质量受质疑。** 美国人口普查局在 2020 年人口普查中采用差分隐私，是史上最大规模的 DP 部署（[Differential Privacy 2026](https://www.programming-helper.com/tech/differential-privacy-2026-enterprise-data-science-ai)），其动因是数据库重建攻击——研究证明发布精细普查表可近乎还原个体记录（[Differential Privacy Is the Only Mathematically Honest Answer to Data Anonymization](https://www.aioapex.com/en/blog/differential-privacy-apple-google-census-guide-2026)）。Google 则称其差分隐私部署覆盖过去一年近 30 亿台设备，是"已知全球最大的差分隐私应用"（[Sharing our latest differential privacy milestones and advancements](https://googledevelopers.blogspot.com.au/en/sharing-our-latest-differential-privacy-milestones-and-advancements/)）。与此同时，一篇对 Apple `DifferentialPrivacy.framework` 的审计论文指出：所有依赖浮点噪声的算法都未达到其声称的 DP 与零知识证明保证，原因是使用了自 2012 年起已知存在浮点漏洞的不安全噪声生成器；此外框架中的 SecAgg 协议被配置为关闭本地 DP，导致数据在上传时没有任何本地 DP 保护，审计在 9 个算法中的 5 个发现了 DP 违规证据（[Auditing Apple's DifferentialPrivacy.framework（arXiv）](https://arxiv.org/html/2605.21378v2)）。

**PSI 成为最实用、部署最广的 PET 之一。** Apple 用 PSI 把广告主客户名单与 Apple 用户做匹配以支持广告测量，同时不让 Apple 获知广告主名单、也不让广告主获知 Apple 用户数据；Google 用 PSI 做类似广告归因；英国 NHS 也在疫情期间使用类似协议（[Private Set Intersection: Finding Overlaps Without Sharing Data](https://kindatechnical.com/cryptography/private-set-intersection-finding-overlaps-without-sharing-data.html)）。AWS Clean Rooms 通过执行双方预先约定的分析规则完成交集计算，只提供匹配记录，任何一方都无法访问对方原始数据、无法看到完整用户名单、也无法判断哪些用户未匹配（[Privacy-Enhanced Cross-Media Measurement（AWS）](https://aws.amazon.com/blogs/industries/privacy-enhanced-cross-media-measurement-how-fifty5blue-formerly-kantar-media-leveraged-aws-clean-rooms-to-establish-audit-transparency-during-panel-data-exchange/)）。多标识匹配方面，PrivacyGo 使用反向 OPRF 与盲化密钥轮换支持跨多个标识的安全匹配，并加入差分隐私机制混淆交集规模以缓解成员推断（[PrivacyGo（arXiv）](https://arxiv.org/html/2506.20981v1)）。

**合规环境的推动。** 2026 年 7 月 8 日，EDPB 通过关于匿名化的指南与关于生成式 AI 场景下网络爬取的指南，并采纳了区块链个人数据处理指南的最终版本（[EDPB sheds light on anonymisation and web scraping for generative AI](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en)）。2026 年 4 月 16 日，EDPB 还通过了科研目的个人数据处理指南，并批准首批欧洲数据保护印章（Europrivacy 认证标准）作为传输工具（[EDPB brings clarity to data processing for scientific research](https://www.edpb.europa.eu/news/news/2026/edpb-brings-clarity-data-processing-scientific-research-speeds-finalisation_el)）。欧盟数字综合立法（Digital Omnibus）提案中，EDPB 与 EDPS 在联合意见 2/2026 中支持澄清"科研目的处理构成 GDPR 第 6(1)(f) 条下的合法利益"，同时强调仍须满足该条其他条件（[EDPB-EDPS JOINT OPINION 2/2026](https://www.edpb.europa.eu/system/files/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf)）。

**TEE 与机密计算。** 硬件级机密计算被用于在共享或云环境中保护 AI 工作负载：有报道称 Apple 将使用 Google Cloud 与 NVIDIA 芯片处理 Siri 查询，并启用 NVIDIA 机密计算，官方表述为该能力"可保护部署在 Rubin、Blackwell 和 Hopper GPU 上的 AI 模型的机密性和完整性"，使敏感 AI 负载"即使在共享或云环境中，也能以接近原生性能的方式大规模安全运行"（[消息称苹果将借谷歌云英伟达芯片处理Siri查询](http://m.toutiao.com/group/7647440339338363426/)）。

## 核心技术与关键概念

- **差分隐私与隐私预算**：DP 通过形式化保证约束个体记录对输出的影响；大规模部署需要显式管理隐私预算（如 2020 年普查重新划分数据使用了一定的总预算口径）（[Differential Privacy Is the Only Mathematically Honest Answer](https://www.aioapex.com/en/blog/differential-privacy-apple-google-census-guide-2026)）。
- **联邦学习的三类风险**：梯度反演可重建患者信息、拜占庭客户端可投毒全局模型、HNDL 使今日加密流量面临未来量子威胁（[ZKFL-PQ（arXiv）](https://arxiv.org/html/2603.03398)）。
- **SMPC 的性能特征**：SMPC 在处理较大模型（含卷积网络）时表现良好，但受网络伪影（丢包、传输时间）影响显著，适合近距离网络或高速通道（[A Pragmatic Comparison of Cryptographic Computation Technologies for Machine Learning（arXiv）](https://arxiv.org/html/2605.04858)）；实践中的优化手段包括专用高带宽低延迟链路、批量化密码学运算、以及优先选择线性/逻辑回归等更易高效实现的模型（[Architecting Secure Multi-Party Computation for Privacy-Preserving AI Training](https://www.vroble.com/2026/02/the-unseen-collaboration-architecting.html?m=1)）。
- **PSI 与 OPRF**：PSI 返回交集而不暴露各自集合，是洁净室与广告测量的关键构件（[The Signal Landscape — Deterministic Audience Activation](https://scientiamobile.com/the-signal-landscape-deterministic-audience-activation/)）。
- **匿名化的法律边界**：EDPB 的匿名化指南与科研处理指南界定了"匿名"与"科研目的"在 GDPR 下的判定因素（[EDPB](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en)）；EDPB 为科研目的给出六项关键指示性因素：方法与系统性、遵循伦理标准、可验证与透明、自主与独立、研究目标、以及对既有知识的贡献潜力（[EDPB 新闻汇总](https://www.edpb.europa.eu/feed/news_el)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Google HEIR**（[Google Security Blog](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/)）：开源 FHE 编译器工具链，Apache 2.0。
- **AWS Clean Rooms**（[AWS Blog](https://aws.amazon.com/blogs/industries/privacy-enhanced-cross-media-measurement-how-fifty5blue-formerly-kantar-media-leveraged-aws-clean-rooms-to-establish-audit-transparency-during-panel-data-exchange/)）：以 PSI 与预约定分析规则实现跨方测量。
- **PrivacyGo**（[arXiv](https://arxiv.org/html/2506.20981v1)）：基于反向 OPRF 的多标识私密匹配框架，用于广告测量。
- **Apple DifferentialPrivacy.framework / Google 差分隐私**（[审计论文](https://arxiv.org/html/2605.21378v2)、[Google 官方博客](https://googledevelopers.blogspot.com.au/en/sharing-our-latest-differential-privacy-milestones-and-advancements/)）：大规模端侧 DP 部署代表。
- **NVIDIA 机密计算**（[相关报道](http://m.toutiao.com/group/7647440339338363426/)）：面向 Rubin/Blackwell/Hopper GPU 的 AI 模型机密性与完整性保护。

## 关键数据与评测结果（附来源）

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| FHE 相对明文性能开销 | 约 1,000× 慢 | [Lindley Labs](https://lindleylabs.com/blog/google-just-made-ai-on-encrypted-data-practical) |
| FHE ML 推理开销 | 可达五个数量级 | [reptile.haus](https://reptile.haus/journal/homomorphic-encryption-private-ai-heir-business-guide-2026/) |
| AlphaEvolve 优化 FHE 收益 | TFHE bootstrap 2.5×；CKKS 旋转 1.31×、乘法 1.18× | [arXiv](https://arxiv.org/html/2605.14718) |
| Google DP 部署规模 | 近 30 亿台设备（过去一年） | [Google Developers Blog](https://googledevelopers.blogspot.com.au/en/sharing-our-latest-differential-privacy-milestones-and-advancements/) |
| Apple DP 框架审计结果 | 9 个算法中 5 个发现 DP 违规证据 | [arXiv](https://arxiv.org/html/2605.21378v2) |
| 洁净室导出阈值示例 | k≥50 | [Data Clean Rooms, Smarter AI](https://petronellatech.com/blog/data-clean-rooms-smarter-ai-safer-growth/) |

## 趋势与争议

- **性能与场景的取舍**：FHE 目前仍不适用于交互式推理，价值集中在高价值、可批处理的场景（医疗、金融、行为数据）（[Lindley Labs](https://lindleylabs.com/blog/google-just-made-ai-on-encrypted-data-practical)）；SMPC 则更适合模型较简单但网络条件友好的联盟场景（[arXiv](https://arxiv.org/html/2605.04858)）。
- **实现即攻击面**：Apple DP 框架的审计表明，即使算法设计正确，不安全的噪声生成器与默认关闭的本地 DP 配置也会使合规声明落空（[arXiv](https://arxiv.org/html/2605.21378v2)）。
- **技术组合仍是常态**：单一 PET 难以同时满足隐私、可用性与性能，DDP-SA、Joint-DP-FL、FedDecouple、ZKFL-PQ 等均采用"DP + 安全聚合/密码学"的组合路线（[arXiv 2604.07125](https://arxiv.org/html/2604.07125v1)、[IEEE](https://xplorestaging.ieee.org/document/11456084)、[MDPI](https://www.mdpi.com/2227-7390/14/17/3086)、[arXiv 2603.03398](https://arxiv.org/html/2603.03398)）。
- **合规口径仍在收敛**：匿名化与科研处理的法律边界、以及 TEE 能否作为满足合规义务的手段，仍在指南与个案层面演进（[EDPB](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en)）。

## 参考来源

- [How Google is Making Private AI Practical with Homomorphic Encryption](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/)
- [Google Just Open-Sourced the Compiler for Encrypted AI](https://reptile.haus/journal/homomorphic-encryption-private-ai-heir-business-guide-2026/)
- [Google Just Made AI on Encrypted Data Practical](https://lindleylabs.com/blog/google-just-made-ai-on-encrypted-data-practical)
- [Adapting AlphaEvolve to Optimize Fully Homomorphic Encryption on TPUs（arXiv）](https://arxiv.org/html/2605.14718)
- [Zero-Knowledge Federated Learning with Lattice-Based Hybrid Encryption for Quantum-Resilient Medical AI（arXiv）](https://arxiv.org/html/2603.03398)
- [DDP-SA: Scalable Privacy-Preserving Federated Learning（arXiv）](https://arxiv.org/html/2604.07125v1)
- [Privacy-Preserving Against Gradients Leakage Attacks via Joint Differential Privacy in Federated Learning（IEEE）](https://xplorestaging.ieee.org/document/11456084)
- [FedDecouple: Mitigating Noise Accumulation in Differentially Private Federated Learning（MDPI）](https://www.mdpi.com/2227-7390/14/17/3086)
- [Differential Privacy 2026: How Enterprise Data Science Is Adopting Mathematical Privacy Guarantees](https://www.programming-helper.com/tech/differential-privacy-2026-enterprise-data-science-ai)
- [Differential Privacy Is the Only Mathematically Honest Answer to Data Anonymization](https://www.aioapex.com/en/blog/differential-privacy-apple-google-census-guide-2026)
- [Sharing our latest differential privacy milestones and advancements（Google）](https://googledevelopers.blogspot.com.au/en/sharing-our-latest-differential-privacy-milestones-and-advancements/)
- [Auditing Apple's DifferentialPrivacy.framework（arXiv）](https://arxiv.org/html/2605.21378v2)
- [Secure Multi-Party Computation for 2026 Cybersecurity](https://rasec.app/blog/secure-multi-party-computation-2026-cybersecurity)
- [A Pragmatic Comparison of Cryptographic Computation Technologies for Machine Learning（arXiv）](https://arxiv.org/html/2605.04858)
- [The Unseen Collaboration: Architecting Secure Multi-Party Computation for Privacy-Preserving AI Training](https://www.vroble.com/2026/02/the-unseen-collaboration-architecting.html?m=1)
- [EDPB sheds light on anonymisation and web scraping for generative AI](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en)
- [EDPB brings clarity to data processing for scientific research](https://www.edpb.europa.eu/news/news/2026/edpb-brings-clarity-data-processing-scientific-research-speeds-finalisation_el)
- [EDPB-EDPS JOINT OPINION 2/2026（Digital Omnibus）](https://www.edpb.europa.eu/system/files/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf)
- [EDPB News（六项科研指示性因素）](https://www.edpb.europa.eu/feed/news_el)
- [Privacy-Enhanced Cross-Media Measurement（AWS Blog）](https://aws.amazon.com/blogs/industries/privacy-enhanced-cross-media-measurement-how-fifty5blue-formerly-kantar-media-leveraged-aws-clean-rooms-to-establish-audit-transparency-during-panel-data-exchange/)
- [PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection（arXiv）](https://arxiv.org/html/2506.20981v1)
- [Private Set Intersection: Finding Overlaps Without Sharing Data](https://kindatechnical.com/cryptography/private-set-intersection-finding-overlaps-without-sharing-data.html)
- [The Signal Landscape — Deterministic Audience Activation](https://scientiamobile.com/the-signal-landscape-deterministic-audience-activation/)
- [Data Clean Rooms, Smarter AI, Safer Growth](https://petronellatech.com/blog/data-clean-rooms-smarter-ai-safer-growth/)
- [消息称苹果将借谷歌云英伟达芯片处理 Siri 查询](http://m.toutiao.com/group/7647440339338363426/)