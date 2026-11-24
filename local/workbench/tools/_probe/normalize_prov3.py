import pathlib,re
changed=0
for p in pathlib.Path('provenance').rglob('*.md'):
    if p.name=='README.md': continue
    t=p.read_text(encoding='utf-8'); out=[]; in_score=False
    for ln in t.splitlines():
        if ln.strip().startswith('## 谱例'): in_score=True
        elif in_score and ln.strip().startswith('## '): in_score=False
        if in_score and ln.startswith('|'):
            cells=ln.split('|')
            if len(cells)>3:
                cell=cells[1].strip()
                if '文本占位' in cell or cell in ('占位','占位（未出谱）'):
                    cells[1]=' 占位（未出谱） '; ln='|'.join(cells); changed+=1
                elif cell.startswith('关联既有：'):
                    cid=cell.split('：',1)[1].strip('` ').strip()
                    cells[1]=f' `{cid}`（关联引用） '; ln='|'.join(cells); changed+=1
        out.append(ln)
    p.write_text('\n'.join(out)+'\n',encoding='utf-8')
print('changed',changed)
