import zipfile, xml.etree.ElementTree as ET, sys, os

sys.stdout.reconfigure(encoding='utf-8')

dir_path = 'local/workbench/scores/score-r3/downloads/schumann-dichterliebe'
files = sorted([f for f in os.listdir(dir_path) if f.endswith('.mxl')])

print('=== Schumann Dichterliebe Op.48 16 Songs Overview ===')
for idx, f in enumerate(files):
    zp = os.path.join(dir_path, f)
    z = zipfile.ZipFile(zp)
    xml_name = [x for x in z.namelist() if x.endswith('.xml') and not x.startswith('META-INF')][0]
    tree = ET.fromstring(z.read(xml_name))
    parts = tree.findall('part')
    p0_m = parts[0].findall('measure')
    m0 = p0_m[0]
    t = m0.find('.//time')
    time_str = f"{t.find('beats').text}/{t.find('beat-type').text}" if t is not None else "?"
    k = m0.find('.//key')
    fifths = k.find('fifths').text if k is not None and k.find('fifths') is not None else "?"
    title = f.split('_')[1]
    print(f"No.{idx+1:02d}: bars={len(p0_m):2d}, fifths={fifths:2s}, time={time_str:4s} | {f}")

def inspect_details(num_str):
    match_file = [f for f in files if f.startswith(f"op48-{num_str}")][0]
    zp = os.path.join(dir_path, match_file)
    z = zipfile.ZipFile(zp)
    xml_name = [x for x in z.namelist() if x.endswith('.xml') and not x.startswith('META-INF')][0]
    tree = ET.fromstring(z.read(xml_name))
    parts = tree.findall('part')
    print(f"\n--- Detailed inspection of {match_file} ---")
    measures = parts[0].findall('measure')
    p_measures = parts[1].findall('measure')
    for m_idx in range(len(measures)):
        m_num = m_idx + 1
        vm = measures[m_idx]
        pm = p_measures[m_idx]
        words = [w.text for w in pm.findall('.//words') if w.text]
        v_lyrics = ' '.join([ly.find('.//text').text for ly in vm.findall('.//lyric') if ly.find('.//text') is not None])
        k = vm.find('.//key') or pm.find('.//key')
        k_str = f"fifths:{k.find('fifths').text}" if k is not None and k.find('fifths') is not None else ""
        if words or k_str or m_num in [1, 2, 3, len(measures)-2, len(measures)-1, len(measures)]:
            print(f"m.{m_num:2d} {k_str}: words={words} lyric='{v_lyrics}'")

inspect_details('01')
inspect_details('08')
inspect_details('12')
inspect_details('16')
