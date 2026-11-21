#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MuseData Stage-2 (.md2) 解析器：按 part × measure 抽出音高/时值/连音线，供 Op.125 谱例编码。

格式要点（CCARH MuseData）：
  * `Q:24`  —— 每四分音符 24 divisions，故 24=四分、48=二分、12=八分、6=十六分、3=三十二分、72=附点二分、36=附点四分
  * `measure N` 标记小节起点（其后的记录属于该小节）
  * 音符/休止记录：第 1 段=音高（字母+八度+可选变化音记在字母后，如 A5 / C#4 / B-3），第 2 段=divs（带 `-` 表示连音），
    第 3 段=voice 号，第 4 段=时值类型（h/q/e/t/s/w，`.`=附点、`:`=双附点），后面是符干/连音线等
  * `rest  <divs> <voice>` = 休止；`back <divs>` = 该小节内另起一声部；`*`/`P` 行是排版与力度注解，忽略
用法：
  python md2_parse.py <file.md2> <part_no> <start_measure> <end_measure> [--ly]
"""
import re
import sys

PITCH_RE = re.compile(r"^([A-Ga-g])([#\-n]?)([0-9]+)$")
DURNAME = {24: "4", 48: "2", 12: "8", 6: "16", 3: "32", 96: "1", 72: "2.", 36: "4.",
           18: "8.", 9: "16.", 4: "32", 6: "16"}
LY_OCT = {0: ",,,", 1: ",,", 2: ",", 3: "", 4: "'", 5: "''", 6: "'''", 7: "''''"}


def ly_pitch(p):
    m = PITCH_RE.match(p)
    if not m:
        return None
    letter, acc, octv = m.group(1).lower(), m.group(2), int(m.group(3))
    a = ""
    if acc == "#":
        a = "s"
    elif acc == "-":
        a = "f"
    return letter + a + LY_OCT.get(octv, "")


def split_parts(lines):
    """按 `score: part N of M` 切分 part 块，返回 {part_no: (name, [lines])}"""
    parts = {}
    idx = []
    for i, ln in enumerate(lines):
        if ln.startswith("score: part"):
            no = int(re.match(r"score: part (\d+)", ln).group(1))
            name = ""
            for j in range(i - 1, max(0, i - 6), -1):
                if lines[j].startswith("First Movement"):
                    name = lines[j + 1].strip() if j + 1 < len(lines) else ""
                    break
            idx.append((no, name, i))
    for k, (no, name, start) in enumerate(idx):
        end = idx[k + 1][2] - 8 if k + 1 < len(idx) else len(lines)
        parts[no] = (name, lines[start:end])
    return parts


def parse_part(body, start_meas=None, end_meas=None):
    """返回 {measure: {voice: [ (kind, pitch_or_None, divs, type, tie) ]}}，保持记录顺序"""
    out = {}
    cur = None
    voice = 1
    for ln in body:
        if ln.startswith("measure "):
            mm = re.match(r"measure (\d+)", ln)
            if mm:
                cur = int(mm.group(1))
                voice = 1
                out.setdefault(cur, {})
            continue
        if cur is None:
            continue
        if start_meas is not None and cur < start_meas:
            continue
        if end_meas is not None and cur > end_meas:
            continue
        if ln.startswith("back"):
            voice += 1
            continue
        if ln.startswith("rest"):
            m = re.match(r"rest\s+(\d+)", ln)
            if m:
                out[cur].setdefault(voice, []).append(("rest", None, int(m.group(1)), None, False))
            continue
        if not ln or ln[0] not in "ABCDEFGabcdefg":
            continue
        fields = ln.split()
        if len(fields) < 3:
            continue
        pitch = fields[0]
        dur_field = fields[1]
        try:
            divs = int(dur_field.rstrip("-"))
        except ValueError:
            continue
        try:
            v = int(fields[2])
        except ValueError:
            v = voice
        typ = fields[3] if len(fields) > 3 else ""
        tie = dur_field.endswith("-") or ("-" in (fields[-1] if fields else ""))
        out[cur].setdefault(v, []).append(("note", pitch, divs, typ, tie))
    return out


def main():
    path, part = sys.argv[1], int(sys.argv[2])
    lo = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    hi = int(sys.argv[4]) if len(sys.argv) > 4 else 40
    as_ly = "--ly" in sys.argv
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    parts = split_parts(lines)
    name, body = parts[part]
    data = parse_part(body, lo, hi)
    print("# part %d: %s" % (part, name))
    for mm in range(lo, hi + 1):
        if mm not in data:
            continue
        print("== measure %d ==" % mm)
        for v in sorted(data[mm]):
            evs = data[mm][v]
            if as_ly:
                items = []
                for kind, pitch, divs, typ, tie in evs:
                    if kind == "rest":
                        items.append("r" + DURNAME.get(divs, "?%d" % divs))
                    else:
                        p = ly_pitch(pitch)
                        items.append("%s%s%s" % (p, DURNAME.get(divs, "?%d" % divs), "~" if tie else ""))
                print("  v%d: %s" % (v, " ".join(items)))
            else:
                print("  v%d: %s" % (v, " | ".join(
                    ("%s(%d%s)" % (pitch, divs, "~" if tie else "")) if kind == "note" else ("rest%d" % divs)
                    for kind, pitch, divs, typ, tie in evs)))


if __name__ == "__main__":
    main()
