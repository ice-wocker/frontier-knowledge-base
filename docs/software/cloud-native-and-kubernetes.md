# 云原生与 Kubernetes

> 最后更新：2026-09-26 ｜ 领域：云原生与 Kubernetes ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

云原生（Cloud Native）已从前沿概念演变为企业基础设施的默认范式。根据 CNCF 于 2026 年 1 月 20 日发布的《CNCF Annual Cloud Native Survey》，98% 的受访组织已采用云原生技术，82% 的容器用户在生产环境运行 Kubernetes，较 2023 年的 66% 显著提升，报告称 Kubernetes 已成为「AI 的事实操作系统」（[Kubernetes Established as the De Facto 'Operating System' for AI as Production Use Hits 82% in 2025](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)）。这一轮增长的核心驱动力是 AI 推理负载与平台工程实践的普及：66% 承载生成式 AI 模型的组织使用 Kubernetes 管理部分或全部推理工作负载（[Kubernetes Fuels AI Growth; Organizational Culture Remains the Decisive Factor](https://www.cncf.io/blog/2026/01/20/kubernetes-fuels-ai-growth-organizational-culture-remains-the-decisive-factor/)）。

## 2025–2026 最新进展

### 1. Kubernetes 版本节奏与最新发布

Kubernetes 保持每年约 3 个 minor 版本、约 15 周一个版本的发布节奏，官方仅维护最近三个 minor 版本（当前为 1.37、1.36、1.35），每个版本提供约 1 年的补丁支持（[Releases](https://kubernetes.io/releases/)）。截至 2026-09-26：

- **1.37.0**（2026-08-26 发布，EOL 2027-10-28）为当前最新版本，其主题聚焦 DRA（Dynamic Resource Allocation）能力升级（[Kubernetes v1.37: DRA Updates](https://kubernetes.io/blog/2026/09/03/kubernetes-v1-37-dra-updates/)）。
- **1.36.4**（2026-08-11）、**1.35.8**（2026-08-11）、**1.34.11**（2026-08-11）为各版本线最新补丁；1.34 的 EOL 为 2026-10-27，1.33 已于 2026-06-28 结束生命周期（[Releases](https://kubernetes.io/releases/)）。
- **1.35** 代号「Timbernetes（世界树版本）」，为 cloud-controller-manager 路由控制器引入基于 watch 的事件驱动调谐，显著降低云厂商 API 调用（[Kubernetes v1.35: Timbernetes](https://kubernetes.io/zh-cn/blog/2025/12/17/kubernetes-v1-35-release/)）。
- **1.34** 代号「Of Wind & Will」，通过 DRA consumable capacity 支持更细粒度的设备共享（[Kubernetes v1.34: DRA Consumable Capacity](https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/)）。

需要特别注意的是，**Ingress-NGINX 已于 2026 年 3 月正式停止维护**，社区建议迁移到 Gateway API 或更换其它 Ingress 控制器（[Before You Migrate: Five Surprising Ingress-NGINX Behaviors You Need to Know](https://kubernetes.io/blog/2026/02/27/ingress-nginx-before-you-migrate/)）。官方同步推出迁移工具 **ingress2gateway 1.0**（[Announcing Ingress2Gateway 1.0: Your Path to Gateway API](https://kubernetes.io/blog/2026/03/20/ingress2gateway-1-0-release/)）。

### 2. Gateway API 快速成熟

Gateway API 自 2023 年 v1.0 GA 后进入高频演进：v1.4.0 于 2025-10-06 GA，将 BackendTLSPolicy 等三项特性纳入 Standard 通道（[Gateway API 1.4: New Features](https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/)）；v1.5 于 2026-02-27 发布，集中将实验性特性迁移到稳定版（[Gateway API v1.5: Moving features to Stable](https://kubernetes.io/blog/2026/04/21/gateway-api-v1-5/)）；v1.6.0 进一步让 TCPRoute 与 UDPRoute 在 `v1` 版本达到 GA，并将实验性资源迁移到独立的 `gateway.networking.x-k8s.io` API 组（[Gateway API v1.6:TCPRoute 和 UDPRoute 进阶为标准版](https://kubernetes.io/zh-cn/blog/2026/08/03/gateway-api-v1-6-release/)）。Gateway API 通过 Gateway（集群运维职责）与 HTTPRoute（应用开发职责）的职责分离，替代了 Ingress 的耦合模型，天然适配多租户与 RBAC（[A Welcome Guide for Ingress-NGINX Users](https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress-nginx/)）。

### 3. Service Mesh：Sidecar 退场，Ambient 与 eBPF 上位

**Istio ambient 模式** 以「拆分代理」架构取代每 Pod sidecar：`ztunnel` 是每节点一个的 L4 代理，负责 mTLS 隧道与身份验证；`waypoint` 是按命名空间/服务账号按需启用的 Envoy 代理，仅承载 L7 能力（[Istio Ambient Overview](https://istio.io/latest/docs/ambient/overview/)）。官方文档将 ambient 定位为可与 sidecar 模式混用的生产就绪模式，且自 Istio 1.22 起即为生产就绪（[Sidecar or ambient?](https://istio.io/latest/docs/overview/dataplane-modes/)）。Istio 1.29 带来 ambient multi-network multicluster 的 Beta 支持（[Istio Blog](https://istio.io/latest/blog/)），并于 2026 年 5 月引入统一的 TrafficExtension API 以支持 Wasm 与 Lua 扩展（[Istio Blog](https://istio.io/latest/blog/)）。

**Cilium** 则基于 eBPF 在内核态实现数据面，L4 的 TCP/mTLS 甚至无需代理，L7 按需嵌入 Envoy。其版本节奏密集：1.18 扩大 IPv6 支持并引入加密 overlay；1.19（2026-02-24）强化网络策略、将 Multi Pool IPAM 转为 stable；1.20（2026-07-31）继续推进 IPv6（[Cilium Blog — Release](https://cilium.io/blog/categories/release/)）。在 KubeCon EU 2026 上，Cilium 展示了无 sidecar 的原生 mTLS，以每节点 eBPF 程序替代每 Pod 约 50–100 MB 的 Envoy 代理（[eBPF in Kubernetes 2026: From Kernel Feature to Standard Infrastructure](https://dev.to/saaro_net/ebpf-in-kubernetes-2026-from-kernel-feature-to-standard-infrastructure-5cj9)）。

### 4. KubeVirt 与 Wasm

**KubeVirt** 让虚拟机成为 Kubernetes 原生工作负载。v1.8（2026 年 3 月发布，对齐 Kubernetes v1.35）引入**虚拟机管理程序抽象层（HAL）**，使项目可使用 KVM 之外的后端，并加入机密计算能力（[KubeVirt v1.8 Brings Multi-Hypervisor Support and Confidential Computing to Kubernetes](https://www.infoq.com/news/2026/03/kubevirt-18-announcement/)）；v1.9 于 2026-07-22 发布，面向 Kubernetes v1.36 构建（[KubeVirt release notes](https://kubevirt.io/user-guide/release_notes/)）。

**WebAssembly on Kubernetes** 的代表是 **SpinKube**，它组合 Spin operator、containerd shim Spin 与 runtime class manager，由 Microsoft、SUSE、Liquid Reply、Fermyon 共同贡献，使 Wasm 工作负载可原生运行于 Kubernetes 节点（[SpinKube](https://www.spinkube.dev/)）。

### 5. GitOps、多集群与平台工程

GitOps 双雄 **Argo** 与 **Flux** 均为 CNCF 毕业项目（Argo 于 2022-12-06 毕业，Flux 于 2022-11-30 毕业），Argo 正推进 Argo CD 3.5，Flux 已发布 2.9 GA 并原生支持 Helm v4（[Argo](https://www.cncf.io/projects/argo/)、[Flux at KubeCon EU 2026](https://fluxcd.io/kubecon/)、[Flux](https://www.cncf.io/projects/flux/)）。多集群编排项目 **Karmada** 于 2026-09-03 从 CNCF 毕业（2026-09-07 正式公告），拥有 1214 名贡献者、292 家组织，用于跨集群 AI 训练与 GPU 调度（[Cloud Native Computing Foundation Announces Karmada Graduation](https://www.cncf.io/announcements/2026/09/07/cloud-native-computing-foundation-announces-karmada-graduation/)、[Karmada 正式从 CNCF 毕业](https://www.infoq.cn/article/yfQdTa8cRxjJB0rzZMJR)）。平台工程方面，**Backstage** 是 CNCF 孵化项目、按项目活跃度排名第 5，并在 v1.54 引入 `AiResource` 目录实体类型以纳入 AI 资源（[Backstage](https://www.cncf.io/projects/backstage/)、[Backstage 2026: From Service Catalog to AI Hub for Developer Portals](https://dev.to/saaro_net/backstage-2026-from-service-catalog-to-ai-hub-for-developer-portals-4dn)）。

### 6. Serverless 与 FinOps

Serverless 领域，**Knative** 于 2025-09-11 从 CNCF 毕业，最新版本为 1.22，包含 Serving、Eventing、Functions 三大组件（[Knative](https://www.cncf.io/projects/knative/)、[v1.22 release](https://knative.dev/blog/releases/announcing-knative-v1-22-release/)）。自托管方案 **OpenFaaS** 以 Kubernetes 为推荐平台，2026 年 2 月发布 Gateway API 迁移指南，4 月推出 Python SDK（[OpenFaaS](https://www.openfaas.com/)、[How to Migrate OpenFaaS to Gateway API](https://www.openfaas.com/blog/gateway-api-migration/)）。

FinOps 方面，CNCF 孵化项目 **OpenCost** 提供厂商中立的 Kubernetes 成本分配，1.121.0 版本首次支持 LLM 推理成本追踪（[OpenCost 1.121.0: First-of-a-Kind Kubernetes Inference Cost Tracking](https://opencost.io/blog/opencost-llmd-inference-cost/)）；Kubecost 与 OpenCost 是成本管理与分摊的主流选择（[Kubernetes FinOps: Build Cost Ownership Into Engineering](https://cast.ai/blog/kubernetes-finops/)）。

## 核心技术与关键概念

- **DRA（Dynamic Resource Allocation）**：按属性申请设备、自定义配置与设备共享。1.34 引入 consumable capacity；1.36 对 ResourceClaim 状态更新实施细粒度授权（beta，默认开启）；1.37 将 DRA Extended Resource 支持推进到 GA（[Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)、[Kubernetes v1.37: DRA Updates](https://kubernetes.io/blog/2026/09/03/kubernetes-v1-37-dra-updates/)）。
- **Gateway API**：角色化的 L4/L7 流量入口 API，Standard 与 Experimental 两个发布通道并行（[Versioning](https://gateway-api.sigs.k8s.io/docs/concepts/versioning/)）。
- **Ambient Service Mesh**：以 ztunnel + waypoint 的拆分代理消除 sidecar 资源开销。
- **eBPF**：在 Linux 内核中运行沙盒程序，实现高性能网络、安全与可观测性的数据面。
- **Wasm**：以组件模型规范为标准的轻量运行时，适合边缘、插件与 Serverless。
- **GitOps、FinOps、IDP**：分别对应交付、成本与开发者体验的工程化实践。

## 代表性项目/框架

| 项目 | 类别 | 官方链接 |
|---|---|---|
| Kubernetes | 容器编排 | https://kubernetes.io/ |
| Istio | Service Mesh | https://istio.io/ |
| Cilium | eBPF 网络/安全 | https://cilium.io/ |
| Gateway API | 流量入口 | https://gateway-api.sigs.k8s.io/ |
| KubeVirt | 虚拟机编排 | https://kubevirt.io/ |
| Argo / Flux | GitOps | https://argo-cd.readthedocs.io/、https://fluxcd.io/ |
| Karmada | 多集群编排 | https://karmada.io/ |
| Knative | Serverless | https://knative.dev/ |
| OpenFaaS | Serverless | https://www.openfaas.com/ |
| SpinKube | Wasm | https://www.spinkube.dev/ |
| OpenCost | FinOps | https://opencost.io/ |
| Backstage | IDP | https://backstage.io/ |

## 版本与生态数据

| 指标 | 数据 | 来源 |
|---|---|---|
| Kubernetes 最新版本 | 1.37.0（2026-08-26） | kubernetes.io/releases |
| 维护窗口 | 最近 3 个 minor（1.37/1.36/1.35），约 1 年补丁支持 | kubernetes.io/releases |
| 生产环境 K8s 使用率 | 82%（2023 年为 66%） | CNCF Annual Survey 2025 |
| 组织云原生化程度 | 59% 表示「大部分或几乎全部」 | CNCF Annual Survey 2025 |
| AI 推理使用 K8s | 66% 承载生成式 AI 模型的组织 | CNCF Annual Survey 2025 |
| GitOps 使用差距 | 创新者 58% vs 采纳者 23% | CNCF Annual Survey 2025 |
| OpenTelemetry 贡献者 | 24,000+ | CNCF Annual Survey 2025 |
| Karmada 社区规模 | 1214 名贡献者、292 家组织 | InfoQ |

## 趋势与争议

1. **文化挑战取代技术复杂度成为首要障碍**：2025 年调研中，「开发团队的文化变革」首次成为云原生采用的首要挑战（47%），而培训（36%）、安全（36%）、复杂度（34%）的排名均下降（[Kubernetes Established as the De Facto 'Operating System' for AI](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)）。
2. **AI 工作负载成为新增长点**：Kubernetes 正被定位为 AI 推理平台，但 AI 生产成熟度仍处早期——仅 7% 组织每天部署模型，44% 尚未在 K8s 上运行 AI/ML 负载。
3. **Sidecar 与 eBPF 的路线之争**：ambient mesh 与 Cilium 的「无 sidecar、内核态数据面」方案在资源效率上具备优势，但也带来内核依赖与调试复杂性的权衡。
4. **Ingress 退场引发的迁移压力**：Ingress-NGINX 停止维护迫使大量存量集群迁移至 Gateway API 或替代控制器，迁移过程中存在默认行为差异导致的风险。

## 参考来源

1. [Releases — Kubernetes](https://kubernetes.io/releases/)
2. [Kubernetes v1.37: DRA Updates](https://kubernetes.io/blog/2026/09/03/kubernetes-v1-37-dra-updates/)
3. [Kubernetes v1.35: Timbernetes（世界树版本）](https://kubernetes.io/zh-cn/blog/2025/12/17/kubernetes-v1-35-release/)
4. [Kubernetes v1.34: DRA Consumable Capacity](https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/)
5. [Dynamic Resource Allocation — Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
6. [Before You Migrate: Five Surprising Ingress-NGINX Behaviors You Need to Know](https://kubernetes.io/blog/2026/02/27/ingress-nginx-before-you-migrate/)
7. [Announcing Ingress2Gateway 1.0: Your Path to Gateway API](https://kubernetes.io/blog/2026/03/20/ingress2gateway-1-0-release/)
8. [Gateway API 1.4: New Features](https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/)
9. [Gateway API v1.5: Moving features to Stable](https://kubernetes.io/blog/2026/04/21/gateway-api-v1-5/)
10. [Gateway API v1.6:TCPRoute 和 UDPRoute 进阶为标准版](https://kubernetes.io/zh-cn/blog/2026/08/03/gateway-api-v1-6-release/)
11. [Versioning — Gateway API](https://gateway-api.sigs.k8s.io/docs/concepts/versioning/)
12. [A Welcome Guide for Ingress-NGINX Users](https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress-nginx/)
13. [Istio Ambient Overview](https://istio.io/latest/docs/ambient/overview/)
14. [Sidecar or ambient? — Istio](https://istio.io/latest/docs/overview/dataplane-modes/)
15. [Istio Blog](https://istio.io/latest/blog/)
16. [Cilium Blog — Release](https://cilium.io/blog/categories/release/)
17. [eBPF in Kubernetes 2026: From Kernel Feature to Standard Infrastructure](https://dev.to/saaro_net/ebpf-in-kubernetes-2026-from-kernel-feature-to-standard-infrastructure-5cj9)
18. [KubeVirt v1.8 Brings Multi-Hypervisor Support and Confidential Computing to Kubernetes](https://www.infoq.com/news/2026/03/kubevirt-18-announcement/)
19. [KubeVirt release notes](https://kubevirt.io/user-guide/release_notes/)
20. [SpinKube](https://www.spinkube.dev/)
21. [Argo — CNCF](https://www.cncf.io/projects/argo/)
22. [Flux — CNCF](https://www.cncf.io/projects/flux/)
23. [Flux at KubeCon EU 2026](https://fluxcd.io/kubecon/)
24. [Cloud Native Computing Foundation Announces Karmada Graduation](https://www.cncf.io/announcements/2026/09/07/cloud-native-computing-foundation-announces-karmada-graduation/)
25. [Karmada 正式从 CNCF 毕业，已用于多集群 AI 训练与 GPU 调度](https://www.infoq.cn/article/yfQdTa8cRxjJB0rzZMJR)
26. [Backstage — CNCF](https://www.cncf.io/projects/backstage/)
27. [Backstage 2026: From Service Catalog to AI Hub for Developer Portals](https://dev.to/saaro_net/backstage-2026-from-service-catalog-to-ai-hub-for-developer-portals-4dn)
28. [Knative — CNCF](https://www.cncf.io/projects/knative/)
29. [v1.22 release — Knative](https://knative.dev/blog/releases/announcing-knative-v1-22-release/)
30. [OpenFaaS](https://www.openfaas.com/)
31. [How to Migrate OpenFaaS to Gateway API](https://www.openfaas.com/blog/gateway-api-migration/)
32. [OpenCost 1.121.0: First-of-a-Kind Kubernetes Inference Cost Tracking](https://opencost.io/blog/opencost-llmd-inference-cost/)
33. [Kubernetes FinOps: Build Cost Ownership Into Engineering](https://cast.ai/blog/kubernetes-finops/)
34. [Kubernetes Established as the De Facto 'Operating System' for AI as Production Use Hits 82% in 2025 CNCF Annual Cloud Native Survey](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)
35. [Kubernetes Fuels AI Growth; Organizational Culture Remains the Decisive Factor](https://www.cncf.io/blog/2026/01/20/kubernetes-fuels-ai-growth-organizational-culture-remains-the-decisive-factor/)