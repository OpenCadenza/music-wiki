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
# strip namespaces
for el in root.iter():
    if '}' in el.tag:
        el.tag = el.tag.split('}', 1)[1]

print('== part-list ==')
for sp in root.iter('score-part'):
    print(' ', sp.get('id'), sp.findtext('part-name'))
print('== metadata ==')
for tag in ('work-title', 'movement-title', 'movement-number'):
    for el in root.iter(tag):
        print(tag, '=', el.text)
for el in root.iter('creator'):
    print('creator', el.get('type'), '=', el.text)
print('== staves ==')
for part in root.iter('part'):
    st = part.find('.//staves')
    print(' part', part.get('id'), 'staves:', st.text if st is not None else '(default 1)')
