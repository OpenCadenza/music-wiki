import zipfile, os, sys
from lxml import etree

SRC = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\origin_resources\downloads\2026-11-17\pdmx\extract"
OUT = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s9\src"

os.makedirs(OUT, exist_ok=True)

files = []
for root, dirs, fs in os.walk(SRC):
    for f in fs:
        if f.endswith('.mxl') or '.' not in f:
            files.append(os.path.join(root, f))

print("== found", len(files))
info = []
for i, p in enumerate(files):
    tag = os.path.basename(os.path.dirname(p)) + "_" + str(i)
    size = os.path.getsize(p)
    print("\n----", p, size)
    try:
        z = zipfile.ZipFile(p)
    except Exception as e:
        print("  not a zip:", e)
        continue
    names = z.namelist()
    print("  zip entries:", names)
    xmls = [n for n in names if n.lower().endswith('.xml') and 'META-INF' not in n]
    if not xmls:
        print("  NO XML")
        continue
    data = z.read(xmls[0])
    dest = os.path.join(OUT, f"src{i}_{size}.xml")
    open(dest, 'wb').write(data)
    root_el = etree.fromstring(data)
    def txt(path):
        e = root_el.find(path)
        return (e.text or '').strip() if e is not None else None
    print("  work-title:", txt('./work/work-title'))
    print("  movement-title:", txt('./movement-title'))
    print("  movement-number:", txt('./movement-number'))
    parts = root_el.findall('./part-list/score-part')
    print("  parts:", [(pt.get('id'), (pt.findtext('part-name') or '').strip()) for pt in parts])
    scoreparts = root_el.findall('./part')
    for sp in scoreparts:
        pid = sp.get('id')
        meas = sp.findall('./measure')
        print(f"   part {pid}: {len(meas)} measures, first@ {meas[0].get('number') if meas else None}, last@ {meas[-1].get('number') if meas else None}")
    print("  saved ->", dest)
