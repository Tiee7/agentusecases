# 用 Claude 和 Supabase 整理个人人脉档案

本案为经修正的简要分析；不计入完整深研，两轨总分均为待核实。
案例 ID：enrich-and-store-contacts-in-a-personal-crm
研究时间：2026-10-19T13:35:43.718507+00:00
来源归档：[案例页](https://agentusecases.ai/use-case/enrich-and-store-contacts-in-a-personal-crm)。

## 完整中文译文

在个人 CRM 中富集并存储联系人档案
Claude 通过 MCP 连接至 Supabase 数据库，接收姓名与 LinkedIn 链接后，通过 Harmonic 自动富集背景资料，并将记录写入个人 CRM 数据库。
使用工具
CL
Claude
他们做了什么
作者搭建了一个 Supabase 数据库，并通过一个提供 query、insert、update 和 delete 四项工具的 MCP 服务将其连接至 Claude。Markdown 文件使用通俗自然语言描述具体业务工作流。当用户提供一个姓名与 LinkedIn 链接时，Claude 会读取该工作流并调用 Harmonic 接口获取其职位、所属公司、工作履历及推断出的技能标签。同时，它还会检查 Granola 中提及该联系人的会议笔记并自动完成挂载关联。
进展与成效
数秒之内即可生成一份完整的人物背景档案，无需作者手动填写任何字段。系统支持跨技能、备忘、职位与公司进行多维度联合检索。此外，在每次 Granola 会议纪要同步后，系统会自动标记出出现在文字记录中但尚未录入 CRM 的联系人，提醒作者跟进建档。
亲自尝试
使用
Claude
复制提示词
我将向你提供一个联系人的姓名与 LinkedIn 链接：[姓名] 和 [LinkedIn 链接]。请使用我已连接的背景富集工具补充该档案，随后将包含姓名、公司、职位、所在地区及个人主页链接的记录保存至我已连接数据库的 [联系人表名] 表中。在实际写入数据前先向我展示拟保存的记录内容；当确认记录保存成功且该行数据已存在后停止执行。
原始来源：https://jax.substack.com/p/uncovered-bookmarks-23-building-a

## 作者方法与出处

本次未重新取得外链原帖；仅使用已授权归档转述。旧包声称的读取时间和短摘不被当成本次独立核验。

The archive describes a custom four-tool database interface and Markdown workflow instructions.
归档描述自建四工具数据库接口和 Markdown 流程说明。

Claude uses Harmonic enrichment and links matching Granola notes; after sync it flags people missing from the CRM.
Claude 富集资料并关联匹配笔记；同步后标记未建档者，不据此推断自动新增。

以上为聚合归档转述摘要，具体实现不超出已读材料。

## 我们的分析

结论：仅建议受控试点。先核同名匹配、授权与数据流
适合先做合成资料原型；自动建档、准确率和净收益无证，不支持无监督客户服务承诺。

- author_claim：归档称 Claude 通过自定义四工具 MCP 接 Supabase，按 Markdown 工作流用 Harmonic 富集角色、公司、履历和推断技能，关联 Granola 会议笔记。（archive）

- author_claim：归档声称数秒形成档案，并在 Granola 同步后标记尚未入库者；标记不等于无需确认自动新增。没有准确率或独立效果日志。（archive）

### 业务、交付与替代方案
整合公开职业线索和本人获准会议笔记有便利，但身份匹配与推断技能需要人工核验。没有依据从作者职业推定高级采购特权，也不以泛供应商定位推断 Harmonic 高价或廉价。Harmonic 价格、可用权限和作者订阅均未知；旧稿列的泛名称替代品移除，未核现用产品不推荐为便宜兼容替代。

### 自用净收益与证据边界
猎头、咨询顾问等专业高频场景不替换普通画像。五小时设置与每周省四十分钟只是未测试毛时间假设；未扣订阅、复核、维护、清洗不能承诺两个月回本。净周收益=25(G−M)−C，设置成本25S；正值才可算连续回本。

### 自用价值

无固定画像频次、全成本、身份匹配或数据控制实测。
- 人群：固定画像 solo-generalist-v1：普通通用知识工作者；专业或高频客户仅作敏感性场景。
- 用途：查询与整理获准联系人记录，待审后写入并核对结果。
- 收益：可能减少手工整理；不保证匹配、会议归属或推断技能正确。
- 设置：设置工时未实测，须记录初次配置、授权与排错。
- 维护：维护、逐项复核与返工均未实测；自用边界每周维护不超过 1 小时、月新增现金不超过 USD 20。
- 频次：普通人实际维护人脉资料频次未知，专业用户需另测。
- 隐私：联系人和私人会议笔记可能流经模型、Supabase、Harmonic 与 Granola。最小权限、授权范围、导出/删除和留存未核，云数据库不是无约束私有库。
- 错误风险：同名误匹配、推断技能当事实、误删和重复；须逐条核来源并保持可恢复。

### 双轨评分
每维 0–4，满分 4。1/3 分须有中间锚点理由；缺证为 null/unknown；简报两轨总分始终为 null。

commercial：total=null
- demand_payment：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- acquisition：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- delivery_economics：2 / low。透明情景保留有限正贡献，但工时、数据采购和客户需求未验证，月维护贡献很薄。
- differentiation：2 / low。归档描述富集、会议笔记与自然语言检索组合便利；没有对照或可积累壁垒，只支持有限差异。
- validation_replication：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。

personal：total=null
- audience_frequency：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- net_benefit：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- reliability：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- setup_maintenance：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。
- cost_data_control：null / unknown。目前资料不足以支持该维锚点；未测试并不等于表现为零。

### 单位经济：仅为可复算情景，未获真实订单
商业画像：4 周、最多 40 小时、总现金预算 USD 200；人工机会成本 USD 25/小时。月度摊销不等于四周预付现金。

个人 CRM 集成配置交付（规划）
单位：一套获准数据的辅助配置，不承诺无人自动建档。USD 报价 300.0；API/模型预算 10.0；人工 125.0；其他变动费 null（未知）；获客 45.0；月交付量 2.0；月固定预算 20.0。
已知项变动成本 180.0；单位贡献 120.0；月贡献 220.0。若每单位未知其他费用为 x，则月贡献还应减去 2.0x。
四周已列项现金 130。遗漏现金合计不超过 70 才符合 USD 200 预算。
人工125=5小时；月贡献2×(300−10−125−45)−20=220−2x，现金2×(10+45)+20=130。固定20为服务商沙箱月付预算；客户生产Claude/Granola/Harmonic/Supabase另付，服务商如需这些额外许可须加计。 所有报价、销量、API预算、获客费与工时均为未测试情景，人工按 USD 25/小时；模型/API预算不等于单位调用实测价。客户生产许可及既有设备由客户承担，不含在服务商测试预算内；服务商仍未核的付款手续费、税费、超额用量及额外预付须另计，不以 null 当 0。已知项贡献不是实际利润或订单证明。

联系人数据健康维护（规划）
单位：一个客户月的抽查和维护，不含删除未授权记录。USD 报价 70.0；API/模型预算 5.0；人工 37.5；其他变动费 null（未知）；获客 15.0；月交付量 3.0；月固定预算 15.0。
已知项变动成本 57.5；单位贡献 12.5；月贡献 22.5。若每单位未知其他费用为 x，则月贡献还应减去 3.0x。
四周已列项现金 75。遗漏现金合计不超过 125 才符合 USD 200 预算。
人工37.5=1.5小时；月贡献3×(70−5−37.5−15)−15=22.5−3x，现金3×(5+15)+15=75。Granola/Harmonic实际资格、付款周期和用量未核；不能从客户已有账户推服务商没有附加费。 所有报价、销量、API预算、获客费与工时均为未测试情景，人工按 USD 25/小时；模型/API预算不等于单位调用实测价。客户生产许可及既有设备由客户承担，不含在服务商测试预算内；服务商仍未核的付款手续费、税费、超额用量及额外预付须另计，不以 null 当 0。已知项贡献不是实际利润或订单证明。

### 反馈、反证与限制
归档中的作者叙述是聚合转述，无独立直接使用者效果样本；无证据不等于差评。
现有联系人/笔记搜索也可能满足需求；数据富集许可和持续清洗可能比模型成本更重要。
本次未重新取得外链原帖；仅使用已授权归档转述。旧包声称的读取时间和短摘不被当成本次独立核验。 Substack 原文本次未读；未核 Harmonic 当前报价与作者订阅，无95%准确率、自动增网、免维护、可复现经营或私人资料操作。

### 试用模板
源站模板为编辑建议，不是作者实际 prompt：
I'm going to give you a person's name and LinkedIn URL: [name] and [LinkedIn URL]. Enrich the profile using my connected enrichment tool, then save a record to the [contacts table name] table in my connected database with name, company, role, location, and profile link. Show me the record before you write it, and stop once it's saved and you've confirmed the row exists.

准备：仅用合成或获准脱敏输入，先检查所需账户、许可和额度；本轮未登录、调用付费 API 或创建凭据。
工具：Claude、自建 MCP、Supabase、Harmonic、Granola；不要把官方开发MCP直接当面向客户的四工具接口。
自编合成演练，未实测：
仅使用虚构姓名、职业与会议记录。逐字段注明来源，推断技能单列，不猜私人信息；同名或来源冲突交人工。展示拟写记录及关联笔记并等待明确批准，未经批准不得新增、修改或删除；同步发现未建档者只列候选。演练重复、误匹配与回滚，不上传真实会议。

合成联系人的候选匹配、来源和待写草稿，不接真实会议或数据库。

### 下一步与停止条件
设计脱敏匹配样本、人工参考记录和回滚规则，核实际供应商资格及全费用后再决定接入。
若同名错误不可发现、会议授权不足或持续维护吃完贡献，停止自动写入方案。

### 实际读取凭据
- [Enrich and store contacts in a personal CRM](https://agentusecases.ai/use-case/enrich-and-store-contacts-in-a-personal-crm)，approved_git_archive，2026-10-19T13:35:43.718507+00:00。本次离线实读归档正文；归档是聚合站转述，不能等同外链原作者已实读。
- [Supabase 计划](https://supabase.com/pricing)，public_web_read，读取区间 2026-10-19T13:18:00+00:00 至 2026-10-19T13:30:00+00:00（精确秒未知）。Free 含500MB数据库、1GB文件存储等限制，闲置一周可能暂停；Pro 每月 USD 25起，附加计算和资源另算。非作者账单。
- [Supabase 官方 MCP 边界](https://supabase.com/docs/guides/ai-tools/mcp)，public_web_read，读取区间 2026-10-19T13:18:00+00:00 至 2026-10-19T13:30:00+00:00（精确秒未知）。官方开发 MCP 有项目范围、只读和工具组控制，并不等同作者自建 query/insert/update/delete 四工具接口；应最小权限并审查工具调用。
- [Granola 当前计划](https://www.granola.ai/pricing)，public_web_read，读取区间 2026-10-19T13:18:00+00:00 至 2026-10-19T13:30:00+00:00（精确秒未知）。Basic 免费且历史限30天；Business 显示每人每月 USD 14，含更广历史/集成/API。未核结账支付周期，不能当作者历史方案或十至十八美元通用成本。
