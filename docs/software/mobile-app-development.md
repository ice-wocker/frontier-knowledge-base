# 移动应用开发

> 最后更新：2026-09-26 ｜ 领域：软件·平台与领域应用 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 概述

移动应用开发目前呈现「原生优先」与「跨平台共享」并行的格局。iOS 侧以 **Swift / SwiftUI** 为官方技术栈，Android 侧以 **Kotlin / Jetpack Compose** 为官方技术栈；跨平台方向则由 **Kotlin Multiplatform（KMP）**、**Flutter**、**React Native** 等方案分担，分别在共享业务逻辑、共享 UI、复用 Web 技能等维度取舍。下文按「最新进展、核心技术、代表项目、关键数据、趋势与争议」组织。

## 最新进展（2025–2026）

**iOS / SwiftUI**：Apple 在 WWDC 2026 上推出 refreshed Liquid Glass 外观与交互改进，官方说明应用在 2027 OS 版本上会自动采用更新后的 Liquid Glass 外观而无需改代码，涉及交互式 Liquid Glass 元素、iPadOS 非活动窗口外观、工具栏自定义（溢出菜单与固定位置）、滚动最小化行为，以及基于 size classes 构建可缩放应用的指引（[What's new in SwiftUI — WWDC26](https://developer.apple.com/videos/play/wwdc2026/269/)）。Liquid Glass 本身最初在 WWDC 2025 介绍，被描述为受玻璃光学特性与液体流动性启发的新自适应材质（[Build a SwiftUI app with the new design](https://developer.apple.com/videos/play/wwdc2025/323/)）。语言层面，Apple 于 2026 年 6 月发布 Swift 6.4，新增精准抑制警告、简化 `anyAppleOS` 等可用性属性，并强化编译器诊断（[Apple accelerates app development with new intelligence frameworks and advanced tools](https://www.apple.com/qa/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/)）。

**Android / Compose**：在 Google I/O 2026 上，Google 宣布 Android 进入 **Compose First** 阶段，Views 进入维护模式；未来的指南与库都以 Compose 优先。官方称最新版本基于五年演进提供了成熟工具链，包括高度可定制的 Styles API、改进的共享元素转场与增强的输入支持（[17 Things to know for Android developers at Google I/O](https://developer.android.google.cn/blog/posts/17-things-to-know-for-android-developers-at-google-i-o)）。

**Kotlin Multiplatform**：Kotlin Multiplatform 自 2023 年 11 月由 JetBrains 宣布进入 **Stable**。据两次开发者生态调查，KMP 使用率在一年内翻倍以上，从 2024 年的 7% 升至 2025 年的 18%（[Ten reasons to adopt Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/multiplatform-reasons-to-try.html)）。KotlinConf'26 主题演讲显示，Google 生产环境使用 Kotlin 已超过十年，**92% 的专业 Android 开发者**使用 Kotlin；KMP 案例覆盖的应用每天服务数亿用户，并展示了基于 Google Gemma 模型的端侧 AI 能力（[KotlinConf'26 Keynote Highlights](https://blog.jetbrains.com/kotlin/2026/05/kotlinconf26-keynote-highlights/)）。

**Flutter**：据第三方汇总，Flutter 3.44.0 于 2026 年 5 月 21 日随 Google I/O 发布，文档在 8 月初已反映 3.44.7（[Flutter](https://bundl.run/apps/flutter)）。

**React Native**：New Architecture（Fabric + TurboModules + Bridgeless）已成为默认与唯一标准。Expo SDK 53 起新架构在所有项目中默认启用；截至 2026 年 1 月，约 **83% 的 SDK 54 项目**（使用 EAS Build 构建）采用 New Architecture（[React Native's New Architecture](https://docs.expo.dev/guides/new-architecture/)）。SDK 54 是最后一个支持 Legacy Architecture 的版本，SDK 55 起移除 `newArchEnabled` 配置项（[Expo SDK 55](https://expo.dev/changelog/sdk-55)）。

## 核心技术与关键概念

**声明式 UI 范式对比**：三种主流框架均为声明式，但组件模型不同——Jetpack Compose 采用函数式 approach 的 Composable functions；SwiftUI 采用面向协议的 View protocol conforming structs；Flutter 采用基于 widget 的 Widget classes（有状态与无状态）（[Compare Declarative Frameworks](https://www.jetpackcompose.app/compare-declarative-frameworks/JetpackCompose-vs-SwiftUI-vs-Flutter)）。

**跨平台共享层级**：KMP 允许在 Android、iOS、桌面（JVM）、服务端（JVM）与 Web 之间共享代码，官方定位其为「stable technology」可用于最保守的生产场景；配合 JetBrains 的 Compose Multiplatform（CMP）还可共享 UI（[Kotlin Multiplatform vs. React Native](https://kotlinlang.org/docs/multiplatform/kotlin-multiplatform-react-native.html)、[Kotlin Multiplatform — Android Developers](https://developer.android.google.cn/kotlin/multiplatform.html)）。

**渲染与性能机制**：Flutter 通过编译后的 Dart 代码与 Skia 渲染引擎实现接近原生的性能，适合图形密集与复杂动画场景；React Native 在多数业务应用中性能足够，但其「桥」通信在计算密集场景可能引入延迟；SwiftUI 在 iOS 上提供最佳原生性能但限于 Apple 生态（[Comprehensive comparison](https://www.index.dev/skill-vs-skill/swiftui-vs-flutter-vs-react-native)）。Flutter 采用 Impeller 渲染引擎，而 SwiftUI 直接基于原生 Metal；访问 iOS 新特性时 Flutter 通常有 3–12 个月的插件滞后，SwiftUI 可首日使用（[Flutter vs SwiftUI: Cross-Platform vs Native iOS in 2026](https://www.misar.blog/compare/flutter-vs-swiftui-ios)）。

## 代表性项目 / 公司 / 产品（附官方链接）

- **SwiftUI / Xcode（Apple）**：官方声明式 UI 框架，2026 年随系统更新迭代 Liquid Glass 外观（[Apple Developer](https://developer.apple.com/videos/play/wwdc2026/269/)）。
- **Jetpack Compose（Google）**：Android 官方 UI 标准，官方进入 Compose First 阶段（[Android Developers Blog](https://developer.android.google.cn/blog/posts/17-things-to-know-for-android-developers-at-google-i-o)）。
- **Kotlin Multiplatform / Compose Multiplatform（JetBrains）**：KMP 提供跨平台逻辑共享，CMP 提供跨平台 UI 共享，官方列出超过 **20,000 家公司**在全球使用 KMP，覆盖金融、电商、社交媒体等行业（[Kotlin Multiplatform Case studies](https://kotlinlang.org/case-studies/?type=multiplatform)）。
- **Flutter（Google）**：跨 iOS/Android/Web/Desktop 的开源 UI 工具包，第三方资料记录其 3.44 系列于 2026 年发布（[Flutter](https://bundl.run/apps/flutter)）。
- **React Native / Expo（Meta / Expo）**：跨平台方案，New Architecture 已强制化，Expo 提供 SDK 与 EAS Build 工具链（[Expo SDK 55](https://expo.dev/changelog/sdk-55)）。

## 关键数据与评测结果（附来源）

- **框架市场份额（2026，口径不一）**：有来源称 Flutter 约 46%、React Native 约 35–38%，两者合计占混合应用开发的 80% 以上（[Flutter Vs React Native in 2026](https://www.mobiindia.in/blog/flutter-vs-react-native/)）；另有来源给出 Flutter 46%、React Native 32%、Swift 14%、Kotlin 12%、Ionic/Cordova 6%（[Why Flutter Is the Best Framework](https://mobilemerit.com/why-flutter-is-the-best-framework-for-app-development-the-ultimate-guide/)）。两者在 React Native 份额上存在差异，来源口径与统计方法不同，宜并列看待。
- **Stack Overflow 2024 调查**：Flutter 在所有受访者中使用率 9.4%、React Native 8.4%；专业开发者中分别为 9.4% 与 9.0%；«Admired» 比例 Flutter 60.6%、React Native 56.5%（[Flutter vs React Native: Statistics 2026](https://quashbugs.com/blog/flutter-vs-react-native-statistics)）。
- **KMP 采用率**：一年内由 7%（2024）升至 18%（2025）（[Ten reasons to adopt Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/multiplatform-reasons-to-try.html)）。
- **New Architecture 采用率**：约 83% 的 SDK 54 项目使用 New Architecture（截至 2026 年 1 月）（[React Native's New Architecture](https://docs.expo.dev/guides/new-architecture/)）；对照 SDK 52 项目在 2025 年 4 月为 74.6%（[Expo SDK 53](https://www.expo.io/changelog/sdk-53)）。
- **Flutter 工具链调查（Q2 2026）**：传统 IDE 中 VS Code 占 66%、Android Studio 占 40%；AI 编程代理中 Claude Code 占 32%、Antigravity 占 23%，均超过 GitHub Copilot（19%）、Cursor（18%）与 Codex（17%）；受访者可多选，数值合计远超 100%（[Flutter Q2 2026 survey](https://flutter.dev/blog/flutter-q2-2026-survey)）。

## 趋势与争议

**趋势**：一是「原生栈的现代化」——SwiftUI 的 Liquid Glass 与 Android 的 Compose First 都在推动声明式 UI 成为唯一主流；二是「跨平台分层共享」——KMP 的增长与官方支持把共享从 UI 层下沉到业务逻辑层，CMP 再补足 UI 共享；三是「AI 进入研发流程」——Flutter 调查显示 AI 编程代理使用率已超过部分传统补全工具（[Flutter Q2 2026 survey](https://flutter.dev/blog/flutter-q2-2026-survey)）。

**争议与取舍**：Android-only 项目普遍认为 Compose 在性能、首日平台特性与代码库归属上更优，iOS+Android 双端项目则认为 Flutter 在单代码库经济性与品牌一致渲染上更优——2026 年的讨论更强调「匹配度」而非绝对优劣（[Jetpack Compose vs Flutter for Android in 2026](https://ecorpit.com/jetpack-compose-vs-flutter/)）。跨平台方案的固有代价是平台特性访问滞后（Flutter 插件滞后 3–12 个月）与桥接开销（React Native），而原生栈的代价是双代码库与双团队（[Flutter vs SwiftUI](https://www.misar.blog/compare/flutter-vs-swiftui-ios)）。市场份额数据本身因口径差异较大，尚无统一权威结论。

## 参考来源

- [What's new in SwiftUI — WWDC26](https://developer.apple.com/videos/play/wwdc2026/269/)
- [Build a SwiftUI app with the new design](https://developer.apple.com/videos/play/wwdc2025/323/)
- [Apple accelerates app development with new intelligence frameworks and advanced tools](https://www.apple.com/qa/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/)
- [17 Things to know for Android developers at Google I/O](https://developer.android.google.cn/blog/posts/17-things-to-know-for-android-developers-at-google-i-o)
- [KotlinConf'26 Keynote Highlights](https://blog.jetbrains.com/kotlin/2026/05/kotlinconf26-keynote-highlights/)
- [Kotlin Multiplatform Case studies](https://kotlinlang.org/case-studies/?type=multiplatform)
- [Kotlin Multiplatform vs. React Native: A cross-platform comparison](https://kotlinlang.org/docs/multiplatform/kotlin-multiplatform-react-native.html)
- [Kotlin Multiplatform — Android Developers](https://developer.android.google.cn/kotlin/multiplatform.html)
- [Ten reasons to adopt Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform/multiplatform-reasons-to-try.html)
- [Flutter Q2 2026 survey](https://flutter.dev/blog/flutter-q2-2026-survey)
- [Flutter（版本汇总）](https://bundl.run/apps/flutter)
- [React Native's New Architecture](https://docs.expo.dev/guides/new-architecture/)
- [Expo SDK 55](https://expo.dev/changelog/sdk-55)
- [Expo SDK 53](https://www.expo.io/changelog/sdk-53)
- [Compare Declarative Frameworks: Jetpack Compose vs SwiftUI vs Flutter](https://www.jetpackcompose.app/compare-declarative-frameworks/JetpackCompose-vs-SwiftUI-vs-Flutter)
- [Flutter vs SwiftUI: Cross-Platform vs Native iOS in 2026](https://www.misar.blog/compare/flutter-vs-swiftui-ios)
- [Jetpack Compose vs Flutter for Android in 2026](https://ecorpit.com/jetpack-compose-vs-flutter/)
- [Comprehensive comparison for technology in applications](https://www.index.dev/skill-vs-skill/swiftui-vs-flutter-vs-react-native)
- [Flutter vs React Native: Statistics, Market Share, Jobs & Adoption (2026)](https://quashbugs.com/blog/flutter-vs-react-native-statistics)
- [Why Flutter Is the Best Framework for App Development](https://mobilemerit.com/why-flutter-is-the-best-framework-for-app-development-the-ultimate-guide/)
- [Flutter Vs React Native in 2026](https://www.mobiindia.in/blog/flutter-vs-react-native/)