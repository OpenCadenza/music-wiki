import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/ant_cad.xml')
root = tree.getroot()

# Check parts, measures 0 to 8
for p in root.findall('.//part'):
    measures = p.findall('measure')
    for m in measures[:9]:
        num = m.attrib.get('number')
        print(f"--- Measure {num} ---")
        for n in m.findall('note'):
            pitch = n.find('pitch')
            rest = n.find('rest')
            staff = n.find('staff').text if n.find('staff') is not None else '?'
            voice = n.find('voice').text if n.find('voice') is not None else '?'
            dur = n.find('type').text if n.find('type') is not None else '?'
            chord = n.find('chord') is not None
            stacc = n.find('.//staccato') is not None
            slur = [s.attrib.get('type') for s in n.findall('.//slur')]
            dyn = [d.tag for d in n.findall('.//dynamics/*')]
            if rest is not None:
                print(f"  s{staff}v{voice}: Rest {dur}")
            else:
                step = pitch.find('step').text
                alt = pitch.find('alter').text if pitch.find('alter') is not None else ''
                octv = pitch.find('octave').text
                print(f"  {'+' if chord else ' '}s{staff}v{voice}: {step}{alt}{octv} {dur} stacc={stacc} slur={slur} dyn={dyn}")
