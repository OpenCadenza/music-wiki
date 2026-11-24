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

def inspect_bars(title, filepath, bars_to_show):
    bars = parse_piece(filepath, max(bars_to_show))
    print(f'================ {title} ================')
    for b in bars_to_show:
        if b not in bars: continue
        print(f'--- Bar {b} ---')
        for r in bars[b]:
            print('  ', r)

base = 'local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/'
inspect_bars('Op. 18 No. 1 mm. 1-4, 21-30', base + 'quartet01-1.krn', [1, 2, 3, 4, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
inspect_bars('Op. 59 No. 1 mm. 1-8, 18-24', base + 'quartet07-1.krn', [1, 2, 3, 4, 5, 6, 7, 8, 18, 19, 20, 21, 22, 23, 24])
inspect_bars('Op. 135 Mvt 3 mm. 1-12', base + 'quartet16-3.krn', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
