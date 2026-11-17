"""Driver: compare the three excerpt .ly files against their sources."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cmp_staff

ROOT = r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb'
SCH = r'E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local'

MODE = sys.argv[1]

if MODE == 'op14':
    cmp_staff.main_args(
        os.path.join(SCH, r'resources\scores\source-packages\beethoven-score-sources\beethoven-piano-sonatas-main\beethoven-piano-sonatas-main\kern\sonata09-1.krn'),
        os.path.join(ROOT, r'local\workbench\scores\score-s5\beethoven-op14-1-mvt1-mm1-16.ly'),
        {"1": ["rhUpper", "rhLower", "rhThird"], "2": ["lhUpper", "lhLower"]},
        1, 16)

elif MODE == 'op135':
    cmp_staff.main_args(
        os.path.join(SCH, r'resources\scores\source-packages\beethoven-score-sources\beethoven-string-quartets-main\beethoven-string-quartets-main\kern\quartet16-3.krn'),
        os.path.join(ROOT, r'local\workbench\scores\score-s1\beethoven-op135-mvt3-mm01-12.ly'),
        {"1": ["violinOne"], "2": ["violinTwo"], "3": ["viola"], "4": ["cello"]},
        1, 12)
