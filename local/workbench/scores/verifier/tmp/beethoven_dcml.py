import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from fractions import Fraction

def q(s):
    s = (s or "0").strip()
    if not s: return Fraction(0)
    try:
        return Fraction(s)
    except Exception:
        return Fraction(str(float(s))).limit_denominator(64)

p = Path("local/resources/scores/dcml-abc/n10op74_01.notes.tsv")
lines = p.read_text(encoding="utf-8").splitlines()
hdr = lines[0].split("\t")
idx = {h: i for i, h in enumerate(hdr)}
rows = []
for ln in lines[1:]:
    if not ln.strip(): continue
    f = ln.split("\t")
    try: mc = int(f[idx["mc"]])
    except Exception: continue
    if mc > 9: continue
    rows.append(f)

STAFF = {"1": "VnI", "2": "VnII", "3": "Vla", "4": "Vc"}
N = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]
def nm(m): return f"{N[m%12]}{m//12-1}"

for mc in range(1, 10):
    print(f"\n===== m.{mc} =====")
    sel = [f for f in rows if int(f[idx["mc"]]) == mc]
    sel.sort(key=lambda f: (int(f[idx["staff"]]), q(f[idx["mn_onset"]]), int(f[idx["midi"]])))
    for f in sel:
        on = q(f[idx["mn_onset"]]); du = q(f[idx["duration"]])
        m = int(f[idx["midi"]])
        print(f"  {STAFF[f[idx['staff']]]:5s} v{f[idx['voice']]} onset={str(on):>4} dur={str(du):>4} "
              f"midi={m:>3} {nm(m):>4} tpc={f[idx['tpc']]:>3} tie={(f[idx['tied']] or '-'):>2} grace={(f[idx['gracenote']] or '-'):>3}")
