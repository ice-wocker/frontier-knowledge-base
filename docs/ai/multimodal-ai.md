# 多模态 AI（Multimodal AI）

> 最后更新：2026-09-26 ｜ 领域：人工智能 / 多模态模型与生成 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 一、概述

多模态 AI 指同时理解与生成文本、图像、音频、视频乃至 3D 世界的模型体系。2025–2026 年的主线是「**原生多模态（native multimodal）**」——不再把视觉/语音作为外挂模块，而是在同一模型内统一建模；与此同时，图像生成、视频生成、实时语音对话与「世界模型（world model）」四条产品线并行爆发，多模态能力成为前沿模型的默认配置而非附加项。

## 二、2025–2026 最新进展

- **前沿模型全面多模态化**。OpenAI 的 GPT-5 系列强调「基于图像与其他非文本输入进行更准确推理」，可解读图表、总结演示文稿照片并回答与图示相关的问题（[Introducing GPT-5](https://openai.com/hu-HU/index/introducing-gpt-5/)）。OpenAI 后续推出 GPT-5.4，称其与既有模型「智能相同、只是更快」，但 API 单价高于 GPT-5.2，并用更高的 token 效率降低总用量（[Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)）。
- **Google Gemini 3 系列**将图像生成与视觉理解进一步原生整合：官方发布原生视觉模型 **Gemini 3.1 Flash Image** 与 **Gemini 3 Pro Image** 的正式版（GA），支持以视频（含 YouTube 链接）作为多模态上下文做「视频转图片」生成；Gemini 3 引入 `media_resolution` 参数，可精细控制每张图片/视频帧分配的 token 上限，并支持最高 2K/4K 分辨率与文本渲染（[Gemini API 版本说明](https://ai.google.dev/gemini-api/docs/changelog)、[Gemini 3 开发者指南](https://ai.google.dev/gemini-api/docs/gemini-3)）。
- **开放权重多模态**由阿里 Qwen 引领：Qwen3-VL 提供 2B/4B/8B/32B/30B-A3B/235B-A22B 多档规模，上下文 256K 可扩展至 1M，支持文本·图像·视频输入，采用 Apache 风格开放权重（[Qwen VL](https://qwen3lm.com/qwen-vl/)）。官方博客强调其可识别名人、食物、植物、动物、汽车品牌与动漫角色，并强化多图多轮对话中的上下文保持（[Qwen3-VL: Sharper Vision, Deeper Thought, Broader Action](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef)）。
- **实时语音对话**进入全双工时代：OpenAI 发布 **GPT-Live**，称这是新一代语音模型，基于**全双工（full-duplex）架构**，可边听边说，并用「嗯」「对」这类语气词表明在倾听（[Presentamos GPT-Live](https://openai.com/es-419/index/introducing-gpt-live/)）。
- **世界模型成为新战场**：Google DeepMind 的 **Genie 3** 是通用世界模型，用简单文本即可生成可实时探索的逼真环境；World Labs 的 **Marble** 从文本、图像、视频或 360 全景生成可持久存在的 3D 世界（[Genie 3](https://deepmind.google/models/genie/)、[World Labs](https://www.worldlabs.ai/)）。

## 三、核心技术与关键概念

- **原生多模态 vs 拼接式**：原生模型在一个架构内对齐多种模态的表征，减少「视觉编码器 + LLM」拼接带来的信息损失；Gemini 3 的 `media_resolution` 说明厂商开始把「视觉 token 预算」显式暴露为可调参数（[Gemini 3 Developer Guide](https://goo.gle/3Y3qDr8)）。
- **图像生成**：扩散模型与流匹配（flow matching）并存。Black Forest Labs 的 **FLUX.2**（2025 年 11 月发布，2026 年 1 月补充 FLUX.2 [klein] 家族）据称在 4 百万像素分辨率下保持一致性，并支持最多 10 张参考图用于角色与风格一致（[Best AI image generators 2026](https://genai.club/blog/best-ai-image-generators-2026)）。文本渲染与版式能力成为差异化重点（Ideogram 3.0 等）（[Best AI Image Generators](https://aionx.co/ai-comparisons/ai-image-generators-comparison/)）。
- **视频生成**：主流模型在时长、分辨率与是否原生音频上分层。据整理对比，**Sora 2**（OpenAI，2025 年 9 月）最长 20 秒、1080p、同步音频；**Veo 3.1**（Google DeepMind，2025 年 10 月）8 秒可延长、原生对白与音效；**Runway Gen-4.5** 约 10 秒、强物理与角色一致性（[AI Video Generation](https://aiwiki.ai/wiki/ai_video_generation/edit)）。另有对比指出 Veo 3 在画质与音频领先、Seedance 2.0 在速度与角色一致性见长、Kling 3 在动态运动与低价上占优（[Sora 2 vs Veo 3 vs Seedance 2.0](https://www.seedance-25.ai/blog/sora-2-vs-veo-3-vs-seedance)、[Sora 2 vs Veo 3 vs Runway Gen-4 vs Kling 3](https://kursvideoai.pl/en/blog/sora-vs-veo-vs-runway-vs-kling/)）。
- **世界模型**：目标是让模型预测世界如何演化、行动如何影响环境。Genie 3 自称在「世界模拟」方向实现重大跃升（[Genie 3](https://deepmind.google/models/genie/)）；World Labs 提出端到端「Real-to-sim-to-real（R2S2R）」以训练机器人，并于 2026 年 9 月发布面向空间智能的 omnimodal 世界模型 **Atlas**（[World Labs Research & Insights](https://www.worldlabs.ai/blog)）。
- **多模态评测**：**MMMU-Pro** 通过更稳健的设置抑制了模型在原始 MMMU 上可能利用的捷径与猜测策略，且发现思维链（CoT）提示普遍提升表现（[MMMU-Pro](https://arxiv.org/html/2409.02813)）。

## 四、代表性项目 / 产品

| 类别 | 项目 / 产品 | 官方链接 |
| --- | --- | --- |
| 通用多模态 LLM | OpenAI GPT-5 系列 | https://openai.com/index/introducing-gpt-5/ |
| 通用多模态 LLM | Google Gemini 3 系列 | https://ai.google.dev/gemini-api/docs/gemini-3 |
| 开放权重 VLM | 阿里 Qwen3-VL / Qwen3-Omni | https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef |
| 图像生成 | Black Forest Labs FLUX.2 | https://bfl.ai/ |
| 视频生成 | OpenAI Sora 2 | https://openai.com/sora/ |
| 视频生成 | Google DeepMind Veo 3.1 | https://deepmind.google/models/veo/ |
| 视频生成 | 快手 可灵 Kling、字节 Seedance | https://klingai.com/ |
| 实时语音 | OpenAI GPT-Live | https://openai.com/index/introducing-gpt-live/ |
| 世界模型 | Google DeepMind Genie 3 | https://deepmind.google/models/genie/ |
| 世界模型 | World Labs Marble / Atlas | https://www.worldlabs.ai/ |

> 注：上表除检索结果直接给出的页面外，部分为厂商客观存在的官方站点域名，具体页面以厂商发布为准。

## 五、关键数据与评测结果

- **MMMU-Pro（OpenAI 官方评测表）**：GPT-5.6 Sol 83%、GPT-5.6 Terra 80.7%、GPT-5.6 Luna 78.4%、GPT-5.5 81.2%、Gemini 3.1 Pro Preview 80.5%（[GPT-5.6 — OpenAI](https://openai.com/index/gpt-5-6/)）。
- **MMMU-Pro 排行榜（BenchLM，2026-09-24）**：Gemini 3.1 Pro 以 **83.9%** 居首，其后为 Gemini 3.5 Flash（83.6%）与 GPT-5.6 Sol（83%）（[MMMU-Pro — BenchLM](https://benchlm.ai/benchmarks/mmmu-pro)）。
- **MMMU-Pro 排行榜（Artificial Analysis，2026-09-18 前后）**：AA-MMMU-Pro 上 GPT-6 Astra 以 **86.9%** 领先，其后为 Gemini 3.8 Flash（85.6%）；Artificial Analysis 另列出 Claude Opus 5.5 在 MMMU-Pro 上达 **88%**（[AA-MMMU-Pro](https://benchlm.ai/benchmarks/aammmupro)、[MMMU-Pro Benchmark Leaderboard](https://artificialanalysis.ai/evaluations/mmmu-pro)）。

> 不同榜单因评测口径、工具调用与推理预算设置不同而给出不一致的排名，引用时需注明来源与日期。

- **视频模型参数**：Sora 2 最长 20s/1080p/同步音频；Veo 3.1 8s（可延长）/1080p（可 4K 放大）/原生对白+音效；Runway Gen-4.5 约 10s/1080p（[AI Video Generation](https://aiwiki.ai/wiki/ai_video_generation/edit)）。
- **Gemini 3 Flash 规格**：上下文窗口 1,048,576 token，最大输出 65,536 token，文本输入输出、图像/音频/视频仅输入（[Gemini 3 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash)）。

## 六、趋势与争议

1. **原生多模态 vs 模态专用模型之争**：通用模型持续吞并图像/视频生成能力，但专用工具（FLUX、Midjourney、可灵等）在特定质量维度仍领先，「通才够用、专才够好」并存。
2. **世界模型是通向具身智能的桥梁还是营销概念**：Genie 3、Atlas 等强调对物理世界的预测与因果，但可交互、可持久的 3D 世界在真实任务中的价值仍待验证。
3. **评测可信度**：MMMU-Pro 的提出本身即说明旧基准易被「刷分」；且不同排行榜结果差异明显，反映出多模态评测尚未标准化（[MMMU-Pro](https://arxiv.org/html/2409.02813)）。
4. **版权与内容溯源**：图像生成工具的差异化开始包含 C2PA 内容凭证、训练数据透明度与商业使用条款等治理维度（[Best AI Image Generators Compared](https://ailove.ai/blog/best-ai-image-generators-compared)），但各平台披露程度不一（如 Midjourney 训练数据被指未披露）。

## 参考来源

1. [Introducing GPT-5 — OpenAI](https://openai.com/hu-HU/index/introducing-gpt-5/)
2. [Introducing GPT-5.4 — OpenAI](https://openai.com/index/introducing-gpt-5-4/)
3. [GPT-5.6: Frontier intelligence that scales with your ambition — OpenAI](https://openai.com/index/gpt-5-6/)
4. [Gemini API 版本说明 — Google AI for Developers](https://ai.google.dev/gemini-api/docs/changelog)
5. [Gemini 3 开发者指南 — Google AI for Developers](https://ai.google.dev/gemini-api/docs/gemini-3)
6. [Gemini 3 Developer Guide](https://goo.gle/3Y3qDr8)
7. [Gemini 3 Flash — Google Cloud Docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash)
8. [Qwen VL: See, Read, Reason](https://qwen3lm.com/qwen-vl/)
9. [Qwen3-VL: Sharper Vision, Deeper Thought, Broader Action](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef)
10. [Qwen3-VL-Flash Launched on Model Studio](https://tongyi.aliyun.com/news?eId=pxwhvf%2Fsuodqg%2Frtgo7st53v06y1gh)
11. [Qwen3.7-Plus: Multimodal Agent Intelligence](https://qwen.ai/blog?id=qwen3.7-plus)
12. [Best AI image generators 2026 (gpt-image-2, Nano Banana Pro)](https://genai.club/blog/best-ai-image-generators-2026)
13. [Best AI Image Generators: Midjourney vs DALL-E vs Stable Diffusion](https://aionx.co/ai-comparisons/ai-image-generators-comparison/)
14. [10 Best AI Image Generators Compared](https://ailove.ai/blog/best-ai-image-generators-compared)
15. [Best AI Image Generators August 2026](https://aiflashreport.com/ai-image-generators)
16. [Sora 2 vs Veo 3 vs Seedance 2.0: Which AI Video Model Actually Wins?](https://www.seedance-25.ai/blog/sora-2-vs-veo-3-vs-seedance)
17. [Sora 2 vs Veo 3 vs Runway Gen-4 vs Kling 3 — 2026 Comparison](https://kursvideoai.pl/en/blog/sora-vs-veo-vs-runway-vs-kling/)
18. [AI Video Generation — aiwiki.ai](https://aiwiki.ai/wiki/ai_video_generation/edit)
19. [Seedance 2.0 Review (2026)](https://www.seedance2pro.com/review)
20. [Presentamos GPT-Live — OpenAI](https://openai.com/es-419/index/introducing-gpt-live/)
21. [Genie 3 — Google DeepMind](https://deepmind.google/models/genie/)
22. [World Labs 官网](https://www.worldlabs.ai/)
23. [World Labs Research & Insights (Marble / Atlas)](https://www.worldlabs.ai/blog)
24. [Welcome to Marble — World Labs Docs](https://docs.worldlabs.ai/)
25. [MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark](https://arxiv.org/html/2409.02813)
26. [MMMU-Pro — BenchLM](https://benchlm.ai/benchmarks/mmmu-pro)
27. [Artificial Analysis MMMU-Pro (AA-MMMU-Pro)](https://benchlm.ai/benchmarks/aammmupro)
28. [MMMU-Pro Benchmark Leaderboard — Artificial Analysis](https://artificialanalysis.ai/evaluations/mmmu-pro)