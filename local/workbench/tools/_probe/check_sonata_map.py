import zipfile

ZIP = r'local/origin_resources/sources/beethoven-score-sources/raw/beethoven-piano-sonatas-main.zip'
z = zipfile.ZipFile(ZIP)
refs = [n for n in z.namelist() if '/reference-edition/' in n and n.lower().endswith('.pdf')]
print('reference pdf count:', len(refs))
for s in ['sonata01-1', 'sonata02-1', 'sonata31-3']:
    k = 'beethoven-piano-sonatas-main/kern/%s.krn' % s
    txt = z.read(k).decode('utf-8', 'replace').split('\n')
    info = [l for l in txt if l.startswith(('!!!OPS', '!!!OTL', '!!!OMV', '!!!!SEGMENT'))]
    key = [l for l in txt if l.startswith('*k[')][:1]
    print(s, info, key)
