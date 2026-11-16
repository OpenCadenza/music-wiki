"""核验用：把 MusicXML 前 N 小节按声部导出为文本（音高/时值/休止），供逐音比对。

用法: python musicxml_dump.py <xml> [最大小节号]
"""
import sys
import xml.etree.ElementTree as ET

STEP_SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def midi_of(step, alter, octave):
    return (int(octave) + 1) * 12 + STEP_SEMI[step] + int(alter or 0)


def dump(path, max_measure):
    tree = ET.parse(path)
    root = tree.getroot()
    parts = root.findall("part")
    print(f"文件: {path}")
    print(f"声部数: {len(parts)}")
    for pi, part in enumerate(parts):
        print(f"\n===== Part {pi+1} (id={part.get('id')}) =====")
        for meas in part.findall("measure"):
            num = meas.get("number")
            try:
                if int(''.join(ch for ch in str(num) if ch.isdigit())) > max_measure:
                    break
            except ValueError:
                pass
            notes = []
            for elem in meas:
                if elem.tag == "attributes":
                    for sub in elem:
                        if sub.tag in ("divisions", "time", "key", "clef"):
                            notes.append(f"[{sub.tag}:{sub.attrib}]")
                elif elem.tag == "note":
                    if elem.find("rest") is not None:
                        dur = elem.findtext("duration")
                        notes.append(f"rest(d={dur})")
                        continue
                    p = elem.find("pitch")
                    if p is None:
                        notes.append("?no-pitch")
                        continue
                    step = p.findtext("step")
                    alter = p.findtext("alter") or 0
                    octv = p.findtext("octave")
                    dur = elem.findtext("duration")
                    typ = elem.findtext("type")
                    dot = len(elem.findall("dot"))
                    tie = ""
                    for t in elem.findall("tie"):
                        tie += "/tie-" + t.get("type", "")
                    staff = elem.findtext("staff") or "1"
                    voice = elem.findtext("voice") or "1"
                    chord = "CHORD+" if elem.find("chord") is not None else ""
                    m = midi_of(step, alter, octv)
                    notes.append(
                        f"{chord}{step}{'' if not alter else ('+' + ustr(alter))}{octv}"
                        f"(m{m},d={dur},{typ}{'.'*dot}{tie},v{voice},st{staff})"
                    )
            print(f"m.{num}: " + " ".join(notes))


def ustr(alter):
    try:
        f = float(alter)
        if f == int(f):
            return str(int(f))
        return str(f)
    except Exception:
        return str(alter)


if __name__ == "__main__":
    dump(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 10)
