#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CCARH MuseData（.md2）→ LilyPond 片段生成器（Op.125 第一乐章）。

MuseData 口径（已被第二源 MuseScore MXL 交叉确认，见 downloads/beethoven-op125-i/第二源核对-op125.md）：
  * 每个 part 自带 `$ … Q:n`：弦乐/木管/定音鼓 Q:24（2/4 每小节 48 divisions）；
    圆号/小号 Q:8（每小节 16 divisions）。
  * **行首有一个空格的音符 = 和弦音**：与上一音**同一发响点**，不推进时间。
  * `back N` 才是换声部；`rest` / `irest` 是（可见/不可见）休止；`P …`、`*` 行是排版/力度控制行，不是音符。
  * 连续同一（和弦）音高、时值 = 1/6 四分音符 = 弦乐 tremolo，折叠为 `\\tuplet 3/2 { …16 ×12 }`（一小节一组）。
移调（写实音；依据第二源 MXL 的 <transpose> 属性）：
  Clarinetti in B♭ −2；Corni in D −10；Corno 3,4 in B♭ basso −14；Trombe in D **+2**；Contrabasso −12。
用法：python md2_score.py <file.md2> <out.ly> <start> <end> [--barchecks]
"""
import re
import sys

SEMI = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
NAMES = ["c", "cs", "d", "ef", "e", "f", "fs", "g", "af", "a", "bf", "b"]
PITCH_RE = re.compile(r"^([A-G])([#\-nsf]*)(\d+)$")
LY_OCT = {1: ",,", 2: ",", 3: "", 4: "'", 5: "''", 6: "'''", 7: "''''", 8: "'''''"}
BARCHECKS = False

SPEC = [
    (1, "flauti", "flute", "treble", 0, "Flauti 1, 2"),
    (2, "oboi", "oboe", "treble", 0, "Oboe 1, 2"),
    (3, "clarinetti", "clarinet", "treble", -2, "Clarinetti 1, 2 in B♭（实音）"),
    (4, "fagotti", "bassoon", "bass", 0, "Fagotto 1, 2"),
    (5, "corni", "french horn", "treble", -10, "Corni 1, 2 in D（实音）"),
    (6, "corniBassi", "french horn", "treble", -14, "Corno 3, 4 in B♭ basso（实音）"),
    (7, "trombe", "trumpet", "treble", 2, "Trombe 1, 2 in D（实音）"),
    (8, "timpani", "timpani", "bass", 0, "Timpani in D, A"),
    (9, "violinoI", "violin", "treble", 0, "Violino I"),
    (10, "violinoII", "violin", "treble", 0, "Violino II"),
    (11, "viola", "viola", "alto", 0, "Viola"),
    (12, "violoncello", "cello", "bass", 0, "Violoncello"),
    (13, "contrabass", "contrabass", "bass", -12, "Contrabasso（实音）"),
]


def parse_pitch_midi(p):
    m = PITCH_RE.match(p)
    if not m:
        return None
    letter, acc, octv = m.group(1).lower(), m.group(2), int(m.group(3))
    semi = SEMI[letter]
    for ch in acc:
        if ch in "#s":
            semi += 1
        elif ch in "-f":
            semi -= 1
    return (octv + 1) * 12 + semi


def ly_pitch(midi):
    return NAMES[midi % 12] + LY_OCT.get(midi // 12 - 1, "'''''")


DUR = [(4.0, "1"), (3.0, "2."), (2.0, "2"), (1.5, "4."), (1.0, "4"),
       (0.875, "8.."), (0.75, "8."), (0.5, "8"), (0.375, "16."), (0.25, "16"),
       (0.125, "32"), (1.0 / 6, "T16"), (1.0 / 12, "T32"), (0.0625, "64")]


def dur_of(beats):
    for v, n in DUR:
        if abs(beats - v) < 1e-6:
            return n
    return None


def split_parts(lines):
    idx = []
    for i, ln in enumerate(lines):
        if ln.startswith("score: part"):
            no = int(re.match(r"score: part (\d+)", ln).group(1))
            name = ""
            for j in range(i - 1, max(0, i - 6), -1):
                if lines[j].startswith("First Movement"):
                    name = lines[j + 1].strip()
                    break
            idx.append((no, name, i))
    out = {}
    for k, (no, name, start) in enumerate(idx):
        end = idx[k + 1][2] - 8 if k + 1 < len(idx) else len(lines)
        out[no] = (name, lines[start:end])
    return out


def parse_part(body):
    """→ (q, {measure: {voice: [ (kind, pitches_tuple, divs, tie) ]}})"""
    q = 24
    for ln in body:
        m = re.match(r"^\$\s+.*Q:(\d+)", ln)
        if m:
            q = int(m.group(1))
            break
    measures, cur, voice = {1: {}}, 1, 1
    for ln in body:
        if ln.startswith("measure "):
            cur = int(re.match(r"measure (\d+)", ln).group(1))
            voice = 1
            measures.setdefault(cur, {})
            continue
        if ln.startswith("back"):
            voice += 1
            continue
        s = ln.strip()
        if not s:
            continue
        if s.startswith("rest") or s.startswith("irest"):
            m = re.match(r"irest\s+(\d+)", s) if s.startswith("irest") else re.match(r"rest\s+(\d+)", s)
            if m:
                measures[cur].setdefault(voice, []).append(("rest", (), int(m.group(1)), False))
            continue
        if s[0] not in "ABCDEFG":
            continue
        f = s.split()
        if len(f) < 3:
            continue
        try:
            divs = int(f[1].rstrip("-"))
        except ValueError:
            continue
        tie = f[1].endswith("-")
        evs = measures[cur].setdefault(voice, [])
        indented = ln[:1] in (" ", "\t")
        if indented and evs and evs[-1][0] == "note":
            # 和弦音：与上一音同起点
            kind, pitches, d0, t0 = evs[-1]
            evs[-1] = ("note", pitches + (f[0],), d0, t0 or tie)
        else:
            evs.append(("note", (f[0],), divs, tie))
    return q, measures


def render_voice(events_by_meas, q, shift, lo, hi):
    out = []
    for mm in range(lo, hi + 1):
        evs = events_by_meas.get(mm, [])
        if not evs:
            out.append("r2 |")
            continue
        bar_beats = 2.0
        total = sum(e[2] for e in evs) / float(q)
        if total > bar_beats + 1e-9:
            out.append("r2 |")
            continue
        toks = []
        i = 0
        while i < len(evs):
            kind, pitches, divs, tie = evs[i]
            beats = divs / float(q)
            if kind == "note" and abs(beats - 1.0 / 6) < 1e-6:
                j = i
                while j < len(evs) and evs[j][0] == "note" and evs[j][1] == pitches \
                        and abs(evs[j][2] / float(q) - 1.0 / 6) < 1e-6:
                    j += 1
                n = j - i
                p = chord_ly(pitches, shift)
                while n >= 12:
                    toks.append("\\tuplet 3/2 { %s }" % (" ".join([p + "16"] * 12)))
                    n -= 12
                if n:
                    toks.append("\\tuplet 3/2 { %s }" % (" ".join([p + "16"] * n)))
                i = j
                continue
            if kind == "rest":
                dn = dur_of(beats) or "8"
                toks.append("r" + (dn if not dn.startswith("T") else "16"))
                i += 1
                continue
            dn = dur_of(beats)
            if dn is None:
                toks.append("%%UNKNOWN(%s/%d)" % (pitches, divs))
                i += 1
                continue
            p = chord_ly(pitches, shift)
            nxt = evs[i + 1] if i + 1 < len(evs) else None
            tie_mark = ""
            if tie and nxt and nxt[0] == "note" and nxt[1] == pitches:
                tie_mark = "~"
            if dn.startswith("T"):
                toks.append("\\tuplet 3/2 { %s%s }" % (p, dn[1:]))
            else:
                toks.append(p + dn + tie_mark)
            i += 1
        # 1/24 为单位精确补足小节
        bar_beats = 2.0
        total = sum(e[2] for e in evs) / float(q)
        left24 = int(round((bar_beats - total) * 24))
        FILL24 = [(96, "1"), (72, "2."), (48, "2"), (36, "4."), (24, "4"),
                  (18, "8."), (12, "8"), (9, "16."), (6, "16"), (4, "T16"),
                  (3, "32"), (2, "T32")]
        while left24 > 0:
            for units, name in FILL24:
                if units <= left24:
                    if name.startswith("T"):
                        toks.append("\\tuplet 3/2 { r%s }" % name[1:])
                    else:
                        toks.append("r" + name)
                    left24 -= units
                    break
            else:
                toks.append("%%FILL_UNRESOLVED(%d)" % left24)
                break
        suffix = (" \\barNumberCheck #%d" % mm) if BARCHECKS else ""
        out.append(" ".join(toks) + " |" + suffix)
    return out


def chord_ly(pitches, shift):
    ps = [ly_pitch(parse_pitch_midi(x) + shift) for x in pitches]
    if len(ps) == 1:
        return ps[0]
    return "<" + " ".join(ps) + ">"


def main():
    global BARCHECKS
    BARCHECKS = "--barchecks" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path, outly, lo, hi = args[0], args[1], int(args[2]), int(args[3])
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    parts = split_parts(lines)
    body = ['\\version "2.26.0"', '\\language "english"', ""]
    body.append("%% 贝多芬 第九交响曲 Op.125 第一乐章 Allegro ma non troppo, un poco maestoso，mm.%d–%d" % (lo, hi))
    body.append("%% 底本：CCARH MuseData `sym9-mvmt1.md2`（依 Breitkopf & Härtel 全集 / Bennion 2005；非 CC0）")
    body.append("%%       per-part Q 已分别换算（弦乐/木管/定音鼓 Q:24；圆号/小号 Q:8）；行首缩进音 = 和弦音。")
    body.append("%% 移调乐器写实音（不写 \\transposition）：Cl in B♭ −2；Hn in D −10；Hn3,4 in B♭ basso −14；Tr in D +2；Cb −12。")
    body.append("%% 弦乐 tremolo 按底本实际时值（每音 1/6 四分音符）折叠为十六分三连音组。")
    body += ["global = {", "  \\key d \\minor", "  \\time 2/4",
             '  \\tempo "Allegro ma non troppo" 2 = 88', "}", ""]
    used = []
    for no, var, gm, clef, shift, label in SPEC:
        name, pbody = parts[no]
        q, meas = parse_part(pbody)
        voices = {}
        for mm in range(lo, hi + 1):
            for v, evs in meas.get(mm, {}).items():
                voices.setdefault(v, {})[mm] = evs
        if not voices:
            continue
        has_notes = any(any(e[0] == "note" for e in evs)
                       for mmd in voices.values() for evs in mmd.values())
        if not has_notes:
            continue
        rendered = {v: render_voice(ev, q, shift, lo, hi) for v, ev in voices.items()}
        body.append("%% ---- %s ----" % label)
        body.append("%s = {" % var)
        body += ["  \\global", "  \\clef %s" % clef, '  \\set Staff.midiInstrument = "%s"' % gm]
        if len(rendered) == 1:
            for b in rendered[min(rendered)]:
                body.append("  " + b)
        else:
            v1 = rendered.get(1) or rendered[min(rendered)]
            v2 = rendered.get(2) or ["r2 |"] * (hi - lo + 1)
            body.append("  <<")
            body.append("    { " + " ".join(v1) + " }")
            body.append("    \\\\")
            body.append("    { " + " ".join(v2) + " }")
            body.append("  >>")
        body.append("}")
        body.append("")
        used.append(var)
    body.append("#(set-global-staff-size 11)")
    body.append('\\paper { #(set-paper-size "a4landscape") }')
    body.append("")
    body += ["\\score {", "  <<", "    \\new StaffGroup <<"]
    for var in used:
        body.append("      \\new Staff \\%s" % var)
    body += ["    >>", "  >>", "  \\layout { ragged-right = ##f }", "  \\midi { }", "}"]
    open(outly, "w", encoding="utf-8").write("\n".join(body) + "\n")
    print("written", outly, "staves:", len(used))


if __name__ == "__main__":
    main()
