from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
tree = etree.parse(XML)
root = tree.getroot()
parts = root.findall("./part")
NAMES = ["Vn1", "Vn2", "Va", "Vc"]
LO, HI = 10, 16

for pi, p in enumerate(parts):
    ms = p.findall("./measure")
    print("\n===== %s =====" % NAMES[pi])
    for m in ms:
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
            grace = n.find("./grace") is not None
            arts = [a.tag for a in n.findall("./notations/articulations/*")]
            slurs = ["%s%s" % (s.get("type"), s.get("number") or "") for s in n.findall("./notations/slur")]
            ties = [t.get("type") for t in n.findall("./tie")]
            s = "%s%s%s" % (st.text, (alt.text if alt is not None else ""), oc.text)
            if acc is not None:
                s += "[printed:%s]" % acc.text
            if grace:
                s += "(grace)"
            if typ is not None:
                s += ":" + typ.text
            if arts:
                s += "{" + ",".join(arts) + "}"
            if slurs:
                s += "<slur " + ",".join(slurs) + ">"
            if ties:
                s += "<tie " + ",".join(x for x in ties if x) + ">"
            items.append(s)
        print("m%-3s  %s" % (num, "  ".join(items)))
