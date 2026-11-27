#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""replace_fence (score-r6)：按 id 定位既有围栏整块替换为草稿（用于底本修正后的重出谱）。"""
import io
import re
import sys

TARGETS = [
    dict(
        target=r"content/techniques/structure/concertante-principle-and-double-exposition.md",
        fid="mozart-k467-i-mm9-28",
        fence=r"local/workbench/tmp/mozart-r6/k467-i-9-28.fence.md",
    ),
]


def main():
    for t in TARGETS:
        src = io.open(t["target"], encoding="utf-8").read()
        lines = src.split("\n")
        starts = [i for i, ln in enumerate(lines)
                  if ln.startswith("```lilypond") and ('id="%s"' % t["fid"]) in ln]
        if len(starts) != 1:
            print("!! %s：id=%s 命中 %d 次" % (t["target"], t["fid"], len(starts)))
            continue
        start = starts[0]
        end = start + 1
        while end < len(lines) and lines[end].strip() != "```":
            end += 1
        block = io.open(t["fence"], encoding="utf-8").read().rstrip("\n").split("\n")
        lines[start:end + 1] = block
        io.open(t["target"], "w", encoding="utf-8", newline="\n").write("\n".join(lines))
        print("OK %s ← %s（原 %d 行 → 新 %d 行）" % (t["target"], t["fence"], end - start + 1, len(block)))


if __name__ == "__main__":
    main()
