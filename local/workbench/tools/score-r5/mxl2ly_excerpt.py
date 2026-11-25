#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MusicXML -> clean LilyPond excerpt writer (score-a, round 5).

Reads a (uncompressed) MusicXML file, selects parts and a measure range,
and emits clean absolute-pitch LilyPond note bodies which are then wrapped
by the caller into the score skeleton.

Only the subset needed by the wiki excerpts is supported:
  - per-measure attributes: key, time, clef, transpose
  - notes / rests / chords, dots, ties, slurs
  - multiple voices per staff (backup / forward)
  - tuplets via <time-modification>
  - grace notes (approximated as \grace with their notated value)
Usage:
  python mxl2ly_excerpt.py list  <file.musicxml>
  python mxl2ly_excerpt.py dump  <file.musicxml> <part-id> <first-measure> <last-measure>
"""
import sys
import xml.etree.ElementTree as ET

# ---------- pitch ----------
STEPS = {'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'A': 'a', 'B': 'b'}
SHARP = {1: 's', 2: 'ss', 3: 'sss'}
FLAT = {-1: 'f', -2: 'ff', -3: 'fff'}


def pitch_name(step, alter, octave):
    base = STEPS[step]
    if alter > 0:
        base += SHARP.get(alter, 's' * alter)
    elif alter < 0:
        base += FLAT.get(alter, 'f' * (-alter))
    if octave >= 3:
        base += "'" * (octave - 3)
    else:
        base += ',' * (3 - octave)
    return base


DUR_NAMES = {1: '1', 2: '2', 4: '4', 8: '8', 16: '16', 32: '32', 64: '64'}


def text(el, path, default=None):
    if el is None:
        return default
    found = el.find(path)
    if found is None or found.text is None:
        return default
    return found.text.strip()


def num(el, path, default=None):
    v = text(el, path)
    if v is None:
        return default
    return int(float(v))


def list_parts(root):
    out = []
    for sp in root.findall('./part-list/score-part'):
        pid = sp.get('id')
        name = text(sp, 'part-name', '')
        tr = sp.find('midi-instrument')
        out.append((pid, name))
    return out


def measure_numbers(part):
    return [m.get('number') for m in part.findall('measure')]


def part_attributes(part, first_idx):
    """Collect key/time/clef/transpose in force at the start of the range."""
    attrs = {'key': None, 'time': None, 'clefs': {}, 'transpose': None}
    for m in part.findall('measure')[:first_idx]:
        for a in m.findall('attributes'):
            k = a.find('key')
            if k is not None:
                attrs['key'] = (num(k, 'fifths', 0), text(k, 'mode', 'major'))
            t = a.find('time')
            if t is not None:
                attrs['time'] = (num(t, 'beats'), num(t, 'beat-type'))
            tr = a.find('transpose')
            if tr is not None:
                attrs['transpose'] = (num(tr, 'chromatic', 0), num(tr, 'octave-change', 0))
            for c in a.findall('clef'):
                attrs['clefs'][c.get('number', '1')] = clef_of(c)
    return attrs


def clef_of(c):
    sign = text(c, 'sign', 'G')
    line = num(c, 'line', 2)
    octc = num(c, 'clef-octave-change', 0) or 0
    if sign == 'G':
        name = 'treble'
    elif sign == 'F':
        name = 'bass'
    elif sign == 'C':
        name = {1: 'soprano', 2: 'mezzo-soprano', 3: 'alto', 4: 'tenor', 5: 'baritone'}.get(line, 'alto')
    else:
        name = 'treble'
    if octc == 1:
        name += '^8'
    elif octc == -1:
        name += '_8'
    return name


def key_of(fifths, mode):
    # major / minor keys spelled the conventional way
    major = {0: 'c', 1: 'g', 2: 'd', 3: 'a', 4: 'e', 5: 'b', 6: 'fs', 7: 'cs',
             -1: 'f', -2: 'bf', -3: 'ef', -4: 'af', -5: 'df', -6: 'gf', -7: 'cf'}
    minor = {0: 'a', 1: 'e', 2: 'b', 3: 'fs', 4: 'cs', 5: 'gs', 6: 'ds', 7: 'as',
             -1: 'd', -2: 'g', -3: 'c', -4: 'f', -5: 'bf', -6: 'ef', -7: 'af'}
    table = minor if mode == 'minor' else major
    return table.get(fifths, 'c'), ('minor' if mode == 'minor' else 'major')


class Ev:
    __slots__ = ('onset', 'dur', 'kind', 'name', 'dots', 'base_type', 'voice',
                 'tie_stop', 'tie_start', 'slur_start', 'slur_stop', 'tm',
                 'oct_shift', 'artic', 'dyn')

    def __init__(self):
        self.onset = 0
        self.dur = 0
        self.kind = 'note'      # note | rest | chord
        self.name = 'c'
        self.dots = 0
        self.base_type = 4
        self.voice = '1'
        self.tie_stop = False
        self.tie_start = False
        self.slur_start = False
        self.slur_stop = False
        self.tm = None          # (actual, normal)
        self.oct_shift = 0
        self.artic = []
        self.dyn = []


def parse_measures(part, lo, hi):
    """Return {measure_number: {'idx':i,'attrs':...,'events':[...], 'max_dur':div}}"""
    divisions = 1
    measures = part.findall('measure')
    result = []
    for idx, m in enumerate(measures):
        number = m.get('number')
        attrs_here = {'key': None, 'time': None, 'clefs': {}, 'transpose': None}
        for a in m.findall('attributes'):
            d = num(a, 'divisions')
            if d:
                divisions = d
            k = a.find('key')
            if k is not None:
                attrs_here['key'] = (num(k, 'fifths', 0), text(k, 'mode', 'major'))
            t = a.find('time')
            if t is not None:
                attrs_here['time'] = (num(t, 'beats'), num(t, 'beat-type'))
            tr = a.find('transpose')
            if tr is not None:
                attrs_here['transpose'] = (num(tr, 'chromatic', 0), num(tr, 'octave-change', 0))
            for c in a.findall('clef'):
                attrs_here['clefs'][c.get('number', '1')] = clef_of(c)

        evs = []
        pos = 0
        maxpos = 0
        last = None
        for el in m:
            tag = el.tag
            if tag == 'note':
                dur_el = el.find('duration')
                dur = int(float(dur_el.text)) if dur_el is not None else 0
                e = Ev()
                e.dur = dur
                e.onset = pos if el.find('chord') is None else (last.onset if last else pos)
                e.voice = text(el, 'voice', '1')
                e.base_type = num(el, 'type', 0) or 0
                e.dots = len(el.findall('dot'))
                if el.find('rest') is not None:
                    e.kind = 'rest'
                else:
                    p = el.find('pitch')
                    step = text(p, 'step', 'C')
                    alter = num(p, 'alter', 0) or 0
                    octv = num(p, 'octave', 4)
                    e.kind = 'note'
                    e.name = pitch_name(step, alter, octv)
                tm = el.find('time-modification')
                if tm is not None:
                    e.tm = (num(tm, 'actual-notes', 0), num(tm, 'normal-notes', 0))
                for tie in el.findall('tie'):
                    if tie.get('type') == 'stop':
                        e.tie_stop = True
                    elif tie.get('type') == 'start':
                        e.tie_start = True
                nots = el.find('notations')
                if nots is not None:
                    for t2 in nots.findall('tied'):
                        if t2.get('type') == 'stop':
                            e.tie_stop = True
                        elif t2.get('type') == 'start':
                            e.tie_start = True
                    for s in nots.findall('slur'):
                        if s.get('type') == 'start':
                            e.slur_start = True
                        elif s.get('type') == 'stop':
                            e.slur_stop = True
                    for art in nots.findall('articulations/*'):
                        if art.tag in ('staccato', 'accent', 'tenuto', 'marcato'):
                            e.artic.append('\\' + art.tag)
                    if nots.find('trill-mark') is not None:
                        e.artic.append('\\trill')
                if el.find('grace') is not None:
                    e.dur = 0
                dirs = el.findall('notations/ornaments/turn')
                if el.find('chord') is None:
                    maxpos = max(maxpos, pos + dur)
                    pos += dur
                evs.append(e)
                last = e
            elif tag == 'backup':
                pos -= int(float(text(el, 'duration', '0')))
            elif tag == 'forward':
                pos += int(float(text(el, 'duration', '0')))
                maxpos = max(maxpos, pos)

        result.append({
            'idx': idx,
            'number': number,
            'attrs': attrs_here,
            'events': evs,
            'maxpos': maxpos,
            'divisions': divisions,
        })
    return result


def dur_str(base_type, dots, kind):
    if base_type and base_type in DUR_NAMES:
        s = ('.' if kind == 'rest' and base_type == 1 else '') + DUR_NAMES[base_type]
        s += '.' * dots
        return s
    return None


def emit_voice(measures, voice_ids, divisions_hint):
    """Render one voice as text, one line per measure, ties/slurs attached."""
    lines = []
    for m in measures:
        toks = []
        own = [e for e in m['events'] if e.voice in voice_ids]
        if not own:
            lines.append('%')
            continue
        i = 0
        while i < len(own):
            e = own[i]
            # gather tuplet run
            if e.tm:
                run = []
                ratio = e.tm
                j = i
                while j < len(own) and own[j].tm == ratio:
                    run.append(own[j])
                    j += 1
                toks.append('\\tuplet %d/%d { %s }' % (ratio[0], ratio[1],
                                                       ' '.join(render_note(x) for x in run)))
                i = j
                continue
            toks.append(render_note(e))
            i += 1
        # pad to full measure if short
        lines.append(' '.join(toks))
    return lines


def render_note(e):
    body = 'r' if e.kind == 'rest' else e.name
    d = dur_str(e.base_type, e.dots, e.kind)
    s = body + (d or '')
    if e.kind == 'rest' and d is None:
        s = 'r'
    if e.tie_stop:
        # previous note keeps the tie; nothing to print but rearticulation is avoided
        pass
    if e.tie_start and not e.tie_stop:
        s += '~'
    if e.slur_start:
        s += '('
    if e.slur_stop:
        s += ')'
    for a in e.artic:
        s += '-' + a
    return s


def main():
    cmd = sys.argv[1]
    path = sys.argv[2]
    tree = ET.parse(path)
    root = tree.getroot()
    if cmd == 'list':
        for pid, name in list_parts(root):
            part = root.find("./part[@id='%s']" % pid)
            nums = measure_numbers(part) if part is not None else []
            print(pid, '|', name, '| measures:', len(nums), '| first:', nums[:3], '| last:', nums[-2:])
        return
    if cmd == 'dump':
        pid = sys.argv[3]
        lo = int(sys.argv[4])
        hi = int(sys.argv[5])
        part = root.find("./part[@id='%s']" % pid)
        ms = parse_measures(part, lo, hi)
        sel = [m for m in ms if m['number'] is not None and m['number'].isdigit() and lo <= int(m['number']) <= hi]
        print('# measures', [m['number'] for m in sel])
        print('# attrs at start:', sel[0]['attrs'])
        for m in sel:
            print('=== m%s div=%s maxpos=%s' % (m['number'], m['divisions'], m['maxpos']))
            for e in m['events']:
                print('   v%s on=%-5s dur=%-4s %-6s %-6s dots=%s tm=%s tie=%s/%s slur=%s/%s' % (
                    e.voice, e.onset, e.dur, e.kind, e.name, e.dots, e.tm,
                    e.tie_stop, e.tie_start, e.slur_stop, e.slur_start))
        return


if __name__ == '__main__':
    main()
