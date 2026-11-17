p='cmp_staff.py'
s=open(p,encoding='utf-8').read()

# 1) key-signature support
s = s.replace("""def midi_of(letter, acc, om):
    p = STEP[letter]
    if acc == 's': p += 1""",
"""SHARP_ORDER = ['f', 'c', 'g', 'd', 'a', 'e', 'b']
FLAT_ORDER = ['b', 'e', 'a', 'd', 'g', 'c', 'f']
MAJOR_SHARPS = {'c': 0, 'g': 1, 'd': 2, 'a': 3, 'e': 4, 'b': 5, 'fs': 6, 'cs': 7}
MAJOR_FLATS = {'f': 1, 'bf': 2, 'ef': 3, 'af': 4, 'df': 5, 'gf': 6, 'cf': 7}
KEYSIG = {}          # letter -> -1/0/+1 default accidental


def set_key(tonic, mode):
    KEYSIG.clear()
    if mode == 'major':
        if tonic in MAJOR_SHARPS:
            for L in SHARP_ORDER[:MAJOR_SHARPS[tonic]]:
                KEYSIG[L] = 1
        elif tonic in MAJOR_FLATS:
            for L in FLAT_ORDER[:MAJOR_FLATS[tonic]]:
                KEYSIG[L] = -1
    else:                                      # minor: relative major
        order = ['a', 'e', 'b', 'fs', 'cs', 'gs', 'ds', 'as']
        rel = {'a': 'c', 'e': 'g', 'b': 'd', 'fs': 'a', 'cs': 'e',
               'gs': 'b', 'ds': 'fs', 'as': 'cs'}
        if tonic in rel:
            set_key(rel[tonic], 'major')


def detect_key(src):
    m = re.search(r'\\\\key\\s+([a-g](?:s|f)?)\\s+\\\\(major|minor)', src)
    if m:
        set_key(m.group(1), m.group(2))
    return KEYSIG


def midi_of(letter, acc, om):
    p = STEP[letter]
    if acc is None and KEYSIG:
        acc = {1: 's', -1: 'f'}.get(KEYSIG.get(letter, 0))
    if acc == 's': p += 1""")

# 2) call detect_key in main_args
s = s.replace("""    text = open(ly, encoding='utf-8').read()
    blocks = split_vars(text)""",
"""    text = open(ly, encoding='utf-8').read()
    detect_key(text)
    blocks = split_vars(text)""")
open(p,'w',encoding='utf-8').write(s)
print('key signature support added')
