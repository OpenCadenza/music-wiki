import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n16op135_04.mscx')
root = tree.getroot()

score = root.find('Score')
staffs = score.findall('Staff')

for s_idx, staff in enumerate(staffs):
    s_id = staff.get('id')
    print(f"\n==================== Staff {s_idx + 1} id={s_id} ====================")
    measures = staff.findall('Measure')
    for m_count, m in enumerate(measures):
        # m_count 165 corresponds to measure index 166 (since 1-based, first measure is count 1)
        # Note: mm.165-172
        if 164 <= m_count + 1 <= 173:
            print(f"\n--- Measure {m_count + 1} ---")
            for elem in m.iter():
                if elem.tag in ('StaffText', 'Dynamic', 'Spanner', 'Tempo', 'TimeSig', 'KeySig', 'HairPin', 'Tuplet'):
                    xml_str = ET.tostring(elem, encoding='unicode').strip()
                    # print on one line or short
                    lines = [l.strip() for l in xml_str.split('\n')]
                    print(f"  {elem.tag}: {' '.join(lines[:3])}")
