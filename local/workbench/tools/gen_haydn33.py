#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble Haydn 104 mm.33-40 tutti .ly from krn2ly extraction."""
import sys, re

def read_blocks(path):
    blocks = {}
    cur = None
    for line in open(path, encoding='utf-8'):
        m = re.match(r'%%% COL (\d+) %%%', line)
        if m:
            cur = int(m.group(1)); blocks[cur] = []; continue
        if cur is not None:
            line = line.strip()
            if line:
                blocks[cur].append(line)
    return blocks

def body(blocks, col):
    return '\n  '.join(blocks.get(col, []))

TPL = r'''\version "2.26.0"
\language "english"

\header {
  title = "Symphony No. 104 in D major („London“), Hob. I:104"
  subtitle = "I. Allegro — mm. 33–40 (tutti: horns/oboes/flutes/timpani on D pedal)"
  location = "Score example 2b: mm. 33–40, tutti excerpt"
  composer = "Franz Joseph Haydn"
  tagline = ##f
}

% 谱源：local/origin_resources/downloads/2026-11-17/s3/haydn104-1.krn
%   （MuseData/CCARH, Humdrum **kern, Symphony No.104, Movement 1, Eulenburg 版转录；
%     GitHub musedata/humdrum-haydn-symphonies），并已与 Hauptstimme/OpenScore 的
%   管弦乐总谱 MusicXML（Haydn_104_1.mxl）交叉核对弦乐/双簧管/长笛/定音鼓的音高：
%   二者在 mm.33 的 Vln1=D6-B5-G5、Vln2=<D4 A4 F#5>+G5+E5、Ob1=A5-B5-G5、Timp=D3 上完全一致。
% 摘录内容（12 行，按 kern 实际参奏声部）：
%   Flauto 1/2、Oboe 1/2、Corno 1/2 (in D, written)、Timpani、Violino I/II、Viola、
%   Violoncello、Contrabasso。
%   kern 另含 Tromba 1/2 (in D)、Clarinetto 1/2 (in A)、Fagotto 1/2，本摘录未收录
%   （避免移调/八度不确定；不涉及本段论证）。
% 圆号：按 kern 的 written 音收录（Corno 1 = written D4 长音、Corno 2 = written D3 长音，
%   即“持续的八度 D 音”）。注意 Hauptstimme 转录的 D Horn 写作 written C5（实音 D5），
%   与 kern 的 written D3/D4 相差八度，本谱例从 kern（Eulenburg 版）并保留 written 记谱。
% 拍号 2/2；调号 D 大调（F#, C#）；速度 二分音符 = 120。力度：文章称全奏强奏，m.33 标 f。
% GM：Flute=73, Oboe=68, Horn=60, Timpani=47, Violin=40, Viola=41, Cello=42, Contrabass=32。

global = {
  \key d \major
  \time 2/2
  \tempo "Allegro" 2 = 120
  \set Score.currentBarNumber = #33
}

flautoOne = { \global \clef treble %{FL1%} \bar "|." }
flautoTwo = { \global \clef treble %{FL2%} \bar "|." }
oboeOne = { \global \clef treble %{OB1%} \bar "|." }
oboeTwo = { \global \clef treble %{OB2%} \bar "|." }
cornoOne = { \global \clef treble %{CO1%} \bar "|." }
cornoTwo = { \global \clef treble %{CO2%} \bar "|." }
timpani = { \global \clef bass %{TIMP%} \bar "|." }
violinOne = { \global \clef treble %{VLN1%} \bar "|." }
violinTwo = { \global \clef treble %{VLN2%} \bar "|." }
viola = { \global \clef alto %{VIOLA%} \bar "|." }
cello = { \global \clef bass %{CELLO%} \bar "|." }
bass = { \global \clef bass %{BASS%} \bar "|." }

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Flauto I" midiInstrument = "flute" } { \flautoOne }
    \new Staff \with { instrumentName = "Flauto II" midiInstrument = "flute" } { \flautoTwo }
    \new Staff \with { instrumentName = "Oboe I" midiInstrument = "oboe" } { \oboeOne }
    \new Staff \with { instrumentName = "Oboe II" midiInstrument = "oboe" } { \oboeTwo }
    \new Staff \with { instrumentName = "Corno I in D" midiInstrument = "french horn" } { \cornoOne }
    \new Staff \with { instrumentName = "Corno II in D" midiInstrument = "french horn" } { \cornoTwo }
    \new Staff \with { instrumentName = "Timpani" midiInstrument = "timpani" } { \timpani }
    \new Staff \with { instrumentName = "Violino I" midiInstrument = "violin" } { \violinOne }
    \new Staff \with { instrumentName = "Violino II" midiInstrument = "violin" } { \violinTwo }
    \new Staff \with { instrumentName = "Viola" midiInstrument = "viola" } { \viola }
    \new Staff \with { instrumentName = "Violoncello" midiInstrument = "cello" } { \cello }
    \new Staff \with { instrumentName = "Contrabasso" midiInstrument = "contrabass" } { \bass }
  >>
  \layout { }
  \midi { }
}'''

def main(src, dst):
    blocks = read_blocks(src)
    txt = TPL
    txt = txt.replace('%{FL1%}', body(blocks, 17))
    txt = txt.replace('%{FL2%}', body(blocks, 16))
    txt = txt.replace('%{OB1%}', body(blocks, 15))
    txt = txt.replace('%{OB2%}', body(blocks, 14))
    txt = txt.replace('%{CO1%}', body(blocks, 9))
    txt = txt.replace('%{CO2%}', body(blocks, 8))
    txt = txt.replace('%{TIMP%}', body(blocks, 5))
    txt = txt.replace('%{VLN1%}', body(blocks, 4))
    txt = txt.replace('%{VLN2%}', body(blocks, 3))
    txt = txt.replace('%{VIOLA%}', body(blocks, 2))
    txt = txt.replace('%{CELLO%}', body(blocks, 1))
    txt = txt.replace('%{BASS%}', body(blocks, 0))
    open(dst, 'w', encoding='utf-8').write(txt)
    print('written', dst)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
