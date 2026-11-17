p='kern2.py'
s=open(p,encoding='utf-8').read()
old = """            for i in reversed([i for i, t in enumerate(toks) if t == '*v']):
                if i + 1 < len(staff_of):
                    del staff_of[i + 1]"""
new = """            # a *^ pair is undone by a consecutive run of *v marks: the run
            # collapses to its leftmost spine (keep first, drop the rest).
            vidx = [i for i, t in enumerate(toks) if t == '*v']
            for run in _runs(vidx):
                for i in reversed(run[1:]):
                    if i < len(staff_of):
                        del staff_of[i]"""
assert old in s, 'anchor not found'
s = s.replace(old, new)
s = s.replace("def parse(path):", """def _runs(idx):
    out = []
    for i in idx:
        if out and i == out[-1][-1] + 1:
            out[-1].append(i)
        else:
            out.append([i])
    return out


def parse(path):""")
open(p,'w',encoding='utf-8').write(s)
print('merge-run handling patched')
