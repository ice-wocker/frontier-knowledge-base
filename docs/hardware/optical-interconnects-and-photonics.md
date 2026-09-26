# 硅光与光互连（Optical Interconnects and Photonics）

> 最后更新：2026-09-26 ｜ 领域：硬件·互连与数据中心 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

光互连（optical interconnect）承担数据中心内计算芯片与高速网络之间海量数据的光电转换与传输，是连接算力芯片与网络的关键器件。随着 AI 数据中心规模扩张，机架内与机架间的东西向流量激增，光模块的重要性随之提升。国家能源局数据显示，2025 年全国算力中心总用电量达 1700 亿千瓦时，占全社会用电量 1.6%，算力规模扩张意味着数据中心内部数据流动更加频繁（[AI算力催热光模块新赛道](http://m.toutiao.com/group/7689742243267953187/)）。面对功耗挑战，产业界正沿近封装光学（NPO）与共封装光学（CPO）两条路径突围：NPO 将光引擎布置在更靠近交换芯片的位置，兼顾高速互联与维护便利；CPO 则进一步把光学器件与交换芯片共封装，缩短电互连路径（[AI算力催热光模块新赛道](http://m.toutiao.com/group/7689742243267953187/)）。

## 最新进展（2025–2026）

- **速率迭代**：业界观点认为 2026 年 800G 是严肃 AI 数据中心的部署目标，1.6T 已进入超大规模客户的早期商用阶段（[Why 800G and 1.6T Optical Modules Are the Next Must-Have for AI Data Centers in 2026](https://www.hytoptodevice.com/blog-detail/why-800g-and-16t-optical-modules-are-the-next-must-have-for-ai-data-centers-in-2026)）。有分析指出 800G 难以支撑 Blackwell 的 scale-up NVLink 带宽需求，因为 NVLink 5.0 单对 GPU 聚合带宽达 1.8 Tbps，超过 800G 的 8×100G 通道能力（[Why 1.6T Optical Transceivers Overtake 800G in 2026 AI Clusters?](https://www.szwecent.com/why-1-6t-optical-transceivers-overtake-800g-in-2026-ai-clusters/)）。

- **CPO 交换机量产**：2026 年 8 月 14 日，NVIDIA 宣布 Spectrum-X 以太网硅光交换机全面量产，被称为全球首款进入量产的 200G/lane CPO 以太网交换机（[英伟达 CPO 交换机量产落地!光互联产业迎来拐点](https://news.sohu.com/a/1074390405_438296)）。该产品线旗舰型号 SN6810 在 2U 液冷机箱内提供 128 个 800G 端口，总交换能力 102.4 Tb/s，更高规格型号 SN6800 达更高端口密度（[CPO量产重塑产业分工](https://www.cnblogs.com/zhangxinghe/p/22729429)）。厂商口径称该方案把激光器数量减少 75%、功耗降低 80%、平均故障间隔时间（MTBF）提升 10 倍（[硅光模块出货额首超半壁江山](https://h5.ifeng.com/c/vivoArticle/v002z1CQhR0MA-_ie9mqGEToVaOUsCqd--Z5ClDQ2ayNNGxrs__?isNews=1&showComments=0)）。

- **交换芯片侧 CPO**：Broadcom 发布 Tomahawk 6–Davisson，称为业界首款 102.4 Tbps 的光学使能（CPO）以太网交换机，带宽为当时任何已上市 CPO 交换机的两倍（[Broadcom Announces Tomahawk 6 – Davisson](https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-tomahawkr-6-davisson-industrys-first-1024)）。该系列还包括面向超低时延的 Tomahawk Ultra（250ns 时延）与面向 100 万+ XPU 集群无损网络的 Jericho 4（[Broadcom Showcases Industry-Leading Solutions for Scaling AI Infrastructure at OFC 2026](https://broadcom.gcs-web.com/news-releases/news-release-details/broadcom-showcases-industry-leading-solutions-scaling-ai)）。

- **光电路交换（OCS）**：Google 的 Apollo 项目被认为是全球首个数据中心级光电路交换的生产部署，用于平衡成本、端口数、切换时间与光学性能（[Mission Apollo: Landing Optical Circuit Switching at Datacenter Scale](https://arxiv.org/pdf/2208.10041v1)）。OCS 主要部署在 scale-out 层以替代 Spine 网络，也用于 scale-up 层动态连接 GPU/CPU 节点，支撑随训练阶段调整拓扑（[OCP Global Summit 2025_Google_OCP Optical Circuit Switching Subproject Update](https://www.simpletechtrend.com/post/ocp-global-summit-2025_google_ocp-optical-circuit-switching-subproject-update)）。据分析，TPUv4 pod 采用 136×136 OCS 交换机、pod 规模为 4096 颗 TPU，OCS 交换机在 DCNI 层组织为 4 个 Apollo zone、合计最多 256 台 OCS（[TPUv7: Google Takes a Swing at the King](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)）。第七代 TPU（Ironwood）的 pod 通过自有光互连连接多达 9216 颗芯片，而 NVIDIA NVL72 系统为 72 颗（[Google's 1000x AI Capacity Target and the Efficiency Thesis](https://www.stanleylaman.com/signals-and-noise/googles-1000x-capacity-target)）。

## 核心技术与关键概念

- **可插拔光模块 → LPO → NPO → CPO**：整体演进趋势围绕带宽提升，持续推进封装扩容、架构集成与接口高密度化，以解决高速场景下的功耗、散热、布线、传输距离问题；头部厂商已在关键场景导入 LPO（线性直驱）技术，CPO 处于验证与规划阶段（[光模块行业深度报告](http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/841233665283/index.phtml)）。
- **硅光（silicon photonics）**：以硅基工艺集成光器件，是降低 1.6T 模块功耗的关键路径之一。
- **光交换**：包括 OCS（光电路交换）与基于光开关的可重构拓扑。
- **关键上游器件**：200G/lane 电吸收调制激光器（EML）、连续波（CW）激光器与 1.6T DSP，被普遍视为供给瓶颈环节（[大摩:科技硬件投资主线切换至结构升级+AI基建](http://m.toutiao.com/group/7689757819721925120/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **NVIDIA**：Spectrum-X Photonics 以太网 CPO 交换机（2026-08 量产）；Quantum-X Photonics InfiniBand 交换机，通过缩短光学与电子之间的连接距离降低总功耗与时延（[NVIDIA Quantum InfiniBand Switches and Appliances](https://www.nvidia.com/en-us/networking/infiniband-switching/)）。
- **Google**：Project Apollo / OCS 光交换架构，用于 TPU pod 互联（[Mission Apollo](https://arxiv.org/pdf/2208.10041v1)）。
- **产业链玩家**：AI 芯片（NVIDIA）、交换芯片（Broadcom）、网络设备（Cisco）、光器件（Lumentum、Coherent），构成「芯片+光子」融合格局（[CPO(共封装光学)深度研究报告](https://finance.sina.com.cn/wm/2026-04-10/doc-inhtymqf5244535.shtml)）；Marvell 亦布局高速光模块、硅光与 CPO（[2026光模块趋势｜Marvell布局拆解](https://m.10100.com/article/143412890)）。
- **中国光模块厂商**：报道显示中际旭创 2026 年上半年营收 417.78 亿元、同比增长 182.5%；新易盛上半年营收 209.1 亿元、同比增长超 100%（[英伟达 CPO 交换机量产落地](https://news.sohu.com/a/1074390405_438296)）。

## 关键数据与评测结果（附来源）

- **市场规模**：Goldman Sachs 大幅上调全球光模块市场预测，预计 2026 年 677 亿美元、2027 年 1314 亿美元、2028 年 1485 亿美元（[Goldman Sachs Raises Optical Module Forecast to $148.5B by 2028](https://gigadevice.icgoodfind.com/Semiconductor_Technology/86896.html)）。
- **LightCounting**：预计当年以太网光收发模块市场增长 73%，到 2031 年市场销售额达 800 亿美元；中国云厂商预计在 2026—2027 年规模部署 800G 光模块，1.6T、3.2T 产品随后进入部署阶段（[AI算力催热光模块新赛道](http://m.toutiao.com/group/7689742243267953187/)）。
- **800G 口径不一**：需求端野村/部分机构乐观预期 6000 万只，高盛 3800 万只，LightCounting 4000–4500 万只；受 200G EML 芯片 20%–30% 供应缺口制约，实际出货约 3500–4000 万只（[2026全球800G/1.6T光模块需求](https://guba.sina.cn/view_10376_182518.html)）。

## 趋势与争议

- **CPO 落地节奏争议**：CPO 在架构上可缩短光电信号传输路径、降低损耗，但当前仍面临良率、成本、散热等落地难题，有观点认为短期难以大规模商用，一旦工艺瓶颈突破才会重构产业格局（[2026光模块趋势｜Marvell布局拆解](https://m.10100.com/article/143412890)）；亦有分析认为 CPO 更可能先重塑垂直扩展（Scale-up）场景，其所需带宽可达水平扩展（Scale-out）的十倍以上（[光通信行业点评报告:英伟达宣布CPO量产](http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/industry/rptid/840541920267/index.phtml)）。
- **中美欧路径差异**：各方在硅光与 CPO 上的竞逐路径存在差异，硅光模块出货额已首次超过半壁江山（[硅光模块出货额首超半壁江山](https://h5.ifeng.com/c/vivoArticle/v002z1CQhR0MA-_ie9mqGEToVaOUsCqd--Z5ClDQ2ayNNGxrs__?isNews=1&showComments=0)）。

## 参考来源

- [Why 800G and 1.6T Optical Modules Are the Next Must-Have for AI Data Centers in 2026](https://www.hytoptodevice.com/blog-detail/why-800g-and-16t-optical-modules-are-the-next-must-have-for-ai-data-centers-in-2026)
- [Why 1.6T Optical Transceivers Overtake 800G in 2026 AI Clusters?](https://www.szwecent.com/why-1-6t-optical-transceivers-overtake-800g-in-2026-ai-clusters/)
- [Goldman Sachs Raises Optical Module Forecast to $148.5B by 2028](https://gigadevice.icgoodfind.com/Semiconductor_Technology/86896.html)
- [英伟达 CPO 交换机量产落地!光互联产业迎来拐点](https://news.sohu.com/a/1074390405_438296)
- [CPO量产重塑产业分工，光通信产业格局和技术路线演进深度拆解](https://www.cnblogs.com/zhangxinghe/p/22729429)
- [硅光模块出货额首超半壁江山，中美欧CPO竞逐路径有何不同?](https://h5.ifeng.com/c/vivoArticle/v002z1CQhR0MA-_ie9mqGEToVaOUsCqd--Z5ClDQ2ayNNGxrs__?isNews=1&showComments=0)
- [Mission Apollo: Landing Optical Circuit Switching at Datacenter Scale](https://arxiv.org/pdf/2208.10041v1)
- [OCP Global Summit 2025_Google_OCP Optical Circuit Switching Subproject Update](https://www.simpletechtrend.com/post/ocp-global-summit-2025_google_ocp-optical-circuit-switching-subproject-update)
- [TPUv7: Google Takes a Swing at the King](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)
- [Broadcom Announces Tomahawk 6 – Davisson, the Industry's First 102.4-Tbps Ethernet Switch with Co-Packaged Optics](https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-tomahawkr-6-davisson-industrys-first-1024)
- [Broadcom Showcases Industry-Leading Solutions for Scaling AI Infrastructure at OFC 2026](https://broadcom.gcs-web.com/news-releases/news-release-details/broadcom-showcases-industry-leading-solutions-scaling-ai)
- [Google's 1000x AI Capacity Target and the Efficiency Thesis](https://www.stanleylaman.com/signals-and-noise/googles-1000x-capacity-target)
- [NVIDIA Quantum InfiniBand Switches and Appliances](https://www.nvidia.com/en-us/networking/infiniband-switching/)
- [CPO(共封装光学)深度研究报告](https://finance.sina.com.cn/wm/2026-04-10/doc-inhtymqf5244535.shtml)
- [2026光模块趋势｜Marvell布局拆解](https://m.10100.com/article/143412890)
- [光模块行业深度报告:集成度逐步提升重构光模块价值链](http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/841233665283/index.phtml)
- [光通信行业点评报告:英伟达宣布CPO量产](http://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/industry/rptid/840541920267/index.phtml)
- [2026全球800G/1.6T光模块需求](https://guba.sina.cn/view_10376_182518.html)
- [AI算力催热光模块新赛道](http://m.toutiao.com/group/7689742243267953187/)
- [大摩:科技硬件投资主线切换至结构升级+AI基建](http://m.toutiao.com/group/7689757819721925120/)