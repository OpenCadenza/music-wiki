import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/scores/source-packages/dcml/ABC-main/ABC-main/reviewed/n02op18-2_04_reviewed.mscx')
root = tree.getroot()

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def pname(p):
    p = int(p)
    return f"{NOTE_NAMES[p%12]}{p//12-1}({p})"

staves = root.findall('.//Staff')
print('Staff count:', len(staves))

for s_idx, staff in enumerate(staves):
    staff_id = staff.attrib.get('id')
    print(f"\n================ STAFF {staff_id} ================")
    measures = staff.findall('Measure')
    for m_idx in range(min(8, len(measures))):
        m = measures[m_idx]
        items = []
        for v in m.findall('voice'):
            for child in v:
                if child.tag == 'Chord':
                    notes = [pname(n.find('pitch').text) for n in child.findall('Note')]
                    dur = child.find('durationType').text if child.find('durationType') is not None else '?'
                    dots = child.find('dots') is not None
                    art = [a.find('subtype').text for a in child.findall('Articulation') if a.find('subtype') is not None]
                    slur_start = child.find('.//Slur[@type="start"]') is not None
                    items.append(f"Chord({notes}, {dur}{'.' if dots else ''}, art={art})")
                elif child.tag == 'Rest':
                    dur = child.find('durationType').text if child.find('durationType') is not None else '?'
                    items.append(f"Rest({dur})")
                elif child.tag == 'Dynamic':
                    items.append(f"Dyn({child.find('subtype').text})")
        print(f"M{m_idx+1}: {items}")
