import sys, os
sys.path.insert(0, os.getcwd())
import cmp_staff as C
ly=r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s5\beethoven-op14-1-mvt1-mm1-16.ly'
txt=open(ly,encoding='utf-8').read()
blocks=C.split_vars(txt)
print('blocks:', list(blocks))
for name in ('rhUpper','rhLower','rhThird','lhUpper','lhLower'):
    ms=C.parse_block(blocks.get(name,''))
    print(name, 'measures:', len(ms))
    for i,mv in enumerate(ms[:3],1):
        print('   m%d'%i, [(t,p,d) for t,p,d in mv])
