# 用 Claude Code 跟踪个人财务并保存分析计划

分析深度：简要研究（brief）；商业评分未评定；不计入深研完成数。

## 案例完整中文译文

    使用Claude Code助手跟踪个人财务
    作者使用MCP提供的宏观数据及自己的财务资料，构建了Claude Code财务助手，用于跟踪财务、评估状况并支持投资决策。
    实际使用
    Claude Code
    具体做法
    作者把Baselight MCP连接到Claude Code，再让Claude生成一个Markdown文件仓库：用CLAUDE.md规定行为，用YAML和Markdown文件保存记忆，包括组合、决策和行动计划，并保存SQL查询。他没有手写代码或Markdown。每次运行都会向Baselight查询宏观数据，然后分析他的投资组合。Git hooks会加密敏感数据。
    结果如何
    这个名为Mr. Malone的助手会分析作者自己的组合，并保存行动计划供后续会话使用。文章没有给出量化结果；作者表示，大语言模型可能不可靠，输出具有随机性。
    值得知道
    他在同一次Claude Code会话中构建并使用了助手，因此混合了上下文。由于数据敏感，他将仓库保持私有，并进行了加密。
    自行试用
    推荐工具
    Claude Code
    复制提示词
    使用[文件夹或导出文件]中的我的数据，构建个人财务助手。总结收入、支出、债务和储蓄，评估财务健康状况，并标记[需要关注的问题，例如资金可支撑时间或高息债务]。所有内容保留在本地，不进行任何交易。生成一页报告及三个我应考虑的问题或决策后结束。
    原始来源：https://adlrocha.substack.com/p/adlrocha-agents-will-make-code-and

<details>
<summary>English · 完整归档原文</summary>

<pre>Track personal finances with a Claude Code assistant
The author built a Claude Code financial assistant using macro data over MCP and his own financials to track his finances, assess health and support investment decisions.
Done with
CC
Claude Code
What they did
The author connected the Baselight MCP to Claude Code, then had Claude generate a repo of markdown files: CLAUDE.md for behavior, YAML and markdown files for memory (portfolio, decisions, action plans), and saved SQL queries. He wrote no code and no markdown by hand. Each run queries Baselight for macro data, then analyses his portfolio. Git hooks encrypt sensitive data.
How it went
The assistant, called Mr. Malone, runs analyses against his own portfolio and stores action plans for later sessions. The post gives no quantitative results, and he says LLMs can be unreliable and stochastic.
Worth knowing
He built and used the assistant in one Claude Code session, which mixed contexts, and he kept the repo private and encrypted because the data is sensitive.
Try it yourself
with
Claude Code
Copy prompt
Build me a personal finance assistant using my data in [folder or export files]. Summarize my income, spending, debts and savings, assess my financial health, and flag [concerns like runway or high-interest debt]. Keep everything local and don&#x27;t make any transactions. You&#x27;re done when I have a one-page report and a list of three questions or decisions I should consider next.
Original source: https://adlrocha.substack.com/p/adlrocha-agents-will-make-code-and</pre>

</details>

## 原作者的方法与来源

[原始文章](https://adlrocha.substack.com/p/adlrocha-agents-will-make-code-and)。原文已有访问限制，实现据归档为私有，未请求或读取；方法摘要未收录。以下分析基于批准使用的源站归档和官方文档。

## 我们的简要分析

商业判断：先验证只读账目整理，现有证据不足以支持投资决策产品。商业评分未评定；自用价值待核实。

### 实际做法与证据边界

归档称作者把Baselight MCP接到Claude Code，让它生成CLAUDE.md、YAML/Markdown形式的组合与决策记忆，以及保存的SQL查询；每次运行查询宏观数据，再分析自己的组合。作者称没有手写代码或Markdown，但这不等于整个设置、核对和维护无需劳动。没有给出计算准确率、节省时间、投资收益、完整代码或独立用户结果。我们未取得受限原文和私有仓库，因此只把这些内容作为源站转述，不能补写作者实际操作步骤。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/track-personal-finances-with-a-claude-code-assistant)。

### 把财务事实、说明和行动计划分开

记忆文件能让后续会话找到历史上下文，不能保证余额正确。官方文档说明CLAUDE.md是行为指导，技术限制应由客户端设置等机制执行。复现时可以将原始合成流水、确定性汇总、模型解释和带日期的行动建议分开保存；每次结论应指向输入版本与计算表，不把前一轮建议自动升级成新事实。归档提到同一会话混合搭建与使用上下文，这提示应拆分开发会话与分析会话，并将导入文字当成数据，避免其成为工具操作指令。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/track-personal-finances-with-a-claude-code-assistant), [Sf1c064262dc8](https://code.claude.com/docs/en/memory)。

### 本地文件不等于全部处理都在本地

源站试用模板要求“所有内容保留在本地”，这是目标而非已验证的数据流。Claude Code官方说明本地客户端会通过网络与模型交互，因此在输入真实资料前仍需确认会发送哪些内容、服务及账户设置、日志与留存。私有仓库和Git hooks加密只能说明作者采取了存储保护措施；Git文档显示hook还依赖安装位置与执行权限。未检查其脚本、密钥管理、历史提交、临时文件或日志，不能宣称已端到端保护。宏观数据查询也不应无必要携带个人持仓或账户信息；本轮没有输入任何私人财务。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/track-personal-finances-with-a-claude-code-assistant), [S06b2864aaa7d](https://code.claude.com/docs/en/data-usage), [S69bab27d9df2](https://git-scm.com/docs/githooks)。

### 先验算流水，再解释财务状况

可从纯合成的两个账户开始：期初合计1500、收入2000、消费300、退款50、账户间转账200，期末应为3250，转账不增加收入或支出。重复交易ID要报告，不能重复记账；不同币种在缺少汇率时分开显示。信用卡消费与还款、退款关联、日期边界和缺失余额还需单独设计样例，不能把上述小样例通过当成真实账务可靠。我们仅用本地Decimal核对这个合成样例与去重标记，未运行作者助手或模型；模型适合解释已核对的表格，数值由可检查的计算完成。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/track-personal-finances-with-a-claude-code-assistant), [Sf1c064262dc8](https://code.claude.com/docs/en/memory)。

### 自用价值与维护成本

自用价值待核实。对于能够审阅账目、愿意维护输入口径的人，它可能把分散的资料和待办集中到可追踪文件中；没有实测证据表明它比现有表格更省时间。设置需要字段字典、账户和币种范围、人工答案、数据流检查和固定报告模板。维护包括新增账户、修正分类、处理格式变化、清理敏感上下文及审核行动计划。先只读生成疑问清单，将资金可支撑时间等指标的假设写明；本案例不足以支持个性化投资建议或自动交易。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/track-personal-finances-with-a-claude-code-assistant), [S06b2864aaa7d](https://code.claude.com/docs/en/data-usage)。

### 可交付范围与费用假设

较可检验的方向是合成或合规脱敏资料的整理模板、确定性汇总和人工复核工作流，而非保证投资回报的助手。尚无客户、订单、定价、续费或获客证据。规划情景一：每用户每月49美元，模型及数据预算5、人工1小时×30美元=30、其他5、获客10，贡献负1美元；人工增至2小时则负31美元。情景二：一次设置900美元，模型/数据测试预算20、人工15小时×40美元=600、其他30、获客100，贡献150美元；多4小时返工则负10美元。全部是假设，未扣固定费与税费，不是实际平台报价或作者账单，本轮未发生任何付费调用。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/track-personal-finances-with-a-claude-code-assistant)。

### 下一步与停止条件

下一步先明确一页报告服务于哪些问题，再准备合成流水和人工核算基准，检查重复、退款、转账及多币种异常，并为每条解释附输入和计算依据。若数据流无法说明、账目无法对齐、输出混入无来源数字，或必须依靠模型猜测才能补全缺失资料，就停在试验阶段。宏观数据接入并非首个验收条件，先保证输入和汇总正确；没有私人材料也可以验证整理格式。后续涉及真实资料或投资决定仍需另行界定范围，本轮没有注册、凭据、账户接入或交易。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/track-personal-finances-with-a-claude-code-assistant), [Sf1c064262dc8](https://code.claude.com/docs/en/memory), [S06b2864aaa7d](https://code.claude.com/docs/en/data-usage), [S69bab27d9df2](https://git-scm.com/docs/githooks)。

## 自用与试用准备

资料整理与历史计划可追踪的潜在价值存在，但没有计算准确性、节省时间或持续使用的独立证据。

准备：纯合成或充分脱敏且获准使用的流水、字段定义、币种、期初余额和人工答案。

预期：一页报告草案、计算依据、异常清单及三个待人工核对问题；自编模型模板未实测。

源站试用模板完整保留在上方原文与忠实译文中，不代表作者实际提示词。

### 用合成流水设计只读财务报告

研究团队自编，未调用模型实测。

    请只使用我提供的[纯合成或已充分脱敏且获准使用的流水、字段字典、币种、期初余额和人工答案]，设计一个只读财务报告流程。先核对字段、重复交易ID、转账配对、退款关联、消费与信用卡还款、日期和币种，缺失汇率不得自行补值。将确定性计算表、输入版本、解释、未解决问题和行动建议分开保存，每条数字附计算依据，历史建议不可当作新事实。先核对期初1500、收入2000、消费300、退款50、内部转账200应得期末3250的合成样例。不要读取真实财务、凭据或私人聊天，不向MCP发送个人持仓，不注册、不购买、不调用额外付费API、不交易或发送资料。说明工具的数据流和无法验证的部分，不能以“保存在本地”保证不上云。输出一页报告草案、验收表、缺失资料以及三个待人工确认的问题后停止，不提供个性化投资买卖建议。

## 来源

- [Track personal finances with a Claude Code assistant](https://agentusecases.ai/use-case/track-personal-finances-with-a-claude-code-assistant)：作者关于Baselight MCP、财务记忆文件、私有加密仓库和无量化结果的源站归档转述。
- [How Claude remembers your project - Claude Code Docs](https://code.claude.com/docs/en/memory)：CLAUDE.md提供行为指导，官方文档区分它与由客户端强制执行的设置。
- [Data usage - Claude Code Docs](https://code.claude.com/docs/en/data-usage)：本地运行的Claude Code仍会联网与模型交互；数据流、留存及训练政策取决于具体产品和设置。
- [Git - githooks Documentation](https://git-scm.com/docs/githooks)：Git hooks是执行特定动作的程序，位置可配置且不可执行的hook被忽略；文档不证明本案例加密实现正确。
