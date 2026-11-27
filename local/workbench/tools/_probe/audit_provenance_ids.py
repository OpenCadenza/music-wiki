#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit consistency between content lilypond fence ids and provenance score tables.

Read-only. Prints:
- fences whose id is missing from the matching provenance file's score table
- provenance score-table ids that no longer exist in content
- articles with fences but no provenance file
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..', '..'))
CONTENT = os.path.join(ROOT, 'content')
PROV = os.path.join(ROOT, 'provenance')

fence_re = re.compile(r'```lilypond([^\n]*)\n')
id_re = re.compile(r'\bid="([^"]+)"')
prov_row_re = re.compile(r'^\|\s*`([^`]+)`\s*\|', re.M)

missing_rows = []
orphan_rows = []
no_prov = []
checked = 0

for dirpath, dirnames, filenames in os.walk(CONTENT):
    for fn in filenames:
        if not fn.endswith('.md'):
            continue
        cpath = os.path.join(dirpath, fn)
        rel = os.path.relpath(cpath, CONTENT)
        text = open(cpath, encoding='utf-8').read()
        ids = []
        for m in fence_re.finditer(text):
            attrs = m.group(1)
            mid = id_re.search(attrs)
            if mid:
                ids.append(mid.group(1))
        if not ids:
            continue
        checked += 1
        ppath = os.path.join(PROV, rel)
        if not os.path.exists(ppath):
            no_prov.append((rel, ids))
            continue
        prov = open(ppath, encoding='utf-8').read()
        prov_ids = prov_row_re.findall(prov)
        for i in ids:
            if i not in prov_ids:
                missing_rows.append((rel, i))
        for i in prov_ids:
            if i not in ids:
                orphan_rows.append((rel, i))

print('articles with fences:', checked)
print('\n== fences without provenance row ==')
for rel, i in missing_rows:
    print('%-70s %s' % (rel, i))
print('\n== provenance rows without fence ==')
for rel, i in orphan_rows:
    print('%-70s %s' % (rel, i))
print('\n== articles with fences but no provenance file ==')
for rel, ids in no_prov:
    print('%-70s %d fences' % (rel, len(ids)))
