#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble Op.74 I .ly (mm.6-9) from krn2ly extraction."""
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
  title = "String Quartet No. 10 in E-flat Major, Op. 74 („Harp“)"
  subtitle = "I. Poco Adagio — mm. 6–9 (clef/octave trap: cello B♭2 and violin passage)"
  location = "Score example 2: mm. 6–9"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% 谱源：
%   1. local/resources/scores/source-packages/beethoven-score-sources/.../kern/quartet10-1.krn（mm.6–9）
%   2. local/materials/theory/dcml-abc/n10op74_01.notes.tsv（reviewed, DCML；逐音交叉验证）
% 音符经 krn2ly 转换（绝对音名、显式升降号）并与 DCML notes 的 midi 值逐音比对：
%   m.6 Vln2 = A♭5（80）二分 — DCML 证实（非八度噪声）；m.7 Vc = B♭2（46）全音符（文章指出的旧谱
%   bf,,1 = B♭1 错误，本版为 bf,1 = B♭2）；m.9 Vln1 花彩 16ee- 16ff 16gg 16ff（E♭5–F5–G5–F5）。
% 拍号：原谱 2/2（Poco Adagio）；kern 记 4/4（等价）。速度：四分音符 = 72（kern *MM72）→ 二分音符 = 36。
% 力度：kern 的 **dynam 列在 mm.6–9 为空，从略。
% GM：Violin I/II=40, Viola=41, Violoncello=42。

global = {
  \key ef \major
  \time 2/2
  \tempo "Poco Adagio" 2 = 36
  \set Score.currentBarNumber = #6
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

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Violin I" midiInstrument = "violin" } { \violinOne }
    \new Staff \with { instrumentName = "Violin II" midiInstrument = "violin" } { \violinTwo }
    \new Staff \with { instrumentName = "Viola" midiInstrument = "viola" } { \viola }
    \new Staff \with { instrumentName = "Violoncello" midiInstrument = "cello" } { \cello }
  >>
  \layout { }
  \midi { }
}'''

def main(src, dst):
    blocks = read_blocks(src)
    txt = TPL
    txt = txt.replace('%{VLN1%}', body(blocks, 6))
    txt = txt.replace('%{VLN2%}', body(blocks, 4))
    txt = txt.replace('%{VIOLA%}', body(blocks, 2))
    txt = txt.replace('%{CELLO%}', body(blocks, 0))
    open(dst, 'w', encoding='utf-8').write(txt)
    print('written', dst)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])