import sys, xml.etree.ElementTree as ET
sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]
def nm(p): return f"{NAMES[p%12]}{p//12-1}"
for path in [r"local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n10op74_01.mscx",
             r"local/resources/scores/source-packages/dcml/ABC-main/ABC-main/reviewed/n10op74_01_reviewed.mscx"]:
    root = ET.parse(path).getroot()
    score = root.find("Score")
    print("\n########", path.split("ABC-main/")[-1], "########")
    for staff in score.findall("Staff"):
        if staff.get("id") != "1":
            continue
        for mi, meas in enumerate(staff.findall("Measure"), start=1):
            if mi != 9: continue
            for voice in meas.findall("voice"):
                for el in voice:
                    if el.tag == "Chord":
                        for n in el.findall("Note"):
                            p = int(n.findtext("pitch")); acc = n.findtext("Accidental/subtype") or "-"
                            tpc = n.findtext("tpc") or ""
                            print(f"   midi={p:3d} {nm(p):>4} acc={acc:>22s} tpc={tpc}")
