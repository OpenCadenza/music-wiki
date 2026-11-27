#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""build_k467 (score-r6)：从 CCARH md2 生成 K.467 I mm.9-28 的 LilyPond 围栏草稿。

用法：python build_k467.py [--from 9] [--to 28] [--out file.ly]
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import md2parse
from md2ly import part_to_ly

MD2 = os.path.join("local", "origin_resources", "sources",
                   "ccarh-musedata-concertos", "mozart-k467-mvt1.md2")

STAFFS = [
    # (分谱名, LilyPond 变量名, 谱号, GM 乐器, 注释)
    ("Vln_1_", "violinoI", "treble", "violin", "Violino I"),
    ("Vln_2_", "violinoII", "treble", "violin", "Violino II"),
    ("Vc_", "violoncello", "bass", "cello", "Violoncello e Contrabasso"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="first", type=int, default=9)
    ap.add_argument("--to", dest="last", type=int, default=28)
    ap.add_argument("--out", default="")
    ap.add_argument("--title", default="莫扎特 第21钢琴协奏曲 K.467 第一乐章")
    ap.add_argument("--loc", default="Allegro maestoso，mm.9–28（全奏动能过渡：弦乐十六分音符冲刺与八分音符步态）")
    ap.add_argument("--id", default="mozart-k467-i-mm9-28")
    args = ap.parse_args()

    parts = md2parse.parse(MD2)
    byname = {p["name"]: p for p in parts}
    bodies = []
    for name, var, clef, gm, label in STAFFS:
        lines = part_to_ly(byname[name], args.first, args.last)
        bodies.append((var, clef, gm, label, lines))

    out = []
    out.append('```lilypond title="%s" location="%s" id="%s"' % (args.title, args.loc, args.id))
    out.append('\\version "2.26.0"')
    out.append('\\language "english"')
    out.append("")
    out.append("% 莫扎特 C 大调第 21 钢琴协奏曲 K.467 第一乐章 mm.{}-{}：乐队利都奈罗的动能过渡段。"
               .format(args.first, args.last))
    out.append("% 据 CCARH MuseData（Neue Mozart-Ausgabe 转录）核对后自编码摘录，学术用途；")
    out.append("% 试听速度 4=120 为编选，非原谱标记。谱表只取论证需要的弦乐三组：")
    out.append("% 第一小提琴（十六分音符音阶/琶音冲刺）、第二小提琴（平行三度跟随）、")
    out.append("% 大提琴与低音提琴（同声部，八分音符步态）。本段木管与铜管在上方以持续和弦加入，此处不列。")
    out.append("% 小节号按刊本印刷号；底本 md2 的 measure 行与本段一一对应（m.11 为全休止）。")
    out.append("")
    out.append("global = {")
    out.append("  \\key c \\major")
    out.append("  \\time 4/4")
    out.append('  \\tempo "Allegro maestoso" 4 = 120')
    out.append("}")
    out.append("")
    for var, clef, gm, label, lines in bodies:
        out.append("% " + label)
        out.append("%s = {" % var)
        out.append("  \\global")
        out.append("  \\clef " + clef)
        out.append('  \\set Staff.midiInstrument = "%s"' % gm)
        for ln in lines:
            out.append("  " + ln)
        out.append("}")
        out.append("")
    out.append("\\score {")
    out.append("  \\new StaffGroup <<")
    for var, clef, gm, label, lines in bodies:
        out.append('    \\new Staff { \\set Staff.midiInstrument = "%s" \\%s }' % (gm, var))
    out.append("  >>")
    out.append("  \\layout { ragged-right = ##f }")
    out.append("  \\midi { }")
    out.append("}")
    out.append("```")
    text = "\n".join(out) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote", args.out, len(text), "chars")
    else:
        print(text)


if __name__ == "__main__":
    main()
