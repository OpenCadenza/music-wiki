import re
p='cmp_staff.py'
s=open(p,encoding='utf-8').read()

# 1) expand multimeasure rests into separate measures
s = s.replace("""            if d and not in_aftergrace:
                for _ in range(mult):
                    cur.append(('R', None, d))
            skip_grace = False
            continue""",
"""            if d and not in_aftergrace:
                if mult > 1:
                    for _ in range(mult):
                        cur.append(('R', None, d))
                        measures.append(cur); cur = []
                else:
                    cur.append(('R', None, d))
            skip_grace = False
            continue""")

# 2) add set-based comparison inside the reporting loop
s = s.replace("""            A = collections.Counter(a); B = collections.Counter(b)""",
"""            A = collections.Counter(a); B = collections.Counter(b)
            SA = set(x for x, _ in a); SB = set(x for x, _ in b)""")
s = s.replace("""            ok = 'OK  ' if A == B else 'DIFF'
            print(f"[{ok}] m{n} staff{st}  ly={totA:g} kern={totB:g}")
            if A != B:""",
"""            ok = 'OK  ' if A == B else 'DIFF'
            sok = 'OK  ' if SA == SB else 'SET!'
            print(f"[{ok}/{sok}] m{n} staff{st}  ly={totA:g} kern={totB:g}")
            if SA != SB:
                miss = sorted(SB - SA); extra = sorted(SA - SB)
                if miss:  print('        kern-only pitches: ' + ', '.join(nm(x) for x in miss))
                if extra: print('        ly-only   pitches: ' + ', '.join(nm(x) for x in extra))
                continue
            if A != B:""")
open(p,'w',encoding='utf-8').write(s)
print('patched sets')
