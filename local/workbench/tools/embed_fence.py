import json, sys, pathlib
spec=json.load(open(sys.argv[1],encoding='utf-8'))
art=pathlib.Path(sys.argv[2]); text=art.read_text(encoding='utf-8')
for item in spec:
    ly=pathlib.Path(item['ly']).read_text(encoding='utf-8').splitlines()
    code=[ln for ln in ly if not ln.lstrip().startswith('%')]
    while code and not code[0].strip(): code.pop(0)
    while code and not code[-1].strip(): code.pop()
    fence='```lilypond title="%s" location="%s" id="%s"\n%s\n```' % (item['title'],item['location'],item['id'],'\n'.join(code))
    ph=item['placeholder']
    if ph not in text: print('MISSING:',ph); sys.exit(1)
    text=text.replace(ph,fence,1)
art.write_text(text,encoding='utf-8')
print('embedded',len(spec),'fences into',art)
