\version "2.26.0"

% 用 LilyPond 自身解析 \relative，确认 Brahms Op.90 III 底本的绝对音高。
% 直接抄录底本（downloads\brahms90\BrahmsSYMPH3M3）的裸音序列，去掉宏与力度，
% 以求绝对音高。文件头 \relative c'（大提琴）/ \relative c（大管）与底本一致。

cello = \relative c' {
  c16.( d32)              % 弱起
  ees4.(                  % m.1
  g16.[ f32 d8] c16.( d32)   % m.2
  ees4.(                  % m.3
  bes'16. aes32 d,8) d16.[ ees32]  % m.4
  f4 aes16.( g32)         % m.5
  ees4 g16.( f32)         % m.6
  c8.( d32 c) b16[( c])   % m.7
  d8( ees e)              % m.8
}

fagotto = \relative c {
  r8                      % 弱起
  c4 r8                   % m.1
  f4 r8                   % m.2
  c4 r8                   % m.3
  f4 r8                   % m.4
  b,4 r8                  % m.5
  c4 r8                   % m.6
  aes'4 r8                % m.7
  g8 c bes                % m.8
}

\score {
  <<
    \new Staff { \clef tenor \cello }
    \new Staff { \clef bass \fagotto }
  >>
  \layout { }
  \midi { }
}