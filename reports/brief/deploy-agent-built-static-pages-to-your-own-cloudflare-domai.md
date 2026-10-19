# 用 Cloudflare Workers 发布 agent 静态页面

本案为经修正的简要分析；不计入完整深研，两轨总分均为待核实。
案例 ID：deploy-agent-built-static-pages-to-your-own-cloudflare-domai
研究时间：2026-10-19T13:35:43.645383+00:00
来源归档：[案例页](https://agentusecases.ai/use-case/deploy-agent-built-static-pages-to-your-own-cloudflare-domai)。

## 完整中文译文

将 Agent 构建的静态网页部署至自有 Cloudflare 域名
作者构建了 getonup 工具，使 Agent 能在自有域名上自动化配置 Cloudflare Workers 与 Zero Trust 安全网关，让团队能够发布带有按日期排序索引的静态 HTML 页面。
使用工具
自建或未命名 Agent
他们做了什么
作者希望获得类似 Claude Artifacts 风格的 HTML 研报展示能力，同时又不希望被锁定在单一模型厂商平台上。为此，他们构建了基于 Cloudflare Workers 的开源项目 getonup。用户只需将 Agent 指向该项目的代码仓库，并要求 Agent 在指定域名下将其部署至自己的 Cloudflare 账户中；Agent 会自动完成环境配置并设置 Cloudflare Zero Trust 以保障站点的访问安全。
进展与成效
该系统能够生成按日期排序的已部署制品（Artifacts）索引页，并支持静态网页部署。作者表示该工具虽然目前功能仍十分简朴，但对他们团队而言已经非常实用，团队成员通常一天发布数个页面。
值得注意
该项目免费且开源，但使用者需要拥有自己的 Cloudflare 账户并提供一个绑定的域名。
亲自尝试
使用
Claude Code
复制提示词
请协助我建立一套通过 Cloudflare Workers 将静态 HTML 页面发布至我自有域名 [yourdomain.com] 的工作流，并通过 Cloudflare Zero Trust 将访问权限限制为仅限 [团队邮箱域名]。每个已发布的页面都应在索引页上生成一条带有日期的条目。在执行任何更改我的账户配置或 DNS 记录的操作之前，向我详细解释 Cloudflare 的每一步变更并向我展示确切的执行命令或配置内容。当我能够成功发布一个测试页面，并在登录鉴权后于索引页中查看到该页面时，任务即告完成。
原始来源：https://news.ycombinator.com/item?id=49941666

## 作者方法与出处

本次未重新取得外链原帖；仅使用已授权归档转述。旧包声称的读取时间和短摘不被当成本次独立核验。

The archive reports that the author built getonup and pointed an agent to its repository.
归档转述作者构建 getonup，并让 agent 读取其仓库。

The agent was asked to configure the project on a chosen Cloudflare account and domain, including Zero Trust.
要求 agent 在选定的 Cloudflare 账户与域名配置项目及 Zero Trust；具体内部配置未核。

以上为聚合归档转述摘要，具体实现不超出已读材料。

## 我们的分析

结论：仅建议受控试点。先核访问边界与完整运营成本
团队初步使用可作为设计线索；未经部署、权限与配额验收，不认证安全隔离或免维护。

- author_claim：归档称作者构建 getonup，让 agent 对选定 Cloudflare 账户和域名配置 Workers 与 Zero Trust，生成按日期排序的页面索引；作者与团队自述经常一天发布数页。（archive）

- verified：当前官方计费区分 Worker 调用、普通静态资产与 KV；免费层有范围和上限，Paid 最低费不是总费用封顶。（workers, kv）

### 业务、交付与替代方案
可提供团队发布入口、索引与受控访问配置的交付，不应宣传物理私有部署或任何工具无缝迁移。KV、邮箱域规则、OTP 和一键脚本仅是可选设计；未读代码不能归为作者实装。需要验收默认域、预览、资产和所有路由的访问策略，不能因登录页存在就保证无旁路。

### 自用净收益与证据边界
自有域名仍是托管云端；减少服务器补丁工作不等于免 DNS、域名、授权、备份与额度维护。三小时设置、每次省五分钟若只比毛时间是36次，但缺频次、复核维护和现金，不认证二至三个月净回本。净收益以 25×(累计毛省时−设置−复核返工维护)−新增现金 计算。

### 自用价值

有团队初步使用转述，没有固定普通人的频次、完整净收益或安全实测。
- 人群：固定画像 solo-generalist-v1：普通通用知识工作者；专业或高频客户仅作敏感性场景。
- 用途：在自有域名发布静态成果并管理受控访问与索引。
- 收益：可能降低平台切换成本，实际可移植性与净节省未测。
- 设置：设置工时未实测，须记录初次配置、授权与排错。
- 维护：维护、逐项复核与返工均未实测；自用边界每周维护不超过 1 小时、月新增现金不超过 USD 20。
- 频次：团队经常日发数页为作者自述；普通人的发布量未知。
- 隐私：内容托管 Cloudflare，可能还经模型与身份服务。自有域名不是本地私有；实际保护范围、保留与数据地域未知。
- 错误风险：错误 Access/DNS 或预览入口可能暴露内容；配额、部署和续期仍需维护。没有99.9%工作流可用性证明。

### 双轨评分
每维 0–4，满分 4。1/3 分须有中间锚点理由；缺证为 null/unknown；简报两轨总分始终为 null。

commercial：total=null
- demand_payment：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- acquisition：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- delivery_economics：2 / low。在透明报价、工时、域名与额度假设下有正贡献；未知费用与全年履约风险未测，仅有限规划支持。
- differentiation：2 / low。归档描述跨模型的自有发布入口与索引便利，缺对照和独有资产，仅限定流程差异。
- validation_replication：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。

personal：total=null
- audience_frequency：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- net_benefit：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- reliability：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- setup_maintenance：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- cost_data_control：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。

### 单位经济：仅为可复算情景，未获真实订单
商业画像：4 周、最多 40 小时、总现金预算 USD 200；人工机会成本 USD 25/小时。月度摊销不等于四周预付现金。

自有域名静态成果发布与访问配置交付（规划）
单位：一套托管云端发布入口配置，不含物理私有部署承诺。USD 报价 350.0；API/模型预算 5.0；人工 125.0；其他变动费 null（未知）；获客 50.0；月交付量 2.0；月固定预算 20.0。
已知项变动成本 180.0；单位贡献 170.0；月贡献 320.0。若每单位未知其他费用为 x，则月贡献还应减去 2.0x。
四周已列项现金 130。遗漏现金合计不超过 70 才符合 USD 200 预算。
人工125=5小时；月贡献2×(350−5−125−50)−20=320−2x，现金2×(5+50)+20=130。固定20为软件测试规划，不是完整官方报价；域名、Access和其他用量未核费用须另计。 所有报价、销量、API预算、获客费与工时均为未测试情景，人工按 USD 25/小时；模型/API预算不等于单位调用实测价。客户生产许可及既有设备由客户承担，不含在服务商测试预算内；服务商仍未核的付款手续费、税费、超额用量及额外预付须另计，不以 null 当 0。已知项贡献不是实际利润或订单证明。

年度静态成果基础维保（每月新增年约批次规划）
单位：一个新签年约；需承担未来全年履约，不等于月度续费收入。USD 报价 120.0；API/模型预算 1.0；人工 25.0；其他变动费 12.0；获客 20.0；月交付量 3.0；月固定预算 15.0。
已知项变动成本 58.0；单位贡献 62.0；月贡献 171.0。仍需扣未列出的履约费用。
四周已列项现金 114。遗漏现金合计不超过 86 才符合 USD 200 预算。
人工25=1小时的全年基础维保假设，不代表足够；12是每新年约域名年费预算而非通用官方价。本月新签3份年约，则贡献3×(120−1−25−12−20)−15=171，现金3×(1+12+20)+15=114。未来全年维护、续期和未列服务成本仍须扣除。 所有报价、销量、API预算、获客费与工时均为未测试情景，人工按 USD 25/小时；模型/API预算不等于单位调用实测价。客户生产许可及既有设备由客户承担，不含在服务商测试预算内；服务商仍未核的付款手续费、税费、超额用量及额外预付须另计，不以 null 当 0。已知项贡献不是实际利润或订单证明。

### 反馈、反证与限制
归档中的作者叙述是聚合转述，无独立直接使用者效果样本；无证据不等于差评。
现有静态托管与文档发布可能满足需求；免费额度不能替代权限与维护验收。
本次未重新取得外链原帖；仅使用已授权归档转述。旧包声称的读取时间和短摘不被当成本次独立核验。 HN 原帖和 getonup 代码本次未读；没有独立复现、SLA或实际账单。旧包复核时间与封包冲突，未反猜历史时刻。当前来源不证明作者当时采购。

### 试用模板
源站模板为编辑建议，不是作者实际 prompt：
Help me set up a way to publish static HTML pages to my own domain [yourdomain.com] using Cloudflare Workers, with access limited to [team email domain] through Cloudflare Zero Trust. Each published page should get a dated entry on an index page. Walk me through each Cloudflare change and show me the exact commands or config before running anything that changes my account or DNS. You're done when I can publish a test page and see it listed on the index behind login.

准备：仅用合成或获准脱敏输入，先检查所需账户、许可和额度；本轮未登录、调用付费 API 或创建凭据。
工具：未具名作者 agent、getonup、Cloudflare Workers/Zero Trust；Claude Code 是源站推荐。
自编合成演练，未实测：
对合成静态页面拟定发布流程。先列全部域名、默认/预览路由、资源、访问规则、回滚与费用，并展示拟改配置。不得实际登录、改 DNS、安全权限、创建凭据或部署。明确检查未授权访问与所有备用入口，未测试前不得承诺私有或高可用。

形成部署/路由/权限/用量验收清单，未改 DNS、账户或发布页面。

### 下一步与停止条件
离线检查配置方案和全部访问入口，用合成页面计划最小验收；真实账户变更应单独获得授权。
若不能验证全部入口受控，或实际维护/域名/用量超预算，停止交付安全承诺。

### 实际读取凭据
- [Deploy agent-built static pages to your own Cloudflare domain](https://agentusecases.ai/use-case/deploy-agent-built-static-pages-to-your-own-cloudflare-domai)，approved_git_archive，2026-10-19T13:35:43.645383+00:00。本次离线实读归档正文；归档是聚合站转述，不能等同外链原作者已实读。
- [Workers 当前计费](https://developers.cloudflare.com/workers/platform/pricing/)，public_web_read，读取区间 2026-10-19T13:18:00+00:00 至 2026-10-19T13:30:00+00:00（精确秒未知）。Free 为每日十万次 Worker 调用，Paid 账户最低每月 USD 5，超额另计。普通直接静态资源请求与执行 Worker 分开；启用 Workers Caching 的缓存请求仍按请求费计。
- [KV 额度](https://developers.cloudflare.com/kv/platform/pricing/)，public_web_read，读取区间 2026-10-19T13:18:00+00:00 至 2026-10-19T13:30:00+00:00（精确秒未知）。Free 每日读十万键，写、删、list 各一千，总存储1GB；每天 UTC 零点重置，超出该类操作失败。若经 KV 读 HTML，仍需计相关用量。
