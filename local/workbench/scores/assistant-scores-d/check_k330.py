import xml.etree.ElementTree as ET

xml_path = "local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml"
tree = ET.parse(xml_path)
root = tree.getroot()

for measure in root.findall(".//measure"):
    num = measure.attrib.get("number")
    if int(num) <= 8:
        print(f"--- Measure {num} ---")
        for elem in measure:
            if elem.tag == "direction":
                words = elem.findall(".//words")
                for w in words:
                    print(f"  [Direction] {w.text}")
            elif elem.tag == "note":
                rest = elem.find("rest")
                pitch = elem.find("pitch")
                dur = elem.find("duration")
                voice = elem.find("voice")
                staff = elem.find("staff")
                notations = elem.find("notations")
                note_str = "Rest" if rest is not None else f"{pitch.find('step').text}{pitch.find('octave').text}"
                acc = elem.find("accidental")
                if acc is not None:
                    note_str += f"({acc.text})"
                dots = len(elem.findall("dot"))
                beam = [b.text for b in elem.findall("beam")]
                artic = []
                if notations is not None:
                    for child in notations:
                        artic.append(child.tag)
                print(f"  Staff {staff.text if staff is not None else '?'} V{voice.text if voice is not None else '?'}: {note_str} dur={dur.text if dur is not None else '?'} dots={dots} beam={beam} {artic}")
