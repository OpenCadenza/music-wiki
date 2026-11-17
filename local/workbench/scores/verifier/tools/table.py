from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
tree = etree.parse(XML)
root = tree.getroot()
parts = root.findall("./part")
NAMES = ["Vn1", "Vn2", "Va", "Vc"]
STEPS = "CDEFGAB"
BASE = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def tok(n):
    st = n.find("./pitch/step")
    if st is None:
        return "r"
    alt = n.find("./pitch/alter")
    oc = n.find("./pitch/octave")
    a = 0 if alt is None else int(float(alt.text))
    midi = (int(oc.text) + 1) * 12 + BASE[st.text] + a
    typ = n.find("./type")
    t = typ.text if typ is not None else "?"
    dots = "." * len(n.findall("./dot"))
    tm = n.find("./time-modification")
    tupl = ""
    if tm is not None:
        ac = tm.find("./actual-notes"); nm = tm.find("./normal-notes")
        if ac is not None and nm is not None:
            tupl = "{%s:%s}" % (ac.text, nm.text)
    g = "g" if n.find("./grace") is not None else ""
    chord = "+" if n.find("./chord") is not None else ""
    dur = n.find("./duration")
    return "%s%s%s%s%s%s" % (midi, t, dots, tupl, g, chord)


def measure_sum(part_ms):
    ms = part_ms.findall("./measure")
    out = []
    for i, m in enumerate(ms):
        try:
            num = int(m.get("number"))
        except Exception:
            continue
        dur = 0
        toks = []
        for el in m:
            if el.tag == "note":
                if el.find("./chord") is None:
                    d = el.find("./duration")
                    dur += int(d.text) if d is not None else 0
                if el.find("./grace") is None:
                    toks.append(tok(el))
            elif el.tag == "forward":
                dur += int(el.find("./duration").text)
        out.append((num, dur, toks, m.get("implicit"), i))
    return out


for pi, p in enumerate(parts):
    rows = measure_sum(p)
    print("\n=== %s : movement IV numbers 0..20 ===" % NAMES[pi])
    for num, dur, toks, imp, i in rows:
        if num < 0 or num > 20:
            continue
        if i < 467:
            pass
        # only movement IV: index >= 467
        if i < 467:
            continue
        print("n%-3s dur=%-3s implicit=%-4s idx=%-4d %s" % (num, dur, imp, i + 1, " ".join(toks)))
