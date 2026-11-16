import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/haydn, xv27.xml')
root = tree.getroot()

part = root.find('part')
for m in part.findall('measure')[:10]:
    num = m.attrib.get('number', '')
    notes = []
    for n in m.findall('note'):
        p = n.find('pitch')
        if p is not None:
            step = p.find('step').text
            octave = p.find('octave').text
            alter = p.find('alter')
            alt = '#' if alter is not None and alter.text == '1' else ''
            notes.append(f"{step}{alt}{octave}")
        else:
            notes.append("rest")
    print(f"Measure {num}: {' '.join(notes)}")
