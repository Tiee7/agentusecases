# 用 Manus 批量研究公开资料并制作演示文稿

## 中文

    批量研究数百位人物并制作演示文稿
    这份指南介绍如何使用 Manus 完成大规模研究，例如梳理顶尖的250位AI研究者、把活动导出数据转成演示文稿，以及部署网站。
    使用工具
    MA
    Manus
    做了什么
    帖子说，Manus 把大型研究任务拆成许多并行子任务，例如启动250个子智能体，每个研究一位AI研究者，并在10至15分钟内完成。它也描述了输入 Luma 活动导出文件或 Google 表格等结构化资料，再让 Manus 抓取网站、调用 SimilarWeb 等已连接工具，并组装成演示文稿或已部署的可搜索网站等成果；人需要提供提示词、文件、模板、API 以及品牌规则。
    结果如何
    帖子声称得到的结果是可供生产使用的规模化成果：10至15分钟完成250个人物资料的研究、根据活动导出数据制作带图表的演示文稿，以及用含100篇论文的表格建立公开网站。帖子把这些作为示例和提示词模式介绍，但几乎没有说明如何核验结果或遇到哪些失败。
    值得了解
    主要难点在前期准备：结果依赖提供连接器、附加模板或文件，以及清楚的项目或知识规则，让 Manus 遵守品牌和格式要求。
    亲自试用
    使用
    Manus
    复制提示词
    研究[名单或群体，例如某领域排名靠前的100人]，制作一份电子表格，为每个人包含[列，例如姓名、雇主、重要工作、来源链接]。仅使用公开来源，每行都引用一个链接。表格完成后，将主要发现转成一份[数量]页的演示文稿，并标出任何你不确定事实的行。
    原始来源：https://www.reddit.com/r/promptingmagic/comments/1qruaq7/the_complete_guide_to_metas_ai_agent_manus_the

<details><summary>English original</summary>

    Research hundreds of people and build slide decks at scale
    Guide describes using Manus for large research jobs like profiling the top 250 AI researchers, turning event exports into slide decks, and deploying websites.
    Done with
    MA
    Manus
    What they did
    The post says Manus handles big research jobs by splitting them into many parallel sub-tasks, like spinning up 250 sub-agents to profile one AI researcher each and finishing in 10–15 minutes. It also describes feeding in structured inputs such as a Luma event export or a Google Sheet, then having Manus scrape sites, call connected tools like SimilarWeb, and assemble outputs such as slide decks or a deployed searchable website; the person provides the prompt, files, templates, APIs, and any brand rules.
    How it went
    The reported outputs are production-ready assets at scale: a 250-profile research pass in 10–15 minutes, event-export slide decks with charts, and public websites built from a sheet of 100 papers. The post presents these as examples and prompt patterns, but gives little detail on verification or failures.
    Worth knowing
    The main catch is setup: results depend on supplying connectors, attached templates/files, and clear project or knowledge rules so Manus follows brand and formatting requirements.
    Try it yourself
    with
    Manus
    Copy prompt
    Research [list or group, e.g. the top 100 people in a field] and build a spreadsheet with [columns, e.g. name, employer, notable work, source link] for each. Use public sources only and cite a link for every row. When the sheet is complete, turn the key findings into a [number]-slide deck, and flag any rows where you were unsure of the facts.
    Original source: https://www.reddit.com/r/promptingmagic/comments/1qruaq7/the_complete_guide_to_metas_ai_agent_manus_the

</details>

## 原作者方法

原Reddit全文未读取；官方示例回放仅标题可读，不补造作者运行步骤。

## 结论

有实际功能与覆盖核对依据，但指南示例未给逐项结果、失败记录或独立效果验证，交付有依据简报。

## 批量产出与逐项可信是两层要求

这个案例来自指南式介绍，不是附完整测试材料的交付复盘。250个人物、10至15分钟、可供生产使用都保留为原文声称。厂商回放链接在本轮只显示250AI研究者标题，未看到逐行数据、引用和运行日志，所以不能把标题当成功验收。分析重点是能否稳定完成每个条目并准确汇总，而不是宣传启动了多少代理。

来源：Sdirectory, Sguide

## 任务总数不能直接当同时运行数量

当前帮助中心明确写20个并发子任务；指南和产品文档又以250条目或数百代理描述规模，两者可分别指总任务数与并发数，并非必须相互矛盾。每子任务50credits上限也不是整个项目总价。即便假设正好250个子任务，其上限算术为12500credits，仍未覆盖主任务、额外修复或展示加工，且不是实际账单。没有当前账户计费明细，不转换美元，也不承诺固定时长。

来源：Swide, Sguide

## 购买者要的是可使用的比较资料

可能需求来自会务研究、行业分析、市场团队或需要公开研究资料的编辑；付款人可能是项目负责人。价值应体现在统一字段、来源可追溯、遗漏可见和成品可修改，而不在名单长度。案例没有付费客户、销售或净节省时间数据。若现有数据已完整，只差整理和展示，用表格加幻灯片模板或人工分析更简单；如果每个条目问题完全不同，分成同质并行任务反而可能失去必要上下文。

来源：Sdirectory, Srefine, Sslides

## 先固定清单和字段，再研究

研究者建议在开始前明确条目ID、纳入标准、时间窗、字段定义、来源优先级和无法核实的标记。人物同名、雇主变动、论文版本等都可能造成错配，应记录来源日期并交叉核对，而不是用一列名字当唯一标识。把每个独立条目拆开有助于控范围，但最终还需验证所有ID恰好出现一次，并把失败或未知行保留下来。并行不能保证不同代理实际使用了独立来源，也不能消除共同提示词造成的系统性错误。

来源：Sguide, Sintegration

## 验收应分数据、摘要与展示三关

第一关检查名单覆盖、重复、字段类型、引用是否真的支持对应陈述；第二关检验汇总数字的分母、缺失处理和比较口径；第三关逐页检查图表、字号、溢出、来源脚注和可编辑导出。做成精美幻灯片不会修复错误资料，网站公开也不代表通过内容审查。建议先用少量已知结果测试字段，再扩大清单，并保留原始表到图表的映射。OpenRefine能帮助统一格式，但相似名字聚类仍需人判断，不能自动合并成同一人。

来源：Srefine, Sslides, Sintegration

## 连接器不是免费且自动可用的资源

原文提到Luma导出、Google表格、SimilarWeb和品牌模板，但没有逐项提供权限、配额或费用。拥有数据文件不等于获准公开个人资料或长文，工具连接也不等于所有字段都能取到。确定性清理可由OpenRefine与表格承担，研究判断和图表审校交给人；这是具体替代流程，不是声称OpenRefine可替代网络研究。自建编排可更明确追踪任务ID，但需要开发维护和接口预算。本轮没有安装集成、调用付费API或上传任何私有名单。

来源：Sdirectory, Srefine, Sintegration

## 按一份100条目研究加10页简报估算

以下全为研究者假设，美元计价，不是Manus报价。资料整齐情景：工具及额度摊销15、人工5小时×40=200、其它10、获客25，单位250；每月4包另加固定80，共1080。高返工情景：工具60、人工15小时×40=600、其它30、获客80，单位770；每月4包加固定160，共3240。售价未知，不算毛利。SimilarWeb等数据许可、客户接入、专门审稿和持续更新另计；不能把10分钟运行当总交付工时，模板复用也不能把人工复核归零。

来源：Swide, Sslides, Sdirectory

## 服务边界应是可核对交付包

可探索按一份有明确清单、字段与展示页数的交付包收费，再另计后续更新；这是经营假设。本案没有证据支持按代理数量收费或保证资料完整。第一批客户可以来自已有会务或咨询合作，用虚构或公开非敏感样本展示来源链和缺失行，不群发陌生人画像。本轮没有获客外联。可保留的竞争力在选题、数据口径、领域判断和复核，而非简单转售一个宽泛提示词。客户自用工具已能满足时，外包必须说明额外验收价值。

来源：Sdirectory, Sslides, Srefine

## 外围资料只证明机制，不证明本案收益

帮助文档与集成项目提供拆分、格式和覆盖核对的依据，但都是功能或设计说明。官方关于任意规模质量一致、没有其他工具能做的说法缺独立对照，本报告不采用为事实。社区、评价站和代码渠道检索未取得本案等效的可核验用户结果；评论索引片段不算完整反馈。模板支持和导出格式也不证明复杂品牌稿必然完全可编辑或无需人工修复。

来源：Swide, Sguide, Sintegration

## 只建议受控试点

先选择非敏感、字段稳定的小规模公开资料任务，与人工或表格流程比较总时间、错误、缺失、引用覆盖及返工成本，验收后再增加数量。若引用无法支持结论、同名错误反复发生、缺失被静默补齐，或最终人工复核超过约定，应停止扩大。公开网站另设发布确认，人物画像不延伸到敏感属性或高影响个体判断。原案逐步日志、实交数据、真实成本和客户付费仍待补，因此当前是有依据简报而非效果已验证的深研。

来源：Sdirectory, Sguide, Sintegration

## 自用与试用

- 有明确研究清单、能核对来源和使用表格的个人研究者或编辑。
- 把同类条目整理成结构表，再生成阅读简报。
- 可能减少重复搜集与排版，未测净时间或正确率。
- 名单去重、字段定义、合法公开来源、模板与工具权限。
- 来源失效、人物信息变化、模板兼容与修复失败行。
- 按报告或资料更新周期使用，不必为低频小任务启动大批代理。
- 名单和活动导出可能含个人信息，需最小输入与单独发布审阅。
- 同名错配、共同错误来源、缺失填造、图表分母错误与过时资料。

公开非敏感清单、明确字段、允许来源、模板及工具可用额度。
带逐项来源和未知标记的表格及简报，须人工核对再发布。

## 来源

- [Sdirectory · 许可目录案例](https://agentusecases.ai/use-case/research-hundreds-of-people-and-build-slide-decks-at-scale)：指南介绍250人物研究、活动表转幻灯片和100论文表转网站，时间和生产可用性都是帖子声称，核验细节不足。
- [Swide · Wide Research帮助中心](https://help.manus.im/en/articles/11960169-what-is-wide-research)：当前帮助页称付费用户可用、系统自动触发、可同时运行20子任务，每个子任务额度上限50credits。
- [Sguide · Wide Research官方文档](https://manus.im/docs/features/wide-research)：厂商描述按条目分配独立上下文再汇总，给出250人物示例回放链接；回放本轮只有标题，未核250行或过程。
- [Sslides · Manus Slides官方文档](https://manus.im/docs/features/slides)：支持PPTX模板、CSV/Excel输入，以及PPTX/PDF/网页幻灯片和备注导出；时间与效果是厂商说明。
- [Sintegration · Elves第三方集成文档](https://github.com/aigorahub/elves/blob/main/references/provider-shortcuts.md)：该项目描述按清单核对结果ID与缺失项，并区分请求原生Wide和外层独立任务；文档不是本案性能实测。
- [Srefine · OpenRefine数据清理文档](https://openrefine.org/docs/manual/cellediting)：提供列变换、分面与相似字符串聚类；聚类建议需要人确认，类型转换未成功项要检查。

## 核验边界

只读研究，未运行250代理、采集人物画像、上传私密名单或付费调用。云浏览器首次及一次5分钟恢复均超时；采用许可存档和公开Web正文。官方回放仅标题，未核结果。
