import re,sys
path=sys.argv[1]
lines=open(path,encoding='utf-8',errors='replace').read().splitlines()
cur=0
for ln in lines:
    m=re.match(r'^=(\d+)',ln)
    if m: cur=int(m.group(1))
    if ln.startswith('*k['):
        print(f'm.{cur}: {ln.split(chr(9))[0]}')
