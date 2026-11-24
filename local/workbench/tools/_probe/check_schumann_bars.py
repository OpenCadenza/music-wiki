import zipfile, xml.etree.ElementTree as ET, sys

sys.stdout.reconfigure(encoding='utf-8')

def check_song(fn, bars):
    z = zipfile.ZipFile('local/workbench/scores/score-r3/downloads/schumann-dichterliebe/' + fn)
    xml_name = [x for x in z.namelist() if x.endswith('.xml') and not x.startswith('META-INF')][0]
    tree = ET.fromstring(z.read(xml_name))
    parts = tree.findall('part')
    print(f'=== {fn} ===')
    for b in bars:
        vm = parts[0].findall('measure')[b-1]
        pm = parts[1].findall('measure')[b-1]
        v_notes = []
        for n in vm.findall('note'):
            if n.find('rest') is not None: continue
            p = n.find('pitch')
            if p is not None:
                alt = p.find('alter').text if p.find('alter') is not None else ''
                alts = '#' if alt=='1' else ('b' if alt=='-1' else '')
                v_notes.append(p.find('step').text + alts + p.find('octave').text)
        p_notes = []
        for n in pm.findall('note'):
            if n.find('rest') is not None: continue
            p = n.find('pitch')
            if p is not None:
                alt = p.find('alter').text if p.find('alter') is not None else ''
                alts = '#' if alt=='1' else ('b' if alt=='-1' else '')
                p_notes.append(p.find('step').text + alts + p.find('octave').text)
        words = [w.text for w in pm.findall('.//words') if w.text]
        v_lyric = ' '.join([ly.find('.//text').text for ly in vm.findall('.//lyric') if ly.find('.//text') is not None])
        print(f'm.{b}: Voice={v_notes} lyric="{v_lyric}" | Piano={p_notes[:8]} words={words}')

check_song('op48-01_Im_wunderschönen_Monat_Mai.mxl', [1, 2, 4, 12, 13, 23, 25, 26])
check_song('op48-08_Und_wüssten-s_die_Blumen.mxl', [1, 20, 31, 32, 33, 36, 38])
check_song('op48-12_Am_leuchtenden_Sommermorgen.mxl', [1, 15, 20, 21, 23, 27, 30])
check_song('op48-16_Die_alten-_bösen_Lieder.mxl', [1, 40, 52, 53, 54, 59, 63, 67])
