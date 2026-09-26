# 前沿科技知识库（Frontier Tech Knowledge Base）

> 最后更新：2026-09-26 ｜ 收录 172 篇专题文档 ｜ 全部内容基于公开网络资料整理，逐条附来源链接

一个纯 Markdown 的前沿科技知识库，覆盖人工智能、硬件与半导体、软件工程、数据工程、网络安全、基础科学、新兴科技、产业与社会等九大领域。所有内容均通过公开网络检索整理而成，关键事实在正文中就地标注来源，每篇文末设有「参考来源」章节列出完整链接清单，便于逐条回溯核验。

## 说明与免责

- **信息来源**：本知识库为公开资料的整理与汇编，非原创研究。所有事实性陈述均标注了来源链接，但**不对来源的准确性、完整性作担保**。
- **时效性**：前沿科技领域迭代极快，模型版本、基准分数、法规条款、融资数据等可能在数周内变化。文中数据均标注了对应的时间点或来源日期，**请以官方一手信息为准**。
- **非主观判断**：本库刻意不加入主观预测与价值判断；对于存在多口径或来源冲突的数据，正文中会并列呈现分歧而非取单一结论。
- **引用规范**：转载或引用本库内容时，建议直接回溯原始来源链接。

## 目录

### 一、人工智能（AI）（46 篇）

| 文档 | 内容概要 |
| --- | --- |
| [3D 与高斯泼溅](docs/ai/3d-and-gaussian-splatting.md) | 三维内容生成的主流技术可归为两类：一是重建/渲染（Neural Radiance Fields，NeRF； |
| [Agent 工程实践（Agent Engineering Patterns）](docs/ai/agent-engineering-patterns.md) | Agent 工程（Agent Engineering）指把大语言模型（LLM）从单轮文本补全扩展为能自主规划、调用工具、维护状态并多步完成任务的系统的实践体系。 |
| [Agent 框架与工具链](docs/ai/agent-frameworks-and-tooling.md) | Agent 框架与工具链指构建 LLM 智能体（agent）所需的软件分层：编排框架（LangGraph、CrewAI、AutoGen、OpenAI Agents SDK 等）… |
| [AI Agent（智能体）技术与生态](docs/ai/ai-agents.md) | AI Agent（智能体）指以大语言模型为推理核心、能够调用工具、读取与写入外部系统、并在多步任务中自主决策的系统。 |
| [大模型评测基准（Benchmarks）](docs/ai/ai-benchmarks.md) | 评测基准（benchmark）是衡量大模型能力的标尺，也是厂商发布时的「成绩单」。 |
| [AI 编程工具与编程智能体](docs/ai/ai-coding-tools.md) | AI 编程工具已从「补全代码」演进为「自主完成任务的编程智能体（coding agent）」。 |
| [成本与性能工程](docs/ai/ai-cost-and-performance-optimization.md) | LLM 成本与性能工程的核心是把「单位经济（unit economics）」拆解为可优化的变量。 |
| [企业 AI 落地](docs/ai/ai-enterprise-adoption.md) | 企业 AI 落地指组织把 AI 能力从概念验证（PoC）推进到生产系统并产生可衡量业务价值的过程，涉及用例筛选、ROI 评估、数据准备、部署形态选择（公有云 API / 私有化 / 混合）… |
| [AI 评测实践](docs/ai/ai-evaluation-practices.md) | AI 评测实践（evaluation）指对模型与 AI 应用的能力、可靠性与安全性进行系统化测量，涵盖评测集构建、打分方法（LLM-as-judge、人工评测、A/B）、数据污染检测… |
| [AI for Science](docs/ai/ai-for-science.md) | AI for Science 指用机器学习方法加速自然科学发现，代表性方向包括：蛋白质与生物分子结构预测（AlphaFold 系列）、生物基础模型（ESM3）、材料发现（GNoME… |
| [软硬协同设计（AI Hardware-Software Co-Design）](docs/ai/ai-hardware-software-codesign.md) | 软硬协同设计（co-design）指把模型架构、数值精度、编译栈与芯片微架构作为同一系统联合优化，而非「先定模型再适配硬件」。 |
| [AI 发展史与关键里程碑](docs/ai/ai-history-and-milestones.md) | 人工智能（Artificial Intelligence, AI）作为一个被正式命名的学科，通常以 1956 年在美国达特茅斯学院（Dartmouth College）举办的暑期研讨会为起点… |
| [AI 基础设施与算力](docs/ai/ai-infrastructure-and-compute.md) | AI 基础设施是前沿模型的物理底座，涵盖超大规模训练集群、GPU/TPU 互联网络、训练与推理软件栈、模型架构效率技术（MoE、量化、KV cache 优化）、以及数据中心的电力与散热。 |
| [AI 产品与 UX](docs/ai/ai-product-and-ux.md) | 2025–2026 年，AI 产品的交互范式从「对话框」向「入口 + 智能体」演进：AI 助手不再只是插件，而成为承载任务执行、应用构建与持续工作的入口。 |
| [AI 安全与对齐（AI Safety and Alignment）](docs/ai/ai-safety-and-alignment.md) | AI 安全与对齐关注两类问题：误用风险（misuse）——模型被用于生化、网络、操控等危害； |
| [AI 搜索与深度研究（AI Search & Deep Research）](docs/ai/ai-search-and-deep-research.md) | AI 搜索（AI Search）指以对话式界面替代或补充传统关键词检索的产品形态，典型代表包括 ChatGPT Search、Google AI Overviews、Perplexity 等； |
| [AI 安全攻防](docs/ai/ai-security-threats-and-defense.md) | 随着 LLM 与 Agent 进入生产系统，AI 的攻击面从「内容风险」向「行为风险」扩散：一方面智能体在复杂环境中的错误决策或越权操作可能直接导致事故… |
| [音乐与音频生成](docs/ai/audio-music-and-speech-generation.md) | 音乐与音频生成覆盖三条主线：歌曲生成（Suno、Udio 等）、语音合成与识别（TTS/ASR，如 ElevenLabs、VibeVoice、Whisper 生态）… |
| [对话助手与语音（Conversational Assistants & Voice）](docs/ai/conversational-assistants-and-voice.md) | 对话助手与语音技术栈由四层构成：语音识别（ASR，语音转文本）、语音合成（TTS，文本转语音）、实时语音对话模型（speech-in / speech-out，端到端低延迟交互）… |
| [扩散与图像生成](docs/ai/diffusion-and-image-generation.md) | 扩散模型（Diffusion Model）已成为文生图（Text-to-Image）与图像编辑的主流范式。 |
| [分布式训练与并行策略](docs/ai/distributed-training-and-parallelism.md) | 当模型参数、激活值与优化器状态总量远超单卡显存时，训练必须切分到多卡、多节点。 |
| [小模型与高效模型](docs/ai/efficient-and-small-models.md) | 小语言模型（Small Language Model, SLM）与"高效模型"指以极低推理成本换取可用智能的一类模型，通常具备三个特征之一或多个：参数量小（一般指 3B 以下）… |
| [GPU 编程与算子：CUDA、Triton 与 FlashAttention](docs/ai/gpu-kernels-and-cuda.md) | 大模型的训练与推理性能，最终取决于 GPU 上算子（kernel）的实现质量。 |
| [图学习与知识图谱](docs/ai/graph-neural-networks-and-knowledge-graphs.md) | 图学习（Graph Learning）以图神经网络（GNN）与图 Transformer 为核心，处理节点、边与整图的表示学习； |
| [推理优化与服务：从 PagedAttention 到分离式部署](docs/ai/inference-optimization-and-serving.md) | 大语言模型推理服务（LLM Serving）的目标是在给定 GPU 预算下同时优化两个相互制约的指标：吞吐量（throughput，tokens/s）与时延（latency，TTFT / TPOT）。 |
| [可解释性与机制分析](docs/ai/interpretability-and-mechanistic-analysis.md) | 可解释性研究分为两条主线：一条是行为层面的「外部可解释」（探针、输入输出测试），另一条是机制可解释性（Mechanistic Interpretability）… |
| [通用大模型前沿格局（2025–2026）](docs/ai/llm-frontier-2026.md) | 截至 2026 年 9 月，通用大模型（frontier LLM）的竞争格局已从"单一旗舰迭代"演变为"多厂商、多层次、按月刷新"的密集竞赛。 |
| [长上下文技术：位置外推、稀疏注意力与状态空间模型](docs/ai/long-context-techniques.md) | 长上下文（Long Context）指让大语言模型在一次前向计算中处理 128K、1M 乃至更长 token 序列的能力。 |
| [MoE 稀疏架构](docs/ai/mixture-of-experts.md) | 混合专家（Mixture of Experts, MoE）通过让网络的局部组件"条件性激活"来突破稠密模型的算力约束… |
| [MLOps 与 LLMOps](docs/ai/mlops-and-llmops.md) | MLOps（Machine Learning Operations）指把软件工程中的持续集成、持续交付、监控与治理实践延伸到机器学习模型的全生命周期，典型环节包括实验跟踪、模型注册、部署发布… |
| [多模态 AI（Multimodal AI）](docs/ai/multimodal-ai.md) | 多模态 AI 指同时理解与生成文本、图像、音频、视频乃至 3D 世界的模型体系。 |
| [开源 AI 工具链](docs/ai/open-source-ai-tooling.md) | 开源 AI 工具链涵盖模型与数据托管、训练与微调、推理与服务、本地运行、评测等环节。 |
| [开放权重（开源）模型生态](docs/ai/open-weight-models.md) | 「开放权重（open-weight）」指模型参数可公开下载、可自行部署与微调，区别于仅提供 API 的闭源模型。 |
| [后训练与对齐方法](docs/ai/post-training-and-alignment-methods.md) | 后训练（Post-training）指预训练之后、使模型具备指令遵循、偏好对齐与推理能力的一系列方法。 |
| [预训练与缩放定律](docs/ai/pretraining-and-scaling-laws.md) | 预训练是 LLM 通过海量文本以自监督方式学习通用语言能力的基础阶段。 |
| [提示工程与上下文工程（Prompt & Context Engineering）](docs/ai/prompt-and-context-engineering.md) | 提示工程（Prompt Engineering）指通过设计输入文本、指令格式与示例来引导大语言模型（LLM）产生期望输出的方法体系； |
| [量化与模型压缩](docs/ai/quantization-and-model-compression.md) | 量化（Quantization）把模型权重与激活值从高精度浮点（FP16/BF16/FP32）转换为低位宽表示（FP8/INT8/INT4/FP4，甚至 INT2），以换取更小的显存占用… |
| [RAG 与上下文工程（Context Engineering）与智能体记忆](docs/ai/rag-and-memory.md) | 检索增强生成（Retrieval-Augmented Generation, RAG）曾长期被简化为「向量检索 + 拼接进提示词」的标准模式。 |
| [推理模型与测试时计算（Test-Time Compute）](docs/ai/reasoning-and-test-time-compute.md) | 推理模型（reasoning model）与测试时计算（test-time compute，TTS）是 2024 年以来的核心范式转变：模型不再「一次性作答」… |
| [推荐系统与 AI（Recommender Systems & AI）](docs/ai/recommender-systems-and-ai.md) | 推荐系统（Recommender Systems）从早期的协同过滤（Collaborative Filtering）与矩阵分解，演进到深度学习排序模型… |
| [强化学习前沿](docs/ai/reinforcement-learning-frontier.md) | 强化学习（Reinforcement Learning, RL）在 2025–2026 年重新成为大模型与具身智能的核心方法。 |
| [检索深入：稀疏、稠密、混合检索与向量搜索（Retrieval & Vector Search）](docs/ai/retrieval-and-vector-search.md) | 现代检索栈（尤其是 RAG 场景）通常由三层构成：候选召回（稀疏词法检索、稠密语义检索或两者混合）、重排序（reranking）与向量索引（ANN）。 |
| [合成数据与数据引擎](docs/ai/synthetic-data-and-data-engines.md) | 合成数据（Synthetic Data）指由模型而非人工生成、用于训练的数据。 |
| [分词与嵌入](docs/ai/tokenization-and-embeddings.md) | 分词（Tokenization）把原始文本切分为模型可处理的 token 序列，嵌入（Embedding）则把 token 或整段文本映射为稠密向量。 |
| [Transformer 架构原理](docs/ai/transformer-architecture.md) | Transformer 由 Vaswani 等人在 2017 年论文《Attention Is All You Need》中提出，是此后所有主流大语言模型的基础架构。 |
| [视频生成与世界模型](docs/ai/video-generation-and-world-models.md) | 视频生成模型在过去两年从「短片段、无声音」快速演进到「多镜头、带原生音频、可交互世界」的阶段。 |

### 二、硬件与半导体（22 篇）

| 文档 | 内容概要 |
| --- | --- |
| [先进封装](docs/hardware/advanced-packaging.md) | 当制程微缩的收益趋缓、单芯片面积受光罩尺寸与良率限制时，先进封装成为继续提升系统算力的主要路径。 |
| [AI 芯片与加速器](docs/hardware/ai-accelerators.md) | AI 加速器是支撑大模型训练与推理的物理底座。 |
| [芯片设计与 EDA](docs/hardware/chip-design-and-eda.md) | 一颗现代数字芯片从需求到可制造版图，典型流程为：架构定义 → RTL 设计（Verilog/SystemVerilog/VHDL）→ 功能验证 → 逻辑综合 → DFT（可测性设计）→ 布局布线（Pl… |
| [算力市场与 GPU 云（Compute Market and GPU Cloud）](docs/hardware/compute-market-and-gpu-cloud.md) | 算力市场指围绕 AI 训练与推理所需加速卡及其配套基础设施形成的供需与交易体系。 |
| [消费电子与移动硬件](docs/hardware/consumer-and-mobile-hardware.md) | 消费电子与移动硬件涵盖智能手机、PC（含 AI PC）、可穿戴（智能手表、手环、耳机）与 AR 眼镜等品类。 |
| [数据中心基础设施（Data Center Infrastructure and Power）](docs/hardware/data-center-infrastructure-and-power.md) | AI 训练与推理把数据中心从「IT 房地产」变成「能源与热管理工程」。 |
| [端侧 AI](docs/hardware/edge-and-on-device-ai.md) | 端侧 AI（On-Device AI）指在手机、PC、可穿戴、车载等终端本地完成模型推理，而非依赖云端。 |
| [边缘 SoC 与 NPU](docs/hardware/edge-soc-and-npu.md) | 边缘 SoC（System-on-Chip）指把 CPU、GPU、NPU（Neural Processing Unit，神经网络处理单元）、ISP、DSP、内存控制器与基带等功能模块集成到单一芯片… |
| [FPGA 与可重构计算（FPGA and Reconfigurable Computing）](docs/hardware/fpga-and-reconfigurable-computing.md) | FPGA（Field Programmable Gate Array，现场可编程门阵列）是一类可在出厂后重复编程的集成电路，其核心价值在于把硬件逻辑与数据通路按需定制… |
| [GPU 架构深入与 CUDA](docs/hardware/gpu-architecture-and-cuda.md) | GPU 最初为图形渲染设计，其核心思路是用大量相对简单的流多处理器（SM，Streaming Multiprocessor）并行执行同一段代码的不同数据（SIMT… |
| [IoT 与嵌入式硬件](docs/hardware/iot-and-embedded-hardware.md) | IoT（Internet of Things，物联网）与嵌入式硬件指面向传感、连接与控制的微控制器（MCU）、无线 SoC、通信模组与工业/边缘网关等。 |
| [光刻与半导体设备](docs/hardware/lithography-and-equipment.md) | 半导体制造设备通常分为前道（晶圆制造）与后道（封装测试）两大类。 |
| [存储技术](docs/hardware/memory-technologies.md) | 存储技术构成现代计算系统的数据层级：寄存器与 SRAM 靠近计算单元但容量小、成本高； |
| [AI 集群网络（Networking for AI Clusters）](docs/hardware/networking-for-ai-clusters.md) | AI 集群网络负责把成千上万颗加速卡连接成一个可协同训练与推理的整体，其性能直接决定大规模并行任务的效率。 |
| [类脑与新型计算（Neuromorphic and Novel Computing）](docs/hardware/neuromorphic-and-novel-computing.md) | 类脑与新型计算（neuromorphic and novel computing）指不依赖传统冯·诺依曼架构与二进制同步时钟的一类计算范式探索，包括神经形态芯片（脉冲神经网络、事件驱动）… |
| [硅光与光互连（Optical Interconnects and Photonics）](docs/hardware/optical-interconnects-and-photonics.md) | 光互连（optical interconnect）承担数据中心内计算芯片与高速网络之间海量数据的光电转换与传输，是连接算力芯片与网络的关键器件。 |
| [量子计算](docs/hardware/quantum-computing.md) | 量子计算利用叠加与纠缠等量子特性进行运算，被普遍认为有望在药物与材料模拟、优化、密码分析等领域带来突破。 |
| [RISC-V 与开放硬件](docs/hardware/risc-v-and-open-hardware.md) | RISC-V 是一套开放、免专利费的精简指令集架构（ISA），任何人可自由实现与扩展，被称为芯片界的"通用标准"，被视为突破芯片生态壁垒、发展自主可控算力的重要路线之一。 |
| [机器人硬件与执行器](docs/hardware/robot-hardware-and-actuators.md) | 机器人硬件是指支撑机器人运动与感知的物理部件体系，核心包括执行器（actuator，含电机、减速器、编码器）、灵巧手、力觉与触觉传感器、IMU、结构件与电池等。 |
| [半导体制造前沿](docs/hardware/semiconductor-frontier.md) | 半导体制造是所有前沿计算的物理基础。 |
| [半导体材料](docs/hardware/semiconductor-materials.md) | 半导体材料分为晶圆制造材料（wafer fab materials）与封装材料（packaging materials）两大类。 |
| [传感器与 MEMS](docs/hardware/sensors-and-mems.md) | 传感器是把物理量（光、声、压力、加速度、角速度、磁场等）转换为电信号的器件，是消费电子、汽车、工业与机器人感知物理世界的基础。 |

### 三、软件工程（33 篇）

| 文档 | 内容概要 |
| --- | --- |
| [AI 原生研发流程（AI-Native Development Workflow）](docs/software/ai-native-development-workflow.md) | AI 原生研发流程指把大模型与智能体（agent）作为默认参与者，嵌入从需求、设计、编码、评审、测试、文档到部署与事故响应的软件开发生命周期（SDLC），而非仅在编辑器里提供补全。 |
| [API 设计与协议](docs/software/api-design-and-protocols.md) | API 设计决定系统对外与对内的契约形态。 |
| [后端语言与运行时](docs/software/backend-languages-and-runtimes.md) | 后端语言与运行时的 2025–2026 主线是并发模型的普及化与性能的底层重写：Java 的虚拟线程走向常态、Python 进入无 GIL 时代、Go 与 Rust 补齐泛型与异步短板… |
| [缓存与存储策略（Caching and Storage Strategies）](docs/software/caching-and-storage-strategies.md) | 缓存的本质是在更快的介质上保存数据的副本，以降低延迟、减少对下游（数据库、源站）的压力。 |
| [云原生与 Kubernetes](docs/software/cloud-native-and-kubernetes.md) | 云原生（Cloud Native）已从前沿概念演变为企业基础设施的默认范式。 |
| [并发与并行（Concurrency and Parallelism）](docs/software/concurrency-and-parallelism.md) | 并发（concurrency）指多个任务在时间上重叠推进，并行（parallelism）指多个任务在同一时刻真正同时执行。 |
| [系统编程语言：C/C++ 与 Zig、Carbon 等](docs/software/cpp-and-systems-languages.md) | 系统编程语言指直接面向操作系统内核、嵌入式、编译器、数据库与高性能基础设施的语言家族，长期以 C 与 C++ 为核心。 |
| [网络安全前沿](docs/software/cybersecurity.md) | 2025–2026 年网络安全呈现「攻击面收敛于 AI 与供应链、防御重心转向身份与零信任」的双向挤压。 |
| [数据库与数据平台](docs/software/databases-and-data-platforms.md) | 2025–2026 年数据领域的核心变化有两个：AI 原生（AI-native）成为数据库的一等设计目标，以及湖仓一体与开放表格式的融合。 |
| [桌面与跨平台应用](docs/software/desktop-and-cross-platform-apps.md) | 桌面应用开发主要分为三条路线：Web 技术栈封装（Electron、Tauri）、自绘 UI 跨平台框架（Flutter Desktop、Qt… |
| [开发体验与工具（Developer Experience and Tooling）](docs/software/developer-experience-and-tooling.md) | 开发体验（Developer Experience，DX）指开发者在使用工具链、平台与流程时感受到的效率、认知负荷与满意度。 |
| [领域驱动设计（DDD）](docs/software/domain-driven-design.md) | 领域驱动设计（Domain-Driven Design, DDD）由 Eric Evans 提出，核心是在复杂业务系统中以领域模型为中心，让软件结构与业务概念对齐。 |
| [嵌入式系统与 RTOS](docs/software/embedded-systems-and-rtos.md) | 嵌入式系统以 MCU（微控制器）为核心，围绕实时操作系统（RTOS）、固件实时性、功能安全认证与 IoT 协议栈构建。 |
| [事件驱动与消息系统](docs/software/event-driven-and-messaging.md) | 事件驱动架构（EDA）以事件的产生、传输与消费组织系统，实现服务间的松耦合、异步与可扩展。 |
| [前端与 Web 平台](docs/software/frontend-and-web-platforms.md) | 2025–2026 年的前端与 Web 平台呈现出三条主线：框架编译化与去虚拟 DOM 化（Svelte Runes、Vue Vapor、Solid 编译器）… |
| [游戏开发与引擎](docs/software/game-development-and-engines.md) | 游戏开发围绕引擎、渲染、运行时架构（ECS）、网络同步与内容生产五条主线展开。 |
| [Go 生态](docs/software/go-ecosystem.md) | Go 是由 Google 主导设计的静态类型、编译型语言，以简洁语法、内置并发原语、快速编译与单一静态二进制产物为主要卖点。 |
| [Java 与 JVM 生态](docs/software/java-and-jvm-ecosystem.md) | Java 是一门面向对象的静态类型语言，依托 JVM（Java Virtual Machine）实现「一次编写，到处运行」。 |
| [JavaScript 与 TypeScript 生态](docs/software/javascript-and-typescript-ecosystem.md) | JavaScript（正式标准为 ECMAScript）是 Web 平台的通用语言，也是全球使用率最高的编程语言； |
| [低延迟系统](docs/software/low-latency-systems.md) | 低延迟系统追求从微秒到纳秒级的确定性响应，广泛用于高频交易（HFT）、实时音视频、工业控制与电信前传等场景。 |
| [微服务与分布式架构](docs/software/microservices-and-distributed-architecture.md) | 微服务架构把系统拆分为一组围绕业务能力组织、可独立部署的小型服务，配合轻量级通信机制与去中心化治理。 |
| [移动应用开发](docs/software/mobile-app-development.md) | 移动应用开发目前呈现「原生优先」与「跨平台共享」并行的格局。 |
| [单仓与构建系统（Monorepo and Build Systems）](docs/software/monorepo-and-build-systems.md) | 单仓（monorepo）指把多个项目、服务、库放在同一个版本控制仓库中统一管理； |
| [开源许可与治理（Open Source Licensing and Governance）](docs/software/open-source-licensing-and-governance.md) | 开源许可与治理研究的是三组相互纠缠的问题：代码以何种法律许可发布（许可证类型与兼容性）、项目由谁决策与维护（基金会、公司或社区治理）、以及使用方如何履行义务并控制风险（合规、SBOM、审计）。 |
| [性能工程（Performance Engineering）](docs/software/performance-engineering.md) | 性能工程是把「延迟、吞吐、资源占用」当作一等的设计约束，并用度量驱动的方式持续验证与优化的工程学科。 |
| [平台工程与 DevOps](docs/software/platform-engineering-and-devops.md) | 2025–2026 年，DevOps 的重心从「工具链拼接」转向平台工程（Platform Engineering）与AI 辅助运维。 |
| [编程语言理论与范式](docs/software/programming-language-theory.md) | 编程语言理论（Programming Language Theory, PLT）研究语言的形式语义、类型系统、内存模型与编译实现，是系统软件与工程语言设计的理论基础。 |
| [Python 生态](docs/software/python-ecosystem.md) | Python 是一门动态类型、解释执行的高级语言，以可读性与「自带电池」的标准库著称，并通过大量第三方包成为数据科学、机器学习、AI 与研究计算的事实标准。 |
| [重构与遗留系统现代化（Refactoring and Legacy Modernization）](docs/software/refactoring-and-legacy-modernization.md) | 重构指在不改变外部可观察行为的前提下改善代码内部结构； |
| [Rust 生态](docs/software/rust-ecosystem.md) | Rust 是一门面向系统编程的静态类型语言，设计目标是在不使用垃圾回收（GC）的前提下提供内存安全、并发安全与接近 C 的性能。 |
| [软件架构模式](docs/software/software-architecture-patterns.md) | 架构模式是对系统整体结构的可复用组织方式，决定依赖方向、边界划分、部署形态与演进路径。 |
| [测试与质量工程（Testing and Quality Engineering）](docs/software/testing-and-quality-engineering.md) | 测试与质量工程关注如何用可重复、可自动化的手段验证软件行为，并把质量约束固化进研发流程，而不是在交付末端做一次性把关。 |
| [WebAssembly 与 Web 平台](docs/software/webassembly-and-web-platform.md) | WebAssembly（简称 Wasm）是一种可移植的二进制指令格式，最初为在浏览器中以接近原生速度运行高性能代码而设计，随后扩展到服务端、边缘计算、插件系统与嵌入式等场景。 |

### 四、数据工程与数据平台（14 篇）

| 文档 | 内容概要 |
| --- | --- |
| [分析工程与指标](docs/data/analytics-engineering-and-metrics.md) | 分析工程（Analytics Engineering）是把软件工程实践（版本控制、测试、CI/CD、代码评审、模块化）引入数据分析领域的一门实践，其代表性工具是 dbt。 |
| [数据架构与建模](docs/data/data-architecture-and-modeling.md) | 数据架构与建模关注两件事：数据在系统间如何分层与流动（架构），以及数据以何种结构被组织与表达（建模）。 |
| [数据工程基础](docs/data/data-engineering-fundamentals.md) | 数据工程（Data Engineering）是围绕数据的采集、传输、转换、编排与质量保障构建可复用基础设施的工程学科。 |
| [数据治理与隐私](docs/data/data-governance-and-privacy.md) | 数据治理是围绕数据资产建立权责、标准、流程与度量的一整套机制，核心组件包括数据目录、血缘追踪、权限模型、分类分级、隐私合规与数据契约（Data Contract）。 |
| [数据可观测性与质量](docs/data/data-observability-and-quality.md) | 数据可观测性（Data Observability）把软件可观测性的思路引入数据平台：通过持续监控数据本身的特征（新鲜度、数据量、schema、分布、空值率等），在数据出错时主动告警并帮助定位根因。 |
| [数据库内核](docs/data/database-internals.md) | 数据库内核研究数据在磁盘与内存中如何组织、事务如何保证正确性、查询如何被优化与执行。 |
| [分布式一致性与事务](docs/data/distributed-consistency-and-transactions.md) | 分布式一致性与事务研究的是：当数据被复制到多台机器、跨多个区域甚至多个云之后，如何让系统对外表现出一致的读写语义，并在网络分区、节点故障、时钟漂移等条件下保持事务的 ACID 属性。 |
| [特征平台与 ML 数据](docs/data/feature-stores-and-ml-data.md) | 特征平台（Feature Platform）与特征存储（Feature Store）是机器学习工程中连接数据工程与模型训练/推理的中间层。 |
| [图数据库与时序数据库](docs/data/graph-and-time-series-databases.md) | 图数据库与时序数据库是两类为特定数据形态优化的专用数据库。 |
| [湖仓一体与表格式](docs/data/lakehouse-and-table-formats.md) | 湖仓一体（Lakehouse）试图把数据湖的可扩展性、开放性与数据仓库的事务性和性能结合起来，其技术地基是开放表格式（Open Table Format）。 |
| [OLAP 与查询引擎](docs/data/olap-and-query-engines.md) | OLAP（联机分析处理）与查询引擎面向大规模数据的分析与聚合查询，核心设计是列式存储加向量化执行：数据按列存储以提高压缩率与扫描效率，执行引擎以「批」（向量）为单位处理，而非逐行迭代。 |
| [搜索引擎与信息检索](docs/data/search-engines-and-information-retrieval.md) | 搜索引擎与信息检索（IR）技术负责把海量非结构化与半结构化内容组织为可检索、可排序的索引。 |
| [流处理与实时分析](docs/data/streaming-and-real-time-analytics.md) | 流处理与实时分析面向「数据到达即处理」的场景，用持续计算代替按周期批处理，把延迟从分钟/小时级压缩到秒级。 |
| [向量数据库与嵌入检索](docs/data/vector-databases-and-embeddings.md) | 向量数据库与嵌入检索（embeddings）是 RAG（检索增强生成）与语义搜索的存储与检索底座。 |

### 五、网络安全（14 篇）

| 文档 | 内容概要 |
| --- | --- |
| [AI 与 LLM 安全](docs/security/ai-security-and-llm-attacks.md) | LLM 应用的安全问题源于一个结构性事实：模型无法在上下文窗口内对"数据"与"指令"做硬性隔离。 |
| [应用安全](docs/security/application-security.md) | 应用安全（Application Security，AppSec）关注在软件设计、开发、测试与运行各阶段识别与消除应用层弱点。 |
| [云安全](docs/security/cloud-security.md) | 云安全（Cloud Security）围绕云上身份、配置、工作负载、数据与基础设施即代码（IaC）的风险展开。 |
| [合规与安全治理](docs/security/compliance-and-security-governance.md) | 安全合规与治理是把外部要求（法规、标准、行业规范）转化为可审计、可持续运行的内部控制的工程。 |
| [密码学与后量子迁移](docs/security/cryptography-and-pqc.md) | 密码学为保密性、完整性与身份认证提供数学基础。 |
| [终端与勒索软件防御](docs/security/endpoint-and-ransomware-defense.md) | 终端与勒索软件防御（Endpoint and Ransomware Defense）以端点检测与响应（EDR/XDR）、勒索攻击链阻断、备份与恢复策略、威胁情报与狩猎为核心。 |
| [身份与访问管理（IAM）](docs/security/identity-and-access-management.md) | 身份与访问管理（Identity and Access Management，IAM）负责对「谁在什么条件下可以访问什么资源」进行认证、授权与治理。 |
| [网络安全与零信任](docs/security/network-security-and-zero-trust.md) | 网络安全与零信任（Network Security and Zero Trust）关注如何在网络层控制东西向与南北向流量、抵御大流量攻击，并以身份与上下文替代静态边界。 |
| [攻防安全与漏洞赏金](docs/security/offensive-security-and-bug-bounty.md) | 攻防安全（offensive security）涵盖渗透测试、红队演练、漏洞挖掘与协调披露（CVD）、漏洞赏金计划以及漏洞交易市场。 |
| [OT 与 IoT 安全](docs/security/ot-and-iot-security.md) | OT（Operational Technology）安全关注工业自动化与控制系统（IACS/ICS）、SCADA、PLC、HMI 等生产环境的可用性、完整性与安全性； |
| [隐私增强技术（PETs）](docs/security/privacy-enhancing-technologies.md) | 隐私增强技术（Privacy-Enhancing Technologies, PETs）指在保留数据可用价值的前提下，降低个人数据暴露面的一类技术集合… |
| [安全运营与 SOC](docs/security/security-operations-and-soc.md) | 安全运营中心（Security Operations Center, SOC）承担持续监控、检测、分诊、响应与复盘的职责，其技术栈通常由 SIEM（日志汇聚与关联分析）、SOAR（编排… |
| [软件供应链安全](docs/security/supply-chain-security.md) | 软件供应链安全关注代码从源码、依赖、构建、打包到分发全链路被篡改的风险。 |
| [威胁态势 2026](docs/security/threat-landscape-2026.md) | 2025–2026 年的全球网络安全威胁态势呈现三个相互叠加的特征：勒索软件在「攻击量激增」与「赎金支付萎缩」之间背离，国家级 APT 活动向供应链与云基础设施纵深渗透… |

### 六、基础科学前沿（14 篇）

| 文档 | 内容概要 |
| --- | --- |
| [天文与宇宙学](docs/science/astronomy-and-cosmology.md) | 2025–2026 年的天文学与宇宙学由三股力量推动：詹姆斯·韦布空间望远镜（JWST）持续产出系外行星大气与早期宇宙观测； |
| [生物学与基因组学](docs/science/biology-and-genomics.md) | 2025–2026 年，生物学与基因组学的推进主要沿三个方向：单细胞与空间组学把「图谱化」从组织推进到全身体、全胚胎尺度； |
| [化学与催化](docs/science/chemistry-and-catalysis.md) | 化学与催化前沿在 2025–2026 年的核心特征，是「AI 与自动化」对传统合成化学与催化研发流程的系统性渗透：从反应产率预测、逆设计催化剂，到由 AI 智能体自主规划并执行实验的闭环工作流… |
| [气候科学与地球系统](docs/science/climate-science-and-earth-system.md) | 气候科学以地球系统为对象，涵盖大气、海洋、冰冻圈、陆地生物圈及其与人类活动的相互作用，通过观测、再分析、数值模式与统计归因来理解气候变化的成因与后果。 |
| [复杂系统与网络科学](docs/science/complex-systems-and-network-science.md) | 复杂系统研究由大量异质单元通过非线性相互作用组成的系统如何涌现出宏观有序行为，网络科学则以图、超图与多层网络为语言刻画结构—功能关系。 |
| [计算科学与仿真](docs/science/computational-science-and-simulation.md) | 计算科学以数值方法、算法与高性能计算（HPC）求解无法解析处理的数学模型，覆盖分子动力学、计算流体力学（CFD）、电子结构计算、数字孪生等方向。 |
| [信息论与编码](docs/science/information-theory-and-coding.md) | 信息论研究信息度量、压缩与传输的理论极限； |
| [材料科学](docs/science/materials-science.md) | 材料科学前沿在 2025–2026 年呈现出「AI 驱动发现 + 自动化实验」与「经典体系持续突破」双线并进的特征… |
| [数学前沿](docs/science/mathematics-frontier.md) | 数学前沿通常由三类事件标记：顶级奖项的颁发（菲尔兹奖等）、长期悬而未决猜想被证明或推翻，以及人工智能开始实质性介入数学研究与证明流程。 |
| [神经科学](docs/science/neuroscience.md) | 神经科学在 2025–2026 年的主线是「连接组（connectome）与脑图谱的规模化」：从完整果蝇脑到完整的雄性果蝇中枢神经系统，连接组研究不断突破规模与跨脑区连通的限制； |
| [开放科学与科研基础设施](docs/science/open-science-and-research-infrastructure.md) | 开放科学主张研究成果（论文、数据、代码、协议）可发现、可访问、可互操作、可复用，并通过预印本、开放获取、数据仓储与科研评价改革来落地。 |
| [物理学前沿](docs/science/physics-frontier.md) | 物理学前沿在 2025–2026 年围绕几条主线推进：大型对撞机（LHC Run 3）在 13.6 TeV 能量下持续检验标准模型； |
| [量子信息科学](docs/science/quantum-information-science.md) | 量子信息科学研究如何利用叠加、纠缠与测量等量子特性处理信息，涵盖量子计算、量子通信/量子网络与量子传感/计量三大方向。 |
| [统计学与因果推断](docs/science/statistics-and-causal-inference.md) | 统计学提供从有限样本推断总体、量化不确定性与设计实验的工具； |

### 七、新兴科技（26 篇）

| 文档 | 内容概要 |
| --- | --- |
| [6G 与下一代连接](docs/emerging/6g-and-next-gen-connectivity.md) | 6G（第六代移动通信）是继 5G 之后的下一代无线通信网络，核心目标是从「万物互联」向「万物智联」跃迁，将通信、感知、计算与 AI 深度融合，构建空天地一体化网络。 |
| [AI 制药（AI Drug Discovery）](docs/emerging/ai-drug-discovery.md) | AI 制药指把机器学习、生成式模型、蛋白质结构预测与自动化实验室（干湿闭环）等技术，用于靶点发现与验证、分子生成与优化、成药性与毒性预测、临床方案设计等环节，目标是缩短研发周期、降低失败率与成本。 |
| [配送机器人与物流自动化（Autonomous Delivery and Logistics Robots）](docs/emerging/autonomous-delivery-and-logistics-robots.md) | 配送机器人与物流自动化覆盖两个主要方向：一是面向末端配送的无人配送车（无人城配车、配送机器人），二是面向仓内的仓储机器人（AGV/AMR、货到人系统、自动化立体库）与无人仓。 |
| [自动驾驶](docs/emerging/autonomous-driving.md) | 自动驾驶（Autonomous Driving）指车辆在无需或仅需少量人类干预下完成感知、决策与控制的技术体系。 |
| [生物科技与合成生物学](docs/emerging/biotech-and-synthetic-biology.md) | 生物科技（Biotechnology）与合成生物学（Synthetic Biology）正在被 AI 深度重塑。 |
| [脑机接口（Brain-Computer Interfaces, BCI）](docs/emerging/brain-computer-interfaces.md) | 脑机接口（Brain-Computer Interface, BCI）通过采集、解码神经信号并转换为对外部设备的控制指令，或对神经系统进行刺激，建立大脑与外部设备之间的直接通信通道。 |
| [碳捕集与气候适应（Carbon Capture & Climate Adaptation）](docs/emerging/carbon-capture-and-climate-adaptation.md) | 碳捕集、利用与封存（CCUS）及二氧化碳移除（CDR，含直接空气捕集 DAC）被视为实现净零排放的补充手段； |
| [数字健康与医疗器械（Digital Health and Medical Devices）](docs/emerging/digital-health-and-medical-devices.md) | 数字健康（digital health）涵盖远程医疗、可穿戴健康监测、数字疗法、医疗软件与 AI 医疗器械等。 |
| [无人机与低空经济（Drones and Low-Altitude Economy）](docs/emerging/drones-and-low-altitude-economy.md) | 低空经济指以低空空域为依托、以常态化低空飞行活动为牵引，辐射带动相关领域形成的综合性经济业态，核心载体包括消费级/工业级无人机与 eVTOL（电动垂直起降飞行器… |
| [电动汽车与交通电动化](docs/emerging/evs-and-transport-electrification.md) | 电动汽车（EV）与交通电动化指以动力电池与电驱动系统替代内燃机的道路交通变革，涵盖纯电动（BEV）、插电式混动（PHEV）乘用车，以及重卡、轻商用车、巴士等商用车型，并延伸至充电与换电网络… |
| [聚变能源（Fusion Energy）](docs/emerging/fusion-energy.md) | 聚变能源旨在模拟太阳内部的核反应，使轻原子核（主要是氘与氚）在极高温高压下结合并释放能量，被普遍视为近似无碳、燃料资源丰富、可提供基荷电力的潜在终极能源。 |
| [基因编辑与细胞治疗（Gene Editing and Cell Therapy）](docs/emerging/gene-editing-and-cell-therapy.md) | 基因编辑指通过核酸酶或碱基编辑工具对基因组进行定点改造，主要包括 CRISPR-Cas9 等核酸酶编辑、碱基编辑（base editing）与先导编辑（prime editing）。 |
| [人形机器人（Humanoid Robotics）](docs/emerging/humanoid-robotics.md) | 人形机器人（humanoid robot）指具备类人形态（头部、双臂、双足或轮式底盘）并能在人类环境中执行通用任务的机器人，通常被视为具身智能（embodied intelligence）的主要载体。 |
| [氢能与绿色燃料（Hydrogen & Green Fuels）](docs/emerging/hydrogen-and-green-fuels.md) | 氢能被视为难减排行业（钢铁、化工、重型交通、航运航空）脱碳的重要载体。 |
| [工业机器人与自动化（Industrial Robotics and Automation）](docs/emerging/industrial-robotics-and-automation.md) | 工业机器人指面向制造业的自动化操作系统，主要包括多关节机器人、SCARA、直角坐标、并联（Delta）机器人与协作机器人（cobot）。 |
| [长寿与抗衰老研究（Longevity and Aging Research）](docs/emerging/longevity-and-aging-research.md) | 长寿与抗衰老研究（longevity / geroscience）以「衰老是可干预的生物学过程」为前提，试图通过药理学或基因干预延缓衰老、延长健康寿命（healthspan）。 |
| [新能源与气候科技](docs/emerging/new-energy-and-climate-tech.md) | 新能源与气候科技涵盖光伏、储能、电动汽车与电池供应链、电网与虚拟电厂、绿氢、核能（含小型模块化反应堆 SMR 与聚变）、碳捕集（DAC）以及相关政策框架。 |
| [机器人与具身智能](docs/emerging/robotics-and-embodied-ai.md) | 具身智能（Embodied AI）指让智能体通过物理身体与环境交互、感知并执行任务的技术方向，其核心载体是人形机器人（Humanoid Robot）以及各类通用操作机器人。 |
| [火箭与航天发射](docs/emerging/rockets-and-space-launch.md) | 火箭与航天发射是商业航天与卫星星座部署的基础环节，核心议题包括可复用火箭技术、单位载荷发射成本、全球发射频次与商业发射市场份额。 |
| [卫星星座与卫星通信](docs/emerging/satellite-constellations-and-satcom.md) | 卫星星座与卫星通信指以大量低轨（LEO）卫星组网提供宽带互联网接入、手机直连（Direct-to-Cell / D2D）等服务的产业。 |
| [小型模块化反应堆与核能（Small Modular Reactors & Nuclear）](docs/emerging/small-modular-reactors.md) | 小型模块化反应堆（Small Modular Reactor，SMR）通常指单机功率较小（业界常以 IAEA 的约 300 MWe 上限为口径）、采用工厂预制、模块化运输与现场组装的裂变反应堆… |
| [固态电池与下一代电池（Solid-State & Next-Gen Batteries）](docs/emerging/solid-state-and-next-gen-batteries.md) | 下一代电池主要指以固态电解质替代液态电解液的全固态电池（solid-state battery），以及钠离子电池、锂金属负极、硅负极等新化学体系。 |
| [深空探索与太空经济](docs/emerging/space-exploration-and-commerce.md) | 深空探索与太空经济涵盖载人航天（月球与火星任务、空间站）、无人探测（月球、火星、小行星样本返回）、在轨服务与制造，以及由此形成的商业市场规模。 |
| [航天科技](docs/emerging/space-tech.md) | 航天科技在 2025–2026 年进入"可复用化 + 巨型星座 + 深空回归"三重加速期。 |
| [空间计算与 XR](docs/emerging/spatial-computing-xr.md) | 空间计算（Spatial Computing）与扩展现实（XR，含 VR/AR/MR）指将数字内容与物理空间融合、并通过眼动、手势、语音等自然交互方式操作的计算形态。 |
| [合成生物学与生物制造（Synthetic Biology and Bio-Manufacturing）](docs/emerging/synthetic-biology-and-bio-manufacturing.md) | 合成生物学（synthetic biology）以工程化理念设计和改造生物系统，通过标准化生物元件、基因线路与底盘细胞，实现化学品、材料、能源、食品与医药的定向生产； |

### 八、产业与政策（2 篇）

| 文档 | 内容概要 |
| --- | --- |
| [AI 监管与政策（全球）](docs/industry/ai-regulation-and-policy.md) | 截至 2026 年 9 月，全球人工智能监管已从"原则宣言"阶段进入"分阶段执法"阶段。 |
| [Web3 与数字资产](docs/industry/web3-and-digital-assets.md) | 2026 年的 Web3 与数字资产行业，已从"加密原生叙事"转向"机构基础设施 + 全球监管落地"的双轮驱动。 |

### 九、社会与数字权利（1 篇）

| 文档 | 内容概要 |
| --- | --- |
| [数字权利与监控](docs/society/digital-rights-and-surveillance.md) | 数字权利与监控（digital rights and surveillance）关注个人在数字化环境中的隐私权、免受无差别监控的权利、数据经纪（data broker）对个人信息的商业化利用… |

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
