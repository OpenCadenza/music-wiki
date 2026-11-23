import pathlib
p=pathlib.Path('local/docs/研究归档/augmented-sixth-mechanics-and-syntactic-drift.md')
t=p.read_text(encoding='utf-8')
if '- **正文**' not in t:
    t=t.replace('- **学者**：', '- **正文**：`content/techniques/harmony/augmented-sixth-mechanics-and-syntactic-drift.md`\n- **学者**：',1)
p.write_text(t,encoding='utf-8')
print('ok')
