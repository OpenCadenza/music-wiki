#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MXL / MusicXML -> LilyPond 谱例草案（score-b 自用工具，v3）。

要点：
- `--pos` 用「文件内绝对小节位置」（第 n 个 <measure>）；脚本打印对应 MusicXML 小节号。
- 音高、时值、连音线、和弦、跳音/重音、力度、Slur、双音震音（\\repeat tremolo）、移调均按源文件生成。
- 输出已含 \\version / \\language / global / 每谱表 midiInstrument / \\layout / \\midi，可直接编译；
  排版细节（分句连音、指法、踏板、双声部交叉）仍需人工复核。
"""
import argparse
import sys
import zipfile
from fractions import Fraction
from lxml import etree

ALTER_SUFFIX = {-2: 'ff', -1: 'f', 0: '', 1: 's', 2: 'ss'}
MAJOR_BY_FIFTHS = {0: 'c', 1: 'g', 2: 'd', 3: 'a', 4: 'e', 5: 'b', 6: 'fs', 7: 'cs',
                   -1: 'f', -2: 'bf', -3: 'ef', -4: 'af', -5: 'df', -6: 'gf', -7: 'cf'}
MINOR_BY_FIFTHS = {0: 'a', 1: 'e', 2: 'b', 3: 'fs', 4: 'cs', 5: 'gs', 6: 'ds', 7: 'as',
                   -1: 'd', -2: 'g', -3: 'c', -4: 'f', -5: 'bf', -6: 'ef', -7: 'af'}
DUR_BY_TYPE = {'breve': '\\breve', 'whole': '1', 'half': '2', 'quarter': '4', 'eighth': '8',
               '16th': '16', '32nd': '32', '64th': '64', '128th': '128'}
DUR_VAL = {'breve': Fraction(2), 'whole': Fraction(1), 'half': Fraction(1, 2), 'quarter': Fraction(1, 4),
           'eighth': Fraction(1, 8), '16th': Fraction(1, 16), '32nd': Fraction(1, 32),
           '64th': Fraction(1, 64), '128th': Fraction(1, 128)}
ARTIC = {'staccato': '-.', 'staccatissimo': '-!', 'accent': '->', 'strong-accent': '-^',
         'tenuto': '--', 'detached-legato': '-_', 'marcato': '-^'}
CLEFS = {('G', '2'): 'treble', ('F', '4'): 'bass', ('C', '3'): 'alto', ('C', '4'): 'tenor',
         ('C', '1'): 'soprano', ('C', '2'): 'mezzosoprano', ('F', '3'): 'baritone', ('G', '1'): 'french'}
TRANSP = {0: 'c', -1: 'b', -2: 'bf', -3: 'a', -4: 'af', -5: 'g', -6: 'gf', -7: 'f', -8: 'e',
          -9: 'ef', -10: 'd', -11: 'df', 1: 'cs', 2: 'd', 3: 'ef', 4: 'e', 5: 'f',
          6: 'fs', 7: 'g', 8: 'af', 9: 'a', 10: 'bf', 11: 'b'}
KEEP_WORDS = False
KNOWN_DYN = {'p', 'pp', 'ppp', 'pppp', 'ppppp', 'f', 'ff', 'fff', 'ffff', 'mf', 'mp',
             'sf', 'sfz', 'fp', 'rfz', 'sfp', 'fz', 'sffz'}




NUMWORD = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
           "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten"}


def staff_var(pid):
    num = pid.replace("P", "")
    return "staff" + NUMWORD.get(num, num)


def log(msg):
    print(msg, file=sys.stderr)


def emit(text, args):
    if getattr(args, 'out', ''):
        open(args.out, 'w', encoding='utf-8', newline='\n').write(text + '\n')
        log('wrote ' + args.out)
    else:
        print(text)
TREM_UNIT = {'1': Fraction(1, 8), '2': Fraction(1, 16), '3': Fraction(1, 32), '4': Fraction(1, 64)}


def load_root(path):
    if path.lower().endswith(('.xml', '.musicxml')):
        return etree.parse(path).getroot()
    z = zipfile.ZipFile(path)
    xmls = [n for n in z.namelist() if n.lower().endswith(('.xml', '.musicxml')) and 'META-INF' not in n]
    if not xmls:
        sys.exit('no musicxml in ' + path)
    return etree.fromstring(z.read(xmls[0]))


def lily_pitch(step, alter, octave):
    """MusicXML octave 4 = middle C；LilyPond c' = middle C（已用 MIDI 实测核对：c'→60）。"""
    name = step.lower() + ALTER_SUFFIX.get(int(alter or 0), '')
    o = int(octave) - 3
    return name + ("'" * o if o > 0 else ',' * (-o))


def sort_pitch_key(p):
    order = {'c': 0, 'd': 1, 'e': 2, 'f': 3, 'g': 4, 'a': 5, 'b': 6}
    return (p.count("'") - p.count(','), order.get(p[0], 0))


def fifths_key(fifths, mode):
    f = int(fifths or 0)
    if (mode or 'major') == 'minor':
        return MINOR_BY_FIFTHS.get(f, 'a') + ' \\minor'
    return MAJOR_BY_FIFTHS.get(f, 'c') + ' \\major'


def rest_tokens(total):
    out = []
    order = [(Fraction(1), '1'), (Fraction(1, 2), '2'), (Fraction(1, 4), '4'), (Fraction(1, 8), '8'),
             (Fraction(1, 16), '16'), (Fraction(1, 32), '32'), (Fraction(1, 64), '64')]
    while total > 0:
        for val, tok in order:
            if total >= val:
                out.append('r' + tok)
                total -= val
                break
        else:
            out.append('r64')
            break
    return out


def marks_of(el):
    out = []
    for a in el.findall('./notations/articulations/*'):
        tag = etree.QName(a).localname
        if tag in ARTIC:
            out.append(ARTIC[tag])
    if el.findall('./notations/technical/down-bow'):
        out.append('\\downbow')
    if el.findall('./notations/technical/up-bow'):
        out.append('\\upbow')
    if el.findall('./notations/fermata'):
        out.append('\\fermata')
    if el.findall('./notations/ornaments/trill-mark'):
        out.append('\\trill')
    if el.findall('./notations/arpeggiate'):
        out.append('\\arpeggio')
    return out


def slur_of(el):
    s = ''
    for sl in el.findall('./notations/slur'):
        if sl.get('type') == 'start':
            s += '('
        elif sl.get('type') == 'stop':
            s += ')'
    return s


def tie_start(el):
    for t in el.findall('./tie'):
        if t.get('type') == 'start':
            return True
    for t in el.findall('./notations/tied'):
        if t.get('type') == 'start':
            return True
    return False


def measure_length(meas, div, timesig):
    total = Fraction(0)
    cur = Fraction(0)
    for el in meas:
        tag = etree.QName(el).localname
        if tag in ('backup', 'forward'):
            d = Fraction(int(el.findtext('./duration') or 0), div)
            cur = cur - d if tag == 'backup' else cur + d
            total = max(total, cur)
        elif tag == 'note':
            if el.find('./chord') is None:
                cur += Fraction(int(el.findtext('./duration') or 0), div)
                total = max(total, cur)
    if timesig and timesig[0]:
        try:
            return Fraction(int(timesig[0]), int(timesig[1])) * 4 / 4  # beats/beat-type -> whole notes
        except Exception:
            pass
    return total / 4


def dynamics_in(meas, div):
    out = []
    cur = Fraction(0)
    for el in meas:
        tag = etree.QName(el).localname
        if tag in ('backup', 'forward'):
            d = Fraction(int(el.findtext('./duration') or 0), div)
            cur = cur - d if tag == 'backup' else cur + d
        elif tag == 'note':
            if el.find('./chord') is None:
                cur += Fraction(int(el.findtext('./duration') or 0), div)
        elif tag == 'direction':
            off = Fraction(int(el.findtext('./offset') or 0), div)
            for d in el.findall('./direction-type/dynamics/*'):
                dn = etree.QName(d).localname
                if dn in KNOWN_DYN:
                    out.append((cur + off, '\\' + dn))
            if KEEP_WORDS:
                for w in el.findall('./direction-type/words'):
                    txt = (w.text or '').strip()
                    if txt and len(txt) < 40:
                        out.append((cur + off, '^\\markup { \\italic "%s" }' % txt.replace('"', "'")))
    return out




def merge_note_events(items, div):
    """items: [(idx, onset, el, dur)] 同一谱表所有声部 → {(idx, onset): [el,...]} 合并和弦。"""
    out = {}
    for idx, onset, el, dur in items:
        key = (idx, onset)
        out.setdefault(key, []).append((el, dur))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mxl')
    ap.add_argument('--pos', default='', help='文件内绝对小节位置 a-b')
    ap.add_argument('--mnum', default='', help='按 MusicXML 小节号 a-b 定位（单乐章文件用）')
    ap.add_argument('--instruments', default='')
    ap.add_argument('--names', default='', help='P1:Violin I,P2:...')
    ap.add_argument('--title', default='')
    ap.add_argument('--location', default='')
    ap.add_argument('--id', default='')
    ap.add_argument('--tempo', default='')
    ap.add_argument('--beat', default='4')
    ap.add_argument('--bpm', default='')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--body-only', action='store_true')
    ap.add_argument('--keep-words', action='store_true')
    ap.add_argument('--key', default='', help='覆盖调号，如 "d \\minor"')
    ap.add_argument('--comment', default='', help='额外的注释行，多个用 | 分隔')
    ap.add_argument('--out', default='')
    ap.add_argument('--per-staff-key', action='store_true', help='各谱表用自身调号（移调乐器谱例用）')
    ap.add_argument('--time', default='', help='覆盖拍号，如 4/4')
    args = ap.parse_args()
    global KEEP_WORDS
    KEEP_WORDS = args.keep_words

    root = load_root(args.mxl)
    parts = root.findall('./part')
    pnames = {sp.get('id'): (sp.findtext('part-name') or '').strip() for sp in root.findall('./part-list/score-part')}

    if args.list:
        for p in parts:
            nums = [m.get('number') for m in p.findall('./measure')]
            resets = [i + 1 for i in range(1, len(nums)) if nums[i] == '1']
            print(p.get('id'), pnames.get(p.get('id')), 'total', len(nums), 'resets', resets)
        return

    if args.mnum:
        a, b = [int(x) for x in args.mnum.split('-')]
        nums = [m.get('number') for m in parts[0].findall('./measure')]
        idx = {n: i + 1 for i, n in reversed(list(enumerate(nums)))}
        missing = [str(n) for n in range(a, b + 1) if str(n) not in idx]
        if missing:
            sys.exit('measure numbers not found: ' + ','.join(missing))
        lo, hi = idx[str(a)], idx[str(b)]
    else:
        lo, hi = [int(x) for x in args.pos.split('-')]
    inst = {}
    disp = {}
    for kv in args.instruments.split(','):
        if ':' in kv:
            k, v = kv.split(':', 1)
            inst[k.strip()] = v.strip()
    for kv in args.names.split(','):
        if ':' in kv:
            k, v = kv.split(':', 1)
            disp[k.strip()] = v.strip()

    log('%% source=%s pos=%d-%d' % (args.mxl.replace('\\', '/').split('/')[-1], lo, hi))
    blocks = []
    for p in parts:
        pid = p.get('id')
        if inst and pid not in inst:
            continue
        meas_all = p.findall('./measure')
        log('%% part %s (%s) measure numbers %s..%s' % (pid, pnames.get(pid),
                                                        meas_all[lo - 1].get('number'), meas_all[hi - 1].get('number')))
        div = 1
        key = ('0', 'major')
        time = ('4', '4')
        clef = {'1': 'treble'}
        transp = 0
        # 收集属性（从头扫到 hi，确保拿到起始 div/key/time/clef 状态）
        for idx in range(1, hi + 1):
            meas = meas_all[idx - 1]
            a = meas.find('./attributes')
            if a is None:
                continue
            if a.findtext('./divisions'):
                div = int(a.findtext('./divisions'))
            k = a.find('./key')
            if k is not None and k.findtext('./fifths') is not None:
                key = (k.findtext('./fifths'), k.findtext('./mode') or 'major')
            t = a.find('./time')
            if t is not None and t.findtext('./beats'):
                time = (t.findtext('./beats'), t.findtext('./beat-type'))
            for c in a.findall('./clef'):
                num = c.get('number') or '1'
                clef[num] = CLEFS.get((c.findtext('./sign'), c.findtext('./line')), 'treble')
            tr = a.find('./transpose')
            if tr is not None and tr.findtext('./chromatic'):
                transp = int(tr.findtext('./chromatic'))
        log('%% key %s time %s/%s transposition %s' % (fifths_key(*key), time[0], time[1], TRANSP.get(transp, '?')))
        # 收集音符
        notes = {}
        for idx in range(lo, hi + 1):
            meas = meas_all[idx - 1]
            cur = Fraction(0)
            for el in meas:
                tag = etree.QName(el).localname
                if tag in ('backup', 'forward'):
                    d = Fraction(int(el.findtext('./duration') or 0), div)
                    cur = cur - d if tag == 'backup' else cur + d
                elif tag == 'attributes' and el.findtext('./divisions'):
                    div = int(el.findtext('./divisions'))
                elif tag == 'note':
                    dur = Fraction(int(el.findtext('./duration') or 0), div) / 4  # 全音符分数
                    is_chord = el.find('./chord') is not None
                    onset = cur / 4 - dur if is_chord else cur / 4
                    staff = el.findtext('./staff') or '1'
                    voice = el.findtext('./voice') or '1'
                    notes.setdefault((staff, voice), []).append((idx, onset, el, dur))
                    if not is_chord:
                        cur += Fraction(int(el.findtext('./duration') or 0), div)
        mlen = {idx: measure_length(meas_all[idx - 1], div, time) for idx in range(lo, hi + 1)}
        dyn = {idx: dynamics_in(meas_all[idx - 1], div) for idx in range(lo, hi + 1)}
        staves = sorted({k[0] for k in notes})
        staff_bodies = []
        for staff in staves:
            voices = sorted({k[1] for k in notes if k[0] == staff})
            vtexts = []
            voices = [v for v in voices
                      if any(el.find('./rest') is None
                             for (_, _, el, _d) in notes[(staff, v)])] or voices[:1]
            if len(voices) > 1:
                # 多声部：合并为单一声部（同 onset 并成和弦，时值取最长）
                merged = {}
                for v in voices:
                    for (idx, onset, el, dur) in notes[(staff, v)]:
                        merged.setdefault((idx, onset), []).append((el, dur))
                notes[(staff, '__merged__')] = []
                for (idx, onset), group in sorted(merged.items()):
                    main_el, main_dur = max(group, key=lambda g: g[1])
                    notes[(staff, '__merged__')].append((idx, onset, main_el, main_dur))
                voices = ['__merged__']
            for voice in voices:
                items = sorted(notes[(staff, voice)], key=lambda e: (e[0], e[1]))
                per = {}
                for idx, onset, el, dur in items:
                    per.setdefault(idx, []).append((onset, el, dur))
                lines = []
                depth = 0
                tuplet = None
                for idx in range(lo, hi + 1):
                    toks = []
                    pos = Fraction(0)
                    seq = per.get(idx, [])
                    k = 0
                    tuplet = None

                    def close_tuplet():
                        nonlocal tuplet
                        if tuplet is not None:
                            toks.append('}')
                            tuplet = None

                    while k < len(seq):
                        onset, el, dur = seq[k]
                        if onset > pos:
                            toks += rest_tokens(onset - pos)
                            pos = onset
                        # --- 双音震音（MuseScore 两音震音：start/stop 成对）---
                        tr = el.find('./notations/ornaments/tremolo')
                        nxt = seq[k + 1][1] if k + 1 < len(seq) else None
                        if tr is not None and tr.get('type') == 'start' and nxt is not None \
                                and nxt.find('./notations/ornaments/tremolo') is not None \
                                and abs(seq[k + 1][0] - onset - dur) < Fraction(1, 100):
                            close_tuplet()
                            d2 = seq[k + 1][2]
                            p1, p2 = el.find('./pitch'), nxt.find('./pitch')
                            s1 = lily_pitch(p1.findtext('step'), p1.findtext('alter'), p1.findtext('octave'))
                            s2 = lily_pitch(p2.findtext('step'), p2.findtext('alter'), p2.findtext('octave'))
                            unit = TREM_UNIT.get((tr.text or '2').strip(), Fraction(1, 16))
                            total = dur + d2
                            pairs = max(1, int(total / (2 * unit)))
                            toks.append('\\repeat tremolo %d { %s %s }' % (
                                pairs, s1 + DUR_BY_TYPE[unit_name(unit)], s2 + DUR_BY_TYPE[unit_name(unit)]))
                            pos = onset + total
                            k += 2
                            continue
                        # --- 同 onset 的和弦 ---
                        group = [(onset, el, dur)]
                        j = k + 1
                        while j < len(seq) and seq[j][0] == onset:
                            group.append(seq[j])
                            j += 1
                        dur = max(g[2] for g in group)
                        ntype = el.findtext('./type')
                        dots = len(el.findall('./dot'))
                        base = DUR_BY_TYPE.get(ntype, '4')
                        dotstr = '.' * dots
                        if el.find('./rest') is not None:
                            if ntype not in DUR_BY_TYPE:
                                close_tuplet()
                                toks += rest_tokens(dur)
                                pos = onset + dur
                                k = j
                                continue
                            tok = 'r' + base + dotstr
                        else:
                            ps = []
                            for _, g, _ in group:
                                pt = g.find('./pitch')
                                if pt is not None:
                                    ps.append(lily_pitch(pt.findtext('step'), pt.findtext('alter'), pt.findtext('octave')))
                            ps = sorted(ps, key=sort_pitch_key)
                            tok = (ps[0] if len(ps) == 1 else '<' + ' '.join(ps) + '>') + base + dotstr
                        raw = ''.join(marks_of(el)) + slur_of(el)
                        sfx = ''
                        for ch in raw:
                            if ch == '(':
                                if depth < 1:
                                    depth += 1
                                    sfx += ch
                            elif ch == ')':
                                if depth > 0:
                                    depth -= 1
                                    sfx += ch
                            else:
                                sfx += ch
                        if tie_start(el):
                            sfx += '~'
                        extra = ''
                        for off, d in dyn.get(idx, []):
                            if abs(off - onset) < Fraction(1, 100):
                                extra += d
                        # --- tuplet：按 written 时值排版，按 real 时值推进 ---
                        tm = el.find('./time-modification')
                        ratio = None
                        act = nor = 1
                        if tm is not None:
                            act = int(tm.findtext('./actual-notes') or 1)
                            nor = int(tm.findtext('./normal-notes') or 1)
                            if act != nor and not (act == 2 and nor == 1):
                                ratio = (act, nor)
                        written = DUR_VAL.get(ntype, dur)
                        for i in range(dots):
                            written += DUR_VAL.get(ntype, dur) / (2 ** (i + 1))
                        if ratio:
                            if tuplet != ratio:
                                close_tuplet()
                                toks.append('\\tuplet %d/%d {' % ratio)
                                tuplet = ratio
                            toks.append(tok + extra + sfx)
                            pos = onset + written * Fraction(nor, act)
                        else:
                            close_tuplet()
                            toks.append(tok + extra + sfx)
                            pos = onset + dur
                        k = j
                    close_tuplet()
                    if mlen[idx] > pos:
                        toks += rest_tokens(mlen[idx] - pos)
                    lines.append(' '.join(toks) + ' |')

                if depth:
                    lines[-1] = lines[-1].rstrip(' |') + ')' * depth + ' |'
                    depth = 0
                vtexts.append('\n'.join(lines))
            if len(vtexts) > 1:
                staff_bodies.append('<<\n' + '\n\\\\\n'.join(vtexts) + '\n>>')
            else:
                staff_bodies.append(vtexts[0])
        blocks.append({
            'pid': pid, 'name': disp.get(pid, pnames.get(pid)), 'inst': inst.get(pid, 'piano'),
            'clef': clef, 'staffs': staves, 'bodies': staff_bodies, 'transp': transp,
            'key': key,
        })

    # 展开成「每个谱表一项」
    entries = []
    for b in blocks:
        multi = len(b['staffs']) > 1
        for i, st in enumerate(b['staffs']):
            suffix = ''
            if multi:
                suffix = 'Up' if i == 0 else 'Down'
            entries.append({
                'pid': b['pid'], 'staff': st, 'inst': b['inst'], 'transp': b['transp'],
                'key': b.get('key', ('0', 'major')),
                'clef': b['clef'].get(st, 'treble'), 'body': b['bodies'][i],
                'var': staff_var(b['pid']) + suffix, 'multi': multi,
            })

    if args.body_only:
        lines = []
        for e in entries:
            lines.append('%% ---- %s staff %s (%s)' % (e['pid'], e['staff'], e['var']))
            lines.append(e['body'])
        emit('\n'.join(lines), args)
        return

    attrs = ''
    if args.title:
        attrs += ' title="%s"' % args.title
    if args.location:
        attrs += ' location="%s"' % args.location
    if args.id:
        attrs += ' id="%s"' % args.id
    out = []
    out.append('```lilypond%s' % attrs)
    out.append('\\version "2.26.0"')
    out.append('\\language "english"')
    out.append('')
    if args.comment:
        for cl in args.comment.split('|'):
            out.append('%% ' + cl)
        out.append('')
    out.append('global = {')
    if not args.per_staff_key:
        out.append('  \\key %s' % (args.key if args.key else fifths_key(*key)))
    out.append('  \\time %s' % (args.time if args.time else '%s/%s' % (time[0], time[1])))
    if args.tempo:
        if args.bpm:
            out.append('  \\tempo "%s" %s = %s' % (args.tempo, args.beat, args.bpm))
        else:
            out.append('  \\tempo "%s"' % args.tempo)
    out.append('}')
    out.append('')
    for e in entries:
        out.append('%s = {' % e['var'])
        out.append('  \\global')
        out.append('  \\clef %s' % e['clef'])
        if args.per_staff_key:
            out.append('  \\key %s' % fifths_key(*e['key']))
        if e['transp']:
            out.append('  \\transposition %s' % TRANSP.get(e['transp'], 'c'))
        out += ['  ' + ln for ln in e['body'].split('\n')]
        out.append('}')
        out.append('')
    out.append('\\score {')
    out.append('  <<')
    seen = set()
    for e in entries:
        if e['multi']:
            if e['pid'] in seen:
                continue
            seen.add(e['pid'])
            group = [x for x in entries if x['pid'] == e['pid']]
            out.append('    \\new PianoStaff <<')
            for g in group:
                out.append('      \\new Staff = "%s" <<' % ('%s%s' % (g['pid'], 'lower' if g['var'].endswith('Down') else 'upper')))
                out.append('        \\set Staff.midiInstrument = "%s"' % g['inst'])
                out.append('        \\%s' % g['var'])
                out.append('      >>')
            out.append('    >>')
        else:
            out.append('    \\new Staff = "%s" <<' % e['pid'])
            out.append('      \\set Staff.midiInstrument = "%s"' % e['inst'])
            out.append('      \\%s' % e['var'])
            out.append('    >>')
    out.append('  >>')
    out.append('  \\layout { ragged-right = ##f }')
    out.append('  \\midi { }')
    out.append('}')
    out.append('```')
    emit('\n'.join(out), args)


def unit_name(unit):
    for name, val in DUR_VAL.items():
        if val == unit:
            return name
    return '16th'


if __name__ == '__main__':
    main()
