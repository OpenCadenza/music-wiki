import glob, io, re
from collections import Counter

vals = Counter()
patterns = Counter()
for p in [q for q in glob.glob("content/**/*.md", recursive=True) if not q.endswith("index.md")]:
    t = io.open(p, encoding="utf-8").read()
    for attrs, body in re.findall(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        for m in re.finditer(r"\\new\s+Staff[^{]*\{", body):
            patterns["with" if "\\with" in body[max(0, m.start() - 5):m.end()] else "plain"] += 1
        for m in re.finditer(r'midiInstrument\s*=\s*"([^"]+)"', body):
            vals[m.group(1)] += 1
        for m in re.finditer(r"%\s*GM\s*\d+", body):
            patterns["gm_comment"] += 1
        for m in re.finditer(r"instrumentName\s*=\s*\"([^\"]*)\"", body):
            patterns["instrumentName"] += 1
print("midiInstrument 取值:")
for k, v in vals.most_common():
    print("  ", repr(k), v)
print("\n统计:", dict(patterns))