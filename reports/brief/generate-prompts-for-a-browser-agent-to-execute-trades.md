# 为Perplexity Comet生成交易信号和操作提示

## 中文

    生成供浏览器智能体执行交易的提示词
    一名开发者的信号生成器读取股票和加密货币投资组合文件，并生成浏览器自动化提示词，供Perplexity Comet在券商网站执行交易。
    使用的是
    PC
    Perplexity Comet
    他们做了什么
    一个Python脚本读取CSV或Excel投资组合。它根据技术指标、Yahoo Finance新闻情绪和X帖子为每项持仓评分，权重按时间跨度设置。它把评分映射为强烈买入、买入、持有、减持或卖出，并给出配置比例变化。随后写出信号CSV，以及包含券商专用Comet提示词的文本文件。提示词会为双重验证和订单确认暂停。
    进展与成效
    仓库含有多次运行的信号和提示词样例，以及回测输出。README没有提供交易执行结果或业绩数字。
    值得了解
    README称其用于教育而非财务建议，并建议先用模拟交易测试。Comet提交订单前，务必审核信号和提示词。
    亲自尝试
    使用
    Perplexity Comet
    复制提示词
    编写一个脚本，读取我放在[文件夹]中的投资组合文件，把我的交易信号转换为清晰的逐步指令，以便交给浏览器智能体在[券商网站]上使用。每条指令应包含股票代码、买入或卖出、数量和限价。把它们输出到[文件]供我审核，并确保指令要求智能体在提交任何订单之前停止并询问我。
    原始来源：https://github.com/cometportfolio/CometAgent

<details><summary>English original</summary>

    Generate prompts for a browser agent to execute trades
    A developer's signal generator reads stock and crypto portfolio files and produces browser-automation prompts for Perplexity Comet to execute trades on brokerage sites.
    Done with
    PC
    Perplexity Comet
    What they did
    A Python script reads a CSV or Excel portfolio. It scores each holding from technical indicators, Yahoo Finance news sentiment and X posts, using weights set by time horizon. It maps scores to Strong Buy, Buy, Hold, Trim or Sell with allocation changes. It then writes a signals CSV and a text file of brokerage-specific prompts for Comet. Prompts pause for 2FA and order confirmation.
    How it went
    The repo includes sample signal and prompt files from several runs, plus backtest outputs. The README gives no trade-execution results or performance numbers.
    Worth knowing
    The README calls it educational, not financial advice, and recommends testing with paper trading first. Always review signals and prompts before Comet submits orders.
    Try it yourself
    with
    Perplexity Comet
    Copy prompt
    Write a script that reads my portfolio files in [folder] and turns my trading signals into clear step-by-step instructions I can give a browser agent for [brokerage site]. Each instruction should include the ticker, buy or sell, quantity and limit price. Output them to [file] for me to review, and make sure the instructions tell the agent to stop and ask me before submitting any order.
    Original source: https://github.com/cometportfolio/CometAgent

</details>

## 原作者的方法与来源

https://github.com/cometportfolio/CometAgent

作者描述读取持仓文件、组合指标与情绪，再写出信号和浏览器提示文件。
The author describes reading portfolio files, combining indicators and sentiment, and writing signal and browser-prompt files.

README建议教育性测试与模拟交易，但实现及许可文字仍有不一致。
The README recommends educational testing and paper trading, but implementation and licensing discrepancies remain.

## 简要分析

商业分数未评定。

### 生成文件已经可读，执行与业绩未证实

已静态读取README和主脚本。主函数最终调用信号分析、生成提示词并写CSV和文本，不能据此说程序已与券商完成交易。README列支持平台和Coinbase合作说法，本轮没有得到券商或Comet对应功能证据。未读取私人持仓，未运行脚本，未审计回测输出，不报告胜率、收益或真实成交。

依据：[Sreadme](https://github.com/cometportfolio/CometAgent/blob/main/README.md), [Scode](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py)

### 确认要求与模板并不一致

目录及README称订单提交前需要确认；实际_prompt_for_platform模板同时包含直接place/submit等步骤。双重验证分支会要求用户确认，但不能代替每一笔订单批准。默认订单类型为market，limit_hint仅定义未使用，generate_prompts也未传入限价。源站试用模板要求数量和限价，不能被误认为当前脚本已完整落实这些要求。

依据：[Sdirectory](https://agentusecases.ai/use-case/generate-prompts-for-a-browser-agent-to-execute-trades), [Sreadme](https://github.com/cometportfolio/CometAgent/blob/main/README.md), [Scode](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py)

### README与实际权重不同

主脚本已加入Reddit情绪，与README三源描述不同。按代码相乘，短期技术/新闻/X/Reddit为60%/20%/10%/10%，中期50%/27.5%/12.5%/10%，长期40%/36%/12%/12%；这些是静态算术，不是策略验证。空文本或情绪组件不可用返回0，缺数据可能被当作中性值参与固定权重，不能把中性得分解释为已充分获取消息。

依据：[Sreadme](https://github.com/cometportfolio/CometAgent/blob/main/README.md), [Scode](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py)

### 可研究的需求是整理与审核一致性

推断用户需求是把分散的持仓输入和研究信号转为统一待审清单，减少人工复制。代码把配置比例和实时账户值换算委托数量的工作留给后续提示执行者；持仓数量、可用余额、交易单位和订单状态并没有因此形成完整约束。最小有用产物应先是可追溯的研究记录及异常列表，不必直接连接真实资金。

依据：[Sreadme](https://github.com/cometportfolio/CometAgent/blob/main/README.md), [Scode](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py)

### 固定版本、来源完整度和输出边界

拟议交付需记录文件版本、行情时点、缺失源、规则参数与每条结论依据。现有CSV读取含原始前几行debug输出，真实持仓若进入共享日志会扩大暴露面。信号分数和所谓confidence也不等于经过校准的盈利概率。还应区分建议动作、待审委托和已成交回执，缺失任何环节都不能补造成功。

依据：[Scode](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py)

### 商业复制前先解决许可文字冲突

README写教育用途并限制未经许可商业分发，LICENSE却是MIT并允许使用和分发等行为。两份文件同属作者仓库，不算两个独立支持来源。本轮如实记录冲突，不自行判定哪份声明优先、也不把公开仓库等同于无条件商业授权；报告只保存原创分析及短证据，不复制整套实现。

依据：[Sreadme](https://github.com/cometportfolio/CometAgent/blob/main/README.md), [Slicense](https://github.com/cometportfolio/CometAgent/blob/main/LICENSE)

### 收费方向不等于收益承诺

可假设为研究团队提供数据清洗、规则审计或模拟流程质量检查服务，但本案无客户、付款或采购反馈。把信号直接包装为盈利订阅会要求远高于当前证据的验证和合规评估。官方投资者警示只是通用风险背景，不代表该项目被认定欺诈。本轮不提出买卖任何标的，也不接管交易。

依据：[Sreadme](https://github.com/cometportfolio/CometAgent/blob/main/README.md), [Salert](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/artificial-intelligence-fraud)

### 数据维护和执行验证可能高于生成成本

成本未知项包括行情许可、社交数据可用性、接口维护、回归验证与人工审核。抓取失败后输出0容易让表格看似完整，维护必须区分数据未取到和真实中性判断。模拟环境可帮助检查流程，但其成交假设与实际流动性、滑点及队列不同。没有实测运行成本和客户价值，不填虚构单位经济或回报。

依据：[Scode](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py), [Salpaca](https://docs.alpaca.markets/us/v1.4.2/docs/paper-trading)

### 研究自用仍要避免敏感输入与误读

适合愿阅读代码和检查数据的研究型使用者；可用于理解规则如何生成待审文本，收益尚未证明。设置需要虚构或脱敏输入、依赖版本、源可用性和输出核查；维护涉及数据和页面变化。频率由研究计划决定。隐私风险在持仓、账户值与日志；错误风险包括错标的、缺数据当中性、重复指令、卖出超持仓和限价遗漏。

依据：[Sreadme](https://github.com/cometportfolio/CometAgent/blob/main/README.md), [Scode](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py)

### 先做纯静态规则清单

本轮已完成代码阅读和权重算术，未执行第三方程序或模拟交易。下一步可设计本地纯数据验收：缺新闻、空持仓、非法数量、重复输入和无明确限价时，输出应保留未知并停止进入任何订单渠道。只有输出规则与说明一致才谈后续验证；不得把通过模拟视作真实盈利，更不应在研究阶段登录券商或提交订单。

依据：[Scode](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py), [Salpaca](https://docs.alpaca.markets/us/v1.4.2/docs/paper-trading)

## 试用准备与预期结果

虚构数据与脱敏规则清单，不连接任何账户。
参数、来源缺失、说明与代码差异清单；已做静态核验，未运行第三方程序。
只阅读提供的代码与虚构数据说明，列出缺失数据、订单类型、数量、限价、重复指令和批准步骤的不一致。不要运行第三方程序，不联网获取行情，不登录券商，也不生成可提交的真实订单。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/generate-prompts-for-a-browser-agent-to-execute-trades)：目录称生成信号与提示文件，无已证交易执行结果；来源未标日期。
- [CometAgent README](https://github.com/cometportfolio/CometAgent/blob/main/README.md)：说明CSV/Excel、技术与情绪评分和多券商提示。宣称提交前确认；License段又写仅教育用途、商业分发需许可。
- [CometAgent主脚本静态检查](https://github.com/cometportfolio/CometAgent/blob/main/agentic-trader.py)：实际生成函数默认market，limit_hint只在签名出现；模板含直接submit/place指令，未明确强制用户批准后才提交。空情绪输入为0；短期有效权重60/20/10/10。
- [CometAgent LICENSE文件](https://github.com/cometportfolio/CometAgent/blob/main/LICENSE)：文件为2025 Comet Portfolio LLC MIT License，含商业使用/分发许可和保留声明条件；与README限制措辞冲突，需澄清范围。
- [Alpaca模拟交易说明](https://docs.alpaca.markets/us/v1.4.2/docs/paper-trading)：模拟成交不同于真实市场，不能覆盖市场冲击、延迟滑点和排队等全部执行因素。仅作方法对比，本轮未开户或使用。
- [SEC等机构AI投资警示](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/artificial-intelligence-fraud)：2024-01-25投资者教育警示：AI信息可能不完整或错误，不能据AI标签承诺收益；该警示不是对本项目的调查或欺诈认定。
