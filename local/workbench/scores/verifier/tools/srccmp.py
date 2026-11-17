"""Compare MusicXML measures with **kern measures (pitch multisets, per staff)."""
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xmlparse as X
import kernparse as K


def kern_staff_map(path):
    """Read the *staffN spines header to know which spine is which staff."""
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    for ln in lines:
        if ln.startswith('*staff'):
            out = []
            for t in ln.split('\t'):
                m = re.match(r'\*staff(\d+)', t)
                if m:
                    out.append(int(m.group(1)))
            return out
    return None


def xml_by_measure(part_measures, staff_filter=None):
    """Printed-measure view: 'X1' continuation elements fold into the measure
    they continue."""
    out = collections.OrderedDict()
    cur = None
    for m in part_measures:
        num = str(m['mnum'])
        if not num.startswith('X'):
            cur = num
            out[cur] = []
        notes = [e['pitch'] for e in m['events']
                 if e['pitch'] is not None
                 and (staff_filter is None or e['staff'] == staff_filter)]
        out[cur].extend(notes)
    return out


def kern_by_measure(path):
    return {m['label']: m['notes'] for m in K.parse(path)}


def compare(xmlpath, kernpath, part_of_staff, first, last, combine_x=True):
    parts = X.parse_parts(xmlpath)
    kms = kern_by_measure(kernpath)
    smap = kern_staff_map(kernpath) or [2, 1]
    print('## kern staff spines:', smap)
    for staff_no in (1, 2):
        pk, filt = part_of_staff[staff_no]
        xm = xml_by_measure(parts[pk], filt)
        spine = smap.index(staff_no) if staff_no in smap else None
        print('== staff', staff_no, 'part', pk, 'kern spine', spine)
        for n in range(first, last + 1):
            xp = list(xm.get(str(n), []))
            kp = kms.get(str(n), {}).get(staff_no, [])
            xa = set(xp)
            ka = set(p for p, _ in kp)
            if xa != ka:
                print('  m%-4d xml-only %s | kern-only %s   (counts xml %d kern %d)'
                      % (n, sorted(xa - ka), sorted(ka - xa), len(xp), len(kp)))
        print()


if __name__ == '__main__':
    pass
