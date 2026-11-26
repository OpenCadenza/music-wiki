#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Convert Humdrum **kern excerpts to the repo's LilyPond fence format.

Modes:
  probe <file.krn>                      : staff layout, attrs per measure
  dump  <file.krn> <m0> <m1> [staves]   : per-measure / per-staff / per-voice dump
  emit  <spec.json>                     : full fence body to stdout

Slicing model: each data record advances time by the minimum of (durations of new
notes, remaining time of sustained notes).  '.' keeps the previous note sounding.
Barlines advance a sequence index; numbered barlines carry the printed measure
number, unnumbered ones (repeat endings) do not.

Pitch: lowercase n letters -> octave 3+n (c=C4); uppercase n letters -> octave 4-n
(C=C3).  '#' sharp, '-' flat, 'n' natural, 'X' double sharp.
Suffix signs: ' staccato, ^ accent, ( ) slur, [ ] _ tie, q grace, k cautionary,
L/J beams, \ / stems.
"""
import json
import re
import sys
from fractions import Fraction

PREFIX_CHARS = '([<>{_~'

REST_RE = re.compile(r'^(?P<dur>\d+)(?P<dots>\.*)r(?P<suf>.*)$')
DUR_FIRST_RE = re.compile(r'^(?P<dur>\d+)(?P<dots>\.*)(?P<letters>[A-Ga-g]+)'
                          r'(?P<acc>[#nXx-]*)(?P<suf>.*)$')
PITCH_FIRST_RE = re.compile(r'^(?P<letters>[A-Ga-g]+)(?P<acc>[#nXx-]*)'
                            r'(?P<dur>\d+)(?P<dots>\.*)(?P<suf>.*)$')

POW2 = {1: Fraction(1), 2: Fraction(1, 2), 4: Fraction(1, 4), 8: Fraction(1, 8),
        16: Fraction(1, 16), 32: Fraction(1, 32), 64: Fraction(1, 64),
        128: Fraction(1, 128), 256: Fraction(1, 256)}
DUR_ORDER = [(1, '1'), (2, '2'), (4, '4'), (8, '8'), (16, '16'), (32, '32'),
             (64, '64'), (128, '128')]
CLEF_MAP = {'G2': 'treble', 'G1': 'treble', 'F4': 'bass', 'F3': 'bass',
            'C3': 'alto', 'C4': 'tenor', 'C1': 'soprano', 'C2': 'mezzosoprano'}
KEY_MAJOR = {0: 'c', 1: 'g', 2: 'd', 3: 'a', 4: 'e', 5: 'b', 6: 'fs', 7: 'cs',
             -1: 'f', -2: 'bf', -3: 'ef', -4: 'af', -5: 'df', -6: 'gf', -7: 'cf'}
KEY_MINOR = {0: 'a', 1: 'e', 2: 'b', 3: 'fs', 4: 'cs', 5: 'gs', 6: 'ds', 7: 'as',
             -1: 'd', -2: 'g', -3: 'c', -4: 'f', -5: 'bf', -6: 'ef', -7: 'af'}


def dur_value(digits, dots):
    if digits in ('0', '00'):
        base = Fraction(2) if digits == '0' else Fraction(4)
    else:
        base = Fraction(1, int(digits))
    return base * (Fraction(2) - Fraction(1, 2 ** len(dots)))


def dur_regular(dur):
    for den, name in DUR_ORDER:
        base = POW2[den]
        for k in range(4):
            if base * (Fraction(2) - Fraction(1, 2 ** k)) == dur:
                return name + '.' * k
    return None


def dur_ly(dur):
    reg = dur_regular(dur)
    if reg:
        return reg
    for den, name in reversed(DUR_ORDER):
        base = POW2[den]
        if base >= dur:
            ratio = dur / base
            return '%s*%d/%d' % (name, ratio.numerator, ratio.denominator)
    return '128'


def dur_tokens(dur, symbol='s'):
    out = []
    rest = dur
    for den, name in DUR_ORDER:
        for k in (3, 2, 1, 0):
            val = POW2[den] * (Fraction(2) - Fraction(1, 2 ** k))
            while rest >= val - Fraction(1, 1024):
                out.append(symbol + name + '.' * k)
                rest -= val
    if rest > Fraction(1, 1024):
        out.append(symbol + dur_ly(rest))
    return out


def pitch_of(letters, acc, suf):
    n = len(letters)
    base = letters[0].lower()
    octave = 3 + n if letters[0].islower() else 4 - n
    # NOTE: 'X' in these MuseData-derived kern files is an editorial/cautionary
    # accidental marker, not a double sharp; real double sharps appear as '##'.
    if '##' in acc:
        alter = 2
    elif '#' in acc:
        alter = 1
    elif '--' in acc:
        alter = -2
    elif '-' in acc:
        alter = -1
    else:
        alter = 0
    name = base + {1: 's', -1: 'f', 2: 'x', -2: 'ff'}.get(alter, '')
    name += ("'" * (octave - 3)) if octave >= 3 else (',' * (3 - octave))
    midi = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}[base]
    return name, midi + alter + 12 * (octave + 1), alter, 'k' in suf


def parse_piece(piece):
    pre = ''
    i = 0
    while i < len(piece) and piece[i] in PREFIX_CHARS:
        pre += piece[i]
        i += 1
    body = piece[i:]
    rest = False
    if body[:1].isdigit():
        m = REST_RE.match(body)
        if m:
            rest = True
            dur = dur_value(m.group('dur'), m.group('dots'))
            letters, acc, suf = '', '', m.group('suf')
        else:
            m = DUR_FIRST_RE.match(body)
            if not m:
                return None
            dur = dur_value(m.group('dur'), m.group('dots'))
            letters, acc, suf = m.group('letters'), m.group('acc'), m.group('suf')
    else:
        m = PITCH_FIRST_RE.match(body)
        if not m:
            return None
        dur = dur_value(m.group('dur'), m.group('dots'))
        letters, acc, suf = m.group('letters'), m.group('acc'), m.group('suf')
    notes = []
    if not rest:
        name, midi, alter, caut = pitch_of(letters, acc, suf)
        notes.append({'name': name, 'midi': midi, 'alter': alter, 'caut': caut})
    return {
        'rest': rest, 'dur': dur, 'notes': notes,
        'grace': 'q' in suf,
        'tie_start': '[' in pre or '_' in pre or '_' in suf,
        'tie_stop': ']' in pre or ']' in suf,
        'slur_start': '(' in pre,
        'slur_end': ')' in pre or ')' in suf,
        'stacc': "'" in suf,
        'accent': '^' in suf,
        'invisible': rest and 'y' in suf,
    }


class Spine:
    __slots__ = ('staff', 'voice', 'kind', 'clef', 'remaining', 'clef_dirty')

    def __init__(self, staff, voice, kind, clef='G2'):
        self.staff, self.voice, self.kind, self.clef = staff, voice, kind, clef
        self.remaining = Fraction(0)
        self.clef_dirty = False

    def copy(self):
        s = Spine(self.staff, self.voice, self.kind, self.clef)
        s.remaining = self.remaining
        s.clef_dirty = self.clef_dirty
        return s


class Ev:
    __slots__ = ('kind', 'dur', 'notes', 'grace', 'slur_s', 'slur_e',
                 'stacc', 'accent', 'invisible', 'time', 'clef',
                 'tie_start', 'tie_stop', 'tuplet')

    def __init__(self, **kw):
        self.grace = []
        self.clef = None
        self.slur_s = self.slur_e = False
        self.stacc = self.accent = self.invisible = False
        self.tie_start = self.tie_stop = False
        self.tuplet = None
        for k, v in kw.items():
            setattr(self, k, v)


def load(path):
    raw = open(path, encoding='utf-8', errors='replace').read().splitlines()
    meta, spines = {}, []
    for ln in raw:
        if ln.startswith('!!!'):
            m = re.match(r'!!!(\w+):\s*(.*)', ln)
            if m:
                meta.setdefault(m.group(1), m.group(2).strip())
        if ln.startswith('**'):
            header = ln.split('\t')
            spines = [Spine(None, i, 'dynam' if h.lstrip('*') == 'dynam' else 'kern')
                      for i, h in enumerate(header)]
            break
    next_voice = [len(spines)]
    measures, measure_len, meter_str = {}, {}, {}
    label = {}          # seq -> printed measure number (or None)
    mstart = {}         # seq -> attrs in effect at measure start
    clef_at = {}        # seq -> {staff: clef}
    order = {}
    warnings = []
    seq = 0
    elapsed = Fraction(0)
    meter, meter_s = Fraction(3, 4), '3/4'
    cur = {'key': None, 'tempo': None, 'designation': None}
    pending_grace = {}
    slur_open = {}
    slur_defer = {}
    label[0] = None
    measures[0] = {}
    for ln in raw:
        if not ln.strip() or ln.startswith('**') or ln.startswith('!!!'):
            continue
        if ln.startswith('*'):
            toks = ln.split('\t')
            if len(toks) != len(spines):
                warnings.append('interp token mismatch seq%d: %r' % (seq, ln))
                continue
            out, i = [], 0
            while i < len(toks):
                t, sp = toks[i], spines[i]
                tm = re.match(r'\*M(\d+)/(\d+)$', t)
                if tm:
                    n, d = tm.groups()
                    meter, meter_s = Fraction(int(n), int(d)), '%s/%s' % (n, d)
                tk = re.match(r'\*MM(\d+)$', t)
                if tk:
                    cur['tempo'] = int(tk.group(1))
                tk = re.match(r'\*k\[(.*?)\]$', t)
                if tk:
                    cur['key'] = tk.group(1)
                tk = re.match(r'\*([A-Ga-g][#n-]*):$', t)
                if tk:
                    cur['designation'] = t[1:-1]
                if t == '*^':
                    out.append(sp.copy())
                    v = next_voice[0]
                    next_voice[0] += 1
                    ns = sp.copy()
                    ns.voice = v
                    out.append(ns)
                    i += 1
                    continue
                if t == '*v':
                    out.append(sp.copy())
                    i += 2
                    continue
                tc = re.match(r'\*clef(\S+)$', t)
                if tc:
                    sp.clef = tc.group(1)
                    sp.clef_dirty = True
                ts = re.match(r'\*staff(\d+)$', t)
                if ts:
                    sp.staff = int(ts.group(1))
                out.append(sp)
                i += 1
            spines = out
            continue
        if ln.startswith('='):
            measure_len[seq], meter_str[seq] = meter, meter_s
            mm = re.match(r'=(\d+)', ln)
            seq += 1
            label[seq] = int(mm.group(1)) if mm else None
            measures.setdefault(seq, {})
            elapsed = Fraction(0)
            continue
        if ln.startswith('!'):
            continue
        toks = ln.split('\t')
        if len(toks) != len(spines):
            warnings.append('data token mismatch seq%d: %r' % (seq, ln))
            continue
        measures.setdefault(seq, {})
        if seq not in clef_at:
            clef_at[seq] = {}
            for sp in spines:
                if sp.staff is not None and sp.kind == 'kern':
                    clef_at[seq].setdefault(sp.staff, sp.clef)
        if seq not in mstart:
            prev = mstart.get(seq - 1, {})
            snap = {'meter': meter_s, 'key': prev.get('key'),
                    'tempo': cur['tempo'], 'designation': prev.get('designation')}
            snap['key'] = cur['key'] or prev.get('key')
            snap['designation'] = cur['designation'] or prev.get('designation')
            mstart[seq] = snap
        cands, infos = [], []
        for sp, t in zip(spines, toks):
            t = t.strip()
            if sp.kind != 'kern':
                infos.append(None)
                continue
            if not t or t == '.':
                cands.append(sp.remaining if sp.remaining > 0 else None)
                infos.append(('null', None))
                continue
            pieces = []
            for piece in t.split():
                try:
                    ev = parse_piece(piece)
                except ValueError as exc:
                    warnings.append('parse error seq%d: %r (%s)' % (seq, piece, exc))
                    ev = None
                if ev is not None:
                    pieces.append(ev)
            real = [p for p in pieces if not p['grace']]
            cands.append(min(p['dur'] for p in real) if real else Fraction(0))
            infos.append(('ev', pieces))
        slice_dur = min([c for c in cands if c is not None], default=Fraction(0))
        # lane = position of this spine among its staff's kern spines in this record
        kern_idx = [i for i, sp in enumerate(spines)
                    if sp.kind == 'kern' and sp.staff is not None]
        lane_of = {}
        for i in kern_idx:
            lane_of[i] = sum(1 for j in kern_idx
                             if j < i and spines[j].staff == spines[i].staff)
        for si_, (sp, info) in enumerate(zip(spines, infos)):
            if info is None or sp.staff is None or sp.kind != 'kern':
                continue
            lane = lane_of.get(si_, 0)
            kind, pieces = info
            if kind == 'null':
                sp.remaining = max(Fraction(0), sp.remaining - slice_dur)
                continue
            real = [p for p in pieces if not p['grace']]
            graces = [p for p in pieces if p['grace']]
            if graces and not real:
                pending_grace.setdefault(sp.voice, []).extend(graces)
                continue
            if not real:
                sp.remaining = max(Fraction(0), sp.remaining - slice_dur)
                continue
            notes = [n for p in real for n in p['notes']]
            durs = {p['dur'] for p in real}
            dur = max(durs)
            if len(durs) > 1:
                warnings.append('chord mixed durations seq%d %r' % (seq, notes))
            ev = Ev(kind='rest' if real[0]['rest'] else 'note', dur=dur,
                    notes=notes, time=elapsed,
                    tie_start=any(p['tie_start'] for p in real),
                    tie_stop=any(p['tie_stop'] for p in real),
                    slur_s=any(p['slur_start'] for p in real),
                    slur_e=any(p['slur_end'] for p in real),
                    stacc=any(p['stacc'] for p in real),
                    accent=any(p['accent'] for p in real),
                    invisible=all(p['invisible'] for p in real))
            if sp.clef_dirty:
                ev.clef = sp.clef
                sp.clef_dirty = False
            ev.grace = pending_grace.pop(sp.voice, [])
            if ev.slur_e:
                if slur_open.get(sp.voice):
                    slur_open[sp.voice] = False
                else:
                    ev.slur_e = False
            if ev.slur_s:
                if ev.slur_e or slur_open.get(sp.voice):
                    ev.slur_s = False
                    slur_defer[sp.voice] = True
                else:
                    slur_open[sp.voice] = True
            elif slur_defer.pop(sp.voice, False):
                ev.slur_s = True
                slur_open[sp.voice] = True
            measures[seq].setdefault(sp.staff, {}).setdefault(lane, []).append(ev)
            if lane not in order.setdefault(sp.staff, []):
                order[sp.staff].append(lane)
            sp.remaining = dur - slice_dur
        elapsed += slice_dur
        measure_len[seq], meter_str[seq] = meter, meter_s
    for k in order:
        order[k] = sorted(order[k])
    return {'measures': measures, 'len': measure_len, 'meter': meter_str,
            'label': label, 'mstart': mstart, 'order': order, 'meta': meta,
            'clef_at': clef_at, 'warnings': warnings}


# ---------------------------------------------------------------- rendering

def key_of(mstart, seq):
    a = mstart.get(seq, {})
    sig, desig = a.get('key'), a.get('designation')
    n = 0
    if sig:
        n = sig.count('#') - sig.count('-')
    minor = bool(desig) and desig[0].islower()
    if desig:
        name = desig[0].lower() + desig[1:].replace('-', 'f')
        return '%s \\%s' % (name, 'minor' if minor else 'major')
    table = KEY_MINOR if minor else KEY_MAJOR
    return '%s \\%s' % (table.get(n, 'c'), 'minor' if minor else 'major')


def beat_unit(meter):
    n, d = meter.split('/')
    n, d = int(n), int(d)
    if d in (8, 16) and n % 3 == 0:
        return '8.'
    if d == 16:
        return '16'
    if d == 32:
        return '32'
    return str(d) if d <= 4 else str(d)


def group_tuplets(events):
    out = []
    i = 0
    while i < len(events):
        e = events[i]
        if dur_regular(e.dur) or e.kind == 'rest':
            out.append(('ev', e))
            i += 1
            continue
        cand = []
        for den, name in DUR_ORDER:
            base = POW2[den]
            for n in range(3, 8):
                for m in range(2, n):
                    if base * Fraction(m, n) == e.dur:
                        cand.append((0 if m == n - 1 else 1, n, -m, n, m, base))
        cand.sort()
        ratio = (cand[0][3], cand[0][4], cand[0][5]) if cand else None
        if not ratio:
            out.append(('ev', e))
            i += 1
            continue
        n, m, base = ratio
        group, total = [], Fraction(0)
        j = i
        while j < len(events) and total < m * base:
            ev = events[j]
            if dur_regular(ev.dur):
                break
            group.append(ev)
            total += ev.dur
            j += 1
        if total == m * base and len(group) >= 2:
            for ev in group:
                ev.tuplet = (n, m)
            out.append(('tuplet', n, m, group))
            i = j
        else:
            out.append(('ev', e))
            i += 1
    return out


def event_ly(e):
    parts = []
    if e.clef:
        parts.append('\\clef "%s"' % CLEF_MAP.get(e.clef, 'treble'))
    if e.grace:
        g = ' '.join(n['name'] + dur_ly(gg['dur'])
                     for gg in e.grace for n in gg['notes'])
        parts.append('\\grace { %s }' % g)
    if e.slur_s:
        parts.append('(')
    if e.kind == 'rest':
        parts.append('s' if e.invisible else 'r')
    else:
        names = ' '.join(n['name'] for n in e.notes)
        if len(e.notes) > 1:
            names = '<%s>' % names
        parts.append(names)
    dur = dur_ly(e.dur)
    if e.tuplet:
        n, m = e.tuplet
        writ = e.dur * Fraction(n, m)
        dur = dur_regular(writ) or dur_ly(writ)
    parts.append(dur)
    if e.accent:
        parts.append('->')
    if e.stacc:
        parts.append('-.')
    if e.tie_start:
        parts.append('~')
    if e.slur_e:
        parts.append(')')
    return ' '.join(parts)


def fmt_seq(piece, seq):
    lab = piece['label'].get(seq)
    if lab is not None:
        return 'm.%d' % lab
    k = seq - 1
    while k >= 0 and piece['label'].get(k) is None:
        k -= 1
    return 'm.%s+%d' % (piece['label'].get(k), seq - k)


def render_voice(piece, staff_no, vid, s0, s1, tempo_ok=False,
                 label_prefix=''):
    prev_meter = piece['meter'].get(s0)
    prev_key = key_of(piece['mstart'], s0)
    prev_tempo = piece['mstart'].get(s0, {}).get('tempo')
    per_measure = []
    carry = []
    for seq in range(s0, s1 + 1):
        mlen = piece['len'].get(seq)
        meter_s = piece['meter'].get(seq)
        key_s = key_of(piece['mstart'], seq)
        tempo = piece['mstart'].get(seq, {}).get('tempo')
        pre = []
        if seq != s0:
            if meter_s != prev_meter:
                pre.append('\\time %s' % meter_s)
                prev_meter = meter_s
            if key_s != prev_key:
                pre.append('\\key %s' % key_s)
                prev_key = key_s
            if tempo and tempo != prev_tempo:
                if tempo_ok:
                    pre.append('\\tempo %s = %s' % (beat_unit(meter_s or '4/4'), tempo))
                prev_tempo = tempo
        evs = carry + list(piece['measures'].get(seq, {}).get(staff_no, {}).get(vid, []))
        carry = []
        cells, used = [], Fraction(0)
        for e in evs:
            if mlen is None:
                cells.append(e)
                used += e.dur
                continue
            room = mlen - used
            if e.dur <= room:
                cells.append(e)
                used += e.dur
            else:
                first = Ev(kind=e.kind, dur=room, notes=e.notes, time=e.time,
                           slur_s=e.slur_s, slur_e=False, stacc=e.stacc,
                           accent=e.accent, invisible=e.invisible, clef=e.clef,
                           tie_start=True, tie_stop=False)
                first.grace = e.grace
                cells.append(first)
                used += room
                carry.append(Ev(kind=e.kind, dur=e.dur - room, notes=e.notes,
                                time=Fraction(0), slur_s=False, slur_e=e.slur_e,
                                stacc=e.stacc, accent=e.accent,
                                invisible=e.invisible))
                break
        per_measure.append({'seq': seq, 'cells': cells, 'used': used,
                            'len': mlen, 'pre': pre})
    # tie sanity: keep '~' only when the next event repeats the pitches
    flat = []
    for item in per_measure:
        for e in item['cells']:
            flat.append(e)
    for k, e in enumerate(flat):
        if not e.tie_start:
            continue
        ok = False
        if k + 1 < len(flat):
            nxt = flat[k + 1]
            if nxt.kind == 'note' and e.kind == 'note':
                a = sorted(n['midi'] for n in e.notes)
                b = sorted(n['midi'] for n in nxt.notes)
                ok = a == b
        e.tie_start = ok
    if carry and flat:
        flat[-1].tie_start = False
    lines = []
    for item in per_measure:
        toks = list(item['pre'])
        for sub in group_tuplets(item['cells']):
            if sub[0] == 'ev':
                toks.append(event_ly(sub[1]))
            else:
                n, m, evs2 = sub[1], sub[2], sub[3]
                toks.append('\\tuplet %d/%d { %s }'
                            % (n, m, ' '.join(event_ly(x) for x in evs2)))
        if item['len'] is not None and item['used'] < item['len']:
            toks.extend(dur_tokens(item['len'] - item['used'], 's'))
        if toks:
            lines.append(' '.join(toks) + ' | % ' + label_prefix
                         + fmt_seq(piece, item['seq']))
        else:
            lines.append('% ' + label_prefix + fmt_seq(piece, item['seq']))
    return lines


def resolve_range(piece, m_from, m_to):
    seqs = [s for s, lab in piece['label'].items() if lab is not None]
    s0 = min(s for s in seqs if piece['label'][s] == int(m_from))
    s1 = max(s for s in seqs if piece['label'][s] == int(m_to))
    return s0, s1


def emit(piece, spec):
    s0, s1 = resolve_range(piece, spec['from'], spec['to'])
    staves = spec['staves']
    order = piece['order']
    out = []

    def add(s=''):
        out.append(s)

    if spec.get('title'):
        hdr = '```lilypond title="%s" location="%s"' % (spec['title'],
                                                        spec.get('location', ''))
        if spec.get('id'):
            hdr += ' id="%s"' % spec['id']
        add(hdr)
    add('\\version "2.26.0"')
    add('\\language "english"')
    add('')
    for c in spec.get('comment', []):
        add('% ' + c)
    if spec.get('comment'):
        add('')
    meter0 = piece['meter'].get(s0) or '4/4'
    key0 = key_of(piece['mstart'], s0)
    tempo0 = piece['mstart'].get(s0, {}).get('tempo')
    tempo_text = spec.get('tempo_text')
    add('global = {')
    add('  \\key %s' % key0)
    add('  \\time %s' % meter0)
    add('}')
    tempo_head = None
    if tempo_text:
        if tempo0:
            tempo_head = '\\tempo "%s" %s = %s' % (tempo_text, beat_unit(meter0), tempo0)
        else:
            tempo_head = '\\tempo "%s"' % tempo_text
    elif tempo0:
        tempo_head = '\\tempo %s = %s' % (beat_unit(meter0), tempo0)
    add('')
    piano = len(staves) == 2 and all(s.get('gm') == 'acoustic grand' for s in staves)
    label_prefix = 'kern ' if spec.get('kern_labels') else ''
    for si, st in enumerate(staves):
        staff_no = st['staff']
        vids = [v for v in order.get(staff_no, [])
                if any(piece['measures'].get(s, {}).get(staff_no, {}).get(v)
                       for s in range(s0, s1 + 1))]
        vids = vids[:4]
        names = ['%s%s' % (st.get('prefix', 'v'), x)
                 for x in ['I', 'II', 'III', 'IV'][:len(vids)]]
        first_clef = CLEF_MAP.get(
            piece.get('clef_at', {}).get(s0, {}).get(staff_no, 'G2'), 'treble')
        add('%s = {' % st['var'])
        add('  \\clef "%s"' % first_clef)
        if si == 0 and tempo_head:
            add('  ' + tempo_head)
        if len(vids) > 1:
            add('  <<')
            for vi, (v, name) in enumerate(zip(vids, names)):
                add('    \\new Voice = "%s" {' % name)
                add('      \\voice%s' % ['One', 'Two', 'Three', 'Four'][vi])
                for line in render_voice(piece, staff_no, v, s0, s1,
                                         tempo_ok=(si == 0 and vi == 0),
                                         label_prefix=label_prefix):
                    add('      ' + line)
                add('    }')
            add('  >>')
        else:
            for line in render_voice(piece, staff_no, vids[0] if vids else None,
                                     s0, s1, tempo_ok=(si == 0),
                                     label_prefix=label_prefix):
                add('  ' + line)
        add('}')
        add('')
    add('\\score {')
    add('  \\new PianoStaff <<' if piano else '  <<')
    for st in staves:
        add('    \\new Staff = "%s" {' % st.get('label', st['var']))
        add('      \\set Staff.midiInstrument = "%s"' % st['gm'])
        add('      \\global')
        add('      \\%s' % st['var'])
        add('    }')
    add('  >>')
    add('  \\layout { ragged-right = ##f }')
    add('  \\midi { }')
    add('}')
    return '\n'.join(out)


def dump(piece, s0, s1, staves):
    out = []
    for seq in range(s0, s1 + 1):
        ms = piece['measures'].get(seq)
        a = piece['mstart'].get(seq, {})
        if not ms:
            out.append('== %s  (no data)' % fmt_seq(piece, seq))
            continue
        out.append('== %s  meter=%s key=%s tempo=%s designation=%s' % (
            fmt_seq(piece, seq), piece['meter'].get(seq), a.get('key'),
            a.get('tempo'), a.get('designation')))
        for st in staves:
            voices = ms.get(st, {})
            if not voices:
                out.append('  staff%d: (empty)' % st)
            for v in piece['order'].get(st, []):
                evs = voices.get(v, [])
                if not evs:
                    continue
                out.append('  staff%d v%-3d: %s' % (st, v,
                                                    ' '.join(ev_dump(e) for e in evs)))
    return '\n'.join(out)


def ev_dump(e):
    pre = ''
    if e.grace:
        pre = '\\grace{%s} ' % ' '.join(n['name'] + dur_ly(g['dur'])
                                        for g in e.grace for n in g['notes'])
    if e.clef:
        pre += '[CLEF %s] ' % e.clef
    if e.slur_s:
        pre += '('
    body = 'r' if e.kind == 'rest' else ' '.join(n['name'] for n in e.notes)
    if len(e.notes) > 1:
        body = '<%s>' % body
    post = ''
    if e.accent:
        post += '->'
    if e.stacc:
        post += '-.'
    if e.tie_start:
        post += '~'
    if e.slur_e:
        post += ')'
    return pre + body + dur_ly(e.dur) + post


def main():
    mode = sys.argv[1]
    if mode == 'probe':
        piece = load(sys.argv[2])
        print('meta', piece['meta'])
        print('order', piece['order'])
        labs = [lab for lab in piece['label'].values() if lab is not None]
        print('measures', min(labs), '..', max(labs), 'seqs', max(piece['measures']))
        prev = None
        for seq in sorted(piece['measures']):
            a = piece['mstart'].get(seq, {})
            key = (piece['meter'].get(seq), a.get('tempo'), a.get('key'),
                   a.get('designation'))
            if key != prev:
                print(' %-10s meter=%s tempo=%s key=%s designation=%s' % (
                    fmt_seq(piece, seq), piece['meter'].get(seq), a.get('tempo'),
                    a.get('key'), a.get('designation')))
                prev = key
        for w in piece['warnings'][:40]:
            print('WARN', w)
    elif mode == 'dump':
        path, m0, m1 = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        staves = [int(x) for x in sys.argv[5].split(',')] if len(sys.argv) > 5 else [1, 2]
        piece = load(path)
        s0, s1 = resolve_range(piece, m0, m1)
        print(dump(piece, s0, s1, staves))
        for w in piece['warnings'][:20]:
            print('WARN', w)
    elif mode == 'emit':
        spec = json.load(open(sys.argv[2], encoding='utf-8'))
        piece = load(spec['kern'])
        print(emit(piece, spec))
        for w in piece['warnings'][:20]:
            sys.stderr.write('WARN %s\n' % w)
    else:
        raise SystemExit('unknown mode ' + mode)


if __name__ == '__main__':
    main()
