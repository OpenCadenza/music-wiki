import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..', '..'))
CONTENT = os.path.join(ROOT, 'content')
fence_re = re.compile(r'```lilypond')
id_re = re.compile(r'\bid="([^"]+)"')

total = 0
ids = []
per_file = {}
for dirpath, _dirs, files in os.walk(CONTENT):
    for fn in files:
        if not fn.endswith('.md'):
            continue
        p = os.path.join(dirpath, fn)
        text = open(p, encoding='utf-8').read()
        n = len(fence_re.findall(text))
        if n:
            rel = os.path.relpath(p, CONTENT)
            per_file[rel] = n
            total += n
            for m in re.finditer(r'```lilypond([^\n]*)\n', text):
                mid = id_re.search(m.group(1))
                if mid:
                    ids.append(mid.group(1))

print('total lilypond fences:', total)
print('distinct fence ids:', len(set(ids)))
print('dup ids:', [i for i in set(ids) if ids.count(i) > 1])
print('files with fences:', len(per_file))
