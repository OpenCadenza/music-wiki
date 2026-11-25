#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Emit a complete LilyPond score fence body from a MusicXML source (score-a, round 5).

Spec (JSON):
{
  "source": "../raw/haydn-op76no3.musicxml",
  "segment": 1,                 # 0-based movement index (measure-number resets)
  "index_from": 128, "index_to": 147,   # optional explicit positions (overrides from/to)
  "from": 21, "to": 32,         # printed measure numbers inside the segment
  "voices": "merge" | "keep",   # "merge" collapses editorial voice splits (default)
  "comment": ["..."],           # provenance comment lines
  "tempo": "\\tempo \"...\" 4 = 56",
  "show_bar_numbers": false,
  "parts": [{"id": "P1", "var": "violinOne", "clef": "treble", "gm": "violin"}]
}
"""
import json
import os
import sys
import xml.etree.ElementTree as ET

STEPS = {'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'A': 'a', 'B': 'b'}
SHARP = {1: 's', 2: 'ss', 3: 'sss'}
FLAT = {-1: 'f', -2: 'ff', -3: 'fff'}
DUR_NAMES = {1: '1', 2: '2', 4: '4', 8: '8', 16: '16', 32: '32', 64: '64'}
TYPE_MAP = {'maxima': 0, 'long': 0, 'breve': 0, 'whole': 1, 'half': 2, 'quarter': 4,
            'eighth': 8, '16th': 16, '32nd': 32, '64th': 64, '128th': 128}
MIDI_NAMES = ['c', 'cs', 'd', 'ef', 'e', 'f', 'fs', 'g', 'af', 'a', 'bf', 'b']
DYNS = ('pppp', 'ppp', 'pp', 'p', 'ffff', 'fff', 'ff', 'f', 'mf', 'mp', 'sfz', 'sf', 'fp', 'fz')
MAJOR = {0: 'c', 1: 'g', 2: 'd', 3: 'a', 4: 'e', 5: 'b', 6: 'fs', 7: 'cs',
         -1: 'f', -2: 'bf', -3: 'ef', -4: 'af', -5: 'df', -6: 'gf', -7: 'cf'}
MINOR = {0: 'a', 1: 'e', 2: 'b', 3: 'fs', 4: 'cs', 5: 'gs', 6: 'ds', 7: 'as',
         -1: 'd', -2: 'g', -3: 'c', -4: 'f', -5: 'bf', -6: 'ef', -7: 'af'}
WARNINGS = []


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
    try:
        return int(float(v))
    except ValueError:
        return default


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


def name_of_midi(midi):
    pc = midi % 12
    octave = (midi - pc) // 12 - 1
    base = MIDI_NAMES[pc]
    if octave >= 3:
        return base + "'" * (octave - 3)
    return base + ',' * (3 - octave)


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


def quarters_of(sig):
    if not sig:
        return None
    beats, beat_type = sig
    return beats * 4.0 / beat_type



LETTERS = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
NAT_PC = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}
NAME_ACC = {0: '', 1: 's', 2: 'ss', -1: 'f', -2: 'ff'}
ACC_VAL = {'': 0, 's': 1, 'ss': 2, 'f': -1, 'ff': -2}
FIFTHS = {}
for _f, _n in MAJOR.items():
    FIFTHS[(_n, 'major')] = _f
for _f, _n in MINOR.items():
    FIFTHS[(_n, 'minor')] = _f


def split_key(keytext):
    """'g minor' -> ('g', 'minor')"""
    head, _, mode = keytext.partition(' ')
    return head, (mode or 'major')


def written_key(keytext, chromatic, diatonic):
    """Key signature a transposing instrument actually reads.

    sounding = written + chromatic, and the letter moves by `diatonic` steps, so
    the written tonic sits (chromatic, diatonic) below the sounding tonic.
    """
    head, mode = split_key(keytext)
    letter = head[0]
    acc = head[1:]
    sounding_pc = (NAT_PC[letter] + ACC_VAL.get(acc, 0)) % 12
    target_pc = (sounding_pc - chromatic) % 12
    steps = (-diatonic) % 7
    idx = (LETTERS.index(letter) + steps) % 7
    wl = LETTERS[idx]
    want = (target_pc - NAT_PC[wl]) % 12
    if want > 6:
        want -= 12
    name = wl + NAME_ACC.get(want, '')
    return name, mode, FIFTHS.get((name, mode))

def key_cmd(fifths, mode):
    if mode == 'minor':
        return '\\key %s \\minor' % MINOR.get(fifths, 'a')
    return '\\key %s \\major' % MAJOR.get(fifths, 'c')


def note_type(el):
    v = text(el, 'type')
    if v is None:
        return 0
    if v in TYPE_MAP:
        return TYPE_MAP[v]
    try:
        return int(float(v))
    except ValueError:
        return 0


def dot_value(base, dots):
    v = 1.0 / base
    add = v / 2.0
    for _ in range(dots):
        v += add
        add /= 2.0
    return v


CANDIDATES = sorted([(DUR_NAMES[b] + '.' * d, dot_value(b, d))
                     for b in (1, 2, 4, 8, 16, 32, 64) for d in (0, 1, 2)],
                    key=lambda kv: -kv[1])


def frac_to_durs(frac):
    out = []
    guard = 0
    while frac > 1e-9 and guard < 24:
        guard += 1
        for name, val in CANDIDATES:
            if val <= frac + 1e-9:
                out.append(name)
                frac -= val
                break
        else:
            break
    return out


class Ev(object):
    __slots__ = ('onset', 'dur', 'kind', 'name', 'chord', 'dots', 'type', 'voice', 'staff',
                 'tie_stop', 'tie_start', 'slur_start', 'slur_stop', 'tm', 'artic',
                 'dyn', 'grace')

    def __init__(self):
        self.onset = 0
        self.dur = 0
        self.kind = 'note'
        self.name = 'c'
        self.chord = []
        self.dots = 0
        self.type = 0
        self.voice = '1'
        self.staff = '1'
        self.tie_stop = False
        self.tie_start = False
        self.slur_start = False
        self.slur_stop = False
        self.tm = None
        self.artic = []
        self.dyn = []
        self.grace = False


def parse_measure(m):
    info = {'key': None, 'time': None, 'clef': None, 'transpose': None,
            'transpose_diatonic': -1, 'divisions': None}
    for a in m.findall('attributes'):
        d = num(a, 'divisions')
        if d:
            info['divisions'] = d
        k = a.find('key')
        if k is not None:
            info['key'] = (num(k, 'fifths', 0), text(k, 'mode', 'major'))
        t = a.find('time')
        if t is not None:
            info['time'] = (num(t, 'beats'), num(t, 'beat-type'))
        tr = a.find('transpose')
        if tr is not None:
            info['transpose'] = (num(tr, 'chromatic', 0), num(tr, 'octave-change', 0))
            info['transpose_diatonic'] = num(tr, 'diatonic', -1)
        for c in a.findall('clef'):
            info['clef'] = clef_of(c)

    evs = []
    pos = 0
    maxpos = 0
    last_by_voice = {}
    for el in m:
        tag = el.tag
        if tag == 'note':
            dur_el = el.find('duration')
            dur = int(float(dur_el.text)) if dur_el is not None else 0
            e = Ev()
            e.dur = dur
            e.voice = text(el, 'voice', '1')
            e.staff = text(el, 'staff', '1')
            is_chord_note = el.find('chord') is not None
            e.onset = last_by_voice.get(e.voice, None).onset if (is_chord_note and last_by_voice.get(e.voice)) else pos
            e.type = note_type(el)
            e.dots = len(el.findall('dot'))
            if el.find('rest') is not None:
                e.kind = 'rest'
            else:
                p = el.find('pitch')
                e.kind = 'note'
                e.name = pitch_name(text(p, 'step', 'C'), num(p, 'alter', 0) or 0,
                                    num(p, 'octave', 4))
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
                e.grace = True
            if is_chord_note:
                prev = last_by_voice.get(e.voice)
                if prev is not None and e.kind == 'note':
                    prev.chord.append(e.name)
                    continue
            maxpos = max(maxpos, pos + dur)
            pos += dur
            evs.append(e)
            last_by_voice[e.voice] = e
        elif tag == 'backup':
            pos -= int(float(text(el, 'duration', '0')))
        elif tag == 'forward':
            pos += int(float(text(el, 'duration', '0')))
            maxpos = max(maxpos, pos)
        elif tag == 'direction':
            d = el.find('.//dynamics/*')
            if d is not None and d.tag in DYNS:
                for e in reversed(evs):
                    if e.onset <= pos:
                        if d.tag not in e.dyn:
                            e.dyn.append(d.tag)
                        break
    return info, evs, maxpos


def movement_segments(part):
    measures = part.findall('measure')
    nums = []
    for m in measures:
        try:
            nums.append(int(m.get('number')))
        except (TypeError, ValueError):
            nums.append(None)
    segs = []
    start = 0
    prev = None
    for i, v in enumerate(nums):
        if v is None:
            continue
        if prev is not None and v <= prev:
            segs.append((start, i - 1))
            start = i
        prev = v
    segs.append((start, len(measures) - 1))
    return measures, nums, segs


def dur_text(e, divisions):
    """LilyPond duration token for an event, falling back to <duration>/<divisions>."""
    d = DUR_NAMES.get(e.type, '')
    if d:
        return d + '.' * e.dots
    if e.dur and divisions:
        parts = frac_to_durs(float(e.dur) / (divisions * 4.0))
        if parts:
            return parts
    return ''


def render(e, slur, mode, divisions=1):
    if e.grace:
        return None
    if e.kind == 'rest':
        body = 'r'
    elif e.chord:
        body = '<%s>' % ' '.join([e.name] + e.chord)
    else:
        body = e.name
    d = dur_text(e, divisions)
    if isinstance(d, list):
        # a duration that is not a single notated value: emit the first, pad later
        d = d[0]
    s = body + d
    if not d:
        s = body
    if e.tie_start:
        s += '~'
    if e.slur_stop and slur['open'] > 0:
        s += ')'
        slur['open'] -= 1
    if e.slur_start and slur['open'] == 0:
        s += '('
        slur['open'] += 1
    for a in e.artic:
        s += a
    for dname in e.dyn:
        s += '\\' + dname
    if mode == 'keep' and e.slur_stop:
        pass
    return s


def measure_events(evs, mode, staff=None):
    """Group a measure's events per voice.

    merge mode: keep the first voice's material and only splice in events of the
    other voices that fall in gaps, so editorial voice splits collapse onto one
    stem without inventing simultaneities.
    """
    if mode == 'keep':
        if staff is not None:
            evs = [e for e in evs if e.staff == staff]
        groups = {}
        for e in evs:
            if e.grace:
                continue
            groups.setdefault(e.voice, []).append(e)
        for v in groups:
            groups[v].sort(key=lambda x: x.onset)
        return groups

    if staff is not None:
        evs = [e for e in evs if e.staff == staff]
    order = []
    by_voice = {}
    for e in evs:
        if e.grace:
            continue
        if e.voice not in by_voice:
            order.append(e.voice)
            by_voice[e.voice] = []
        by_voice[e.voice].append(e)
    for v in by_voice:
        by_voice[v].sort(key=lambda x: x.onset)
    placed = []
    out = []
    dropped = 0
    for v in order:
        for e in by_voice[v]:
            end = e.onset + e.dur
            if any(not (end <= s or e.onset >= t) for s, t in placed):
                dropped += 1
                continue
            placed.append((e.onset, end))
            out.append(e)
    if dropped:
        WARNINGS.append('merge dropped %d overlapping event(s)' % dropped)
    out.sort(key=lambda x: x.onset)
    return {'merged': out}


def voice_lines(evlist, divisions, q_time, mode, slur=None):
    """Render one measure's events for one voice."""
    if slur is None:
        slur = {'open': 0}
    toks = []
    if not evlist:
        qn = quarters_of(q_time)
        if qn:
            return ['R' + frac_to_durs(qn / 4.0)[0]], 0.0
        return [], 0.0
    i = 0
    while i < len(evlist):
        e = evlist[i]
        if e.tm:
            ratio = e.tm
            run = []
            j = i
            while j < len(evlist) and evlist[j].tm == ratio:
                run.append(evlist[j])
                j += 1
            inner = [render(x, slur, mode, divisions) for x in run]
            inner = [x for x in inner if x]
            toks.append('\\tuplet %d/%d { %s }' % (ratio[0], ratio[1], ' '.join(inner)))
            i = j
            continue
        r = render(e, slur, mode, divisions)
        if r:
            toks.append(r)
        i += 1
    used = sum(e.dur for e in evlist if not e.grace) / float((divisions or 1) * 4)
    return toks, used


def main():
    spec = json.load(open(sys.argv[1], encoding='utf-8'))
    base = os.path.dirname(os.path.abspath(sys.argv[1]))
    src = spec['source'] if os.path.isabs(spec['source']) else os.path.join(base, spec['source'])
    root = ET.parse(src).getroot()
    mode = spec.get('voices', 'merge')

    first_id = spec['parts'][0]['id']
    measures0, nums0, segs0 = movement_segments(root.find("./part[@id='%s']" % first_id))
    if spec.get('index_from') is not None:
        sel_idx = list(range(spec['index_from'], spec['index_to'] + 1))
    else:
        a, b = segs0[spec['segment']]
        sel_idx = [i for i in range(a, b + 1)
                   if nums0[i] is not None and spec['from'] <= nums0[i] <= spec['to']]
    if not sel_idx:
        raise SystemExit('empty selection')

    # carry attribute state forward from the start of the part
    state = {'key': (0, 'major'), 'time': None, 'divisions': 1}
    for i in range(0, sel_idx[0] + 1):
        info, _, _ = parse_measure(measures0[i])
        if info['key']:
            state['key'] = info['key']
        if info['time']:
            state['time'] = info['time']
        if info['divisions']:
            state['divisions'] = info['divisions']

    out = ['\\version "2.26.0"', '\\language "english"', '']
    for line in spec.get('comment', []):
        out.append('% ' + line)
    if spec.get('comment'):
        out.append('')

    out.append('global = {')
    if spec.get('key'):
        tonic, _, mode = spec['key'].partition(' ')
        sounding_key = (tonic, mode or 'major')
    else:
        sounding_key = key_of_state = state['key']
        sounding_key = (key_cmd(*state['key']).split()[1], 'minor' if 'minor' in key_cmd(*state['key']) else 'major')
    time_str = spec.get('time') or ('%d/%d' % state['time'] if state['time'] else None)
    if time_str:
        out.append('  \\time %s' % time_str)
    if spec.get('tempo'):
        out.append('  ' + spec['tempo'])
    out.append('}')
    out.append('')

    for part_spec in spec['parts']:
        pid = part_spec['id']
        part = root.find("./part[@id='%s']" % pid)
        measures, nums, segs = movement_segments(part)
        parsed = [parse_measure(m) for m in measures]

        tr = None
        tr_diatonic = {}
        clef = part_spec.get('clef', 'treble')
        pstate = dict(state)
        for i in range(0, sel_idx[0] + 1):
            info = parsed[i][0]
            if info['transpose']:
                tr = info['transpose']
                tr_diatonic[pid] = info.get('transpose_diatonic', -1)
            if info['key']:
                pstate['key'] = info['key']
            if info['time']:
                pstate['time'] = info['time']
            if info['divisions']:
                pstate['divisions'] = info['divisions']
            if info['clef'] and not part_spec.get('clef'):
                clef = info['clef']

        # per-voice accumulator
        voice_order = []
        lines_by_voice = {}
        slurs = {}
        first_info, first_evs, _ = parsed[sel_idx[0]]
        q_first = quarters_of(first_info['time'] or pstate['time'])
        div_first = first_info['divisions'] or pstate['divisions']
        partial = None
        if q_first:
            total0 = sum(e.dur for e in first_evs if not e.grace) / float(div_first * 4)
            if total0 and abs(total0 - q_first / 4.0) > 1e-6 and total0 < q_first / 4.0:
                partial = frac_to_durs(total0)
        for pos, i in enumerate(sel_idx):
            info, evs, maxpos = parsed[i]
            q = (info['time'] or pstate['time'])
            div = info['divisions'] or pstate['divisions']
            groups = measure_events(evs, mode, part_spec.get('staff'))
            for v in groups:
                if v not in lines_by_voice:
                    voice_order.append(v)
                    lines_by_voice[v] = []
            # render
            for v in voice_order:
                evlist = groups.get(v, [])
                if v not in slurs:
                    slurs[v] = {'open': 0}
                toks, used = voice_lines(evlist, div, q, mode, slurs[v])
                qnum = quarters_of(q)
                if qnum and not (pos == 0 and partial):
                    rest = qnum / 4.0 - used
                    if rest > 1e-6:
                        toks.extend(['r' + x for x in frac_to_durs(rest)])
                lines_by_voice[v].append(' '.join(toks) + ' |')
        for v in voice_order:
            if not lines_by_voice[v]:
                continue
            slurs.setdefault(v, {'open': 0})
            while slurs[v]['open'] > 0:
                removed = False
                for li in range(len(lines_by_voice[v]) - 1, -1, -1):
                    txt = lines_by_voice[v][li]
                    k = txt.rfind('(')
                    if k >= 0:
                        lines_by_voice[v][li] = txt[:k] + txt[k + 1:]
                        removed = True
                        break
                if not removed:
                    break
                slurs[v]['open'] -= 1
            # a tie that runs past the end of the excerpt must not dangle either
            last = lines_by_voice[v][-1]
            body = last[:-2].rstrip() if last.endswith(' |') else last.rstrip()
            while body.endswith('~'):
                body = body[:-1].rstrip()
            lines_by_voice[v][-1] = body + ' |'
        # fill empty voices
        for v in voice_order:
            lines_by_voice[v] = [ln if ln.strip() not in ('|', ' |') else 'R1 |'
                                 for ln in lines_by_voice[v]]

        out.append('%s = {' % part_spec['var'])
        out.append('  \\global')
        out.append('  \\clef %s' % clef)
        if tr:
            out.append('  \\transposition %s' % name_of_midi(60 + tr[0]))
            wname, wmode, wf = written_key(spec.get('key') or 'c major', tr[0],
                                           tr_diatonic.get(pid, -1))
            if spec.get('key') and wf is not None:
                out.append('  \\key %s \\%s' % (wname, wmode))
            else:
                out.append('  \\key %s \\%s' % (sounding_key[0], sounding_key[1]))
        else:
            out.append('  \\key %s \\%s' % (sounding_key[0], sounding_key[1]))
        if partial:
            out.append('  \\partial ' + ' '.join(partial))
        if len(voice_order) == 1:
            for ln in lines_by_voice[voice_order[0]]:
                out.append('  ' + ln)
        else:
            names = ['voiceOne', 'voiceTwo', 'voiceThree', 'voiceFour']
            out.append('  <<')
            for bi, v in enumerate(voice_order):
                out.append('    \\new Voice { \\%s' % names[min(bi, 3)])
                for ln in lines_by_voice[v]:
                    out.append('      ' + ln)
                out.append('    }')
            out.append('  >>')
        out.append('}')
        out.append('')

    out.append('\\score {')
    out.append('  \\new StaffGroup <<')
    for part_spec in spec['parts']:
        out.append('    \\new Staff { \\set Staff.midiInstrument = "%s" \\%s }'
                   % (part_spec['gm'], part_spec['var']))
    out.append('  >>')
    out.append('  \\layout { ragged-right = ##f }')
    out.append('  \\midi { }')
    out.append('}')

    dst = sys.argv[2]
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print('wrote', dst)
    print('measures:', [nums0[i] for i in sel_idx][:4], '...',
          [nums0[i] for i in sel_idx][-3:], 'count', len(sel_idx))
    for w in WARNINGS[:20]:
        print('WARN', w)
    if len(WARNINGS) > 20:
        print('WARN ... %d more' % (len(WARNINGS) - 20))


if __name__ == '__main__':
    main()
