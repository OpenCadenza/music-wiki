import sys
from pathlib import Path

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def name(pitch):
    return f"{NOTE_NAMES[pitch % 12]}{pitch // 12 - 1}"

# Import parse_midi from midi_pitch_check
sys.path.append("local/workbench/tools")
from midi_pitch_check import parse_midi

notes, div = parse_midi("test_k330_full.mid")
print(f"Total notes: {len(notes)}")
for tick, pitch, ch in notes:
    print(f"tick={tick:5d} ch={ch} pitch={pitch:3d} ({name(pitch)})")
