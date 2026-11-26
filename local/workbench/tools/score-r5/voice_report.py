#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Report voices per staff for each spec: which are rendered / dropped."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kern2ly

for path in sys.argv[1:]:
    spec = json.load(open(path, encoding='utf-8'))
    piece = kern2ly.load(spec['kern'])
    s0, s1 = kern2ly.resolve_range(piece, spec['from'], spec['to'])
    print('==', os.path.basename(path), 'seqs', s0, '..', s1)
    for st in spec['staves']:
        staff = st['staff']
        rows = []
        for v in piece['order'].get(staff, []):
            n = 0
            for s in range(s0, s1 + 1):
                n += len(piece['measures'].get(s, {}).get(staff, {}).get(v, []))
            if n:
                rows.append((v, n))
        print('  staff%d %-6s voices with notes: %s' % (staff, st.get('label'), rows))
