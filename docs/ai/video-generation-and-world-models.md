# 视频生成与世界模型

> 最后更新：2026-09-26 ｜ 领域：AI·生成与多模态 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

视频生成模型在过去两年从「短片段、无声音」快速演进到「多镜头、带原生音频、可交互世界」的阶段。技术路线上，主流模型普遍采用 DiT（Diffusion Transformer）在潜空间做时空去噪，并逐步引入自回归、多模态联合训练与实时交互能力。与之并行的是「世界模型（World Model）」方向：不再只输出一段视频，而是生成可被实时导航、具有持久性（persistent）的 3D 环境。2025–2026 年的关键变化是原生音频成为标配（如 Veo 3.1、可灵 2.6），以及世界模型进入「可实时交互」与「可导出复用」阶段（[Introducing Veo 3.1](https://blog.google/technology/ai/veo-updates-flow/)、[Kling AI Models Compared (2026)](https://www.kling4.co/blog/kling-ai-models-compared-2026)、[World model](https://aiwiki.ai/wiki/world_model)、[Marble: A Multimodal World Model](https://www.worldlabs.ai/blog/marble-world-model)）。

## 最新进展（2025–2026）

- OpenAI 于 2025 年 9 月发布 Sora 2，支持文生视频与图生视频、最高 1080p、时长约 20–25 秒并带原生同步音频，强调物理一致性与多镜头叙事；Google DeepMind 于 2025 年 5 月发布 Veo 3，定位最高 4K、60fps、时长可达 2 分钟并集成音频（[Sora 2 vs Veo 3](https://geniostack.com/sora-2-vs-veo-3/)、[Veo 3 vs Sora](https://pxz.ai/blog/veo-3-vs-sora-2)）。
- Google 于 2025 年 10 月 16 日推出 Veo 3.1，提升音频、叙事控制与真实质感，支持生成 720p/1080p、最长 148 秒的片段，并集成进 Flow 平台、Gemini API 与 Vertex AI（[Introducing Veo 3.1 and advanced capabilities in Flow](https://blog.google/technology/ai/veo-updates-flow/)、[Veo 3.1 百科](https://m.baike.com/wiki/Veo%203.1/7563118069347041330)）。
- OpenAI 于 2026 年 3 月 24 日宣布 Sora 停运，Sora 应用与网页版于 2026 年 4 月 26 日关闭，Sora API 于 2026 年 9 月 24 日终止；外部报道将原因归结为大规模高保真视频生成的算力成本与训练数据相关的法律摩擦（[Sora API Shuts Down September 24, 2026](https://twinailabs.com/pt/blog/sora-api-shutdown-september-2026)、[Veo 3.1 vs Sora](https://mstudio.ai/vs/veo-3-vs-sora)、[Sora — Discontinued](https://aiproplaybook.com/learn/module-6/section-6-124)）。
- 快手可灵（Kling）持续迭代：据整理，2.1 于 2025 年 5 月发布，2.5 Turbo 于 2025 年 9 月降价，2.6 于 2025 年 12 月引入运动控制、30 秒与原生音频，3.0 于 2026 年 1 月支持原生多模态、多镜头与 4K；官方更新记录显示 2026 年 2 月 25 日上线 3.0 Omni 与 V3 模型（[Kling AI Models Compared (2026)](https://www.kling4.co/blog/kling-ai-models-compared-2026)、[可灵 AI 更新通知](https://app.klingai.com/cn/dev/document-api/apiReference/updateNotice)）。
- 世界模型方面，Google DeepMind 的 Genie 3 于 2025 年 8 月发布，据其描述是「首个支持实时交互的世界模型」，可在文本提示下生成 720p、24fps、可实时导航并保持数分钟一致性的动态世界；Google 通过 Project Genie 面向美国 AI Ultra 订阅者开放该原型（[World model](https://aiwiki.ai/wiki/world_model)、[Лучшие ИИ-модели мира в 2026 году](https://thehappyoyster.com/ru/best-ai-world-models/)）。李飞飞团队 World Labs 推出首个产品 Marble，可从文本、图像、视频或 360 全景生成空间一致、高保真且持久可编辑的 3D 世界（[World Labs](https://www.worldlabs.ai/)、[Marble: A Multimodal World Model](https://www.worldlabs.ai/blog/marble-world-model)）。
- **规格对照**：据 2026 年 9 月的整理，Sora 2 / Sora 2 Pro 基础分辨率为竖屏 720×1280、横屏 1280×720；Veo 3.1 各档以 720p 为基线，并在 2026 年 9 月对标准版/快速版在 Gemini API 做了刷新；Kling 3.0 Turbo 与 Omni 于 2026 年 6 月 17 日发布，免费档为 720p（[Sora 2 vs Veo 3.1 vs Kling 3.0](https://tech-insider.org/ca/sora-2-vs-veo-3-1-vs-kling-3-0-2026/)）。Veo 3.1 支持 4s、6s、8s 时长与 24fps，分辨率覆盖 720p、1080p 与 4K（[Veo 3.1](https://aistudio.google.com/models/veo-3)）。

## 核心技术与关键概念

- **时空建模**：可灵 Kling 2.5 Pro 采用 3D 时空联合注意力机制（3D Spatiotemporal Joint Attention），以理解物体在三维空间中随时间的运动规律（[Kling 2.5 Pro](https://kunya.ai/models/kling-2.5-pro)）。
- **原生音频**：Veo 3.1 首次将音频带入「Ingredients to Video」「Frames to Video」「Extend」等既有能力，使音画上下文匹配（[Introducing Veo 3.1](https://blog.google/technology/ai/veo-updates-flow/)）。
- **多模态联合训练**：Black Forest Labs 的 FLUX 3 定位为跨图像、视频与音频联合训练的多模态基础模型，视频预览支持最长 20 秒、1920×1088、24fps（[Release Notes](https://docs.bfl.ml/release-notes)）。
- **世界模型表示**：Marble 生成的 3D 世界以 Gaussian splats 渲染，也可导出为 mesh 供游戏、VFX 与设计管线复用（[Best World Models in 2026](https://ltx.io/blog/best-world-models)）。
- **流式音视频**：出现专门面向流式音视频生成的基准 StreamAV-Bench，含「渐进式」与「交互式」两条赛道，评估指令逐步遵循、长时序稳定、状态保持与复用等能力（[StreamAV-Bench](https://hub.baai.ac.cn/paper/b1452f8c-eb90-493c-b96a-ffe3b587f0cd)）。
- **视觉记忆与持久性**：Genie 3 的官方描述称其维持对环境的视觉记忆，从而在数分钟内保持一致性，这是「可交互世界」区别于一次性视频生成的关键（[World model](https://aiwiki.ai/wiki/world_model)）。
- **多模态可控世界生成**：Marble 支持从文本、图像、视频或粗略 3D 布局创建世界，并允许交互式编辑、扩展与合并；生成结果可导出用于其他管线（[Marble: A Multimodal World Model](https://www.worldlabs.ai/blog/marble-world-model)、[World Labs](https://www.worldlabs.ai/)）。
- **音画上下文匹配**：Veo 3.1 将音频引入既有能力（Ingredients to Video、Frames to Video、Extend），使声音与画面在上下文中配对，提升沉浸感与写实度（[Introducing Veo 3.1 and advanced capabilities in Flow](https://blog.google/technology/ai/veo-updates-flow/)）。
- **多镜头与叙事连续性**：Sora 2 强调物理真实感与叙事连续性，并在时间一致性与多镜头能力上大幅改进；Veo 3.1 则提供更细粒度的编辑控制与更强的叙事控制（[Veo 3 vs Sora](https://pxz.ai/blog/veo-3-vs-sora-2)、[Introducing Veo 3.1](https://blog.google/technology/ai/veo-updates-flow/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- OpenAI：Sora / Sora 2（已于 2026 年停运）。
- Google DeepMind：Veo 3 / Veo 3.1（[blog.google](https://blog.google/technology/ai/veo-updates-flow/)）。
- 快手：可灵 AI Kling 系列（[可灵 AI 开放平台](https://app.klingai.com/cn/dev/document-api/apiReference/updateNotice)）。
- 阿里巴巴：通义万相（Wan）系列，2025 年 2 月 25 日全面开源万相 2.1（[阿里开源万相 2.1](http://m.toutiao.com/group/7475531742238310949/)）。
- World Labs：Marble 世界模型（[worldlabs.ai](https://www.worldlabs.ai/)）。
- Google DeepMind：Genie 3 世界模型（[World model](https://aiwiki.ai/wiki/world_model)）。

## 关键数据与评测结果（附来源）

- 可灵 AI 商业化数据：据快手 2026 年第一季度演示材料，2026 年第一季度可灵 AI 营业收入超过 6.5 亿元人民币、同比增长 300%；2026 年 3 月可灵 AI 的 ARR 接近 5 亿美元（[快手科技 2026 年第一季度演示材料](https://ir.kuaishou.com/static-files/f366a227-eddf-4e56-9cfa-f544e9503303)）。
- VBench 是视频生成的权威评测集，含 16 个评分维度。有报道称通义万相以总分 84.7% 登顶 VBench；另有报道称万相 2.1 在 VBench 上以总分 86.22% 位居榜首；亦有论文称 Lumos-Nexus 以 84.12 分刷新 VBench——三者口径与评测版本、时间不同，仅作并列呈现（[通义万相重磅升级](http://m.toutiao.com/group/7457820753539383817/)、[阿里开源万相 2.1](http://m.toutiao.com/group/7475531742238310949/)、[ECCV 2026 Lumos-Nexus](https://m.sohu.com/a/1079292602_100279313/)）。
- 物理一致性仍是薄弱环节，出现针对物理推理的专门评估与改进工作（如 ProPhy 在 VBench 的 Dynamic Degree 指标上显著提升）（[生成视频总出物理 bug?](http://m.toutiao.com/group/7618882740896793107/)）。

## 趋势与争议

- **产品退出**：Sora 的停运表明，高保真视频生成在算力成本与训练数据法律风险上的压力可能超过商业收益，头部厂商战略随之调整（[Sora API Shuts Down September 24, 2026](https://twinailabs.com/pt/blog/sora-api-shutdown-september-2026)）。
- **世界模型路线分歧**：一派追求实时可交互的视频式世界（如 Genie 3），一派追求可导出、可复用的持久 3D 资产（如 Marble），两者在一致性、可控性与工程可用性上各有取舍（[World model](https://aiwiki.ai/wiki/world_model)、[Best World Models in 2026](https://ltx.io/blog/best-world-models)）。
- **评测分歧**：VBench 等基准存在多版本、多口径并存，且物理规律、长时序一致性与音画同步的度量仍缺乏统一共识（[StreamAV-Bench](https://hub.baai.ac.cn/paper/b1452f8c-eb90-493c-b96a-ffe3b587f0cd)、[生成视频总出物理 bug?](http://m.toutiao.com/group/7618882740896793107/)）。
- **开源与闭源并进**：阿里于 2025 年 2 月全面开源万相 2.1，并在 VBench 上登顶，说明开源视频模型已进入第一梯队，与闭源商业模型形成直接竞争（[阿里开源万相 2.1](http://m.toutiao.com/group/7475531742238310949/)）。

## 参考来源

- [Sora 2 vs Veo 3: Best AI Video Generator Compared](https://geniostack.com/sora-2-vs-veo-3/)
- [Veo 3 vs Sora: Real Testing, Pricing, Quality & Best Use Cases](https://pxz.ai/blog/veo-3-vs-sora-2)
- [Introducing Veo 3.1 and advanced capabilities in Flow](https://blog.google/technology/ai/veo-updates-flow/)
- [Veo 3.1](https://aistudio.google.com/models/veo-3)
- [Introducing Veo 3.1 相关更新（Gemini Drop October 2025）](https://blog.google/products-and-platforms/products/gemini/gemini-drop-october-2025/)
- [Sora 2 vs Veo 3.1 vs Kling 3.0](https://tech-insider.org/ca/sora-2-vs-veo-3-1-vs-kling-3-0-2026/)
- [Лучшие ИИ-модели мира в 2026 году](https://thehappyoyster.com/ru/best-ai-world-models/)
- [Veo 3.1 百科](https://m.baike.com/wiki/Veo%203.1/7563118069347041330)
- [Sora API Shuts Down September 24, 2026](https://twinailabs.com/pt/blog/sora-api-shutdown-september-2026)
- [Veo 3.1 vs Sora](https://mstudio.ai/vs/veo-3-vs-sora)
- [Sora — Discontinued](https://aiproplaybook.com/learn/module-6/section-6-124)
- [Kling AI Models Compared (2026)](https://www.kling4.co/blog/kling-ai-models-compared-2026)
- [可灵 AI 更新通知](https://app.klingai.com/cn/dev/document-api/apiReference/updateNotice)
- [Kling 2.5 Pro](https://kunya.ai/models/kling-2.5-pro)
- [快手科技 2026 年第一季度演示材料](https://ir.kuaishou.com/static-files/f366a227-eddf-4e56-9cfa-f544e9503303)
- [World Labs](https://www.worldlabs.ai/)
- [Marble: A Multimodal World Model](https://www.worldlabs.ai/blog/marble-world-model)
- [World model](https://aiwiki.ai/wiki/world_model)
- [Best World Models in 2026 (Open & Closed)](https://ltx.io/blog/best-world-models)
- [StreamAV-Bench](https://hub.baai.ac.cn/paper/b1452f8c-eb90-493c-b96a-ffe3b587f0cd)
- [通义万相重磅升级](http://m.toutiao.com/group/7457820753539383817/)
- [大模型开源卷至视频生成领域：阿里开源万相 2.1](http://m.toutiao.com/group/7475531742238310949/)
- [ECCV 2026 Lumos-Nexus](https://m.sohu.com/a/1079292602_100279313/)
- [生成视频总出物理 bug?](http://m.toutiao.com/group/7618882740896793107/)
- [Black Forest Labs Release Notes](https://docs.bfl.ml/release-notes)