import xml.etree.ElementTree as ET
tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml')
m3 = tree.getroot().find('.//measure[@number="3"]')
for n in m3.findall('note'):
    print(ET.tostring(n, encoding='utf-8').decode('utf-8'))
for d in m3.findall('.//dynamics'):
    print('DYN:', [c.tag for c in d])
