import urllib.request, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
req = urllib.request.Request(
    'https://cn.imslp.org/wiki/String_Quartet_in_G_major,_Hob.III:66_(Haydn,_Joseph)',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req, timeout=40).read().decode('utf-8', 'replace')
pats = re.findall(r'/images/[^)"]+', html)
print('image links:', len(pats))
seen = set()
for p in pats:
    if 'PMLP630989' in p and p not in seen:
        seen.add(p)
        print(p[:160])
# file pages
print('--- file page names ---')
for m in sorted(set(re.findall(r'File:PMLP630989[^"|<]*', html))):
    print(m[:120])