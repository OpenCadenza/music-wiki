import pathlib,re
p=pathlib.Path('content/techniques/sound/timbral-contrast-and-formal-articulation.md')
t=p.read_text(encoding='utf-8')
ly=pathlib.Path('local/workbench/scores/score-p1/beethoven-op125-i-mm1-35/beethoven-op125-i-mm1-35.ly').read_text(encoding='utf-8').splitlines()
code=[ln for ln in ly if not ln.lstrip().startswith('%')]
while code and not code[0].strip(): code.pop(0)
while code and not code[-1].strip(): code.pop()
new='```lilypond title="贝多芬 第九交响曲 Op.125 第一乐章" location="Allegro ma non troppo, un poco maestoso，mm.1–35" id="beethoven-op125-i-mm1-35"\n'+'\n'.join(code)+'\n```'
pat=re.compile(r'```lilypond title="贝多芬 第九交响曲 Op\.125 第一乐章".*?\n```',re.S)
assert pat.search(t), 'fence not found'
t=pat.sub(lambda m:new,t,count=1)
p.write_text(t,encoding='utf-8')
print('replaced')
