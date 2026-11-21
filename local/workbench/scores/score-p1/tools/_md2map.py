import re
path = r"local/workbench/scores/score-p1/downloads/beethoven-op125-i/sym9-mvmt1.md2"
lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
# 切 part 块
idx = []
for i, ln in enumerate(lines):
    if ln.startswith("score: part"):
        no = int(re.match(r"score: part (\d+)", ln).group(1))
        name = ""
        for j in range(i-1, max(0,i-6), -1):
            if lines[j].startswith("First Movement"):
                name = lines[j+1].strip(); break
        idx.append((no, name, i))
blocks = {}
for k,(no,name,start) in enumerate(idx):
    end = idx[k+1][2]-8 if k+1 < len(idx) else len(lines)
    blocks[no] = (name, lines[start:end])

def parse(no):
    name, body = blocks[no]
    Q = 24
    for ln in body:
        m = re.match(r"^\$\s+.*Q:(\d+)", ln)
        if m: Q = int(m.group(1)); break
    cur = None; meas = {}
    for ln in body:
        if ln.startswith("measure "):
            mm = re.match(r"measure (\d+)", ln)
            cur = int(mm.group(1)); meas.setdefault(cur, []); continue
        s = ln.strip()
        if not s or s[0] not in "ABCDEFGabcdefg": continue
        f = s.split()
        if len(f) < 3: continue
        try: divs = int(f[1].rstrip("-"))
        except ValueError: continue
        mnum = cur if cur is not None else 1
        meas.setdefault(mnum, []).append((f[0], divs))
    return name, Q, meas

print("%-28s %-4s %s" % ("part", "Q", "mm.1-35 内有音的 measure（音符数）"))
for no in range(1, 15):
    name, Q, meas = parse(no)
    hits = []
    for mm in sorted(meas):
        if 1 <= mm <= 35 and meas[mm]:
            hits.append("%d(%d)" % (mm, len(meas[mm])))
    print("%-28s %-4d %s" % (name[:28], Q, " ".join(hits) if hits else "— 全休止"))
