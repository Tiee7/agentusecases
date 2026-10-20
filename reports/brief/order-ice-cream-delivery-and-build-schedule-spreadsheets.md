# 用Operator订购冰淇淋配送并制作日程表

## 中文

    订购冰淇淋配送并制作日程电子表格
    记者们测试了Operator：它让冰淇淋送达了，但需要指导、付款信息和购买批准，而且常把电子表格的细节弄错。
    使用的是
    OP
    Operator
    他们做了什么
    彭博社的Rachel Metz试用了OpenAI的Operator，这是一个替你浏览网站的浏览器型agent。她让它订购冰淇淋配送，并制作一份日程电子表格。她全程看着它操作。完成购买之前，它向她寻求指导、付款信息和批准。
    进展与成效
    冰淇淋送到了，但依赖她的帮助。日程表中的细节经常出错。Metz觉得它很慢，OpenAI也承认Operator难以处理幻灯片和日历等复杂界面。
    值得了解
    当时只有每月200美元的ChatGPT Pro套餐可以使用Operator，它需要持续监督，并在重要操作前取得确认。
    亲自尝试
    使用
    Operator
    复制提示词
    从[配送服务或商店]订购[商品，例如一品脱冰淇淋]，送到[我的地址]，预算为[金额]。选择符合要求且评价最好的选项，加入购物车。在输入付款信息或下单前停下，向我展示购物车、总价和配送时间，让我批准。
    原始来源：https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html

<details><summary>English original</summary>

    Order ice cream delivery and build schedule spreadsheets
    Reporters tested Operator: it got ice cream delivered but needed guidance, payment info and purchase approval, and often got spreadsheet details wrong.
    Done with
    OP
    Operator
    What they did
    Bloomberg's Rachel Metz tried OpenAI's Operator, a browser-based agent that navigates websites for you. She asked it to get ice cream delivered and to build a schedule spreadsheet. She watched it the whole time. It asked her for guidance, payment details and approval before it completed the purchase.
    How it went
    The ice cream got delivered, but only with her help. The schedule spreadsheet often had wrong details. Metz found it slow, and OpenAI admits Operator struggles with complex interfaces such as slideshows and calendars.
    Worth knowing
    Operator was available only on the $200 per month ChatGPT Pro plan, and it needed constant monitoring and confirmation before important actions.
    Try it yourself
    with
    Operator
    Copy prompt
    Order [item, e.g. a pint of ice cream] for delivery to [my address] from [delivery service or store], with a budget of [amount]. Pick the best-reviewed option that fits, and add it to the cart. Stop before entering payment details or placing the order, and show me the cart, total, and delivery time so I can approve it.
    Original source: https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html

</details>

## 原作者的方法与来源

https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html
第三方报道转述，未读到彭博原始文章。
A reporter supervised Operator while it arranged delivery, provided guidance and approved payment; schedule details needed correction.
记者监督Operator安排配送，提供指导并批准付款；日程细节需要纠正。

## 简要分析

商业分数未评定。

### 一次送达与持续可用性分别判断

2025年2月1日，Frank Landymore在Futurism/Yahoo文章中转述Rachel Metz测试：冰淇淋送达，但需要指导、付款信息与批准；她全程监督，日程表细节经常错误。本轮读到的是这篇二手报道，没有取得彭博原始测试记录、订单回执、具体等待分钟或错误率。目录和报道属于同一证据链，不能计作两组独立体验。因缺可重复工作流、客户及成本，本篇交付简报。

依据：[Sarticle](https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html), [Sdirectory](https://agentusecases.ai/use-case/order-ice-cream-delivery-and-build-schedule-spreadsheets)

### 200美元与Operator入口属于历史背景

官方2025年1月23日发布说明定位为美国Pro用户研究预览；同页2025年7月更新记载整合至ChatGPT agent。当前agent帮助页顶部又声明该功能不可用并指向Work，但下文仍残留旧额度说明。本报告保留源站原文，同时提醒复制时查看现有账号实际入口和权限，不把每月200美元写成今天完成购物必须购买的套餐。历史界面错误也不能直接当成当前版本错误率。

依据：[Slaunch](https://openai.com/index/introducing-operator/), [Sretired](https://help.openai.com/en/articles/11752874-chatgpt-agent), [Swork](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)

### 付款确认是正常控制步骤

报道语气把多次求助和确认放在一起。研究者建议区分两类成本：身份登录、付款和订单批准属于正常控制；反复理解错商品、卡在界面和修正表格则属于执行返工。不能为了提高表面无人值守率删除支付审核。应分别测主动操作分钟、等待时间、必要批准次数与错误纠正次数。人类确认存在并不自动证明失败，成功送达也不证明节省了人类时间。

依据：[Slaunch](https://openai.com/index/introducing-operator/), [Sarticle](https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html)

### 购物车草稿应说明缺货与最终变化

Instacart现行说明允许检查已选商品、替代品和退款；换地址、换店或缺货可使商品从购物车移除，部分提前预订类商品下单后不能编辑。研究者建议从明确商品规格、数量、预算、配送窗口开始，在付款前核对实际购物车，不把搜索结果价当最终总价。替代后金额或关键规格变化需要重新审阅。平台本身已提供这类功能，应以原生购物流程作效率对照。

依据：[Sorder](https://www.instacart.com/help/section/360008835771)

### 日程表要按字段与约束验收

研究者提出独立的表格验收方法：用固定输入清单核对日期、时区、起止时间、人员、持续时长和冲突，检查遗漏与重复，再交付可编辑文件。界面上出现一个表格不代表细节正确；能订购商品不证明能维护日历。这个案例没有提供具体表格内容，本轮也没有猜测错误细节或改动真实日历。纯数据整理可以先输出结构化草稿，再决定是否需要浏览器操作。

依据：[Sdirectory](https://agentusecases.ai/use-case/order-ice-cream-delivery-and-build-schedule-spreadsheets)

### 最可能先验证的是限定任务服务

商业假设是帮助频繁整理采购需求或不便操作网页的人，把明确清单变成可批准订单草稿；另一类是组织内的日程资料整理。买方、预算与需要完全不同，不应以同一个购物成功样例推导通用个人助理订阅可卖。获客可以用虚构订单和可复核表格展示，交付限定在拟购清单及检查结果。现有购物应用、人工助理和表格工具是直接替代，未发现本案付费客户、复购或第三方服务收入。

依据：[Sarticle](https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html), [Sorder](https://www.instacart.com/help/section/360008835771)

### 把监督与售后算入成本

未取得当事人实际账单、每单模型成本或完成时间，不做收益数字推断。研究者列出需要测的成本：工具使用、人工准备、全程观察、错选修正、配送异常、退换协助和流程变更维护；服务经营还包含获客、支持和退款风险。低价单件购物节省可能不足以覆盖这些成本。只有相对熟练手动流程仍减少总人工时间，且质量没有下降，才值得扩大测试。

依据：[Sarticle](https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html)

### 自用收益取决于是否真能少盯屏幕

适用者是假定已有合适工具、能明确规格并愿审查最终金额的个人。潜在收益是减少网站切换和重复录入，实际收益未测。设置需要清单、商店偏好和批准边界；维护涉及商品替代、账号会话、地址与配送条件变动。频率跟随实际购物或排程需要。隐私风险是地址、支付和账户资料，错误风险是错品、重复单、超预算和日程冲突。本轮没有登录商店、提交真实地址或下单。

依据：[Sdirectory](https://agentusecases.ai/use-case/order-ice-cream-delivery-and-build-schedule-spreadsheets), [Sarticle](https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html)

### 先做不下单的对照演练

拟议小测试使用三件虚构商品和两份相互冲突的日程输入，先手动计时，再让已有获准助手生成购物比较草稿与日程表。保留人工标准答案，统计准备、监督与修正分钟；期待得到能逐项核对的清单、费用待确认项和冲突提示。本轮没有执行测试。若仍需全程盯屏幕、表格基本字段错或总时间不降，停止扩大；不将聊天回复中的完成字样当订单或文件回执。

依据：[Sorder](https://www.instacart.com/help/section/360008835771), [Sdirectory](https://agentusecases.ai/use-case/order-ice-cream-delivery-and-build-schedule-spreadsheets)

## 试用准备与预期结果

虚构商品、固定价格片段、日程输入与人工标准答案。
可核对的购物与日程草稿，不下单；本轮未试用。
只依据提供的虚构商品和日程，列出商品规格、数量、费用未知项与替代差异；日程逐项检查日期、时区、时长、重叠和遗漏。输出待审草稿，不登录、加入真实购物车、付款或修改日历。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/order-ice-cream-delivery-and-build-schedule-spreadsheets)：完整许可正文、模板与历史使用描述。
- [Futurism在Yahoo发布的Operator体验报道](https://tech.yahoo.com/ai/articles/openais-ai-agent-monitored-nonstop-183005989.html)：2025-02-01文章转述Rachel Metz测试；不是我们实测或彭博原文。
- [OpenAI Operator历史发布说明](https://openai.com/index/introducing-operator/)：2025-01-23研究预览，历史复杂界面限制；后续迁移说明。
- [ChatGPT agent现行页面顶部状态](https://help.openai.com/en/articles/11752874-chatgpt-agent)：顶部声明已不可用、改用Work；下文遗留旧额度不作现价依据。
- [ChatGPT Work当前说明](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)：当前工作入口有自己的工具、权限及可用性，不能把旧Operator当现产品。
- [Instacart订单变更说明](https://www.instacart.com/help/section/360008835771)：商品可能缺货或换店移除，替代与退款需检查，已有原生操作可对照。
