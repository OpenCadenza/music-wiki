#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""extract_ly (score-r6)：把草稿 .md 里的 lilypond 围栏抽出为可编译 .ly，便于本地编译自测。"""
import glob
import io
import os
import re

FENCE = re.compile(r"^```lilypond[^\n]*\n(.*?)\n```\s*$", re.S | re.M)


def main():
    d = r"local/workbench/tmp/mozart-r6"
    for f in sorted(glob.glob(os.path.join(d, "*.md"))):
        t = io.open(f, encoding="utf-8").read()
        m = FENCE.search(t)
        if not m:
            print("NOFENCE", f)
            continue
        ly = os.path.splitext(f)[0] + ".ly"
        io.open(ly, "w", encoding="utf-8", newline="\n").write(m.group(1) + "\n")
        print("extracted", os.path.basename(ly), len(m.group(1)))


if __name__ == "__main__":
    main()
