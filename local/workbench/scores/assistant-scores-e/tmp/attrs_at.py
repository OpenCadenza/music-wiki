"""检查指定绝对小节的 attributes 块与 ending/barline 结构。"""
import zipfile, sys
import xml.etree.ElementTree as ET

path = sys.argv[1]
idxs = [int(x) for x in sys.argv[2:]]
if path.endswith('.mxl'):
    z = zipfile.ZipFile(path)
    n = [x for x in z.namelist() if x.lower().endswith('.xml') and 'META-INF' not in x]
    data = z.read(n[0])
else:
    data = open(path, 'rb').read()
root = ET.fromstring(data)
for el in root.iter():
    if '}' in el.tag:
        el.tag = el.tag.split('}', 1)[1]
parts = list(root.iter('part'))
p0 = parts[0]
meas = list(p0.iter('measure'))
for i in idxs:
    m = meas[i]
    print('==== idx=%d num=%s ====' % (i, m.get('number')))
    a = m.find('attributes')
    if a is not None:
        print('attributes:', ET.tostring(a, encoding='unicode').strip())
    for bl in m.iter('barline'):
        print('barline:', ET.tostring(bl, encoding='unicode').strip())