import re
path = r"local/resources/scores/source-packages/humdrum/mozart-sonatas/0016-16-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 1.abc"
lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
meas = {}
for ln in lines:
    s = ln.strip()
    mt = re.match(r"\[V:(\d+)\]\s*(.*)$", s)
    if not mt: continue
    v = int(mt.group(1)); body = mt.group(2)
    if v == 1:
        cur = meas.setdefault("n", 0) + 1
        meas["n"] = cur
    meas.setdefault(v, []).append(body)
for k in sorted(k for k in meas if k != "n"):
    pass
n = meas.get("n", 0)
print("measures:", n)
for m in range(13, 27):
    for v in (1, 2):
        arr = meas.get(v, [])
        if m-1 < len(arr):
            print("m%-3d V%d: %s" % (m, v, arr[m-1]))
    print()
