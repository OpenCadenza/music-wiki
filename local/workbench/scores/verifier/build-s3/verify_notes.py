# -*- coding: utf-8 -*-
"""Compare producer MIDI excerpts against authoritative notes (DCML tsv for Op.135,
Mutopia project MIDI for D.328).  Prints per-measure / per-onset diffs."""
import sys, os, csv
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dump_producer import parse, notes_of

# ---------- producer side ----------
def prod_notes(mid, bar_len_fn, offset_qb=0.0, track_map=None):
    fmt, div, tracks = parse(mid)
    out = defaultdict(list)   # (measure, rel_qb, dur, pitch)
    for ti, tr in enumerate(tracks):
        if track_map is not None and ti not in track_map:
            continue
        part = track_map[ti] if track_map else ti
        for (on, off, ch, p) in notes_of(tr, div):
            q0 = on / div
            q1 = off / div
            m, rel = bar_len_fn(q0 - offset_qb)
            out[(m, rel, round(q1 - q0, 3), p)].append(part)
    return out

def bar3_2(q):
    m = int(q // 6) + 1
    return m, round(q - (m-1)*6, 3)

def bar12_then44(q):
    # q measured from start of m.12 ; m.12 is 3/2 (6 quarters), then 4/4
    if q < 6:
        return 12, round(q, 3)
    m = 13 + int((q - 6) // 4)
    return m, round((q - 6) - (m-13)*4, 3)

# ---------- authoritative side ----------
def fr(s):
    if '/' in s:
        a, b = s.split('/')
        return float(a) / float(b)
    return float(s)

def dcml_notes(path, mc_from, mc_to, shift):
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    staff2part = {1: 'VI', 2: 'VII', 3: 'VA', 4: 'VC'}
    out = []
    for r in rows:
        mc = int(r['mc'])
        if not (mc_from <= mc <= mc_to):
            continue
        qb = fr(r['quarterbeats']) - shift
        qbend = float(r['quarterbeats_all_endings'].replace('0', '0')) if False else None
        out.append(dict(staff=staff2part[int(r['staff'])], qb=qb,
                        dur=fr(r['duration_qb']), midi=int(r['midi']),
                        name=r['name'], tied=r['tied']))
    return out

def src_midi_notes(path, qb_from, qb_to, tracks_keep=None):
    fmt, div, tracks = parse(path)
    res = []
    for ti, tr in enumerate(tracks):
        if tracks_keep is not None and ti not in tracks_keep:
            continue
        for (on, off, ch, p) in notes_of(tr, div):
            q0 = on / div
            if qb_from <= q0 < qb_to:
                res.append(dict(track=ti, qb=q0 - qb_from, dur=(off-on)/div, midi=p))
    return res

def compare(name, prod, exp, bar_fn, label):
    print(f'===== {name} =====')
    pmap = {}
    for (m, rel, dur, p), parts in prod.items():
        pmap[(round(m), round(rel, 2), round(dur, 2), p)] = tuple(sorted(parts))
    emap = defaultdict(list)
    for e in exp:
        m, rel = bar_fn(e['qb'])
        emap[(round(m), round(rel, 2), round(e['dur'], 2), e['midi'])].append(e.get('staff', e.get('track')))
    only_prod = sorted(set(pmap) - set(emap))
    only_exp = sorted(set(emap) - set(pmap))
    print(f'producer events={len(pmap)} expected={len(emap)} matched={len(set(pmap)&set(emap))}')
    if only_prod:
        print(' only in producer:')
        for k in only_prod:
            print('   ', k, pmap[k])
    if only_exp:
        print(' only in source:')
        for k in only_exp:
            print('   ', k, emap[k])
    return only_prod, only_exp

if __name__ == '__main__':
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))
    auth = r'E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local'
    dcml = os.path.join(auth, r'resources\scores\dcml-abc\n16op135_04.notes.tsv')
    prod_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'score-s3')
    sch = os.path.join(auth, r'origin_resources\corpus\lilypond\SchubertF\D328\Erlkoenig\Erlkoenig.mid')

    # --- Op135 mm1-4
    prod = prod_notes(os.path.join(prod_dir, 'beethoven-op135-mvt4-mm1-4-grave.mid'), bar3_2,
                      track_map={1: 'VI', 2: 'VII', 3: 'VA', 4: 'VC'})
    exp = dcml_notes(dcml, 1, 4, 0.0)
    compare('Op.135 IV mm.1-4 (Grave, 3/2)', prod, exp, bar3_2, 'dcml')

    # --- Op135 mm12-16
    prod = prod_notes(os.path.join(prod_dir, 'beethoven-op135-mvt4-mm12-16-allegro.mid'), bar12_then44,
                      offset_qb=0.0, track_map={1: 'VI', 2: 'VII', 3: 'VA', 4: 'VC'})
    exp = dcml_notes(dcml, 12, 16, 66.0)
    compare('Op.135 IV mm.12-16 (Allegro)', prod, exp, bar12_then44, 'dcml')

    # --- D328 mm1-5
    prod = prod_notes(os.path.join(prod_dir, 'schubert-d328-mm1-5-prelude.mid'), lambda q: (int(q // 4) + 1, round(q - int(q//4)*4, 3)))
    exp = src_midi_notes(sch, 0.0, 20.0)
    compare('D.328 mm.1-5 (piano)', prod, exp, lambda q: (int(q // 4) + 1, round(q - int(q//4)*4, 3)), 'mutopia')

    # --- D328 mm72-76
    prod = prod_notes(os.path.join(prod_dir, 'schubert-d328-mm72-76-mein-vater.mid'), lambda q: (72 + int(q // 4), round(q - int(q//4)*4, 3)))
    exp = src_midi_notes(sch, 284.0, 304.0)
    compare('D.328 mm.72-76 (voice+piano)', prod, exp, lambda q: (72 + int(q // 4), round(q - int(q//4)*4, 3)), 'mutopia')

