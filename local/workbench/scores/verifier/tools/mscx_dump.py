"""核验用：从 MuseScore .mscx 中导出指定小节范围的音高与临时记号。
MuseScore <pitch> 以 C0=12 记，MIDI = pitch - 12。
"""
import sys
import xml.etree.ElementTree as ET

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
def nm(p): return f"{NAMES[p % 12]}{p // 12 - 1}"

path = sys.argv[1]
maxm = int(sys.argv[2]) if len(sys.argv) > 2 else 9
root = ET.parse(path).getroot()

score = root.find("Score")
for staff in score.findall("Staff"):
    sid = staff.get("id")
    if sid not in ("1", "2", "3", "4"):
        continue
    print(f"\n######## Staff id={sid} ########")
    for mi, meas in enumerate(staff.findall("Measure"), start=1):
        if mi > maxm:
            break
        out = []
        for voice in meas.findall("voice"):
            for el in voice:
                if el.tag == "Rest":
                    d = el.findtext("durationType")
                    dots = len(el.findall("dots")) * "."
                    out.append(f"[rest {d}{dots}]")
                elif el.tag == "Chord":
                    d = el.findtext("durationType") or ""
                    dots = len(el.findall("dots")) * "."
                    notes = []
                    for n in el.findall("Note"):
                        p = n.findtext("pitch")
                        acc = n.findtext("Accidental/subtype") or ""
                        tpc = n.findtext("tpc") or ""
                        midi = int(p) - 12 if p else None
                        notes.append(f"{nm(midi)}({midi}){('/acc=' + acc) if acc else ''}{('/tpc=' + tpc) if tpc else ''}")
                    out.append(f"<{' + '.join(notes)} {d}{dots}>")
        print(f"  m.{mi}: " + " ".join(out))
