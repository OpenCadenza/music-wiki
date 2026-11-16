"""把 .ly 事件与各源事件按小节做集合比对。"""
import csv
import xml.etree.ElementTree as ET
from fractions import Fraction
from pathlib import Path

import lyparse
import src_abc

NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
STEP = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def nm(p):
    return f"{NAMES[p % 12]}{p // 12 - 1}"


def ly_per_measure(display, names, bar_len, partial):
    tracks = lyparse.load(display, names)
    out = {}
    for name, tr in tracks.items():
        for t, d, p in tr.events:
            if t < partial - 1e-9:
                m, onset = 0, t
            else:
                m = int((t - partial) / bar_len + 1e-9) + 1
                onset = round(t - partial - (m - 1) * bar_len, 4)
            out.setdefault(m, []).append((round(onset, 4), p, round(d, 4), name))
    for m in out:
        out[m].sort()
    return out


def xml_per_measure(path, maxm, part_filter=None):
    root = ET.parse(path).getroot()
    out = {}
    for part in root.findall("part"):
        if part_filter is not None and part.get("id") != part_filter:
            continue
        div = 1
        for meas in part.findall("measure"):
            num = meas.get("number")
            try:
                mi = int("".join(c for c in str(num) if c.isdigit()))
            except ValueError:
                continue
            if mi > maxm:
                break
            t = 0.0
            cursors = {}
            prev_onset = 0.0
            for el in meas:
                if el.tag == "attributes":
                    dv = el.findtext("divisions")
                    if dv:
                        div = int(dv)
                    continue
                if el.tag not in ("note",):
                    continue
                grace = el.find("grace") is not None
                chord = el.find("chord") is not None
                dur = int(el.findtext("duration") or 0) / div
                voice = el.findtext("voice") or "1"
                staff = el.findtext("staff") or "1"
                key = voice
                t = prev_onset if chord else cursors.get(key, 0.0)
                if el.find("rest") is not None:
                    if not grace and not chord:
                        cursors[key] = t + dur
                    continue
                p = el.find("pitch")
                if p is None:
                    continue
                midi = ((int(p.findtext("octave")) + 1) * 12 + STEP[p.findtext("step")]
                        + int(p.findtext("alter") or 0))
                if grace:
                    continue
                out.setdefault(mi, []).append((round(t, 4), midi, round(dur, 4),
                                               f"p{part.get('id')}s{staff}v{voice}"))
                if not chord:
                    cursors[key] = t + dur
                    prev_onset = t
    for m in out:
        out[m].sort()
    return out


def abc_per_measure(path, first_line, last_line, unit=0.5, key_alters=None, only_v=None):
    """返回 {小节下标(0=弱起): [(小节内 onset, midi, 时值, 声部标签)]}。"""
    import re
    key_alters = key_alters or {}
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    counter = {}
    out = {}
    for idx in range(first_line - 1, last_line):
        m = re.match(r"\s*\[V:(\d+)\]\s*(.*)$", lines[idx])
        if not m:
            continue
        v = int(m.group(1))
        if only_v is not None and v != only_v:
            continue
        text = m.group(2)
        for piece in split_bars(text):
            if not piece.strip(" |:"):
                continue
            n = counter.get(v, 0) + 1
            counter[v] = n
            voices, total = src_abc.parse_field(piece, unit, key_alters)
            for ev in voices:
                for onset, midi, dur in ev:
                    if midi is None:
                        continue
                    out.setdefault(n - 1, []).append((round(onset, 4), midi, round(dur, 4), f"V{v}"))
    for k in out:
        out[k].sort()
    return out


def split_bars(text):
    parts, cur = [], []
    for ch in text:
        if ch == "|":
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts


def dcml_per_measure(path, maxm):
    rows = list(csv.DictReader(Path(path).open(encoding="utf-8"), delimiter="\t"))
    out = {}
    for r in rows:
        mc = int(r["mc"])
        if mc > maxm:
            continue
        if r["gracenote"]:
            continue
        onset = float(Fraction(r["mc_onset"])) * 4.0   # DCML 的 mc_onset 以全音符为单位
        out.setdefault(mc, []).append((round(onset, 4), int(r["midi"]),
                                       round(float(Fraction(r["duration_qb"])), 4),
                                       f"st{r['staff']}v{r['voice']}"))
    for k in out:
        out[k].sort()
    return out


def diff(actual, source, label, ms, with_dur=False):
    def key(ev):
        return (round(ev[0], 3), ev[1], round(ev[2], 3)) if with_dur else (round(ev[0], 3), ev[1])

    bad = []
    for m in ms:
        a = sorted(key(x) for x in actual.get(m, []))
        s = sorted(key(x) for x in source.get(m, []))
        if a != s:
            from collections import Counter
            ca, cs = Counter(a), Counter(s)
            missing = list((cs - ca).elements())
            extra = list((ca - cs).elements())
            bad.append((m, missing, extra))
    print(f"### {label}: 不一致小节 {len(bad)}/{len(ms)}")
    def fmt(items):
        out = []
        for it in items:
            o, p = it[0], it[1]
            if with_dur and len(it) > 2:
                out.append(f"{nm(p)}({p})@{o:g}+{it[2]:g}")
            else:
                out.append(f"{nm(p)}({p})@{o:g}")
        return ", ".join(out) or "-"

    for m, missing, extra in bad:
        print(f"  m.{m}: 源有而实测无: {fmt(missing)}")
        print(f"        实测有而源无: {fmt(extra)}")
    return bad


def show(events, ms, title):
    print(f"--- {title}")
    for m in ms:
        txt = " ".join(f"{nm(p)}({p})@{o:g}" for o, p, *_ in events.get(m, []))
        print(f"  m.{m}: {txt}")
