# 怎样把谐谑曲写得令人不安？

先让听者认出一个动作，再改变他们对下一次动作的预期。马勒第四交响曲第二乐章让熟悉的三拍
遇到一把升弦的小提琴，第六交响曲让拨弦音型从长短不同的小节末尾伸出来，第七交响曲则把
强弱拍交给不同的乐器。三段可以分别练习音色、拍组长度和重音位置。

## 第四交响曲第二乐章：给舞步换一把琴

第 6 小节第 2 拍后半，独奏小提琴用三个上行十六分音符插入，谱上标着 *Wie eine Fidel*，
要求像民间提琴那样拉。四条空弦从 G₃、D₄、A₄、E₅ 升到 A₃、E₄、B₄、F♯₅。
谱例保留独奏小提琴演奏者读到的音，实音整体高一个全音。开头写出的 A₄–D♭₅–F₅ 因而响成
B₄–E♭₅–G₅，第一个音可以直接用重新调高的 A 弦空弦演奏。

```lilypond title="马勒 第四交响曲 第二乐章" location="In gemächlicher Bewegung. Ohne Hast.，mm.6–8" id="mahler-4-ii-scordatura"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff {
      \set Staff.instrumentName = "Solo-Violine"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \transposition d'
      \key bf \minor
      \time 3/8
      \set Score.currentBarNumber = #6
      \tempo "In gemächlicher Bewegung. Ohne Hast." 8 = 160

      r8 r16 a'!16\mf\< ( ^\markup { "Wie eine Fidel" } df'' f'' |
      e''!8.\p\< c''16 a'! ef''\f ) |
      df''16\p ( ef'' df'' c'' bf' df'' ) |
    }
    \new Staff {
      \set Staff.instrumentName = "Viola solo"
      \set Staff.midiInstrument = "viola"
      % GM 41
      \clef alto
      \key c \minor
      R4. | R4. |
      c''16-.\pp^\markup { "mit Dämpfer" } g'-. c''8-. ef'-. |
    }
    \new Staff {
      \set Staff.instrumentName = "Violoncello solo"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef tenor
      \key c \minor
      R4. | R4. |
      c'16-.\pp^\markup { "mit Dämpfer" } ef'-. g'8( af'16-.) g'-. |
    }
  >>
  \layout { }
  \midi { }
}
```

第 8 小节，独奏小提琴保持活跃的十六分音符；中提琴与大提琴各有一个加弱音器的独奏声部以
pp 加入。让前景独奏用开放的发音，让伴奏的起音更软，升弦的声音才有清楚的参照。写类似段落时，
在总谱实音、独奏分谱和指法之间核对。相同的 B₄ 在普通琴上需要按弦，在升弦琴上可以用空弦。

## 第六交响曲谐谑曲：同一个拨弦音型，等不同的时间

排练号 88 起，第一小提琴以 pp 拨弦。听每组跨小节的四个 A₅，前三次都从前一小节最后一个
八分音符起步，接到 3/8 小节的三个等长音。三次起步所在小节依次是 3/8、2/4、3/4。
八分音符保持等长，前面依次空出两个、三个、五个八分音符。竖琴在 2/4 和 3/4 小节开头奏
带重音的 A₄，把小节边界和小提琴的弱起分给两个音区。

```lilypond title="马勒 第六交响曲 谐谑曲" location="Poco meno mosso，排练号 88 起七小节" id="mahler-6-scherzo-reh88"
\version "2.26.0"
\language "english"

meters = {
  \time 3/8 s4. | s4. |
  \time 2/4 s2 |
  \time 3/8 s4. |
  \time 3/4 s2. |
  \time 3/8 s4. |
  \time 2/4 s2 |
}

\score {
  \new StaffGroup <<
    \new Staff {
      \set Staff.instrumentName = "Violine I"
      \set Staff.midiInstrument = "pizzicato strings"
      % GM 45
      \key d \major
      \tempo "Poco meno mosso" 8 = 144
      << \meters {
        r8 r8 a''8\pp^\markup { pizz. } | a''8-. a'' a'' |
        r4 r8 a''8 | a''8 a'' a'' |
        r4 r4 r8 a''8 | a''8 a'' a'' |
        R2 |
      } >>
    }
    \new Staff {
      \set Staff.instrumentName = "Harfe I"
      \set Staff.midiInstrument = "orchestral harp"
      % GM 46
      \key d \major
      << \meters {
        R4. | R4. |
        a'2->\p | R4. |
        a'2.-> | R4. |
        a'2-> |
      } >>
    }
  >>
  \layout { }
  \midi { }
}
```

写这种变拍时，先把固定音型标在时间线上，再移动小节线和其他声部的重音。保留每个短音的速度，
让等待时间发生变化。即使听者已认出重复音型，也需要重新判断它何时回来。

## 第七交响曲第三乐章：让第三拍抢走重音

开头是 3/4。定音鼓在弱起敲带重音的 A₂，并迅速止音。第 1 小节第一拍，大提琴与低音提琴
以弱奏拨出 B♭，随后各休止两拍。第 5–8 小节，低弦已在每个第一拍拨弦，定音鼓在每个第三拍
回应。定音鼓给第 6、8 小节的第三拍加重音，第 5、7 小节的第三拍保持轻触。谱上特意要求演奏者
注意这种有重音与无重音的交替。

```lilypond title="马勒 第七交响曲 第三乐章" location="Schattenhaft，弱起及 mm.1–8" id="mahler-7-iii-schattenhaft"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff {
      \set Staff.instrumentName = "Pauken"
      \set Staff.midiInstrument = "timpani"
      % GM 47
      \clef bass
      \time 3/4
      \tempo "Schattenhaft. Fließend, aber nicht schnell." 4 = 132
      \partial 4 a,4->\p^\markup { "Immer schnell abdämpfen" }
      R2. | r4 r a,-> | R2. | r4 r a,-> |
      r4 r a, | r4 r a,-> | r4 r a, | r4 r a,-> |
    }
    \new Staff {
      \set Staff.instrumentName = "Violoncelli"
      \set Staff.midiInstrument = "pizzicato strings"
      % GM 45
      \clef bass
      \key d \minor
      r4
      bf,4\p^\markup { pizz. } r r | R2. | bf,4 r r | R2. |
      bf,4^\markup { "sempre p" } r r | bf, r r | bf, r r | bf, r r |
    }
  >>
  \layout { }
  \midi { }
}
```

两种短音之间有空白，力度也压得很低。听者可以从低弦找到第一拍，又会被较突出的定音鼓拉向第三拍。
这里的两个音是 A 与 B♭，把两个拍位的音型听成问答时，半音让这句问答带着持续的紧张感。

## 写给 Agent 的任务

1. 先写一个可反复辨认的三拍动作，例如弱起加三个短音。保留一个标记第一拍的声部。
2. 生成三个试听版本。第一版只改变前景的发音或演奏动作。第二版保留短音的时值，用一次延长的
   小节推迟弱起。第三版保留小节长度，把重音移到另一件乐器的第三拍，并安排一次无重音的重复。
3. 逐版听短音是否仍能被辨认为同一个动作。检查变拍前后的八分音符时长是否一致，重音是否落在
   预定拍位。写到升弦时，另核对实音和演奏者读到的音。
