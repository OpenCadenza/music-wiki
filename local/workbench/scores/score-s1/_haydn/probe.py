import sys
import xml.etree.ElementTree as ET
from collections import OrderedDict

path = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s1\_haydn\haydn-xml\score.xml"
tree = ET.parse(path)
root = tree.getroot()

# namespace
def strip_ns(tag):
    return tag.split('}')[-1] if '}' in tag else tag

part_list = None
parts = []
for elem in root.iter():
    t = strip_ns(elem.tag)
    if t == 'part':
        parts.append(elem)

print("num parts:", len(parts))
for p in parts:
    print("part id:", p.attrib.get('id'))

# collect score-level defaults
for p in parts:
    measures = [m for m in p if strip_ns(m.tag) == 'measure']
    print("part", p.attrib.get('id'), "measures:", len(measures))
    # detect movement boundaries: where <attributes><key><fifths> changes or <time> changes
    prev_key = None
    prev_time = None
    for m in measures:
        attrs = [a for a in m if strip_ns(a.tag) == 'attributes']
        for a in attrs:
            k = [x for x in a if strip_ns(x.tag) == 'key']
            t = [x for x in a if strip_ns(x.tag) == 'time']
            if k:
                fifths = [x for x in k[0] if strip_ns(x.tag) == 'fifths'][0].text
                if fifths != prev_key:
                    print("  measure", m.attrib.get('number'), "key fifths ->", fifths)
                    prev_key = fifths
            if t:
                beats = [x for x in t[0] if strip_ns(x.tag) == 'beats'][0].text
                btype = [x for x in t[0] if strip_ns(x.tag) == 'beat-type'][0].text
                tv = beats + "/" + btype
                if tv != prev_time:
                    print("  measure", m.attrib.get('number'), "time ->", tv)
                    prev_time = tv
    break
