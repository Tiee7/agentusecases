# 用ChatGPT根据菜单照片整理点餐清单

## 中文

    根据餐厅菜单照片，用ChatGPT整理点餐清单
    顾客拍下菜单，让ChatGPT编排点餐内容，再把手机屏幕展示给餐厅工作人员。
    使用的是
    ChatGPT
    他们做了什么
    在Reddit讨论中，一位服务员说，有位顾客在手机上看餐厅菜单，咨询ChatGPT，然后点了它认为最好的菜。评论里另一位服务员描述了更完整的做法：客人拍下大菜单，请ChatGPT搭配一份订单，再把手机上生成的清单展示出来，让服务员抄下并录入。
    进展与成效
    对于犹豫不决或不善社交的客人，这有时能加快点餐；但多位评论者说，它也会推荐不存在的菜品、折扣或餐厅，导致餐桌上的争论和更正。
    值得了解
    主要问题是可靠性：评论者反复报告ChatGPT编造菜单菜品，因此工作人员仍须将每道菜与实际菜单核对。
    亲自尝试
    使用ChatGPT
    复制提示词
    我附上了[餐厅]的菜单照片。我想为[人数]人点一餐，预算大约[金额]，偏好或限制如下：[饮食需求、不喜欢的食物、辣度]。请建议一份点餐清单，再写成可以给服务员看的简短清晰列表，并明确写出所有调整要求。给出最终清单后就停止。
    原始来源：https://www.reddit.com/r/Serverlife/comments/1vfnswm/a_customer_ordered_from_our_menu_using_chatgpt

<details><summary>English original</summary>

    Order from a restaurant menu photo with ChatGPT
    Customers photograph a menu, have ChatGPT compose their order, and show the phone screen to restaurant staff.
    Done with
    GP
    ChatGPT
    What they did
    In the Reddit thread, a server says one customer looked at the restaurant menu on his phone, consulted ChatGPT, and then ordered the item it said was best. In the comments, another server describes the fuller pattern: guests photograph a big menu, ask ChatGPT to build an order, then show the generated order on their phone for the server to write down and enter.
    How it went
    It sometimes speeds ordering for indecisive or socially awkward guests, but multiple commenters say it also recommends dishes, discounts, or restaurants that do not exist, leading to arguments and corrections at the table.
    Worth knowing
    The main catch is reliability: commenters repeatedly report ChatGPT inventing menu items, so staff still have to verify every item against the actual menu.
    Try it yourself
    with
    ChatGPT
    Copy prompt
    I'm attaching a photo of the menu at [restaurant]. I want a meal for [number of people] with a budget of about [amount], and these preferences or restrictions: [dietary needs, dislikes, spice level]. Suggest an order, then write it as a short, clear list I can show the waiter, with any modifications spelled out. Stop when you've given me the final list.
    Original source: https://www.reddit.com/r/Serverlife/comments/1vfnswm/a_customer_ordered_from_our_menu_using_chatgpt

</details>

## 原作者的方法与来源

https://www.reddit.com/r/Serverlife/comments/1vfnswm/a_customer_ordered_from_our_menu_using_chatgpt
既有Reddit站点安全拦截后不继续访问；原帖未读取。

## 简要分析

商业分数未评定。

### 实际交付是一张给服务员看的清单

目录描述顾客看菜单、拍照或咨询ChatGPT，再把结果交给服务员录入。这个过程没有证明接入餐厅系统，也没有自动付款或正式提交订单。标题中的点餐应理解为辅助选择与表达。原帖在此前Reddit站点安全拦截后没有继续访问，目录标未注明日期，不能把本次收录日当事件发生日。

依据：[Sdirectory](https://agentusecases.ai/use-case/order-from-a-restaurant-menu-photo-with-chatgpt)

### 省去选择负担，也可能转嫁核对负担

目录转述有时帮助犹豫或不善表达的顾客，也转述不存在菜品、折扣和餐厅造成争论。这是两面的观察，缺总样本、发生率和耗时日志，不能算成功率或节省人工。研究者建议同时测顾客选择时间与服务员纠错时间；只看生成清单速度会漏掉餐桌上的返工。

依据：[Sdirectory](https://agentusecases.ai/use-case/order-from-a-restaurant-menu-photo-with-chatgpt)

### 先读清楚菜单，再做选择

官方说明图片解读可能出错，模糊、旋转、小字和部分非拉丁文字会影响结果。拟议流程先列实际识别出的菜名、价格、照片区域和看不清字段，经人核对后再组合。不要用模型熟悉的常见菜补齐缺失项；更不能凭印象增加折扣。菜名原文保留便于服务员对照，译名只作辅助。

依据：[Simage](https://help.openai.com/en/articles/8400551-chatgpt-image-inputs-faq)

### 餐费估算必须保留未知项

目录模板要求人数和预算，但没有显示它能获取当日供应、规格、税费或服务费。拟议清单应把数量乘单价的小计与尚未确认的费用分开；修改要求可能不被餐厅接受或另行收费。订单应在工作人员确认菜品、供应、调整和最终金额后才成立。照片推导出的清单不是餐厅报价，本轮没有实际购物或下单。

依据：[Sdirectory](https://agentusecases.ai/use-case/order-from-a-restaurant-menu-photo-with-chatgpt)

### 饮食偏好与过敏安全分别处理

FARE建议直接与工作人员沟通原料和制作方式，并确认交叉接触风险。照片没有列出某种原料，不表示厨房没有该原料或共用设备。研究者建议清单把过敏事项写成需要餐厅确认的问题，不生成“肯定安全”的标签。普通口味偏好可以帮助筛选，但不能替代过敏沟通；本轮不处理任何人的私人健康信息。

依据：[Sdining](https://www.foodallergy.org/resources/dining-out), [Scross](https://www.foodallergy.org/resources/avoiding-cross-contact)

### 仅需翻译时，现成工具已能完成一部分

Google相机翻译支持图片文字与原文对照，也提醒清晰度影响准确性。它与本案的多人预算搭配不完全等价，却足以覆盖只想读懂菜单的需求。另一替代是指着原菜单直接询问服务员。因此独立产品要证明在有限菜单内组合、清晰表达和减少纠错方面有额外价值，而非把已有拍照翻译重新包装就声称有付费市场。

依据：[Stranslate](https://support.google.com/translate/answer/6142483?hl=en), [Sdirectory](https://agentusecases.ai/use-case/order-from-a-restaurant-menu-photo-with-chatgpt)

### 商业化尚缺付费人与稳定菜单来源

商业假设有两种：面向旅行者的工具功能，或餐厅维护官方菜单后提供辅助选菜。前者面临现成工具和获客成本，后者需要餐厅维护SKU、价格、售罄和调整规则，交付范围明显扩大。没有本案客户、订单收入或使用留存证据，不做虚构利润模型。若试验，先验证菜单维护与客服纠错成本；模型调用费不能代表总成本。

依据：[Sdirectory](https://agentusecases.ai/use-case/order-from-a-restaurant-menu-photo-with-chatgpt), [Stranslate](https://support.google.com/translate/answer/6142483?hl=en)

### 低准备成本仍需逐次确认

自用准备是清晰完整照片、人数、预算和口味；使用频率随外出就餐，没有证据证明每天高频。清单可能减少组织语言的负担，但净收益尚未测量。每次都要核对当前菜单，旧照片不能当实时库存。隐私方面避免拍入旁人、账单和个人信息；若涉及敏感饮食健康信息，需明确使用范围。错误风险集中在识别、价格、可用性和不被接受的修改。

依据：[Sdirectory](https://agentusecases.ai/use-case/order-from-a-restaurant-menu-photo-with-chatgpt), [Simage](https://help.openai.com/en/articles/8400551-chatgpt-image-inputs-faq)

### 先做离线人工对照，不接订单系统

下一步用自制无敏感信息的菜单测试：十个明确菜品、两处故意模糊字段和一个不存在的优惠请求。要求只从可辨认项目选菜，未知项保留，并输出原文菜名、数量、小计与待确认问题。由人对照检查是否新增菜名或臆造优惠，再与直接读菜单或相机翻译比较总时间。若仍经常补造菜品，或纠错多于节省，就停止投入。本轮只是提出测试方案，未真实试用。

依据：[Sdirectory](https://agentusecases.ai/use-case/order-from-a-restaurant-menu-photo-with-chatgpt), [Stranslate](https://support.google.com/translate/answer/6142483?hl=en)

## 试用准备与预期结果

自制无敏感信息菜单、人工答案、明确预算人数。
仅含可读菜单项目的候选清单及待确认事项；本轮未测试。
仅根据这份自制菜单，先列能确定的原文菜名和价格；模糊内容标未知，不补造菜品、餐厅或优惠。按人数预算组合，列数量与小计，未知费用另列。输出供人审核的清单，修改要求和过敏相关事项标待餐厅确认，不声称安全，不下单。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/order-from-a-restaurant-menu-photo-with-chatgpt)：菜单照片、顾客清单和服务员人工录入；正负反馈均为转述。
- [OpenAI图像输入说明](https://help.openai.com/en/articles/8400551-chatgpt-image-inputs-faq)：图像识别支持及模糊、小字、旋转与准确性限制。
- [Google相机翻译说明](https://support.google.com/translate/answer/6142483?hl=en)：现成图片翻译、原文对照，文字清晰度影响准确性。
- [FARE外出就餐沟通](https://www.foodallergy.org/resources/dining-out)：直接向餐厅确认原料和制备方式。
- [FARE交叉接触说明](https://www.foodallergy.org/resources/avoiding-cross-contact)：菜单文字不足以判断交叉接触情况。
- [原始服务员讨论](https://www.reddit.com/r/Serverlife/comments/1vfnswm/a_customer_ordered_from_our_menu_using_chatgpt)：未核验原帖作者、日期、样本或评论原话。
