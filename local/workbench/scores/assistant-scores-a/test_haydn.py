import subprocess

ly_test = r'''\version "2.26.0"
\include "nederlands.ly"

m_right = \relative c' {
  \partial 8 d8
  g8( b d g,)
  g4( fis8) d
  a'( c e <a, c>)
  <a c>4( <g b>8 b)
  b'( g dis e)
  a( fis cis d!)
  e8( g4) cis,8
  d4 r8
}
m_left = \relative c' {
  \partial 8 r8
  <g b>4 r8 <b d>
  <a c>4 r
  r r8 fis
  g4 g,8 r
  \clef treble
  g''4 r8 g
  fis4 r8 fis
  g4 a
  \clef bass
  d,4 d,8
}

t_right = \relative c'' {
  \partial 8 d8
  g8( b8 d8 g,8)
  g4( fis8) d8
  a'( c8 e8 <a, c>8)
  <a c>4( <g b>8 b8)
  b'( g8 dis8 e8)
  a8( fis8 cis8 d!8)
  e8( g4) cis,8
  d4 r8
}
t_left = \relative c' {
  \partial 8 r8
  <g b>4 r8 <b d>8
  <a c>4 r4
  r4 r8 fis8
  g4 g,8 r8
  \clef treble
  g'4 r8 g8
  fis4 r8 fis8
  g4 a4
  \clef bass
  d,4 d,8
}

\score {
  <<
    \new Staff = "m_rh" { \m_right }
    \new Staff = "m_lh" { \m_left }
    \new Staff = "t_rh" { \t_right }
    \new Staff = "t_lh" { \t_left }
  >>
  \midi { }
}
'''

ly_path = 'local/workbench/scores/assistant-scores-a/temp_haydn.ly'
mid_path = 'local/workbench/scores/assistant-scores-a/temp_haydn.midi'
with open(ly_path, 'w', encoding='utf-8') as f:
    f.write(ly_test)

res = subprocess.run(['E:\\GreenSoftware\\lilypond-2.26.0\\bin\\lilypond.exe', '-o', 'local/workbench/scores/assistant-scores-a/temp_haydn', ly_path], capture_output=True, text=True)
print('Lilypond exit:', res.returncode)
if res.stderr:
    print('Lilypond stderr:', res.stderr[:500])

import glob, os
mid_files = glob.glob('local/workbench/scores/assistant-scores-a/temp_haydn*.mid*')
print('Mid files found:', mid_files)

with open(mid_files[0], 'rb') as f:
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
        print(f'Track {track_num} ({name}): {notes}')
