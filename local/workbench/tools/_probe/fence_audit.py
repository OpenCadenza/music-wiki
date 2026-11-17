import glob, io, re

fs = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
tot = inst = ids = gm = setmidi = 0
notempo = []
title_measure = 0
loc_measure = 0
for p in fs:
    t = io.open(p, encoding="utf-8").read()
    for attrs, body in re.findall(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        tot += 1
        if "instrumentName" in body:
            inst += 1
        if "\\tempo" not in body:
            notempo.append((p, attrs.strip()[:50]))
        if 'id="' in attrs:
            ids += 1
        gm += len(re.findall(r"%\s*GM\s*\d+", body))
        setmidi += body.count("\\set Staff.midiInstrument")
        m = re.search(r'title="([^"]*)"', attrs)
        l = re.search(r'location="([^"]*)"', attrs)
        if m and re.search(r"mm\.|小节", m.group(1)):
            title_measure += 1
        if l and re.search(r"[A-Za-z]", l.group(1)) is None:
            loc_measure += 1

print("围栏总数", tot)
print("含 instrumentName（会在谱面印乐器名）", inst)
print("含 \\set Staff.midiInstrument", setmidi, "｜含 % GM 注释", gm)
print("含 id 属性", ids)
print("缺 \\tempo 的围栏", len(notempo))
for x in notempo:
    print("  ", x)
print("title 里带小节范围（main 要求 title 只放作曲家/作品/乐章）", title_measure)
print("location 只有小节号无速度/乐章（main 要求含速度）", loc_measure)