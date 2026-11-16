import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n16op135_04.mscx')
root = tree.getroot()
score = root.find('Score')
staffs = score.findall('Staff')

for m_idx in range(165, 173):
    bar_no = m_idx
    for s_idx, staff in enumerate(staffs):
        m = staff.findall('Measure')[m_idx]
        for elem in m.iter('StaffText'):
            txt = ''.join(elem.itertext()).strip()
            print(f"Bar {bar_no} Staff {s_idx+1}: StaffText = '{txt}'")
