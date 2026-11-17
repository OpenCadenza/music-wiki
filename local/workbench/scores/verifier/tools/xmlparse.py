"""Parse a MusicXML file into measure-indexed absolute-time note events.

Beethoven DCML exports carry two <part> elements (P1 = RH, P2 = LH) in which the
<staff> child is absent; Mozart K309 has a single part with real <staff> values.
`parse()` therefore returns {part_id_or_index: [measure, ...]} and each measure
holds its own event list.

event: dict(measure_index, mnum, onset(quarters, within measure), pitch(midi),
            dur(quarters), staff, voice, grace, rest, tie_start, tie_stop)
"""
import xml.etree.ElementTree as ET

STEP = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def _txt(e, tag, default=None):
    x = e.find(tag)
    return x.text if x is not None else default


def parse_parts(path):
    root = ET.parse(path).getroot()
    result = {}
    for pi, part in enumerate(root.findall('part')):
        key = part.get('id') or 'P%d' % (pi + 1)
        measures = []
        divisions = 1
        for meas in part.findall('measure'):
            events = []
            cursor = 0
            maxpos = 0
            last = {}
            for el in meas:
                if el.tag == 'attributes':
                    for d in el.findall('divisions'):
                        divisions = int(d.text)
                elif el.tag == 'note':
                    grace = el.find('grace') is not None
                    voice = _txt(el, 'voice', '1')
                    staff = _txt(el, 'staff', str(pi + 1))
                    dur = int(_txt(el, 'duration', '0') or 0)
                    is_chord = el.find('chord') is not None
                    onset = last.get(voice, (cursor, 0))[0] if is_chord else cursor
                    p = el.find('pitch')
                    pitch = None
                    if p is not None:
                        step = p.find('step').text
                        octv = int(p.find('octave').text)
                        alter = float(_txt(p, 'alter', '0') or 0)
                        pitch = (octv + 1) * 12 + STEP[step] + int(round(alter))
                    tie_start = tie_stop = False
                    for t in el.findall('tie') + el.findall('./notations/tied'):
                        if t.get('type') == 'start':
                            tie_start = True
                        elif t.get('type') == 'stop':
                            tie_stop = True
                    if not grace and not is_chord:
                        cursor += dur
                        maxpos = max(maxpos, cursor)
                    last[voice] = (onset, dur)
                    events.append(dict(mnum=meas.get('number'),
                                       implicit=meas.get('implicit') == 'yes',
                                       onset=onset / divisions, pitch=pitch,
                                       dur=dur / divisions, staff=int(staff),
                                       voice=voice, grace=grace,
                                       rest=p is None, tie_start=tie_start,
                                       tie_stop=tie_stop))
                elif el.tag == 'backup':
                    cursor -= int(el.find('duration').text)
                elif el.tag == 'forward':
                    cursor += int(el.find('duration').text)
            measures.append(dict(mnum=meas.get('number'),
                                 implicit=meas.get('implicit') == 'yes',
                                 length=maxpos / divisions, events=events))
        result[key] = measures
    return result


def window(measures, start_mnum, count):
    """Select `count` printed measures from start_mnum.

    DCML splits some printed measures into two <measure> elements (the second is
    numbered 'X1', 'X2', ...).  Those continuation elements are attached to the
    preceding printed measure and do not advance the count.
    """
    idx = next(i for i, m in enumerate(measures) if m['mnum'] == start_mnum)
    sel = []
    seen = 0
    for m in measures[idx:]:
        sel.append(m)
        if not str(m['mnum']).startswith('X'):
            seen += 1
        if seen >= count:
            break
    return sel


def flatten(part_measures):
    """Absolute onsets from the start of the given measure list."""
    out = []
    t = 0.0
    for m in part_measures:
        for e in m['events']:
            e2 = dict(e)
            e2['meas_idx'] = len(out)
            e2['abs'] = t + e['onset']
            out.append(e2)
        t += m['length']
    return out, t


if __name__ == '__main__':
    import sys
    parts = parse_parts(sys.argv[1])
    for k, ms in parts.items():
        print(k, 'measures', len(ms), 'nums', ms[0]['mnum'], '..', ms[-1]['mnum'])
        for m in ms[:6]:
            print('  ', m['mnum'], 'impl' if m['implicit'] else '    ',
                  round(m['length'], 3), len(m['events']),
                  [e['pitch'] for e in m['events'] if e['pitch']][:14])
