# 用Claude搜索种子并交给qBittorrent处理

## 中文

    让Claude寻找种子并加入qBittorrent
    发帖者让Claude搜索种子并将其加入qBittorrent，这是其智能家居配置的一部分。
    使用的是
    CL
    Claude
    他们做了什么
    发帖者把Claude接入了本地智能家居和媒体系统：Home Assistant负责设备控制；在媒体方面，他们说Wyoming转录服务把内容传给Python桥接程序，后者调用Claude API，再由Claude搜索种子并加入qBittorrent。当时，他们先大声让Claude根据自己的Plex观看历史和Letterboxd评分推荐内容，然后要求它获取《Euphoria》。流程卡住后，他们手动排查运行Plex的Ubuntu机器，而没有使用能在手机上访问的qBittorrent网页界面。
    进展与成效
    系统运行并不稳定。发帖者说种子处理流程挂起，自己调试了15分钟，约会对象则离开了。他们还说，范围更广的“Crash-at-home”例行流程大约有80%的时候能运行成功。
    值得了解
    主要问题是在时间紧张时的可靠性：自动化种子步骤慢到打乱了现场互动，而当时忘了已有的网页界面备用方案。
    亲自尝试
    使用
    Claude
    复制提示词
    从[可信来源或网站，如有]搜索[我想要的标题及版本或画质]的种子，选择做种情况最好的合法选项。在将其加入位于[我的qBittorrent网页界面地址]的qBittorrent之前，先展示名称、大小、做种者数量和来源，让我批准。等我确认后再添加，并向我报告它已进入队列且正在下载。
    原始来源：https://www.reddit.com/r/redscarepod/comments/1uj7cdl/date_ruined_because_of_my_smart_home_setup

<details><summary>English original</summary>

    Have Claude find a torrent and add it to qBittorrent
    The poster has Claude search for a torrent and add it to qBittorrent as part of a smart home setup.
    Done with
    CL
    Claude
    What they did
    The poster had Claude wired into a local smart-home and media setup: Home Assistant handled device control, and for media they say a Wyoming transcription service fed a Python bridge that called the Claude API, which then searched for a torrent and added it to qBittorrent. In the moment, they asked Claude aloud for recommendations from their Plex history and Letterboxd ratings, then told it to fetch Euphoria; when it stalled, they manually troubleshot the Ubuntu box hosting Plex instead of using qBittorrent’s phone-accessible web UI.
    How it went
    It worked inconsistently enough that the poster says the torrent flow hung and they spent 15 minutes debugging while their date left. They also say the broader Crash-at-home routine works about 80% of the time.
    Worth knowing
    The main catch is reliability under pressure: the automated torrent step was slow enough to derail the interaction, and the fallback web UI existed but was forgotten in the moment.
    Try it yourself
    with
    Claude
    Copy prompt
    Search for a torrent of [title and version or quality I want] from [trusted source or site, if any] and pick the best-seeded legitimate option. Before adding it to qBittorrent at [my qBittorrent web UI address], show me the name, size, seeders, and source so I can approve it. Once I confirm, add it and report back that it's queued and downloading.
    Original source: https://www.reddit.com/r/redscarepod/comments/1uj7cdl/date_ruined_because_of_my_smart_home_setup

</details>

## 原作者的方法与来源

https://www.reddit.com/r/redscarepod/comments/1uj7cdl/date_ruined_because_of_my_smart_home_setup
原Reddit存在既有安全限制；只保存目录转述，未读取或翻译原帖。

## 简要分析

商业分数未评定。

### 一次失败叙述，不能换算成功率

案例最有用的是失败路径：语音调用与下载链路卡住后，作者转去排障，没有及时使用已有网页界面。目录转述的15分钟未有日志核验；80%描述范围更大的Crash-at-home流程，不能当种子下载、Claude或qBittorrent的成功率。没有样本量、条件或收入数据，个人故事也未经原帖核验。

依据：[Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)

### 方便操作的收益容易被故障抵消

推断需求是用口头意图替代寻找资源、复制链接和打开下载器。适合已有本地媒体管理习惯的人，但临时社交场景对等待更敏感。如果用户必须理解多台机器、多个进程才能恢复，便利性可能转为维护负担。先比较正常一次操作与失败恢复所用时间，而不是只展示语音触发的顺畅片段。

依据：[Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)

### 语音协议、桥接与下载器职责分开

目录所述链路为Wyoming转录、Python桥接、Claude API、搜索和qBittorrent；Home Assistant另负责设备控制，Plex与Letterboxd提供偏好背景。官方Wyoming文档只支持语音服务连接这一部分，不能证明作者桥接程序存在或可靠。未取得源码、版本、重试策略和故障位置，不补造完整实现。

依据：[Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent), [Swyoming](https://www.home-assistant.io/integrations/wyoming)

### 先区分候选、批准、入队与实际状态

目录模板要求批准后添加并报告排队和下载。技术上排队、获取元数据、传输、停滞和完成是不同状态；必须按可读取的实际状态反馈，不能因添加请求被接受就说下载完成。拟议设计先列出来源与目标供核对，重复触发先查同一任务，超时显示停在哪一步并提供人工入口；这不是本案已实现功能。

依据：[Sqbit](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-5.0)), [Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)

### 只在已授权发行材料上验证

原文提及特定影视作品，但本轮没有核验其分发授权，也不寻找该作品下载源。BitTorrent只是传输方式，做种者多不能证明内容合法、真实或安全。可用Ubuntu官方发布材料设计测试，先核对来源、版本和校验信息；本轮只读页面，不添加、下载、安装或做种。目录原模板作为许可文本保留，与实际演练范围区分。

依据：[Subuntu](https://ubuntu.com/download/alternative-downloads), [Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)

### 商业候选是有限范围配置支持

若客户确有持续需求，可假设对合法文件分发或家庭工作流提供配置、状态监测和维护服务，而非售卖未经授权内容获取。付费理由应是可靠性、可恢复性和更少人工操作；本案没有客户合同或付款。低频个人用途可能只值一次设置，不能直接推出订阅收入、复购率或可规模复制。

依据：[Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)

### 先展示可退出的最小流程

拟议获客演示可限定为一个获准公开文件和模拟下载状态，展示准确反馈、去重、超时后退出与人工接管。交付要有版本清单、健康检查、停止方式和简单界面。若每户网络与设备都需要定制排障，服务很难低价复制；应先记录支持时间，再讨论推广。本轮未联系客户或部署系统。

依据：[Sqbit](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-5.0)), [Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)

### 维护与流量也是成本

成本未知项包括Claude API用量、常开机器电费、存储与带宽、语音误识别复核和桥接维护。局部语音可本地运行，不等于后续Claude API不外发数据。原系统失败可能来自任一环节，不能未经日志就归因模型。自用也应把恢复时间纳入成本；没有真实用量与耗时，不填虚构单位经济。

依据：[Swyoming](https://www.home-assistant.io/integrations/wyoming), [Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)

### 适用人群、频率与隐私风险

更适合能维护本地服务、且确有重复合法下载需求的爱好者。收益只是减少入口切换的可能，尚无净节省测量。设置涉及语音链路、桥接、下载器连接和权限；维护要检查版本、磁盘、任务状态与人工备用入口。频率按真实需求。语音、观看历史和评分可能暴露偏好，下载器权限也可能影响已有文件；误识别、错误版本、重复任务和失去响应都需能安全停止。

依据：[Sdirectory](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)

### 先做离线失败回执演练

用虚构文件名及模拟状态序列练习：待批准、入队、取元数据、停滞、传输、完成、重复和拒绝。不调用真实下载API，不使用影视作品。预期输出准确的阶段说明与停止选项；本轮未执行。如果模型把排队说成已下载、超时重复添加或要求关闭安全措施，先修流程。通过后是否进行真实公开材料下载需另行明确范围。

依据：[Sqbit](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-5.0)), [Subuntu](https://ubuntu.com/download/alternative-downloads)

## 试用准备与预期结果

虚构文件名与模拟状态表，不接真实下载器。
阶段说明、去重和停止选项；本轮未运行。
只处理虚构文件和我提供的下载状态，不访问真实下载器。区分待批准、排队、获取元数据、传输、停滞和完成。重复输入先去重，超时输出人工退出选项。不要添加或下载任何文件，不修改安全设置。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/have-claude-find-a-torrent-and-add-it-to-qbittorrent)：目录正文现场复核与既有归档一致（忽略CL装饰缩写）；15分钟排障与80%均为作者自述，80%属于更广例行流程。
- [Home Assistant Wyoming协议说明](https://www.home-assistant.io/integrations/wyoming)：Wyoming连接语音服务，支持本地语音识别、合成和唤醒；可在局域网其他设备运行。不是内置种子搜索或Claude桥接实现。
- [Ubuntu官方替代下载](https://ubuntu.com/download/alternative-downloads)：官方提供BitTorrent下载，可作为已授权发行材料的候选测试来源；页面也提供标准下载。未实际下载。
- [qBittorrent官方WebUI API文档](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-5.0))：文档适用v5.0+；添加与查询状态分开。queuedDL排队、metaDL取元数据、downloading传输、stalledDL无连接，不能混称完成。
- [原Reddit智能家居叙述](https://www.reddit.com/r/redscarepod/comments/1uj7cdl/date_ruined_because_of_my_smart_home_setup)：未独立核验个人经历、80%或15分钟。
