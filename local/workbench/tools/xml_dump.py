#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump MusicXML structure: measures, time/key/tempo changes, and optionally notes of one part."""
import sys
import xml.etree.ElementTree as ET

def text(el, path):
    x = el.find(path)
    return x.text if x is not None and x.text is not None else ''

def main(path, part_id=None, m_from=None, m_to=None):
    tree = ET.parse(path)
    root = tree.getroot()
    parts = {p.get('id'): p for p in root.findall('part')}
    names = {sp.get('id'): text(sp, 'part-name') for sp in root.findall('part-list/score-part')}
    print("PARTS:", ", ".join(f"{k}={names.get(k)}" for k in parts))
    for pid, part in parts.items():
        if part_id and pid != part_id:
            continue
        print(f"\n=== {pid} {names.get(pid)} : {len(part.findall('measure'))} measures ===")
        for i, m in enumerate(part.findall('measure'), 1):
            a = []
            for att in m.findall('attributes'):
                d = att.findtext('divisions')
                if d: a.append(f"div={d}")
                k = att.findtext('key/fifths')
                if k is not None: a.append(f"key={k}")
                t = att.findtext('time')
                if att.find('time') is not None:
                    bt = att.find('time').findall('beat')
                    btm = att.find('time').findall('beat-type')
                    if bt:
                        a.append("time=" + "/".join(f"{b.text}.{btm[j].text}" for j, b in enumerate(bt)))
            dirs = []
            for d in m.findall('direction'):
                w = d.findtext('direction-type/words')
                if w: dirs.append(w)
                for snd in d.findall('sound'):
                    t = snd.get('tempo')
                    if t: dirs.append(f"tempo={t}")
            if a or dirs:
                print(f"m{i}: {' '.join(a)} {' | '.join(dirs)}")
            if m_from is not None and m_to is not None and m_from <= i <= m_to:
                for n in m.findall('note'):
                    if n.find('rest') is not None:
                        continue
                    st = n.findtext('staff') or ''
                    dur = n.findtext('duration')
                    typ = n.findtext('type')
                    step = n.findtext('pitch/step'); octv = n.findtext('pitch/octave')
                    acc = n.findtext('accidental') or ''
                    ch = n.findtext('chord') is not None
                    print(f"  m{i} staff{st} {step}{acc}{octv} {typ} dur{dur} {'chord' if ch else ''}")
if __name__ == '__main__':
    path = sys.argv[1]
    pid = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != '-' else None
    mf = int(sys.argv[3]) if len(sys.argv) > 3 else None
    mt = int(sys.argv[4]) if len(sys.argv) > 4 else None
    main(path, pid, mf, mt)