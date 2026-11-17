import struct, sys
from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
MID = r"local\workbench\scores\verifier\build-k465\S2-K1-mozart-k465-4-m10-16.mid"
NAMES = ["Vn1", "Vn2", "Va", "Vc"]
BASE = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
MSTART = 467
LO, HI = 10, 16

# ---------- source ----------
def source():
    root = etree.parse(XML).getroot()
    out = {}
    for pi, p in enumerate(root.findall("./part")):
        ms = p.findall("./measure")
        per = {}
        for m in ms[MSTART:]:
            try:
                num = int(m.get("number"))
            except Exception:
                continue
            if num < LO or num > HI:
                continue
            onset = 0.0
            notes = []
            for el in m:
                if el.tag == "note":
                    if el.find("./grace") is not None:
                        continue
                    d = el.find("./duration")
                    du = int(d.text) if d is not None else 0
                    if el.find("./chord") is None:
                        st = el.find("./pitch/step")
                        if st is None:
                            notes.append((onset / 24.0, None, du / 24.0))
                        else:
                            alt = el.find("./pitch/alter")
                            oc = el.find("./pitch/octave")
                            a = 0 if alt is None or alt.text is None else int(float(alt.text))
                            midi = (int(oc.text) + 1) * 12 + BASE[st.text] + a
                            notes.append((onset / 24.0, midi, du / 24.0))
                        onset += du
                    else:
                        notes.append((onset / 24.0, None, du / 24.0))
                elif el.tag == "forward":
                    onset += int(el.find("./duration").text)
            per[num] = notes
        out[NAMES[pi]] = per
    return out

# ---------- midi ----------
def read_vlq(b, i):
    v = 0
    while True:
        c = b[i]; i += 1
        v = (v << 7) | (c & 0x7F)
        if not c & 0x80:
            return v, i

def midi():
    b = open(MID, "rb").read()
    hlen = struct.unpack(">I", b[4:8])[0]
    fmt, ntrk, div = struct.unpack(">HHH", b[8:14])
    i = 8 + hlen
    tracks = []
    for t in range(ntrk):
        ln = struct.unpack(">I", b[i + 4:i + 8])[0]
        body = b[i + 8:i + 8 + ln]
        i += 8 + ln
        tme = 0; status = None; j = 0; notes = []; on = {}
        while j < len(body):
            d, j = read_vlq(body, j)
            tme += d
            c = body[j]
            if c & 0x80:
                status = c; j += 1
            if status == 0xFF:
                meta = body[j]; j += 1
                ln2, j = read_vlq(body, j)
                j += ln2
            elif status in (0xF0, 0xF7):
                ln2, j = read_vlq(body, j); j += ln2
            else:
                hi = status & 0xF0; ch = status & 0x0F
                n = 1 if hi in (0xC0, 0xD0) else 2
                data = body[j:j + n]; j += n
                if hi == 0x90 and data[1] > 0:
                    on[(ch, data[0])] = tme
                elif hi == 0x80 or (hi == 0x90 and data[1] == 0):
                    k = (ch, data[0])
                    if k in on:
                        notes.append((on[k], data[0], tme - on[k])); del on[k]
        notes.sort()
        tracks.append(notes)
    return div, tracks

div, tracks = midi()
Q = div
per_track = {}
for ti, notes in enumerate(tracks[1:], start=1):
    d = {}
    for st, p, du in notes:
        bar = st // (2 * Q) + LO
        beat = (st % (2 * Q)) / Q
        d.setdefault(bar, []).append((round(beat, 3), p, round(du / Q, 3)))
    per_track[NAMES[ti - 1]] = d

src = source()
print("divisions:", div, "  MIDI bar1 == source measure %d" % LO)
total_bad = 0
for name in NAMES:
    print("\n===== %s =====" % name)
    for num in range(LO, HI + 1):
        s = [(b, p) for (b, p, d) in src[name].get(num, [])]
        m = [(b, p) for (b, p, d) in per_track[name].get(num, [])]
        sd = [d for (b, p, d) in src[name].get(num, [])]
        md = [d for (b, p, d) in per_track[name].get(num, [])]
        # grace notes in MIDI appear as very short notes; drop them for comparison but remember
        grace_like = [(b, p) for (b, p, d) in per_track[name].get(num, []) if d <= 0.06]
        s_np = [(b, p) for (b, p) in s if p is not None]
        m_np = [(b, p) for (b, p, d) in per_track[name].get(num, []) if p is not None and d > 0.06]
        ok = s_np == m_np
        if not ok:
            total_bad += 1
        print(" m%-3d %s" % (num, "OK " if ok else "DIFF"))
        if not ok:
            print("     source:", s_np)
            print("     lily  :", m_np)
        if grace_like:
            print("     midi grace-like (dur<=0.06q):", grace_like)
        # duration check for non-grace
        print("     src dur:", sd)
        print("     mid dur:", md)
print("\nDIFF measures:", total_bad)

