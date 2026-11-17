#!/usr/bin/env python3
"""Verifier: independent 3-way canonical comparison of the three MusicXML sources
+ global metadata/barline/tempo inventory."""
import sys, re
from lxml import etree

def canon(path):
    root = etree.parse(path).getroot()
    info = dict(
        title=root.findtext('movement-title'),
        software=root.findtext('.//software'),
        date=root.findtext('.//encoding-date'),
        nparts=len(root.findall('part')),
        partnames=[p.findtext('part-name') for p in root.findall('part-list/score-part')],
        midiprogs=[p.findtext('.//midi-instrument/midi-program') for p in root.findall('part-list/score-part')],
    )
    parts = []
    for part in root.findall('part'):
        measures = []
        for meas in part.findall('measure'):
            evs = []
            for el in meas:
                tag = el.tag
                if tag == 'note':
                    p = el.find('pitch')
                    evs.append(('note',
                        p.findtext('step') if p is not None else 'R',
                        p.findtext('alter') if p is not None else '',
                        p.findtext('octave') if p is not None else '',
                        el.findtext('duration'), el.findtext('type'),
                        len(el.findall('dot')), el.find('chord') is not None,
                        el.find('rest') is not None, el.find('grace') is not None,
                        tuple(sorted(t.get('type') for t in el.findall('tie'))),
                        tuple(sorted(a.tag for a in el.findall('notations/articulations/*'))),
                        tuple(sorted((s.get('type'), s.get('number')) for s in el.findall('notations/slur'))),
                        el.findtext('accidental'),
                        el.findtext('time-modification/actual-notes'),
                        el.findtext('time-modification/normal-notes')))
                elif tag in ('backup','forward'):
                    evs.append((tag, el.findtext('duration')))
                elif tag == 'attributes':
                    k = el.find('key'); t = el.find('time')
                    evs.append(('attr',
                        el.findtext('divisions'),
                        k.findtext('fifths') if k is not None else None,
                        k.findtext('mode') if k is not None else None,
                        t.findtext('beats') if t is not None else None,
                        t.findtext('beat-type') if t is not None else None,
                        tuple(el.findtext('sign') for el in el.findall('clef')),
                        tuple(el.findtext('line') for el in el.findall('clef'))))
                elif tag == 'barline':
                    evs.append(('barline', el.get('location'), el.findtext('bar-style'),
                                el.find('repeat').get('direction') if el.find('repeat') is not None else None))
                elif tag == 'direction':
                    met = el.find('.//metronome')
                    snd = el.find('.//sound')
                    evs.append(('direction', el.get('staff'), el.get('placement'),
                                tuple((w.text or '') for w in el.iter('words')),
                                snd.get('tempo') if snd is not None else None,
                                (met.findtext('.//beat-unit'), met.findtext('.//per-minute'), met.findtext('.//beat-unit-dot')) if met is not None else None,
                                (el.find('.//direction-type/dynamics') is not None)))
                elif tag == 'sound':
                    evs.append(('sound', el.get('tempo')))
            measures.append(evs)
        parts.append(measures)

    # tempo/marking inventory across the whole file
    tempos = []
    words = []
    for part in root.findall('part'):
        for meas in part.findall('measure'):
            for el in meas.iter('sound'):
                if el.get('tempo'): tempos.append((meas.get('number'), el.get('tempo')))
            for el in meas.iter('metronome'):
                tempos.append((meas.get('number'), 'metronome', etree.tostring(el)))
            for el in meas.iter('words'):
                if (el.text or '').strip(): words.append((meas.get('number'), el.text))
    info['sound_tempo'] = tempos
    info['words'] = words
    barlines = []
    keys = []
    for pi, part in enumerate(root.findall('part')):
        for meas in part.findall('measure'):
            for b in meas.findall('barline'):
                barlines.append((pi, meas.get('number'), b.get('location'), b.findtext('bar-style')))
            for k in meas.findall('attributes/key'):
                keys.append((pi, meas.get('number'), k.findtext('fifths')))
    info['barlines'] = barlines
    info['keys'] = keys
    return info, parts

def diff(a, b, la, lb):
    n = 0
    for pi in range(min(len(a), len(b))):
        ma, mb = a[pi], b[pi]
        for mi in range(min(len(ma), len(mb))):
            if ma[mi] != mb[mi]:
                n += 1
                if n <= 15:
                    print("  DIFF part%d m.%d" % (pi, mi+1))
                    sa, sb = set(ma[mi]), set(mb[mi])
                    for x in ma[mi]:
                        if x not in sb: print("    only-%s: %r" % (la, x))
                    for x in mb[mi]:
                        if x not in sa: print("    only-%s: %r" % (lb, x))
        if len(ma) != len(mb):
            print("  MEASURE COUNT part%d: %s=%d %s=%d" % (pi, la, len(ma), lb, len(mb)))
    return n

if __name__ == '__main__':
    files = sys.argv[1:]
    infos, parts = {}, {}
    for f in files:
        tag = f.split('x_')[-1].split('\\')[0] if 'x_' in f else f[-12:]
        i, p = canon(f)
        tag = {'a':'A(98865)','b':'B(99688)','c':'C(125808)'}.get(tag, tag)
        infos[tag] = i; parts[tag] = p
        print("\n### %s  %s" % (tag, f))
        for k in ('title','software','date','nparts','partnames','midiprogs'):
            print("   %-10s %r" % (k, i[k]))
        print("   sound/metronome entries: %d" % len(i['sound_tempo']))
        for x in i['sound_tempo'][:6]: print("      ", x)
        print("   non-empty <words>: %d" % len(i['words']))
        for x in i['words'][:6]: print("      ", x)
        bl = [x for x in i['barlines'] if x[3] and x[3] != 'regular']
        print("   non-regular barlines: %r" % (bl,))
        ks = sorted(set((x[2]) for x in i['keys']))
        print("   key fifths seen: %r" % (ks,))
        print("   key-change measures (part0): %r" % ([x[1] for x in i['keys'] if x[0]==0],))
    tags = list(parts)
    for j in range(1, len(tags)):
        print("\n--- canonical note diff %s vs %s" % (tags[0], tags[j]))
        print("   differing measures:", diff(parts[tags[0]], parts[tags[j]], tags[0], tags[j]))
