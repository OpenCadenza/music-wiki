\version "2.26.0"
\language "english"

% =====================================================================
% 卡尔·尼尔森 C. Nielsen —— 管乐五重奏 Op.43（FS 100）第一乐章
% Allegro ben moderato —— 弱起 + 印刷谱 mm.1–11（共 12 个谱面小节；弱起处只有大管发声）
%
% 小节号：印本弱起不编号，第一个完整小节印 1，故 印刷谱 m.N = MusicXML 小节 N。
%   本谱例 = 弱起（XML 小节 0）+ XML 1–11 = 印刷谱 mm.1–11（不含印刷谱第 12 小节）。
%
% 速度：印本只印字样 "Allegro ben moderato"，没有节拍机数字；
%   下面的 ♩ = 100 是试听速度（取自本 XML 的 <sound tempo>），并非原谱标记。
%
% 谱源：PDMX MusicXML 文件 work-title "Quintet op. 43"
%       （5 声部 Flute / Oboe / A Clarinet / Horn in F / Bassoon；
%        每声部 507 小节 —— XML 里 5 个声部合计 2535 个 <measure> 元素；
%        第一乐章 = 该文件内小节编号 0–146，4/4，实音 E 大调 4 升）
%       逐小节比对见同目录 核对记录.md
%
% 调性：实音 E 大调。长笛／双簧管／大管为非移调乐器，记谱音 = 实音。
% 移调乐器一律写“演奏者看到的记谱音”，实音由 \transposition 产生：
%   A 调单簧管：记谱 C 实音 A（低小三度）→ \transposition a；记谱调号 G 大调（1 升）
%   F 调圆号　：记谱 C 实音 F（低纯五度）→ \transposition f；记谱调号 B 大调（5 升）
%   例：单簧管小节 4 的记谱 g'' 实音为 e''，
%   与长笛同处的 b'' 构成同一动机上的音色分裂。
%
% 记谱细节：大管在小节 5–6 按 XML 的 C 谱 4 线（次中音谱号）进入高音区，
%   小节 7 回到低音谱号；A 调单簧管小节 7 起亦进入记谱高音区。
% 拍号：小节 7 为 5/4、小节 8 回 4/4 —— XML 与校勘版印本均如此（印本在该小节线处
%   五个声部同时印 5/4，下一小节线回 4/4），照录，不作归一。
% =====================================================================

global = {
  \time 4/4
  \partial 4
  \tempo "Allegro ben moderato" 4 = 100
  % 小节号：逐小节出号；break-visibility = (行首 行中 行末) = (#t #t #f)，
  % 行末不印号（LilyPond 默认的 #all-visible 会在每行末多印下一行的号 + 末尾幽灵号）
  \set Score.barNumberVisibility = #all-bar-numbers-visible
  \override Score.BarNumber.break-visibility = #end-of-line-invisible
  % 弱起小节（XML 0）按印本不出号
  \once \override Score.BarNumber.stencil = ##f
}

% ---------------------------------------------------------------- 长笛
flute = {
  \global
  % 小节 0 弱起（1 拍休止；本乐章此处只有大管发声）
  r4 |
  % 小节 1–3 大管单独陈述主题，长笛静默
  r1 |
  r1 |
  r1 |
  % 小节 4 长笛在高音区接过同一动机（实音 b''–a''–gs''–a''–b''），装饰音上行回环
  r8\mp b''16( a''16 gs''16 a''16 b''16) r16
      \grace { a''16( b''16 } a''8-> gs''16) r16
      \grace { a''16( b''16 } a''8-> gs''16) r16 |
  % 小节 5
  fs''8( b''8-.) b''8-. b''8-. b''2~( |
  % 小节 6
  b''2 e'''2) |
  % 小节 7：拍号转 5/4（XML 与印本同）
  \time 5/4
  r2 r8\mp c'''16( b''16 a''8 e''8 a''8 e''8 |
  % 小节 8：回 4/4
  \time 4/4
  a''2) e'''8( b''16 a''16 g''8 fs''8 |
  % 小节 9
  e''8 ds''8 e''8 ds''8 e''8 fs''8 g''8 a''8 |
  % 小节 10
  b''8 cs'''8 d'''8 \f e'''8 fs'''4 e'''4 |
  % 小节 11
  d'''4 cs'''4 \textMark \markup \italic "calando" b''2) |
}

% -------------------------------------------------------------- 双簧管
oboe = {
  \global
  r4 |
  r1 |
  r1 |
  r1 |
  % 小节 4 双簧管在低三度上重复同一动机（实音 gs''–fs''–e''–fs''–gs''）
  r8 \pp gs''16( fs''16 e''16 fs''16 gs''16) r16
      \grace { fs''16( gs''16 } fs''8-> e''16) r16
      \grace { fs''16( gs''16 } fs''8-> e''16) r16 |
  ds''8( b'8-.) b'8-. b'8-. b'2~( |
  b'2 e''2) |
  % 小节 7：转 5/4
  \time 5/4
  r2 r8 \pp a''16( e''16 c''8 b'8 c''8 b'8 |
  % 小节 8：回 4/4
  \time 4/4
  c''8 d''8 e''8 fs''8 g''16 a''16 g''16 fs''16 e''8 b'8 |
  c''8 b'8 c''8 b'8 c''8 d''8 e''8 fs''8 |
  g''8 a''8 b''8 \pp cs'''8 d'''4~ d'''16 cs'''16 b''16 d'''16 |
  cs'''16 b''16 a''16 cs'''16 b''16 a''16 g''16 b''16
      a''16 g''16 fs''16 a''16 g''4) |
}

% ------------------------------------------- A 调单簧管（记谱音，实音低小三度）
clarinet = {
  \global
  \transposition a
  r4 |
  r1 |
  r1 |
  r1 |
  % 小节 4 单簧管入口音型（记谱 g''–d''–e''–d''–g''；实音 e''–b'–cs''–b'–e''）
  r8 \p g''16( d''16 e''16 d''16 g''16) r16
      f''8(-> d''16) r16 e''8(-> d''16) r16 |
  % 小节 5 与长笛同一动机的记谱形态（记谱 a''–g''–fs''–g''–a''，实音 fs''–e''–ds''–e''–fs''）
  r8 a''16( g''16 fs''16 g''16 a''16) r16
      \grace { g''16( a''16 } g''8-> fs''16) r16
      \grace { g''16( a''16 } g''8-> fs''16) r16 |
  \grace { f''16( g''16 } f''8-> d''16) r16 \grace { f''16( g''16 } f''8-> d''16) r16 e''2 |
  % 小节 7：转 5/4
  \time 5/4
  r2 r4 g'16( a'16) bf'16-. bf'16-. bf'4~( |
  % 小节 8：回 4/4
  \time 4/4
  bf'4. c''8 d''2~ |
  d''16 c''16 bf'16 c''16 a'4 bf'16 c''16 d''16 ef''16 f''16 c''16 a'16 f'16 |
  c''16 g'16 e'16 c'16 g'8) r8 d'''16( a''16 f''16 d''16 g''4~ |
  g''2.~ g''16 f''16 e''16 g''16) |
}

% ------------------------------------------------ F 调圆号（记谱音，实音低纯五度）
horn = {
  \global
  \transposition f
  r4 |
  r1 |
  r1 |
  r1 |
  % 小节 4 圆号以记谱 fs'（实音 b）长音进入，持续到小节 6
  fs'1\p->~ |
  fs'1~ |
  fs'2~ fs'8 gs'16( fs'16 e'16 b16) e'16-. e'16-. |
  % 小节 7 圆号短暂奏出动机片段（记谱 e'–b–e'–fs'–gs'–b'，实音 a–e–a–b–cs'–e'）
  \time 5/4
  e'16(-> b16) e'16-. e'16-. fs'16(-> gs'16) b'16-. b'16-. b'4 r2 |
  % 小节 8：回 4/4（圆号此后休止到谱例末）
  \time 4/4
  r1 |
  r1 |
  r1 |
  r1 |
}

% ---------------------------------------------------------------- 大管
bassoon = {
  \global
  \clef bass
  % 小节 0 弱起：大管单独起奏，两音 b–gs（实音即记谱音）
  b8\mp( gs8 |
  % 小节 1 主题核心：同音反复 e–e–e–ds–e–ds
  e4-.) e4-. e8( ds8 e8 ds8 |
  % 小节 2 上行音阶 e–fs–gs–a–b–cs'–ds'–e'
  e8 fs8 gs8 a8 b8 cs'8 ds'8 e'8 |
  % 小节 3 十六分音符下行回环
  f'4\mf~ f'16 e'16 d'16 f'16 e'16 d'16 c'16 e'16 d'16 c'16 b16 d'16 |
  b4) r4 r2 |
  % 小节 5 次中音谱号（XML C 谱 4 线）：大管在高音区接过动机
  \clef tenor
  r8 \p a'16( gs'16 fs'16 gs'16 a'16) r16
      \grace { gs'16 a'16 } gs'8-> fs'16 r16
      \grace { gs'16 a'16 } gs'8-> fs'8 |
  \grace { f'16( g'16 } f'8-> d'16) r16 \grace { f'16( g'16 } f'8-> d'16) r16 e'2 |
  % 小节 7 回到低音谱号；本小节为 5/4
  \clef bass
  \time 5/4
  r2 e'2.~( |
  % 小节 8 回 4/4
  \time 4/4
  e'8 d'16 c'16 b16 a16 g16 fs16 e4 e,4 |
  fs,4. b,8 e,4) r4 |
  r4 \p e'16( b16 g16 e16 b8) r8 r4 |
  r1 |
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Flauto" } {
      \set Staff.midiInstrument = "flute"
      % GM 73
      \clef treble
      \key e \major
      \flute
    }
    \new Staff \with { instrumentName = "Oboe" } {
      \set Staff.midiInstrument = "oboe"
      % GM 68
      \clef treble
      \key e \major
      \oboe
    }
    \new Staff \with { instrumentName = "Clarinetto in A" } {
      \set Staff.midiInstrument = "clarinet"
      % GM 71
      \clef treble
      \key g \major
      \clarinet
    }
    \new Staff \with { instrumentName = "Corno in F" } {
      \set Staff.midiInstrument = "french horn"
      % GM 60
      \clef treble
      \key b \major
      \horn
    }
    \new Staff \with { instrumentName = "Fagotto" } {
      \set Staff.midiInstrument = "bassoon"
      % GM 70
      \clef bass
      \key e \major
      \bassoon
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
