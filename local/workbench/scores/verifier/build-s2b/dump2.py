import sys
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "md", str(Path(__file__).parent.parent / "tools" / "midi_dump.py"))
md = importlib.util.module_from_spec(spec)
spec.loader.exec_module(md)

NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def nm(p):
    return f"{NAMES[p % 12]}{p // 12 - 1}"


for path in sys.argv[1:]:
    tracks, div = md.parse(path)
    print(f"== {path}")
    for ti, ev in enumerate(tracks):
        ns = md.notes_of(ev, div)
        if not ns:
            print(f"  track{ti}: (empty)")
            continue
        print(f"  track{ti}: " + " ".join(f"{nm(p)}({p})@{s:g}" for s, d, p, c in ns))
