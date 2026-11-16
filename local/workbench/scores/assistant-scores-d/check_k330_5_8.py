import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml')
for m_num in range(5, 9):
    m = tree.getroot().find(f'.//measure[@number="{m_num}"]')
    print(f'=== Measure {m_num} ===')
    for elem in m:
        if elem.tag == 'note':
            pitch = elem.find('pitch')
            rest = elem.find('rest')
            grace = elem.find('grace')
            chord = elem.find('chord')
            dur = elem.find('duration')
            voice = elem.find('voice')
            staff = elem.find('staff')
            stem = elem.find('stem')
            type_elem = elem.find('type')
            acc = elem.find('accidental')
            dots = len(elem.findall('dot'))
            tie = elem.findall('.//tie') or elem.findall('.//tied')
            slurs = [s.attrib.get('type') for s in elem.findall('.//slur')]
            not_str = 'Rest' if rest is not None else f'{pitch.find("step").text}{pitch.find("octave").text}'
            if acc is not None: not_str += f'({acc.text})'
            g_str = 'GRACE ' if grace is not None else ''
            c_str = 'CHORD ' if chord is not None else ''
            print(f'  St{staff.text if staff is not None else "?"} V{voice.text if voice is not None else "?"}: {g_str}{c_str}{not_str} {type_elem.text if type_elem is not None else ""} dots={dots} dur={dur.text if dur is not None else "?"} stem={stem.text if stem is not None else ""} slur={slurs} ties={len(tie)}')
        elif elem.tag == 'direction':
            for w in elem.findall('.//words'): print(f'  [DIR] words={w.text}')
            for d in elem.findall('.//dynamics'): print(f'  [DIR] dyn={[c.tag for c in d]}')
