"""扫描 mxl 全部小节的拍号/调号变化，定位各乐章起点。"""
import zipfile, sys
import xml.etree.ElementTree as ET

path = sys.argv[1]
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

# movement titles (work->movement)
for el in root.iter('movement-title'):
    print('movement-title =', el.text)

parts = list(root.iter('part'))
p0 = parts[0]
meas = list(p0.iter('measure'))
print('total measures in part1:', len(meas))
cur_time = cur_fifths = None
for i, m in enumerate(meas):
    a = m.find('attributes')
    if a is None:
        continue
    t = a.find('time')
    f = a.find('key')
    tt = None
    ff = None
    if t is not None:
        tt = '/'.join([x.text for x in t if x.tag in ('beats', 'beat-type')])
    if f is not None:
        ff = f.findtext('fifths')
    if tt != cur_time or ff != cur_fifths:
        print('idx=%d num=%s time=%s fifths=%s' % (i, m.get('number'), tt, ff))
        cur_time, cur_fifths = tt, ff