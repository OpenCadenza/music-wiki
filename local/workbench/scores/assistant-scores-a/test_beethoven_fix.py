import subprocess

ly_text = r'''\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 10 in E-flat Major, Op. 74 (\"Harp\")"
  subtitle = "I. Poco adagio (mm. 1–9)"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% 依据 Humdrum Kern (quartet10-1.krn 第 23–77 行 = mm. 1–9) 与 DCML 权威校订重编码
% 修正记录：
% 1. 第一小提琴 m. 9 修正旋律琶音加花中漏掉的降记号：第 3 拍为 ef'16 (Eb4)，第 4 拍为 ef''16 (Eb5)；
% 2. 中提琴 m. 6 修正绝对音高八度偏差：cf''4 bf'4 c'4 (Cb5 / Bb4 / C4)，恢复向高音区穿插之原版对位；
% 3. 大提琴 mm. 6–7 修正低于乐器物理发音极限的八度错误：m. 6 末拍改为 a,4 (A2)，m. 7 改为 bf,1 (Bb2)，完全合规于四弦大提琴 C2–C6 物理音域。

global = {
  \key ef \major
  \time 2/2
  \tempo "Poco adagio" 4 = 72
}

violinOne = {
  \global
  \clef treble
  ef''2\p g'4. af'8 |
  df''4\fp r4 r2 |
  ef''2\p g'4. af'8 |
  df''1~\fp |
  df''2. d''4~ |
  d''2 ef''4 c''8( f''8) |
  ef''4( d''4 c''4 bf'4) |
  bf'4( af'8) r8 af'4( g'8) r8 |
  g'4~\fp g'16( f'16 e'16 f'16 ef'16 f'16 g'16 f'16 ef''16 f''16 g''16 f''16) |
  \bar "||"
}

violinTwo = {
  \global
  \clef treble
  g'2\p ef'4. ef'8 |
  ef'4\fp r4 r2 |
  g'2\p ef'4. ef'8 |
  e'4\fp r4 bf''2~ |
  bf''2 af''2~ |
  af''2 g''4 f''8( f'8) |
  f'2 af'4( g'4) |
  g'4( f'8) r8 bf4( bf8) r8 |
  c'4\fp r4 r2 |
  \bar "||"
}

viola = {
  \global
  \clef alto
  bf2\p bf4. af8 |
  g4\fp r4 r2 |
  bf2\p bf4. af8 |
  bf4\fp r4 r4 e'4~ |
  e'2 f'2~ |
  f'4 cf''4( bf'4 c'4) |
  af2 d4. ef8 |
  e4 f4 d4 ef4 |
  af4\fp r4 r4 af4~ |
  \bar "||"
}

cello = {
  \global
  \clef bass
  ef2\p df4. c8 |
  bf,4\fp r4 r2 |
  ef2\p df4. c8 |
  g,4\fp r4 r2 |
  f,2. bf,4 |
  ef,2. a,4 |
  bf,1 |
  c2 f,4. g,8 |
  af,4\fp r4 r4 f,4~ |
  \bar "||"
}

\score {
  \new StaffGroup <<
    \new Staff \with {
      instrumentName = "Violin I"
      midiInstrument = "violin"
    } { \violinOne }

    \new Staff \with {
      instrumentName = "Violin II"
      midiInstrument = "violin"
    } { \violinTwo }

    \new Staff \with {
      instrumentName = "Viola"
      midiInstrument = "viola"
    } { \viola }

    \new Staff \with {
      instrumentName = "Cello"
      midiInstrument = "cello"
    } { \cello }
  >>
  \layout { }
  \midi { }
}
'''

ly_path = 'local/workbench/scores/assistant-scores-a/beethoven-op74-mvt1-mm1-9-adagio.ly'
with open(ly_path, 'w', encoding='utf-8') as f:
    f.write(ly_text)

res = subprocess.run([r'E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe', '-o', 'local/workbench/scores/assistant-scores-a/beethoven-op74-mvt1-mm1-9-adagio', ly_path], capture_output=True, text=True)
print("Exit code:", res.returncode)
if res.stderr:
    print("Stderr:", res.stderr)

# Now inspect MIDI notes and ranges
with open('local/workbench/scores/assistant-scores-a/beethoven-op74-mvt1-mm1-9-adagio.mid', 'rb') as f:
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
names = ["", "Violin I", "Violin II", "Viola", "Cello"]
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
        if notes:
            inst = names[track_num-1]
            print(f"Track {track_num} ({inst}): count={len(notes)}, min={min(notes)}, max={max(notes)}")
            print("  Pitches:", notes)
