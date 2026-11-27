#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Search a PDF's embedded text layer for a pattern and print page + context.

Usage: python pdf_grep.py <pdf> <regex> [context_chars]
"""
import re
import sys

import fitz

path, pattern = sys.argv[1], sys.argv[2]
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 200
rx = re.compile(pattern, re.I)

doc = fitz.open(path)
print('pages:', doc.page_count)
for pno in range(doc.page_count):
    text = doc[pno].get_text('text')
    if not text:
        continue
    flat = re.sub(r'\s+', ' ', text)
    for m in rx.finditer(flat):
        a = max(0, m.start() - ctx)
        b = min(len(flat), m.end() + ctx)
        print('\n--- page %d ---' % (pno + 1))
        print(flat[a:b])
