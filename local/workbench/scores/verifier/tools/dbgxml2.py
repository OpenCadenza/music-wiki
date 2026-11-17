import sys, os
sys.path.insert(0, os.getcwd())
import cmp_xml as X
h=r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\verifier\mxl\haydn-op76-3\score.xml'
o=r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\verifier\mxl\beethoven-op135\score.xml'
for tag,p,m in [('HAYDN',h,'Poco adagio'),('OP135',o,'Lento assai')]:
    i,n = X.find_marker(p,m)
    print(tag,'marker at index',i,'number',n)
    # show first 3 measures durations of part1 to align pickup
    src = X.read_part(p,1,i,3)
    for k,ev in enumerate(src):
        print('   idx+%d  notes=%d  totalDur=%g'%(k,len(ev),sum(d for _,_,d in ev)))
