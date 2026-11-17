"""S3 第二批核验：**kern 与 LilyPond 独立解析 + 逐音比对。

依据：
- **kern 规范（https://www.humdrum.org/rep/kern/）：八度只由字母大小写与字母重复决定；
  撇号 ' 是 staccato 记号，不改变音高。
- LilyPond english 音名：裸字母 = C3 所在八度，' 升一个八度，, 降一个八度。
"""
import re

PC = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}
NAMES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']


def nm(midi):
    return f"{NAMES[midi % 12]}{midi // 12 - 1}"


# ------------------------------------------------------------------ kern
def kern_dur(tok, prev):
    """kern token -> 四分音符为单位的时值（无时值数字则继承 prev）"""
    t = tok
    while t and t[0] in '[({':
        t = t[1:]
    m = re.match(r'^(\d+)(\.*)', t)
    if not m:
        return prev
    num, dots = m.group(1), len(m.group(2))
    if num == '0':
        base = 8.0
    elif num == '00':
        base = 16.0
    elif num == '000':
        base = 32.0
    else:
        base = 4.0 / int(num)
    if dots:
        f, add = 1.0, 1.0
        for _ in range(dots):
            add *= 0.5
            f += add
        base *= f
    return base


def kern_note(tok):
    """单音 token -> ('rest',) 或 (midi, tie_start, tie_end, tie_cont) 或 None"""
    t = tok
    while t and t[0] in '[({':
        t = t[1:]
    m = re.match(r'^(\d+)(\.*)', t)
    if m:
        t = t[m.end():]
    if not t:
        return None
    if t[0] == 'r':
        return ('rest',)
    mm = re.match(r'([a-gA-G]+)([#\-n]*)', t)
    if not mm:
        return None
    letters, acc = mm.group(1), mm.group(2)
    k = len(letters)
    letter = letters[0].lower()
    octv = 4 + (k - 1) if letters[0].islower() else 4 - k
    midi = 12 * (octv + 1) + PC[letter]
    midi += acc.count('#') - acc.count('-')
    return (midi, '[' in tok, ']' in tok, '_' in tok)


def parse_kern(path):
    """-> (voices {idx: [(meas, midi|None, dur, ts, te, tc)]}, kinds, labels)"""
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    n = None
    kinds = None
    voices = {}
    prev_dur = {}
    labels = None
    meas = 0
    for ln in lines:
        if not ln.strip() or ln.startswith('!!'):
            continue
        if ln.startswith('**'):
            p = ln.split('\t')
            kinds = [x[2:] if x.startswith('**') else x for x in p]
            n = len(p)
            for i in range(n):
                voices[i] = []
                prev_dur[i] = None
            continue
        if n is None:
            continue
        parts = ln.split('\t')
        if parts[0].startswith('!'):
            labels = parts
            continue
        if ln.startswith('*'):
            continue
        if parts[0].startswith('='):
            m = re.match(r'=(\d+)', parts[0])
            if m:
                meas = int(m.group(1))
            continue
        if len(parts) != n:
            continue
        for i, tok in enumerate(parts):
            if kinds[i] != 'kern' or tok == '.':
                continue
            d = kern_dur(tok, prev_dur[i] if prev_dur[i] is not None else 1.0)
            prev_dur[i] = d
            for sub in tok.split(' '):
                p = kern_note(sub)
                if p is None:
                    continue
                if p[0] == 'rest':
                    voices[i].append((meas, None, d, False, False, False))
                else:
                    mi, ts, te, tc = p
                    voices[i].append((meas, mi, d, ts, te, tc))
    return voices, kinds, labels


def kern_stream(kern_notes):
    """合并 tie，返回 (onset, midi|None, dur, measure)；onset 以四分音符累计"""
    out = []
    pos = 0.0
    for meas, midi, dur, ts, te, tc in kern_notes:
        if (te or tc) and out and out[-1][1] == midi and out[-1][4]:
            out[-1][2] += dur
            out[-1][4] = False
            pos += dur
            continue
        out.append([pos, midi, dur, meas, ts])
        pos += dur
    return out


# ------------------------------------------------------------- LilyPond
NOTE = re.compile(r"([a-g])((?:s|f){0,2})([',]*)(\d+)(\.*)")
# 和弦内部的音可以不带时值（时值写在整个和弦之后）
NOTE_CH = re.compile(r"([a-g])((?:s|f){0,2})([',]*)(\d+)?(\.*)?")


def ly_note(m, start=0):
    letter, acc, octs, dur, dots = m.groups()
    octv = 3 + octs.count("'") - octs.count(',')
    midi = 12 * (octv + 1) + PC[letter] + acc.count('s') - acc.count('f')
    q = 4.0 / int(dur) if dur else None
    if q is not None:
        for _ in range(len(dots or '')):
            q *= 1.5
    return midi, q


def ly_parse(path):
    src = open(path, encoding='utf-8').read()
    src = re.sub(r'%[^\n]*', '', src)
    vardefs = {}
    for m in re.finditer(r'^(\w+)\s*=\s*\{', src, re.M):
        i = m.end() - 1
        depth, j = 0, i
        while j < len(src):
            if src[j] == '{':
                depth += 1
            elif src[j] == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        vardefs[m.group(1)] = src[i + 1:j]
    out = {}
    for name, body in vardefs.items():
        out[name] = ly_events(body, vardefs)
    return out, vardefs


def ly_events(body, vardefs):
    body = re.sub(r'\\global\b', lambda m: vardefs.get('global', ''), body)
    body = body.replace('\n', ' ')
    ev = []
    i, n = 0, len(body)
    while i < n:
        c = body[i]
        if c.isspace():
            i += 1
            continue
        if c == '|':
            ev.append(('bar',))
            i += 1
            continue
        if c == '~':
            i += 1
            continue
        if c == '<':
            k = body.find('>', i)
            inner = body[i + 1:k]
            j = k + 1
            dur = 0.0
            m = re.match(r'\s*(\d+)(\.*)', body[j:])
            if m:
                dur = 4.0 / int(m.group(1))
                for _ in range(len(m.group(2))):
                    dur *= 1.5
                j += m.end()
            else:
                m2 = NOTE.match(body, j)
                if m2:
                    dur = ly_note(m2)[1]
                    j = m2.end()
            chord = []
            for mm in NOTE_CH.finditer(inner):
                chord.append(ly_note(mm)[0])
            ev.append(('notes', chord, dur))
            i = j
            continue
        if c == '\\':
            m = re.match(r'\\(\w+)', body[i:])
            if not m:
                i += 1
                continue
            cmd = m.group(1)
            j = i + m.end()
            if cmd == 'partial':
                m2 = re.match(r'\s*(\d+)(\.*)', body[j:])
                q = 0.0
                if m2:
                    q = 4.0 / int(m2.group(1))
                    for _ in range(len(m2.group(2))):
                        q *= 1.5
                    j += m2.end()
                ev.append(('partial', q))
            elif cmd == 'bar':
                m2 = re.match(r'\s*"([^"]*)"', body[j:])
                if m2:
                    j += m2.end()
                ev.append(('bar',))
            elif cmd == 'time':
                m2 = re.match(r'\s*(\S+)', body[j:])
                if m2:
                    ev.append(('time', m2.group(1)))
                    j += m2.end()
            elif cmd == 'key':
                m2 = re.match(r'\s*([a-g][sf]?)\s*\\(\w+)', body[j:])
                if m2:
                    ev.append(('key', m2.group(1), m2.group(2)))
                    j += m2.end()
                else:
                    j = body.find(' ', j) if body.find(' ', j) > 0 else n
            elif cmd == 'tempo':
                m2 = re.match(r'\s*("([^"]*)"|\S+)?\s*(\d+)?\s*=\s*(\d+)?', body[j:])
                if m2:
                    ev.append(('tempo', (m2.group(2) or m2.group(1) or '').strip(),
                               int(m2.group(4)) if m2.group(4) else None))
                    j += m2.end()
            elif cmd == 'clef':
                m2 = re.match(r'\s*(\w+)', body[j:])
                if m2:
                    ev.append(('clef', m2.group(1)))
                    j += m2.end()
            elif cmd == 'set':
                m2 = re.match(r'\s*\S+\s*=\s*#?\d+', body[j:])
                if m2:
                    j += m2.end()
                    ev.append(('set', body[m2.start():m2.end()].strip()))
            i = j
            continue
        if c in 'rRs':
            m = re.match(r'r(\d+)(\.*)', body[i:])
            if m:
                q = 4.0 / int(m.group(1))
                for _ in range(len(m.group(2))):
                    q *= 1.5
                ev.append(('rest', q))
                i += m.end()
                continue
            i += 1
            continue
        m = NOTE.match(body, i)
        if m:
            midi, q = ly_note(m)
            ev.append(('notes', [midi], q))
            i = m.end()
            continue
        i += 1
    return ev


def ly_stream(ev):
    """-> ([(onset, midi, dur, bar_index_of_start)], bars[onset列表], partials)"""
    out = []
    bars = []
    partials = []
    pos = 0.0
    for e in ev:
        if e[0] == 'bar':
            bars.append(pos)
        elif e[0] == 'partial':
            partials.append(e[1])
        elif e[0] == 'rest':
            pos += e[1]
        elif e[0] == 'notes':
            for midi in e[1]:
                out.append([pos, midi, e[2], len(bars)])
            pos += e[2]
    return out, bars, partials


# ------------------------------------------------- 供 compare2 使用的 token 级解析
def parse_kern_tokens(path):
    """-> (tokens {spine: [ {meas, pitches:[midi|None], dur, ts, te, tc} ]}, kinds, labels)"""
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    n = None
    kinds = None
    toks = {}
    prev_dur = {}
    pos = {}
    labels = None
    meas = 0
    for ln in lines:
        if not ln.strip() or ln.startswith('!!'):
            continue
        if ln.startswith('**'):
            p = ln.split('\t')
            kinds = [x[2:] if x.startswith('**') else x for x in p]
            n = len(p)
            for i in range(n):
                toks[i] = []
                prev_dur[i] = None
                pos[i] = 0.0
            continue
        if n is None:
            continue
        parts = ln.split('\t')
        if parts[0].startswith('!'):
            labels = parts
            continue
        if ln.startswith('*'):
            continue
        if parts[0].startswith('='):
            m = re.match(r'=(\d+)', parts[0])
            if m:
                meas = int(m.group(1))
            continue
        if len(parts) != n:
            continue
        for i, tok in enumerate(parts):
            if kinds[i] != 'kern' or tok == '.':
                continue
            d = kern_dur(tok, prev_dur[i] if prev_dur[i] is not None else 1.0)
            prev_dur[i] = d
            pitches = []
            for sub in tok.split(' '):
                p = kern_note(sub)
                if p is None:
                    continue
                pitches.append(None if p[0] == 'rest' else p[0])
            if not pitches:
                continue
            toks[i].append(dict(meas=meas, onset=pos[i], pitches=pitches, dur=d,
                                ts='[' in tok, te=']' in tok, tc='_' in tok))
            pos[i] = round(pos[i] + d, 8)
    return toks, kinds, labels


def kern_stream2(tokens):
    """tie 合并后的发声事件（休止保留为 pitches=[None]）"""
    out = []
    for t in tokens:
        p = t['pitches']
        if (t['te'] or t['tc']) and out and out[-1]['pitches'] == p and out[-1]['open']:
            out[-1]['dur'] += t['dur']
            out[-1]['open'] = False
            continue
        out.append(dict(onset=t['onset'], pitches=list(p), dur=t['dur'],
                        meas=t['meas'], open=t['ts']))
    return out


def kern_measure_onsets(tokens):
    """{measure: 该小节第一个 token 的起点}"""
    m = {}
    for t in tokens:
        m.setdefault(t['meas'], t['onset'])
    return m
