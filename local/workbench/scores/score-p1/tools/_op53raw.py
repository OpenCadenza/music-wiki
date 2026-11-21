path = r"local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata21-1.krn"
raw = open(path, encoding="utf-8", errors="replace").read().splitlines()
cur=None
for ln in raw:
    if ln.startswith("="):
        cur = ln.split("\t")[0].strip("=!|:")
        continue
    if cur in ("3","7","9","11","13","14") and ln.strip() and not ln.startswith("*") and not ln.startswith("!"):
        f = ln.split("\t")
        print("m%-3s LH=%-14s RH=%s" % (cur, f[0], f[1] if len(f)>1 else ""))
