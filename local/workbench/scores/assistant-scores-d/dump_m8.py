import xml.etree.ElementTree as ET
tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml')
m8 = tree.getroot().find('.//measure[@number="8"]')
print(ET.tostring(m8, encoding='utf-8').decode('utf-8'))
