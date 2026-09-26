# 扩散与图像生成

> 最后更新：2026-09-26 ｜ 领域：AI·生成与多模态 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

扩散模型（Diffusion Model）已成为文生图（Text-to-Image）与图像编辑的主流范式。其核心思想是通过前向加噪与反向去噪学习数据分布，早期由 DDPM（Denoising Diffusion Probabilistic Models）与 DDIM（Denoising Diffusion Implicit Models）奠定基础；随后 Latent Diffusion 将扩散过程搬进潜空间（代表作为 Stable Diffusion），大幅降低算力成本。2022 年 Peebles 与 Xie 提出以 Transformer 替换 U-Net 的 Diffusion Transformer（DiT），此后 DiT 成为 SD3、FLUX、Stable Cascade，以及 Sora、Veo 等模型的主干架构（[Module 86 — Diffusion Deep Dive](https://colab.research.google.com/github/kader-xai/data-science-roadmap/blob/main/module_86_diffusion_deep_dive.ipynb)）。2025–2026 年的代表组合是「latent flow matching + 大规模视觉语言模型」，例如 FLUX.2 将 Mistral-3 24B VLM 与 rectified flow transformer 耦合，使生成与编辑共用同一架构（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)）。

## 最新进展（2025–2026）

- Black Forest Labs 于 2025 年 11 月 25 日发布 FLUX.2 家族，将图像生成与编辑统一进单一架构，基于 latent flow matching，并将 Mistral-3 24B 参数的视觉语言模型（VLM）与 rectified flow transformer 耦合；支持最多 10 张参考图的多参考生成、最高 4MP 输出与复杂文字排版（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)、[FLUX.2 [pro] | [flex]](https://bfl.ai/models/flux-2)）。
- 2026 年 1 月 15 日，Black Forest Labs 发布 FLUX.2 [klein] 系列，把生成与编辑统一进紧凑架构，端到端推理最低可低于 1 秒（[FLUX.2 [klein]: Towards Interactive Visual Intelligence](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence)）。
- 据官方发布记录，2026 年 7 月 23 日 Black Forest Labs 宣布 FLUX 3，定位为跨图像、视频与音频联合训练的多模态基础模型；2026 年 8 月 4 日放出视频能力预览，支持最长 20 秒、1920×1088、24fps 的生成（[Release Notes](https://docs.bfl.ml/release-notes)、[Stable Diffusion review](https://www.scx.hu/reviews/stable-diffusion-review)）。
- Google 方面以 Gemini 图像模型推出 Nano Banana 系列：Nano Banana（Gemini 2.5 Flash Image）主打身份一致性编辑与多图融合，Nano Banana Pro（Gemini 3 Pro Image）支持原生 4K 输出、94%+ 文字渲染准确率、最多 5 人角色一致性与最多 14 张参考图，Nano Banana 2（Gemini 3.1 Flash Image）则以 3–5 秒级速度提供接近 Pro 的质量（[Run Nano Banana on Floyo](https://www.floyo.ai/models/nano-banana)、[Free Nano Banana 2](https://nanobanana2ai.com/)）。
- 阿里 Qwen 系列于 2025 年 8 月发布 20B 参数 MMDiT（Multimodal Diffusion Transformer）图像基础模型 Qwen-Image，宣称在复杂文字渲染上取得突破；2026 年 2 月 10 日升级为更精简的 7B 版本 Qwen-Image 2.0，并于 2026 年 9 月 20 日开源 Qwen-Image-2.1，强调生成质量与推理效率的平衡；此前 2025 年 12 月还推出面向透明图像生成的 Qwen-Image-Layered（[Qwen Image AI](https://qwen3lm.com/image/)、[Qwen-Image-2.1: Compact, Efficient, and Unified Image Creation](https://qwen.ai/blog?id=qwen-image-2.1)、[Qwen Research](https://qwen.ai/research)）。
- **开源可运行性提升**：FLUX.2 提供参考推理代码（GitHub）与 Apache 2.0 许可的 FLUX.2 VAE，并与 NVIDIA、ComfyUI 合作推出面向消费级 GeForce RTX GPU 的 fp8 优化实现；FLUX.2 [dev] 权重也可通过 FAL、Replicate、Runware、TogetherAI、Cloudflare、DeepInfra 等第三方端点采样（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)）。

## 核心技术与关键概念

- **Latent Diffusion / VAE**：在压缩潜空间中扩散以降低计算量。FLUX.2 从零重训新的 VAE 与潜空间，试图同时提升可学习性与图像质量，官方称其为对「可学习性—质量—压缩率」三难问题的推进（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)）。
- **DiT**：以 patchify + Transformer block 处理潜变量，替代 U-Net 主干，在稳定性、可扩展性与多模态支持上具备优势（[Diffusion Transformer(DiT)架构简介](https://blog.csdn.net/sinat_28461591/article/details/148646816)）。
- **控制与适配**：ControlNet 通过附加条件（如边缘图、深度图）控制空间构图，可串联多个 ControlNet；LoRA（低秩适配）则以低成本微调实现风格与主体定制。面向 DiT 的控制研究（如 NanoControl）采用 LoRA 式控制模块与 KV-Context 增强，以降低算力开销（[SwiftDiffusion](https://arxiv.org/html/2407.02031v2)、[NanoControl](https://arxiv.org/html/2508.10424)）。
- **Flow Matching / Rectified Flow**：FLUX.2 建立在 latent flow matching 之上，把生成与编辑合并到单一架构，官方称其重训潜空间是为同时获得更好的可学习性与更高的图像质量（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)）。
- **参数可控推理**：FLUX.2 [flex] 暴露步数（steps）与 guidance scale 等参数，步数从 6 到 50 可换取文字排版精度、图像细节与延迟的权衡（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)）。
- **图像编辑一体化**：FLUX.2 全系列均支持「文本 + 多参考图」的编辑，能在单模型中完成组合、风格化与精修，最高支持 4MP 分辨率下编辑（[FLUX.2](https://bfl.ai/blog/flux-2)）。Nano Banana 系列则以多轮对话式编辑与身份一致性为主要卖点（[Nano Banana AI Image Generator](https://www.goenhance.ai/image-models/nano-banana)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- Black Forest Labs：FLUX.1 / FLUX.2 / FLUX 3（[bfl.ai](https://bfl.ai/blog/flux-2)）。其 FLUX.1 [dev] 被称为全球最受欢迎的开源图像模型（以 Hugging Face 点赞数计），FLUX.1 Kontext [pro] 被 Adobe 至 Meta 等团队采用（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)）。
- Stability AI：Stable Diffusion 3.5（Large 为 8.1B 参数）（[Flux vs Stable Diffusion](https://aitoolfit.ai/fr/compare/flux-vs-stable-diffusion.html)）。评测方面，Stable Diffusion 早期在生成可读文字上表现欠佳，FLUX.1 [dev] 则以「真正可读的文字」为主要差异点（[The Best AI Image Generation Models You Can Run on Your Own GPU in 2026](https://awesomeagents.ai/guides/best-local-image-generation-models-2026/)）。
- Google DeepMind：Nano Banana / Nano Banana Pro（Gemini 3 Pro Image）及网页端应用（[Nano Banana - AI 图像生成平台](https://nanobananana.com/zh)）。
- 阿里巴巴：Qwen-Image 系列（[Qwen Image AI](https://qwen3lm.com/image/)）。
- 开源生态与运行门槛：FLUX 系列可在 ComfyUI 中运行，据 2026 年初的整理需 FluxPipeline 节点与相匹配的 checkpoint；硬件上 4090 适合 Pro、4080 适合 Dev、3080 适合 Schnell（[Flux vs Stable Diffusion 比較](https://my-best.ai/flux-vs-stable-diffusion%E6%AF%94%E8%BC%83%EF%BC%9A%E3%82%AA%E3%83%BC%E3%83%97%E3%83%B3%E3%82%BD%E3%83%BC%E3%82%B9%E7%94%BB%E5%83%8Fai%E5%AF%BE%E6%B1%BA/)）。

## 关键数据与评测结果（附来源）

- FLUX.1 [dev] 为 12B 参数 DiT，搭配 4.5B 的 T5-XXL 文本编码器，可在本地 GPU 运行并生成可读文字（[The Best AI Image Generation Models You Can Run on Your Own GPU in 2026](https://awesomeagents.ai/guides/best-local-image-generation-models-2026/)）。
- FLUX.2 [dev] 被描述为 32B 开源权重模型；FLUX.2 [klein] 9B 属于蒸馏模型，官方给出 GB200 上约 0.5 秒、RTX 5090 上约 2 秒的推理时间与 19.6GB 显存需求（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)、[FLUX.2 [klein]](https://bfl.ai/models/flux-2-klein)）。
- GenEval 是常用的对象中心式文生图基准，覆盖对象共现、空间关系、计数与颜色一致性等维度（[GPT-ImgEval](https://arxiv.org/pdf/2504.02782v1)）。有研究指出 GenEval 已出现显著「基准漂移」，与人类判断的绝对误差最高可达 17.7%，据此提出 GenEval 2（[GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation](https://arxiv.org/html/2512.16853)）。
- **评测指标的局限**：传统自动指标（如 FID、CLIPScore）主要衡量整体图像质量或文图对齐，不适合细粒度或实例级分析，这正是对象中心式基准（如 GenEval）出现的原因（[GPT-ImgEval](https://arxiv.org/pdf/2504.02782v1)）。
- 在 CVPR 2026 一篇论文的对比表中，Playground v3 的 GenEval 得分为 0.76，HiDream-I1-Full 为 0.83（[RAISE](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_RAISE_Requirement-Adaptive_Evolutionary_Refinement_for_Training-Free_Text-to-Image_Alignment_CVPR_2026_paper.pdf)）。

## 趋势与争议

- **版权诉讼**：Getty Images 诉 Stability AI 案中，英国高等法院法官 Joanna Smith 于 2025 年 11 月 4 日作出判决，Getty 在主要版权与数据库权主张上基本败诉，仅获「历史性且极其有限」的商标侵权认定，次要版权侵权主张被驳回；Getty 在结案陈词前放弃了主要版权与数据库权主张（[Getty Images v Stability AI [2025] EWHC 2863 (Ch)](https://www.judiciary.uk/wp-content/uploads/2025/11/Getty-Images-v-Stability-AI.pdf)、[Artificial Intelligence Insight: A win for AI developers?](https://www.milbank.com/a/web/3te6Up1t3XcsvFCCHaNFXL/aXcURC/litigation-client-alert-getty-v-stability-ai.pdf)、[英国高等法院的混合裁决未能解答人工智能侵权的核心问题](https://ipr.mofcom.gov.cn/article/gjxw/ajzz/bqajzz/202511/1993780.html)）。
- **开源权重 vs 闭源**：头部厂商普遍采取「开放核心（Open Core）」策略，同时提供开源权重与商用 API 端点；但部分开源权重受非商用或社区许可限制，规模化商用需另行授权（[FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)、[Flux vs Stable Diffusion](https://aitoolfit.ai/fr/compare/flux-vs-stable-diffusion.html)）。
- **评测饱和**：主流基准随时间漂移、与人类判断脱节，成为图像生成评测的持续争议点（[GenEval 2](https://arxiv.org/html/2512.16853)）。
- **编辑能力成竞争焦点**：Nano Banana 与 Flux Kontext、GPT Image 的对比显示，各家在场景连贯性、角色一致性与身份保持上的差异成为选型关键；有评测称 Nano Banana 在复杂编辑与融合上一致性更强，而 GPT Image 在编辑中有时会改变面部特征（[Nano Banana AI Image Generator](https://www.goenhance.ai/image-models/nano-banana)）。

## 参考来源

- [Module 86 — Diffusion Deep Dive（DiT 与 SD3/FLUX/Sora）](https://colab.research.google.com/github/kader-xai/data-science-roadmap/blob/main/module_86_diffusion_deep_dive.ipynb)
- [FLUX.2: Frontier Visual Intelligence](https://bfl.ai/blog/flux-2)
- [FLUX.2 [pro] | [flex]](https://bfl.ai/models/flux-2)
- [FLUX.2 [klein]: Towards Interactive Visual Intelligence](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence)
- [FLUX.2 [klein]](https://bfl.ai/models/flux-2-klein)
- [Black Forest Labs Release Notes](https://docs.bfl.ml/release-notes)
- [Stable Diffusion review](https://www.scx.hu/reviews/stable-diffusion-review)
- [Flux vs Stable Diffusion 比較](https://aitoolfit.ai/fr/compare/flux-vs-stable-diffusion.html)
- [Flux vs Stable Diffusion比較：オープンソース画像AI対決（my-best.ai）](https://my-best.ai/flux-vs-stable-diffusion%E6%AF%94%E8%BC%83%EF%BC%9A%E3%82%AA%E3%83%BC%E3%83%97%E3%83%B3%E3%82%BD%E3%83%BC%E3%82%B9%E7%94%BB%E5%83%8Fai%E5%AF%BE%E6%B1%BA/)
- [Run Nano Banana on Floyo](https://www.floyo.ai/models/nano-banana)
- [Free Nano Banana 2](https://nanobanana2ai.com/)
- [Nano Banana - AI 图像生成平台](https://nanobananana.com/zh)
- [Qwen Image AI](https://qwen3lm.com/image/)
- [Qwen-Image-2.1: Compact, Efficient, and Unified Image Creation](https://qwen.ai/blog?id=qwen-image-2.1)
- [Qwen Research](https://qwen.ai/research)
- [Nano Banana AI Image Generator](https://www.goenhance.ai/image-models/nano-banana)
- [The Best AI Image Generation Models You Can Run on Your Own GPU in 2026](https://awesomeagents.ai/guides/best-local-image-generation-models-2026/)
- [Diffusion Transformer(DiT)架构简介](https://blog.csdn.net/sinat_28461591/article/details/148646816)
- [SwiftDiffusion: Efficient Diffusion Model Serving with Add-on Modules](https://arxiv.org/html/2407.02031v2)
- [NanoControl: A Lightweight Framework for Precise and Efficient Control in Diffusion Transformer](https://arxiv.org/html/2508.10424)
- [GPT-ImgEval](https://arxiv.org/pdf/2504.02782v1)
- [GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation](https://arxiv.org/html/2512.16853)
- [RAISE (CVPR 2026)](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_RAISE_Requirement-Adaptive_Evolutionary_Refinement_for_Training-Free_Text-to-Image_Alignment_CVPR_2026_paper.pdf)
- [Getty Images v Stability AI [2025] EWHC 2863 (Ch)](https://www.judiciary.uk/wp-content/uploads/2025/11/Getty-Images-v-Stability-AI.pdf)
- [Artificial Intelligence Insight: A win for AI developers? (Milbank)](https://www.milbank.com/a/web/3te6Up1t3XcsvFCCHaNFXL/aXcURC/litigation-client-alert-getty-v-stability-ai.pdf)
- [英国高等法院的混合裁决未能解答人工智能侵权的核心问题](https://ipr.mofcom.gov.cn/article/gjxw/ajzz/bqajzz/202511/1993780.html)