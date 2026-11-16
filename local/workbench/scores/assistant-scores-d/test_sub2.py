import subprocess
import sys
sys.path.append("local/workbench/tools")
from midi_pitch_check import parse_midi

ly_code = """\\version "2.26.0"
\\language "english"
\\score {
  \\new PianoStaff <<
    \\new Staff = "upper" {
      \\key f \\major
      \\time 3/4
      \\partial 4.
      c''8-. c''8-. c''8-. |
      c''8. \\grace { d''16 c'' b' c'' } f''16 c''8 a'8 c''8 e'8 |
    }
    \\new Staff = "lower" {
      \\key f \\major
      \\time 3/4
      \\clef bass
      \\partial 4.
      r8 r4 |
      <f a c'>2 <c g bf>4 |
    }
  >>
  \\midi {}
}
"""
with open("local/workbench/scores/assistant-scores-d/test_m0_m1.ly", "w") as f:
    f.write(ly_code)
subprocess.run(["E:/GreenSoftware/lilypond-2.26.0/bin/lilypond.exe", "--pdf", "-o", "local/workbench/scores/assistant-scores-d/test_m0_m1", "local/workbench/scores/assistant-scores-d/test_m0_m1.ly"], capture_output=True)
notes, div = parse_midi("local/workbench/scores/assistant-scores-d/test_m0_m1.mid")
print("div:", div)
for t, p, ch in notes:
    print(f"t={t:4d} ch={ch} p={p}")
