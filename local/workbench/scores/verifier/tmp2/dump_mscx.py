"""MuseScore .mscx → 逐小节逐谱表导出 chord/rest 与时值。"""
import sys
import xml.etree.ElementTree as ET

DURQB = {"whole": 4.0, "half": 2.0, "quarter": 1.0, "eighth": 0.5,
         "16th": 0.25, "32nd": 0.125, "64th": 0.0625, "measure": None}


def dump(path, maxm):
    root = ET.parse(path).getroot()
    score = root.find("Score")
    staffs = score.findall("Staff")
    print(f"{path}: {len(staffs)} 谱表")
    for si, staff in enumerate(staffs, 1):
        print(f"--- Staff {si} (id={staff.get('id')})")
        for mi, meas in enumerate(staff.findall("Measure"), 1):
            if mi > maxm:
                break
            desc = []
            for voice in meas.findall("voice"):
                items = []
                for el in voice:
                    if el.tag == "Rest":
                        dt = el.findtext("durationType")
                        dots = len(el.findall("dots")) or (1 if el.findtext("dots") else 0)
                        items.append(f"rest:{dt}{'.' * dots}")
                    elif el.tag == "Chord":
                        dt = el.findtext("durationType")
                        dots = el.find("dots")
                        ndot = 1 if dots is not None else 0
                        for n in el.findall("Note"):
                            p = n.findtext("pitch")
                            tpc = n.findtext("tpc")
                            acc = n.find("Accidental")
                            atype = acc.get("subtype") if acc is not None else ""
                            items.append(f"midi{p}(tpc{tpc}{',' + atype if atype else ''}):{dt}{'.' * ndot}")
                desc.append("[" + " ".join(items) + "]")
            print(f"  m.{mi}: " + "  ".join(desc))


if __name__ == "__main__":
    dump(sys.argv[1], int(sys.argv[2]))
