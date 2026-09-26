# 量子计算

> 最后更新：2026-09-26 ｜ 领域：量子计算 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

量子计算利用叠加与纠缠等量子特性进行运算，被普遍认为有望在药物与材料模拟、优化、密码分析等领域带来突破。行业目前处于"从 NISQ（含噪声中等规模量子）走向容错量子计算（FTQC）"的过渡期：**量子纠错（QEC）首次被验证"低于阈值"、逻辑量子比特开始可演示、科技巨头与初创公司纷纷给出 2029 年前后实现容错的路线图**。但与此同时，"量子优越性"实验的实用价值、"拓扑量子比特"的物理证据、以及商业化时间表均存在显著争议。

## 2025–2026 最新进展

### IBM：从 Nighthawk 到 Starling
IBM 的路线图核心是超导 + qLDPC 纠错码 + 模块化。2025 年 11 月，IBM 发布当时最先进的处理器 IBM Quantum Nighthawk：120 个量子比特，采用方形格点（square lattice），每个量子比特与四个最近邻通过新一代可调耦合器（共 218 个）连接，相较 Heron 的 heavy-hex 格点连接度提升超 20%，可运行含 5000 个门的电路（[IBM: How IBM will build the world's first large-scale, fault-tolerant quantum computer](https://www.ibm.com/quantum/blog/large-scale-ftqc)、[IBM Delivers New Quantum Processors](https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance)）。

按 IBM 公开路线图：**Loon（2025）** 用于测试 qLDPC 架构组件；**Kookaburra（2026）** 是首个模块化处理器，可存储与处理编码信息；**Starling（2029）** 是 IBM 计划中的大规模容错量子计算机，通过多模块纠错架构运行 200 个逻辑量子比特上的 1 亿个量子门（[IBM Quantum Roadmap](https://www.ibm.com/roadmaps/quantum/)、[IBM Quantum Hardware: Starling](https://www.ibm.com/quantum/hardware)）。2026 年的目标包括：Nighthawk 在最多三个 120 比特模块上运行含 7500 个门的电路，并原型化实时纠错解码器——这是可扩展容错的关键能力（[IBM Quantum Roadmap 2026](https://www.ibm.com/roadmaps/quantum/2026/)）。2026 年 6 月 2 日，IBM 宣布向量子计算投入超 100 亿美元，以支撑其从当前系统走向全球首批容错量子计算机的路线图（[IBM 新闻稿](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers)）。

### Google：Willow 与"可验证量子优势"
Google 的路线图里程碑依次是：2019 年实现超越经典的计算；2023 年完成量子纠错原型；2024 年底发布 Willow 芯片，首次演示**"低于阈值"的量子纠错**——即随着比特数增加误差率反而指数下降，逻辑错误率随码距增加而减半（[Meet Willow, our state-of-the-art quantum chip](https://blog.google/technology/research/google-willow-quantum-chip/)）。量子纠错自 1995 年 Peter Shor 提出以来一直是核心难题，"低于阈值"被视为真正进展的前提。

2025 年，Google 进一步提出 **Quantum Echoes** 算法并声称实现"可验证的量子优势"，称这是迈向真实应用的重要一步（[Our Quantum Echoes algorithm](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/)、[Our quantum hardware: the engine for verifiable quantum advantage](https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/)）。

### Quantinuum、IonQ：离子阱路线
Quantinuum 于 2025 年 11 月发布 **Helios** 处理器，采用 98 个全连接的 ¹⁷¹Yb⁺ 离子，可操作 50 个逻辑量子比特，并展示了 48 个完全纠错的逻辑比特（[Quantinuum Helios](https://pronetic.geeknetic.es/Noticia/39187/Quantinuum-muestra-Helios-su-ordenador-cuantico-con-50-qubits-logicos.html)、[Quantum Industry Map](https://amotoolkit.com/pages/qc-landscape.html)）。据报道，其两比特门保真度达 99.92%（与 Sandia 合作、2026 年 6 月同行评审）。

IonQ 的路线图规划到 2030 年实现 200 万个物理量子比特与 8 万个逻辑量子比特；2026 年阶段目标为 100–256+ 物理量子比特、99.99% 物理比特保真度与 12 个逻辑量子比特（[IonQ Roadmap](https://www.ionq.com/roadmap)）。2026 年投资者日上，IonQ 开放了第六代旗舰系统 **Superion 256** 的订单，首批交付计划于 2027 年，并将其 2026 年全年营收指引上调至 4.5–4.6 亿美元（[IonQ Investor Day 2026](https://www.ionq.com/blog/innovating-manufacturing-and-scaling-highlights-from-ionq-investor-day-2026)）。IonQ 还宣布收购 SkyWater Technology，以打造垂直整合的全栈量子平台，并预期 2028 年开始对 20 万比特 QPU（对应 8000 个超高保真逻辑比特）进行功能测试（[IonQ to Acquire SkyWater Technology](https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/)）。

### Microsoft：拓扑量子比特的进展与争议
Microsoft 走拓扑量子比特路线。继 2025 年发布 Majorana 1 后，公司于 2026 年 6 月 2 日在 Build 大会发布 **Majorana 2**，声称比特稳定性相比第一代提升 1000 倍，并将可扩展量子计算机的时间表从 2033 年提前到 2029 年（[PostQuantum: Microsoft's Majorana 2 Chip](https://postquantum.com/industry-news/microsoft-majorana-2-analysis/)）。DARPA 已获得对 Majorana 2 比特的首次现场访问权限（[TechTimes](https://www.techtimes.com/articles/327905/20260923/darpa-gets-first-site-access-microsoft-majorana-2-qubits-under-scrutiny.htm)）。

然而该路线备受质疑。2026 年 6 月 24 日，Nature 刊出凝聚态物理学家 Henry Legg 的正式质疑，指 Microsoft 2025 年的 Majorana 结果依赖编码错误与选择性呈现的数据；Microsoft 则辩称相关错误是琐碎的、其物理结论成立（[Clouds of Uncertainty Dog Microsoft's Majorana Qubit Claims](https://quantumzeitgeist.com/microsoft-majorana-qubit-claims/)）。

### PsiQuantum：光子路线的大额融资
PsiQuantum 采用光子方案，目标是百万物理比特级、数据中心规模的容错量子计算机。公司在 2025 年 9 月完成 10 亿美元 E 轮融资，估值 70 亿美元，由 BlackRock 领投，Temasek、Baillie Gifford、NVIDIA 的 NVentures 等参投，用于在布里斯班与芝加哥建设设施（[PsiQuantum Raises $1 Billion](https://ukquantum.org/psiquantum-raises-1-billion-to-build-million-qubit-scale-fault-tolerant-quantum-computers/)）。澳大利亚联邦与昆士兰州政府合计承诺约 A$940M 的资助；PsiQuantum 于 2026 年 6 月 18 日在布里斯班北部的 Moreton Bay Central 破土动工（[Australia Quantum Computing Companies 2026](https://quantumzeitgeist.com/australia-quantum-computing-companies/)）。2026 年 7 月，PsiQuantum 又与 DARPA 签署 1.25 亿美元的扩展协议（[PsiQuantum 公司档案](https://quantummarketcap.com/company/psiquantum)）。

### 中国团队：祖冲之三号与九章四号
中国科学技术大学潘建伟、朱晓波、彭承志团队于 2025 年 3 月构建 105 比特超导量子计算原型机"**祖冲之三号**"，在"量子随机线路采样"任务上再次打破超导体系量子计算优越性世界纪录（[新华网](https://www.news.cn/tech/20250304/6dcfc2372cf440c2afe38369341a7f4c/c.html)），该成果入选 2025 年中国十大科技进展新闻（[中国科大](https://quantumcas.ac.cn/2026/0126/c20522a720520/page.htm)）。据报道，2025 年底中国在量子纠错领域取得"低于阈值，越纠越对"的里程碑式成就（[新华网：九章四号](https://www.news.cn/20260513/30003713c6e74ff8bbcc71a1215f0bf5/c.html)）。

2026 年 5 月 13 日，团队发布光量子计算原型机"**九章四号**"，用于高效求解高斯玻色采样，计算速度比当时全球最快超级计算机 El Capitan 快 10⁵⁴ 倍，论文发表于《自然》（[中国科大新闻网](http://news.ustc.edu.cn/info/1056/94962.htm)）。中国是全球唯一在光量子与超导两条路线上均实现量子计算优越性的国家。

### 后量子密码（PQC）
量子威胁的另一面是密码安全。NIST 已于 2024 年 8 月发布首批 PQC 标准，包括基于 CRYSTALS-Kyber 的 **FIPS 203（ML-KEM）** 密钥封装机制与基于 CRYSTALS-Dilithium 的 **FIPS 204（ML-DSA）** 数字签名（[NIST: The First NIST PQC Standards](https://www.nist.gov/system/files/documents/2024/10/28/5.Moody%20PQC%20VCAT.pdf)）。2025 年 3 月，NIST 在第四轮遴选中选定 HQC 算法进行标准化（[NIST IR 8545 第四轮状态报告](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf)）。按美国国家安全备忘录 NSM-10，联邦系统完成向 PQC 迁移的主要目标是 **2035 年**（[NIST IR 8547 Transition to Post-Quantum Cryptography Standards](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf)）。

## 核心技术与关键概念

- **主要技术路线**：超导（IBM、Google、中国科大）、离子阱（Quantinuum、IonQ）、中性原子（QuEra 等）、光子（PsiQuantum、Xanadu）、拓扑（Microsoft）。超导在门速度与规模化上领先；离子阱在保真度与全连接上占优；光子在室温运行与网络化上有优势；拓扑若能成立则天然抗噪。
- **量子纠错（QEC）与表面码**：用大量物理比特编码一个逻辑比特，通过反复测量稳定子抑制错误。**"低于阈值"** 指增大码距能进一步降低逻辑错误率，是纠错有效性的核心判据；Google Willow 首次演示。
- **NISQ vs 容错**：NISQ 阶段（无纠错、比特数有限）只能做特定演示；容错阶段（FTQC）才能运行 Shor 等长算法。
- **qLDPC 码**：相比表面码有更高的编码效率，是 IBM 2029 Starling 架构的基础。
- **量子优越性 vs 量子实用性**：前者指在特定人为构造任务上超越经典超算，后者指解决有实际价值的问题——两者之间的鸿沟是当前最大争议点。
- **逻辑量子比特**：多个物理比特经纠错后形成的"可用"比特，是衡量容错进展的关键指标（如 Quantinuum Helios 的 50 逻辑比特、IBM Starling 的 200 逻辑比特）。

## 关键数据

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| IBM Nighthawk | 120 比特、218 耦合器、5000 门 | [IBM 博客](https://www.ibm.com/quantum/blog/large-scale-ftqc) |
| IBM Starling（2029） | 200 逻辑比特、1 亿量子门 | [IBM Quantum Hardware](https://www.ibm.com/quantum/hardware) |
| IBM 投入 | 超 100 亿美元 | [IBM 新闻稿](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers) |
| Quantinuum Helios | 98 物理比特、50 逻辑比特、2Q 保真度 99.92% | [Quantum Industry Map](https://amotoolkit.com/pages/qc-landscape.html) |
| IonQ 2030 目标 | 200 万物理比特、8 万逻辑比特 | [IonQ Roadmap](https://www.ionq.com/roadmap) |
| IonQ 2026 营收指引 | 4.5–4.6 亿美元 | [IonQ Investor Day 2026](https://www.ionq.com/blog/innovating-manufacturing-and-scaling-highlights-from-ionq-investor-day-2026) |
| PsiQuantum E 轮 | 10 亿美元，估值 70 亿美元 | [PsiQuantum Raises $1 Billion](https://ukquantum.org/psiquantum-raises-1-billion-to-build-million-qubit-scale-fault-tolerant-quantum-computers/) |
| 祖冲之三号 | 105 比特超导原型机 | [新华网](https://www.news.cn/tech/20250304/6dcfc2372cf440c2afe38369341a7f4c/c.html) |
| 九章四号 | 比 El Capitan 快 10⁵⁴ 倍 | [中国科大新闻网](http://news.ustc.edu.cn/info/1056/94962.htm) |
| PQC 迁移目标 | 2035 年（NSM-10） | [NIST IR 8547](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf) |

## 趋势与争议

1. **商业化时间表的分歧**：IBM 称 2029 年交付大规模容错机、Microsoft 把时间表提前到 2029 年、IonQ 与 PsiQuantum 分别把规模化目标放在 2028–2030 年，但业界普遍认为"有用"的容错量子计算仍遥远。光明网报道指出，量子计算正处于"关乎成败的关键时刻"，其潜力始终受到质疑（[光明网：量子计算离实用还有多远](https://news.gmw.cn/2026-09/24/content_39017806.htm)）。
2. **"量子优越性"的实用性质疑**：无论 Google 的随机线路采样还是中国科大的高斯玻色采样，都是在人为构造、缺乏已知实用价值的任务上取得速度优势，且经典算法可能持续缩小差距。
3. **拓扑量子比特的科学争议**：Microsoft 的 Majorana 结果被同行正式质疑，凸显"证据强度"在该领域的重要性。
4. **资本狂热与商业空白**：2026 年第一季度中国量子计算赛道融资总额达 32 亿元，超过 2025 年全年总和；图灵量子完成近 10 亿元融资、估值超 70 亿元，玻色量子完成 10 亿元 B 轮（[澎湃：量子计算的2026](https://m.thepaper.cn/newsDetail_forward_33474602)）。文章同时指出，技术密集突破之年仍存在"未解的商业之问"。
5. **量子安全的紧迫性被普遍接受**：相较量子计算的商业化不确定，PQC 迁移的紧迫性已成为行业共识——Shor 算法在足够强的通用量子计算机上可破解 RSA/ECC，因此"先收集、后解密"（harvest now, decrypt later）风险推动各国提前迁移（[澎湃：量子计算的2026](https://m.thepaper.cn/newsDetail_forward_33474602)）。

## 参考来源

1. [IBM Quantum Roadmap](https://www.ibm.com/roadmaps/quantum/)
2. [IBM Quantum Roadmap 2026](https://www.ibm.com/roadmaps/quantum/2026/)
3. [IBM Commits More Than $10 Billion to Quantum Computing](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers)
4. [IBM Quantum Hardware for useful quantum computing](https://www.ibm.com/quantum/hardware)
5. [IBM Delivers New Quantum Processors, Software, and Algorithm Breakthroughs](https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance)
6. [How IBM will build the world's first large-scale, fault-tolerant quantum computer](https://www.ibm.com/quantum/blog/large-scale-ftqc)
7. [IBM Quantum Starling 路线图（意大利语新闻稿）](https://it.newsroom.ibm.com/quantum-starling)
8. [Meet Willow, our state-of-the-art quantum chip](https://blog.google/technology/research/google-willow-quantum-chip/)
9. [Our quantum hardware: the engine for verifiable quantum advantage](https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage/)
10. [Our Quantum Echoes algorithm is a big step toward real-world applications](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/)
11. [IonQ Industry-leading roadmap](https://www.ionq.com/roadmap)
12. [IonQ: Innovating, Manufacturing, and Scaling — Investor Day 2026](https://www.ionq.com/blog/innovating-manufacturing-and-scaling-highlights-from-ionq-investor-day-2026)
13. [IonQ to Acquire SkyWater Technology](https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/)
14. [Quantinuum muestra Helios, su ordenador cuántico con 50 qubits lógicos](https://pronetic.geeknetic.es/Noticia/39187/Quantinuum-muestra-Helios-su-ordenador-cuantico-con-50-qubits-logicos.html)
15. [Quantum Industry Map](https://amotoolkit.com/pages/qc-landscape.html)
16. [Microsoft's Majorana 2 Chip Achieves 20-Second Parity Lifetime](https://postquantum.com/industry-news/microsoft-majorana-2-analysis/)
17. [Clouds of Uncertainty Dog Microsoft's Majorana Qubit Claims](https://quantumzeitgeist.com/microsoft-majorana-qubit-claims/)
18. [DARPA Gets First On-Site Access to Microsoft Majorana 2 Qubits](https://www.techtimes.com/articles/327905/20260923/darpa-gets-first-site-access-microsoft-majorana-2-qubits-under-scrutiny.htm)
19. [PsiQuantum Raises $1 Billion to Build Million-Qubit Scale Fault-Tolerant Quantum Computers](https://ukquantum.org/psiquantum-raises-1-billion-to-build-million-qubit-scale-fault-tolerant-quantum-computers/)
20. [Australia Quantum Computing Companies 2026: Complete Vendor Guide](https://quantumzeitgeist.com/australia-quantum-computing-companies/)
21. [PsiQuantum 公司档案（Quantum Market Cap）](https://quantummarketcap.com/company/psiquantum)
22. [新华网：“祖冲之三号”问世，中国再创全球量子计算优越性里程碑](https://www.news.cn/tech/20250304/6dcfc2372cf440c2afe38369341a7f4c/c.html)
23. [新华网：“九章四号”问世，中国科学家再建最强“量子计算优越性”](https://www.news.cn/20260513/30003713c6e74ff8bbcc71a1215f0bf5/c.html)
24. [中国科大新闻网：“九章四号”原型机在合肥问世](http://news.ustc.edu.cn/info/1056/94962.htm)
25. [“祖冲之三号”量子计算成果入选2025年度中国十大科技进展新闻](https://quantumcas.ac.cn/2026/0126/c20522a720520/page.htm)
26. [NIST: Migration to Post-Quantum Cryptography（演示文稿）](https://csrc.nist.gov/csrc/media/presentations/2026/mpts2026-3b1/images-media/mpts2026-3b1-slides-nist-pqc-moody.pdf)
27. [NIST IR 8547: Transition to Post-Quantum Cryptography Standards（PDF）](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf)
28. [NIST IR 8545: Status Report on the Fourth Round of NIST PQC Standardization（PDF）](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf)
29. [NIST: The First NIST PQC Standards（PDF）](https://www.nist.gov/system/files/documents/2024/10/28/5.Moody%20PQC%20VCAT.pdf)
30. [澎湃新闻：量子计算的2026——技术密集突破之年与未解的商业之问](https://m.thepaper.cn/newsDetail_forward_33474602)
31. [光明网：量子计算离实用还有多远](https://news.gmw.cn/2026-09/24/content_39017806.htm)
32. [IBM Quantum Nighthawk（意大利语新闻稿）](https://it.newsroom.ibm.com/ibm-quantum-nighthawk)