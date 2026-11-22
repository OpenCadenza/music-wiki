import sys,re
lines=open(sys.argv[1],encoding='utf-8',errors='replace').read().splitlines()
body=[]; inbody=False
for ln in lines:
    if ln.startswith('K:'): inbody=True; continue
    if not inbody or ln.startswith('%') or not ln.strip(): continue
    body.append(ln.strip())
s=' '.join(body)
bars=[b.strip() for b in s.split('|')]
print('total bars',len(bars))
for i in range(40,56):
    if i < len(bars): print(f'--- bar {i+1} ---'); print(bars[i][:400])
