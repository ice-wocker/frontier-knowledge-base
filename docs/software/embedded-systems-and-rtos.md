# 嵌入式系统与 RTOS

> 最后更新：2026-09-26 ｜ 领域：软件·平台与领域应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

嵌入式系统以 MCU（微控制器）为核心，围绕实时操作系统（RTOS）、固件实时性、功能安全认证与 IoT 协议栈构建。2025–2026 年，Zephyr 与 FreeRTOS 两条开源主线分别通过新架构与长期支持（LTS）版本推进企业级落地；安全认证（ISO 26262、IEC 61508、IEC 62304、EN 50128）成为商用 RTOS 的竞争焦点；互联层面，Matter 生态持续迭代，MCU 架构上 ARM Cortex-M 仍占主导而 RISC-V 快速上升。

## 最新进展（2025–2026）

**Zephyr**：Zephyr 3.7.0 是最后一个非维护性的 3.x 版本，也因此成为下一个长期支持（LTS）版本；该版本引入全新重构的硬件模型，改变 SoC 与开发板在 Zephyr 中的命名、定义与构建方式，并新增期待已久的 HTTP Server 库（[Zephyr 3.7.0](https://docs.zephyrproject.org/latest/releases/release-notes-3.7.html)）。此后 Zephyr 4.2 加入对 Armv8.1-M MPU 的 PXN（Privileged Execute Never）属性支持（[Zephyr 4.2.0](https://docs.zephyrproject.org/latest/releases/release-notes-4.2.html)）；4.4 新增一次性可编程（OTP）存储 API、生物识别 API（指纹/人脸等）、唤醒控制器（WUC）API，以及 Zbus 异步监听器与代理（[Zephyr 4.4.0](https://docs.zephyrproject.org/latest/releases/release-notes-4.4.html)）；4.5（工作草案）新增 Infineon TriCore 架构支持、Clock Monitor 驱动类与 Video 子系统（[Zephyr 4.5.0 (Working Draft)](https://docs.zephyrproject.org/latest/releases/release-notes-4.5.html)）。2026 年 9 月 21 日，Canonical 在 embedded world North America 前宣布即将推出 **Zephyr 26.04 LTS**，定位为企业级 Zephyr 发行版，为 MCU 级设备提供最长 15 年的支持（[Canonical announces Zephyr 26.04 LTS](https://canonical.com/blog/zephyr-lts-announcement)）。

**FreeRTOS**：最新的 LTS 版本 FreeRTOS **202604.00 LTS** 将获得 AWS 认定为关键的安全与缺陷修复支持至 2028 年 4 月 30 日；上一版 LTS（202406.05 LTS）的支持于 2026 年 6 月 30 日结束，LTS 的支持期通常为两年（[FreeRTOS FAQ — Long Term Support](https://www.freertos.org/Why-FreeRTOS/FAQs/Long-term-support/)）。FreeRTOS 202604 LTS 提供两年特性稳定性、安全更新与关键缺陷修复，覆盖内存安全、代码质量与协议支持等嵌入式挑战，其内核为 **FreeRTOS v11.3.0**（[FreeRTOS 202604 LTS 现已发布](https://aws.amazon.com/pt/about-aws/whats-new/2026/04/freertos-lts/)）。该版本提供 MQTT v5.0 支持，并包含 coreMQTT、coreSNTP 的迁移指南；coreSNTP v2.0.0 的可用周期可持续至 2038 年，使设备在整个运行周期内都能正确验证 TLS 证书与时间戳数据（[FreeRTOS 202604 LTS 现已发布（中文）](https://aws.amazon.com/cn/about-aws/whats-new/2026/04/freertos-lts/)）。此外，FreeRTOS 已通过 **SESIP Level 2** 与 **PSA Level 1** 认证，其基础连接库包括 FreeRTOS-Plus-TCP 与 coreMQTT（[FreeRTOS Security overview](https://smtp1.freertos.org/Security/01-Security-overview)）。

## 核心技术与关键概念

**实时性与调度**：RTOS 的核心在于确定性调度、优先级管理与低中断延迟。开源方案（Zephyr、FreeRTOS）通过配置裁剪适配不同资源预算，商用方案则在此基础上提供内存保护与认证证据。

**功能安全标准与认证**：面向不同领域，认证标准各异——
- 汽车：ISO 26262，安全等级 ASIL A–D；
- 工业：IEC 61508，SIL 1–4；
- 医疗：IEC 62304，Class A–C；
- 轨交：EN 50128，SIL 1–4；
- 航空：RTCA DO-178C / EUROCAE ED-12C。

**商用与认证 RTOS**：Arm 的功能安全运行时系统（FuSa RTS）经 TÜV SÜD 认证，适用于汽车（ISO 26262, ASIL D）、工业（IEC 61508, SIL 3）、医疗（IEC 62304, Class C）与铁路（EN 50128, SIL 4）（[Arm FuSa RTS](https://www.arm.com/products/development-tools/embedded-and-software/fusa-rts)）。SafeRTOS 由 WITTENSTEIN high integrity systems（WHIS）开发，基于 FreeRTOS 功能模型，预认证至 IEC 61508 SIL 3 与 ISO 26262 ASIL D（[Safety Critical Real-Time OS](https://hop.freertos.org/Partners/Software/SafeRTOS)）。VxWorks Cert Edition 面向需认证至 DO-178C/ED-12C、IEC 61508、ISO 26262 的安全关键应用（[VxWorks Cert Edition](https://www.windriver.com/themes/Windriver/pdf/vxworks-cert-product-overview.pdf)）。µ-velOSity 以约 2.6 KB 的最小占用与微内核架构，认证至 ISO 26262 ASIL D 与 IEC 61508 SIL 3，支持 Arm 与 RISC-V 架构（[µ-velOSity RTOS](https://www.st.com/en/partner-products-and-services/181-velosity-real-time-operating-system.html)）。

**系统语言与安全**：Ferrocene 提供经认证的 Rust 编译器工具链，面向汽车、工业与医疗的安全关键嵌入式系统，可满足 ISO 26262（ASIL D）、IEC 61508（SIL 4）与 IEC 62304（Class C）（[Ferrocene](https://www.st.com/en/partner-products-and-services/ferrocene.html)）。

**IoT 协议栈**：Matter 使用 Thread、Wi-Fi 与 Ethernet 作为传输层，并以 Bluetooth LE 进行配网（commissioning）；所有基于 Thread 的 Matter 设备必须同时具备 BLE 以便加入网络；Wi-Fi 用于高带宽应用，Thread 是面向低带宽、以电池供电设备的 IPv6 mesh 协议（[Matter Protocol — Nordic Semiconductor](https://www.nordicsemi.com/Products/Technologies/Matter)）。Matter 规范首版即运行于 Ethernet（802.3）、Wi-Fi（802.11）、Thread（802.15.4）之上，并以 BLE 便于配网（[The Connectivity Standards Alliance Unveils Matter](https://csa-iot.org/newsroom/chip-is-now-matter/)）。2026 年 4 月，CSA 发布 **Matter 1.5.1**，在 Matter 1.5 引入摄像头与视频门铃支持的基础上，进一步方便厂商打造高质量摄像头与门铃产品（[Matter 1.5.1](https://csa-iot.org/newsroom/matter-1-5-1-enhancing-camera-performance-and-expanding-device-flexibility/)）。学术界也指出，Zigbee 是成熟的非 IP mesh 方案，而 Matter over Thread 以 IPv6 低功耗 mesh 上的统一应用层应对互操作挑战，二者正成为智能家居基础设施级低功耗通信的两大范式（[Zigbee vs. Matter over Thread](https://arxiv.org/pdf/2603.04221)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **Zephyr Project**：Linux Foundation 旗下开源 RTOS，硬件抽象与驱动模型重构后向企业 LTS 演进（[Zephyr Releases](https://docs.zephyrproject.org/latest/releases/release-notes-3.7.html)）。
- **FreeRTOS（Amazon/AWS）**：广泛使用的开源 RTOS，提供 LTS、CMSIS Packs 与连接库；其最新 LTS 库已作为 CMSIS Packs 发布，供 Arm Cortex-M 团队通过 IDE 内置包管理器管理依赖（[FreeRTOS](https://en.freertos.org/)）。
- **Arm**：Cortex-M 生态与 FuSa RTS 认证软件（[Arm FuSa RTS](https://www.arm.com/products/development-tools/embedded-and-software/fusa-rts)）。
- **Wind River / WITTENSTEIN / Green Hills（ST 合作）**：商用认证 RTOS 提供方（[VxWorks Cert](https://www.windriver.com/themes/Windriver/pdf/vxworks-cert-product-overview.pdf)、[SafeRTOS](https://hop.freertos.org/Partners/Software/SafeRTOS)、[µ-velOSity](https://www.st.com/en/partner-products-and-services/181-velosity-real-time-operating-system.html)）。
- **CSA（Connectivity Standards Alliance）**：Matter 标准制定组织（[CSA](https://csa-iot.org/newsroom/matter-1-5-1-enhancing-camera-performance-and-expanding-device-flexibility/)）。

## 关键数据与评测结果（附来源）

- **MCU 架构份额**：按核心架构，ARM Cortex-M 在 2025 年保持 **68.25%** 的份额，得益于成熟工具链与稳健中间件栈；RISC-V 预计以 **15.09% 的 CAGR** 扩张至 2031 年（[Microcontroller (MCU) Market Share Analysis 2026-2031](https://www.researchandmarkets.com/reports/5601267/microcontroller-mcu-market-share-analysis)）。在 IoT MCU 细分中，ARM 架构 MCU 2025 年约占出货量的 **71.89%**，RISC-V 设备预计到 2031 年以 **16.41%** 的 CAGR 增长（[IoT Microcontroller Market](https://www.mordorintelligence.kr/industry-reports/iot-microcontroller-market)）。
- **RISC-V 出货**：有来源称 RISC-V 核心年出货量已突破 **25 亿颗**，其中中国市场（GigaDevice、Nuclei 等）到 2026 年初累计出货约 8 亿颗 RISC-V MCU；另有数据称 RISC-V 架构已占新 MCU 产品发布量的约 **18%**（[RISC-V in 2026](https://www.justlast.in/risc-v-in-2026-how-the-open-source-processor-architecture-is-disrupting-arm-in-embedded-systems-and-iot/)、[32-bit MCU Market](https://www.globalgrowthinsights.com/ko/market-reports/32-bit-microcontroller-unit-mcu-market-117403)）。上述数字来自不同市场研究机构，口径与统计范围不一，宜并列参考。
- **安全认证等级**：Arm FuSa RTS 覆盖 ISO 26262 ASIL D / IEC 61508 SIL 3 / IEC 62304 Class C / EN 50128 SIL 4；SafeRTOS 预认证至 IEC 61508 SIL 3 与 ISO 26262 ASIL D；µ-velOSity 认证至 ISO 26262 ASIL D 与 IEC 61508 SIL 3（各见上引来源）。
- **支持周期**：FreeRTOS LTS 支持期两年，202604.00 LTS 至 2028-04-30；Zephyr 26.04 LTS 宣称最长 15 年（[FreeRTOS LTS FAQ](https://www.freertos.org/Why-FreeRTOS/FAQs/Long-term-support/)、[Canonical Zephyr 26.04 LTS](https://canonical.com/blog/zephyr-lts-announcement)）。

## 趋势与争议

**趋势**：一是「LTS 化与长周期支持」——无论是 FreeRTOS 的两年 LTS 还是 Canonical 提出的最长 15 年 Zephyr 支持，都指向嵌入式长生命周期设备的维护诉求；二是「安全认证商品化」——多家厂商以预认证 RTOS 与经认证的 Rust 工具链降低合规成本；三是「RISC-V 上升」——开源指令集在成本敏感与主权政策驱动下加速，但目前 Cortex-M 仍占出货大头。

**争议与分化**：其一，市场份额数据分散——Cortex-M 份额在不同报告中从 68.25% 到 IoT 细分的 71.89% 不等，且 RISC-V 的「份额」与「增长率」口径常被混用，需区分出货占比与 CAGR（[Research and Markets](https://www.researchandmarkets.com/reports/5601267/microcontroller-mcu-market-share-analysis)、[Mordor Intelligence](https://www.mordorintelligence.kr/industry-reports/iot-microcontroller-market)）。其二，IoT 协议路线之争——Zigbee（非 IP mesh，成熟）与 Matter over Thread（IPv6 统一应用层）长期并存，迁移与互操作仍有成本（[Zigbee vs. Matter over Thread](https://arxiv.org/pdf/2603.04221)）。其三，安全语言选择上，Rust 被引入安全关键领域的同时，也引发与既有 C/C++ 认证资产的衔接与工具链成熟度讨论（[Ferrocene](https://www.st.com/en/partner-products-and-services/ferrocene.html)）。

## 参考来源

- [Zephyr 3.7.0](https://docs.zephyrproject.org/latest/releases/release-notes-3.7.html)
- [Zephyr 4.2.0](https://docs.zephyrproject.org/latest/releases/release-notes-4.2.html)
- [Zephyr 4.4.0](https://docs.zephyrproject.org/latest/releases/release-notes-4.4.html)
- [Zephyr 4.5.0 (Working Draft)](https://docs.zephyrproject.org/latest/releases/release-notes-4.5.html)
- [Canonical announces Zephyr 26.04 LTS](https://canonical.com/blog/zephyr-lts-announcement)
- [FreeRTOS FAQ — Long Term Support](https://www.freertos.org/Why-FreeRTOS/FAQs/Long-term-support/)
- [FreeRTOS 202604 LTS 现已发布（AWS 中文）](https://aws.amazon.com/cn/about-aws/whats-new/2026/04/freertos-lts/)
- [FreeRTOS 202604 LTS (AWS)](https://aws.amazon.com/pt/about-aws/whats-new/2026/04/freertos-lts/)
- [FreeRTOS Security overview](https://smtp1.freertos.org/Security/01-Security-overview)
- [FreeRTOS 官网](https://en.freertos.org/)
- [Arm FuSa RTS](https://www.arm.com/products/development-tools/embedded-and-software/fusa-rts)
- [SafeRTOS — Safety Critical Real-Time OS](https://hop.freertos.org/Partners/Software/SafeRTOS)
- [VxWorks Cert Edition](https://www.windriver.com/themes/Windriver/pdf/vxworks-cert-product-overview.pdf)
- [µ-velOSity Real Time Operating System](https://www.st.com/en/partner-products-and-services/181-velosity-real-time-operating-system.html)
- [Ferrocene qualified Rust toolchain](https://www.st.com/en/partner-products-and-services/ferrocene.html)
- [Matter Protocol — Nordic Semiconductor](https://www.nordicsemi.com/Products/Technologies/Matter)
- [The Connectivity Standards Alliance Unveils Matter](https://csa-iot.org/newsroom/chip-is-now-matter/)
- [Matter 1.5.1: Enhancing Camera Performance and Expanding Device Flexibility](https://csa-iot.org/newsroom/matter-1-5-1-enhancing-camera-performance-and-expanding-device-flexibility/)
- [Matter 1.5.1 规范发布（电子工程专辑）](https://www.eet-china.com/mp/a485363.html)
- [Zigbee vs. Matter over Thread: Understanding IoT Protocol Performance in Practice](https://arxiv.org/pdf/2603.04221)
- [Microcontroller (MCU) Market Share Analysis 2026-2031](https://www.researchandmarkets.com/reports/5601267/microcontroller-mcu-market-share-analysis)
- [IoT Microcontroller Market](https://www.mordorintelligence.kr/industry-reports/iot-microcontroller-market)
- [RISC-V in 2026](https://www.justlast.in/risc-v-in-2026-how-the-open-source-processor-architecture-is-disrupting-arm-in-embedded-systems-and-iot/)
- [32-bit MCU Market](https://www.globalgrowthinsights.com/ko/market-reports/32-bit-microcontroller-unit-mcu-market-117403)