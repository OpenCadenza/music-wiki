import pathlib,re
root=pathlib.Path('.')
prov_files=list(pathlib.Path('provenance').rglob('*.md'))
print('prov files',len(prov_files))
bad=0; changed=0
for p in prov_files:
    t=p.read_text(encoding='utf-8')
    m=re.search(r'文章：`([^`]+)`',t)
    if not m:
        print('NO ARTICLE',p); bad+=1; continue
    cpath=pathlib.Path(m.group(1))
    if not cpath.exists():
        print('NO CONTENT',p,cpath); bad+=1; continue
    ctext=cpath.read_text(encoding='utf-8')
    fences=set(re.findall(r'id="([^"]+)"',ctext))
    lines=t.splitlines(); out=[]; in_score=False
    for ln in lines:
        if ln.strip().startswith('## 谱例'): in_score=True
        elif in_score and ln.strip().startswith('## '): in_score=False
        if in_score and ln.startswith('|'):
            cells=ln.split('|')
            if len(cells)>3 and cells[1].strip().startswith('`') and cells[1].strip().endswith('`'):
                pid=cells[1].strip().strip('`')
                if pid not in fences:
                    cells[1]=' 占位（未出谱） '
                    ln='|'.join(cells); changed+=1
        out.append(ln)
    t2='\n'.join(out)+'\n'
    # license summary
    lower=t2.lower()
    if 'cc0' in lower:
        lic='CC0-1.0（部分条目为学术核对，详见两表）'
    elif '公有领域' in t2 or 'public domain' in lower:
        lic='公有领域（详见两表）'
    elif 'ccarh' in lower or '学术' in t2:
        lic='CCARH MuseData 学术用途（非 CC0；详见两表）'
    else:
        lic='待确认（详见两表）'
    t2=re.sub(r'- 许可：.*', f'- 许可：{lic}', t2, count=1)
    if t2!=t:
        p.write_text(t2,encoding='utf-8')
print('rows changed',changed,'bad',bad)
