# 密码学与后量子迁移

> 最后更新：2026-09-26 ｜ 领域：安全 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

密码学为保密性、完整性与身份认证提供数学基础。2025–2026 年的核心叙事是「后量子迁移（PQC Migration）」从标准制定转向工程落地：NIST 已发布首批 PQC 标准并选定第五个算法，TLS 1.3 的混合密钥交换开始规模化部署，而中国商用密码体系（国密 SM 系列）也在推进标准更新与抗量子改造。

## 最新进展（2025–2026）

### NIST PQC 标准进展

NIST 明确：FIPS 203、FIPS 204 与 FIPS 205 于 2024 年 8 月 13 日发布，分别源自 CRYSTALS-Kyber、CRYSTALS-Dilithium 与 SPHINCS⁺；FALCON 亦被选中，将随后以 FIPS 形式发布；HQC 于 2025 年 3 月 11 日被选定进入标准化（[Post-Quantum Cryptography PQC — NIST CSRC](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization)）。

- **FIPS 203（ML-KEM）**：基于模格的密钥封装机制，源自 CRYSTALS-Kyber，用于通用加密。
- **FIPS 204（ML-DSA）**：基于模格的数字签名，源自 CRYSTALS-Dilithium。
- **FIPS 205（SLH-DSA）**：基于哈希的无状态签名，源自 SPHINCS⁺。
- **FALCON（FN-DSA）**：另一被选中的签名方案，待发布。
- **HQC**：被选定为第五个算法，将作为 ML-KEM 的备份，用于通用加密。NIST 数学家 Dustin Moody 表示，ML-KEM 仍将是通用加密的推荐选择，各组织应继续向已发布标准迁移（[NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption)）。

第四轮标准化状态报告（IR 8545）梳理了评估与筛选过程，确认 HQC 是唯一将被标准化的密钥建立类算法，NIST 将基于 HQC 制定标准以补充并多样化其密钥建立组合（[Status Report on the Fourth Round of the NIST Post-Quantum Cryptography Standardization Process](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=959556)）。同期，NIST 于 2025 年 1 月发布 KEM 指南 SP 800-227 草案征求意见。

### TLS 1.3 的混合密钥交换

IETF 草案 draft-ietf-tls-ecdhe-mlkem 定义了 TLS 1.3 的三种混合密钥协商机制——X25519MLKEM768、SecP256r1MLKEM768 与 SecP384r1MLKEM1024——将后量子 ML-KEM 与 ECDHE（椭圆曲线 Diffie-Hellman 临时密钥交换）组合（[Post-quantum hybrid ECDHE-MLKEM Key Agreement for TLSv1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/)）。混合方案的工程价值在于：即使 PQC 算法后来被证明存在缺陷，经典 ECDHE 仍提供兜底安全性。

部署侧，Cloudflare 在其边缘到源站的 TLS 连接上同时支持后量子密钥协商（X25519MLKEM768）与后量子签名（ML-DSA，通过 Authenticated Origin Pulls 与 Custom Origin Trust Store）（[Post-quantum between Cloudflare and origin servers](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-to-origin/)）。另有分析称，ANSSI 于 2026 年 2 月发布了关于在 TLS 1.3 握手中用 ML-KEM 替换 RSA/ECDH 密钥交换的实操指南，且 Cloudflare 端到端 PQC 加密流量占比已达约 52%（[ML-KEM vs RSA/ECDH: TLS 1.3 Post-Quantique à 52% [2026]](https://shattered.io/fr/ml-kem-vs-rsa-ecdh-tls-1-3-2026/)）。工程实践的建议是：将证书与代码签名同密钥交换解耦，避免 ML-KEM 推广连带成 ML-DSA 证书计划，并按客户端版本与依赖跟踪 TLS 错误率（[Post-quantum TLS is a platform migration, not a crypto project](https://dev.to/pvgomes/post-quantum-tls-is-a-platform-migration-not-a-crypto-project-1iek)）。

### 中国商用密码标准更新

国家密码管理局公告（第 54 号）列出的 2025 年标准中包含 SM9 标识密码算法的多项更新：GM/T 0044.2-2025（数字签名算法）、GM/T 0044.3-2025（密钥交换协议）、GM/T 0044.4-2025（密钥封装机制和公钥加密算法）等（[国家密码管理局公告（第54号）](http://sca.gov.cn/sca/xwdt/2026-01/05/content_1061311.shtml)）。基础算法标准方面，GM/T 0002 定义 SM4 分组密码算法，GM/T 0003.1 定义 SM2 椭圆曲线公钥密码算法总则，均由 2012 年发布实施（[标准规范查询 — 国家商用密码管理办公室](https://www.sca.gov.cn/app-zxfw/zxfw/bzgfcx.jsp)）。

抗量子方向的研究提出「经典国密算法 + 后量子密码算法」双重加密机制，并预置基于格的 SM2 抗量子扩展算法、部署量子随机数发生器作为系统随机源（[基于服务器密码机数据加密保护的国密算法升级改造方案研究](https://xxjlclzzs.com/public/uploads/20250928/5dc7d0f4d1aa470415dd1c1e4a86b2ce.pdf)）。

## 核心技术与关键概念

- **对称密码**：AES（含 AES-GCM/CCM 模式）、ChaCha20-Poly1305；国密体系对应 SM4。
- **非对称密码**：RSA、ECDSA/EdDSA、ECDH；国密体系对应 SM2（密钥交换与公钥加密）、SM9（标识密码）。
- **哈希**：SHA-2、SHA-3；国密对应 SM3。
- **TLS 1.3**：简化握手、前向保密（ECDHE）、强制 AEAD 加密，是后量子混合密钥交换的主要落点。
- **PQC 方案族**：格基（ML-KEM、ML-DSA、FALCON）、哈希基（SLH-DSA）、编码基（HQC）。
- **密钥管理（KMS/HSM）**：密钥生成、轮换、托管与生命周期治理，是 PQC 迁移中改动量最大的环节之一。
- **PQC 风险评估**：识别长期保密数据、性能敏感链路与依赖库，制定优先级迁移路线。

对 ML-KEM 在 TLS 1.3 中部署的技术风险（含混合与独立模式、实现指引）也有专门讨论草案（[draft-usama-tls-risks-of-mlkem-04](https://www.ietf.org/archive/id/draft-usama-tls-risks-of-mlkem-04.txt)）。

## 代表性组织 / 标准 / 产品

- **NIST**：PQC 标准化与 FIPS 系列（[NIST CSRC PQC](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization)）。
- **IETF TLS 工作组**：混合密钥交换草案（[draft-ietf-tls-ecdhe-mlkem](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/)）。
- **Cloudflare**：在边缘与源站间部署 PQC 密钥协商与签名（[Cloudflare PQC to origin](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-to-origin/)）。
- **国家密码管理局 / 商用密码管理办公室**：SM 系列算法标准与更新（[公告第54号](http://sca.gov.cn/sca/xwdt/2026-01/05/content_1061311.shtml)）。

## 关键数据与评测结果

| 指标 | 数值 / 事实 | 来源 |
| --- | --- | --- |
| FIPS 203/204/205 发布日期 | 2024-08-13 | [NIST](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization) |
| HQC 选定日期 | 2025-03-11 | [NIST](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption) |
| TLS 1.3 混合密钥协商方案 | X25519MLKEM768、SecP256r1MLKEM768、SecP384r1MLKEM1024 | [IETF](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/) |
| Cloudflare 端到端 PQC 加密流量占比 | 约 52% | [Shattered](https://shattered.io/fr/ml-kem-vs-rsa-ecdh-tls-1-3-2026/) |
| SM9 标准更新编号 | GM/T 0044.2/3/4-2025 | [国家密码管理局](http://sca.gov.cn/sca/xwdt/2026-01/05/content_1061311.shtml) |

## 趋势与争议

- **迁移时间表之争**：是否存在「先收集、后解密（HNDL）」的现实紧迫性，各机构给出的时间点不一；主流共识是先迁移密钥交换（防 HNDL），再迁移签名。
- **混合 vs 纯 PQC**：混合方案提升兼容性与安全性冗余，但增加握手体积与性能开销；纯 PQC 效率更高但缺乏兜底，业界尚未完全一致。
- **国密与 PQC 的融合**：中国路径强调在保留 SM 体系的前提下叠加抗量子能力（双重加密、格基 SM2 扩展），与 NIST 体系并存且口径不同。
- **工程复杂度**：PQC 迁移不是单纯的密码项目，而涉及证书、HSM、固件与全链路依赖的平台级改造，常被低估。

## 参考来源

1. [Post-Quantum Cryptography PQC — NIST CSRC](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization)
2. [NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption — NIST](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption)
3. [NIST PQC: The Road Ahead (March 2025) — NIST CSRC](https://csrc.nist.gov/csrc/media/Presentations/2025/nist-pqc-the-road-ahead/images-media/rwcpqc-march2025-moody.pdf)
4. [Status Report on the Fourth Round of the NIST Post-Quantum Cryptography Standardization Process — NIST](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=959556)
5. [Post-quantum hybrid ECDHE-MLKEM Key Agreement for TLSv1.3 — IETF](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/)
6. [draft-usama-tls-risks-of-mlkem-04 — IETF](https://www.ietf.org/archive/id/draft-usama-tls-risks-of-mlkem-04.txt)
7. [Post-quantum between Cloudflare and origin servers — Cloudflare](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-to-origin/)
8. [ML-KEM vs RSA/ECDH: TLS 1.3 Post-Quantique à 52% [2026] — Shattered](https://shattered.io/fr/ml-kem-vs-rsa-ecdh-tls-1-3-2026/)
9. [Post-quantum TLS is a platform migration, not a crypto project — DEV Community](https://dev.to/pvgomes/post-quantum-tls-is-a-platform-migration-not-a-crypto-project-1iek)
10. [国家密码管理局公告（第54号）](http://sca.gov.cn/sca/xwdt/2026-01/05/content_1061311.shtml)
11. [标准规范查询 — 国家商用密码管理办公室](https://www.sca.gov.cn/app-zxfw/zxfw/bzgfcx.jsp)
12. [基于服务器密码机数据加密保护的国密算法升级改造方案研究](https://xxjlclzzs.com/public/uploads/20250928/5dc7d0f4d1aa470415dd1c1e4a86b2ce.pdf)