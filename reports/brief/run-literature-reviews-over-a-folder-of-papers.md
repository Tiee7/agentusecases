# 用 Claude Code 整理论文文件夹与共同引用

## 中文

    对整份论文文件夹开展文献梳理
    研究人员让Claude Code处理50多篇论文，提取参考文献、查找共同引用的核心作品，并围绕研究主题把相关性列表写入文件。
    使用的是
    Claude Code
    他们做了什么
    作者在Claude Code中设置自定义斜杠命令，将研究主题写入CLAUDE.md。/lit-map从papers/文件夹的每份PDF提取文本，再提取各篇论文的研究目标、方法、结论和关键词，把高、中、低相关性列表写入literature_map.md。/citation-network提取参考文献，找出多篇论文共同引用的作品并排序。
    进展与成效
    作者声称，/lit-map把处理50篇论文的时间从2至3天缩短到30分钟，/citation-network把处理10篇论文的时间从4至5小时缩短到15分钟。这些是前后对比说法，并非测量结果。
    值得注意
    扫描版或纯图片PDF会降低准确性。研究人员仍需检查AI的评分和摘要，并应在把未发表或受版权保护的文本发送到云服务前检查条款和政策。
    亲自尝试
    使用Claude Code
    复制提示词
    阅读文件夹[我的论文文件夹路径]中的每篇论文，将各篇的参考文献提取到名为bibliographies.md的文件。然后识别这些论文中被引用次数最多的作品，并写出relevance_list.md，按照与[我的研究主题]的相关程度为所有论文排序，每篇给出一句理由。不要修改或删除任何原文件。两个文件都已生成，并告诉我排名前10的核心作品后，任务才算完成。
    原始来源：https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en

<details><summary>English original</summary>

    Run literature reviews over a folder of papers
    Researchers point Claude Code at 50+ papers to extract bibliographies, find core cited works, and write relevance lists against a theme as files.
    Done with
    CC
    Claude Code
    What they did
    The author sets up custom slash commands in Claude Code, and the research theme goes in CLAUDE.md. /lit-map extracts text from every PDF in a papers/ folder. It pulls each paper's objective, method, conclusion and keywords, then writes a High/Medium/Low relevance list to literature_map.md. /citation-network extracts the bibliographies, finds works cited across several papers, and ranks them.
    How it went
    The author claims /lit-map cuts 50 papers from 2-3 days to 30 minutes, and /citation-network cuts 10 papers from 4-5 hours to 15 minutes. These are before/after claims, not measured results.
    Worth knowing
    Scanned or image-only PDFs lower accuracy. The researcher still has to check the AI's scores and summaries, and should review the terms and policies before sending unpublished or copyrighted text to cloud services.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Read every paper in the folder [path to my papers folder] and extract each one's bibliography into a file called bibliographies.md. Then identify the works cited most often across the papers, and write relevance_list.md ranking all papers by how relevant they are to [my research theme], with one sentence of reasoning each. Don't modify or delete any of the original files. You're done when both files exist and you've told me the top 10 core works.
    Original source: https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en

</details>

## 原作者的方法与来源

https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en

The tutorial proposes custom commands for PDF extraction and citation overlap.
教程提出自定义命令用于PDF提取和引用重叠整理。

Timing claims lack input sets, command definitions and reproducible output artifacts.
耗时主张缺输入集合、命令定义和可复现输出。

## 简要分析

商业分数未评定。

### 教程能提供思路，效果尚无复现依据

原文可读，日期显示2026年7月27日；目录标Undated，两者分别记录。作者是发布Claude Code培训内容的账号，文末有课程推广。文章展示两个命令名和阶段，却没有命令定义、输入论文列表、模型版本、输出样本或计时日志。30分钟和15分钟属于教程声称的前后对比，不能当已测效率，更不能当收入。当前保留简报，优先补可重现材料。

依据：[Sauthor](https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en), [Sdirectory](https://agentusecases.ai/use-case/run-literature-reviews-over-a-folder-of-papers)

### 两个命令与目录试用模板并不完全相同

作者描述/lit-map先提取PDF文本，再整理目标、方法、结论、关键词及主题相关性；/citation-network统计参考文献的重叠。目录Copy prompt把任务合并，要求bibliographies.md和relevance_list.md，而原教程提到literature_map.md。保留这一区别，不能声称下载了现成命令。研究主题、排除条件和输出位置需事先明确，原始文件只读。

依据：[Sauthor](https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en), [Sdirectory](https://agentusecases.ai/use-case/run-literature-reviews-over-a-folder-of-papers)

### 引用频次不能直接充当相关性

在指定文件夹内频繁被引，只代表该集合内的共同引用，不证明全领域重要性。需先处理同篇论文标题变体、DOI、预印本与正式版重复，再计算去重后的引用论文数。相关性排序应另有主题标准和页码依据；方法相反或负面结果也可能重要。扫描文本和参考文献排版可能产生漏项，这些是建议验收风险，尚未量化本工作流误差。

依据：[Sauthor](https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en)

### 多文件处理有现成替代

教程把其他聊天工具描述为只能逐篇处理，不能据此建立独占卖点。Google官方说明支持多份来源与PDF；Elicit已有文献检索和提取流程。Claude Code可自定义文件输出和处理步骤，官方技能机制确实存在，但自定义能力不等于该教程效果已验证。选择应比较可追溯输出、人工纠错和机构允许的数据路径。

依据：[Snotebook](https://support.google.com/gemininotebook/answer/16215270?co=GENIE.Platform%3DDesktop&hl=en-5), [Selicit](https://elicit.com/pricing?redirected=true), [Sskills](https://code.claude.com/docs/en/skills)

### 适合已有论文集合的研究者先小样本验证

使用场景是定期整理已收集资料；真正收益应计算提取加复核的总时间。首次需明确研究问题、准备有权使用的文本PDF、建立引用去重规则；维护涉及格式变化和主题调整。未发表材料可能敏感，终端本地文件并不自动意味着推理完全离线。应先核机构与服务设置，不把教程关于本地处理的笼统表述当权限结论。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-literature-reviews-over-a-folder-of-papers), [Sauthor](https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en)

### 付费方向与作者成果分别看

可能收费的工作是给团队配置可审计整理流程、培训和维护，而非售卖未经复核的学术结论。这只是候选模式。已有专业产品构成替代，作者推广课程也不证明课程销量。缺实际交付工时、复核错误、付费客户和续用证据，本例不评分也不编利润情景。下一步问清哪类结果人工最难校对，再判断是否需要定制。

依据：[Selicit](https://elicit.com/pricing?redirected=true), [Sauthor](https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en)

### 先做三份合成材料的可核对检查

拟议验证用三份自行编写的小文档：两份共享同一引用但格式不同，一份与主题无关，再放一条缺DOI的引用。预期输出标注文件与页码、合并重复项、单列未知、不删除原件；人工已知答案用于核对。计时应包括复核。此轮没有运行Claude Code或上传真实论文，没有宣称已通过此测试。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-literature-reviews-over-a-folder-of-papers)

### 升级深研需要的材料

先补作者命令定义和可分享的小样本输入输出，再记录运行配置、失败项与复核耗时。若只得到相似教程而没有执行证据，继续保持简报。若输出无法逐条回到论文位置，或整理加复核比手工更慢，就缩小为目录索引辅助，不把自动摘要用于最终综述结论。

依据：[Sauthor](https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en), [Sskills](https://code.claude.com/docs/en/skills)

## 试用准备与预期结果

三份自行编写且答案已知的小文档，无机密或未授权全文。
来源位置、引用去重、未知项与相关性理由，原件不改。

仅整理这三份合成材料，逐条保留文件和页码。合并格式不同的同一引用；缺失标未知。引用频次与主题相关性分开，不修改原件。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/run-literature-reviews-over-a-folder-of-papers)：保留目录原文、工具与提示词，目录自己标明耗时为作者说法。
- [Claude Code研究所教程，页面日期2026-07-27](https://note.com/claudecode_lab/n/n8bc3cb76575d?hl=en)：教程列操作阶段与效率主张，但没有提供命令文件、论文集合或结果样本；末尾推广培训。
- [Claude Code技能官方文档](https://code.claude.com/docs/en/skills)：官方确认自定义技能机制，不能据此验证该作者的命令或耗时。
- [Google多来源笔记官方说明](https://support.google.com/gemininotebook/answer/16215270?co=GENIE.Platform%3DDesktop&hl=en-5)：官方支持多份来源及PDF，反驳教程将多文档处理说成独有优势。
- [Elicit官方产品与价格](https://elicit.com/pricing?redirected=true)：提供论文搜索、提取和系统综述工作流；价格存在不同客群与年付档，不混成单一月付报价。
