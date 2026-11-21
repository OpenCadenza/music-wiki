path = r"local/workbench/scores/score-p1/downloads/beethoven-op125-i/sym9-mvmt1.md2"
lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
for want in (10, 12, 5):
    for i, ln in enumerate(lines):
        if ln.startswith("score: part %d " % want):
            start = i
            break
    print("########## part %d ##########" % want)
    for j in range(start, start+34):
        print(repr(lines[j]))
