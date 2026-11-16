# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
tree = ET.parse("local/workbench/scores/verifier/beluva_op135_mvt4.xml")
root = tree.getroot()
parts = root.findall("part")


def P(n):
    p = n.find("pitch")
    if p is None:
        return None
    st = p.find("step").text
    al = p.find("alter")
    a = int(al.text) if al is not None else 0
    oc = int(p.find("octave").text)
    acc = "#" if a > 0 else ("b" if a < 0 else "")
    return f"{st}{acc}{oc}"


for pi in (2, 0):
    print("==== Part", pi + 1, "====")
    for m in parts[pi].findall("measure"):
        n = int(m.get("number"))
        if n not in (165, 166, 167, 168):
            continue
        items = []
        for note in m.findall("note"):
            if note.find("grace") is not None:
                continue
            crd = note.find("chord") is not None
            pit = P(note)
            if pit is None:
                typ = "R"
            else:
                typ = "&" + pit if crd else pit
            items.append(typ)
        print(" m", n, ":", " ".join(items))