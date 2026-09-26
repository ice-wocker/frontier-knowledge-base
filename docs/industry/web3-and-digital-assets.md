# Web3 与数字资产

> 最后更新：2026-09-26 ｜ 领域：区块链与数字金融 ｜ 说明：信息来源为公开网络资料，详见文末参考来源

## 一、概述

2026 年的 Web3 与数字资产行业，已从"加密原生叙事"转向"机构基础设施 + 全球监管落地"的双轮驱动。一方面，比特币、以太坊完成了从"实验网络"到"受监管资产类别"的身份转换：现货比特币 ETF 规模突破千亿美元，美国、香港、欧盟等主要法域相继建立稳定币与加密资产监管框架；另一方面，行业内生的风险仍未消除——2026 年 9 月 Bitget 热钱包被盗约 3.516 亿美元，链上非法资金流规模持续攀升。技术层面，以太坊通过 Dencun、Pectra、Fusaka 三次升级持续推进 Layer 2 扩容，比特币则围绕 OP_CAT 等"契约（covenant）"提案展开争议，AI 与加密的融合（智能体支付）成为最受关注的新兴用例。

## 二、2025–2026 最新进展

**以太坊升级路线图。** 继 2024 年 3 月 13 日 Dencun 升级引入 EIP-4844（proto-danksharding，以 blob 交易显著降低 Rollup 成本）与 EIP-1153（瞬态存储操作码 TSTORE/TLOAD）后，以太坊于 2025 年 5 月 7 日完成 Pectra 升级：通过 EIP-7702 让 EOA（外部账户）具备智能合约能力（支持交易批量处理、手续费代付、更好的恢复机制），提高最大有效余额以允许质押者按每 1 ETH 增量获得奖励，并将 blob 目标数从 3 提升至 6、上限提升至 9（[Dencun — Ethereum roadmap](https://www.ethereum.org/roadmap/)、[Pectra / 以太坊路线图](https://ethereum.org/zh/roadmap/)、[Transaction Costs and Speed in the Ethereum Ecosystem](https://arxiv.org/pdf/2606.22206v1)）。2025 年 12 月 3 日的 Fusaka 升级引入 PeerDAS（对等数据可用性采样）以提升 Rollup 数据可用性并降低节点门槛，同时引入"仅 blob 参数分叉"（BPO）以灵活调整 blob 数量（[Fusaka — Ethereum roadmap](https://www.ethereum.org/ru/roadmap/)）。

**稳定币立法密集落地。** 美国《GENIUS Act》（Guiding and Establishing National Innovation for U.S. Stablecoins Act，由参议员 Bill Hagerty 提出）为支付型稳定币建立联邦监管框架，在参议院以 68 票的跨党派结果通过，强调消费者保护与美元储备货币地位（[Guiding and Establishing National Innovation for U.S. Stablecoins Act](https://financialservices.house.gov/uploadedfiles/2025-07-10_--_one-pager_genius_final.pdf)）。香港《稳定币条例》（Stablecoins Ordinance, Cap. 656）自 2025 年 8 月 1 日生效，规定任何在港发行或锚定港元的法币挂钩稳定币均须取得金管局牌照（[Explanatory Note on Transitional Provisions for Pre-existing Stablecoin Issuers — HKMA](https://www.hkma.gov.hk/media/eng/doc/key-functions/ifc/stablecoin-issuers/Explanatory_Notes_on_Transitional_Provisions_for_Pre-existing_Stablecoin_Issuers_eng.pdf)、[Regulatory Regime for Stablecoin Issuers — HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/)）。2026 年，金管局向由渣打银行（香港）、香港电讯与 Animoca 合组的"碇点金融科技"以及汇丰银行批出首批稳定币发行人牌照（[余伟文谈稳健发展香港合规稳定币生态圈 — HKMA](https://www.hkma.gov.hk/chi/news-and-media/insight/2026/04/20260410)、[Standard Chartered-led venture, HSBC win HK's first stablecoin licenses](https://www.chinadailyasia.com/hk/article/631800)）。欧盟 MiCA（Markets in Crypto-Assets Regulation，Regulation (EU) 2023/1114）自 2024 年 12 月 30 日全面适用，ART/EMT 相关条款自 2024 年 6 月 30 日起适用；旧有服务商"祖父条款"过渡最长可至 2026 年 7 月 1 日（[MiCA — ESMA](https://www.esma.europa.eu/sites/default/files/2023-10/ESMA74-449133380-441_Statement_on_MiCA_Supervisory_Convergence.pdf)、[MiCA — CNMV](https://www.cnmv.es/portal/MiCA/Regulacion-Criptoactivos)）。

**机构入场与 ETF 规模。** 2026 年，美国现货比特币 ETF 合计资产管理规模正式突破 1000 亿美元，贝莱德 iShares Bitcoin Trust（IBIT）持续主导新增资金流入（[Bitcoin ETF 2026: How Spot Funds Are Reshaping Institutional Markets](https://cryptoetfpro.com/bitcoin-etf-2026-institutional-adoption-analysis)、[Bitcoin ETF Holdings 2026](https://cryptoetfpro.com/bitcoin-etf-holdings-2026-institutional-shifts)）。据中文财经报道，美国已建立战略比特币储备，持有约 32.8 万枚比特币（价值超 255 亿美元），美国 ETF 与上市公司合计持有约 12% 的比特币流通量（[比特币数字黄金属性持续强化 — 新浪财经](https://finance.sina.com.cn/wm/2026-09-03/doc-iniqqfvq1064789.shtml)）。

**美国监管框架重构。** SEC 于 2026 年 3 月发布解释，明确联邦证券法对部分加密资产及交易的适用方式（CFTC 参与联署），并随后提出名为"Regulation Crypto Assets"的新规则提案，为涉及加密资产的投资合同建立定制化的证券发行制度（[SEC Clarifies the Application of Federal Securities Laws to Crypto Assets](https://www.sec.gov/newsroom/press-releases/2026-30-sec-clarifies-application-federal-securities-laws-crypto-assets)、[SEC Proposes New Regulation Crypto Assets](https://www.sec.gov/newsroom/press-releases/2026-76-sec-proposes-new-regulation-crypto-assets)）。与此同时，国会推进《CLARITY 法案》（Digital Asset Market Clarity Act），试图以立法方式确立数字资产市场结构框架（[《CLARITY法案》：迈向监管清晰之年及对香港的启示](https://www.stcn.com/article/detail/3920362.html)）。

## 三、核心概念与关键条款

**Rollup 与 Blob 经济。** Layer 2 扩容的核心是将执行搬到链下、把数据可用性（DA）成本压到最低。Dencun 引入的 blob 交易让 Rollup 的 L2 成本大幅下降；Pectra 通过 EIP-7840 简化 blob 更新流程、EIP-7549 提升 blob 数量，进一步扩大吞吐（[Transaction Costs and Speed in the Ethereum Ecosystem](https://arxiv.org/pdf/2606.22206v1)、[Pectra / 以太坊路线图](https://ethereum.org/zh/roadmap/)）。Fusaka 的 PeerDAS 则通过采样提升数据可用性效率（[Fusaka — Ethereum roadmap](https://www.ethereum.org/ru/roadmap/)）。以太坊官方还将 ZK Rollup 与 Optimistic Rollup 按 TVL、生产运行时长与风险因素进行"成熟度分级"（[Ethereum Layer 2: Explore networks](https://www.ethereum.org/layer-2/networks/)）。

**稳定币监管要件。** GENIUS Act 将支付型稳定币纳入联邦框架，储备资产包含美国国债等（由此把稳定币需求导向 T-bill 市场）（[Stablecoins under the GENIUS Act — Chicago Fed](https://www.chicagofed.org/-/media/others/people/documents/decarlo-stablecoins-under-genius-act.pdf)、[Crypto-assets and decentralised finance — ESRB](https://www.esrb.europa.eu/pub/pdf/reports/esrb.report202510_cryptoassets.et.pdf)）。香港稳定币牌照制度要求 100% 储备支持、储备隔离、审计与透明度、可执行的赎回权，并禁止向用户支付收益（[From Rulemaking to Real-World Compliance Q1 2026](https://www.cense.com/app/uploads/2026/04/13312-Cense-Quarterly-report-2026-Q1.pdf)）。MiCA 则为加密资产服务提供商（CASP）建立全欧盟统一牌照，但实际发行端极为审慎——截至 2026 年 9 月 1 日，仅有 39 种 EMT 获批发行，ART 为 0 种（[The EBA identifies priorities for the review of MiCA](https://www.eba.europa.eu/publications-and-media/press-releases/eba-identifies-priorities-review-mica)）。

**RWA 代币化。** 真实世界资产（RWA）代币化以"代币化美国国债/货币基金"为锚，贝莱德 BUIDL（USD Institutional Digital Liquidity Fund）与 Franklin Templeton 的 OnChain U.S. Government Money Fund 为代表（[Digital Assets and the Treasury Market — U.S. Treasury](https://home.treasury.gov/system/files/221/TBACCharge2Q42024.pdf)）。按不同统计口径，2026 年代币化 RWA 总规模在 100 亿至 600 亿美元区间；代币化美债与货币基金约 130–150 亿美元，私募信贷约 80–190 亿美元，代币化股票自 2025 年中期诞生、在 2026 年 3 月纳斯达克批准后加速（[The State of RWA Tokenization](https://www.stobox.io/reports/state-of-rwa-2026)、[RWA Tokenization 2026: The $60 Billion Market](https://deficoverage.org/rwa-tokenization-2026-blackrock-treasuries-defi-2)、[Tokenized Treasuries Crossed $10 Billion](https://www.vaasblock.com/crypto/tokenized-real-world-assets-blackrock-buidl-ondo-2026/)）。

**比特币的契约之争。** 是否激活 OP_CAT 成为 Taproot 以来最具争议的升级议题。OP_CAT 可启用"契约"（跨交易持续生效的花费条件），解锁金库（vault）、免信任跨链桥与新型 Layer 2；反对者担忧引入 MEV、降低可替代性。其 BIP-347 规范于 2026 年 3 月 1 日达到"Complete"状态（文档定稿，但不代表激活共识），并在 Inquisition signet 上累计测试约 74,000 笔交易，远超 CTV（16 笔）与 APO（约 1,000 笔）（[OP_CAT and the Great Covenant Debate](https://www.spark.money/research/bitcoin-op-cat-covenant-debate)、[Bitcoin Covenant Proposals Compared: CTV, APO, OP_CAT](https://www.spark.money/tools/bitcoin-covenant-proposals-compared)）。

## 四、代表性案例/机构（带官方链接）

- **HKMA 稳定币监管**：首批持牌机构为渣打系"碇点"与汇丰（[HKMA Insight](https://www.hkma.gov.hk/chi/news-and-media/insight/2026/04/20260410)）。
- **新加坡 MAS**：通过 Project Guardian 探索资产代币化，Project Orchid 探索"用途绑定货币"与数字新加坡元基础设施，2026 年 6 月成立 Future of Finance Institute（FFI）；2026 年 9 月就稳定币监管框架的立法修订公开征求意见（[Digital Assets — MAS](https://www.mas.gov.sg/development/fintech/digital-assets)、[MAS Establishes Future of Finance Institute](https://www.mas.gov.sg/news/media-releases/2026/mas-establishes-future-of-finance-institute-to-scale-financial-innovation)、[Central Bank Digital Currency — MAS](https://www.mas.gov.sg/development/fintech/central-bank-digital-currency)）。
- **美国 SEC Crypto Task Force**：就加密资产分类与代币化证券（如 OTCM 的 Model B Digital Securities）征询意见（[Crypto Task Force Written Input](https://www.sec.gov/featured-topics/crypto-task-force/crypto-task-force-written-input?page=5)）。
- **数字人民币（e-CNY）运营体系**：首批 26 家金融机构签约接入数字人民币国际运营中心，依托"数币达"（CBETS）跨境结算平台（[新华鲜报丨接入首批金融机构 数字人民币跨境服务新进展](https://www.news.cn/20260617/0ffe52402db24b9f95b6187c4265415a/c.html)）。

## 五、关键数据（带来源）

- **稳定币规模**：2026 年稳定币总市值突破 3000 亿美元；USDT 约 1834 亿美元（占 60.5%），USDC 约 743 亿美元（占 24.5%），两者合计约 85.1%（[Stablecoins surge past $300 billion — CoinDesk](https://www.coindesk.cc/stablecoins-surge-past-300-billion-forcing-a-reckoning-over-the-dollar-s-future-112895.html)、[Tether and Circle control 85% of stablecoin supply — CoinDesk](https://www.coindesk.cc/tether-and-circle-control-85-of-stablecoin-supply-as-market-concentration-stays-near-record-highs-111999.html)）。IMF 数据亦显示 2026 年 Q1 稳定币市值约 0.3 万亿美元，USDT+USDC 合计持有约 2% 的美国未偿国债（[Crypto Assets Monitor Highlights: Q1 2026 — IMF](https://www.imfconnect.org/content/dam/imf/News%20and%20Generic%20Content/GMM/Special%20Features/Crypto%20Monitor%20Q1%202026.pdf)）。
- **DeFi TVL**：据 DeFiLlama，2026 年 9 月 20 日当周全市场 DeFi 总 TVL 约 881.72 亿美元；公链排名中以太坊约 536.5 亿美元（占比约 66.6%），Solana 约 64.0 亿美元、Base 约 61.7 亿美元、BSC 约 58.3 亿美元（[CoinW研究院周报 | PANews](https://www.panewslab.com/zh/articles/01a0c1d2-77bd-71cb-ba93-d10ddd3c707e)、[Chain TVL Tracker](https://blockchainmagazine.net/chain-tvl-tracker/)）。L2 层面，截至 2026 年中期约 73 条活跃 Rollup 承载 480 亿美元以上 L2 DeFi TVL，Arbitrum One（约 138 亿美元）与 Base（约 112 亿美元）合计约占 L2 流动性的 77%（[Which Ethereum L2 Wins When You Score TVL, Fees, and Security?](https://www.spotedcrypto.com/defi-layer-2-comparison-2026-arbitrum-base-optimism-zksync/)）。
- **比特币行情**：2026 年 9 月 26 日 BTC 报约 83,931 美元，市值约 1.69 万亿美元，市占率约 58.5%（[Bitcoin — CryptoSlate](https://cryptoslate.com/coins/bitcoin/)）；IMF 记录 BTC 从 2025 年 10 月峰值一度下跌约 43% 至约 70,000 美元，市值缩至约 1.4 万亿美元（[Crypto Assets Monitor Highlights: Q1 2026 — IMF](https://www.imfconnect.org/content/dam/imf/News%20and%20Generic%20Content/GMM/Special%20Features/Crypto%20Monitor%20Q1%202026.pdf)）。
- **AI 智能体支付**：据做市商 Keyrock 2026 年 5 月报告，截至 2026 年 4 月的 12 个月内，AI 智能体完成约 1.76 亿笔链上支付，总金额约 7,300 万美元；Circle 称 USDC 占智能体驱动交易量的约 98.8%–99.3%（[Could AI Agents Be Crypto's First Real Mass Adoption Use Case?](https://www.coinmarketcapa.com/academy/es/article/ai-agents-crypto-first-real-mass-adoption-use-case)、[AI Agents Are Starting to Pay for Things in Crypto — 24/7 Wall St.](https://247wallst.com/investing/cryptocurrency/2026/09/18/ai-agents-are-starting-to-pay-for-things-in-crypto-which-coin-do-they-use-xrp-solana-or-usdc/)）。
- **数字人民币**：通过数字人民币 App 开立个人钱包 2.3 亿个、单位钱包 1884 万个；多边央行数字货币桥（mBridge）累计处理跨境支付 4047 笔、金额折合人民币 3872 亿元，其中数字人民币占比约 95.3%（[数字人民币迎来重大调整 — 中国政府网](https://www.gov.cn/lianbo/202512/content_7053034.htm)）。新一代数字人民币运行机制于 2026 年 1 月 1 日正式启动实施（[央行：新一代数字人民币运行机制将于2026年1月1日正式启动实施](http://m.toutiao.com/group/7589114302913675819/)）。

## 六、趋势与争议

**1. 黑客与非法资金流高企。** 2025 年 2 月，Bybit 遭朝鲜 Lazarus 集团攻击，被盗约 15 亿美元；2026 年 8 月 Bybit 提起民事诉讼并获法院初步禁令冻结部分资产，累计追回约 4840 万美元、冻结约 3050 万美元（约占被盗资金的 5.26%）（[Bybit Sues North Korea and Lazarus Group](https://www.prnewswire.com/in/news-releases/bybit-sues-north-korea-and-lazarus-group-secures-preliminary-injunction-freezing-stolen-assets-in-landmark-crypto-asset-recovery-effort-302846551.html)、[Bybit v. DPRK Lazarus Group — $1.5B Hack Civil Lawsuit](https://avoid.net/bybit-v-dprk-lazarus-group-1-5b-hack-civil-lawsuit-august-2026)）。2026 年 9 月 25 日，Bitget 确认热钱包未授权转出，初步核算受影响资金约 3.516 亿美元（[Bitget 凌晨突然被盗 — 新浪财经](https://finance.sina.com.cn/blockchain/roll/2026-09-24/doc-inisyuqn9846431.shtml)、[Everything We Know About Bitget's Massive $351M Hack — CoinDesk](https://www.coindesk.cc/everything-we-know-about-bitget-s-massive-351m-hack-118856.html)）。TRM 的《2026 Crypto Crime Report》记录 2025 年非法加密资金流约 1580 亿美元，较 2024 年的 645 亿美元增长 145%（[Online Scams, Crypto Fraud, and Digital Extortion — U.S. House Homeland Security](https://homeland.house.gov/wp-content/uploads/2026/04/2026-04-21-BSECIP-Hearing.pdf)）。

**2. 市场波动与杠杆风险。** BTC 在 2025 年 10 月创下峰值后大幅回撤，IMF 指出下跌与风险偏好转向、以及杠杆头寸自动平仓有关（[Crypto Assets Monitor Highlights: Q1 2026 — IMF](https://www.imfconnect.org/content/dam/imf/News%20and%20Generic%20Content/GMM/Special%20Features/Crypto%20Monitor%20Q1%202026.pdf)）。稳定币高度集中于 USDT/USDC，也使单一发行人的储备与合规风险具备系统重要性（[Tether and Circle control 85% of stablecoin supply — CoinDesk](https://www.coindesk.cc/tether-and-circle-control-85-of-stablecoin-supply-as-market-concentration-stays-near-record-highs-111999.html)）。

**3. 央行数字货币的分化。** 数字人民币在跨境结算上依托 mBridge 与中国—东盟场景加速推进；数字欧元则受隐私与立法博弈影响，欧盟层面法案自 2026 年 7 月进入"三方会谈"，欧洲议会 7 月 9 日批准谈判授权，欧洲央行规划 2027 年启动试点、2029 年正式发行（前提是法律框架在 2026 年底前通过）（[数字欧元最新进展 — 新浪财经](https://finance.sina.com.cn/blockchain/2026-09-17/doc-inisayaf4199431.shtml)、[欧洲议会批准数字欧元谈判授权 — 北京市商务局](https://sw.beijing.gov.cn/zt/mymcyd/smdtx/202608/t20260824_4834267.html)、[警惕对美依赖 欧洲加快数字欧元布局 — 光明网](http://m.toutiao.com/group/7604947414511796774/)）。

**4. 全球监管格局差异。** 美国走向"SEC 解释 + 规则提案 + 立法"的清晰化路径；欧盟以 MiCA 建立统一牌照但发行审慎；香港以稳定币牌照制度吸引合规发行；新加坡以 Project Guardian/BLOOM 推动代币化结算资产。有分析将 2026 年全球数字货币格局概括为"三极分化与秩序重构"（[2026全球数字货币新格局：三极分化与秩序重构 — 第一财经](https://m.yicai.com/news/102999946.html)）。

**5. AI+Crypto 融合。** "智能体支付"（agentic payments）让 AI 代理以稳定币在链上自主支付，被视为加密走向大规模应用的首个真实场景；但 Chainalysis 提示 x402 交易量激增部分由迷因币活动驱动，可能高估真实市场需求（[AI Agents Are Starting to Pay for Things in Crypto — 24/7 Wall St.](https://247wallst.com/investing/cryptocurrency/2026/09/18/ai-agents-are-starting-to-pay-for-things-in-crypto-which-coin-do-they-use-xrp-solana-or-usdc/)、[How AI and crypto are converging: eight use cases](https://www.21shares.com/en-eu/insights/ai-crypto-convergence-use-cases)）。

## 参考来源

1. [Dencun — Ethereum roadmap](https://www.ethereum.org/roadmap/)
2. [以太坊路线图（Pectra）— ethereum.org](https://ethereum.org/zh/roadmap/)
3. [Fusaka — Ethereum roadmap](https://www.ethereum.org/ru/roadmap/)
4. [Transaction Costs and Speed in the Ethereum Ecosystem: Scalability of the Mainnet and Layer 2s (arXiv)](https://arxiv.org/pdf/2606.22206v1)
5. [Ethereum Layer 2: Explore networks — ethereum.org](https://www.ethereum.org/layer-2/networks/)
6. [Guiding and Establishing National Innovation for U.S. Stablecoins Act (GENIUS Act) — U.S. House](https://financialservices.house.gov/uploadedfiles/2025-07-10_--_one-pager_genius_final.pdf)
7. [Stablecoins under the GENIUS Act: background and open questions — Chicago Fed](https://www.chicagofed.org/-/media/others/people/documents/decarlo-stablecoins-under-genius-act.pdf)
8. [Crypto-assets and decentralised finance — ESRB Report](https://www.esrb.europa.eu/pub/pdf/reports/esrb.report202510_cryptoassets.et.pdf)
9. [Explanatory Note on Transitional Provisions for Pre-existing Stablecoin Issuers — HKMA](https://www.hkma.gov.hk/media/eng/doc/key-functions/ifc/stablecoin-issuers/Explanatory_Notes_on_Transitional_Provisions_for_Pre-existing_Stablecoin_Issuers_eng.pdf)
10. [Regulatory Regime for Stablecoin Issuers — HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/)
11. [余伟文谈稳健发展香港合规稳定币生态圈 — HKMA](https://www.hkma.gov.hk/chi/news-and-media/insight/2026/04/20260410)
12. [Standard Chartered-led venture, HSBC win HK's first stablecoin licenses — China Daily](https://www.chinadailyasia.com/hk/article/631800)
13. [MiCA supervisory convergence statement — ESMA](https://www.esma.europa.eu/sites/default/files/2023-10/ESMA74-449133380-441_Statement_on_MiCA_Supervisory_Convergence.pdf)
14. [MiCA: New regulation for crypto-assets — CNMV](https://www.cnmv.es/portal/MiCA/Regulacion-Criptoactivos)
15. [MiCA — ESMA](https://www.esma.europa.eu/ga/node/201529)
16. [The EBA identifies priorities for the review of MiCA — EBA](https://www.eba.europa.eu/publications-and-media/press-releases/eba-identifies-priorities-review-mica)
17. [Bitcoin ETF 2026: How Spot Funds Are Reshaping Institutional Markets](https://cryptoetfpro.com/bitcoin-etf-2026-institutional-adoption-analysis)
18. [Bitcoin ETF Holdings 2026: Record Inflows and Institutional Shifts](https://cryptoetfpro.com/bitcoin-etf-holdings-2026-institutional-shifts)
19. [比特币数字黄金属性持续强化 — 新浪财经](https://finance.sina.com.cn/wm/2026-09-03/doc-iniqqfvq1064789.shtml)
20. [Institutional Bitcoin Adoption Explained — The Block](https://www.theblock.co/learn/407111)
21. [SEC Clarifies the Application of Federal Securities Laws to Crypto Assets](https://www.sec.gov/newsroom/press-releases/2026-30-sec-clarifies-application-federal-securities-laws-crypto-assets)
22. [SEC Proposes New Regulation Crypto Assets](https://www.sec.gov/newsroom/press-releases/2026-76-sec-proposes-new-regulation-crypto-assets)
23. [Crypto Task Force Written Input — SEC](https://www.sec.gov/featured-topics/crypto-task-force/crypto-task-force-written-input?page=5)
24. [《CLARITY法案》：迈向监管清晰之年及对香港的启示 — 证券时报](https://www.stcn.com/article/detail/3920362.html)
25. [From Rulemaking to Real-World Compliance Q1 2026 Crypto Regulatory Update — Cense](https://www.cense.com/app/uploads/2026/04/13312-Cense-Quarterly-report-2026-Q1.pdf)
26. [Digital Assets and the Treasury Market — U.S. Department of the Treasury](https://home.treasury.gov/system/files/221/TBACCharge2Q42024.pdf)
27. [The State of RWA Tokenization — Stobox](https://www.stobox.io/reports/state-of-rwa-2026)
28. [RWA Tokenization 2026: The $60 Billion Market — DeFi Coverage](https://deficoverage.org/rwa-tokenization-2026-blackrock-treasuries-defi-2)
29. [Tokenized Treasuries Crossed $10 Billion — VAAS](https://www.vaasblock.com/crypto/tokenized-real-world-assets-blackrock-buidl-ondo-2026/)
30. [OP_CAT and the Great Covenant Debate — Spark](https://www.spark.money/research/bitcoin-op-cat-covenant-debate)
31. [Bitcoin Covenant Proposals Compared: CTV, APO, OP_CAT — Spark](https://www.spark.money/tools/bitcoin-covenant-proposals-compared)
32. [Digital Assets — Monetary Authority of Singapore](https://www.mas.gov.sg/development/fintech/digital-assets)
33. [MAS Establishes Future of Finance Institute to Scale Financial Innovation](https://www.mas.gov.sg/news/media-releases/2026/mas-establishes-future-of-finance-institute-to-scale-financial-innovation)
34. [Central Bank Digital Currency — MAS](https://www.mas.gov.sg/development/fintech/central-bank-digital-currency)
35. [新华鲜报丨接入首批金融机构 数字人民币跨境服务新进展 — 新华网](https://www.news.cn/20260617/0ffe52402db24b9f95b6187c4265415a/c.html)
36. [数字人民币迎来重大调整 — 中国政府网](https://www.gov.cn/lianbo/202512/content_7053034.htm)
37. [央行：新一代数字人民币运行机制将于2026年1月1日正式启动实施 — 人民网](http://m.toutiao.com/group/7589114302913675819/)
38. [Stablecoins surge past $300 billion — CoinDesk](https://www.coindesk.cc/stablecoins-surge-past-300-billion-forcing-a-reckoning-over-the-dollar-s-future-112895.html)
39. [Tether and Circle control 85% of stablecoin supply — CoinDesk](https://www.coindesk.cc/tether-and-circle-control-85-of-stablecoin-supply-as-market-concentration-stays-near-record-highs-111999.html)
40. [Crypto Assets Monitor Highlights: Q1 2026 — IMF](https://www.imfconnect.org/content/dam/imf/News%20and%20Generic%20Content/GMM/Special%20Features/Crypto%20Monitor%20Q1%202026.pdf)
41. [CoinW研究院周报(2026.9.14-2026.9.20期) — PANews](https://www.panewslab.com/zh/articles/01a0c1d2-77bd-71cb-ba93-d10ddd3c707e)
42. [Chain TVL Tracker: DeFi Capital Committed, By Chain — Blockchain Magazine](https://blockchainmagazine.net/chain-tvl-tracker/)
43. [BNB Chain surpasses Solana in DeFi TVL — CoinDesk](https://coindesk.cc/bnb-chain-surpasses-solana-in-defi-tvl-as-race-for-second-place-tightens-113645.html)
44. [Which Ethereum L2 Wins When You Score TVL, Fees, and Security?](https://www.spotedcrypto.com/defi-layer-2-comparison-2026-arbitrum-base-optimism-zksync/)
45. [Bitcoin — CryptoSlate](https://cryptoslate.com/coins/bitcoin/)
46. [Could AI Agents Be Crypto's First Real Mass Adoption Use Case?](https://www.coinmarketcapa.com/academy/es/article/ai-agents-crypto-first-real-mass-adoption-use-case)
47. [AI Agents Are Starting to Pay for Things in Crypto — 24/7 Wall St.](https://247wallst.com/investing/cryptocurrency/2026/09/18/ai-agents-are-starting-to-pay-for-things-in-crypto-which-coin-do-they-use-xrp-solana-or-usdc/)
48. [How AI and crypto are converging: eight use cases — 21Shares](https://www.21shares.com/en-eu/insights/ai-crypto-convergence-use-cases)
49. [Bybit Sues North Korea and Lazarus Group — PR Newswire](https://www.prnewswire.com/in/news-releases/bybit-sues-north-korea-and-lazarus-group-secures-preliminary-injunction-freezing-stolen-assets-in-landmark-crypto-asset-recovery-effort-302846551.html)
50. [Bybit v. DPRK Lazarus Group — $1.5B Hack Civil Lawsuit (August 2026)](https://avoid.net/bybit-v-dprk-lazarus-group-1-5b-hack-civil-lawsuit-august-2026)
51. [Bitget 凌晨突然被盗 — 新浪财经](https://finance.sina.com.cn/blockchain/roll/2026-09-24/doc-inisyuqn9846431.shtml)
52. [Everything We Know About Bitget's Massive $351M Hack — CoinDesk](https://www.coindesk.cc/everything-we-know-about-bitget-s-massive-351m-hack-118856.html)
53. [Online Scams, Crypto Fraud, and Digital Extortion — U.S. House Homeland Security](https://homeland.house.gov/wp-content/uploads/2026/04/2026-04-21-BSECIP-Hearing.pdf)
54. [数字欧元最新进展 — 新浪财经](https://finance.sina.com.cn/blockchain/2026-09-17/doc-inisayaf4199431.shtml)
55. [欧洲议会批准数字欧元谈判授权 — 北京市商务局](https://sw.beijing.gov.cn/zt/mymcyd/smdtx/202608/t20260824_4834267.html)
56. [警惕对美依赖 欧洲加快数字欧元布局 — 光明网](http://m.toutiao.com/group/7604947414511796774/)
57. [2026全球数字货币新格局：三极分化与秩序重构 — 第一财经](https://m.yicai.com/news/102999946.html)
58. [数字欧元项目迈出实质性步伐 — 中国经济网](http://m.toutiao.com/group/7611689507422732863/)