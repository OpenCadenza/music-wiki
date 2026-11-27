import re
import sys

path = sys.argv[1]
lo, hi = int(sys.argv[2]), int(sys.argv[3])
parts = [int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else None

lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
starts = [i for i, l in enumerate(lines) if re.match(r'^(?:score|data): part \d+ of \d+', l)]

skip_prefix = ('*', 'P ', '$', '&', '@', 'Group', 'score:', 'data:', 'back', 'forward')

for pno in range(1, len(starts) + 1):
    if parts and pno not in parts:
        continue
    s = starts[pno - 1]
    e = starts[pno] if pno < len(starts) else len(lines)
    head = [x for x in lines[max(0, s - 8):s] if x.strip()]
    name = head[-2] if len(head) >= 2 else '?'
    cur = None
    first_note = None
    per_meas = {}
    for line in lines[s:e]:
        m = re.match(r'^measure\s+(\d+)\s*$', line)
        if m:
            cur = int(m.group(1))
            continue
        t = line.rstrip()
        if not t or t.startswith(skip_prefix):
            continue
        if re.match(r'^\d+\s+\d+\s*$', t):
            continue
        if cur is None:
            cur = 1
        per_meas.setdefault(cur, []).append(t)
    notes = {k: v for k, v in per_meas.items()
             if any(not x.startswith(('rest', 'grest')) for x in v)}
    if notes:
        first_note = min(notes)
        last = max(notes)
    else:
        last = None
    # note density in the requested window
    window = sorted(k for k in notes if lo <= k <= hi)
    print('part %2d %-28s first-note-m=%s last-note-m=%s  window %d..%d -> %s'
          % (pno, name, first_note, last, lo, hi,
             ','.join(str(x) for x in window[:40])))
