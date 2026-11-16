import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
fence = open('local/workbench/scores/verifier/tmp3/fence_haydn.ly', encoding='utf-8').read()
prod = open('local/workbench/scores/assistant-scores-e/haydn-hobIII66-op64no4-mvt2-mm1-8.ly', encoding='utf-8').read()

def norm(s):
    s = re.sub(r'%[^\n]*', '', s)
    s = re.sub(r'\\version[^\n]*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def body(s):
    return norm(s)[norm(s).find('global = {'):]

ba, bb = body(fence), body(prod)
if ba == bb:
    print('SCORE BODY IDENTICAL (md fence == producer .ly)')
else:
    print('SCORE BODY DIFF; fence len', len(ba), 'prod len', len(bb))
    for k in range(min(len(ba), len(bb))):
        if ba[k] != bb[k]:
            print('first diff at', k)
            print('fence:', repr(ba[max(0, k-100):k+100]))
            print('prod :', repr(bb[max(0, k-100):k+100]))
            break
print('\n--- NORMALIZED FENCE BODY ---')
print(ba)