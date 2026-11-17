from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
tree = etree.parse(XML)
root = tree.getroot()
parts = root.findall("./part")
NAMES = ["Vn1", "Vn2", "Va", "Vc"]

print("=== clef state entering movement IV (last clef before index 467) and within mm.0-16 ===")
for pi, p in enumerate(parts):
    ms = p.findall("./measure")
    clefs = []
    for i, m in enumerate(ms):
        for c in m.findall("./attributes/clef"):
            sn = c.find("./sign"); ln = c.find("./line"); oc = c.find("./clef-octave-change")
            clefs.append((i + 1, m.get("number"), "%s%s%s" % (sn.text if sn is not None else "?",
                                                              ln.text if ln is not None else "",
                                                              (" oct" + oc.text) if oc is not None else "")))
    before = [c for c in clefs if c[0] <= 468]
    print("%s: clefs up to mvt-IV start -> %s" % (NAMES[pi], before[-2:]))

print("\n=== dynamics / directions in movement IV mm.0-16 ===")
for pi, p in enumerate(parts):
    ms = p.findall("./measure")
    print("-- %s --" % NAMES[pi])
    for m in ms[467:]:
        try:
            num = int(m.get("number"))
        except Exception:
            continue
        if num > 16:
            continue
        for d in m.findall("./direction"):
            for dt in d.findall("./direction-type"):
                for w in dt:
                    if w.tag == "words":
                        print("   m%-3s words=%r" % (num, w.text))
                    elif w.tag == "dynamics":
                        print("   m%-3s dynamics=%s" % (num, [c.tag for c in w]))
    # also tempo sound
    for m in ms[467:]:
        for s in m.findall("./direction/sound"):
            if s.get("tempo"):
                print("   m%s tempo=%s" % (m.get("number"), s.get("tempo")))
        try:
            if int(m.get("number")) > 2:
                break
        except Exception:
            pass

print("\n=== movement titles / numbers in all parts (mvt IV start measure 0) ===")
for pi, p in enumerate(parts):
    m = p.findall("./measure")[467]
    print(NAMES[pi], "number=", m.get("number"), "implicit=", m.get("implicit"))
