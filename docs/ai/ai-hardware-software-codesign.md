# 软硬协同设计（AI Hardware-Software Co-Design）

> 最后更新：2026-09-26 ｜ 领域：AI·平台、工具与落地 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

软硬协同设计（co-design）指把模型架构、数值精度、编译栈与芯片微架构作为同一系统联合优化，而非「先定模型再适配硬件」。在 LLM 推理成本由内存带宽、互连与算子效率主导的背景下，协同设计被视为提升单位算力产出的关键路径。其技术抓手包括：面向硬件友好的模型结构设计（稀疏、低精度、算子规整化）、编译器与运行时（XLA、TVM、MLIR、Triton）、以及把整个加速器集群当作单一超级计算机的系统级设计。

## 最新进展（2025–2026）

**系统级协同设计成为主流叙事。** Google 在介绍 Ironwood TPU 栈时明确其核心哲学是「系统级协同设计」——把整个 TPU pod 视为一台内聚的超级计算机而非离散加速器集合；该架构建立在支持大规模 RDMA 的定制互连之上，使数千芯片可绕过主机 CPU 直接以高带宽、低延迟交换数据，Ironwood 总计拥有 1.77 PB 可直接访问的 HBM 容量（[From silicon to softmax: Inside the Ironwood AI stack](https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack)）。

**NVIDIA 推进「极端协同设计」与模型侧硬件友好设计。** 其在 2026 年 GTC 设有「Holistic Model Co-Design: Close the Loop With Software and Hardware for Inference Efficiency」专题，主张通过软硬件更紧的集成加速下一代前沿模型开发（[Holistic Model Co-Design (GTC26)](https://www.nvidia.com/en-us/on-demand/session/gtc26-s82154/)）。相关技术博客给出具体手段：Dynamo 与 Attention-FFN Disaggregation（AFD）把工作负载按最合适的处理器拆分并协调执行，以减少资源争用与延迟；NVFP4 降低精度开销，使 MoE agent 以更低延迟、更高吞吐与更小内存压力运行；TRT-LLM WideEP 面向前沿 MoE 优化大规模专家并行（[Building for the Rising Complexity of Agentic Systems with Extreme Co-Design](https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/)）。在模型架构层面，NVIDIA 提出「更宽更浅的 Transformer 在同参数量下具有更高算术强度与更低时延」，称 NVFP4 量化在 DeepSeek-R1 等基准上接近 FP8 精度却获得 4-bit 计算速度，并指出跨多 GPU 扩展专家并行可同时提升全局并发与聚合内存带宽（[AI Model Co-Design: Hardware-Friendly LLM Design](https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/)）。

**异构加速器拆分（GPU + LPU）成为新方向。** NVIDIA 介绍与 Groq 相关的 LPX 低时延推理加速器，其与 GPU 组成的异构系统形成「双引擎」架构：GPU 承担上下文密集的 prefill 与 decode attention，LPU 加速 FFN/MoE 等时延敏感的 decode 组件，从而在不牺牲 AI 工厂吞吐的前提下改善交互性（[Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform)）。

**编译栈向 MLIR 收敛。** 面向 AMD NPU 的 MLIR-AIR 工作展示了如何把 AI 工作负载从循环嵌套（loop nests）映射到硅片（[From Loop Nests to Silicon: Mapping AI Workloads onto AMD NPUs with MLIR-AIR](https://arxiv.org/html/2510.14871v1)）。Qualcomm 的 Hexagon-MLIR 是一个面向 Hexagon NPU 的开源编译栈，基于 MLIR 框架，统一支持将 Triton kernel 与 PyTorch 模型 lowering；其针对大模型的模块切分在 MLIR 层实现，可把常量（权重/偏置）单独抽出为独立模块，因为约 99% 的内存占用来自常量参数（[Hexagon-MLIR: An AI Compilation Stack For Qualcomm's Neural Processing Units (NPUs)](https://arxiv.org/pdf/2602.19762)、[Accelerating ML on Hexagon: A Glimpse into Qualcomm's MLIR-based Compiler](https://llvm.org/devmtg/2025-10/slides/quick_talks/baskaran_slama.pdf)）。开源方向还出现从 PyTorch 到可综合 SystemVerilog 的端到端工具链，利用加速器设计语言 Allo、硬件 IR Calyx 与 LLVM 下的 CIRCT 项目，并实现内存划分编译 pass（[From PyTorch to Calyx: An Open-Source Compiler Toolchain for ML Accelerators (C4ML 2026)](https://arxiv.org/html/2512.06177)）。面向 AMD AI Engine 的编译研究则用 MLIR 的 `aie` 与 `adf` 方言表达 AIE 计算 tile 间的流式连接与自适应数据流图（[Lifting to tensors when compiling scientific computing workloads for AI Engines](https://arxiv.org/html/2605.03566v1)）。在 MLIR Workshop 上还出现从张量 kernel 到可综合数据通路（datapath）的渐进算术 lowering 工作（[Progressive Arithmetic Lowering from Tensor Kernels to Synthesizable Datapaths](https://www.llvm.org/devmtg/2026-04/slides/mlir/mlir_ledoux.pdf)）。

**低精度与稀疏友好的数值设计。** NVFP4 使用 16 元素微块缩放、E4M3 块缩放因子、对 WGRAD GEMM 输入的 Random Hadamard Transform、2D 权重缩放与随机舍入，以在超低精度下保持收敛；TransformerEngine 提供的 NVFP4 训练配方可在 Blackwell 上实现 4-bit 混合精度预训练，据称相对 FP8 基线无可测精度损失（[Train Models Faster with JAX and MaxText Using NVFP4 on NVIDIA Blackwell](https://developer.nvidia.com/blog/train-models-faster-with-jax-and-maxtext-using-nvfp4-on-nvidia-blackwell)）。NVFP4 的数据类型由 1 符号位、2 指数位、1 尾数位（E2M1）构成（[NVIDIA Transformer Engine NVFP4](https://docs.nvidia.com/deeplearning/transformer-engine-releases/release-2.16/user-guide/_sources/features/low_precision_training/nvfp4/nvfp4.rst.txt)）。NVIDIA 研究侧解释 NVFP4 相对 MXFP4 的两处关键差异：块更小（16 vs 32，离群值污染减半）与更细的缩放刻度（E4M3 含尾数位对比二的幂 E8M0），并称相对二的幂缩放可将量化误差降低约 88%（[Pushing Intelligence to 4-bit](https://research.nvidia.com/labs/eai/blogs/pushing-intelligence-to-4-bit/)）。而 MXFP4 是 OCP Microscaling Formats 标准，块大小为 32，采用单一 E8M0 指数缩放，由 AMD、Arm、Intel、Microsoft、NVIDIA、Qualcomm 等多厂商共同支持（[FP4 Just Landed in llama.cpp: NVFP4 vs MXFP4 Explained (2026)](https://insiderllm.com/pdfs/fp4-inference-llamacpp-nvfp4-mxfp4.pdf)）。

## 核心技术与关键概念

**模型架构与芯片协同**：通过算子规整化、注意力/FFN 拆分（AFD）、专家并行（WideEP）、以及「更宽更浅」的网络形态匹配芯片的内存层级与互连能力（[NVIDIA Extreme Co-Design](https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/)、[AI Model Co-Design](https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/)）。

**稀疏与低精度友好设计**：硬件需原生支持低精度张量核心操作与校准 scale，模型侧则需按层敏感性分配精度；NVFP4 的微块缩放与 Random Hadamard Transform 即为对抗离群值、保持收敛的协同设计（[Train Models Faster with JAX and MaxText](https://developer.nvidia.com/blog/train-models-faster-with-jax-and-maxtext-using-nvfp4-on-nvidia-blackwell)、[NVFP4 实践](https://ollama.com/aiconjured/embeddinggemma-300M-NVFP4-Q8-GGUF)）。

**自动共设计/共搜索**：A3C3 将算法与加速器两个设计空间同时参数化并联合搜索，其中可微分架构与实现共搜索把设计决策表述为连续、可优化的变量，而非仅依赖离散的人工探索，从而自动生成更好平衡精度、延迟、吞吐、能效与硬件利用率的「模型—加速器」对（[A3C3: AI Algorithm and Accelerator Co-design, Co-search, and Co-generation](https://arxiv.org/html/2606.20869)）。

**编译栈**：
- **XLA**：最初是 TensorFlow/JAX 的独立编译器，现已越来越多采用 MLIR 组件以增强模块化与可扩展性；其要求函数大体纯（无副作用）且具备静态形状以取得最佳效果，相同形状/类型的后续调用复用已编译版本从而加速（[Unlocking AI Potential: Navigating the Challenges and Opportunities of Diverse Hardware Accelerators](https://the-ai-alliance.github.io/ai-accelerator-software-ecosystem-guide/ecosystem-guide/)、[From Loop Nests to Silicon](https://arxiv.org/html/2510.14871v1)）。一条典型 lowering 流水线为 JAX primitives → Jaxpr → StableHLO → 简化 → MHLO → LLVM IR 或 NVVM IR（[Interpretable AI with MLIR (IAM)](https://dl.acm.org/doi/10.1145/3774748.3787677)）。
- **TVM**：近年以 IRModule（Relax + TensorIR/TIR）为编译管线中心，支持从图级变换到张量程序优化再到目标特定代码生成的分阶段 lowering，覆盖算子融合、内存规划与多后端 lowering（[Unlocking AI Potential](https://the-ai-alliance.github.io/ai-accelerator-software-ecosystem-guide/ecosystem-guide/)）。其 AutoTVM 采用模板引导搜索，Ansor 扩展为无模板搜索，但受限于单算子调优、缺乏跨算子划分意识（[From LLM to Silicon: RL-Driven ASIC Architecture Exploration for On-Device AI Inference](https://arxiv.org/html/2604.07526v1)）。
- **MLIR**：提供多级 IR 简化渐进 lowering，但被指出不具备内建 PPA（功耗/性能/面积）感知的优化回路（[From LLM to Silicon](https://arxiv.org/html/2604.07526v1)）。
- **Triton**：被多份资料列为自定义 kernel 开发的主流路径之一，并在 Hexagon-MLIR 等栈中被作为 lowering 输入（[Hardware Acceleration: TPUs vs GPUs vs custom ASICs for Inference](https://www.shyankdev.com/blogs/hardware-acceleration-tpus-vs-gpus-vs-custom-asics-inference)、[Hexagon-MLIR](https://arxiv.org/pdf/2602.19762)）。

**运行时与 megakernel**：2026 年吞吐提升的一部分来自运行时层面的变化——从逐算子启动转向常驻 megakernel（如 TileRT 所代表的路线）（[Lecture 03 - Compilers and Runtimes: From Autoscheduling to Megakernels](https://jared-hpc.com/ai-hardware-engineer-roadmap/Phase%205%20-%20Advanced%20Topics%20and%20Specialization/7.%20ML%20Systems%20Engineering/MLSys%20Deep%20Dives/Lecture-03/)）。

**定制加速器适配**：不同加速器在动态形状支持、自定义 kernel 开发与推理框架集成上差异显著——例如 NVIDIA 侧动态形状原生支持、可用 Triton/CUDA C++/CuTe 开发并集成 vLLM/SGLang/TensorRT-LLM；Google 侧 JAX/Pallas 与 OpenXLA 需 bucketing/padding；Groq 采用固定形状的静态编译器；AWS Neuron SDK 需静态维度绑定（[Hardware Acceleration: TPUs vs GPUs vs custom ASICs](https://www.shyankdev.com/blogs/hardware-acceleration-tpus-vs-gpus-vs-custom-asics-inference)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Google Ironwood TPU 栈**：系统级协同设计、定制 RDMA 互连（[https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack](https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack)）。
- **NVIDIA**：Dynamo、AFD、NVFP4、TRT-LLM WideEP、异构 GPU+LPU（LPX）（[https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/](https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/)、[LPX](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform)）。
- **AMD MLIR-AIR / Qualcomm Hexagon-MLIR**：面向 NPU 的 MLIR 编译栈（[MLIR-AIR](https://arxiv.org/html/2510.14871v1)、[Hexagon-MLIR](https://arxiv.org/pdf/2602.19762)）。
- **SambaNova SambaFlow**：编译器与运行时栈，将 PyTorch/TensorFlow 图映射到 RDU 的 PCU/PMU（[SambaNova Systems](https://aiwiki.ai/wiki/sambanova)）。
- **Groq Static Compiler / AWS Neuron SDK**：固定形状 / 静态维度绑定的定制工具链（[Hardware Acceleration](https://www.shyankdev.com/blogs/hardware-acceleration-tpus-vs-gpus-vs-custom-asics-inference)）。
- **Apache TVM / XLA / MLIR-based（IREE、torch-mlir）**：主流开源编译栈（[Lecture 5: ML-to-Hardware Compilation Pipelines](https://jared-hpc.com/ai-hardware-engineer-roadmap/Phase%205%20-%20Advanced%20Topics%20and%20Specialization/6.%20AI%20Chip%20Design/Lectures/Lecture-05/)、[Unlocking AI Potential](https://the-ai-alliance.github.io/ai-accelerator-software-ecosystem-guide/ecosystem-guide/)）。

## 关键数据与评测结果（附来源）

- Ironwood TPU：1.77 PB 可直接访问 HBM 容量，定制互连支持数千芯片大规模 RDMA（Google 官方）（[Inside the Ironwood AI stack](https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack)）。
- SambaNova SambaFlow 支持的算子数量远小于 PyTorch 的 3,000+ 算子（第三方评测）（[The xPU-athalon: Quantifying the Competition of AI Acceleration](https://arxiv.org/html/2604.10852v1)、[SambaNova Systems](https://aiwiki.ai/wiki/sambanova)）。
- PyTorch to Calyx 工具链可生成经优化的、可在 FPGA 上实现的硬件（论文自述）（[From PyTorch to Calyx](https://arxiv.org/html/2512.06177)）。
- 量化实践：NVFP4 用于 FFN 权重、norm 保留 F32 以符合 CUDA kernel 约束（[NVFP4-Q8-GGUF](https://ollama.com/aiconjured/embeddinggemma-300M-NVFP4-Q8-GGUF)）。
- NVFP4 vs MXFP4：块大小 16 vs 32、缩放 E4M3 vs E8M0，NVIDIA 称相对二的幂缩放量化误差降低约 88%（NVIDIA 研究）（[Pushing Intelligence to 4-bit](https://research.nvidia.com/labs/eai/blogs/pushing-intelligence-to-4-bit/)）。
- NVFP4 训练：TransformerEngine 的 NVFP4 配方称在 Blackwell 上相对 FP8 基线无可测精度损失（厂商自评）（[Train Models Faster with JAX and MaxText](https://developer.nvidia.com/blog/train-models-faster-with-jax-and-maxtext-using-nvfp4-on-nvidia-blackwell)）。

## 趋势与争议

**协同设计的边界**：一派主张深度绑定（模型为特定芯片定制，如 TPU/GPU 特有算子与精度格式），另一派主张可移植性优先（通过 MLIR/TVM 等抽象层跨后端 lowering）。二者在峰值效率与工程复用力之间形成张力（[Unlocking AI Potential](https://the-ai-alliance.github.io/ai-accelerator-software-ecosystem-guide/ecosystem-guide/)、[Inside the Ironwood AI stack](https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack)）。

**PPA 感知优化缺失**：有研究指出 MLIR 等通用 IR 缺乏内建的 PPA 感知优化回路，而 AutoTVM/Ansor 局限于单算子调优，这促使出现以强化学习驱动的 ASIC 架构探索、以及把算法与加速器联合共搜索（A3C3）等新路线（[From LLM to Silicon](https://arxiv.org/html/2604.07526v1)、[A3C3](https://arxiv.org/html/2606.20869)）。

**定制加速器的软件门槛**：定制芯片往往需要专用语言/SDK（如 SambaFlow 要求专用 PyTorch 方言），且部分系统无法运行单算子基准，增加了适配与评测成本（[The xPU-athalon](https://arxiv.org/html/2604.10852v1)）。

**动态形状 vs 静态编译**：Groq、AWS Neuron 等静态编译路线在效率上有优势，但需 padding/bucketing 与固定形状，牺牲了对变长 prompt 的原生支持（[Hardware Acceleration](https://www.shyankdev.com/blogs/hardware-acceleration-tpus-vs-gpus-vs-custom-asics-inference)）。

**低精度格式的标准之争**：NVFP4（NVIDIA 主导、微块 16、E4M3 缩放）与 MXFP4（OCP 标准、块 32、E8M0 缩放、多厂商支持）代表两种路线；前者精度更高但生态绑定 NVIDIA 硬件，后者更利于跨厂商部署，二者的取舍尚无统一结论（[Pushing Intelligence to 4-bit](https://research.nvidia.com/labs/eai/blogs/pushing-intelligence-to-4-bit/)、[FP4 Just Landed in llama.cpp](https://insiderllm.com/pdfs/fp4-inference-llamacpp-nvfp4-mxfp4.pdf)）。

## 参考来源

- [From silicon to softmax: Inside the Ironwood AI stack (Google Cloud)](https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack)
- [Holistic Model Co-Design: Close the Loop With Software and Hardware for Inference Efficiency (NVIDIA GTC26)](https://www.nvidia.com/en-us/on-demand/session/gtc26-s82154/)
- [Building for the Rising Complexity of Agentic Systems with Extreme Co-Design (NVIDIA)](https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/)
- [AI Model Co-Design: Hardware-Friendly LLM Design (NVIDIA)](https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/)
- [Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform)
- [From Loop Nests to Silicon: Mapping AI Workloads onto AMD NPUs with MLIR-AIR](https://arxiv.org/html/2510.14871v1)
- [Hexagon-MLIR: An AI Compilation Stack For Qualcomm's Neural Processing Units (NPUs)](https://arxiv.org/pdf/2602.19762)
- [Accelerating ML on Hexagon: A Glimpse into Qualcomm's MLIR-based Compiler](https://llvm.org/devmtg/2025-10/slides/quick_talks/baskaran_slama.pdf)
- [From PyTorch to Calyx: An Open-Source Compiler Toolchain for ML Accelerators (C4ML 2026)](https://arxiv.org/html/2512.06177)
- [Lifting to tensors when compiling scientific computing workloads for AI Engines](https://arxiv.org/html/2605.03566v1)
- [Progressive Arithmetic Lowering from Tensor Kernels to Synthesizable Datapaths (MLIR Workshop @ Euro LLVM 2026)](https://www.llvm.org/devmtg/2026-04/slides/mlir/mlir_ledoux.pdf)
- [From LLM to Silicon: RL-Driven ASIC Architecture Exploration for On-Device AI Inference](https://arxiv.org/html/2604.07526v1)
- [A3C3: AI Algorithm and Accelerator Co-design, Co-search, and Co-generation](https://arxiv.org/html/2606.20869)
- [Unlocking AI Potential: Navigating the Challenges and Opportunities of Diverse Hardware Accelerators](https://the-ai-alliance.github.io/ai-accelerator-software-ecosystem-guide/ecosystem-guide/)
- [Hardware Acceleration: TPUs vs GPUs vs custom ASICs for Inference](https://www.shyankdev.com/blogs/hardware-acceleration-tpus-vs-gpus-vs-custom-asics-inference)
- [The xPU-athalon: Quantifying the Competition of AI Acceleration](https://arxiv.org/html/2604.10852v1)
- [SambaNova Systems](https://aiwiki.ai/wiki/sambanova)
- [Lecture 5: ML-to-Hardware Compilation Pipelines — TVM, MLIR-Based Compilers & tinygrad](https://jared-hpc.com/ai-hardware-engineer-roadmap/Phase%205%20-%20Advanced%20Topics%20and%20Specialization/6.%20AI%20Chip%20Design/Lectures/Lecture-05/)
- [Lecture 03 - Compilers and Runtimes: From Autoscheduling to Megakernels](https://jared-hpc.com/ai-hardware-engineer-roadmap/Phase%205%20-%20Advanced%20Topics%20and%20Specialization/7.%20ML%20Systems%20Engineering/MLSys%20Deep%20Dives/Lecture-03/)
- [aiconjured/embeddinggemma-300M-NVFP4-Q8-GGUF (Ollama)](https://ollama.com/aiconjured/embeddinggemma-300M-NVFP4-Q8-GGUF)
- [Pushing Intelligence to 4-bit (NVIDIA Research)](https://research.nvidia.com/labs/eai/blogs/pushing-intelligence-to-4-bit/)
- [FP4 Just Landed in llama.cpp: NVFP4 vs MXFP4 Explained (2026)](https://insiderllm.com/pdfs/fp4-inference-llamacpp-nvfp4-mxfp4.pdf)
- [Train Models Faster with JAX and MaxText Using NVFP4 on NVIDIA Blackwell](https://developer.nvidia.com/blog/train-models-faster-with-jax-and-maxtext-using-nvfp4-on-nvidia-blackwell)
- [NVIDIA Transformer Engine: NVFP4 Low Precision Training](https://docs.nvidia.com/deeplearning/transformer-engine-releases/release-2.16/user-guide/_sources/features/low_precision_training/nvfp4/nvfp4.rst.txt)
- [Interpretable AI with MLIR (IAM): A Unified Framework for Neural Network Transparency](https://dl.acm.org/doi/10.1145/3774748.3787677)