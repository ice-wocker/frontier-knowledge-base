# 多模态 AI（Multimodal AI）

> 最后更新：2026-09-26 ｜ 领域：人工智能 / 多模态模型与生成 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 一、概述

多模态 AI 指同时理解与生成文本、图像、音频、视频乃至 3D 世界的模型体系。2025–2026 年的主线是「**原生多模态（native multimodal）**」——不再把视觉/语音作为外挂模块，而是在同一模型内统一建模；与此同时，图像生成、视频生成、实时语音对话与「世界模型（world model）」四条产品线并行爆发，多模态能力成为前沿模型的默认配置而非附加项。

从能力评测看，多模态仍是「进展快但边界明显」的领域：一方面前沿模型在文档、图表、屏幕与视频理解上快速提升，另一方面在最难的空间推理任务上仍远低于人类——例如在视频空间智能基准 MMSI-Video-Bench 上，表现最好的 Gemini 3 Pro 仅得 38.0 分，而人类为 96.4 分（[MMSI-Video-Bench](https://arxiv.org/html/2512.10863)）；在 GST-Bench 上，最强的零样本模型 Gemini-3-Pro 得 42.68 分，人类基线为 79.08 分（[GST-Bench](https://arxiv.org/html/2608.05747v1)）。这说明「看得懂」与「真正理解空间/物理」之间仍有明显鸿沟。

## 二、2025–2026 最新进展

- **前沿模型全面多模态化**。OpenAI 的 GPT-5 系列强调「基于图像与其他非文本输入进行更准确推理」，可解读图表、总结演示文稿照片并回答与图示相关的问题（[Introducing GPT-5](https://openai.com/hu-HU/index/introducing-gpt-5/)）。OpenAI 后续推出 GPT-5.4，称其与既有模型「智能相同、只是更快」，但 API 单价高于 GPT-5.2，并用更高的 token 效率降低总用量（[Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)）。
- **Google Gemini 3 系列**将图像生成与视觉理解进一步原生整合。Gemini 3 Pro 称在推理与多模态上全面超越 2.5 Pro，以 1501 Elo 登顶 LMArena，并在 Humanity's Last Exam（无工具 37.5%）与 GPQA Diamond（91.9%）上取得高分（[A new era of intelligence with Gemini 3](https://blog.google/products/gemini/gemini-3/)）。Google 将 Gemini 3 Pro 描述为「从简单识别到真正视觉与空间推理」的世代跃升，在 MMMU Pro 与 Video MMMU 等视觉基准上创下新高（[Gemini 3 Pro: the frontier of vision AI](https://blog.google/technology/developers/gemini-3-pro-vision/)）；Gemini 3.1 Pro 的官方模型卡称其在需要增强推理的多项基准上进一步超越 Gemini 3 Pro（[Gemini 3.1 Pro](https://deepmind.google/models/model-cards/gemini-3-1-pro/)）。官方发布原生视觉模型 **Gemini 3.1 Flash Image** 与 **Gemini 3 Pro Image** 的正式版（GA），支持以视频（含 YouTube 链接）作为多模态上下文做「视频转图片」生成；Gemini 3 引入 `media_resolution` 参数，可精细控制每张图片/视频帧分配的 token 上限，并支持最高 2K/4K 分辨率与文本渲染（[Gemini API 版本说明](https://ai.google.dev/gemini-api/docs/changelog)、[Gemini 3 开发者指南](https://ai.google.dev/gemini-api/docs/gemini-3)）。
- **图像生成进入「Nano Banana」世代**。Google 把图像生成/编辑模型命名为 **Nano Banana**：**Nano Banana Pro**（`gemini-3-pro-image`）构建于 Gemini 3 之上，提供工作室级精度与控制、最高 4K 分辨率、多语言文本渲染，可在单图内组织最多 14 个对象或 5 个人物（[Nano Banana 图片生成 — Google AI for Developers](https://ai.google.dev/gemini-api/docs/image-generation/)、[Nano Banana 🍌 — Google DeepMind](https://deepmind.google/models/gemini-image/)、[Nano Banana Pro](https://aicharalab.com/nano-banana-pro)）。云文档显示 `gemini-3-pro-image` 的 GA 发布日期为 2026 年 5 月 28 日（[Gemini 3 Pro Image — Google Cloud Docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-pro-image)）；Google 还发布更快的 **Nano Banana 2 Lite**，主打高速、低成本（[Nano Banana — Google DeepMind](https://deepmind.google/models/gemini-image/)）。
- **开放权重多模态**由阿里 Qwen 引领：Qwen3-VL 提供 2B/4B/8B/32B/30B-A3B/235B-A22B 多档规模，上下文 256K 可扩展至 1M，支持文本·图像·视频输入，采用 Apache 风格开放权重（[Qwen VL](https://qwen3lm.com/qwen-vl/)）。官方博客强调其可识别名人、食物、植物、动物、汽车品牌与动漫角色，并强化多图多轮对话中的上下文保持（[Qwen3-VL: Sharper Vision, Deeper Thought, Broader Action](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef)）。Qwen 还发布多模态 MoE 模型 **Qwen3.8-Flash-Next** 并开放权重，定位极致成本效率（[Qwen3.8-Flash-Next](https://qwen.ai/blog?id=qwen3.8-flash-next)）。
- **实时语音对话**进入全双工时代：OpenAI 发布 **GPT-Live**，称这是新一代语音模型，基于**全双工（full-duplex）架构**，可边听边说，并用「嗯」「对」这类语气词表明在倾听（[Presentamos GPT-Live](https://openai.com/es-419/index/introducing-gpt-live/)）。
- **全模态（omni）模型把「理解 + 生成 + 行动」合一**：阿里发布 **Qwen3.8-Omni-Flash**（2026 年 9 月），原生统一文本、图像、音频、视频四类输入，提供 100 万 token 上下文窗口，官方称在 29 项基准上平均较上代 Qwen3.5-Omni-Plus 提升逾 25%，并支持 113 种语言/方言的音频输入与立体声/四声道空间音频分析，官方称其音频输入成本每小时下降超 98%、音视频混合输入下降超 93%（[Alibaba Launches Qwen3.8-Omni-Flash: Native Multimodal, Million-Context Audio Cost Cut by 98%](https://news.aibase.com/news/31158)）。Google 在 I/O 2026 发布 **Gemini Omni**，定位「从任意输入生成任意输出」（先支持视频输出），融合对重力、动能、流体等物理量的理解，并在生成视频中嵌入 SynthID 数字水印以便验证（[100 things we announced at Google I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)）。
- **开放 3D 世界生成**：腾讯混元的 **HY-World 2.0** 可从文本、图像与视频生成真实 3D 资产（网格、3D 高斯泼溅与点云），可直接导入 Blender、Unity、Unreal Engine 或 Isaac Sim，并以完整开源（含模型权重与推理代码）发布（[Tencent-Hunyuan/HY-World-2.0: Open 3D World Generation from Text, Images, and Video](https://www.blog.brightcoding.dev/2026/09/16/tencent-hunyuanhy-world-20-open-3d-world-generation-from-text-images-and-video)）。
- **世界模型成为新战场**：Google DeepMind 的 **Genie 3**（2025 年 8 月 5 日发布研究预览）是通用世界模型，用简单文本即可生成可实时探索的 3D 环境，运行在 720p、24 fps，并具备一定程度的物体持久性与涌现物理（[10 Open World AI Models Actually Worth Following in 2026](https://autogpt.net/top-open-world-ai-models/)、[World Models in 2026](https://www.ai.cc/blogs/world-models-2026-google-nvidia-physical-ai-breakthroughs/)）；Google 于 2026 年 1 月推出面向消费者的 **Project Genie**（[spatial intelligence — aiwiki](https://aiwiki.ai/wiki/spatial_intelligence/raw)）。NVIDIA 提供开放权重的世界基础模型平台 **Cosmos**（[World Models in 2026](https://www.ai.cc/blogs/world-models-2026-google-nvidia-physical-ai-breakthroughs/)）；Waymo 于 2026 年 2 月发布 **Waymo World Model**（Genie 3 的专用分支，用于自动驾驶训练）（[Как устроены world models](https://habr.com/ru/articles/1038818/)）；World Labs 的 **Marble** 从文本、图像、视频或 360 全景生成可持久存在的 3D 世界，并于 2026 年 9 月发布面向空间智能的 omnimodal 世界模型 **Atlas**（[World Labs](https://www.worldlabs.ai/)、[World Labs Research & Insights](https://www.worldlabs.ai/blog)）。

## 三、核心技术与关键概念

- **原生多模态 vs 拼接式**：原生模型在一个架构内对齐多种模态的表征，减少「视觉编码器 + LLM」拼接带来的信息损失；Gemini 3 的 `media_resolution` 说明厂商开始把「视觉 token 预算」显式暴露为可调参数（[Gemini 3 Developer Guide](https://goo.gle/3Y3qDr8)）。
- **图像生成**：扩散模型与流匹配（flow matching）并存。Black Forest Labs 的 **FLUX.2**（2025 年 11 月发布，2026 年 1 月补充 FLUX.2 [klein] 家族）据称在 4 百万像素分辨率下保持一致性，并支持最多 10 张参考图用于角色与风格一致（[Best AI image generators 2026](https://genai.club/blog/best-ai-image-generators-2026)）。文本渲染与版式能力成为差异化重点（[Best AI Image Generators](https://aionx.co/ai-comparisons/ai-image-generators-comparison/)）。
- **视频生成**：主流模型在时长、分辨率与是否原生音频上分层。据整理对比，**Veo 3.1**（Google DeepMind，2025 年 10 月）支持最高 4K、原生同步音频（对白/音效/环境声），剪辑工具最完整（[Best AI Video Generation Models in 2026](https://www.toolmintx.in/blog/best-ai-video-generation-models-2026-compared)），有来源称其最长可延长至 60 秒以上（[Veo 3.1 vs Kling 3.0 vs Sora 2](https://blogs.grouptoolz.com/ai-video-generator-veo-3-vs-kling-3-vs-sora-2/)）；**Kling 3.0**（快手）以最长约 15–180 秒、多镜头、支持 5 种语言唇形同步与音效见长（不同来源口径不一：有称 15 秒多镜头，也有称 180 秒）（[Veo 3.1 vs Kling 3.0 vs Sora 2](https://www.aimagicx.com/blog/veo-3-vs-kling-3-vs-sora-2-april-2026-comparison)）；**Sora 2**（OpenAI，2025 年 9 月）最长 20 秒、1080p、带基础音频（[AI Video Generation](https://aiwiki.ai/wiki/ai_video_generation/edit)），但有来源称其第三方 API（FAL.AI）将于 2026-09-24 停止服务（[2026 AI Video Generation Top 3 Compared](https://gocodelab.com/en/blog/en-sora-2-vs-veo-3-1-vs-kling-3-0-ai-video-comparison-2026)）——不同来源对 Sora 2 的可用状态说法不一，须注意口径。此外，**Seedance 2.0**（字节）在速度与角色一致性上被指见长（[Sora 2 vs Veo 3 vs Seedance 2.0](https://www.seedance-25.ai/blog/sora-2-vs-veo-3-vs-seedance)），**Wan 2.6** 被列为无原生音频的开放选项（[Veo 3.1 vs Kling 3.0 vs Sora 2](https://www.aimagicx.com/blog/veo-3-vs-kling-3-vs-sora-2-april-2026-comparison)）。
- **世界模型**：目标是让模型预测世界如何演化、行动如何影响环境。Genie 3 被描述为「纯生成式像素引擎」，用神经物理取代传统游戏引擎的硬编码物理，逐帧生成可探索 3D 环境（[These AI research labs are building very different world models for robot training](https://roboticsbiz.com/these-ai-research-labs-are-building-very-different-world-models-for-robot-training/)）；World Labs 则提出端到端「Real-to-sim-to-real（R2S2R）」以训练机器人（[World Labs Research & Insights](https://www.worldlabs.ai/blog)）。
- **开放权重部署**：Ollama 生态中 2026 年最佳视觉模型被列为 Qwen3-VL 与 Gemma 4，二者均为原生多模态；Google 的 Gemma 3 提供 1B–27B 参数、较大变体支持图像输入与视觉问答（[Which Ollama Models Support Vision?](https://www.promptquorum.com/prompt-bites/which-ollama-models-support-vision)、[Meilleures APIs de Computer Vision & modèles open source 2026](https://www.edenai.co/fr/post/top-free-computer-vision-apis-and-open-source-models)）。
- **语音合成与实时语音**：语音合成模型按「表现力 vs 延迟」分层，ElevenLabs 的 v3 Conversational 主打高表现力、延迟约 280 ms，并支持 70+ 语言与自定义音频标签（audio tags）；Flash v2.5 主打约 75 ms 的超低延迟并支持 32 种语言，两者定价均约 0.05 美元/分钟（[Text to Speech API — ElevenLabs](https://elevenlabs.io/text-to-speech-api)）。
- **多模态智能体与「计算机使用（computer use）」**：把屏幕截图作为视觉输入、输出点击/输入/滚动等结构化动作，已成为 GUI 智能体的通用范式；Microsoft Copilot Studio 的 computer use 由「Computer-Using Agents（CUA）」驱动，结合视觉与推理操作图形界面，并能适应按钮或界面变化（[Automate web and desktop apps with computer use — Microsoft Learn](https://learn.microsoft.com/sr-latn-rs/microsoft-copilot-studio/computer-use)）。阿里的 Qwen3.7-Plus 定位「多模态交互混合智能体」，在单一智能体循环内统一 GUI 与 CLI 操作，可读屏、依据视觉参考写代码并端到端操作移动应用（[Qwen3.7-Plus: Multimodal Agent Intelligence](https://qwen.ai/blog?id=qwen3.7-plus)）。
- **文档理解与多模态 RAG**：文档场景是视觉语言模型的重要落地面。CC-OCR v2 覆盖 5 条 OCR 主赛道与 74 种场景，以细粒度评测衡量「文档素养」，并指出既有评测可能高估模型在真实文档处理上的成熟度（[CC-OCR v2](https://arxiv.org/html/2605.03903v1)）；DocAtlas 则以 82 种语言、覆盖文本/表格/公式/图表等全部元素的多语言文档解析为卖点（[DocAtlas](https://arxiv.org/html/2605.12623v2)）。在检索侧，把图像并入与文本同一检索管道已成为企业 RAG 的标配：Azure AI Search 的 multimodal search 可召回图表、截图、信息图与扫描表格中的信息（[Multimodal search in Azure AI Search](https://learn.microsoft.com/en-gb/Azure/search/multimodal-search-overview)）；NVIDIA 的多模态 RAG 参考架构用 NeMo Retriever 抽取文本、表格、图表并做向量索引，其 Nemotron 推理据称可将准确率提升约 5%（[Build AI-Ready Knowledge Systems Using 5 Essential Multimodal RAG Capabilities](https://developer.nvidia.com/blog/build-ai-ready-knowledge-systems-using-5-essential-multimodal-rag-capabilities)）。
- **具身多模态（VLA）**：把「图像 + 语言指令」直接映射为机器人动作的 **Vision-Language-Action（VLA）** 模型成为多模态与机器人交叉的新方向。EmbodiedBench 面向多模态大模型充当具身智能体，在高层与低层任务及六项智能体能力上做细粒度评测，并在 CVPR 2026 举办挑战赛（[EmbodiedBench](https://embodiedbench.github.io/)、[EmbodiedBench Challenge](https://embodiedbench.github.io/challenge.html)）；也有基准在低成本 SO-101 平台上系统评估 pi0.5、SmolVLA、Wall-X、ACT 等策略的任务成功率与失败恢复（[Benchmarking Vision-Language-Action Models on SO-101](https://arxiv.org/html/2606.08881)）。
- **多模态工具使用与全模态智能体评测**：随着智能体从纯文本走向多模态，评测开始强调「闭环多模态验证」——TOBench 含 100 个可执行任务、20 个子类、27 个 MCP server 与 324 个工具，要求智能体执行工具、检查渲染或转换后的产物并在失败时自我纠正（[TOBench](https://arxiv.org/html/2605.16909v1)）；EgoBench 以 1,045 个第一人称视频任务覆盖四类日常场景，评测工具使用智能体对视觉感知与工具增强多跳推理的联合运用（[EgoBench](https://arxiv.org/html/2605.27820v1)）；LiViBench 则被列为面向互动直播视频理解的 omnimodal 基准（[Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms](https://arxiv.org/html/2606.04701v1)）。
- **多模态评测**：**MMMU-Pro** 通过更稳健的设置抑制了模型在原始 MMMU 上可能利用的捷径与猜测策略——当候选选项从 4 个增加到 10 个时，GPT-4o（0513）从 64.7% 降到 54.0%，且发现思维链（CoT）提示普遍提升表现（[MMMU-Pro](https://arxiv.org/html/2409.02813)、[MMMU-Pro (PDF)](https://arxiv.org/pdf/2409.02813v2)）。

## 四、代表性项目 / 产品

| 类别 | 项目 / 产品 | 官方链接 |
| --- | --- | --- |
| 通用多模态 LLM | OpenAI GPT-5 系列 | https://openai.com/index/introducing-gpt-5/ |
| 通用多模态 LLM | Google Gemini 3 系列 | https://ai.google.dev/gemini-api/docs/gemini-3 |
| 开放权重 VLM | 阿里 Qwen3-VL / Qwen3-Omni | https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef |
| 开放权重 VLM | Google Gemma 3 | https://ai.google.dev/gemma |
| 图像生成 | Google Nano Banana Pro | https://deepmind.google/models/gemini-image/ |
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
- **MMMU-Pro 排行榜（Interfaze）**：Interfaze 以 71.1% 居首，其后为 Grok-4.3（68.7%）、Gemini-3-Flash（67.6%）、Claude-Sonnet-5（53.3%），并区分 Standard 与 Vision-only 两种设置（[MMMU-Pro — Interfaze](https://interfaze.ai/leaderboards/mmmu-pro)）。
- **MMMU-Pro 排行榜（Artificial Analysis，2026-09-18 前后）**：AA-MMMU-Pro 上 GPT-6 Astra 以 **86.9%** 领先，其后为 Gemini 3.8 Flash（85.6%）；Artificial Analysis 另列出 Claude Opus 5.5 在 MMMU-Pro 上达 **88%**（[AA-MMMU-Pro](https://benchlm.ai/benchmarks/aammmupro)、[MMMU-Pro Benchmark Leaderboard](https://artificialanalysis.ai/evaluations/mmmu-pro)）。
- **空间/视频推理**：MMSI-Video-Bench 上最佳模型 Gemini 3 Pro 仅 38.0 分（人类 96.4）；GST-Bench 上最强零样本模型 Gemini-3-Pro 42.68 分（人类 79.08）（[MMSI-Video-Bench](https://arxiv.org/html/2512.10863)、[GST-Bench](https://arxiv.org/html/2608.05747v1)）。
- **Qwen3.8-Omni-Flash vs Gemini3.8Flash（官方自报）**：WildClawBench-MM 多模态工具调用 71.0 vs 58.9、SpotSoundBench 67.2 vs 39.7、MMAU 81.8 vs 76.9、DailyOmni 85.1 vs 84.0；但在 AgenticVBench 上 36.8 落后于 45.0，部分视频理解任务 Gemini 仍占优（[Alibaba Launches Qwen3.8-Omni-Flash](https://news.aibase.com/news/31158)）。
- **Qwen3.7-Plus 多模态基准（官方）**：MMMU-Pro 79.0、MathVision 90.3、BabyVision 70.4、CharXiv(RQ) 85.9；对照 Gemini-3.1 Pro（81.8 / 87.4 / 55.9 / 84.4）与 GPT-5.4（xhigh）（81.2 / 91.0 / 53.1 / 84.5）（[Qwen3.7-Plus](https://qwen.ai/blog?id=qwen3.7-plus)）。
- **Video-MMMU（ACL 2026）**：300 个专家级视频、900 道人工标注题，覆盖艺术/商业/科学/医学/人文/工程六学科与「感知·理解·适应」三阶段；在衡量「看完视频后知识增益」的指标 Δknowledge 上人类达 33.1%，而 GPT-4o 仅 15.6%、Claude-3.5-Sonnet 仅 11.4%（[Video-MMMU](https://videommmu.github.io/)）。
- **文档/OCR 榜（OCR and Document AI Leaderboard 2026）**：以 OCRBench、DocVQA、InfoVQA、ChartQA、TextVQA 等指标比较模型，并指出 Mistral OCR、LlamaParse、Nougat 等专用文档管线未在标准 VQA 基准上报数，难以与通用 VLM 直接横比（[OCR and Document AI Leaderboard 2026](https://awesomeagents.ai/leaderboards/ocr-document-ai-leaderboard/)）。

> 不同榜单因评测口径、工具调用与推理预算设置不同而给出不一致的排名，引用时需注明来源与日期。

- **视频模型参数**：Veo 3.1 最高 4K、原生同步音频、最长约 60 秒并可延长；Kling 3.0 最长约 15–180 秒（口径不一）、支持多语言唇形同步；Sora 2 最长 20s/1080p/基础音频（[Best AI Video Generation Models in 2026](https://www.toolmintx.in/blog/best-ai-video-generation-models-2026-compared)、[Veo 3.1 vs Kling 3.0 vs Sora 2](https://blogs.grouptoolz.com/ai-video-generator-veo-3-vs-kling-3-vs-sora-2/)、[AI Video Generation](https://aiwiki.ai/wiki/ai_video_generation/edit)）。
- **Gemini 3 Pro 综合**：LMArena 1501 Elo、Humanity's Last Exam 37.5%（无工具）、GPQA Diamond 91.9%（[A new era of intelligence with Gemini 3](https://blog.google/products/gemini/gemini-3/)）。
- **Gemini 3 Flash 规格**：上下文窗口 1,048,576 token，最大输出 65,536 token，文本输入输出、图像/音频/视频仅输入（[Gemini 3 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash)）。

## 六、趋势与争议

1. **原生多模态 vs 模态专用模型之争**：通用模型持续吞并图像/视频生成能力（如 Gemini 3 Pro 同时提供理解与图像生成），但专用工具（FLUX、Midjourney、可灵等）在特定质量维度仍领先，「通才够用、专才够好」并存。
2. **世界模型是通向具身智能的桥梁还是营销概念**：Genie 3、Cosmos、Atlas、Waymo World Model 等强调对物理世界的预测与因果，并已用于机器人与自动驾驶仿真，但可交互、可持久的 3D 世界在真实任务中的价值仍待验证。
3. **评测可信度**：MMMU-Pro 的提出本身即说明旧基准易被「刷分」；空间/视频基准上模型与人类的巨大差距（38.0 vs 96.4）说明能力被高估的风险，且不同排行榜结果差异明显，反映多模态评测尚未标准化（[MMMU-Pro](https://arxiv.org/html/2409.02813)、[MMSI-Video-Bench](https://arxiv.org/html/2512.10863)）。
4. **版权与内容溯源**：图像生成工具的差异化开始包含 C2PA 内容凭证、训练数据透明度与商业使用条款等治理维度（[Best AI Image Generators Compared](https://ailove.ai/blog/best-ai-image-generators-compared)），但各平台披露程度不一（如 Midjourney 训练数据被指未披露）。
5. **开放权重 vs 闭源前沿**：Qwen3-VL、Gemma 3、Qwen3.8-Flash-Next 等以开放权重覆盖从端侧到超大 MoE 的档位，正在缩小与闭源前沿在多数实用多模态任务上的差距，但在最难的空间推理上仍与最强闭源模型存在落差（[Qwen VL](https://qwen3lm.com/qwen-vl/)、[Which Ollama Models Support Vision?](https://www.promptquorum.com/prompt-bites/which-ollama-models-support-vision)）。

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
29. [A new era of intelligence with Gemini 3 — Google Blog](https://blog.google/products/gemini/gemini-3/)
30. [Gemini 3 Pro: the frontier of vision AI — Google Blog](https://blog.google/technology/developers/gemini-3-pro-vision/)
31. [Gemini 3.1 Pro — Google DeepMind Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
32. [Nano Banana 图片生成 — Google AI for Developers](https://ai.google.dev/gemini-api/docs/image-generation/)
33. [Nano Banana 🍌 — Google DeepMind](https://deepmind.google/models/gemini-image/)
34. [Gemini 3 Pro Image (Nano Banana Pro) — Google AI Studio](https://aistudio.google.com/models/gemini-3-pro-image)
35. [Gemini 3 Pro Image (Nano Banana Pro) — Google Cloud Docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-pro-image)
36. [Nano Banana Pro — aicharalab](https://aicharalab.com/nano-banana-pro)
37. [Qwen3.8-Flash-Next: A New Architecture, Towards Ultimate Cost-Efficiency](https://qwen.ai/blog?id=qwen3.8-flash-next)
38. [Which Ollama Models Support Vision?](https://www.promptquorum.com/prompt-bites/which-ollama-models-support-vision)
39. [Meilleures APIs de Computer Vision & modèles open source 2026](https://www.edenai.co/fr/post/top-free-computer-vision-apis-and-open-source-models)
40. [10 Open World AI Models Actually Worth Following in 2026](https://autogpt.net/top-open-world-ai-models/)
41. [These AI research labs are building very different world models for robot training](https://roboticsbiz.com/these-ai-research-labs-are-building-very-different-world-models-for-robot-training/)
42. [World Models in 2026: Why Google, NVIDIA, LeCun & Fei-Fei Li Are Betting Billions](https://www.ai.cc/blogs/world-models-2026-google-nvidia-physical-ai-breakthroughs/)
43. [spatial intelligence — aiwiki](https://aiwiki.ai/wiki/spatial_intelligence/raw)
44. [Как устроены world models (Waymo World Model)](https://habr.com/ru/articles/1038818/)
45. [MMSI-Video-Bench: A Holistic Benchmark for Video-Based Spatial Intelligence](https://arxiv.org/html/2512.10863)
46. [GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?](https://arxiv.org/html/2608.05747v1)
47. [MMMU-Pro (PDF)](https://arxiv.org/pdf/2409.02813v2)
48. [MMMU-Pro — Interfaze](https://interfaze.ai/leaderboards/mmmu-pro)
49. [Veo 3.1 vs Kling 3.0 vs Sora 2: The Definitive April 2026 AI Video Comparison](https://www.aimagicx.com/blog/veo-3-vs-kling-3-vs-sora-2-april-2026-comparison)
50. [2026 AI Video Generation Top 3 Compared: Veo 3.1 vs Kling 3.0 After Sora 2 Shutdown](https://gocodelab.com/en/blog/en-sora-2-vs-veo-3-1-vs-kling-3-0-ai-video-comparison-2026)
51. [Best AI Video Generation Models in 2026 Compared](https://www.toolmintx.in/blog/best-ai-video-generation-models-2026-compared)
52. [Veo 3.1 vs Kling 3.0 vs Sora 2: Which AI Video Generator Should You Pick in 2026?](https://blogs.grouptoolz.com/ai-video-generator-veo-3-vs-kling-3-vs-sora-2/)
53. [Alibaba Launches Qwen3.8-Omni-Flash: Native Multimodal, Million-Context Audio Cost Cut by 98% — AIBase](https://news.aibase.com/news/31158)
54. [Qwen3.8-Omni-Flash: AI Model for Audio, Video and Autonomous Agents — AI Arabai](https://aiarabai.com/en/qwen3-8-omni-flash-model-ai/)
55. [Qwen3.7-Plus: Multimodal Agent Intelligence — Qwen](https://qwen.ai/blog?id=qwen3.7-plus)
56. [Video-MMMU: Evaluating Knowledge Acquisition from Multi-Discipline Professional Videos](https://videommmu.github.io/)
57. [100 things we announced at Google I/O 2026 — Google Blog](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
58. [Text to Speech API — ElevenLabs](https://elevenlabs.io/text-to-speech-api)
59. [Automate web and desktop apps with computer use — Microsoft Learn](https://learn.microsoft.com/sr-latn-rs/microsoft-copilot-studio/computer-use)
60. [Toward Native Multimodal Modeling: A Roadmap — arXiv](https://arxiv.org/html/2605.25343v1)
61. [Tencent-Hunyuan/HY-World-2.0: Open 3D World Generation from Text, Images, and Video](https://www.blog.brightcoding.dev/2026/09/16/tencent-hunyuanhy-world-20-open-3d-world-generation-from-text-images-and-video)
62. [CC-OCR v2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing — arXiv](https://arxiv.org/html/2605.03903v1)
63. [DocAtlas: Multilingual Document Understanding — arXiv](https://arxiv.org/html/2605.12623v2)
64. [Multimodal search in Azure AI Search — Microsoft Learn](https://learn.microsoft.com/en-gb/Azure/search/multimodal-search-overview)
65. [Build AI-Ready Knowledge Systems Using 5 Essential Multimodal RAG Capabilities — NVIDIA](https://developer.nvidia.com/blog/build-ai-ready-knowledge-systems-using-5-essential-multimodal-rag-capabilities)
66. [EmbodiedBench: A Comprehensive Benchmark for Multimodal LLM-based Embodied Agents](https://embodiedbench.github.io/)
67. [EmbodiedBench Challenge — CVPR 2026 Workshop](https://embodiedbench.github.io/challenge.html)
68. [Benchmarking Vision-Language-Action Models on SO-101: Failure and Recovery Analysis — arXiv](https://arxiv.org/html/2606.08881)
69. [OCR and Document AI Leaderboard 2026: Top Models Ranked — Awesome Agents](https://awesomeagents.ai/leaderboards/ocr-document-ai-leaderboard/)
70. [TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents — arXiv](https://arxiv.org/html/2605.16909v1)
71. [EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents — arXiv](https://arxiv.org/html/2605.27820v1)
72. [Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms — arXiv](https://arxiv.org/html/2606.04701v1)