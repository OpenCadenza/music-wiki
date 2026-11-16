import sys
sys.path.append("local/workbench/tools")
from midi_pitch_check import parse_midi

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def name(pitch): return f"{NOTE_NAMES[pitch % 12]}{pitch // 12 - 1}"

notes, div = parse_midi("local/workbench/scores/assistant-scores-d/mozart-k330-mvt2-mm1-8.mid")
for tick, pitch, ch in notes:
    # 384 divisions per quarter note.
    # 3/4 measure = 3 * 384 = 1152 ticks.
    # partial 4. = 1.5 * 384 = 576 ticks.
    print(f"tick={tick:5d} beat={tick/div:.2f} ch={ch} pitch={pitch:3d} ({name(pitch)})")
