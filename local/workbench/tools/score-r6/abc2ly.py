#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""abc2ly (score-r6): 把 hum2abc（Craig Sapp, kern->ABC）转出的多声部 ABC 解析成 LilyPond。

为什么不用 abc2ly.py：LilyPond 自带的 abc2ly 对这些文件会把每小节拆成 cadenza measure、
丢掉拍号与和弦力度，无法用于知识库围栏。本工具只覆盖这批语料真正出现的语法：
L/M/K/Q 头字段、[V:n] 分轨、[K:clef=...] 换谱号、[I:setbarnb N] 小节号、
数字/斜杠时值、点、连音线 -、圆括号连奏、>&< 破节奏、[] 和弦、& 层叠、z/x 休止、
!装饰!/./{} 装饰音、^^/__/^/_/= 临时记号，并维护 ABC 的临时记号状态（按字母+八度，过小节线重置）。

用法：
  python abc2ly.py --abc <file.abc> [--measures 5-8] [--dump] [--json out.json]

--dump 输出每小节的音高多重集（MIDI 号），用于与 MusicXML 独立底本回比对。
"""
import argparse
import json
import re
import sys
from fractions import Fraction

LETTERS = "CDEFGAB"
SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
SHARP_ORDER = ["F", "C", "G", "D", "A", "E", "B"]
FLAT_ORDER = ["B", "E", "A", "D", "G", "C", "F"]

MAJOR_SIG = {
    "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "Fs": 6, "Cs": 7,
    "F": -1, "Bf": -2, "Ef": -3, "Af": -4, "Df": -5, "Gf": -6, "Cf": -7,
}
MINOR_SIG = {
    "A": 0, "E": 1, "B": 2, "Fs": 3, "Cs": 4, "Gs": 5, "Ds": 6,
    "D": -1, "G": -2, "C": -3, "F": -4, "Bf": -5, "Ef": -6, "Af": -7,
}

DECOS = {
    "trill": r"\trill", "trill^": r"\trill", "mordent": r"\mordent",
    "pralltriller": r"\mordent", "turn": r"\turn", "arpeggio": r"\arpeggio",
    "fermata": r"\fermata", "accent": r"\accent", "staccato": r"\staccato",
    "tenuto": r"\tenuto", "downbow": r"\downbow", "upbow": r"\upbow",
    "snap": r"\snappizzicato", "breath": r"\breathe",
}

# ---------------------------------------------------------------- durations


def dur_to_ly(frac, force=None):
    """Fraction(whole-note) -> LilyPond 时值串（含附点）。"""
    dur = frac
    if dur <= 0:
        raise ValueError("non-positive duration")
    for dots in range(4):
        factor = sum(Fraction(1, 2 ** i) for i in range(dots + 1))  # 1, 3/2, 7/4 ...
        for denom in (1, 2, 4, 8, 16, 32, 64, 128):
            if dur == Fraction(1, denom) * factor:
                return str(denom) + "." * dots
    raise ValueError("无法表示的时值: %s" % frac)


# ---------------------------------------------------------------- pitch


def key_signature(keyname):
    """'A' / 'Am' / 'Bf' / 'Fs' -> (tonic_display, mode, {letter: alter})"""
    k = keyname.strip()
    m = re.match(r"^([A-G])([#b]?)(m|min|major|maj)?$", k)
    if not m:
        raise ValueError("无法解析调号: %r" % keyname)
    letter, acc, mode = m.group(1), m.group(2) or "", m.group(3) or ""
    key = letter + ("s" if acc == "#" else "f" if acc == "b" else "")
    is_minor = mode.startswith("m")
    table = MINOR_SIG if is_minor else MAJOR_SIG
    if key not in table:
        raise ValueError("未登记的调号: %r" % keyname)
    n = table[key]
    sig = {}
    if n > 0:
        for i in range(n):
            sig[SHARP_ORDER[i]] = 1
    elif n < 0:
        for i in range(-n):
            sig[FLAT_ORDER[i]] = -1
    tonic = letter.lower() + {"": "", "s": "s", "f": "f"}[acc]
    return tonic, "minor" if is_minor else "major", sig


def ly_pitch(letter, alter, octave):
    """ABC 音高 -> LilyPond 绝对音高。ABC octave: 大写=4，小写=5，,/-1 ' /+1。
    LilyPond: c' = C4，故记谱八度 = ABC octave - 1，撇号数 = 记谱八度 - 3。"""
    name = letter.lower()
    if alter == 2:
        name += "ss"
    elif alter == 1:
        name += "s"
    elif alter == -1:
        name += "f"
    elif alter == -2:
        name += "ff"
    elif alter != 0:
        raise ValueError("不支持的变音数 %d" % alter)
    marks = octave - 3          # LilyPond: c' = C4（实测 MIDI 60）
    if marks > 0:
        name += "'" * marks
    elif marks < 0:
        name += "," * (-marks)
    return name


# ---------------------------------------------------------------- lexer


TOKEN_RE = re.compile(
    r"""
    (?P<field>\[(?:[VKLMIQPTW]:)[^\]]*\])         # 行内字段
    |(?P<bar>(?:\:\|\]|\|\:\||\|\]|\|\:|\:\:|\|\||\[\||\|))   # 小节线
    |(?P<chord>\[)                                # 和弦开始
    |(?P<chordend>\])
    |(?P<grace>\{[^}]*\})                         # 装饰音组
    |(?P<deco>![^!]*!)                            # !trill! 等
    |(?P<overlay>&)                               # 层叠
    |(?P<tuplet>\(\d*(?::\d*(?::\d*)?)?)          # 连音
    |(?P<slur>[()])                               # 连奏线
    |(?P<tie>-)
    |(?P<anno>[\^_]"(?:[^"]*)")                   # 文字注解
    |(?P<rest>[zxZ])(?P<rdur>\d*(?:/\d*)*)
    |(?P<acc>\^{1,2}|_{1,2}|=)
    |(?P<note>[A-Ga-g])(?P<oct>[',]*)(?P<ndur>\d*(?:/\d*)*)(?P<broken>[<>]+)?
    |(?P<dot>\.)
    |(?P<broken2>[<>]+)
    |(?P<ws>\s+)
    """,
    re.X,
)


class Measure(object):
    def __init__(self, number):
        self.number = number
        self.layers = [[]]      # list of layers; each layer = list of event str
        self.clef_changes = []  # (layer_index, clef)
        self.duration = [Fraction(0)] * 1

    def add(self, ev):
        self.layers[-1].append(ev)


def parse_duration(txt, L, default=1):
    """ABC 时值后缀 -> Fraction(whole note)。"""
    if not txt:
        return L * default
    m = re.match(r"^(\d*)((?:/\d*)*)$", txt)
    if not m:
        raise ValueError("坏时值 %r" % txt)
    num, slashes = m.group(1), m.group(2)
    n = int(num) if num else 1
    if slashes:
        parts = slashes.split("/")[1:]
        if len(parts) == 1 and parts[0] == "":
            div = 2
        elif len(parts) == 1 and parts[0].isdigit():
            div = int(parts[0])
        else:
            div = 2 ** len(parts)
        return L * Fraction(n, div)
    return L * n


class Voice(object):
    def __init__(self, name, clef, key_sig):
        self.name = name
        self.clef = clef
        self.measures = []
        self.pending_acc = {}   # (letter, octave) -> alter, reset per bar
        self.key_sig = key_sig
        self.tuplet = None
        self.pending_shrink = None
        self.bar_number = None
        self.start_bar = 1

    def new_measure(self):
        n = self.bar_number if self.bar_number is not None else (
            self.measures[-1].number + 1 if self.measures else self.start_bar)
        self.measures.append(Measure(n))
        # [I:setbarnb] 指定下一小节号后只生效一次
        self.bar_number = None

    def cur(self):
        if not self.measures:
            self.new_measure()
        return self.measures[-1]


def parse_abc(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        raw = fh.read().splitlines()

    header = {}
    key_raw = None
    L = Fraction(1, 16)
    meter = None
    tempo = None
    voices = {}
    voice_order = []
    cur_voice = None
    start_bar = 1
    first_music = True

    for line in raw:
        s = line.rstrip()
        if not s.strip():
            continue
        m = re.match(r"^%%setbarnb\s+(\d+)", s)
        if m:
            start_bar = int(m.group(1))
            continue
        if s.startswith("%%"):
            continue
        m = re.match(r"^([A-Za-z]):\s*(.*)$", s)
        if m and not s.startswith("["):
            f, v = m.group(1), m.group(2)
            if f == "L":
                a, b = v.split("/")
                L = Fraction(int(a), int(b))
                if cur_voice is not None:
                    pass
                header["L"] = v
            elif f == "M":
                meter = v
                header["M"] = v
            elif f == "K":
                key_raw = v.split()[0] if v.split() else v
                header["K"] = v
            elif f == "Q":
                tempo = v
                header["Q"] = v
            elif f == "V":
                mm = re.match(r"^(\d+)\s*(?:clef=(\w+))?", v)
                vn = mm.group(1)
                clef = mm.group(2) or "treble"
                if vn not in voices:
                    voices[vn] = Voice(vn, clef, {})
                    voice_order.append(vn)
                else:
                    voices[vn].clef = clef
            elif f in ("X", "T", "C", "N", "P", "U", "W", "O", "R", "S", "B", "D", "E", "F", "G", "H", "I", "J"):
                header[f] = v
            continue

        if key_raw is None:
            continue
        if not voices:
            voices["1"] = Voice("1", "treble", {})
            voice_order.append("1")
        tonic, mode, sig = key_signature(key_raw)
        for vn in voices:
            if not voices[vn].key_sig:
                voices[vn].key_sig = sig

        # 音乐行：[V:n] 开头（可能带行内字段）
        body = s
        mv = re.match(r"^\[V:(\d+)\]\s*", body)
        if mv:
            cur_voice = voices[mv.group(1)]
            body = body[mv.end():]
        if cur_voice is None:
            continue
        if first_music:
            for vn in voice_order:
                voices[vn].start_bar = start_bar
            first_music = False

        parse_voice_body(cur_voice, body, L)

    tonic, mode, sig = key_signature(key_raw or "C")
    for vn in voice_order:
        if not voices[vn].key_sig:
            voices[vn].key_sig = sig
    return {
        "header": header, "tonic": tonic, "mode": mode, "key_sig": sig,
        "L": L, "meter": meter, "tempo": tempo,
        "voices": voices, "order": voice_order,
    }


def parse_voice_body(voice, body, L):
    pos = 0
    pending_deco = []
    prefix_acc = None
    last_note_ev = None   # (layer idx, event list ref) 用于破节奏
    while pos < len(body):
        m = TOKEN_RE.match(body, pos)
        if not m:
            raise ValueError("无法解析 %r ... 于 %r" % (body[pos:pos + 12], body))
        pos = m.end()
        if m.group("field"):
            fld = m.group("field")[1:-1]
            name, val = fld.split(":", 1)
            if name == "K":
                mm = re.search(r"clef=(\w+)", val)
                if mm:
                    voice.cur().clef_changes.append(
                        [len(voice.cur().layers) - 1, len(voice.cur().layers[-1]), mm.group(1)])
                    voice.clef = mm.group(1)
            elif name == "I":
                mm = re.search(r"setbarnb\s+(\d+)", val)
                if mm:
                    voice.bar_number = int(mm.group(1))
            continue
        if m.group("bar"):
            # 把连续的重复/终止小节线并成一条（如 ":|]|:"），避免多造空小节
            end = m.end()
            while end < len(body) and body[end] in "|:":
                end += 1
            pos = end
            voice.new_measure()
            voice.pending_acc = {}
            voice.pending_shrink = None
            voice.tuplet = None
            last_note_ev = None
            continue
        if m.group("ws"):
            continue
        if m.group("deco"):
            txt = m.group("deco")[1:-1]
            if txt in DECOS:
                pending_deco.append(DECOS[txt])
            continue
        if m.group("grace"):
            continue
        if m.group("tuplet"):
            txt = m.group("tuplet")[1:]
            parts = txt.split(":")
            p = int(parts[0]) if parts[0] else 3
            q = int(parts[1]) if len(parts) > 1 and parts[1] else 2
            if p in (5, 6, 7):
                q = 3
            elif p in (8, 9):
                q = 4
            voice.tuplet = [p, q, p]
            continue
        if m.group("slur"):
            voice.cur().add(m.group("slur"))
            continue
        if m.group("overlay"):
            meas = voice.cur()
            meas.layers.append([])
            meas.duration.append(Fraction(0))
            last_note_ev = None
            continue
        if m.group("anno"):
            continue
        if m.group("dot"):
            pending_deco.append(r"\staccato")
            continue
        if m.group("chord"):
            # 读整个和弦
            end = body.find("]", pos)
            if end < 0:
                raise ValueError("未闭合和弦: %r" % body[pos:])
            inner = body[pos:end]
            pos = end + 1
            notes = []
            ties = []
            dur = None
            p = 0
            while p < len(inner):
                if inner[p] in " \t":
                    p += 1
                    continue
                if inner[p] == "-":
                    # 和弦内的连音线：只有全部音都连时才写成和弦连音线
                    ties.append(len(notes) - 1)
                    p += 1
                    continue
                mm = re.match(r"(\^{1,2}|_{1,2}|=)?([A-Ga-g])([',]*)(\d*(?:/\d*)*)", inner[p:])
                if not mm:
                    raise ValueError("和弦内无法解析 %r" % inner[p:])
                p += mm.end()
                acc, letter, octs, dtxt = mm.group(1), mm.group(2), mm.group(3), mm.group(4)
                d = parse_duration(dtxt, L)
                if dur is None:
                    dur = d
                pitch = resolve_pitch(voice, letter, octs, acc)
                notes.append(pitch)
            if getattr(voice, "pending_shrink", None):
                dur = dur * Fraction(1, 2 ** voice.pending_shrink)
                voice.pending_shrink = None
            ev = "<" + " ".join(notes) + ">" + dur_to_ly(dur)
            if notes and len(set(ties)) == len(notes):
                ev += "~"
            for deco in pending_deco:
                ev += deco
            pending_deco = []
            push_event(voice, ev, dur)
            last_note_ev = (voice.cur(), len(voice.cur().layers) - 1)
            continue
        if m.group("rest"):
            letter = m.group("rest")
            d = parse_duration(m.group("rdur") or "1", L)
            if getattr(voice, "pending_shrink", None):
                d = d * Fraction(1, 2 ** voice.pending_shrink)
                voice.pending_shrink = None
            ev = ("s" if letter != "z" else "r") + dur_to_ly(d)
            push_event(voice, ev, d)
            last_note_ev = (voice.cur(), len(voice.cur().layers) - 1)
            continue
        if m.group("note"):
            acc = prefix_acc
            prefix_acc = None
            letter, octs, dtxt, broken = (m.group("note"), m.group("oct"),
                                          m.group("ndur"), m.group("broken"))
            # ABC 破节奏：A>B 表示 A 加长、B 缩短；标记跟在 A 的谱面后面
            d = parse_duration(dtxt, L)
            if getattr(voice, "pending_shrink", None):
                k = voice.pending_shrink
                d = d * Fraction(1, 2 ** k)
                voice.pending_shrink = None
            if broken:
                k = len(broken)
                voice.pending_shrink = k
                d = d * (2 - Fraction(1, 2 ** k))
            pitch = resolve_pitch(voice, letter, octs, acc)
            ev = pitch + dur_to_ly(d)
            for deco in pending_deco:
                ev += deco
            pending_deco = []
            push_event(voice, ev, d)
            last_note_ev = (voice.cur(), len(voice.cur().layers) - 1)
            continue
        if m.group("tie"):
            lay = voice.cur().layers[-1]
            if lay:
                lay[-1] += "~"
            continue
        if m.group("acc"):
            # 独立临时记号，作用于下一个音符
            prefix_acc = m.group("acc")
            continue
        if m.group("chordend"):
            continue
        if m.group("broken2"):
            continue
        raise ValueError("未处理 token: %r" % m.group(0))


def push_event(voice, ev, d_raw):
    """把一个事件压入当前层；若处于连音内，则收集并用 \\tuplet 包裹。"""
    t = getattr(voice, "tuplet", None)
    meas = voice.cur()
    lay = meas.layers[-1]
    if not t:
        lay.append(ev)
        meas.duration[-1] += d_raw
        return
    lay.append(ev)
    meas.duration[-1] += d_raw * Fraction(t[1], t[0])
    t[2] -= 1
    if t[2] <= 0:
        p, q, _ = t
        items = lay[len(lay) - p:]
        del lay[len(lay) - p:]
        lay.append("\\tuplet %d/%d { %s }" % (p, q, " ".join(items)))
        voice.tuplet = None


def apply_broken(ev, k, gain):
    m = re.match(r"^(.*?)(\d+\.*)$", ev)
    if not m:
        return ev
    dur = m.group(2)
    frac_map = {"1": Fraction(1), "2": Fraction(1, 2), "4": Fraction(1, 4),
                "8": Fraction(1, 8), "16": Fraction(1, 16), "32": Fraction(1, 32),
                "64": Fraction(1, 64), "128": Fraction(1, 128)}
    base = dur.rstrip(".")
    dots = len(dur) - len(base)
    val = frac_map[base] * sum(Fraction(1, 2 ** i) for i in range(dots + 1))
    val = val * (Fraction(2) - Fraction(1, 2 ** k)) if gain else val * Fraction(1, 2 ** k)
    return m.group(1) + dur_to_ly(val)


def resolve_pitch(voice, letter, octs, acc):
    """按 ABC 规则算出 (letter, alter, octave) 并维护临时记号状态。"""
    octave = (4 if letter.isupper() else 5)
    octave += octs.count("'") - octs.count(",")
    key_alter = voice.key_sig.get(letter.upper(), 0)
    if acc == "^":
        alter = 1
    elif acc == "^^":
        alter = 2
    elif acc == "_":
        alter = -1
    elif acc == "__":
        alter = -2
    elif acc == "=":
        alter = 0
    else:
        # 按 ABC 2.1：未标变音号的同名同八度音符继承本小节内的临时记号状态。
        # （hum2abc 对偏离调号处一律显式写字号，故两种读法在绝大多数小节一致）
        alter = voice.pending_acc.get((letter.upper(), octave), key_alter)
    voice.pending_acc[(letter.upper(), octave)] = alter
    return ly_pitch(letter.upper(), alter, octave)


def midi_of(lypitch):
    m = re.match(r"^([a-g])(s{0,2}|f{0,2})?(,*)('*)$", lypitch)
    if not m:
        return None
    letter = m.group(1).upper()
    acc = m.group(2) or ""
    alter = acc.count("s") * 1 - acc.count("f") * 1
    octave = 3 + len(m.group(4)) - len(m.group(3))   # LilyPond c' = C4（实测）
    return (octave + 1) * 12 + SEMI[letter] + alter


def measure_pitches(meas):
    """一小节（含层）的音高 MIDI 多重集，忽略休止。"""
    out = []
    for layer in meas.layers:
        for ev in layer:
            if ev.startswith("\\tuplet"):
                inner = ev[ev.index("{") + 1:ev.rindex("}")]
                for tok in inner.split():
                    out.extend(_tok_pitch(tok))
                continue
            out.extend(_tok_pitch(ev))
    return sorted(out)


def _tok_pitch(ev):
    if ev.startswith("<"):
        inner = ev[1:ev.index(">")]
        res = []
        for p in inner.split():
            mm = midi_of(p)
            if mm is not None:
                res.append(mm)
        return res
    if ev and ev[0] in "abcdefg":
        m = re.match(r"^[a-g][sf,']*", ev)
        if m:
            mm = midi_of(m.group(0))
            if mm is not None:
                return [mm]
    return []


# ---------------------------------------------------------------- emit


def emit_voice(voice, first, last):
    """输出 [first,last] 小节的 LilyPond 音符串。"""
    out = []
    for meas in voice.measures:
        if meas.number < first or meas.number > last:
            continue
        parts = []
        for li, layer in enumerate(meas.layers):
            clefs = {c[1]: c[2] for c in meas.clef_changes if c[0] == li}
            evs = []
            for idx, ev in enumerate(layer):
                if idx in clefs:
                    evs.append(r"\clef %s" % clefs[idx])   # 谱号换在本小节内原位置
                evs.append(ev)
            body = " ".join(evs)
            if len(meas.layers) > 1:
                parts.append("{ %s }" % body)
            else:
                parts.append(body)
        if len(parts) > 1:
            out.append("<< " + " \\\\ ".join(parts) + " >>")
        else:
            out.append(parts[0])
    out = [o + " |" for o in out]
    return "\n  ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--abc", required=True)
    ap.add_argument("--measures")
    ap.add_argument("--dump", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--title", default="")
    ap.add_argument("--location", default="")
    ap.add_argument("--id", default="")
    ap.add_argument("--tempo", default=None)
    ap.add_argument("--out")
    args = ap.parse_args()

    data = parse_abc(args.abc)
    first, last = 1, 10 ** 6
    if args.measures:
        a, b = args.measures.split("-")
        first, last = int(a), int(b)

    info = {"voices": {}}
    for vn in data["order"]:
        v = data["voices"][vn]
        info["voices"][vn] = {
            "measures": len(v.measures),
            "first": v.measures[0].number if v.measures else None,
            "last": v.measures[-1].number if v.measures else None,
        }
    if args.dump:
        dump = {"header": data["header"],
                "tonic": data["tonic"], "mode": data["mode"],
                "meter": data["meter"], "voices": {}}
        for vn in data["order"]:
            v = data["voices"][vn]
            dump["voices"][vn] = {str(m.number): measure_pitches(m) for m in v.measures}
        print(json.dumps(dump, ensure_ascii=False, indent=1))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            dump = {"voices": {}}
            for vn in data["order"]:
                v = data["voices"][vn]
                dump["voices"][vn] = {str(m.number): measure_pitches(m) for m in v.measures}
            json.dump(dump, fh, ensure_ascii=False, indent=1)
    if args.out:
        write_fence(data, first, last, args)


def write_fence(data, first, last, args, comment_lines=None):
    tonic = data["tonic"]
    mode = data["mode"]
    meter = (data["meter"] or "")
    if meter in ("C", "C|"):
        meter = "4/4" if meter == "C" else "2/2"
    lines = []
    attrs = 'title="%s" location="%s"' % (args.title, args.location)
    if args.id:
        attrs += ' id="%s"' % args.id
    lines.append("```lilypond " + attrs)
    lines.append('\\version "2.26.0"')
    lines.append('\\language "english"')
    lines.append("")
    for c in (comment_lines or []):
        lines.append("% " + c) if not c.startswith("%") else lines.append(c)
    if comment_lines:
        lines.append("")
    lines.append("global = {")
    lines.append("  \\key %s \\%s" % (tonic, mode))
    if meter:
        lines.append("  \\time %s" % meter)
    if data["tempo"]:
        q = data["tempo"]
        m = re.match(r'^"([^"]*)"\s*(\S*)=(\d+)', q)
        if m:
            unit = {"1/4": "4", "1/8": "8", "1/2": "2", "1/1": "1"}.get(m.group(2), "4")
            lines.append('  \\tempo "%s" %s = %s' % (m.group(1), unit, m.group(3)))
        else:
            lines.append("  \\tempo %s" % q)
    lines.append("}")
    lines.append("")
    clef_override = getattr(args, "clefs", None) or {}
    for vn in data["order"]:
        v = data["voices"][vn]
        name = "upper" if vn == "1" else "lower"
        clef = clef_override.get(vn) or ("treble" if vn == "1" else "bass")
        lines.append("%s = {" % name)
        lines.append("  \\global")
        lines.append("  \\clef %s" % clef)
        lines.append("  \\set Staff.midiInstrument = \"acoustic grand\"")
        lines.append("  " + emit_voice(v, first, last))
        lines.append("}")
        lines.append("")
    lines.append("\\score {")
    lines.append("  \\new PianoStaff <<")
    lines.append('    \\new Staff { \\set Staff.midiInstrument = "acoustic grand" \\upper }')
    lines.append('    \\new Staff { \\set Staff.midiInstrument = "acoustic grand" \\lower }')
    lines.append("  >>")
    lines.append("  \\layout { ragged-right = ##f }")
    lines.append("  \\midi { }")
    lines.append("}")
    lines.append("```")
    body = "\n".join(lines)
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    print(body)


if __name__ == "__main__":
    main()
