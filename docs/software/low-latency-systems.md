# 低延迟系统

> 最后更新：2026-09-26 ｜ 领域：软件·平台与领域应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

低延迟系统追求从微秒到纳秒级的确定性响应，广泛用于高频交易（HFT）、实时音视频、工业控制与电信前传等场景。其核心技术路线包括**内核旁路（kernel bypass）**、**用户态网络栈（DPDK / AF_XDP）**、**硬件卸载（FPGA/ASIC）**、**异步 I/O（io_uring）**以及**介质与部署拓扑优化**。2025–2026 年，这些技术的关注点从「绝对最快」转向「可控的尾延迟」与「可编程性」。

## 最新进展（2025–2026）

**DPDK**：DPDK 26.07 发布了多个新特性与 API 变更，包括将 `rte_memeq_timingsafe()` 由实验性提升为稳定、将若干流元数据符号提升为稳定，且 26.07 相对 25.11 无破坏兼容性的 ABI 变更（[DPDK Release 26.07](https://doc.dpdk.org/guides/rel_notes/release_26_07.html)）。社区月报显示 26.07 的 Release Candidate 1 于 2026 年 6 月 11 日发布，包含 432 个补丁，面向性能、虚拟化、内存与 RISC-V 改进，最终发布目标为 7 月 16 日；同时 25.11.1 维护版本已发布（[DPDK July 2026](https://www.dpdk.org/2026/07/)）。路线图显示下一版 26.11（2026 年 11 月）的关键节点为 8 月 31 日 RFC/v1 提案截止、10 月 2 日 rc1（API 冻结）、10 月 23 日 rc2（PMD 特性冻结）、10 月 30 日 rc3（内置应用特性冻结）（[DPDK Roadmap](https://core.dpdk.org/roadmap/#dates)）。

**io_uring**：作为统一存储、网络与系统调用的内核 I/O 接口，io_uring 支持完全异步执行与批量提交/完成，以摊销系统调用开销与上下文切换（[io_uring for High-Performance DBMSs](https://arxiv.org/html/2512.04859v1)）。据 2026 年的生产规模评估，Oracle Database 26ai 在混合 OLTP（TPC-C）负载下 io_uring 吞吐持平但服务器 CPU 使用率降低 1.2 个百分点；分析查询（TPC-H）每查询 CPU 下降 8.5%（几何平均）；单独隔离写路径可降低约 29%（[io_uring in Oracle Database](https://arxiv.org/pdf/2609.22781)）。与网络零拷贝相关的 `IORING_OP_RECV_ZC` 自 Linux 6.0 引入，到 2026 年已趋成熟（[io_uring без розовых очков](https://habr.com/ru/articles/1039820/)）；Oracle UEK 8（6.12 内核）则引入 `IORING_OP_SENDZC` 以执行零拷贝写（[UEK 8 Release Notes](https://docs.oracle.com/cd/F10276_01/8/relnotes8.0/UEK-RELNOTES-8-0.pdf)）。

**实时媒体**：WebRTC 直播实现约 0.5 秒的端到端（glass-to-glass）延迟，而基于 HTTP 的协议在同等流下延迟达 8 秒级（[What is WebRTC Video Streaming](https://antmedia.io/webrtc-video-streaming/)）。WHIP/WHEP 的 RFC 9725 已定稿，经 SFU 的端到端延迟在 200–500 ms（[WHIP и WHEP](https://blog.fora-soft.ru/post/whip-i-whep-zamena-rtmp-v-vashem-steke-striminga-2026)）。

## 核心技术与关键概念

**内核旁路与用户态网络**：内核旁路网络（DPDK、Solarflare OpenOnload、ef_vi）将网络包直接送达用户态应用而不经过 OS 内核，消除系统调用开销、上下文切换与中断处理抖动；对交易负载而言，可将网络延迟从微秒级降到纳秒级，并消除由内核调度与中断合并导致的尾延迟尖峰（[IT Infrastructure Consulting — kernel bypass](https://microversesystems.com/consulting)）。AMD Solarflare 加速栈包含 Onload（透明 socket 加速）、ef_vi（最低延迟的原始二层 API）与 TCPDirect，涉及自旋、中断处理、NUMA/IRQ 亲和性等调优项以及各型号适配器的延迟测试结果（[Reference Summaries: Networking, NICs & Kernel Bypass](https://lowlatencysystem.com/summaries/networking/)）。

**AF_XDP / XDP**：AF_XDP 地址族下的特殊 socket（XSK）配合 XDP 程序可实现完全或部分内核旁路；它结合 XDP 的 `XDP_REDIRECT` 判决，把数据包直接投递到用户态内存区（UMEM），是 eBPF 生态对 DPDK 内核旁路模型的回应（[AF_XDP](https://docs.ebpf.io/linux/concepts/af_xdp/)、[Linux eBPF & XDP Networking Primer](https://baud9600.com/lt/pages/articles/ebpf-xdp-networking/)）。学术界进一步提出 FLASH（Fast Linked AF_XDP Sockets）以优化高性能网络功能链（[FLASH](https://dl.acm.org/doi/pdf/10.1145/3772052.3772258?download=true)）。DTU 侧还有厂商在 DPDK 的 ICE poll mode driver 中提供 `rx_low_latency=1` 参数，将 Rx 中断延迟降低到 **2 µs**，服务 vRAN 前传（[ICE Poll Mode Driver](https://doc.dpdk.org/guides/nics/ice.html)）。

**硬件卸载（FPGA/ASIC）**：为达到亚微秒级，工程师使用 FPGA：与按指令序列执行的 CPU 不同，FPGA 是可被「布线」以在硬件层面并行执行特定交易逻辑的空白硅片；当行情数据进入 FPGA 系统时无需等待 CPU 中断，硅逻辑直接解析数据包、执行策略并在纳秒内生成订单响应（[The Nanosecond Edge](https://marketclutch.com/the-nanosecond-edge-architectural-foundations-of-sub-microsecond-trading-systems/)）。

**介质与拓扑**：除协议栈外，传输介质影响显著——光在标准光纤中比在空气中慢约 31%，因此空芯光纤（HCF）被用于缩短传播时延（[High Frequency Trading Platforms: Architecture, Speed & Infrastructure — 2026](https://www.quantvps.com/blog/high-frequency-trading-platform)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **DPDK**：Linux Foundation 托管的用户态数据面开发套件，覆盖 NIC 轮询模式驱动与低延迟选项（[DPDK](https://doc.dpdk.org/guides/rel_notes/release_26_07.html)）。
- **AMD Solarflare（Onload / ef_vi / TCPDirect）**：商用低延迟网络加速栈（[Reference Summaries](https://lowlatencysystem.com/summaries/networking/)）。
- **AF_XDP / eBPF**：Linux 内核内建的内核旁路与可编程数据面方案（[docs.ebpf.io](https://docs.ebpf.io/linux/concepts/af_xdp/)）。
- **io_uring**：Linux 异步 I/O 框架，被 Oracle Database 等生产系统采用（[io_uring in Oracle Database](https://arxiv.org/pdf/2609.22781)）。
- **WebRTC / WHIP / WHEP**：实时音视频传输标准，WHIP/WHEP RFC 9725 已定稿（[WHIP и WHEP](https://blog.fora-soft.ru/post/whip-i-whep-zamena-rtmp-v-vashem-steke-striminga-2026)）。

## 关键数据与评测结果（附来源）

- **NIC 延迟对照**：标准网卡因 OS 开销引入 20–50 µs 延迟；DPDK 与 Solarflare OpenOnload 通过旁路 OS、将 NIC 内存直接映射到应用，把延迟降至 **1–5 µs**（[High Frequency Trading Platforms: Architecture, Speed & Infrastructure — 2026](https://www.quantvps.com/blog/high-frequency-trading-platform)）。
- **内核旁路收益**：有来源称内核旁路可将网络传输延迟降至 **低于 1.0 µs**，并消除 OS 抖动（[High-Frequency Trading latency setups](https://alphatradecircle.com/blog/high-frequency-trading-setups)）。
- **DPDK 低延迟模式**：ICE PMD 的 `rx_low_latency` 可将 Rx 中断延迟降至 2 µs（[ICE Poll Mode Driver](https://doc.dpdk.org/guides/nics/ice.html)）。
- **io_uring 生产数据**：TPC-C 吞吐持平、服务器 CPU −1.2pp；TPC-H 每查询 CPU（几何平均）−8.5%；写路径 −29%（[io_uring in Oracle Database](https://arxiv.org/pdf/2609.22781)）。
- **实时媒体延迟分级**：WebRTC <300 ms（交互场景）；WHIP→SFU→WHEP 200–500 ms；RTMP 3–5 s；HLS 6–30 s；LL-HLS 约 2 秒级（[WebRTC Live Streaming（2026）](https://trtc.io/blog/details/webrtc-live-streaming-sports-2026)、[Low-Latency Streaming: WebRTC vs LL-HLS](https://revidd.com/blog/low-latency-streaming-webrtc-vs-ll-hls)、[WHIP и WHEP](https://blog.fora-soft.ru/post/whip-i-whep-zamena-rtmp-v-vashem-steke-striminga-2026)）。

上述延迟数字来自不同厂商/博客与场景，测量口径（端到端、单向、硬件配置）并不统一，仅作量级参考。

## 趋势与争议

**趋势**：一是「可编程内核旁路」——AF_XDP / eBPF 让「Darwin 式」的完全旁路与内核网络栈之间出现可编程的中间态，成为 DPDK 之外的选择（[AF_XDP](https://docs.ebpf.io/linux/concepts/af_xdp/)）；二是「异步 I/O 复兴」——io_uring 的零拷贝与批量能力在数据库等存储密集型系统获得实测收益（[io_uring in Oracle Database](https://arxiv.org/pdf/2609.22781)）；三是「实时媒体的低延迟分层」——WebRTC/WHIP 负责交互级，LL-HLS 负责大规模型（[Low-Latency Streaming](https://revidd.com/blog/low-latency-streaming-webrtc-vs-ll-hls)）。

**争议与取舍**：其一，绝对延迟 vs 系统复杂度——FPGA/ASIC 可进入亚微秒甚至纳秒级，但开发与维护成本高、迭代慢，软件方案（DPDK/OpenOnload）更易维护（[The Nanosecond Edge](https://marketclutch.com/the-nanosecond-edge-architectural-foundations-of-sub-microsecond-trading-systems/)）。其二，DPDK vs AF_XDP——后者集成于内核、可编程性好，但完全旁路能力与成熟度、生态（如 PMD 覆盖）仍以 DPDK 为强项。其三，实时音视频中 WebRTC 延迟最低但规模化成本高（单台服务器可承载数百观众量级），LL-HLS 易扩展但延迟在 2 秒级，多数运营方采用混合架构（[Low-Latency Streaming](https://revidd.com/blog/low-latency-streaming-webrtc-vs-ll-hls)）。其四，延迟数据高度依赖测量口径，跨来源比较需谨慎。

## 参考来源

- [DPDK Release 26.07](https://doc.dpdk.org/guides/rel_notes/release_26_07.html)
- [DPDK July 2026](https://www.dpdk.org/2026/07/)
- [DPDK Roadmap](https://core.dpdk.org/roadmap/#dates)
- [DPDK Release 26.03](https://doc.dpdk.org/guides/rel_notes/release_26_03.html)
- [DPDK ICE Poll Mode Driver](https://doc.dpdk.org/guides/nics/ice.html)
- [IT Infrastructure Consulting — kernel bypass networking](https://microversesystems.com/consulting)
- [Reference Summaries: Networking, NICs & Kernel Bypass](https://lowlatencysystem.com/summaries/networking/)
- [High-Frequency Trading latency setups](https://alphatradecircle.com/blog/high-frequency-trading-setups)
- [The Nanosecond Edge: Architectural Foundations of Sub-Microsecond Trading Systems](https://marketclutch.com/the-nanosecond-edge-architectural-foundations-of-sub-microsecond-trading-systems/)
- [High Frequency Trading Platforms: Architecture, Speed & Infrastructure Explained (2026)](https://www.quantvps.com/blog/high-frequency-trading-platform)
- [AF_XDP](https://docs.ebpf.io/linux/concepts/af_xdp/)
- [eBPF and XDP Technologies as Enablers for Ultra-Fast and Programmable Next-Gen Network Infrastructures](https://zenodo.org/records/17182690/files/eBPF%20and%20XDP%20technologies%20as%20enablers.pdf?download=1)
- [Linux eBPF & XDP Networking Primer](https://baud9600.com/lt/pages/articles/ebpf-xdp-networking/)
- [FLASH: Fast Linked AF_XDP Sockets](https://dl.acm.org/doi/pdf/10.1145/3772052.3772258?download=true)
- [io_uring in Oracle Database](https://arxiv.org/pdf/2609.22781)
- [io_uring for High-Performance DBMSs](https://arxiv.org/html/2512.04859v1)
- [Oracle UEK 8 Release Notes](https://docs.oracle.com/cd/F10276_01/8/relnotes8.0/UEK-RELNOTES-8-0.pdf)
- [io_uring без розовых очков](https://habr.com/ru/articles/1039820/)
- [What is WebRTC Video Streaming](https://antmedia.io/webrtc-video-streaming/)
- [WebRTC Live Streaming: Real-Time Sports Broadcasting (2026)](https://trtc.io/blog/details/webrtc-live-streaming-sports-2026)
- [Low-Latency Streaming: WebRTC vs LL-HLS](https://revidd.com/blog/low-latency-streaming-webrtc-vs-ll-hls)
- [WHIP и WHEP: замена RTMP (2026)](https://blog.fora-soft.ru/post/whip-i-whep-zamena-rtmp-v-vashem-steke-striminga-2026)