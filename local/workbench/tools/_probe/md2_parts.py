import re
import sys

path = sys.argv[1]
lines = open(path, encoding='utf-8', errors='replace').read().split('\n')

part_starts = [(i, m) for i, l in enumerate(lines)
               for m in [re.match(r'^(?:score|data): part (\d+) of (\d+)', l)] if m]
print('parts found:', len(part_starts))
for idx, (i, m) in enumerate(part_starts):
    head = [x for x in lines[max(0, i - 8):i] if x.strip()]
    print('part %s/%s @line %d :: %s' % (m.group(1), m.group(2), i + 1, ' | '.join(head[-4:])))
