# -*- coding: utf-8 -*-
"""解析 BeLuva MusicXML（kern 同源，music21 转换）mm.165-173 四声部音高，
用于校准 kern 八度读音并交叉验证。"""
import xml.etree.ElementTree as ET

fname = "local/workbench/scores/verifier/beluva_op135_mvt4.xml"
tree = ET.parse(fname)
root = tree.getroot()
parts = root.findall("part")

def pitch_of(note):
    p = note.find("pitch")
    if p is None:
        return None
    step = p.find("step").text
    alter = p.find("alter")
    a = int(alter.text) if alter is not None else 0
    octv = int(p.find("octave").text)
    base = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}[step]
    midi = 12 * (octv + 1) + base + a
    return f"{step}{'#'*(a>0) or 'b'*(-a) if a else ''}{octv}({midi})"

for pi, part in enumerate(parts):
    pname = part.find("part-name").text if part.find("part-name") is not None else "?"
    measures = part.findall("measure")
    print(f"\n===== Part {pi+1}: {pname} =====")
    for m in measures:
        num = int(m.get("number"))
        if not (163 <= num <= 173):
            continue
        notes = []
        for note in m.findall("note"):
            # 跳过 grace / chord 附属
            if note.find("grace") is not None:
                continue
            if note.find("chord") is not None:
                continue
            pit = pitch_of(note)
            dur = note.find("duration").text
            typ = note.find("type")
            rest = note.find("rest") is not None
            notes.append((("R" if rest else pit), typ.text if typ is not None else dur))
        # 合并（pitch, type）序列
        seq = " ".join(f"{a}:{b}" for a, b in notes)
        print(f"  m.{num}: {seq}")