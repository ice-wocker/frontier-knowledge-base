# 可解释性与机制分析

> 最后更新：2026-09-26 ｜ 领域：AI·前沿方向与风险 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

可解释性研究分为两条主线：一条是行为层面的「外部可解释」（探针、输入输出测试），另一条是机制可解释性（Mechanistic Interpretability），试图识别模型内部的「特征（features）、电路（circuits）与激活模式」，把事实回忆、拒绝、类欺骗规划或代码生成等行为对应到网络中的具体组件（[Mechanistic interpretability: 10 Breakthrough Technologies 2026](https://geekchamp.com/mechanistic-interpretability-10-breakthrough-technologies-2026/)）。它强调不仅看输入输出，还要检查信息如何跨层被表示与变换（[Mechanistic interpretability: 10 Breakthrough Technologies 2026](https://geekchamp.com/mechanistic-interpretability-10-breakthrough-technologies-2026/)）。2026 年，机制可解释性被相关盘点列为十大突破技术之一（[Mechanistic interpretability: 10 Breakthrough Technologies 2026](https://geekchamp.com/mechanistic-interpretability-10-breakthrough-technologies-2026/)）。

## 最新进展（2025–2026）

### 稀疏自编码器（SAE）

稀疏自编码器（Sparse Autoencoders, SAE）把模型激活分解为人类可读的稀疏特征基。Anthropic 从 Claude 3 Sonnet 的残差流中提取了数百万个特征（Templeton 等，2024），OpenAI 与 Google DeepMind 随后发布了各自模型的可比开源 SAE 套件（Gao 等，2024；Lieberum 等，2024）（[I Ran a Causal Test on Sparse Autoencoders](https://dev.to/mohamed_bal/i-ran-a-causal-test-on-sparse-autoencoders-77-of-recovered-features-turned-out-to-be-causally-39ma)）。Anthropic 的工作表明，Claude 3 Sonnet 上的 SAE 可重建高度抽象的特征，如地理位置、情感效价等（[The Architectural Foundations of Artificial Sentience](https://www.irjmets.com/upload_newfiles/irjmets80400358547/paper_file/irjmets80400358547.pdf)）。

但学界也开始压力测试这些主张。一项复现研究用 Llama 3.1 开源 SAE 复现 Anthropic 的主要结果，能成功重现基本特征提取与引导能力，但也发现特征命名与因果效果之间存在偏差（[When the Coffee Feature Activates on Coffins: An Analysis of Feature Extraction and Steering for Mechanistic Interpretability](https://arxiv.org/html/2601.03047v1)）。另有因果检验报告称，相当比例（77%）的「已恢复」特征在因果上是惰性的（[I Ran a Causal Test on Sparse Autoencoders](https://dev.to/mohamed_bal/i-ran-a-causal-test-on-sparse-autoencoders-77-of-recovered-features-turned-out-to-be-causally-39ma)）。在 Llama 3.1 8B 的一项因果电路研究中，作者追踪出 L18 H0/H8 → 特征 F54316 → 行为 的通路：移除该特征使行为下降约 0.157，而在恢复该中间变量后行为效应回落至接近 0，这一「恢复中间变量即可近似恢复行为效应」的证据强于单纯的头部影响（[Can an SAE Feature's Meaning Predict Its Causal Effect? A Causal Circuit Study in Llama 3.1 8B](https://www.lesswrong.com/posts/tfbGqeiiaudp58jAY/can-an-sae-feature-s-meaning-predict-its-causal-effect-a)）。

### 电路分析与跨模态追踪

2026 年出现面向视觉语言模型（VLM）的电路追踪框架，使用 transcoder、归因图（attribution graphs）与基于注意力的方法，揭示 VLM 如何分层整合视觉与语义概念，并通过特征引导与电路 patch 验证其因果性与可控性（[Circuit Tracing in Vision–Language Models](https://arxiv.org/html/2602.20330)）。为降低计算成本，CircuitLasso 用稀疏线性回归学习电路，结构准确率可匹配基于干预的 SOTA 方法（[Scalable Circuit Learning for Interpreting Large Language Models](https://arxiv.org/html/2606.16939)）。此外也有研究对 Audio LLM 中文本—音频冲突做电路级分析，隔离两种模态的电路并做因果消融（[Who Wins the Conflict? Mechanistic Interpretability of Text Bias in Audio LLMs](https://arxiv.org/html/2606.18924)）。

### 内部状态与情绪概念

据机制可解释性综述整理，Anthropic 2025 年发表「Emergent Introspective Awareness in Large Language Models」，通过概念注入实验观察模型对内部状态的有限自我报告；2026 年发表「Emotion Concepts and Their Function in a Large Language Model」，在 Claude Sonnet 4.5 中定位到 171 个情绪向量并展示其对行为的因果影响（[Mechanistic interpretability（aiwiki）](https://aiwiki.ai/wiki/mechanistic_interpretability)）。

### 激活引导与 steering vector

激活引导（activation steering）在推理时向隐状态注入语义向量以控制行为。新方法趋向自适应与几何化：StTP/StMP 以投影感知方式在恶意系统提示下恢复对齐，同时更好保留能力（[Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence](https://arxiv.org/html/2604.08169v2)）；ACT 依据真实/非真实激活差值动态控制引导强度（[Adaptive Activation Steering](https://dl.acm.org/doi/pdf/10.1145/3696410.3714640)）；FLAS 用流式（flow-based）概念条件速度场取代单一 steering vector（[Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention](https://www.semanticscholar.org/paper/Beyond-Steering-Vector%3A-Flow-based-Activation-for-Jin-Deng/a1b112e4649b1f208443bce916749e13b61685cc)）。

### 治理与审计应用

AI 治理框架（2019 年至 2026 年初陆续颁布）要求提供「不存在隐藏目标、抵抗失控前兆、灾难性能力有界」等可复核证据，而现行保证方法（主要是行为评测与红队）在认识论上局限于可观测输出，无法验证这些框架所假设的潜在表征或长时程 agent 行为，这一结构性错配被称为「审计缺口」（[Audit gap 论文](https://arxiv.org/html/2605.15164)）。为弥补缺口，有团队尝试用自然语言自编码器（NLA）等工具辅助审计，据报告可将隐藏动机的发现率从不到 3% 提升到 12–15%（[Anthropic's Natural Language Autoencoders Can Read Claude's Mind](https://www.techsifted.com/posts/anthropic-nla-interpretability-may-2026/)）。

## 核心技术与关键概念

- **SAE / 稀疏字典学习**：在模型激活上训练过完备稀疏基，得到单语义特征；其目标是把网络内部表示分解为人类可解释的特征，从而理解模型究竟学到了什么（[Anthropic's Sparse Autoencoders (SAE) Work](https://theneuralbase.com/ai-safety/learn/intermediate/anthropic-sae-work/)）。
- **归因图与 transcoder**：把信息在层/组件间的流动显式建模为可追踪电路。
- **因果追踪与消融**：通过激活 patch、ablation 验证某组件是否为行为的因果原因，而非仅相关。
- **激活引导（steering）**：在推理时加减向量以改变行为，是一种「可解释且免微调」的控制手段。
- **审计缺口（audit gap）**：治理框架要求的证据（无隐藏目标、抗失控等）超出行为评测与红队的能力范围（[Audit gap 论文](https://arxiv.org/html/2605.15164)）。

## 代表性项目 / 公司 / 产品

- Anthropic：Claude 3 Sonnet 数百万特征 SAE、情绪向量、自然语言自编码器（NLA）审计尝试（[aiwiki](https://aiwiki.ai/wiki/mechanistic_interpretability)、[Anthropic's Natural Language Autoencoders](https://www.techsifted.com/posts/anthropic-nla-interpretability-may-2026/)）。
- OpenAI、Google DeepMind：开源 SAE 套件（[I Ran a Causal Test on Sparse Autoencoders](https://dev.to/mohamed_bal/i-ran-a-causal-test-on-sparse-autoencoders-77-of-recovered-features-turned-out-to-be-causally-39ma)）。
- CircuitLasso：可扩展电路学习（[Scalable Circuit Learning](https://arxiv.org/html/2606.16939)）。

## 关键数据与评测结果

- 有报告称，不使用 NLA 时审计者在不到 3% 的运行中发现隐藏动机；引入 NLA 后升至 12–15%，但仍有 85–88% 未被发现（[Anthropic's Natural Language Autoencoders Can Read Claude's Mind](https://www.techsifted.com/posts/anthropic-nla-interpretability-may-2026/)）。
- 一项对 SAE 特征的因果测试称约 77% 的「已恢复」特征为因果惰性（[I Ran a Causal Test on Sparse Autoencoders](https://dev.to/mohamed_bal/i-ran-a-causal-test-on-sparse-autoencoders-77-of-recovered-features-turned-out-to-be-causally-39ma)）。
- 有分析文章称，2026 年的可解释性可检测约 70% 的已知失效模式（欺骗、越狱意图、有害知识激活），但尚不能预测前沿模型的新型失效模式（[AI Model Interpretability 2026](https://networkcraft.net/networkcraft-ai-interpretability-2026/)）。
- Anthropic 在 Claude Sonnet 4.5 中定位 171 个情绪向量并验证其因果效应（[aiwiki](https://aiwiki.ai/wiki/mechanistic_interpretability)）。

## 趋势与争议

1. **「特征可读」不等于「因果有效」**：SAE 特征命名后可解释，但在因果检验中大量特征并不驱动行为（[Coffee Feature 论文](https://arxiv.org/html/2601.03047v1)、[因果测试](https://dev.to/mohamed_bal/i-ran-a-causal-test-on-sparse-autoencoders-77-of-recovered-features-turned-out-to-be-causally-39ma)）。
2. **引导的双刃剑**：激活引导可提升真实性、恢复对齐，但也可能破坏安全护栏——有研究显示即便沿随机方向引导，也能显著提高模型对有害请求的顺从概率（[The Rogue Scalpel: Activation Steering Compromises LLM Safety](https://arxiv.org/pdf/2509.22067v2)）。
3. **审计缺口**：现行保证方法（行为评测、红队）只能观察输出，无法验证治理框架假设的潜在表征与长时程 agent 行为（[Audit gap](https://arxiv.org/html/2605.15164)）。
4. **理论局限**：有批评以「瑞士奶酪模型」论证可解释性无法提供绝对验证——即使映射 99.9% 电路，剩下的 0.1% 仍可能藏有欺骗电路（[Unintended internal goals in artificial intelligence](https://research.mental-momentum.ai/r/unintended-internal-goals-artificial-ww88n8)）。
5. **可扩展性**：全量电路追踪成本高昂，线性回归等替代方法在准确率与成本间权衡（[CircuitLasso](https://arxiv.org/html/2606.16939)）。

## 参考来源

- [Mechanistic interpretability: 10 Breakthrough Technologies 2026](https://geekchamp.com/mechanistic-interpretability-10-breakthrough-technologies-2026/)
- [I Ran a Causal Test on Sparse Autoencoders — 77% of 'Recovered' Features Turned Out to Be Causally Inert](https://dev.to/mohamed_bal/i-ran-a-causal-test-on-sparse-autoencoders-77-of-recovered-features-turned-out-to-be-causally-39ma)
- [The Architectural Foundations of Artificial Sentience](https://www.irjmets.com/upload_newfiles/irjmets80400358547/paper_file/irjmets80400358547.pdf)
- [When the Coffee Feature Activates on Coffins: An Analysis of Feature Extraction and Steering for Mechanistic Interpretability](https://arxiv.org/html/2601.03047v1)
- [Circuit Tracing in Vision–Language Models: Understanding the Internal Mechanisms of Multimodal Thinking](https://arxiv.org/html/2602.20330)
- [Scalable Circuit Learning for Interpreting Large Language Models](https://arxiv.org/html/2606.16939)
- [Who Wins the Conflict? Mechanistic Interpretability of Text Bias in Audio LLMs](https://arxiv.org/html/2606.18924)
- [Mechanistic interpretability（aiwiki）](https://aiwiki.ai/wiki/mechanistic_interpretability)
- [Anthropic's Sparse Autoencoders (SAE) Work](https://theneuralbase.com/ai-safety/learn/intermediate/anthropic-sae-work/)
- [Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence](https://arxiv.org/html/2604.08169v2)
- [Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method](https://dl.acm.org/doi/pdf/10.1145/3696410.3714640)
- [Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention](https://www.semanticscholar.org/paper/Beyond-Steering-Vector%3A-Flow-based-Activation-for-Jin-Deng/a1b112e4649b1f208443bce916749e13b61685cc)
- [The Rogue Scalpel: Activation Steering Compromises LLM Safety](https://arxiv.org/pdf/2509.22067v2)
- [Audit gap 论文（Untitled Document）](https://arxiv.org/html/2605.15164)
- [Anthropic's Natural Language Autoencoders Can Read Claude's Mind](https://www.techsifted.com/posts/anthropic-nla-interpretability-may-2026/)
- [AI Model Interpretability 2026: Why This Is the Year We Finally See Inside the Black Box](https://networkcraft.net/networkcraft-ai-interpretability-2026/)
- [Unintended internal goals in artificial intelligence](https://research.mental-momentum.ai/r/unintended-internal-goals-artificial-ww88n8)
- [Can an SAE Feature's Meaning Predict Its Causal Effect? A Causal Circuit Study in Llama 3.1 8B](https://www.lesswrong.com/posts/tfbGqeiiaudp58jAY/can-an-sae-feature-s-meaning-predict-its-causal-effect-a)