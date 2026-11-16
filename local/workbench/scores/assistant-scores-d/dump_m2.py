import xml.etree.ElementTree as ET
tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml')
m2 = tree.getroot().find('.//measure[@number="2"]')
for n in m2.findall('note'):
    print(ET.tostring(n, encoding='utf-8').decode('utf-8'))
