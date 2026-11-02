#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""翻译 README.zh-CN.md 中仍用英文的条目说明与章节 intro。

- 条目：[名称](url) 与 URL/标签 原样保留，仅翻译说明文字。
- 章节 intro：翻译紧跟标题后的第一段英文说明文字。
- 完整 [text](url) 链接整体保留，避免机器翻译破坏链接。
- 翻译结果缓存到 trans_cache.json，可断点续传。
- 仅当 MyMemory 真正返回配额耗尽时才优雅停止。
"""
import re, json, time, os, sys, urllib.parse, urllib.request

SRC = "README.zh-CN.md"
CACHE = "trans_cache.json"

entry_re = re.compile(r'^(\s*)- \[([^\]]+)\]\((https?://[^)]+)\)(\s*`⚠`)?')
header_re = re.compile(r'^(#{2,3})\s+')
toc_re = re.compile(r'^\s*- \[.+\]\(#')
backtop_re = re.compile(r'返回顶部', re.I)
anchor_re = re.compile(r'^<a id=')
LIMIT = int(os.environ.get("LIMIT", "0"))  # 0 = 全部
DELAY = float(os.environ.get("DELAY", "0.3"))

try:
    cache = json.load(open(CACHE, encoding="utf-8"))
except Exception:
    cache = {}

STOP = False

def has_cjk(s):
    return any('\u4e00' <= c <= '\u9fff' for c in s)

def is_prose(line):
    s = line.strip()
    if len(s) < 12:
        return False
    if not re.search(r'[A-Za-z]{4,}', s):
        return False
    if s.startswith(('*', '`', '|', '<', '#', '>', '[')):
        return False
    return True

LINK_RE = re.compile(r'\[[^\]]*\]\(https?://[^)]+\)')
# 用于切分的带捕获组版本：split 后奇数下标为链接，偶数下标为纯文本片段
SPLIT_RE = re.compile(r'(\[[^\]]*\]\(https?://[^)]+\))')

def _mt_call(text):
    """调用 MyMemory 翻译单段文本。返回 (translated_text_or_None, stop_flag)。
    stop_flag=True 表示配额耗尽/持续限流，调用方应停止且不缓存该条。"""
    global STOP
    q = urllib.parse.quote(text)
    url = ("https://api.mymemory.translated.net/get?q=%s"
           "&langpair=en|zh-CN&de=selfhost-translate@example.com") % q
    backoff = 20
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            data = json.load(urllib.request.urlopen(req, timeout=15))
            st = data.get("responseStatus")
            t = data.get("responseData", {}).get("translatedText", "")
            if st == 200 and t:
                if "YOU USED ALL" in t.upper() or "QUOTA" in str(data.get("responseDetails", "")).upper():
                    STOP = True
                    return None, True
                return t, False
            if st == 429:
                if attempt < 4:
                    time.sleep(backoff)
                    backoff = min(backoff * 2, 120)
                    continue
                STOP = True
                return None, True
            if st in (402, 403) or "QUOTA" in str(data.get("responseDetails", "")).upper():
                STOP = True
                return None, True
        except Exception:
            time.sleep(2)
    return None, False

def translate(text, retries=5):
    global STOP
    text = text.strip()
    if not text:
        return text
    if text in cache:
        return cache[text]
    if has_cjk(text):
        cache[text] = text
        return text
    orig = text  # 含真实链接的原始文本，失败时回退用
    # 链接保护：按 [text](url) 切分为片段，仅翻译链接之间的纯文本，链接整体原样保留，
    # 从根本上避免翻译服务丢弃占位符导致链接丢失（旧版 \u0002 占位符被 MyMemory 剥离）。
    segs = SPLIT_RE.split(text)  # 偶数下标=纯文本片段，奇数下标=链接
    out = []
    for i, seg in enumerate(segs):
        if i % 2 == 1:
            out.append(seg)  # 链接整体保留，绝不送入翻译
            continue
        if not seg.strip():
            out.append(seg)
            continue
        if has_cjk(seg) or not re.search(r'[A-Za-z]{3,}', seg):
            out.append(seg)
            continue
        t, stop = _mt_call(seg)
        if stop:
            # 配额耗尽：本条回退原文（含真实链接），不缓存，便于后续续传
            return orig
        out.append(t if t is not None else seg)  # 网络失败则保留该片段原文
    result = "".join(out)
    # 完整性校验：翻译后链接数量必须与原文一致，否则放弃该条（绝不提交破损链接）
    if len(LINK_RE.findall(result)) != len(LINK_RE.findall(orig)):
        return orig
    cache[text] = result
    time.sleep(DELAY)
    return result

def process_entry(line):
    m = entry_re.match(line)
    if not m:
        return line
    indent, name, url, warn = m.groups()
    warn = warn or ""
    rest = line[m.end():]
    tag_m = re.search(r'(\s+`[^`]+`(?:\s+`[^`]+`)*)\s*$', rest)
    if tag_m:
        tags = tag_m.group(1)
        body = rest[:tag_m.start()]
    else:
        tags = ""
        body = rest
    if not body.startswith(" - "):
        return line
    desc = body[3:]
    if has_cjk(desc):
        return line
    newdesc = translate(desc)
    return f"{indent}- [{name}]({url}){warn} - {newdesc}{tags}"

def main():
    global STOP
    lines = open(SRC, encoding="utf-8").read().split("\n")
    out = []
    expect_intro = True
    done = 0
    for line in lines:
        if STOP:
            out.append(line)
            continue
        em = entry_re.match(line)
        if em:
            res = process_entry(line)
            if res != line:
                done += 1
                if LIMIT and done >= LIMIT:
                    STOP = True
            out.append(res)
            expect_intro = False
            continue
        if header_re.match(line):
            out.append(line)
            expect_intro = True
            continue
        if toc_re.match(line) or backtop_re.search(line) or anchor_re.match(line):
            out.append(line)
            continue
        if expect_intro and is_prose(line):
            out.append(translate(line))
            expect_intro = False
            continue
        out.append(line)

    open(SRC, "w", encoding="utf-8").write("\n".join(out) + "\n")
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"translated this run: {done}; cache size: {len(cache)}; stopped_by_quota: {STOP}")

if __name__ == "__main__":
    main()
