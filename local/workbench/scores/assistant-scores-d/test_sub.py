import subprocess
import sys
sys.path.append("local/workbench/tools")
from midi_pitch_check import parse_midi

ly_code = """\\version "2.26.0"
\\language "english"
\\score {
  \\new Staff {
    \\partial 4.
    c''8-. c''8-. c''8-. |
    c''2. |
  }
  \\midi {}
}
"""
with open("local/workbench/scores/assistant-scores-d/test_partial.ly", "w") as f:
    f.write(ly_code)
subprocess.run(["E:/GreenSoftware/lilypond-2.26.0/bin/lilypond.exe", "--pdf", "-o", "local/workbench/scores/assistant-scores-d/test_partial", "local/workbench/scores/assistant-scores-d/test_partial.ly"], capture_output=True)
notes, div = parse_midi("local/workbench/scores/assistant-scores-d/test_partial.mid")
print("div:", div)
for t, p, ch in notes:
    print(f"t={t} p={p}")
