import re,sys
NAMES={'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
def parse(tok):
    # remove rhythms/brackets/articulations; find note patterns
    res=[]
    for m in re.finditer(r'[a-gA-G][#n-]*', tok):
        s=m.group(0); base=NAMES[s[0].lower()]
        acc=0
        for ch in s[1:]:
            if ch=='#': acc+=1
            elif ch=='-': acc-=1
            elif ch=='n': acc=0
        up=sum(1 for ch in s if ch.isupper()); low=sum(1 for ch in s if ch.islower())
        octv = 4 - up if up else 4 + (low-1)
        res.append(base+acc+12*octv)
    return res
def dump(path,wanted):
    lines=open(path,encoding='utf-8',errors='replace').read().splitlines()
    cur=None; data={}; keys={}
    for ln in lines:
        m=re.match(r'^=(\d+)',ln)
        if m: cur=int(m.group(1)); continue
        if cur is None: continue
        if ln.startswith('*k['): keys[cur]=ln.split('\t')[0]
        if cur in wanted and '\t' in ln and not ln.startswith('*') and not ln.startswith('!'):
            data.setdefault(cur,[]).append(ln)
    for b in wanted:
        rows=data.get(b,[])
        lh=[];rh=[]
        for ln in rows:
            parts=ln.split('\t')
            if parts and not parts[0].startswith('.'):
                toks=parts[0].split()
                for t in toks:
                    if re.search(r'[a-gA-G]',t): lh+=parse(t)
            if len(parts)>1 and not parts[1].startswith('.'):
                toks=parts[1].split()
                for t in toks:
                    if re.search(r'[a-gA-G]',t): rh+=parse(t)
        print(f'm.{b} key={keys.get(b,"")} LH={sorted(set(lh))} RH={sorted(set(rh))}')
dump(sys.argv[1],[int(x) for x in sys.argv[2].split(',')])
