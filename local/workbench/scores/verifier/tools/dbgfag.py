import sys, os
sys.path.insert(0, os.getcwd())
import cmp_staff as C
f=r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s2\downloads\op67-2\Symphony5_2-lys\fagotti.ly'
t=open(f,encoding='utf-8').read()
print('key detect:', end=' ')
print(re.search(r'\\key\s+\S+\s+\\\w+', t).group(0) if True else '')
C.detect_key(t)
b=C.split_vars(t)
print('vars:', list(b))
for k in b:
    ms=C.parse_block(b[k])
    if ms: print(' ', k, 'measures:', len(ms))
