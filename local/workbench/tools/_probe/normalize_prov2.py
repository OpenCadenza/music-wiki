import pathlib,re
changed=0
for p in pathlib.Path('provenance').rglob('*.md'):
    if p.name=='README.md': continue
    t=p.read_text(encoding='utf-8')
    m=re.search(r'文章：`([^`]+)`',t)
    if not m: continue
    cpath=pathlib.Path(m.group(1))
    if not cpath.exists(): continue
    fences=set(re.findall(r'id="([^"]+)"',cpath.read_text(encoding='utf-8')))
    out=[]; in_score=False
    for ln in t.splitlines():
        if ln.strip().startswith('## 谱例'): in_score=True
        elif in_score and ln.strip().startswith('## '): in_score=False
        if in_score and ln.startswith('|'):
            cells=ln.split('|')
            if len(cells)>3:
                cell=cells[1].strip()
                bare=cell.strip('`').strip()
                if re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._:-]*', bare) and bare not in fences:
                    cells[1]=' 占位（未出谱） '; ln='|'.join(cells); changed+=1
        out.append(ln)
    p.write_text('\n'.join(out)+'\n',encoding='utf-8')
print('changed',changed)
