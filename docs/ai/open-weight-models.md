# 开放权重（开源）模型生态

> 最后更新：2026-09-26 ｜ 领域：人工智能 / 开放权重模型与本地部署 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 一、概述

「开放权重（open-weight）」指模型参数可公开下载、可自行部署与微调，区别于仅提供 API 的闭源模型。2025–2026 年，开放权重阵营从「追赶者」变为「半壁江山」：一方面，Meta Llama、阿里 Qwen、DeepSeek、Google Gemma、Mistral、微软 Phi、OpenAI gpt-oss、智谱 GLM、MiniMax、月之暗面 Kimi 等构成庞大的模型矩阵；另一方面，中国开源模型在 OpenRouter 等平台上的调用量持续领先。有分析称，截至 2026 年 3 月，OpenRouter 月度榜单前五名中有三席为中国模型，MiniMax、Kimi、DeepSeek 正成为全球开发者的优先选项，其优势可归纳为「开源、活跃、价格」三要素（[事关AI，中国首次超越美国 — 中新网](http://www.chinanews.com.cn/cj/2026/03-06/10582565.shtml)）。

需要澄清一个术语混淆：多数所谓「开源模型」实为**开放权重**，其许可证并非都通过 OSI 认证，例如 Llama 4 采用自定义的社区许可证，因而被明确指为「open-weight 但不是 OSI 认可的开源」（[Llama 4 — The Planet Tools](https://theplanettools.ai/tools/llama-4)）。

## 二、2025–2026 最新进展

- **DeepSeek V4**：2026 年 4 月 24 日发布并开源 DeepSeek-V4 Preview，官方称其开启「高性价比 1M 上下文时代」，含 **V4-Pro（1.6T 总参数 / 49B 激活）** 与 **V4-Flash（284B / 13B 激活）** 两个 MoE 变体（[DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)）。模型卡明确开放仓库中的权重与代码采用 **MIT 许可证**（[DeepSeek V4 Technical Documentation](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)）。该系列建立在 token-wise compression 与 **DeepSeek Sparse Attention** 之上（[Open-Weights LLM Release History and Timeline](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html)）。2026 年 9 月 10 日又发布 **DeepSeek-V4.1-Flash**，具备原生多模态视觉理解能力，官方称 GPQA Diamond 达 90% 以上（[DeepSeek API 更新日志](https://api-docs.deepseek.com/zh-cn/updates/)）。
- **阿里 Qwen**：Qwen3.5 全系开放权重采用 **Apache 2.0** 许可，支持 201 种语言（[Qwen 3.5](https://qwen3lm.com/qwen3.5/)）。旗舰 **Qwen3.8-2.4T-A95B** 于 2026 年 8 月开源，稀疏 MoE 架构拥有 2.4T 总参数、每步约 95B 激活，搭配混合注意力与 1M 上下文（[qwen3.8-2.4t-a95b Model Info](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-2-4t-a95b)）。阿里云称其已开源 460 多个模型，衍生出 30 万以上衍生模型、累计下载超 30 亿次（[Alibaba Unveils Qwen3.8-27B and Releases Weights of Qwen3.8 Flagship Model](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463)）。
- **Google Gemma 4**：2026 年 3 月 31 日发布 Gemma 4（含 E2B/E4B 等移动优先型号），4 月 16 日推出 MTP 版本，6 月 3 日发布 **Gemma 4 12B Unified**（统一、无编码器的多模态模型），并衍生 DiffusionGemma 与 Gemma 4 QAT 量化版本；官方以 **Apache 2.0** 发布权重（[Gemma 版本 — Google AI for Developers](https://ai.google.dev/gemma/docs/releases)、[Gemma 4: Byte for byte, the most capable open models](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)）。
- **OpenAI gpt-oss**：OpenAI 于 2025 年 8 月 5 日发布 **gpt-oss-120b / gpt-oss-20b**，采用 **Apache 2.0** 许可，参数结构分别为 117B/5.1B 与 21B/3.6B，上下文 128K token（[Open-Weight AI Models 2026](https://www.progressiverobot.com/2026/08/13/open-weight-ai-models-2026/)）。
- **Mistral 与 MiniMax**：Mistral Large 3（2025 年 12 月）为 675B/41B MoE、256K 上下文、Apache 2.0（[同上](https://www.progressiverobot.com/2026/08/13/open-weight-ai-models-2026/)）。MiniMax M2.5 于 2026 年 2 月 13 日全球开源并支持本地化部署（[MiniMax M2.5宣布全球开源并支持本地化部署 — 经济参考网](http://jjckb.xinhuanet.com/20260213/f083116f8a184cb4919d6b783df219ea/c.html)）；M3 于 2026 年 6 月发布；多模态生成模型 **MiniMax H3** 亦宣布开源（[MiniMax H3来了 — 上观新闻](http://m.toutiao.com/group/7668511907879354880/)）。
- **中国模型出海**：2026 年 9 月 21 日，月之暗面确认 **Kimi K3** 接入 Amazon Bedrock，全球企业开发者可直接调用（[北美云分成破冰，Kimi K3落地亚马逊Bedrock — 每日经济新闻](http://m.toutiao.com/group/7687957605545558562/)）。

## 三、核心技术与关键概念

### 1. 许可证类型

| 许可证 | 代表模型 | 特点 |
| --- | --- | --- |
| **Apache 2.0** | Qwen 3.5/3.8、Gemma 4、Mistral Large 3、gpt-oss | 宽松，允许自由商用、修改、分发 |
| **MIT** | DeepSeek V4 | 宽松，开放仓库权重与代码 |
| **Llama 社区许可** | Meta Llama 4 | 自定义商业许可，非 OSI 开源 |

**Llama 4 社区许可**的关键条款：月活超过 **7 亿** 的产品需向 Meta 单独申请许可（由其酌情授予）；衍生 AI 模型名称须含「Llama」；分发须显著标注「Built with Llama」并保留版权声明；可接受使用政策排除军事等用途（[Llama 4 许可说明](https://theplanettools.ai/tools/llama-4)、[Meta AI — aiwiki](https://aiwiki.ai/wiki/meta_ai)）。Llama 4 于 2025 年 4 月 5 日发布，为原生生多模态模型，Scout 版本上下文窗口达 **1000 万 token**，知识截止于 2024 年 8 月（[Llama 4](https://howaiworks.ai/models/llama)）。注：另有中文来源称 Llama 4 采用 Apache 2.0，与多数英文来源不符，本库以官方社区许可口径为准，读者引用时需交叉核对（[Meta Llama 4 全系列深度解析](https://blog.csdn.net/zsh_1314520/article/details/161386672)）。

### 2. 蒸馏与能力差距

**蒸馏（distillation）** 指用更强模型的输出训练另一个模型，是行业标准技术，在中国 AI 产业尤为普遍。据 Interconnects 分析，蒸馏大约能把中国公司相对美国前沿的差距缩小 **1–2 个月**（[The current balance of power in open models](https://www.interconnects.ai/p/the-current-balance-of-power-in-open)）。2026 年 2 月，Anthropic 披露三家中国实验室（DeepSeek、Moonshot、MiniMax）的「工业化规模」蒸馏活动，称其通过约 **24,000 个欺诈账号**产生了超过 **1600 万次交互**，以抽取 Claude 的推理、编码与智能体能力；Anthropic 与 OpenAI 随后将此类抽取定性为国家安全关切（[Everyone's Watching the Wrong Benchmark — Gradient](https://www.gradient.com/blog/posts/open-vs-closed-model-gap/)）。围绕此事的争论在于：闭源 API 本身可被系统性「挖矿」，而开放权重则让蒸馏变得「无需服务条款」即可进行（[What Is AI Distillation?](https://www.explainx.ai/blog/what-is-ai-distillation-knowledge-transfer-fable-5-2026)、[In Defense of Open Models — IDC](https://www.idc.com/resource-center/blog/in-defense-of-open-models-kimi-k3-distillation-and-the-future-of-intelligence/)）。

### 3. 本地部署与量化

**llama.cpp**（MIT 许可，GitHub 星标 85,000+）是本地推理生态的基石：纯 C/C++、无外部依赖，可在 NVIDIA CUDA、AMD ROCm、Apple Metal、纯 CPU 乃至 Raspberry Pi 上运行 **GGUF** 量化模型（[The Complete Guide to Local LLM Inference Tools in July 2026](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)）。典型量化档位的质量/体积权衡（以 7B 模型为例）：F16 14GB（基准）、Q8_0 8.5GB（约 99% 质量）、Q4_K_M 5.0GB（约 97%）、Q3_K_M 4.1GB（约 94%）（[Running LLMs Locally in 2026](https://technologypulse.app/2026-04-28-local-llm-guide-2026/)）。**Ollama** 与 **LM Studio** 则封装了 GGUF 的选择与运行，降低使用门槛（[GGUF Quantization Benchmarks](https://vucense.com/dev-corner/gguf-quantization-explained-q4-k-m-vs-q8-0-vs-f16-2026/)）。

## 四、代表性项目 / 产品

| 模型系列 | 开发者 | 代表版本 | 官方链接 |
| --- | --- | --- | --- |
| Llama | Meta | Llama 4（Scout / Maverick） | https://www.llama.com/ |
| DeepSeek | 深度求索 | V4-Pro / V4-Flash / V4.1-Flash | https://api-docs.deepseek.com/news/news260424 |
| Qwen | 阿里巴巴 | Qwen3.8 / Qwen3-VL / Qwen3-Omni | https://qwen.ai/ |
| Gemma | Google DeepMind | Gemma 4 | https://deepmind.google/models/gemma/ |
| Mistral | Mistral AI | Mistral Large 3 | https://mistral.ai/ |
| gpt-oss | OpenAI | gpt-oss-120b / 20b | https://openai.com/index/introducing-gpt-oss/ |
| GLM | 智谱 AI | GLM-5.3 Flash | https://www.zhipuai.cn/ |
| MiniMax | MiniMax | M2.5 / M3 / H3 | https://www.minimax.io/ |
| Kimi | 月之暗面 | Kimi K3 | https://www.moonshot.cn/ |
| Phi | 微软 | Phi 系列 | https://azure.microsoft.com/en-us/products/phi |

## 五、关键数据与评测结果

- **调用量**：中国 AI 大模型调用量连续十九周领跑，环比增长 **379%**；某周榜单中 GPT-5.6 Luna 以 12.9 万亿 Token 居第二、智谱 GLM-5.3 Flash 以 12.4 万亿 Token 升至第三、DeepSeek-V4-Flash（0731 正式版）同以 12.4 万亿 Token 居第四（[每日经济新闻](http://m.toutiao.com/group/7682613135580086825/)）。
- **性价比**：中信建投研报称国产模型 MiniMax M2.5 性能比肩 Claude Opus 4.6，但价格仅为其 **1/6–1/20**（[中新网](http://www.chinanews.com.cn/cj/2026/03-06/10582565.shtml)）。
- **能力差距**：有分析给出开放权重模型达到闭源基准分数的 **91%**，且推理成本低 **8–12 倍**（[Open Source Models Closed the Gap](https://arjunjaggi.com/blog/open-source-models-closed-the-gap)）。
- **DeepSeek V4.1-Flash**：官方称 GPQA Diamond 达 **90% 以上**（[DeepSeek API 更新日志](https://api-docs.deepseek.com/zh-cn/updates/)）。
- **Qwen3.8-2.4T-A95B 核心基准**：GPQA Diamond 92.6、PaperBench 93.0、OSWorld 86.1、BabyVision 82.0（[阿里云百炼模型信息](https://help.aliyun.com/zh/model-studio/qwen3-8-2-4t-a95b)）。

## 六、趋势与争议

1. **开源 vs 闭源的边界之争**：支持者认为开放权重降低推理成本、增强数字主权与可审计性（Google 称 Apache 2.0 发布 Gemma 4 是「巨大里程碑」，赋予开发者数字主权）（[Gemma 4 韩文博客](https://blog.google/intl/ko-kr/company-news/technology/gemma-4-kr/)）；反对者（如 Anthropic、OpenAI）担忧滥用与知识产权问题。
2. **蒸馏的合法性与安全叙事**：IDC 指出闭源厂商本就控制着被「蒸馏」系统的访问权、条款与自动化行为模式，把开放模型一律限制并不合理（[In Defense of Open Models](https://www.idc.com/resource-center/blog/in-defense-of-open-models-kimi-k3-distillation-and-the-future-of-intelligence/)）。
3. **许可证合规风险**：Llama 社区许可的 7 亿 MAU 门槛、命名与署名要求，使「开源」在法务上并非无约束；企业采用前需评估（[Llama 4 许可说明](https://theplanettools.ai/tools/llama-4)）。
4. **中国模型的全球博弈**：模型出海伴随云厂商分成等商业机制变化，分析师提醒当多个同质化中国模型供应商竞争同一分销渠道时，议价地位可能反转（[每日经济新闻](http://m.toutiao.com/group/7687957605545558562/)）。

## 参考来源

1. [Open-Weight AI Models 2026: Complete Guide to the Best](https://www.progressiverobot.com/2026/08/13/open-weight-ai-models-2026/)
2. [Open-Weights LLM Release History and Timeline](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html)
3. [DeepSeek V4 Preview Release — DeepSeek API Docs](https://api-docs.deepseek.com/news/news260424)
4. [DeepSeek V4 Technical Documentation (Model Card)](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)
5. [DeepSeek API 更新日志（V4.1-Flash）](https://api-docs.deepseek.com/zh-cn/updates/)
6. [Build with DeepSeek V4 Using NVIDIA Blackwell](https://developer.nvidia.com/blog/build-with-deepseek-v4-using-nvidia-blackwell-and-gpu-accelerated-endpoints)
7. [Qwen 3.5: The Next Generation of Open AI](https://qwen3lm.com/qwen3.5/)
8. [qwen3.8-2.4t-a95b Model Info — Alibaba Cloud Model Studio](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-2-4t-a95b)
9. [Alibaba Unveils Qwen3.8-27B and Releases Weights of Qwen3.8 Flagship Model](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463)
10. [qwen3.8-2.4t-a95b 模型信息 — 阿里云百炼](https://help.aliyun.com/zh/model-studio/qwen3-8-2-4t-a95b)
11. [Gemma 版本 — Google AI for Developers](https://ai.google.dev/gemma/docs/releases)
12. [Gemma 4: Byte for byte, the most capable open models — Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
13. [Gemma 4 — Google DeepMind](https://deepmind.google/models/gemma/gemma-4/)
14. [Gemma 4 소개 (Apache 2.0) — Google Blog](https://blog.google/intl/ko-kr/company-news/technology/gemma-4-kr/)
15. [Llama 4 — howaiworks.ai](https://howaiworks.ai/models/llama)
16. [Llama 4 License 说明 — The Planet Tools](https://theplanettools.ai/tools/llama-4)
17. [Meta AI — aiwiki.ai](https://aiwiki.ai/wiki/meta_ai)
18. [Meta Llama 4 全系列深度解析 — CSDN](https://blog.csdn.net/zsh_1314520/article/details/161386672)
19. [MiniMax M2.5宣布全球开源并支持本地化部署 — 经济参考网](http://jjckb.xinhuanet.com/20260213/f083116f8a184cb4919d6b783df219ea/c.html)
20. [MiniMax H3来了 — 上观新闻](http://m.toutiao.com/group/7668511907879354880/)
21. [中国AI大模型调用量连续十九周领跑 — 每日经济新闻](http://m.toutiao.com/group/7682613135580086825/)
22. [事关AI，中国首次超越美国 — 中新网](http://www.chinanews.com.cn/cj/2026/03-06/10582565.shtml)
23. [北美云分成破冰，Kimi K3落地亚马逊Bedrock — 每日经济新闻](http://m.toutiao.com/group/7687957605545558562/)
24. [The current balance of power in open models — Interconnects](https://www.interconnects.ai/p/the-current-balance-of-power-in-open)
25. [Everyone's Watching the Wrong Benchmark — Gradient](https://www.gradient.com/blog/posts/open-vs-closed-model-gap/)
26. [What Is AI Distillation? — ExplainX](https://www.explainx.ai/blog/what-is-ai-distillation-knowledge-transfer-fable-5-2026)
27. [In Defense of Open Models: Kimi K3, Distillation — IDC](https://www.idc.com/resource-center/blog/in-defense-of-open-models-kimi-k3-distillation-and-the-future-of-intelligence/)
28. [Open Source Models Closed the Gap](https://arjunjaggi.com/blog/open-source-models-closed-the-gap)
29. [The Complete Guide to Local LLM Inference Tools in July 2026](https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1)
30. [GGUF Quantization Benchmarks: Q4_K_M vs Q8_0 vs F16 (2026)](https://vucense.com/dev-corner/gguf-quantization-explained-q4-k-m-vs-q8-0-vs-f16-2026/)
31. [Running LLMs Locally in 2026: Ollama, LM Studio, llama.cpp](https://technologypulse.app/2026-04-28-local-llm-guide-2026/)
32. [GGUF - llama.cpp 的量化格式 — ModelScope](https://www.modelscope.cn/skills/@davila7/optimization-gguf)