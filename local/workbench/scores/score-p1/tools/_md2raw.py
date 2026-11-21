path = r"local/workbench/scores/score-p1/downloads/beethoven-op125-i/sym9-mvmt1.md2"
lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
# find part 9 (Violino I) block start
for i, ln in enumerate(lines):
    if ln.startswith("score: part 9 "):
        start = i
        break
for j in range(start, start+55):
    print(repr(lines[j]))
