# 用Manus查询附近商店的商品库存

## 中文

    致电商店确认商品是否有货
    发帖者尝试让Manus完成多项任务，包括致电商店查库存；每项任务都失败了，而且它没有拨打任何电话。
    使用的是
    Manus
    他们做了什么
    在Reddit帖子中，用户表示自己用Manus Lite测试了几项需要智能体执行的杂事，其中包括让它致电附近商店，确认某种商品是否有货。Manus没有拨打电话，似乎改用了其他方法，却返回了错误的库存信息；用户亲自核实了至少一个结果，发现该商品实际上没有货。
    进展与成效
    查库存任务失败了：Manus报告一件商品有货，但实际没有，而且尽管用户要求拨打电话，它并未拨打。帖子的更广泛结论是，这名用户在免费档进行的所有试用任务都失败了。
    值得注意
    给出的唯一具体限定是，这些测试是在免费档Manus Lite上完成的。
    亲自尝试
    使用
    Manus
    复制提示词
    请致电或联系[商店名称或附近商店]，询问今天是否有[商品、尺码或型号]的库存。如果你无法拨打电话，请立即告诉我，不要猜测。完成后，给我一份清单，列出每家商店、它们的答复、营业时间和电话号码。在向我展示详情并得到我的批准之前，不要预留或购买任何商品。
    原始来源：https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt

<details><summary>English original</summary>

    Phone stores to check if items are in stock
    Poster tried Manus on several tasks including calling stores to check stock; every task failed and it made no calls.
    Done with
    MA
    Manus
    What they did
    In the Reddit post, the user says they tested Manus Lite on several agent-style errands, including asking it to check whether a product was in stock by calling local stores. Instead of placing calls, Manus appears to have relied on other methods and returned wrong availability information; the user verified at least one result themselves and found the item was not actually in stock.
    How it went
    The stock-check task failed: Manus reported an item was available when it was not, and it made no phone calls despite being asked. The broader takeaway in the post is that all of the user’s trial tasks failed on the free tier.
    Worth knowing
    The only concrete caveat given is that this was done on Manus Lite, the free tier.
    Try it yourself
    with
    Manus
    Copy prompt
    Please call or contact [store names or nearby stores] and ask whether they have [item, size, or model] in stock today. If you cannot place calls, tell me so right away instead of guessing. When finished, give me a list showing each store, its answer, its hours, and its phone number. Do not reserve or buy anything without showing me the details and getting my approval first.
    Original source: https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt

</details>

## 原作者的方法与来源

来源：[nimjay on stock checks with Manus Lite](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt)

作者方法摘要

1. 作者要求Manus Lite致电当地商店确认商品库存。
   English summary: The author asked Manus Lite to check local product stock by calling stores.

2. 作者报告收到错误的有货答复，且没有发生通话，同时承认为此拨号可能没有必要。
   English summary: They report a false in-stock answer and no calls, while acknowledging that a call might have been unnecessary.

## 简要分析

商业分数未评定。

### 错误库存与没有打电话分别看

原帖可读，作者描述的是一次免费档使用经历，不是我们实测。核心反证是有货答复与作者核实不一致；作者自己也承认为库存特地打电话可能过度，所以只要可靠线上来源已满足需求，不拨号不必然代表失败。真正问题在于没有解释实际查证方法，却给出不可靠库存结论。缺商品、门店、查询时点和会话记录，无法复现原因或统计失败率。

依据：[Sauthor](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt), [Sdirectory](https://agentusecases.ai/use-case/phone-stores-to-check-if-items-are-in-stock)

### 历史经历不能替代当前能力核查

目录标2026年1月16日，原帖本次显示相对时间，未独立确定精确发帖日。作者明确用Manus Lite免费档，不能推广到全部版本、付费方案或今天的接入。针对官方域名检索未取得足以确认当前原生拨号能力的文档，这是本轮资料缺口，不是“不支持电话”的证明。第三方连接器宣传也不能当作Manus官方已验证能力。

依据：[Sauthor](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt)

### 交付要保留方法、时间与商品身份

拟议输出先固定门店地址、精确型号/规格/尺码、数量和查询时间，再分别标注门店人员答复、官方库存页面、聚合库存或未确认。官网列出商品不等于该分店现货；确认时有货也不保证到店时仍在。Google库存说明显示某些状态由销售扫描规律推断，提示不能把所有“有货”标签当逐件实时盘点。无法接通、对方不确定和不出售该型号要分开，不让模型补全肯定答复。

依据：[Sauthor](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt), [Sinventory](https://support.google.com/business/answer/13738543?hl=en)

### 谁可能需要，谁未必付款

自用需求可能来自急需某个确定型号、希望少跑空趟的人；低频普通购物多半可以自己看官网或打一通电话。拟议付款者还可能是已有客户的采购或跑腿团队，但本案没有收费、续费或订单证据。可以探索减少多店核对与人工交接的成本，不应把一条吐槽当成大市场。商品紧急程度、替代型号接受度和跨店数量，会影响价值。

依据：[Sauthor](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt)

### 已有免费的部分替代

Google官方已有致电商店查询库存功能，代客户查询可免费；这使通用“替人问有货没”的包装面对直接替代。覆盖并不普遍：地区、语言、商品类别和问题类型有限，不能把免费方案说成所有市场完全等价，也不能把库存查询扩展成预留或购买能力。结果还可能混合电话和网页资料，用户应看到每条结论来源，而不只看到一个统一推荐分。

依据：[Sgoogle](https://support.google.com/googleshopping/answer/16742225?hl=en), [Sbusiness](https://support.google.com/business/answer/7690269?hl=en)

### 可复制的是核对流程，不是通用承诺

候选交付是固定数量门店的带来源清单，明确未确认项与过期时间，不承诺一定买到。获客可以假设从已有采购协作或本地服务关系提供合成样例开始；这不是已验证渠道，本轮没有联系商家或潜在客户。复制前必须核实际拨号工具、号码地域、收费、语言和商家退出要求。只卖一段提示词差异很弱；可能积累的是产品字段规范、失败分类和交接记录，但尚无付费验证。

依据：[Sauthor](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt), [Sgoogle](https://support.google.com/googleshopping/answer/16742225?hl=en)

### 同范围的两种成本压力情景

以一份最多五家商店的来源核对清单为单位，每月20份，不含采购或保留商品。低返工假设人工15分钟、按20美元/小时为5美元，加模型预算0.2，已列小计5.2/份、104/月；高返工45分钟为15美元，加模型0.5，小计15.5/份、310/月。全是研究者假设，不是Manus价格或实际工资。电话分钟费、工具固定费、获客、维护、税费未知，必须另加；售价未知，不计算利润或把缺项填零。

依据：[Sauthor](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt)

### 明确同意和通话边界

拨号是联系第三方，不只是搜索。若以后开展真实试点，需要批准商店、目的、频次和费用，按实际地区要求处理身份说明、录音与商家退出，不冒充真人或熟客。查询库存通常不需要透露用户家庭住址、购物历史或账户资料。Google公开说明存在监控与录音，不能向客户承诺所有语音系统不留痕。本轮只读公开网页，没有拨号、提交请求、预留或购买。

依据：[Sbusiness](https://support.google.com/business/answer/7690269?hl=en)

### 自用净收益与维护独立核对

适用人群是愿意核对商品细节、能够判断来源是否可靠的购物者。可能省去重复查询与跑店，但原案只有失败自述，没有净节省数据。设置包括明确型号、地点、可接受替代与来源格式，维护包括号码、营业时间、工具能力和库存时效；频率随实际购买需求而定。应比较总核查与返工时间，不用生成一张表的速度代替实际收益。

依据：[Sauthor](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt), [Sgoogle](https://support.google.com/googleshopping/answer/16742225?hl=en)

### 不拨号的合成验收

先准备三条虚构门店记录：网页有商品但库存未知、店员明确确认指定型号、旧库存记录已过期。要求输出来源/时间/型号/状态，并把不确定项保留为未知。添加同名不同地址与相似型号作为反例；没有通话回执就不得标记“已致电”。预期是正确分类和人工待办，不是证明真实电话任务可用。本轮未运行模型或电话试用。

依据：[Sauthor](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt)

## 自用价值：待核实

原案失败，无净省时测量；来源清晰才可能减少跑空。

依据：Sauthor, Sgoogle, Sbusiness

- 适用人群：有明确型号需求、能复核门店资料的购物者。
- 用途：整理库存来源、时点和待确认门店，不代替预留或购买。
- 预期收益：可能减少重复核对，但没有独立收益证据。
- 设置成本：商品规格、门店地点、工具实际能力与输出标准。
- 维护成本：号码、营业时间、库存时效和工具额度变化。
- 使用频率：按购买需求，通常非每日固定高频。
- 隐私风险：位置、联络方式和录音处理；只给必要资料。
- 错误风险：相似型号、分店错配、旧数据、未接通被补成有货。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/phone-stores-to-check-if-items-are-in-stock

建议工具：Manus

    Please call or contact [store names or nearby stores] and ask whether they have [item, size, or model] in stock today. If you cannot place calls, tell me so right away instead of guessing. When finished, give me a list showing each store, its answer, its hours, and its phone number. Do not reserve or buy anything without showing me the details and getting my approval first.

自编试用模板

准备条件：三条虚构门店与已知状态，加入同名分店和过期记录，不含真实客户信息。

工具：已有文本助手或本地表格；不连接拨号工具。

预期结果：来源、型号、时间与未知状态清楚；未拨号不写已致电，未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/phone-stores-to-check-if-items-are-in-stock

依据：Sdirectory

    Please call or contact [store names or nearby stores] and ask whether they have [item, size, or model] in stock today. If you cannot place calls, tell me so right away instead of guessing. When finished, give me a list showing each store, its answer, its hours, and its phone number. Do not reserve or buy anything without showing me the details and getting my approval first.

### 合成库存来源核对

自编模板

出处：研究团队自编

依据：Sauthor

    只用以下虚构记录核对商品型号、分店、查询时间与库存状态。没有来源就标未知；过期或型号不一致列待确认。没有通话回执不得写已致电。不要访问门店、不拨号、不发送消息、不预留或购买。

## 来源

- [许可目录：电话询问库存案例](https://agentusecases.ai/use-case/phone-stores-to-check-if-items-are-in-stock)：目录完整原文、实际Manus与编辑试用模板；一次个人失败经历不是总体成功率。
- [nimjay：Manus免费档三项任务体验](https://www.reddit.com/r/ManusOfficial/comments/1q6cjfc/good_manus_ai_use_cases_not_covered_by_chatgpt)：作者nimjay自述取消预约未拨号、在线预约遇验证码且耗时超过十分钟、查库存误报有货且未拨号；明确Manus Lite/free。作者也说为库存特地打电话可能过度，因此不能把未拨号本身等同所有失败。无商店、商品、会话或通话证据。其他评论的YouTube采集月花费不属于本案。
- [Google：让Google致电附近商店](https://support.google.com/googleshopping/answer/16742225?hl=en)：官方库存电话功能支持美国已登录用户英文查询，排除IN/LA/MN/MT/NE；多数服装及食品不支持，不能加自定义问题。结果包含电话和在线库存，需区分来源；没有据此推断为用户保留商品。
- [Google：面向商家的自动电话说明](https://support.google.com/business/answer/7690269?hl=en)：代客户查询可免费使用；电话受质量监控和录音，商家可以退出，地区/语言与频次有限，避免深夜清晨拨打。官方称有已提供的商品数据时可直接使用而不再电话询问。
- [Google：库存状态如何判断](https://support.google.com/business/answer/13738543?hl=en)：Local Inventory原Pointy：库存状态可按扫描和销售规律推断，低频商品可显示可用性未知；更长使用时间、更多扫描、POS和库存数量可改善准确度，不等于逐件现场核实或保留库存。
