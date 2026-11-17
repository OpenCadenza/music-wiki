from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
root = etree.parse(XML).getroot()
parts = root.findall("./part")
NAMES = ["Vn1", "Vn2", "Va", "Vc"]
MSTART = 467

print("notes whose <accidental> disagrees with <alter> (movement IV) :")
tot = 0
per = {}
for pi, p in enumerate(parts):
    ms = p.findall("./measure")
    for m in ms[MSTART:]:
        for n in m.findall("./note"):
            acc = n.find("./accidental")
            if acc is None:
                continue
            st = n.find("./pitch/step")
            if st is None:
                continue
            alt = n.find("./pitch/alter")
            a = 0 if alt is None or alt.text is None else int(float(alt.text))
            want = {"sharp": 1, "flat": -1, "natural": 0, "double-sharp": 2, "flat-flat": -2}.get(acc.text, None)
            if want is None:
                continue
            if want != a:
                per.setdefault(NAMES[pi], []).append((m.get("number"), st.text, a, acc.text))
                tot += 1
print("total mismatches:", tot)
for k, v in per.items():
    print(" %s: %d ->" % (k, len(v)), v[:12])

print("\nall <accidental> count in movement IV per part:")
for pi, p in enumerate(parts):
    c = 0
    for m in p.findall("./measure")[MSTART:]:
        c += len(m.findall("./note/accidental"))
    print("  %s: %d" % (NAMES[pi], c))
