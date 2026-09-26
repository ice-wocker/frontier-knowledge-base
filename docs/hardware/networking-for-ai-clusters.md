# AI 集群网络（Networking for AI Clusters）

> 最后更新：2026-09-26 ｜ 领域：硬件·互连与数据中心 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI 集群网络负责把成千上万颗加速卡连接成一个可协同训练与推理的整体，其性能直接决定大规模并行任务的效率。业界把网络分为两个层次：**Scale-up（纵向扩展）**，在机架内以高带宽、低时延的私有互连打通 GPU 之间的全互联；**Scale-out（横向扩展）**，通过 InfiniBand 或以太网把大量节点连接为集群。随着 Mixture-of-Experts（MoE）等架构普及，all-to-all 通信量显著上升，网络的带宽、时延与拥塞控制成为训练性能的关键变量。工程上，AI 集群组网主要有两类实践：以 InfiniBand 为代表的专用高性能网络，和以以太网（RoCEv2，以及 UEC 规范的持续演进）为代表的开放网络，NVIDIA 同时提供两条路线（[NVIDIA Quantum InfiniBand Switches and Appliances](https://www.nvidia.com/en-us/networking/infiniband-switching/)）。

## 最新进展（2025–2026）

- **Scale-up 带宽翻倍**：NVIDIA 的 NVLink 系列按代演进，单 GPU 到 GPU 带宽从 NVLink 4 的 900 GB/s、NVLink 5 的 1800 GB/s 提升到 NVLink 6 的 3600 GB/s；机架级聚合带宽从 7.2 TB/s（NVLink 4）提升到 130 TB/s（NVL72，NVLink 5）与 260 TB/s（NVL72，NVLink 6）（[NVIDIA NVLink und NVLink Switch](https://www.nvidia.com/de-de/data-center/nvlink/)）。GB200 NVL72 以 72 颗 GPU 全互联拓扑提供 130 TB/s NVLink 带宽、13.4 TB HBM3E 与 576 TB/s 显存带宽（[NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)）；GB300 NVL72 采用 9 个 NVSwitch tray 实现 72 颗 GPU 的全非阻塞 P2P 连接，聚合带宽 130 TB/s（[System Hardware & Components](https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/components.html)）。下一代 Vera Rubin NVL72 采用第六代 NVLink，NVLink 6 Switch 新增控制面韧性、部分填充机架运行与热插拔等运维能力（[NVIDIA NVLink and NVLink Switch](https://www.nvidia.com/en-sg/data-center/nvlink/)）。**需注意口径冲突**：NVIDIA 官方 NVLink 页面标注 Vera Rubin NVL72 聚合带宽为 260 TB/s，而 Vera Rubin NVL72 产品页标注为 216 TB/s（[NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-gb/data-center/vera-rubin-nvl72/)），两处数字不一致，引用时应并列呈现。

- **Scale-out 双路线并进**：NVIDIA 同时提供 InfiniBand（Quantum-X800，单端口 800 Gb/s）与以太网（Spectrum-X）两条路线，并在 Vera Rubin 代引入 ConnectX-9 SuperNIC（[NVIDIA Quantum InfiniBand Switches and Appliances](https://www.nvidia.com/en-us/networking/infiniband-switching/)、[NVIDIA DGX SuperPOD 为基于 Rubin 的系统奠定基础](https://blogs.nvidia.cn/blog/dgx-superpod-rubin/)）。基于 DGX Vera Rubin NVL72 的 DGX SuperPOD 整合 8 个系统、576 颗 Rubin GPU，可提供 28.8 ExaFlops 的 FP4 性能。

- **第三条支柱：Scale-across**：2025 年 8 月 22 日 NVIDIA 推出 Spectrum-XGS 以太网，定位为超越 scale-up 与 scale-out 的「跨区域扩展（scale-across）」基础设施，用于把多个分布式数据中心互联为十亿瓦级 AI 超级工厂（[NVIDIA 推出 Spectrum-XGS 以太网](https://blogs.nvidia.cn/blog/nvidia-introduces-spectrum-xgs-ethernet-to-connect-distributed-data-centers-into-giga-scale-ai-super-factories/)、[NVIDIA Introduces Spectrum-XGS Ethernet](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Introduces-Spectrum-XGS-Ethernet-to-Connect-Distributed-Data-Centers-Into-Giga-Scale-AI-Super-Factories/default.aspx)）。该技术采用距离感知的拥塞控制与自适应路由，复用与 scale-out 相同的 Spectrum-X 交换机与 ConnectX-8 SuperNIC，在 10 km 距离测试中取得显著性能表现，CoreWeave 将部署该跨区域扩展技术（[How to Connect Distributed Data Centers Into Large AI Factories with Scale-Across Networking](https://developer.nvidia.com/blog/how-to-connect-distributed-data-centers-into-large-ai-factories-with-scale-across-networking)）。

- **交换芯片侧的以太网军备竞赛**：Broadcom 的 Tomahawk 6 系列称实现全球首个单芯片 102.4 Tbps 交换容量，较前代 Tomahawk 5 翻倍，支持 100G/200G SerDes 与 CPO，面向超过 100 万颗 XPU 的 AI 集群（[Broadcom Ships Tomahawk 6: World's First 102.4 Tbps Switch](https://investors.broadcom.com/news-releases/news-release-details/broadcom-ships-tomahawk-6-worlds-first-1024-tbps-switch)）。其完整以太网组合覆盖 scale-up、scale-out 与 scale-across：Tomahawk 6、Tomahawk 6–Davisson CPO、Tomahawk Ultra（250ns 超低时延）与 Jericho 4（面向 100 万+ XPU 集群的安全无损网络）（[Broadcom Showcases Industry-Leading Solutions for Scaling AI Infrastructure at OFC 2026](https://broadcom.gcs-web.com/news-releases/news-release-details/broadcom-showcases-industry-leading-solutions-scaling-ai)）。

- **开放以太网标准落地**：Ultra Ethernet Consortium（UEC）于 2025 年 6 月 11 日发布 UEC 1.0 规范，随后于 2025 年 9 月 5 日发布 1.0.1（编辑澄清与 RCCC 源算法修正），2026 年 7 月 16 日发布当前版本 1.0.3（[Specification History - Ultra Ethernet Consortium](https://ultraethernet.org/specification-history/)）。UEC 主席在 2025 年度回顾中把 1.0 规范的发布称为该组织的里程碑（[UEC 2025 in Review: Preparing for What Comes Next](https://ultraethernet.org/uec-2025-in-review-preparing-for-what-comes-next-a-letter-from-uecs-chair/)）。UEC 采用 Steering、General、Contributor 三级会员制（[Ultra Ethernet Consortium](https://ultraethernet.org/)）。UEC 创始成员包括 AMD、Arista、Broadcom、Cisco、Eviden、HPE、Intel、Meta、Microsoft 等（[Overview of and Motivation for the Forthcoming UEC Specification](https://ultraethernet.org/wp-content/uploads/sites/20/2023/10/23.07.12-UEC-1.0-Overview-FINAL-WITH-LOGO.pdf)），Steering Members 包括 Meta、Microsoft、Oracle，General Members 还包括 Alibaba、ByteDance、Google（[UEC 1.0 Whitepaper](https://ultraethernet.org/wp-content/uploads/sites/20/2025/06/UEC1.0Whitepaper.pdf)）。

## 核心技术与关键概念

- **协议选型**：InfiniBand 采用原生 RDMA 与 SHARP 网络内计算；Spectrum-X 基于 RoCEv2 以太网，一个对比表给出的口径为：Spectrum-X 每交换机 64×800G、8B 消息时延约 1.7 µs（RoCE），Quantum-2 NDR 每交换机 64×400G、时延约 0.9 µs，网络内计算分别为 SHARP v4（ConnectX-8）与 SHARP v3（[AI Wiki: NVIDIA Spectrum-X](https://aiwiki.ai/wiki/nvidia_spectrum_x/raw)）。
- **拓扑：Rail-Optimized**：在 Rail-Optimized 设计中，所有 GPU 节点的同一端口连接同一台 leaf 交换机，使集合通信可在 leaf 层单跳转发而不经过 spine，从而提高集合通信性能；配合非阻塞设计可保证所有 GPU 同时满速收发（[Cisco Nexus 9000 Series Switches for AI Clusters White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/nexus-9000-series-switches-ai-clusters-wp.html)、[Cisco: Addressing the Challenges of AI/ML Infrastructure](https://www.cisco.com/c/en/us/td/docs/dcn/whitepapers/cisco-addressing-ai-ml-network-challenges.html)）。Rail-Optimized、3-ply 与 multi-plane 等设计变体均建立在集群内 GPU 之间的流量模式之上（[Cisco: Addressing the Challenges of AI/ML Infrastructure](https://www.cisco.com/c/en/us/td/docs/dcn/whitepapers/cisco-addressing-ai-ml-network-challenges.html)）。
- **集合通信与拥塞控制**：大规模训练依赖 all-reduce、all-to-all 等集合通信；MoE 训练中的 all-to-all 负载均衡成为研究热点，RailS 等方案利用 Rail 拓扑对称性把全局协调转化为本地调度，通过本地 LPT spraying 调度器与多路径传输降低完成时间（[RailS: Load Balancing for All-to-All Communication in Distributed Mixture-of-Experts Training](https://arxiv.org/html/2510.19262)）。
- **网络内计算（In-Network Computing）**：InfiniBand 提供 SHARP 网络内计算，在交换机内完成部分集合通信加速；Spectrum-X 平台在 ConnectX-8 代提供 SHARP v4（[AI Wiki: NVIDIA Spectrum-X](https://aiwiki.ai/wiki/nvidia_spectrum_x/raw)）。
- **多租户隔离**：Spectrum-X 结合 BlueField SuperNIC，引入自适应路由与基于遥测的拥塞控制，面向多租户 AI 云，强调性能隔离（[Why AI Training Speed Depends on the Network Fabric Choice](https://discover.oreateai.com/discover/why-ai-training-speed-depends-on-the-network-fabric-choice)）。
- **非阻塞设计与超订比**：Cisco 建议 AI 集群采用非超订（non-oversubscribed）设计，以保证所有 GPU 同时满速收发时仍有足够容量；在同规格设计中，需要把计算流量与存储流量分离以减少争用（[Cisco Nexus 9000 Series Switches for AI Clusters White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/nexus-9000-series-switches-ai-clusters-wp.html)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **NVIDIA**：Quantum InfiniBand（含 Quantum-X800、Quantum-X Photonics）与 Spectrum-X 以太网平台（[NVIDIA Quantum InfiniBand](https://www.nvidia.com/en-us/networking/infiniband-switching/)）。
- **UEC 生态**：Broadcom、Cisco、Arista、HPE、AMD、Intel、Meta、Microsoft、Oracle 等（[Ultra Ethernet Consortium](https://ultraethernet.org/)）。
- **工程案例**：日本 SAKURAONE 采用 Rail-Optimized 拓扑，leaf 与 spine 之间以 800 GbE 互联，并结合 RoCEv2 实现无损传输（[SAKURAONE: Empowering Transparent and Open AI Platforms](https://arxiv.org/html/2507.02124)）；公开整理显示 Meta 的 16000 颗 A100 集群采用 400Gbps Quantum-2 InfiniBand 与 5 层 CLOS 拓扑、25.6Tbps 二分带宽，Microsoft Azure NDv5 采用 Quantum-2 InfiniBand 与自适应路由，每颗 H100 配 8×400Gbps（合计 3.2Tbps），并采用 rail-optimized 设计分离计算与存储流量（[LLM Training Cluster Network Design](https://luxoptx.com/blogs/news/llm-training-cluster-network-design-architectural-fundamentals-for-large-scale-ai-infrastructure)）。

## 关键数据与评测结果（附来源）

- 关于以太网与 InfiniBand 的性能差距存在不同口径：有分析称 Spectrum-X 800GbE 在 8 节点规模下与 InfiniBand NDR 差距在 5% 以内，到 64 节点扩大到 10%–15%，而调优良好的 RoCEv2 已达 InfiniBand 约 70%–80% 的性能，Spectrum-X 相对调优 RoCEv2 的实际提升约为 10%–20% 而非 60%（[Nvidia's Spectrum-X: The $300K Ethernet Fabric That Pretends to Be Open](https://wiggels.dev/posts/nvidia-spectrum-x-deep-dive/)）。
- UEC 规范版本与日期（1.0 / 1.0.1 / 1.0.3）详见官方版本历史页（[Specification History](https://ultraethernet.org/specification-history/)）。
- Broadcom 称 Tomahawk 6 从首次送样到量产用时不到三个季度，并称其代表 AI 基础设施设计的真正突破（[Broadcom Now Shipping World's First 102.4 Tbps Switch in Production Volume](https://www.broadcom.com/company/news/product-releases/64031)）。

## 趋势与争议

- **光互连进入集群组网**：光电路交换（OCS）开始进入 AI 集群组网，Google 的 Apollo 项目把 OCS 部署在 scale-out 层替代 spine 网络，也用于 scale-up 层动态连接 GPU/CPU 节点，并随训练阶段调整拓扑（[Mission Apollo: Landing Optical Circuit Switching at Datacenter Scale](https://arxiv.org/pdf/2208.10041v1)）。
- **网络技术融合**：NVIDIA 将光互连引入交换机（Quantum-X Photonics），通过缩短光学与电子之间的连接距离降低总功耗与时延（[NVIDIA Quantum InfiniBand Switches and Appliances](https://www.nvidia.com/en-us/networking/infiniband-switching/)），暗示 scale-up 与 scale-out 的网络技术正在融合。

- **路线之争**：InfiniBand 在专用「超级计算机」式环境表现优异，而以太网方案面向多租户 AI 云强调性能隔离（[Why AI Training Speed Depends on the Network Fabric Choice](https://discover.oreateai.com/discover/why-ai-training-speed-depends-on-the-network-fabric-choice)）。
- **开放标准 vs 私有互连**：UEC 试图以开放以太网标准覆盖 HPC 与 AI 负载（[UEC 1.0 Whitepaper](https://ultraethernet.org/wp-content/uploads/sites/20/2025/06/UEC1.0Whitepaper.pdf)），而 NVIDIA 的 NVLink/NVSwitch 仍为私有 scale-up 互连，两者在「机架内全互联」与「标准以太网」之间形成张力。
- **Scale-up 与 Scale-out 边界模糊**：光互连与 CPO 交换机让更大规模的单域互联成为可能（详见硅光与光互连篇），推动「机架即计算机」的架构演进。

## 参考来源

- [NVIDIA NVLink und NVLink Switch](https://www.nvidia.com/de-de/data-center/nvlink/)
- [NVIDIA NVLink and NVLink Switch](https://www.nvidia.com/en-sg/data-center/nvlink/)
- [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)
- [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-gb/data-center/vera-rubin-nvl72/)
- [System Hardware & Components (GB300 NVL72)](https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/components.html)
- [NVIDIA Quantum InfiniBand Switches and Appliances](https://www.nvidia.com/en-us/networking/infiniband-switching/)
- [NVIDIA DGX SuperPOD 为基于 Rubin 的系统奠定基础](https://blogs.nvidia.cn/blog/dgx-superpod-rubin/)
- [Specification History - Ultra Ethernet Consortium](https://ultraethernet.org/specification-history/)
- [UEC 2025 in Review: Preparing for What Comes Next](https://ultraethernet.org/uec-2025-in-review-preparing-for-what-comes-next-a-letter-from-uecs-chair/)
- [UEC 1.0: NEW HIGH-PERFORMANCE STANDARD FOR SCALING HPC-AI (Whitepaper)](https://ultraethernet.org/wp-content/uploads/sites/20/2025/06/UEC1.0Whitepaper.pdf)
- [Overview of and Motivation for the Forthcoming UEC Specification](https://ultraethernet.org/wp-content/uploads/sites/20/2023/10/23.07.12-UEC-1.0-Overview-FINAL-WITH-LOGO.pdf)
- [Ultra Ethernet Consortium](https://ultraethernet.org/)
- [NVIDIA 推出 Spectrum-XGS 以太网，助力分布式数据中心迈入十亿瓦级 AI 超级工厂](https://blogs.nvidia.cn/blog/nvidia-introduces-spectrum-xgs-ethernet-to-connect-distributed-data-centers-into-giga-scale-ai-super-factories/)
- [NVIDIA Introduces Spectrum-XGS Ethernet to Connect Distributed Data Centers Into Giga-Scale AI Super-Factories](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Introduces-Spectrum-XGS-Ethernet-to-Connect-Distributed-Data-Centers-Into-Giga-Scale-AI-Super-Factories/default.aspx)
- [How to Connect Distributed Data Centers Into Large AI Factories with Scale-Across Networking](https://developer.nvidia.com/blog/how-to-connect-distributed-data-centers-into-large-ai-factories-with-scale-across-networking)
- [Broadcom Ships Tomahawk 6: World's First 102.4 Tbps Switch](https://investors.broadcom.com/news-releases/news-release-details/broadcom-ships-tomahawk-6-worlds-first-1024-tbps-switch)
- [Broadcom Now Shipping World's First 102.4 Tbps Switch in Production Volume](https://www.broadcom.com/company/news/product-releases/64031)
- [Mission Apollo: Landing Optical Circuit Switching at Datacenter Scale](https://arxiv.org/pdf/2208.10041v1)
- [Broadcom Showcases Industry-Leading Solutions for Scaling AI Infrastructure at OFC 2026](https://broadcom.gcs-web.com/news-releases/news-release-details/broadcom-showcases-industry-leading-solutions-scaling-ai)
- [AI Wiki: NVIDIA Spectrum-X](https://aiwiki.ai/wiki/nvidia_spectrum_x/raw)
- [Cisco Nexus 9000 Series Switches for AI Clusters White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/nexus-9000-series-switches-ai-clusters-wp.html)
- [Cisco: Addressing the Challenges of AI/ML Infrastructure](https://www.cisco.com/c/en/us/td/docs/dcn/whitepapers/cisco-addressing-ai-ml-network-challenges.html)
- [RailS: Load Balancing for All-to-All Communication in Distributed Mixture-of-Experts Training](https://arxiv.org/html/2510.19262)
- [Why AI Training Speed Depends on the Network Fabric Choice](https://discover.oreateai.com/discover/why-ai-training-speed-depends-on-the-network-fabric-choice)
- [SAKURAONE: Empowering Transparent and Open AI Platforms](https://arxiv.org/html/2507.02124)
- [LLM Training Cluster Network Design](https://luxoptx.com/blogs/news/llm-training-cluster-network-design-architectural-fundamentals-for-large-scale-ai-infrastructure)
- [Nvidia's Spectrum-X: The $300K Ethernet Fabric That Pretends to Be Open](https://wiggels.dev/posts/nvidia-spectrum-x-deep-dive/)