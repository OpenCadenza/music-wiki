import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n16op135_04.mscx')
score = tree.getroot().find('Score')
staffs = score.findall('Staff')

for s_idx, staff in enumerate(staffs):
    print(f"=== Staff {s_idx+1} ===")
    for m_idx in range(4):
        m = staff.findall('Measure')[m_idx]
        notes = []
        for chord in m.iter('Chord'):
            d = chord.find('durationType').text
            dots = chord.find('dots')
            dot_str = "." if dots is not None else ""
            ps = [n.find('pitch').text for n in chord.findall('Note')]
            notes.append(f"{d}{dot_str}:{','.join(ps)}")
        rests = [r.find('durationType').text for r in m.iter('Rest')]
        print(f"  m.{m_idx+1}: notes=[{' '.join(notes)}] rests=[{' '.join(rests)}]")
