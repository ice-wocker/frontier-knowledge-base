# 量子信息科学

> 最后更新：2026-09-26 ｜ 领域：科学·量子信息科学 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

量子信息科学研究如何利用叠加、纠缠与测量等量子特性处理信息，涵盖量子计算、量子通信/量子网络与量子传感/计量三大方向。2025–2026 年，该领域在纠错、网络实用化与精密测量上均取得标志性进展，并因 2025 年诺贝尔物理学奖而受到更广泛的公众关注。

## 最新进展（2025–2026）

**基础与荣誉。** 2025 年诺贝尔物理学奖授予 John Clarke、Michel H. Devoret 与 John M. Martinis，表彰其在电路中"发现宏观量子力学隧穿与能量量子化"（[The Nobel Prize in Physics 2025](https://www.nobelprize.org/prizes/physics/2025/press-release/)）。评审材料指出，三人用超导电路系统证明量子特性可在可手持尺度的系统中具体呈现：该系统能像穿墙一样从一个状态隧穿到另一个状态，并表现出能量的吸收与发射量子化（[Popular information](https://www.nobelprize.org/prizes/physics/2025/popular-information/)）。

**量子纠错与可验证量子优势。** Google 的 Willow 芯片于 2024 年 12 月以表面码在三个不同码距上演示：码距每增大 2，逻辑错误率约下降一半，被视为阈值定理的规范性实验验证（[What is Quantum Error Correction? Complete 2026 Beginner's Guide](https://quantumzeitgeist.com/what-is-quantum-error-correction/)）。2025 年 10 月，Google 以 Willow 结合其 "Quantum Echoes" 算法在 Nature 发表可验证量子优势结果，称在某个基准上比最快的经典超级计算机快约 13,000 倍，且结果可在同类量子机器上复现（[The Latest in Quantum Computing: The Advances Reshaping the Field](https://quantum-nature.com/quantum-computing-advances/)）。另有研究把量子纠错事件本身作为强化学习信号，实现表面码逻辑错误率 7.72×10⁻⁴，并在注入漂移条件下提升约 3.5 倍的逻辑稳定性（[Google Cuts Surface Code Error Rate to 7.72 × 10−4 With RL](https://quantumzeitgeist.com/google-quantum-ai-surface-code-error/)）。编码层面，Cornucopia 系列量子 LDPC 码实现超过 1/2 的编码率与超过 0.4% 的伪阈值，以实现超低开销纠错（[Quantum error correction at ultra-low overhead](https://arxiv.org/html/2608.02773v2)）。

**量子计算硬件与产业化。** 超导路线上，IBM 于 2025 年 11 月发布 IBM Quantum Nighthawk，采用 120 个量子比特的方形格点，以 218 个新一代可调耦合器连接每个比特与四个最近邻，连接度相较 Heron 的 heavy-hex 提升超 20%，可运行含 5000 个门的电路（[How IBM will build the world's first large-scale, fault-tolerant quantum computer](https://www.ibm.com/quantum/blog/large-scale-ftqc)）。其公开路线图为 Loon（2025，测试 qLDPC 组件）、Kookaburra（2026，首个可存储与处理编码信息的模块化处理器）、Starling（2029，通过多模块纠错架构在 200 个逻辑量子比特上运行 1 亿个量子门）（[IBM Quantum Roadmap](https://www.ibm.com/roadmaps/quantum/)）；IBM 于 2026 年 6 月宣布向量子计算投入超 100 亿美元，以支撑向量子容错机的路线图（[IBM 新闻稿](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers)）。离子阱路线上，Quantinuum 于 2025 年 11 月发布 Helios 处理器，采用 98 个全连接的 ¹⁷¹Yb⁺ 离子，可操作 50 个逻辑量子比特，并展示 48 个完全纠错的逻辑比特，两比特门保真度达 99.92%（[Quantinuum Helios](https://pronetic.geeknetic.es/Noticia/39187/Quantinuum-muestra-Helios-su-ordenador-cuantico-con-50-qubits-logicos.html)、[Quantum Industry Map](https://amotoolkit.com/pages/qc-landscape.html)）。IonQ 的路线图规划到 2030 年实现 200 万个物理量子比特与 8 万个逻辑量子比特，2026 年阶段目标为 100–256+ 物理量子比特、99.99% 物理比特保真度与 12 个逻辑量子比特（[IonQ Roadmap](https://www.ionq.com/roadmap)）；2026 年投资者日上开放第六代旗舰系统 Superion 256 订单，首批交付计划于 2027 年，并把 2026 年全年营收指引上调至 4.5–4.6 亿美元（[IonQ Investor Day 2026](https://www.ionq.com/blog/innovating-manufacturing-and-scaling-highlights-from-ionq-investor-day-2026)），同时宣布收购 SkyWater Technology 以打造垂直整合的全栈量子平台（[IonQ to Acquire SkyWater Technology](https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/)）。光子路线上，PsiQuantum 于 2025 年 9 月完成 10 亿美元 E 轮融资、估值 70 亿美元，由 BlackRock 领投、NVIDIA 的 NVentures 等参投，用于在布里斯班与芝加哥建设设施（[PsiQuantum Raises $1 Billion](https://ukquantum.org/psiquantum-raises-1-billion-to-build-million-qubit-scale-fault-tolerant-quantum-computers/)）；澳大利亚联邦与昆士兰州政府合计承诺约 A$940M 资助，2026 年 7 月又与 DARPA 签署 1.25 亿美元扩展协议（[PsiQuantum 公司档案](https://quantummarketcap.com/company/psiquantum)）。拓扑路线上，Microsoft 于 2026 年 6 月发布 Majorana 2，声称比特稳定性较第一代提升 1000 倍、并把可扩展量子计算机时间表从 2033 年提前到 2029 年（[PostQuantum: Microsoft's Majorana 2 Chip](https://postquantum.com/industry-news/microsoft-majorana-2-analysis/)）；但 2026 年 6 月 24 日 Nature 刊出凝聚态物理学家 Henry Legg 的正式质疑，指其 2025 年 Majorana 结果依赖编码错误与选择性呈现的数据，Microsoft 则辩称相关错误是琐碎的、物理结论成立（[Clouds of Uncertainty Dog Microsoft's Majorana Qubit Claims](https://quantumzeitgeist.com/microsoft-majorana-qubit-claims/)）。中国方面，中国科学技术大学潘建伟、朱晓波、彭承志团队于 2025 年 3 月构建 105 比特超导量子计算原型机"祖冲之三号"，在量子随机线路采样任务上再次打破超导体系量子计算优越性世界纪录（[新华网](https://www.news.cn/tech/20250304/6dcfc2372cf440c2afe38369341a7f4c/c.html)）；2026 年 5 月 13 日发布光量子计算原型机"九章四号"，求解高斯玻色采样的速度比当时全球最快超级计算机 El Capitan 快 10⁵⁴ 倍（[中国科大新闻网](http://news.ustc.edu.cn/info/1056/94962.htm)）。

**后量子密码（PQC）。** 量子威胁的另一面是密码安全。NIST 已于 2024 年 8 月发布首批 PQC 标准，包括基于 CRYSTALS-Kyber 的 FIPS 203（ML-KEM）密钥封装机制与基于 CRYSTALS-Dilithium 的 FIPS 204（ML-DSA）数字签名（[The First NIST PQC Standards](https://www.nist.gov/system/files/documents/2024/10/28/5.Moody%20PQC%20VCAT.pdf)）；2025 年 3 月又选定 HQC 算法进行标准化（[NIST IR 8545](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf)）。按美国国家安全备忘录 NSM-10，联邦系统完成向 PQC 迁移的主要目标为 2035 年（[NIST IR 8547](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf)）。

**纠缠理论与实验。** 有实验在非厄米系统中用囚禁离子平台实现纠缠生成的加速，制备速度相对传统厄米量子速度极限提升 1.52 倍（[Researchers Break Quantum Speed Limit with Non-Hermitian Entanglement Acceleration](https://english.cas.cn/newsroom/research-news/202607/t20260714_1178374.shtml)）。另一项工作利用"合成压缩"在超导量子比特上实现耗散驱动的纠缠，且纠缠处于稳态，原则上可在任意大距离上维持（[Entanglement over large separations because of, not despite dissipation](https://iquist.illinois.edu/news/87114)）。在中性原子量子处理器 QuEra Aquila 上，研究者用随机测量协议观测到由可编程无序诱导的纠缠转变，从混沌型转变为局域化纠缠动力学（[Randomised measurements of a disorder-induced entanglement transition in a neutral atom quantum processor](https://arxiv.org/html/2604.24854v1)）。综述性工作则系统整理了纠缠的数学基础（希尔伯特空间、张量积、纠缠度量）与从早期贝尔实验到无漏洞违背的实验突破（[Foundations and Frontiers of Quantum Entanglement](https://zenodo.org/records/16283556/files/Foundations_and_Frontiers_of_Quantum_Entanglement.pdf)）。

**量子网络与量子通信。** NIST 及其合作者把纠缠光子通过 62 公里商用光纤从 Gaithersburg 园区传输到马里兰大学 College Park，显示脆弱纠缠可在真实条件下存活（['Spooky' Particles Transit DC Suburbs, a Step Toward a Quantum Network](https://www.nist.gov/news-events/news/2026/08/spooky-particles-transit-dc-suburbs-step-toward-quantum-network)）。德国电信 T-Labs 与 Qunnect 在柏林商用网络上演示量子隐形传态，被视为在既有电信基础设施上推进可部署量子技术的里程碑（[Deutsche Telekom and Qunnect Successfully Test Quantum Teleportation Over Live Berlin Network](https://www.telekom.com/en/media/media-information/archive/teleportation-via-fiber-optics-in-berlin-1102518)）。有五节点中继的纠缠交换实验在最长 40 公里光纤（四段 10 公里）上交换纠缠，同时在各段传输 10 Gbps 经典数据（[Entanglement swapping across a five-node relay in a multiplexed quantum-classical network](https://arxiv.org/abs/2609.18899)）。中国团队报告"星汉二号"多模式量子中继实现 14.5 公里远距离物质纠缠，为公开报道中最远距离的物质纠缠（[实现14.5公里远距离物质纠缠 中国科学家取得新突破（新华网）](http://www.news.cn/liangzi/20260508/16bb4971119442139a1cb71a0061cae3/c.html)）；另有工作将纠缠寿命提升至 550 毫秒、显著超过建立纠缠所需的 450 毫秒，从而构建可扩展量子中继的基本模块，并在此基础上开展器件无关量子密钥分发（DI-QKD）实验（[科学家在可扩展量子网络研究方面获重要突破（中国科学院）](http://www.cas.cn/cm/202602/t20260209_5100193.shtml)）。欧洲方面，研究团队在瑞典斯德哥尔摩 303 公里现网多芯光纤上演示 QKD，并与实时以太网业务共存（[Quantum Key Distribution Spans 303 km Over Live Swedish Fiber](https://www.techtimes.com/articles/318075/20260609/quantum-key-distribution-spans-303-km-over-live-swedish-fiber-euroqci-blueprint-confirmed.htm)）。欧盟 EuroQCI 计划正与 ESA 合作建设第一代 EuroQCI 卫星星座，原型卫星 Eagle-1 计划于 2027 年底发射（[European Quantum Communication Infrastructure - EuroQCI](https://digital-strategy.ec.europa.eu/en/policies/european-quantum-communication-infrastructure-euroqci)）；欧洲量子技术旗舰的 2026 年通信路线图也指出，中国采取强国家驱动、需求牵引的策略，大规模公开部署带来了可观的用户基数（[Quantum Communication Roadmap Update 2026](https://qt.eu/media/pdf/SRIA2026drafts/QT_SRIA_Communication_Roadmap_v1.pdf)）。

**量子传感与计量。** 中国科学技术大学团队把锶原子光晶格钟的稳定度与不确定度全面突破 10⁻¹⁹ 量级，相当于 300 亿年误差不超过 1 秒（[中国科大实现稳定度和不确定度均达到10^-19量级的光钟](https://quantum.ustc.edu.cn/web/index.php/node/1258)）；有研究报道多离子光钟的频率不确定度达 5.3×10⁻¹⁹（[A multi-ion optical clock](https://arxiv.org/html/2603.23446)）。NIST 指出最先进的光钟不确定度已低于 1×10⁻¹⁸，比铯基准高两个数量级（[Optical atomic clocks: defining the future of time and frequency metrology](https://tf.nist.gov/general/pdf/3351.pdf)）。此外，有工作展示了用片上集成光子波导供光、可自主运行的多离子光钟，短时频率不稳定度为 3.14×10⁻¹⁴/√τ（[Autonomous multi-ion optical clock with on-chip integrated photonic light delivery](https://arxiv.org/html/2512.08921v3)）。

## 核心技术与关键概念

- **量子比特与量子线路**：超导、离子阱、中性原子、光子等实现路径。
- **纠缠与贝尔不等式**：无漏洞贝尔检验确证纠缠的物理实在性；非局域关联与测量问题仍是基础争论点。
- **量子纠错**：表面码、量子 LDPC 码、自校正码；阈值定理规定物理错误率低于阈值时可通过增大码距指数抑制逻辑错误。
- **主要技术路线**：超导（IBM、Google、中国科大）、离子阱（Quantinuum、IonQ）、中性原子（QuEra 等）、光子（PsiQuantum、Xanadu）、拓扑（Microsoft）。超导在门速度与规模化上领先；离子阱在保真度与全连接上占优；光子在室温运行与网络化上有优势；拓扑若能成立则天然抗噪。
- **NISQ 与容错量子计算（FTQC）**：NISQ 阶段（无纠错、比特数有限）只能做特定演示；容错阶段才能运行 Shor 等长算法。行业正处在从 NISQ 走向 FTQC 的过渡期。
- **qLDPC 码**：相比表面码有更高的编码效率，是 IBM 2029 年 Starling 架构的基础。
- **逻辑量子比特**：多个物理比特经纠错后形成的"可用"比特，是衡量容错进展的关键指标（如 Quantinuum Helios 的 50 逻辑比特、IBM Starling 的 200 逻辑比特）。
- **量子优越性 vs 量子实用性**：前者指在特定人为构造任务上超越经典超算，后者指解决有实际价值的问题，两者之间的鸿沟是当前最大争议点。
- **后量子密码（PQC）**：以能抵抗量子攻击的数学难题（如格问题）替代 RSA/ECC，NIST 已标准化的 ML-KEM、ML-DSA 与 HQC 是迁移的核心算法族，各国按"先收集、后解密"（harvest now, decrypt later）风险提前推进迁移。
- **量子通信**：QKD（含器件无关方案 DI-QKD）、量子中继与纠缠交换、量子隐形传态、量子与经典共纤复用。
- **量子计量**：光钟（不确定度已达 10⁻¹⁹ 量级）、量子速度极限、量子增强测量。

## 趋势与争议

1. **纠错从"演示"走向"工程化"**：关注点转向编码率、硬件连接度与解码器效率的联合优化。
2. **"量子优势"的评判标准**：从随机线路采样转向"可验证、可在同类量子机器上复现"的结果。
3. **量子网络的现实约束**：退相干、噪声与成本仍限制规模，量子中继、卫星链路与现网共存三种路线并行推进。
4. **时间表争议**：量子计算在纠错取得进展的同时，其实际应用价值与商用时间表仍存在明显分歧。IBM 称 2029 年交付大规模容错机、Microsoft 把时间表提前到 2029 年、IonQ 与 PsiQuantum 分别把规模化目标放在 2028–2030 年，但业界普遍认为"有用"的容错量子计算仍遥远；光明网报道指出，量子计算正处于"关乎成败的关键时刻"，其潜力始终受到质疑（[光明网：量子计算离实用还有多远](https://news.gmw.cn/2026-09/24/content_39017806.htm)）。
5. **"量子优越性"的实用性质疑与资本狂热并存**：无论 Google 的随机线路采样还是中国科大的高斯玻色采样，都在人为构造、缺乏已知实用价值的任务上取得速度优势，且经典算法可能持续缩小差距。资本端则热度高涨——2026 年第一季度中国量子计算赛道融资总额达 32 亿元，超过 2025 年全年总和，图灵量子完成近 10 亿元融资、估值超 70 亿元，玻色量子完成 10 亿元 B 轮（[澎湃：量子计算的2026](https://m.thepaper.cn/newsDetail_forward_33474602)）。
6. **拓扑量子比特的科学争议**：Microsoft 的 Majorana 结果被同行正式质疑，凸显"证据强度"在该领域的重要性。
7. **量子安全的紧迫性被普遍接受**：相较量子计算的商业化不确定，PQC 迁移的紧迫性已成为行业共识——Shor 算法在足够强的通用量子计算机上可破解 RSA/ECC，因此"先收集、后解密"风险推动各国提前迁移（[澎湃：量子计算的2026](https://m.thepaper.cn/newsDetail_forward_33474602)）。

## 参考来源

- [The Nobel Prize in Physics 2025（press release）](https://www.nobelprize.org/prizes/physics/2025/press-release/)
- [The Nobel Prize in Physics 2025: Popular information](https://www.nobelprize.org/prizes/physics/2025/popular-information/)
- [What is Quantum Error Correction? Complete 2026 Beginner's Guide](https://quantumzeitgeist.com/what-is-quantum-error-correction/)
- [The Latest in Quantum Computing: The Advances Reshaping the Field（Quantum Echoes）](https://quantum-nature.com/quantum-computing-advances/)
- [Google Cuts Surface Code Error Rate to 7.72 × 10−4 With RL](https://quantumzeitgeist.com/google-quantum-ai-surface-code-error/)
- [Quantum error correction at ultra-low overhead（Cornucopia codes）](https://arxiv.org/html/2608.02773v2)
- [Researchers Break Quantum Speed Limit with Non-Hermitian Entanglement Acceleration（CAS）](https://english.cas.cn/newsroom/research-news/202607/t20260714_1178374.shtml)
- [Entanglement over large separations because of, not despite dissipation（UIUC）](https://iquist.illinois.edu/news/87114)
- [Randomised measurements of a disorder-induced entanglement transition in a neutral atom quantum processor](https://arxiv.org/html/2604.24854v1)
- [Foundations and Frontiers of Quantum Entanglement](https://zenodo.org/records/16283556/files/Foundations_and_Frontiers_of_Quantum_Entanglement.pdf)
- ['Spooky' Particles Transit DC Suburbs, a Step Toward a Quantum Network（NIST）](https://www.nist.gov/news-events/news/2026/08/spooky-particles-transit-dc-suburbs-step-toward-quantum-network)
- [Deutsche Telekom and Qunnect Successfully Test Quantum Teleportation Over Live Berlin Network](https://www.telekom.com/en/media/media-information/archive/teleportation-via-fiber-optics-in-berlin-1102518)
- [Entanglement swapping across a five-node relay in a multiplexed quantum-classical network](https://arxiv.org/abs/2609.18899)
- [实现14.5公里远距离物质纠缠 中国科学家取得新突破（新华网）](http://www.news.cn/liangzi/20260508/16bb4971119442139a1cb71a0061cae3/c.html)
- [科学家在可扩展量子网络研究方面获重要突破（中国科学院）](http://www.cas.cn/cm/202602/t20260209_5100193.shtml)
- [Quantum Key Distribution Spans 303 km Over Live Swedish Fiber](https://www.techtimes.com/articles/318075/20260609/quantum-key-distribution-spans-303-km-over-live-swedish-fiber-euroqci-blueprint-confirmed.htm)
- [European Quantum Communication Infrastructure - EuroQCI（EC）](https://digital-strategy.ec.europa.eu/en/policies/european-quantum-communication-infrastructure-euroqci)
- [Quantum Communication Roadmap Update 2026（QT Flagship SRIA）](https://qt.eu/media/pdf/SRIA2026drafts/QT_SRIA_Communication_Roadmap_v1.pdf)
- [中国科大实现稳定度和不确定度均达到10^-19量级的光钟](https://quantum.ustc.edu.cn/web/index.php/node/1258)
- [A multi-ion optical clock](https://arxiv.org/html/2603.23446)
- [Optical atomic clocks: defining the future of time and frequency metrology（NIST）](https://tf.nist.gov/general/pdf/3351.pdf)
- [Autonomous multi-ion optical clock with on-chip integrated photonic light delivery](https://arxiv.org/html/2512.08921v3)
- [How IBM will build the world's first large-scale, fault-tolerant quantum computer](https://www.ibm.com/quantum/blog/large-scale-ftqc)
- [IBM Quantum Roadmap](https://www.ibm.com/roadmaps/quantum/)
- [IBM Commits More Than $10 Billion to Quantum Computing](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers)
- [Quantinuum muestra Helios, su ordenador cuántico con 50 qubits lógicos](https://pronetic.geeknetic.es/Noticia/39187/Quantinuum-muestra-Helios-su-ordenador-cuantico-con-50-qubits-logicos.html)
- [Quantum Industry Map](https://amotoolkit.com/pages/qc-landscape.html)
- [IonQ Industry-leading roadmap](https://www.ionq.com/roadmap)
- [IonQ: Innovating, Manufacturing, and Scaling — Investor Day 2026](https://www.ionq.com/blog/innovating-manufacturing-and-scaling-highlights-from-ionq-investor-day-2026)
- [IonQ to Acquire SkyWater Technology](https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/)
- [PsiQuantum Raises $1 Billion to Build Million-Qubit Scale Fault-Tolerant Quantum Computers](https://ukquantum.org/psiquantum-raises-1-billion-to-build-million-qubit-scale-fault-tolerant-quantum-computers/)
- [PsiQuantum 公司档案（Quantum Market Cap）](https://quantummarketcap.com/company/psiquantum)
- [Microsoft's Majorana 2 Chip Achieves 20-Second Parity Lifetime](https://postquantum.com/industry-news/microsoft-majorana-2-analysis/)
- [Clouds of Uncertainty Dog Microsoft's Majorana Qubit Claims](https://quantumzeitgeist.com/microsoft-majorana-qubit-claims/)
- [新华网：“祖冲之三号”问世，中国再创全球量子计算优越性里程碑](https://www.news.cn/tech/20250304/6dcfc2372cf440c2afe38369341a7f4c/c.html)
- [中国科大新闻网：“九章四号”原型机在合肥问世](http://news.ustc.edu.cn/info/1056/94962.htm)
- [NIST: The First NIST PQC Standards（PDF）](https://www.nist.gov/system/files/documents/2024/10/28/5.Moody%20PQC%20VCAT.pdf)
- [NIST IR 8545: Status Report on the Fourth Round of NIST PQC Standardization（PDF）](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf)
- [NIST IR 8547: Transition to Post-Quantum Cryptography Standards（PDF）](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf)
- [澎湃新闻：量子计算的2026——技术密集突破之年与未解的商业之问](https://m.thepaper.cn/newsDetail_forward_33474602)
- [光明网：量子计算离实用还有多远](https://news.gmw.cn/2026-09/24/content_39017806.htm)