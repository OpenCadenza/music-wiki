p='cmp_staff.py'
s=open(p,encoding='utf-8').read()
old = """    (?P<comment>%[^\\n]*)
  | (?P<chord><[^<>]*>)"""
new = """    (?P<comment>%[^\\n]*)
  | (?P<simul><<|>>)
  | (?P<vsep>\\\\\\\\)
  | (?P<chord><(?![<])[^<>]*>)"""
assert old in s, 'anchor missing'
s = s.replace(old, new)
s = s.replace("""        if k in ('ws', 'comment'):""",
"""        if k in ('ws', 'comment', 'simul', 'vsep'):""")
open(p,'w',encoding='utf-8').write(s)
print('simultaneous-block fix applied')
