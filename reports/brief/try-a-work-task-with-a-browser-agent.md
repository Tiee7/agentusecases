# 用Operator搜集工作资料并整理表格

## 中文

    用浏览器agent尝试一项工作任务
    发帖者让Operator为一项工作任务搜索网页；它犯了错，而且所需时间会比手动完成更长。
    使用的是
    Operator
    他们做了什么
    发帖者通过Operator网站，使用ChatGPT Pro订阅来操作OpenAI的Operator，并给它一项明确的浏览器任务：找出50位受欢迎的财经YouTuber，收集LinkedIn信息、电子邮件地址和频道简介，再放进一张表格。Operator随后自主浏览，搜索Bing、访问网页并尝试表格工具；人主要在旁观察，发现它从未请求登录帮助，并在约20分钟后停止任务。
    进展与成效
    20分钟后，它只整理出18位网红。表格格式本身没有问题，但LinkedIn详情和邮件地址是编造的。发帖者说，自己手动做大约15分钟就能完成，而且错误更少。
    值得了解
    一个主要问题是速度：每次点击或滚动花约1至2秒；它还花了大约5分钟寻找表格选项，而不是请用户登录。
    亲自尝试
    使用
    Operator
    复制提示词
    我需要完成这项工作任务：[描述任务，例如汇总供应商价格或寻找联系方式]。搜索网页，把结果收集到表格里，为每一行附来源链接，并标明任何你不确定的内容。提交任何表单或发送任何内容之前，先暂停并向我展示你准备做什么；表格完成后就停止。
    原始来源：https://www.reddit.com/r/csMajors/comments/1i8joi4/ai_agents_are_not_coming_for_your_job_my

<details><summary>English original</summary>

    Try a work task with a browser agent
    The poster had Operator search the web for a work task; it made mistakes and would have taken longer than doing it manually.
    Done with
    OP
    Operator
    What they did
    The poster used OpenAI’s Operator through the Operator website with a ChatGPT Pro subscription and gave it a concrete browser task: find 50 popular financial YouTubers, gather LinkedIn info, emails, and channel summaries, and put it all in a table. Operator then browsed on its own, searching Bing, visiting pages, and trying spreadsheet tools; the human mainly watched, noticed it never asked for sign-in help, and stopped it after about 20 minutes.
    How it went
    It produced only 18 influencers after 20 minutes, and the table format itself was fine, but the LinkedIn details and email addresses were made up. The poster says they could have done the job manually in about 15 minutes with fewer mistakes.
    Worth knowing
    A key catch was speed: each click or scroll took about 1–2 seconds, and it also wasted roughly 5 minutes looking for a spreadsheet option instead of asking the user to sign in.
    Try it yourself
    with
    Operator
    Copy prompt
    I need to do this work task: [describe task, such as compiling vendor pricing or finding contact details]. Search the web, collect the results in a table with a source link for each row, and flag anything you are unsure about. Before you submit any form or send anything, pause and show me what you are about to do, and stop once the table is complete.
    Original source: https://www.reddit.com/r/csMajors/comments/1i8joi4/ai_agents_are_not_coming_for_your_job_my

</details>

## 原作者的方法与来源

原帖位于此前受限Reddit，本轮不重试或绕过。未取得作者原始表格、准确计时、身份或发帖日期。

[原始链接](https://www.reddit.com/r/csMajors/comments/1i8joi4/ai_agents_are_not_coming_for_your_job_my)

## 简要分析

商业分数未评定。

### 高度相似记录不当两次独立实验

本条50人、18行、20分钟和联系资料编造的细节，与已收录的[网红名单案例](gather-a-list-of-influencers-with-a-browser-agent.md)高度一致，但原始Reddit路径不同。可能是同一经历的跨帖或二次转述；原文不可读，不能确定作者相同或强行合并。保留两个原slug，同时不把它们作为独立相互佐证，不增加独立反馈数。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)

### 目录日期保留，时序疑点单列

目录显示2025年1月1日，官方公开发布页为1月23日，且目录描述的是Pro订阅经公开网站使用。这里保留实际看到的元数据，标为未核实，不把它当可靠的作者发表日，也不擅自改成1月23日。官方历史限制和后续整合说明不能用来描述当前产品性能。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent), [Slaunch](https://openai.com/index/introducing-operator/)

### 别把作者估计当受控计时

20分钟后停止与预计人工15分钟不是完整对照。任务完成标准、正确字段数、资料新旧、人工检索范围都未知，不能用18除50当准确率，也不能计算省时百分比。重新评估时需相同输入、相同字段和事实核验门槛，并把返工计入总用时。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)

### 每个重要字段都应有依据

拟议资料表记录对象身份、来源、观测时间和未知状态。联系资料缺失就保持缺失，不猜邮箱或主页；行级来源也不必然证明该行所有字段都可靠，必要时记录字段级出处。格式整齐只是交付形式，不是验收结果。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)

### 遇到依赖及时停，不把受阻藏起来

在线表格未登录不必阻止先在聊天中整理资料。应清楚区分研究完成、写入目标系统失败和结果尚待核实，避免在无法写表时继续无效寻找工具。源模板要求表单或发送前暂停，这不是自动外联授权。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)

### 先交付可审查研究，而非承诺替代岗位

假设需求来自定期整理供应商或公开对象资料的人，但本案具体是财经创作者名单，没有企业采购或付款。潜在收入机制可以是明确范围的研究服务，而不是按未经核实行数收费。获客可展示合成样本和核验方法，本轮不联系客户或创作者。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)

### 比较包含人工审核的完整成本

费用和时间应包括搜索、读页、身份核实、缺项处理、表格整理、复核与返工。模型费用并不等于交付成本；低频小任务可能直接人工更省事。没有实付和工时证据，不填利润、固定预算或真实收入。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)

### 适合有清晰标准且愿意复核的人

自用者先定义领域、字段、数量和停止条件，再从小批资料开始。设置包括授权范围及来源标准，维护包括页面变更、资料过期和重复对象。频率由工作需求决定；隐私风险是收集多余联系人信息，错误风险是错认人和编造。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)

### 离线样本先验证缺项处理

给三条虚构供应商资料：一条完整、一条缺价格、一条与另一对象同名。仅做带出处和未知字段的表格，不访问账号或发送消息。预期应区分身份、保留缺项并停止；本轮未运行真实工作任务。

依据：[Sdirectory](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)

## 试用准备与预期结果

三条虚构资料，不含真实个人联系方式或账号。
来源清楚、缺项写未知的表格，未实测。
只整理给定的三条虚构供应商资料。每项附原始资料标识，缺价格写未知；同名不自动合并，不猜邮箱，不提交表单或发送任何内容。完成表格后停止。

## 来源

- [许可目录现场正文](https://agentusecases.ai/use-case/try-a-work-task-with-a-browser-agent)：目录转述50人任务、20分钟18行与编造联系资料，以及作者估计手动15分钟；源日期显示Jan1,2025但未核实。
- [OpenAI Operator发布说明](https://openai.com/index/introducing-operator/)：官方发布页标2025-01-23，并称当天向美国Pro用户开放研究预览；页面2025-07-17更新说明整合进ChatGPT agent。历史资料不能当当前产品用法或价格。
- [原作者文章](https://www.reddit.com/r/csMajors/comments/1i8joi4/ai_agents_are_not_coming_for_your_job_my)：原文未读；目录转述和试用模板不冒充作者实现。
