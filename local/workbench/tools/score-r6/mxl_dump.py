#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mxl_dump (score-r6)：把 MusicXML / MXL 读成「每小节音高多重集」，用于与 ABC/kern 底本回比对。

用法：
  python mxl_dump.py <file.xml|file.mxl> [--measures 1-10] [--parts 1,2] [--json out.json]
输出：{"measures": {"1": [60, 64, 67]}, ...}（按 part 分别）。
"""
import argparse
import io
import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

STEP = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def read_xml(path):
    if path.lower().endswith(".mxl") or path.lower().endswith(".zip"):
        z = zipfile.ZipFile(path)
        names = [n for n in z.namelist() if n.lower().endswith((".xml", ".musicxml"))]
        # 优先 container 指向的 rootfile
        root = None
        if "META-INF/container.xml" in z.namelist():
            c = z.read("META-INF/container.xml").decode("utf-8", "replace")
            m = re.search(r'full-path="([^"]+)"', c)
            if m and m.group(1) in z.namelist():
                root = m.group(1)
        if root is None:
            root = names[0]
        return z.read(root)
    with open(path, "rb") as fh:
        return fh.read()


def dump(path, first, last):
    data = read_xml(path)
    root = ET.fromstring(data)
    out = {}
    for part in root.iter("part"):
        pid = part.get("id")
        measures = []
        for meas in part.iter("measure"):
            num = meas.get("number")
            pitches = []
            for note in meas.iter("note"):
                if note.find("rest") is not None or note.find("grace") is not None:
                    continue
                p = note.find("pitch")
                if p is None:
                    continue
                step = p.findtext("step")
                octv = int(p.findtext("octave"))
                alter = int(float(p.findtext("alter") or 0))
                pitches.append((octv + 1) * 12 + STEP[step] + alter)
            measures.append((num, sorted(pitches)))
        out[pid] = measures
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--measures")
    ap.add_argument("--json")
    args = ap.parse_args()
    first, last = 1, 10 ** 6
    if args.measures:
        a, b = args.measures.split("-")
        first, last = int(a), int(b)
    data = dump(args.path, first, last)
    res = {}
    for pid, measures in data.items():
        res[pid] = {num: p for num, p in measures if num and num.isdigit() and first <= int(num) <= last}
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(res, fh, ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False))
    # 统计
    for pid, mm in data.items():
        print("%s: %d measures, first=%s last=%s" % (pid, len(mm), mm[0][0] if mm else "-",
                                                     mm[-1][0] if mm else "-"))


if __name__ == "__main__":
    main()
