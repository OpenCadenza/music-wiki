import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/beethovenop30.xml')
root = tree.getroot()

for p in root.findall('.//part'):
    measures = p.findall('measure')
    for m in measures:
        num = m.attrib.get('number')
        print(f"=== Measure {num} ===")
        # directions (dynamics, tempo, etc.)
        for d in m.findall('.//direction'):
            dyn = [x.tag for x in d.findall('.//dynamics/*')]
            words = [x.text for x in d.findall('.//words')]
            print(f"  Direction: dyn={dyn} words={words}")
        for n in m.findall('note'):
            pitch = n.find('pitch')
            rest = n.find('rest')
            staff = n.find('staff').text if n.find('staff') is not None else '?'
            voice = n.find('voice').text if n.find('voice') is not None else '?'
            dur = n.find('type').text if n.find('type') is not None else '?'
            chord = n.find('chord') is not None
            grace = n.find('grace') is not None
            dot = n.find('dot') is not None
            stacc = n.find('.//staccato') is not None
            slurs = [s.attrib.get('type') for s in n.findall('.//slur')]
            ties = [t.attrib.get('type') for t in n.findall('.//tie')]
            ornaments = [o.tag for o in n.findall('.//ornaments/*')]
            dyns = [x.tag for x in n.findall('.//dynamics/*')]
            if rest is not None:
                print(f"  s{staff}v{voice}: Rest {dur}{'.' if dot else ''}")
            else:
                step = pitch.find('step').text
                alt = pitch.find('alter').text if pitch.find('alter') is not None else ''
                octv = pitch.find('octave').text
                acc = ''
                if alt == '1': acc = '#'
                elif alt == '-1': acc = 'b'
                print(f"  {'+' if chord else ' '}s{staff}v{voice}: {'grace ' if grace else ''}{step}{acc}{octv} {dur}{'.' if dot else ''} stacc={stacc} slurs={slurs} ties={ties} orn={ornaments} dyns={dyns}")
