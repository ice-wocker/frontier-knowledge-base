# OT 与 IoT 安全

> 最后更新：2026-09-26 ｜ 领域：安全 · 工控、物联网与车联网 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

OT（Operational Technology）安全关注工业自动化与控制系统（IACS/ICS）、SCADA、PLC、HMI 等生产环境的可用性、完整性与安全性；IoT 安全关注海量联网终端（路由器、摄像头、DVR、消费设备）的固件、凭据与生命周期管理；车联网安全则围绕车辆电子电气架构、软件更新与供应链展开。OT 安全的核心标准是 IEC 62443 系列：它通过七项基础要求（FR）与安全等级（SL）把所需对策与潜在对手强度相关联，其中 IEC 62443-3-3 定义了 SL1–SL4 四个等级（[IEC 62443（IEC Cyber Security）](https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/)）。IEC 62443-4-2 则为四类组件（软件应用 SAR、嵌入式设备 EDR、主机设备 HDR、网络设备 NDR）给出组件要求（CR）与要求增强（RE），二者组合决定组件可达到的目标安全等级（[IEC 62443-4-2 Ed.1 预览](https://webstore.ansi.org/preview-pages/IEC/preview_iec62443-4-2%7Bed1.0%7Db.pdf)）。

## 最新进展（2025–2026）

**标准向 IIoT 与强制验证演进。** IEC PAS 62443-1-6 是面向工业 IoT 的新标准，为分布式软件、边到云架构、容器化、编排与虚拟化等现代形态提供把 IEC 62443 落到实处的实践指引（[Cyber security milestone for the industrial IoT（IEC e-tech）](https://etech.iec.ch/issue/cyber-security-milestone-for-the-industrial-iot)）。2026 年 5 月 1 日，IEC 62443-4-2:2026 正式实施，被视为对面向欧盟/美国 OEM 与系统集成商的工业仪表厂商（压力变送器、智能流量计、DCS 控制器等）产生直接影响（[IEC 62443-4-2:2026 Effective May 1](https://www.taeastargeo.com/news/Import_Export_Updates/IEC_62443_4_2_2026_Effective_May_1_Cybersecurity_Verification_Mandatory_for_Industrial_Instrument_Procurement_in_EU_US.html)）。英国标准 BS EN IEC 62443-4-2/AA:2026 亦作为修订件，替换了 Scope 并重申七项基础要求（system integrity、data confidentiality、restricted data flow、timely response to events、resource availability 等）（[BS EN IEC 62443-4-2/AA:2026](https://standardsdevelopment.bsigroup.com/projects/2026-00822)）。

**工业勒索软件持续高企。** Dragos 的 2026 年第二季度分析记录了 1,140 起影响工业组织的勒索事件，较第一季度的 1,020 起增长 12%；制造业以 747 起（65%）成为受影响最严重的行业，ICS 相关组织（工程公司、系统集成商、设备制造商）以 117 起位居第二（[Industrial Ransomware Analysis for Q2 2026](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026)）。第一季度的案例之一是罗马尼亚国家石油管道运营商 Conpet 在 2026 年 2 月确认遭网络攻击，其企业 IT 环境受影响、公开网站一度下线，但公司称未波及 SCADA、电信基础设施或管道控制环境，石油运输照常进行（[Industrial Ransomware Analysis for the First Quarter of 2026](https://www.dragos.com/dragos-industrial-ransomware-analysis-q1-2026)）。Kaspersky ICS CERT 亦报告 2026 年第二季度针对工业控制系统的勒索软件活动上升（[Kaspersky ICS CERT: Q2 2026](https://multisite3.geo.kaspersky.com/about/press-releases/kaspersky-ics-cert-q2-2026-saw-a-rise-in-ransomware-targeting-industrial-control-systems)）。

**水处理等关键基础设施的 PLC 成为直接目标。** Forescout 的分析指出，在 2025 年 7 月 27 日之后，至少 12 个州的供水与污水处理设施观察到类似事件，密歇根、南达科他、佐治亚等州被点名，其中密歇根有 9 个系统受影响、南达科他 1 个污水提升泵站受影响；FBI 与 EPA 的联合咨询指出攻击者针对 Rockwell Automation/Allen-Bradley MicroLogix 1100 与 1400 系列 PLC（[OT Security Analysis: Exposed Devices Attacked in US Water Systems](https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/)）。CISA 报告称面向水与污水处理部门 PLC 的攻击显著增加，攻击者修改密码以锁死操作员、通过更改 IP 地址断开 PLC，导致受影响水厂发布煮沸水通知并长时间转入人工操作（[Coordinated "cyberattack" on U.S. water utilities](https://fr.tenable.com/blog/coordinated-cyberattack-on-minnesota-water-utilities-what-you-need-to-know)）。相关报道还提到 CyberAv3ngers 在四个有记录阶段展现出能力递进（同上）。Forescout 的蜜罐在 2025 年 9 月捕获了针对诱饵水处理厂的攻击活动，与俄罗斯结盟的团伙 TwoNet 宣称负责，该团伙登录 HMI 实施了篡改、流程干扰、操纵与规避，并出现了与俄罗斯、伊朗相关的针对 PLC 与 Modbus 协议的额外攻击（[Anatomy of a Hacktivist Attack](https://www.forescout.com/blog/anatomy-of-a-hacktivist-attack-russian-aligned-group-targets-otics/)）。加拿大网络安全中心则就"威胁行为者利用 AI 在全球范围内主动攻击暴露在互联网的 PLC"发出警示，并关联到 Siemens S7 系列 PLC 的活动（[Canadian Centre for Cyber Security](https://www.cyber.gc.ca/en/news-events/cyber-threat-actors-use-artificial-intelligence-active-global-campaign-disrupt-internet-exposed-programmable-logic-controllers)）。

**IoT 僵尸网络转向"旧漏洞 + 长尾设备"。** Akamai 观察到两个 Mirai 变种并行传播：tuxnokill 通过 CVE-2025-29635（D-Link DIR-823X 路由器的命令注入漏洞，2025 年 3 月披露）扩散——该漏洞在披露后整整一年未被利用，直到公开 PoC 出现（[New Mirai variants target routers and DVRs in parallel campaigns](https://www.helpnetsecurity.com/2026/04/22/new-mirai-variants-target-routers-and-dvrs-via-old-flaws/)）。HKCERT 亦就 Mirai 变种利用 CVE-2025-29635 攻击已停止支持（EOL）的 D-Link DIR-823X 路由器发出告警，攻击者通过特定端点执行任意系统命令（[Botnet Alert - Mirai Botnet Targets End-of-Life D-Link Routers](https://www.hkcert.org/security-bulletin/botnet-alert-mirai-botnet-targets-end-of-life-d-link-routers_20260423)）。另一款 Linux 僵尸网络 Evooo1Bot 除 DDoS 外还具备 SOCKS5 代理、凭据窃取、网络扫描、SSH 暴力破解、流量嗅探、远程命令执行、文件传输、持久化与漏洞利用等能力，并可把路由器变为流量中继节点（[New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/amp/)、[Evooo1Bot: The New Linux Botnet](https://undercodenews.com/evooo1bot-the-new-linux-botnet-turning-routers-firewalls-and-edge-devices-into-weapons-video/)）。

**车联网合规框架持续细化。** UN Regulation No. 155 规定车辆网络安全与网络安全管理体系（CSMS）的统一条款，范围覆盖乘用车（M）、货车（N）、挂车（O，若装有至少一个 ECU）与四轮车（L6、L7）等类别，其要求可与 ISO/SAE 21434《道路车辆—网络安全工程》高度对应（[Cyber Security and Software Updating（VCA）](https://www.vehicle-certification-agency.gov.uk/connected-and-automated-vehicles/cyber-security-and-software-updating/)）。2026 年 5 月的 UNECE GRVA 文件提出对 UN R155 的修订提案（[Proposal for amendments to UN Regulation No. 155](https://unece.org/sites/default/files/2026-05/GRVA-25-31e.pdf)）；法规文本亦要求车辆制造商至少每年（或更频繁）向审批机构或技术服务部门报告监测活动结果，并要求密码模块符合共识标准，否则厂商需说明理由（[UN Regulation No. 155 [2025/5]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500005)）。

**IoT 法规侧向强制化收拢。** 欧盟《网络韧性法案》（Regulation (EU) 2024/2847，CRA）针对带数字元素的产品制定水平化网络安全要求，覆盖规划、设计、开发与维护各阶段，适用于智能家居助手、联网玩具、可穿戴等品类（[Horizontal cybersecurity requirements for products with digital elements（EUR-Lex）](https://eur-lex.europa.eu/EN/legal-content/summary/horizontal-cybersecurity-requirements-for-products-with-digital-elements-cyber-resilience-act.html?fromSummary=31)）。ETSI 已启动 17 项 CRA 欧洲标准（EN 304 6xx 系列）的批准流程，这些标准由 EN 303 645 衍生并加入专用安全要求与评估准则，预计自 2027 年起用于帮助制造商获得 CRA 合规、并为 Important Class I 产品提供符合性推定（[ETSI launches approval process for 17 European Standards supporting the CRA](https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/)、[How to raise the cybersecurity bar in Europe（ETSI 材料）](https://www.sil.fi/site/assets/files/9941/telepaiva26_davide_pratone.pdf)）。

## 核心技术与关键概念

- **IEC 62443 的结构**：七项基础要求 + 安全等级（SL1–SL4）把对策强度与对手强度对应；组件侧用 CR + RE 组合决定目标 SL，并按组件类型区分 SAR/EDR/HDR/NDR（[IEC](https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/)、[ANSI 预览](https://webstore.ansi.org/preview-pages/IEC/preview_iec62443-4-2%7Bed1.0%7Db.pdf)）。
- **控制层"从未设计过认证"的问题**：水厂 PLC 攻击暴露了控制层协议（如 Modbus）在设计上缺乏身份认证，使暴露在互联网上的设备可被直接操作（[Water utility PLC attacks](https://dev.to/kozhevniko/water-utility-plc-attacks-the-control-layer-that-was-never-designed-to-authenticate-1n61)）。
- **IT 与 OT 的隔离价值与现实**：Conpet 事件中 IT 受扰而 OT 未受影响，说明分区与纵深防御仍能限制损失范围（[Dragos Q1 2026](https://www.dragos.com/dragos-industrial-ransomware-analysis-q1-2026)）。
- **IoT 加固基线**：保持固件更新、更换默认管理员凭据、关闭远程管理面板、在厂商停止支持时替换设备（[BleepingComputer](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/amp/)）。
- **车联网合规工程**：以 CSMS 为核心，通过网络安全风险分析与缓解措施落地，并映射到 ISO/SAE 21434 的工程流程；密码模块需符合共识标准（[VCA](https://www.vehicle-certification-agency.gov.uk/connected-and-automated-vehicles/cyber-security-and-software-updating/)、[EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500005)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **标准组织**：IEC/ISA 62443 系列与 IEC PAS 62443-1-6（[IEC e-tech](https://etech.iec.ch/issue/cyber-security-milestone-for-the-industrial-iot)）；UNECE UN R155、ISO/SAE 21434（[VCA](https://www.vehicle-certification-agency.gov.uk/connected-and-automated-vehicles/cyber-security-and-software-updating/)）；ETSI EN 303 645 与 CRA 协调标准（[ETSI](https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/)）。
- **威胁情报与检测厂商**：Dragos（工业勒索季度分析，[dragos.com](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026)）、Kaspersky ICS CERT（[Kaspersky](https://multisite3.geo.kaspersky.com/about/press-releases/kaspersky-ics-cert-q2-2026-saw-a-rise-in-ransomware-targeting-industrial-control-systems)）、Forescout（蜜罐与暴露面分析，[forescout.com](https://www.forescout.com/blog/anatomy-of-a-hacktivist-attack-russian-aligned-group-targets-otics/)）。
- **政府与协调机构**：CISA、FBI/EPA 联合咨询（[Forescout 引述](https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/)）、加拿大网络安全中心（[cyber.gc.ca](https://www.cyber.gc.ca/en/news-events/cyber-threat-actors-use-artificial-intelligence-active-global-campaign-disrupt-internet-exposed-programmable-logic-controllers)）、HKCERT（[hkcert.org](https://www.hkcert.org/security-bulletin/botnet-alert-mirai-botnet-targets-end-of-life-d-link-routers_20260423)）。

## 关键数据与评测结果（附来源）

| 指标 | 数值 | 来源 |
| --- | --- | --- |
| 2026 Q2 工业组织勒索事件 | 1,140 起（Q1 为 1,020 起，+12%） | [Dragos Q2 2026](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026) |
| 制造业占比 | 747 起（65%） | 同上 |
| ICS 相关组织受影响数 | 117 起 | 同上 |
| 美国受影响州数（水/污水） | 至少 12 个州 | [Forescout](https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/) |
| 针对的水厂 PLC 型号 | Rockwell/Allen-Bradley MicroLogix 1100、1400 | 同上 |
| Mirai 变种利用的漏洞 | CVE-2025-29635（D-Link DIR-823X） | [Help Net Security](https://www.helpnetsecurity.com/2026/04/22/new-mirai-variants-target-routers-and-dvrs-via-old-flaws/) |
| 漏洞披露到被利用的间隔 | 约一年（2025-03 披露） | 同上 |
| 车厂报告监测结果频率 | 至少每年一次 | [UN R155 [2025/5]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500005) |
| 另据厂商报告（需谨慎引用） | 勒索占关键基础设施事件 38%、OT 内平均驻留 21 天 | [Shieldworkz OT Threat Landscape 2026](https://shieldworkz.com/blogs/how-ransomware-attacks-disrupt-industrial-systems) |

## 趋势与争议

- **暴露面是主要风险源**：多起事件的共同点是 PLC/HMI 直接或间接暴露在网络可达位置，且控制协议本身不认证调用方（[Forescout](https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/)、[dev.to](https://dev.to/kozhevniko/water-utility-plc-attacks-the-control-layer-that-was-never-designed-to-authenticate-1n61)）。
- **勒索目标从 IT 蔓延到 OT 可用性**：季度数据与 CERT 报告均显示针对工业控制系统的勒索活动上升（[Dragos](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026)、[Kaspersky](https://multisite3.geo.kaspersky.com/about/press-releases/kaspersky-ics-cert-q2-2026-saw-a-rise-in-ransomware-targeting-industrial-control-systems)）。
- **AI 被用于攻击暴露的 PLC**：官方机构已就 AI 参与的全球性 PLC 攻击活动发出警示（[Canadian Centre for Cyber Security](https://www.cyber.gc.ca/en/news-events/cyber-threat-actors-use-artificial-intelligence-active-global-campaign-disrupt-internet-exposed-programmable-logic-controllers)）。
- **长尾 IoT 设备的"漏洞长尾"**：EOL 设备与旧漏洞的组合仍可支撑大规模僵尸网络，且新型僵尸网络的能力已远超纯 DDoS（[Help Net Security](https://www.helpnetsecurity.com/2026/04/22/new-mirai-variants-target-routers-and-dvrs-via-old-flaws/)、[BleepingComputer](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/amp/)）。
- **从自愿指南到强制合规**：CRA 与 ETSI 协调标准把 IoT 安全要求推入法律义务与符合性推定框架，厂商需在 2027 年前完成适配（[ETSI](https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/)、[ETSI 材料](https://www.sil.fi/site/assets/files/9941/telepaiva26_davide_pratone.pdf)）。
- **数据口径差异**：工业勒索事件数由不同厂商按各自方法学统计（如 Dragos 的季度口径与厂商年度报告口径不同），不宜直接相加或横向比较（[Dragos](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026)、[Shieldworkz](https://shieldworkz.com/blogs/how-ransomware-attacks-disrupt-industrial-systems)）。

## 参考来源

- [IEC 62443（IEC Cyber Security）](https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/)
- [Security for industrial automation and control systems - Part 4-2（ANSI 预览）](https://webstore.ansi.org/preview-pages/IEC/preview_iec62443-4-2%7Bed1.0%7Db.pdf)
- [BS EN IEC 62443-4-2/AA:2026](https://standardsdevelopment.bsigroup.com/projects/2026-00822)
- [Cyber security milestone for the industrial IoT（IEC e-tech）](https://etech.iec.ch/issue/cyber-security-milestone-for-the-industrial-iot)
- [IEC 62443-4-2:2026 Effective May 1](https://www.taeastargeo.com/news/Import_Export_Updates/IEC_62443_4_2_2026_Effective_May_1_Cybersecurity_Verification_Mandatory_for_Industrial_Instrument_Procurement_in_EU_US.html)
- [Dragos Industrial Ransomware Analysis for Q2 2026](https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026)
- [Dragos Industrial Ransomware Analysis for the First Quarter of 2026](https://www.dragos.com/dragos-industrial-ransomware-analysis-q1-2026)
- [Kaspersky ICS CERT: Q2 2026 saw a rise in ransomware targeting ICS](https://multisite3.geo.kaspersky.com/about/press-releases/kaspersky-ics-cert-q2-2026-saw-a-rise-in-ransomware-targeting-industrial-control-systems)
- [OT Security Analysis: Exposed Devices Attacked in US Water Systems（Forescout）](https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/)
- [Anatomy of a Hacktivist Attack: Russian-Aligned Group Targets OT/ICS（Forescout）](https://www.forescout.com/blog/anatomy-of-a-hacktivist-attack-russian-aligned-group-targets-otics/)
- [Coordinated "cyberattack" on U.S. water utilities（Tenable）](https://fr.tenable.com/blog/coordinated-cyberattack-on-minnesota-water-utilities-what-you-need-to-know)
- [Water utility PLC attacks: the control layer that was never designed to authenticate](https://dev.to/kozhevniko/water-utility-plc-attacks-the-control-layer-that-was-never-designed-to-authenticate-1n61)
- [Cyber threat actors use artificial intelligence in an active global campaign to disrupt internet-exposed PLCs（Canadian Centre for Cyber Security）](https://www.cyber.gc.ca/en/news-events/cyber-threat-actors-use-artificial-intelligence-active-global-campaign-disrupt-internet-exposed-programmable-logic-controllers)
- [How ransomware attacks disrupt industrial systems（Shieldworkz）](https://shieldworkz.com/blogs/how-ransomware-attacks-disrupt-industrial-systems)
- [New Mirai variants target routers and DVRs in parallel campaigns](https://www.helpnetsecurity.com/2026/04/22/new-mirai-variants-target-routers-and-dvrs-via-old-flaws/)
- [Botnet Alert - Mirai Botnet Targets End-of-Life D-Link Routers（HKCERT）](https://www.hkcert.org/security-bulletin/botnet-alert-mirai-botnet-targets-end-of-life-d-link-routers_20260423)
- [New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/amp/)
- [Evooo1Bot: The New Linux Botnet Turning Routers, Firewalls, and Edge Devices Into Weapons](https://undercodenews.com/evooo1bot-the-new-linux-botnet-turning-routers-firewalls-and-edge-devices-into-weapons-video/)
- [Cyber Security and Software Updating（UK VCA）](https://www.vehicle-certification-agency.gov.uk/connected-and-automated-vehicles/cyber-security-and-software-updating/)
- [Proposal for amendments to UN Regulation No. 155（UNECE, 2026-05）](https://unece.org/sites/default/files/2026-05/GRVA-25-31e.pdf)
- [UN Regulation No. 155 [2025/5]（EUR-Lex）](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202500005)
- [UN Regulation 155 on Cybersecurity and its impact（UNECE PDF）](https://unece.org/sites/default/files/2023-09/WP5_Session36_KaiFrederikZastrow.pdf)
- [Horizontal cybersecurity requirements for products with digital elements (CRA)（EUR-Lex）](https://eur-lex.europa.eu/EN/legal-content/summary/horizontal-cybersecurity-requirements-for-products-with-digital-elements-cyber-resilience-act.html?fromSummary=31)
- [ETSI launches approval process for 17 European Standards supporting the CRA](https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/)
- [How to raise the cybersecurity bar in Europe with the harmonized standards（ETSI 材料 PDF）](https://www.sil.fi/site/assets/files/9941/telepaiva26_davide_pratone.pdf)