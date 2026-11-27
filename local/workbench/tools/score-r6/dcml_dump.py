#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""dcml_dump (score-r6)：把 DCML notes.tsv 读成「每小节的音高多重集」，按谱表(staff)分组。

DCML notes TSV 列：mc mn quarterbeats quarterbeats_all_endings duration_qb mc_onset mn_onset
timesig staff voice duration gracenote ... tpc midi name octave chord_id

用法：
  python dcml_dump.py <notes.tsv> --measures 1-10 [--staff 1,2] [--json out.json]
"""
import argparse
import json


def read_tsv(path):
    with open(path, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        rows = []
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < len(header):
                parts += [""] * (len(header) - len(parts))
            rows.append(dict(zip(header, parts)))
    return header, rows


def dump(path, first, last, staffs=None):
    header, rows = read_tsv(path)
    out = {}
    for r in rows:
        if r.get("mc") in ("", None):
            continue
        mn = int(float(r["mn"]))
        if mn < first or mn > last:
            continue
        st = r["staff"]
        if staffs and st not in staffs:
            continue
        midi = int(float(r["midi"]))
        out.setdefault(st, {}).setdefault(str(mn), []).append(midi)
    for st in out:
        for mn in out[st]:
            out[st][mn].sort()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--measures")
    ap.add_argument("--staff")
    ap.add_argument("--json")
    args = ap.parse_args()
    first, last = 1, 10 ** 6
    if args.measures:
        a, b = args.measures.split("-")
        first, last = int(a), int(b)
    staffs = args.staff.split(",") if args.staff else None
    res = dump(args.path, first, last, staffs)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(res, fh, ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
