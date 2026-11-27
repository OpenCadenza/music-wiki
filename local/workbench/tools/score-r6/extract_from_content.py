#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""extract_from_content (score-r6)：从正文按 id 抽出围栏为 .ly，便于直接编译自测。"""
import io
import sys


def main():
    doc, fid, out = sys.argv[1], sys.argv[2], sys.argv[3]
    lines = io.open(doc, encoding="utf-8").read().split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("```lilypond") and ('id="%s"' % fid) in ln:
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            io.open(out, "w", encoding="utf-8", newline="\n").write(
                "\n".join(lines[i + 1:j]) + "\n")
            print("extracted %d lines -> %s" % (j - i - 1, out))
            return 0
    print("!! 找不到 id=%s" % fid)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
