import pathlib,re
# safe term normalization
for p in pathlib.Path('content').rglob('*.md'):
    if p.name=='index.md': continue
    t=p.read_text(encoding='utf-8'); n=t.replace('乐念','乐思').replace('普林纳','Prinner')
    if n!=t: p.write_text(n,encoding='utf-8')
# add missing articles to techniques root index
p=pathlib.Path('content/techniques/index.md'); t=p.read_text(encoding='utf-8')
subs=['material','structure','harmony','counterpoint','rhythm','sound']
for sub in subs:
    lines=[]
    for a in sorted(pathlib.Path('content/techniques',sub).glob('*.md')):
        if a.name=='index.md': continue
        txt=a.read_text(encoding='utf-8')
        m=re.search(r'^# (.+)$',txt,re.M)
        title=m.group(1).strip() if m else a.stem
        rel=f'{sub}/{a.name}'
        if f']({rel})' in t: continue
        lines.append(f'- [{title}]({rel})')
    if lines:
        # append at end of file (root index sections are all at bottom); simple
        t=t.rstrip()+'\n'+'\n'.join(lines)+'\n'
p.write_text(t,encoding='utf-8')
print('ok')
