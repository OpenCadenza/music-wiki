import xml.etree.ElementTree as ET

tree = ET.parse('local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n16op135_04.mscx')
root = tree.getroot()
score = root.find('Score')
staffs = score.findall('Staff')

# Print measure texts, hairpins, dynamics for Measure count 166 to 173 (which correspond to mm. 165-172)
for m_idx in range(165, 173):
    m_real = m_idx + 1 # 1-based measure count in MSCX (166 to 173)
    bar_no = m_idx     # 165 to 172
    print(f"\n==========================================")
    print(f"=== BAR {bar_no} (MSCX measure count {m_real}) ===")
    print(f"==========================================")
    for s_idx, staff in enumerate(staffs):
        s_id = staff.get('id')
        m = staff.findall('Measure')[m_idx]
        print(f"  -- Staff {s_idx + 1} (id={s_id}) --")
        for voice in m.findall('voice'):
            for child in voice:
                if child.tag == 'StaffText':
                    t = child.find('text')
                    print(f"     [StaffText] {t.text if t is not None else ''}")
                elif child.tag == 'Dynamic':
                    sub = child.find('subtype')
                    print(f"     [Dynamic] {sub.text if sub is not None else ''}")
                elif child.tag == 'Spanner':
                    sp_type = child.get('type')
                    hp = child.find('HairPin')
                    sub = hp.find('subtype').text if hp is not None and hp.find('subtype') is not None else ''
                    print(f"     [Spanner {sp_type}] subtype={sub}")
                elif child.tag == 'Chord':
                    d = child.find('durationType')
                    notes = child.findall('Note')
                    trem = child.find('Tremolo')
                    articulations = child.findall('Articulation')
                    art_types = [a.find('subtype').text for a in articulations if a.find('subtype') is not None]
                    trem_str = f"trem:{trem.find('subtype').text}" if trem is not None else ""
                    pitches = []
                    for n in notes:
                        p = n.find('pitch').text if n.find('pitch') is not None else ''
                        tpc = n.find('tpc').text if n.find('tpc') is not None else ''
                        tie = n.find('Spanner')
                        pitches.append(f"p:{p}(tpc:{tpc})")
                    print(f"     Chord dur={d.text} {' '.join(pitches)} {trem_str} arts={art_types}")
                elif child.tag == 'Rest':
                    d = child.find('durationType')
                    print(f"     Rest dur={d.text if d is not None else ''}")
