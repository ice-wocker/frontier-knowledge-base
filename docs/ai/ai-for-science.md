# AI for Science

> 最后更新：2026-09-26 ｜ 领域：AI·生成与多模态 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

AI for Science 指用机器学习方法加速自然科学发现，代表性方向包括：蛋白质与生物分子结构预测（AlphaFold 系列）、生物基础模型（ESM3）、材料发现（GNoME、MatterGen）、AI 气象预报（GraphCast、Pangu-Weather、Aurora、GenCast、AIFS）、数学定理证明（AlphaProof）与基因组调控预测（AlphaGenome）。其共同范式是把深度学习、图神经网络或扩散模型与第一性原理（如 DFT、数值天气预报）结合，并通过主动学习/实验验证闭环。典型成果包括 AlphaFold 3 的统一分子结构预测、GNoME 发现的数百万种候选晶体、已被 ECMWF 投入业务运行的多个 AI 气象模型，以及达到 IMO 金牌线的数学推理系统（[Isomorphic Labs — Our Tech](https://www.isomorphiclabs.com/our-tech)、[AI for Scientific Discovery](https://aiinovationhub.com/ai-for-scientific-discovery/)、[Farewell to the external AI models](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models)、[From silver to gold](https://www.seanbreeden.com/blog/google-deepmind-math-reinforcement-learning-alphaproof-gemini-deep-think-imo/)）。

## 最新进展（2025–2026）

- **蛋白质结构数据库扩张**：AlphaFold 3 与 AlphaFold Server 于 2024 年发布，后者为科学家提供免费的非商业研究结构预测入口；DeepMind 将 AlphaFold 列入其「生命科学与健康、地球与可持续、能源与材料、算法基础」的科学版图（[AlphaFold](https://deepmind.google/science/alphafold/)、[Science — Google DeepMind](https://deepmind.google/science/)）。数据库持续扩容：2026 年 2 月新增异构体（isoforms）与来自 AllTheBacteria、Kinetoplastids、Viro3D、Big Fantastic Virus Database 的条目；2026 年 3 月发布 1,754,199 个源自 Swiss-Prot、WHO 清单与参考蛋白质组的同源二聚体；2026 年 5 月发布约 2.2M 同源二聚体（[AlphaFold Database FAQ](https://alphafold.ebi.ac.uk/faq)）。EMBL-EBI、Google DeepMind、NVIDIA 与首尔大学合作开展了横跨 4,777 个蛋白质组的大规模复合物预测研究，涵盖约 19M 同源多聚体与约 8M 异源多聚体，包含 16 个模式生物与 30 个由 WHO 全球健康蛋白质组计划优先的蛋白质组（[AlphaFold Database](https://alphafold.ebi.ac.uk/?ref=thefragilesea.com)）。
- **生物基础模型**：EvolutionaryScale 的 ESM3 被称为首个同时对蛋白质序列、结构与功能进行推理的生成模型，训练覆盖地球自然多样性（从亚马逊雨林、深海到热液喷口等极端环境的数十亿蛋白质）；其方法学以「用语言模型模拟 5 亿年演化」为题发表于 Science（[ESM3: Simulating 500 million years of evolution with a language model](https://www.evolutionaryscale.ai/blog/esm3-release)、[Simulating 500 million years of evolution with a language model（Science）](https://www.science.org/doi/pdf/10.1126/science.ads0018)）。一篇蛋白质大语言模型综述指出，ESM-3 为 98B 参数的多模态生成模型，可用思维链方式设计蛋白质（[Protein Large Language Models: A Comprehensive Survey](https://arxiv.org/html/2502.17504v2)）。
- **蛋白与生物分子工具的智能体化**：NVIDIA 将 BioNeMo NIM 微服务封装为可被智能体调用的生物学、化学、基因组学与药物发现技能，并与 Claude Science 集成，使 AI 智能体能够编排蛋白质结构预测流程（[Run NVIDIA BioNeMo NIM Microservices for Protein Structure Prediction in Claude Science](https://developer.nvidia.com/blog/run-nvidia-bionemo-nim-microservices-for-protein-structure-prediction-in-claude-science/)）；Anthropic 报告称 Claude 在不到四周内完成了 30 余个开源生物分子结构预测、蛋白质设计、蛋白质语言建模与基因组学模型的加速（[How Claude is uplifting biomolecular modeling](https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling)）。
- **基因组学**：DeepMind 的 AlphaGenome 可预测人类 DNA 序列中单个变异或突变如何影响调控基因的生物学过程（[Science — Google DeepMind](https://deepmind.google/science/)）。
- **材料发现**：Google DeepMind 的 GNoME 利用图神经网络发现约 220 万种新晶体材料，其中约 38 万种被预测为稳定；同期另一团队证明这类预测材料可被高效合成，「AI 程序 + 机器人」正在加速新型电池、超导体与催化剂探索（[DeepMind predicts millions of new materials（Science）](https://www.science.org/doi/pdf/10.1126/science.adn2116)、[AI for Scientific Discovery](https://aiinovationhub.com/ai-for-scientific-discovery/)）。微软的 MatterGen 于 2025 年 1 月发表于 Nature，是面向无机材料设计的扩散生成模型，可在整个元素周期表范围内生成稳定、多样的材料，并可微调以定向满足化学、对称性及力学/电子/磁性等约束；其配套工具 MatterSim 用于加速仿真验证（[A generative model for inorganic materials design（Nature, 2025-01）](https://www.microsoft.com/en-us/research/publication/a-generative-model-for-inorganic-materials-design/)、[MatterGen: A new paradigm of materials design with generative AI](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)）。
- **AI 气象**：截至 2026 年初，ECMWF 每天运行的外部机器学习模型包括华为 Pangu-Weather、Google DeepMind GraphCast、微软 Aurora 与 NVIDIA FourCastNet，每天运行两次（0 与 12 UTC），由 IFS 业务分析场初始化；在 50r1 升级后 ECMWF 转向内部 AI 模型（[Farewell to the external AI models](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models)）。ECMWF 的自研 AIFS（Artificial Intelligence Forecasting System）于 2024 年转为业务运行，是首个投入业务化的主流气象机构 AI 天气模型；其集合预报系统 AIFS ENS 亦已投入业务运行（[AI Weather Forecasting in 2026 Explained](https://www.articsledge.com/post/ai-weather-forecasting)、[AIFS ENS becomes operational（ECMWF）](https://www.ecmwf.int/sites/default/files/elibrary/102025/81687-aifs-ens-becomes-operational.pdf)）。
- **数学**：AlphaProof 是 Google DeepMind 的强化学习系统，在 Lean 4 证明助手中寻找并验证形式化证明；2024 年 7 月它与 AlphaGeometry 2 组合解决 IMO 六题中的四题，得 28/42 分，达到银牌水平，整套方法于 2025 年发表于 Nature（[AlphaProof](https://aiwiki.ai/wiki/alphaproof)、[Mathematicians put AlphaProof to the test（Nature）](https://media.nature.com/original/magazine-assets/d41586-025-03585-5/d41586-025-03585-5.pdf)）。2025 年 7 月，配备 Deep Think 的 Gemini 高级版本在自然语言端到端条件下解决六题中的五题、得 35 分，达金牌线，IMO 主席 Gregor Dolinar 教授确认了这一成绩（[Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the IMO](https://deepmind.com/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)、[From silver to gold](https://www.seanbreeden.com/blog/google-deepmind-math-reinforcement-learning-alphaproof-gemini-deep-think-imo/)）。
- **地球与生态**：Google DeepMind 的 AlphaEarth Foundations 可在数分钟内分析 PB 级地图数据以检测、分割与分类地理空间变化；Perch 2 可解耦复杂音频以监测动物种群；Fusion 通过学习的等离子体控制加速聚变科学（[Science — Google DeepMind](https://deepmind.google/science/)）。
- **应用扩散**：据报道，OpenAI Foundation 宣布 6000 万美元规模的投入，用于向南亚/东南亚与东非的小农提供 AI 驱动的天气与作物病害预警；美国 NOAA 与 MIT、Penn 等高校合作使用 Aurora 等模型提前识别突发风暴与山洪等局地极端事件（[The AI and Machine Learning Forecasting Revolution](https://meteorologicalconsultant.wordpress.com/2026/09/12/the-ai-and-machine-learning-forecasting-revolution/)）。

## 核心技术与关键概念

- **图神经网络 + 主动学习 + DFT**：GNoME 的方法学组合是材料发现加速的模板（[AI for Science — Landscape & Method Spectrum](https://jimmyresearch.com/modules/ai-for-science/)）。
- **扩散模型做结构预测**：AlphaFold 3 用扩散在原始原子坐标上生成结构，被视为「大规模生成模型」路线相对等变架构路线的胜利（[AI for Science — Landscape & Method Spectrum](https://jimmyresearch.com/modules/ai-for-science/)）。
- **生成式材料设计 vs 候选筛选**：传统计算材料学依赖对已知/枚举候选做筛选，而 MatterGen 以设计需求为提示直接生成新材料，微软将其定位为「创意生成器」，MatterSim 承担验证，二者构成 inverse design 的新范式（[MatterGen](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)、[AI meets materials discovery: The vision behind MatterGen and MatterSim](https://www.microsoft.com/en-us/research/story/ai-meets-materials-discovery/)）。
- **多模态生物语言模型**：ESM3 将序列、结构、功能统一为一个生成空间，可用组合模态的提示（prompt）引导生成，这与纯结构模型的能力面不同（[ESM3](https://www.evolutionaryscale.ai/blog/esm3-release)）。
- **数据驱动天气预报**：以历史再分析数据训练的模型可媲美最先进的数值天气预报（NWP），但存在次季节尺度的失效模式——大尺度环流在 14–21 天仍有中等技巧，而基于阈值的极端强度预测会随回归气候态而崩塌（[Evaluating the Predictability of Selected Weather Extremes with Aurora](https://arxiv.org/pdf/2603.06516v1)）。Pangu-Weather 由华为诺亚方舟实验室于 2023 年 7 月发表于 Nature；GraphCast 在 1,380 个验证目标中的 90.3% 上比 ECMWF 高分辨率确定性模式 HRES 更准确，且可在单块 Cloud TPU v4 上运行（[AI Weather Forecasting in 2026 Explained](https://www.articsledge.com/post/ai-weather-forecasting)、[GraphCast（AI Wiki）](https://aiwiki.ai/wiki/graphcast/raw)）。
- **形式化与自然语言两条路线**：AlphaProof 走 Lean 4 形式化路线，需先把题目翻译为形式语言；2025 年 Gemini Deep Think 则直接用自然语言在竞赛时长内完成证明（[AlphaProof](https://aiwiki.ai/wiki/alphaproof)、[From silver to gold](https://www.seanbreeden.com/blog/google-deepmind-math-reinforcement-learning-alphaproof-gemini-deep-think-imo/)）。
- **概率化与集合预报**：GraphCast 以确定性点预报闻名，GenCast 则作为其概率化（集合）后继，用于表达预报不确定性（[AI for Science](https://aiwiki.ai/wiki/ai_for_science)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- Google DeepMind / Isomorphic Labs：AlphaFold 3、AlphaGenome、GNoME、AlphaEarth Foundations、Perch 2、Fusion（等离子体控制）（[Science](https://deepmind.google/science/)、[Isomorphic Labs](https://www.isomorphiclabs.com/our-tech)）。
- Microsoft Research：MatterGen（材料生成）、MatterSim（材料仿真）、Aurora 气象模型（[Materials](https://www.microsoft.com/en-us/research/project/materials/)、[Farewell to the external AI models](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models)）。
- EvolutionaryScale：ESM3 蛋白语言/生成模型（[ESM3](https://www.evolutionaryscale.ai/blog/esm3-release)）。
- NVIDIA：BioNeMo NIM 微服务，封装为可被智能体调用的生物医药技能（[NVIDIA BioNeMo NIM](https://developer.nvidia.com/blog/run-nvidia-bionemo-nim-microservices-for-protein-structure-prediction-in-claude-science/)）。
- 华为云：Pangu-Weather；ECMWF：AIFS / AIFS ENS 内部 AI 预报（[AI Weather Forecasting in 2026](https://www.articsledge.com/post/ai-weather-forecasting)、[AIFS ENS becomes operational](https://www.ecmwf.int/sites/default/files/elibrary/102025/81687-aifs-ens-becomes-operational.pdf)）。

## 关键数据与评测结果（附来源）

- GNoME：约 220 万种新晶体，约 38 万种预测稳定；相较之下，人类实验与早期计算方法此前仅识别数万种（[AI for Scientific Discovery](https://aiinovationhub.com/ai-for-scientific-discovery/)）。
- AlphaFold Database：2026 年 3 月 1,754,199 个同源二聚体、2026 年 5 月约 2.2M 同源二聚体；跨 4,777 个蛋白质组完成约 19M 同源多聚体与约 8M 异源多聚体预测（[AlphaFold Database FAQ](https://alphafold.ebi.ac.uk/faq)、[AlphaFold Database](https://alphafold.ebi.ac.uk/?ref=thefragilesea.com)）。
- GraphCast：10 天全球预报在单块 TPU 上不到一分钟完成，并在 90.3% 的验证目标上优于 HRES（[GraphCast（AI Wiki）](https://aiwiki.ai/wiki/graphcast/raw)）。
- ESM3：98B 参数多模态生成模型，可用思维链设计蛋白质（[Protein LLMs Survey](https://arxiv.org/html/2502.17504v2)）。
- AlphaProof（2024，IMO）：28/42 分，银牌水平；2025 Gemini Deep Think：35 分（六题中解决五题），金牌线（[AlphaProof](https://aiwiki.ai/wiki/alphaproof)、[Advanced version of Gemini with Deep Think（Google DeepMind）](https://deepmind.com/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)）。
- Isomorphic Labs：6 亿美元融资、17 条管线、与礼来/诺华近 30 亿美元合作（[IsoDDE](https://m.baike.com/wiki/IsoDDE/7608874365359308851)）。

## 趋势与争议

- **从预测到临床**：AI 制药的关键考验在于管线能否真正进入并通过临床试验，首个 AI 设计药物的试验时间表已被推迟一次（[Isomorphic Labs & AlphaFold](https://intuitionlabs.ai/articles/isomorphic-labs-alphafold-ai-drug-discovery-trials)）。
- **AI 气象的边界**：数据驱动模型在极端天气强度的次季节预测上会失效，说明其并非全面替代 NWP；有基准研究进一步比较 AI 模型两周以上的长时段滚动预报能力（[Evaluating the Predictability of Selected Weather Extremes with Aurora](https://arxiv.org/pdf/2603.06516v1)、[Can AI Weather Models Predict Beyond Two Weeks?](https://arxiv.org/html/2605.30184)）。
- **架构与范式之争**：等变网络 vs 大规模数据驱动生成模型（如 AlphaFold 3 的扩散路线）仍是方法学争议焦点；材料领域则出现「生成式 inverse design」与「计算筛选」两条技术路线的对比（[AI for Science — Landscape & Method Spectrum](https://jimmyresearch.com/modules/ai-for-science/)、[MatterGen](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)）。
- **口径差异**：关于 2025 年 IMO 成绩，Google DeepMind 官方表述为「六题中解决五题、得 35 分」达金牌线，另有第三方文章称「解决全部六题」，两口径并存需注意（[Google DeepMind](https://deepmind.com/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)、[When AI Earned a Silver Medal in Mathematics](https://international-maths-challenge.com/when-ai-earned-a-silver-medal-in-mathematics/)）。
- **科研基础设施化**：从 GNoME 的晶体库、AlphaFold 的结构数据库到 ECMWF 的业务化 AI 预报，AI for Science 正从论文走向可持续的科研基础设施（[Science — Google DeepMind](https://deepmind.google/science/)、[Farewell to the external AI models](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models)）。

## 参考来源

- [Science — Google DeepMind](https://deepmind.google/science/)
- [AlphaFold — Google DeepMind](https://deepmind.google/science/alphafold/)
- [AlphaFold Database FAQ](https://alphafold.ebi.ac.uk/faq)
- [AlphaFold Database](https://alphafold.ebi.ac.uk/?ref=thefragilesea.com)
- [Isomorphic Labs — Our Tech](https://www.isomorphiclabs.com/our-tech)
- [AI for Science — Landscape & Method Spectrum](https://jimmyresearch.com/modules/ai-for-science/)
- [AI for Scientific Discovery](https://aiinovationhub.com/ai-for-scientific-discovery/)
- [DeepMind predicts millions of new materials（Science）](https://www.science.org/doi/pdf/10.1126/science.adn2116)
- [A generative model for inorganic materials design（Nature, 2025-01）](https://www.microsoft.com/en-us/research/publication/a-generative-model-for-inorganic-materials-design/)
- [MatterGen: A new paradigm of materials design with generative AI](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)
- [Materials（Microsoft Research）](https://www.microsoft.com/en-us/research/project/materials/)
- [AI meets materials discovery: The vision behind MatterGen and MatterSim](https://www.microsoft.com/en-us/research/story/ai-meets-materials-discovery/)
- [ESM3: Simulating 500 million years of evolution with a language model](https://www.evolutionaryscale.ai/blog/esm3-release)
- [Simulating 500 million years of evolution with a language model（Science）](https://www.science.org/doi/pdf/10.1126/science.ads0018)
- [Protein Large Language Models: A Comprehensive Survey](https://arxiv.org/html/2502.17504v2)
- [Run NVIDIA BioNeMo NIM Microservices for Protein Structure Prediction in Claude Science](https://developer.nvidia.com/blog/run-nvidia-bionemo-nim-microservices-for-protein-structure-prediction-in-claude-science/)
- [How Claude is uplifting biomolecular modeling（Anthropic）](https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling)
- [Farewell to the external AI models（ECMWF）](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models)
- [AIFS ENS becomes operational（ECMWF）](https://www.ecmwf.int/sites/default/files/elibrary/102025/81687-aifs-ens-becomes-operational.pdf)
- [AI Weather Forecasting in 2026 Explained](https://www.articsledge.com/post/ai-weather-forecasting)
- [GraphCast（AI Wiki）](https://aiwiki.ai/wiki/graphcast/raw)
- [Evaluating the Predictability of Selected Weather Extremes with Aurora](https://arxiv.org/pdf/2603.06516v1)
- [Can AI Weather Models Predict Beyond Two Weeks?](https://arxiv.org/html/2605.30184)
- [The AI and Machine Learning Forecasting Revolution](https://meteorologicalconsultant.wordpress.com/2026/09/12/the-ai-and-machine-learning-forecasting-revolution/)
- [AlphaProof（wiki）](https://aiwiki.ai/wiki/alphaproof)
- [Mathematicians put AlphaProof to the test（Nature）](https://media.nature.com/original/magazine-assets/d41586-025-03585-5/d41586-025-03585-5.pdf)
- [Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the IMO（Google DeepMind）](https://deepmind.com/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)
- [From silver to gold](https://www.seanbreeden.com/blog/google-deepmind-math-reinforcement-learning-alphaproof-gemini-deep-think-imo/)
- [When AI Earned a Silver Medal in Mathematics](https://international-maths-challenge.com/when-ai-earned-a-silver-medal-in-mathematics/)
- [AI for Science（wiki）](https://aiwiki.ai/wiki/ai_for_science)
- [IsoDDE](https://m.baike.com/wiki/IsoDDE/7608874365359308851)
- [Google DeepMind CEO Announces AI-Designed Cancer Drug Clinical Trials](https://creati.ai/ai-news/2026-02-14/deepmind-ai-cancer-drug-clinical-trials-2026-demis-hassabis/)
- [Isomorphic Labs & AlphaFold: AI Drug Discovery in Trials](https://intuitionlabs.ai/articles/isomorphic-labs-alphafold-ai-drug-discovery-trials)