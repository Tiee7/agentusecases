# 用Operator搜集YouTube创作者资料并整理名单

## 中文

    用浏览器agent收集网红名单
    Operator浏览网页收集网红资料，但被Google表格和Excel的登录挡住，因此任务只完成了一部分。
    使用的是
    Operator
    他们做了什么
    发帖者给OpenAI Operator布置了一项浏览器任务：找出50位受欢迎的财经YouTube网红，收集LinkedIn资料、电子邮件地址和简短的频道介绍，再整理成表格。Operator自主打开Bing、访问网页并尝试使用在线表格工具，但卡在Google表格和Excel登录上；用户在旁观察，20分钟后发现它开始编造联系方式而不是核实，于是停止了任务。
    进展与成效
    大约20分钟后，它只生成了18行网红资料，尽管已经在三页内容中查看了70多位网红。表格格式没有问题，但LinkedIn资料和邮件地址是编造的，作者认为它太慢、错误太多，不实用。
    值得了解
    主要问题是速度和登录受阻：每次点击或滚动要花1至2秒，没有就Google表格或Excel请求帮助，大约浪费了5分钟。
    亲自尝试
    使用
    Operator
    复制提示词
    寻找[数量]位在[平台]发布内容、粉丝数大约在[范围]内的[细分领域]网红。为每位收集姓名、主页链接、粉丝数量，以及已公开列出的联系方式（如果有）。在聊天中用表格展示结果，以避开登录障碍；如果遇到登录或验证码，请停下来询问我，不要尝试绕过。
    原始来源：https://www.reddit.com/r/ChatGPTPromptGenius/comments/1i8l5lf

<details><summary>English original</summary>

    Gather a list of influencers with a browser agent
    Operator browsed the web to collect influencer information but got blocked by Google Sheets and Excel sign-ins, so the task was only partly completed.
    Done with
    OP
    Operator
    What they did
    The post author gave OpenAI Operator a browser task: find 50 popular financial YouTube influencers, collect LinkedIn info, email addresses, and a short channel summary, then put it into a table. Operator autonomously opened Bing, visited pages, and tried to use online spreadsheet tools, but got stuck on Google Sheets and Excel sign-ins; the human watched, then stopped it after 20 minutes when it began inventing contact details instead of verifying them.
    How it went
    It produced only 18 influencer rows after about 20 minutes, even though it had looked at 70+ influencers across three pages. The table formatting worked, but the LinkedIn information and emails were made up, and the author judged it too slow and error-prone to be useful.
    Worth knowing
    The main catch was speed and blocked sign-ins: each click or scroll took 1–2 seconds, and failing to ask for help with Google Sheets or Excel cost roughly five minutes.
    Try it yourself
    with
    Operator
    Copy prompt
    Find [number] influencers in [niche] who post on [platform] and have roughly [follower range] followers. For each, collect their name, profile link, follower count, and a public contact method if one is listed. Present the results as a table in the chat so we avoid sign-in walls, and stop and ask me if you hit a login or CAPTCHA instead of trying to get around it.
    Original source: https://www.reddit.com/r/ChatGPTPromptGenius/comments/1i8l5lf

</details>

## 原作者的方法与来源

原帖与补充帖子在此前受限Reddit，本轮不访问、不绕过，未取得作者表格和逐项核实记录。

[原始链接](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1i8l5lf)

## 简要分析

商业分数未评定。

### 18行不等于18条有效线索

目录把格式正确与联系资料错误分开。作者看到70多位也不表示逐一完成核实，更不能用18除以50计算准确率；缺少真实输出与正确答案。本案是特定历史体验，不代表当前Operator或继任产品的一般水平。

依据：[Sdirectory](https://agentusecases.ai/use-case/gather-a-list-of-influencers-with-a-browser-agent)

### 先确认频道身份，再匹配其他主页

拟议记录稳定频道ID、主页链接、显示名称、观测日期和领域依据。LinkedIn匹配需要频道或本人公开页面的对应证据，仅同名、相似头像或行业相同不够。无法确认时保留未知，不为了列完整而创建一个看似合理的链接。

依据：[Schannel](https://developers.google.com/youtube/data/reference/rest/v3/channels)

### 公开联系方法必须确实出现

记录所有者公开提供的业务邮箱、表单或经纪联系人及用途标签。没有列出就写未提供或未取得，不按常见邮箱格式猜测，也不把私人地址用于商务名单。找到公开邮箱不等于得到发送任意内容的授权。

依据：[Scontact](https://support.google.com/youtube/answer/57955?hl=en)

### 粉丝数不是销售能力

记录数字的来源、日期与显示精度，隐藏或取整不填精确值。领域匹配还需查看可见内容，不能仅靠频道名称。粉丝、观看量和互动都不直接等于合作转化、广告报价或品牌安全，本案没有这些商业结果。

依据：[Schannel](https://developers.google.com/youtube/data/reference/rest/v3/channels)

### 先给聊天表或本地文件，避免不必要登录

目录模板已经改成聊天中展示表格，减少对在线表格账号的依赖。流程可先输出研究结果，用户确认目的地后再写入获准系统。登录受阻要及时说明，不能在无法完成写表时改为编造数据或声称交付成功。

依据：[Sdirectory](https://agentusecases.ai/use-case/gather-a-list-of-influencers-with-a-browser-agent)

### 候选服务应按已核实资料收费

潜在付款人是需要创作者合作研究的品牌或代理机构，但本案没有客户付款或持续需求规模。候选交付是带来源的短名单和缺项说明，获客验证可以展示合成样本及质量标准；本轮不联系任何创作者或品牌，也不承诺合作转化。

依据：[Sdirectory](https://agentusecases.ai/use-case/gather-a-list-of-influencers-with-a-browser-agent)

### 核验和返工需计入单位成本

成本由搜索、页面读取、身份交叉核实、联系字段核验、去重与更新组成，模型或点击费用只是部分。计时应比较同一字段范围与质量门槛；作者20分钟缺完整基线，不推导利润、时薪或固定预算门槛。人工能够快速发现编造，也仍要计算返工时间。

依据：[Sdirectory](https://agentusecases.ai/use-case/gather-a-list-of-influencers-with-a-browser-agent)

### 平台原生信息与授权API各有范围

少量名单可以直接查看公开频道信息；已有合规API接入时可读取支持的元数据，但不能假设API能提供所有商务联系人。没有授权不新建凭据或绕限制。专业数据库也需检查更新时间和来源，不把购买名单当真实性保证。

依据：[Schannel](https://developers.google.com/youtube/data/reference/rest/v3/channels), [Scontact](https://support.google.com/youtube/answer/57955?hl=en)

### 适合愿意复核的重复研究

自用者可以先确定细分领域、地域、内容类型和数量上限，再检查少量结果。设置包括字段定义与缺失状态；维护包括改名、地址变化和重复频道。主要风险是错认人、无依据联系方式与将旧数据当当前数据，频率应由实际合作计划决定。

依据：[Sdirectory](https://agentusecases.ai/use-case/gather-a-list-of-influencers-with-a-browser-agent)

### 用缺邮箱和同名样本验规则

准备三条虚构频道卡片：一条公开商务邮箱、一条没有邮箱、一条与另一人同名。只整理来源和字段，不访问账号、不推测、不外联。预期是缺项保持未知且同名不自动合并，本轮没有运行真实网红搜集。

依据：[Sdirectory](https://agentusecases.ai/use-case/gather-a-list-of-influencers-with-a-browser-agent)

## 试用准备与预期结果

三条虚构频道资料，不含真实私人信息。
带来源的字段表，未提供邮箱保持未知；不外联，未实测。
只整理这三条虚构频道资料，保留频道ID和来源。仅记录明确提供的商务联系方式，缺失写未知。同名不自动合并，不猜邮箱或链接，不发送消息。

## 来源

- [许可目录现场正文](https://agentusecases.ai/use-case/gather-a-list-of-influencers-with-a-browser-agent)：许可目录转述50人目标、18行结果、约20分钟和联系方式编造；未取得原帖或原始表格。
- [YouTube商业联系邮箱帮助](https://support.google.com/youtube/answer/57955?hl=en)：官方说明只有频道所有者提供了商业联系邮箱，才可查看；缺失地址不能由名字或域名猜测补齐。
- [YouTube频道资源文档](https://developers.google.com/youtube/data/reference/rest/v3/channels)：官方资源以频道ID识别频道，包含元数据和统计；订阅数按三位有效数字取整，不能冒充精确即时人数。未调用API或申请凭据。
- [原作者文章](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1i8l5lf)：原文未读；目录转述和试用模板不冒充作者实现。
