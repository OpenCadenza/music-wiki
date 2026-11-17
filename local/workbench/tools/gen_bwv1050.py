#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble BWV1050 .ly from krn2ly extraction output."""
import sys, re, os

def read_blocks(path):
    blocks = {}
    cur = None
    for line in open(path, encoding='utf-8'):
        m = re.match(r'%%% COL (\d+) %%%', line)
        if m:
            cur = int(m.group(1))
            blocks[cur] = []
            continue
        if cur is not None:
            line = line.strip()
            if line:
                blocks[cur].append(line)
    return blocks

def body(blocks, col):
    lines = blocks.get(col, [])
    return '\n  '.join(lines)

TPL = r'''\version "2.26.0"
\language "english"

\header {
  title = "Brandenburg Concerto No. 5 in D major, BWV 1050"
  subtitle = "I. Allegro — mm. 1–9 (tutti, baroque polarity and continuo scaffolding)"
  location = "Score example 1: mm. 1–9"
  composer = "Johann Sebastian Bach"
  tagline = ##f
}

% 谱源：
%   local/origin_resources/downloads/2026-11-17/s3/bwv1050-1.krn
%   （MuseData / CCARH, Humdrum **kern, BWV 1050 Movement 1, Eulenburg 版转录；经 GitHub musedata/humdrum-bach-brandenburg 下载）
% 音高/时值经自写 krn2ly 转换（绝对音名、显式升降号）并逐小节比对 kern 原文；编译后经 MIDI 反查。
% 声部：Flauto traverso, Violino principale, Violino di ripieno, Viola di ripieno,
%       Violoncello, Violone, Cembalo concertato（本谱例的大键琴以右手/左手两行呈现，
%       kern 的第三行 cemba2 与大键琴高声部和弦重叠，故从略——记录中说明）。
% 拍号 2/2（alla breve）；调号 D 大调（F#, C#）；速度 二分音符 = 66。
% GM：Flute=73, Violin=40(x2), Viola=41, Cello=42, Acoustic Bass=32, Harpsichord=6。

global = {
  \key d \major
  \time 2/2
  \tempo "Allegro" 2 = 66
}

flauto = {
  \global
  \clef treble
  %{FLAUTO%}
  \bar "|."
}

violinoPrincipale = {
  \global
  \clef treble
  %{VLNPRI%}
  \bar "|."
}

violinoRipieno = {
  \global
  \clef treble
  %{VLNRIP%}
  \bar "|."
}

viola = {
  \global
  \clef alto
  %{VIOLA%}
  \bar "|."
}

violoncello = {
  \global
  \clef bass
  %{CELLO%}
  \bar "|."
}

violone = {
  \global
  \clef bass
  %{VIOLONE%}
  \bar "|."
}

cembaloUpper = {
  \global
  \clef treble
  %{CEMBA3%}
  \bar "|."
}

cembaloLower = {
  \global
  \clef bass
  %{CEMBA1%}
  \bar "|."
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Flauto" midiInstrument = "flute" } { \flauto }
    \new Staff \with { instrumentName = "Vl. principale" midiInstrument = "violin" } { \violinoPrincipale }
    \new Staff \with { instrumentName = "Vl. di ripieno" midiInstrument = "violin" } { \violinoRipieno }
    \new Staff \with { instrumentName = "Viola" midiInstrument = "viola" } { \viola }
    \new Staff \with { instrumentName = "Violoncello" midiInstrument = "cello" } { \violoncello }
    \new Staff \with { instrumentName = "Violone" midiInstrument = "contrabass" } { \violone }
    \new PianoStaff <<
      \new Staff \with { instrumentName = "Cembalo" midiInstrument = "harpsichord" } { \cembaloUpper }
      \new Staff \with { midiInstrument = "harpsichord" } { \cembaloLower }
    >>
  >>
  \layout { }
  \midi { }
}'''

def main(src, dst):
    blocks = read_blocks(src)
    txt = TPL
    txt = txt.replace('%{FLAUTO%}', body(blocks, 8))
    txt = txt.replace('%{VLNPRI%}', body(blocks, 7))
    txt = txt.replace('%{VLNRIP%}', body(blocks, 6))
    txt = txt.replace('%{VIOLA%}', body(blocks, 5))
    txt = txt.replace('%{CELLO%}', body(blocks, 4))
    txt = txt.replace('%{VIOLONE%}', body(blocks, 3))
    txt = txt.replace('%{CEMBA3%}', body(blocks, 2))
    txt = txt.replace('%{CEMBA1%}', body(blocks, 0))
    open(dst, 'w', encoding='utf-8').write(txt)
    print('written', dst)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])