import sys, os
sys.path.insert(0, os.getcwd())
import cmp_xml as X
h=r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\verifier\mxl\haydn-op76-3\score.xml'
o=r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\verifier\mxl\beethoven-op135\score.xml'
ROOT=r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb'
m1={"1":["violinOne"],"2":["violinTwo"],"3":["viola"],"4":["cello"]}
print('########## HAYDN (start=pickup idx 128) ##########')
X.main.__globals__['sys'].argv=['cmp_xml.py',h,'Poco adagio',os.path.join(ROOT,r'local\workbench\scores\score-s1\haydn-op76-3-mvt2-mm01-20-emperor.ly'),__import__('json').dumps(m1),'21','128']
X.main()
print()
print('########## OP135 (start=idx 468) ##########')
X.main.__globals__['sys'].argv=['cmp_xml.py',o,'Lento assai',os.path.join(ROOT,r'local\workbench\scores\score-s1\beethoven-op135-mvt3-mm01-12.ly'),__import__('json').dumps(m1),'12','468']
X.main()
