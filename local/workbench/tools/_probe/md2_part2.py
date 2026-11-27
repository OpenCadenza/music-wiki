import re
import sys

path, part_no, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
lines = open(path, encoding='utf-8', errors='replace').read().split('\n')

starts = [i for i, l in enumerate(lines) if re.match(r'^(?:score|data): part \d+ of \d+', l)]
s = starts[part_no - 1]
e = starts[part_no] if part_no < len(starts) else len(lines)

skip_prefix = ('*', 'P ', '$', '&', '@', 'Group', 'score:', 'data:', 'back', 'forward')
cur = None
recs = []


def new_measure(num):
    recs.append([num, []])


for line in lines[s:e]:
    m = re.match(r'^measure\s+(\d+)\s*$', line)
    if m:
        cur = int(m.group(1))
        new_measure(cur)
        continue
    t = line.rstrip()
    if not t or t.startswith(skip_prefix):
        continue
    if re.match(r'^\d+\s+\d+\s*$', t):
        continue
    if cur is None:
        cur = 1
        new_measure(1)
    recs[-1][1].append(t)

out = []
for num, items in recs:
    if not (lo <= num <= hi):
        continue
    notes = [i for i in items if not i.startswith(('rest', 'grest'))]
    if notes:
        out.append('m.%d: %s' % (num, ' ; '.join(notes)))
    else:
        out.append('m.%d: (rests)' % num)
print('\n'.join(out))
