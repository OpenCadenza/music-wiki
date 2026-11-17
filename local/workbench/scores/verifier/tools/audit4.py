from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
tree = etree.parse(XML)
root = tree.getroot()
parts = root.findall("./part")
NAMES = ["Vn1", "Vn2", "Va", "Vc"]
LO, HI = 10, 16
MSTART_IDX = 467  # 0-based index in each part of movement IV measure number=0


def spell(st, alt, oc):
    names = {0: "", 1: "#", -1: "b", 2: "##", -2: "bb"}
    v = 0 if alt is None or alt.text is None else int(float(alt.text))
    return "%s%s%s" % (st.text, names.get(v, "?%s" % v), oc.text)


for pi, p in enumerate(parts):
    ms = p.findall("./measure")
    print("\n===== %s (movement IV only) =====" % NAMES[pi])
    for m in ms[MSTART_IDX:]:
        try:
            num = int(m.get("number"))
        except Exception:
            continue
        if num < LO or num > HI:
            continue
        items = []
        for n in m.findall("./note"):
            st = n.find("./pitch/step")
            if st is None:
                items.append("REST")
                continue
            alt = n.find("./pitch/alter")
            oc = n.find("./pitch/octave")
            acc = n.find("./accidental")
            typ = n.find("./type")
            dots = "." * len(n.findall("./dot"))
            tm = n.find("./time-modification")
            grace = "G" if n.find("./grace") is not None else ""
            arts = [a.tag for a in n.findall("./notations/articulations/*")]
            slurs = ["%s%s" % (s.get("type"), s.get("number") or "") for s in n.findall("./notations/slur")]
            ties = [t.get("type") for t in n.findall("./tie") if t.get("type")]
            s = "%s%s%s" % (spell(st, alt, oc), grace, (typ.text + dots) if typ is not None else "?")
            if acc is not None:
                s += "[printed:%s]" % acc.text
            if tm is not None:
                s += "<tuplet>"
            if arts:
                s += "|" + ",".join(arts)
            if slurs:
                s += "<slur:" + ",".join(slurs) + ">"
            if ties:
                s += "<tie:" + ",".join(ties) + ">"
            items.append(s)
        print("m%-3s %s" % (num, "   ".join(items)))
