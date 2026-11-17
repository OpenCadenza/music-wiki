"""Greedy pitch/onset matching of XML attacks against compiled-MIDI notes.

XML grace notes have zero nominal duration; LilyPond renders them as very short
notes.  Both are therefore kept out of the rhythm comparison and reported
separately.  Everything else is matched by (pitch, nearest onset) so that the
comparison is immune to voice-ordering differences.
"""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xmlparse as X
import compare as C

W_ON = 0.20      # onset window for a match (quarters)
W_DUR = 0.06     # duration tolerance


def run(cfg):
    parts = X.parse_parts(cfg['xml'])
    tracks, div = C.midi_notes(cfg['mid'])
    out = []
    for si, (pk, stf) in enumerate(cfg['staff']):
        ms = X.window(parts[pk], cfg['start'], cfg['count'])
        att, total = C.xml_attacks(ms)
        if stf is not None:
            att = [a for a in att if a['staff'] == stf]
        graces = [a for a in att if a['grace']]
        main = [a for a in att if not a['grace']]
        mid = tracks[si]
        pool = list(mid)
        matched, unmatched_xml = [], []
        for a in sorted(main, key=lambda a: a['abs']):
            cands = [(abs(n['onset'] - a['abs']), i) for i, n in enumerate(pool)
                     if n['pitch'] == a['pitch'] and abs(n['onset'] - a['abs']) < W_ON]
            if not cands:
                unmatched_xml.append(a)
                continue
            cands.sort()
            i = cands[0][1]
            matched.append((a, pool.pop(i)))
        row = dict(part=pk, staff=si, n_xml=len(att), n_xml_main=len(main),
                   n_xml_grace=len(graces), n_midi=len(mid),
                   leftover_midi=len(pool), unmatched_xml=len(unmatched_xml),
                   xml_total=round(total, 3),
                   midi_span=round(max((n['onset'] + n['dur'] for n in mid), default=0), 3))
        row['unmatched'] = [dict(mnum=a['mnum'], pitch=a['pitch'],
                                 onset=round(a['abs'], 3)) for a in unmatched_xml]
        leftover = sorted(pool, key=lambda n: n['onset'])
        row['leftover'] = [dict(onset=round(n['onset'], 3), pitch=n['pitch'],
                                dur=round(n['dur'], 3)) for n in leftover]
        # graces: compare pitch multiset
        row['grace_pitch_xml'] = sorted(g['pitch'] for g in graces)
        row['grace_pitch_midi'] = sorted(n['pitch'] for n in leftover)
        bad = []
        for a, b in matched:
            dd = b['dur'] - a['dur_eff']
            if abs(dd) > W_DUR:
                bad.append(dict(mnum=a['mnum'], pitch=a['pitch'],
                                xml_on=round(a['abs'], 3),
                                xml_dur=round(a['dur_eff'], 3),
                                mid_dur=round(b['dur'], 3)))
        row['bad_dur'] = bad
        out.append(row)
    return out


if __name__ == '__main__':
    for cfg in json.load(open(sys.argv[1])):
        print('###', cfg['name'])
        for r in run(cfg):
            print('  %s staff%d: xml %d (main %d + grace %d) midi %d | unmatched %d leftover %d | total %s span %s'
                  % (r['part'], r['staff'], r['n_xml'], r['n_xml_main'], r['n_xml_grace'],
                     r['n_midi'], r['unmatched_xml'], r['leftover_midi'],
                     r['xml_total'], r['midi_span']))
            if r['unmatched']:
                print('    UNMATCHED XML:', r['unmatched'])
            if r['leftover']:
                print('    LEFTOVER MIDI:', r['leftover'])
            if r['grace_pitch_xml'] or r['grace_pitch_midi']:
                same = r['grace_pitch_xml'] == r['grace_pitch_midi']
                print('    graces xml %d midi %d  pitch-sets-equal=%s'
                      % (len(r['grace_pitch_xml']), len(r['grace_pitch_midi']), same))
                if not same:
                    print('      xml  ', r['grace_pitch_xml'])
                    print('      midi ', r['grace_pitch_midi'])
            print('    duration deviations (%d):' % len(r['bad_dur']))
            for d in r['bad_dur']:
                print('      ', d)
