"""Per-measure cross-check of kern vs LilyPond MIDI for a piano fragment."""
import re
import struct
import sys
from collections import Counter

KERNPITCH = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}


def kern_notes(path, m0, m1):
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    spines, measure, out = None, 0, []
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("**"):
            spines = [{"kern": t.strip() == "**kern", "staff": 1} for t in line.split("\t")]
            continue
        if spines is None or line.startswith("!!"):
            continue
        if line.startswith("*"):
            toks, new, i = line.split("\t"), [], 0
            while i < len(toks):
                tok = toks[i].strip()
                cur = spines[i] if i < len(spines) else {"kern": False, "staff": 1}
                if tok == "*^":
                    new += [dict(cur), dict(cur)]
                    i += 1
                elif tok == "*v":
                    new.append(dict(cur))
                    i += 2
                elif tok == "*-":
                    i += 1
                else:
                    s = dict(cur)
                    ms = re.match(r"^\*staff(\d+)$", tok)
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
        for si in range(min(len(toks), len(spines))):
            sp = spines[si]
            if not sp["kern"]:
                continue
            raw = toks[si].strip()
            if not raw or raw == ".":
                continue
            if re.match(r"^[\[\(\{<>]*\d+\.*r", raw):
                continue
            for p in raw.split():
                m = re.match(r"^[\[\(\{<>]*(\d+)(\.*)([A-Ga-g]+)([#\-n]*)(.*)$", p)
                if not m:
                    continue
                dur, dots, letters, acc, rest = m.groups()
                # skip grace notes (q prefix inside dur) and tie continuations
                if "]" in rest or "_" in rest or "q" in dur:
                    continue
                n = len(letters)
                base = letters[0]
                pc = KERNPITCH[base.lower()]
                for a in acc:
                    if a == "-":
                        pc -= 1
                    elif a == "#":
                        pc += 1
                octv = (4 + (n - 1)) if base.islower() else (3 - (n - 1))
                out.append((measure, sp["staff"], (octv + 1) * 12 + pc))
    return out


def rd_vlq(buf, pos):
    v = 0
    while True:
        b = buf[pos]
        pos += 1
        v = (v << 7) | (b & 0x7F)
        if not (b & 0x80):
            return v, pos


def midi_notes(path):
    data = open(path, "rb").read()
    fmt, ntrks, div = struct.unpack(">HHH", data[8:14])
    pos = 14
    res = []
    for ti in range(ntrks):
        ln = struct.unpack(">I", data[pos + 4:pos + 8])[0]
        body = data[pos + 8:pos + 8 + ln]
        pos += 8 + ln
        p, t, status, notes = 0, 0, None, []
        while p < len(body):
            dt, p = rd_vlq(body, p)
            t += dt
            b = body[p]
            if b & 0x80:
                status = b
                p += 1
            ev = status & 0xF0
            if ev == 0x90:
                pitch, vel = body[p], body[p + 1]
                p += 2
                if vel > 0:
                    notes.append((t, pitch))
            elif ev in (0x80, 0xA0, 0xB0, 0xE0):
                p += 2
            elif ev in (0xC0, 0xD0):
                p += 1
            elif status == 0xFF:
                p += 1
                ln2, p = rd_vlq(body, p)
                p += ln2
            else:
                p += 1
        res.append((ti, notes))
    return res, div


def main():
    krn, mid = sys.argv[1], sys.argv[2]
    kn = kern_notes(krn, 1, 16)
    tracks, div = midi_notes(mid)
    tpm = div * 4  # ticks per 4/4 measure

    for ti, notes in tracks:
        if not notes:
            continue
        print(f"\n### MIDI track {ti}: {len(notes)} notes")
        bym = Counter((t // tpm + 1, p) for t, p in notes)
        print("  measures:", sorted({m for m, _ in bym}))

    for staff in (1, 2):
        expected = Counter((m, p) for m, s, p in kn if s == staff)
        # choose matching track by note count
        cand = [(ti, Counter((t // tpm + 1, p) for t, p in notes)) for ti, notes in tracks if notes]
        best = min(cand, key=lambda x: sum(((x[1] - expected)).values()) + sum(((expected - x[1])).values()))
        got = best[1]
        print(f"\n===== staff {staff}: expected {sum(expected.values())}, track {best[0]} has {sum(got.values())}")
        diff = (expected - got) + (got - expected)
        if not diff:
            print("  PERFECT per-measure match")
        else:
            for k in sorted(diff):
                side = "MISSING in midi" if (expected - got)[k] else "EXTRA in midi"
                print(f"   measure {k[0]:>3} pitch {k[1]:>3}  x{abs(diff[k])}  {side}")


if __name__ == "__main__":
    main()
