# 用未命名 AI 智能体辅助杂货购物与机票比价

## 中文

    添加杂货、在Amazon购物并比较机票价格
    一位评论者和妻子经常使用AI智能体，向Walmart杂货配送订单添加商品、在Amazon购买商品并比较机票价格。
    使用的是
    自建或未命名智能体
    他们做了什么
    一位评论者说，他和妻子经常用自己的AI智能体完成三类购物任务：向Walmart杂货配送订单加商品、在Amazon购物，以及比较机票价格。但在这个讨论中，他没有解释系统配置、智能体拥有哪些访问权限、哪些步骤是自主完成的，以及他们在哪里批准或介入。
    进展与成效
    唯一明确陈述的结果是，他们经常用它做这些事情。帖子没有提供具体结果、节省金额、准确率、预订细节或失败情况。
    亲自尝试
    使用ChatGPT Agent
    复制提示词
    在浏览器中登录我的[Walmart]账户，把这些商品添加到下一次杂货配送订单：[列出商品及品牌或规格]。然后在[网站]搜索从[出发地]到[目的地]、日期为[日期]的往返航班，并在[2至3个网站]比较价格。在结账或购买任何东西前停止，向我展示购物车和最佳航班选项。
    原始来源：https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping

<details><summary>English original</summary>

    Add groceries, buy on Amazon, and price-shop flights
    A commenter and their wife regularly use an AI agent to add items to Walmart grocery delivery orders, buy from Amazon, and compare flight prices.
    Done with a
    custom-built or unnamed agent
    What they did
    A commenter says he and his wife regularly use their AI agent for three shopping tasks: adding items to Walmart grocery delivery orders, buying from Amazon, and price-shopping flights. In this thread, though, he does not explain the setup, what access the agent had, what steps it took by itself, or where they approve or intervene.
    How it went
    The only outcome stated is that they use it regularly for those tasks. The post gives no results, savings, accuracy, booking details, or failures.
    Try it yourself
    with ChatGPT Agent
    Copy prompt
    Log in to my [Walmart] account in the browser and add these items to my next grocery delivery order: [list of items with brands or sizes]. Then search [site] for round-trip flights from [origin] to [destination] on [dates] and compare prices across [2-3 sites]. Stop and show me the cart and the best flight options before checking out or buying anything.
    Original source: https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping

</details>

## 原作者的方法与来源

来源：[Shopping use described by commenter turnipsium](https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping/)

A commenter, not the journalist who opened the thread, reports regular grocery, Amazon and flight-comparison use.
评论者而非发帖记者，自述经常用智能体处理杂货、Amazon购物和机票比价。

The comment does not identify the agent or explain its setup, permissions or approval steps.
评论没有说明智能体身份、配置、权限或批准步骤。

## 简要分析

商业分数未评定。

### 这是使用线索，不是完整实现记录

原帖由记者征集访谈，真正的购物叙述来自turnipsium的一条评论。没有产品名、配置、订单回执或节省数据，因此不能将目录推荐的ChatGPT Agent当成实际工具，也不能把其他评论者的x402使用和销售广告工具拼进去。保留未评分简报；经常使用表示自述频率，不等于成功率、真实成交金额或可复制服务。

依据：[Sdirectory](https://agentusecases.ai/use-case/add-groceries-buy-on-amazon-and-price-shop-flights), [Soriginal](https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping/)

### 三项任务不能共用一个验收结果

杂货加购需要核商品规格、数量和替代规则；Amazon购买还需核卖家、配送、总价及最终批准；机票比价需要统一日期、机场、时区、行李和退改条件。完成其中一项不能证明另外两项也完成。原评论只列任务，没有说明实际步骤，因此这些是拟议验收项，不是还原出的作者操作录像。

依据：[Soriginal](https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping/), [Sedit](https://www.walmart.com/help/article/edit-or-cancel-walmartn-order/2c7e3d99812044f8aaa65aee0eae3d1c), [Sbags](https://support.google.com/travel/answer/9074247?hl=en)

### 订单编辑与购物车不同

给未结账购物车加商品和修改已存在的配送订单具有不同后果。Walmart公开说明符合条件的订单可以在截止前修改，截止随订单类型和地区变化，应以实际订单页为准。本轮没有登录、查看用户订单或加购。将来试用应先确认是在草拟清单还是修改订单，并在任何会改变支付或配送承诺前核授权；失败时先查已完成状态，避免重复商品。

依据：[Sedit](https://www.walmart.com/help/article/edit-or-cancel-walmartn-order/2c7e3d99812044f8aaa65aee0eae3d1c)

### 价格数字需要可比条件

机票最低展示价未必是用户最终可接受的成本。Google Flights提供行李费用过滤，但信息来自合作方，航空公司尺寸和费用仍需核对。比价表应保留查询时间、航段、人数、币种和费用包含项，缺项标未知，不用模型补报价。原评论没有实际行程或预订结果，本例不报告节省比例，也不因“比较过”认定已买到最便宜机票。

依据：[Sbags](https://support.google.com/travel/answer/9074247?hl=en)

### 现成复购功能构成替代

家庭常买同一批商品时，平台购物列表与复购入口可能比跨站智能体更直接。潜在增量是把自然语言偏好转成准确的候选清单，并减少多站核对；这仍需测净省时。没有实际工具、预算、错误率和售后工时，无法建立有依据的收费或利润模型。可以验证用户是否愿为具体整理任务付费，不能凭一条使用评论推出自动采购服务市场。

依据：[Sapp](https://www.walmart.com/help/article/the-walmart-site-and-app-experience/27f2678cb25a40a7b57a359fec3ca67f), [Soriginal](https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping/)

### 不同人的体验分开

同一讨论里，有人自述多次使用购物工具后觉得规格会编造、优惠会漏掉、复核比自己浏览更慢；这只能作为相邻负面体验。另一人提及用x402服务购物，是不同实现；推广分类广告工具的评论更不是购买助手验证。原用户没有解释如何使用的追问答案，关键复制信息仍缺失。正负评论都保留其身份和范围，不将旁观意见换成满意度。

依据：[Soriginal](https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping/)

### 先用虚构商品和报价测试

准备几条虚构商品候选，故意加入同品牌不同容量、数量单位不一致和缺货替代；再准备两组行李包含条件不同的虚构机票。要求助手列匹配与未知项，不能自动下单。验收关注是否识别不可比、是否保持数量和预算、是否在未知条件停止，而非输出推荐多漂亮。本轮未执行任何购物试用。

依据：[Sedit](https://www.walmart.com/help/article/edit-or-cancel-walmartn-order/2c7e3d99812044f8aaa65aee0eae3d1c), [Sbags](https://support.google.com/travel/answer/9074247?hl=en)

### 下一步只补最关键证据

若继续研究，优先取得实际agent名称、任务轨迹和批准边界，再决定是否值得做端到端评估。没有这些，不应靠更多泛化平台文档把简报扩写成已验证深研。如果复核清单的成本超过人工复购，或任务要求交出无限支付权限，应停止扩大自动化；保留搜索和草拟清单可能已足够。

依据：[Soriginal](https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping/)

## 试用准备与预期结果

虚构商品及报价表，无账号、地址、银行卡或真实订单。
规格、数量、总价包含项与未知项清单；无购买或订单更改。

比较这些虚构商品和航班候选。商品核品牌、容量、数量单位与替代；航班核航段日期时区人数、行李与退改条件。缺失项列未知，不补价格。输出可比清单和需确认问题，不登录、不改订单、不购买。

## 来源

- [许可目录与试用模板](https://agentusecases.ai/use-case/add-groceries-buy-on-amazon-and-price-shop-flights)：明确实际agent未知，推荐ChatGPT Agent只属于目录试用区。
- [记者征集与购物用户评论](https://www.reddit.com/r/AI_Agents/comments/1u7ptrk/anyone_use_agentic_ai_for_shopping/)：turnipsium评论自述经常购物；记者不是实际使用者，其他评论不能合并为同一实现。
- [Walmart订单编辑边界](https://www.walmart.com/help/article/edit-or-cancel-walmartn-order/2c7e3d99812044f8aaa65aee0eae3d1c)：符合条件订单在截止前可修改，截止随订单类型和地区变化；不是无限期加购。
- [Google Flights行李费比较](https://support.google.com/travel/answer/9074247?hl=en)：行李过滤可调整含费价格，数据来自合作方，需核航空公司规则。
- [Walmart现有站点功能](https://www.walmart.com/help/article/the-walmart-site-and-app-experience/27f2678cb25a40a7b57a359fec3ca67f)：平台已有购物列表、复购和配送选项；不能把所有下单便捷性归给agent。
