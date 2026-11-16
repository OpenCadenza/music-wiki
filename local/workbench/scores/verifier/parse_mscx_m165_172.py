# -*- coding: utf-8 -*-
"""核验用：解析 DCML mscx mm.165-172 四声部（MS3 与 reviewed 两版），
打印每小节每 Chord/Rest 的 MIDI pitch / pname / alter / octave / durationType，
并输出 TimeSig 变化点用于验证小节对齐。"""
import xml.etree.ElementTree as ET
import sys

FILES = [
    "local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n16op135_04.mscx",
    "local/resources/scores/source-packages/dcml/ABC-main/ABC-main/reviewed/n16op135_04_reviewed.mscx",
]

DUR_Q = {  # durationType -> quarter beats
    "whole": 4.0, "half": 2.0, "quarter": 1.0, "eighth": 0.5, "16th": 0.25,
    "32nd": 0.125, "64th": 0.0625, "measure": None,
    "breve": 8.0, "longa": 16.0,
}

def dur_to_q(child):
    dt = child.find("durationType")
    d = dt.text if dt is not None else "?"
    base = DUR_Q.get(d, None)
    if base is None:
        return d, None
    q = base
    dots = child.find("dots")
    if dots is not None:
        for _ in range(int(dots.text)):
            q += base / 2
    return d, q

def fmt_note(n):
    p = n.find("pitch")
    pn = n.find("pname")
    alt = n.find("alter")
    oc = n.find("octave")
    tpc = n.find("tpc")
    return (f"p:{p.text if p is not None else '?'}"
            f"(pname:{pn.text if pn is not None else '?'}"
            f" alt:{alt.text if alt is not None else '0'}"
            f" oct:{oc.text if oc is not None else '?'}"
            f" tpc:{tpc.text if tpc is not None else '?'})")

for fname in FILES:
    print("=" * 80)
    print("FILE:", fname)
    print("=" * 80)
    tree = ET.parse(fname)
    root = tree.getroot()
    score = root.find("Score")
    staffs = score.findall("Staff")

    # ---- 1) 小节对齐验证: TimeSig 变化点 ----
    print("\n--- TimeSig 变化点（measure count 1-based）---")
    prev_sig = None
    for s_idx, staff in enumerate(staffs[:1]):
        for m_count, m in enumerate(staff.findall("Measure")):
            sigs = []
            for sig in m.iter("TimeSig"):
                ns = sig.find("sigN"); ds = sig.find("sigD")
                sigs.append(f"{ns.text}/{ds.text}" if ns is not None and ds is not None else "?")
            for v in m.findall("voice"):
                for tempo in v.iter("Tempo"):
                    t = tempo.find("text")
                    if t is not None and t.text:
                        sigs.append(f"TEMPO:{t.text}")
            if sigs:
                print(f"  measure {m_count+1}: {sigs}")
    print()

    # ---- 2) 指定小节范围内容 ----
    start, end = 165, 172  # 1-based measure counts（假设 = 曲谱小节号，对齐验证后确认）
    for s_idx, staff in enumerate(staffs):
        ms = staff.findall("Measure")
        print(f"\n===== Staff {s_idx+1} (id={staff.get('id')}) =====")
        for m_count in range(start - 1, min(end, len(ms))):
            m = ms[m_count]
            print(f"  -- Measure {m_count+1} --")
            qsum = 0.0
            for v in m.findall("voice"):
                for child in v:
                    tag = child.tag
                    if tag == "Chord":
                        dt, q = dur_to_q(child)
                        trem = child.find("Tremolo")
                        trems = f" trem:{trem.get('type')}/{trem.find('subtype').text}" if trem is not None else ""
                        notes = " ".join(fmt_note(n) for n in child.findall("Note"))
                        print(f"     Chord {dt} q={q}{trems} | {notes}")
                        if q is not None:
                            qsum += q
                    elif tag == "Rest":
                        dt, q = dur_to_q(child)
                        print(f"     Rest  {dt} q={q}")
                        if q is not None:
                            qsum += q
                    elif tag in ("TimeSig", "KeySig"):
                        pass
            print(f"     [sum q={qsum}]")