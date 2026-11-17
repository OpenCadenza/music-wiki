# -*- coding: utf-8 -*-
import os, sys
from lxml import etree

BASE = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s9\src"
FILES = {
    "A": os.path.join(BASE, "src2_125808.xml"),
    "B": os.path.join(BASE, "src3_98865.xml"),
    "C": os.path.join(BASE, "src4_99688.xml"),
}
which = sys.argv[1] if len(sys.argv) > 1 else 'A'
part = sys.argv[2] if len(sys.argv) > 2 else 'P1'
meas = int(sys.argv[3]) if len(sys.argv) > 3 else 1
nmeas = int(sys.argv[4]) if len(sys.argv) > 4 else 1

root = etree.parse(FILES[which]).getroot()
sp = root.find(f"./part[@id='{part}']")
ms = sp.findall('./measure')
for mm in ms[meas-1:meas-1+nmeas]:
    print("="*40, "measure", mm.get('number'))
    print(etree.tostring(mm, pretty_print=True, encoding='unicode'))
