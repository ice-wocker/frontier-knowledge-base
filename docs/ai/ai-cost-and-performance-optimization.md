# 成本与性能工程

> 最后更新：2026-09-26 ｜ 领域：AI·前沿方向与风险 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

LLM 成本与性能工程的核心是把「单位经济（unit economics）」拆解为可优化的变量。其基本关系为：每 token 成本 = 运营成本 ÷ 处理的 token 数，因此降低成本要么减少总成本，要么提升吞吐；改进该指标既可以降本、也可以提高处理的 token 量，或两者兼施。例如 LLM 基础设施月成本约 5 万美元、当月处理 500 亿 token 时，约合每百万 token 1 美元（[The tokenomics of self-hosted LLMs](https://developers.redhat.com/articles/2026/08/19/tokenomics-self-hosted-llms)）。围绕这一关系，主要杠杆包括：模型路由与级联、提示/前缀缓存（prompt caching）、批处理、量化与高效推理引擎，以及自托管与 API 之间的取舍，各手段需结合流量规模与质量约束综合取舍。

## 最新进展（2025–2026）

### 自托管 vs API 的盈亏平衡

自托管以 GPU 小时计费，成本固定，随利用率提升而摊薄；托管 API 成本近似随 token 量线性增长，但无需基础设施人员（[Hosted AI APIs vs Self-Hosted Models: Cost Comparison](https://intuitionlabs.ai/pdfs/hosted-ai-api-vs-self-hosted-llm-cost.pdf)）。GPU 租用价格方面，H100 在两份统计中分别约为 2.69–12.29 美元/小时（[Hosted AI APIs vs Self-Hosted](https://intuitionlabs.ai/pdfs/hosted-ai-api-vs-self-hosted-llm-cost.pdf)）与 H100 SXM 2.50–3.50 美元/小时、H200 3.72–5.00 美元/小时、B200 5.50–6.26 美元/小时（[Local LLM on Dedicated Servers vs Cloud APIs: TCO Comparison in 2026](https://www.hostrunway.com/blog/local-llm-on-dedicated-servers-vs-cloud-apis-tco-comparison-in-2026/)）。

关于盈亏平衡点，不同来源给出不同口径：有分析称在预留 GPU 容量、以 12 个月为窗口时，与前沿 API 的成本交叉点约在每天 200 万–500 万 token（[Self-Hosting LLMs in 2026: The Complete Guide](https://codersera.com/blog/self-hosting-llms-complete-guide-2026/)）；另一来源称对现代 GPU 上、利用率合理的 7B 级模型，交叉点约在每模型每天 5 万 token（[Self-Host LLM vs Cloud API - Cost Break-Even Analysis](https://www.tencentcloud.com/techpedia/146585?lang=en)）。两个口径差异巨大，取决于模型规模、GPU 价格与利用率假设。值得注意的是，同一款 H100 的租用单价在不同平台与时段可从约 2.69 美元/小时到 12.29 美元/小时不等，使 TCO 结论高度依赖采购渠道（[Hosted AI APIs vs Self-Hosted Models: Cost Comparison](https://intuitionlabs.ai/pdfs/hosted-ai-api-vs-self-hosted-llm-cost.pdf)）。

### 推理引擎与吞吐

推理引擎的吞吐差异直接影响单位成本。有统计称 SGLang 在 H100 上比 vLLM 吞吐高约 29%（标准负载 16,200 vs 12,500 tok/s），在前缀密集的 RAG 管线中借助 RadixAttention 最多可达 6 倍（[Self-Hosting LLMs in 2026](https://codersera.com/blog/self-hosting-llms-complete-guide-2026/)）。

### 提示缓存（Prompt Caching）

提示缓存对前缀相同的长提示复用已处理 token 的计算，降低延迟与成本，且不改变输出内容（[Prompt caching（Microsoft Foundry）](https://learn.microsoft.com/ga-ie/azure/foundry/openai/how-to/prompt-caching?view=foundry)）。价格杠杆很大：在 Claude Sonnet 4.6 上，缓存 token 为 0.30 美元/百万，而普通输入 token 为 3.00 美元/百万，即约 10 倍折扣；OpenAI GPT-5 系列缓存自动给予约 50% 折扣（[What Is Prompt Caching?](https://ai-tldr.dev/learn/llm-apis/cost-caching-rate-limits/prompt-caching-explained/)）。在真实 agent 轨迹上，提示缓存可降低 token 成本 49–80%，其中 claude-haiku-4-5 约降 77%、gpt-5.4-mini 约降 80%（[Prompt Caching with Deep Agents](https://www.langchain.com/blog/deep-agents-prompt-caching)）。需要注意，对于复用率低的提示，缓存写入溢价可能抵消收益，因此应先评估前缀复用频率（[Prompt Caching and KV Cache: Speeding Up LLM Responses](https://stackviv.ai/blog/prompt-caching-kv-cache-explained)）。以一个具体例子说明：在 Anthropic Claude Sonnet 4.5 定价（输入 3.00 美元/百万）下，单次含 50,000 输入 token 的提问成本为 0.15 美元，10 次合计 1.50 美元；启用缓存后，首次「缓存写入」按 3.75 美元/百万计约 0.1875 美元，后续「缓存读取」成本显著降低（[Prompt Caching and KV Cache: Speeding Up LLM Responses](https://stackviv.ai/blog/prompt-caching-kv-cache-explained)）。

### 模型路由与级联

级联路由（model cascading）是最激进的降本方式：先送廉价模型（如 Claude Haiku 4.5，输入约 1 美元/百万），再用质量检查（schema 校验、置信度、judge 模型）判断，通过则返回，否则升级到前沿模型（如 GPT-5.4，输入约 2.50 美元/百万）（[LLM Routing: What It Is and How to Cut Costs With It](https://gingerlabs.ai/blog/llm-semantic-routing)）。有面向生产负载的路由指南称可将 LLM API 成本减半（[Cutting LLM API Costs in Half: A Model Routing Guide for Production Workloads in 2026](https://dev.to/nathanbrooks1/cutting-llm-api-costs-in-half-a-model-routing-guide-for-production-workloads-in-2026-b4m)）。路由决策需以具体厂商定价为依据，有比较专门整理了 GPT-5.5、Claude Sonnet 4.6、Gemini 3.5 Flash 与 DeepSeek V4 的价格（[The 2026 LLM API Pricing Comparison](https://dev.to/dylanfoster1/the-2026-llm-api-pricing-comparison-gpt-55-claude-sonnet-46-gemini-35-flash-and-deepseek-v4-4g4)）。

### 输出成本与延迟

输出 token 通常比输入 token 更贵，且 token 数量本身会带来延迟，因此在比较供应商时应同时计入成本与延迟（[LLM Token Costs and Efficiency: A Practitioner's Guide (August 2026)](https://stochasticsandbox.com/posts/llm-token-costs-and-efficiency-2026-08-10/)）。按 2026 年的实践规则，采购方在比较中国开源模型的每 token 报价时，应针对 agentic 负载先乘以 2–3 倍再与前沿模型对比（[AI Model Costs 2026: US Frontier vs Chinese Open Source](https://digitalinasia.com/ai-model-cost-tracker/)）。

## 核心技术与关键概念

- **单位经济**：成本/token = 运营成本 ÷ token 数。
- **模型路由 / 级联**：按难度分配模型，廉价模型优先、必要时升级。
- **提示/前缀缓存**：复用相同前缀的 KV 计算，缓存读取价格远低于普通输入；缓存写入价格通常高于普通输入，但读取价远低于普通输入（[What Is Prompt Caching?](https://ai-tldr.dev/learn/llm-apis/cost-caching-rate-limits/prompt-caching-explained/)）。
- **质量检查（升级判定）**：schema 校验、置信度或 judge 模型决定是否从廉价模型升级（[LLM Routing](https://gingerlabs.ai/blog/llm-semantic-routing)）。
- **批处理与连续批处理**：提升 GPU 利用率以摊薄单位成本。
- **自托管 vs API**：固定成本 vs 可变成本，交叉点取决于量级与利用率，需按模型规模、GPU 价格与流量画像重算，并不存在通用答案（[Tencent Cloud](https://www.tencentcloud.com/techpedia/146585?lang=en)）。

## 关键数据与评测结果

| 事项 | 数据 | 来源 |
| --- | --- | --- |
| 每百万 token 成本示例 | 5 万美元/月 ÷ 500 亿 token ≈ 1 美元/百万 | [Red Hat](https://developers.redhat.com/articles/2026/08/19/tokenomics-self-hosted-llms) |
| GPU 租用（H100 SXM / H200 / B200） | 2.50–3.50 / 3.72–5.00 / 5.50–6.26 美元每小时 | [HostRunway](https://www.hostrunway.com/blog/local-llm-on-dedicated-servers-vs-cloud-apis-tco-comparison-in-2026/) |
| 自托管盈亏平衡 | 约 200 万–500 万 token/天（12 个月窗口） | [Codersera](https://codersera.com/blog/self-hosting-llms-complete-guide-2026/) |
| 自托管盈亏平衡（另一口径） | 7B 级约 5 万 token/天/模型 | [Tencent Cloud](https://www.tencentcloud.com/techpedia/146585?lang=en) |
| SGLang vs vLLM | H100 吞吐约 +29%；前缀密集 RAG 最多 6× | [Codersera](https://codersera.com/blog/self-hosting-llms-complete-guide-2026/) |
| 缓存价格（Claude Sonnet 4.6） | 0.30 vs 3.00 美元/百万（约 10×） | [ai-tldr.dev](https://ai-tldr.dev/learn/llm-apis/cost-caching-rate-limits/prompt-caching-explained/) |
| 提示缓存降本（真实 agent 轨迹） | 49–80% | [LangChain](https://www.langchain.com/blog/deep-agents-prompt-caching) |
| 输出 token 价格（2026-08） | Claude Haiku 4.5 $5.00、Grok 4.5 $6.00、Qwen3.7-Max $7.50、Gemini 3.5 Flash $9.00、GPT-5.4 Thinking $12.00 | [Stochastic Sandbox](https://stochasticsandbox.com/posts/llm-token-costs-and-efficiency-2026-08-10/) |

需要说明的是，上述模型名称与价格来自第三方统计与博客整理，不同来源口径不一，实际采购应以各厂商官方定价页为准。

## 趋势与争议

1. **成本口径冲突**：自托管盈亏平衡点存在「约 500 万 token/天」与「约 5 万 token/天」等差异巨大的口径，说明结论高度依赖模型规模、GPU 价格与利用率假设（[Codersera](https://codersera.com/blog/self-hosting-llms-complete-guide-2026/)、[Tencent Cloud](https://www.tencentcloud.com/techpedia/146585?lang=en)）。
2. **缓存成为标配**：前缀缓存的 10 倍折扣使其成为 agent 与长上下文产品的默认优化（[ai-tldr.dev](https://ai-tldr.dev/learn/llm-apis/cost-caching-rate-limits/prompt-caching-explained/)）。
3. **路由的质量-成本权衡**：级联虽大幅降本，但升级判定错误会损害体验，需要质量检查与评测支撑（[Gingerlabs](https://gingerlabs.ai/blog/llm-semantic-routing)）。
4. **中外模型价格差异**：有分析提醒，对中国开源模型的每 token 报价在 agentic 负载下应乘以 2–3 倍再与前沿模型比较（[AI Model Costs 2026: US Frontier vs Chinese Open Source](https://digitalinasia.com/ai-model-cost-tracker/)）。
5. **输出成本与延迟**：输出 token 通常比输入贵，且 token 量也带来延迟，单位经济需同时计入成本与延迟（[Stochastic Sandbox](https://stochasticsandbox.com/posts/llm-token-costs-and-efficiency-2026-08-10/)）。
6. **采购建议**：鉴于第三方价格表存在模型代次与口径差异，实际采购应以各厂商官方定价页与自有流量画像为准（[AI Model Costs 2026](https://digitalinasia.com/ai-model-cost-tracker/)）。

## 参考来源

- [The tokenomics of self-hosted LLMs（Red Hat）](https://developers.redhat.com/articles/2026/08/19/tokenomics-self-hosted-llms)
- [Hosted AI APIs vs Self-Hosted Models: Cost Comparison](https://intuitionlabs.ai/pdfs/hosted-ai-api-vs-self-hosted-llm-cost.pdf)
- [Local LLM on Dedicated Servers vs Cloud APIs: TCO Comparison in 2026](https://www.hostrunway.com/blog/local-llm-on-dedicated-servers-vs-cloud-apis-tco-comparison-in-2026/)
- [Self-Hosting LLMs in 2026: The Complete Guide](https://codersera.com/blog/self-hosting-llms-complete-guide-2026/)
- [Self-Host LLM vs Cloud API - Cost Break-Even Analysis（Tencent Cloud）](https://www.tencentcloud.com/techpedia/146585?lang=en)
- [Prompt caching（Microsoft Foundry）](https://learn.microsoft.com/ga-ie/azure/foundry/openai/how-to/prompt-caching?view=foundry)
- [What Is Prompt Caching?（ai-tldr.dev）](https://ai-tldr.dev/learn/llm-apis/cost-caching-rate-limits/prompt-caching-explained/)
- [Prompt Caching with Deep Agents（LangChain）](https://www.langchain.com/blog/deep-agents-prompt-caching)
- [LLM Routing: What It Is and How to Cut Costs With It](https://gingerlabs.ai/blog/llm-semantic-routing)
- [Cutting LLM API Costs in Half: A Model Routing Guide for Production Workloads in 2026](https://dev.to/nathanbrooks1/cutting-llm-api-costs-in-half-a-model-routing-guide-for-production-workloads-in-2026-b4m)
- [The 2026 LLM API Pricing Comparison: GPT-5.5, Claude Sonnet 4.6, Gemini 3.5 Flash and DeepSeek V4](https://dev.to/dylanfoster1/the-2026-llm-api-pricing-comparison-gpt-55-claude-sonnet-46-gemini-35-flash-and-deepseek-v4-4g4)
- [AI Model Costs 2026: US Frontier vs Chinese Open Source](https://digitalinasia.com/ai-model-cost-tracker/)
- [LLM Token Costs and Efficiency: A Practitioner's Guide (August 2026)](https://stochasticsandbox.com/posts/llm-token-costs-and-efficiency-2026-08-10/)
- [Prompt Caching and KV Cache: Speeding Up LLM Responses](https://stackviv.ai/blog/prompt-caching-kv-cache-explained)