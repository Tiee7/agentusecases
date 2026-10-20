# 用Perplexity Comet研究公司信息并整理股票观察清单

## 中文

    在浏览器中研究股票并更新观察清单
    一位投资者用Perplexity Comet查看自己的股票观察清单，寻找受美国关税影响的瑞士公司，汇总Reddit和市场评论，并把选出的股票加入Google表格。
    使用的是
    PC
    Perplexity Comet
    他们做了什么
    作者使用AI浏览器Perplexity Comet，以自然语言提出跨标签页任务。Comet查看了他的股票观察清单，列出受美国关税影响的瑞士公司。它还总结了Goehring和Rozencwajg的一篇评论，以及Reddit上排名最高的一篇帖子。随后，他测试了让它把新选出的股票加入Google Sheets观察清单。
    进展与成效
    Comet在几分钟内返回了受关税影响的公司清单，并附上简短解释。作者说结果有时深度不足。他没有展示写入Sheets这一步的结果。
    值得了解
    帖子写于2025年8月，当时Comet仅向Perplexity Max订阅者或受邀用户开放。
    亲自尝试
    使用
    Perplexity Comet
    复制提示词
    打开我在[Google表格链接]中的观察清单，查看每家公司的近期新闻。然后寻找[公司类型，例如受美国关税影响的瑞士企业]，并总结[Reddit社区和新闻网站]对它们的讨论。把你选出的前[数量]家公司加入表格的新标签页，每家附一句理由和来源链接，然后停止并向我展示添加了什么。
    原始来源：https://rhinoinsight.substack.com/p/is-perplexity-comet-the-best-browser

<details><summary>English original</summary>

    Research stocks and update a watchlist in the browser
    An investor uses Perplexity Comet to scan his watchlist, find Swiss companies hit by US tariffs, summarize Reddit and market commentary, and add stock picks to a Google Sheet.
    Done with
    PC
    Perplexity Comet
    What they did
    Using Perplexity Comet, an AI browser, the author asked in plain language for tasks across tabs. Comet went through his stock watchlist and listed Swiss companies hit by the US tariffs. It summarized a Goehring and Rozencwajg commentary and the top Reddit post. He then tested asking it to add new picks to his Google Sheets watchlist.
    How it went
    Comet returned the tariff-affected list with short explanations within a few minutes. The author says the depth of results was sometimes lacking. He shows no result for the Sheets step.
    Worth knowing
    Comet was available only to Perplexity Max subscribers or by invite when the post was written in August 2025.
    Try it yourself
    with
    Perplexity Comet
    Copy prompt
    Open my watchlist in [Google Sheet link] and check each company for recent news. Then find [type of companies, e.g. Swiss firms hurt by US tariffs] and summarize what [Reddit communities and news sites] are saying about them. Add your top [number] picks to a new tab of the sheet with a one-line reason and source link each, then stop and show me what you added.
    Original source: https://rhinoinsight.substack.com/p/is-perplexity-comet-the-best-browser

</details>

## 原作者的方法与来源

https://rhinoinsight.substack.com/p/is-perplexity-comet-the-best-browser
同一自有云浏览器两次Site Unavailable后停止读取；原文与截图未核验。

## 简要分析

商业分数未评定。

### 研究输出与表格写入分开验收

目录描述作者跨标签页研究、摘要和尝试更新观察清单，同时明确没有展示Sheets步骤的结果。不能因为标题写了更新，就认定写入成功。几分钟返回清单和内容有时浅也是转述，缺原文、输出和测量；原文章两次返回Site Unavailable后停止读取。本篇是有依据简报，不把通用功能介绍补成原作者工作流验证。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-stocks-and-update-a-watchlist-in-the-browser)

### 2025年的访问条件不用于今天报价

目录说文章写于2025年8月，仅Max或受邀用户可用是当时背景。后续官方公告已开放免费下载；当前套餐表仍对Comet Assistant查询分层，免费层列为无浏览器agent查询。研究者据此区分浏览器安装与助手运行额度，复制前查看实际账户。原作者订阅成本和用量未知，不把免费下载推成零运行成本，也不照搬旧邀请门槛。

依据：[Srelease](https://www.perplexity.ai/en-GB/changelog/what-we-shipped-october-3rd), [Splans](https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you), [Sdirectory](https://agentusecases.ai/use-case/research-stocks-and-update-a-watchlist-in-the-browser)

### 关税主题只是历史研究线索

本案没有提供公司名单、政策生效日、收入地域、产品税号或财报证据，因此不报告哪些股票现在受益或受损。研究者建议把“关注某主题”与“证实公司业务暴露”分开，每条结论保留事件日期、原始公告、公司披露与尚未验证的因果链。社交帖热度不是经营影响，更不是交易信号；本报告不创建真实投资建议或订单。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-stocks-and-update-a-watchlist-in-the-browser)

### 先在草稿中保留可追溯事实

拟议流程是固定观察清单版本和日期范围，按公司标识核对来源，区分新闻事实、评论观点和研究推断，再生成待审新增行。每行保存公司名称、代码与市场、来源链接、日期、摘要、未知项和去重键；同名代码或不同市场必须明确。研究者建议优先公司原始披露，再用评论补充观点，不把同一消息的转载当多条独立验证。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-stocks-and-update-a-watchlist-in-the-browser)

### 新标签页也需要检查目标和差异

Google说明版本历史可追溯变化，但单元格历史不一定显示行列增删、格式或公式产生的变化；恢复旧版会清除此前部分逐格编辑历史。研究者建议在写入前保存版本标识，明确新标签名称和列映射，写后回读行数、字段与原表未变。权限或冲突不明时保留草稿，不覆盖整表。本轮没有打开或修改任何私人观察清单。

依据：[Ssheets](https://support.google.com/docs/answer/190843?hl=en)

### 本地浏览器不等于研究内容全留本机

官方隐私FAQ说明个人化请求会使用当前标签页和相关浏览历史，部分页面资料可能在Perplexity服务器处理。该资源页含面向未来版本的描述，不将其当全部当前设置的完整清单。研究者建议只提供公开公司资料或虚构观察名单，避免同开账户余额、持仓和私人通信；核对实际页面与连接范围后才考虑接入。本轮没有登录Comet或证券账户。

依据：[Sprivacy](https://www.perplexity.ai/comet/resources/articles/comet-data-privacy-security-faq-s)

### 可验证的是整理服务，不是收益优势

潜在用户是反复整理公开公司信息的研究者，付款人可能是本人或研究团队。商业假设为限定主题资料整理、来源核验和表格维护，按明确交付范围收费；获客可以通过可复核的研究样例，但本案没有客户、报价或复购证据。浏览器助手、普通搜索和表格已有替代，差异需来自来源质量与核对节省。订阅、人工复核、数据许可、维护和获客成本均待测，不能把研究速度当投资收益。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-stocks-and-update-a-watchlist-in-the-browser), [Splans](https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you)

### 减少切换是可能价值，深度仍要人补

自用价值待核实。适用者需要能审查来源、公司标识和时间线；预期减少多页整理和复制，原作者却报告深度有时不足。准备需清楚主题和表头，维护需处理失效链接、重复条目及新旧观点。频率可按资讯更新或定期复核，而非自动高频刷新。错误风险是混淆事实和观点、过期政策、错写表格及误把热门评论当结论。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-stocks-and-update-a-watchlist-in-the-browser)

### 离线清单演练先证明没有漏写错写

用三家虚构公司、固定资料片段和本地空表演练：生成带日期来源的草稿，模拟同名、重复、缺失日期和字段冲突，比较人工答案。预期得到可审阅的研究记录和拟新增行，不涉及买卖或真实账户。本轮未实际运行。若每条都需重新研究、缺出处或表格变更无法精确回读，应停止扩大自动化范围。

依据：[Ssheets](https://support.google.com/docs/answer/190843?hl=en), [Sdirectory](https://agentusecases.ai/use-case/research-stocks-and-update-a-watchlist-in-the-browser)

## 试用准备与预期结果

三家虚构公司、固定来源片段、人工答案与本地表头。
含日期来源的研究记录及待审新增行；本轮未试用、不提供真实买卖建议。
仅依据给定虚构公司与资料，输出公司标识、来源日期、事实、评论观点、推断和未知项。不得把热点推成经营影响或买卖建议。按给定表头生成待审新增行，以标识和来源去重；不连接或修改Google表格，不访问证券账户。

## 来源

- [许可目录及当前云浏览器核验](https://agentusecases.ai/use-case/research-stocks-and-update-a-watchlist-in-the-browser)：作者尝试Sheets但未展示结果；深度不足为目录转述。
- [Comet开放下载公告](https://www.perplexity.ai/en-GB/changelog/what-we-shipped-october-3rd)：2025年10月公告已开放免费下载，不能把2025年8月邀请限制写成现在。
- [Perplexity套餐比较](https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you)：当前浏览器agent查询按套餐限制；免费下载不等于自动化功能免费无限。
- [Comet数据隐私说明](https://www.perplexity.ai/comet/resources/articles/comet-data-privacy-security-faq-s)：个人化请求可使用当前页和相关历史，部分数据服务器处理；不是全离线。
- [Google文件版本与单元格历史](https://support.google.com/docs/answer/190843?hl=en)：可检查变化但部分变化不在单元格历史中，恢复旧版有额外影响。
- [原作者Comet体验文章](https://rhinoinsight.substack.com/p/is-perplexity-comet-the-best-browser)：无法核验原文、截图、作者身份或Sheets实际变化。
