import re, io, sys
p='kern2.py'
s=open(p,encoding='utf-8').read()
s=s.replace("""            for sub in t.split():
                core = re.sub(r'[()\\[\\]{}<>LKJk~\\\\]', '', sub)""",
"""            for sub in t.split():
                core = re.sub(r'[^0-9A-Ga-g#.-]', '', sub)""")
open(p,'w',encoding='utf-8').write(s)

p2='cmp_staff.py'
s=open(p2,encoding='utf-8').read()
s=s.replace("""        if k in ('ws', 'comment', 'punct'):
            continue""",
"""        if k in ('ws', 'comment'):
            continue
        if k == 'punct':
            if t == '|':
                measures.append(cur); cur = []
            continue""")
open(p2,'w',encoding='utf-8').write(s)
print('patched')
