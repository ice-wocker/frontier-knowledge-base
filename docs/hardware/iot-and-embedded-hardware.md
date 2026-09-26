# IoT 与嵌入式硬件

> 最后更新：2026-09-26 ｜ 领域：硬件 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

IoT（Internet of Things，物联网）与嵌入式硬件指面向传感、连接与控制的微控制器（MCU）、无线 SoC、通信模组与工业/边缘网关等。其技术栈核心是 MCU 生态、无线协议（BLE、Thread、Wi-Fi、LoRa、NB-IoT、Matter）与边缘计算能力。IoT 与嵌入式硬件覆盖面广，一款产品往往需同时权衡功耗、成本、连接协议与安全能力，因此 MCU、无线 SoC 与通信模组构成其核心供应链。2025–2026 年，Matter 标准迭代、LoRaWAN 规模化部署与无线 MCU 集成化是三条主线，安全能力（如安全启动与密钥存储）也日益成为选型要点。

## 最新进展（2025–2026）

- **无线 MCU 国产放量**：一份 2026 年行业报告显示，截至 2025 年国内主流厂商已实现从 40nm 向 22nm 工艺平台的批量导入，其中乐鑫科技 ESP32 系列 2025 年出货量达 4.8 亿颗，占国内短距无线 MCU 总出货量的 31.6%；国民技术 N32WB 系列全年销量 1.2 亿颗，市占率 7.9%（[2026 年中国短距离连接无线 MCU 行业市场现状调查及投资机会研判报告（豆丁网）](https://www.docin.com/touch_new/preview_new.do?id=4986815211)）。
- **Matter 1.5 补齐视频框架**：2025 年末发布的 Matter 1.5 为视频设备带来完整框架，覆盖泛光照明摄像头、视频门铃、门铃提示器与室内对讲机，支持直播、录制、双向音频与云台控制，并采用 WebRTC 等成熟技术保障安全与跨平台兼容（[Matter 通过五大里程碑改变智能家居世界（电子工程专辑）](https://www.eet-china.com/mp/a480095.html)）。
- **Matter over Thread 模组成熟**：移远通信（Quectel）发布基于 Silicon Labs EFR32MG24 的 KGM133S 系列 Matter over Thread 模组，支持最新 Matter 1.4 协议，旨在打通 Apple Home、Google Home、Amazon Alexa、Samsung SmartThings 等生态（[Quectel unveils advanced Matter over Thread modules](https://www.quectel.com/news-and-pr/matter-over-thread-modules-interoperability-kgm133s/)）。
- **LoRaWAN 规模里程碑**：LoRa Alliance 于 2025 年 12 月 10 日宣布其成员全球部署的 LoRaWAN 终端设备已突破 1.25 亿台，复合年增长率约 25%（[LoRa Alliance Reports 125 Million LoRaWAN End Devices Deployed Globally](https://resources.lora-alliance.org/lora-alliance-blog/lora-alliance-reports-125-million-lorawan-end-devices-deployed-globally)）。

## 核心技术与关键概念

- **MCU 与无线 MCU**：MCU 是嵌入式系统的主控芯片；集成 Wi-Fi/BLE/802.15.4 射频的无线 MCU 可单芯片同时支持多种协议，减少多芯片方案。2025 年 BLE 占低功耗无线 IoT SoC 协议份额的 45.9%，智能家居与消费电子为最大应用（35.7%）（[Worldwide Low Power Wireless IoT System-on-Chip Market 2026](https://pmarketresearch.com/worldwide-low-power-wireless-iot-system-on-chip-market-research/)）。
- **Matter / Thread**：Matter 是跨生态的应用层互操作标准，Thread 是其常用的低功耗网状网络承载（基于 802.15.4）。Matter 1.4（2024 年秋季）引入增强多管理员（Enhanced Multi-Admin）、家庭路由器与接入点（HRAP）支持，并新增太阳能板、电池、热泵、热水器、入墙式负载控制器等设备类型（[Matter Protocol — Nordic Semiconductor](https://www.nordicsemi.com/Products/Technologies/Matter)）。
- **BLE 与 802.15.4 融合**：Silicon Labs 的 Matter over Thread SoC/模组同时支持用于配网的 BLE 与用于 Matter 的 802.15.4，无需多芯片；其 EFR32MG21/MG24/MG26 与 SiMG301 覆盖不同 Flash/RAM 配置（[Matter Developer Journey With Silicon Labs](https://www.silabs.com/wireless/matter/matter-developer-journey)）。乐鑫 ESP-Matter 亦支持 ESP32-C6/ESP32-H 等带 802.15.4 的 SoC 构建 Matter Thread 设备，并用 ESP32-H 与 Wi-Fi SoC 组合构建 Thread 边界路由器（[ESP-Matter Programming Guide](https://docs.espressif.com/projects/esp-matter/en/release-v1.4.2/esp32c6/esp-matter-en-master-esp32c6.pdf)）。
- **LPWAN（LoRa / NB-IoT）**：面向远距离低功耗场景，LoRaWAN 由 LoRa Alliance 维护，成员约 360 家（2025 年新增 57 家）（[LPWAN 市场格局 2026：LoRaWAN vs NB-IoT vs Sigfox（腾讯云开发者社区）](https://cloud.tencent.com/developer/article/2741424)）。
- **协议选型**：短距场景常用 BLE 与 Thread/802.15.4（Matter 的常用承载），远距离低功耗场景则用 LoRaWAN 或 NB-IoT 等 LPWAN；BLE 在低功耗无线 IoT SoC 中份额领先（45.9%），智能家居与消费电子为最大终端市场（[Worldwide Low Power Wireless IoT System-on-Chip Market 2026](https://pmarketresearch.com/worldwide-low-power-wireless-iot-system-on-chip-market-research/)）。
- **MCU 与无线 SoC 的集成趋势**：将 MCU、射频、存储与安全单元（如 Secure Vault）集成到单芯片，可减小体积与功耗；Silicon Labs 的 Matter SoC 即把 802.15.4 与 BLE 集成于同一芯片以简化配网（[Matter Developer Journey With Silicon Labs](https://www.silabs.com/wireless/matter/matter-developer-journey)）。
- **边缘/工业网关**：网关负责协议转换、边缘计算与上行汇聚，是 IoT 与工业现场的关键节点；LoRa 网关芯片组在公用事业与物流网络带动下保持增长（见下节数据）。

## 代表性厂商 / 产品

| 领域 | 厂商 / 产品 | 说明 |
| --- | --- | --- |
| 无线 MCU | 乐鑫科技 ESP32 系列 | 2025 年出货 4.8 亿颗，国内份额 31.6% |
| 无线 MCU | 国民技术 N32WB 系列 | 2025 年销量 1.2 亿颗，份额 7.9% |
| Matter SoC/模组 | Silicon Labs EFR32MG 系列、SiMG301 | 支持 Matter over Thread + BLE 配网 |
| Matter 模组 | Quectel KGM133S | 基于 EFR32MG24，支持 Matter 1.4 |
| Matter 生态 | Apple Home、Google Home、Amazon Alexa、Samsung SmartThings | Matter 跨生态目标 |
| LPWAN | LoRa Alliance / LoRaWAN | 全球终端部署超 1.25 亿台 |

## 关键数据与评测结果

**市场规模（多口径并列）**：
- MCU 市场：2025 年约 347.5 亿美元，2026 年约 383.4 亿美元，预计 2031 年达 627.4 亿美元，CAGR 约 10.33%（[Microcontroller (MCU) Market（Mordor Intelligence）](https://www.mordorintelligence.it/industry-reports/microcontroller-mcu-market)）。
- Wi-Fi 与蓝牙 MCU：2025 年约 60.0 亿美元，2026 年约 67.71 亿美元（[Worldwide Wi-Fi and Bluetooth MCU Market 2026](https://pmarketresearch.com/worldwide-wi-fi-and-bluetooth-mcu-market-research/)）。
- 低功耗无线 IoT SoC：亚太区 2025 年约 19.4 亿美元；BLE 为最大协议份额（45.9%）（[Worldwide Low Power Wireless IoT System-on-Chip Market 2026](https://pmarketresearch.com/worldwide-low-power-wireless-iot-system-on-chip-market-research/)）。该市场以亚太为最大区域，智能家居与消费电子为主要应用场景。
- LoRa 网关市场：2025 年约 12.8 亿美元，预计 2032 年达 37.3 亿美元，CAGR 约 16.5%（[LoRa Gateway Market 2026](https://pmarketresearch.com/worldwide-lora-gateway-market-research/)）。
- LoRa/LoRaWAN IoT 市场：2025 年约 112.9 亿美元，2026 年约 172.9 亿美元，2032 年预计 692.9 亿美元，CAGR 约 26.03%（[LoRa and LoRaWAN IoT Market Research Report](https://www.marknteladvisors.com/research-library/lora-lorawan-iot-market-study.html)）。
- LoRa 芯片组：2025 年美国网关芯片组市场约 5510 万美元、份额约 30%，预计 2034 年达 7.744 亿美元，由公用事业与物流网络带动（[LoRa chipsets Market](https://www.industryresearch.biz/es/market-reports/lora-chipsets-market-107323)）。

## 趋势与争议

1. **协议碎片化**：多种竞争性无线协议并存提升了设计复杂度、延长了多协议共存测试与认证周期，被视为无线 MCU 市场的主要制约之一（[Wireless Microcontroller Market](https://www.emergenresearch.com/industry-report/wireless-microcontroller-market)）。
2. **Matter 的"最后一公里"**：Matter 通过视频设备框架与多管理员改进来扩大覆盖，但生态实际互操作体验仍是落地关键（见 Matter 1.5 与 Nordic 资料）。
3. **LoRaWAN vs NB-IoT vs Sigfox**：不同 LPWAN 路线在成本、覆盖与生态上竞争，市场规模预测差异较大，引用需注明口径。
4. **边缘智能上移**：随着无线 MCU 工艺向 22nm 乃至更先进节点迁移，端侧算力与边缘网关能力持续增强（见无线 MCU 行业报告）。
5. **工艺迁移**：国内短距无线 MCU 主流厂商已完成从 40nm 向 22nm 工艺平台的批量导入，推动单芯片集成度与能效提升（见上）。
6. **标准化与生态竞争**：Matter 通过视频设备框架与多管理员改进扩大覆盖面，但跨生态互操作的实际体验仍是落地关键（见上）。
7. **模组化与一站式方案**：模组厂商提供预集成射频、协议栈与安全能力的方案（如 Quectel 的 Matter over Thread 模组），以降低终端厂商的开发与认证门槛，加速产品上市（[Quectel unveils advanced Matter over Thread modules](https://www.quectel.com/news-and-pr/matter-over-thread-modules-interoperability-kgm133s/)）。

## 参考来源

- [2026 年中国短距离连接无线 MCU 行业市场现状调查及投资机会研判报告（豆丁网）](https://www.docin.com/touch_new/preview_new.do?id=4986815211)
- [Matter 通过五大里程碑改变智能家居世界（电子工程专辑）](https://www.eet-china.com/mp/a480095.html)
- [Quectel unveils advanced Matter over Thread modules](https://www.quectel.com/news-and-pr/matter-over-thread-modules-interoperability-kgm133s/)
- [LoRa Alliance Reports 125 Million LoRaWAN End Devices Deployed Globally](https://resources.lora-alliance.org/lora-alliance-blog/lora-alliance-reports-125-million-lorawan-end-devices-deployed-globally)
- [LPWAN 市场格局 2026：LoRaWAN vs NB-IoT vs Sigfox（腾讯云开发者社区）](https://cloud.tencent.com/developer/article/2741424)
- [Matter Protocol — Nordic Semiconductor](https://www.nordicsemi.com/Products/Technologies/Matter)
- [Matter Developer Journey With Silicon Labs](https://www.silabs.com/wireless/matter/matter-developer-journey)
- [ESP-Matter Programming Guide（Espressif）](https://docs.espressif.com/projects/esp-matter/en/release-v1.4.2/esp32c6/esp-matter-en-master-esp32c6.pdf)
- [Worldwide Low Power Wireless IoT System-on-Chip Market 2026](https://pmarketresearch.com/worldwide-low-power-wireless-iot-system-on-chip-market-research/)
- [Worldwide Wi-Fi and Bluetooth MCU Market 2026](https://pmarketresearch.com/worldwide-wi-fi-and-bluetooth-mcu-market-research/)
- [Microcontroller (MCU) Market（Mordor Intelligence）](https://www.mordorintelligence.it/industry-reports/microcontroller-mcu-market)
- [LoRa Gateway Market 2026](https://pmarketresearch.com/worldwide-lora-gateway-market-research/)
- [LoRa and LoRaWAN IoT Market Research Report](https://www.marknteladvisors.com/research-library/lora-lorawan-iot-market-study.html)
- [Wireless Microcontroller Market](https://www.emergenresearch.com/industry-report/wireless-microcontroller-market)
- [LoRa chipsets Market（industryresearch.biz）](https://www.industryresearch.biz/es/market-reports/lora-chipsets-market-107323)