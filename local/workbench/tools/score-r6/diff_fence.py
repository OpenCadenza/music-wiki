#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""diff_fence (score-r6)：把正文里的围栏与已验证草稿逐行对比（防止 edit 手抄串行）。"""
import difflib
import io
import sys


def find_fence(text, fid):
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("```lilypond") and ('id="%s"' % fid) in ln:
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            return "\n".join(lines[i + 1:j])
    return None


def draft_body(path):
    lines = io.open(path, encoding="utf-8").read().split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("```lilypond"):
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            return "\n".join(lines[i + 1:j])
    return None


def main():
    doc, draft, fid = sys.argv[1], sys.argv[2], sys.argv[3]
    body = find_fence(io.open(doc, encoding="utf-8").read(), fid)
    dbody = draft_body(draft)
    if body is None:
        print("!! 正文里找不到 id=%s 的围栏" % fid)
        return 1
    same = body.strip() == dbody.strip()
    print("与已验证草稿一致:", same)
    if not same:
        for line in difflib.unified_diff(dbody.strip().split("\n"), body.strip().split("\n"),
                                         fromfile="draft", tofile="content",
                                         lineterm="", n=0):
            print(line[:200])
    return 0 if same else 1


if __name__ == "__main__":
    raise SystemExit(main())
