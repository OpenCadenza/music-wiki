import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
md = open('content/techniques/structure/hybrid-themes-and-syntax-decoupling.md', encoding='utf-8').read()
prod = open('local/workbench/scores/assistant-scores-e/haydn-hobIII66-op64no4-mvt2-mm1-8.ly', encoding='utf-8').read()

def norm(s):
    s = re.sub(r'%[^\n]*', '', s)
    s = re.sub(r'\\version[^\n]*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

m = re.search(r'```lilypond[^\n]*\n(.*?)\n```', md, re.S)
fence = m.group(1)
nm = norm(fence)
np_ = norm(prod)

def body(s):
    i = s.find('global = {')
    return s[i:]

ba, bb = body(nm), body(np_)
if ba == bb:
    print('SCORE BODY IDENTICAL (md fence == producer .ly)')
else:
    print('SCORE BODY DIFF; fence len', len(ba), 'prod len', len(bb))
    for k in range(min(len(ba), len(bb))):
        if ba[k] != bb[k]:
            print('first diff at', k)
            print('fence:', repr(ba[max(0, k-80):k+80]))
            print('prod :', repr(bb[max(0, k-80):k+80]))
            break
# also show normalized fence body for reference
print('\n--- NORMALIZED FENCE BODY ---')
print(ba)