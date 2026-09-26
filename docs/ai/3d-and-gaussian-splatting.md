# 3D 与高斯泼溅

> 最后更新：2026-09-26 ｜ 领域：AI·生成与多模态 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

三维内容生成的主流技术可归为两类：一是**重建/渲染**（Neural Radiance Fields，NeRF；3D Gaussian Splatting，3DGS），从多视角图像恢复可渲染的场景表示；二是**生成式 3D**（image/text-to-3D），直接产出可直接使用的 3D 资产（mesh + PBR 贴图）。2025–2026 年的趋势是两者融合：前馈式（feed-forward）高斯重建把重建速度从「每场景优化」提升到「单次前向」，而 3D 生成模型则追求「秒级、可商用、游戏可用」的资产输出；同时 4D（动态）高斯与数字人成为热点。代表性进展包括：从文本或多视角图像生成带 PBR 贴图的 3D 资产（Hunyuan3D、Rodin、Tripo3D 等），以及从单张人像生成可动画 4D 高斯头像（GeoDiff4D、AniGS、AvatarPointillist 等）（[AI 3D Generator](https://lovegen.ai/da/ai-3d-generator)、[Hunyuan3D](https://hunyuan3d.dev/)、[GeoDiff4D](https://en.papernotes.org/CVPR2026/3d_vision/geodiff4d_geometry-aware_diffusion_for_4d_head_avatar_reconstruction/)、[AniGS](https://arxiv.org/html/2412.02684)、[AvatarPointillist](https://arxiv.org/html/2604.04787v1)）。

## 最新进展（2025–2026）

- **3DGS 持续演进**：CVPR 2026 出现面向任意分辨率渲染的工作，采用紧凑代理锚点（compact proxy anchors）表示场景，参数化各向异性 3D 高斯并经由可微分的 tile-based 光栅化优化，初始化通常来自 Structure-from-Motion（SfM）点云（[3D Gaussian Splatting for Arbitrary Resolutions with Compact Proxy Anchors](https://openaccess.thecvf.com/content/CVPR2026/papers/Jeong_3D_Gaussian_Splatting_at_Arbitrary_Resolutions_with_Compact_Proxy_Anchors_CVPR_2026_paper.pdf)）。AnchorSplat 等工作提出前馈式 3DGS，用 3D 几何先验（如稀疏点云）进行锚点对齐，摆脱逐像素与输入图像的强耦合（[AnchorSplat](https://arxiv.org/html/2604.07053v1)）。TR-Gaussians 结合可学习反射平面建模室内玻璃的透射与反射（[TR-Gaussians](https://www.computer.org/csdl/journal/tg/5555/01/11442723/2eXekqhJba0)）。
- **NeRF 与 3DGS 互补**：有研究指出两者性能互补——3DGS 渲染更快、NeRF 质量更高，于是提出用预训练 NeRF 渲染图像来增强 3DGS，如在街景场景中（[Leveraging NeRF-Rendered Images for 3D Gaussian Splatting](https://arxiv.org/html/2606.09034v1)）。
- **3D 生成模型**：腾讯 Hunyuan3D 以 Apache 2.0 开源权重发布，v2.5 约 10B 参数，最低可在 6GB 显存运行，支持图像或文本输入并输出带 PBR 贴图的 3D 模型（[Hunyuan3D](https://hunyuan3d.dev/)）。对比资料列出 Hunyuan 3D V3.1、Tripo3D H3.1、Hyper3D Rodin v2.5 等主流模型，输入支持图像、多视角与文本，输出 GLB/OBJ 等格式（[AI 3D Generator](https://lovegen.ai/da/ai-3d-generator)）。Hyper3D Rodin Gen-2.5 提供五档质量层级、最高约 200 万多边形与 HD PBR 贴图（[Rodin Gen-2.5](https://rodinai.net/)）。
- **4D 与数字人**：AvatarPointillist 提出从单张人像自回归生成动态 4D 高斯头像，用 decoder-only Transformer 逐点生成并自适应调整点密度，同时联合预测每点的绑定信息（[AvatarPointillist](https://arxiv.org/html/2604.04787v1)）。GeoDiff4D 用几何感知扩散联合生成人像帧与表面法线，再蒸馏进可动画的 4D 头像（[GeoDiff4D](https://en.papernotes.org/CVPR2026/3d_vision/geodiff4d_geometry-aware_diffusion_for_4d_head_avatar_reconstruction/)）。AniGS 从单张图像生成可动画高斯头像（[AniGS](https://arxiv.org/html/2412.02684)）。
- **重建走向实时与可部署**：前馈式方法把场景级重建从「逐场景优化」变为「单次前向」，配合紧凑代理锚点等表示支持任意分辨率渲染，反映 3DGS 研究对实时性与部署效率的追求（[AnchorSplat](https://arxiv.org/html/2604.07053v1)、[3D Gaussian Splatting for Arbitrary Resolutions](https://openaccess.thecvf.com/content/CVPR2026/papers/Jeong_3D_Gaussian_Splatting_at_Arbitrary_Resolutions_with_Compact_Proxy_Anchors_CVPR_2026_paper.pdf)）。

## 核心技术与关键概念

- **3DGS 表示**：将场景表示为带均值、尺度、旋转、不透明度与颜色的可微各向异性 3D 高斯，通过可微分 tile-based 光栅化优化（[3D Gaussian Splatting for Arbitrary Resolutions](https://openaccess.thecvf.com/content/CVPR2026/papers/Jeong_3D_Gaussian_Splatting_at_Arbitrary_Resolutions_with_Compact_Proxy_Anchors_CVPR_2026_paper.pdf)）。
- **NeRF**：以神经辐射场隐式表示场景，渲染质量高但速度慢，与 3DGS 形成互补（[Leveraging NeRF-Rendered Images for 3D Gaussian Splatting](https://arxiv.org/html/2606.09034v1)）。
- **前馈式重建**：从「逐场景优化」转为「一次前向推理」，是 3D 重建工程化的关键。传统前馈模型多采用像素对齐（pixel-aligned）表述，把每个 2D 像素映射到一个 3D 高斯，使高斯表示与输入图像强耦合；AnchorSplat 则直接在 3D 空间中以锚点对齐表示场景，并引入稀疏点云等 3D 几何先验（[AnchorSplat](https://arxiv.org/html/2604.07053v1)）。
- **材质与反射建模**：TR-Gaussians 将 3D 高斯与可学习的反射平面结合，显式建模室内场景中常见的玻璃平面透射与反射，其中反射分量由镜像高斯表示（[TR-Gaussians](https://www.computer.org/csdl/journal/tg/5555/01/11442723/2eXekqhJba0)）。
- **网格绑定与形变**：动捕/动画头像常把高斯挂载到参数化人体或头部模型（如 SMPL、FLAME）的三角面上，并用 LBS 或形变场网络驱动。AniGS 采用多分辨率 HexPlane 与紧凑 MLP 组成的时空编码器，在六张 2D 体素平面上编码 3D 高斯的时间与空间特征（[Dynamic Avatar-Scene Rendering](https://arxiv.org/html/2511.10539)、[AniGS](https://arxiv.org/html/2412.02684)、[GeoDiff4D](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_GeoDiff4D_Geometry-Aware_Diffusion_for_4D_Head_Avatar_Reconstruction_CVPR_2026_paper.pdf)）。
- **资产管线**：生成结果普遍以 GLB/OBJ/STL 等形式导出，并携带 PBR 材质，以对接游戏引擎与设计工具。常见可控参数包括生成类型、面数（Face Count）、PBR 材质、条件模式、质量层级以及 T/A Pose 等；Rodin 支持文本、单张或最多四张图像输入，输出 GLB/OBJ/STL（[AI 3D Model Generators Compared: 5 Options for 2026](https://learn.rundiffusion.com/ai-3d-model-generators/)）。
- **2D→3D 与可导航世界**：除单物体资产生成外，3D/4D 生成也被用于构建可导航场景。Marble 等世界模型把单张 2D 图像转为可持久导航的 3D 环境，并可渲染为高斯泼溅或导出为 mesh，直接进入游戏、VFX 与设计管线（[Best World Models in 2026](https://ltx.io/blog/best-world-models)）。
- **动态场景渲染**：4D 工作把参数化人体先验（如 SMPL）与隐式或显式神经渲染结合，用 LBS 驱动的可变形 3D 高斯表示人体头像，从而支持新姿态动画（[Dynamic Avatar-Scene Rendering from Human-centric Context](https://arxiv.org/html/2511.10539)）。
- **几何/人体先验的注入**：无论是 AnchorSplat 使用稀疏点云先验，还是 4D 头像使用 SMPL/FLAME 网格绑定，把几何与人体先验注入生成与重建流程，是被多项工作反复验证的有效手段（[AnchorSplat](https://arxiv.org/html/2604.07053v1)、[Dynamic Avatar-Scene Rendering](https://arxiv.org/html/2511.10539)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- 腾讯：Hunyuan3D（Apache 2.0 开源）（[Hunyuan3D](https://hunyuan3d.dev/)）。
- Tripo3D：Tripo3D H3.1，主打多角度忠实重建（[AI 3D Generator](https://lovegen.ai/da/ai-3d-generator)）。
- Hyper3D：Rodin Gen-2.5，支持质量分层与 T/A Pose、HighPack 附加项，输出 GLB/OBJ/STL（[Rodin Gen-2.5](https://rodinai.net/)、[AI 3D Model Generators Compared](https://learn.rundiffusion.com/ai-3d-model-generators/)）。
- 学术侧：3DGS、AnchorSplat、TR-Gaussians、AvatarPointillist、GeoDiff4D、AniGS 等（见参考来源）。

## 关键数据与评测结果（附来源）

- Hunyuan3D：Apache 2.0 许可、约 6GB 显存可运行、v2.5 约 10B 参数，可在数秒内返回带 PBR 贴图的 3D 模型（[Hunyuan3D](https://hunyuan3d.dev/)）。
- Hyper3D Rodin Gen-2.5：五档质量层级、最高约 200 万多边形、HD PBR 贴图，支持最多 5 张图像或文本输入（[Rodin Gen-2.5](https://rodinai.net/)、[AI 3D Generator](https://lovegen.ai/da/ai-3d-generator)）。
- 4D 头像：GeoDiff4D 报告在身份保持、表情恢复与跨视角一致性上显著优于既有方法（[GeoDiff4D](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_GeoDiff4D_Geometry-Aware_Diffusion_for_4D_Head_Avatar_Reconstruction_CVPR_2026_paper.pdf)）。

## 趋势与争议

- **质量与效率权衡**：3DGS 快、NeRF 精，如何在统一管线中兼顾仍是活跃研究问题（[Leveraging NeRF-Rendered Images for 3D Gaussian Splatting](https://arxiv.org/html/2606.09034v1)）。
- **生成资产的可用性**：从「能看」到「可用」（拓扑、UV、PBR、可绑定）仍有差距，商业模型以质量分层、面数上限与导出格式来弥合（[AI 3D Model Generators Compared](https://learn.rundiffusion.com/ai-3d-model-generators/)）。
- **许可问题**：部分高保真 3D 生成能力仍以闭源 API 为主，开源权重多受特定许可约束（[Hunyuan3D](https://hunyuan3d.dev/)）。
- **数字人伦理与一致性**：单图生成可动画头像在身份保持与跨视角一致性提升的同时，也带来肖像权与深度伪造相关争议（[GeoDiff4D](https://en.papernotes.org/CVPR2026/3d_vision/geodiff4d_geometry-aware_diffusion_for_4d_head_avatar_reconstruction/)）。

## 参考来源

- [3D Gaussian Splatting for Arbitrary Resolutions with Compact Proxy Anchors (CVPR 2026)](https://openaccess.thecvf.com/content/CVPR2026/papers/Jeong_3D_Gaussian_Splatting_at_Arbitrary_Resolutions_with_Compact_Proxy_Anchors_CVPR_2026_paper.pdf)
- [Leveraging NeRF-Rendered Images for 3D Gaussian Splatting](https://arxiv.org/html/2606.09034v1)
- [AnchorSplat: Feed-Forward 3D Gaussian Splatting With 3D Geometric Priors](https://arxiv.org/html/2604.07053v1)
- [TR-Gaussians](https://www.computer.org/csdl/journal/tg/5555/01/11442723/2eXekqhJba0)
- [Hunyuan3D](https://hunyuan3d.dev/)
- [AI 3D Generator](https://lovegen.ai/da/ai-3d-generator)
- [Rodin Gen-2.5](https://rodinai.net/)
- [AI 3D Model Generators Compared: 5 Options for 2026](https://learn.rundiffusion.com/ai-3d-model-generators/)
- [Best World Models in 2026 (Open & Closed)](https://ltx.io/blog/best-world-models)
- [AvatarPointillist: AutoRegressive 4D Gaussian Avatarization](https://arxiv.org/html/2604.04787v1)
- [GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://en.papernotes.org/CVPR2026/3d_vision/geodiff4d_geometry-aware_diffusion_for_4d_head_avatar_reconstruction/)
- [GeoDiff4D (CVPR 2026 paper)](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_GeoDiff4D_Geometry-Aware_Diffusion_for_4D_Head_Avatar_Reconstruction_CVPR_2026_paper.pdf)
- [Dynamic Avatar-Scene Rendering from Human-centric Context](https://arxiv.org/html/2511.10539)
- [AniGS: Animatable Gaussian Avatar from a Single Image](https://arxiv.org/html/2412.02684)