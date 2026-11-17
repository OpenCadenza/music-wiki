#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble Haydn 104 .ly from krn2ly extraction (strings excerpt, mm.17-32)."""
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
  subtitle = "I. Allegro — mm. 17–32 (strings excerpt; horns rest in this passage)"
  location = "Score example 2: mm. 17–32, excerpt (strings only)"
  composer = "Franz Joseph Haydn"
  tagline = ##f
}

% 谱源：
%   local/origin_resources/downloads/2026-11-17/s3/haydn104-1.krn
%   （MuseData / CCARH, Humdrum **kern, Symphony No.104, Movement 1, Eulenburg 版转录；
%    经 GitHub musedata/humdrum-haydn-symphonies 下载）
% 摘录说明：本段实际参奏为弦乐五部（Vln I/II、Va、Vc、Cb）；kern 显示 mm.18–32 圆号/小号/
%   定音鼓/木管均为休止，全奏爆发（圆号 D 长音、双簧管加倍）实际始于 m.33。故本摘录只取弦乐，
%   并在记录中说明与文章描述的差异（文章称 mm.25–32 圆号长音）。
% 拍号：m.17 为 4/4 引子的 1 拍弱起（\partial 4）；m.18 起 Allegro 转 2/2。
% 调号 D 大调（F#, C#）；速度 二分音符 = 120（kern *MM240）。
% 力度：article 称 mm.17–24 弦乐弱奏；谱面标 p 于 m.18。其余从略（kern 无力度层）。
% GM：Violin I/II=40, Viola=41, Violoncello=42, Contrabass=32。

global = {
  \key d \major
  \partial 4
  \set Score.currentBarNumber = #17
  r4 |                              % m.17 (1-beat anacrusis, end of Adagio)
  \time 2/2
  \tempo "Allegro" 2 = 120
}

violinOne = {
  \global
  \clef treble
  %{VLN1%}
  \bar "|."
}

violinTwo = {
  \global
  \clef treble
  %{VLN2%}
  \bar "|."
}

viola = {
  \global
  \clef alto
  %{VIOLA%}
  \bar "|."
}

cello = {
  \global
  \clef bass
  %{CELLO%}
  \bar "|."
}

bass = {
  \global
  \clef bass
  %{BASS%}
  \bar "|."
}

\score {
  \new StaffGroup <<
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
    b4 = body(blocks, 4)
    b4 = b4.replace("fs'2 g'4 e'4", r"\\p fs'2 g'4 e'4", 1)
    txt = txt.replace('%{VLN1%}', b4)
    txt = txt.replace('%{VLN2%}', body(blocks, 3))
    txt = txt.replace('%{VIOLA%}', body(blocks, 2))
    txt = txt.replace('%{CELLO%}', body(blocks, 1))
    txt = txt.replace('%{BASS%}', body(blocks, 0))
    open(dst, 'w', encoding='utf-8').write(txt)
    print('written', dst)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
