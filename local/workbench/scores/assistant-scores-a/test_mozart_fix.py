import subprocess

ly_mozart = r'''\version "2.26.0"
\language "english"

global = {
  \key g \major
  \time 3/4
  \tempo "Allegro" 4 = 120
}

rightHand = \relative c'' {
  \global
  \clef treble
  \partial 4 d8.(\p b16) |
  d4 r4 g,4 |
  fs4 r4 a'8.( fs16) |
  a4 r4 c,4 |
  b4 r4 g'8.(\f fs16) |
  fs8( e8) e4 g8.( e16) |
  e8( d8) d4 g8.( d16) |
  d4-.\p d4-. d4-. |
  d16( e fs g a b c d c b a g) |
  fs16( e d c b d b g a c a fs) |
  g4 r4 \bar "||"
}

leftHand = \relative c {
  \global
  \clef bass
  \partial 4 r4 |
  g8(\p b d b d b) |
  a8( c d c d c) |
  fs,8( a d a d a) |
  g8( b d b) g4\f |
  \clef treble
  <c' g'>2\fp r4 |
  <b g'>2\fp r4 |
  \clef bass
  <a c'>4-.\p <g b>4-. <fs a>4-. |
  <g b>4 r4 <e g>4 |
  r4 << { g4 c4 } \\ { d,2 } >> |
  <g b>4 g,4 r4 \bar "||"
}

\score {
  \new PianoStaff <<
    \new Staff = "upper" { \rightHand }
    \new Staff = "lower" { \leftHand }
  >>
  \midi { }
}
'''

with open('local/workbench/scores/assistant-scores-a/temp_mozart_fix.ly', 'w') as f:
    f.write(ly_mozart)

res = subprocess.run([r'E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe', '-o', 'local/workbench/scores/assistant-scores-a/temp_mozart_fix', 'local/workbench/scores/assistant-scores-a/temp_mozart_fix.ly'], capture_output=True, text=True)
print("Exit:", res.returncode)
if res.stderr:
    print("Stderr:", res.stderr)

with open('local/workbench/scores/assistant-scores-a/temp_mozart_fix.mid', 'rb') as f:
    data = f.read()

def parse_vlq(data, idx):
    val = 0
    while True:
        b = data[idx]
        idx += 1
        val = (val << 7) | (b & 0x7F)
        if not (b & 0x80):
            break
    return val, idx

idx = 14
track_num = 0
while idx < len(data):
    if data[idx:idx+4] == b'MTrk':
        track_num += 1
        length = int.from_bytes(data[idx+4:idx+8], 'big')
        track_data = data[idx+8:idx+8+length]
        idx += 8 + length
        t_idx = 0
        running_status = None
        notes = []
        name = ''
        while t_idx < len(track_data):
            delta, t_idx = parse_vlq(track_data, t_idx)
            b = track_data[t_idx]
            if b >= 0x80:
                status = b
                t_idx += 1
                running_status = status
            else:
                status = running_status
            if (status & 0xF0) == 0x90:
                pitch = track_data[t_idx]
                vel = track_data[t_idx+1]
                t_idx += 2
                if vel > 0:
                    notes.append(pitch)
            elif (status & 0xF0) in (0x80, 0xA0, 0xB0, 0xE0):
                t_idx += 2
            elif (status & 0xF0) in (0xC0, 0xD0):
                t_idx += 1
            elif status == 0xFF:
                meta_type = track_data[t_idx]
                t_idx += 1
                meta_len, t_idx = parse_vlq(track_data, t_idx)
                if meta_type == 3:
                    name = track_data[t_idx:t_idx+meta_len].decode('latin1', errors='ignore')
                t_idx += meta_len
        print(f"Track {track_num} ({name}): min={min(notes) if notes else None}, max={max(notes) if notes else None}")
        print("  Notes:", notes)
