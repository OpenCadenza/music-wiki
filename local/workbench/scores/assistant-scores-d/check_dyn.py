import xml.etree.ElementTree as ET
tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml')
for m in tree.getroot().findall('.//measure'):
    num = m.attrib.get('number')
    if int(num) <= 8:
        for d in m.findall('.//direction'):
            for dyn in d.findall('.//dynamics'):
                print(f'M{num}: {[c.tag for c in dyn]} staff={d.find("staff").text if d.find("staff") is not None else "?"}')
            for w in d.findall('.//words'):
                print(f'M{num}: words="{w.text}" staff={d.find("staff").text if d.find("staff") is not None else "?"}')
