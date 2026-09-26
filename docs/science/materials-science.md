# 材料科学

> 最后更新：2026-09-26 ｜ 领域：科学·数理与材料 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

材料科学前沿在 2025–2026 年呈现出「AI 驱动发现 + 自动化实验」与「经典体系持续突破」双线并进的特征：以 Google DeepMind 的 GNoME 为代表的深度学习预测大幅扩张了已知稳定材料的空间，自主实验室（self-driving lab）把发现-验证周期压缩到天级；与此同时，二维材料、金属有机框架（MOF）、超导与量子材料等经典方向仍在产出重要成果，MOF 更因此获得 2025 年诺贝尔化学奖。超导材料方面，常压超导温度纪录被刷新，超薄超导薄膜的可规模化制备也取得进展。

## 最新进展（2025–2026）

### AI 驱动的材料发现

- **GNoME 的持续影响**：2023 年底，Google DeepMind 发布 GNoME（Graph Networks for Materials Exploration），用深度学习预测了 220 万种新晶体结构，其中约 38 万种足够稳定，可作为电池、芯片与太阳能电池等的候选材料，相当于把人类已知技术可行材料的数量扩大近一个数量级。（[Millions of new materials discovered with deep learning — Google DeepMind](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/?ref=aigood.news)）（[GNoME AI Materials Discovery](https://aiinovationhub.com/gnome-ai-materials-discovery/)）
- **从预测走向实验验证**：有报道称，GNoME 预测中已有部分晶体被实验验证；自主实验室可将实验周期从数月乃至数年缩短到数天，并已出现用于锂电池的新电解液等成果。（[Descubrimiento de Materiales: La Revolución de la IA](https://blog.donweb.com/descubrimiento-materiales-ia-nuevas-direcciones-2026/)）
- **LLM 提取材料知识**：有工作用 Llama-3.3-70B（LoRA 微调）从 61,766 篇材料科学论文中提取因果机制，构建了含 207,200 条因果机制描述、由 1,113,940 条多模态证据（图、表、公式、正文）支撑的数据集。（[2.2 Million New Materials Discovered by AI: Three Revolutions in Materials Science](https://ordoresearch.ai/blog/ai-materials-discovery-gnome-revolution)）
- **对 GNoME 的反思**：也有分析指出，GNoME 更接近「近十倍扩张已知稳定无机材料」的框架叙事，其成果能否转化为实际器件仍需长期验证。（[AI Materials Discovery After GNoME](https://pdpspectra.com/blog/ai-materials-discovery-gnome-2026/)）

### 二维材料与石墨烯

- **方形莫尔图案首次在石墨烯中实现**：研究团队结合层间扭转与受控机械应变（被称为 twistraintronics），首次在堆叠石墨烯中生成方形莫尔图案，成果发表于 Physical Review Letters，为设计新型量子材料提供路径。（[They create square moiré patterns in graphene for the first time — UAM](https://www.uam.es/uam/en/investigacion/cultura-cientifica/noticias/fisica-grafeno)）
- **近邻屏蔽提升石墨烯器件质量**：在 2026 深圳国际石墨烯论坛上，诺贝尔奖得主 Andre Geim 报告其团队开发的「近邻屏蔽」技术——在石墨烯附近放置间距约 1 纳米的石墨栅极，将石墨烯器件电子质量提升 10–100 倍，并首次观测到因质量跃升而涌现的丰富分数量子霍尔态（FQHE）。（[2026深圳国际石墨烯论坛暨二维材料国际研讨会闭幕 — 清华大学深圳国际研究生院](https://www.sigs.tsinghua.edu.cn/2026/0415/c7917a290174/page.htm)）

### MOF 与杂化材料

- 2025 年诺贝尔化学奖授予 Susumu Kitagawa、Richard Robson 与 Omar M. Yaghi，表彰他们「金属有机框架的开发」。（[Press release — NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/press-release/)）
- MOF 与二维材料的杂化架构（MOF-2D hybrid）被视为能源转换与存储的重要方向，可构筑多功能杂化材料。（[Low-Dimensional MOF Nanoarchitectonics — Advanced Materials](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202521053)）连续流工艺也被用于制备 MOF/纳米碳复合材料，提升产率与规模化可行性。（[Continuous flow synthesis of MOF/nanocarbon composites — RSC Nanoscale](https://pubs.rsc.org/en/content/articlehtml/2026/nr/d6nr00739b)）

### 超导与量子材料

- **空气稳定的超薄超导薄膜**：MIT 研究者开发出可在晶圆尺度制备、空气稳定的超薄超导材料技术，克服了此类材料用于量子器件的主要障碍。（[Researchers make air-stable, ultrathin superconductors, for more scalable quantum devices — MIT News](https://news.mit.edu/2026/researchers-make-air-stable-ultrathin-superconductors-more-scalable-quantum-devices)）
- **常压超导温度纪录**：见「物理学前沿」条目的 151 K 常压超导纪录与常压镍基超导材料进展。

## 核心技术与关键概念

- **图神经网络材料预测**：GNoME 使用图网络预测晶体结构的稳定性，从已知结构中学习、再扩展到未探索的组成空间。
- **自主实验室（self-driving lab）**：由 AI 规划实验、机器人执行、数据回流形成闭环，缩短设计-合成-表征周期。
- **莫尔超晶格与扭转电子学（twistronics）**：通过层间扭转角调控二维材料电子态；twistraintronics 进一步叠加机械应变。
- **近邻屏蔽（proximity screening）**：用近距金属栅极屏蔽长程杂质势，显著提升二维材料器件质量。
- **MOF（金属有机框架）**：由金属节点与有机配体自组装成的多孔晶体材料，具有极高比表面积与可设计性。
- **材料基因组计划（Materials Genome Initiative）**：以计算、数据与实验协同加速材料发现的国家级框架（概念背景）。

## 代表性项目 / 机构 / 产品

- **GNoME**（Google DeepMind）。（[Google DeepMind](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/?ref=aigood.news)）
- **MOF 奠基工作**（Kitagawa / Robson / Yaghi）：2025 年诺贝尔化学奖。（[NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/press-release/)）
- **石墨烯与二维材料**（Andre Geim 团队等）。（[清华 SIGS](https://www.sigs.tsinghua.edu.cn/2026/0415/c7917a290174/page.htm)）
- **MIT 超薄超导薄膜技术**。（[MIT News](https://news.mit.edu/2026/researchers-make-air-stable-ultrathin-superconductors-more-scalable-quantum-devices)）

## 关键数据与评测结果（附来源）

| 事项 | 数据 | 来源 |
| --- | --- | --- |
| GNoME 预测晶体 | 220 万种，约 38 万种稳定 | [DeepMind](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/?ref=aigood.news) |
| AI 知识提取规模 | 61,766 篇论文 → 207,200 条因果机制 | [ordo research](https://ordoresearch.ai/blog/ai-materials-discovery-gnome-revolution) |
| 石墨烯近邻屏蔽效果 | 电子质量提升 10–100 倍 | [清华 SIGS](https://www.sigs.tsinghua.edu.cn/2026/0415/c7917a290174/page.htm) |
| MOF 连续流产率 | 约 3.5 g h⁻¹（UiO-66-NH₂/CGA） | [RSC Nanoscale](https://pubs.rsc.org/en/content/articlehtml/2026/nr/d6nr00739b) |

## 趋势与争议

1. **「预测数量」与「实用材料」的落差**：AI 大规模预测结构令人振奋，但稳定候选能否合成、加工并进入器件，仍需实验闭环验证。
2. **自主实验室的可扩展性与可复现性**：闭环自动化提高了速度，但数据质量、实验噪声与跨实验室复现仍是瓶颈。
3. **二维材料的规模化**：莫尔工程与高质量器件多在实验室尺度实现，晶圆级、空气稳定的制备是走向应用的关键。
4. **超导纪录的可持续验证**：常压高 Tc 与室温超导类工作历史上争议频发，独立复现与机制解释仍是关键。

## 参考来源

- [Millions of new materials discovered with deep learning — Google DeepMind](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/?ref=aigood.news)
- [GNoME AI Materials Discovery — aiinovationhub](https://aiinovationhub.com/gnome-ai-materials-discovery/)
- [Descubrimiento de Materiales: La Revolución de la IA](https://blog.donweb.com/descubrimiento-materiales-ia-nuevas-direcciones-2026/)
- [2.2 Million New Materials Discovered by AI — ordoresearch](https://ordoresearch.ai/blog/ai-materials-discovery-gnome-revolution)
- [AI Materials Discovery After GNoME — pdpspectra](https://pdpspectra.com/blog/ai-materials-discovery-gnome-2026/)
- [They create square moiré patterns in graphene for the first time — UAM](https://www.uam.es/uam/en/investigacion/cultura-cientifica/noticias/fisica-grafeno)
- [2026深圳国际石墨烯论坛暨二维材料国际研讨会闭幕 — 清华大学深圳国际研究生院](https://www.sigs.tsinghua.edu.cn/2026/0415/c7917a290174/page.htm)
- [Press release: Nobel Prize in Chemistry 2025 — NobelPrize.org](https://www.nobelprize.org/prizes/chemistry/2025/press-release/)
- [Low-Dimensional MOF Nanoarchitectonics — Advanced Materials](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202521053)
- [Continuous flow synthesis of MOF/nanocarbon composites — RSC Nanoscale](https://pubs.rsc.org/en/content/articlehtml/2026/nr/d6nr00739b)
- [Researchers make air-stable, ultrathin superconductors — MIT News](https://news.mit.edu/2026/researchers-make-air-stable-ultrathin-superconductors-more-scalable-quantum-devices)