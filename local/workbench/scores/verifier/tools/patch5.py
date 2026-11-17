p='kern2.py'
s=open(p,encoding='utf-8').read()
old = """            if t.strip() in ('.', ''):
                continue
            if t.split()[0] in ('r', 'rr'):
                cur[st].append((None, ()))
                continue
            dur = None; ps = []
            for sub in t.split():
                core = re.sub(r'[^0-9A-Ga-g#.-]', '', sub)"""
new = """            if t.strip() in ('.', ''):
                continue
            toks = t.split()
            if re.match(r'^[0-9.]*[rR]', toks[0]):
                cur[st].append((None, ()))
                continue
            dur = None; ps = []
            for sub in toks:
                if re.match(r'^[0-9.]*[rR]', sub):
                    continue
                core = re.sub(r'[^0-9A-Ga-g#.-]', '', sub)
                core = re.sub(r'[rR]', '', core)"""
assert old in s
s = s.replace(old, new)
open(p,'w',encoding='utf-8').write(s)
print('rest detection patched')
