import zipfile, xml.etree.ElementTree as ET, sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_no2():
    z2 = zipfile.ZipFile('local/workbench/scores/score-r3/downloads/debussy-ariettes/ariettes-2-Il-pleure.mxl')
    xml_name = [f for f in z2.namelist() if f.endswith('.xml') and not f.startswith('META-INF')][0]
    tree = ET.fromstring(z2.read(xml_name))
    parts = tree.findall('part')
    print('=== No. 2 Il pleure dans mon coeur (80 bars) ===')
    
    # check tempo / directions
    for m_idx in range(len(parts[0].findall('measure'))):
        m_num = m_idx + 1
        v_m = parts[0].findall('measure')[m_idx]
        p_m = parts[1].findall('measure')[m_idx]
        
        words = [w.text for w in p_m.findall('.//words') if w.text]
        v_words = [w.text for w in v_m.findall('.//words') if w.text]
        v_lyric = ' '.join([ly.find('.//text').text for ly in v_m.findall('.//lyric') if ly.find('.//text') is not None])
        
        # print measures with words or lyrics or key changes
        key = v_m.find('.//key') or p_m.find('.//key')
        k_str = f"fifths:{key.find('fifths').text}" if key is not None and key.find('fifths') is not None else ""
        
        if words or v_words or v_lyric or k_str or m_num in [1, 2, 3, 9, 10, 11, 14, 15, 20, 25, 30, 40, 50, 60, 70, 80]:
            print(f"m.{m_num} {k_str}: words={words+v_words} lyric='{v_lyric}'")

def inspect_no4():
    z4 = zipfile.ZipFile('local/workbench/scores/score-r3/downloads/debussy-ariettes/ariettes-4-Paysages-belges.mxl')
    xml_name = [f for f in z4.namelist() if f.endswith('.xml') and not f.startswith('META-INF')][0]
    tree = ET.fromstring(z4.read(xml_name))
    parts = tree.findall('part')
    print('\n=== No. 4 Paysages belges. Chevaux de bois (102 bars) ===')
    
    for m_idx in range(len(parts[0].findall('measure'))):
        m_num = m_idx + 1
        v_m = parts[0].findall('measure')[m_idx]
        p_m = parts[1].findall('measure')[m_idx]
        
        words = [w.text for w in p_m.findall('.//words') if w.text]
        v_words = [w.text for w in v_m.findall('.//words') if w.text]
        v_lyric = ' '.join([ly.find('.//text').text for ly in v_m.findall('.//lyric') if ly.find('.//text') is not None])
        
        key = v_m.find('.//key') or p_m.find('.//key')
        k_str = f"fifths:{key.find('fifths').text}" if key is not None and key.find('fifths') is not None else ""
        
        if words or v_words or v_lyric or k_str or m_num in [1, 2, 3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 102]:
            print(f"m.{m_num} {k_str}: words={words+v_words} lyric='{v_lyric}'")

if __name__ == '__main__':
    inspect_no2()
    inspect_no4()
