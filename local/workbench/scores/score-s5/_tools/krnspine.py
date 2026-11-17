"""Spine-tracking **kern parser -> per-staff, per-voice, per-measure event streams.

Handles Humdrum spine manipulators (*^ split, *v join, *- terminate), *staffN
assignment, chords (space-separated tokens within one spine), ties, rests,
dotted durations, and articulation/beam markers.

Usage: python krnspine.py <file.krn> <m0> <m1>
"""
import re
import sys

NAMES = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]
KERNPITCH = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}


def parse_pitch(token):
    """-> (midi, dur_str, tie_start, tie_stop) or None"""
    m = re.match(r"^([\[\(\{<>]*)(\d+)(\.*)([A-Ga-g]+)([#\-n]*)(.*)$", token)
    if not m:
        return None
    _, dur, dots, letters, acc, rest = m.groups()
    n = len(letters)
    base = letters[0]
    pc = KERNPITCH[base.lower()]
    for a in acc:
        if a == "-":
            pc -= 1
        elif a == "#":
            pc += 1
    octv = (4 + (n - 1)) if base.islower() else (3 - (n - 1))
    pass  # octave comes from letter case/repetition only; ' and , are articulations
    midi = (octv + 1) * 12 + pc
    return (midi, dur + dots, "[" in rest, "]" in rest)


def is_rest(token):
    return bool(re.match(r"^[\[\(\{<>]*\d+\.*r", token))


def lp(midi):
    name = NAMES[midi % 12]
    apos = midi // 12 - 4
    return name + ("'" * apos if apos >= 0 else "," * (-apos))


def main():
    path, m0, m1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()

    spines = None          # list of {'kern':bool,'staff':int}
    measure = 0
    events = []            # (measure, staff, voice_slot, ev)

    for line in lines:
        if not line.strip():
            continue
        if line.startswith("**"):
            toks = line.split("\t")
            spines = [{"kern": t.strip() == "**kern", "staff": 1} for t in toks]
            continue
        if spines is None:
            continue
        if line.startswith("!!"):
            continue
        if line.startswith("!") and not line.startswith("!!"):
            continue
        if line.startswith("*"):
            toks = line.split("\t")
            new = []
            i = 0
            while i < len(toks):
                tok = toks[i].strip()
                cur = spines[i] if i < len(spines) else {"kern": False, "staff": 1}
                if tok == "*^":
                    new.append(dict(cur))
                    new.append(dict(cur))
                    i += 1
                elif tok == "*v":
                    new.append(dict(cur))
                    i += 2          # consume partner spine
                elif tok == "*-":
                    i += 1          # spine ends
                else:
                    ms = re.match(r"^\*staff(\d+)$", tok)
                    s = dict(cur)
                    if ms:
                        s["staff"] = int(ms.group(1))
                    new.append(s)
                    i += 1
            spines = new
            continue
        if line.startswith("="):
            mm = re.match(r"=(\d+)", line)
            if mm:
                measure = int(mm.group(1))
            continue
        if not (m0 <= measure <= m1):
            continue

        toks = line.split("\t")
        # voice slot = index among kern spines of same staff
        seen = {}
        for si in range(min(len(toks), len(spines))):
            sp = spines[si]
            if not sp["kern"]:
                continue
            slot = seen.get(sp["staff"], 0)
            seen[sp["staff"]] = slot + 1
            raw = toks[si].strip()
            if not raw or raw == ".":
                continue
            parts = [p for p in raw.split() if p and p != "."]
            if not parts:
                continue
            if is_rest(parts[0]):
                dm = re.match(r"^(\d+)(\.*)r", parts[0])
                events.append((measure, sp["staff"], slot, ("r", dm.group(1) + dm.group(2))))
                continue
            chord, dur, ts, te = [], None, False, False
            for p in parts:
                pr = parse_pitch(p)
                if pr is None:
                    continue
                chord.append(pr[0])
                dur = pr[1]
                ts = ts or pr[2]
                te = te or pr[3]
            if chord:
                events.append((measure, sp["staff"], slot, (sorted(chord), dur, ts, te)))

    staffs = sorted({e[1] for e in events})
    for st in staffs:
        print(f"\n########## STAFF {st}")
        slots = sorted({e[2] for e in events if e[1] == st})
        for sl in slots:
            print(f"  --- voice slot {sl} ---")
            cur_m = None
            out = []
            for meas, s, slot, ev in events:
                if s != st or slot != sl:
                    continue
                if meas != cur_m:
                    if cur_m is not None:
                        print(f"   m{cur_m}: " + " ".join(out))
                    cur_m = meas
                    out = []
                if ev[0] == "r":
                    out.append("r" + ev[1])
                else:
                    chord, d, ts, te = ev
                    tok = ("<" + " ".join(lp(c) for c in chord) + ">") if len(chord) > 1 else lp(chord[0])
                    tok += d
                    if ts:
                        tok += "~"
                    if te:
                        tok += "^"
                    out.append(tok)
            if cur_m is not None:
                print(f"   m{cur_m}: " + " ".join(out))


if __name__ == "__main__":
    main()

