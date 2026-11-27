#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""verify_all (score-r6)：把每个围栏草稿编译出的 MIDI 与底本音高做回比对。

比对口径：
- 音高**集合**必须一致（抓八度、变音记号、和弦漏音）；
- 音数差异单独报告，通常来自连音线（LilyPond 在 MIDI 里合并连音）与装饰音（本工具不展开）。
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import abc2ly
import md2parse
from verify_midi import read_midi

SRC = os.path.join("local", "resources", "scores", "source-packages", "humdrum", "mozart-sonatas")
TMP = os.path.join("local", "workbench", "tmp", "mozart-r6")
MD2 = os.path.join("local", "origin_resources", "sources",
                   "ccarh-musedata-concertos", "mozart-k467-mvt1.md2")

ABC_TARGETS = [
    ("k331-theme", "0043-43-Piano Sonata No. 11 in A major, K 331 (300i), mvmt. 1a.abc", 1, 8),
    ("k331-var1", "0044-44-Piano Sonata No. 11 in A major, K 331 (300i), mvmt. 1b.abc", 19, 26),
    ("k331-var3", "0046-46-Piano Sonata No. 11 in A major, K 331 (300i), mvmt. 1d.abc", 1, 18),
    ("k545-cadence", "0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc", 5, 8),
    ("k545-ic", "0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc", 22, 26),
    ("k545-dev", "0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc", 29, 42),
    ("k332-compound", "0052-52-Piano Sonata No. 12 in F major, K 332 (300k), mvmt. 1.abc", 41, 56),
    ("k284-ii", "0017-17-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 2.abc", 1, 16),
]

K467_STAFFS = ["Vln_1_", "Vln_2_", "Vc_"]


def abc_expected(fname, first, last):
    data = abc2ly.parse_abc(os.path.join(SRC, fname))
    out = []
    for vn in data["order"]:
        for m in data["voices"][vn].measures:
            if first <= m.number <= last:
                out.extend(abc2ly.measure_pitches(m))
    return out


def k467_expected(first, last):
    parts = {p["name"]: p for p in md2parse.parse(MD2)}
    out = []
    for name in K467_STAFFS:
        for meas in parts[name]["measures"]:
            if first <= meas["num"] <= last:
                for n in meas["notes"]:
                    tok = n.get("tok") or ""
                    if n["pitch"] is not None and not tok.startswith("g"):
                        out.append(n["pitch"])
    return out


def cmp(name, want, got):
    sw, sg = sorted(set(want)), sorted(set(got))
    ok = sw == sg
    print("%-16s MIDI=%4d 底本=%4d  音高集合%s" % (name, len(got), len(want), "一致" if ok else "不一致"))
    if not ok:
        print("   仅在底本:", [p for p in sw if p not in sg])
        print("   仅在 MIDI:", [p for p in sg if p not in sw])
    if len(got) != len(want):
        print("   （音数差 %+d：连音线在 MIDI 中合并 / 装饰音未展开）" % (len(got) - len(want)))
    return ok


def main():
    allok = True
    for key, fname, first, last in ABC_TARGETS:
        mid = os.path.join(TMP, "out-" + key + ".mid")
        if not os.path.exists(mid):
            print("%-16s 缺少 MIDI（未编译？）" % key)
            allok = False
            continue
        allok &= cmp(key, abc_expected(fname, first, last), read_midi(mid))
    mid = os.path.join(TMP, "out-k467-i-9-28.fence.mid")
    if os.path.exists(mid):
        allok &= cmp("k467-i-9-28", k467_expected(9, 28), read_midi(mid))
    else:
        print("k467-i-9-28 缺少 MIDI")
        allok = False
    print("\n总体:", "全部一致" if allok else "存在差异")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
