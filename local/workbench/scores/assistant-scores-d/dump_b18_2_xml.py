import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/beethoven_18_2.xml')
root = tree.getroot()

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def pname(step, alter, octv):
    base = [0, 2, 4, 5, 7, 9, 11][["C", "D", "E", "F", "G", "A", "B"].index(step)]
    mid = (int(octv) + 1) * 12 + base + int(alter or 0)
    return f"{step}{'#' if alter=='1' else ('b' if alter=='-1' else '')}{octv}({mid})"

parts = root.findall('.//part')
for p in parts:
    pid = p.attrib.get('id')
    # find part name
    pname_el = root.find(f'.//score-part[@id="{pid}"]/part-name')
    part_name = pname_el.text if pname_el is not None else pid
    print(f"\n=== Part {pid}: {part_name} ===")
    measures = p.findall('measure')
    for m in measures:
        num = int(m.attrib.get('number'))
        if num > 8: break
        items = []
        for n in m.findall('note'):
            if n.find('rest') is not None:
                dur = n.find('type').text if n.find('type') is not None else 'rest'
                items.append(f"Rest({dur})")
            else:
                p_el = n.find('pitch')
                step = p_el.find('step').text
                alt = p_el.find('alter').text if p_el.find('alter') is not None else None
                octv = p_el.find('octave').text
                dur = n.find('type').text if n.find('type') is not None else '?'
                dot = n.find('dot') is not None
                stacc = n.find('.//staccato') is not None
                slur = n.find('.//slur') is not None
                items.append(f"{pname(step, alt, octv)} {dur}{'.' if dot else ''}{' stacc' if stacc else ''}")
        print(f"M{num}: {items}")
