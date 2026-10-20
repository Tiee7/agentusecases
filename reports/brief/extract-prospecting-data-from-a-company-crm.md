# 用浏览器Agent从公司CRM提取销售线索字段

## 中文

    从公司CRM中提取潜客开发数据
    一位用户让ChatGPT agent浏览其公司的CRM，并从中提取用于销售潜客开发的有用数据。
    使用的是
    ChatGPT Agent
    他们做了什么
    发帖者说，他们此前曾使用ChatGPT agent打开公司CRM、浏览网站，并提取有用的潜客开发数据。在帖子中，他们询问这是否依赖旧agent自己的浏览器，加上由人接管完成登录，因为较新的ChatGPT Work似乎已无法完成同样的任务。
    进展与成效
    来源只能表明这件事以前成功过，而用户现在无法让ChatGPT Work重复完成。回复认为新工具有所不同，或已整合到ChatGPT应用中，但这里没有人报告成功的替代工作流。
    值得了解
    问题在于产品变化：这个用例似乎依赖较旧的agent模式，帖子没有给出已确认的当前复现方法。
    亲自尝试
    使用
    ChatGPT Agent
    复制提示词
    登录我们位于[CRM网址]的公司CRM（到达登录页时我会自行登录）。浏览[账户、线索或一个已保存的视图]，为每条符合[潜客开发条件]的记录提取[公司名、联系人、职位、最近活动、交易阶段等字段]。把结果放进一张我能复制到电子表格中的表格，覆盖全部匹配记录后停止。不要在CRM中编辑、删除或发送任何内容。
    原始来源：https://www.reddit.com/r/ChatGPT/comments/1v1cmxi/chatgpt_work_worse_than_agent

<details><summary>English original</summary>

    Extract prospecting data from a company CRM
    A user had ChatGPT agent navigate their company's CRM and pull useful data for sales prospecting.
    Done with
    GA
    ChatGPT Agent
    What they did
    The poster says they had previously used ChatGPT agent to open their company CRM, navigate the site, and extract useful prospecting data from it. In the thread they ask whether that depended on the old agent’s own browser plus a human taking over to log in, because the newer ChatGPT Work no longer seems able to do the same task.
    How it went
    The source only establishes that this had worked before and that the user now cannot get ChatGPT Work to repeat it. Replies suggest newer tools are different or folded into the ChatGPT app, but no one reports a successful replacement workflow here.
    Worth knowing
    The catch is product drift: this use case appears tied to an older agent mode, and the thread gives no confirmed current method for reproducing it.
    Try it yourself
    with
    ChatGPT Agent
    Copy prompt
    Log into our company CRM at [CRM URL] (I'll sign in myself when you reach the login page). Go through [the accounts, leads, or a saved view] and pull [fields such as company name, contact, role, last activity, deal stage] for every record that matches [prospecting criteria]. Put the result in a table I can copy into a spreadsheet and stop when you've covered all matching records. Do not edit, delete, or send anything in the CRM.
    Original source: https://www.reddit.com/r/ChatGPT/comments/1v1cmxi/chatgpt_work_worse_than_agent

</details>

## 原作者的方法与来源

原帖位于此前明确受限Reddit，不重试或绕过。未登录任何公司CRM、读取客户记录、导出真实名单或运行试用。

[原始链接](https://www.reddit.com/r/ChatGPT/comments/1v1cmxi/chatgpt_work_worse_than_agent)

## 简要分析

商业分数未评定。

### 过去做过和现在可复现分开

作者说旧agent曾浏览CRM并提取数据，没有给数量、字段准确率、处理时间和人工复核。当前无法重复也没有错误日志，不能认定某模型更弱或所有Work都不支持。官方旧agent页概览已引导Work，下方却残留旧可用性描述，研究记录这一矛盾，不自行补出发布日期、迁移完成时间或账号能力。

依据：[Sdirectory](https://agentusecases.ai/use-case/extract-prospecting-data-from-a-company-crm), [Sagent](https://help.openai.com/en/articles/11752874-chatgpt-agent)

### 先查CRM本身能否导出

HubSpot只是现成能力的例子，不是已确认的案例工具。其视图可导出当前属性与关联，活动记录另有路径，并要求导出权限。真实任务应先核对所需字段是否属于普通记录还是互动历史；若原生导出已覆盖，无须为了使用AI逐页点击。没有导出权限不是换浏览器绕限制的理由。

依据：[Sexport](https://knowledge.hubspot.com/import-and-export/export-records)

### 筛选范围与完整性是交付核心

拟议流程先写清对象、筛选条件、时间范围、字段定义和允许输出位置，再核对总匹配数。分页、滚动加载、关联对象、多联系人和空值都可能让表格看似完整却漏数。保留记录ID和来源定位用于去重，抽查首末页与例外，不能把显示行数当总记录数。

依据：[Sdirectory](https://agentusecases.ai/use-case/extract-prospecting-data-from-a-company-crm)

### 能登录不代表可搬运全部数据

官方说明云浏览器有独立登录会话，能做支持网站上的任务，但访问与动作能力依网站而异。应使用获准安全登录方式，不在研究报告存密码或客户名单；只读取指定范围。表格输出本身仍可能传输内部客户信息，须先明确目的、字段、保存位置与可见人群。

依据：[Sbrowser](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)

### 交付是可靠数据整理而非承诺成交

潜在需求是销售运营减少重复筛选抄录。可假设交付按批次收费或长期维护，但本案没有付款人、成交单价、销售转化或营收证据。获客需要展示同一CRM中字段完整、无重复、可追溯和安全边界，不能把抓到联系人称为拿到客户。工具模式升级导致的维护也应包含在服务范围里。

依据：[Sdirectory](https://agentusecases.ai/use-case/extract-prospecting-data-from-a-company-crm)

### 把产品变化算进维护成本

成本包含登录配合、视图配置、读取等待、校验、返工、保存及产品变动适配。原作者没有费用与耗时，不填利润模型。低频导出可能直接人工更便宜；高频任务也应先比较现成导出或正式接口，而不是以浏览器每次能跑完为唯一成功标准。

依据：[Sdirectory](https://agentusecases.ai/use-case/extract-prospecting-data-from-a-company-crm)

### 自用需要能核对业务字段

适合有合法CRM权限且知道字段含义的销售运营人员。预期收益是减少重复抄录，实际节省未知。设置要明确视图与字段，维护随CRM界面、权限和工具变化。频率按业务批次；风险包括错配联系人、漏页、混淆最近活动时间，以及将无权外传信息复制到别处。

依据：[Sdirectory](https://agentusecases.ai/use-case/extract-prospecting-data-from-a-company-crm)

### 合成样例验证边界

准备一份虚构CRM列表，含分页、相同公司多联系人、同名联系人、空职位、不同阶段和不匹配记录，预先建立正确输出。要求只读提取，不修改、不发信、不删除，遇登录或权限不足停止。验收包括筛选准确、记录ID去重、匹配总数与缺失说明。本轮没有实际运行或接触公司数据。

依据：[Sdirectory](https://agentusecases.ai/use-case/extract-prospecting-data-from-a-company-crm)

## 试用准备与预期结果

合成CRM样例、正确答案与只读范围；不接真实账户。
字段表、记录ID、缺失与覆盖说明，不写回或联系；未实测。
从以下虚构CRM列表按指定条件提取字段，保留记录ID，列出匹配数、去重结果和缺失项。不要补造字段，不访问账号、不写回、不发信。

## 来源

- [许可目录现场正文](https://agentusecases.ai/use-case/extract-prospecting-data-from-a-company-crm)：目录仅转述旧agent曾提取CRM数据，当前作者无法复现且没有确认替代流程；CRM品牌、数量与收益未披露。
- [HubSpot导出记录官方说明](https://knowledge.hubspot.com/import-and-export/export-records)：官方区分导出权限、视图字段/关联与活动数据。用于现成替代对照，不证明原作者使用HubSpot。
- [OpenAI agent帮助页](https://help.openai.com/en/articles/11752874-chatgpt-agent)：当前概览写旧agent不再可用并指向Work，但页面下方仍保留旧启动及可用性文字；记录页面内部不一致，不据旧段落承诺可复现。
- [OpenAI云浏览器帮助页](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)：官方支持获准网站的登录后任务，优先可用连接器；云浏览器与本机登录独立，网站或具体步骤仍可能不支持。
- [原作者文章](https://www.reddit.com/r/ChatGPT/comments/1v1cmxi/chatgpt_work_worse_than_agent)：原文未读；目录转述和试用模板不冒充作者实现。
