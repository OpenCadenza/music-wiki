import pathlib
p=pathlib.Path('provenance/techniques/structure/cadential-prinner-and-structural-closure.md')
t=p.read_text(encoding='utf-8')
t=t.replace('| William E. Caplin 论文 | Markus Neuwirth & Pieter Bergé 编《What Is a Cadence? Theoretical and Analytical...','| William E. Caplin 论文（经本地导读转述，原文 PDF 未入库） | Markus Neuwirth & Pieter Bergé 编《What Is a Cadence? Theoretical and Analytical...')
p.write_text(t,encoding='utf-8')
print('ok')
