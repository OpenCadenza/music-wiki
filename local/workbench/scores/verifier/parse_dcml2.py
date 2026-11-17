"""Rigorous DCML MusicXML parse: per-voice onset/duration, slur/tie types, articulations, dynamics."""
import xml.etree.ElementTree as ET

PATH = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\score-s6\beethoven-op109\dcml-30-3.musicxml"
STEP = {"C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11}
NAMES = [("C",0),("C",1),("D",0),("D",1),("E",0),("F",0),("F",1),("G",0),("G",1),("A",0),("A",1),("B",0)]

def pnm(m):
    st, al = NAMES[m % 12]
    return f"{st}{'#' if al else ''}{m//12 - 1}"

def walk(meas, divisions, label):
    cur = 0            # cursor in "divisions"
    prev_dur = 0
    events = []
    for el in meas:
        if el.tag == "backup":
            cur -= int(el.findtext("duration") or 0)
        elif el.tag == "forward":
            d = int(el.findtext("duration") or 0)
            events.append((cur/divisions, d/divisions, "FORWARD", label))
            cur += d
        elif el.tag == "note":
            if el.find("grace") is not None:
                p = el.find("pitch")
                m = 12*(int(p.findtext("octave"))+1)+STEP[p.findtext("step")]+(int(p.findtext("alter")) if p.findtext("alter") else 0)
                events.append((cur/divisions, 0.0, f"GRACE {pnm(m)}", label))
                continue
            dur = int(el.findtext("duration") or 0)
            if el.find("chord") is None:
                if el.find("rest") is not None:
                    events.append((cur/divisions, dur/divisions, "REST", label))
                    cur += dur; prev_dur = dur
                    continue
                onset = cur
                cur += dur; prev_dur = dur
            else:
                onset = cur - prev_dur
            p = el.find("pitch")
            m = 12*(int(p.findtext("octave"))+1)+STEP[p.findtext("step")]+(int(p.findtext("alter")) if p.findtext("alter") else 0)
            slurs, arts, ties = [], [], []
            for t in el.findall("notations/slur"):
                slurs.append(f"slur{t.get('type')}#{t.get('number')}")
            for a in el.findall("notations/articulations/*"):
                arts.append(a.tag)
            for t in el.findall("tie") + p.findall("tie"):
                ties.append(t.get("type"))
            for t in el.findall("notations/tied"):
                ties.append("tied-"+t.get("type"))
            events.append((onset/divisions, dur/divisions, pnm(m), label,
                           " ".join(slurs+arts+ties)))
    return events

def main():
    root = ET.parse(PATH).getroot()
    for part in root.findall("part"):
        print("="*95)
        print(f"PART {part.get('id')}")
        print("="*95)
        divisions = 240
        for meas in part.findall("measure"):
            num = meas.get("number")
            if num not in [str(i) for i in range(1, 9)]:
                continue
            for attrs in meas.findall("attributes"):
                if attrs.findtext("divisions"):
                    divisions = int(attrs.findtext("divisions"))
                info = []
                if attrs.find("key/fifths") is not None: info.append("fifths="+attrs.findtext("key/fifths"))
                if attrs.find("time") is not None: info.append("time="+attrs.findtext("time/beats")+"/"+attrs.findtext("time/beat-type"))
                for c in attrs.findall("clef"):
                    info.append("clef="+c.findtext("sign")+c.findtext("line"))
                if info: print(f"  [m{num} attrs] " + " ".join(info))
            # directions
            dirs = []
            for d in meas.findall("direction"):
                texts = [w.text for w in d.findall("direction-type/words")]
                dyn = [x.tag for x in d.findall("direction-type/dynamics/*")]
                sounds = [s.get("dynamics") for s in d.findall("sound")]
                if texts or dyn or sounds:
                    dirs.append(f"words={texts} dyn={dyn} sound_dyn={sounds}")
            ev = walk(meas, divisions, f"P{part.get('id')[-1]}")
            ev.sort(key=lambda x: (x[0], 0 if x[2].startswith("GRACE") else 1))
            print(f"--- measure {num} ---")
            if dirs:
                for d in dirs: print(f"   DIRECTION: {d}")
            for e in ev:
                onset, dur, name, lab, ann = (e + ("",))[:5] if len(e) == 4 else e
                print(f"   @{onset:<5g} dur={dur:<4g} {name:10s} {ann}")

if __name__ == "__main__":
    main()