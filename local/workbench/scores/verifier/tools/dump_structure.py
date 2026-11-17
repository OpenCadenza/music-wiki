import sys
from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
tree = etree.parse(XML)
root = tree.getroot()
parts = root.findall("./part")
print("parts:", len(parts))
for p in parts:
    ms = p.findall("./measure")
    print(p.get("id"), "measures:", len(ms), "first#", ms[0].get("number"), "last#", ms[-1].get("number"))

p1 = parts[0]
print("\n=== attributes / key / time / tempo changes in part 1 ===")
for i, m in enumerate(p1.findall("./measure"), 1):
    num = m.get("number")
    attrs = m.find("./attributes")
    info = []
    if attrs is not None:
        for tag in ("divisions", "key", "time", "clef", "staves"):
            for el in attrs.findall("./" + tag):
                if tag == "key":
                    f = el.find("./fifths")
                    mo = el.find("./mode")
                    info.append("key(fifths=%s,mode=%s)" % (f.text if f is not None else "?", mo.text if mo is not None else "?"))
                elif tag == "time":
                    b = el.find("./beats"); bt = el.find("./beat-type")
                    info.append("time(%s/%s)" % (b.text if b is not None else "?",
                                                 bt.text if bt is not None else "?"))
                elif tag == "clef":
                    sn = el.find("./sign"); ln = el.find("./line")
                    info.append("clef(%s%s)" % (sn.text if sn is not None else "?",
                                                ln.text if ln is not None else "?"))
                else:
                    info.append("%s=%s" % (tag, el.text))
    d = m.find("./direction")
    if d is not None:
        for dt in d.findall("./direction-type"):
            for w in dt:
                if w.tag in ("words", "metronome"):
                    txt = w.text if w.tag == "words" else etree.tostring(w, encoding="unicode")
                    info.append("dir(%s)" % txt)
    pr = m.find("./print")
    if pr is not None and (pr.get("new-page") or pr.get("new-system")):
        info.append("PRINT(%s%s)" % (pr.get("new-page") and "new-page " or "", pr.get("new-system") and "new-system" or ""))
    barline = m.find("./barline")
    if barline is not None:
        st = barline.get("location")
        bt = barline.find("./bar-style")
        if bt is not None:
            info.append("barline(%s,%s)" % (st, bt.text))
    if info:
        print(i, "number=" + str(num), " | ".join(info))
