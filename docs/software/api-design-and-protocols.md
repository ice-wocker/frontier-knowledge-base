# API 设计与协议

> 最后更新：2026-09-26 ｜ 领域：软件·架构与 API ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

API 设计决定系统对外与对内的契约形态。主流风格包括面向资源的 REST、面向查询图的 GraphQL、面向高性能内部调用的 gRPC、面向 TypeScript 全栈的 tRPC，以及面向实时场景的 WebSocket/SSE。2025–2026 年的关键动态包括：OpenAPI 规范发布 3.2 并持续迭代、GraphQL 联邦（federation）成为大规模平台首选、AI 流式输出推动 SSE 普及，以及 API 安全风险（尤其对象级授权与业务流滥用）受到持续关注。

## 最新进展（2025–2026）

### OpenAPI 3.2 与 4.0 路线

OpenAPI Initiative 于 2025 年 9 月 23 日发布 v3.2.0，新增了 HTTP 方法支持、全新的 tag 结构、流式媒体类型支持等特性（[Announcing OpenAPI v3.2](https://www.openapis.org/blog/2025/09/23/announcing-openapi-v3-2)）。规范站点显示 3.2 的迭代版本已推进至 3.2.1（2026 年 9 月 10 日）（[OpenAPI Specification v3.2.1](https://spec.openapis.org/oas/latest)）。官方通讯进一步提到 3.2 的安全增强，包括对 Device Authorization Flow 的支持、用于标识 OAuth 2.0 Server Metadata 的新属性，以及弃用部分 OAuth2 方案；下一代版本 4（代号 Moonwalk）也在持续演进（[OpenAPI Initiative newsletter](https://www.openapis.org/tag/newsletter)）。

### GraphQL 联邦与规模采纳

Apollo 引用 Gartner 研究称，预计到 2028 年将有 60% 的企业在生产中使用 GraphQL，而 2026 年这一比例不足 40%；同时指出 schema federation 已成为大规模、动态且 AI 集成平台的首选方案，取代 schema stitching（[Apollo GraphQL Recognized in 2026 Gartner Peer Insights](https://www.apollographql.com/newsroom/press-releases/apollo-graphql-recognized-for-first-time-in-2026-gartnerr-peer-insightstm-voice-o)）。Apollo 的发布生命周期文档显示 Router v2.10 搭配 Federation v2.12 自 2025 年 12 月起成为 LTS，维护窗口至 2026 年 9 月（[GraphOS Runtime Release Lifecycle](https://www.apollographql.com/docs/graphos/resources/runtime-release-lifecycle)）。

### 实时传输：SSE 借 AI 流式重新走红

对比资料指出，SSE 基于标准 HTTP、单向服务端推送、浏览器内置自动重连，适合 AI 流式输出、实时订阅与通知；WebSocket 是独立的双向协议，适合聊天、游戏与协同编辑（[Server-Sent Events vs WebSockets in 2026](https://blog.codercops.com/blog/server-sent-events-vs-websockets-2026/)；[Streaming APIs: SSE and WebSocket Patterns 2026](https://apiscout.dev/guides/streaming-apis-sse-websocket-2026)）。从资源开销看，一条 SSE 连接约占 2–5 KiB 服务端状态，而 WebSocket 常达 50 KiB 以上，因其需维护帧缓冲、掩码状态与 ping/pong（[WebSocket vs. Server-Sent Events](https://getstream.io/blog/websocket-sse/)）。Vercel 的分析同样强调：客户端上行与下行速率相当才选 WebSocket，否则优先 SSE 搭配 HTTP（[WebSocket vs Server-Sent Events](https://vercel.com/i/websocket-vs-server-sent-events)）。

## 核心技术与关键概念

- **REST**：以名词建模领域资源，用 HTTP 动词操作；是所有 HTTP 客户端都支持的事实标准，适合公开 API 与外部集成（[API Architecture Guide for 2026](https://kanopylabs.com/blog/grpc-vs-rest-vs-graphql-api-architecture)）。
- **GraphQL**：解决过度获取与获取不足，单一端点 + 强 schema，适合多客户端、数据需求可变的场景（[Beginner's Guide to APIs in 2026](https://nirajiitr.com/blog/apis-2026-rest-vs-graphql-vs-grpc-use-cases)）。
- **gRPC**：基于 HTTP/2 与二进制序列化，支持原生流式；资料普遍称其在高频内部通信场景比 REST 快 5–10 倍，但需更多工具且非浏览器原生（[REST vs GraphQL vs gRPC](https://precisionaiacademy.com/blog/api-design-patterns-2026)）。
- **tRPC**：面向 TypeScript 全栈，类型端到端安全、学习曲线低，但仅限 TypeScript 生态（[REST vs GraphQL vs gRPC vs tRPC: API Architecture 2026](https://apiscout.dev/guides/rest-vs-graphql-vs-grpc-vs-trpc-2026)）。
- **实时协议**：WebSocket（双向、有状态、单条消息开销低）、SSE（单向、HTTP 原生、自动重连）、长轮询与分块传输（[Server-Sent Events vs WebSockets in 2026](https://blog.codercops.com/blog/server-sent-events-vs-websockets-2026/)）。
- **API 网关**：限流应放在网关（如 AWS API Gateway、Kong、nginx）而非应用内；网关统一处理认证、限流与 schema 校验（[API Design Patterns 2026](https://precisionaiacademy.com/blog/api-design-patterns-2026)）。
- **版本化与契约**：用 OpenAPI 描述 REST 契约可自动生成 SDK 与 mock 服务；GraphQL 侧则以联邦 schema 做跨团队组合（[API Design Patterns 2026](https://precisionaiacademy.com/blog/api-design-patterns-2026)）。

## 代表性项目 / 组织 / 产品

- **OpenAPI Initiative**：维护 OpenAPI Specification 的行业组织（[OpenAPI Initiative](https://www.openapis.org/tag/api)）。
- **Apollo GraphQL / GraphOS**：GraphQL 联邦与路由平台，Router v2.x 持续演进（[Apollo GraphOS](https://apollostack.com)）。
- **OWASP API Security Project**：API 安全风险清单与测试框架的制定方（[OWASP API Security Testing Framework](https://owasp.org/www-project-api-security-testing-framework/)）。

## 关键数据与评测结果

- **性能量级**：多份资料称 gRPC 在高吞吐场景比 REST 快 5–10 倍（[API Design Patterns 2026](https://precisionaiacademy.com/blog/api-design-patterns-2026)）。
- **连接开销**：SSE 每连接约 2–5 KiB，WebSocket 约 50 KiB 或更多（[WebSocket vs. Server-Sent Events](https://getstream.io/blog/websocket-sse/)）。
- **GraphQL 采纳预测**：Gartner 预计 2028 年 60% 企业生产使用 GraphQL，2026 年不足 40%（[Apollo 2026 Gartner Peer Insights](https://www.apollographql.com/newsroom/press-releases/apollo-graphql-recognized-for-first-time-in-2026-gartnerr-peer-insightstm-voice-o)）。

## 趋势与争议

- **安全风险居高不下**：OWASP API Security Top 10（2023）中，API1 为对象级授权失效（BOLA）、API5 为功能级授权失效、API6 为对敏感业务流的无限制访问（[OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)）。云原生安全视角强调，网关/WAF/WAAP 能在边缘实施认证、限流与 schema 校验，但它们「必要而不充分」——WAF 并不知道调用者是否拥有对象 124（[OWASP API Security Top 10: A Cloud-Native Guide](https://orca.security/resources/blog/owasp-api-security-top-10/)）。
- **风格选择之争**：主流共识是「没有最好，只有最适合每层」，同一系统可在公开层用 REST、BFF 层用 GraphQL、内部层用 gRPC（[API Architecture Guide for 2026](https://kanopylabs.com/blog/grpc-vs-rest-vs-graphql-api-architecture)）。
- **AI 时代 API 的角色**：OpenAPI 官方社区开始讨论「在 AI 时代 OpenAPI 是否仍然重要」，反映 API 契约与 AI 工具调用（工具描述/函数调用）正在融合（[OpenAPI Initiative api 标签](https://www.openapis.org/tag/api)）。

## 参考来源

- [Announcing OpenAPI v3.2](https://www.openapis.org/blog/2025/09/23/announcing-openapi-v3-2)
- [OpenAPI Specification v3.2.1（spec.openapis.org）](https://spec.openapis.org/oas/latest)
- [OpenAPI Specification（版本迭代页）](https://spec.openapis.org/oas/)
- [OpenAPI Initiative newsletter](https://www.openapis.org/tag/newsletter)
- [OpenAPI Initiative — api 标签](https://www.openapis.org/tag/api)
- [Apollo GraphQL Recognized in 2026 Gartner Peer Insights Voice of the Customer](https://www.apollographql.com/newsroom/press-releases/apollo-graphql-recognized-for-first-time-in-2026-gartnerr-peer-insightstm-voice-o)
- [Apollo GraphOS Runtime Release Lifecycle](https://www.apollographql.com/docs/graphos/resources/runtime-release-lifecycle)
- [Apollo GraphQL — 平台介绍](https://apollostack.com)
- [Server-Sent Events vs WebSockets in 2026](https://blog.codercops.com/blog/server-sent-events-vs-websockets-2026/)
- [Streaming APIs: SSE and WebSocket Patterns 2026](https://apiscout.dev/guides/streaming-apis-sse-websocket-2026)
- [WebSocket vs. Server-Sent Events: Key Differences](https://getstream.io/blog/websocket-sse/)
- [WebSocket vs Server-Sent Events — Vercel](https://vercel.com/i/websocket-vs-server-sent-events)
- [REST vs GraphQL vs gRPC vs tRPC: API Architecture 2026](https://apiscout.dev/guides/rest-vs-graphql-vs-grpc-vs-trpc-2026)
- [API Design Patterns [2026]: REST, GraphQL, gRPC Compared](https://precisionaiacademy.com/blog/api-design-patterns-2026)
- [gRPC vs REST vs GraphQL: API Architecture Guide for 2026](https://kanopylabs.com/blog/grpc-vs-rest-vs-graphql-api-architecture)
- [Beginner's Guide to APIs in 2026: REST vs GraphQL vs gRPC](https://nirajiitr.com/blog/apis-2026-rest-vs-graphql-vs-grpc-use-cases)
- [OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [OWASP API Security Top 10 (2023): A Cloud-Native Guide](https://orca.security/resources/blog/owasp-api-security-top-10/)
- [OWASP API Security Testing Framework](https://owasp.org/www-project-api-security-testing-framework/)