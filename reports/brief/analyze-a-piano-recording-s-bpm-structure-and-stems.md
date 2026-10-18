# 用 Claude Code 分析钢琴录音的速度、结构与分轨报告

分析深度：简要研究（brief）；商业评分未评定，不计入深研完成数。

## 案例完整中文译文

    分析钢琴录音的 BPM、结构和分轨
    安装一个技能后，Claude Code 安装了 ffmpeg 和 librosa，并对本地 MP3 运行 Python 处理流程，生成了一份关于 BPM、结构和分轨的报告。
    实际使用
    Claude Code
    具体做法
    作者让 Gemini 在 Loooom 上起草了一个技能，然后通过网页界面发布，并将其安装到 Claude Code。他让 Claude 识别歌曲的各个部分，并指向本地 MP3 文件，内容是他的一段 37 秒钢琴片段。Claude 在会话过程中安装了 ffmpeg 和 librosa，并运行了一个 Python 处理流程。
    结果如何
    它生成了一份报告，包含 BPM、拍号、调性、由四个段落组成的时间线，以及分轨列表。BPM 估计约为 91，而标准版本约为 104。虽然片段是钢琴独奏，分轨列表却包含人声和鼓。
    值得知道
    准确度只能粗略看待：BPM 与实际速度有偏差，列出的分轨（底鼓、人声、踩镲）也与钢琴独奏录音不相符。
    自行试用
    推荐工具
    Claude Code
    复制提示词
    我有一份钢琴录音，位于[MP3 文件路径]。安装所需的任何工具（例如 ffmpeg 和 librosa），然后分析它，给我写一份报告，涵盖 BPM、带有各段大致时间戳的歌曲结构，以及在可行情况下分离出的分轨。将报告以[报告文件名]保存在同一个文件夹中，完成后告诉我，并说明输出文件的位置。
    原始来源：https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/

<details>
<summary>English · 完整归档原文</summary>

<pre>Analyze a piano recording&#x27;s BPM, structure and stems
With a skill installed, Claude Code installed ffmpeg and librosa and ran a Python pipeline on a local MP3, producing a report on BPM, structure and stems.
Done with
CC
Claude Code
What they did
The author had Gemini draft a skill on Loooom, then published it through the web UI and installed it in Claude Code. He asked Claude to identify parts of a song and pointed it at a local MP3 of his 37-second piano clip. Claude installed ffmpeg and librosa mid-session and ran a Python pipeline.
How it went
It produced a report with BPM, meter, key, a four-section timeline and a list of stems. The BPM was estimated at about 91 against a canonical ~104. The stem list included vocals and drums, though the clip was solo piano.
Worth knowing
Expect rough accuracy: the BPM was off from the real tempo, and the stems listed (kick, vocal, hi-hat) don&#x27;t match a solo piano recording.
Try it yourself
with
Claude Code
Copy prompt
I have a piano recording at [path to MP3 file]. Install whatever you need (such as ffmpeg and librosa), then analyze it and write me a report covering the BPM, the song structure with approximate timestamps for each section, and separated stems if possible. Save the report as [report filename] in the same folder and tell me when it&#x27;s finished and where the output files are.
Original source: https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/</pre>

</details>

## 原作者的方法与来源

[Loooom: I Built a Skill to Teach Claude to Hear Music — mager.co](https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/)。以下为短双语方法摘要，不是外链文章全文或独立复现。

1. 作者用Gemini起草Loooom技能，发布后在Claude Code中加载，用于一段本地钢琴短录音。
   English summary: The author drafted a Loooom skill with Gemini, published it, and loaded it in Claude Code for a short local piano recording.

2. 他报告称Claude安装了音频依赖，并用Python生成含速度和段落标签的分析报告。
   English summary: He reports that Claude installed audio dependencies and generated a Python analysis report, including tempo and section labels.

3. 展示的速度比较和意外乐器标签属于报告输出，没有独立核验的时间真值或分离音频。
   English summary: The displayed tempo comparison and unexpected instrument labels are reported outputs, without independently verified timing or separated audio.

## 我们的简要分析

商业判断：现有证据不建议商业投入；自用价值待核实。

### 报告生成与音频效果分别验收

当前证据不足以支持商业交付，商业评分不评定。案例只展示一次短录音的报告，没有人工标注真值、误差分布、可听输出或付费使用者。文字完整、术语丰富和流程执行成功，都不能替代音频结果验收。商业交付应逐项检查节拍、段落和文件，而不是以报告看起来专业为通过条件。潜在价值是协助复核已有材料，尚未证明可替代音乐教师、制作人或剪辑师。 依据：[Sd9f07c75a984](https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/), [archive-case-20261017](https://agentusecases.ai/use-case/analyze-a-piano-recording-s-bpm-structure-and-stems)。

### 从输入到交付保留可追踪证据

作者描述的链路是技能说明、Claude Code、本地文件、依赖安装和Python分析；本轮不安装该技能或执行陌生代码。拟议流程应先记录文件哈希、时长、采样率、工具版本和参数，再输出带依据的候选结论，并让人工回听。先复制到独立工作目录、保留原文件，区分分析失败、无信号和未生成文件。FFmpeg的流映射面向已有输入流，命名一个人声输出并不会证明从混音中分离了人声。 依据：[Sd9f07c75a984](https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/), [Sc53a75c06263](https://ffmpeg.org/ffmpeg.html)。

### 标准歌曲速度不是这次演奏的真值

源站译文忠实保留其“约91对标准约104”的表述；分析只把二者作为作者报告中的比较值。业余翻弹可能改变速度，未听取并人工标注该录音，不能断言它实际就应为104，也不能把差13 BPM或12.5%解释为对这次录音的实测误差率。当前librosa开发文档将起音强度、速度估计、节拍选择分成步骤，起音数量也不能直接等同拍数。无可用起音时文档中的0 BPM属于算法输出状态，应在产品层显示未检出而非真实零速度。 依据：[Sd9f07c75a984](https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/), [Se3f89845a890](https://librosa.org/doc/main/_modules/librosa/beat.html), [archive-case-20261017](https://agentusecases.ai/use-case/analyze-a-piano-recording-s-bpm-structure-and-stems)。

### 分轨名称、频带和可听音轨分开

案例归档指出钢琴独奏对应了人声、鼓等分轨名称，这是必须保留的反证。研究未取得可听分轨，不能宣布成功或据此算分离准确率。已读历史librosa示例使用前景/背景掩码，其范围也不能外推到任意乐器多分轨。拟议验收需要实际非空音频文件、与输入一致的时长范围，以及人工回听确认目标声源；文件存在仍不等于声源正确。结构中的主歌、副歌名称也应作为待核对标签，不能仅凭能量高低就判定歌曲形式。 依据：[Sd9f07c75a984](https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/), [S588654d7563a](https://librosa.org/librosa_gallery/auto_examples/plot_vocal_separation.html), [archive-case-20261017](https://agentusecases.ai/use-case/analyze-a-piano-recording-s-bpm-structure-and-stems)。

### 付款理由与免费替代之间的距离

潜在用户是整理自有练习录音的学习者、教师或制作人员，可能的付款人是本人或承担备课与交付预算的工作室；现有资料没有证明这些人已为本技能付款。对于偶发短片段，人工回听和免费Sonic Visualiser的波形、分析及标注功能是具体基线。增加Agent层只有在净复核时间下降、错误可控制时才可能值得付费。平台作者后续回顾提到早期使用有限并调整产品方向，不能把其技能评分当作音频效果或商业需求验证。 依据：[S3b3e7a281dd7](https://www.sonicvisualiser.org/), [S33ce31fd1088](https://www.mager.co/blog/2026-06-02-loooom/), [Sd9f07c75a984](https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/)。

### 人工回听决定单位经济

以下全部为美元预算假设，不是厂商报价或作者账单。每份短录音报告收15，模型/运行0.5、人工20分钟乘30每小时=10、其他0.5、获客2，单位贡献2；月100份、固定50，经营贡献150。人工改为40分钟，单位负8、月负850。另一情景为教师批量设置服务200，运行5、人工4小时乘30=120、其他5、获客30，单位贡献40；月5份固定50时贡献150。若返工至6小时，单位负20、月负150。未扣税和额外固定费用，不能用技能免费推出总成本为零。 依据：[S33ce31fd1088](https://www.mager.co/blog/2026-06-02-loooom/), [S3b3e7a281dd7](https://www.sonicvisualiser.org/), [Sc53a75c06263](https://ffmpeg.org/ffmpeg.html)。

### 反馈与证据等级

本轮检索公开搜索、GitHub和Hacker News方向的Loooom及本技能使用评价，取得原作者材料和平台代码线索，没有取得可核验的独立付费使用结果。作者自评、模型对技能的评分以及平台可访问，都不是客户验证。六份已读资料能够支持工具链和验收边界，但缺少独立市场与音频效果证据，故保存为schema-1简版，不伪装成completed v2深研。404路径不算已读，也不将搜索摘要充当完整技能或实际运行记录。 依据：[Sd9f07c75a984](https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/), [S33ce31fd1088](https://www.mager.co/blog/2026-06-02-loooom/), [Se3f89845a890](https://librosa.org/doc/main/_modules/librosa/beat.html), [S588654d7563a](https://librosa.org/librosa_gallery/auto_examples/plot_vocal_separation.html), [S3b3e7a281dd7](https://www.sonicvisualiser.org/), [Sc53a75c06263](https://ffmpeg.org/ffmpeg.html)。

### 合成检查的范围与停止条件

本轮只用本地自生成脉冲与静音WAV检查输入/输出时长、原文件哈希、-n禁止覆盖及简单间隔计算，并用虚构时间线检查越界、缺口和重叠；不是Claude、librosa或真实钢琴识别测试。91与104的算术差只验证计算。下一步应先有自有音频和人工标注，再比较回听总时间、节拍及段落错误；没有实测就不承诺准确率或节省。如果产生不存在的声源、覆盖原文件、无法给出可听输出，或人工返工吃掉预算，应停止作为收费交付。 依据：[Sc53a75c06263](https://ffmpeg.org/ffmpeg.html), [Se3f89845a890](https://librosa.org/doc/main/_modules/librosa/beat.html), [S588654d7563a](https://librosa.org/librosa_gallery/auto_examples/plot_vocal_separation.html)。

## 自用与试用准备

可以辅助设计报告和验收，但没有独立准确性或净省时证据，真实录音仍需回听。

准备：自生成脉冲或静音音频、虚构时间线和人工答案；不含私人或第三方录音。

工具：仅现有本地Python标准库及已安装FFmpeg；不安装技能、模型、项目或依赖。

预期：输入/输出元数据、区间验收和待核实项；不声称真实钢琴识别成功。

### 用合成音频设计报告验收

研究团队自编，未调用模型实测。

    请仅使用[自生成脉冲/静音音频及人工提供的虚构时间线]设计离线音频报告验收。先列现有工具，禁止安装依赖、安装技能、下载模型或调用付费API。保留输入哈希和原文件，在独立目录处理。分别核对时长、采样率、区间起止、重叠/缺口和文件是否存在；未检出速度、未知调性、未生成分轨必须明确标注，不猜测。不要把起音个数当拍数，不把标准歌曲速度当本次演奏真值，不把能量峰当副歌，也不把频带或分轨名称当可听声源。若没有独立音轨就写未分离；若有输出仍需人工回听，不宣称识别正确。列出需人工验证的节拍、段落和声源，输出误差与人工时间记录表后停止。本模板为研究团队自编，未调用模型实测。

## 来源

- [Analyze a piano recording's BPM, structure and stems](https://agentusecases.ai/use-case/analyze-a-piano-recording-s-bpm-structure-and-stems)：完整源站叙述和试用模板的既有归档；不是独立准确率验证。
- [Loooom: I Built a Skill to Teach Claude to Hear Music — mager.co](https://www.mager.co/blog/2026-03-26-loooom-identify-song-parts/)：作者单次37秒钢琴演示、工具链和报告结果，未独立复现，不等于测量真值或可听分轨。
- [Loooom: Curated Skills for People Who Don't Code — mager.co](https://www.mager.co/blog/2026-06-02-loooom/)：作者2026年6月回顾平台尝试、使用有限、转向精选非技术技能及免费定位；非独立用户证据。
- [Sonic Visualiser](https://www.sonicvisualiser.org/)：Sonic Visualiser官方免费开源音频可视化、分析和标注功能，作为人工复核替代。
- [ffmpeg Documentation](https://ffmpeg.org/ffmpeg.html)：FFmpeg官方媒体转换、流映射和-n禁止覆盖说明；不证明可由名称分离独立声源。
- [librosa.beat — librosa 1.0.0 documentation](https://librosa.org/doc/main/_modules/librosa/beat.html)：当前main开发文档源码说明起音、速度估计和节拍跟踪步骤与无起音时输出；不证明案例当时版本或准确率。
- [Vocal separation — librosa-gallery 0.1.0 documentation](https://librosa.org/librosa_gallery/auto_examples/plot_vocal_separation.html)：历史librosa-gallery 0.1.0文档演示前景/背景分离；不是任意六种乐器分轨保证或当前版本复现。
