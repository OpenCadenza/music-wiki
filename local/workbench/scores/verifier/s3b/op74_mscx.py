"""读 DCML 的 MuseScore 源（.mscx），核对 Op.74 m.9 第 4 拍 Vln I 的 E 是否带降号。"""
import sys
import xml.etree.ElementTree as ET

BASE = r'E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\source-packages\dcml\ABC-main\ABC-main'
NAMES = {0: 'C', 1: 'G', 2: 'D', 3: 'A', 4: 'E', 5: 'B', 6: 'F#', 7: 'C#',
         -1: 'F', -2: 'Bb', -3: 'Eb', -4: 'Ab', -5: 'Db', -6: 'Gb', -7: 'Cb'}

for path in (BASE + r'\MS3\n10op74_01.mscx', BASE + r'\reviewed\n10op74_01_reviewed.mscx'):
    print('=' * 70)
    print(path)
    root = ET.parse(path).getroot()
    score = root.find('Score')
    staff = score.find("Staff[@id='1']")
    if staff is None:
        print('  no staff 1'); continue
    for mi, meas in enumerate(staff.findall('Measure'), start=1):
        if mi < 6 or mi > 10:
            continue
        out = []
        for ch in meas.iter('Chord'):
            staffno = ch.findtext('staff', default='1')
            if staffno != '1':
                continue
            for n in ch.findall('Note'):
                p = n.findtext('pitch')
                tpc = n.findtext('tpc') or n.findtext('tpc2')
                d = ch.findtext('duration')
                dot = len(ch.findall('dots'))
                out.append(f"pitch={p}({NAMES.get(int(tpc), tpc) if tpc else '?'},tpc={tpc}) d={d}"
                           + ('.' * dot))
        print(f'  m.{mi}: ' + ' | '.join(out))
