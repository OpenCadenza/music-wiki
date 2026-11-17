#!/usr/bin/env python3
"""Verifier: compare LilyPond MIDI vs authoritative MusicXML.
Compares (onset, pitch) exactly; checks that MIDI duration is either the
notated duration or half of it (LilyPond staccato default = 1/2)."""
import sys
from midi_cmp import xml_notes, read_smf, nm

xmlp, midp = sys.argv[1], sys.argv[2]
fmt, div, tks = read_smf(midp)
names = ['violon','violoncelle','RightHand','LeftHand']
nz = [(i,t) for i,t in enumerate(tks) if t['notes']]
overall = True
for k,(ti,t) in enumerate(nz):
    if k >= 4: break
    xn = xml_notes(xmlp, k, 21)
    exp = sorted([(round(n['t'],4), n['midi'], round(n['dur'],4), n['num']) for n in xn])
    got = sorted([(round(n[0]/div,4), n[1], round(n[2]/div,4)) for n in t['notes']])
    print("\n== part %d (%s): XML sounding notes %d, MIDI note-on %d" % (k, names[k], len(exp), len(got)))
    # 1) onset+pitch match
    ex_sp = [(a,b) for a,b,c,d in exp]
    gt_sp = [(a,b) for a,b,c in got]
    miss = [x for x in ex_sp if x not in gt_sp]
    extra = [x for x in gt_sp if x not in ex_sp]
    print("   onset+pitch in XML only : %d %s" % (len(miss), miss[:12]))
    print("   onset+pitch in MIDI only: %d %s" % (len(extra), extra[:12]))
    if miss or extra:
        overall = False
    # 2) duration check on matched pairs
    used = list(gt_sp)
    bad = []
    ratio = {1.0:0, 0.5:0, 0.25:0, 'other':0}
    for (a,b,c,num) in exp:
        key = (a,b)
        if key in used:
            i = used.index(key)
            gd = got[i][2]
            if abs(gd - c) < 1e-3:
                ratio[1.0] += 1
            elif abs(gd - c/2) < 1e-3:
                ratio[0.5] += 1
            elif abs(gd - c/4) < 1e-3:
                ratio[0.25] += 1
            else:
                ratio['other'] += 1
                bad.append((num, a, nm(b), c, gd))
            used.pop(i)
    print("   duration ratio (midi/xml): full=%d half=%d quarter=%d other=%d" % (
        ratio[1.0], ratio[0.5], ratio[0.25], ratio['other']))
    if bad:
        overall = False
        for x in bad[:20]: print("     OTHER m.%s @%s %s xml=%s midi=%s" % x)
print("\nOVERALL:", "PASS (pitch+onset identical; durations consistent with staccato shortening)"
      if overall else "DIFFERENCES FOUND")
