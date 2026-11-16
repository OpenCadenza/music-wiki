import xml.etree.ElementTree as ET

for name in ['beethoven_18_2.xml', 'ant_cad.xml', 'beethovenop30.xml']:
    path = f'local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/{name}'
    tree = ET.parse(path)
    root = tree.getroot()
    parts = [p.text for p in root.findall('.//part-name')]
    m1 = root.find('.//measure[@number="1"]')
    fifths = m1.find('.//key/fifths').text if m1.find('.//key/fifths') is not None else '?'
    beats = m1.find('.//time/beats').text if m1.find('.//time/beats') is not None else '?'
    beattype = m1.find('.//time/beat-type').text if m1.find('.//time/beat-type') is not None else '?'
    words = [w.text for w in m1.findall('.//words')]
    m_count = len(root.findall('.//part[1]/measure'))
    print(f"=== {name} ===")
    print(f"  Parts: {parts}")
    print(f"  Key (fifths): {fifths}, Time: {beats}/{beattype}")
    print(f"  Words: {words}")
    print(f"  Measure count: {m_count}")
