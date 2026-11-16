#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify a LilyPond fragment's MIDI pitches against DCML notes.tsv, voice by voice.

For each fragment:
  - read DCML notes rows in [mn0, mn1], group by staff (1..4 -> ch1..ch4 in MIDI)
  - build absolute onset in quarter beats relative to the fragment start
  - drop tie-continuation notes (same pitch, contiguous with previous note)
  - parse the .mid note-on stream per channel (tick -> quarter beats, divisions-based)
  - compare pitch sequences and onset sequences; report mismatches
"""
import csv
import io
import os
import struct
import sys

BASE = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\dcml-abc"
SCORES = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s2"

FRAGMENTS = [
    ("S2-C1", "n11op95_01.notes.tsv", 1, 8, "S2-C1-beethoven-op95-m1-8.mid"),
    ("S2-C2", "n11op95_01.notes.tsv", 19, 24, "S2-C2-beethoven-op95-m19-24.mid"),
    ("S2-D1", "n10op74_01.notes.tsv", 18, 24, "S2-D1-beethoven-op74-m18-24.mid"),
    ("S2-D2", "n14op131_01.notes.tsv", 6, 11, "S2-D2-beethoven-op131-m6-11.mid"),
    ("S2-D3", "n15op132_01.notes.tsv", 1, 8, "S2-D3-beethoven-op132-m1-8.mid"),
]

def frac(s):
    if "/" in s:
        a, b = s.split("/")
        return float(a) / float(b)
    return float(s)

def read_tsv(path):
    with io.open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def parse_midi(path):
    data = open(path, "rb").read()
    assert data[:4] == b"MThd"
    ntrks = struct.unpack(">H", data[10:12])[0]
    div = struct.unpack(">H", data[12:14])[0]
    idx = 14
    tracks = []
    for _ in range(ntrks):
        assert data[idx:idx + 4] == b"MTrk"
        ln = struct.unpack(">I", data[idx + 4:idx + 8])[0]
        tracks.append(data[idx + 8: idx + 8 + ln])
        idx += 8 + ln

    def vlq(buf, i):
        v = 0
        while True:
            b = buf[i]; i += 1
            v = (v << 7) | (b & 0x7F)
            if not (b & 0x80):
                return v, i

    notes = []  # (tick, channel, pitch)
    for data in tracks:
        i = 0; tick = 0; run = None
        while i < len(data):
            delta, i = vlq(data, i)
            tick += delta
            if i >= len(data):
                break
            st = data[i]
            if st == 0xFF:
                i += 1; i += 1
                ln, i = vlq(data, i); i += ln; run = None; continue
            if st in (0xF0, 0xF7):
                i += 1
                ln, i = vlq(data, i); i += ln; run = None; continue
            if st & 0x80:
                i += 1; run = st
            else:
                st = run
            kind = st & 0xF0; ch = st & 0x0F
            if kind in (0x80, 0x90):
                pitch = data[i]; vel = data[i + 1]; i += 2
                if kind == 0x90 and vel > 0:
                    notes.append((tick, ch, pitch))
            elif kind in (0xA0, 0xB0, 0xE0):
                i += 2
            elif kind in (0xC0, 0xD0):
                i += 1
            else:
                break
    ppq = div & 0x7FFF
    return notes, ppq

def main():
    ok_all = True
    for fid, tsv, mn0, mn1, midname in FRAGMENTS:
        rows = read_tsv(os.path.join(BASE, tsv))
        sel = [r for r in rows if mn0 <= int(r["mn"]) <= mn1]
        # staff -> list of (abs_qb, pitch, dur_qb, tied)
        by_staff = {}
        for r in sel:
            qb = (int(r["mn"]) - mn0) * 4.0 + frac(r["mc_onset"]) * 4.0
            dur = float(r["duration_qb"])
            by_staff.setdefault(r["staff"], []).append([qb, int(r["midi"]), dur, r.get("tied") or ""])
        # drop tie continuations
        cleaned = {}
        for st, evs in by_staff.items():
            evs.sort(key=lambda e: e[0])
            out = []
            for e in evs:
                if out:
                    prev = out[-1]
                    # continuation: same pitch, starts where previous ends, and previous was tied
                    if e[1] == prev[1] and abs(e[0] - (prev[0] + prev[2])) < 1e-6 and prev[3]:
                        prev[3] = e[3]  # extend
                        prev[2] += e[2]
                        continue
                out.append(e)
            cleaned[st] = out

        notes, ppq = parse_midi(os.path.join(SCORES, midname))
        by_ch = {}
        for tick, ch, pitch in notes:
            by_ch.setdefault(ch, []).append((tick / ppq, pitch))  # quarter beats
        for ch in by_ch:
            by_ch[ch].sort()

        print("=" * 70)
        print(f"{fid}  ({midname})")
        frag_ok = True
        for st in ["1", "2", "3", "4"]:
            ch = int(st) - 1
            d = cleaned.get(st, [])
            m = by_ch.get(ch, [])
            dp = [e[1] for e in d]
            mp = [p for _, p in m]
            if dp != mp:
                frag_ok = False
                ok_all = False
                print(f"  staff {st} (ch{ch+1}): MISMATCH  dcml={len(dp)} midi={len(mp)}")
                for i in range(max(len(dp), len(mp))):
                    a = dp[i] if i < len(dp) else None
                    b = mp[i] if i < len(mp) else None
                    if a != b:
                        print(f"    #{i}: dcml={a} midi={b}")
                        if i > 40:
                            print("    ..."); break
            else:
                print(f"  staff {st} (ch{ch+1}): OK ({len(dp)} notes)")
        print(f"  -> {'PASS' if frag_ok else 'FAIL'}")
    print("\nALL:", "PASS" if ok_all else "FAIL")

if __name__ == "__main__":
    main()
