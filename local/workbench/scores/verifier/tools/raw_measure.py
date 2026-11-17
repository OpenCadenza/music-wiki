import sys
from lxml import etree

XML = r"local\workbench\scores\score-s2\downloads\mozart-mxl\sq7471661.xml"
tree = etree.parse(XML)
root = tree.getroot()
p1 = root.findall("./part")[0]
ms = p1.findall("./measure")
for idx in (int(x) for x in sys.argv[1:]):
    m = ms[idx - 1]
    print("\n===== part 1, index %d, number=%s =====" % (idx, m.get("number")))
    print(etree.tostring(m, pretty_print=True, encoding="unicode"))
