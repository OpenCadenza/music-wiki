import glob, io, re
from collections import Counter

files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
tot_staff = tot_midi = tot_inst = tot_gm = 0
bad = []
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        body = m.group(2)
        n = len(re.findall(r"\\new Staff", body))
        k = len(re.findall(r"\\set Staff\.midiInstrument", body)) + len(re.findall(r"midiInstrument\s*=", body))
        tot_staff += n
        tot_midi += k
        tot_inst += len(re.findall(r"instrumentName", body))
        tot_gm += len(re.findall(r"%\s*GM\s*\d+", body))
        if n != k:
            bad.append((p, n, k))
print("staff 总数:", tot_staff, "｜乐器声明:", tot_midi, "｜残留 instrumentName:", tot_inst, "｜残留 GM 注释:", tot_gm)
for b in bad:
    print("不匹配:", b)

print("\n剩余含 instrumentName 的围栏片段：")
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        if "instrumentName" in m.group(2):
            idx = m.group(2).find("instrumentName")
            print(" ", p, "|", m.group(2)[max(0, idx - 120): idx + 160].replace("\n", " / "))
print("\n剩余含 midiInstrument 但未转 \\set 的：")
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        if re.search(r"midiInstrument\s*=", m.group(2)):
            idx = re.search(r"midiInstrument\s*=", m.group(2)).start()
            print(" ", p, "|", m.group(2)[max(0, idx - 120): idx + 120].replace("\n", " / "))