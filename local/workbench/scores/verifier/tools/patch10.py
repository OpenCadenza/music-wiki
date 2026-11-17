p='cmp_xml.py'
s=open(p,encoding='utf-8').read()
s=s.replace("""    text = open(ly, encoding='utf-8').read()
    blocks = C.split_vars(text)""",
"""    text = open(ly, encoding='utf-8').read()
    C.detect_key(text)
    blocks = C.split_vars(text)""")
open(p,'w',encoding='utf-8').write(s)
print('cmp_xml key wired')
