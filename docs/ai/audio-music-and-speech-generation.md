# 音乐与音频生成

> 最后更新：2026-09-26 ｜ 领域：AI·生成与多模态 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

音乐与音频生成覆盖三条主线：歌曲生成（Suno、Udio 等）、语音合成与识别（TTS/ASR，如 ElevenLabs、VibeVoice、Whisper 生态），以及音效与通用音频生成（Stable Audio、MusicGen 等）。2025–2026 年最显著的产业变化是「版权合规化」：头部音乐生成公司与唱片公司达成授权合作，并陆续以「完全授权训练数据」重建模型；同时开源权重音频模型的规模与质量快速提升。本周期三条主线的代表分别是：Suno 以授权曲库重建 v6、Stability AI 发布完全授权数据训练的 Stable Audio 3.0、Microsoft Research 开源 VibeVoice 语音模型家族（[Suno Launches v6 AI Music Models with Licensed Catalogs](https://musicnews.com/news/2026-09-11-suno-launches-v6-ai-music-models-with-licensed-catalogs-amid-ongoing-copyright-lawsuits)、[Meet Stable Audio 3.0](https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models)、[VibeVoice](https://www.everydev.ai/tools/vibevoice)）。

## 最新进展（2025–2026）

- **Suno**：RIAA 于 2024 年 6 月代表 Sony、Universal、Warner 起诉 Suno，指控其未经许可使用受版权保护的音乐训练模型。Suno 于 2025 年 11 月与 Warner Music Group（WMG）达成和解与授权合作，并随后与 BMG 达成类似协议；Suno v6 成为其首个基于「已获授权音乐」构建的版本，并引入音频水印与指纹技术以抑制滥用（[Suno Launches v6 AI Music Models with Licensed Catalogs](https://musicnews.com/news/2026-09-11-suno-launches-v6-ai-music-models-with-licensed-catalogs-amid-ongoing-copyright-lawsuits)、[Major Labels Settle Suno Udio](https://ailawwiki.com/News_Major_Labels_Settle_Suno_Udio_2026)）。
- **Suno v6 时间线**：据行业分析，Suno 于 2026 年 9 月 9 日发布 v6，此前一天（9 月 8 日）宣布与独立分销商 Believe 的第三项合作；UMG 与 Sony Music 截至发稿仍与 Suno 处于诉讼状态，有报道称 UMG 与 Suno 在 2026 年 4 月陷入和解僵局且尚无开庭日期（[Suno v6: The First Fully Licensed AI Music Models](https://aitoolsreview.co.uk/insights/suno-v6-licensed-music-models)）。
- **诉讼细节**：据报道，2026 年 8 月 18 日法官 Saylor 允许 Sony 与 Universal 就 Suno 从 YouTube 下载音频一事追加 DMCA「stream-ripping」主张，但驳回了其追加 61,026 条录音的请求；唱片公司于 8 月 25 日提交首次修订起诉状，Suno 于 9 月 1 日答辩，承认使用 YT-DLP 获取 YouTube 音频，同时主张唱片公司缺乏诉讼资格（[The Suno Lawsuit: RIAA v. Suno and the Warner Settlement, Explained](https://www.aimusicpreneur.com/knowledge-base/legal/riaa-suno-copyright-case/)）。
- **和解与授权条款**：2025 年 11 月 25 日 WMG 与 Suno 宣布和解并建立「首创性」合作，为艺术家与词曲作者提供补偿与保护，涵盖姓名、形象、肖像、声音与作品在 AI 音乐中的控制权；协议使 Suno 就 Warner 曲库放弃合理使用抗辩，并约定按协商版税框架授权未来训练数据，同时计划在 2026 年推出授权模型并逐步退役既有模型（[Major Labels Settle Suno Udio](https://ailawwiki.com/News_Major_Labels_Settle_Suno_Udio_2026)、[Suno（wiki）](https://aiwiki.ai/wiki/suno)）。
- **Stability AI**：发布 Stable Audio 3.0，为使用完全授权数据训练的开源权重音乐模型家族，支持可变长度生成最长约 6 分钟、可在便携设备上完成整曲创作，用户可依 Stability AI Community License（年收入超过 100 万美元的组织适用 Enterprise License）拥有并商业化输出（[Meet Stable Audio 3.0](https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models)）。据整理，Stable Audio 3.0 于 2026 年 5 月 20 日发布，含 Small SFX / Small / Medium / Large，参数规模 459M、1.4B、2.7B 等（[Stable Audio（wiki）](https://aiwiki.ai/wiki/stable_audio/edit)、[Stability AI launches open-weight Stable Audio 3.0](https://www.aitechsuite.com/ai-news/stability-ai-launches-open-weight-stable-audio-30-for-copyright-safe-six-minute-music-generation)）。
- **语音侧**：Microsoft Research 推出开源前沿语音模型家族 VibeVoice，覆盖 TTS 与 ASR；其中 VibeVoice-TTS-1.5B 单次可生成最长 90 分钟、最多 4 位说话人、支持中英及跨语言，并被 ICLR 2026 接收为 Oral；VibeVoice-Realtime-0.5B 面向实时流式 TTS，首可闻延迟约 300ms（[Microsoft VibeVoice](https://minixium.com/en/posts/vibevoice-microsoft-open-source-voice-ai-2026/)、[VibeVoice](https://www.everydev.ai/tools/vibevoice)）。
- **实时转录**：2026 年开源实时转录/TTS 的推荐模型包括 Fish Speech V1.5、CosyVoice2-0.5B 与 IndexTTS-2（[2026年实时转录最佳开源模型](https://www.siliconflow.com/zh/articles/best-open-source-models-for-real-time-transcription)）。
- **音频生成工具链下沉到 DAW**：Stable Audio 3.0 提供网页应用与桌面插件，插件可在 Ableton、Logic、Pro Tools 等主流 DAW 内直接使用，支持音频到音频（audio-to-audio）、inpainting 与实验性分轨导出，用于制作个人采样库与歌曲起始素材（[Stable Audio](https://stableaudio.com/)）。
- **语音商业平台扩张**：ElevenLabs 以 ElevenAgents 面向企业提供语音智能体平台，客户用于客服、对话式商务、市民服务、内部培训与入库销售等场景（[ElevenLabs raises $500M Series D](https://elevenlabs.io/blog/series-d)）。

## 核心技术与关键概念

- **授权数据重建模型**：Suno v6 与 Stable Audio 3.0 均强调以「合规授权数据」训练，是版权压力下的关键转向（[Suno Launches v6](https://musicnews.com/news/2026-09-11-suno-launches-v6-ai-music-models-with-licensed-catalogs-amid-ongoing-copyright-lawsuits)、[Meet Stable Audio 3.0](https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models)）。
- **水印与指纹**：为遏制滥用，新模型普遍部署音频水印（watermarking）与指纹（fingerprint）技术（[Suno Launches v6](https://musicnews.com/news/2026-09-11-suno-launches-v6-ai-music-models-with-licensed-catalogs-amid-ongoing-copyright-lawsuits)）。
- **语义—声学自编码器**：Stable Audio 3.0 引入新的 semantic-acoustic autoencoder，并支持 inpainting 与音轨延展（[Stable Audio（wiki）](https://aiwiki.ai/wiki/stable_audio/edit)）。
- **可控音频编辑**：Stable Audio 支持 audio-to-audio、inpainting 与分轨（stems，实验性）导出，并可作为插件在 Ableton、Logic、Pro Tools 等 DAW 内使用（[Stable Audio](https://stableaudio.com/)）。
- **长时长与多说话人**：VibeVoice 把单次生成时长推到 90 分钟、4 说话人，支持自发歌唱（spontaneous singing），是长篇语音合成的重要进展（[VibeVoice](https://www.everydev.ai/tools/vibevoice)、[Microsoft VibeVoice](https://minixium.com/en/posts/vibevoice-microsoft-open-source-voice-ai-2026/)）。
- **音效与样本生成**：Stable Audio Open 面向鼓点、乐器 riff、环境声与拟音（foley）等音频样本与音效设计，生成最高 47 秒、44.1kHz 立体声（[Stable Audio Open](https://stableaudioopen.app/)）。
- **端侧/便携生成**：Stable Audio 3.0 的 Small 系列以轻量换速度（最长约 2 分钟），Medium/Large 可生成最长约 6 分 20 秒，并支持在便携设备上完成整曲创作（[Stable Audio（wiki）](https://aiwiki.ai/wiki/stable_audio/edit)）。
- **声音克隆与多语言**：开源系统可先用 LLM 做句子切分与翻译，再用带声音克隆能力的 TTS 复现原说话人音色，实现多语言克隆语音合成（[Open-Source System for Multilingual Translation and Cloned Speech Synthesis](https://arxiv.org/html/2507.02530)）；PaddleSpeech 等工具包除 ASR/TTS 外还提供关键词唤醒与说话人验证（[Speech Synthesis and Recognition Models](https://awesome-repositories.com/q/speech-to-text-and-voice-generation-models)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- Suno：Suno v6（授权模型）。
- Stability AI：Stable Audio 3.0 / Stable Audio Open（[stableaudio.com](https://stableaudio.com/)）。
- ElevenLabs：面向企业的语音合成与语音 Agent 平台 ElevenAgents（[ElevenLabs raises $500M Series D](https://elevenlabs.io/blog/series-d)）。
- Microsoft Research：VibeVoice 开源语音模型家族（[VibeVoice](https://www.everydev.ai/tools/vibevoice)）。
- 开源工具链：PaddleSpeech 等提供 ASR（含 Whisper、Wav2Vec2）与 TTS 预训练模型，支持多语言、声音克隆与实时流式（[Speech Synthesis and Recognition Models](https://awesome-repositories.com/q/speech-to-text-and-voice-generation-models)）。

## 关键数据与评测结果（附来源）

- ElevenLabs：2025 年完成 5 亿美元 D 轮融资，估值 110 亿美元，较一年前增值逾 3 倍；2025 年底 ARR 超过 3.3 亿美元，客户包括 Deutsche Telekom、Square、乌克兰政府与 Revolut（[ElevenLabs raises $500M Series D at $11B valuation](https://elevenlabs.io/blog/series-d)）。另有报道称其估值达 220 亿美元、ARR 约 6 亿美元（[ElevenLabs surges to $22B value with $600M ARR](https://thedailytechfeed.com/elevenlabs-surges-to-22b-value-with-600m-arr-and-enterprise-dominance/)——两者口径不同，并列呈现。
- Stable Audio Open：2024 年 6 月发布，1.21B 参数，最长 47 秒、44.1kHz 立体声，仅使用 Creative Commons 音频训练（[Stable Audio（wiki）](https://aiwiki.ai/wiki/stable_audio/edit)）。

## 趋势与争议

- **版权与产业重构**：从「先训练后诉讼」转向「授权合作 + 重建模型」成为主流路径；但不同唱片公司策略分化，Suno 与 UMG、Sony 的诉讼仍未了结（[Suno v6](https://aitoolsreview.co.uk/insights/suno-v6-licensed-music-models)、[Major Labels Settle Suno Udio](https://ailawwiki.com/News_Major_Labels_Settle_Suno_Udio_2026)）。
- **数据来源合法性**：Suno 使用 YT-DLP 获取 YouTube 音频的行为成为追加 DMCA 主张的焦点，凸显训练数据获取链路的合规风险（[The Suno Lawsuit](https://www.aimusicpreneur.com/knowledge-base/legal/riaa-suno-copyright-case/)）。
- **开源与商用许可**：开源权重音频模型多附带社区许可与非商用限制，规模化商用需满足收入门槛或另行授权（[Meet Stable Audio 3.0](https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models)）。
- **声音透明性与竞争压力**：随着语音克隆与实时语音普及，声音透明性（voice transparency）成为企业关注的新议题，同时软件毛利与竞争格局也给语音 AI 公司带来压力（[ElevenLabs Hits $600M ARR and $22B Valuation as Voice AI Surges](https://www.aibreakingwire.com/news/elevenlabs-hits-600m-arr-and-22b-valuation-as-voice-ai-surges)）。

## 参考来源

- [Suno Launches v6 AI Music Models with Licensed Catalogs](https://musicnews.com/news/2026-09-11-suno-launches-v6-ai-music-models-with-licensed-catalogs-amid-ongoing-copyright-lawsuits)
- [Major Labels Settle Suno Udio 2026](https://ailawwiki.com/News_Major_Labels_Settle_Suno_Udio_2026)
- [Suno v6: The First Fully Licensed AI Music Models](https://aitoolsreview.co.uk/insights/suno-v6-licensed-music-models)
- [The Suno Lawsuit: RIAA v. Suno and the Warner Settlement, Explained](https://www.aimusicpreneur.com/knowledge-base/legal/riaa-suno-copyright-case/)
- [Suno（wiki）](https://aiwiki.ai/wiki/suno)
- [Meet Stable Audio 3.0（Stability AI）](https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models)
- [Stable Audio（wiki）](https://aiwiki.ai/wiki/stable_audio/edit)
- [Stability AI launches open-weight Stable Audio 3.0](https://www.aitechsuite.com/ai-news/stability-ai-launches-open-weight-stable-audio-30-for-copyright-safe-six-minute-music-generation)
- [Stable Audio 官网](https://stableaudio.com/)
- [Stable Audio Open](https://stableaudioopen.app/)
- [ElevenLabs raises $500M Series D at $11B valuation](https://elevenlabs.io/blog/series-d)
- [ElevenLabs surges to $22B value with $600M ARR](https://thedailytechfeed.com/elevenlabs-surges-to-22b-value-with-600m-arr-and-enterprise-dominance/)
- [ElevenLabs Hits $600M ARR and $22B Valuation as Voice AI Surges](https://www.aibreakingwire.com/news/elevenlabs-hits-600m-arr-and-22b-valuation-as-voice-ai-surges)
- [Microsoft VibeVoice](https://minixium.com/en/posts/vibevoice-microsoft-open-source-voice-ai-2026/)
- [VibeVoice](https://www.everydev.ai/tools/vibevoice)
- [2026年实时转录最佳开源模型](https://www.siliconflow.com/zh/articles/best-open-source-models-for-real-time-transcription)
- [Speech Synthesis and Recognition Models](https://awesome-repositories.com/q/speech-to-text-and-voice-generation-models)
- [Open-Source System for Multilingual Translation and Cloned Speech Synthesis](https://arxiv.org/html/2507.02530)