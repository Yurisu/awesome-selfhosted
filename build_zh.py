#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 awesome-selfhosted 的 README.md 翻译为中文（保留所有链接/锚点）。

策略：
- 标题：在原英文标题前插入 <a id="原始slug"></a>，并追加「英文 中文」。
- 目录 / 相关链接：仅改显示文字，#anchor 原样保留。
- 条目：保留 [名称](url)、`⚠`、[Source Code]/[Demo]/[Clients] 链接与尾部标签，
  说明文字优先用已从半成品里提取的中文，未提取到的保留英文。
- 说明段落（intro）：用 INTRO_ZH 精确匹配替换，未匹配保留英文。
"""
import re

SRC = "README.md"
HALF = "README.zh-CN.md"  # 我之前手工翻的半成品，用于提取条目中文

# ---------- 标题中英映射（覆盖全部章节） ----------
HEADER_ZH = {
    "Awesome-Selfhosted": "自托管软件精选清单",
    "Table of contents": "目录",
    "Software": "软件",
    "Analytics": "分析",
    "Archiving and Digital Preservation (DP)": "存档与数字化保存（DP）",
    "Automation": "自动化",
    "Backup": "备份",
    "Blogging Platforms": "博客平台",
    "Booking and Scheduling": "预订与排程",
    "Bookmarks and Link Sharing": "书签与链接分享",
    "Calendar & Contacts": "日历与联系人",
    "Communication - Custom Communication Systems": "通信 - 自定义通信系统",
    "Communication - Email - Complete Solutions": "通信 - 电子邮件 - 完整方案",
    "Communication - Email - Mail Delivery Agents": "通信 - 电子邮件 - 邮件投递代理",
    "Communication - Email - Mail Transfer Agents": "通信 - 电子邮件 - 邮件传输代理",
    "Communication - Email - Mailing Lists and Newsletters": "通信 - 电子邮件 - 邮件列表与新闻稿",
    "Communication - Email - Webmail Clients": "通信 - 电子邮件 - Web 邮件客户端",
    "Communication - IRC": "通信 - IRC",
    "Communication - SIP": "通信 - SIP",
    "Communication - Social Networks and Forums": "通信 - 社交网络与论坛",
    "Communication - Video Conferencing": "通信 - 视频会议",
    "Communication - XMPP - Servers": "通信 - XMPP - 服务器",
    "Communication - XMPP - Web Clients": "通信 - XMPP - Web 客户端",
    "Community-Supported Agriculture (CSA)": "社区支持农业（CSA）",
    "Conference Management": "会议管理",
    "Content Management Systems (CMS)": "内容管理系统（CMS）",
    "Customer Relationship Management (CRM)": "客户关系管理（CRM）",
    "Database Management": "数据库管理",
    "DNS": "域名系统（DNS）",
    "Document Management": "文档管理",
    "Document Management - E-books": "文档管理 - 电子书",
    "Document Management - Institutional Repository and Digital Library Software": "文档管理 - 机构知识库与数字图书馆软件",
    "Document Management - Integrated Library Systems (ILS)": "文档管理 - 集成图书馆系统（ILS）",
    "E-commerce": "电子商务",
    "Federated Identity & Authentication": "联合身份与认证",
    "Feed Readers": "订阅源阅读器",
    "File Transfer & Synchronization": "文件传输与同步",
    "File Transfer - Distributed Filesystems": "文件传输 - 分布式文件系统",
    "File Transfer - Object Storage & File Servers": "文件传输 - 对象存储与文件服务器",
    "File Transfer - Peer-to-peer Filesharing": "文件传输 - 点对点文件共享",
    "File Transfer - Single-click & Drag-n-drop Upload": "文件传输 - 一键与拖拽上传",
    "File Transfer - Web-based File Managers": "文件传输 - 基于 Web 的文件管理器",
    "Games": "游戏",
    "Games - Administrative Utilities & Control Panels": "游戏 - 管理工具与控制面板",
    "Genealogy": "家谱",
    "Generative Artificial Intelligence (GenAI)": "生成式人工智能（GenAI）",
    "Groupware": "群件",
    "Health and Fitness": "健康与健身",
    "Human Resources Management (HRM)": "人力资源管理（HRM）",
    "Identity Management": "身份管理",
    "Internet of Things (IoT)": "物联网（IoT）",
    "Inventory Management": "库存管理",
    "Knowledge Management Tools": "知识管理工具",
    "Learning and Courses": "学习与课程",
    "Manufacturing": "制造",
    "Maps and Global Positioning System (GPS)": "地图与全球定位系统（GPS）",
    "Media Management": "媒体管理",
    "Media Streaming": "媒体流",
    "Media Streaming - Audio Streaming": "媒体流 - 音频流",
    "Media Streaming - Multimedia Streaming": "媒体流 - 多媒体流",
    "Media Streaming - Video Streaming": "媒体流 - 视频流",
    "Miscellaneous": "杂项",
    "Money, Budgeting & Management": "金钱、预算与管理",
    "Monitoring & Status Pages": "监控与状态页",
    "Network Utilities": "网络工具",
    "Note-taking & Editors": "笔记与编辑器",
    "Office Suites": "办公套件",
    "Password Managers": "密码管理器",
    "Pastebins": "粘贴板",
    "Personal Dashboards": "个人仪表盘",
    "Photo Galleries": "相册",
    "Polls and Events": "投票与活动",
    "Proxy": "代理",
    "Recipe Management": "食谱管理",
    "Remote Access": "远程访问",
    "Resource Planning": "资源规划",
    "Search Engines": "搜索引擎",
    "Self-hosting Solutions": "自托管方案",
    "Software Development": "软件开发",
    "Software Development - API Management": "软件开发 - API 管理",
    "Software Development - Continuous Integration & Deployment": "软件开发 - 持续集成与部署",
    "Software Development - FaaS & Serverless": "软件开发 - FaaS 与无服务器",
    "Software Development - Feature Toggle": "软件开发 - 功能开关",
    "Software Development - IDE & Tools": "软件开发 - IDE 与工具",
    "Software Development - Localization": "软件开发 - 本地化",
    "Software Development - Low Code": "软件开发 - 低代码",
    "Software Development - Project Management": "软件开发 - 项目管理",
    "Software Development - Testing": "软件开发 - 测试",
    "Static Site Generators": "静态站点生成器",
    "Task Management & To-do Lists": "任务管理与待办清单",
    "Ticketing": "工单",
    "Time Tracking": "时间追踪",
    "Travel Organization": "旅行规划",
    "URL Shorteners": "短链接",
    "Video Surveillance": "视频监控",
    "VPN": "虚拟专用网络（VPN）",
    "Web Servers": "Web 服务器",
    "Wikis": "维基",
    "List of Licenses": "许可证列表",
    "Anti-features": "反特性",
    "External Links": "外部链接",
    "Contributing": "贡献",
    "License": "许可证",
}

# ---------- 说明段落（intro）精确中英映射 ----------
INTRO_ZH = {
    "[Analytics](https://en.wikipedia.org/wiki/Analytics) is the systematic computational analysis of data or statistics. It is used for the discovery, interpretation, and communication of meaningful patterns in data.":
        "[Analytics 分析学](https://en.wikipedia.org/wiki/Analytics) 是对数据或统计资料的系统性计算分析，用于发现、解读数据中的有意义模式，并把这些模式传达出来。",
    "Digital [archiving](https://en.wikipedia.org/wiki/Archival_science) and [preservation](https://en.wikipedia.org/wiki/Digital_preservation) software.":
        "Digital [archiving 存档](https://en.wikipedia.org/wiki/Archival_science) 与 [preservation 保存](https://en.wikipedia.org/wiki/Digital_preservation) 软件。",
    "[Automation](https://en.wikipedia.org/wiki/Automation) software designed to reduce human intervention in processes.":
        "[Automation 自动化](https://en.wikipedia.org/wiki/Automation) 软件，用于减少流程中的人工干预。",
    "[Backup](https://en.wikipedia.org/wiki/Backup) software.":
        "[Backup 备份](https://en.wikipedia.org/wiki/Backup) 软件。",
    "A blog is a discussion or informational website consisting of discrete, diary-style text entries (posts).":
        "A blog 博客 是一种讨论性或信息性的网站，由离散的、日记式文本条目（posts 文章）组成。",
    "Event scheduling, reservation, and appointment management software.":
        "活动排程、预订与预约管理软件。",
    "Software which allows users to add, annotate, edit, and share [bookmarks](https://en.wikipedia.org/wiki/Bookmark_(digital)) of web documents.":
        "用于添加、标注、编辑并分享 Web 文档 [bookmarks 书签](https://en.wikipedia.org/wiki/Bookmark_(digital)) 的软件。",
    "[CalDAV](https://en.wikipedia.org/wiki/CalDAV) and [CardDAV](https://en.wikipedia.org/wiki/CardDAV) protocol servers and web clients/interfaces for [Electronic calendar](https://en.wikipedia.org/wiki/Calendaring_software), [address book](https://en.wikipedia.org/wiki/Address_book) and [contact management](https://en.wikipedia.org/wiki/Contact_manager).":
        "[CalDAV](https://en.wikipedia.org/wiki/CalDAV) 与 [CardDAV](https://en.wikipedia.org/wiki/CardDAV) 协议服务器，以及用于 [Electronic calendar 电子日历](https://en.wikipedia.org/wiki/Calendaring_software)、[address book 通讯录](https://en.wikipedia.org/wiki/Address_book) 与 [contact management 联系人管理](https://en.wikipedia.org/wiki/Contact_manager) 的 Web 客户端/界面。",
    "[Communication software](https://en.wikipedia.org/wiki/Communication_software) used to provide remote access to systems and exchange files and messages in text, audio and/or video formats between different computers or users, using their own custom protocols.":
        "[Communication software 通信软件](https://en.wikipedia.org/wiki/Communication_software) 用于提供对系统的远程访问，并在不同计算机或用户之间以文本、音频和/或视频格式交换文件与消息，使用其自定义协议。",
    "Simple deployment of [E-mail](https://en.wikipedia.org/wiki/Email) servers, e.g. for inexperienced or impatient admins.":
        "[E-mail 电子邮件](https://en.wikipedia.org/wiki/Email) 服务器的简易部署，例如面向经验不足或没耐心的管理员。",
    "[Mail Delivery Agents](https://en.wikipedia.org/wiki/Message_delivery_agent) (MDAs) - [IMAP](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol)/[POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) server software.":
        "[Mail Delivery Agents 邮件投递代理](https://en.wikipedia.org/wiki/Message_delivery_agent)（MDA）——[IMAP](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol)/[POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) 服务器软件。",
    "[Mail Transfer Agents](https://en.wikipedia.org/wiki/Message_transfer_agent) (MTAs) - [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) servers.":
        "[Mail Transfer Agents 邮件传输代理](https://en.wikipedia.org/wiki/Message_transfer_agent)（MTA）——[SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) 服务器。",
    "[Mailing list](https://en.wikipedia.org/wiki/Mailing_list) servers and mass mailing software - one message to many recipients.":
        "[Mailing list 邮件列表](https://en.wikipedia.org/wiki/Mailing_list) 服务器与群发邮件软件——一条消息发给众多收件人。",
    "[Webmail](https://en.wikipedia.org/wiki/Webmail) clients.":
        "[Webmail Web 邮件](https://en.wikipedia.org/wiki/Webmail) 客户端。",
    "[IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) communication software.":
        "[IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) 通信软件。",
    "[SIP](https://en.wikipedia.org/wiki/Session_Initiation_Protocol)/[IPBX](https://en.wikipedia.org/wiki/IP_PBX) telephony software.":
        "[SIP](https://en.wikipedia.org/wiki/Session_Initiation_Protocol)/[IPBX](https://en.wikipedia.org/wiki/IP_PBX) 电话软件。",
    "[Video/Web Conferencing](https://en.wikipedia.org/wiki/Web_conferencing) tools and software.":
        "[Video/Web Conferencing 视频/Web 会议](https://en.wikipedia.org/wiki/Web_conferencing) 工具与软件。",
    "[Extensible Messaging and Presence Protocol](https://en.wikipedia.org/wiki/XMPP) servers.":
        "[Extensible Messaging and Presence Protocol](https://en.wikipedia.org/wiki/XMPP) 服务器。",
    "[Extensible Messaging and Presence Protocol](https://en.wikipedia.org/wiki/XMPP) Web clients/interfaces.":
        "[Extensible Messaging and Presence Protocol](https://en.wikipedia.org/wiki/XMPP) Web 客户端/界面。",
    "Management and administration tools for community supported agriculture and food cooperatives.":
        "面向社区支持农业与食物合作社的管理与行政工具。",
    "Software for submission of [abstracts](https://en.wikipedia.org/wiki/Abstract_management) and preparation/management of academic conferences.":
        "用于提交 [abstracts 摘要](https://en.wikipedia.org/wiki/Abstract_management) 并筹备/管理学术会议的软件。",
    "[Social Networking](https://en.wikipedia.org/wiki/Social_networking_service) and [Forum](https://en.wikipedia.org/wiki/Internet_forum) software.":
        "[Social Networking 社交网络](https://en.wikipedia.org/wiki/Social_networking_service) 与 [Forum 论坛](https://en.wikipedia.org/wiki/Internet_forum) 软件。",
}

# ---------- 从半成品里提取「条目名 -> 中文说明」 ----------
zh_desc_map = {}
try:
    with open(HALF, encoding="utf-8") as f:
        for line in f:
            m = re.match(
                r'^- \[([^\]]+)\]\((https?://[^)]+)\)(?:\s*`⚠`)?\s*-\s*(.+?)(?:\s+`[^`]+`(?:\s+`[^`]+`)*)?\s*$',
                line.rstrip("\n"),
            )
            if m:
                zh_desc_map[m.group(1)] = m.group(3)
except FileNotFoundError:
    pass


def github_slug(text):
    s = text.strip().lower()
    s = s.replace('&', '-')  # GitHub slugger 把 & 变成 -，导致 calendar--contacts 双连字符
    # 移除 github-slugger 会清除的标点（保留 - 与 _）
    s = re.sub(r'[\u2000-\u206F\u2E00-\u2E7F\\\'!"#$%&()*+,./:;<=>?@[\]^`{|}~\t]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s.strip('-')


def build_anchor_map(src):
    """从原始 README 的目录里取出 标题 -> 原始anchor 的映射。

    awesome-selfhosted 自有一套 slug（如 calendar--contacts 双连字符），
    与其反向推导，不如直接复用原始目录里的 anchor，保证跳转 100% 一致。
    """
    amap = {}
    toc = False
    with open(src, encoding="utf-8") as f:
        for line in f:
            if re.match(r'^##\s+Table of contents', line):
                toc = True
                continue
            if toc and re.match(r'^##\s+Software', line):
                break
            if toc:
                m = re.match(r'^\s*- \[(.+?)\]\(#([^)]+)\)\s*$', line)
                if m:
                    amap[m.group(1).strip()] = m.group(2)
    return amap


header_re = re.compile(r'^(#{1,3})\s+(.+?)\s*$')
toc_re = re.compile(r'^(\s*)- \[(.+?)\]\(#(.+?)\)$')
related_re = re.compile(r'^(_(?:Related|See also):)\s*(.*)$')
entry_re = re.compile(r'^(\s*)- \[([^\]]+)\]\((https?://[^)]+)\)(\s*`⚠`)?(.*)$')
rel_link_re = re.compile(r'\[([^\]]+)\]\(#([^)]+)\)')


def transform_related(rest):
    return rel_link_re.sub(
        lambda m: f'[{m.group(1)} {HEADER_ZH.get(m.group(1), "")}](#{m.group(2)})'.strip(), rest
    )


def transform_entry(line):
    m = entry_re.match(line)
    if not m:
        return None
    indent, name, url, warn, rest = m.groups()
    warn = warn or ''
    if ' - ' not in rest:
        return line  # 无说明、仅有标签的条目，原样保留
    tag_m = re.search(r'(\s+`[^`]+`(?:\s+`[^`]+`)*)\s*$', rest)
    if tag_m:
        tags = tag_m.group(1)
        body = rest[:tag_m.start()]
    else:
        tags = ''
        body = rest
    orig_desc = body[3:] if body.startswith(' - ') else body
    desc = zh_desc_map.get(name, orig_desc)
    return f"{indent}- [{name}]({url}){warn} - {desc}{tags}"


def main():
    out = []
    anchor_map = build_anchor_map(SRC)
    with open(SRC, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            # 标题
            hm = header_re.match(line)
            if hm:
                hashes, text = hm.group(1), hm.group(2)
                slug = anchor_map.get(text, github_slug(text))
                zh = HEADER_ZH.get(text)
                out.append(f'<a id="{slug}"></a>')
                out.append(f"{hashes} {text} {zh}" if zh else line)
                continue
            # 目录项
            tm = toc_re.match(line)
            if tm:
                indent, text, anchor = tm.group(1), tm.group(2), tm.group(3)
                zh = (text + " " + HEADER_ZH.get(text, "")).strip()
                out.append(f"{indent}- [{zh}](#{anchor})")
                continue
            # _Related:_ / _See also:_
            rm = related_re.match(line)
            if rm:
                out.append(f"{rm.group(1)} {transform_related(rm.group(2))}")
                continue
            # 返回顶部
            if 'back to top' in line:
                out.append(line.replace('back to top', '返回顶部'))
                continue
            # 说明段落精确匹配
            if line in INTRO_ZH:
                out.append(INTRO_ZH[line])
                continue
            # 条目
            em = entry_re.match(line)
            if em:
                res = transform_entry(line)
                if res is not None:
                    out.append(res)
                    continue
            # 行内小替换
            line = line.replace('Please visit ', '请访问 ')
            line = line.replace('See [', '参见 [')
            out.append(line)

    with open(HALF, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    print(f"written {HALF}: {len(out)} lines")
    print(f"extracted {len(zh_desc_map)} entry translations reused")


if __name__ == "__main__":
    main()
