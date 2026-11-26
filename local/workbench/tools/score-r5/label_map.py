#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print seq -> label mapping (and meter) for a measure window of a kern file."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kern2ly

piece = kern2ly.load(sys.argv[1])
m0, m1 = int(sys.argv[2]), int(sys.argv[3])
s0, s1 = kern2ly.resolve_range(piece, m0, m1)
for s in range(max(0, s0 - 3), s1 + 4):
    print('seq %-4d label %-8s meter %-6s %s' % (
        s, piece['label'].get(s), piece['meter'].get(s),
        'EMPTY' if not piece['measures'].get(s) else ''))
