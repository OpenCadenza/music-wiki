import sys
from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
tree = etree.parse(XML)
root = tree.getroot()
parts = root.findall("./part")


def note_repr(n):
    tag = "grace" if n.find("./grace") is not None else ""
    st = n.find("./pitch/step")
    alt = n.find("./pitch/alter")
    oc = n.find("./pitch/octave")
    if st is None:
        unp = n.find("./unpitched")
        pitch = "UNPITCHED" if unp is not None else "REST"
    else:
        acc = ""
        if alt is not None and alt.text not in (None, "0"):
            acc = {1: "#", -1: "b", 2: "##", -2: "bb"}.get(int(float(alt.text)), "(alt%s)" % alt.text)
        pitch = "%s%s%s" % (st.text, acc, oc.text if oc is not None else "?")
    dur = n.find("./duration")
    typ = n.find("./type")
    dot = len(n.findall("./dot"))
    tm = n.find("./time-modification")
    stem = n.find("./stem")
    chord = n.find("./chord") is not None
    accidental = n.find("./accidental")
    tie = [t.get("type") for t in n.findall("./tie")]
    slur = [s.get("type") + s.get("number", "") for s in n.findall("./notations/slur")]
    artic = [(a.tag) for a in n.findall("./notations/*")]
    beam = [b.text for b in n.findall("./beam")]
    voice = n.find("./voice")
    return dict(pitch=pitch, dur=dur.text if dur is not None else "?",
                type=(typ.text if typ is not None else "") + ("." * dot),
                tm=(etree.tostring(tm, encoding="unicode").strip() if tm is not None else ""),
                grace=tag, chord=chord, stem=stem.text if stem is not None else "",
                accidental=accidental.text if accidental is not None else "",
                tie=",".join(x for x in tie if x), slur=",".join(slur),
                artic=",".join(a for a in artic if a not in ("slur", "tied", "tuplet")),
                beam="".join(beam), voice=voice.text if voice is not None else "")


def dump(part_index, lo, hi, mstart_index):
    p = parts[part_index]
    ms = p.findall("./measure")
    print("\n########## PART %s (%s) ##########" % (part_index + 1, p.get("id")))
    for i in range(mstart_index, len(ms)):
        m = ms[i]
        num = m.get("number")
        try:
            n = int(num)
        except Exception:
            continue
        if n < lo or n > hi:
            continue
        print("\n--- measure number=%s (part-measure index %d) implicit=%s ---" % (num, i + 1, m.get("implicit")))
        attrs = m.find("./attributes")
        if attrs is not None:
            print("   [attributes] " + etree.tostring(attrs, encoding="unicode").replace("\n", " ").replace("  ", " ")[:400])
        for el in m:
            if el.tag == "note":
                r = note_repr(el)
                print("   note %-9s dur=%-3s type=%-5s %s%s%s%s%s%s%s%s%s" % (
                    r["pitch"], r["dur"], r["type"],
                    ("GRACE " if r["grace"] else ""),
                    ("CHORD " if r["chord"] else ""),
                    ("tm=" + r["tm"] + " ") if r["tm"] else "",
                    ("acc=" + r["accidental"] + " ") if r["accidental"] else "",
                    ("tie=" + r["tie"] + " ") if r["tie"] else "",
                    ("slur=" + r["slur"] + " ") if r["slur"] else "",
                    ("artic=" + r["artic"] + " ") if r["artic"] else "",
                    ("stem=" + r["stem"] + " ") if r["stem"] else "",
                    ("beam=" + r["beam"] + " ") if r["beam"] else ""))
            elif el.tag == "forward":
                print("   forward dur=%s" % (el.find("./duration").text))
            elif el.tag == "backup":
                print("   backup dur=%s" % (el.find("./duration").text))
            elif el.tag in ("direction", "barline", "print", "harmony"):
                s = etree.tostring(el, encoding="unicode").replace("\n", " ")
                print("   [%s] %s" % (el.tag, s[:250]))


MSTART = int(sys.argv[1]) if len(sys.argv) > 1 else 467  # 0-based index of movement-IV measure number=0
for pi in range(4):
    dump(pi, int(sys.argv[2]) if len(sys.argv) > 2 else 0,
         int(sys.argv[3]) if len(sys.argv) > 3 else 20, MSTART)
