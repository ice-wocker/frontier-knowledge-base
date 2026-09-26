# 类脑与新型计算（Neuromorphic and Novel Computing）

> 最后更新：2026-09-26 ｜ 领域：硬件·计算架构 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

类脑与新型计算（neuromorphic and novel computing）指不依赖传统冯·诺依曼架构与二进制同步时钟的一类计算范式探索，包括神经形态芯片（脉冲神经网络、事件驱动）、近存/存内计算、光计算、DNA 存储与概率计算等方向。其共同动机是突破「存储与计算分离」带来的数据搬运瓶颈。IBM 研究指出，数十年前确立的冯·诺依曼架构决策，正成为当今 AI 计算能力的制约因素（[Why a decades old architecture decision is impeding the power of AI computing](https://research.ibm.com/blog/why-von-neumann-architecture-is-impeding-the-power-of-ai-computing)）。类脑智能被描述为受生物脑神经机制与认知行为启发、通过软硬件协同实现的机器智能，被视为下一代人工智能的颠覆性路径之一（[下一代人工智能重要突破口是什么?](https://www.jfdaily.com/staticsg/res/html/web/newsDetail.html?id=1176853&sid=11)）。

## 最新进展（2025–2026）

- **Intel Loihi 2 与 Hala Point**：Intel 公布全球最大神经形态系统 Hala Point，采用 Loihi 2 处理器，是业界首个 11.5 亿神经元级神经形态系统，最初部署于 Sandia National Laboratories（[Intel Builds World's Largest Neuromorphic System to Enable More Sustainable AI](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai)）。该系统集成 1152 颗 Loihi 2 芯片、140,544 个神经形态核心、2304 个嵌入式 x86 主机核心、11.5 亿神经元与约 1280 亿突触（部分 Sandia 文档报告接近 1382 亿突触），聚合内存带宽 16 PB/s（[Intel Loihi](https://aiwiki.ai/wiki/intel_loihi)）；其形态约为微波炉大小的 6U 机箱，最大功耗 2600 W（[AI Wiki: Neuromorphic Computing](https://aiwiki.ai/wiki/neuromorphic_computing/raw)）。
- **IBM NorthPole**：IBM 团队在 2023 年论文中报告 NorthPole 神经形态芯片能以传统系统极小的能耗完成图像分类，且速度更快（约 5 倍）（[Dharmendra S. Modha](https://modha.org/page/2/)）。后续实验以基于 IBM Granite-8B-Code-Base 的 30 亿参数 LLM 进行推理，团队实现每 token 延迟低于 1 毫秒，相比次优能效 GPU 快近 47 倍（[Charting a path to a more sustainable AI future](https://research.ibm.com/blog/aiu-chip-family-ibm-research)）；NorthPole 在时延与能效上同时优于多款常用 LLM 推理 GPU（[For LLMs, IBM's NorthPole chip overcomes the tradeoff between speed and efficiency](https://research.ibm.com/blog/northpole-llm-inference-results)）。2025 年研究进一步将 18 台 2U 服务器组成机架，形成 288 颗 NorthPole 的可扩展系统，面向低时延、高能效的 LLM 推理（[A Scalable NorthPole System with End-to-End Vertical Integration](https://arxiv.org/html/2511.15950v1/)）。
- **商用边缘神经形态芯片**：BrainChip 于 2026 年 6 月 30 日宣布其 Akida AKD1500 参考芯片实现商用供货，与 GlobalFoundries 合作采用 22nm 工艺（[BrainChip Announces Commercial Availability and Production Shipments of AKD1500 Neuromorphic Processors](https://brainchip.com/brainchip-announces-commercial-availability-and-production-shipments-of-akd1500-neuromorphic-processors/)）；2026 年 7 月 28 日推出紧凑 M.2 形态，用于工业与商业的无风扇边缘 AI（[BrainChip AKD1500 Now Available in Compact M.2 Form Factor](https://brainchip.com/press/brainchip-akd1500-now-available-in-compact-m-2-form-factor-enabling-fanless-edge-ai-in-industrial-and-commercial-designs/)）。Innatera 于 2025 年 5 月 21 日发布 Pulsar，宣称是全球首款面向传感器边缘的量产级神经形态微控制器，相比传统 AI 处理器时延低至 1/100、能耗低至 1/500（[Innatera unveils Pulsar](https://www.innatera.com/newsroom/innatera-unveils-pulsar-the-worlds-first-mass-market-neuromorphic-microcontroller-for-the-sensor-edge)）。
- **光计算**：2026 年，光本位科技全球首发 256×256 光计算芯片，称其为当时全球矩阵规模最大的全可编程光计算芯片，单颗晶粒集成超 65000 个光计算单元，并将存储与计算融合于同一光学通路、模型权重可静态保持且功耗为零；同年与计算卫星研发商联合研制全球首颗光计算卫星（[全球首发256×256芯片，光本位光电混合计算领跑AI算力新纪元](https://m.bjnews.com.cn/detail/1788512736129339.html)）。

## 核心技术与关键概念

- **神经形态计算**：以脉冲神经网络（SNN）与事件驱动为核心，模拟生物神经元；优势在于稀疏事件下的极低功耗，代价是训练方法与工具链尚不成熟。
- **近存/存内计算**：NorthPole 将存储器置于数字 SRAM 中，虽然内存未像模拟芯片那样与计算交织，但其众多核心各自可访问本地内存，构成近存计算的极端案例（[Why a decades old architecture decision is impeding the power of AI computing](https://research.ibm.com/blog/why-von-neumann-architecture-is-impeding-the-power-of-ai-computing)）。
- **光计算**：以光子替代电子承载矩阵运算，理论上具备高并行与低功耗潜力，但可编程性、精度与封装是关键挑战。
- **DNA 存储**：以合成 DNA 分子编码数字信息，具备极高存储密度与长期保存潜力；2026 年微软与华盛顿大学的研究项目称已成功编码并检索 1 PB 数据（约相当于 5000 亿页文本），存储容器不大于一块方糖，读取准确率 99.9999%（[DNA Digital Data Storage](https://internet-pros.com/blog/dna-digital-data-storage-2026/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Intel**：Loihi 2 处理器与 Hala Point 系统（[Intel Newsroom](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai)）。
- **IBM Research**：NorthPole 推理芯片研究原型（PCIe 卡形态）（[A Scalable NorthPole System](https://arxiv.org/html/2511.15950v1/)）。
- **BrainChip**：Akida AKD1500，面向边缘信号智能与国防系统，强调亚瓦级持续推理（对比 FPGA/GPU 边缘模块的多瓦功耗）（[BrainChip Unveils Communication Reference Platform](https://brainchip.com/brainchip-unveils-communication-reference-platform-fueling-signal-intelligence-at-the-edge/)）。
- **Innatera**：Pulsar 神经形态微控制器（[Innatera](https://www.innatera.com/newsroom/innatera-unveils-pulsar-the-worlds-first-mass-market-neuromorphic-microcontroller-for-the-sensor-edge)）。
- **DNA 存储生态**：Twist Bioscience 于 2025 年 5 月 2 日将 DNA 数据存储产品组出售给 Atlas Data Storage（该轮融资约 1.55 亿美元）（[Twist Bioscience SEC Filing](https://investors.twistbioscience.com/node/15331/html)）；Atlas 计划 2026 年实现太字节级 DNA 存储、目标把 13 TB 数据存入「一滴水」体积（[Twist Bioscience spin-off plans Terabyte-scale DNA storage in 2026](https://www.aivanet.com/2025/12/after-nearly-10-years-twist-bioscience-spin-off-plans-terabyte-scale-dna-storage-in-2026-intending-to-store-13tb-of-data-in-a-single-drop-of-water/)）。
- **中国类脑**：报道称相关团队已推出全球首台 100 亿神经元类脑异构融合超算系统，以及超小型移动式类脑智算体「智者一号」；中科院院士张旭认为类脑智能有望 5 年内走进千家万户（[中国科学院院士张旭:类脑智能有望5年内走进千家万户](https://www.stdaily.com/web/gdxw/2026-09/24/content_587047.html)）。

## 关键数据与评测结果（附来源）

- **Hala Point**：1.15×10⁹ 神经元、1152 颗 Loihi 2、140,544 神经形态核心、约 1.28×10¹¹ 突触、16 PB/s 聚合内存带宽、最大功耗 2600 W（[Intel Loihi](https://aiwiki.ai/wiki/intel_loihi)、[AI Wiki: Neuromorphic Computing](https://aiwiki.ai/wiki/neuromorphic_computing/raw)）。
- **NorthPole**：单 token 延迟 < 1 ms，相比次优能效 GPU 快近 47 倍；论文报告图像分类任务约 5 倍速度且能耗极低（[IBM Research](https://research.ibm.com/blog/aiu-chip-family-ibm-research)、[Dharmendra S. Modha](https://modha.org/page/2/)）。
- **DNA 存储**：2026 年微软与华盛顿大学演示的全自动 DNA 存储与检索系统实验室写入速度达 400 MB/天，被视为迈向商用吞吐目标的重要里程碑（[DNA Data Storage Market Size, Share & Global Forecast 2026-2035](https://www.snsinsider.com/reports/dna-data-storage-market-6505)）；相关市场报告亦列举 Microsoft Research、Twist Bioscience、Catalog Technologies 等作为主要参与者（[DNA Data Storage Market](https://www.precedenceresearch.com/dna-data-storage-market)）。
- **Pulsar**：官方宣称相比传统 AI 处理器时延低 100 倍、能耗低 500 倍（厂商口径）（[Innatera](https://www.innatera.com/newsroom/innatera-unveils-pulsar-the-worlds-first-mass-market-neuromorphic-microcontroller-for-the-sensor-edge)）。

## 趋势与争议

- **「实验室里程碑」与「规模化商用」之间仍有差距**：神经形态、光计算与 DNA 存储的宣传指标多来自研究原型或厂商口径，实际部署规模、软件生态与编程模型成熟度仍是主要障碍。
- **应用场景分化**：神经形态芯片在超低功耗边缘感知/信号分类上具备明确诉求（如 BrainChip 的亚瓦级持续推理），但其在通用 LLM 训练与推理上尚未替代 GPU。
- **架构路线之争**：数字近存（NorthPole）、模拟/存内计算与光计算三条路线各有主张，尚无统一标准；部分数据为单一团队实验结果，需注意可复现性与口径差异。

## 参考来源

- [Why a decades old architecture decision is impeding the power of AI computing](https://research.ibm.com/blog/why-von-neumann-architecture-is-impeding-the-power-of-ai-computing)
- [下一代人工智能重要突破口是什么?](https://www.jfdaily.com/staticsg/res/html/web/newsDetail.html?id=1176853&sid=11)
- [Intel Builds World's Largest Neuromorphic System to Enable More Sustainable AI](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai)
- [Intel Loihi](https://aiwiki.ai/wiki/intel_loihi)
- [AI Wiki: Neuromorphic Computing](https://aiwiki.ai/wiki/neuromorphic_computing/raw)
- [Dharmendra S. Modha](https://modha.org/page/2/)
- [Charting a path to a more sustainable AI future](https://research.ibm.com/blog/aiu-chip-family-ibm-research)
- [For LLMs, IBM's NorthPole chip overcomes the tradeoff between speed and efficiency](https://research.ibm.com/blog/northpole-llm-inference-results)
- [A Scalable NorthPole System with End-to-End Vertical Integration for Low-Latency and Energy-Efficient LLM Inference](https://arxiv.org/html/2511.15950v1/)
- [BrainChip Announces Commercial Availability and Production Shipments of AKD1500 Neuromorphic Processors](https://brainchip.com/brainchip-announces-commercial-availability-and-production-shipments-of-akd1500-neuromorphic-processors/)
- [BrainChip Unveils Communication Reference Platform, Fueling Signal Intelligence at the Edge](https://brainchip.com/brainchip-unveils-communication-reference-platform-fueling-signal-intelligence-at-the-edge/)
- [BrainChip AKD1500 Now Available in Compact M.2 Form Factor](https://brainchip.com/press/brainchip-akd1500-now-available-in-compact-m-2-form-factor-enabling-fanless-edge-ai-in-industrial-and-commercial-designs/)
- [Innatera unveils Pulsar](https://www.innatera.com/newsroom/innatera-unveils-pulsar-the-worlds-first-mass-market-neuromorphic-microcontroller-for-the-sensor-edge)
- [全球首发256×256芯片，光本位光电混合计算领跑AI算力新纪元](https://m.bjnews.com.cn/detail/1788512736129339.html)
- [DNA Digital Data Storage: How Synthetic Biology Is Building the Ultimate Archive in 2026](https://internet-pros.com/blog/dna-digital-data-storage-2026/)
- [Twist Bioscience SEC Filing](https://investors.twistbioscience.com/node/15331/html)
- [Twist Bioscience spin-off plans Terabyte-scale DNA storage in 2026](https://www.aivanet.com/2025/12/after-nearly-10-years-twist-bioscience-spin-off-plans-terabyte-scale-dna-storage-in-2026-intending-to-store-13tb-of-data-in-a-single-drop-of-water/)
- [DNA Data Storage Market Size, Share & Global Forecast 2026-2035](https://www.snsinsider.com/reports/dna-data-storage-market-6505)
- [DNA Data Storage Market Size, Share and Trends 2026 to 2035](https://www.precedenceresearch.com/dna-data-storage-market)
- [中国科学院院士张旭:类脑智能有望5年内走进千家万户](https://www.stdaily.com/web/gdxw/2026-09/24/content_587047.html)