import sys
sys.path.insert(0,r"_pdmx")
from verify_per_measure import kern_notes, midi_notes
krn="E:/github/music-wiki/.agents/worktrees/scholar-plan-dev/local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata09-1.krn"
kn=kern_notes(krn,1,16)
tracks,div=midi_notes("beethoven-op14-1-mvt1-mm1-16.mid"); tpm=div*4
for staff,tidx in ((1,1),(2,2)):
    exp={}
    for m,s,p in kn:
        if s==staff: exp.setdefault(m,set()).add(p)
    got={}
    for t,p in tracks[tidx][1]:
        got.setdefault(t//tpm+1,set()).add(p)
    bad=[m for m in exp if exp[m]!=got.get(m,set())]
    print(f"staff {staff}: measures compared={len(exp)}  pitch-set mismatches={bad}")
    for m in bad:
        print("   m",m,"kern-only",sorted(exp[m]-got.get(m,set())),"midi-only",sorted(got.get(m,set())-exp[m]))
