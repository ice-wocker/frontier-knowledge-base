# 机器人与具身智能

> 最后更新：2026-09-26 ｜ 领域：机器人与具身智能 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

具身智能（Embodied AI）指让智能体通过物理身体与环境交互、感知并执行任务的技术方向，其核心载体是人形机器人（Humanoid Robot）以及各类通用操作机器人。2023 年以来，随着视觉-语言-动作（Vision-Language-Action，VLA）大模型的出现，机器人从"预编程自动化"走向"通用策略学习"，2025–2026 年则进入从原型演示到量产与商业部署的关键转折期。业界普遍把 2026 年称为人形机器人的"量产元年"，其标志是特斯拉 Optimus 进入量产、宇树科技登陆 A 股科创板、以及大量消费级与工业级机型开始批量交付。

## 2025–2026 最新进展

**特斯拉 Optimus 进入 V3 量产阶段。** 特斯拉在 2025 年第四季度及全年更新中表示，Optimus 项目在 2025 年取得进展，计划于 2026 年第一季度发布 Gen 3 版本，该版本相对 2.5 版有重大升级（包括最新的手部设计），并称"第一代量产线正在安装，为量产做准备"（[Tesla Q4 and FY 2025 Update](https://static.seekingalpha.com/uploads/sa_presentations/536/120536/original.pdf)）。多个行业追踪来源称，特斯拉于 2026 年夏季在 Fremont 工厂启动 Optimus V3 量产，此前该产线完成了 Model S/X 停产后的改造，Optimus 与 FSD 共用视觉神经网络与自研 AI 芯片（[读懂马斯克 · 擎天柱 Optimus](https://readmusk.com/optimus)）。

**宇树科技成为"A 股人形机器人第一股"。** 根据公司公告，宇树科技于 2026 年 8 月 19 日登陆科创板（代码 688836），发行价 150.8 元/股，对应发行市值约 610 亿元，首发募资约 61 亿元（[上海证券报：宇树科技将于8月19日科创板上市](https://www.stcn.com/article/detail/4082146.html)）。招股书显示，2025 年公司实现营业收入 16.99 亿元、扣非后净利润 5.9 亿元，并实现人形机器人出货量全球第一（[宇树科技科创板上市招股说明书](http://big5.sse.com.cn/site/cht/www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2026-08-14/688836_20260814_AJKD.pdf)）；2026 年上半年预计营业收入 10.52 亿–11.28 亿元（[上海证券报](https://www.stcn.com/article/detail/4082146.html)）。

**国内形成 IPO 潮。** 截至 2026 年 7 月，国内已有超 20 家人形机器人核心企业进入 IPO 辅导、申报、聆讯或发行阶段，2026 年以来国内机器人领域融资达 391 起，多家券商认为 2026 年有望成为国产机器人主机厂的"IPO 元年"（[中国日报网：人形机器人2026年上半年复盘](http://cn.chinadaily.com.cn/a/202607/15/WS6a56f4dba310d709c2fbd8f1.html)）。

**国际头部企业加速资本化与交付。** Agility Robotics 宣布与 Churchill Capital Corp XI 合并上市，交易预计带来逾 6.2 亿美元总收益（含 Churchill XI 信托账户 4.2 亿美元及约 2 亿美元 PIPE，由 Foxconn 领投）（[Agility Robotics to Go Public](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)）。Figure AI 在 2025 年 9 月的 C 轮后估值达到 390 亿美元，较 2024 年 2 月的 26 亿美元增长约 15 倍（[Top Humanoid Robotics Startups Funded in 2026](https://aifundingtracker.com/top-humanoid-robotics-startups-funded/)）。

**国家级政策落地。** 2026 年 6 月 9 日，工业和信息化部、国务院国资委联合印发通知，启动 2026 年度人形机器人与具身智能实景实训专项行动，提出到 2026 年底人形机器人等重点产品在一批代表性场景率先完成应用验证和常态部署，形成百个以上高价值应用场景，带动形成万台级规模落地能力（[中国政府网：人形机器人与具身智能实景实训专项行动启动](https://www.gov.cn/lianbo/202606/content_7071714.htm)、[工信部通知原文](https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2026/art_f291ccd3da4c47ce95741de63cc088e6.html)）。

## 核心技术与关键概念

**VLA（Vision-Language-Action）模型。** VLA 模型将视觉感知、语言理解与机器人控制统一到端到端框架中。早期工作 RT-1、RT-2 验证了大规模 Transformer 机器人策略学习以及将视觉-语言预训练知识迁移到机器人控制的可行性，后续开源模型 OpenVLA、Octo 进一步推动了 VLA 架构与训练范式（[VLAFlow, arXiv](https://arxiv.org/pdf/2607.01586v2)）。

**双系统（System 1 / System 2）架构。** 当前主流基础模型多采用"慢思考 + 快执行"的双系统设计。NVIDIA GR00T N1 即为双系统模型，利用异构训练数据并支持多种机器人形态（跨形态，cross-embodiment）（[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots, arXiv](https://arxiv.org/html/2503.14734v2)）。Google DeepMind 的 Gemini Robotics 系列同样采用"VLA 模型 + 具身推理（ER）模型"分工协作的系统结构（[Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)）。

**仿真与 Sim2Real。** NVIDIA Isaac Sim / Isaac Lab 与开源物理引擎 Newton 构成训练与评估基础设施。NVIDIA 宣布开源 Newton 物理引擎已可在 Isaac Lab 中使用，并推出 Isaac GR00T N1.6 推理型 VLA 模型（[NVIDIA Accelerates Robotics R&D With New Open Models and Simulation Libraries](https://nvidianews.nvidia.com/_gallery/download_pdf/68da9f263d6332a3dba5f16c/)）。在评估侧，RoboLab 等仿真基准被用于在训练/评估无视觉重叠的条件下评测通用策略（[How to Evaluate General-Purpose Robot Policies, NVIDIA](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/)）。

**具身数据集与基准。** Open X-Embodiment 汇集了来自多机构、多机器人平台的操作数据，并训练出 RT-X 系列模型；其中 RT-2-X 在涌现技能评测中相比 RT-2 提升约 3 倍（[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://robotics-transformer-x.github.io/)）。此外还出现了 DexVerse 等面向多任务、多形态灵巧操作的模块化基准（[DexVerse, arXiv](https://arxiv.org/html/2607.08751)）。

## 代表性项目/公司

- **特斯拉 Tesla Optimus**：与 FSD 共用视觉神经网络与自研 AI 芯片，V3 于 2026 年夏季在 Fremont 开始量产（[读懂马斯克 · Optimus](https://readmusk.com/optimus)）。
- **Figure AI**：估值 390 亿美元（2025 年 9 月 C 轮），为全球融资额最高的纯人形机器人公司（[aifundingtracker](https://aifundingtracker.com/top-humanoid-robotics-startups-funded/)）。
- **宇树科技 Unitree**：官网 https://www.unitree.com ；2025 年人形机器人出货量全球第一，2026 年 8 月科创板上市（[上海证券报](https://www.stcn.com/article/detail/4082146.html)）。
- **Agility Robotics**：Digit 已在九个付费客户站点部署，并通过 SPAC 上市（[The Robotic Life](https://theroboticlife.com/top-10-humanoid-robot-startups-2026/)、[Agility Robotics](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)）。
- **NVIDIA Isaac GR00T**：https://developer.nvidia.com/isaac/gr00t ，开放的人形机器人参考平台与基础模型（[NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t)）。
- **Google DeepMind Gemini Robotics**：https://deepmind.google/models/gemini-robotics/ ，Gemini Robotics 2 可控制从脚趾到指尖的完整人形机器人（[Gemini Robotics 2](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)）。
- **Physical Intelligence (π)**：https://www.pi.website/ ，2026 年 4 月 16 日发布可操控基础模型 π0.7，称为在泛化性上出现阶跃式提升（[Physical Intelligence](https://www.pi.website/)）；公司累计融资约 10.7 亿美元，含 2025 年 11 月由 CapitalG 领投的 6 亿美元 B 轮，估值约 56 亿美元（[usagepricing](https://www.usagepricing.com/blueprint/physical-intelligence)）。
- **其他被提及玩家**：1X、Apptronik、Sanctuary AI、UBTECH、Fourier Intelligence 等（[The Robotic Life](https://theroboticlife.com/top-10-humanoid-robot-startups-2026/)）。

## 关键数据

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 宇树科技 2025 年营业收入 | 16.99 亿元，扣非净利润 5.9 亿元 | [招股说明书](http://big5.sse.com.cn/site/cht/www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2026-08-14/688836_20260814_AJKD.pdf) |
| 宇树科技发行市值 | 约 610 亿元（发行价 150.8 元/股） | [上海证券报](https://www.stcn.com/article/detail/4082146.html) |
| Figure AI 估值 | 390 亿美元（2025 年 9 月 C 轮） | [aifundingtracker](https://aifundingtracker.com/top-humanoid-robotics-startups-funded/) |
| Agility SPAC 交易总收益 | 逾 6.2 亿美元 | [Agility Robotics](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi) |
| 全球人形机器人出货量预测 | 2026 年 7.5 万台 → 2030 年约 89 万台 → 2035 年约 650 万台 | [财联社/高盛](https://www.cls.cn/detail/2469961) |
| 2035 年人形机器人市场规模预测 | 约 1383 亿美元 | [财联社/高盛](https://www.cls.cn/detail/2469961) |

## 趋势与争议

1. **量产与"演示"的落差**：尽管 Optimus、宇树等已进入量产或批量交付，但多数机型仍主要面向科研、自有工厂或试点客户。有分析指出，Unitree 收入中相当比例来自科研用途而非工业生产（[tooldirectory](https://tooldirectory.ai/compare/tesla-optimus-vs-unitree-robotics)）。"能否真正规模化替代人力"仍是核心质疑。
2. **成本与供应链**：降低成本依赖 BOM（物料清单）下降与供应链成熟。高盛认为出货量提升与 BOM 成本降低将加快盈利路径（[Goldman Sachs: Humanoid Robot, The AI accelerant](https://www.goldmansachs.com/intelligence/pages/gs-research/global-automation-humanoid-robot-the-ai-accelerant/report.pdf)）。
3. **技术路线之争**：端到端 VLA 大模型 vs. 分层/模块化控制；纯数据驱动 vs. 仿真强化学习；双系统架构中"具身推理"与"动作生成"如何分工，仍是活跃研究方向（[Gemini Robotics 1.5 tech report, arXiv](https://arxiv.org/html/2510.03342v3)）。
4. **数据瓶颈**：高质量真实操作数据稀缺，Open X-Embodiment 等跨机构数据合作为重要路径，但数据规模、形态覆盖与标注标准仍未统一（[Open X-Embodiment](https://robotics-transformer-x.github.io/)）。
5. **政策与标准**：中国已发布首个覆盖人形机器人与具身智能全产业链、全生命周期的国家级标准体系，由 120 余家单位联合编制，涵盖基础共性、类脑与智算、肢体与部组件、整机与系统、应用、安全伦理六大板块（[中国具身智能行业洞察报告](https://pdf.dfcfw.com/pdf/H3_AP202607221827240551_1.pdf)）。标准化与安全伦理将成为商业化前置条件。

## 参考来源

1. [Tesla Q4 and FY 2025 Update](https://static.seekingalpha.com/uploads/sa_presentations/536/120536/original.pdf)
2. [读懂马斯克 · 擎天柱 Optimus：特斯拉机器人量产与进展](https://readmusk.com/optimus)
3. [上海证券报：宇树科技将于8月19日科创板上市](https://www.stcn.com/article/detail/4082146.html)
4. [宇树科技股份有限公司首次公开发行股票并在科创板上市招股说明书](http://big5.sse.com.cn/site/cht/www.sse.com.cn/disclosure/listedinfo/announcement/c/new/2026-08-14/688836_20260814_AJKD.pdf)
5. [中国日报网：人形机器人2026年上半年复盘——商业化拐点已现、技术发展超预期](http://cn.chinadaily.com.cn/a/202607/15/WS6a56f4dba310d709c2fbd8f1.html)
6. [Agility Robotics to Go Public Through Merger with Churchill Capital Corp XI](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)
7. [Top Humanoid Robotics Startups Funded in 2026](https://aifundingtracker.com/top-humanoid-robotics-startups-funded/)
8. [中国政府网：人形机器人与具身智能实景实训专项行动启动](https://www.gov.cn/lianbo/202606/content_7071714.htm)
9. [工信部：两部门关于联合开展2026年度人形机器人与具身智能实景实训专项行动的通知](https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2026/art_f291ccd3da4c47ce95741de63cc088e6.html)
10. [VLAFlow: A Unified Training Framework for Vision-Language-Action Models, arXiv](https://arxiv.org/pdf/2607.01586v2)
11. [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots, arXiv](https://arxiv.org/html/2503.14734v2)
12. [Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)
13. [NVIDIA Accelerates Robotics Research and Development With New Open Models and Simulation Libraries](https://nvidianews.nvidia.com/_gallery/download_pdf/68da9f263d6332a3dba5f16c/)
14. [How to Evaluate General-Purpose Robot Policies for Real-World Deployment, NVIDIA](https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/)
15. [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://robotics-transformer-x.github.io/)
16. [DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation, arXiv](https://arxiv.org/html/2607.08751)
17. [The Robotic Life: Top 10 Humanoid Robot Startups Pulling Ahead in 2026](https://theroboticlife.com/top-10-humanoid-robot-startups-2026/)
18. [NVIDIA Isaac GR00T](https://developer.nvidia.com/isaac/gr00t)
19. [Gemini Robotics (Google DeepMind)](https://deepmind.google/models/gemini-robotics/)
20. [Physical Intelligence (π)](https://www.pi.website/)
21. [Physical Intelligence 融资概况 (usagepricing)](https://www.usagepricing.com/blueprint/physical-intelligence)
22. [财联社海外研选：高盛上调人形机器人预期，2035年出货650万台](https://www.cls.cn/detail/2469961)
23. [Goldman Sachs: Global Automation — Humanoid Robot: The AI accelerant](https://www.goldmansachs.com/intelligence/pages/gs-research/global-automation-humanoid-robot-the-ai-accelerant/report.pdf)
24. [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots, arXiv](https://arxiv.org/html/2510.03342v3)
25. [中国具身智能行业洞察报告：从能力底座到场景落地](https://pdf.dfcfw.com/pdf/H3_AP202607221827240551_1.pdf)