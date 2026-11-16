import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k283.xml')
root = tree.getroot()

for p in root.findall('.//score-part'):
    pid = p.attrib['id']
    name = p.find('part-name').text if p.find('part-name') is not None else ''
    print(f"Part {pid}: {name}")

for part in root.findall('part'):
    pid = part.attrib['id']
    print(f"=== Part {pid} ===")
    for m in part.findall('measure')[:11]:
        num = m.attrib.get('number', '')
        staves_notes = {}
        for n in m.findall('note'):
            staff = n.find('staff')
            s_id = staff.text if staff is not None else '1'
            pitch_elem = n.find('pitch')
            if pitch_elem is not None:
                step = pitch_elem.find('step').text
                octave = pitch_elem.find('octave').text
                alter = pitch_elem.find('alter')
                alter_str = ('#' if alter.text == '1' else 'b') if alter is not None else ''
                pitch_str = f"{step}{alter_str}{octave}"
            else:
                pitch_str = 'rest'
            dur = n.find('type')
            dur_str = dur.text if dur is not None else ''
            dot = '.' if n.find('dot') is not None else ''
            chord = '+' if n.find('chord') is not None else ''
            staves_notes.setdefault(s_id, []).append(f"{chord}{pitch_str}({dur_str}{dot})")
        print(f"M{num}: {' '.join(staves_notes.get('1', []))}")
