import re,sys
lines=open(sys.argv[1],encoding="utf-8",errors="replace").read().splitlines()
cur=0
for ln in lines:
    m=re.match(r"^=(\d+)",ln)
    if m: cur=int(m.group(1))
    if "dolce" in ln.lower(): print(f"m.{cur}: {ln[:120]}")
