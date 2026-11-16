import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml')
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def to_midi(step, alter, octave):
    base = [0, 2, 4, 5, 7, 9, 11][["C", "D", "E", "F", "G", "A", "B"].index(step)]
    return (int(octave) + 1) * 12 + base + int(alter or 0)

notes = []
for m in tree.getroot().findall('.//measure'):
    m_num = int(m.attrib.get('number'))
    if m_num > 8: break
    for n in m.findall('note'):
        rest = n.find('rest')
        if rest is not None: continue
        pitch = n.find('pitch')
        step = pitch.find('step').text
        alter = pitch.find('alter')
        alt_val = int(alter.text) if alter is not None else 0
        octave = int(pitch.find('octave').text)
        mid = to_midi(step, alt_val, octave)
        voice = n.find('voice').text if n.find('voice') is not None else '?'
        staff = n.find('staff').text if n.find('staff') is not None else '?'
        dur = n.find('duration').text if n.find('duration') is not None else 'grace'
        name_str = f"{NOTE_NAMES[mid%12]}{mid//12-1}"
        notes.append((m_num, staff, voice, mid, name_str, dur))

print(f"Total notes in XML (mm 0-8): {len(notes)}")
for n in notes:
    print(f"M{n[0]} St{n[1]} V{n[2]}: {n[3]:3d} ({n[4]}) dur={n[5]}")
