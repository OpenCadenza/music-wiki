import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/scores/source-packages/dcml/ABC-main/ABC-main/reviewed/n02op18-2_04_reviewed.mscx')
root = tree.getroot()

# Find parts and staves
parts = root.findall('.//Part')
print('Parts:', len(parts))
for p in parts:
    track_name = p.find('.//trackName')
    name = track_name.text if track_name is not None else '?'
    print('Part:', name)

# Let's inspect measures 1-8
measures = root.findall('.//Measure')
print('Total measures:', len(measures))

# In MuseScore 3 mscx, measures contain Voice elements for each staff
for idx in range(min(8, len(measures))):
    m = measures[idx]
    print(f'=== Measure {idx+1} ===')
    # Staves/voices
    voices = m.findall('voice')
    for v_idx, v in enumerate(voices):
        elements = []
        for child in v:
            if child.tag == 'Chord':
                notes = [n.find('pitch').text for n in child.findall('Note')]
                dur = child.find('durationType').text if child.find('durationType') is not None else '?'
                dots = child.find('dots') is not None
                artic = [a.find('subtype').text for a in child.findall('Articulation') if a.find('subtype') is not None]
                elements.append(f'Chord(p={notes}, dur={dur}, dots={dots}, art={artic})')
            elif child.tag == 'Rest':
                dur = child.find('durationType').text if child.find('durationType') is not None else '?'
                elements.append(f'Rest({dur})')
            elif child.tag == 'Dynamic':
                subtype = child.find('subtype').text if child.find('subtype') is not None else '?'
                elements.append(f'Dyn({subtype})')
        print(f'  Voice {v_idx}: {elements}')
