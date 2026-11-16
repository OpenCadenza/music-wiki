import urllib.request, re, sys, io, json, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get(url, referer='https://cn.imslp.org/'):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': referer})
    return urllib.request.urlopen(req, timeout=40).read()

# File page for Haydn Op.64 No.4
html = get('https://cn.imslp.org/wiki/File:Haydn_-_Op._64,_No._4.pdf',
           'https://cn.imslp.org/wiki/String_Quartet_in_G_major,_Hob.III:66_(Haydn,_Joseph)').decode('utf-8', 'replace')
print('len', len(html))
# imslp page images usually in djvu/xml or via /images/thumb ... find preview jpgs
for m in re.finditer(r'<img[^>]+src="([^"]+)"', html):
    src = m.group(1)
    if 'thumb' in src or 'jpg' in src or 'png' in src:
        print('IMG', src[:160])