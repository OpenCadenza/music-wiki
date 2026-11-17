import re
for p in ('cmp_staff.py','lyparse.py'):
    s=open(p,encoding='utf-8').read()
    s=s.replace("""    o = 4
    if om:
        o = 4 + len(om) if om[0] == "'" else 4 - len(om)
    return 12 * (o + 1) + p""",
"""    o = 3
    if om:
        o = 3 + len(om) if om[0] == "'" else 3 - len(om)
    return 12 * (o + 1) + p""")
    s=s.replace("""    octv = 4
    if octmark:
        if octmark[0] == "'": octv = 4 + len(octmark)
        else: octv = 4 - len(octmark)
    return 12 * (octv + 1) + p""",
"""    octv = 3
    if octmark:
        if octmark[0] == "'": octv = 3 + len(octmark)
        else: octv = 3 - len(octmark)
    return 12 * (octv + 1) + p""")
    open(p,'w',encoding='utf-8').write(s)
print('octave base fixed')
