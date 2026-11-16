import sys
sys.path.append("local/workbench/tools")
from midi_pitch_check import parse_midi

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def name(pitch): return f"{NOTE_NAMES[pitch % 12]}{pitch // 12 - 1}"

notes, div = parse_midi("local/workbench/scores/assistant-scores-d/mozart-k330-mvt2-mm1-8.mid")
print(f"Total notes in MIDI: {len(notes)}")
for tick, pitch, ch in notes:
    print(f"tick={tick:5d} ch={ch} pitch={pitch:3d} ({name(pitch)})")
