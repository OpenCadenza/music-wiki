"""Parse DCML MusicXML (Beethoven Op.109 mvt 3) measures 1-8 into a normalized note list."""
import sys, xml.etree.ElementTree as ET

PATH = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\score-s6\beethoven-op109\dcml-30-3.musicxml"

STEP_SEMI = {"C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11}
NAMES = [("C",0),("C",1),("D",0),("D",1),("E",0),("F",0),("F",1),("G",0),("G",1),("A",0),("A",1),("B",0)]

def midi_of(step, alter, octv):
    return 12*(int(octv)+1) + STEP_SEMI[step] + int(alter) if alter else 12*(int(octv)+1)+STEP_SEMI[step]

def pname(m):
    pc = m % 12
    octave = m//12 - 1
    st, al = NAMES[pc]
    return f"{st}{'#' if al else ''}{octave}", octave, al

def dur_q(divs, divisions):
    return divs/divisions

def main():
    tree = ET.parse(PATH)
    root = tree.getroot()
    for part in root.findall("part"):
        pid = part.get("id")
        staff_label = "P1(staff1/RH)" if pid == "P1" else "P2(staff2/LH)"
        print("="*100)
        print(f"PART {pid}  {staff_label}")
        print("="*100)
        measures = part.findall("measure")
        # first 8 measures
        for meas in measures[:9]:
            num = meas.get("number")
            if num not in [str(i) for i in range(1,9)]:
                continue
            print(f"\n--- measure {num} (implicit={meas.get('implicit')}) ---")
            divisions = None
            for attrs in meas.findall("attributes"):
                d = attrs.findtext("divisions")
                if d:
                    divisions = int(d)
                    print(f"  [attributes] divisions={divisions}", end="")
                fifths = attrs.find("key/fifths")
                if fifths is not None:
                    print(f" key/fifths={fifths.text}", end="")
                mode = attrs.find("key/mode")
                if mode is not None:
                    print(f" mode={mode.text}", end="")
                t = attrs.find("time")
                if t is not None:
                    print(f" time={t.findtext('beats')}/{t.findtext('beat-type')}", end="")
                clefs = attrs.findall("clef")
                for c in clefs:
                    print(f" clef={c.findtext('sign')}{c.findtext('line')} staff={c.get('number')}", end="")
                print()
            pos = 0  # position in whole notes-ish (in quarter units) per measure
            for el in meas:
                tag = el.tag
                if tag == "note":
                    rest = el.find("rest") is not None
                    grace = el.find("grace") is not None
                    chord = el.find("chord") is not None
                    pitch = el.find("pitch")
                    dur = el.findtext("duration")
                    typ = el.findtext("type")
                    dot = "dot" if el.find("dot") is not None else ""
                    voice = el.findtext("voice")
                    staff = el.findtext("staff")
                    dq = dur_q(int(dur), divisions or 240) if dur else None
                    if not chord and not grace and not rest:
                        pos += dq
                    if rest:
                        print(f"  m{num} v{voice} st{staff} REST {typ}{dot} dur={dq}q")
                        continue
                    if pitch is None:
                        continue
                    st_ = pitch.findtext("step")
                    alt = pitch.findtext("alter")
                    octv = pitch.findtext("octave")
                    m = midi_of(st_, alt, octv)
                    nm, o, al = pname(m)
                    ties = [t.get("type") for t in pitch.findall("tie")] + [t.get("type") for t in el.findall("tie")]
                    artic = [a.tag for a in el.findall("notations/*")]
                    flag = ""
                    if chord: flag += " [CHORD]"
                    if grace: flag += " [GRACE]"
                    if ties: flag += f" tie={','.join(ties)}"
                    print(f"  m{num} v{voice} st{staff} {nm:5s} midi={m:3d} typ={typ}{dot:3s} dur={dq}q"
                          f" onset={pos:g}{flag}  notations={artic}")

if __name__ == "__main__":
    main()