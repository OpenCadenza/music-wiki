import sys
sys.path.insert(0, ".")
import src_abc as A
from pathlib import Path
import re

path = sys.argv[1]
lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
unit = 0.5
key = {"B": -1}
for idx in range(24, 42):
    m = re.match(r"\s*\[V:(\d+)\]\s*(.*)$", lines[idx])
    if not m:
        continue
    text = m.group(2)
    voices = A.parse_field(text, unit, key)
    sums = [round(sum(tk.dur for tk in v), 4) for v in voices]
    print(f"行{idx+1} V{m.group(1)} sums={sums}  tokens={[[repr(t) for t in v] for v in voices]}")
