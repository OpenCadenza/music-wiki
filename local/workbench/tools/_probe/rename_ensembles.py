import pathlib
p=pathlib.Path('content/ensembles/index.md')
t=p.read_text(encoding='utf-8')
t=t.replace('title: 室内乐与重奏编制','title: 编制')
t=t.replace('description: 探讨不同室内乐编制（弦乐四重奏、管乐五重奏、钢琴三重奏等）的声学异质性、声部角色分工、和声几何排布与声学平衡机制。','description: 探讨不同编制（弦乐四重奏、管乐五重奏、钢琴三重奏等）的声学异质性、声部角色分工、和声几何排布与声学平衡机制。')
t=t.replace('# 室内乐\n','# 编制\n',1)
p.write_text(t,encoding='utf-8')
print('ok')
