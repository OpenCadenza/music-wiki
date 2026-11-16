import csv
from fractions import Fraction
from pathlib import Path

p = Path("local/resources/scores/dcml-abc/n02op18-2_04.notes.tsv")
rows = list(csv.DictReader(p.open(encoding="utf-8"), delimiter="\t"))
NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def f(x):
    return float(Fraction(x)) if x else 0.0


def nm(x):
    return f"{NAMES[x % 12]}{x // 12 - 1}"


for r in rows:
    if int(r["mc"]) <= 9:
        m = int(r["midi"])
        print(f"mc{r['mc']} st{r['staff']} v{r['voice']} qb{f(r['quarterbeats']):5.2f} "
              f"onset{f(r['mc_onset']):4.2f} dur{f(r['duration_qb']):5.3f} "
              f"{r['name']}{r['octave']} midi={m} tpc={r['tpc']} grace={r['gracenote'] or '-'} tie={r['tied'] or '-'}")
