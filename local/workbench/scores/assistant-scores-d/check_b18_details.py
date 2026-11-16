import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/beethoven_18_2.xml')
root = tree.getroot()

for p in root.findall('.//part'):
    pid = p.attrib.get('id')
    pname_el = root.find(f'.//score-part[@id="{pid}"]/part-name')
    pname = pname_el.text if pname_el is not None else pid
    print(f"\n=== {pname} ===")
    for m in p.findall('measure'):
        num = int(m.attrib.get('number'))
        if num > 8: break
        dyns = [d.text for d in m.findall('.//dynamics/*')]
        slurs = [s.attrib for s in m.findall('.//slur')]
        words = [w.text for w in m.findall('.//words')]
        print(f"M{num}: dyns={dyns} words={words} slurs={slurs}")
