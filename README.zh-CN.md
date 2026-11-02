<a id="awesome-selfhosted"></a>
# Awesome-Selfhosted 自托管软件精选清单

[![Awesome](_static/awesome.png)](https://github.com/sindresorhus/awesome) [![](https://github.com/awesome-selfhosted/awesome-selfhosted-data/actions/workflows/check-dead-links.yml/badge.svg)](https://github.com/awesome-selfhosted/awesome-selfhosted-data/issues/1) [![](https://github.com/awesome-selfhosted/awesome-selfhosted-data/actions/workflows/check-unmaintained-projects.yml/badge.svg)](https://github.com/awesome-selfhosted/awesome-selfhosted-data/issues/1) [![](https://img.shields.io/liberapay/goal/awesome-selfhosted.svg?logo=liberapay)](https://liberapay.com/awesome-selfhosted/)

Self-hosting is the practice of hosting and managing applications on your own server(s) instead of consuming from [SaaSS](https://www.gnu.org/philosophy/who-does-that-server-really-serve.html) providers.

This is a list of [Free](https://en.wikipedia.org/wiki/Free_software) Software [network services](https://en.wikipedia.org/wiki/Network_service) and [web applications](https://en.wikipedia.org/wiki/Web_application) which can be hosted on your own server(s). Non-Free software is listed on the [Non-Free](https://github.com/awesome-selfhosted/awesome-selfhosted/blob/master/non-free.md) page.

**[HTML version](https://awesome-selfhosted.net/) (recommended)**, [Markdown version](https://github.com/awesome-selfhosted/awesome-selfhosted) (legacy).

参见 [Contributing](#contributing).

--------------------

<a id="table-of-contents"></a>
## Table of contents 目录

- [Software 软件](#software)
  - [Analytics 分析](#analytics)
  - [Archiving and Digital Preservation (DP) 存档与数字化保存（DP）](#archiving-and-digital-preservation-dp)
  - [Automation 自动化](#automation)
  - [Backup 备份](#backup)
  - [Blogging Platforms 博客平台](#blogging-platforms)
  - [Booking and Scheduling 预订与排程](#booking-and-scheduling)
  - [Bookmarks and Link Sharing 书签与链接分享](#bookmarks-and-link-sharing)
  - [Calendar & Contacts 日历与联系人](#calendar--contacts)
  - [Communication - Custom Communication Systems 通信 - 自定义通信系统](#communication---custom-communication-systems)
  - [Communication - Email - Complete Solutions 通信 - 电子邮件 - 完整方案](#communication---email---complete-solutions)
  - [Communication - Email - Mail Delivery Agents 通信 - 电子邮件 - 邮件投递代理](#communication---email---mail-delivery-agents)
  - [Communication - Email - Mail Transfer Agents 通信 - 电子邮件 - 邮件传输代理](#communication---email---mail-transfer-agents)
  - [Communication - Email - Mailing Lists and Newsletters 通信 - 电子邮件 - 邮件列表与新闻稿](#communication---email---mailing-lists-and-newsletters)
  - [Communication - Email - Webmail Clients 通信 - 电子邮件 - Web 邮件客户端](#communication---email---webmail-clients)
  - [Communication - IRC 通信 - IRC](#communication---irc)
  - [Communication - SIP 通信 - SIP](#communication---sip)
  - [Communication - Social Networks and Forums 通信 - 社交网络与论坛](#communication---social-networks-and-forums)
  - [Communication - Video Conferencing 通信 - 视频会议](#communication---video-conferencing)
  - [Communication - XMPP - Servers 通信 - XMPP - 服务器](#communication---xmpp---servers)
  - [Communication - XMPP - Web Clients 通信 - XMPP - Web 客户端](#communication---xmpp---web-clients)
  - [Community-Supported Agriculture (CSA) 社区支持农业（CSA）](#community-supported-agriculture-csa)
  - [Conference Management 会议管理](#conference-management)
  - [Content Management Systems (CMS) 内容管理系统（CMS）](#content-management-systems-cms)
  - [Customer Relationship Management (CRM) 客户关系管理（CRM）](#customer-relationship-management-crm)
  - [Database Management 数据库管理](#database-management)
  - [DNS 域名系统（DNS）](#dns)
  - [Document Management 文档管理](#document-management)
  - [Document Management - E-books 文档管理 - 电子书](#document-management---e-books)
  - [Document Management - Institutional Repository and Digital Library Software 文档管理 - 机构知识库与数字图书馆软件](#document-management---institutional-repository-and-digital-library-software)
  - [Document Management - Integrated Library Systems (ILS) 文档管理 - 集成图书馆系统（ILS）](#document-management---integrated-library-systems-ils)
  - [E-commerce 电子商务](#e-commerce)
  - [Federated Identity & Authentication 联合身份与认证](#federated-identity--authentication)
  - [Feed Readers 订阅源阅读器](#feed-readers)
  - [File Transfer & Synchronization 文件传输与同步](#file-transfer--synchronization)
  - [File Transfer - Distributed Filesystems 文件传输 - 分布式文件系统](#file-transfer---distributed-filesystems)
  - [File Transfer - Object Storage & File Servers 文件传输 - 对象存储与文件服务器](#file-transfer---object-storage--file-servers)
  - [File Transfer - Peer-to-peer Filesharing 文件传输 - 点对点文件共享](#file-transfer---peer-to-peer-filesharing)
  - [File Transfer - Single-click & Drag-n-drop Upload 文件传输 - 一键与拖拽上传](#file-transfer---single-click--drag-n-drop-upload)
  - [File Transfer - Web-based File Managers 文件传输 - 基于 Web 的文件管理器](#file-transfer---web-based-file-managers)
  - [Games 游戏](#games)
  - [Games - Administrative Utilities & Control Panels 游戏 - 管理工具与控制面板](#games---administrative-utilities--control-panels)
  - [Genealogy 家谱](#genealogy)
  - [Generative Artificial Intelligence (GenAI) 生成式人工智能（GenAI）](#generative-artificial-intelligence-genai)
  - [Groupware 群件](#groupware)
  - [Health and Fitness 健康与健身](#health-and-fitness)
  - [Human Resources Management (HRM) 人力资源管理（HRM）](#human-resources-management-hrm)
  - [Identity Management 身份管理](#identity-management)
  - [Internet of Things (IoT) 物联网（IoT）](#internet-of-things-iot)
  - [Inventory Management 库存管理](#inventory-management)
  - [Knowledge Management Tools 知识管理工具](#knowledge-management-tools)
  - [Learning and Courses 学习与课程](#learning-and-courses)
  - [Manufacturing 制造](#manufacturing)
  - [Maps and Global Positioning System (GPS) 地图与全球定位系统（GPS）](#maps-and-global-positioning-system-gps)
  - [Media Management 媒体管理](#media-management)
  - [Media Streaming 媒体流](#media-streaming)
  - [Media Streaming - Audio Streaming 媒体流 - 音频流](#media-streaming---audio-streaming)
  - [Media Streaming - Multimedia Streaming 媒体流 - 多媒体流](#media-streaming---multimedia-streaming)
  - [Media Streaming - Video Streaming 媒体流 - 视频流](#media-streaming---video-streaming)
  - [Miscellaneous 杂项](#miscellaneous)
  - [Money, Budgeting & Management 金钱、预算与管理](#money-budgeting--management)
  - [Monitoring & Status Pages 监控与状态页](#monitoring--status-pages)
  - [Network Utilities 网络工具](#network-utilities)
  - [Note-taking & Editors 笔记与编辑器](#note-taking--editors)
  - [Office Suites 办公套件](#office-suites)
  - [Password Managers 密码管理器](#password-managers)
  - [Pastebins 粘贴板](#pastebins)
  - [Personal Dashboards 个人仪表盘](#personal-dashboards)
  - [Photo Galleries 相册](#photo-galleries)
  - [Polls and Events 投票与活动](#polls-and-events)
  - [Proxy 代理](#proxy)
  - [Recipe Management 食谱管理](#recipe-management)
  - [Remote Access 远程访问](#remote-access)
  - [Resource Planning 资源规划](#resource-planning)
  - [Search Engines 搜索引擎](#search-engines)
  - [Self-hosting Solutions 自托管方案](#self-hosting-solutions)
  - [Software Development 软件开发](#software-development)
  - [Software Development - API Management 软件开发 - API 管理](#software-development---api-management)
  - [Software Development - Continuous Integration & Deployment 软件开发 - 持续集成与部署](#software-development---continuous-integration--deployment)
  - [Software Development - FaaS & Serverless 软件开发 - FaaS 与无服务器](#software-development---faas--serverless)
  - [Software Development - Feature Toggle 软件开发 - 功能开关](#software-development---feature-toggle)
  - [Software Development - IDE & Tools 软件开发 - IDE 与工具](#software-development---ide--tools)
  - [Software Development - Localization 软件开发 - 本地化](#software-development---localization)
  - [Software Development - Low Code 软件开发 - 低代码](#software-development---low-code)
  - [Software Development - Project Management 软件开发 - 项目管理](#software-development---project-management)
  - [Software Development - Testing 软件开发 - 测试](#software-development---testing)
  - [Static Site Generators 静态站点生成器](#static-site-generators)
  - [Task Management & To-do Lists 任务管理与待办清单](#task-management--to-do-lists)
  - [Ticketing 工单](#ticketing)
  - [Time Tracking 时间追踪](#time-tracking)
  - [Travel Organization 旅行规划](#travel-organization)
  - [URL Shorteners 短链接](#url-shorteners)
  - [Video Surveillance 视频监控](#video-surveillance)
  - [VPN 虚拟专用网络（VPN）](#vpn)
  - [Web Servers Web 服务器](#web-servers)
  - [Wikis 维基](#wikis)
- [List of Licenses 许可证列表](#list-of-licenses)
- [Anti-features 反特性](#anti-features)
- [External Links 外部链接](#external-links)
- [Contributing 贡献](#contributing)
- [License 许可证](#license)

--------------------

<a id="software"></a>
## Software 软件

<a id="analytics"></a>
### Analytics 分析

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Analytics 分析学](https://en.wikipedia.org/wiki/Analytics) 是对数据或统计资料的系统性计算分析，用于发现、解读数据中的有意义模式，并把这些模式传达出来。

_Related: [Database Management 数据库管理](#database-management), [Personal Dashboards 个人仪表盘](#personal-dashboards)_

- [ANALOG](https://github.com/orangecoloured/analog) - 轻量级 analytics 分析 工具。记录 10 至 30 天内的事件。`MIT` `MIT` `Nodejs/Docker`
- [Aptabase](https://aptabase.com/) - 注重隐私、简洁的 analytics 分析 工具，面向移动与桌面应用。([Source Code](https://github.com/aptabase/aptabase)) `AGPL-3.0` `Docker`
- [AWStats](http://www.awstats.org/) - 从 Web、流媒体、FTP 或邮件服务器日志生成统计信息。([Demo](https://www.awstats.org/#DEMO), [Source Code](https://github.com/eldy/awstats)) `GPL-3.0` `Perl`
- [Countly Community Edition](https://count.ly) - 实时移动与 Web analytics 分析、崩溃报告及推送通知平台。([Source Code](https://github.com/Countly/countly-server)) `AGPL-3.0` `Nodejs/Docker`
- [d8a.tech](https://d8a.tech) - 数据收集服务，与你现有的 Google Analytics 配置协同工作，采集用户活动并直接发送至你自己的私有数据库。([Demo](https://lookerstudio.google.com/u/0/reporting/0e4102b6-c38b-4f55-aa25-c1fe91d1c1e9), [Source Code](https://github.com/d8a-tech/d8a)) `MIT` `Go/Docker`
- [Daily Stars Explorer](https://emanuelef.github.io/daily-stars-explorer) `⚠` - 追踪 GitHub 仓库趋势，通过每日 star 洞察查看长期增长与社区关注度。([Demo](https://emanuelef.github.io/daily-stars-explorer), [Source Code](https://github.com/emanuelef/daily-stars-explorer)) `MIT` `Go/Nodejs/Docker`
- [Dreeve](https://dreeve.app/) `⚠` - 基于 Strava 数据生成的统计仪表盘。([Demo](https://statistics-for-strava.robiningelbrecht.be/), [Source Code](https://github.com/dreeveapp/dreeve)) `AGPL-3.0` `Docker/K8S`
- [Druid](https://druid.apache.org) - 分布式、面向列的实时 analytics 分析 数据存储。([Source Code](https://github.com/apache/druid)) `Apache-2.0` `Java/Docker`
- [EDA](https://github.com/jortilles/EDA) - 用于数据分析与可视化的 Web 应用。`AGPL-3.0` `AGPL-3.0` `Nodejs/Docker`
- [GoAccess](http://goaccess.io/) - 运行于终端的实时 Web 日志分析器与交互式查看器。([Source Code](https://github.com/allinurl/goaccess)) `GPL-2.0` `C`
- [GoatCounter](https://www.goatcounter.com) - 轻量 Web 统计，不追踪个人数据。([Source Code](https://github.com/arp242/goatcounter)) `EUPL-1.2` `Go`
- [HitKeep](https://hitkeep.com/) - 注重隐私的 Web analytics 分析，内置目标、漏斗、电商追踪与团队管理，单一二进制内嵌 DuckDB（Google Analytics、Plausible、Umami 的替代方案）。([Source Code](https://github.com/HitKeep/hitkeep)) `MIT` `Go/Docker`
- [Litlyx](https://litlyx.com) - 一体化 analytics 分析 方案。30 秒完成配置。在 AI 驱动的仪表盘上展示全部数据。可完全自托管，符合 GDPR。([Source Code](https://github.com/Litlyx/litlyx)) `Apache-2.0` `Docker`
- [Liwan](https://liwan.dev/) - 注重隐私的 Web analytics 分析。([Demo](https://demo.liwan.dev/p/liwan.dev), [Source Code](https://github.com/explodingcamera/liwan)) `Apache-2.0` `Rust/Docker`
- [Matomo](https://matomo.org/) - 保护你的数据与客户隐私的 Web analytics 分析（Google Analytics 的替代方案）。([Source Code](https://github.com/matomo-org/matomo)) `GPL-3.0` `PHP`
- [Metabase](https://metabase.com/) - 让你公司中每位成员都能提问并从数据中学习的简便方式。([Source Code](https://github.com/metabase/metabase)) `AGPL-3.0` `Java/Docker`
- [Middleware](https://middlewarehq.com/) - 帮助工程负责人借助 DORA 指标衡量并分析团队效能的工具。([Source Code](https://github.com/middlewarehq/middleware)) `Apache-2.0` `Docker/Python/Nodejs`
- [Netron](https://netron.app/) - 神经网络与机器学习模型的可视化工具。([Source Code](https://github.com/lutzroeder/netron)) `MIT` `Python/Nodejs`
- [Offen](https://www.offen.dev/) - 公平、轻量且开放的 Web analytics 分析 工具。在用户可完全访问其自身数据的同时获取洞察。([Demo](https://www.offen.dev/try-demo/), [Source Code](https://github.com/offen/offen)) `Apache-2.0` `Go/Docker`
- [Plausible Analytics](https://plausible.io/) - 简洁、轻量（< 1 KB）且注重隐私的 Web analytics 分析。([Source Code](https://github.com/plausible/analytics/)) `AGPL-3.0` `Elixir`
- [PostHog](https://posthog.com) - 可自托管的 product analytics 产品分析、会话录制、feature flagging 功能开关 与 A/B 测试（Mixpanel、Amplitude、Heap 的替代方案）。([Source Code](https://github.com/posthog/posthog)) `MIT` `Python`
- [Postiz](https://postiz.com) `⚠` - 排程发帖、追踪内容表现，并在一处管理全部社交媒体账号（Buffer、Hootsuite、Sprout Social 的替代方案）。([Source Code](https://github.com/gitroomhq/postiz-app)) `AGPL-3.0` `Docker`
- [Prisme Analytics](https://www.prismeanalytics.com) - 基于 Grafana、注重隐私且渐进式增强的 analytics 分析 服务。([Source Code](https://github.com/prismelabs/analytics)) `AGPL-3.0/MIT` `Docker`
- [Redash](http://redash.io) - 连接并查询数据源，构建仪表盘以可视化数据，并与公司内部分享。([Source Code](https://github.com/getredash/redash)) `BSD-2-Clause` `Docker`
- [Rybbit](https://rybbit.com/) - 易于配置且更直观的 Web 与产品 analytics 分析（Google Analytics 的替代方案）。([Demo](https://demo.rybbit.com/1), [Source Code](https://github.com/rybbit-io/rybbit)) `AGPL-3.0` `Docker`
- [Shaper](https://taleshape.com/shaper/docs) - 完全用 SQL 构建数据仪表盘。由 DuckDB 驱动。([Demo](https://demo.taleshape.com/view/pvggvdpiwb9wlyppuqbyx0nt), [Source Code](https://github.com/taleshape-com/shaper)) `MPL-2.0` `Docker/Nodejs/Python/Go`
- [Socioboard](https://github.com/Socioboard-developers/Socioboard-5.0) `⚠` - 社交媒体管理、analytics 分析 与报告平台，开箱即支持九个社交网络。`GPL-3.0` `GPL-3.0` `Nodejs`
- [Superset](http://superset.apache.org/) - 现代数据探索与可视化平台。([Source Code](https://github.com/apache/superset)) `Apache-2.0` `Python`
- [Swetrix](https://swetrix.com/) - Web analytics 分析，可追踪站点流量、监控站点速度、分析用户会话与页面流向、查看用户路径等（Google Analytics 的替代方案）。([Demo](https://swetrix.com/projects/STEzHcB1rALV), [Source Code](https://github.com/Swetrix/selfhosting)) `AGPL-3.0` `Docker`
- [Umami](https://umami.is/) - 简洁、快速、注重隐私（Google Analytics 的替代方案）。([Demo](https://cloud.umami.is/share/LGazGOecbDtaIwDr), [Source Code](https://github.com/umami-software/umami)) `MIT` `Nodejs/Docker`


<a id="archiving-and-digital-preservation-dp"></a>
### Archiving and Digital Preservation (DP) 存档与数字化保存（DP）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Digital [archiving 存档](https://en.wikipedia.org/wiki/Archival_science) 与 [preservation 保存](https://en.wikipedia.org/wiki/Digital_preservation) 软件。

_Related: [Backup 备份](#backup), [Content Management Systems (CMS) 内容管理系统（CMS）](#content-management-systems-cms)_

_See also: [awesome-web-archiving](https://github.com/iipc/awesome-web-archiving)_

- [ArchiveBox](https://archivebox.io/) - 从书签、浏览历史、RSS 订阅源或其他来源为站点创建 HTML 与截图存档（Wayback Machine 的替代方案）。([Source Code](https://github.com/ArchiveBox/ArchiveBox)) `MIT` `Python/Docker`
- [ArchivesSpace](https://archivesspace.org/) - 档案信息管理应用，用于管理档案、手稿与数字对象并提供 Web 访问。([Demo](https://archivesspace.org/application/sandbox), [Source Code](https://github.com/archivesspace/archivesspace)) `ECL-2.0` `Ruby`
- [Bichon](https://github.com/rustmailer/bichon) - 电子邮件存档服务器，从 IMAP 账号同步，为邮件建立全文检索索引，并提供 REST API。无需外部数据库，内置支持多账号的 WebUI。`AGPL-3.0` `AGPL-3.0` `Rust/Docker`
- [bitmagnet](https://bitmagnet.io) - BitTorrent 索引器、DHT 爬虫、内容分类器与 torrent 种子 搜索引擎，带 Web UI、GraphQL API 与 Servarr 套件集成。([Source Code](https://github.com/bitmagnet-io/bitmagnet)) `MIT` `Go/Docker`
- [CKAN](https://ckan.org) - 用于构建开放数据网站。([Source Code](https://github.com/ckan/ckan)) `AGPL-3.0` `Python`
- [Collective Access - Providence](https://collectiveaccess.org/) - 可高度配置的 Web 框架，用于对数字与实体藏品进行管理、描述与发现，支持多种 metadata standards 元数据标准、data types 数据类型 与 media formats 媒体格式。([Source Code](https://github.com/collectiveaccess/providence)) `GPL-3.0` `PHP`
- [Eonvelope](https://dacid99.gitlab.io/eonvelope) - 电子邮件存档软件，可长期、无限期地保存你的邮件。([Source Code](https://gitlab.com/dacid99/eonvelope)) `AGPL-3.0` `K8S/Docker`
- [Ganymede](https://github.com/Zibbp/ganymede) `⚠` - Twitch VOD 与直播存档平台。每个存档都包含渲染后的聊天记录。`GPL-3.0` `GPL-3.0` `Docker`
- [mail-archiver](https://github.com/s1t5/mail-archiver) - 用于存档、搜索并导出多个账号（IMAP、M365 或导入）邮件的 Web 应用。具备文件夹同步、附件支持、邮箱迁移与仪表盘。`GPL-3.0` `GPL-3.0` `Docker`
- [Omeka S](https://omeka.org/s/) - 面向机构的下一代 Web 发布平台，用于将数字文化遗产藏品与其他在线资源关联。([Source Code](https://github.com/omeka/omeka-s)) `GPL-3.0` `Nodejs`
- [Open Archiver](https://openarchiver.com/) - 带全文检索与 eDiscovery 电子取证 搜索功能的电子邮件存档方案。([Demo](https://github.com/LogicLabs-OU/OpenArchiver?tab=readme-ov-file#-live-demo), [Source Code](https://github.com/LogicLabs-OU/OpenArchiver)) `AGPL-3.0` `Docker`
- [Piler](https://www.mailpiler.org/) - 功能丰富的电子邮件存档方案。([Source Code](https://github.com/jsuto/piler/)) `GPL-3.0` `C/Docker/deb`
- [Wallabag](https://www.wallabag.org) - Web 应用（前身为 Poche），可保存文章以便稍后阅读，并提升可读性。([Source Code](https://github.com/wallabag/wallabag)) `MIT` `PHP`
- [Wayback](https://github.com/wabarc/wayback) - 将网页存档至 Internet Archive、archive.today、IPFS 与本地文件系统的工具集。`GPL-3.0` `GPL-3.0` `Go`


<a id="automation"></a>
### Automation 自动化

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Automation 自动化](https://en.wikipedia.org/wiki/Automation) 软件，用于减少流程中的人工干预。

_Related: [Internet of Things (IoT) 物联网（IoT）](#internet-of-things-iot), [Software Development - Continuous Integration & Deployment 软件开发 - 持续集成与部署](#software-development---continuous-integration--deployment), [Media Management 媒体管理](#media-management)_

- [Activepieces](https://www.activepieces.com) - 无代码 business automation 业务自动化 工具，类似 Zapier 或 Tray。例如，每张新 Trello 卡片都可触发 Slack 通知。([Source Code](https://github.com/activepieces/activepieces)) `MIT` `Docker`
- [Apache Airflow](https://airflow.apache.org/) - 用于以编程方式编写、排程和监控 workflows 工作流 的平台。([Source Code](https://github.com/apache/airflow/)) `Apache-2.0` `Python/Docker`
- [Automatisch](https://automatisch.io) - 业务自动化 工具，可连接 Twitter、Slack 等不同服务以自动化业务流程（Zapier 的替代方案）。([Source Code](https://github.com/automatisch/automatisch)) `AGPL-3.0` `Docker`
- [BookBounty](https://github.com/TheWicklowWolf/BookBounty) `⚠` - 从 Library Genesis 获取缺失的 Readarr 图书。`MPL-2.0` `MPL-2.0` `Docker`
- [changedetection.io](https://changedetection.io/) - 跟踪网站内容变更，保持更新。([Source Code](https://github.com/dgtlmoon/changedetection.io)) `Apache-2.0` `Python/Docker`
- [ChiefOnboarding](https://chiefonboarding.com) - 员工入职平台，可开通用户账号并创建包含待办项、资源、文本/邮件/Slack 消息等的序列。提供 Web 门户与 Slack 机器人两种形式。([Source Code](https://github.com/chiefonboarding/ChiefOnboarding)) `AGPL-3.0` `Docker`
- [Cronicle](https://cronicle.net/) - 简洁的分布式任务排程器与执行器，带 Web UI。([Source Code](https://github.com/jhuckaby/Cronicle)) `MIT` `Nodejs`
- [Cronmaster](https://github.com/fccview/cronmaster) - 带可读语法的 cron 任务管理 UI，提供实时日志与日志历史。`AGPL-3.0` `AGPL-3.0` `Docker`
- [Dagu](https://docs.dagu.cloud/) - 功能强大的 Cron 替代方案，带 Web UI。可用声明式 YAML 将命令间的依赖定义为有向无环图（DAG）。([Source Code](https://github.com/dagucloud/dagu)) `GPL-3.0` `Go/Docker`
- [Discount Bandit](https://discount-bandit.cybrarist.com/) `⚠` - 追踪 Amazon、Ebay、Walmart 等多家商店的商品价格与库存状态。([Source Code](https://github.com/Cybrarist/Discount-Bandit)) `GPL-3.0` `PHP/Docker`
- [Dittofeed](https://www.dittofeed.com) - 全渠道客户互动与消息 automation 自动化 平台（Braze、Customer.io、Iterable 的替代方案）。([Demo](https://demo.dittofeed.com/dashboard/journeys), [Source Code](https://github.com/dittofeed/dittofeed)) `MIT` `Docker`
- [flowctl](https://flowctl.net) - 自助式 workflow 工作流 执行平台，带审批、远程执行与排程。([Demo](https://demo.flowctl.net), [Source Code](https://github.com/cvhariharan/flowctl)) `Apache-2.0` `Go/Docker`
- [Fredy](https://fredy.orange-coding.net/) `⚠` - 在德国 ImmoScout24、Immowelt 等平台上搜索新公寓、住宅与套房，并通过 Slack、Telegram 等即时向你推送结果。([Demo](https://fredy-demo.orange-coding.net), [Source Code](https://github.com/orangecoding/fredy)) `Apache-2.0` `Nodejs/Docker`
- [gocron](https://github.com/flohoss/gocron) - 任务排程器，用户可通过简单 YAML 配置文件指定周期性任务。`MIT` `MIT` `Docker`
- [HandBrake Web](https://github.com/TheNickOfTime/handbrake-web) - 通过 Web 界面在无头设备上使用一个或多个 HandBrake 视频转码实例。`AGPL-3.0` `AGPL-3.0` `Docker`
- [Healthchecks](https://healthchecks.io/) - 监听 ping，并在 ping 延迟时发送告警。([Source Code](https://github.com/healthchecks/healthchecks)) `BSD-3-Clause` `Python/Docker`
- [Huginn](https://github.com/huginn/huginn) - 构建可监控并代你执行操作的 agents 代理。`MIT` `MIT` `Ruby`
- [Kestra](https://kestra.io) - 事件驱动、语言无关的平台，用于创建、排程和监控 workflows 工作流，以代码方式协调 ETL 与 ELT 等数据管道与任务。([Source Code](https://github.com/kestra-io/kestra)) `Apache-2.0` `Docker`
- [Kibitzr](https://kibitzr.github.io) - 轻量级个人 Web 助手，具备强大的集成能力。([Source Code](https://github.com/kibitzr/kibitzr)) `MIT` `Python`
- [LazyLibrarian](https://gitlab.com/LazyLibrarian/LazyLibrarian) `⚠` - 关注作者并获取满足你数字阅读需求的 metadata 元数据。结合 Goodreads、Librarything，以及可选的 GoogleBooks，作为作者与图书信息的来源。`GPL-3.0` `GPL-3.0` `Python`
- [Leon](https://getleon.ai) - 可运行于你服务器上的个人 assistant 助手。`MIT` `MIT` `Nodejs`
- [Matchering](https://github.com/sergree/matchering) - 自动化音乐母带处理（LANDR、eMastered、MajorDecibel 的替代方案）。`GPL-3.0` `GPL-3.0` `Docker`
- [Mylar3](https://mylar.nerdfirehurricane.com/) - 用于 NZB 与 torrent 种子 的自动化漫画（cbr/cbz）下载程序。([Source Code](https://github.com/MylarComics/mylar3)) `GPL-3.0` `Python/Docker`
- [OliveTin](https://www.olivetin.app/) - 用于执行 Linux shell 命令的 Web 界面。([Source Code](https://github.com/OliveTin/OliveTin)) `AGPL-3.0` `Go`
- [pyLoad](https://pyload.net/) - 轻量、可定制且可远程管理的下载器，面向 rapidshare.com、uploaded.to 等一键托管站点。([Source Code](https://github.com/pyload/pyload)) `AGPL-3.0` `Python`
- [StackStorm](https://stackstorm.com) - StackStorm（即运维版 IFTTT）是事件驱动的 automation 自动化 工具，用于自动修复、安全响应、故障排查、部署等。包含规则引擎、工作流、160 个集成包（6000+ 动作）与 ChatOps。([Source Code](https://github.com/StackStorm/st2)) `Apache-2.0` `Python`
- [µTask](https://github.com/ovh/utask) - 以 yaml 声明业务模型并执行其流程的 automation 自动化 引擎。`BSD-3-Clause` `BSD-3-Clause` `Go/Docker`


<a id="backup"></a>
### Backup 备份

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Backup 备份](https://en.wikipedia.org/wiki/Backup) 软件。

**请访问 [awesome-sysadmin/Backups](https://github.com/awesome-foss/awesome-sysadmin#backups)**

_Related: [Archiving and Digital Preservation (DP) 存档与数字化保存（DP）](#archiving-and-digital-preservation-dp)_



<a id="blogging-platforms"></a>
### Blogging Platforms 博客平台

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [blog](https://en.wikipedia.org/wiki/Blog) is a discussion or informational website consisting of discrete, diary-style text entries (posts).

_Related: [Static Site Generators 静态站点生成器](#static-site-generators), [Content Management Systems (CMS) 内容管理系统（CMS）](#content-management-systems-cms)_

_See also: [WeblogMatrix](https://www.weblogmatrix.org/)_

- [Antville](https://antville.org) - 功能丰富的博客托管软件，可托管上万个博客。([Source Code](https://github.com/antville/antville)) `Apache-2.0` `Javascript`
- [bloglite](https://github.com/rikhuijzer/bloglite) - 微型博客工具，提供内置语法高亮、移动端发布等功能（Twitter、Bluesky 的替代方案）。`MIT` `MIT` `Docker`
- [Chyrp Lite](https://chyrplite.net) - 格外出色、格外轻量的博客引擎。([Source Code](https://github.com/xenocrat/chyrp-lite)) `BSD-3-Clause` `PHP`
- [Dotclear](https://git.dotclear.org/dev/dotclear) - 让你完全掌控自己的博客。`GPL-2.0` `GPL-2.0` `PHP`
- [Ech0](https://ech0.app/) - 轻量级联邦化发布平台，专注于个人观点分享（文档为中文）。([Demo](https://memo.vaaat.com/), [Source Code](https://github.com/lin-snow/Ech0)) `AGPL-3.0` `Docker/K8S`
- [FlatPress](https://flatpress.org/) - 轻量、易部署的纯文本文件博客引擎。([Source Code](https://github.com/flatpressblog/flatpress)) `GPL-2.0` `PHP`
- [Ghost](https://ghost.org/) - 纯粹的博客平台。([Source Code](https://github.com/TryGhost/Ghost)) `MIT` `Nodejs`
- [Haven](https://havenweb.org/) - 支持 markdown 编辑与内置 RSS 阅读器的私有博客系统。([Demo](https://havenweb.org/demo.html), [Source Code](https://github.com/havenweb/haven)) `MIT` `Ruby`
- [HTMLy](https://www.htmly.com/) - 无数据库的 PHP 博客平台。一种纯文本文件 CMS，可让你在数秒内创建快速、安全且强大的网站或博客。([Demo](http://demo.htmly.com/), [Source Code](https://github.com/danpros/htmly)) `GPL-2.0` `PHP`
- [Known](https://withknown.com/) - 协作式社交发布平台。([Source Code](https://github.com/idno/idno)) `Apache-2.0` `PHP`
- [Mataroa](https://mataroa.blog/) - 面向极简主义者的朴素博客平台。([Source Code](https://github.com/mataroablog/mataroa)) `MIT` `Python`
- [PluXml](https://pluxml.org) - 基于 XML 的博客/CMS 平台。([Source Code](https://github.com/pluxml/PluXml)) `GPL-3.0` `PHP`
- [Serendipity](https://docs.s9y.org/) - 高度可扩展、可定制的 PHP 博客引擎，使用 Smarty 模板（s9y）。([Source Code](https://github.com/s9y/serendipity)) `BSD-3-Clause` `PHP`
- [WriteFreely](https://writefreely.org) - 用于启动极简、联邦化博客——或整个社区的写作软件。([Source Code](https://github.com/writefreely/writefreely)) `AGPL-3.0` `Go`


<a id="booking-and-scheduling"></a>
### Booking and Scheduling 预订与排程

**[`^        返回顶部        ^`](#awesome-selfhosted)**

活动排程、预订与预约管理软件。

_Related: [Polls and Events 投票与活动](#polls-and-events), [Groupware 群件](#groupware)_

- [Alf.io](https://alf.io/) - 票务预订系统。([Demo](https://demo.alf.io/authentication), [Source Code](https://github.com/alfio-event/alf.io)) `GPL-3.0` `Java`
- [Cal.diy](https://cal.diy/) - 在线预约排程系统。([Source Code](https://github.com/calcom/cal.diy)) `MIT` `Nodejs`
- [Chobble Tickets](https://tickets.chobble.com) - 活动票务，支持二维码签到与加密的参与者记录。完整产品采用 AGPL-3.0，无开放核心、无品牌要求，并作为边缘脚本运行，无需常驻服务器（Eventbrite 的替代方案）。([Demo](https://tickets.crumpsallfolkclub.co.uk), [Source Code](https://github.com/chobbledotcom/tickets)) `AGPL-3.0` `Deno/Docker`
- [Easy!Appointments](https://easyappointments.org/) - 让你的客户通过 Web 与你预约。([Demo](https://demo.easyappointments.org/), [Source Code](https://github.com/alextselegidis/easyappointments)) `GPL-3.0` `PHP`
- [Hi.Events](https://hi.events) - 面向会议、演唱会等活动的管理与票务平台。提供可定制的活动页面与可嵌入的票务组件。([Demo](https://demo.hi.events/event/1/dog-conf-2030), [Source Code](https://github.com/HiEventsDev/hi.events)) `AGPL-3.0` `Docker`
- [LibreBooking](https://librebooking.readthedocs.io/) - 资源排程方案，为组织提供灵活、移动友好且可扩展的界面来管理资源预订。([Demo](https://librebooking-demo.fly.dev/), [Source Code](https://github.com/LibreBooking/librebooking)) `GPL-3.0` `PHP/Docker`
- [QloApps](https://qloapps.com/) - 可定制、直观的基于 Web 的酒店预订系统与预订引擎。([Demo](https://demo.qloapps.com/), [Source Code](https://github.com/Qloapps/QloApps)) `OSL-3.0` `PHP/Nodejs`
- [Rallly](https://rallly.co) - 创建投票以对日期与时间进行表决（Doodle 的替代方案）。([Demo](https://app.rallly.co), [Source Code](https://github.com/lukevella/rallly)) `AGPL-3.0` `Nodejs/Docker`
- [Seatsurfing](https://seatsurfing.app/) - 用于为办公室预订座位、工位与房间的 Web 应用。([Source Code](https://github.com/seatsurfing/seatsurfing)) `GPL-3.0` `Docker`


<a id="bookmarks-and-link-sharing"></a>
### Bookmarks and Link Sharing 书签与链接分享

**[`^        返回顶部        ^`](#awesome-selfhosted)**

用于添加、标注、编辑并分享 Web 文档 [bookmarks 书签](https://en.wikipedia.org/wiki/Bookmark_(digital)) 的软件。

_Related: [Personal Dashboards 个人仪表盘](#personal-dashboards)_

- [Betula](https://joinbetula.org) - 单用户联邦化书签管理器，支持 Fediverse 与存档。([Source Code](https://codeberg.org/bouncepaw/betula)) `AGPL-3.0` `Go`
- [Buku](https://github.com/jarun/Buku) - 强大的书签管理器，也是个人的文本迷你网络。`GPL-3.0` `GPL-3.0` `Python/deb`
- [Digibunch](https://ladigitale.dev/digibunch/#/) - 创建一批链接，与你的学员或同事分享。([Demo](https://ladigitale.dev/digibunch/#/b/5f67b12092b60), [Source Code](https://codeberg.org/ladigitale/digibunch)) `AGPL-3.0` `Nodejs/PHP`
- [Espial](https://github.com/jonschoning/espial) - 支持多用户账号的基于 Web 的书签服务器。`AGPL-3.0` `AGPL-3.0` `Haskell`
- [Faved](https://faved.to/) - 手工打造的书签管理器，结合强大的标签、即时搜索与干净、免干扰的界面。为大型收藏与高级工作流而构建，并针对效率与易用性优化。([Demo](https://demo.faved.to/), [Source Code](https://github.com/denho/faved)) `MIT` `Docker`
- [Firefox Account Server](https://mozilla-services.readthedocs.io/en/latest/howtos/run-fxa.html) - 托管你自己的 Firefox 账号服务器。([Source Code](https://github.com/mozilla/fxa)) `MPL-2.0` `Nodejs/Java`
- [Karakeep](https://karakeep.app/) - 书签一切的应用，为数据囤积者加入了一点 AI。([Demo](https://try.karakeep.app/signin), [Source Code](https://github.com/karakeep-app/karakeep)) `AGPL-3.0` `Docker`
- [LinkAce](https://www.linkace.org/) - 书签存档，自动备份至 Internet Archive，提供链接监控与完整 REST API。可通过 Docker 安装，或作为简单 PHP 应用运行。([Demo](https://demo.linkace.org/guest/links), [Source Code](https://github.com/Kovah/LinkAce/)) `GPL-3.0` `Docker/PHP`
- [linkding](https://linkding.link/) - 极简书签管理，界面快速干净。通过 Docker 安装简单，可运行于你的 Raspberry Pi。([Demo](https://demo.linkding.link/login/), [Source Code](https://github.com/sissbruecker/linkding)) `MIT` `Docker`
- [LinkWarden](https://linkwarden.app/) - 用于保存有用链接的书签与存档管理器。([Source Code](https://github.com/linkwarden/linkwarden)) `MIT` `Docker/Nodejs`
- [NeonLink](https://github.com/AlexSciFier/neonlink) - 设计独特、通过 Docker 简易安装的书签服务。`MIT` `MIT` `Docker`
- [Readeck](https://readeck.org/en/) - 保存你喜爱并想永久保留的网页中珍贵的只读内容。可视为书签管理器与稍后读工具。([Source Code](https://codeberg.org/readeck/readeck), [Clients](https://codeberg.org/readeck/browser-extension)) `AGPL-3.0` `Go/Docker`
- [Servas](https://github.com/beromir/Servas) - 书签管理工具。可通过标签、分组与专门的稍后访问列表进行整理。支持多用户与 2FA。提供 Firefox 与 Chrome 的配套浏览器扩展。([Clients](https://github.com/beromir/Servas#browser-extensions)) `GPL-3.0` `Docker/Nodejs/PHP`
- [Shaarli](https://github.com/shaarli/Shaarli) - 个人、极简、超快、无数据库的书签与链接分享平台。([Demo](https://demo.shaarli.org)) `Zlib` `PHP/deb`
- [Shiori](https://github.com/go-shiori/shiori) - 用 Go 构建的简易书签管理器。`MIT` `MIT` `Go/Docker`
- [Slash](https://github.com/yourselfhosted/slash) - 书签与链接分享平台。`GPL-3.0` `GPL-3.0` `Docker`
- [SyncMarks](https://codeberg.org/Offerel/SyncMarks-Webapp) - 从 Edge、Firefox 与 Chromium 同步并管理你的浏览器书签。([Clients](https://codeberg.org/Offerel/SyncMarks-Extension)) `AGPL-3.0` `PHP`


<a id="calendar--contacts"></a>
### Calendar & Contacts 日历与联系人

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[CalDAV](https://en.wikipedia.org/wiki/CalDAV) 与 [CardDAV](https://en.wikipedia.org/wiki/CardDAV) 协议服务器，以及用于 [Electronic calendar 电子日历](https://en.wikipedia.org/wiki/Calendaring_software)、[address book 通讯录](https://en.wikipedia.org/wiki/Address_book) 与 [contact management 联系人管理](https://en.wikipedia.org/wiki/Contact_manager) 的 Web 客户端/界面。

_Related: [Groupware 群件](#groupware)_

- [Baïkal](https://sabre.io/baikal/) - 基于 sabre/dav 的轻量级 CalDAV 与 CardDAV 服务器。([Source Code](https://github.com/sabre-io/Baikal)) `GPL-3.0` `PHP`
- [DAViCal](https://www.davical.org/) - 日历共享（CalDAV）服务器，使用 PostgreSQL 数据库作为数据存储。([Source Code](https://gitlab.com/davical-project/davical)) `GPL-2.0` `PHP/deb`
- [Davis](https://github.com/tchapi/davis) - 基于 Symfony 5 与 Bootstrap 4 的 sabre/dav 简易、可容器化且完全可翻译的管理界面，深受 Baïkal 启发。`MIT` `MIT` `PHP`
- [Keeper.sh](https://keeper.sh/) - 日历同步工具，通过 iCal/ICS 或 OAuth 在日历源与目标之间拉取与推送事件，支持匿名化的忙/闲事件。([Source Code](https://github.com/ridafkih/keeper.sh)) `AGPL-3.0` `Docker`
- [Manage My Damn Life](https://intri.in/manage-my-damn-life/) - Manage my Damn Life（MMDL）是用于管理你 CalDAV 任务与日历的前端。([Source Code](https://github.com/intri-in/manage-my-damn-life-nextjs)) `GPL-3.0` `Nodejs/Docker`
- [Radicale](https://radicale.org/) - 管理开销极低的简易日历与联系人服务器。([Source Code](https://github.com/Kozea/Radicale)) `GPL-3.0` `Python/deb`
- [SabreDAV](https://sabre.io/) - CardDAV、CalDAV 与 WebDAV 框架及服务器。([Source Code](https://github.com/sabre-io/dav)) `MIT` `PHP`
- [Xandikos](https://github.com/jelmer/xandikos) - 管理开销极低的 CardDAV 与 CalDAV 服务器，由 Git 仓库支撑。`GPL-3.0` `GPL-3.0` `Python/deb`


<a id="communication---custom-communication-systems"></a>
### Communication - Custom Communication Systems 通信 - 自定义通信系统

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Communication software 通信软件](https://en.wikipedia.org/wiki/Communication_software) 用于提供对系统的远程访问，并在不同计算机或用户之间以文本、音频和/或视频格式交换文件与消息，使用其自定义协议。

- [AnyCable](https://anycable.io/) - 用于通过 WebSockets、Server-sent events 等进行可靠双向通信的实时服务器。([Demo](https://demo.anycable.io), [Source Code](https://github.com/anycable/anycable)) `MIT` `Go/Docker`
- [Apprise](https://github.com/caronc/apprise) - Apprise 可向你如今几乎所有主流通知服务发送通知，例如 Telegram、Discord、Slack、Amazon SNS、Gotify 等。`MIT` `MIT` `Python/Docker/deb`
- [Centrifugo](https://centrifugal.dev/) - 语言无关、实时 messaging 消息 传递（Websocket 或 SockJS）服务器。([Demo](https://github.com/centrifugal/centrifugo#demo), [Source Code](https://github.com/centrifugal/centrifugo)) `MIT` `Go/Docker/K8S`
- [Chitchatter](https://chitchatter.im/) - 点对点聊天应用，无服务器、去中心化且临时。([Source Code](https://github.com/jeremyckahn/chitchatter)) `GPL-2.0` `Nodejs`
- [Conduit](https://conduit.rs/) - 由 Matrix 驱动、简单、快速且可靠的聊天服务器。([Source Code](https://gitlab.com/famedly/conduit)) `Apache-2.0` `Rust`
- [Continuwuity](https://continuwuity.org/) - 社区驱动的 Matrix homeserver，是 conduwuit 的延续，聚焦用户体验与新功能（Conduit 的 fork）。([Source Code](https://forgejo.ellis.link/continuwuation/continuwuity)) `Apache-2.0` `Rust/Docker/K8S/deb`
- [Databag](https://github.com/balzack/databag) - 联邦化、端到端加密的消息服务，面向 Web、iOS 与 Android，支持文本、照片、视频及 WebRTC 音视频通话。`Apache-2.0` `Apache-2.0` `Docker`
- [Element](https://element.io) - 功能完备的 Matrix 客户端，面向 Web、iOS 与 Android。([Source Code](https://github.com/element-hq/element-web)) `Apache-2.0` `Nodejs`
- [Fluxer](https://fluxer.app) - 为朋友、群组与社区打造的即时消息与 VoIP 平台（Discord 的替代方案）。([Demo](https://fluxer.app), [Source Code](https://github.com/fluxerapp/fluxer), [Clients](https://github.com/awesome-fluxer/awesome-fluxer)) `AGPL-3.0` `Docker`
- [GlobaLeaks](https://www.globaleaks.org/) - 举报人软件，让任何人都可轻松搭建并维护安全的举报平台。([Demo](https://demo.globaleaks.org), [Source Code](https://github.com/globaleaks/globaleaks-whistleblowing-software)) `AGPL-3.0` `Python/deb/Docker`
- [GNUnet](https://gnunet.org/) - 去中心化、点对点网络的软件框架。([Source Code](https://gnunet.org/git/)) `GPL-3.0` `C`
- [Gotify](https://gotify.net/) - 通知服务器，带 Android 与 CLI 客户端（PushBullet 的替代方案）。([Source Code](https://github.com/gotify/server), [Clients](https://github.com/gotify/android)) `MIT` `Go/Docker`
- [Hyphanet](https://hyphanet.org/) - 匿名分享文件、浏览并发布 freesites（仅可通过 Hyphanet 访问的网站），并在论坛中聊天。([Source Code](https://github.com/hyphanet/fred)) `GPL-2.0` `Java`
- [Jami](https://jami.net/) - 保护用户隐私与自由的通用通信平台。([Source Code](https://git.jami.net/savoirfairelinux?sort=latest_activity_desc&filter=jami)) `GPL-3.0` `C++`
- [Live Helper Chat](https://livehelperchat.com/) - 面向你网站的实时客服聊天。([Source Code](https://github.com/LiveHelperChat/livehelperchat)) `Apache-2.0` `PHP`
- [Mumble](https://wiki.mumble.info/wiki/Main_Page) - 低延迟、高质量的语音/文本聊天软件。([Source Code](https://github.com/mumble-voip/mumble), [Clients](https://wiki.mumble.info/wiki/3rd_Party_Applications)) `BSD-3-Clause` `C++/deb`
- [Notifo](https://github.com/notifo-io/notifo) - 多通道通知服务器，支持 Email、移动推送、Web 推送、SMS、消息与 JavaScript 插件。`MIT` `MIT` `C#`
- [Novu](https://novu.co/) - 面向开发者的通知基础设施。([Source Code](https://github.com/novuhq/novu/)) `MIT` `Docker/Nodejs`
- [ntfy](https://ntfy.sh/) - 通过 HTTP PUT/POST 向手机或桌面推送通知，提供 Android 应用、CLI 与 Web 应用，类似 Pushover 与 Gotify。([Demo](https://ntfy.sh/app), [Source Code](https://github.com/binwiederhier/ntfy), [Clients](https://github.com/binwiederhier/ntfy-android)) `Apache-2.0/GPL-2.0` `Go/Docker/K8S`
- [One Time Secret](https://docs.onetimesecret.com) - 通过仅可查看一次的自毁链接安全分享敏感信息。([Demo](https://onetimesecret.com), [Source Code](https://github.com/onetimesecret/onetimesecret)) `MIT` `Docker/Ruby/Nodejs`
- [OpenWA](https://www.open-wa.org) `⚠` - WhatsApp API 网关，将消息以 REST 端点暴露，提供 Web 仪表盘、多账号会话与 webhook 事件（WhatsApp Business API 提供商的替代方案）。([Source Code](https://github.com/rmyndharis/OpenWA), [Clients](https://github.com/rmyndharis/OpenWA-plugins)) `MIT` `Docker`
- [OTS](https://ots.fyi/) - 一次性秘密分享平台，在浏览器中使用对称 256 位 AES 加密。([Source Code](https://github.com/Luzifer/ots)) `Apache-2.0` `Go`
- [PushBits](https://github.com/pushbits/server) - 通过 Matrix 转发推送通知的通知服务器，类似 PushBullet 与 Gotify。`ISC` `ISC` `Go`
- [RetroShare](https://retroshare.cc) - 安全、去中心化的通信系统。提供去中心化聊天、论坛、消息与文件传输。([Source Code](https://github.com/RetroShare/RetroShare)) `GPL-2.0` `C++`
- [Rocket.Chat](https://rocket.chat/) - 将数据保护放在首位的通信平台（Gitter.im 与 Slack 的替代方案）。([Source Code](https://github.com/RocketChat/Rocket.Chat)) `MIT` `Nodejs/Docker/K8S`
- [SAMA](https://samacloud.io) - 下一代自托管聊天服务器与客户端。([Demo](https://app.samacloud.io/demo), [Source Code](https://github.com/SAMA-Communications/sama-server), [Clients](https://github.com/SAMA-Communications/sama-client)) `GPL-3.0` `Nodejs/Docker`
- [Screego](https://screego.net) - 通过 Web 浏览器快速向一人或多人分享屏幕的简单工具。([Demo](https://app.screego.net/), [Source Code](https://github.com/screego/server)) `GPL-3.0` `Docker/Go`
- [Shhh](https://github.com/smallwat3r/shhh) - 让秘密远离邮件或聊天记录，通过带口令与过期时间的 secure 安全 链接分享。`MIT` `MIT` `Python`
- [SimpleX Chat](https://github.com/simplex-chat/simplex-chat) - 最注重隐私与安全的聊天及应用平台——现已采用双棘轮端到端加密。`AGPL-3.0` `AGPL-3.0` `Haskell`
- [Spectrum 2](https://spectrum.im/) - 即时消息传输器。即使用户使用不同 IM 网络，也能一起聊天。([Source Code](https://github.com/SpectrumIM/spectrum2)) `GPL-3.0` `C++`
- [Stoat](https://stoat.chat/) - 以用户为先、使用现代 Web 技术构建的聊天平台。([Source Code](https://github.com/stoatchat/self-hosted)) `AGPL-3.0/MIT` `Rust`
- [Synapse](https://element-hq.github.io/synapse/latest/index.html) - Matrix 的服务器，Matrix 是去中心化持久通信的开放标准。([Source Code](https://github.com/element-hq/synapse)) `Apache-2.0` `Python/deb`
- [Tiledesk](https://tiledesk.com) - 从获客到售后、从 WhatsApp 到你网站的一体化客户互动平台。提供全渠道人工坐席与 AI 驱动的聊天机器人（Intercom、Zendesk、Tawk.to 的替代方案）。([Source Code](https://github.com/Tiledesk/tiledesk)) `MIT` `Docker/K8S`
- [Tinode](https://github.com/tinode) - 即时消息平台。后端用 Go。客户端：Swift iOS、Java Android、JS webapp、可脚本化命令行；以及聊天机器人。([Demo](https://sandbox.tinode.co/), [Source Code](https://github.com/tinode/chat), [Clients](https://github.com/tinode/webapp)) `GPL-3.0` `Go`
- [Tox](https://tox.chat/) - 分布式、安全的 messenger 即时通讯 工具，具备音视频聊天能力。([Source Code](https://github.com/TokTok/c-toxcore)) `GPL-3.0` `C`
- [Tuwunel](https://tuwunel.chat) - 面向 Matrix 的高性能、功能丰富的聊天服务器，是 conduwuit 的继任者（Conduit 的 fork）。([Demo](https://try.tuwunel.chat/), [Source Code](https://github.com/matrix-construct/tuwunel)) `Apache-2.0` `deb/Docker/Nix/Rust`
- [Typebot](https://typebot.io) - 对话式应用构建器（Typeform 与 Landbot 的替代方案）。([Source Code](https://github.com/baptisteArno/typebot.io)) `AGPL-3.0` `Docker`
- [WBO](https://github.com/lovasoa/whitebophir) - 用于实时协作示意图、绘图与笔记的 Web 白板。([Demo](https://wbo.ophir.dev/)) `AGPL-3.0` `Nodejs/Docker`
- [Zulip](https://zulip.org) - 强大的群组聊天应用。([Source Code](https://github.com/zulip/zulip)) `Apache-2.0` `Python`


<a id="communication---email---complete-solutions"></a>
### Communication - Email - Complete Solutions 通信 - 电子邮件 - 完整方案

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[E-mail 电子邮件](https://en.wikipedia.org/wiki/Email) 服务器的简易部署，例如面向经验不足或没耐心的管理员。

- [AnonAddy](https://anonaddy.com) - 用于创建别名（alias）的邮件转发服务。([Source Code](https://github.com/anonaddy/anonaddy)) `MIT` `PHP/Docker`
- [b1gMail](https://www.b1gmail.eu) - 完整邮件方案，可运行于任何带 PHP 与 MariaDB 的虚拟主机。支持 POP3 catchall 邮箱，若你自建服务器还可与 Postfix 或 b1gMailServer 集成。([Source Code](https://codeberg.org/b1gMail/b1gMail), [Clients](https://www.b1gmail.eu/en/start/addon-b1gmailserver/)) `GPL-2.0` `PHP`
- [DebOps](https://docs.debops.org/) - 开箱即用的、基于 Debian 的数据中心。一组通用 Ansible 角色，用于管理 Debian 或 Ubuntu 主机。([Source Code](https://github.com/debops/debops)) `GPL-3.0` `Ansible/Python`
- [docker-mailserver](https://docker-mailserver.github.io/docker-mailserver/edge/) - 生产可用、全栈但简洁的邮件服务器（SMTP、IMAP、LDAP、反垃圾邮件、杀毒等），运行于容器内。仅配置文件，无 SQL 数据库。([Source Code](https://github.com/docker-mailserver/docker-mailserver)) `MIT` `Docker`
- [Inboxen](https://inboxen.org) - 让你拥有无限数量的独立收件箱。([Source Code](https://codeberg.org/Inboxen/Inboxen)) `GPL-3.0` `Python`
- [iRedMail](https://www.iredmail.org/) - 基于 Postfix 与 Dovecot 的功能完备邮件服务器方案。([Source Code](https://github.com/iredmail/iRedMail)) `GPL-3.0` `Shell`
- [Maddy Mail Server](https://maddy.email/) - 一体化邮件服务器，实现 SMTP（MTA 与 MX 兼具）与 IMAP。用单一守护进程取代 Postfix、Dovecot、OpenDKIM、OpenSPF、OpenDMARC。([Source Code](https://github.com/foxcpp/maddy)) `GPL-3.0` `Go`
- [Mail-in-a-Box](https://mailinabox.email/) - 用一条命令将任意 Ubuntu 服务器变为功能完整的邮件服务器。([Source Code](https://github.com/mail-in-a-box/mailinabox)) `CC0-1.0` `Shell`
- [Mailcow](https://mailcow.email/) - 基于 Dovecot、Postfix 等软件的邮件服务器套件，提供现代化的 Web 管理界面。([Source Code](https://github.com/mailcow/mailcow-dockerized)) `GPL-3.0` `Docker/PHP`
- [Mailu](https://mailu.io/) - 简洁却功能完备的邮件服务器，以一组 Docker 镜像形式提供。([Source Code](https://github.com/Mailu/Mailu)) `MIT` `Docker/Python`
- [Modoboa](https://modoboa.org/en/) - 邮件托管与管理平台，包含现代化、简化的 Web 用户界面。([Source Code](https://github.com/modoboa/modoboa)) `ISC` `Python`
- [Mox](https://www.xmox.nl/) - 完整电子邮件方案，支持 IMAP4、SMTP、SPF、DKIM、DMARC、MTA-STS、DANE 与 DNSSEC，基于信誉与内容的垃圾过滤，国际化（IDNA），通过 ACME 与 Let's Encrypt 的自动 TLS，账号自动配置，以及 Webmail。([Source Code](https://github.com/mjl-/mox)) `MIT` `Go`
- [Postal](https://docs.postalserver.io/) - 完整且功能齐全、供网站与 Web 服务器使用的邮件服务器。([Source Code](https://github.com/postalserver/postal)) `MIT` `Docker/Ruby`
- [Simple NixOS Mailserver](https://gitlab.com/simple-nixos-mailserver/nixos-mailserver) - 利用 Nix 生态的完整邮件服务器方案。`GPL-3.0` `GPL-3.0` `Nix`
- [SimpleLogin](https://simplelogin.io) - 保护你邮箱地址的邮件别名方案。提供浏览器扩展与移动应用。([Source Code](https://github.com/simple-login/app)) `MIT` `Docker/Python`
- [Stalwart Mail Server](https://stalw.art) - 一体化邮件服务器，支持 JMAP、IMAP4 与 SMTP，并具备广泛现代特性。([Source Code](https://github.com/stalwartlabs/stalwart)) `AGPL-3.0` `Rust/Docker`
- [wildduck](https://wildduck.email/) - 可扩展、无单点故障（no-SPOF）的 IMAP/POP3 邮件服务器。([Source Code](https://github.com/zone-eu/wildduck)) `EUPL-1.2` `Nodejs/Docker`


<a id="communication---email---mail-delivery-agents"></a>
### Communication - Email - Mail Delivery Agents 通信 - 电子邮件 - 邮件投递代理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Mail Delivery Agents 邮件投递代理](https://en.wikipedia.org/wiki/Message_delivery_agent)（MDA）——[IMAP](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol)/[POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) 服务器软件。

- [Cyrus IMAP](https://www.cyrusimap.org/) - 邮件（IMAP/POP3）、联系人与日历服务器。([Source Code](https://github.com/cyrusimap/cyrus-imapd)) `BSD-3-Clause-Attribution` `C`
- [DavMail](https://davmail.sourceforge.net/) `⚠` - POP/IMAP/SMTP/Caldav/Carddav/LDAP 交换网关，让用户可在任何邮件/日历客户端配合 Exchange 服务器使用，即使通过互联网或经防火墙后的 Outlook Web Access 亦可。([Source Code](https://github.com/mguessan/davmail)) `GPL-2.0` `Java`
- [Dovecot](https://www.dovecot.org/) - 以安全为首要考量的 IMAP 与 POP3 服务器。([Source Code](https://github.com/dovecot/core)) `MIT/LGPL-2.1` `C/deb`


<a id="communication---email---mail-transfer-agents"></a>
### Communication - Email - Mail Transfer Agents 通信 - 电子邮件 - 邮件传输代理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Mail Transfer Agents 邮件传输代理](https://en.wikipedia.org/wiki/Message_transfer_agent)（MTA）——[SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) 服务器。

- [chasquid](https://blitiri.com.ar/p/chasquid/) - 专注简洁、安全与易运维的 SMTP（邮件）服务器。([Source Code](https://blitiri.com.ar/git/r/chasquid/)) `Apache-2.0` `Go`
- [Courier MTA](https://www.courier-mta.org/) - 快速、可扩展的企业级邮件/群件服务器，提供 ESMTP、IMAP、POP3、Webmail、邮件列表、基础 Web 日历与排程服务。([Source Code](https://www.courier-mta.org/repo.html)) `GPL-3.0` `C/deb`
- [DragonFly](https://github.com/corecode/dma) - 用于家庭与办公室的小型 MTA。可运行于 Linux 与 FreeBSD。`BSD-3-Clause` `BSD-3-Clause` `C`
- [EmailRelay](https://emailrelay.sourceforge.net/) - 用于 Windows 与 Linux 的小型、易配置的 SMTP 与 POP3 服务器。([Source Code](https://sourceforge.net/p/emailrelay/code/HEAD/tree/)) `GPL-3.0` `C++`
- [Exim](https://www.exim.org/) - 由剑桥大学开发的邮件传输代理（MTA）。([Source Code](https://git.exim.org/exim.git)) `GPL-3.0` `C/deb`
- [Haraka](https://haraka.github.io/) - 快速、高度可扩展且事件驱动的 SMTP 服务器。([Source Code](https://github.com/haraka/Haraka)) `MIT` `Nodejs`
- [OpenSMTPD](https://opensmtpd.org/) - 来自 OpenBSD 项目的安全 SMTP 服务器实现。([Source Code](https://github.com/OpenSMTPD/OpenSMTPD/)) `ISC` `C/deb`
- [Postfix](http://www.postfix.org/) - 快速、易管理且安全的 Sendmail 替代品。`IPL-1.0` `IPL-1.0` `C/deb`
- [Sendmail](https://www.proofpoint.com/us/products/email-protection/open-source-email-solution) - 邮件传输代理（MTA）。`Sendmail` `Sendmail` `C/deb`


<a id="communication---email---mailing-lists-and-newsletters"></a>
### Communication - Email - Mailing Lists and Newsletters 通信 - 电子邮件 - 邮件列表与新闻稿

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Mailing list 邮件列表](https://en.wikipedia.org/wiki/Mailing_list) 服务器与群发邮件软件——一条消息发给众多收件人。

_Related: [Customer Relationship Management (CRM) 客户关系管理（CRM）](#customer-relationship-management-crm)_

- [HyperKitty](https://wiki.list.org/HyperKitty) - 访问 GNU Mailman v3 归档。([Demo](https://lists.mailman3.org/), [Source Code](https://gitlab.com/mailman/hyperkitty)) `GPL-3.0` `Python`
- [Keila](https://www.keila.io) - 可靠且易用的新闻稿工具（Mailchimp 与 Sendinblue 的替代方案）。([Demo](https://app.keila.io), [Source Code](https://github.com/pentacent/keila)) `AGPL-3.0` `Docker`
- [Listmonk](https://listmonk.app/) - 高性能新闻稿与邮件列表管理器，带现代化仪表盘。([Demo](https://demo.listmonk.app/), [Source Code](https://github.com/knadh/listmonk)) `AGPL-3.0` `Go/Docker`
- [Mailman](https://www.list.org/) - 管理电子邮件讨论与电子新闻稿列表。([Source Code](https://gitlab.com/mailman/)) `GPL-3.0` `Python`
- [Mautic](https://www.mautic.org/) - 营销自动化软件（邮件、社交等）。([Source Code](https://github.com/mautic/mautic)) `GPL-3.0` `PHP`
- [mlmmj](https://mlmmj.org/) - 让邮件列表管理变得愉悦。([Source Code](https://codeberg.org/mlmmj/mlmmj)) `MIT` `C`
- [phpList](https://www.phplist.org) - 新闻稿与邮件营销，提供订阅者、退信与插件的进阶管理。([Source Code](https://github.com/phpList/phplist3)) `AGPL-3.0` `PHP`
- [Postorius](https://docs.mailman3.org/projects/postorius/en/latest/) - 访问 GNU Mailman 的 Web 用户界面。([Source Code](https://gitlab.com/mailman/postorius/)) `GPL-3.0` `Python`
- [Schleuder](https://schleuder.nadir.org/) - 支持 GPG、具备重发能力的邮件列表管理器。([Source Code](https://0xacab.org/schleuder/schleuder/tree/master)) `GPL-3.0` `Ruby`
- [Sympa](https://www.sympa.community/) - 邮件列表管理器。([Source Code](https://github.com/sympa-community/sympa)) `GPL-2.0` `Perl`


<a id="communication---email---webmail-clients"></a>
### Communication - Email - Webmail Clients 通信 - 电子邮件 - Web 邮件客户端

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Webmail Web 邮件](https://en.wikipedia.org/wiki/Webmail) 客户端。

- [Cypht](https://cypht.org) - 面向你邮件账号的订阅源阅读器。([Source Code](https://github.com/cypht-org/cypht)) `LGPL-2.1` `PHP`
- [Roundcube](https://roundcube.net) - 基于浏览器的 IMAP 客户端，具备类应用的用户界面。([Source Code](https://github.com/roundcube/roundcubemail)) `GPL-3.0` `PHP/deb`
- [SnappyMail](https://github.com/the-djmaze/snappymail) - 简单、现代、轻量且快速的基于 Web 的邮件客户端（RainLoop 的 fork）。`AGPL-3.0` `AGPL-3.0` `PHP`
- [SquirrelMail](https://squirrelmail.org) - 又一个基于浏览器的 IMAP 客户端。([Source Code](https://sourceforge.net/p/squirrelmail/code/HEAD/tree/)) `GPL-2.0` `PHP`


<a id="communication---irc"></a>
### Communication - IRC 通信 - IRC

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) 通信软件。

- [Ergo](https://ergo.chat/) - 用 Go 编写的现代化 IRCv3 服务器，融合 ircd、服务框架与 bouncer 的特性。([Source Code](https://github.com/ergochat/ergo)) `MIT` `Go/Docker`
- [Glowing Bear](https://github.com/glowing-bear/glowing-bear) - WeeChat 的 Web 前端。([Demo](https://www.glowing-bear.org)) `GPL-3.0` `Nodejs`
- [InspIRCd](https://www.inspircd.org/) - 用 C++ 编写、面向 Linux、BSD、Windows 与 macOS 的模块化 IRC 服务器。([Source Code](https://github.com/inspircd/inspircd)) `GPL-2.0` `C++/Docker`
- [Kiwi IRC](https://kiwiirc.com/) - 响应式 Web IRC 客户端，支持主题。([Demo](https://kiwiirc.com/nextclient/), [Source Code](https://github.com/kiwiirc/kiwiirc)) `Apache-2.0` `Nodejs`
- [ngircd](https://ngircd.barton.de/) - 可移植、轻量的 Internet Relay Chat 服务器，面向小型或私有网络。([Source Code](https://github.com/ngircd/ngircd)) `GPL-2.0` `C/deb`
- [Quassel IRC](https://quassel-irc.org/) - 分布式 IRC 客户端，即一个或多个客户端可连接并脱离中心核心。([Source Code](https://github.com/quassel/quassel)) `GPL-2.0` `C++`
- [Robust IRC](https://robustirc.net/) - 无 netsplit 的 IRC。基于 RobustSession 协议的分布式 IRC 服务器。([Source Code](https://github.com/robustirc/robustirc)) `BSD-3-Clause` `Go`
- [The Lounge](https://thelounge.chat/) - Web IRC 客户端。([Demo](https://demo.thelounge.chat/), [Source Code](https://github.com/thelounge/thelounge)) `MIT` `Nodejs/Docker`
- [UnrealIRCd](https://www.unrealircd.org/) - 用 C 编写、面向 Linux、BSD、Windows 与 macOS 的模块化、先进且高度可配置的 IRC 服务器。([Source Code](https://github.com/unrealircd/unrealircd)) `GPL-2.0` `C`
- [Weechat](https://weechat.org/) - 快速、轻量且可扩展的聊天客户端。([Source Code](https://github.com/weechat/weechat)) `GPL-3.0` `C/Docker/deb`
- [ZNC](https://wiki.znc.in/ZNC) - 先进的 IRC bouncer。([Source Code](https://github.com/znc/znc)) `Apache-2.0` `C++/deb`


<a id="communication---sip"></a>
### Communication - SIP 通信 - SIP

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[SIP](https://en.wikipedia.org/wiki/Session_Initiation_Protocol)/[IPBX](https://en.wikipedia.org/wiki/IP_PBX) 电话软件。

- [Asterisk](https://www.asterisk.org/) - 易用却先进的 IP PBX 系统、VoIP 网关与会议服务器。([Source Code](https://github.com/asterisk/asterisk)) `GPL-2.0` `C/deb`
- [Flexisip](https://www.linphone.org/en/flexisip-sip-server/) - 完整、模块化且可扩展的 SIP 服务器，包含推送网关，在需要推送通知才能在应用非前台时接收信息的移动平台上投递 SIP 来电或短信。([Source Code](https://github.com/BelledonneCommunications/flexisip)) `AGPL-3.0` `C/Docker`
- [Freepbx](https://www.freepbx.org) - 控制并管理 Asterisk 的基于 Web 的 GUI。([Source Code](https://git.freepbx.org/projects/FREEPBX)) `GPL-2.0` `PHP`
- [FreeSWITCH](https://freeswitch.org/) - 可扩展的跨平台电话平台。([Source Code](https://github.com/signalwire/freeswitch)) `MPL-2.0` `C`
- [FusionPBX](https://www.fusionpbx.com/) - 名为 FreeSWITCH 的多平台语音交换机的 Web 界面。([Source Code](https://github.com/fusionpbx/fusionpbx)) `MPL-1.1` `PHP`
- [Kamailio](https://www.kamailio.org/w/) - 模块化 SIP 服务器（注册/代理/路由等）。([Source Code](https://github.com/kamailio/kamailio)) `GPL-2.0` `C/deb`
- [openSIPS](https://opensips.org/) - 面向语音、视频、IM、在线状态及其他 SIP 扩展的 SIP 代理/服务器。([Source Code](https://github.com/OpenSIPS/opensips)) `GPL-2.0` `C`
- [Routr](https://routr.io) - 轻量 SIP 代理、位置服务器与注册器，用于可靠且可扩展的 SIP 基础设施。([Source Code](https://github.com/fonoster/routr)) `MIT` `Docker/K8S`
- [SIP3](https://sip3.io/) - VoIP 排障与监控平台。([Demo](https://demo.sip3.io), [Source Code](https://github.com/sip3io/)) `Apache-2.0` `Java`
- [SIPCAPTURE Homer](https://www.sipcapture.org/) - VoIP 呼叫的排障与监控。([Source Code](https://github.com/sipcapture/homer)) `AGPL-3.0` `Nodejs/Go/Docker`
- [Wazo](https://wazo-platform.org/) - 构建于 Asterisk 之上、功能完备的 IPBX 方案，带集成 Web 管理界面与 REST API。([Source Code](https://github.com/wazo-platform)) `GPL-3.0` `Python`
- [Yeti-Switch](https://yeti-switch.org/) - 带集成计费与路由引擎及 REST API 的 Transit 4 类软交换（SBC）。([Demo](https://demo.yeti-switch.org/), [Source Code](https://github.com/yeti-switch)) `GPL-2.0` `C++/Ruby`


<a id="communication---social-networks-and-forums"></a>
### Communication - Social Networks and Forums 通信 - 社交网络与论坛

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Social Networking 社交网络](https://en.wikipedia.org/wiki/Social_networking_service) 与 [Forum 论坛](https://en.wikipedia.org/wiki/Internet_forum) 软件。

- [Akkoma](https://akkoma.social/) - 联邦化微博服务器，兼容 Mastodon、GNU social 与 ActivityPub。([Source Code](https://akkoma.dev/AkkomaGang/akkoma)) `AGPL-3.0` `Elixir/Docker`
- [Answer](https://answer.apache.org) - 基于知识的社区软件。可用于快速搭建面向产品技术支持、客户支持、用户交流的问答社区等。([Source Code](https://github.com/apache/answer)) `Apache-2.0` `Docker/Go`
- [Artalk](https://artalk.js.org/) - 用 Golang 构建的评论系统，为你的网站添加评论提供轻量且高度可定制方案。([Source Code](https://github.com/ArtalkJS/Artalk)) `MIT` `Go/Docker`
- [AsmBB](https://board.asm32.info) - 用汇编编写、由 SQLite 驱动的快速论坛引擎。([Source Code](https://asm32.info/fossil/asmbb/index)) `EUPL-1.2` `Assembly`
- [BuddyPress](https://buddypress.org/about/) - 强大的插件，借助用户资料、动态流、用户群组等社交网络特性，让你的 WordPress 站点超越博客。([Source Code](https://github.com/buddypress/BuddyPress)) `GPL-2.0` `PHP`
- [Coral](https://coralproject.net/) - 来自 Vox Media 的更佳评论体验。([Source Code](https://github.com/coralproject/talk)) `Apache-2.0` `Docker/Nodejs`
- [diaspora*](https://diasporafoundation.org/) - 分布式社交网络服务器。([Source Code](https://github.com/diaspora/diaspora)) `AGPL-3.0` `Ruby`
- [Discourse](https://www.discourse.org/) - 基于 Ruby 与 JS 的先进论坛/社区方案。([Demo](https://try.discourse.org/), [Source Code](https://github.com/discourse/discourse)) `GPL-2.0` `Docker`
- [Elgg](https://elgg.org/) - 强大的社交网络引擎。([Source Code](https://github.com/Elgg/Elgg)) `GPL-2.0` `PHP`
- [Enigma 1/2 BBS](https://nuskooler.github.io/enigma-bbs/) - 现代、多平台 BBS 引擎，支持无限“呼叫者”与旧版 DOS 门游戏。([Source Code](https://github.com/NuSkooler/enigma-bbs)) `BSD-2-Clause` `Shell/Docker/Nodejs`
- [Flarum](https://flarum.org) - 令人愉悦的极简论坛。让在线讨论重新变得有趣的第三代论坛软件。([Source Code](https://github.com/flarum/flarum)) `MIT` `PHP`
- [Friendica](https://friendi.ca/) - 社交通信服务器。([Source Code](https://github.com/friendica/friendica)) `AGPL-3.0` `PHP`
- [GoToSocial](https://docs.gotosocial.org/en/latest/) - 实现 Mastodon 客户端 API 的 ActivityPub 联邦化社交网络服务器。([Source Code](https://codeberg.org/superseriousbusiness/gotosocial)) `AGPL-3.0` `Docker/Go`
- [Habitat](https://gethabitat.org/) - 面向本地社区的平台。([Source Code](https://github.com/carlnewton/habitat)) `AGPL-3.0` `Docker`
- [Hatsu](https://hatsu.cli.rs/) - 代表你的静态站点与 Fediverse 交互的桥接器。([Source Code](https://github.com/importantimport/hatsu)) `AGPL-3.0` `Docker/Rust`
- [Hubzilla](https://hubzilla.org) - 去中心化身份、隐私、发布、分享、云存储及通信/社交平台。([Source Code](https://framagit.org/hubzilla/core)) `MIT` `PHP`
- [HumHub](https://www.humhub.org/) - 用于私有社交网络的灵活套件。([Source Code](https://github.com/humhub/humhub)) `AGPL-3.0` `PHP`
- [Iceshrimp.NET](https://iceshrimp.net) - 通过 ActivityPub 通信的联邦化微博服务器。([Source Code](https://iceshrimp.dev/iceshrimp/iceshrimp.net)) `EUPL-1.2` `.NET/C#/Docker`
- [Isso](https://isso-comments.de/) - 用 Python 与 Javascript 编写的轻量评论服务器。目标是作为 Disqus 的即插即用替代品。([Source Code](https://github.com/isso-comments/isso)) `MIT` `Python/Docker`
- [Lemmy](https://join-lemmy.org/) - 面向 fediverse 的链接聚合器（Reddit 的替代方案）。([Source Code](https://github.com/LemmyNet/lemmy)) `AGPL-3.0` `Docker/Rust`
- [Loomio](https://www.loomio.org/) - 协作式决策工具，让任何人都能轻松参与影响其自身的决策。([Source Code](https://github.com/loomio/loomio)) `AGPL-3.0` `Docker`
- [Mastodon](https://joinmastodon.org/) - 联邦化微博服务器。([Source Code](https://github.com/mastodon/mastodon), [Clients](https://github.com/hyperupcall/awesome-mastodon)) `AGPL-3.0` `Ruby`
- [Misago](https://misago-project.org/) - 功能完备的现代论坛应用，快速、可扩展且响应式。([Source Code](https://github.com/rafalp/Misago)) `GPL-2.0` `Docker`
- [Misskey](https://misskey.io/) - 面向 Fediverse、类应用的去中心化微博服务器/SNS，使用与 GNU social、Mastodon 相同的 ActivityPub 协议。([Source Code](https://github.com/misskey-dev/misskey)) `AGPL-3.0` `Nodejs/Docker`
- [Movim](https://movim.eu/) - 基于 XMPP 的现代联邦化社交网络，具备功能完备的群聊、订阅与微博。([Source Code](https://github.com/movim/movim)) `AGPL-3.0` `PHP/Docker`
- [MyBB](https://mybb.com/) - 免费、可扩展的论坛软件包。([Source Code](https://github.com/mybb/mybb)) `LGPL-3.0` `PHP`
- [NodeBB](https://nodebb.org/) - 为现代 Web 构建的论坛软件。([Demo](https://try.nodebb.org/), [Source Code](https://github.com/NodeBB/NodeBB)) `GPL-3.0` `Nodejs/Docker`
- [OSSN](https://www.opensource-socialnetwork.org/) - 社交网络软件，让你创建社交网站，并帮助成员与有相似专业或个人兴趣的人建立社交关系。([Source Code](https://github.com/opensource-socialnetwork/opensource-socialnetwork)) `CAL-1.0` `PHP`
- [phpBB](https://www.phpbb.com/) - 纯文本论坛公告板软件方案，可用于与一群人保持联系，也可驱动你的整个网站。([Source Code](https://github.com/phpbb/phpbb)) `GPL-2.0` `PHP`
- [PieFed](https://join.piefed.social) - 面向 fediverse 的链接聚合器/Reddit 克隆（Reddit 的替代方案）。([Demo](https://piefed.social), [Source Code](https://codeberg.org/rimu/pyfedi)) `AGPL-3.0` `Python/Docker`
- [PixelFed](https://pixelfed.social) - 合乎伦理的图片分享平台，由 ActivityPub 联邦驱动（Instagram 的替代方案）。([Source Code](https://github.com/pixelfed/pixelfed)) `AGPL-3.0` `PHP`
- [Pleroma](https://pleroma.social) - 联邦化微博服务器，兼容 Mastodon、GNU social 与 ActivityPub。([Source Code](https://git.pleroma.social/pleroma/pleroma)) `AGPL-3.0` `Elixir`
- [qpixel](https://codidact.com/) - 基于问答的社区知识分享软件。([Source Code](https://github.com/codidact/qpixel)) `AGPL-3.0` `Ruby`
- [Redlib](https://github.com/redlib-org/redlib) `⚠` - 注重隐私的 Reddit 替代前端，起源于 Libreddit。`AGPL-3.0` `AGPL-3.0` `Rust`
- [remark42](https://remark42.com/) - 轻量、简单的评论引擎，不窥探用户。可嵌入博客、文章或任何读者发表评论之处。([Demo](https://remark42.com/demo/), [Source Code](https://github.com/umputun/remark42)) `MIT` `Docker/Go`
- [Scoold](https://scoold.com) - 打包于 JAR 中的 Stack Overflow。企业级问答平台，支持全文搜索、SAML、LDAP 集成与社交登录。([Demo](https://live.scoold.com), [Source Code](https://github.com/Erudika/scoold)) `Apache-2.0` `Java/Docker/K8S`
- [Simple Machines Forum](https://www.simplemachines.org/) - 免费、专业级的软件包，让你在数分钟内搭建自己的在线社区。([Source Code](https://github.com/SimpleMachines/SMF)) `BSD-3-Clause` `PHP`
- [Socialhome](https://socialhome.network) - 联邦化、去中心化的个人资料构建器与社交网络引擎。([Demo](https://socialhome.network/), [Source Code](https://github.com/jaywink/socialhome)) `AGPL-3.0` `Docker/Python`
- [Talkyard](https://www.talkyard.io/) - 创建社区，让用户可提议想法并获得问题解答。还支持友好的开放式讨论与聊天（Slack/StackOverflow/Discourse/Reddit/Disqus 混合体）。([Demo](https://www.talkyard.io/forum/latest), [Source Code](https://github.com/debiki/talkyard)) `AGPL-3.0` `Docker/Scala`
- [yarn.social](https://yarn.social) - 类似 Twitter™ 的去中心化微记录平台。无广告、无追踪，内容归你，数据归你。([Source Code](https://git.mills.io/yarnsocial/yarn)) `MIT` `Go`


<a id="communication---video-conferencing"></a>
### Communication - Video Conferencing 通信 - 视频会议

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Video/Web Conferencing 视频/Web 会议](https://en.wikipedia.org/wiki/Web_conferencing) 工具与软件。

_Related: [Conference Management 会议管理](#conference-management)_

- [BigBlueButton](https://bigbluebutton.org/) - 支持音频、视频、幻灯片（含白板控制）、聊天与屏幕的实时共享。教师可用投票、表情与分组讨论室吸引远程学生。([Source Code](https://github.com/bigbluebutton/bigbluebutton)) `LGPL-3.0` `Java`
- [Galene](https://galene.org/) - 易部署、所需服务器资源适中的视频会议服务器。([Source Code](https://github.com/jech/galene)) `MIT` `Go`
- [Janus](https://janus.conf.meetecho.com/) - 通用、轻量、极简的 WebRTC 服务器。([Demo](https://janus.conf.meetecho.com/demos/), [Source Code](https://github.com/meetecho/janus-gateway)) `GPL-3.0` `C`
- [Jitsi Meet](https://jitsi.org/Projects/JitsiMeet) - 使用 Jitsi Videobridge 提供高质量、可扩展视频会议的 WebRTC 应用。([Demo](https://meet.jit.si), [Source Code](https://github.com/jitsi/jitsi-meet)) `Apache-2.0` `Nodejs/Docker/deb`
- [Jitsi Video Bridge](https://jitsi.org/Projects/JitsiVideobridge) - 兼容 WebRTC 的选择性转发单元（SFU），支持多用户视频通信。([Source Code](https://github.com/jitsi/jitsi-videobridge)) `Apache-2.0` `Java/deb`
- [MiroTalk C2C](https://c2c.mirotalk.com) - 实时摄像头对摄像头视频通话与屏幕共享，端到端加密，可通过简单 iframe 嵌入任意网站。([Source Code](https://github.com/miroslavpejic85/mirotalkc2c)) `AGPL-3.0` `Nodejs/Docker`
- [MiroTalk P2P](https://p2p.mirotalk.com) - 简单、安全、快速、最高 4k 与 60fps 的实时视频会议，兼容所有浏览器与平台。([Demo](https://p2p.mirotalk.com/newcall), [Source Code](https://github.com/miroslavpejic85/mirotalk)) `AGPL-3.0` `Nodejs/Docker`
- [MiroTalk SFU](https://sfu.mirotalk.com) - 简单、安全、可扩展、最高 4k 的实时视频会议，兼容所有浏览器与平台。([Demo](https://sfu.mirotalk.com/newroom), [Source Code](https://github.com/miroslavpejic85/mirotalksfu)) `AGPL-3.0` `Nodejs/Docker`
- [plugNmeet](https://www.plugnmeet.org/) - 可扩展、高性能的 Web 会议系统。([Demo](https://demo.plugnmeet.com/login.html), [Source Code](https://github.com/mynaparrot/plugNmeet-server)) `MIT` `Docker/Go`


<a id="communication---xmpp---servers"></a>
### Communication - XMPP - Servers 通信 - XMPP - 服务器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Extensible Messaging and Presence Protocol](https://en.wikipedia.org/wiki/XMPP) 服务器。

- [ejabberd](https://www.ejabberd.im/) - XMPP 即时消息服务器。([Source Code](https://github.com/processone/ejabberd)) `GPL-2.0` `Erlang/Docker`
- [MongooseIM](https://www.erlang-solutions.com/products/mongooseim.html) - 注重性能与可扩展性的移动消息平台。([Source Code](https://github.com/esl/MongooseIM)) `GPL-2.0` `Erlang/Docker/K8S`
- [Openfire](https://www.igniterealtime.org/projects/openfire/) - 实时协作（RTC）服务器。([Source Code](https://github.com/igniterealtime/Openfire)) `Apache-2.0` `Java`
- [Prosody IM](https://prosody.im/) - 功能丰富且易配置的 XMPP 服务器。([Source Code](https://hg.prosody.im/)) `MIT` `Lua`
- [Snikket](https://snikket.org/) - 一体化、容器化的简易 XMPP 方案，含 Web 管理与客户端。([Source Code](https://github.com/snikket-im/snikket-server), [Clients](https://snikket.org/app/)) `Apache-2.0` `Docker`
- [Tigase](https://tigase.net/xmpp-server) - 用 Java 实现的 XMPP 服务器。([Source Code](https://github.com/tigase/tigase-server)) `GPL-3.0` `Java`


<a id="communication---xmpp---web-clients"></a>
### Communication - XMPP - Web Clients 通信 - XMPP - Web 客户端

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Extensible Messaging and Presence Protocol](https://en.wikipedia.org/wiki/XMPP) Web 客户端/界面。

- [Converse.js](https://conversejs.org/) - 浏览器中的 XMPP 聊天客户端。([Source Code](https://github.com/conversejs/converse.js)) `MPL-2.0` `Javascript`
- [Libervia](https://repos.goffi.org/libervia-web) - 来自 Salut à Toi 的 Web 前端。`AGPL-3.0` `AGPL-3.0` `Python`
- [Salut à Toi](https://www.salut-a-toi.org/) - 多用途、多前端、自由且去中心化的通信工具。([Source Code](https://repos.goffi.org/libervia-backend)) `AGPL-3.0` `Python`


<a id="community-supported-agriculture-csa"></a>
### Community-Supported Agriculture (CSA) 社区支持农业（CSA）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

面向社区支持农业与食物合作社的管理与行政工具。

_Related: [E-commerce 电子商务](#e-commerce)_

- [ACP Admin](https://acp-admin.ch/) - CSA 管理。管理成员、订阅、交付、自提点、成员参与、发票与邮件（文档为法语）。([Source Code](https://github.com/csa-admin-org/csa-admin)) `MIT` `Ruby`
- [FoodCoopShop](https://www.foodcoopshop.com/) - 面向食物合作社、用户友好的软件。([Source Code](https://github.com/foodcoopshop/foodcoopshop)) `AGPL-3.0` `PHP/Docker`
- [Foodsoft](https://foodcoops.net/) - 管理非营利食物合作社（产品目录、订购、记账、排班）。([Source Code](https://github.com/foodcoops/foodsoft)) `AGPL-3.0` `Docker/Ruby`
- [Hive-Pal](https://hivepal.app) - 移动优先的养蜂管理应用，用于追踪蜂箱、检查、蜂后记录与设备，数据录入精简、适合现场使用。([Demo](https://hivepal.app), [Source Code](https://github.com/martinhrvn/hive-pal)) `MIT` `Nodejs/Docker`
- [juntagrico](https://juntagrico.org/) - 面向社区花园与蔬菜合作社的管理平台。([Source Code](https://github.com/juntagrico/juntagrico)) `LGPL-3.0` `Python`
- [Open Food Network](https://www.openfoodnetwork.org/) - 本地食物的在线市场。它支撑一个由独立在线食品商店组成的网络，把农户与食物枢纽同个人及本地商家连接起来。([Source Code](https://github.com/openfoodfoundation/openfoodnetwork)) `AGPL-3.0` `Ruby`
- [OpenOlitor](https://openolitor.org/) - 面向社区支持农业团体的管理平台。([Source Code](https://github.com/OpenOlitor/openolitor-server)) `AGPL-3.0` `Scala`
- [teikei](https://github.com/teikei/teikei) - 基于众包数据、将社区支持农业标注于地图的 Web 应用。([Demo](https://ernte-teilen.org/karte/#/)) `AGPL-3.0` `Nodejs`


<a id="conference-management"></a>
### Conference Management 会议管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

用于提交 [abstracts 摘要](https://en.wikipedia.org/wiki/Abstract_management) 并筹备/管理学术会议的软件。

_Related: [Communication - Video Conferencing 通信 - 视频会议](#communication---video-conferencing)_

- [indico](https://getindico.io/) - 功能丰富的活动管理系统，诞生于万维网发源地 CERN。([Demo](https://sandbox.getindico.io/), [Source Code](https://github.com/indico/indico)) `MIT` `Python`
- [motion.tools (Antragsgrün)](https://motion.tools/) - 为（政治性）大会管理动议与修正案。([Demo](https://sandbox.motion.tools/createsite), [Source Code](https://github.com/CatoTH/antragsgruen)) `AGPL-3.0` `PHP/Docker`
- [OpenSlides](https://openslides.com/) - 用于管理与投影会议议程、动议与选举的演示与大会系统。([Demo](https://demo.openslides.org/login), [Source Code](https://github.com/OpenSlides/OpenSlides)) `MIT` `Docker`
- [osem](https://osem.io/) - 面向自由软件会议定制的活动管理。([Source Code](https://github.com/openSUSE/osem)) `MIT` `Ruby/Docker`
- [pretalx](https://pretalx.org) - 基于 Web 的活动管理，包括发起征文（Call for Papers）、评审投稿与排定演讲。支持多种相关工具的导入导出。([Source Code](https://github.com/pretalx/pretalx)) `Apache-2.0` `Python`


<a id="content-management-systems-cms"></a>
### Content Management Systems (CMS) 内容管理系统（CMS）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Content Management Systems](https://en.wikipedia.org/wiki/Content_management_system) offer a practical way to setup a website with many features, using third party plugins, themes and functionality that are easy to add and customize.

_Related: [Blogging Platforms 博客平台](#blogging-platforms), [Static Site Generators 静态站点生成器](#static-site-generators), [Photo Galleries 相册](#photo-galleries)_

- [Alfresco Community Edition](https://www.alfresco.com/products/community/download) - 企业内容管理软件，可处理任何类型的内容，使用户能够轻松共享内容并进行协作。(L0) `LGPL-3.0` `Java`
- [Apostrophe](https://apostrophecms.com/) - 内容管理系统侧重于可扩展的上下文编辑工具。(L0, L1) `MIT` `Nodejs`
- [Automad](https://automad.org/) - 平面文件内容管理系统和模板引擎。(L0, L1) `MIT` `PHP/Docker`
- [Backdrop CMS](https://backdropcms.org/) - 面向中小型企业和非营利组织的全面内容管理系统。(L0) `GPL-2.0` `PHP`
- [Bludit](https://www.bludit.com/) `⚠` - 在几秒钟内构建网站或博客。Bludit使用平面文件（ JSON格式的文本文件）来存储帖子和页面。（ L0 ） `MIT` `PHP`
- [Bolt CMS](https://boltcms.io/) - 内容管理工具，力求尽可能简单明了。（ L0 ） `MIT` `PHP`
- [CMS Made Simple](https://www.cmsmadesimple.org/) - 更快、更轻松地管理网站内容，可扩展到小型企业和大型企业。（ L0 ） `GPL-2.0` `PHP`
- [Cockpit](https://getcockpit.com) - 用于管理任何结构化内容的简单内容平台。（ L0 ） `MIT` `PHP`
- [Concrete 5 CMS](https://www.concretecms.com) - 开源内容管理系统。（ L0 ） `MIT` `PHP`
- [Contao](https://contao.org/) - 强大的CMS ，可让您创建专业网站和可扩展的Web应用程序。(L0, L1) `LGPL-3.0` `PHP`
- [CouchCMS](https://www.couchcms.com/) - 面向设计师的CMS。（ L0 ） `CPAL-1.0` `PHP`
- [Drupal](https://www.drupal.org/) - 高级内容管理平台。（ L0 ） `GPL-2.0` `PHP`
- [eLabFTW](https://www.elabftw.net) - 用于研究实验室的在线实验室笔记本。存储实验，使用数据库查找试剂或协议，使用可信时间戳为实验添加合法时间戳，导出为pdf或zip存档，与合作者共享……。(L0, L1) `AGPL-3.0` `PHP`
- [Expressa](https://github.com/thomas4019/expressa) - 内容管理系统，用于使用JSON架构为数据库驱动的网站提供支持。提供权限管理和自动REST API。 `MIT` `Nodejs`
- [Joomla!](https://www.joomla.org/) - 高级内容管理系统(CMS)。(L0) `GPL-2.0` `PHP`
- [KeystoneJS](https://keystonejs.com/) - CMS和Web应用程序平台。（ L0 ） `MIT` `Nodejs`
- [Localess](https://localess.org/home) `⚠` - 强大的翻译管理和内容管理系统。使用人工智能更快地将您的网站或应用内容管理和翻译成多种语言。(L0) `MIT` `Docker`
- [MODX](https://modx.com/) - 先进的内容管理和发布平台。当前版本称为“Revolution”。（ L0 ） `GPL-2.0` `PHP`
- [Neos](https://www.neos.io) - 现代CMS。NEOS或TYPO3 NEOS （适用于版本1 ）。（ L0 ） `GPL-3.0` `PHP`
- [Noosfero](https://gitlab.com/noosfero/noosfero) - 在同一系统中，通过博客、电子投资组合、CMS、RSS、主题讨论、活动议程和团结经济的集体智慧，为社会和团结经济网络提供平台。 `AGPL-3.0` `Ruby`
- [Omeka](https://omeka.org) - 在您的服务器上使用专为学者、博物馆、图书馆、档案馆和爱好者设计的Omeka ，遵循都柏林核心标准，创建复杂的叙事并分享丰富的藏品。(L0, L1) `GPL-3.0` `PHP`
- [Payload CMS](https://payloadcms.com/) - 开发人员优先的无头CMS和应用程序框架。（ L0 ） `MIT` `Nodejs`
- [Pimcore](http://www.pimcore.com/) - 多渠道体验和参与管理平台。（ L0 ） `GPL-3.0` `PHP/Docker`
- [Plone](https://plone.org/) - 用于创建、编辑和管理数字内容（如网站、Intranet和自定义解决方案）的CMS系统。（ L0 ） `ZPL-2.0` `Python/Docker`
- [Publify](https://publify.github.io/) - 简单但功能齐全的网络发布软件。（ L0 ） `MIT` `Ruby`
- [Pushword](https://pushword.piedweb.com) - 基于Symfony构建的内容管理系统，其中页面为Markdown ，主题为Twig ，可选的基于Git的平面文件存储。(L0, L1) `MIT` `PHP`
- [REDAXO](https://www.redaxo.org) - 简单、灵活和实用的内容管理系统（德语文档）。（ L0 ） `MIT` `PHP/Docker`
- [SilverStripe](https://www.silverstripe.org) - 易于使用的CMS ，具有强大的MVC框架底层。(L0, L1) `BSD-3-Clause` `PHP`
- [SPIP](https://www.spip.net/fr) - 面向互联网的出版系统，旨在为网络作者提供协作工作、多语言环境和使用简便性。（ L0 ） `GPL-3.0` `PHP`
- [Squidex](https://squidex.io) - 无头CMS ，基于MongoDB、CQRS和事件源。(L0, L1) `MIT` `.NET`
- [Strapi](https://strapi.io/) - 无头CMS ，允许开发人员快速构建内容API ，同时为内容创建者提供友好的编辑界面。(L0) `MIT` `Nodejs`
- [Superdesk](https://superdesk.org/) `⚠` - 端到端的新闻创作、制作、策展、分发和发布平台。（ L0 ） `AGPL-3.0` `Docker/Python/PHP`
- [Textpattern](https://textpattern.com/) - 灵活、优雅且易于使用的CMS。(L0, L1) `GPL-2.0` `PHP`
- [Typemill](https://typemill.net/) - 使用基于vue.js的可视化降价编辑器，编写方便的平面文件-CMS。(L0) `MIT` `PHP`
- [TYPO3](https://typo3.org/) - 强大而先进的CMS ，拥有庞大的社区。（ L0 ） `GPL-2.0` `PHP`
- [Umbraco](https://umbraco.com/) - 友好的CMS ，拥有令人惊叹的社区。（ L0 ） `MIT` `.NET`
- [Vvveb CMS](https://www.vvveb.com) - 功能强大且易于使用的CMS来构建网站、博客或电子商务商店。(L0, L1) `AGPL-3.0` `PHP/Docker`
- [Wagtail](https://wagtail.io/) - Django内容管理系统专注于灵活性和用户体验。（ L0 ） `BSD-3-Clause` `Python`
- [WinterCMS](https://wintercms.com/) - 基于Laravel PHP框架构建的快速安全的内容管理系统。（ L0 ） `MIT` `PHP`
- [WonderCMS](https://www.wondercms.com) - 自2008年以来最小的平面文件CMS。(L0, L1) `MIT` `PHP`
- [WordPress](https://wordpress.org/) - 全球最常用的博客和CMS引擎。（ L0 ） `GPL-2.0` `PHP`


<a id="customer-relationship-management-crm"></a>
### Customer Relationship Management (CRM) 客户关系管理（CRM）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Customer relationship management (CRM)](https://en.wikipedia.org/wiki/Customer_relationship_management) is a strategic process that organizations use to manage, analyze, and improve their interactions with customers.

_Related: [Communication - Email - Mailing Lists and Newsletters 通信 - 电子邮件 - 邮件列表与新闻稿](#communication---email---mailing-lists-and-newsletters), [Analytics 分析](#analytics), [Calendar & Contacts 日历与联系人](#calendar--contacts)_

- [Corteza](https://docs.cortezaproject.org) - CRM包括统一的工作空间、企业消息传递和低代码环境，可快速安全地提供基于记录的管理解决方案。(L0, L1) `Apache-2.0` `Go`
- [Django-CRM](https://DjangoCRM.github.io/info/) - 具有任务管理、电子邮件营销等功能的分析型CRM。Django CRM专为个人使用、任何规模的企业或自由职业者而构建，旨在提供轻松定制和快速开发。（ L0 ） `AGPL-3.0` `Python`
- [EspoCRM](https://www.espocrm.com/) - 具有设计为单页应用程序的前端和REST API的CRM。(L0, L1) `AGPL-3.0` `PHP`
- [Krayin](https://krayincrm.com/) - 面向中小企业和企业的CRM解决方案，可实现完整的客户生命周期管理。(L0, L1) `MIT` `PHP`
- [Relaticle](https://relaticle.com) - 具有MCP服务器、具有人工批准更改的AI助手、REST API、自定义字段和看板的CRM。（ L0 ） `AGPL-3.0` `PHP/Docker`
- [SuiteCRM](https://suitecrm.com) - 屡获殊荣的企业级CRM。(L0) `AGPL-3.0` `PHP`
- [Twenty](https://twenty.com) - 现代CRM提供灵活性、高级功能和时尚设计。（ L0 ） `AGPL-3.0` `Docker`


<a id="database-management"></a>
### Database Management 数据库管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Web interfaces for [database](https://en.wikipedia.org/wiki/Database) management. Includes tools for database analytics and visualization.

_Related: [Analytics 分析](#analytics), [Automation 自动化](#automation)_

_See also: [dbdb.io - Database of Databases](https://dbdb.io/)_

- [Adminer](https://www.adminer.org/) - 单个PHP文件中的数据库管理。适用于MySQL、MariaDB、PostgreSQL、SQLite、MS SQL、Oracle、Elasticsearch、MongoDB等。（ L0 ） `Apache-2.0/GPL-2.0` `PHP`
- [Azimutt](https://azimutt.app) - 为真实世界的数据库（大而凌乱）进行的可视化数据库探索。探索您的数据库架构以及数据，记录它们，扩展它们，甚至获得分析和指南。(L0, L1) `MIT` `Elixir/Nodejs/Docker`
- [Baserow](https://baserow.io/) - 在没有技术经验的情况下创建自己的数据库（ Airtable的替代品）。（ L0 ） `MIT` `Docker`
- [Bytebase](https://www.bytebase.com/) - DevOps团队安全的数据库架构更改和版本控制，支持MySQL、PostgreSQL、TiDB、ClickHouse和Snowflake。（ L0 ） `MIT` `Docker/K8S/Go`
- [Chartbrew](https://chartbrew.com) - 直接连接到数据库和API ，并使用数据创建精美的图表。(L0, L1) `MIT` `Nodejs/Docker`
- [ChartDB](https://chartdb.io/) - 数据库图编辑器，允许您使用单个查询可视化和设计数据库。(L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [CloudBeaver](https://dbeaver.com/) - 管理数据库，支持PostgreSQL、MySQL、SQLite等。DBeaver的Web/托管版本。（ L0 ） `Apache-2.0` `Docker`
- [d9](https://d9.webcapsule.io) - 通过直观的管理界面将SQL数据库转换为安全的API。数据平台和无头CMS （ Directus分支）。（ L0 ） `GPL-3.0` `Nodejs`
- [Databunker](https://databunker.org/) - 基于网络、符合GDPR、安全的个人数据库或PII。(L0) `MIT` `Docker`
- [datannur](https://datannur.com) - 轻量级数据目录，用于记录和探索结构化数据文件和数据库。(L0, L1) `MIT` `Python`
- [Datasette](https://datasette.io/) - 通过轻松的导入导出和数据库管理，探索和发布数据。（ L0 ） `Apache-2.0` `Python/Docker`
- [drawDB](https://www.drawdb.app) - MySQL、PostgreSQL、SQLite、MariaDB、MSSQL和Oracle的基于浏览器的可视化和DBML数据库图编辑器和SQL生成器。(L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [Evidence](https://evidence.dev) - 基于代码的BI工具。使用SQL和markdown编写报告，并将其呈现为网站。(L0) `MIT` `Nodejs`
- [LibreDB Studio](https://libredb.org) - 基于浏览器的SQL IDE ，适用于PostgreSQL、MySQL、Oracle、SQL Server、MongoDB、Redis、ClickHouse、DuckDB等，具有SSO、审计跟踪、ER图和您自己的模型密钥上的可选AI辅助（ DataGrip、DBeaver、CloudBeaver的替代品）。（ L0 ） `MIT` `Docker/K8S`
- [Limbas](https://www.limbas.com/en/) - 用于创建数据库驱动业务应用程序的数据库框架。作为一个图形数据库前端，它可以实现数据存储的高效处理和舒适的数据库应用程序的灵活开发。（ L0 ） `GPL-2.0` `PHP`
- [Mathesar](https://mathesar.org/) - 直观的用户界面，以协作方式管理数据，适用于所有技术技能水平的用户。基于Postgres构建–连接现有数据库或设置新数据库。（ L0 ） `GPL-3.0` `Docker/Python`
- [OrcaQ](https://orca-q.com) - 使用内置AI助手管理、查询和探索多种数据库类型的现代数据库客户端和IDE。（ L0 ） `MIT` `Nodejs/deb/Docker`
- [StackRender](https://stackrender.io/) - 支持PostgreSQL、MySQL、MariaDB、SQLite、SQL Server和Oracle的数据库架构设计和SQL迁移生成器。(L0, L1) `AGPL-3.0` `Nodejs/Docker`


<a id="dns"></a>
### DNS 域名系统（DNS）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[DNS](https://en.wikipedia.org/wiki/Domain_Name_System) servers and management tools with advertisement blocking functionality, primarily aimed at home or small networks.

_See also: [awesome-sysadmin/DNS - Servers](https://github.com/awesome-foss/awesome-sysadmin#dns---servers), [awesome-sysadmin/DNS - Control Panels & Domain Management](https://github.com/awesome-foss/awesome-sysadmin#dns---control-panels--domain-management)_

- [AdGuard Home](https://adguard.com/en/adguard-home/overview.html) - 用户友好的广告和跟踪器拦截DNS服务器。（ L0 ） `GPL-3.0` `Docker`
- [blocky](https://0xerr0r.github.io/blocky/latest/) - 快速轻量级的DNS代理作为本地网络的广告拦截器，具有许多功能（ Pi-hole的替代品）。（ L0 ） `Apache-2.0` `Go/Docker`
- [Maza ad blocking](https://maza-ad-blocking.andros.dev/) - 本地广告拦截器。类似于Pi-hole ，但本地并使用您的操作系统。（ L0 ） `Apache-2.0` `Shell`
- [Numa](https://numa.rs/) - 在单个Rust二进制文件（ Pi-hole、AdGuard Home、NextDNS的替代品）中，使用DNSSEC验证递归解析、DoH/DoT/Oblivious DoH、短暂覆盖和本地服务域的广告拦截DNS解析器。（ L0 ） `MIT` `Rust/Docker/Nix`
- [Pi-hole](https://pi-hole.net/) - 具有用于管理和监控的GUI的互联网广告黑洞。（ L0 ） `EUPL-1.2` `Shell/PHP/Docker`
- [Technitium DNS Server](https://technitium.com/dns/) - 具有广告拦截功能的权威/递归DNS服务器。（ L0 ） `GPL-3.0` `Docker/C#`


<a id="document-management"></a>
### Document Management 文档管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [document management system](https://en.wikipedia.org/wiki/Document_management_system) (DMS) is a system used to receive, track, manage and store documents and reduce paper.

- [BentoPDF](https://bentopdf.com) `⚠` - 功能强大、以隐私为先的客户端PDF工具包，可让您直接在浏览器中操作、编辑、合并和处理PDF文件。(L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [Bottle Rocket](https://bottle-rocket.app/) - 文档扫描和管理应用程序，兼容Rocketbook和Scribzee格式。（ L0 ） `MIT` `C#/Docker`
- [Docspell](https://docspell.org) - 自动标记文档管理器和存档。（ L0 ） `GPL-3.0` `Scala/Java/Docker`
- [Documenso](https://documenso.com) - 数字文档签名平台（ DocuSign的替代品）。（ L0 ） `AGPL-3.0` `Nodejs/Docker`
- [Docuseal](https://www.docuseal.co) - 创建、填写和签署数字文档（ DocuSign的替代方案）。(L0, L1) `AGPL-3.0` `Docker`
- [EveryDocs](https://github.com/jonashellmann/everydocs-core) - 供私人使用的简单文档管理系统，具有以数字方式组织文档的基本功能。 `GPL-3.0` `Docker/Ruby`
- [Gotenberg](https://gotenberg.dev) - 开发人员友好的API ，可与Chromium和LibreOffice等强大工具进行交互，将多种文档格式（ HTML、Markdown、Word、Excel等）转换为PDF文件等。（ L0 ） `MIT` `Docker`
- [I, Librarian](https://i-librarian.net) - 整理PDF文件和办公文件。它为工业界和学术界的学生和研究团体提供了许多额外的功能。(L0, L1) `GPL-3.0` `PHP`
- [Mayan EDMS](https://www.mayan-edms.com) - 使用预览生成、OCR和自动分类等功能，为您的文档提供电子文档管理系统。（ L0 ） `GPL-2.0` `Docker/K8S`
- [OpenSign](https://www.opensignlabs.com) `⚠` - 文档签名软件（ DocuSign的替代品）。（ L0 ） `AGPL-3.0` `Nodejs/Docker`
- [Paperless-ngx](https://docs.paperless-ngx.com/) - 使用改进的界面（无纸分叉）扫描、索引和存档所有纸质文档。(L0, L1) `GPL-3.0` `Python/Docker`
- [Papermerge](https://papermerge.com) - 文件管理系统侧重于扫描文件（电子档案）。具有类似于Dropbox/Google云端硬盘的文件浏览功能。OCR、全文搜索、文本叠加/选择。（ L0 ） `Apache-2.0` `Docker/K8S`
- [Papra](https://papra.app) - 简约的文档存储、管理和存档平台，易于使用，每个人都可以访问。(L0, L1) `AGPL-3.0` `Docker`
- [PdfDing](https://www.pdfding.com) - PDF管理器、查看器和编辑器，在多个设备上提供无缝的用户体验。它旨在使用Docker进行最小、快速和易于设置的设计。(L0, L1) `AGPL-3.0` `Docker/K8S`
- [SeedDMS](https://www.seeddms.org) - 文档管理系统，包括工作流、访问权限、全文搜索等。(L0, L1) `GPL-2.0` `PHP`
- [Signature PDF](https://github.com/24eme/signaturepdf) - 通过协作、组织、压缩和元数据编辑对PDF进行签名和操作。(L0) `AGPL-3.0` `PHP/deb/Docker`
- [SimpleDMS](https://simpledms.eu) - 易于使用、元数据驱动的小型企业文档管理系统(DMS) ，几乎可以自行对文档进行排序。(L0, L1) `AGPL-3.0` `Docker`
- [SnapOtter](https://snapotter.com) - 200多种用于转换和编辑图像、视频、音频和PDF的网络工具套件，包括基于图层的图像编辑器、OCR、转录、背景去除和批处理管道（ SmallPDF、iLovePDF、CloudConvert的替代品）。(L0, L1) `AGPL-3.0` `Docker`
- [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) - 本地托管的Web应用程序，允许您对PDF文件执行各种操作，例如合并、拆分、文件转换和OCR。 `Apache-2.0` `Docker/Java`


<a id="document-management---e-books"></a>
### Document Management - E-books 文档管理 - 电子书

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Ebook](https://en.wikipedia.org/wiki/Ebook) library management software.

- [Atsumeru](https://atsumeru.xyz) - 漫画/漫画/轻小说媒体服务器，带有适用于Windows、Linux、macOS和Android的客户端。(L0, L1) `MIT` `Java/Docker`
- [Bindery](https://github.com/jarynclouatre/bindery) - 电子书和漫画的文件夹观看转换器。EPUB到Kobo KEPUB通过kepubify ， CBZ/CBR/PDF通过Kindle漫画转换器，具有每个设备配置文件， ComicInfo.xml命名，章节到卷捆绑和Web UI。 `MIT` `Docker`
- [BookLogr](https://github.com/Mozzo1000/booklogr) - 轻松管理您的个人图书库。（ L0 ） `Apache-2.0` `Docker`
- [Calibre Web Automated](https://github.com/crocodilestick/Calibre-Web-Automated) - 一体化解决方案，将Calibre-Web的现代轻量级Web UI与Calibre （ Calibre Web的分支）的强大、多功能功能集相结合。 `GPL-3.0` `Docker`
- [Calibre Web](https://github.com/janeczku/calibre-web) - 使用现有的Calibre数据库浏览、阅读和下载电子书。 `GPL-3.0` `Python`
- [Calibre](https://calibre-ebook.com/) - 电子书库管理器，可以查看、转换和编目大多数主要电子书格式的电子书，并为远程客户端提供内置的Web服务器。(L0, L1) `GPL-3.0` `Python/deb`
- [Grimmory](https://grimmory.org/) - 内置阅读器、元数据查找、多用户支持、OPD和Kobo/KOReader同步的电子书、漫画和有声读物库。（ L0 ） `AGPL-3.0` `Docker`
- [Inkheart](https://gitlab.com/Nystik/inkheart) - 轻量级PDF库和阅读器。 `Apache-2.0` `Docker`
- [Kapowarr](https://casvt.github.io/Kapowarr/) - 构建和管理漫画书库。根据您的喜好下载、重命名、移动和转换卷的问题。（ L0 ） `GPL-3.0` `Docker/Python`
- [Kavita](https://www.kavitareader.com/) - 跨平台电子书/漫画/漫画/pdf服务器和网络阅读器，具有用户管理、评级和评论以及元数据支持。(L0, L1) `GPL-3.0` `.NET/Docker`
- [kiwix-serve](https://github.com/kiwix/kiwix-tools) - 用于从ZIM文件提供wiki的HTTP后台程序。 `GPL-3.0` `C++`
- [Komga](https://komga.org) - 用于漫画/漫画/BD的媒体服务器，支持API和OPD ，用于探索库的现代Web界面，以及Web阅读器。（ L0 ） `MIT` `Java/Docker`
- [MyMangaDB](https://github.com/FabianRolfMatthiasNoll/MyMangaDB) `⚠` - 漫画收藏管理器，具有自动元数据、MyAnimeList导入和详细的收藏统计信息。 `GPL-3.0` `Docker`
- [Stump](https://www.stumpapp.dev) - 支持OPDS的快速漫画、漫画和数字图书服务器。（ L0 ） `MIT` `Rust`


<a id="document-management---institutional-repository-and-digital-library-software"></a>
### Document Management - Institutional Repository and Digital Library Software 文档管理 - 机构知识库与数字图书馆软件

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Institutional repository](https://en.wikipedia.org/wiki/Institutional_repository) and [digital library](https://en.wikipedia.org/wiki/Digital_library) management software.

- [DSpace](http://www.dspace.org/) - 交钥匙存储库应用程序，提供对数字资源的持久访问。（ L0 ） `BSD-3-Clause` `Java`
- [EPrints](https://www.eprints.org/) - 数字文档管理系统，具有灵活的元数据和工作流程模型，主要针对学术机构。(L0, L1) `GPL-3.0` `Perl`
- [Fedora Commons Repository](https://wiki.lyrasis.org/display/FF/Fedora+Repository+Home) - 强大的模块化存储系统，用于管理和传播数字内容，特别适用于数字图书馆和档案馆，用于访问和保存。（ L0 ） `Apache-2.0` `Java`
- [InvenioRDM](https://inveniordm.docs.cern.ch/) - 高度可扩展的交钥匙研究数据管理平台，具有出色的用户体验。（ L0、L1、L2 ） `MIT` `Python`
- [Islandora](https://www.islandora.ca/) - 用于浏览和管理基于Fedora的数字存储库的Drupal模块。(L0, L1) `GPL-3.0` `PHP`
- [Samvera Hyrax](https://samvera.org/) - Samvera框架的前端，它本身就是一个Ruby on Rails应用程序，用于浏览和管理基于Fedora的数字存储库。（ L0 ） `Apache-2.0` `Ruby`


<a id="document-management---integrated-library-systems-ils"></a>
### Document Management - Integrated Library Systems (ILS) 文档管理 - 集成图书馆系统（ILS）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

An [integrated library system](https://en.wikipedia.org/wiki/Integrated_library_system) is an enterprise resource planning system for a library, used to track items owned, orders made, bills paid, and patrons who have borrowed.

_Related: [Content Management Systems (CMS) 内容管理系统（CMS）](#content-management-systems-cms), [Archiving and Digital Preservation (DP) 存档与数字化保存（DP）](#archiving-and-digital-preservation-dp)_

- [Evergreen](https://evergreen-ils.org) - 为图书馆提供高度可扩展的软件，帮助图书馆订阅会员查找图书馆资料，并帮助图书馆管理、编目和传播这些资料。（ L0 ） `GPL-2.0` `PLpgSQL`
- [Koha](https://koha-community.org/) - 企业级ILS ，带有收购、流通、编目、标签打印、离线流通等模块，适用于无法访问互联网时。(L0, L1) `GPL-3.0` `Perl`
- [RERO ILS](https://rero21.ch/) - 可以作为具有联合功能的服务运行的大规模ILS ，主要用于图书馆网络。包括大多数标准模块（发行、收购、编目等）和基于网络的公共和专业界面。(L0, L1) `AGPL-3.0` `Python/Docker`


<a id="e-commerce"></a>
### E-commerce 电子商务

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[E-commerce](https://en.wikipedia.org/wiki/E-commerce) software.

_Related: [Community-Supported Agriculture (CSA) 社区支持农业（CSA）](#community-supported-agriculture-csa)_

- [Aimeos](https://aimeos.org/) - 使用Laravel构建定制在线商店、市场和复杂B2B应用程序的电子商务框架，可扩展到数十亿件商品。(L0, L1) `LGPL-3.0/MIT` `PHP`
- [Bagisto](https://bagisto.com/en/) - 领先的Laravel电子商务框架，具有多库存来源、税务、本地化、直销和更多令人兴奋的功能。(L0, L1) `MIT` `PHP`
- [CoreShop](https://www.coreshop.org) - Pimcore的电子商务插件。（ L0 ） `GPL-3.0` `PHP`
- [Drupal Commerce](https://drupalcommerce.org) - Drupal CMS的热门电子商务模块，支持数十个支付、运输和购物相关模块。（ L0 ） `GPL-2.0` `PHP`
- [EverShop](https://evershop.io/) `⚠` - 具有基本商务功能的电子商务平台。模块化架构，完全可定制。(L0, L1) `GPL-3.0` `Docker/Nodejs`
- [Magento Open Source](https://business.adobe.com/products/magento/magento-commerce.html) - 开放式全渠道创新的领先提供商。（ L0 ） `OSL-3.0` `PHP`
- [MedusaJs](https://medusajs.com/) - 无头商务引擎，使开发人员能够创建令人惊叹的数字商务体验。(L0, L1) `MIT` `Nodejs`
- [myCart](https://github.com/shurco/mycart) `⚠` - 1个文件中的购物车（支持通过卡或加密货币付款）。 `MIT` `Go/Docker`
- [Open Source POS](https://github.com/opensourcepos/opensourcepos) - 基于Web的销售点系统。 `MIT` `PHP`
- [OpenCart](https://www.opencart.com) - 购物车解决方案。（ L0 ） `GPL-3.0` `PHP`
- [PrestaShop](https://www.prestashop.com/) - 完全可扩展的电子商务解决方案。(L0, L1) `OSL-3.0` `PHP`
- [Pretix](https://pretix.eu/) - 活动门票销售平台。（ L0 ） `AGPL-3.0` `Python/Docker`
- [s-cart](https://s-cart.org/) - 基于Laravel框架构建的个人和企业电子商务网站。(L0, L1) `MIT` `PHP`
- [Saleor](https://saleor.io) - GraphQL原生、仅限API的平台，用于可扩展的可组合电子商务店面。(L0, L1) `BSD-3-Clause` `Docker/Python`
- [Shopware Community Edition](https://www.shopware.com/en/community/community-edition/) - 基于PHP的开源电子商务软件，德国制造。(L0, L1) `MIT` `PHP`
- [Solidus](https://solidus.io/) - 电子商务平台，让您完全控制您的商店。（ L0 ） `BSD-3-Clause` `Ruby/Docker`
- [Spree Commerce](https://spreecommerce.org) - 完整、模块化和API驱动的Ruby on Rails电子商务解决方案。(L0, L1) `BSD-3-Clause` `Ruby`
- [Sylius](https://sylius.com) - Symfony2支持的电子商务全栈平台。(L0, L1) `MIT` `PHP`
- [Thelia](https://thelia.net/) - 灵活的电子商务解决方案。（ L0 ， L1 ） `LGPL-3.0` `PHP`
- [Vendure](https://www.vendure.io) - 无头商务框架。（ L0 ， L1 ） `MIT` `Nodejs`
- [WooCommerce](https://woocommerce.com/) - 基于WordPress的电子商务解决方案。（ L0 ） `GPL-3.0` `PHP`


<a id="federated-identity--authentication"></a>
### Federated Identity & Authentication 联合身份与认证

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Federated identity](https://en.wikipedia.org/wiki/Federated_identity) and [authentication](https://en.wikipedia.org/wiki/Electronic_authentication) software.

**请访问 [awesome-sysadmin/Identity Management](https://github.com/awesome-foss/awesome-sysadmin#identity-management)**



<a id="feed-readers"></a>
### Feed Readers 订阅源阅读器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [news aggregator](https://en.wikipedia.org/wiki/News_aggregator), also termed a feed aggregator, feed reader, news reader, [RSS](https://en.wikipedia.org/wiki/RSS) reader, is an application that aggregates web content such as newspapers/blogs/vlogs/podcasts in one location for easy viewing.

- [Bubo Reader](https://github.com/georgemandis/bubo-rss) - 不合理的最小RSS源阅读器。（ L0 ） `MIT` `Nodejs`
- [CommaFeed](https://www.commafeed.com/) - 受Google Reader启发的RSS阅读器。(L0, L1) `Apache-2.0` `Java/Docker`
- [Feeds Fun](https://feeds.fun/) - 带有标签、评分和人工智能的新闻阅读器。（ L0 ） `BSD-3-Clause` `Python`
- [FreshRSS](https://freshrss.org/) - 自托管RSS订阅聚合器。(L0, L1) `AGPL-3.0` `PHP/Docker`
- [Fusion](https://github.com/0x2E/fusion) - 轻量级RSS聚合器和阅读器。 `MIT` `Go/Docker`
- [Goeland](https://github.com/slurdge/goeland) - 将任何RSS/Atom订阅源转换为精美的电子邮件摘要。 `MIT` `Go/Docker`
- [JARR](https://1pxsolidblack.pl/jarr-en.html) - JARR （ Just Another RSS Reader ）是一个基于网络的新闻聚合器和阅读器（ Newspipe的分支）。(L0, L1) `AGPL-3.0` `Docker/Python`
- [Kriss Feed](https://github.com/tontof/kriss_feed) - 简单而智能（或愚蠢）的Feed阅读器。 `CC0-1.0` `PHP`
- [Leed](https://github.com/LeedRSS/Leed) - 极简RSS聚合器（ Leed代表Light Feed ）。 `AGPL-3.0` `PHP`
- [Miniflux](https://miniflux.app/) - 极简主义新闻阅读器。（ L0 ） `Apache-2.0` `Go/deb/Docker`
- [NewsBlur](https://www.newsblur.com/) - 个人新闻阅读器，将人们聚集在一起谈论世界。旧乐器的新声音。（ L0 ） `MIT` `Python`
- [Newspipe](https://git.sr.ht/~cedric/newspipe) - 网络新闻阅读器。(L0) `AGPL-3.0` `Python`
- [reader](https://github.com/lemon24/reader) - Feed阅读器Web应用程序和库（因此您可以使用它来构建自己的） ，仅具有标准库和纯Python依赖项。 `BSD-3-Clause` `Python`
- [Readflow](https://readflow.app) - 具有现代界面和功能的轻量级新闻阅读器：全文搜索、自动分类、存档、离线支持、通知。（ L0 ） `AGPL-3.0` `Go/Docker`
- [RSS-Bridge](https://github.com/RSS-Bridge/rss-bridge) - 为没有RSS/ATOM Feed的网站生成RSS/ATOM Feed。 `Unlicense` `PHP/Docker`
- [RSS Monster](https://github.com/pietheinstrengholt/rssmonster) - 易于使用的基于Web的RSS聚合器和阅读器，兼容Fever API （ Google Reader的替代品）。 `MIT` `PHP`
- [RSS2EMail](https://github.com/rss2email/rss2email) - 获取RSS/Atom源并将新内容推送到任何电子邮件接收器，支持OPML。 `GPL-2.0` `Python/deb`
- [RSSHub](https://docs.rsshub.app) - 易于使用且可扩展的RSS订阅聚合器，能够从从社交媒体到大学部门的几乎所有内容生成RSS订阅。(L0, L1) `MIT` `Nodejs/Docker`
- [Selfoss](https://selfoss.aditu.de/) - 新的多用途RSS阅读器，实时流，混搭，聚合Web应用程序。（ L0 ） `GPL-3.0` `PHP`
- [Stringer](https://github.com/stringer-rss/stringer) - 正在进行的工作，反社会RSS阅读器。 `MIT` `Ruby`
- [Tiny Tiny RSS](https://tt-rss.org) - 基于Web的新闻订阅（ RSS/Atom ）阅读器和聚合器。（ L0 ） `GPL-3.0` `Docker/PHP`
- [TinyFeed](https://feed.lovergne.dev/) - 使用简单的CLI从源集合生成静态HTML页面。(L0, L1) `MIT` `Go/Docker`
- [Upvote RSS](https://www.upvote-rss.com/) `⚠` - 从Reddit、Hacker News、Lemmy、Mbin等生成丰富的RSS订阅源。(L0, L1) `MIT` `Docker/PHP`
- [Yarr](https://github.com/nkanaev/yarr) - Yarr （另一个RSS阅读器）是一个基于Web的Feed聚合器，既可以用作桌面应用程序，也可以用作个人服务器。 `MIT` `Go`


<a id="file-transfer--synchronization"></a>
### File Transfer & Synchronization 文件传输与同步

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[File transfer](https://en.wikipedia.org/wiki/File_transfer), [sharing](https://en.wikipedia.org/wiki/File_sharing) and [synchronization software](https://en.wikipedia.org/wiki/File_synchronization) software.

_Related: [Groupware 群件](#groupware)_

- [bewCloud](https://bewcloud.com) - 文件共享+同步、备注和照片（替代Nextcloud和ownCloud的RSS阅读器）。(L0, L1) `AGPL-3.0` `Docker`
- [Cloudreve](https://cloudreve.org/) - 文件管理和共享系统，支持多个存储提供商。(L0, L1) `GPL-3.0` `Docker/Go`
- [Git Annex](https://git-annex.branchable.com/) - 计算机、服务器、外部驱动器之间的文件同步。（ L0 ） `GPL-3.0` `Haskell`
- [Kinto](https://kinto.readthedocs.org) - 具有同步和共享功能的极简JSON存储服务。（ L0 ） `Apache-2.0` `Python`
- [Nextcloud](https://nextcloud.com/) - 根据您的需要，从任何设备访问和共享您的文件、日历、通讯录、邮件等。（ L0、L1、L2 ） `AGPL-3.0` `PHP/deb`
- [OpenCloud](https://docs.opencloud.eu/) - 文件共享和协作平台。（ L0 ） `Apache-2.0` `Docker/Go/Nodejs`
- [OpenSSH SFTP server](https://www.openssh.com/) - 安全文件传输程序。（ L0 ） `BSD-2-Clause` `C/deb`
- [ownCloud](https://owncloud.org/) - 用于保存、同步、查看、编辑和共享文件、日历、通讯簿等的一体化解决方案。(L0, L1) `AGPL-3.0` `PHP/Docker/deb`
- [Peergos](https://peergos.org) - 安全和私密的在线空间，您可以在其中存储、共享和查看您的照片、视频、音乐和文档。还包括日历、新闻订阅、任务列表、聊天和电子邮件客户端。（ L0 ） `AGPL-3.0` `Java`
- [Puter](https://puter.com/) - 基于Web的操作系统，功能丰富，速度极快，可扩展性强。(L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [Pydio](https://pydio.com/) - 将任何Web服务器转变为强大的文件管理系统和主流云存储提供商的替代品。(L0, L1) `AGPL-3.0` `Go`
- [Samba](https://www.samba.org/) - 适用于Linux和Unix的标准Windows互操作性程序套件。它使用SMB/CIFS协议为所有客户端提供安全、稳定和快速的文件和打印服务。（ L0 ） `GPL-3.0` `C`
- [Seafile](https://www.seafile.com/en/home/) - 团队和组织的文件托管和共享解决方案。(L0) `GPL-2.0/GPL-3.0/AGPL-3.0/Apache-2.0` `C`
- [Sync-in](https://sync-in.com) - 使用实时编辑、权限管理和桌面/CLI客户端进行文件存储、同步、共享和协作。（ L0、L1、L2 ） `AGPL-3.0` `Nodejs/Docker`
- [Syncthing](https://syncthing.net/) - 对等文件同步工具。（ L0 ） `MPL-2.0` `Go/Docker/deb`
- [Unison](https://www.cis.upenn.edu/~bcpierce/unison/) - 适用于OSX、Unix和Windows的文件同步工具。（ L0 ） `GPL-3.0` `deb/OCaml`


<a id="file-transfer---distributed-filesystems"></a>
### File Transfer - Distributed Filesystems 文件传输 - 分布式文件系统

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Network distributed filesystems.

**请访问 [awesome-sysadmin/Distributed Filesystems](https://github.com/awesome-foss/awesome-sysadmin#distributed-filesystems)**



<a id="file-transfer---object-storage--file-servers"></a>
### File Transfer - Object Storage & File Servers 文件传输 - 对象存储与文件服务器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Object storage](https://en.wikipedia.org/wiki/Object_storage) is a computer data storage that manages data as objects, as opposed to other storage architectures like file systems which manages data as a file hierarchy, and block storage which manages data as blocks within sectors and tracks.

- [GarageHQ](https://garagehq.deuxfleurs.fr/) - 地理分布式、兼容S3的存储服务，可以满足许多需求。（ L0 ） `AGPL-3.0` `Docker/Rust`
- [Harbor](https://goharbor.io/) - 云原生映像注册表，用于存储、标记和扫描内容。(L0) `Apache-2.0` `Docker/K8S`
- [SeaweedFS](https://github.com/seaweedfs/seaweedfs) - 分布式文件系统支持WebDAV、S3 API、FUSE挂载、HDFS等，针对大量小文件进行了优化，易于添加容量。 `Apache-2.0` `Go`
- [Zenko CloudServer](https://www.zenko.io/cloudserver) - 在多个云（包括Azure和Google ）的前端和后端存储功能上实施Amazon S3协议。（ L0 ） `Apache-2.0` `Docker/Nodejs`
- [ZOT OCI Registry](https://zotregistry.dev) - 生产就绪的供应商中立OCI原生容器映像注册表。(L0, L1) `Apache-2.0` `Go/Docker`


<a id="file-transfer---peer-to-peer-filesharing"></a>
### File Transfer - Peer-to-peer Filesharing 文件传输 - 点对点文件共享

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Peer-to-peer file sharing](https://en.wikipedia.org/wiki/Peer-to-peer_file_sharing) is the distribution and [sharing](https://en.wikipedia.org/wiki/File_sharing) of digital media using [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) (P2P) networking technology.

- [bittorrent-tracker](https://webtorrent.io/) - 简单、强大的BitTorrent跟踪器（客户端和服务器）实现。（ L0 ） `MIT` `Nodejs`
- [Deluge](https://deluge-torrent.org/) - 轻量级、跨平台的BitTorrent客户端。（ L0 ） `GPL-3.0` `Python/deb`
- [PrivyDrop](https://www.privydrop.app) - 基于WebRTC的简单易用、断点可恢复的对等文本、图像和文件传输工具。（ L0 ） `MIT` `Docker/Nodejs`
- [qBittorrent](https://www.qbittorrent.org/) - 免费的跨平台BitTorrent客户端，具有功能丰富的远程访问Web UI。（ L0 ） `GPL-2.0` `C++`
- [slskd](https://github.com/slskd/slskd) `⚠` - 适用于Soulseek文件共享网络的现代客户端-服务器应用程序。 `AGPL-3.0` `Docker/C#`
- [Transmission](https://transmissionbt.com/) - 快速、简单、免费的BitTorrent客户端。（ L0 ） `GPL-3.0` `C++/deb`
- [Webtor](https://github.com/webtor-io/self-hosted) - 具有即时音频/视频流的基于Web的Torrent客户端。（ L0 ） `MIT` `Docker`


<a id="file-transfer---single-click--drag-n-drop-upload"></a>
### File Transfer - Single-click & Drag-n-drop Upload 文件传输 - 一键与拖拽上传

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Simplified file servers for sharing of one-time/short-lived/temporary files, providing single-click or [drag-and-drop](https://en.wikipedia.org/wiki/Drag_and_drop) upload functionality.

- [015](https://send.fudaoyuan.icu) - 临时文件共享平台。专注于提供一次性、临时的文件和文本上传、处理和共享服务。（ L0 ） `AGPL-3.0` `Docker`
- [Chibisafe](https://chibisafe.app) - 旨在易于使用和设置的文件上传服务。它接受文件，照片，文件，任何您想象的东西，并为您提供一个可共享的链接，供您发送给其他人。（ L0 ） `MIT` `Docker/Nodejs`
- [Digirecord](https://ladigitale.dev/digirecord/) - 录制和共享音频文件（法语文档）。（ L0 ） `AGPL-3.0` `Nodejs/PHP`
- [elixire](https://gitlab.com/elixire/elixire) - 简单但高级的截图上传和链接缩短服务。（ L0 ） `AGPL-3.0` `Python`
- [Files Sharing](https://github.com/axeloz/filesharing) - 基于唯一和临时链接的文件共享应用程序。 `GPL-3.0` `PHP/Docker`
- [Flare](https://github.com/FlintSH/Flare) - 支持ShareX、Flameshot和Spectacle的非浮动、现代和高度可配置的文件/屏幕截图保管库服务器。提供OCR搜索等功能。 `MIT` `Docker/Nodejs`
- [Gokapi](https://github.com/Forceu/gokapi) - 用于共享文件的轻量级服务器，在设置的下载量或天数后过期。与已停产的Firefox Send类似，不同之处在于只有管理员可以上传文件。 `GPL-3.0` `Go/Docker`
- [goploader](https://depado.github.io/goploader/) - 使用服务器端加密轻松共享文件，符合curl/httpie/wget标准。（ L0 ） `MIT` `Go`
- [GoSƐ](https://codeberg.org/stv0g/gose) - 专注于可扩展性和简单性的现代文件上传器。它仅依赖于S3存储后端，因此可以水平扩展，而无需额外的数据库或缓存。 `Apache-2.0` `Go/Docker`
- [Jirafeau](https://gitlab.com/jirafeau/Jirafeau) - 一键式文件共享项目。选择您的文件、上传并共享链接。就是这样。 `AGPL-3.0` `PHP/Docker`
- [OnionShare](https://github.com/onionshare/onionshare) - 安全地匿名共享任何大小的文件。 `GPL-3.0` `Python/deb`
- [PicoShare](https://github.com/mtlynch/picoshare) - 简约、易于托管的服务，用于共享图像和其他文件。（ L0 ） `AGPL-3.0` `Go/Docker`
- [PictShare](https://www.pictshare.net/) - 多语言图像托管服务，具有简单的调整大小和上传API。（ L0 ） `Apache-2.0` `PHP/Docker`
- [Pingvin Share X](https://github.com/smp46/pingvin-share-x) - 文件共享平台，支持登录、反向共享、共享到期、S3存储桶、高级身份验证、用于安全扫描的ClamAV等（ Pingvin Share分支）。 `BSD-2-Clause` `Docker/Nodejs`
- [Plik](https://github.com/root-gg/plik) - 可扩展且友好的临时文件上传系统。（ L0 ） `MIT` `Go/Docker`
- [ProjectSend](https://www.projectsend.org/) - 上传文件并将其分配给您创建的特定客户端。向您的客户提供对这些文件的访问权限。（ L0 ） `GPL-2.0` `PHP`
- [PsiTransfer](https://github.com/psi-4ward/psitransfer) - 简单的文件共享解决方案，具有强大的上传/下载简历和密码保护。 `BSD-2-Clause` `Nodejs`
- [QuickShare](https://ihexxa.github.io/quickshare.site/) - 不同设备之间快速简单的文件共享。（ L0 ） `LGPL-3.0` `Docker/Go`
- [Safebucket](https://docs.safebucket.io/) - 具有可插拔基础设施的文件共享平台，其中上传和下载直接在客户端和S3兼容存储之间进行。（ L0 ） `Apache-2.0` `Go/Docker`
- [sE2EEnd](https://github.com/sE2EEnd/sE2EEnd) - 端到端加密文件共享，具有密码保护、下载限制和自动过期功能，与Keycloak集成进行身份验证。 `AGPL-3.0` `Docker`
- [Sharry](https://github.com/eikek/sharry) - 在经过身份验证的用户和匿名用户之间（双向）通过互联网轻松共享文件，并可恢复上传和下载。 `GPL-3.0` `Scala/Java/deb/Docker`
- [Shifter](https://github.com/TobySuch/Shifter) - 简单的文件共享Web应用。 `MIT` `Docker`
- [Slink](https://docs.slinkapp.io/) - 旨在让用户完全控制其媒体共享体验的图像共享平台。（ L0 ） `AGPL-3.0` `Docker`
- [snowshare](https://github.com/TuroYT/snowshare) - 具有网址缩短、代码段共享和文件上传功能的文件和链接共享平台，具有可定制的过期时间、隐私设置和二维码。(L0) `CC0-1.0` `Nodejs/Docker`
- [transfer.sh](https://github.com/dutchcoders/transfer.sh) - 从命令行轻松共享文件。 `MIT` `Go`
- [Uguu](https://github.com/nokonoko/uguu) - 存储文件并在X时间后删除。 `MIT` `PHP`
- [XBackBone](https://xbackbone.app/) - 具有即时共享工具集成的简单、快速和轻量级的文件管理器，如ShareX。（ L0 ） `AGPL-3.0` `PHP/Docker`
- [Zipline](https://github.com/diced/zipline) - 轻量级、快速和可靠的文件共享服务器，常用于ShareX ，提供基于react的Web UI和FAST API。 `MIT` `Docker/Nodejs`


<a id="file-transfer---web-based-file-managers"></a>
### File Transfer - Web-based File Managers 文件传输 - 基于 Web 的文件管理器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Web-based [file managers](https://en.wikipedia.org/wiki/File_manager).

_Related: [Groupware 群件](#groupware)_

- [Apaxy](https://oupala.github.io/apaxy/) - 主题旨在增强浏览Web目录的体验，使用mod_autoindex Apache模块和一些CSS覆盖目录列表的默认样式。（ L0 ） `GPL-3.0` `Javascript`
- [ClyoCloud](https://clyo.cloud/) - 专为隐私、效率和美学而构建的个人云存储和媒体管理应用程序。（ L0 ） `AGPL-3.0` `Nodejs`
- [copyparty](https://github.com/9001/copyparty) - 便携式文件服务器，可在单个文件中加速可恢复上传、重复数据删除、WebDAV、FTP、zeroconf、媒体索引器、视频缩略图、音频转码和只写文件夹，没有强制依赖关系。（ L0 ） `MIT` `Python`
- [Directory Lister](https://www.directorylister.com/) - 简单的基于PHP的目录列表，列出目录及其所有子目录，并允许您在其中导航。(L0) `MIT` `PHP/Docker`
- [FileGator](https://filegator.io/) - 功能强大的多用户文件管理器，单页前端。(L0, L1) `MIT` `PHP/Docker`
- [FileRise](https://github.com/error311/FileRise) - 带有上传、标记、共享链接、库/表视图和浏览器内编辑器的Web文件管理器。(L0) `MIT` `Docker/PHP`
- [Filestash](https://www.filestash.app/) - Web文件管理器，可让您在任何位置管理数据： FTP、SFTP、WebDAV、Git、S3、Minio、Dropbox或Google云端硬盘。(L0, L1) `AGPL-3.0` `Docker`
- [IFM](https://github.com/misterunknown/ifm) - 单脚本文件管理器。 `MIT` `PHP`
- [mikochi](https://github.com/zer0tonin/Mikochi) - 浏览远程文件夹、上传文件、删除、重命名、下载文件并将其流式传输到VLC/MPV。 `MIT` `Go/Docker/K8S`
- [miniserve](https://github.com/svenstaro/miniserve) - 用于通过HTTP提供文件和目录的CLI工具。 `MIT` `Rust`
- [ResourceSpace](https://www.resourcespace.com) - 简单、快速和自由的方式来组织您的数字资产。(L0, L1) `BSD-4-Clause` `PHP`
- [slcl](https://codeberg.org/xavidcr/slcl) - 简单轻便的网络云存储。 `AGPL-3.0` `C`
- [Surfer](https://git.cloudron.io/cloudron/surfer) - 使用webui管理文件的简单静态文件服务器。 `MIT` `Nodejs`
- [TagSpaces](https://www.tagspaces.org/) - 离线、跨平台的文件管理器和管理器，也可以用作笔记记录应用程序。应用程序的WebDAV版本可以安装在WebDAV服务器（如Nextcloud或ownCloud ）之上。(L0, L1) `AGPL-3.0` `Nodejs`
- [Tiny File Manager](https://tinyfilemanager.github.io) - PHP中的基于Web的文件管理器，简单，快速和小的文件管理器，具有单个文件。(L0, L1) `GPL-3.0` `PHP`


<a id="games"></a>
### Games 游戏

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Multiplayer game servers and [browser games](https://en.wikipedia.org/wiki/Browser_game).

_Related: [Games - Administrative Utilities & Control Panels 游戏 - 管理工具与控制面板](#games---administrative-utilities--control-panels)_

- [0 A.D.](https://play0ad.com/) - 古代战争的跨平台实时战略游戏。（ L0 ） `MIT/GPL-2.0/Zlib` `C++/C/deb`
- [A Dark Room](https://github.com/doublespeakgames/adarkroom) - 适用于浏览器的极简主义文字冒险游戏。(L0) `MPL-2.0` `Javascript`
- [DDraceNetwork](https://ddnet.org/) - DDRace的合作平台版本，这是Teeworlds修改版，具有独特的合作游戏玩法。（ L0 ） `Zlib` `C++`
- [Digibuzzer](https://digibuzzer.app/) - 在连接的蜂鸣器周围创建一个虚拟游戏室（法语文档）。(L0, L1) `AGPL-3.0` `Nodejs`
- [Hypersomnia](https://github.com/TeamHypersomnia/Hypersomnia) - 有竞争力的自上而下的射击游戏，将Counter-Strike与Hotline Miami相结合。在Linux、Windows、MacOS和Web上运行。（ L0 ） `AGPL-3.0` `C++/Docker`
- [Lila](https://lichess.org/) - 支持lichess.org的无广告国际象棋服务器，配备官方iOS和Android客户端应用程序。(L0) `AGPL-3.0` `Scala`
- [Luanti](https://www.luanti.org/) - Voxel游戏引擎（前身为Minetest ）。玩我们的众多游戏之一，根据您的喜好修改游戏，制作自己的游戏，或在多人游戏服务器上玩。（ L0 ） `LGPL-2.1/MIT/Zlib` `C++/Lua/deb`
- [Mindustry](https://mindustrygame.github.io/) - 类似Factorio的塔防游戏。建立生产链以收集更多资源，并建立复杂的设施。（ L0 ） `GPL-3.0` `Java`
- [MTA:SA](https://multitheftauto.com/) `⚠` - 将网络游戏功能添加到Rockstar North的侠盗猎车手系列游戏中，其中最初未找到此功能。（ L0 ） `GPL-3.0` `C++`
- [OpenTTD](https://www.openttd.org/) - 运输大亨模拟游戏。(L0, L1) `GPL-2.0` `C++/Docker`
- [piqueserver](https://github.com/piqueserver/piqueserver) - Openspades服务器，可破坏体素世界中的第一人称射击游戏。（ L0 ） `GPL-3.0` `Python/C++`
- [Posio](https://github.com/abrenaut/posio) - 地理多人游戏。 `MIT` `Python`
- [Razzia](https://github.com/Ralex91/Razzia) - 问答游戏平台，专为小型活动而设计（ Kahoot!的替代品）。 `MIT` `Nodejs/Docker`
- [Red Eclipse 2](https://www.redeclipse.net/) - 类似于虚幻锦标赛的竞技场第一人称射击游戏。（ L0 ） `Zlib/MIT/CC-BY-SA-4.0` `C/C++/deb`
- [Scribble.rs](https://github.com/scribble-rs/scribble.rs) - 基于Web的字典游戏。（ L0 ） `BSD-3-Clause` `Go/Docker`
- [Suroi](https://suroi.io/) - 2D战斗royale游戏灵感来自surviv.io。(L0, L1) `GPL-3.0` `Nodejs`
- [The Battle for Wesnoth](https://github.com/wesnoth/wesnoth) - 具有高幻想主题的回合制战术策略游戏，包括单人游戏和在线/热门多人战斗。 `GPL-2.0` `C++/deb`
- [Veloren](https://veloren.net/) - 多人角色扮演游戏。灵感来自立方体世界、塞尔达传说、矮人堡垒和《我的世界》。（ L0 ） `GPL-3.0` `Rust`
- [Zero-K](https://zero-k.info/) - Springrts引擎上的传统实时策略游戏，专注于通过地形操纵、物理和大量独特单位的玩家创造力-同时保持平衡以支持竞技游戏。（ L0 ） `GPL-2.0` `Lua`


<a id="games---administrative-utilities--control-panels"></a>
### Games - Administrative Utilities & Control Panels 游戏 - 管理工具与控制面板

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Utilities for managing game servers and game libraries.

_Related: [Games 游戏](#games)_

- [auto-mcs](https://www.auto-mcs.com) - 跨平台Minecraft服务器管理器。(L0) `AGPL-3.0` `Python`
- [Calagopus](https://calagopus.com) - 现代游戏服务器管理面板。部署、监控和管理具有业界领先性能的Minecraft、Hytale和其他游戏服务器。（ L0 ） `MIT` `Rust/Docker/deb`
- [Crafty Controller](https://craftycontrol.com/) - Minecraft启动器和管理器，允许用户从用户友好的界面启动和管理Minecraft服务器。（ L0 ） `GPL-3.0` `Docker/Python`
- [Drop](https://droposs.org) - 游戏发行平台，专为高效发行和共享无DRM游戏而设计（ Steam、GameVault的替代品）。(L0, L1) `AGPL-3.0` `Docker`
- [EasyWI](https://easy-wi.com) - 允许您管理服务器守护进程（如游戏服务器）的Web界面。此外，它还为您提供CMS ，其中包括全自动游戏和语音服务器借用服务。（ L0 ） `GPL-3.0` `PHP/Shell`
- [GameAP](https://gameap.com/) - 用于在Linux和Windows上管理游戏服务器的游戏管理面板。（ L0、L1、L2 ） `MIT` `Go/Docker`
- [Gameyfin](https://gameyfin.org) - 具有自动扫描、网络访问、下载和插件支持的视频游戏库管理器。（ L0 ） `AGPL-3.0` `Docker`
- [Gaseous Server](https://github.com/gaseous-project/gaseous-server) `⚠` - 游戏ROM管理器，内置基于Web的仿真器，使用多个源来识别和提供元数据。 `AGPL-3.0` `Docker/.NET`
- [Lancache](https://lancache.net) `⚠` - 局域网派对游戏缓存变得简单。（ L0 ） `MIT` `Docker/Shell`
- [LinuxGSM](https://linuxgsm.com/) - 用于在Linux上部署和管理专用游戏服务器的CLI工具：支持120多种游戏。（ L0 ） `MIT` `Shell`
- [Minus Games](https://accessory.github.io/minus_games_user_guide) - 在多个设备上同步游戏并保存文件。（ L0 ） `MIT` `Rust`
- [Ownfoil](https://github.com/a1ex4/ownfoil) - Nintendo Switch库管理器，具有自动管理任务（文件识别和组织、缺少更新/DLC ） ，通过商店定制和多用户身份验证，将您的库提供给Switch上的多个受支持客户端。 `AGPL-3.0` `Docker/Python`
- [Pelican Panel](https://pelican.dev/) - Web应用程序，可轻松管理游戏服务器，提供用户友好的界面，用于部署、配置和管理服务器、服务器监控工具和广泛的自定义选项（ Pterodactyl分支）。（ L0 ） `AGPL-3.0` `PHP/Docker`
- [PKVault](https://github.com/Chnapy/PKVault) - 集中式精灵宝可梦存储管理和Pokedex应用程序（ Pokémon Home的替代品）。（ L0 ） `GPL-3.0` `Docker`
- [Pterodactyl](https://pterodactyl.io/) - 游戏服务器的管理面板，为最终用户提供直观的用户界面。（ L0 ） `MIT` `PHP`
- [PufferPanel](https://www.pufferpanel.com/) - 专为小型网络和游戏服务器提供商设计的游戏服务器管理面板。（ L0 ） `Apache-2.0` `Go`
- [RetroArr](https://retroarr.app) `⚠` - 适用于PC和复古控制台的游戏库管理器，具有元数据抓取、索引器搜索、下载自动化和基于浏览器的仿真（ RomM的替代品）。（ L0 ） `MIT` `Docker/.NET`
- [Retrom](https://github.com/JMBeresford/retrom) - 私有云游戏库分发服务器+前端/启动器。 `GPL-3.0` `Docker/Rust`
- [RomM](https://romm.app/) `⚠` - ROM管理器，用于组织、丰富和玩复古游戏，支持400多个平台。(L0, L1) `AGPL-3.0` `Docker`
- [SourceBans++](https://sbpp.github.io/) - 在源引擎上运行的游戏的管理、封禁和通信管理系统。（ L0 ） `CC-BY-SA-4.0` `PHP`
- [Sunshine](https://app.lizardbyte.dev/Sunshine/) - Moonlight的远程游戏流主机，支持高达每秒120帧和4K分辨率。（ L0 ） `GPL-3.0` `C++/deb/Docker`


<a id="genealogy"></a>
### Genealogy 家谱

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Genealogy software](https://en.wikipedia.org/wiki/Genealogy_software) used to record, organize, and publish genealogical data.

- [Genea.app](https://www.genea.app/) - 家谱工具的设计考虑到隐私，任何人都可以使用它来创作或编辑他们的家谱。数据以GEDCOM格式存储，所有处理均在浏览器中完成。（ L0 ） `MIT` `Javascript`
- [Genealogy](https://genealogy.kreaweb.be/) - 记录家庭成员及其关系，并建立家谱。(L0, L1) `MIT` `PHP`
- [GeneWeb](https://github.com/geneweb/geneweb/wiki) - 可以离线使用或作为Web服务使用的家谱软件。（ L0 ） `GPL-2.0` `OCaml`
- [Gramps Web](https://www.grampsweb.org/) - 用于协作家谱的Web应用程序，基于家谱桌面应用程序Gramps并可与之互操作。(L0, L1) `AGPL-3.0` `Docker`
- [webtrees](https://www.webtrees.net) - 网络上领先的在线协作家谱应用程序。(L0, L1) `GPL-3.0` `PHP`


<a id="generative-artificial-intelligence-genai"></a>
### Generative Artificial Intelligence (GenAI) 生成式人工智能（GenAI）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Generative Artificial Intelligence (GenAI)](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) is a subset of [artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) that uses generative models to produce text, images, videos, or other forms of data.

- [Agenta](https://agenta.ai/) - LLMOps平台，用于及时管理、LLM评估和可观察性。通过协同提示工程构建、评估和监控生产级LLM应用程序。(L0) `MIT` `Docker`
- [AnythingLLM](https://anythingllm.com/) - 内置RAG、AI代理、无代码代理构建器、MCP兼容性等的一体化桌面和Docker AI应用程序。（ L0 ） `MIT` `Nodejs/Docker`
- [GoModel](https://gomodel.enterpilot.io/) - 用Go编写的人工智能网关，具有适用于多个LLM提供商的统一OpenAI兼容API、美元成本跟踪、预算、使用情况分析、护栏、缓存和管理仪表板。（ L0 ） `MIT` `Go/Docker`
- [Khoj](https://khoj.dev/) - 你的AI第二大脑。从网页或文档中获取答案。构建自定义代理、安排自动化、进行深入研究。将任何在线或本地法学硕士转变为您的个人自主人工智能。(L0, L1) `AGPL-3.0` `Python/Docker`
- [LibreChat](https://www.librechat.ai) `⚠` - 增强的ChatGPT兼容AI聊天界面，支持多个AI提供商，支持多用户身份验证、消息搜索和插件。(L0, L1) `MIT` `Nodejs/Docker`
- [LLM Harbor](https://github.com/av/harbor) - 容器化LLM工具包。通过简洁的CLI运行LLM后端、API、前端和其他服务。 `Apache-2.0` `Docker/Shell`
- [LLMKube](https://llmkube.com) - Kubernetes运算符，用于可插拔运行时（ llama.cpp、vLLM、TGI、Ollama、vllm-swift ）、多GPU分片、NVIDIA CUDA + Apple Silicon Metal支持和OpenAI兼容API的LLM推理。（ L0 ） `Apache-2.0` `Go/Docker/K8S`
- [Local Deep Research](https://github.com/LearningCircuit/local-deep-research) - 基于人工智能的深度研究工具，具有多源搜索（ arXiv、PubMed、web ）、PDF文本提取和加密本地存储。 `MIT` `Docker/Python`
- [LocalAI](https://localai.io/) - 在本地运行您的AI模型并生成图像和音频（替代OpenAI和Claude ）。(L0, L1) `MIT` `Docker/K8S`
- [Ollama](https://ollama.com/) - 开始使用Llama 3.3、DeepSeek-R1、Phi-4、Gemma 3和其他大型语言模型。（ L0 ） `MIT` `Docker/Python`
- [Onyx Community Edition](https://onyx.app) - 适用于任何LLM的聊天UI。它配备了高级功能，如代理、网络搜索、RAG、MCP、深入研究、40多个知识来源的连接器等。（ L0 ） `MIT` `Docker/K8S`
- [Open-WebUI](https://openwebui.com) - 用户友好的AI界面，支持Ollama、OpenAI API。（ L0 ） `BSD-3-Clause` `Docker/Python`
- [Vane](https://github.com/ItzCrazyKns/Vane) - 人工智能驱动的搜索引擎（ Perplexity AI的替代品）。 `MIT` `Docker`


<a id="groupware"></a>
### Groupware 群件

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Collaborative software or [groupware](https://en.wikipedia.org/wiki/Collaborative_software) is designed to help people working on a common task to attain their goals. Groupware often regroups multiple services such as file sharing, calendar/events management, appointment scheduling, address books... in a single, integrated application.

_Related: [Booking and Scheduling 预订与排程](#booking-and-scheduling)_

- [Citadel](https://www.citadel.org/) - 群件包括电子邮件、日历/日程安排、通讯簿、论坛、邮件列表、即时消息、维基和博客引擎、RSS聚合等。（ L0 ） `GPL-3.0` `C/Docker/Shell`
- [Colanode](https://colanode.com) - 具有实时消息传递、富文本页面、文件管理和动态数据库的协作套件-专为离线工作而构建（可替代Slack、Notion ）。（ L0 ） `Apache-2.0` `K8S/Docker`
- [Cozy Cloud](https://cozy.io/) - 个人云，您可以在其中管理和同步文件、笔记、联系人、密码和文档。(L0, L1) `GPL-3.0` `Nodejs`
- [Digipad](https://digipad.app/) - 用于创建协作数字记事本的在线应用程序（法语文档）。（ L0 ） `AGPL-3.0` `Nodejs`
- [Digistorm](https://digistorm.app/) - 创建协作调查、测验、头脑风暴和文字云（法语文档）。(L0, L1) `AGPL-3.0` `Nodejs`
- [Digiwall](https://digiwall.app/) - 为面对面或远程工作创建多媒体协作墙（法语文档）。（ L0 ） `AGPL-3.0` `Nodejs`
- [egroupware](https://www.egroupware.org/) - 软件套件包括日历、地址簿、记事本、项目管理工具、客户关系管理工具(CRM)、知识管理工具、wiki和CMS。(L0) `GPL-2.0` `PHP`
- [Group Office](https://www.group-office.com) - 企业CRM和群件工具。与同事和客户在线共享项目、日历、文件和电子邮件。（ L0 ） `AGPL-3.0` `PHP`
- [Openmeetings](https://openmeetings.apache.org/index.html) - 视频会议、即时消息、白板、协作文档编辑和其他群件工具，使用Red5流媒体服务器的API功能进行远程处理和流式处理。（ L0 ） `Apache-2.0` `Java`
- [SOGo](https://www.sogo.nu/) - SOGo提供多种方式访问日历和消息数据。CalDAV、CardDAV、GroupDAV以及ActiveSync ，包括本机Outlook兼容性和Web界面。(L0, L1) `LGPL-2.1` `Objective-C`
- [Tine](https://www.tine-groupware.de/) - 用于公司和组织中数字协作的软件。从强大的群件功能到巧妙的附加组件， TINE结合了所有功能，使日常团队协作更加轻松。（ L0 ） `AGPL-3.0` `Docker`
- [Tracim](https://github.com/tracim/tracim) - 团队协作的协作平台：文件、线程、备注、议程等 `AGPL-3.0/LGPL-3.0/MIT` `Python`
- [Zimbra Collaboration](https://www.zimbra.com/) - 电子邮件、日历、带Web界面的协作服务器和大量集成。（ L0 ） `GPL-2.0/CPAL-1.0` `Java`


<a id="health-and-fitness"></a>
### Health and Fitness 健康与健身

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Medical](https://en.wikipedia.org/wiki/Medical_software), [Health](https://en.wikipedia.org/wiki/Health_information_technology) and [Fitness](https://en.wikipedia.org/wiki/Fitness_tracker) software.

- [Endurain](https://docs.endurain.com/) - 健身追踪服务旨在让用户完全控制其数据和托管环境。(L0) `AGPL-3.0` `Docker`
- [FitTrackee](https://docs.fittrackee.org/) - 简单的锻炼/活动跟踪器。（ L0 ） `AGPL-3.0` `Python/Docker`
- [Mere Medical](https://meremedical.co/) `⚠` - 从Epic MyChart、Cerner和OnPatient患者门户在一个地方管理您的所有医疗记录。以隐私为中心，以线下为先。（ L0、L1 ） `GPL-3.0` `Docker/Nodejs`
- [NutriTrace](https://traceapps.github.io/docs/) - 营养和饮食跟踪器，带有条形码扫描、可穿戴集成（ Fitbit、Withings、Garmin、Health Connect ）、自适应卡路里目标、多用户共享和内置AI助手（ MyFitnessPal、Cronometer的替代品）。（ L0 ） `AGPL-3.0` `Docker`
- [OpenELIS Global](https://openelis-global.org) - 临床、公共卫生、环境和病媒监测实验室的实验室信息系统（ LIS/LIMS ）。FHIR原生，带有分析仪集成（ ASTM/HL7 ）、质量控制和国家级报告。(L0, L1) `MPL-2.0` `Java/Docker`
- [OpenEMR](https://www.open-emr.org/) - 电子健康记录和医疗实践管理解决方案。(L0, L1) `GPL-3.0` `PHP/Docker`
- [wger](https://wger.de/) - 基于网络的个人锻炼、健身和体重记录器/跟踪器。它还可以用作简单的健身房管理实用程序，并提供完整的REST API。(L0, L1) `AGPL-3.0` `Python/Docker`


<a id="human-resources-management-hrm"></a>
### Human Resources Management (HRM) 人力资源管理（HRM）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [human resources management system](https://en.wikipedia.org/wiki/Human_resource_management_system) combines a number of systems and processes to ensure the easy management of [human resources](https://en.wikipedia.org/wiki/Human_resources), business processes and data.

- [admidio](https://www.admidio.org/) - 适用于组织和团体网站的用户管理系统。系统具有灵活的角色模型，因此可以反映组织的结构和权限。(L0, L1) `GPL-2.0` `PHP/Docker`
- [Frappe HR](https://frappe.io/hr) - 完整的人力资源管理系统解决方案，包含超过13个不同的模块，从员工管理、入职、休假到薪资、税务等。(L0) `GPL-3.0` `Docker/Python/Nodejs`
- [MintHCM](https://minthcm.org/) - 基于两个流行的知名业务应用程序SugarCRM Community Edition和SuiteCRM的人力资本管理工具。(L0) `AGPL-3.0` `PHP`


<a id="identity-management"></a>
### Identity Management 身份管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Identity management](https://en.wikipedia.org/wiki/Identity_management) (IdM), also known as identity and access management (IAM or IdAM), is a framework of policies and technologies to ensure that the right users have the appropriate access to technology resources.

**请访问 [awesome-sysadmin/Identity Management](https://github.com/awesome-foss/awesome-sysadmin#identity-management)**



<a id="internet-of-things-iot"></a>
### Internet of Things (IoT) 物联网（IoT）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Internet of Things](https://en.wikipedia.org/wiki/Internet_of_things) describes physical objects with sensors, processing ability, software, and other technologies that connect and exchange data with other devices over the Internet.

_Related: [Automation 自动化](#automation)_

- [Domoticz](https://www.domoticz.com/) - 家庭自动化系统，可让您监控和配置各种设备，如：灯、开关、各种传感器/仪表，如温度、雨、风、紫外线、Electra、燃气、水等。(L0, L1) `GPL-3.0` `C/C++/Docker/Shell`
- [EMQX](https://www.emqx.com/) - 可扩展的MQTT代理。在一个集群中连接1亿多个物联网设备，以1ms的延迟以100万msg/s的吞吐量移动和处理实时物联网数据。(L0, L1) `Apache-2.0` `Docker/Erlang`
- [evcc](https://evcc.io/) - 可扩展电动汽车充电控制器和家庭能源管理系统。（ L0 ） `MIT` `deb/Docker/Go`
- [FHEM](https://fhem.de/fhem.html) - 自动执行家中的常见任务，如开关灯和供暖。它还可用于记录温度或功耗等事件。您可以通过网络或智能手机前端、telnet或TCP/IP直接控制它。（ L0 ） `GPL-3.0` `Perl`
- [FlowForge](https://flowforge.com/) - 以可靠、可扩展和安全的方式部署Node-RED应用程序。FlowForge平台为Node-RED开发团队提供DevOps功能。（ L0 ） `Apache-2.0` `Nodejs/Docker/K8S`
- [FMD Server](https://fmd-foss.org) - 服务器与FMD （查找我的设备） Android应用程序进行通信，以定位和控制您的设备。(L0, L1) `GPL-3.0` `Docker/Go`
- [Gladys](https://gladysassistant.com/) - 隐私至上的家庭助理。（ L0 ） `Apache-2.0` `Nodejs/Docker`
- [Home Assistant](https://home-assistant.io/) - 家庭自动化平台。（ L0、L1 ） `Apache-2.0` `Python/Docker`
- [ioBroker](https://www.iobroker.net/) - 物联网集成平台，专注于楼宇自动化、智能计量、环境辅助生活、过程自动化、可视化和数据记录。（ L0 ） `MIT` `Nodejs`
- [LHA](https://github.com/javalikescript/lha) - 使用Blockly、HTML或Lua完全可扩展的轻型家庭自动化应用程序。它包括ConBee、Philips Hue或Z-Wave JS等扩展。 `MIT` `Lua`
- [Node RED](https://nodered.org/) - 基于浏览器的流编辑器，可帮助您连接硬件设备、API和在线服务，以创建物联网解决方案。(L0) `Apache-2.0` `Nodejs/Docker`
- [Onloc](https://onloc.app) - 实时跟踪并分享您的位置信息。控制和锁定被盗或丢失的手机。(L0, L1) `AGPL-3.0` `Docker`
- [openHAB](https://www.openhab.org) - 适用于家庭自动化的供应商和技术不可知软件。（ L0 ） `EPL-2.0` `Java`
- [OpenRemote](https://openremote.io) - 物联网资产管理、流程规则和规则、数据可视化、边缘网关。(L0, L1) `AGPL-3.0` `Java`
- [polluSensWeb](https://wespeakenglish.github.io/polluSensWeb/) - 基于Web的串行接口和图表工具，用于可视化和记录来自UART污染传感器（ PM2.5、VOC等）的数据。具有实时数据采集、动态图表、CSV导出和webhook集成。（ L0、L1、L2 ） `MIT` `Javascript`
- [SIP Irrigation Control](https://dan-in-ca.github.io/SIP/) - 喷洒器/灌溉控制软件。（ L0 ） `GPL-3.0` `Python`
- [SOLECTRUS](https://solectrus.de) - 光伏仪表板，通过成本和节约计算显示能源生产和消耗。(L0, L1) `AGPL-3.0` `Docker`
- [Tasmota](https://tasmota.com) - ESP设备的固件。通过快速设置和更新实现完全本地控制。使用MQTT、Web UI、HTTP或串行进行控制。使用计时器、规则或脚本实现自动化。与家庭自动化解决方案集成。（ L0 ） `GPL-3.0` `C/C++`
- [Thingsboard](https://thingsboard.io/) - 物联网平台-设备管理、数据收集、处理和可视化。(L0, L1) `Apache-2.0` `Java/Docker/K8S`
- [WebThings Gateway](https://webthings.io/gateway/) - 实施物联网，包括WebThings网关和WebThings框架。（ L0 ） `MPL-2.0` `Nodejs`


<a id="inventory-management"></a>
### Inventory Management 库存管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Inventory management software](https://en.wikipedia.org/wiki/Inventory_management_software).

_Related: [Money, Budgeting & Management 金钱、预算与管理](#money-budgeting--management), [Resource Planning 资源规划](#resource-planning)_

_See also: [awesome-sysadmin/IT Asset Management](https://github.com/awesome-foss/awesome-sysadmin#it-asset-management)_

- [Cannery](https://cannery.app) - 枪支和弹药跟踪器应用程序。（ L0 ） `AGPL-3.0` `Docker`
- [CellarBoss](https://cellarboss.org) - 葡萄酒库存管理系统。（ L0 ） `GPL-3.0` `Docker/Nodejs`
- [DVinyl](https://github.com/Kyonew/DVinyl) `⚠` - 物理媒体（黑胶唱片、CD、磁带、书籍、电影和视频游戏）的现代收藏管理器。 `MIT` `Nodejs/Docker`
- [HomeBox (SysAdminsMedia)](https://homebox.software/) - 为家庭用户构建的库存和组织系统。(L0, L1) `AGPL-3.0` `Docker/Go`
- [Inventaire](https://inventaire.io/welcome) - 协作资源映射器项目，同时仅专注于探索使用维基数据和ISBN进行书籍映射。（ L0 ） `AGPL-3.0` `Nodejs`
- [Inventree](https://docs.inventree.org/en/latest/) - 库存管理系统，提供直观的零件管理和库存控制。(L0, L1) `MIT` `Python`
- [Open QuarterMaster](https://openquartermaster.com/) - 强大的库存管理系统，旨在实现灵活性和可扩展性。（ L0 ） `GPL-3.0` `deb/Docker`
- [Part-DB](https://docs.part-db.de/) - 您的电子元件的库存管理系统。(L0, L1) `AGPL-3.0` `Docker/PHP/Nodejs`
- [Spoolman](https://github.com/Donkie/Spoolman) - 跟踪您的3D打印长丝卷轴库存。 `MIT` `Docker/Python`


<a id="knowledge-management-tools"></a>
### Knowledge Management Tools 知识管理工具

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Knowledge management](https://en.wikipedia.org/wiki/Knowledge_management) is the collection of methods relating to creating, sharing, using and managing the knowledge and information.

_Related: [Note-taking & Editors 笔记与编辑器](#note-taking--editors), [Wikis 维基](#wikis), [Database Management 数据库管理](#database-management)_

- [Atomic Server](https://atomicserver.eu/) - 知识图数据库，包含文档（类似于Notion ）、表格、搜索和强大的链接数据API。轻量级，非常快，没有运行时依赖。(L0, L1) `MIT` `Docker/Rust`
- [Digimindmap](https://ladigitale.dev/digimindmap/#/) - 创建简单的思维导图（法语文档）。(L0, L1) `AGPL-3.0` `Nodejs/PHP`
- [LibreKB](https://librekb.com/) - 基于Web的知识库解决方案。一个简单的Web应用程序，它运行在几乎所有带有PHP和MySQL的Web服务器或托管提供商上。（ L0 ） `GPL-3.0` `PHP`
- [Marmot](https://marmotdata.io) - 用于发现和组织跨堆栈的数据资产的数据目录，包括数据库、API、消息队列和管道。(L0, L1) `MIT` `Docker`
- [memEx](https://memex-app.shibao.dev) - 结构化的个人知识库，灵感来自zettlekasten和组织模式。（ L0 ） `AGPL-3.0` `Docker`
- [SiYuan](https://b3log.org/siyuan/) - 隐私为先的个人知识管理软件，以打字稿和golang编写。（ L0 ） `AGPL-3.0` `Docker/Go`
- [TeamMapper](https://github.com/b310-digital/teammapper) - 出租房源并创建自己的思维导图。与您的团队分享您的思维导图会话，并在思维导图上进行实时协作。(L0) `MIT` `Docker/Nodejs`


<a id="learning-and-courses"></a>
### Learning and Courses 学习与课程

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Tools and software to help with education and learning.

- [Canvas LMS](https://www.instructure.com/canvas/) - 学习管理系统（ LMS ）正在彻底改变我们的教育方式。（ L0 ） `AGPL-3.0` `Ruby`
- [Chamilo LMS](https://chamilo.org/) - 创建一个在线或半在线培训的虚拟校园。（ L0 ） `GPL-3.0` `PHP`
- [Digiscreen](https://ladigitale.dev/digiscreen/) - 交互式白板/教室壁纸，亲自或远程（法语文件）。(L0, L1) `AGPL-3.0` `Nodejs/PHP`
- [Digitools](https://ladigitale.dev/digitools) - 一套简单的工具，可亲自或远程伴随课程动画（法语文档）。(L0, L1) `AGPL-3.0` `PHP`
- [edX](https://www.edx.org/) - 为edX.org网站提供支持的在线学习平台。（ L0 ） `AGPL-3.0` `Python`
- [Gibbon](https://gibbonedu.org/) - 灵活的学校管理平台，旨在为教师、学生、家长和领导者提供更美好的生活。（ L0 ） `GPL-3.0` `PHP`
- [Helium](https://www.heliumedu.com) - 具有智能通知和多设备同步功能的课堂、作业、成绩和笔记的颜色编码学生规划器。(L0, L1) `MIT` `Python/Docker`
- [ILIAS](https://www.ilias.de) - 学习管理系统，可以处理您扔给它的任何事情。(L0, L1) `GPL-3.0` `PHP`
- [INGInious](https://inginious.org/?lang=en) - 智能评分器，可对学生编写的代码进行安全的自动化测试。(L0, L1) `AGPL-3.0` `Python/Docker`
- [Moodle](https://moodle.org/) - 学习和课程平台，拥有全球最大的社区之一。(L0, L1) `GPL-3.0` `PHP`
- [Open eClass](https://www.openeclass.org/) - 先进的在线学习解决方案，可以增强教学和学习过程。(L0, L1) `GPL-2.0` `PHP`
- [OpenOLAT](https://www.openolat.com/?lang=en) - 教学、教育、评估和沟通的学习管理系统。(L0, L1) `Apache-2.0` `Java`
- [QST](https://qstonline.org) - 在线评估软件。从手机上的快速测验到大规模、高风险、监控桌面测试，简单、安全和经济。(L0, L1) `GPL-2.0` `Perl`
- [RELATE](https://documen.tician.de/relate/) - 包含以下功能的课件包：灵活的规则、统计、多课程支持、课堂日历。（ L0 ） `MIT` `Python`
- [RosarioSIS](https://www.rosariosis.org/) - 用于学校管理的学生信息系统。包括学生人口统计、成绩、日程安排、出勤、学生账单、纪律和食品服务模块。(L0, L1) `GPL-2.0` `PHP`


<a id="manufacturing"></a>
### Manufacturing 制造

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Software to manage [3D printers](https://en.wikipedia.org/wiki/3D_printing), [CNC machines](https://en.wikipedia.org/wiki/Numerical_control) and other physical manufacturing tools.

- [CNCjs](https://cnc.js.org/) - 运行Grbl、Smoothieware或TinyG的数控铣削控制器的Web界面。（ L0 ） `MIT` `Nodejs`
- [Fluidd](https://docs.fluidd.xyz/) - 3D打印机固件Klipper的轻量级和响应式用户界面。（ L0 ） `GPL-3.0` `Docker/Nodejs`
- [LinuxCNC](https://www.linuxcnc.org/) - 基于Linux的数控机床控制器。它可以驱动铣床、车床、3D打印机、激光切割机、等离子切割机、机器人手臂、六脚架等。（ L0 ） `GPL-2.0/LGPL-3.0` `C/deb`
- [Mainsail](https://docs.mainsail.xyz/) - Klipper 3D打印机固件的现代化响应式用户界面。从任何地方、任何设备控制和监控您的打印机。(L0) `GPL-3.0` `Docker/Python`
- [Manyfold](https://manyfold.app) - 用于3D打印文件的数字资产管理器； STL、OBJ、3MF等。（ L0 ） `MIT` `Docker`
- [Octoprint](https://octoprint.org/) - 用于控制消费者3D打印机的流畅Web界面。（ L0 ） `AGPL-3.0` `Docker/Python`
- [Orkyo Community](https://orkyo.com) - 制造团队的生产调度—运行作业的机器、人员和工具的一个计划。(L0, L1) `AGPL-3.0` `C#/Docker`


<a id="maps-and-global-positioning-system-gps"></a>
### Maps and Global Positioning System (GPS) 地图与全球定位系统（GPS）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Maps](https://en.wikipedia.org/wiki/Map), [cartography](https://en.wikipedia.org/wiki/Cartography), [GIS](https://en.wikipedia.org/wiki/Geographic_information_system) and [GPS](https://en.wikipedia.org/wiki/Global_Positioning_System) software.

_Related: [Travel Organization 旅行规划](#travel-organization)_

_See also: [awesome-openstreetmap](https://github.com/osmlab/awesome-openstreetmap), [awesome-gis](https://github.com/sshuair/awesome-gis)_

- [AdventureLog](https://adventurelog.app) - 差旅追踪器和差旅管理员。(L0, L1) `GPL-3.0` `Docker`
- [AirTrail](https://airtrail.johan.ohly.dk) - 个人航班跟踪系统。（ L0 ） `GPL-3.0` `Docker/Nodejs`
- [Bicimon](https://github.com/knrdl/bicimon) - 自行车速度计作为渐进式网络应用程序。(L0) `MIT` `Javascript`
- [Dawarich](https://dawarich.app/) - 可视化您的位置历史记录，跟踪您的移动，并通过完全隐私和控制来分析您的旅行模式（ Google时间轴的替代品，又名Google位置历史记录）。（ L0 ） `AGPL-3.0` `Docker`
- [Geo2tz](https://github.com/noandrea/geo2tz) - 从地理坐标(lat, lon)获取时区。 `MIT` `Go/Docker`
- [GraphHopper](https://graphhopper.com/) - 使用OpenStreetMap的快速路由库和服务器。（ L0 ） `Apache-2.0` `Java`
- [NextGIS Web](https://nextgis.com/nextgis-web/) - 用于地理空间数据管理、Web地图发布和以QGIS为中心的协作工作流程的Web GIS服务器。(L0, L1) `GPL-3.0` `Docker`
- [Nominatim](https://nominatim.org/) - 用于OpenStreetMap数据上的地理编码（地址- >坐标）和反向地理编码（坐标- >地址）的服务器应用程序。（ L0 ） `GPL-2.0` `C`
- [Open Source Routing Machine (OSRM)](http://project-osrm.org/) - 高性能路由引擎，设计用于在OpenStreetMap数据上运行，并提供HTTP API、C + +库接口和Nodejs包装器。(L0, L1) `BSD-2-Clause` `C++`
- [OpenRouteService](https://openrouteservice.org/) - 路线服务，包括路线、等时线、时间-距离矩阵、路线优化等。(L0, L1) `GPL-3.0` `Docker/Java`
- [OpenStreetMap](https://www.openstreetmap.org/) - 创建免费可编辑世界地图的合作项目。(L0, L1) `GPL-2.0` `Ruby`
- [OpenTripPlanner](https://www.opentripplanner.org/) - 基于OpenStreetMap数据和使用已发布的GTFS格式数据的多式联运行程规划软件，以建议使用当地公共交通系统的路线。（ L0 ） `LGPL-3.0` `Java/Javascript`
- [OwnTracks Recorder](https://github.com/owntracks/recorder) `⚠` - 存储和访问由OwnTracks位置跟踪应用发布的数据。 `GPL-2.0` `C/Lua/deb/Docker`
- [TileServer GL](https://tileserver.readthedocs.io/) - 具有GL样式的矢量图和光栅图。Mapbox GL Native的服务器端渲染。通过WMTS为Mapbox GL JS、Android、iOS、传单、OpenLayers、GIS等提供地图图块服务器（ L0 ） `BSD-2-Clause` `Nodejs/Docker`
- [Traccar](https://www.traccar.org/) - 用于跟踪GPS位置的Java应用程序。支持大量跟踪设备和协议，具有Android和iOS应用程序。拥有可查看行程的网页界面。(L0, L1) `Apache-2.0` `Java`
- [TRIP](https://itskovacs-trip.netlify.app/) - 极简POI地图跟踪器和行程规划器。(L0, L1) `MIT` `Docker`
- [wanderer](https://github.com/open-wanderer/wanderer) - 跟踪数据库，您可以在其中上传录制的曲目或创建新曲目并添加各种元数据，以构建易于搜索的目录。（ L0 ） `AGPL-3.0` `Docker/Go/Nodejs`


<a id="media-management"></a>
### Media Management 媒体管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Digital media](https://en.wikipedia.org/wiki/Digital_media) management tools and software.

_Related: [Automation 自动化](#automation), [Media Streaming 媒体流](#media-streaming), [Media Streaming - Audio Streaming 媒体流 - 音频流](#media-streaming---audio-streaming), [Media Streaming - Multimedia Streaming 媒体流 - 多媒体流](#media-streaming---multimedia-streaming), [Media Streaming - Video Streaming 媒体流 - 视频流](#media-streaming---video-streaming), [Media Management 媒体管理](#media-management)_

- [ChannelTube](https://github.com/TheWicklowWolf/ChannelTube) `⚠` - 通过yt-dlp按时从YouTube频道下载视频或音频。 `AGPL-3.0` `Docker`
- [Deleterr](https://github.com/rfsbraz/deleterr) - 自动媒体清理工具，根据可配置的规则从Plex、Sonarr和Radarr中删除观看和陈旧的内容。 `MIT` `Docker`
- [Downtify](https://downtify.henriquesebastiao.com) `⚠` - 下载包含专辑封面和元数据的Spotify音乐。(L0) `GPL-3.0` `Docker`
- [Elengrab](https://github.com/neosy/elengrab) - 快速的跨平台视频和音频下载器以及媒体查看器，具有灵活的格式和质量选项。支持1000多个网站，包括YouTube、Instagram、TikTok、Twitch等。（ L0 ） `AGPL-3.0` `Go/Docker`
- [HomeTube](https://hometube.latentnoise.dev) `⚠` - Web UI将1700多个网站的视频和播放列表下载到Plex或Jellyfin库中，包括质量选择、SponsorBlock赞助商删除、字幕、剪辑剪辑和弹性播放列表同步。（ L0 ） `AGPL-3.0` `Python/Docker`
- [Houndarr](https://av1155.github.io/houndarr/) - 已计划的Radarr、Sonarr、Lidarr、Readarr和Whisparr积压搜索。在每个项目冷却时间和每小时上限的小批量限速中处理缺失和截止未满足的项目，以避免索引器过载。（ L0 ） `AGPL-3.0` `Python/Docker`
- [Lidarr](https://lidarr.audio/) - Usenet和BitTorrent用户的音乐收藏管理器。（ L0 ） `GPL-3.0` `C#/Docker`
- [LidaTube](https://github.com/TheWicklowWolf/LidaTube) `⚠` - 通过yt-dlp查找和获取丢失的Lidarr专辑。 `GPL-3.0` `Docker`
- [Lidify](https://github.com/TheWicklowWolf/Lidify) `⚠` - 音乐发现工具，使用Spotify或LastFM根据选定的Lidarr艺术家提供建议。 `MIT` `Docker`
- [Lingarr](https://lingarr.com) - 使用LibreTranslate、本地AI模型或SaaS翻译服务，自动翻译Radarr和Sonarr媒体库中的字幕文件。(L0) `AGPL-3.0` `Docker`
- [Medusa](https://github.com/pymedusa/Medusa) - 电视节目的自动视频库管理器。它会关注您最喜爱的节目的新剧集，当他们发布时，它会发挥其魔力。（ L0 ） `GPL-3.0` `Python`
- [MeTube](https://github.com/alexta69/metube) - YouTube-dl的Web GUI ，支持播放列表。允许从数十个网站下载视频。 `AGPL-3.0` `Python/Nodejs/Docker`
- [MKVPriority](https://github.com/kennethsible/mkvpriority) - 使用可配置的优先级分数选择首选音频和字幕曲目，并设置适当的默认和强制标记。 `MIT` `Python/Docker`
- [MyTube](https://github.com/franklioxygen/MyTube) `⚠` - 具有频道订阅、云上传支持和本地库组织的yt-dlp支持网站的下载器和播放器。（ L0 ） `MIT` `Nodejs/Docker`
- [nefarious](https://lardbit.github.io/nefarious/) - 自动下载电影和电视节目。（ L0 ） `GPL-3.0` `Python`
- [Ombi](https://ombi.io/) - Plex/Emby的内容请求系统连接到SickRage、CouchPotato、Sonarr ，具有不断增长的功能集。(L0, L1) `GPL-2.0` `C#/deb`
- [Pinchflat](https://github.com/kieraneglin/pinchflat) `⚠` - 下载使用yt-dlp构建的YouTube内容。 `AGPL-3.0` `Docker`
- [PodFetch](https://samtv12345.github.io/PodFetch) - 时尚高效的播客下载器。（ L0 ） `Apache-2.0` `Docker/Rust`
- [Radarr](https://radarr.video/) - 通过Usenet和BitTorrent （ Sonarr的分支）自动下载电影。（ L0 ） `GPL-3.0` `C#/Docker`
- [Ratelog](https://ratelog.org) - 电影跟踪器和分级应用程序（ Letterboxd的替代品）。（ L0 ） `AGPL-3.0` `Docker`
- [Reaparr](https://www.reaparr.rocks/) `⚠` - 跨平台Plex媒体下载器，可将来自其他Plex服务器的媒体无缝添加到您自己的服务器。（ L0 ） `GPL-3.0` `Docker`
- [Seerr](https://github.com/seerr-team/seerr) - 管理对媒体库的请求，支持Plex、Jellyfin和Emby媒体服务器（ Overseerr的分支）。 `MIT` `Docker/Nodejs`
- [Sonarr](https://sonarr.tv/) - 用于Usenet和BitTorrent的自动电视节目下载器和管理器。它可以抓取、排序和重命名新剧集，并在有更高质量的格式可用时自动升级已下载文件的质量。（ L0 ） `GPL-3.0` `C#/Docker`
- [TrackWatch](https://trackwatch.emlopezr.com) `⚠` - Spotify的自动音乐发布跟踪器，包括电子邮件通知、唱片生成器和幽灵轨道清洁器（发布雷达的替代品）。（ L0 ） `MIT` `Docker`
- [tubesync](https://github.com/meeb/tubesync) `⚠` - 将YouTube频道和播放列表同步到本地托管的媒体服务器。 `AGPL-3.0` `Docker/Python`
- [Watcharr](https://github.com/sbondCo/Watcharr) - 添加并跟踪您正在观看的所有节目和电影。配备用户身份验证、新式简洁的用户界面和非常简单的设置。 `MIT` `Docker`
- [ydl_api_ng](https://github.com/Totonyus/ydl_api_ng) - 简单的youtube-dl REST API ，可在远程服务器上启动下载。 `GPL-3.0` `Python`
- [Youtarr](https://github.com/DialmasterOrg/Youtarr) `⚠` - 通过yt-dlp按时从YouTube频道下载视频，通过网络用户界面浏览和有选择地下载视频。与Plex Media Server集成，并为Jellyfin、Kodi和Emby生成NFO元数据。 `ISC` `Docker`
- [youtube-dl-nas](https://hyeonsangjeon.github.io/youtube-dl-nas/) `⚠` - 经过身份验证的yt-dlp视频、音频和字幕下载队列，具有历史记录、移动共享和NAS文件管理（ youtube-dl-server的分支）。（ L0 ） `MIT` `Python/Docker`
- [YoutubeDL-Server](https://github.com/nbr23/youtube-dl-server) - Youtube-DL的网络和REST接口，用于将视频下载到服务器上。 `MIT` `Python/Docker`


<a id="media-streaming"></a>
### Media Streaming 媒体流

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Streaming media](https://en.wikipedia.org/wiki/Streaming_media) is multimedia that is delivered and consumed in a continuous manner from a source, with little or no intermediate storage in network elements.

**请访问 [Media streaming - Audio Streaming](#media-streaming---audio-streaming), [Media streaming - Multimedia Streaming](#media-streaming---multimedia-streaming), [Media streaming - Video Streaming](#media-streaming---video-streaming), [Media Management](#media-management)**

_Related: [Media Streaming 媒体流](#media-streaming)_

_See also: [List of streaming media systems - Wikipedia](https://en.wikipedia.org/wiki/List_of_streaming_media_systems), [Comparison of streaming media systems - Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_streaming_media_systems)_



<a id="media-streaming---audio-streaming"></a>
### Media Streaming - Audio Streaming 媒体流 - 音频流

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Audio](https://en.wikipedia.org/wiki/Audio) streaming tools and software.

_Related: [Media Management 媒体管理](#media-management)_

- [Ampache](https://ampache.org/) - 基于Web的音频/视频流应用程序。(L0, L1) `AGPL-3.0` `PHP`
- [Audiobookshelf](https://www.audiobookshelf.org/) - 有声读物和播客服务器。它可以跨设备流式传输所有音频格式，保持和同步进度。附带适用于Android和iOS的应用程序。(L0, L1) `GPL-3.0` `Docker/deb/Nodejs`
- [Audioserve](https://github.com/izderadicka/audioserve) - 简单的个人服务器，用于提供来自目录（有声读物、音乐、播客... ）的音频文件。专注于简单性，并支持客户端之间播放位置的同步。 `MIT` `Rust`
- [AzuraCast](https://www.azuracast.com/) - 现代化且易于访问的网络无线电管理套件。（ L0 ） `Apache-2.0` `Docker`
- [Beets](https://beets.io/) - 音乐库管理器和MusicBrainz标记器（命令行和Web界面）。（ L0 ） `MIT` `Python/deb`
- [Black Candy](https://github.com/blackcandy-org/blackcandy) - 音乐流媒体服务器。 `MIT` `Docker/Ruby`
- [BotWave](https://botwave.dpip.lol) - 具有服务器-客户端架构的调频广播系统，用于远程管理多个Raspberry Pi发射器。（ L0 ） `GPL-3.0` `Python`
- [Funkwhale](https://dev.funkwhale.audio/funkwhale) - 现代、基于Web、欢乐、多用户和免费音乐服务器。 `BSD-3-Clause` `Python`
- [gonic](https://github.com/sentriz/gonic) - 轻量级音乐流媒体服务器。亚音速兼容。 `GPL-3.0` `Go/Docker`
- [koel](https://koel.dev/) - 可正常工作的个人音乐流媒体服务器。(L0, L1) `MIT` `PHP`
- [LibreTime](https://libretime.org) - 在网络上播放流媒体广播（分支为Airtime ）。（ L0 ） `AGPL-3.0` `Docker/PHP`
- [LMS](https://github.com/epoupon/lms) - 使用Web界面访问您自己的音乐。 `GPL-3.0` `Docker/deb/C++`
- [Lyrion Music Server](https://lyrion.org/) - 控制各种Squeezebox/Slim Devices音频播放器和兼容硬件（以前称为罗技媒体服务器）的服务器软件。(L0, L1) `GPL-2.0` `deb/Docker/Perl`
- [moOde Audio](https://moodeaudio.org/) - 发烧友品质的音乐播放，适用于美妙的Raspberry Pi系列单板电脑。（ L0 ） `GPL-3.0` `PHP`
- [Mopidy](https://docs.mopidy.com/) `⚠` - 可扩展的音乐服务器。提供MPD API的超集，以及与Spotify、SoundCloud等第三方服务的集成。（ L0 ） `Apache-2.0` `Python/deb`
- [mpd](https://www.musicpd.org/) - 守护进程可远程播放音乐、流式传输音乐、处理和组织播放列表。许多客户可用。（ L0、L1 ） `GPL-2.0` `C++`
- [mStream](https://mstream.io/) - Music streaming server with GUI management tools. Runs on Mac, Windows, and Linux. (L0) `GPL-3.0` `Nodejs`
- [multi-scrobbler](https://foxxmd.github.io/multi-scrobbler) - Scrobble plays from multiple sources to multiple scrobbling services. (L0) `MIT` `Nodejs/Docker`
- [musikcube](https://github.com/clangen/musikcube) - Streaming audio server with Linux/macOS/Windows/Android clients. `BSD-3-Clause` `C++/deb`
- [Navidrome Music Server](https://www.navidrome.org) - Modern Music Server and Streamer, compatible with Subsonic/Airsonic. (L0, L1, L2) `GPL-3.0` `Docker/Go`
- [Pinepods](https://www.pinepods.online/) - Podcast management system with multi-user support. Pinepods utilizes a central database so aspects like listen time and themes follow from device to device. (L0, L1) `GPL-3.0` `Docker`
- [Polaris](https://github.com/agersant/polaris) - Music browsing and streaming application optimized for large music collections, ease of use and high performance. `MIT` `Rust/Docker`
- [Snapcast](https://github.com/snapcast/snapcast) - Synchronous multiroom audio server. `GPL-3.0` `C++/deb`
- [Stretto](https://github.com/benkaiser/stretto) `⚠` - Music player with Youtube/Soundcloud import and iTunes/Spotify discovery. (L0, L1) `MIT` `Nodejs`
- [Supysonic](https://github.com/spl0k/supysonic) - Python implementation of the Subsonic server API. `AGPL-3.0` `Python/deb`
- [SwingMusic](https://swingmusic.vercel.app/) - Beautiful music player and streaming server for your local audio files. Like a cooler Spotify ... but bring your own music. (L0) `MIT` `Python/Docker`
- [vod2pod-rss](https://github.com/madiele/vod2pod-rss) `⚠` - Convert YouTube and Twitch channels to podcasts, no storage required. Transcodes VoDs to MP3 192k on the fly, generates an RSS feed to use in podcast clients. `MIT` `Docker`


<a id="media-streaming---multimedia-streaming"></a>
### Media Streaming - Multimedia Streaming 媒体流 - 多媒体流

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Multimedia](https://en.wikipedia.org/wiki/Multimedia) streaming tools and software.

_Related: [Media Streaming - Video Streaming 媒体流 - 视频流](#media-streaming---video-streaming), [Media Streaming - Audio Streaming 媒体流 - 音频流](#media-streaming---audio-streaming), [Media Management 媒体管理](#media-management)_

- [ClipBucket](https://clipbucket.fr/) - Start your own video sharing website (YouTube/Netflix Clone) in a matter of minutes. (L0, L1) `AAL` `Docker/PHP`
- [cmyflix](https://github.com/farfalleflickan/cmyflix) - Minimalist Plex/Jellyfin alternative to stream video. `AGPL-3.0` `C/deb`
- [Gerbera](https://gerbera.io/) - UPnP Media Server, which allows you to stream your digital media throughout your home network and listen to/watch it on a variety of UPnP compatible devices. (L0) `GPL-2.0` `Docker/deb/C++`
- [Icecast 2](https://icecast.org) - Streaming audio/video server which can be used to create an Internet radio station or a privately running jukebox and many things in between. (L0, L1) `GPL-2.0` `C`
- [Jellyfin](https://jellyfin.org) - Media server for audio, video, books, comics, and photos with a sleek interface and robust transcoding capabilities. Almost all modern platforms have clients, including Roku, Android TV, iOS, and Kodi. (L0, L1, L2) `GPL-2.0` `C#/deb/Docker`
- [Karaoke Eternal](https://www.karaoke-eternal.com) - Host awesome karaoke parties where everyone can easily find and queue songs from their phone's browser. The player is also fully browser-based with support for MP3+G, MP4 and WebGL visualizations. (L0) `ISC` `Docker/Nodejs`
- [Kodi](https://kodi.tv/) - Multimedia/Entertainment center, formerly known as XBMC. Runs on Android, BSD, Linux, macOS, iOS and Windows. (L0) `GPL-2.0` `C++/deb`
- [Kyoo](https://github.com/zoriya/kyoo) - Innovative media browser designed for seamless streaming of anime, series and movies, offering advanced features like dynamic transcoding, auto watch history and intelligent metadata retrieval. (L0) `GPL-3.0` `Docker`
- [MediaMTX](https://mediamtx.org) - Ready-to-use, zero-dependency real-time media server and proxy to publish, read, record, playback and route video/audio streams over SRT, WebRTC, RTSP, RTMP, HLS, MPEG-TS, RTP. (L0, L1) `MIT` `Go/Docker`
- [Meelo](https://github.com/Arthi-chaud/Meelo) - Personal Music Server, designed for collectors and music maniacs. `GPL-3.0` `Docker`
- [MistServer](https://mistserver.org/) - Public domain streaming media server that works with any device and any format. (L0) `Unlicense` `C++`
- [NymphCast](http://nyanko.ws/nymphcast.php) - Turn your choice of Linux-capable hardware into an audio and video source for a television or powered speakers (alternative to Chromecast). (L0) `BSD-3-Clause` `C++`
- [Rygel](https://gnome.pages.gitlab.gnome.org/rygel/) - UPnP AV MediaServer that allows you to easily share audio, video, and pictures. Media player software may use Rygel to become a MediaRenderer that may be controlled remotely by a UPnP or DLNA Controller. (L0) `LGPL-2.1` `C`
- [Stash](https://stashapp.cc) - Web-based library organizer and player for your adult media stash, with auto-tagging and metadata scraping support. (L0) `AGPL-3.0` `Docker/Go`
- [µStreamer](https://github.com/pikvm/ustreamer) - Lightweight and very quick server to stream MJPEG video from any V4L2 device to the net. `GPL-3.0` `C/deb`
- [üWave](https://u-wave.net/) `⚠` - Collaborative listening platform. Users take turns playing media—songs, talks, gameplay videos, or anything else—from a variety of media sources like YouTube and SoundCloud. (L0, L1) `MIT` `Nodejs`


<a id="media-streaming---video-streaming"></a>
### Media Streaming - Video Streaming 媒体流 - 视频流

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Video](https://en.wikipedia.org/wiki/Video) streaming tools and software.

_Related: [Video Surveillance 视频监控](#video-surveillance), [Media Streaming - Multimedia Streaming 媒体流 - 多媒体流](#media-streaming---multimedia-streaming), [Photo Galleries 相册](#photo-galleries), [Media Management 媒体管理](#media-management)_

- [CyTube](https://github.com/calzoneman/sync) - Synchronize media, chat, and more for an arbitrary number of channels. (L0) `MIT` `Nodejs`
- [Invidious](https://github.com/iv-org/invidious) `⚠` - Alternative YouTube front-end. (L0) `AGPL-3.0` `Docker/Crystal`
- [MediaCMS](https://mediacms.io) - Modern, fully featured video and media CMS, written in Python/Django/React, featuring a REST API. (L0) `AGPL-3.0` `Python/Docker`
- [OvenMediaEngine](https://github.com/OvenMediaLabs/OvenMediaEngine) - Streaming Server with Sub-Second Latency. (L0) `AGPL-3.0` `C++/Docker`
- [Owncast](https://owncast.online/) - Decentralized single-user live video streaming and chat server for running your own live streams similar in style to the large mainstream options. (L0) `MIT` `Go`
- [PeerTube](https://joinpeertube.org/en/) - Decentralized video streaming platform using P2P (BitTorrent) directly in the web browser. (L0) `AGPL-3.0` `Nodejs`
- [Rapidbay](https://github.com/hauxir/rapidbay/) - Videostreaming service/torrent client that allows searching and playing videos from torrents in the browser or from a Chromecast/AppleTV/Smart TV. `MIT` `Python/Docker`
- [Restreamer](https://datarhei.github.io/restreamer/) - Access H.264 real-time video streaming on your website without a streaming provider. (L0) `Apache-2.0` `Nodejs/Docker`
- [SRS](https://ossrs.io/) - Simple, high efficiency and real-time video server, supports RTMP, WebRTC, HLS, HTTP-FLV and SRT. (L0) `MIT` `Docker/C++`
- [SyncTube](https://github.com/RblSb/SyncTube) - Lightweight and very simple to setup CyTube alternative to watch videos with friends and chat. `MIT` `Nodejs/Haxe`
- [Tiramisu](https://github.com/MrRobotoGit/tiramisu) - BitTorrent engine with a FUSE virtual filesystem that streams torrents live to Plex/Jellyfin without downloading (alternative to Real-Debrid). `GPL-2.0` `Go/Docker`
- [Tube Archivist](https://tubearchivist.com/) `⚠` - Organize, search, and enjoy your YouTube collection. Subscribe, download, and track viewed content with metadata indexing and a user-friendly interface. (L0, L1) `GPL-3.0` `Docker`
- [Tube](https://git.mills.io/prologic/tube) - Youtube-like (without censorship and features you don't need!) video sharing app written in Go which also supports automatic transcoding to MP4 H.265 AAC, multiple collections and RSS feed. `MIT` `Go`
- [VideoLAN Client (VLC)](https://www.videolan.org/) - Cross-platform multimedia player client and server supporting most multimedia files as well as DVDs, Audio CDs, VCDs, and various streaming protocols. (L0) `GPL-2.0` `C/deb`


<a id="miscellaneous"></a>
### Miscellaneous 杂项

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Software that does not fit in another section.

- [2FAuth](https://github.com/Bubka/2FAuth) - Manage your Two-Factor Authentication (2FA) accounts and generate their security codes. (L0) `AGPL-3.0` `PHP/Docker`
- [Anchr](https://anchr.io) - Toolbox for tiny tasks on the internet, including bookmark collections, URL shortening and (encrypted) image uploads. (L0) `GPL-3.0` `Nodejs`
- [Anubis](https://anubis.techaro.lol/) - Web AI firewall utility which protects upstream resources from scraper bots. (L0) `MIT` `Docker/deb/Go`
- [asciinema](https://asciinema.org/) - Web app for hosting asciicasts. (L0, L1) `Apache-2.0` `Elixir/Docker`
- [Baby Buddy](https://github.com/babybuddy/babybuddy) - Helps caregivers track baby sleep, feedings, diaper changes, and tummy time. (L0) `BSD-2-Clause` `Python`
- [ClipCascade](https://github.com/Sathvik-Rao/ClipCascade) - Syncs your clipboard across multiple devices instantly, without any button press. Available on Windows, macOS, Linux, and Android, it provides seamless and secure clipboard sharing with end-to-end data encryption. `GPL-3.0` `Java/Docker`
- [Cloudlog](https://magicbug.co.uk/cloudlog/) - Log your amateur radio contacts anywhere. (L0) `MIT` `PHP/Docker`
- [ConvertX](https://github.com/C4illin/ConvertX) - Online file converter which supports over a thousand different formats. `AGPL-3.0` `Docker`
- [CUPS](https://www.cups.org/) - Common Unix Print System uses Internet Printing Protocol (IPP) to support printing to local and network printers. (L0) `GPL-2.0` `C`
- [CyberChef](https://github.com/gchq/CyberChef) - Perform all manner of operations within a web browser such as AES, DES and Blowfish encryption and decryption, creating hexdumps, calculating hashes, and much more. (L0) `Apache-2.0` `Javascript`
- [Digiboard](https://digiboard.app/) - Create collaborative whiteboards (documentation in French). (L0) `AGPL-3.0` `Nodejs`
- [Digicard](https://codeberg.org/ladigitale/digicard) - Create simple graphic compositions (documentation in French). (L0) `AGPL-3.0` `Nodejs`
- [Digicut](https://ladigitale.dev/digicut/) - Cut audio and video files using FFMPEG.wasm (documentation in French). (L0) `AGPL-3.0` `Nodejs`
- [Digiface](https://ladigitale.dev/digiface/) - Create avatars using the Avataaars library (documentation in French). (L0, L1) `AGPL-3.0` `Nodejs`
- [Digiflashcards](https://ladigitale.dev/digiflashcards/) - Online application to create flashcards (documentation in French). (L0) `AGPL-3.0` `Nodejs/PHP`
- [Digimerge](https://ladigitale.dev/digimerge/) - Assemble audio and video files directly in your browser (documentation in French). (L0, L1) `AGPL-3.0` `Nodejs`
- [Digiquiz](https://ladigitale.dev/digiquiz/) - Online application to publish content created with H5P (documentation in French). (L0) `AGPL-3.0` `Nodejs`
- [Digiread](https://ladigitale.dev/digiread/) `⚠` - Clean up online pages and articles using Mozilla's Readability (documentation in French). (L0) `AGPL-3.0` `Nodejs/PHP`
- [Digisteps](https://ladigitale.dev/digisteps/) - Simple application for creating online educational paths (documentation in French). (L0) `AGPL-3.0` `Nodejs/PHP`
- [Digitranscode](https://ladigitale.dev/digitranscode) - Convert audio files and videos directly in the browser (documentation in French). (L0, L1) `AGPL-3.0` `Nodejs`
- [Digiview](https://ladigitale.dev/digiview/) `⚠` - View YouTube videos in a distraction-free interface (documentation in French). (L0, L1) `AGPL-3.0` `Nodejs/PHP`
- [Digiwords](https://ladigitale.dev/digiwords/) - Simple online application for creating word clouds (documentation in French). (L0) `AGPL-3.0` `Nodejs/PHP`
- [DOCAT](https://github.com/docat-org/docat) - Host your docs. Simple. Versioned. Fancy. `MIT` `Python/Docker`
- [Domain Locker](https://domain-locker.com) - Domain name portfolio management and tracker. (L0, L1) `MIT` `Deno/Docker`
- [DOMJudge](https://www.domjudge.org/) - System for running a programming contest, like the ICPC regional and world championship programming contests. (L0, L1) `GPL-2.0/BSD-3-Clause/MIT` `PHP`
- [ESMira](https://esmira.kl.ac.at) - Run longitudinal studies (ESM, AA, EMA) with data collection and communication with participants being completely anonymous. (L0, L1) `AGPL-3.0` `PHP`
- [F-Droid](https://f-droid.org) - Server tools for maintaining an F-Droid repository system. (L0) `AGPL-3.0` `Python/Docker/deb`
- [Flyimg](https://flyimg.io) - Resize and crop images on the fly. Get optimised images with MozJPEG, WebP or PNG using ImageMagick, with an efficient caching system. (L0, L1) `MIT` `Docker`
- [Garlic-Hub](https://garlic-signage.com/garlic-hub/) - Digital signage device and content management system with SMIL playlist support and scheduling. (L0) `AGPL-3.0` `Docker`
- [Geeftlist](https://codeberg.org/nanawel/geeftlist) - Collaborative platform for managing, sharing and reserving gifts between friends and family. `GPL-3.0` `Docker`
- [google-webfonts-helper](https://github.com/majodev/google-webfonts-helper) `⚠` - Hassle-Free Way to Self-Host Google Fonts. Get eot, ttf, svg, woff and woff2 files + CSS snippets. (L0) `MIT` `Nodejs`
- [Habitica](https://habitica.com/) - Habit tracker app which treats your goals like a Role Playing Game. (L0) `GPL-3.0/CC-BY-SA-3.0` `Nodejs/Docker`
- [HortusFox](https://hortusfox.github.io) - Collaborative plant management and tracking system for plant enthusiasts. (L0) `MIT` `PHP/Docker`
- [ImgCompress](https://imgcompress.karimzouine.com) - Image processing tool that runs entirely in Docker. Compress, convert, resize, batch-process images, and remove backgrounds using local AI without cloud dependencies. (L0) `GPL-3.0` `Docker`
- [Infisical Community Edition](https://infisical.com/) - Platform for secrets, certificates, and privileged access management. (L0) `MIT` `Docker/K8S/deb`
- [iSponsorBlockTV](https://github.com/dmunozv04/iSponsorBlockTV) `⚠` - Block and skip sponsors, while also muting and skipping ads on YouTube. `GPL-3.0` `Docker/Python`
- [IT-Tools by sharevb](https://github.com/sharevb/it-tools) - Collection of handy online tools for developers (fork of it-tools). (L0) `GPL-3.0` `Docker`
- [Jelu](https://bayang.github.io/jelu-web) - Read and to-read list book tracker. (L0) `MIT` `Java/Docker`
- [jetlog](https://github.com/pbogre/jetlog) - Personal flight tracker and viewer. `GPL-2.0` `Docker`
- [Kasm Workspaces](https://kasmweb.com/) - Streaming containerized apps and desktops to end-users. Examples include Ubuntu in your browser, or simply single apps such as Chrome, OpenOffice, Gimp, Filezilla etc. (L0, L1) `GPL-3.0` `Docker`
- [Koillection](https://koillection.github.io/) - Service allowing users to manage any kind of collections. (L0) `MIT` `Docker/PHP`
- [LanguageTool](https://languagetool.org/) - Proofread more than 20 languages. It finds many errors that a simple spell checker cannot detect. (L0, L1) `LGPL-2.1` `Java/Docker`
- [Libre Translate](https://libretranslate.com/) - Machine Translation API. (L0) `AGPL-3.0` `Docker/Python`
- [LubeLogger](https://lubelogger.com) - Web-based vehicle maintenance and fuel mileage tracker. (L0, L1) `MIT` `Docker/K8S/C#`
- [Mirumoji](https://svdc1.github.io/mirumoji/docs) - Japanese immersion toolkit providing clickable, tokenized subtitles with dictionary lookups and transcription generation. (L0, L1) `MIT` `Docker/Python`
- [mosparo](https://mosparo.io/) - Modern spam protection tool. It replaces other captcha methods with a simple and easy to use spam protection solution. (L0) `MIT` `PHP`
- [Movary](https://github.com/leepeuker/movary) `⚠` - Web app to track and rate your watched movies. (L0) `MIT` `Docker/PHP`
- [Neko](https://neko.m1k1o.net) - Virtual browser that runs in docker and uses WebRTC. (L0) `Apache-2.0` `Docker/Go`
- [OmniTools](https://omnitools.app/) - Collection of powerful web-based tools for everyday tasks (coding, manipulating images/videos, PDFs or crunching numbers...). (L0) `MIT` `Docker`
- [Open-Meteo](https://open-meteo.com/) - Weather API with open-data forecasts, historical and climate data from all major national weather services. (L0, L1) `AGPL-3.0` `Docker`
- [OpenReader](https://docs.openreader.richardr.dev/) - EPUB, PDF, DOCX, MD, and TXT file text to speech document reader. Read documents in realtime with high-quality TTS; or extract audiobooks. (L0) `MIT` `Docker`
- [OpenZiti](https://openziti.io/) - Fully-featured, zero trust, full mesh overlay network. Includes a 2FA support out of the box, clients for all major desktop/mobile OS'es. (L0) `Apache-2.0` `Go`
- [Operational.co](https://operational.co) - Receive alerts in a live timeline from your product. (L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [penpot](https://penpot.app/) - Web-based design and prototyping platform meant for cross-domain teams. (L0) `MPL-2.0` `Docker`
- [POMjs](https://password.oppetmoln.se/) - Random password generator. (L0) `GPL-2.0` `Javascript`
- [Pønskelisten](https://github.com/aunefyren/poenskelisten) - Sharing wishlists and collaborating on gifts and presents. `GPL-3.0` `Docker/Go`
- [re:Director](https://re-director.github.io/) - Simple domain redirection management tool. (L0) `Apache-2.0` `Java/Docker`
- [Reactive Resume](https://rxresu.me/) - One-of-a-kind resume builder that keeps your privacy in mind. Completely secure, customizable and portable. (L0, L1) `MIT` `Docker/Nodejs`
- [revealjs](https://revealjs.com) - Framework for easily creating beautiful presentations using HTML. (L0, L1) `MIT` `Javascript`
- [Revive Adserver](https://www.revive-adserver.com/) - Ad serving system. Formerly known as OpenX Adserver and phpAdsNew. (L0) `GPL-2.0` `PHP`
- [SANE Network Scanning](http://sane-project.org/) - Allow remote clients to access image acquisition devices (scanners) available on the local host. (L0) `GPL-2.0` `C`
- [string.is](https://string.is/) - Online string toolkit for developers. (L0) `AGPL-3.0` `Nodejs`
- [Teleport](https://goteleport.com/) - Certificate authority and access plane for SSH, Kubernetes, web applications, and databases. (L0) `Apache-2.0` `Go/Docker/K8S`
- [TeslaMate](https://github.com/teslamate-org/teslamate) - Powerful data logger for Tesla vehicles. `MIT` `Elixir/Docker`
- [Transmute](https://transmute.sh) - File converter for images, video, audio, json, excel and more. Supports over 2,000 conversions!. (L0) `MIT` `Docker`
- [URL-to-PNG](https://github.com/jasonraimondi/url-to-png) - URL to PNG utility featuring parallel rendering using Playwright for screenshots and with storage caching via Local, S3, or CouchDB. `MIT` `Nodejs/Docker`
- [Usertour](https://www.usertour.io/) - User onboarding platform allowing you to create in-app product tours, checklists, and surveys in minutes effortlessly. (L0) `AGPL-3.0` `Docker`
- [Warracker](https://warracker.com) - Warranty tracker that lets you monitor expiry dates, upload receipts/files, and get alerts before warranties expire. (L0) `AGPL-3.0` `Docker`
- [Wavelog](https://www.wavelog.org) - Webbased Logging Software for Radio Amateurs. Enhanced QSO logging, statistics and maps for your browser. (L0, L1) `MIT` `PHP/Docker`
- [WeeWX](https://weewx.com/) - Software for your weather station. (L0, L1) `GPL-3.0` `Python/deb`
- [WeTTY](https://butlerx.github.io/wetty/#/) - Terminal in browser over http/https. (L0) `MIT` `Docker/Nodejs`
- [Wishlist](https://github.com/cmintey/wishlist) - Wishlist application that you can share with your friends and family. `MIT` `Docker/K8S`
- [Yamtrack](https://github.com/FuzzyGrim/Yamtrack) `⚠` - Media tracker for movies, tv shows, anime, manga, video games and books. (L0) `AGPL-3.0` `Docker/Python`
- [Zero-TOTP](https://zero-totp.com) - Complete, reliable, secure and zero-trust webapp based on zero-knowledge encryption to store your TOTP codes. (L0) `GPL-3.0` `Docker`


<a id="money-budgeting--management"></a>
### Money, Budgeting & Management 金钱、预算与管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Money management](https://en.wikipedia.org/wiki/Money_management) and budgeting software.

_Related: [Inventory Management 库存管理](#inventory-management), [Resource Planning 资源规划](#resource-planning)_

- [Actual](https://actualbudget.org) - Local-first personal finance tool based on zero-sum budgeting, supporting synchronization across devices, custom rules, manual transaction importing (from QIF, OFX, and QFX files), and optional automatic synchronization with many banks. (L0) `MIT` `Nodejs/Docker`
- [Bigcapital](https://bigcapital.app/) - Financial accounting and inventory management software for small to medium businesses. (L0) `AGPL-3.0` `Docker`
- [Bitcart](https://bitcart.ai) - Cryptocurrencies payment processor and development platform. (L0, L1) `MIT` `Docker/Python/Nodejs`
- [BTCPay Server](https://btcpayserver.org/) - Bitcoin and other cryptocurrencies payment processor. (L0, L1) `MIT` `C#`
- [Budget Board](https://budgetboard.net/) - Simple app for tracking monthly spending and working towards financial goals. (L0) `GPL-3.0` `Docker`
- [DePay](https://depay.com) - Accept Web3 Payments directly into your wallet peer-to-peer. (L0, L1) `MIT` `Nodejs`
- [Econumo](https://econumo.com) - Budgeting application for managing personal and family finances, supporting multiple currencies, joint accounts, and budgets. (L0, L1) `MIT` `Docker`
- [Expensave](https://github.com/algirdasc/expensave) - Expense tracker for personal and family budget management. Track spending on a shared calendar, import bank statements and monitor finances with reports. `GPL-3.0` `Docker`
- [ezbookkeeping](https://ezbookkeeping.mayswind.net/) - Lightweight personal bookkeeping app hosted by yourself. (L0, L1) `MIT` `Go/Docker`
- [Family Accounting Tool](https://github.com/nymanjens/facto) - Web-based finance management tool for partners with partially shared expenses. `Apache-2.0` `Scala`
- [Fava](https://beancount.github.io/fava/) - Web frontend of Beancount, a text based double-entry accounting system. (L0, L1) `MIT` `Python`
- [Firefly III](https://firefly-iii.org/) - Modern financial manager. It helps you to keep track of your money and make budget forecasts. It supports credit cards, has an advanced rule engine and can import data from many banks. (L0, L1) `AGPL-3.0` `PHP/Docker`
- [FOSSBilling](https://fossbilling.org/) - Hosting and billing automation. Integrates with WHM, CWP, cPanel and HestiaCP. Full API and easily extensible. (L0, L1) `Apache-2.0` `PHP/Docker`
- [Galette](https://galette.eu/) - Membership management web application aimed towards non profit organizations. (L0) `GPL-3.0` `PHP`
- [Ghostfolio](https://ghostfol.io/) - Wealth management software to keep track of stocks, ETFs and cryptocurrencies. (L0) `AGPL-3.0` `Docker/Nodejs`
- [GRR](https://grr.devome.com/?lang=en) - Assets management and booking for small/medium companies. (L0) `GPL-2.0` `PHP`
- [HyperSwitch](https://hyperswitch.io/) `⚠` - Payment switch to make payments fast, reliable and affordable. Connect with multiple payment processors and route traffic effortlessly, all with a single API integration. (L0) `Apache-2.0` `Docker/Rust`
- [IHateMoney](https://ihatemoney.org/) - Manage your shared expenses, easily. (L0, L1) `BSD-3-Clause` `Docker/Python`
- [InvoicePlane](https://www.invoiceplane.com/) - Manage quotes, invoices, payments and customers for your small business. (L0) `MIT` `PHP`
- [InvoiceShelf](https://invoiceshelf.com/) - Track expenses, payments & create professional invoices & estimates (fork of Crater). (L0) `AGPL-3.0` `PHP/Docker`
- [Kill Bill](https://killbill.io/) - Subscription billing & payments platform. Have access to real-time analytics and financial reports. (L0) `Apache-2.0` `Java/Docker`
- [Kresus](https://kresus.org/) - Personal finance manager. (L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [Lago](https://www.getlago.com/) - Metering and usage-based billing. (L0) `AGPL-3.0` `Docker`
- [Mybucks.online](https://mybucks.online) - Secure, browser-based, password-only self-custodial cryptocurrency wallet. (L0, L1) `MIT` `Nodejs`
- [MyFin Budget](https://myfinbudget.com) - Personal finances platform (web + REST API + Android) that'll help you budget, keep track of your income/spending and forecast your financial future. (L0, L1, L2) `GPL-3.0` `Nodejs/Docker`
- [OctoBot](https://www.octobot.cloud/) - Cryptocurrency trading bot. (L0) `GPL-3.0` `Python/Docker`
- [Ocular](https://simonwep.github.io/ocular/) - Simplistic and straightforward budgeting app to track your budget across months and years. (L0, L1) `MIT` `Docker`
- [OpenBudgeteer](https://github.com/TheAxelander/OpenBudgeteer) - Budgeting app based on the Bucket Budgeting Principle. `AGPL-3.0` `Docker/C#`
- [Receipt Wrangler](https://receiptwrangler.io) `⚠` - Easy-to-use receipt manager, powered by AI. Allows users to create receipts effortlessly and quickly, categorize and more. (L0, L1) `AGPL-3.0` `Docker`
- [REI3](https://rei3.de/home_en/) - Manage tasks, time, assets and much more within your business. (L0, L1) `MIT` `Go`
- [SHKeeper](https://shkeeper.io/) - Cryptocurrency payment processor with the unique combination of gateway and merchant allowing you to accept payments in multiple cryptocurrencies without fees and intermediaries. (L0, L1) `GPL-3.0` `Python`
- [SolidInvoice](https://solidinvoice.co) - Invoicing and quote application. (L0) `MIT` `PHP`
- [Sure](https://github.com/we-promise/sure) - Personal finance application for everyone (fork of Maybe). `AGPL-3.0` `Docker`
- [VoucherVault](https://github.com/l4rm4nd/VoucherVault) - Store and manage vouchers, coupons, loyalty and gift cards digitally. Supports expiry notifications, transaction histories, file uploads and OIDC SSO. `GPL-3.0` `Docker`
- [Wallos](https://wallosapp.com) - Lightweight personal subscription tracker with statistics and optional notifications. (L0, L1) `GPL-3.0` `PHP/Docker`
- [WYGIWYH](https://github.com/eitchtee/WYGIWYH) - Simple and powerful finance tracker. (L0) `AGPL-3.0` `Docker/Python`
- [YAFFA](https://www.yaffa.cc) - Personal finance web application, that can be used to keep track of your money, expenses, budgets, and investments. It also helps with long-term financial planning. (L0, L1) `MIT` `PHP`


<a id="monitoring--status-pages"></a>
### Monitoring & Status Pages 监控与状态页

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Software for [monitoring](https://en.wikipedia.org/wiki/Monitoring#Computing) systems, networks, applications and websites. 

**请访问 [awesome-sysadmin/Monitoring](https://github.com/awesome-foss/awesome-sysadmin#monitoring--status-pages), [awesome-sysadmin/Metrics and Metric Collection](https://github.com/awesome-foss/awesome-sysadmin#metrics--metric-collection)**

_Related: [Personal Dashboards 个人仪表盘](#personal-dashboards)_



<a id="network-utilities"></a>
### Network Utilities 网络工具

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Network utilities are tools and software that help manage, monitor, and troubleshoot computer networks.

_See also: [awesome-sysadmin/Monitoring](https://github.com/awesome-foss/awesome-sysadmin#monitoring)_

- [beelzebub](https://beelzebub-honeypot.com/) `⚠` - Honeypot framework designed to provide a highly secure environment for detecting and analyzing cyber attacks. (L0) `MIT` `Docker/K8S/Go`
- [Canary Tokens](https://canarytokens.org) - Generates lightweight, embedded honeypot triggers called canary tokens for detecting unauthorized access. (L0) `BSD-3-Clause` `Docker/Python`
- [MyIP](https://ipcheck.ing) `⚠` - All in one IP Toolbox. Easy to check what's your IPs, IP geolocation, check for DNS leaks, examine WebRTC connections, speed test, ping test, MTR test, check website availability and more. (L0, L1) `MIT` `Nodejs/Docker`
- [MySpeed](https://myspeed.dev/) - Speed test analysis software that shows your internet speed for up to 30 days. (L0) `MIT` `Docker/Nodejs`
- [NetAlertX](https://netalertx.com/) - Network intruder and presence detector. Scans for devices connected to your network and alerts you if new and unknown devices are found. (L0) `GPL-3.0` `Docker`
- [PlugNPiN](https://deepspace2.github.io/PlugNPiN) - Automatically scrapes containers with specific labels and creates local DNS/CNAME entries in Pi-Hole/AdGuard Home and proxy hosts in Nginx Proxy Manager. (L0) `GPL-3.0` `Docker`
- [Speed Test by OpenSpeedTest™](https://openspeedtest.com/) - HTML5 Network Performance Estimation Tool. (L0) `MIT` `Docker`
- [Speedtest Tracker](https://docs.speedtest-tracker.dev/) - Monitor the performance and uptime of your internet connection. (L0) `MIT` `Docker/K8S`
- [Upsnap](https://github.com/seriousm4x/UpSnap) - Simple Wake on LAN (WOL) dashboard app. Wake up devices on your network and see current status. `MIT` `Go/Docker`
- [Wakupator](https://github.com/Gibus21250/Wakupator) - Wake On LAN Machine Manager based on network traffic. `MIT` `C`
- [whois](https://github.com/KincaidYang/whois) - WHOIS/RDAP query API for domains, IP addresses, CIDR prefixes and ASNs, with unified JSON output, caching, API key authentication, batch queries and MCP support for AI assistants. (L0) `MIT` `Go/Docker`


<a id="note-taking--editors"></a>
### Note-taking & Editors 笔记与编辑器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Note taking](https://en.wikipedia.org/wiki/Note-taking) editors.

_Related: [Wikis 维基](#wikis)_

- [Blinko](https://blinko.space/) - Personal note tool with AI features. (L0) `AGPL-3.0` `Docker`
- [DailyTxT](https://github.com/PhiTux/DailyTxT) - Encrypted diary Web application to save your personal memories of each day. Includes a search function and encrypted file upload. (L0) `MIT` `Docker`
- [Docs](https://docs.numerique.gouv.fr/) - Collaborative note taking, wiki and documentation platform that scales. (L0) `MIT` `K8S`
- [draw.io](https://draw.io) - Diagram software for making flowcharts, process diagrams, org charts, UML, ER and network diagrams. (L0) `Apache-2.0` `Javascript/Docker`
- [flatnotes](https://github.com/dullage/flatnotes) - Database-less note-taking web app that utilises a flat folder of markdown files for storage. (L0) `MIT` `Docker`
- [HedgeDoc](https://hedgedoc.org/) - Realtime collaborative markdown notes on all platforms, formerly known as CodiMD and HackMD CE. (L0, L1) `AGPL-3.0` `Docker/Nodejs`
- [Joplin](https://joplinapp.org/) - Note taking application with markdown editor and encryption support for mobile and desktop platforms. Runs client-side and syncs through your own Nextcloud instance or similar (alternative to Evernote). (L0) `MIT` `Nodejs`
- [Jotty](https://jotty.page) - Lightweight but powerful alternative for managing your personal, file based, notes and checklists. (L0) `AGPL-3.0` `Docker`
- [Livebook](https://livebook.dev) - Realtime collaborative notebook app based on Markdown that supports running Elixir code snippets, TeX and Mermaid Diagrams. Easily deployed using Docker or Elixir. (L0) `Apache-2.0` `Elixir/Docker`
- [Many Notes](https://github.com/brufdev/many-notes) - Markdown note-taking web application designed for simplicity. `MIT` `Docker`
- [Memos](https://usememos.com/) - Knowledge base that works with a SQLite db file. (L0, L1) `MIT` `Docker/Go`
- [Neverkin](https://neverkin.com/) - Collaborative writing, worldbuilding and D&D-session-planning app. Tools for organizing your notes and stories. (L0, L1) `GPL-3.0` `Nodejs/Docker`
- [Note Mark](https://notemark.docs.enchantedcode.co.uk/) - Minimal web-based Markdown notes app. (L0) `AGPL-3.0` `Docker`
- [NoteDiscovery](https://www.notediscovery.com/) - Markdown note-taking app with plain-file storage, graph view, and MCP integration (alternative to Obsidian, Notion). (L0, L1) `MIT` `Docker/Python`
- [Overleaf](https://www.overleaf.com/) - Web-based collaborative LaTeX editor. (L0) `AGPL-3.0` `Ruby`
- [Plainpad](https://plainpad.org) - Modern note taking application for the cloud, utilizing the best features of progressive web apps technology. (L0, L1) `GPL-3.0` `PHP`
- [plumio](https://plumio.app/) - Markdown notes taking app with live preview, document encryption, multi-user support, multi-organization capabilities and more. (L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [SilverBullet](https://silverbullet.md/) - Note-taking application optimized for people with a hacker mindset. (L0, L1, L2) `MIT` `Docker/Deno`
- [Standard Notes](https://docs.standardnotes.com/self-hosting/getting-started) - Simple and private notes app. Protect your privacy while getting more done. That's Standard Notes. (L0, L1) `GPL-3.0` `Ruby`
- [TriliumNext Notes](https://github.com/TriliumNext/Trilium) - Cross-platform hierarchical note taking application with focus on building large personal knowledge bases (fork of Trilium Notes). `AGPL-3.0` `Nodejs/Docker/K8S`
- [Turtl](https://turtl.it/) - Totally private personal database and note taking app. (L0) `GPL-3.0` `CommonLisp`
- [Writing](https://josephernest.github.io/writing/) - Lightweight distraction-free text editor, in the browser (Markdown and LaTeX supported). No lag when writing. (L0) `MIT` `Javascript`


<a id="office-suites"></a>
### Office Suites 办公套件

**[`^        返回顶部        ^`](#awesome-selfhosted)**

An [office suite](https://en.wikipedia.org/wiki/List_of_office_suites) is a collection of productivity software usually containing at least a word processor, spreadsheet and a presentation program.

- [Collabora Online Development Edition](https://www.collaboraoffice.com/code) - Collabora Online Development Edition (CODE) is a powerful LibreOffice-based online office that supports all major document, spreadsheet and presentation file formats, which you can integrate in your own infrastructure. (L0) `MPL-2.0` `C++`
- [CryptPad](https://cryptpad.org) - Collaboration suite built to enable collaboration, synchronizing changes to documents in real time. (L0) `AGPL-3.0` `Nodejs/Docker`
- [Digislides](https://ladigitale.dev/digislides/) - Create multimedia presentations in a quick and easy way (documentation in French). (L0, L1) `AGPL-3.0` `Nodejs/PHP`
- [Etherpad](https://etherpad.org/) - Highly customizable online editor providing collaborative editing in real-time. (L0, L1) `Apache-2.0` `Nodejs/Docker`
- [Grist](https://getgrist.com/) - Next-generation spreadsheet with relational structure, formula-based access control, and a portable, self-contained format (alternative to Airtable). (L0, L1) `Apache-2.0` `Nodejs/Python/Docker`
- [ONLYOFFICE](https://helpcenter.onlyoffice.com/faq/server-opensource.aspx) - Office suite that enables you to manage documents, projects, team and customer relations in one place. (L0) `AGPL-3.0` `Nodejs/Docker`


<a id="password-managers"></a>
### Password Managers 密码管理器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [password manager](https://en.wikipedia.org/wiki/Password_manager) allows users to store, generate, and manage their passwords for local applications and online services.

- [AliasVault](https://www.aliasvault.net) - End-to-end encrypted password manager with a built-in email alias generator and server. (L0) `MIT` `Docker`
- [Bitwarden](https://bitwarden.com/) `⚠` - Password manager with a webapp, browser extension, and mobile app. (L0) `AGPL-3.0` `Docker/C#`
- [Passbolt](https://www.passbolt.com/) - Collaborative password manager. (L0) `AGPL-3.0` `PHP/deb/K8S/Docker`
- [PassIt](https://passit.io/) - Simple password manage with sharing features by group and user, but no administration interface. (L0, L1) `AGPL-3.0` `Docker/Python`
- [Psono](https://psono.com/) - Password manager for companies. (L0, L1) `Apache-2.0` `Python`
- [Teampass](https://teampass.net/) - Password manager dedicated for managing passwords in a collaborative way. One symmetric key is used to encrypt all shared/team passwords and stored server side in a file and the database. works on any server Apache, MySQL and PHP. (L0) `GPL-3.0` `PHP`
- [Vaultwarden](https://github.com/dani-garcia/vaultwarden) - Lightweight Bitwarden server API implementation written in Rust. `GPL-3.0` `Rust/Docker`


<a id="pastebins"></a>
### Pastebins 粘贴板

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [pastebin](https://en.wikipedia.org/wiki/Pastebin) is a type of online content-hosting service used for sharing and storing code and text.

- [1time](https://1time.io) - Zero-knowledge one-time secret sharing. Create a one-time link for a password, API key, or file. Encrypted client-side in the browser, never reaches the server in plaintext, self-destructs after the allowed number of views (one by default). (L0, L1) `MIT` `Docker`
- [BinPastes](https://github.com/querwurzel/BinPastes) - Minimal pastebin supporting client-side encryption, fulltext search, one-time messages. Intended for one to few users looking for a simple pastebin deployment. `Apache-2.0` `Java`
- [ByteStash](https://github.com/jordan-dalby/ByteStash) - Pastebin and file storage service with a simple web interface. Supports syntax highlighting, optional user authentication and public sharing. (L0) `GPL-3.0` `Docker`
- [Chiyogami](https://github.com/rhee876527/chiyogami) - Pastebin with API, client-side encryption, user accounts, syntax highlighting, markdown rendering, and more. (L0) `BSD-3-Clause` `Docker`
- [dpaste](https://dpaste.org/) - Simple pastebin with multiple text and code option, with short url result easy to remember. (L0) `MIT` `Docker/Python`
- [lesma](https://lesma.eu) - Simple paste app friendly with browser and command line. (L0, L1) `GPL-3.0` `Rust/Docker`
- [Local Content Share](https://github.com/Tanq16/local-content-share) - Store and share text snippets and files within your local network. `MIT` `Docker/Go`
- [not-th.re](https://not-th.re) - Simple paste sharing platform, with client side encryption, featuring the monaco browser-based code editor. (L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [Opengist](https://opengist.io) - Pastebin powered by Git. (L0, L1) `AGPL-3.0` `Docker/Go/Nodejs`
- [paaster](https://paaster.io) - End-to-end encrypted pastebin built with the objective of simplicity. (L0) `AGPL-3.0` `Docker`
- [pacebin](https://git.crueter.xyz/crueter/pacebin) - Super-minimal pastebin and file upload service focusing on small executable size, portability, and ease of configuration. (L0) `AGPL-3.0` `C`
- [Password Pusher](https://pwpush.com) - Dead-simple application to securely communicate passwords (or text) over the web. Passwords automatically expire after a certain number of views and/or time has passed. (L0) `Apache-2.0` `Docker/K8S/Ruby`
- [Pastefy](https://pastefy.app/) - Beautiful, simple and easy to deploy Pastebin with optional client encryption, multitab pastes, an API, a highlighted editor and more. (L0, L1) `MIT` `Docker/K8S/Java`
- [PrivateBin](https://privatebin.info/) - Minimalist pastebin/discussion board where the server has zero knowledge of hosted data. (L0, L1) `Zlib` `PHP`
- [rustypaste](https://github.com/orhun/rustypaste) - Minimal file upload/pastebin service. `MIT` `Rust`
- [Snipo](https://github.com/MohamedElashri/snipo) - Lightweight, self‑hosted snippet manager for saving and organizing code and text snippets with folders, tags, API, and GitHub Gist sync. (L0) `AGPL-3.0` `Go/Docker`
- [SnyPy](https://snypy.com) - On-prem code snippet manager. (L0, L1) `MIT` `Docker`
- [Sup3rS3cretMes5age](https://github.com/algolia/sup3rS3cretMes5age) - Very simple (to deploy and to use) secret message service using Hashicorp Vault as a secrets storage. `MIT` `Go`
- [Wastebin](https://github.com/matze/wastebin) - Lightweight, minimal and fast pastebin with an SQLite backend. (L0) `MIT` `Rust/Docker`
- [Yopass](https://github.com/jhaals/yopass) - Secure sharing of secrets, passwords and files. (L0) `Apache-2.0` `Go/Docker`


<a id="personal-dashboards"></a>
### Personal Dashboards 个人仪表盘

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Dashboards for accessing information and applications.

_Related: [Monitoring & Status Pages 监控与状态页](#monitoring--status-pages), [Bookmarks and Link Sharing 书签与链接分享](#bookmarks-and-link-sharing)_

- [Compass](https://adinhodovic.github.io/compass/) - Landing page for services, dashboards, and documents, with automatic discovery from sources such as Docker, Kubernetes, and Tailscale. (L0) `Apache-2.0` `Go/Docker/K8S`
- [Dashy](https://dashy.to/) - Feature-rich homepage for your homelab, with easy YAML configuration. (L0, L1) `MIT` `Nodejs/Docker`
- [Glance](https://github.com/glanceapp/glance) - Highly customizable dashboard that puts all your feeds in one place. `AGPL-3.0` `Docker/Go`
- [gobookmarks](https://github.com/arran4/gobookmarks) - Landing page to display bookmarks stored in GitHub, GitLab or local Git. `AGPL-3.0` `Go/Docker`
- [Heimdall](https://heimdall.site/) - Elegant solution to organise all your web applications. (L0) `MIT` `PHP`
- [Homarr](https://homarr.dev) - Sleek, modern dashboard with many integrations and web-based config. (L0) `MIT` `Docker/Nodejs`
- [Homepage by gethomepage](https://github.com/gethomepage/homepage) - Highly customizable homepage (or startpage / application dashboard) with Docker and service API integrations. `GPL-3.0` `Docker/Nodejs`
- [Homepage by tomershvueli](https://github.com/tomershvueli/homepage) - Simple, standalone PHP page that is your window to your server and the web. `MIT` `PHP`
- [Homer](https://github.com/bastienwirtz/homer) - Dead simple static homepage to expose your server services, with an easy yaml configuration and connectivity check. (L0) `Apache-2.0` `Docker/K8S/Nodejs`
- [Hubleys](https://github.com/knrdl/hubleys-dashboard) - Personal dashboards to organize links for multiple users via a central yaml config. `MIT` `Docker`
- [LinkStack](https://linkstack.org/) - Link all your social media platforms easily accessible on one page, customizable through an intuitive, easy to use user/admin interface (alternative to Linktree and Manylink). (L0, L1) `AGPL-3.0` `PHP/Docker`
- [LittleLink](https://littlelink.io/) - Simplistic approach for links in bio with 100+ branded buttons (alternative to Linktree). (L0, L1) `MIT` `Javascript`
- [Mafl](https://mafl.hywax.space/) - Minimalistic flexible homepage. (L0) `MIT` `Docker/Nodejs`
- [Nimbus](https://nimbus.turboot.com/) - Modern drag-and-drop homelab dashboard with visual editor and simple configuration. (L0, L1) `AGPL-3.0` `Docker`
- [Personal Management System](https://volmarg.github.io/) - Organize the essentials of everyday life, everything from a simple to-do list, and notes up to payments, and schedules. (L0, L1) `MIT` `Docker`
- [portkey](https://portkey.page) - Simple web portal that serves as a startup page, displaying a compilation of links and URLs, while also allowing the addition of custom pages, all managed through a single configuration file. (L0, L1) `AGPL-3.0` `Go/Docker`
- [ryot](https://github.com/ignisda/ryot) - Track various facets of your life - media, fitness, etc. (L0) `GPL-3.0` `Docker`
- [Starbase 80](https://github.com/notclickable-jordan/starbase-80) - Simple homepage with an iPad-style application grid, for mobile and desktop. One JSON configuration file. `MIT` `Docker`
- [Your Spotify](https://github.com/Yooooomi/your_spotify) `⚠` - Allows you to record your Spotify listening activity and have statistics about them served through a Web application. `MIT` `Nodejs/Docker`


<a id="photo-galleries"></a>
### Photo Galleries 相册

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [gallery](https://en.wikipedia.org/wiki/Gallery_Software) is software that helps the user publish or share photos, pictures, videos or other digital media.

_Related: [Static Site Generators 静态站点生成器](#static-site-generators), [Media Streaming - Video Streaming 媒体流 - 视频流](#media-streaming---video-streaming), [Content Management Systems (CMS) 内容管理系统（CMS）](#content-management-systems-cms)_

- [Chevereto](https://chevereto.com/) - Ultimate image sharing software. Create your very own personal image hosting website in just minutes. (L0) `AGPL-3.0` `PHP/Docker`
- [ChronoFrame](https://chronoframe.bh8.ga/) - Personal gallery application with online photo management, supporting Live/Motion Photos, and explore map. (L0, L1) `MIT` `Nodejs/Docker`
- [Damselfly](https://damselfly.info) - Fast server-based photo management system for large collections of images. Includes face detection, face & object recognition, powerful search, and EXIF Keyword tagging. Runs on Linux, MacOS and Windows. (L0) `GPL-3.0` `Docker/C#/.NET`
- [Ente](https://ente.com/) - End-to-end encrypted photo-sharing platform (alternative to Google Photos, Apple Photos). (L0) `AGPL-3.0` `Docker/Nodejs/Go`
- [HomeGallery](https://home-gallery.org) - Browse personal photos and videos featuring tagging, mobile-friendly, and AI powered image discovery. (L0, L1) `MIT` `Nodejs/Docker`
- [Immich Kiosk](https://github.com/damongolding/immich-kiosk) - Lightweight slideshow for running on kiosk devices and browsers that uses Immich as a data source. (L0) `GPL-3.0` `Docker/Go`
- [Immich](https://immich.app/) - Photo and video backup solution directly from your mobile phone (alternative to Google Photos). (L0, L1) `AGPL-3.0` `Docker`
- [LibrePhotos](https://github.com/LibrePhotos/librephotos) - Photo management service with a slight focus on cool graphs (alternative to Google Photos). (L0) `MIT` `Python/Docker`
- [Lychee](https://lycheeorg.github.io/) - Grid and album based photo-management-system. (L0) `MIT` `PHP/Docker`
- [Mediagoblin](https://mediagoblin.org) - Media publishing platform that anyone can run (alternative to Flickr, YouTube, SoundCloud). (L0) `AGPL-3.0` `Python`
- [Memtly](https://docs.memtly.com/) - Event photo sharing platform and gallery with slideshow that allows guests to view and share memories via a QR code. (L0, L1) `GPL-3.0` `C#/Docker`
- [Nextcloud Memories](https://memories.gallery/) - Fast, modern and advanced photo management suite. Runs as a Nextcloud app. (L0, L1) `AGPL-3.0` `PHP`
- [Photofield](https://github.com/SmilyOrg/photofield) - Experimental fast photo viewer. `MIT` `Docker/Go`
- [PhotoPrism](https://photoprism.org) - Personal photo management powered by Go and Google TensorFlow. Browse, organize, and share your personal photo collection, using the latest technologies to automatically tag and find pictures. (L0, L1) `AGPL-3.0` `Go/Docker`
- [Photoview](https://photoview.github.io/) - Simple and user-friendly photo gallery for personal servers. It is made for photographers and aims to provide an easy and fast way to navigate directories, with thousands of high resolution photos. (L0, L1) `GPL-3.0` `Go/Docker`
- [PiGallery 2](https://bpatrik.github.io/pigallery2/) - Directory-first photo gallery website, with a rich UI, optimised for running on low resource servers. (L0) `MIT` `Docker/Nodejs`
- [Piwigo](https://piwigo.org/) - Photo gallery software for the web, built by an active community of users and developers. (L0) `GPL-2.0` `PHP`
- [SPIS](https://github.com/gbbirkisson/spis) - Simple, lightweight and fast media server with decent mobile support. `GPL-3.0` `Docker/Rust`
- [This week in past](https://github.com/RouHim/this-week-in-past) - Aggregates images taken this week, from previous years and presents them on a web page with a simple slideshow. `MIT` `Docker/Rust`
- [Thumbor](http://thumbor.org/) - Smart imaging service and enables on-demand cropping, resizing, applying filters and optimizing images. (L0) `MIT` `Python/Docker`
- [Zenphoto](https://www.zenphoto.org/) - Gallery and CMS project. (L0) `GPL-2.0` `PHP`


<a id="polls-and-events"></a>
### Polls and Events 投票与活动

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Software for organising [polls](https://en.wikipedia.org/wiki/Opinion_poll) and [events](https://en.wikipedia.org/wiki/Event).

_Related: [Booking and Scheduling 预订与排程](#booking-and-scheduling)_

- [Bitpoll](https://github.com/fsinfuhh/Bitpoll) - Conduct polls about dates, times or general questions. (L0) `GPL-3.0` `Docker/Python`
- [Bracket](https://docs.bracketapp.nl/) - Flexible tournament system to build a tournament setup, add teams, schedule matches, keep track of scores and present ranking live to the public. (L0, L1) `AGPL-3.0` `Docker/Nodejs`
- [Christmas Community](https://github.com/Wingysam/Christmas-Community) - Create a simple place for your entire family to use to find gifts that people want, and to avoid double-gifting. `AGPL-3.0` `Docker/Nodejs`
- [Claper](https://claper.co/) - Add Q&A, polls, quizzes, forms, live captions and reactions to your slides (alternative to Slido, AhaSlides and Mentimeter). (L0) `GPL-3.0` `Elixir/Docker`
- [ClearFlask](https://clearflask.com) - Community-feedback tool for managing incoming feedback and prioritizing a public roadmap (alternative to Canny, UserVoice, Upvoty). (L0, L1) `AGPL-3.0` `Docker`
- [docassemble](https://docassemble.org/) - System for guided interviews and document assembly, based on Python, YAML, and Markdown. (L0, L1) `MIT` `Docker/Python`
- [EventSchedule](https://eventschedule.com/) - Share events, sell tickets, and bring communities together. (L0) `AAL` `PHP/Docker`
- [Fider](https://fider.io) - Open platform to collect and prioritize feedback (alternative to UserVoice). (L0, L1) `MIT` `Docker`
- [Formbricks](https://formbricks.com) - Experience Management Suite built on the largest survey stack worldwide. Gracefully gather feedback at every step of the customer journey to know what your customers need. (L0, L1) `AGPL-3.0` `Nodejs/Docker`
- [Framadate](https://framadate.org/abc/) - Online service for planning an appointment or make a decision quickly and easily: Make a poll, Define dates or subjects to choose, Send the poll link to your friends or colleagues, Discuss and make a decision. (L0, L1) `CECILL-B` `PHP`
- [Gancio](https://gancio.org/) - Local community event and agenda sharing. (L0, L1) `AGPL-3.0` `Nodejs`
- [gathio](https://docs.gath.io/) - Self-destructing, shareable, no-registration event pages. (L0, L1) `GPL-3.0` `Nodejs/Docker`
- [HeyForm](https://heyform.net) - Form builder that allows anyone to create engaging conversational forms for surveys, questionnaires, quizzes, and polls. (L0) `AGPL-3.0` `Docker`
- [hitobito](https://hitobito.com) - Manage complex group hierarchies with members, events and a lot more. (L0, L1) `AGPL-3.0` `Ruby`
- [LimeSurvey](https://www.limesurvey.org) - Feature-rich web-based polling software. Supports extensive survey logic. (L0, L1) `GPL-2.0` `PHP`
- [Meetable](https://events.indieweb.org) - Minimal events aggregator. (L0) `MIT` `PHP`
- [Mobilizon](https://mobilizon.org) - Federated tool that helps you find, create and organise events and groups. (L0) `AGPL-3.0` `Elixir/Docker`
- [OpnForm](https://opnform.com) - Beautiful form builder. (L0, L1) `AGPL-3.0` `PHP/Nodejs/Docker`
- [Revel](https://www.letsrevel.io) `⚠` - Community-focused event management and ticketing platform. (L0, L1, L2) `MIT` `Python/Docker`


<a id="proxy"></a>
### Proxy 代理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [proxy](https://en.wikipedia.org/wiki/Proxy_server) is a server application that acts as an intermediary between a client requesting a resource and the server providing that resource. This section about forward (i.e. outgoing) proxies. For reverse proxies, see the Web Server section.

_Related: [Web Servers Web 服务器](#web-servers)_

- [g3proxy](https://g3-project.readthedocs.io/projects/g3proxy/en/latest/) - Forward proxy server supporting proxy chaining, protocol inspection, MITM Interception, ICAP adaptation and transparent proxy. (L0) `Apache-2.0` `Rust/deb`
- [GitProxy](https://git-proxy.finos.org/) - Proxy for Git that applies rules and workflows to all outgoing git push operations and ensures they are compliant. It supports both HTTP/HTTPS and SSH protocols with security scanning and validation. (L0) `Apache-2.0` `Nodejs/Docker`
- [imagor](https://github.com/cshum/imagor) - Fast, secure image processing server and Go library built on libvips, with on-demand resizing, cropping, filtering, format conversion and image composition, signed URLs and streaming pipelines for high-concurrency throughput. `Apache-2.0` `Docker`
- [imgproxy](https://imgproxy.net/) - Fast and secure standalone server for resizing and converting remote images. (L0) `MIT` `Go/Docker/K8S`
- [Outline Server](https://getoutline.org/) - Proxy server that runs a Shadowsocks instance for each access key and a REST API to manage the access keys. (L0) `Apache-2.0` `Docker/Nodejs`
- [Privoxy](https://www.privoxy.org) - Non-caching web proxy with advanced filtering capabilities for enhancing privacy, modifying web page data and HTTP headers, controlling access, and removing ads and other obnoxious Internet junk. `GPL-2.0` `C/deb`
- [sish](https://github.com/antoniomika/sish) - HTTP(S)/WS(S)/TCP tunnels to localhost using only SSH (serveo/ngrok alternative). `MIT` `Go/Docker`
- [socks5-proxy-server](https://github.com/nskondratev/socks5-proxy-server) - SOCKS5 proxy server with built-in authentication and Telegram-bot for user management and user statistics on data spent (handy when you pay per GB of data). It is dockerised and simple to install. `Apache-2.0` `Docker`
- [Squid](http://www.squid-cache.org/) - Caching proxy for the Web supporting HTTP, HTTPS, FTP, and more. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages. (L0) `GPL-2.0` `C/deb`
- [Tinyproxy](https://tinyproxy.github.io/) - Light-weight HTTP/HTTPS proxy daemon. (L0) `GPL-2.0` `C/deb`


<a id="recipe-management"></a>
### Recipe Management 食谱管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Software and tools for managing [recipes](https://en.wikipedia.org/wiki/Recipe).

- [Bar Assistant](https://barassistant.app/) - Manage your home bar while adding your ingredients, searching for cocktails and creating custom cocktail recipes. (L0, L1) `MIT` `PHP/Docker`
- [CookCLI](https://cooklang.org) - Command-line tool for automating meal planning and shopping with Cooklang recipes, scriptable for UNIX workflows, includes web server. (L0) `MIT` `Rust`
- [Fork Recipes](https://mikebgrep.github.io/forkapi/latest/clients/) - Manage your food recipes with simplicity. (L0) `BSD-3-Clause` `Docker`
- [ManageMeals](https://managemeals.com/) - Manage recipes, import recipes by URL and organize them without any ads or unnecessary text. (L0) `GPL-3.0` `Docker`
- [Mealie](https://nightly.mealie.io/) - Material design inspired recipe manager with category and tag management, shopping-lists, meal-planner, and site customizations. Mealie is focused on simple user interactions to keep the whole family using the app. (L0, L1) `MIT` `Python`
- [RecipeSage](https://github.com/julianpoy/recipesage) - Recipe keeper, meal plan organizer, and shopping list manager that can import recipes directly from any URL. (L0) `AGPL-3.0` `Nodejs`
- [Recipya](https://recipes.musicavis.ca) - Clean, simple and powerful recipe manager your whole family will enjoy. (L0, L1) `GPL-3.0` `Docker/Go`
- [Tamari](https://tamariapp.com) - Recipe manager web app with a built-in collection of recipes. Organize by favorites and categories, create shopping lists, and plan meals. (L0, L1) `GPL-3.0` `Docker/Python`
- [Vanilla Cookbook](https://vanilla-cookbook.readthedocs.io/en/) - Recipe manager designed with complexity under the hood, keeping the user experience as uncluttered, simply vanilla as possible. (L0) `GPL-3.0` `Docker/Nodejs`
- [What To Cook?](https://github.com/kassner/whattocook) - Get a recipe to cook today, based on the ingredients you have at home. `AGPL-3.0` `Docker`


<a id="remote-access"></a>
### Remote Access 远程访问

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Remote desktop](https://en.wikipedia.org/wiki/Remote_desktop_software) and [SSH](https://en.wikipedia.org/wiki/Secure_Shell) servers and web interfaces for remote management of computer systems.

- [Cardea](https://github.com/hectorm/cardea) - SSH bastion server with access control, session recording, and optional TPM-backed key protection. `EUPL-1.2` `Go/Docker`
- [Engity's Bifröst](https://bifroest.engity.org/) - Highly customizable SSH server with several ways to authorize a user and options where and how to execute a user's session. (L0) `Apache-2.0` `Go/Docker`
- [Firezone](https://www.firezone.dev/) - Secure remote access gateway that supports the WireGuard protocol. It offers a Web GUI, 1-line install script, multi-factor auth (MFA), and SSO. (L0) `Apache-2.0` `Elixir/Docker`
- [Guacamole](https://guacamole.apache.org) - Clientless remote desktop gateway supporting standard protocols like VNC and RDP. (L0) `Apache-2.0` `Java/C`
- [MeshCentral](https://meshcentral.com/) - Run your own web server to remotely manage and control computers on a local network or anywhere on the internet. (L0) `Apache-2.0` `Nodejs`
- [ShellHub](https://www.shellhub.io) - Modern SSH server for remotely accessing linux devices via command line (using any SSH client) or web-based user interface (alternative to sshd). (L0) `Apache-2.0` `Docker`
- [Sshwifty](https://github.com/nirui/sshwifty) - SSH and Telnet connector made for the Web. (L0) `AGPL-3.0` `Go/Docker`
- [Termix](https://docs.termix.site/) - Clientless web-based server management platform with SSH terminal, tunneling, and file editing capabilities. (L0) `Apache-2.0` `Docker`
- [Warpgate](https://github.com/warp-tech/warpgate) - Fully transparent SSH, HTTPS, Kubernetes, MySQL and Postgres bastion/PAM that doesn't need additional client-side software. `Apache-2.0` `Rust/Docker`


<a id="resource-planning"></a>
### Resource Planning 资源规划

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Software and tools to help with [resource and supply planning](https://en.wikipedia.org/wiki/Resource_planning), including [enterprise resource and supply planning (ERP)](https://en.wikipedia.org/wiki/Enterprise_resource_planning).

_Related: [Money, Budgeting & Management 金钱、预算与管理](#money-budgeting--management), [Inventory Management 库存管理](#inventory-management)_

- [Dolibarr](https://www.dolibarr.org/) - Modern CRM software package to manage your company or foundation activity (contacts, suppliers, invoices, orders, stocks, agenda, accounting, ...). (L0, L1) `GPL-3.0` `PHP/deb`
- [ERPNext](https://frappe.io/erpnext) - ERP system to help you run your business. (L0) `GPL-3.0` `Python/Docker`
- [farmOS](https://farmos.org/) - Web-based farm record keeping application. (L0, L1) `GPL-2.0` `PHP/Docker`
- [grocy](https://grocy.info/) - ERP beyond your fridge. Groceries & household management solution for your home. (L0, L1) `MIT` `PHP/Docker`
- [LedgerSMB](https://ledgersmb.org/) - Integrated accounting and ERP system for small and midsize businesses, with double entry accounting, budgeting, invoicing, quotations, projects, orders and inventory management, shipping and more. (L0) `GPL-2.0` `Docker/Perl`
- [Odoo](https://www.odoo.com) - Suite of web based business apps for ERP. (L0, L1) `LGPL-3.0` `Python/deb/Docker`
- [OFBiz](https://ofbiz.apache.org/) - Enterprise Resource Planning system with a suite of business applications flexible enough to be used across any industry. (L0) `Apache-2.0` `Java`
- [Tryton](https://www.tryton.org/) - Business solution. (L0, L1) `GPL-3.0` `Python`


<a id="search-engines"></a>
### Search Engines 搜索引擎

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [search engine](https://en.wikipedia.org/wiki/Search_engine_(computing)) is an [information retrieval system](https://en.wikipedia.org/wiki/Information_retrieval) designed to help find information stored on a computer system. This includes [Web search engines](https://en.wikipedia.org/wiki/Web_search_engine).

- [Aleph](https://aleph.occrp.org/) - Tool for indexing large amounts of both documents (PDF, Word, HTML) and structured (CSV, XLS, SQL) data for easy browsing and search. It is built with investigative reporting as a primary use case. (L0, L1) `MIT` `Docker/K8S`
- [Amgix](https://amgix.io) - Hybrid search engine built for flexible deployment and real-world messy data. (L0, L1, L2) `AGPL-3.0` `Docker/K8S`
- [Apache Solr](https://lucene.apache.org/solr/) - Enterprise search platform featuring full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, and rich document (e.g., Word, PDF) handling. (L0) `Apache-2.0` `Java/Docker/K8S`
- [Fess](https://fess.codelibs.org/) - Powerful and easily deployable Enterprise Search Server. (L0, L1) `Apache-2.0` `Java/Docker`
- [Hister](https://hister.org/) - Personal web search engine with automatic indexing of visited websites. Supports offline local result previews, local files, multi-user handling and optional semantic search. (L0, L1) `AGPL-3.0` `Go/Docker`
- [Manticore Search](https://github.com/manticoresoftware/manticoresearch/) - Full-text search and data analytics, with fast response time for small, medium and big data (alternative to Elasticsearch). `GPL-3.0` `Docker/deb/C++/K8S`
- [MeiliSearch](https://www.meilisearch.com) - Ultra relevant, instant and typo-tolerant full-text search API. (L0) `MIT` `Rust/Docker/deb`
- [Meme Search](https://github.com/neonwatty/meme-search) - AI-powered meme search engine. Automatically extracts descriptions from images using vision-language models, then indexes with vector embeddings for semantic and keyword search. (L0) `Apache-2.0` `Docker`
- [OpenSearch](https://opensearch.org) - Distributed and RESTful search engine. (L0) `Apache-2.0` `Java/Docker/K8S/deb`
- [SearXNG](https://docs.searxng.org/) `⚠` - Internet metasearch engine which aggregates results from various search services and databases (fork of Searx). (L0) `AGPL-3.0` `Python/Docker`
- [Sosse](https://sosse.readthedocs.io/en/stable/) - Selenium based search engine and crawler with offline archiving. (L0) `AGPL-3.0` `Python/Docker`
- [Typesense](https://typesense.org) - Blazing fast, typo-tolerant search engine optimized for developer happiness and ease of use. (L0) `GPL-3.0` `C++/Docker/K8S/deb`
- [Websurfx](https://github.com/neon-mmd/websurfx) `⚠` - Aggregate results from other search engines (metasearch engine) without ads while keeping privacy and security in mind. It is extremely fast and provides a high level of customization (alternative to SearX). `AGPL-3.0` `Rust/Docker`
- [Yacy](https://yacy.net/en/index.html) - Peer based, decentralized search engine server. (L0) `GPL-2.0` `Java/Docker/K8S`


<a id="self-hosting-solutions"></a>
### Self-hosting Solutions 自托管方案

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Software for easy installation, management and configuration of self-hosted services and applications.

- [DietPi](https://dietpi.com/) - Minimal Debian OS optimized for single-board computers, which allows you to easily install and manage several services for selfhosting at home. (L0) `GPL-2.0` `Shell`
- [DockSTARTer](https://dockstarter.com/) - DockSTARTer helps you get started with home server apps running in Docker. (L0) `MIT` `Shell`
- [Dropserver](https://dropserver.org) - Application platform for your personal web services. (L0) `Apache-2.0` `Go/Deno`
- [FreedomBox](https://freedombox.org/) - Community project to develop, design and promote personal servers running free software for private, personal, communications. (L0) `AGPL-3.0` `Python/deb`
- [HomeButler](https://homebutler.dev) - Installs and manages a curated catalog of applications via Docker Compose, maps containers and exposed ports, verifies backups restore, and reports what changed since the last run with CLI, JSON, web and MCP interfaces. (L0) `MIT` `Docker/Go`
- [HomelabOS](https://homelabos.com) - Offline privacy-centric data-center. Deploy over 100 services with a few commands. (L0) `MIT` `Docker`
- [HomeServerHQ](https://www.homeserverhq.com/) - All-in-one home server infrastructure and installer. Have a fully configured email server, VPN, and public website(s) set up in less than an hour, even behind CGNAT. (L0) `GPL-3.0` `Shell`
- [LibreServer](https://libreserver.org/) - Home server configuration based on Debian. (L0) `AGPL-3.0` `Shell`
- [Mother-of-All-Self-Hosting](https://github.com/mother-of-all-self-hosting/mash-playbook) - Ansible playbook which helps you host services as Docker containers on your own server. `AGPL-3.0` `Ansible/Docker`
- [NextCloudPi](https://github.com/nextcloud/nextcloudpi) - Nextcloud preinstalled and preconfigured, with a text and web management interface and all the tools needed to self host private data. With installation images for Raspberry Pi, Odroid, Rock64, Docker, and a curl installer for Armbian/Debian. `GPL-2.0` `Shell/PHP`
- [Nirvati](https://nirvati.org) - Easily 1-click spin up popular apps from a convenient web interface. (L0) `AGPL-3.0` `Rust/K8S`
- [OpenMediaVault](https://www.openmediavault.org/) - Network attached storage (NAS) solution based on Debian Linux. It contains services like SSH, (S)FTP, SMB/CIFS, DAAP media server, RSync, BitTorrent client and many more. (L0) `GPL-3.0` `PHP`
- [Sandstorm](https://sandstorm.io/) - Personal server for running apps on your own hardware easily and securely. (L0, L1) `Apache-2.0` `C++/Shell`
- [Self Host Blocks](https://github.com/ibizaman/selfhostblocks) `⚠` - Modular server management based on NixOS modules and focused on best practices. `AGPL-3.0` `Nix`
- [StartOS](https://start9.com) - Browser-based, graphical Operating System (OS) that makes running a personal server as easy as running a personal computer. (L0) `MIT` `Rust`
- [Syncloud](https://syncloud.org/) - OS with an app store and automatic updates for apps such as Nextcloud, Jellyfin, Bitwarden and Paperless, including HTTPS, a domain name and remote access without a public IP. (L0) `GPL-3.0` `Go/Shell`
- [Tipi](https://runtipi.io/) - Homeserver manager. One command setup, one click installs for your favorite home server apps. (L0) `GPL-3.0` `Shell`
- [UBOS](https://ubos.net/) - Linux distro that runs on indie boxes (personal servers and IoT devices). Single-command installation and management of apps - Jenkins, Mediawiki, Owncloud, WordPress, etc., and other features. `GPL-3.0` `Perl`
- [Websoft9](https://www.websoft9.com) `⚠` - GitOps-driven, multi-application hosting for cloud servers and home servers, one-click deployment of 200+ apps. (L0, L1, L2) `LGPL-3.0` `Shell/Python`
- [WikiSuite](https://wikisuite.org) - Most comprehensive and integrated Free / Libre enterprise software suite. (L0) `GPL-3.0/LGPL-2.1/Apache-2.0/MPL-2.0/MPL-1.1/MIT/AGPL-3.0` `Shell/Perl/deb`
- [xsrv](https://xsrv.readthedocs.io/) - Install and manage services/applications on your own server(s). (L0) `GPL-3.0` `Ansible/Shell`
- [YunoHost](https://yunohost.org/) - Server operating system aiming to make self-hosting accessible to everyone. (L0, L1) `AGPL-3.0` `Python/Shell`


<a id="software-development"></a>
### Software Development 软件开发

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Software development](https://en.wikipedia.org/wiki/Software_development) is the process of conceiving, specifying, designing, programming, documenting, testing, and bug fixing involved in creating and maintaining applications, frameworks, or other software components.

**请访问 [Software Development - API Management](#software-development---api-management), [Software Development - Continuous Integration & Deployment](#software-development---continuous-integration--deployment), [Software Development - FaaS & Serverless](#software-development---faas--serverless), [Software Development - IDE & Tools](#software-development---ide--tools), [Software Development - Localization](#software-development---localization), [Software Development - Low Code](#software-development---low-code), [Software Development - Project Management](#software-development---project-management), [Software Development - Testing](#software-development---testing), [Software Development - Feature Toggle](#software-development---feature-toggle)**



<a id="software-development---api-management"></a>
### Software Development - API Management 软件开发 - API 管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[API management](https://en.wikipedia.org/wiki/API_management) is the process of creating and publishing [application programming interfaces (APIs)](https://en.wikipedia.org/wiki/API), enforcing their usage policies, controlling access, nurturing the subscriber community, collecting and analyzing usage statistics, and reporting on performance. 

- [Aastro](https://voidrunner3074.github.io/aastro-docs) - Extensible API Gateway written in Go. (L0) `Apache-2.0` `Go/Docker`
- [DreamFactory](https://www.dreamfactory.com/) - Turns any SQL/NoSQL/Structured data into Restful API. (L0) `Apache-2.0` `PHP/Docker/K8S`
- [Fusio](https://www.fusio-project.org/) - API management platform which helps to build and manage REST APIs. (L0, L1) `AGPL-3.0` `PHP/Docker`
- [Graphweaver](https://graphweaver.com/) - Turn multiple data sources into a single GraphQL API. (L0) `MIT` `Nodejs`
- [Hasura](https://hasura.io) - Fast, instant realtime GraphQL APIs on Postgres with fine grained access control, also trigger webhooks on database events. (L0) `Apache-2.0` `Haskell/Docker/K8S`
- [Hoppscotch Community Edition](https://hoppscotch.io) - Fast and beautiful API request builder. (L0) `MIT` `Nodejs/Docker`
- [Kong](https://konghq.com/kong/) - Microservice API Gateway and Platform. (L0) `Apache-2.0` `Lua/Docker/K8S/deb`
- [Lura](https://luraproject.org/) - High-performance API Gateway. (L0) `Apache-2.0` `Go`
- [Opik](https://www.comet.com/site/products/opik/) `⚠` - Evaluate, test, and ship LLM applications with a suite of observability tools to calibrate language model outputs across your dev and production lifecycle. (L0) `Apache-2.0` `Docker/Python`
- [Para](https://paraio.org) - Flexible and modular backend framework/server for object persistence, API development and authentication. (L0) `Apache-2.0` `Java/Docker`
- [Svix](https://svix.com) - Webhooks as a service that makes it super easy for API providers to send webhooks. (L0) `MIT` `Docker/Rust`
- [Tyk](https://tyk.io) - Fast and scalable API Gateway. Out of the box, Tyk offers an API Management Platform with an API Gateway, API Analytics, Developer Portal and API Management Dashboard. (L0) `MPL-2.0` `Go/Docker/K8S`


<a id="software-development---continuous-integration--deployment"></a>
### Software Development - Continuous Integration & Deployment 软件开发 - 持续集成与部署

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) and [Continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment) software and tools.

**请访问 [awesome-sysadmin/Continuous Integration & Continuous Deployment](https://github.com/awesome-foss/awesome-sysadmin#continuous-integration--continuous-deployment)**

_Related: [Automation 自动化](#automation)_



<a id="software-development---faas--serverless"></a>
### Software Development - FaaS & Serverless 软件开发 - FaaS 与无服务器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Serverless computing](https://en.wikipedia.org/wiki/Serverless_computing), [Function as a Service (FaaS)](https://en.wikipedia.org/wiki/Function_as_a_service) and [Platform as a Service (Paas)](https://en.wikipedia.org/wiki/Platform_as_a_service) management software.

**请访问 [awesome-sysadmin/PaaS](https://github.com/awesome-foss/awesome-sysadmin#paas)**



<a id="software-development---feature-toggle"></a>
### Software Development - Feature Toggle 软件开发 - 功能开关

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [feature toggle](https://en.wikipedia.org/wiki/Feature_toggle) in software development provides an alternative to maintaining multiple feature branches in source code.

_Related: [Software Development - IDE & Tools 软件开发 - IDE 与工具](#software-development---ide--tools)_

- [Featbit](https://www.featbit.co/) - Enterprise-grade feature flag platform that you can self-host. (L0) `MIT` `Docker/K8S`
- [Flagsmith](https://flagsmith.com) - Dashboard, API and SDKs for adding Feature Flags to your applications (alternative to LaunchDarkly). (L0) `BSD-3-Clause` `Docker/K8S`
- [Flipt](https://flipt.io) - Feature flag solution with support for multiple data backends (alternative to LaunchDarkly). (L0) `GPL-3.0` `Docker/K8S/Go`
- [GO Feature Flag](https://gofeatureflag.org) - Simple, complete, and lightweight feature flag solution (alternative to LaunchDarkly). (L0) `MIT` `Go`
- [Nona](https://nonaconfig.com) - Remote configuration and feature flag service with a single REST API, multiple environments, and official JavaScript and .NET clients (alternative to Firebase Remote Config). (L0) `Apache-2.0` `Docker`


<a id="software-development---ide--tools"></a>
### Software Development - IDE & Tools 软件开发 - IDE 与工具

**[`^        返回顶部        ^`](#awesome-selfhosted)**

An [integrated development environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment) is a software application that provides comprehensive facilities to computer programmers for software development.

_Related: [Software Development - Low Code 软件开发 - 低代码](#software-development---low-code)_

- [Atheos](https://www.atheos.io) - Web-based IDE framework with a small footprint and minimal requirements, continued from Codiad. (L0) `MIT` `PHP/Docker`
- [code-server](https://github.com/coder/code-server) - VS Code in the browser, hosted on a remote server. `MIT` `Nodejs/Docker`
- [Coder](https://coder.com/) - Remote development machines on your own infrastructure. (L0) `AGPL-3.0` `Go/Docker/K8S/deb`
- [Eclipse Che](https://www.eclipse.org/che/) - Workspace server and cloud IDE. (L0) `EPL-1.0` `Docker/Java`
- [Hopp](https://gethopp.app) - Remote pair programming app with low-latency 4K screen sharing, drawing, and remote control, with clients for macOS and Windows (alternative to Tuple, Pop, Drovio). (L0) `AGPL-3.0` `Docker`
- [Judge0 CE](https://judge0.com) - API to compile and run source code. (L0) `GPL-3.0` `Docker`
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) - Web-based environment for interactive and reproducible computing. (L0, L1) `BSD-3-Clause` `Python/Docker`
- [Langfuse](https://langfuse.com) - LLM engineering platform for model tracing, prompt management, and application evaluation. Langfuse helps teams collaboratively debug, analyze, and iterate on their LLM applications such as chatbots or AI agents. (L0, L1, L2) `MIT` `Docker`
- [LiveCodes](https://livecodes.io/docs/features/self-hosting) `⚠` - Feature-rich client-side code playground for React, Vue, Svelte, Solid, Typescript, Python, Go, Ruby, PHP and 90+ other languages. (L0, L1) `MIT` `Nodejs`
- [Lowdefy](https://www.lowdefy.com/) - Build internal tools, BI dashboards, admin panels, CRUD apps and workflows in minutes using YAML / JSON. (L0) `Apache-2.0` `Nodejs/Docker`
- [RapidForge](https://rapidforge.io/) - Lightweight platform for building webhooks, scheduled tasks and pages. Implement your logic with Bash or Lua. (L0) `Apache-2.0` `Go/Nodejs`
- [RStudio Server](https://www.rstudio.com/products/rstudio/#Server) - Web browser based IDE for R. (L0) `AGPL-3.0` `Java/C++`


<a id="software-development---localization"></a>
### Software Development - Localization 软件开发 - 本地化

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Localization](https://en.wikipedia.org/wiki/Internationalization_and_localization) is the process of adapting code and software to other languages.

- [Accent](https://www.accent.reviews/) - Developer-oriented translation tool. (L0) `BSD-3-Clause` `Elixir/Docker`
- [Tolgee](https://tolgee.io) - Developer & translator friendly web-based localization platform enabling users to translate directly in the app they develop. (L0) `Apache-2.0` `Docker/Java`
- [Traduora](https://traduora.co) - Translation management platform for teams. (L0) `AGPL-3.0` `Docker/K8S/Nodejs`
- [Weblate](https://weblate.org) - Web-based translation tool with tight version control integration. (L0) `GPL-3.0` `Python/Docker/K8S`


<a id="software-development---low-code"></a>
### Software Development - Low Code 软件开发 - 低代码

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [low-code](https://en.wikipedia.org/wiki/Low-code_development_platform) development platform (LCDP) provides a development environment used to create application software through a graphical user interface.

_Related: [Software Development - IDE & Tools 软件开发 - IDE 与工具](#software-development---ide--tools)_

- [Appsmith](https://www.appsmith.com/) - Build admin panels, CRUD apps and workflows. Build everything you need, 10x faster. (L0) `Apache-2.0` `Java/Docker/K8S`
- [Appwrite](https://appwrite.io) - End to end backend server for web, native, and mobile developers 🚀. (L0) `BSD-3-Clause` `Docker`
- [Halo](https://www.halo.run) - Powerful and easy-to-use website building tool (documentation in Chinese). (L0, L1, L2) `GPL-3.0` `Java/Docker`
- [Manifest](https://manifest.build) - Complete backend that fits into 1 YAML file. (L0, L1) `MIT` `Nodejs`
- [PocketBase](https://pocketbase.io/) - Backend for your next SaaS and Mobile app in one file. (L0) `MIT` `Go/Docker`
- [Saltcorn](https://saltcorn.com/) - No-code database application builder for web and mobile applications. One platform for user interface, data backend, durable workflows, email, PDF generation, and AI applications. (L0) `MIT` `Docker/Nodejs`
- [SQLPage](https://sql-page.com) - SQL-only dynamic website builder. (L0) `MIT` `Rust/Docker`
- [ToolJet](https://tooljet.io/) - Low-code framework to build & deploy internal tools with minimal engineering effort (alternative to Retool and Mendix). (L0) `GPL-3.0` `Nodejs/Docker/K8S`
- [TrailBase](https://trailbase.io/) - Open, sub-millisecond, single-executable FireBase alternative with type-safe REST & realtime APIs, built-in JS/TS runtime, auth & admin UI. (L0, L1) `OSL-3.0` `Rust/Docker`


<a id="software-development---project-management"></a>
### Software Development - Project Management 软件开发 - 项目管理

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Tools and software for [software project management](https://en.wikipedia.org/wiki/Software_project_management).

_Related: [Ticketing 工单](#ticketing), [Task Management & To-do Lists 任务管理与待办清单](#task-management--to-do-lists)_

- [Cgit](https://git.zx2c4.com/cgit/about/) - Fast lightweight web interface for git repositories. (L0) `GPL-2.0` `C`
- [Forgejo](https://forgejo.org) - Lightweight software forge focused on scaling, federation, and privacy (fork of Gitea). (L0, L1, L2) `MIT` `Docker/Go`
- [Fossil](https://www.fossil-scm.org/index.html/doc/trunk/www/index.wiki) - Distributed version control system featuring wiki and bug tracker. `BSD-2-Clause-FreeBSD` `C`
- [Gerrit](https://www.gerritcodereview.com/) - Code review and project management tool for Git-based projects. (L0) `Apache-2.0` `Java/Docker`
- [gitbucket](https://gitbucket.github.io/) - Git platform powered with easy installation, high extensibility & GitHub API compatibility (alternative to GitHub). (L0) `Apache-2.0` `Scala/Java`
- [Gitea](https://gitea.com) - Git with a cup of tea! Painless all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD. (L0, L1) `MIT` `Go/Docker/K8S`
- [GitLab](https://about.gitlab.com) - Git repository management, code reviews, issue tracking, activity feeds and wikis. (L0, L1) `MIT` `Ruby/deb/Docker/K8S`
- [Gogs](https://gogs.io/) - Painless Git Service written in Go. (L0) `MIT` `Go`
- [Huly](https://huly.io) - All-in-one project management platform (alternative to Linear, Jira, Slack). (L0, L1) `EPL-2.0` `Docker/K8S/Nodejs`
- [Ideon](https://www.theideon.com) - Project workspace built around an infinite canvas; embed GitHub, GitLab, Gitea, and Forgejo repositories alongside notes, links, and tasks, with real-time collaboration. (L0) `AGPL-3.0` `Docker`
- [Kaneo](https://kaneo.app/) - Project management platform focused on simplicity and efficiency. (L0, L1) `MIT` `K8S/Docker`
- [Leantime](https://leantime.io) - Lean project management system for small teams and startups helping to manage projects from ideation through delivery. (L0) `AGPL-3.0` `PHP/Docker`
- [Mindwendel](https://www.mindwendel.com/) - Brainstorm and upvote ideas and thoughts within your team. (L0, L1) `AGPL-3.0` `Docker/Elixir`
- [minimal-git-server](https://github.com/mcarbonne/minimal-git-server) - Lightweight git server with a basic CLI to manage repositories, supporting multiple accounts and running in a container. `MIT` `Docker`
- [Octobox](https://octobox.io/) `⚠` - Take back control of your GitHub Notifications. (L0) `AGPL-3.0` `Ruby/Docker`
- [OneDev](https://onedev.io/) - All-In-One DevOps Platform. With Git Management, Issue Tracking, and CI/CD. Simple yet Powerful. (L0) `MIT` `Java/Docker/K8S`
- [OpenProject](https://www.openproject.org) - Manage your projects, tasks and goals. Collaborate via work packages and link them to your pull requests on Github. (L0) `GPL-3.0` `Ruby/deb/Docker`
- [Paca](https://paca-ai.org) - AI-native project management platform where AI agents and humans collaborate as Scrum teammates on the same board and sprints. Configurable via config files and WASM plugins (alternative to Jira, Trello, ClickUp). (L0) `Apache-2.0` `Docker/K8S`
- [Pagure](https://pagure.io/pagure) - Lightweight, powerful, and flexible git-centric forge with features laying the foundation for federated and decentralized development. (L0) `GPL-2.0` `Docker/Python/deb`
- [Phorge](https://we.phorge.it/) - Community-driven platform for collaborating, managing, organizing and reviewing software development projects. (L0) `Apache-2.0` `PHP`
- [Plane](https://plane.so) - Track issues, epics, and product roadmaps in the simplest way possible (alternative to JIRA, Linear and Height). (L0, L1) `AGPL-3.0` `Docker`
- [ProjeQtOr](https://www.projeqtor.org/) - Complete, mature, multi-user project management system with extensive functionality for all phases of a project. (L0, L1) `AGPL-3.0` `PHP`
- [Redmine](https://www.redmine.org/) - Flexible project management web application. (L0) `GPL-2.0` `Ruby`
- [Review Board](https://www.reviewboard.org/) - Extensible and friendly code review tool for projects and companies of all sizes. (L0, L1) `MIT` `Python/Docker`
- [RhodeCode](https://rhodecode.com/) - Unify and simplify repository management for Git, Subversion, and Mercurial. (L0) `AGPL-3.0` `Python`
- [Rukovoditel](https://www.rukovoditel.net/) - Configurable project management, web-based application. (L0) `GPL-2.0` `PHP`
- [SCM Manager](https://www.scm-manager.org/) - Easiest way to share and manage your Git, Mercurial and Subversion repositories over http. (L0) `BSD-3-Clause` `Java/deb/Docker/K8S`
- [Smederee](https://smeder.ee) - Frugal platform which is dedicated to help people build great software together leveraging the power of the Darcs version control system. (L0) `AGPL-3.0` `Scala`
- [Sourcehut](https://sourcehut.org/) - Full web git interface with no javascript. (L0, L1) `GPL-2.0` `Go`
- [Taiga](https://www.taiga.io/) - Agile Project Management Tool based on the Kanban and Scrum methods. (L0) `MPL-2.0` `Docker/Python/Nodejs`
- [Titra](https://titra.io/) - Time-tracking solution for freelancers and small teams. (L0) `GPL-3.0` `Javascript/Docker`
- [Trac](https://trac.edgewall.org/) - Enhanced wiki and issue tracking system for software development projects. `BSD-3-Clause` `Python/deb`
- [Traq](https://traq.io/) - Project management and issue tracking system written in PHP. (L0) `GPL-3.0` `PHP/Nodejs`
- [Tuleap](https://www.tuleap.org/) - Libre suite to plan, track, code and collaborate on software projects. (L0) `GPL-2.0` `PHP`
- [ZenTao](https://www.zentao.pm/) - Agile(scrum) project management system/tool. (L0) `AGPL-3.0` `PHP`


<a id="software-development---testing"></a>
### Software Development - Testing 软件开发 - 测试

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Tools and software for [software testing](https://en.wikipedia.org/wiki/Software_testing).

- [Bencher](https://bencher.dev/) - Suite of continuous benchmarking tools designed to catch performance regressions in CI. (L0) `MIT/Apache-2.0` `Rust`
- [Request Inbox](https://request-inbox.com/) - Collect and inspect HTTP requests for testing and debugging. Create and manage inboxes, capture detailed request data, configure custom responses. (L0, L1) `Apache-2.0` `Docker`
- [WebHook Tester](https://github.com/tarampampam/webhook-tester) - Powerful tool for testing WebHooks and more. `MIT` `Docker/Go/deb/K8S`


<a id="static-site-generators"></a>
### Static Site Generators 静态站点生成器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Static site generators](https://en.wikipedia.org/wiki/Web_template_system#Static_site_generators) generate full static HTML websites based on raw data, plain text files and a set of templates. 

**请访问 [staticsitegenerators.bevry.me](https://staticsitegenerators.bevry.me), [staticgen.com](https://www.staticgen.com)**

_Related: [Blogging Platforms 博客平台](#blogging-platforms), [Photo Galleries 相册](#photo-galleries), [Content Management Systems (CMS) 内容管理系统（CMS）](#content-management-systems-cms)_



<a id="task-management--to-do-lists"></a>
### Task Management & To-do Lists 任务管理与待办清单

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Task management](https://en.wikipedia.org/wiki/Task_management#Task_management_software) software.

_Related: [Software Development - Project Management 软件开发 - 项目管理](#software-development---project-management), [Ticketing 工单](#ticketing)_

- [4ga Boards](https://4gaboards.com) - Straightforward realtime kanban boards management for intuitive task tracking. Featuring an elegant dark mode, collapsible todo lists, and multitasking tools to supercharge your team's productivity. (L0, L1) `MIT` `Nodejs/Docker/K8S`
- [AppFlowy](https://appflowy.io/) - Build detailed lists of to-do’s for different projects while tracking the status of each one (alternative to Notion). (L0) `AGPL-3.0` `Rust/Dart/Docker`
- [dayGLANCE](https://dayglance.app) - Day planner with drag-and-drop time blocking, inbox, recurring tasks, habits, routines, goals, projects and Pomodoro focus mode, plus iCal and CalDAV calendar sync. Data stays in the browser, with optional WebDAV or GLANCEvault sync. (L0, L1) `MIT` `Javascript/Docker`
- [Donetick](https://donetick.com) - Task and chore management tool for personal and family use, with advanced scheduling, flexible assignment, and group sharing capabilities, detailed history, automation via API, simple and modern design. (L0, L1) `AGPL-3.0` `Go/Docker`
- [Focus Flow](https://github.com/francesco-gaglione/focus_flow_cloud) - Complete ecosystem for time management using the Pomodoro technique. `MIT` `Docker/K8S`
- [HamsterBase Tasks](https://tasks.hamsterbase.com) - Tool to help organize ideas and build great things. Plan, organize, build and ship. (L0, L1) `AGPL-3.0` `Docker`
- [Kan](https://kan.bn/) - Flexible kanban app that helps you organise work, track progress, and deliver results (alternative to Trello). (L0) `AGPL-3.0` `Docker`
- [Kanboard](https://kanboard.org/) - Simple visual task board. (L0) `MIT` `PHP`
- [Listaway](https://github.com/jeffrpowell/listaway/) - List management app for creating and publicly sharing lists of items. Supports auth, admin tools, item notes and priorities, and opt-in public read-only links with randomized URLs (alternative to Amazon Lists). (L0) `MIT` `Docker`
- [myTinyTodo](https://www.mytinytodo.net/) - Simple way to manage your todo list in AJAX style. Uses PHP, jQuery, SQLite/MySQL. GTD compliant. (L0, L1) `GPL-2.0` `PHP`
- [Nullboard](https://github.com/apankrat/nullboard) - Single-page minimalist kanban board; compact, highly readable and quick to use. (L0) `BSD-2-Clause` `Javascript`
- [OpenHabitTracker](https://openhabittracker.net) - Track habits, tasks and notes with time tracking, calendar view and completion statistics. (L0, L1) `GPL-3.0` `Docker`
- [Our Shopping List](https://codeberg.org/nanawel/our-shopping-list) - Simple shared list application including shopping lists and any other small todo-list that needs to be used collaboratively. (L0) `AGPL-3.0` `Docker`
- [Super Productivity](https://super-productivity.com) - Advanced todo list app with integrated timeboxing and time tracking capabilities. Integrates with Jira, GitHub, GitLab, Redmine and OpenProject. (L0) `MIT` `Docker`
- [Task Keeper](https://github.com/nymanjens/piga) - List editor for power users, backed by a server. `Apache-2.0` `Scala`
- [Tasks.md](https://github.com/BaldissaraMatheus/Tasks.md) - File based task management board that and that supports Markdown syntax. `MIT` `Docker`
- [Taskwarrior](https://taskwarrior.org/) - Command line tool that manages your TODO list. It is flexible, fast, efficient, and unobtrusive. It does its job then gets out of your way. (L0) `MIT` `C++`
- [Tellor](https://tellor.cc/) - Minimalist single-user kanban todo app. Clean, simplified, and compact UI. Can import boards from Trello. (L0, L1) `MIT` `PHP`
- [Tracks](https://www.getontracks.org/) - Web-based application to help you implement David Allen’s Getting Things Done™ methodology. (L0) `GPL-2.0` `Ruby`
- [tududi](https://tududi.com/) - Task management tool with hierarchical structure, smart recurring tasks, and seamless Telegram integration. (L0) `MIT` `Docker`
- [Vikunja](https://vikunja.io/) - To-do app to organize your life. (L0, L1) `AGPL-3.0/GPL-3.0` `Go`
- [Wekan](https://wekan.github.io/) - Trello-like kanban. (L0) `MIT` `Nodejs`
- [Will Be Done](https://will-be-done.app/) - Offline-first task manager with weekly planning, project boards, real-time sync, Vim keybindings, desktop quick add, and import from popular task managers (alternative to TickTick, Todoist). (L0, L1) `AGPL-3.0` `Docker/Nodejs`


<a id="ticketing"></a>
### Ticketing 工单

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Helpdesk](https://en.wikipedia.org/wiki/Help_desk_software), [bug](https://en.wikipedia.org/wiki/Bug_tracking_system) and [issue](https://en.wikipedia.org/wiki/Issue_tracking_system) tracking software to help the tracking of user requests, bugs and missing features.

_Related: [Task Management & To-do Lists 任务管理与待办清单](#task-management--to-do-lists), [Software Development - Project Management 软件开发 - 项目管理](#software-development---project-management)_

- [BugPin](https://bugpin.io) - Visual bug reporting and ticketing tool for web applications. (L0) `AGPL-3.0/MIT` `Docker`
- [Bugzilla](https://www.bugzilla.org/) - General-purpose bugtracker and testing tool originally developed and used by the Mozilla project. (L0) `MPL-2.0` `Perl`
- [Frappe Helpdesk](https://frappe.io/helpdesk) - Helpdesk software which helps you streamline your company's support, offers an easy setup, clean user interface, and automation tools to resolve customer queries efficiently. (L0) `AGPL-3.0` `Docker`
- [FreeScout](https://freescout.net/) - Email-based customer support application, help desk and shared mailbox (alternative to Zendesk and Help Scout). (L0, L1) `AGPL-3.0` `PHP/Docker`
- [GlitchTip](https://glitchtip.com) - Error tracking app to collect errors reported by your app. (L0) `MIT` `Python/Docker/K8S`
- [ITFlow](https://itflow.org) - Client IT documentation, ticketing, invoicing and accounting for MSPs (Managed Service Providers). (L0, L1) `GPL-3.0` `PHP`
- [Libredesk](https://libredesk.io/) - Modern omnichannel customer support desk. Live chat, email, and more in a single binary. (L0, L1) `AGPL-3.0` `Docker/Go/Nodejs`
- [MantisBT](https://www.mantisbt.org/) - Bug tracker, fits best for software development. (L0, L1) `GPL-2.0` `PHP`
- [OTOBO](https://otobo.io/en/) - Flexible web-based ticketing system used for customer service, help desk, IT service management. (L0, L1) `GPL-3.0` `Perl/Docker`
- [Request Tracker](https://www.bestpractical.com/rt/) - Enterprise-grade issue tracking system. (L0) `GPL-2.0` `Perl`
- [Roundup Issue Tracker](https://www.roundup-tracker.org/) - Simple-to-use and -install issue tracking system with command-line, web, REST, XML-RPC, and e-mail interfaces. Designed with flexibility in mind - not just another bug tracker. (L0) `MIT/ZPL-2.0` `Python/Docker`
- [Rustrak](https://rustrak.github.io/rustrak/) - Error tracking server compatible with Sentry SDKs, using 32 MB of memory at idle with SQLite storage. (L0) `GPL-3.0` `Rust/Docker`
- [Zammad](https://zammad.org/) - Easy to use but powerful support and ticketing system. (L0) `AGPL-3.0` `Ruby/deb`


<a id="time-tracking"></a>
### Time Tracking 时间追踪

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[Time-tracking software](https://en.wikipedia.org/wiki/Time-tracking_software) is a category of computer software that allows its users to record time spent on tasks or projects.

- [ActivityWatch](https://activitywatch.net) - Automatically track how you spend time on your devices. (L0) `MPL-2.0` `Python`
- [Beaver Habit Tracker](https://github.com/daya0576/beaverhabits) - Habit tracking app to save your precious moments in your fleeting life. (L0) `BSD-3-Clause` `Docker`
- [Ever Gauzy](https://gauzy.co) - Open business management platform for collaborative, on-demand and sharing economies (ERP/CRM/HRM/ATS/PM). (L0, L1) `AGPL-3.0` `Docker/Nodejs`
- [Kimai](https://www.kimai.org/) - Track work time and print out a summary of your activities on demand. (L0, L1) `AGPL-3.0` `PHP`
- [solidtime](https://www.solidtime.io) - Modern time tracking application for freelancers and agencies. (L0) `AGPL-3.0` `Docker`
- [TimeTagger](https://timetagger.app) - Time-tracker based on an interactive timeline and powerful reporting. (L0, L1) `GPL-3.0` `Python`
- [TimeTracker](https://timetracker.drytrix.com/) - Track time across projects and clients, with timers, kanban tasks, CRM, expense tracking, multi-currency invoicing (PDF, Peppol/ZugFerd e-invoicing), reports, OIDC/SSO, and a REST API. (L0) `GPL-3.0` `Docker`
- [Traggo](https://traggo.net/) - Tag-based time tracking tool. In Traggo there are no tasks, only tagged time spans. (L0) `GPL-3.0` `Docker/Go`
- [Wakapi](https://wakapi.dev/) - Tracking tool for coding statistics, compatible with WakaTime. (L0) `GPL-3.0` `Go/Docker`
- [Ziit](https://ziit.app) - Swiss army knife of code time tracking (alternative to WakaTime). (L0) `AGPL-3.0` `Docker`


<a id="travel-organization"></a>
### Travel Organization 旅行规划

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Travel organization software to record bookings, view itinerary, plan activities and track expenses.

_Related: [Booking and Scheduling 预订与排程](#booking-and-scheduling), [Maps and Global Positioning System (GPS) 地图与全球定位系统（GPS）](#maps-and-global-positioning-system-gps)_

- [Surmai](https://surmai.app/) - Collaborative personal and family travel organizer. (L0, L1) `MIT` `Docker`
- [TREK](https://github.com/liketrek/TREK) - Collaborative trip planner with interactive maps, day-by-day itineraries, budgets, packing lists, reservations, journey journaling, and PWA support. (L0) `AGPL-3.0` `Docker/K8S`


<a id="url-shorteners"></a>
### URL Shorteners 短链接

**[`^        返回顶部        ^`](#awesome-selfhosted)**

[URL shortening](https://en.wikipedia.org/wiki/URL_shortening) is the action of shortening a [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator) to make it substantially shorter and still direct to the required page. Before hosting one, please see [disadvantages](https://en.wikipedia.org/wiki/URL_shortening#Disadvantages) of URL shorteners.

- [bit](https://github.com/sjdonado/bit) - Fast, lightweight, resource-efficient, compiled URL shortener. `MIT` `Docker/Crystal`
- [Chhoto URL](https://chhoto.link) - Simple, lightning-fast URL shortener with no bloat (fork of simply-shorten). (L0, L1, L2) `MIT` `Rust/Docker`
- [clink](https://git.crueter.xyz/crueter/clink) - Super-minimal link shortening service written in pure C, focusing on small executable size, portability, and ease of configuration. (L0) `AGPL-3.0` `C`
- [Flink](https://gitlab.com/rtraceio/web/flink) - Create QR Codes, embeddable link previews for your website and crawls/scrapes metadata. (L0) `MIT` `Docker`
- [Kutt](https://kutt.to) - Modern URL shortener with support for custom domains and custom URLs. (L0, L1) `MIT` `Nodejs/Docker`
- [rs-short](https://git.42l.fr/42l/rs-short) - Lightweight link shortener written in Rust, with features such as caching, spambot protection and phishing detection. (L0) `MPL-2.0` `Rust`
- [Shlink](https://shlink.io) - URL shortener with REST API and command line interface. Includes official progressive web application and docker images. (L0, L1) `MIT` `PHP/Docker`
- [Simple-URL-Shortener](https://github.com/azlux/Simple-URL-Shortener) - KISS URL shortener, public or private (with account). Minimalist and lightweight. No dependencies. (L0) `MIT` `PHP`
- [YOURLS](https://yourls.org/) - Set of PHP scripts that will allow you to run Your Own URL Shortener. Features include password protection, URL customization, bookmarklets, statistics, API, plugins, jsonp. (L0) `MIT` `PHP`


<a id="video-surveillance"></a>
### Video Surveillance 视频监控

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Video surveillance, also known as [Closed-circuit television (CCTV)](https://en.wikipedia.org/wiki/Closed-circuit_television), is the use of video cameras for surveillance in areas that require additional security or ongoing monitoring.

_Related: [Media Streaming - Video Streaming 媒体流 - 视频流](#media-streaming---video-streaming)_

- [Bluecherry](https://github.com/bluecherrydvr/bluecherry-apps) - Closed-circuit television (CCTV) software application which supports IP and Analog cameras. `GPL-2.0` `PHP`
- [Frigate](https://frigate.video/) - Monitor your security cameras with locally processed AI. (L0) `MIT` `Docker/Python/Nodejs`
- [motionEye](https://github.com/motioneye-project/motioneye) - Online interface for the software Motion, a video surveillance program with motion detection. `GPL-3.0` `Python/Docker`
- [Secluso](https://secluso.com) - Private DIY home security camera system for Raspberry Pi, with end-to-end encrypted remote access and mobile apps for live video, alerts, and recording playback. (L0) `GPL-3.0` `Rust`
- [SentryShot](https://codeberg.org/SentryShot/sentryshot) - Video surveillance management system. `GPL-2.0` `Docker/Rust`
- [Strix](https://github.com/eduard256/Strix) - Auto-discovers working stream URLs for IP cameras and generates ready-to-use Frigate and go2rtc configs. `MIT` `Go/Docker`
- [Viseron](https://viseron.netlify.app/) - Local-only NVR and AI Computer Vision software. With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor. (L0) `MIT` `Docker`
- [Zoneminder](https://www.zoneminder.com/) - Closed-circuit television (CCTV) software application which supports IP, USB and Analog cameras. (L0) `GPL-2.0` `PHP/deb`


<a id="vpn"></a>
### VPN 虚拟专用网络（VPN）

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [virtual private network (VPN)](https://en.wikipedia.org/wiki/Virtual_private_network) extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network.

**请访问 [awesome-sysadmin/VPN](https://github.com/awesome-foss/awesome-sysadmin#vpn)**

_See also: [Awesome-Tunneling](https://github.com/anderspitman/awesome-tunneling)_



<a id="web-servers"></a>
### Web Servers Web 服务器

**[`^        返回顶部        ^`](#awesome-selfhosted)**

Web Servers and Reverse Proxies. A [web server](https://en.wikipedia.org/wiki/Web_server) is a piece of software and underlying hardware that accepts requests via [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) (the network protocol created to distribute web content) or its secure variant [HTTPS](https://en.wikipedia.org/wiki/HTTPS). A [Reverse Proxy](https://en.wikipedia.org/wiki/Reverse_proxy) is a proxy server that appears to any client to be an ordinary web server, but in reality merely acts as an intermediary that forwards requests to one or more ordinary web servers.

_Related: [Proxy 代理](#proxy)_

- [Algernon](https://algernon.roboticoverlords.org/) - Small self-contained pure-Go web server with Lua, Markdown, HTTP/2, QUIC, Redis and PostgreSQL support. (L0) `BSD-3-Clause` `Go/Docker`
- [Apache HTTP Server](https://httpd.apache.org/) - Secure, efficient and extensible server that provides HTTP services in sync with the current HTTP standards. (L0) `Apache-2.0` `C/deb/Docker`
- [BunkerWeb](https://www.bunkerweb.io) - Next-gen Web Application Firewall (WAF) that will protect your web services. (L0, L1, L2) `AGPL-3.0` `deb/Docker/K8S/Python`
- [Caddy](https://caddyserver.com/) - Powerful, enterprise-ready web server with automatic HTTPS. (L0) `Apache-2.0` `Go/deb/Docker`
- [Ferron](https://ferron.sh/) - Fast, memory-safe web server written in Rust. (L0) `MIT` `Rust/Docker/deb`
- [go-doxy](https://github.com/yusing/godoxy) - Lightweight, simple, and performant reverse proxy with WebUI, Docker integration, automatic shutdown/startup for container based on traffic. `MIT` `Docker/Go`
- [HAProxy](https://www.haproxy.org/) - Very fast and reliable reverse-proxy offering high availability, load balancing, and proxying for TCP and HTTP-based applications. (L0) `GPL-2.0` `C/deb/Docker`
- [Lighttpd](https://www.lighttpd.net/) - Secure, fast, compliant, and very flexible web server that has been optimized for high-performance environments. (L0) `BSD-3-Clause` `C/deb/Docker`
- [Nginx Proxy Manager](https://nginxproxymanager.com/) - Docker container for managing Nginx proxy hosts with a simple, powerful interface. (L0) `MIT` `Docker`
- [NGINX](https://nginx.org/en/) - HTTP and reverse proxy server, mail proxy server, and generic TCP/UDP proxy server. (L0) `BSD-2-Clause` `C/deb/Docker`
- [Pangolin](https://digpangolin.com/) - Identity-aware tunneled reverse proxy with dashboard UI, access control, and WireGuard-based tunnels (alternative to Cloudflare Tunnel, Tailscale). (L0) `AGPL-3.0` `Docker`
- [Pomerium](https://www.pomerium.io) - Identity-aware reverse proxy, successor to now obsolete oauth_proxy. It inserts an OAuth step before proxying your request to the backend, so that you can safely expose your own websites to public Internet. (L0) `Apache-2.0` `Go/Docker`
- [SafeLine](https://waf.chaitin.com/) - Web application firewall / reverse proxy to protect your web apps from attacks and exploits. (L0, L1) `GPL-3.0` `Docker`
- [Static Web Server](https://static-web-server.net/) - Cross-platform, high-performance, and asynchronous web server for static file serving. (L0) `Apache-2.0/MIT` `Rust/Docker`
- [SWAG (Secure Web Application Gateway)](https://github.com/linuxserver/docker-swag) - Nginx webserver and reverse proxy with PHP support, built-in Certbot (Let's Encrypt) client and fail2ban integration. `GPL-3.0` `Docker`
- [Traefik](https://traefik.io/) - HTTP reverse proxy and load balancer that makes deploying microservices easy. (L0) `MIT` `Go/Docker`
- [UUSEC WAF](https://waf.uusec.com/) - Industry-leading high-performance, AI and semantic technology web application firewall and API security gateway (fork of nginx). (L0) `GPL-3.0` `C/Lua/Docker`
- [Vinyl Cache](https://vinyl-cache.org/) - Web application accelerator/caching HTTP reverse proxy (formerly Varnish). (L0) `BSD-2-Clause` `Go/deb/Docker`
- [Zoraxy](https://zoraxy.aroz.org/) - General purpose HTTP reverse proxy and forwarding tool. (L0) `AGPL-3.0` `Go/Docker`


<a id="wikis"></a>
### Wikis 维基

**[`^        返回顶部        ^`](#awesome-selfhosted)**

A [wiki](https://en.wikipedia.org/wiki/Wiki) is a publication collaboratively edited and managed by its own audience directly using a web browser.

_Related: [Note-taking & Editors 笔记与编辑器](#note-taking--editors), [Static Site Generators 静态站点生成器](#static-site-generators), [Knowledge Management Tools 知识管理工具](#knowledge-management-tools)_

_See also: [Wikimatrix](https://www.wikimatrix.org/), [List of wiki software - Wikipedia](https://en.wikipedia.org/wiki/List_of_wiki_software), [Comparison of wiki software - Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_wiki_software)_

- [AmuseWiki](https://amusewiki.org/) - Amusewiki is based on the Emacs Muse markup, remaining mostly compatible with the original implementation. It can work as a read-only site, as a moderated wiki, or as a fully open wiki or even as a private site. (L0) `GPL-1.0` `Perl/Docker`
- [BookStack](https://www.bookstackapp.com/) - Organize and store information. Stores documentation in a book like fashion. (L0, L1) `MIT` `PHP/Docker`
- [django-wiki](https://github.com/django-wiki/django-wiki) - Wiki system with complex functionality for simple integration and a superb interface. Store your knowledge with style: Use django models. (L0) `GPL-3.0` `Python`
- [docmost Community Edition](https://docmost.com/) - Collaborative wiki and documentation software (alternative to Confluence, Notion). (L0) `AGPL-3.0` `Docker/Nodejs`
- [Documize](https://documize.com) - Modern Docs + Wiki software with built-in workflow, single binary executable, just bring MySQL/Percona. (L0) `AGPL-3.0` `Go`
- [Dokuwiki](https://www.dokuwiki.org/DokuWiki) - Easy to use, lightweight, standards-compliant wiki engine with a simple syntax allowing reading the data outside the wiki. All data is stored in plain text files, therefore no database is required. (L0) `GPL-2.0` `PHP`
- [Feather Wiki](https://feather.wiki) - Lightning fast and infinitely extensible tool for creating personal non-linear notebooks, databases, and wikis that is entirely self-contained, runs in your browser, and is only 58 kilobytes in size. (L0, L1, L2) `AGPL-3.0` `Javascript`
- [Gitit](https://github.com/jgm/gitit) - Wiki program that stores pages and uploaded files in a git repository, which can then be modified using the VCS command line tools or the wiki's web interface. `GPL-2.0` `Haskell`
- [LeafWiki](https://github.com/perber/leafwiki) - Fast wiki for people who think in folders, not feeds. Fast editing. Tree navigation. Markdown on disk. (L0) `MIT` `Docker/Go`
- [Mediawiki](https://www.mediawiki.org/wiki/MediaWiki) - Wiki software package that powers Wikipedia and all other Wikimedia projects, serving hundreds of millions of users each month. (L0, L1) `GPL-2.0` `PHP`
- [Otter Wiki](https://otterwiki.com/) - Simple, easy to use wiki software using markdown. (L0) `MIT` `Docker`
- [PmWiki](https://www.pmwiki.org) - Wiki-based system for collaborative creation and maintenance of websites. `GPL-3.0` `PHP`
- [Raneto](https://raneto.com/) - Knowledgebase platform that uses static Markdown files. (L0) `MIT` `Nodejs`
- [TiddlyWiki](https://tiddlywiki.com/) - Reusable non-linear personal web notebook. (L0) `BSD-3-Clause` `Nodejs`
- [Tiki](https://tiki.org/HomePage) - Wiki CMS Groupware with the most built-in features. (L0, L1) `LGPL-2.1` `PHP`
- [W](https://w.club1.fr) - Lightweight, mutli-user, flat-file-database Wiki engine. Create pages quickly and edit them in your Web browser using Mardown/HTML/CSS/JS. The main difference with other wiki is that you are encouraged to customize each page style individually. (L0) `AGPL-3.0` `PHP`
- [WackoWiki](https://wackowiki.org/) - Light and easy to install multilingual Wiki-engine. (L0) `BSD-3-Clause` `PHP`
- [Wiki-Go](https://leomoon.com/downloads/web-apps/wiki-go/) - Modern, feature-rich, databaseless flat-file wiki platform. (L0, L1) `GPL-3.0` `Go/Docker`
- [Wiki.js](https://js.wiki/) - Modern, lightweight and powerful wiki app using Git and Markdown. (L0, L1) `AGPL-3.0` `Nodejs/Docker/K8S`
- [WikiDocs](https://www.wikidocs.app/) - Databaseless markdown flat-file wiki engine. (L0) `MIT` `PHP/Docker`
- [WiKiss](https://wikiss.tuxfamily.org/) - Wiki, simple to use and install. (L0) `GPL-2.0` `PHP`
- [XWiki](https://www.xwiki.org) - Second generation wiki that allows the user to extend its functionalities with a powerful extension-based architecture. (L0, L1) `LGPL-2.1` `Java/Docker/deb`
- [Zim](https://zim-wiki.org/) - Graphical text editor used to maintain a collection of wiki pages. Each page can contain links to other pages, simple formatting and images. (L0) `GPL-2.0` `Python/deb`


--------------------

<a id="list-of-licenses"></a>
## List of Licenses 许可证列表

**[`^        返回顶部        ^`](#awesome-selfhosted)**

- `0BSD` - [BSD Zero-Clause Licence](https://spdx.org/licenses/0BSD.html)
- `AAL` - [Attribution Assurance License](https://spdx.org/licenses/AAL.html)
- `AGPL-3.0` - [GNU Affero General Public License 3.0](https://spdx.org/licenses/AGPL-3.0.html)
- `Apache-2.0` - [Apache, Version 2.0](https://spdx.org/licenses/Apache-2.0.html)
- `APSL-2.0` - [Apple Public Source License, Version 2.0](https://spdx.org/licenses/APSL-2.0.html)
- `Artistic-2.0` - [Artistic License Version 2.0](https://spdx.org/licenses/Artistic-2.0.html)
- `Beerware` - [Beerware License](https://spdx.org/licenses/Beerware.html)
- `BSD-2-Clause` - [BSD 2-clause "Simplified"](https://spdx.org/licenses/BSD-2-Clause.html)
- `BSD-2-Clause-FreeBSD` - [BSD 2-Clause FreeBSD License](https://spdx.org/licenses/BSD-2-Clause-FreeBSD.html)
- `BSD-3-Clause` - [BSD 3-Clause "New" or "Revised"](https://spdx.org/licenses/BSD-3-Clause.html)
- `BSD-3-Clause-Attribution` - [BSD with attribution](https://spdx.org/licenses/BSD-3-Clause-Attribution.html)
- `BSD-4-Clause` - [BSD 4-clause "Original"](https://spdx.org/licenses/BSD-4-Clause.html)
- `CAL-1.0` - [Cryptographic Autonomy License 1.0](https://spdx.org/licenses/CAL-1.0.html)
- `CC-BY-SA-3.0` - [Creative Commons Attribution-ShareAlike 3.0 License](https://spdx.org/licenses/CC-BY-SA-3.0.html)
- `CC-BY-SA-4.0` - [Creative Commons Attribution-ShareAlike 4.0 License](https://spdx.org/licenses/CC-BY-SA-4.0.html)
- `CC0-1.0` - [Public Domain/Creative Common Zero 1.0](https://spdx.org/licenses/CC0-1.0.html)
- `CDDL-1.0` - [Common Development and Distribution License](https://spdx.org/licenses/CDDL-1.0.html)
- `CECILL-B` - [CEA CNRS INRIA Logiciel Libre](https://spdx.org/licenses/CECILL-B.html)
- `CPAL-1.0` - [Common Public Attribution License Version 1.0](https://spdx.org/licenses/CPAL-1.0.html)
- `ECL-2.0` - [Educational Community License, Version 2.0](https://spdx.org/licenses/ECL-2.0.html)
- `EPL-1.0` - [Eclipse Public License, Version 1.0](https://spdx.org/licenses/EPL-1.0.html)
- `EPL-2.0` - [Eclipse Public License, Version 2.0](https://spdx.org/licenses/EPL-2.0.html)
- `EUPL-1.2` - [European Union Public License 1.2](https://spdx.org/licenses/EUPL-1.2.html)
- `GPL-1.0` - [GNU General Public License 1.0](https://spdx.org/licenses/GPL-1.0.html)
- `GPL-2.0` - [GNU General Public License 2.0](https://spdx.org/licenses/GPL-2.0.html)
- `GPL-3.0` - [GNU General Public License 3.0](https://spdx.org/licenses/GPL-3.0.html)
- `IPL-1.0` - [IBM Public License](https://spdx.org/licenses/IPL-1.0.html)
- `ISC` - [Internet Systems Consortium License](https://spdx.org/licenses/ISC.html)
- `LGPL-2.1` - [Lesser General Public License 2.1](https://spdx.org/licenses/LGPL-2.1.html)
- `LGPL-3.0` - [Lesser General Public License 3.0](https://spdx.org/licenses/LGPL-3.0.html)
- `MIT` - [MIT License](https://spdx.org/licenses/MIT.html)
- `MPL-1.1` - [Mozilla Public License Version 1.1](https://spdx.org/licenses/MPL-1.1.html)
- `MPL-2.0` - [Mozilla Public License](https://spdx.org/licenses/MPL-2.0.html)
- `OSL-3.0` - [Open Software License 3.0](https://spdx.org/licenses/OSL-3.0.html)
- `Sendmail` - [Sendmail License](https://spdx.org/licenses/Sendmail.html)
- `Ruby` - [Ruby License](https://spdx.org/licenses/Ruby.html)
- `Unlicense` - [The Unlicense](https://spdx.org/licenses/Unlicense.html)
- `WTFPL` - [Do What the Fuck You Want to Public License](https://spdx.org/licenses/WTFPL.html)
- `Zlib` - [Zlib/libpng License](https://spdx.org/licenses/Zlib.html)
- `ZPL-2.0` - [Zope Public License 2.0](https://spdx.org/licenses/ZPL-2.0.html)


--------------------

<a id="anti-features"></a>
## Anti-features 反特性

- `⚠ ` - Depends on a proprietary service outside the user's control

--------------------

<a id="external-links"></a>
## External Links 外部链接

**[`^        返回顶部        ^`](#awesome-selfhosted)**

- Alternative frontends/portals to discover/filter awesome-selfhosted apps: [awweso.me](https://awweso.me/), [awesome-web.theravenhub](https://awesome-web.theravenhub.com/browse.html)
- [Awesome Sysadmin](https://github.com/awesome-foss/awesome-sysadmin) - Curated list of amazingly awesome open source sysadmin resources.
- Lists of software aimed at privacy and decentralization in some form: [PRISM Break](https://prism-break.org/en/), [privacytools.io](https://www.privacytools.io/), [Alternative Internet](https://redecentralize.github.io/alternative-internet/), [Libre Projects](https://libreprojects.net/), [Easy Indie App](https://easyindie.app)
- Other Awesome lists: [Awesome Big Data](https://github.com/0xnr/awesome-bigdata), [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
- Dynamic Domain Name services: [Afraid.org](https://freedns.afraid.org/domain/registry/), [Pagekite](https://pagekite.net/)
- Communities/forums: [/c/selfhosted on lemmy.world](https://lemmy.world/c/selfhosted), [/c/selfhost on lemmy.ml](https://lemmy.ml/c/selfhost), [/r/selfhosted on reddit](https://old.reddit.com/r/selfhosted/), [/r/selfhosted Matrix Channel](https://matrix.to/#/#selfhosted:selfhosted.chat), [/r/homelab on reddit](https://old.reddit.com/r/homelab/), [IndieWeb](https://indieweb.org/)
- [theme.park](https://theme-park.dev/) - A collection of themes/skins for 50 selfhosted apps! (L0) `MIT` `CSS`

--------------------

<a id="contributing"></a>
## Contributing 贡献

Contributing guidelines can be found [here](https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/CONTRIBUTING.md).

<a id="license"></a>
## License 许可证

This list is under the [Creative Commons Attribution-ShareAlike 3.0 Unported](https://github.com/awesome-selfhosted/awesome-selfhosted/blob/master/LICENSE) License.
Terms of the license are summarized [here](https://creativecommons.org/licenses/by-sa/3.0/).  
The list of authors can be found in the [AUTHORS](https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/AUTHORS) file.
