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
    links = LINK_RE.findall(text)
    for i, lk in enumerate(links):
        text = text.replace(lk, f"\u0002L{i}\u0002", 1)
    q = urllib.parse.quote(text)
    url = ("https://api.mymemory.translated.net/get?q=%s"
           "&langpair=en|zh-CN&de=selfhost-translate@example.com") % q
    backoff = 20
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            data = json.load(urllib.request.urlopen(req, timeout=15))
            st = data.get("responseStatus")
            t = data.get("responseData", {}).get("translatedText", "")
            # 真正的配额耗尽：停止且不缓存，便于后续续传重试
            if st == 200 and t:
                if "YOU USED ALL" in t.upper() or "QUOTA" in str(data.get("responseDetails", "")).upper():
                    STOP = True
                    return text
                for i, lk in enumerate(links):
                    t = t.replace(f"\u0002L{i}\u0002", lk)
                cache[text] = t
                time.sleep(DELAY)
                return t
            # 429 限流：退避后重试；持续限流则优雅停止（不缓存，下次续传）
            if st == 429:
                if attempt < retries - 1:
                    time.sleep(backoff)
                    backoff = min(backoff * 2, 120)
                    continue
                STOP = True
                return text
            if st in (402, 403) or "QUOTA" in str(data.get("responseDetails", "")).upper():
                STOP = True
                return text
        except Exception:
            time.sleep(2)
    # 网络/解析失败：保留原文，不缓存（下次重试）
    return text

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
