path = r"local/workbench/scores/score-p1/downloads/beethoven-op125-i/sym9-mvmt1.md2"
lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
for i, ln in enumerate(lines):
    if ln.startswith("score: part"):
        # 往上找乐器名：通常是 First Movement 下面那一行
        for j in range(i-1, max(0,i-6), -1):
            if lines[j].startswith("First Movement"):
                print(ln.strip(), "|", lines[j+1].strip(), "|", lines[j+2].strip() if j+2 < len(lines) else "")
                break
