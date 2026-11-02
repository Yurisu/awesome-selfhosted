#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 README.zh-CN.md 中被泄漏的链接占位符 \u0002L{i}\u0002。

根因：translate() 在 429 限流失败分支返回了已被替换成占位符的 text，
导致这些行的 [text](url) 链接永久丢失。这些行本就是未翻译的英文条目，
因此直接从源文件 README.md 还原其原始英文说明（含完整链接）。
"""
import re

SRC = "README.md"
DST = "README.zh-CN.md"

entry_re = re.compile(r'^(\s*)- \[([^\]]+)\]\((https?://[^)]+)\)')

def strip_links(s):
    s = re.sub(r'\[[^\]]*\]\(https?://[^)]+\)', '', s)
    s = re.sub(r'\u0002L\d+\u0002', '', s)
    return re.sub(r'\s+', ' ', s).strip()

# 建立源文件索引
src_lines = open(SRC, encoding="utf-8").read().split("\n")
entry_map = {}          # (name, url) -> source line
linkkey_map = {}        # strip_links key -> source line
for ln in src_lines:
    m = entry_re.match(ln)
    if m:
        entry_map[(m.group(2), m.group(3))] = ln
    key = strip_links(ln)
    if key and key not in linkkey_map:
        linkkey_map[key] = ln

lines = open(DST, encoding="utf-8").read().split("\n")
out = []
fixed = 0
for ln in lines:
    if "\u0002" not in ln:
        out.append(ln)
        continue
    m = entry_re.match(ln)
    replaced = None
    if m:
        repl = entry_map.get((m.group(2), m.group(3)))
        if repl:
            replaced = repl
    if replaced is None:
        key = strip_links(ln)
        replaced = linkkey_map.get(key)
    if replaced is not None:
        out.append(replaced)
        fixed += 1
    else:
        # 兜底：仅把占位符移除（不应发生）
        out.append(re.sub(r'\u0002L\d+\u0002', '', ln))
        fixed += 1

open(DST, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"repaired lines: {fixed}")
leaked = open(DST, encoding="utf-8").read().count("\u0002")
print("remaining leaked \\u0002:", leaked)
