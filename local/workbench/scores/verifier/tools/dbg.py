import sys, os
sys.path.insert(0, os.getcwd())
import kern2, importlib
importlib.reload(kern2)
k=r'E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\source-packages\beethoven-score-sources\beethoven-piano-sonatas-main\beethoven-piano-sonatas-main\kern\sonata09-1.krn'
ms=kern2.parse(k)
for m in ms[:3]:
    print('LABEL', m['label'])
    for st in sorted(m['onsets']):
        print('   staff', st, m['onsets'][st], 'total', sum(d or 0 for d,_ in m['onsets'][st]))
print('n measures', len(ms))
print('labels', [m['label'] for m in ms[:20]])
