import re
for p in ('cmp_staff.py','lyparse.py'):
    s=open(p,encoding='utf-8').read()
    s=s.replace("(?:''+|,,+)?", "(?:'+|,+)?")
    open(p,'w',encoding='utf-8').write(s)
    print(p, 'quote fix', s.count("(?:'+|,+)?"))
# multimeasure rest measure counting
p='cmp_staff.py'
s=open(p,encoding='utf-8').read()
s=s.replace("""                if mult > 1:
                    for _ in range(mult):
                        cur.append(('R', None, d))
                        measures.append(cur); cur = []""",
"""                if mult > 1:
                    for k in range(mult):
                        cur.append(('R', None, d))
                        if k < mult - 1:
                            measures.append(cur); cur = []""")
open(p,'w',encoding='utf-8').write(s)
print('rest fix done')
