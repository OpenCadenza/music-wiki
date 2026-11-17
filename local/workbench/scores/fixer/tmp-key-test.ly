\version "2.26.0"
\language "english"

% 干净测试：LilyPond 中裸写音名是否受 \key 影响
\score {
  \new Staff {
    \key df \major
    a'4 d'4 g'4 c'4 e'4 b'4 f'4
  }
  \layout { }
  \midi { }
}