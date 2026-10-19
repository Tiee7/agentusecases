# 用 Claude 将个人投资记录表改成手机和电脑可用的界面

## 中文

    用Claude制作的投资组合追踪器记录个人投资
    发帖者用Claude制作了个人投资组合追踪器，以资金加权收益率追踪定投和一次性投资，并辅助研究。
    使用的是
    Claude
    他们做了什么
    发帖者先在Excel中梳理配置逻辑，然后使用网页版Claude将它转成可在笔记本电脑和手机上运行的PWA/HTML投资组合追踪器。应用有平衡和修正两种模式，依据目标区间把定投和一次性投入分配到权重不足的持仓，并使用一个按排名排列的股息分组；发帖者仍手动输入投资组合数据。
    进展与成效
    他们表示，这个追踪器现在适合自己的长期投资流程，并分享了在线演示和视频，但当时仍使用静态手动录入数据，没有券商同步。他们尚未整合Kite或券商API，部分原因是认为Kite API约需2,000印度卢比。
    值得注意
    总共约花了一周，其中在配置结构理清后，将Excel逻辑转成PWA花了2至3天。
    亲自尝试
    使用Claude
    复制提示词
    帮我制作一个可自行运行的简单个人投资组合追踪器。它应记录我在[基金或股票列表]中的每月定投和一次性投入，然后计算每项持仓及整个投资组合的资金加权收益率（XIRR）。我会粘贴一组交易样本：[日期、金额、当前价值]。交付可用代码或电子表格公式、更新说明，并用样本数据测试显示结果后，任务才算完成。
    原始来源：https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude

<details><summary>English original</summary>

    Track personal investments with a Claude-built portfolio tracker
    The poster built a personal portfolio tracker with Claude that tracks SIPs and lump sums using money-weighted returns, and helps with research.
    Done with
    CL
    Claude
    What they did
    The poster first worked out their allocation logic in Excel, then used Claude on the web to turn it into a PWA/HTML portfolio tracker that runs on laptop and phone. The app has balanced and correction modes, allocates SIP and lump-sum money to underweight holdings versus target bands, and uses a ranked dividend bucket; the poster still enters portfolio data manually.
    How it went
    They say the tracker now works for their long-term investing process and shared a live demo plus a video, but it was still using static manual entries with no broker sync. They had not integrated Kite or broker APIs, partly because Kite API would cost about ₹2,000.
    Worth knowing
    It took about a week overall, with 2–3 days to turn the Excel-based logic into a PWA after the allocation structure was figured out.
    Try it yourself
    with
    Claude
    Copy prompt
    Help me build a simple personal investment portfolio tracker I can run myself. It should record my monthly SIP contributions and one-time lump-sum investments in [list of funds or stocks], then calculate my money-weighted return (XIRR) for each holding and for the whole portfolio. I'll paste in a sample of my transactions: [dates, amounts, current values]. You're done when I have working code or a spreadsheet formula set, plus instructions to update it, and a test using my sample data that shows the results.
    Original source: https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude

</details>

## 原作者的方法与来源

来源：[I developed personal portfolio tracker with Claude](https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude/)

The author developed allocation rules in Excel before asking Claude on the web to make a PWA/HTML interface.
作者先在Excel中梳理配置规则，再让网页版Claude制作PWA/HTML界面。

They manually enter static data, with no broker integration, and report about a week of work including two to three days building the interface.
其手工输入静态数据，没有券商集成；自述总体约一周，其中界面开发两至三天。

## 简要分析

商业分数未评定。

### 先作为自用原型理解

作者的价值在于把已有表格规则转成适合自己查看的手机和电脑界面。原帖能支持开发流程和手动输入方式，却没有可检查的当前代码、计算测试、真实省时或收入。本轮公开演示显示404，仓库和视频普通读取各失败两次后停止。证据不足以判断现成工具能否稳定复用，因此保存未评分简报，不以“做出来了”推定商业产品成熟。

依据：[Sauthor](https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude/), [Sdemo](https://thepeakyblinderr.github.io/Wealth-Manager/)

### XIRR与价格需分开核验

目录简介称追踪资金加权收益率，原帖实际可读内容中，IRR出现在另一用户提出的功能建议里；未见作者确认已经实现。忠实保留目录原文与译文，同时将已实现XIRR标为待核实。作者提到Kite约2,000卢比是其当时说法，现行官方页列免费Personal组合管理，以及含实时和历史数据的Connect每月500卢比，不能把旧说法当现在接入必需费用。也不能据免费层推断完整跨券商同步免费可用。

依据：[Sdirectory](https://agentusecases.ai/use-case/track-personal-investments-with-a-claude-built-portfolio-tra), [Sauthor](https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude/), [Skite](https://zerodha.com/products/api/)

### 手动记录与投资建议的区别

原帖说平衡和修正模式按目标区间整理资金，股息分组按权重不足程度排名。这些是作者个人规则，不是经过验证的投资策略。本报告只研究记录、计算与界面构建，不推荐买卖任何资产，也不代接券商或下单。较可复用的部分是日期金额校验、持仓快照、按目标分组和导出备份；计算必须对照已知样本，不能依赖模型解释看起来合理。跨币种、分红再投资、费用及终值日期需事先定义口径。

依据：[Sauthor](https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude/), [Sxirr](https://support.microsoft.com/en-us/excel/functions/xirr-function)

### 付款人和替代路径仍未知

可能使用的是已有表格、想在手机上便捷查看的个人投资者。原帖没有付费客户或售卖计划，评论赞美界面也不代表购买意愿。现有Excel公式已经能处理不规则现金流；若只是把表格换外观，收费空间要另证。定制服务需要承担导入清洗、公式复核、设备迁移和长期维护成本，不能只按生成HTML的两三天估算全部交付。尚缺工作量和报价样本，本例不填商业分数或假利润。

依据：[Sauthor](https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude/), [Sxirr](https://support.microsoft.com/en-us/excel/functions/xirr-function)

### 自用收益与维护负担

对愿意定期手动录入的人，专用界面可能更易坚持记录，作者也说倾向按月查看而非接入实时数据；没有测量净节时。旁观者建议按退休、住房等目标分组，属于需求线索，不是独立实测结果。手动方式的代价是更新遗漏、交易重复和终值过期；网页可打开不等于数据可恢复。公开演示后来不可用提醒我们，应把源文件、数据导出和恢复步骤作为验收项，不将一个外部链接当永久资产。

依据：[Sauthor](https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude/), [Sdemo](https://thepeakyblinderr.github.io/Wealth-Manager/)

### 先用合成数据核对

投资账户和持仓属于敏感资料，测试只用虚构现金流，不上传真实账单、账户号或凭据。需要接口时，应先明确最小权限与数据用途；能查询组合的接口也可能包含下单能力，不能因为是“追踪器”就默认安全只读。本轮没有登录金融账户、创建密钥或运行真实交易。演示中的目标权重只作为界面测试数据，不是面向用户的配置建议。

依据：[Skite](https://zerodha.com/products/api/), [Sxirr](https://support.microsoft.com/en-us/excel/functions/xirr-function)

### 可执行的离线验收

先用两笔合成现金流核计算：第0天投入100，第365天终值110，对应年化内部收益率10%；再验证无正负现金流、日期不一致和重复记录时清楚报错。多笔定投应按日期逐笔计算，不能用简单平均单项收益率代替组合结果。保存输入、公式、输出与版本，人工抽核后才讨论是否重建工具；若数据难恢复、公式边界不明或复核比表格更费时，先继续使用已有表格。离线示例只是算法验收，不能证明作者应用正确或投资赚钱。

依据：[Sxirr](https://support.microsoft.com/en-us/excel/functions/xirr-function), [Sauthor](https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude/)

## 试用准备与预期结果

虚构现金流和已知正确结果；不含真实投资与个人资料。
可核对的日期现金流表、公式、错误提示与备份说明；非真实投资建议。

只处理这组虚构现金流：2025-01-01投入100（负值），2026-01-01终值110（正值）。给出XIRR公式和日期口径，核对结果10%。再列无正现金流、日期错误、重复记录的拒绝条件。不要添加买卖建议，不连接账户、不上传数据、不创建凭据。输出输入校验、计算和导出恢复清单；任何未测试功能明确标记。

## 来源

- [目录案例和试用模板](https://agentusecases.ai/use-case/track-personal-investments-with-a-claude-built-portfolio-tra)：目录全文保持原样；XIRR和2,000卢比说法另行核验。
- [作者的手动投资记录工具讨论](https://www.reddit.com/r/mutualfunds/comments/1rssbp5/i_developed_personal_portfolio_tracker_with_claude/)：作者说使用Claude web/free，先Excel后PWA，手动录入无券商同步；XIRR在评论中是建议而非已确认功能。
- [Zerodha现行API产品价目](https://zerodha.com/products/api/)：Personal免费含组合管理；Connect含实时与历史数据500卢比/月，不能把作者2,000说法当现价。
- [Microsoft XIRR官方说明](https://support.microsoft.com/en-us/excel/functions/xirr-function)：按不规则现金流日期计算，至少正负现金流，365日规则和失败状态；不是作者实现测试。
- [作者演示当前404](https://thepeakyblinderr.github.io/Wealth-Manager/)：实际只看到GitHub Pages 404，不能试用或确认计算能力。
- [原作者相关公开入口未取得](https://github.com/thepeakyblinderr/Wealth-Manager)：未取得可用内容，不计成功来源。
- [原作者相关公开入口未取得](https://youtu.be/lUDW27MgvDU)：未取得可用内容，不计成功来源。
