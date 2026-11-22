import re,sys
def dump(path, wanted):
    lines=open(path,encoding='utf-8',errors='replace').read().splitlines()
    spines=0; cur=None; out={}
    for ln in lines:
        if ln.startswith('**'): spines=ln.count('**'); continue
        m=re.match(r'^=(\d+)',ln)
        if m:
            cur=int(m.group(1)); continue
        if cur in wanted and '\t' in ln:
            out.setdefault(cur,[]).append(ln)
    for b in wanted:
        print(f'--- m.{b} ---')
        for ln in out.get(b,[]): print(ln)
dump(sys.argv[1], [int(x) for x in sys.argv[2].split(',')])
