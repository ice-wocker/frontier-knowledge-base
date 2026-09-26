# 机器人硬件与执行器

> 最后更新：2026-09-26 ｜ 领域：硬件 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

机器人硬件是指支撑机器人运动与感知的物理部件体系，核心包括执行器（actuator，含电机、减速器、编码器）、灵巧手、力觉与触觉传感器、IMU、结构件与电池等。随人形机器人（humanoid）在 2025–2026 年加速走向小批量量产，其硬件成本拆解、关键零部件（尤其是谐波减速器、六维力传感器、灵巧手）的供应链与国产化成为产业焦点。

## 最新进展（2025–2026）

- **量产与场景落地提速**：2026 年 8 月，第二届世界人形机器人运动会在北京国家速滑馆举办，来自六大洲 16 个国家的 666 支队伍参赛，成为具身智能落地的重要展示窗口（[坤维科技将为第二届世界人形机器人运动会提供独家力控技术支持](http://cn.chinadaily.com.cn/a/202608/25/WS6a8d4498e4b09dff9814f032.html)）。
- **触觉传感器突破**：2026 世界机器人大会（WRC，8 月 19 日于北京亦庄开幕）上，武汉华威科发布"万象系列"旗舰级触觉传感器，宣称具备 1%FS 高精度、0.01N 超低触发力与 1%FS/h 超低时漂（[华威科万象系列 WRC 首发](http://caijing.chinadaily.com.cn/a/202608/21/WS6a87c25ca3105d3d7a27c28f.html)）。同期千觉机器人展示"整手触觉"方案，结合三色光视触觉指尖传感器与掌心大面积柔性电子皮肤，将感知从指尖拓展至全手（[亮相 2026 世界机器人大会，千觉机器人让整只灵巧手拥有"高质量触觉"](http://www.shobserver.com/wx/detail.do?id=1163975)）。
- **电子皮肤柔性化**：有研究团队将复杂电路系统"织入"纤维，制成又细又柔的机器人电子皮肤，并实现手指对机械臂与无人机的非接触式空间遥控（[编织机器人电子皮肤成为可能](https://www.shobserver.cn/wx/detail.do?id=1184701)）。
- **供应链成本压力**：谐波减速器与执行器仍是降本关键，中国厂商通过打入国产供应链与规模化生产挤压成本（见下节）。

## 核心技术与关键概念

### 1. 执行器与减速器

执行器是机器人关节的核心，通常由伺服电机、减速器、编码器与驱动器构成。人形机器人一般在几乎所有旋转关节（肩、肘、腕、髋、膝、踝）都需配置谐波减速器，按保守估计单台需 20–30 个关节，减速器因此成为 BOM 上的主导项（[What a Humanoid Robot Costs to Build](https://www.laifualdrive.com/blog/humanoid-robot-cost-harmonic-reducer/)）。谐波减速器核心的柔轮（flexspline）为薄壁高精度件，制造精度要求高，是成本与技术壁垒所在。

### 2. 力觉与触觉传感

- **六维力传感器**：用于测量三个方向的力与三个方向的力矩，是力控（force control）的关键。2025 年中国人形机器人六维力传感器总用量约 1.32 万颗，首次突破万颗，市场规模约 3.3 亿元，国产厂商占据主导（[《2026 年中国人形机器人六维力传感器市场调研报告》发布](https://app.myzaker.com/news/article.php?pk=6a9501ecb15ec023311b1028)）。
- **触觉阵列与电子皮肤**：用于抓取对位、拨动、滚动接触与精细操作。团体标准对高等级（L3 及以上）灵巧手要求配备分布式触觉阵列、采样率不小于 100 Hz，法向压力量程不低于 20 N，可感知力不大于 0.5 N（[具身智能机器人灵巧手操作与驱控技术要求 T/CAMETA 001xxx—2026](https://www.cameta.org.cn/uploadfile/2026/0710/20260710042237363.pdf)）。
- **IMU 与关节力矩传感**：用于姿态稳定与关节闭环控制，详见「传感器与 MEMS」文件。

### 3. 灵巧手

灵巧手被视为机器人从"会移动"到"会操作"的接口，是"最后一厘米"的核心部件，正加速走向量产落地（[2026WRC 观察丨指尖破局：感知具身智能的"最后一厘米"](http://www.xinhuanet.com/tech/20260821/daf4da6b191f4dd4a46e4dfbad02c173/c.html)）。

## 关键数据与成本拆解

**BOM 结构（McKinsey 口径）**：人形机器人核心硬件分五大域——执行器占 BOM 的 40%–60%，感知系统 10%–20%，计算与控制平台 10%–15%，结构件 5%–10%，电池模组 5%–10%；五者合计约占整机成本的 85%–90%（[Turning humanoid supply chain constraints into billion-dollar wins](https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins)）。

**执行器占比的多方口径冲突**：Barclays 估计执行层约占人形机器人生产成本的 50%，McKinsey 等给出 40%–60%，另有工程分析给出高达 50%–70%；在减速器层面，谐波减速器常被视为最昂贵的单一部件（[Harmonic Drive](https://aiwiki.ai/wiki/harmonic_drive)）。

**谐波减速器价格（多口径）**：
- 哈默纳科（Harmonic Drive）标准谐波减速器单价约 1100–1200 元，高端定制款最高可达 8000 元；绿的谐波同类产品单价约 600–750 元；来福谐波 2025 年产品均价约为哈默纳科的 40%–60%（[消费级具身智能落地提速 人形机器人上游核心零部件迎新机遇（新华网）](http://www.news.cn/tech/20260622/20ac2af7c26643af9daa223e5ae9916a/c.html)）。
- 行业报告口径：通用工业级谐波减速器均价约 1000–1500 元/台；人形机器人专用型因轻量化、小型化及定制化要求，单价约 1500–3000 元/台，用于灵巧手的微型谐波减速器附加值更高；按单台机器人配置 14 个标准减速器（按 2000 元/台）与 8 个微型减速器（按 3000 元/台）估算（[“十五五”时期谐波减速器行业市场调研及发展趋势预测报告（新浪财经）](https://finance.sina.com.cn/roll/2026-09-03/doc-iniqpvfw2098419.shtml)）。
- 海外高端口径：单个高端谐波减速器约 800–1500 美元，若一台机器人需 35 个，则仅齿轮箱成本即高达约 5 万美元（[Scaling Humanoid Production: Sourcing Cost-Effective Harmonic Drives in China](https://www.piceamotiondrive.com/scaling-humanoid-production-sourcing-cost-effective-harmonic-drives-in-china.html)）。
- 中国市场份额：J.P. Morgan 于 2026 年初估计绿的谐波（Leaderdrive）占中国谐波减速器市场 30%–40%，其产量从 2022 年约 33 万台增长至 2025 年预期的约 79 万台（[Harmonic Drive](https://aiwiki.ai/wiki/harmonic_drive)）。

**六维力传感器市场（多口径）**：
- 2025 年中国人形机器人六维力传感器 CR3 达 92.8%，其中蓝点触控一家约占 80.3%（[CCID 赛迪《2026 年中国人形机器人六维力传感器市场调研报告》解读](https://www.xhby.net/content/s6a953347e4b02a27aa5a3759.html)）。
- 另一口径显示，2025 年蓝点触控国内人形机器人六维力传感器市占率 72.6%，关节力传感器国内出货量占比超 95%（[数亿元融资落地！六维力传感器龙头获 A 股千亿巨头押注（OFweek）](https://sensor.m.ofweek.com/2026-08/ART-81013-8120-30699992.html)）。
- 坤维科技口径：据 MIR 睿工业《2025 年六维力传感器行业发展白皮书》，坤维科技在智能机器人领域（人形机器人 + 协作机器人）六维力传感器出货量占比达 53%（[坤维科技 B++ 超亿元轮融资落地（人民网）](http://finance.people.com.cn/n1/2026/0609/c1004-40736552.html)）。
  说明：上述份额差异源于统计范围（"人形机器人"与"智能机器人"）及机构口径不同，需并列看待。

## 趋势与争议

1. **降本路径**：谐波减速器、执行器占整机成本过半，规模化与国产替代是降本主线；上游特种钢材（柔轮、刚轮用钢）成本与长期供货协议成为竞争要素（[How Humanoid Robot Joints Get Cheaper as Production Scales Up](https://www.laifualdrive.com/blog/humanoid-robot-joint-cost-scale/)）。
2. **灵巧手与触觉标准之争**：触觉传感的精度、采样率、量程等指标尚在标准化过程中（见 T/CAMETA 标准草案）。
3. **多口径数据并存**：执行器成本占比、减速器价格、力传感器份额均存在显著口径差异，产业尚无统一统计结论。

## 参考来源

- [消费级具身智能落地提速 人形机器人上游核心零部件迎新机遇（新华网）](http://www.news.cn/tech/20260622/20ac2af7c26643af9daa223e5ae9916a/c.html)
- [“十五五”时期谐波减速器行业市场调研及发展趋势预测报告（新浪财经）](https://finance.sina.com.cn/roll/2026-09-03/doc-iniqpvfw2098419.shtml)
- [Turning humanoid supply chain constraints into billion-dollar wins（McKinsey）](https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins)
- [Harmonic Drive](https://aiwiki.ai/wiki/harmonic_drive)
- [What a Humanoid Robot Costs to Build, and Why One Part Dominates the Bill](https://www.laifualdrive.com/blog/humanoid-robot-cost-harmonic-reducer/)
- [How Humanoid Robot Joints Get Cheaper as Production Scales Up](https://www.laifualdrive.com/blog/humanoid-robot-joint-cost-scale/)
- [Scaling Humanoid Production: Sourcing Cost-Effective Harmonic Drives in China](https://www.piceamotiondrive.com/scaling-humanoid-production-sourcing-cost-effective-harmonic-drives-in-china.html)
- [华威科万象系列 WRC 首发（中国日报网）](http://caijing.chinadaily.com.cn/a/202608/21/WS6a87c25ca3105d3d7a27c28f.html)
- [2026WRC 观察丨指尖破局：感知具身智能的"最后一厘米"（新华网）](http://www.xinhuanet.com/tech/20260821/daf4da6b191f4dd4a46e4dfbad02c173/c.html)
- [亮相 2026 世界机器人大会，千觉机器人让整只灵巧手拥有"高质量触觉"（上观新闻）](http://www.shobserver.com/wx/detail.do?id=1163975)
- [编织机器人电子皮肤成为可能（上观新闻）](https://www.shobserver.cn/wx/detail.do?id=1184701)
- [具身智能机器人灵巧手操作与驱控技术要求 T/CAMETA 001xxx—2026](https://www.cameta.org.cn/uploadfile/2026/0710/20260710042237363.pdf)
- [坤维科技将为第二届世界人形机器人运动会提供独家力控技术支持（中国日报网）](http://cn.chinadaily.com.cn/a/202608/25/WS6a8d4498e4b09dff9814f032.html)
- [坤维科技 B++ 超亿元轮融资落地（人民网）](http://finance.people.com.cn/n1/2026/0609/c1004-40736552.html)
- [《2026 年中国人形机器人六维力传感器市场调研报告》发布（ZAKER）](https://app.myzaker.com/news/article.php?pk=6a9501ecb15ec023311b1028)
- [CCID 赛迪《2026 年中国人形机器人六维力传感器市场调研报告》深度解读（新华日报）](https://www.xhby.net/content/s6a953347e4b02a27aa5a3759.html)
- [数亿元融资落地！六维力传感器龙头获 A 股千亿巨头押注（OFweek）](https://sensor.m.ofweek.com/2026-08/ART-81013-8120-30699992.html)