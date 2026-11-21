import re
path = r"local/resources/scores/source-packages/humdrum/mozart-sonatas/0016-16-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 1.abc"
lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
v1, v2 = [], []
for ln in lines:
    s = ln.strip()
    mt = re.match(r"\[V:(\d+)\]\s*(.*)$", s)
    if not mt: continue
    v = int(mt.group(1)); body = mt.group(2)
    (v1 if v == 1 else v2).append(body)
print("V1 lines", len(v1), "V2 lines", len(v2))
for i in range(0, 40):
    a = v1[i] if i < len(v1) else ""
    b = v2[i] if i < len(v2) else ""
    print("idx%-3d %s" % (i+1, a))
    print("       %s" % b)
