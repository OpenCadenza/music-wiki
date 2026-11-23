import pathlib
p=pathlib.Path('local/resources/catalog/score-board.md')
t=p.read_text(encoding='utf-8')
t=t.replace('| 贝多芬 Op.92 第二乐章 | mm.1–10 | 已回填（`beethoven-op92-ii-mm1-10`，verifier-4 核验） |\n','')
t=t.replace('| 贝多芬 Op.125 第一乐章 | mm.1–35 | 已回填（`beethoven-op125-i-mm1-35`，verifier-6 逐音核验） |\n','')
p.write_text(t,encoding='utf-8')
print('ok')
