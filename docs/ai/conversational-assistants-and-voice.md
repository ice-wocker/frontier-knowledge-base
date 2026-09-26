# 对话助手与语音（Conversational Assistants & Voice）

> 最后更新：2026-09-26 ｜ 领域：AI·提示、Agent 与应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

对话助手与语音技术栈由四层构成：语音识别（ASR，语音转文本）、语音合成（TTS，文本转语音）、实时语音对话模型（speech-in / speech-out，端到端低延迟交互），以及承载它们的消费级助手生态（如 Siri、Alexa+、Gemini）。2026 年的关键变化是：实时语音 API 开始支持语音直进直出的对话，且主要平台把"对话式 AI"作为一等公民能力对外提供（[Use the GPT Realtime API via WebRTC — Microsoft Learn](https://learn.microsoft.com/sl-si/azure/foundry/openai/how-to/realtime-audio-webrtc)）。

## 最新进展（2025–2026）

**实时语音（Realtime）**：Azure OpenAI 的 GPT Realtime API 面向语音与音频，属于 GPT-4o 模型家族，支持低延迟的 "speech in, speech out" 对话交互，可通过 WebRTC、SIP 或 WebSocket 传入音频并实时接收音频响应（[Use the GPT Realtime API via WebRTC](https://learn.microsoft.com/sl-si/azure/foundry/openai/how-to/realtime-audio-webrtc)）。不同接入方式的典型延迟不同：WebRTC 面向客户端应用，约 100ms；WebSocket 面向服务端到服务端，约 200ms；SIP 用于电话/呼叫中心集成，延迟视网络而变（[Use the GPT Realtime API for speech and audio](https://learn.microsoft.com/el-gr/azure/foundry/openai/how-to/realtime-audio)）。OpenAI 官方介绍了第三代语音系统 GPT-Live：它把"轮次检测器"（turn detector）从音频路径中移除，语音模型为 full-duplex（全双工），可同时听与说，从而让对话更即时自然；当需要更深推理或工具调用时，GPT-Live 可调用 GPT-5.5 等前沿模型而不打断对话流（[How we built a realtime system for responsive voice AI in six months](https://openai.com/index/continuous-voice-interaction-with-gpt-live/)）。Google 侧的 Gemini 系列在 2026 年推出 `gemini-3.8-live`，被定位为大多数低延迟语音 Agent 体验与实时对话的默认选项，官方称其"不会有推理延迟"，功能包括交错推理、默认异步函数调用，以及完整会话的客户端上下文更新（[Gemini API 版本资讯](https://ai.google.dev/gemini-api/docs/changelog)）。

**TTS**：据报道，Google 于 2026 年 9 月 23 日推出 Gemini 3.8 Flash TTS 与 Gemini 3.8 Flash-Lite TTS 两款文本转语音模型，前者面向声音与角色设计，支持用自然语言创建定制声音并逐句控制语气、语速、口音等，后者面向大规模音频生成与配音（[数智周报](http://m.toutiao.com/group/7689702645484880420/)）。开源与闭源 TTS 竞争加剧：一份 2026 年榜单以 Elo 给出 ElevenLabs Eleven v3 为 1,177（闭源，作为参照）、Fish Audio S2 Pro 1,125（研究性非商业许可）、StepFun Step Audio EditX 1,102（Apache 2.0）、Mistral Voxtral TTS 1,082 分（[Best Open Source Self-Hosted Text-to-Speech Models in 2026](https://pinggy.io/blog/best_open_source_self_hosted_text_to_speech_models/)）。

**ASR**：ElevenLabs 推出 Scribe v2 Medical，并在临床音频上把词错误率（WER）相对基础 Scribe v2 模型降低约 35%，用于弥补通用模型在临床工作流上的退化（[Scribe v2 Medical is now available to everyone](https://elevenlabs.io/blog/scribe-v2-medical-generally-available)）。开源侧，OpenAI Whisper 仍是参考级开放 ASR 模型，其价值更多体现在许可与可移植性：模型尺寸从 tiny（约 39M 参数、约 1GB 显存）到 large（1.55B 参数），仓库同时提供多种规模（[Speech-to-Text Models Compared 2026](https://www.web3aiblog.com/blog/speech-to-text-models-compared-whisper-deepgram-assemblyai-elevenlabs-2026)）；一份 2026 年开放 ASR 对比给出 Whisper large-v3 的平均 WER 为 7.44、支持 99 种语言与英译、MIT 许可、速度在对比组中最慢（large-v3-turbo 把解码器减到 4 层），其架构为 encoder-decoder Transformer、128 个 Mel 频带、在 100 万小时标注数据 + 400 万小时伪标注数据上训练（[Best Open Speech Recognition (ASR) Models in 2026](https://www.marktechpost.com/2026/07/23/best-open-speech-recognition-asr-models-in-2026-wer-languages-latency-and-license-compared/)）。新的多语种基准 GigaSpeechBench 则把 Qwen3-ASR-1.7B、Whisper-large-v3、NVIDIA NeMo Canary 与 Meta OmniASR-LLM-3B 等纳入统一评测（[GigaSpeechBench](https://arxiv.org/html/2606.28884v2)）。

**助手生态**：Apple 于 2026 年 6 月发布 Siri AI，官方称其为"能力大幅提升、更具对话性"的个人助手（[Apple introduces Siri AI](https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)），并在 2026 年 9 月宣布其正式发布（[Siri AI is here](https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/)）；据媒体报道，新 Siri 支持多轮对话、可基于实时世界知识作答、并直接嵌入 Dynamic Island，配有重新设计的语音引擎与可在初始化时微调的声音设置（[Apple Announces 'Siri AI' at WWDC 2026 — MacRumors](https://www.macrumors.com/2026/06/08/apple-announces-siri-ai/)）。Amazon 的 Alexa+ 持续国际扩张，2026 年 9 月 16 日登陆印度，此前已进入美国、英国、加拿大、墨西哥、意大利、西班牙、德国、奥地利、巴西、法国、澳大利亚等市场，并计划在 2027 年扩展至 10 多个国家（[Alexa+ arrives in India](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)）。

## 核心技术与关键概念

**端到端语音模型 vs 级联管线**：传统方案为 ASR → LLM → TTS 三级级联，延迟累加；实时语音 API 则直接做语音到语音，缩短首字响应时间、保留韵律与情感线索（[Use the GPT Realtime API via WebRTC](https://learn.microsoft.com/sl-si/azure/foundry/openai/how-to/realtime-audio-webrtc)）。OpenAI 描述的 GPT-Live 采用全双工模型、去除了独立轮次检测器，代表"端到端语音"路线的进一步演进（[Continuous voice interaction with GPT-Live](https://openai.com/index/continuous-voice-interaction-with-gpt-live/)）。

**关键指标**：TTFA（Time To First Audio，首音频时间）与词错误率（WER）是语音栈的两个核心度量；离线场景还看 RT factor（实时倍率）（[Best AI Models for Voice and Speech](https://awesomeagents.ai/capabilities/voice-and-speech/)；[AI Voice and Speech Leaderboard](https://awesomeagents.ai/leaderboards/ai-voice-speech-leaderboard/)）。接入层的工程指标还包括端到端延迟：WebRTC 约 100ms、WebSocket 约 200ms（[Microsoft Learn](https://learn.microsoft.com/el-gr/azure/foundry/openai/how-to/realtime-audio)）。

**语音克隆与情感表达**：声音质量与克隆能力是 TTS 差异化的关键，多语言情感深度、跨语言传递说话者情感成为新一代卖点（[I Benchmarked the Voice AI Stack in May 2026](https://dev.to/jays_tech/i-benchmarked-the-voice-ai-stack-in-may-2026-what-actually-holds-up-in-production-3fmn)；[ElevenLabs 中文官网](https://elevenlabs.io/zh)）。

**对话式 AI 平台**：以 ElevenLabs Conversational AI 为代表，把 TTS、ASR、LLM 与编排能力打包，允许通过 UI、API 或 SDK 接入不同前沿模型（如 GPT-5）构建企业级语音 Agent（[GPT-5 Available in ElevenLabs Conversational AI](https://elevenlabs.io/blog/gpt-5-available-in-elevenlabs-conversational-ai)）。

**语音 Agent 的延迟预算**：呼叫中心场景把"用户说完到 AI 开口"的延迟拆解为 STT、分流、检索、LLM 首 token 与 TTS 各环节，并给出一个参考预算：端到端 p95 控制在 2.5 秒以内，其中 STT 约 500ms、分流 200ms、检索 800ms、LLM 首 token 500ms、TTS 250ms，常用优化手段包括并行执行、缓存与流式输出（[Contact Center AI Architecture for Voice AI (2026)](https://aivanguard.tech/contact-center-ai-production-architecture/)）。由于人类自然对话停顿约 200–300ms，低于 700ms 的响应通常被视为"自然"（[Best Voice Agents for Call Centers in 2026 — Retell AI](https://www.retellai.com/blog/best-voice-agents-for-call-centers)）；真实 PSTN 电话链路还会在 AI 处理前额外引入约 200–500ms 的 SIP 路由、运营商跳数、抖动缓冲与编解码转换延迟（[Speech latency in voice AI — Parloa](https://www.parloa.com/knowledge-hub/speech-latency-voice-ai/)）。

**消费级助手的架构重建**：Amazon 官方称 Alexa+ 建立在全新架构上，由 Amazon Bedrock 上的大语言模型驱动，连接数百个服务与设备，把"理解意图"转化为"执行动作"，并可在被打断或用不完整表达时继续对话（[Alexa+ launches in Italy](https://www.aboutamazon.com/news/devices/alexa-plus-italy)）；另有官方说明称 Alexa+ 由 Amazon Nova 与 Anthropic 的大语言模型共同驱动（[Alexa+ now available to everyone in the US](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)）。Amazon 还表示重建 Alexa 需要一系列技术突破，包括让 LLM 可靠地编排 API 与创造全新的 agentic 能力，且 Alexa+ 已在美国面向所有人开放、对 Prime 会员免费（[Getting started with Alexa+](https://www.aboutamazon.com/news/devices/new-alexa-plus-amazon-devices)）。

## 代表性项目 / 产品（附官方链接）

- **OpenAI Whisper / Realtime API / GPT-Live**：Whisper 的代码与模型权重以 MIT 许可证发布，`openai-whisper` 包持续维护（[openai-whisper on PyPI](https://pypi.org/project/openai-whisper/)）；Realtime API 提供 WebRTC/SIP/WebSocket 接入（[Microsoft Learn](https://learn.microsoft.com/sl-si/azure/foundry/openai/how-to/realtime-audio-webrtc)）；GPT-Live 为全双工实时语音系统（[OpenAI](https://openai.com/index/continuous-voice-interaction-with-gpt-live/)）。
- **ElevenLabs**：提供 TTS、转录、音乐、语音克隆与对话式 AI 平台，2026 年陆续发布 Agent 表达模式、Music v2、Dubbing v2（首次实现原说话者情感与表现力在所有语言中传递）（[ElevenLabs 中文官网](https://elevenlabs.io/zh)）。
- **Google Gemini Live / Flash TTS**：`gemini-3.8-live` 定位低延迟实时对话（[Gemini API 版本资讯](https://ai.google.dev/gemini-api/docs/changelog)）。
- **消费助手**：Apple Siri AI（[Apple Newsroom 2026-06](https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)）、Amazon Alexa+（[About Amazon](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)）。
- **开源 TTS**：Mistral Voxtral TTS、Fish Audio S2 Pro、StepFun Step Audio EditX 等进入公开榜单（[Best Open Source Self-Hosted TTS Models in 2026](https://pinggy.io/blog/best_open_source_self_hosted_text_to_speech_models/)）。

## 关键数据与评测结果

- **TTS 榜单（2026 年 6 月）**：ElevenLabs Flash v2.5 TTFA 75ms、约 1200+ 音色、$50/百万字符；Mistral Voxtral TTS 为开放权重 4B 模型，TTFA 70ms、$16/百万字符；OpenAI gpt-4o-mini-tts TTFA 约 200ms、$15/百万字符，被评为指令遵循最佳的 TTS（[Best AI Models for Voice and Speech](https://awesomeagents.ai/capabilities/voice-and-speech/)）。
- **TTS Arena 人偏好榜**：ElevenLabs Eleven v3 得 100.0、MyShell OpenVoice 99.1、MiniMax Speech 2.6 96.2、Eleven Multilingual v2 93.0（[TTS Arena: Human Preference Leaderboard](https://www.madebyagents.com/benchmarks/tts-arena)）。
- **TTS 质量排名（另一口径）**：ElevenLabs Turbo v2.5（专有，1350+ Elo）居首，开放权重 Zonos2 8B（8B MoE，Apache 2.0，1320+）紧随（[TTS Model Quality Ranking 2026](https://www.offlinetts.com/blog/tts-model-ranking-2026/)）。
- **STT 榜单**：ElevenLabs Scribe v2 英文 WER 2.3%、速度 31.7x、支持实时流式；Google Gemini 3 Pro 英文 WER 2.9%、速度 5.9x、支持实时流式（[AI Voice and Speech Leaderboard](https://awesomeagents.ai/leaderboards/ai-voice-speech-leaderboard/)）。
- **端侧 ASR**：WhisperKit 论文称其在服务端系统对比中达到最低延迟 0.46s 与最高准确率 2.2% WER，对比对象包括前沿模型 OpenAI gpt-4o-transcribe、专有模型 Deepgram nova-3 与开源 Fireworks large-v3-turbo（[WhisperKit: On-device Real-time ASR](https://arxiv.org/html/2507.10860)）。
- **ElevenLabs v3 Multilingual**：支持 32+ 语言、TTFA 低于 100ms、语音克隆被评价为同类最佳（[I Benchmarked the Voice AI Stack in May 2026](https://dev.to/jays_tech/i-benchmarked-the-voice-ai-stack-in-may-2026-what-actually-holds-up-in-production-3fmn)）。
- **Whisper 模型规格**：whisper-large-v3 与 whisper-large-v3-turbo 均为 1.55B 参数的基础模型（[Benchmarking Large Pretrained Multilingual Models on Québec French Speech Recognition](https://arxiv.org/html/2508.21193)）。
- **开放 ASR 对比（2026）**：Whisper large-v3 平均 WER 7.44、99 种语言、MIT 许可；其解码器为 encoder-decoder Transformer（128 Mel 频带），训练数据为 100 万小时标注 + 400 万小时伪标注（[Best Open ASR Models in 2026](https://www.marktechpost.com/2026/07/23/best-open-speech-recognition-asr-models-in-2026-wer-languages-latency-and-license-compared/)）。
- **语音 Agent 端到端延迟（厂商/第三方口径）**：Retell AI 称其在实时电话通话中端到端延迟约 580–640ms（含 ASR、LLM、TTS）；PolyAI 等托管方案约 700–900ms（[Best Voice Agents for Call Centers in 2026](https://www.retellai.com/blog/best-voice-agents-for-call-centers)；[Best Voice AI Agent Companies for Contact Centers](https://www.retellai.com/blog/best-voice-ai-agent-companies-contact-centers)）。上述数字由厂商发布，需谨慎对待。

## 趋势与争议

一是**实时语音成为默认交互层**：`gemini-3.8-live` 被官方定位为"大多数低延迟语音 Agent 与实时对话的默认选项"（[Gemini API 版本资讯](https://ai.google.dev/gemini-api/docs/changelog)），OpenAI 亦以全双工 GPT-Live 取代轮次检测器（[OpenAI](https://openai.com/index/continuous-voice-interaction-with-gpt-live/)），说明语音不再只是附加功能。二是**助手生态的模型外包与阵营化**：有第三方分析称 Siri 2026 的"大脑"部分依赖 Google Gemini 后端并可与 ChatGPT 交接，Alexa+ 被称由 Claude 驱动，且 Siri 绑定 Apple 硬件、Alexa+ 对 Prime 会员免费（或 $19.99/月）（[Siri vs Alexa in 2026](https://elephas.app/resources/siri-vs-alexa)；[Alexa+ vs Gemini Voice vs Siri 2026](https://versusia.fr/assistants-vocaux-ia-2026/)）——此类说法来自第三方媒体，官方未逐一确认；Amazon 官方仅确认 Alexa+ 使用 Amazon Nova 与 Anthropic 模型（[About Amazon](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)）。三是**开源 TTS 的许可分歧**：Mistral Voxtral TTS 被一份来源标注为 Apache 2.0、并被称在 68% 盲测中胜过 ElevenLabs（[免费语音模型](https://diffnotes.tech/posts/free-tts-models-replace-elevenlabs)），而另一份榜单标注其许可为 CC BY-NC 4.0（非商业）（[Best Open Source Self-Hosted TTS Models in 2026](https://pinggy.io/blog/best_open_source_self_hosted_text_to_speech_models/)），许可表述不一致需以官方仓库为准。四是**硬件与软件解耦的延期争议**：有报道称 Apple 的 HomePad 硬件早已完成，延期完全源于需等待新版 Apple Intelligence 驱动的 Siri（[Gemini for Home vs. Alexa+ vs. Siri](https://smartifiers.com/articles/ai-home-assistants-2026-gemini-vs-alexa-plus-vs-siri/)）。五是**模型退役节奏**：OpenAI 已于 2026 年 2 月 13 日在 ChatGPT 中停用 GPT-4o 等模型（仍可通过 API 使用），提示依赖特定语音模型的系统需关注生命周期（[停用 GPT-4o 和其他 ChatGPT 模型](https://help.openai.com/zh-hans-cn/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)）。

## 参考来源

1. [Use the GPT Realtime API via WebRTC — Microsoft Learn](https://learn.microsoft.com/sl-si/azure/foundry/openai/how-to/realtime-audio-webrtc)
2. [Use the GPT Realtime API for speech and audio — Microsoft Learn](https://learn.microsoft.com/el-gr/azure/foundry/openai/how-to/realtime-audio)
3. [How we built a realtime system for responsive voice AI in six months (GPT-Live) — OpenAI](https://openai.com/index/continuous-voice-interaction-with-gpt-live/)
4. [Gemini API 版本资讯 — Google AI for Developers](https://ai.google.dev/gemini-api/docs/changelog)
5. [数智周报（Gemini 3.8 Flash TTS）](http://m.toutiao.com/group/7689702645484880420/)
6. [Scribe v2 Medical is now available to everyone — ElevenLabs](https://elevenlabs.io/blog/scribe-v2-medical-generally-available)
7. [Apple introduces Siri AI — Apple Newsroom (2026-06)](https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)
8. [Siri AI is here — Apple Newsroom (2026-09)](https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/)
9. [Apple Announces 'Siri AI' at WWDC 2026 — MacRumors](https://www.macrumors.com/2026/06/08/apple-announces-siri-ai/)
10. [Alexa+ arrives in India — About Amazon](https://www.aboutamazon.com/news/devices/alexa-plus-international-launch)
11. [Getting started with Alexa+ — About Amazon](https://www.aboutamazon.com/news/devices/new-alexa-plus-amazon-devices)
12. [Amazon's Alexa+ launches in Italy — About Amazon](https://www.aboutamazon.com/news/devices/alexa-plus-italy)
13. [Alexa+ now available to everyone in the US — About Amazon](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)
14. [Best AI Models for Voice and Speech (June 2026)](https://awesomeagents.ai/capabilities/voice-and-speech/)
15. [AI Voice and Speech Leaderboard: TTS and STT Rankings](https://awesomeagents.ai/leaderboards/ai-voice-speech-leaderboard/)
16. [Best Open Source Self-Hosted Text-to-Speech Models in 2026](https://pinggy.io/blog/best_open_source_self_hosted_text_to_speech_models/)
17. [TTS Arena: Human Preference Leaderboard](https://www.madebyagents.com/benchmarks/tts-arena)
18. [TTS Model Quality Ranking 2026: Speech Arena Results](https://www.offlinetts.com/blog/tts-model-ranking-2026/)
19. [7 бесплатных голосовых моделей (Voxtral TTS)](https://diffnotes.tech/posts/free-tts-models-replace-elevenlabs)
20. [I Benchmarked the Voice AI Stack in May 2026](https://dev.to/jays_tech/i-benchmarked-the-voice-ai-stack-in-may-2026-what-actually-holds-up-in-production-3fmn)
21. [ElevenLabs 中文官网](https://elevenlabs.io/zh)
22. [GPT-5 Available in ElevenLabs Conversational AI](https://elevenlabs.io/blog/gpt-5-available-in-elevenlabs-conversational-ai)
23. [openai-whisper on PyPI](https://pypi.org/project/openai-whisper/)
24. [WhisperKit: On-device Real-time ASR with Billion-Scale Transformers](https://arxiv.org/html/2507.10860)
25. [Benchmarking Large Pretrained Multilingual Models on Québec French Speech Recognition](https://arxiv.org/html/2508.21193)
26. [Siri vs Alexa in 2026 — Elephas](https://elephas.app/resources/siri-vs-alexa)
27. [Alexa+ vs Gemini Voice vs Siri 2026](https://versusia.fr/assistants-vocaux-ia-2026/)
28. [Gemini for Home vs. Alexa+ vs. Siri: The 2026 AI Assistant War](https://smartifiers.com/articles/ai-home-assistants-2026-gemini-vs-alexa-plus-vs-siri/)
29. [停用 GPT-4o 和其他 ChatGPT 模型 — OpenAI Help Center](https://help.openai.com/zh-hans-cn/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)
30. [Speech-to-Text Models Compared 2026: Whisper, Deepgram, AssemblyAI, ElevenLabs Scribe](https://www.web3aiblog.com/blog/speech-to-text-models-compared-whisper-deepgram-assemblyai-elevenlabs-2026)
31. [Best Open Speech Recognition (ASR) Models in 2026: WER, Languages, Latency, and License Compared](https://www.marktechpost.com/2026/07/23/best-open-speech-recognition-asr-models-in-2026-wer-languages-latency-and-license-compared/)
32. [GigaSpeechBench: A Real-World Multilingual Speech-to-Text Benchmark](https://arxiv.org/html/2606.28884v2)
33. [Contact Center AI Architecture for Voice AI (2026)](https://aivanguard.tech/contact-center-ai-production-architecture/)
34. [Speech latency in voice AI — Parloa](https://www.parloa.com/knowledge-hub/speech-latency-voice-ai/)
35. [Best Voice Agents for Call Centers in 2026 — Retell AI](https://www.retellai.com/blog/best-voice-agents-for-call-centers)
36. [8 Best Voice AI Agent Companies for Contact Centers (2026) — Retell AI](https://www.retellai.com/blog/best-voice-ai-agent-companies-contact-centers)