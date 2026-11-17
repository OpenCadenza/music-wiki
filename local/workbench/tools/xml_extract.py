#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract notes of selected parts and measures from a MusicXML file.
Usage: python xml_extract.py <file.musicxml> <partIds comma> <m0> <m1> [--dyn] [--art]
"""
import sys, re
import xml.etree.ElementTree as ET

def txt(el, path, default=''):
    x = el.find(path)
    return x.text if x is not None and x.text is not None else default

def note_info(n, divs):
    # returns dict
    d = {}
    d['rest'] = n.find('rest') is not None
    p = n.find('pitch')
    if p is not None:
        d['step'] = txt(p, 'step')
        d['oct'] = int(txt(p, 'octave', '4'))
        alt = txt(p, 'alter')
        d['alter'] = float(alt) if alt else 0.0
    dur = int(txt(n, 'duration', '0'))
    d['dur'] = dur
    d['durq'] = round(dur / divs, 3) if divs else None
    d['type'] = txt(n, 'type')
    d['dots'] = len(n.findall('dot'))
    d['chord'] = n.find('chord') is not None
    d['voice'] = txt(n, 'voice')
    d['staff'] = txt(n, 'staff')
    d['tie_start'] = any(t.get('type') == 'start' for t in n.findall('tie'))
    d['tie_stop'] = any(t.get('type') == 'stop' for t in n.findall('tie'))
    arts = [a.tag for a in n.findall('notations/articulations/*')]
    d['arts'] = arts
    dyn = n.find('notations/dynamics')
    d['dyn'] = dyn.findtext('*') if dyn is not None else None
    return d

def main(path, pids, m0, m1):
    tree = ET.parse(path)
    root = tree.getroot()
    parts = {p.get('id'): p for p in root.findall('part')}
    names = {sp.get('id'): txt(sp, 'part-name') for sp in root.findall('part-list/score-part')}
    divs = 1
    for pid in pids:
        part = parts.get(pid)
        if part is None:
            print(f"! missing part {pid}"); continue
        print(f"\n##### PART {pid} = {names.get(pid)} #####")
        divs = 1
        for i, m in enumerate(part.findall('measure'), 1):
            for att in m.findall('attributes'):
                d = att.findtext('divisions')
                if d:
                    divs = int(d)
            if not (m0 <= i <= m1):
                continue
            print(f"-- m{i} (div={divs}) --")
            for n in m.findall('note'):
                inf = note_info(n, divs)
                if inf['rest']:
                    print(f"  r durq={inf['durq']} type={inf['type']} dots={inf['dots']} staff{inf['staff']} v{inf['voice']}")
                else:
                    name = f"{inf['step']}"
                    if inf['alter'] == 1: name += '#'
                    elif inf['alter'] == -1: name += 'b'
                    elif inf['alter'] == 2: name += '##'
                    elif inf['alter'] == -2: name += 'bb'
                    else: name += ''
                    print(f"  {name}{inf['oct']} durq={inf['durq']} type={inf['type']} dots={inf['dots']} staff{inf['staff']} v{inf['voice']}"
                          + (" CHORD" if inf['chord'] else "")
                          + (" TIE>" if inf['tie_start'] else "")
                          + (" <TIE" if inf['tie_stop'] else "")
                          + (f" arts={inf['arts']}" if inf['arts'] else "")
                          + (f" dyn={inf['dyn']}" if inf['dyn'] else ""))
            for d in m.findall('direction'):
                w = d.findtext('direction-type/words')
                dd = d.findtext('direction-type/dynamics/*')
                if w: print(f"  [dir] {w}")
                if d.find('direction-type/dynamics') is not None:
                    print(f"  [dyn] {dd}")

if __name__ == '__main__':
    path = sys.argv[1]
    pids = sys.argv[2].split(',')
    m0 = int(sys.argv[3]); m1 = int(sys.argv[4])
    main(path, pids, m0, m1)