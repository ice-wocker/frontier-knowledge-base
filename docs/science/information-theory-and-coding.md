# 信息论与编码

> 最后更新：2026-09-26 ｜ 领域：科学·信息论与编码 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

信息论研究信息度量、压缩与传输的理论极限；编码理论则构造逼近这些极限的实用方案。Claude Shannon 1948 年的奠基性工作同时提出了信道容量定理与信源编码的保真度准则；后续发展包括 Berger 的率失真变分表述、Wyner–Ziv 对带边信息信源的扩展、Zamir–Feder 的格量化框架，以及 Gallager 的 LDPC 码与 Arıkan 的极化码（[Information-Theoretic Equivalences Across Rate–Distortion, Quantization, and Decoding](https://arxiv.org/html/2512.11279v1/)）。当前该领域的一条主线是从通信向存储与量子计算延伸。

## 最新进展（2025–2026）

**移动通信：5G 延续与 6G 定型。** 3GPP 在 2026 年 6 月的全会上决定 6G 信道编码延续 5G 框架：数据信道保留 LDPC 码、控制信道保留 Polar 码，同时新增第三个 LDPC 基图 BG3，目标是改善高数据率下的解码器面积效率并保持可比性能（[Building the 6G standard: What 3GPP's June 2026 plenary decisions mean for device makers](https://www.qualcomm.com/news/onq/2026/06/6g-standardization-release-21-milestones)）。在 6G 中，Polar 码继续作为控制信道的基础，方向是扩展更大载荷支持并采用分段或两阶段解码，以平衡复杂度、功耗与盲解码效率（[6G Channel Coding](https://www.sharetechnote.com/html/6G/6G_TDoc_ChannelCoding.html)）。5G 侧，ETSI TS 138 212 V16.15.0（2026-02）仍包含 Polar 码的码块分割与编码流程（[ETSI TS 138 212 V16.15.0](https://www.etsi.org/deliver/etsi_ts/138200_138299/138212/16.15.00_60/ts_138212v161500p.pdf)）。面向 5G NR 的 LDPC 与 Polar 码有系统性综述（[Demystifying 5G Polar and LDPC Codes: A Comprehensive Review and Foundations](https://arxiv.org/pdf/2502.11053v2.pdf)），面向 6G 的 LDPC–Polar 混合编码对比研究也在进行（[LDPC–Polar Code Comparison under 5G NR: Toward Hybrid Coding Schemes for 6G](https://www.epj-conferences.org/articles/epjconf/pdf/2026/30/epjconf_iceodis2026_01003.pdf)）。

**面向容错量子计算的纠错码。** 量子 LDPC 码成为降低物理比特开销的主线。Cornucopia 系列码在标准电路级噪声模型下实现超过 1/2 的编码率与超过 0.4% 的伪阈值（[Quantum error correction at ultra-low overhead](https://arxiv.org/html/2608.02773v2)）；面向量子 LDPC 的波束搜索解码器以置信传播为引导，在 [[144,12,12]] 双变量自行车码上做了电路级噪声仿真以估计逻辑错误率（[Beam search decoder for quantum LDPC codes](https://arxiv.org/html/2512.07057v1)）。有评估指出，在面向 6G 量子通信的设定中，量子 LDPC 相较表面码在物理比特资源上更高效（[Performance Evaluation of Error Correction Techniques in 6G Quantum Communication](https://pdfs.semanticscholar.org/c83b/7603999376970eed4544cadb4ed1fac7e988.pdf)）。

**网络编码。** 有工作把随机线性网络编码（RLNC）以前向擦除纠错的形式注入 5G 测试床的 IP 层，作为 ARQ/HARQ 重传机制的替代，并在 gNB 与 UE 之间实测其可靠性影响（[Rethinking Reliability Using Network Coding: a Practical 5G Evaluation](https://arxiv.org/html/2508.10247)）。网络编码还被用于非通信任务，例如浮点求和归约（[Publications, Shenghao Yang](https://shhyang.github.io/publications/)）。

**存储与 DNA。** DNA 数据存储把纠错码与专用编码框架结合：DNA-MGC+ 编解码器在 Illumina 与 Nanopore 测序下于测序深度需求、读取成本、解码时间、存储密度与错误率等多项指标上优于若干代表性编解码方案（[DNA-MGC+: A versatile codec for reliable and resource-efficient data storage on synthetic DNA](https://arxiv.org/html/2603.14527v2)）；也有研究以 LDPC 与喷泉码混合方案保护 10 TB 级数据集（[SAVING THE WORLD IN DNA: RECENT PROGRESS IN DNA STORAGE TECHNOLOGY IN 2026](https://pdfs.semanticscholar.org/d2cf/f3f766f678acac9527ae564af62e061786ed.pdf)）。在材料层面，有研究提出长链异源核酸—环状单链 DNA（XNA-cssDNA）杂合策略提升存储鲁棒性（[Long-stranded XNA-cssDNA hybrids for robust data storage](https://www.science.org/doi/10.1126/sciadv.aed2917)）。

## 核心技术与关键概念

- **香农极限与信道容量**：在噪声信道中可实现无误码传输的最高速率上限；信源编码的率失真函数给出给定失真下的最小速率。
- **容量逼近码**：Turbo 码、LDPC 码（含原型图、空间耦合等变体）与极化码；有综述指出 LDPC 在性能与实现上优于 Turbo 码（[Information Theory and Coding for Future Wireless](https://iccc2025.ieee-icc.org/information-theory-and-coding-future-wireless)）。
- **率失真与量化**：Berger 变分表述、Wyner–Ziv 带边信息编码、格量化；有研究给出率失真、量化与解码之间的信息论等价关系（[Information-Theoretic Equivalences Across Rate–Distortion, Quantization, and Decoding](https://arxiv.org/html/2512.11279v1/)）。
- **网络编码**：中间节点对数据做线性组合后再转发，典型场景为多播与擦除信道。
- **量子纠错**：表面码、量子 LDPC 码与自校正码；阈值定理规定只有物理错误率低于阈值时，增大码距才能指数抑制逻辑错误。
- **识别容量等新方向**：有工作总结了在有色高斯噪声统计下由 Mahalanobis 距离解码器诱导的识别容量界（[Information Theory](https://www.sciencestack.ai/explore/cs.IT)）。

## 趋势与争议

1. **6G 的"演进而非替换"**：延续 LDPC/Polar 并通过新增基图优化，降低了产业迁移成本，但也意味着短码/新场景的性能空间可能受限。
2. **量子 LDPC 的权衡**：高编码率与硬件可实现的连接度、解码复杂度之间存在张力。
3. **纠错码的外溢应用**：从通信扩展到 DNA 存储、网络可靠性与量子计算，编码设计目标由单一误码率转为多指标联合优化。

## 参考来源

- [Information-Theoretic Equivalences Across Rate–Distortion, Quantization, and Decoding](https://arxiv.org/html/2512.11279v1/)
- [Building the 6G standard: What 3GPP's June 2026 plenary decisions mean for device makers（Qualcomm）](https://www.qualcomm.com/news/onq/2026/06/6g-standardization-release-21-milestones)
- [6G Channel Coding（ShareTechnote）](https://www.sharetechnote.com/html/6G/6G_TDoc_ChannelCoding.html)
- [ETSI TS 138 212 V16.15.0（5G NR Multiplexing and channel coding）](https://www.etsi.org/deliver/etsi_ts/138200_138299/138212/16.15.00_60/ts_138212v161500p.pdf)
- [Demystifying 5G Polar and LDPC Codes: A Comprehensive Review and Foundations](https://arxiv.org/pdf/2502.11053v2.pdf)
- [LDPC–Polar Code Comparison under 5G NR: Toward Hybrid Coding Schemes for 6G](https://www.epj-conferences.org/articles/epjconf/pdf/2026/30/epjconf_iceodis2026_01003.pdf)
- [Quantum error correction at ultra-low overhead（Cornucopia codes）](https://arxiv.org/html/2608.02773v2)
- [Beam search decoder for quantum LDPC codes](https://arxiv.org/html/2512.07057v1)
- [Performance Evaluation of Error Correction Techniques in 6G Quantum Communication](https://pdfs.semanticscholar.org/c83b/7603999376970eed4544cadb4ed1fac7e988.pdf)
- [Rethinking Reliability Using Network Coding: a Practical 5G Evaluation](https://arxiv.org/html/2508.10247)
- [Publications, Shenghao Yang（network coding）](https://shhyang.github.io/publications/)
- [DNA-MGC+: A versatile codec for reliable and resource-efficient data storage on synthetic DNA](https://arxiv.org/html/2603.14527v2)
- [SAVING THE WORLD IN DNA: RECENT PROGRESS IN DNA STORAGE TECHNOLOGY IN 2026](https://pdfs.semanticscholar.org/d2cf/f3f766f678acac9527ae564af62e061786ed.pdf)
- [Long-stranded XNA-cssDNA hybrids for robust data storage（Science Advances）](https://www.science.org/doi/10.1126/sciadv.aed2917)
- [Information Theory and Coding for Future Wireless（IEEE ICC 2025）](https://iccc2025.ieee-icc.org/information-theory-and-coding-future-wireless)
- [Information Theory（ScienceStack）](https://www.sciencestack.ai/explore/cs.IT)