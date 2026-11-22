import re,sys
NAMES={'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
def parse(tok):
    res=[]
    for m in re.finditer(r'[a-gA-G][#n-]*', tok):
        s=m.group(0); base=NAMES[s[0].lower()]; acc=0
        for ch in s[1:]:
            if ch=='#':acc+=1
            elif ch=='-':acc-=1
            elif ch=='n':acc=0
        up=sum(1 for ch in s if ch.isupper()); low=sum(1 for ch in s if ch.islower())
        octv = 4-up if up else 4+(low-1)
        res.append(base+acc+12*octv)
    return res
path=sys.argv[1]; lo,hi=[int(x) for x in sys.argv[2].split('-')]
lines=open(path,encoding='utf-8',errors='replace').read().splitlines()
cur=0; data={}
for ln in lines:
    m=re.match(r'^=(\d+)',ln)
    if m: cur=int(m.group(1)); continue
    if lo<=cur<=hi and '\t' in ln and not ln.startswith(('*','!')):
        data.setdefault(cur,[]).append(ln)
for b in sorted(data):
    lh=[];rh=[]
    for ln in data[b]:
        p=ln.split('\t')
        for t in p[0].split():
            if re.search(r'[a-gA-G]',t): lh+=parse(t)
        if len(p)>1:
            for t in p[1].split():
                if re.search(r'[a-gA-G]',t): rh+=parse(t)
    pc=lambda xs: sorted(set(x%12 for x in xs))
    print(f'm.{b} LHpc={pc(lh)} low={min(lh) if lh else None} RHpc={pc(rh)}')
