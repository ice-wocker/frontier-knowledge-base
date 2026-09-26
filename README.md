# 前沿科技知识库（Frontier Tech Knowledge Base）

> 最后更新：2026-09-26 ｜ 收录 28 篇专题文档 ｜ 全部内容基于公开网络资料整理，逐条附来源链接

一个纯 Markdown 的前沿科技知识库，覆盖人工智能、硬件半导体、软件工程、新兴科技与产业政策五大领域。所有内容均通过公开网络检索整理而成，关键事实在正文中就地标注来源，每篇文末设有「参考来源」章节列出完整链接清单，便于逐条回溯核验。

## 说明与免责

- **信息来源**：本知识库为公开资料的整理与汇编，非原创研究。所有事实性陈述均标注了来源链接，但**不对来源的准确性、完整性作担保**。
- **时效性**：前沿科技领域迭代极快，模型版本、基准分数、法规条款、融资数据等可能在数周内变化。文中数据均标注了对应的时间点或来源日期，**请以官方一手信息为准**。
- **非主观判断**：本库刻意不加入主观预测与价值判断；对于存在多口径或来源冲突的数据，正文中会并列呈现分歧而非取单一结论。
- **引用规范**：转载或引用本库内容时，建议直接回溯原始来源链接。

## 目录

### 一、人工智能（AI）

| 文档 | 内容概要 |
| --- | --- |
| [通用大模型前沿格局](docs/ai/llm-frontier-2026.md) | OpenAI / Anthropic / Google / xAI / Meta / DeepSeek / Qwen / Kimi 等旗舰模型版本与定价对比 |
| [推理模型与测试时计算](docs/ai/reasoning-and-test-time-compute.md) | 思维链、RLVR、推理档位工程化、推理成本与延迟权衡 |
| [AI Agent](docs/ai/ai-agents.md) | 工具调用、MCP、A2A、Computer Use、多智能体、Agent 评测 |
| [大模型评测基准](docs/ai/ai-benchmarks.md) | GPQA、HLE、ARC-AGI、SWE-bench、Terminal-Bench、LMArena 与刷榜/污染问题 |
| [AI 基础设施与算力](docs/ai/ai-infrastructure-and-compute.md) | 十万卡集群、NVLink、vLLM/SGLang、MoE、液冷与数据中心电力 |
| [RAG 与上下文工程](docs/ai/rag-and-memory.md) | 向量库、混合检索、GraphRAG、Agentic RAG、长上下文之争 |
| [多模态 AI](docs/ai/multimodal-ai.md) | 原生多模态模型、图像/视频生成、实时语音、世界模型 |
| [开放权重模型生态](docs/ai/open-weight-models.md) | Llama / DeepSeek / Qwen / Gemma / Mistral / gpt-oss 与许可证、量化部署 |
| [AI 编程工具](docs/ai/ai-coding-tools.md) | Copilot、Cursor、Claude Code、Codex、Devin 与 SWE-bench 成绩、vibe coding |
| [AI 安全与对齐](docs/ai/ai-safety-and-alignment.md) | RLHF/DPO/CAI、越狱与提示注入、可解释性、前沿安全框架 |

### 二、硬件与半导体

| 文档 | 内容概要 |
| --- | --- |
| [AI 芯片与加速器](docs/hardware/ai-accelerators.md) | NVIDIA 路线图、AMD MI、Google TPU、AWS Trainium、昇腾与自研芯片 |
| [半导体制造前沿](docs/hardware/semiconductor-frontier.md) | 2nm/1.4nm 制程、GAA、背面供电、High-NA EUV、CoWoS 与 HBM |
| [量子计算](docs/hardware/quantum-computing.md) | 超导/离子阱/中性原子路线、量子纠错里程碑、后量子密码 |
| [端侧 AI](docs/hardware/edge-and-on-device-ai.md) | 手机/PC 端模型、NPU 算力、llama.cpp/MLX/ExecuTorch 等端侧推理框架 |

### 三、软件工程

| 文档 | 内容概要 |
| --- | --- |
| [云原生与 Kubernetes](docs/software/cloud-native-and-kubernetes.md) | K8s 版本节奏、Gateway API、Ambient Mesh、eBPF、GitOps、CNCF 数据 |
| [前端与 Web 平台](docs/software/frontend-and-web-platforms.md) | React/Next.js、Vue、Svelte、Vite/Rolldown、Bun/Deno、TypeScript 进展 |
| [后端语言与运行时](docs/software/backend-languages-and-runtimes.md) | Go、Rust、Java LTS、Python、.NET、Zig 与场景取舍 |
| [数据库与数据平台](docs/software/databases-and-data-platforms.md) | PostgreSQL、分布式 SQL、云原生数据库、OLAP、流处理、湖仓一体 |
| [平台工程与 DevOps](docs/software/platform-engineering-and-devops.md) | IDP/Backstage、CI/CD、IaC、OpenTelemetry、供应链安全、DORA 数据 |
| [网络安全](docs/software/cybersecurity.md) | 零信任、Passkey、后量子迁移、CNAPP、AI 新型攻击面、OWASP/CISA 清单 |

### 四、新兴科技

| 文档 | 内容概要 |
| --- | --- |
| [机器人与具身智能](docs/emerging/robotics-and-embodied-ai.md) | 人形机器人、VLA 模型、仿真与 sim2real、量产与商业化 |
| [自动驾驶](docs/emerging/autonomous-driving.md) | L2+/L3/L4、端到端路线、Robotaxi 运营数据、中美监管 |
| [空间计算与 XR](docs/emerging/spatial-computing-xr.md) | Vision Pro、Quest、Android XR、智能眼镜、光学与交互方案 |
| [生物科技与合成生物学](docs/emerging/biotech-and-synthetic-biology.md) | AI 制药、CRISPR 新进展、mRNA 平台、合成生物制造、脑机接口 |
| [新能源与气候科技](docs/emerging/new-energy-and-climate-tech.md) | 光伏、储能与固态电池、绿氢、SMR 与聚变、碳捕集与全球装机数据 |
| [航天科技](docs/emerging/space-tech.md) | 可复用火箭、卫星互联网、月球与深空任务、太空经济规模 |

### 五、产业与政策

| 文档 | 内容概要 |
| --- | --- |
| [AI 监管与政策](docs/industry/ai-regulation-and-policy.md) | 欧盟 AI Act、美国联邦与州法、中国备案与标识、国际峰会与治理分歧 |
| [Web3 与数字资产](docs/industry/web3-and-digital-assets.md) | 以太坊升级、L2、稳定币立法、RWA、DeFi、机构入场与 CBDC |

## 阅读建议

- **入门速览**：先读各文档的「概述」与「趋势与争议」两节，快速建立全局认知。
- **深度核验**：沿正文中的来源链接跳转到原始页面（官方博客、技术报告、监管原文、统计数据发布方）。
- **注意版本与口径**：涉及基准分数、版本号、价格时，务必留意正文标注的时间点与来源；不同评测口径不可直接横向比较。

## 文档规范

每篇文档遵循统一结构：

```
# 标题
> 最后更新：YYYY-MM-DD ｜ 领域：xxx ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述
## 最新进展
## 核心技术与关键概念
## 代表性项目 / 产品（附官方链接）
## 关键数据与评测结果（附来源）
## 趋势与争议
## 参考来源
```

## 贡献

欢迎通过 Issue 或 Pull Request 修正数据、补充来源或更新过时信息。提交时请遵循：

1. 任何事实性修改都必须附带可公开访问的来源链接；
2. 数据需注明对应时间点；
3. 保持「客观陈述 + 来源可追溯」的原则，不引入主观判断。