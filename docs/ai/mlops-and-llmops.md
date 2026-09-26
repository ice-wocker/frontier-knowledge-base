# MLOps 与 LLMOps

> 最后更新：2026-09-26 ｜ 领域：AI·平台、工具与落地 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

MLOps（Machine Learning Operations）指把软件工程中的持续集成、持续交付、监控与治理实践延伸到机器学习模型的全生命周期，典型环节包括实验跟踪、模型注册、部署发布、生产监控与回滚。MLflow 是将这些环节收敛到单一平台的代表，其官方定位强调「自动记录参数、权重、工件、代码、指标与依赖，确保实验可复现」，并内置模型注册表以控制模型状态（[MLflow - Open Source AI Platform for Agents, LLMs & Models](https://mlflow.org/)、[Mastering the ML lifecycle](https://mlflow.github.io/mlflow-website/classical-ml/)）。

LLMOps 则是 MLOps 在生成式 AI 场景下的延伸。与传统 ML 不同，LLM 应用的运维对象从「单一模型权重」扩展为一组非确定性、可分片演进的产物：提示词（prompt）、检索索引与文档库、评测集与判分器（judge）、Agent 轨迹与工具配置等。因此 LLMOps 强调「把提示词当作代码」来管理版本与发布，并用评测门禁替代单纯的单元测试（[Best practices for effective LLMOps implementation](https://www.mlflow.org/articles/tags/how-to-implement-llm-ops/)）。

## 最新进展（2025–2026）

2025–2026 年该领域最明显的变化是「可观测性平台」与「评测平台」的合并。Langfuse 把它自己描述为连接 tracing、monitoring、datasets、experiments 与 evaluation 的连续闭环，让生产信号反过来驱动改进，并在一个集成平台内覆盖「tracing、提示词管理、评测、实验」从原型到生产规模的全流程（[Langfuse](https://langfuse.com/)、[Langfuse（一体化平台）](https://langfuse.com/?trk=organization_guest_main-feed-card-text)）。LangSmith 则强调面向 Agent 的调试、生产监控与 LLM-as-judge 评测，并引入 Annotation Queues，让领域专家无需工程技能即可审阅生产轨迹，反馈直接回流到评测数据集；其 Polly AI 助手用于快速理解大体量 trace，Insights Agent 用于揭示使用模式与常见失败模式（[LLM Observability Tools to Monitor & Eval Agents](https://www.langchain.com/articles/llm-observability-tools)、[LangSmith: The Agent Engineering Platform](https://www.langchain.com/langsmith-platform)）。

MLflow 在 3.14.0 版本中引入 One-Line Agent Onboarding、Review Queues、Pytest Integration 与 LLM Playground，并支持「Continuous Online Monitoring with MLflow LLM Judges」——无需写代码即可对流入的 traces 持续运行 LLM 判分器，覆盖 safety、relevance、groundedness、correctness 等预设维度（[MLflow 3.14.0 Highlights](https://mlflow.org/releases/)）。同时 MLflow 的 observability 基于 OpenTelemetry，支持任意 LLM provider 与 agent framework，并提供 50+ 内置指标与 LLM judges（[MLflow - Open Source AI Platform](https://mlflow.org/)）。LangSmith 同样支持 OpenTelemetry：既可把 trace 数据发往既有管线，也可摄入 OTel 数据，并可跟踪用 OpenAI SDK、Anthropic SDK、Vercel AI SDK、LlamaIndex 或自定义实现构建的应用，而不仅限 LangChain（[LangSmith Observability](https://www.langchain.com/langsmith/observability)）。

在合规与数据驻留敏感的欧洲市场，自托管路线受到关注：Langfuse 4 引入基于 OpenTelemetry 的 tracing，可在不依赖 mock 或 monkey-patching 的情况下跟踪本地 LLM，其开源许可与 Docker 部署被评价为「契合 GDPR 环境下欧洲企业的强数据驻留要求」（[AI observability solutions 2026](https://www.mlflow.org/articles/tags/ai-observability-solutions-2026/)、[Top LLM Observability Tools in 2026: A Pro Guide](https://www.mlflow.org/articles/top-llm-observability-tools-in-2026-a-pro-guide/)）。

MLOps 工具生态在 2026 年进一步细分：实验与数据版本侧出现 LakeFS 的 zero-copy branching、pre-commit/merge hooks，模型监控侧以 Evidently 等库做数据与目标漂移检测，特征侧则依赖 Feature Store 统一训练与推理的特征口径（[25 Top MLOps Tools You Need to Know in 2026](https://www.datacamp.com/hi/blog/top-mlops-tools)）。

## 核心技术与关键概念

**实验跟踪与模型注册**：记录每次训练的输入、超参与产物，形成可审计的版本谱系；模型注册表管理版本状态（Staging/Production/Archived 等）并支持审批工作流，是回滚能力的基础。MLflow 的注册清单要求注册表附加滚动评估窗口上的预测性能指标（accuracy、F1、AUC）、特征漂移指标（PSI 或 Jensen-Shannon 散度）、上游数据契约变更告警与错误率，并保存 append-only 审计日志（[MLflow](https://mlflow.org/)、[AI Model Registry Management Checklist](https://mlflow.org/articles/ai-model-registry-management-checklist/)、[Kubeflow Model Registry Overview](https://www.kubeflow.org/docs/components/model-registry/overview/)）。

**提示词版本化与 CI/CD 门禁**：业界共识是提示词不应硬编码在源码中，而应存放在托管的 Prompt Registry 中，以便独立于应用代码做版本化，并允许产品经理等非工程角色参与迭代（[Continuous Integration for LLM Prompts](https://dev.to/kuldeep_paul/continuous-integration-for-llm-prompts-a-step-by-step-guide-to-automated-prompt-deployment-359k)）。MLflow 的 LLMOps 标准化清单把「提示词纳入版本控制、每次变更需评审与批准」列为第一条控制点，并把「自动化评测门禁」列为必须项——CI/CD 流水线需拦截质量不达标的提示词或模型变更（[A complete LLMOps standardization checklist](https://mlflow.org/articles/tags/llmops-process-optimization/)）。

**自动化评测门禁**：一种被记录的实现方式是版本化对比——先提交新版本但暂不设默认，用 Instruction Adherence、Task Completion 等评测器对固定数据集打分，与当前生产版本比较；若分数更低则构建失败，生产标签不移动；若通过则把标签指向新版本，形成程序化的通过/失败门禁。2026 年的实践进一步强调「按版本可观测」：评测器绑定到 prompt 版本 ID，并在 canary 打开时从 trace store 聚合该版本的指标，以捕获离线评测测不到的生产分布退化（[Best Prompt Versioning Tool for CI/CD Pipelines in 2026](https://futureagi.com/blog/best-prompt-versioning-tool-cicd-pipelines-2026/)、[Prompt Versioning and Lifecycle Management in 2026](https://futureagi.com/blog/prompt-versioning-lifecycle-management-2026/)）。AWS 的 GenAIOps 指南同样指出，PoC 阶段的手动部署必须被全自动 CI/CD 取代，由流水线在每次变更时强制质量、安全与一致性（[Hardening the generative AI application through a GenAIOps framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/preprod-hardening.html?language=en_US)）。

**监控与漂移检测**：传统 ML 侧关注数据漂移与预测漂移。MLflow 允许把分布统计、PSI 值、prediction drift rate 作为时间序列指标记录到已注册模型版本上，并配置告警规则；注册表的 stage 迁移（Staging/Production/Archived）使重训模型的晋级成为受治理、可审计的一步（[best practices for model monitoring](https://www.mlflow.org/articles/tags/best-practices-for-model-monitoring/)、[detecting model drift](https://www.mlflow.org/articles/tags/detecting-model-drift/)）。开源库 Evidently 与 Amazon SageMaker AI、MLflow 结合，可计算数据与模型漂移，并将结果接入看板、告警或自动重训流水线（[Monitoring discriminative ML models using Amazon SageMaker AI with MLflow](https://aws.amazon.com/blogs/machine-learning/monitoring-discriminative-ml-models-using-amazon-sagemaker-ai-with-mlflow/)）。

**LLM 语义指标与合规留痕**：LLMOps 的监控第三层是语义指标——由 LLM-as-judge 评估的回答质量、不当拒答率、幻觉率等。欧洲 AI Act 对高风险系统的义务自 2026 年 8 月起适用，要求可追溯性与技术文档，而持续评测日志、golden datasets、漂移报告与提示词审计恰是其技术文档的组成部分；MLflow 文章称 AI Act 要求高风险部署方保留带 trace ID 的不可篡改结构化日志至少六个月，且需支持完整执行重建；团队被建议每周做一次 LLM-as-judge 质量评测（[LLMOps et Monitoring Agents IA en Production 2026（PDF）](https://ayinedjimi-consultants.fr/static/pdf/llmops-monitoring-agents-production-2026.pdf)、[AI system evaluation guide](https://www.mlflow.org/articles/tags/ai-system-evaluation-guide/)）。

**回滚**：由于提示词、检索索引与模型权重可独立演进，LLMOps 的回滚需要「产物级」而非「应用级」的版本控制，这也是提示词必须进版本库、发布需打标签的直接原因（[LLMOps standardization checklist](https://mlflow.org/articles/tags/llmops-process-optimization/)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **MLflow**：开源 AI 平台，覆盖 tracking、registry、LLM tracing 与评测（[https://mlflow.org/](https://mlflow.org/)）。
- **LangSmith**：LangChain 推出的 observability 与评测平台，支持 OTel，并跟踪非 LangChain 构建的应用（[LangSmith Observability](https://www.langchain.com/langsmith/observability)）。
- **Langfuse**：开源、可自托管的一体化平台，支持 tracing、提示词管理、评测与实验（[Langfuse](https://langfuse.com/)、[Langfuse Overview](https://langfuse.com/docs)）。
- **Evidently**：开源漂移检测库，常与 MLflow/SageMaker 组合使用（[AWS blog](https://aws.amazon.com/blogs/machine-learning/monitoring-discriminative-ml-models-using-amazon-sagemaker-ai-with-mlflow/)）。
- **Kubeflow Model Registry**：开源模型注册组件，覆盖 release/deploy/monitor 三阶段（[Kubeflow](https://www.kubeflow.org/docs/components/model-registry/overview/)）。
- **LakeFS**：数据版本化平台，提供 zero-copy branching 与 CI/CD hooks（[25 Top MLOps Tools](https://www.datacamp.com/hi/blog/top-mlops-tools)）。
- **Future AGI**：提供提示词版本化与 CI/CD 门禁工具（[Best Prompt Versioning Tool](https://futureagi.com/blog/best-prompt-versioning-tool-cicd-pipelines-2026/)）。

## 关键数据与评测结果（附来源）

- MLflow 提供 50+ 内置指标与 LLM judges（[MLflow](https://mlflow.org/)）。
- 关于漂移监控的可操作指标，业内文章给出了 PSI 值、Jensen-Shannon 散度等量化口径（[AI Model Registry Management Checklist](https://mlflow.org/articles/ai-model-registry-management-checklist/)、[best practices for model monitoring](https://www.mlflow.org/articles/tags/best-practices-for-model-monitoring/)）。
- 关于生产监控采样与阈值：有指南建议对 5–10% 的生产 trace 采样，得分低于 7/10 时告警（[AI system evaluation guide](https://www.mlflow.org/articles/tags/ai-system-evaluation-guide/)）；另有指南给出幻觉率的告警口径——通用客服 >5%、医疗/法律等高风险场景 >1% 并强制人工复核（[AI Monitoring in Production: The Complete 2026 Engineering Guide](https://valuestreamai.com/blog/ai-monitoring-in-production-guide-2026)），亦有厂商建议受监管领域阈值取 2–3%、内部工具取 5–8%（[Production AI Hallucination Detection](https://www.openlayer.com/blog/stop-llm-hallucinations)），多口径并存。
- 合规留痕方面，MLflow 文章称 AI Act 要求高风险部署方保留带 trace ID 的不可篡改结构化日志至少六个月（[AI system evaluation guide](https://www.mlflow.org/articles/tags/ai-system-evaluation-guide/)）。

## 趋势与争议

一是**平台整合 vs 工具拼装**：一方主张把 tracing、评测、提示词管理与数据集收敛到统一平台（LangSmith/Langfuse 的叙事），另一方则用 Evidently + MLflow + 自建看板拼装，以换取可控性与可移植性。二是**自托管与数据主权**：在 GDPR 与数据驻留约束下，自托管 LLMOps 成为部分企业的首选，但其运维成本与功能迭代速度构成权衡（[AI observability solutions 2026](https://www.mlflow.org/articles/tags/ai-observability-solutions-2026/)）。三是**「提示词即代码」的边界**：把提示词完全注册化会引入额外治理开销，如何在速度与可审计之间取舍仍是争议点；同时「仅做版本 diff 而不接评测」被指为不够，评测须绑定版本并对真实流量采样运行（[Continuous Integration for LLM Prompts](https://dev.to/kuldeep_paul/continuous-integration-for-llm-prompts-a-step-by-step-guide-to-automated-prompt-deployment-359k)、[Prompt Versioning Without Evals Is Just Diff Tracking](https://www.respan.ai/blog/prompt-versioning-iteration-loop)）。四是**监控阈值的标准缺失**：不同来源对幻觉率、采样比例给出的阈值差异较大，说明该领域尚缺乏统一 SLO 共识（[AI Monitoring in Production](https://valuestreamai.com/blog/ai-monitoring-in-production-guide-2026)、[Production AI Hallucination Detection](https://www.openlayer.com/blog/stop-llm-hallucinations)）。

## 参考来源

- [MLflow - Open Source AI Platform for Agents, LLMs & Models](https://mlflow.org/)
- [Mastering the ML lifecycle](https://mlflow.github.io/mlflow-website/classical-ml/)
- [MLflow 3.14.0 Highlights](https://mlflow.org/releases/)
- [Best practices for effective LLMOps implementation](https://www.mlflow.org/articles/tags/how-to-implement-llm-ops/)
- [A complete LLMOps standardization checklist](https://mlflow.org/articles/tags/llmops-process-optimization/)
- [AI observability solutions 2026](https://www.mlflow.org/articles/tags/ai-observability-solutions-2026/)
- [Top LLM Observability Tools in 2026: A Pro Guide](https://www.mlflow.org/articles/top-llm-observability-tools-in-2026-a-pro-guide/)
- [best practices for model monitoring](https://www.mlflow.org/articles/tags/best-practices-for-model-monitoring/)
- [detecting model drift](https://www.mlflow.org/articles/tags/detecting-model-drift/)
- [AI Model Registry Management Checklist for MLOps Engineers](https://mlflow.org/articles/ai-model-registry-management-checklist/)
- [AI system evaluation guide](https://www.mlflow.org/articles/tags/ai-system-evaluation-guide/)
- [LangSmith: The Agent Engineering Platform](https://www.langchain.com/langsmith-platform)
- [LangSmith Observability: AI Agent Observability Platform](https://www.langchain.com/langsmith/observability)
- [LLM Observability Tools to Monitor & Eval Agents](https://www.langchain.com/articles/llm-observability-tools)
- [Langfuse](https://langfuse.com/)
- [Langfuse Overview](https://langfuse.com/docs)
- [Continuous Integration for LLM Prompts](https://dev.to/kuldeep_paul/continuous-integration-for-llm-prompts-a-step-by-step-guide-to-automated-prompt-deployment-359k)
- [Best Prompt Versioning Tool for CI/CD Pipelines in 2026](https://futureagi.com/blog/best-prompt-versioning-tool-cicd-pipelines-2026/)
- [Prompt Versioning and Lifecycle Management in 2026](https://futureagi.com/blog/prompt-versioning-lifecycle-management-2026/)
- [Prompt Versioning Without Evals Is Just Diff Tracking](https://www.respan.ai/blog/prompt-versioning-iteration-loop)
- [Hardening the generative AI application through a GenAIOps framework (AWS Prescriptive Guidance)](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/preprod-hardening.html?language=en_US)
- [Monitoring discriminative ML models using Amazon SageMaker AI with MLflow](https://aws.amazon.com/blogs/machine-learning/monitoring-discriminative-ml-models-using-amazon-sagemaker-ai-with-mlflow/)
- [25 Top MLOps Tools You Need to Know in 2026](https://www.datacamp.com/hi/blog/top-mlops-tools)
- [Kubeflow Model Registry Overview](https://www.kubeflow.org/docs/components/model-registry/overview/)
- [LLMOps et Monitoring Agents IA en Production 2026（PDF）](https://ayinedjimi-consultants.fr/static/pdf/llmops-monitoring-agents-production-2026.pdf)
- [AI Monitoring in Production: The Complete 2026 Engineering Guide](https://valuestreamai.com/blog/ai-monitoring-in-production-guide-2026)
- [Production AI Hallucination Detection](https://www.openlayer.com/blog/stop-llm-hallucinations)