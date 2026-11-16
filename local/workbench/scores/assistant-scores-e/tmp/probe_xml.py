import re, sys, io
p = sys.argv[1]
t = io.open(p, encoding='utf-8', errors='replace').read()
print('len', len(t))
pats = [r'<work-title>[^<]*</work-title>', r'<movement-title>[^<]*</movement-title>',
        r'<movement-number>[^<]*</movement-number>',
        r'<creator[^>]*>[^<]*</creator>', r'<part-name>[^<]*</part-name>',
        r'<score-part id="([^"]+)">', r'<fifths>-?\d+</fifths>', r'<beats>\d+</beats>',
        r'<beat-type>\d+</beat-type>', r'<per-minute>[^<]*</per-minute>',
        r'<measure number="[^"]*"[^>]*>', r'<divisions>\d+</divisions>']
for pat in pats:
    ms = re.findall(pat, t)
    print(pat, '->', len(ms), ms[:12])
