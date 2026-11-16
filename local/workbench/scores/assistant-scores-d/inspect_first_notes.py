import sys
sys.path.append("local/workbench/tools")
from midi_pitch_check import parse_midi

notes, div = parse_midi("local/workbench/scores/assistant-scores-d/mozart-k330-mvt2-mm1-8.mid")
for t, p, ch in notes[:25]:
    print(f"t={t:4d} ch={ch} p={p}")
