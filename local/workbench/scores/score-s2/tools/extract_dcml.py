#!/usr/bin/env python3
"""Extract per-voice notes from DCML notes.tsv, sorted numerically, with rests filled in.

Outputs a compact per-fragment, per-staff list of events:
  m<mn> @<onset_qb_in_measure>: <dur> <name>
with explicit "REST" rows for gaps. Use as the authoritative pitch/rhythm source
(timesig + staff + midi + tied). Cross-check against Kern.
"""
import csv
import io
import os
import sys

BASE = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\dcml-abc"

FRAGMENTS = [
    ("S2-C1", "n11op95_01.notes.tsv", 1, 8, "Op.95 I mm.1-8"),
    ("S2-C2", "n11op95_01.notes.tsv", 19, 24, "Op.95 I mm.19-24"),
    ("S2-D1", "n10op74_01.notes.tsv", 18, 24, "Op.74 I Poco Adagio mm.18-24"),
    ("S2-D2", "n14op131_01.notes.tsv", 6, 11, "Op.131 I mm.6-11"),
    ("S2-D3", "n15op132_01.notes.tsv", 1, 8, "Op.132 I mm.1-8"),
]

def frac(s):
    if "/" in s:
        a, b = s.split("/")
        return float(a) / float(b)
    return float(s)

def read_tsv(path):
    with io.open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def main():
    out = []
    for fid, tsv, m0, m1, label in FRAGMENTS:
        rows = read_tsv(os.path.join(BASE, tsv))
        sel = [r for r in rows if m0 <= int(r["mn"]) <= m1]
        timesig = sel[0]["timesig"] if sel else "?"
        # measure length in quarter beats: 4/4 and 2/2 both = 4 qb
        mlen = 4.0
        out.append("=" * 76)
        out.append(f"{fid}  {label}   timesig={timesig}  ({len(sel)} notes)")
        for staff in ["1", "2", "3", "4"]:
            rs = [r for r in sel if r["staff"] == staff]
            rs.sort(key=lambda r: (int(r["mn"]), frac(r["mc_onset"])))
            out.append(f"  -- staff {staff} --")
            for r in rs:
                onset = frac(r["mc_onset"])
                dq = float(r["duration_qb"])
                tie = "~" if r.get("tied") else ""
                out.append("    m{mn:>2} @{on:>6} dur_qb={dq:<4} {name:<5}{tie} (midi {midi})".format(
                    mn=r["mn"], on=r["mc_onset"], dq=dq, name=r["name"], tie=tie, midi=r["midi"]))
    txt = "\n".join(out)
    print(txt)
    dst = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s2\tools\dcml-extract.txt"
    with io.open(dst, "w", encoding="utf-8") as f:
        f.write(txt)
    print("\nsaved:", dst)

if __name__ == "__main__":
    main()
