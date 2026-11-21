import re
path = r"local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet14-7.krn"
raw = open(path, encoding="utf-8", errors="replace").read().splitlines()
cur=None
for ln in raw:
    if ln.startswith("="):
        cur = ln.split("\t")[0].strip("=!|:")
        continue
    if cur in ("19","20","21","22","23","24","25","26","27") and ln.strip() and not ln.startswith("*") and not ln.startswith("!"):
        print("m%-4s %s" % (cur, ln))
