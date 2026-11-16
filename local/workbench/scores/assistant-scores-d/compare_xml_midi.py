import sys
sys.path.append("local/workbench/tools")
from midi_pitch_check import parse_midi
import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml')
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def to_midi(step, alter, octave):
    base = [0, 2, 4, 5, 7, 9, 11][["C", "D", "E", "F", "G", "A", "B"].index(step)]
    return (int(octave) + 1) * 12 + base + int(alter or 0)

xml_notes = []
for m in tree.getroot().findall('.//measure'):
    m_num = int(m.attrib.get('number'))
    if m_num > 8: break
    for n in m.findall('note'):
        if n.find('rest') is not None: continue
        p = n.find('pitch')
        alt = p.find('alter')
        alt_val = int(alt.text) if alt is not None else 0
        mid = to_midi(p.find('step').text, alt_val, int(p.find('octave').text))
        voice = n.find('voice').text if n.find('voice') is not None else '?'
        staff = n.find('staff').text if n.find('staff') is not None else '?'
        grace = n.find('grace') is not None
        tie = n.find('.//tie') is not None or n.find('.//tied') is not None
        xml_notes.append((m_num, staff, voice, mid, grace, tie))

midi_notes, div = parse_midi("local/workbench/scores/assistant-scores-d/mozart-k330-mvt2-mm1-8.mid")

print(f"XML note count: {len(xml_notes)}")
print(f"MIDI note count: {len(midi_notes)}")
print(f"XML grace notes count: {sum(1 for x in xml_notes if x[4])}")
print(f"XML tied notes count: {sum(1 for x in xml_notes if x[5])}")
