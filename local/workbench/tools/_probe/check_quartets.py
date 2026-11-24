import sys
sys.stdout.reconfigure(encoding='utf-8')

def parse_piece(filepath, end_b):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    cur = 1
    bars = {1: []}
    for l in lines:
        l = l.strip()
        if l.startswith('='):
            first_tok = l.split()[0]
            digits = ''.join([c for c in first_tok if c.isdigit()])
            if digits:
                cur = int(digits)
                if cur > end_b + 1:
                    break
                bars[cur] = []
        elif not l.startswith('!') and not l.startswith('*'):
            if cur in bars:
                bars[cur].append(l)
    return bars

def summarize_bars(name, filepath, max_b):
    bars = parse_piece(filepath, max_b)
    print(f'=== {name} (mm. 1-{max_b}) ===')
    for b in sorted(bars.keys()):
        if b > max_b: continue
        row_text = ' '.join(bars[b])
        arts = []
        if "'" in row_text: arts.append('staccato')
        if "`" in row_text: arts.append('staccatissimo')
        if "~" in row_text: arts.append('tenuto')
        if "(" in row_text: arts.append('slur')
        if "T" in row_text or "t" in row_text: arts.append('trill')
        if "W" in row_text: arts.append('turn')
        dyns = [x for x in ['pp', 'p', 'f', 'ff', 'fp', 'sf', 'fz', 'sfp'] if x in row_text.split()]
        print(f'm.{b:2d}: arts={arts} dyns={dyns}')

base = 'local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/'
summarize_bars('Op. 18 No. 1 Mvt 1', base + 'quartet01-1.krn', 30)
summarize_bars('Op. 59 No. 1 Mvt 1', base + 'quartet07-1.krn', 24)
summarize_bars('Op. 135 Mvt 3', base + 'quartet16-3.krn', 12)
