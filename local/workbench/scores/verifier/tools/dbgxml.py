import sys, os
sys.path.insert(0, os.getcwd())
import xmlparse as X
for tag, path in [
  ('HAYDN', r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\verifier\mxl\haydn-op76-3\score.xml'),
  ('OP135', r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\verifier\mxl\beethoven-op135\score.xml'),
]:
    parts = X.parse_parts(path)
    print('=====', tag, 'parts:', len(parts))
    for k, ms in parts.items():
        print('  part', k, 'measures:', len(ms), 'first labels:', [m['mnum'] for m in ms[:8]])
