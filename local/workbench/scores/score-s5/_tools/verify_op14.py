"""Cross-check: kern mm.1-16 pitch content vs LilyPond MIDI output.

Compares, per staff, the sorted multiset of note pitches obtained from the
Humdrum source against the note-on pitches in the generated MIDI file.
"""
import re
import struct
import sys

NAMES = ["c", "cs", "d", "ds", "e", "f", "fs", "g", "gs", "a", "as", "b"]
KERNPITCH = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}


def kern_pitches(path, m0, m1):
    """-> {staff: [midi,...]} in document order, ties collapsed"""
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    spines = None
    measure = 0
    out = {}
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("**"):
            spines = [{"kern": t.strip() == "**kern", "staff": 1} for t in line.split("\t")]
            continue
        if spines is None or line.startswith("!!"):
            continue
        if line.startswith("*"):
            toks = line.split("\t")
            new, i = [], 0
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
                m = re.match(r"^[\[\(\{<>]*\d+\.*([A-Ga-g]+)([#\-n]*)(.*)$", p)
                if not m:
                    continue
                letters, acc, rest = m.groups()
                if "]" in rest:
                    continue  # tie continuation: already sounding
                n = len(letters)
                base = letters[0]
                pc = KERNPITCH[base.lower()]
                for a in acc:
                    if a == "-":
                        pc -= 1
                    elif a == "#":
                        pc += 1
                octv = (4 + (n - 1)) if base.islower() else (3 - (n - 1))
                midi = (octv + 1) * 12 + pc
                # skip tie continuations (tie stop on a note already sounding)
                out.setdefault(sp["staff"], []).append(midi)
    return out


def rd_vlq(buf, pos):
    v = 0
    while True:
        b = buf[pos]
        pos += 1
        v = (v << 7) | (b & 0x7F)
        if not (b & 0x80):
            return v, pos


def midi_tracks(path):
    data = open(path, "rb").read()
    assert data[:4] == b"MThd"
    fmt, ntrks, div = struct.unpack(">HHH", data[8:14])
    pos = 14
    tracks = []
    for _ in range(ntrks):
        assert data[pos:pos + 4] == b"MTrk"
        ln = struct.unpack(">I", data[pos + 4:pos + 8])[0]
        body = data[pos + 8:pos + 8 + ln]
        pos += 8 + ln
        p = 0
        t = 0
        status = None
        notes = []
        while p < len(body):
            dt, p = rd_vlq(body, p)
            t += dt
            b = body[p]
            if b & 0x80:
                status = b
                p += 1
            ev = status & 0xF0
            if ev == 0x90:
                pitch = body[p]
                vel = body[p + 1]
                p += 2
                if vel > 0:
                    notes.append(pitch)
            elif ev in (0x80, 0xA0, 0xB0, 0xE0):
                p += 2
            elif ev in (0xC0, 0xD0):
                p += 1
            elif status == 0xFF:
                meta = body[p]
                p += 1
                ln2, p = rd_vlq(body, p)
                p += ln2
            elif status in (0xF0, 0xF7):
                ln2, p = rd_vlq(body, p)
                p += ln2
            else:
                p += 1
        tracks.append(notes)
    return tracks


def main():
    krn, mid = sys.argv[1], sys.argv[2]
    km = kern_pitches(krn, 1, 16)
    mt = midi_tracks(mid)
    print("kern staves:", {k: len(v) for k, v in km.items()})
    print("midi tracks:", [len(t) for t in mt])

    # merge kern staves into two staves: 1 (RH) and 2 (LH)
    for staff in sorted(km):
        expected = sorted(km[staff])
        # pick the midi track whose length is closest
        best = min(mt, key=lambda t: abs(len(t) - len(expected)))
        got = sorted(best)
        print(f"\n=== staff {staff}: expected {len(expected)} notes, midi track {len(got)}")
        if expected == got:
            print("  EXACT MATCH (pitch multiset)")
        else:
            from collections import Counter
            ce, cg = Counter(expected), Counter(got)
            diff = (ce - cg) + (cg - ce)
            print("  DIFF:", dict(diff))
            print("  expected:", expected)
            print("  got     :", got)


if __name__ == "__main__":
    main()

