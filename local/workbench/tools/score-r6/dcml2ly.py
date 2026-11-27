#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""dcml2ly (score-r6)：从 DCML notes.tsv 生成钢琴谱 LilyPond 围栏（用于 K.494 开篇）。

DCML 行给出 mn（刊本小节号）、staff、voice、mn_onset、duration_qb、name（如 Bb4）、tied。
本脚本按 (小节, 谱表, 声部) 归组，onset 相同者写和弦，多声部用 << { } \\\\ { } >> 分层。
"""
import csv
import re
from fractions import Fraction

STEP_SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def qb_frac(s):
    s = str(s).strip()
    if "/" in s:
        return Fraction(s)
    return Fraction(round(float(s) * 48), 48)


def ly_pitch(name):
    m = re.match(r"^([A-G])([#b]?)(-?\d+)$", name)
    if not m:
        raise ValueError("无法解析音名 %r" % name)
    letter, acc, octv = m.group(1), m.group(2), int(m.group(3))
    out = letter.lower()
    if acc == "#":
        out += "s"
    elif acc == "b":
        out += "f"
    marks = octv - 3          # c' = C4
    out += "'" * marks if marks > 0 else "," * (-marks)
    return out


def dur_to_ly(frac):
    for dots in range(4):
        factor = sum(Fraction(1, 2 ** i) for i in range(dots + 1))
        for denom in (1, 2, 4, 8, 16, 32, 64, 128, 256):
            if frac == Fraction(1, denom) * factor:
                return str(denom) + "." * dots
    raise ValueError("无法表示的时值 %s" % frac)


def read_rows(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def rest_frac_series(frac):
    """把一段长度拆成若干可写的休止时值（贪心，优先大时值）。"""
    out = []
    guard = 0
    while frac > 0 and guard < 32:
        guard += 1
        best = None
        for dots in range(4):
            factor = sum(Fraction(1, 2 ** i) for i in range(dots + 1))
            for denom in (1, 2, 4, 8, 16, 32, 64, 128, 256):
                val = Fraction(1, denom) * factor
                if val <= frac and (best is None or val > best[0]):
                    best = (val, str(denom) + "." * dots)
        if best is None:
            break
        out.append("r" + best[1])
        frac -= best[0]
    return out


def build_staff(rows, meter_qb):
    """rows: 同一谱表同一小节的音符行 -> 每声部一个 LilyPond 串（补齐休止）。"""
    voices = {}
    for r in rows:
        voices.setdefault(r["voice"], []).append(r)
    outs = []
    for vname in sorted(voices):
        rs = sorted(voices[vname], key=lambda r: qb_frac(r["mn_onset"]) * 4)
        evs = []
        cursor = Fraction(0)
        i = 0
        while i < len(rs):
            onset = qb_frac(rs[i]["mn_onset"]) * 4   # mn_onset 以全音符分数计
            if onset > cursor:
                evs.extend(rest_frac_series(Fraction(onset - cursor, 4)))
                cursor = onset
            group = [rs[i]]
            j = i + 1
            while j < len(rs) and qb_frac(rs[j]["mn_onset"]) * 4 == onset:
                group.append(rs[j])
                j += 1
            dur = max(qb_frac(g["duration_qb"]) for g in group) / 4
            pitches = [ly_pitch(g["name"]) for g in group if float(g["duration_qb"]) > 0]
            if not pitches:
                i = j
                continue
            dly = dur_to_ly(dur)
            tie = any(g.get("tied") in ("1", "start", "continue") for g in group)
            if len(pitches) == 1:
                ev = pitches[0] + dly
            else:
                ev = "<" + " ".join(sorted(pitches)) + ">" + dly
            if tie:
                ev += "~"
            evs.append(ev)
            cursor = onset + dur * 4
            i = j
        if cursor < meter_qb:
            evs.extend(rest_frac_series(Fraction(meter_qb - cursor, 4)))
        outs.append(" ".join(evs))
    return outs


def measure_lines(rows, first, last, staff_map=None):
    by_mn = {}
    meter_by_mn = {}
    for r in rows:
        mn = int(float(r["mn"]))
        if first <= mn <= last:
            by_mn.setdefault(mn, []).append(r)
            meter_by_mn[mn] = r.get("timesig", "2/2")
    lines = {"upper": [], "lower": []}
    used = set()
    for mn in sorted(by_mn):
        num, den = meter_by_mn[mn].split("/")
        meter_qb = Fraction(int(num) * 4, int(den))
        for st, var in (("1", "upper"), ("2", "lower")):
            rs = [r for r in by_mn[mn] if r["staff"] == st]
            if not rs:
                lines[var].append("s1 |")
                continue
            parts = build_staff(rs, meter_qb)
            for r in rs:
                used.add(int(float(r["midi"])))
            if len(parts) == 1:
                lines[var].append(parts[0] + " |")
            else:
                body = " \\\\ ".join("{ %s }" % p for p in parts)
                lines[var].append("<< %s >> |" % body)
    return lines, sorted(used)


def fence(tsv, first, last, key, time, tempo, title, location, fid, comments):
    rows = read_rows(tsv)
    lines, used = measure_lines(rows, first, last)
    out = ['```lilypond title="%s" location="%s" id="%s"' % (title, location, fid),
           '\\version "2.26.0"', '\\language "english"', ""]
    for c in comments:
        out.append("% " + c)
    out.append("")
    out.append("global = {")
    out.append("  \\key %s" % key)
    out.append("  \\time %s" % time)
    out.append("  \\tempo %s" % tempo)
    out.append("}")
    out.append("")
    lower_clef = "treble" if min(used) >= 55 else "bass"
    for var, clef in (("upper", "treble"), ("lower", lower_clef)):
        out.append("%s = {" % var)
        out.append("  \\global")
        out.append("  \\clef %s" % clef)
        out.append('  \\set Staff.midiInstrument = "acoustic grand"')
        for ln in lines[var]:
            out.append("  " + ln)
        out.append("}")
        out.append("")
    out.append("\\score {")
    out.append("  \\new PianoStaff <<")
    out.append('    \\new Staff { \\set Staff.midiInstrument = "acoustic grand" \\upper }')
    out.append('    \\new Staff { \\set Staff.midiInstrument = "acoustic grand" \\lower }')
    out.append("  >>")
    out.append("  \\layout { ragged-right = ##f }")
    out.append("  \\midi { }")
    out.append("}")
    out.append("```")
    return "\n".join(out) + "\n"
