"""MusicXML → 事件表（按 staff/voice 计算 onset）。"""
import sys
import xml.etree.ElementTree as ET

STEP = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def nm(p):
    return f"{NAMES[p % 12]}{p // 12 - 1}"


def dump(path, maxm):
    root = ET.parse(path).getroot()
    parts = root.findall("part")
    for pi, part in enumerate(parts):
        print(f"===== Part {pi+1} id={part.get('id')} =====")
        divisions = 1
        for meas in part.findall("measure"):
            num = meas.get("number")
            try:
                if int("".join(c for c in str(num) if c.isdigit())) > maxm:
                    break
            except ValueError:
                pass
            t = 0.0
            ev = []
            for el in meas:
                if el.tag == "attributes":
                    dv = el.findtext("divisions")
                    if dv:
                        divisions = int(dv)
                    continue
                if el.tag == "backup":
                    t -= int(el.findtext("duration") or 0) / divisions
                    continue
                if el.tag == "forward":
                    t += int(el.findtext("duration") or 0) / divisions
                    continue
                if el.tag != "note":
                    continue
                grace = el.find("grace") is not None
                is_chord = el.find("chord") is not None
                dur = int(el.findtext("duration") or 0) / divisions
                staff = el.findtext("staff") or "1"
                voice = el.findtext("voice") or "1"
                rest = el.find("rest") is not None
                if rest:
                    if not grace and not is_chord:
                        t += dur
                    continue
                p = el.find("pitch")
                if p is None:
                    continue
                midi = ((int(p.findtext("octave")) + 1) * 12 + STEP[p.findtext("step")]
                        + int(p.findtext("alter") or 0))
                if not is_chord and not grace:
                    start = t
                elif is_chord:
                    start = ev[-1][0] if ev else t
                else:
                    start = t
                ev.append((start, midi, dur, staff, voice, grace))
                if not grace and not is_chord:
                    t += dur
            print(f"m.{num} 总时值={t:g}")
            for start, midi, dur, staff, voice, grace in sorted(ev):
                tag = " [grace]" if grace else ""
                print(f"   st{staff} v{voice} @{start:6.3f} +{dur:5.3f} {nm(midi)}({midi}){tag}")


if __name__ == "__main__":
    dump(sys.argv[1], int(sys.argv[2]))
