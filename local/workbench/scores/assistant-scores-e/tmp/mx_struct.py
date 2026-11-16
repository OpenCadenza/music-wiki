import sys, io, re, zipfile
import xml.etree.ElementTree as ET

path = sys.argv[1]
if path.endswith('.mxl'):
    z = zipfile.ZipFile(path)
    names = [n for n in z.namelist() if n.lower().endswith('.xml') and 'META-INF' not in n]
    data = z.read(names[0])
else:
    data = open(path, 'rb').read()

root = ET.fromstring(data)
for el in root.iter():
    if '}' in el.tag:
        el.tag = el.tag.split('}', 1)[1]

parts = list(root.iter('part'))
part = parts[0]
print('measures in part', part.get('id'), '=', len(list(part.iter('measure'))))
n = 0
for m in part.iter('measure'):
    n += 1
    attrs = m.find('attributes')
    info = []
    if attrs is not None:
        for k in ('divisions', 'key', 'time', 'staves', 'clef'):
            e = attrs.find(k)
            if e is not None:
                if k == 'key':
                    info.append('key fifths=%s mode=%s' % (e.findtext('fifths'), e.findtext('mode')))
                elif k == 'time':
                    info.append('time %s/%s' % (e.findtext('beats'), e.findtext('beat-type')))
                elif k == 'clef':
                    info.append('clef %s%s' % (e.findtext('sign'), e.findtext('line') or ''))
                else:
                    info.append('%s %s' % (k, e.text))
    dirs = [d.findtext('.//words') or d.findtext('.//metronome') or '' for d in m.findall('direction')]
    dirs = [d for d in dirs if d]
    barl = m.find('barline')
    bl = ''
    if barl is not None:
        bl = barl.findtext('bar-style') or ''
        rep = barl.find('repeat')
        if rep is not None:
            bl += ' repeat dir=' + (rep.get('direction') or '')
    if n <= 40 or info or bl:
        print(n, 'num=%s' % m.get('number'), '|', '; '.join(info), '|', dirs, '|', bl)
