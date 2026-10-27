# 动机细胞怎样决定段落边界

Op.67 第一乐章开头的十六个小节，段落边界不是和声划出来的。前五小节里没有一个走到主和弦的终止式，只有一个四音细胞说了两遍，每遍后面挂一个延长记号。真正决定"这里断开、那里连上"的，是这个细胞还有没有话要说：说完就停，还有话要说就撤掉延长记号、改写成连线。

```lilypond title="贝多芬 Op.67 第一乐章" location="Allegro con brio，mm.1–16"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "flauti" {
      \set Staff.instrumentName = "Flauti"
      \set Staff.shortInstrumentName = "Fl"
      \set Staff.midiInstrument = "flute"
      % GM 73
      \clef treble \key c \minor \time 2/4
      \tempo "Allegro con brio" 2 = 96
      r2 | r2^\fermata | R2 | R2 | r2^\fermata | R2 | R2 | \break
      R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
    }
    \new Staff = "oboi" {
      \set Staff.instrumentName = "Oboi"
      \set Staff.shortInstrumentName = "Ob"
      \set Staff.midiInstrument = "oboe"
      % GM 68
      \clef treble \key c \minor \time 2/4
      R2 | r2^\fermata | R2 | R2 | r2^\fermata | R2 | R2 |
      R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
    }
    \new Staff = "clarinetti" {
      \set Staff.instrumentName = "Clarinetti in B."
      \set Staff.shortInstrumentName = "Cl"
      \set Staff.midiInstrument = "clarinet"
      % GM 71
      \transposition bf
      \clef treble \key d \minor \time 2/4
      r8 a'8\ff[ a' a' ] | f'2^\fermata | r8 g'8[ g' g' ] | e'2~ | e'2^\fermata | R2 | R2 |
      R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
    }
    \new Staff = "fagotti" {
      \set Staff.instrumentName = "Fagotti"
      \set Staff.shortInstrumentName = "Fg"
      \set Staff.midiInstrument = "bassoon"
      % GM 70
      \clef bass \key c \minor \time 2/4
      R2 | r2^\fermata | R2 | R2 | r2^\fermata | R2 |
      c'2\p~ | c'2~ | c'2~ | c'2 | b2~ | b2~ | b2~ | b2 | c'2 | b2 |
    }
    \new Staff = "corni" {
      \set Staff.instrumentName = "Corni in Es."
      \set Staff.shortInstrumentName = "Co"
      \set Staff.midiInstrument = "french horn"
      % GM 60
      \transposition ef
      \clef treble \key c \major \time 2/4
      R2 | r2^\fermata | R2 | R2 | r2^\fermata | R2 | R2 |
      R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
    }
    \new Staff = "trombe" {
      \set Staff.instrumentName = "Trombe in Es."
      \set Staff.shortInstrumentName = "Tb"
      \set Staff.midiInstrument = "trumpet"
      % GM 56
      \transposition ef
      \clef treble \key c \major \time 2/4
      R2 | r2^\fermata | R2 | R2 | r2^\fermata | R2 | R2 |
      R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
    }
    \new Staff = "timpani" {
      \set Staff.instrumentName = "Timpani in C.G."
      \set Staff.shortInstrumentName = "Ti"
      \set Staff.midiInstrument = "timpani"
      % GM 47
      \clef bass \key c \major \time 2/4
      R2 | r2^\fermata | R2 | R2 | r2^\fermata | R2 | R2 |
      R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
    }
    \new Staff = "violinoone" {
      \set Staff.instrumentName = "Violino I."
      \set Staff.shortInstrumentName = "Vn I"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 2/4
      r8 g'8\ff[ g' g' ] | ef'2^\fermata | r8 f'8[ f' f' ] | d'2~ | d'2^\fermata | R2 | R2 |
      r8 ef''8\p[ ef'' ef'' ] | c''2~ | c''4 r4 | R2 |
      r8 f''8[ f'' f'' ] | d''2~ | d''8[ g'' g'' f'' ] | ef''2( | d''8)[ g'' g'' f'' ] |
    }
    \new Staff = "violinotwo" {
      \set Staff.instrumentName = "Violino II."
      \set Staff.shortInstrumentName = "Vn II"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 2/4
      r8 g'8\ff[ g' g' ] | ef'2^\fermata | r8 f'8[ f' f' ] | d'2~ | d'2^\fermata | r8 g'8\p[ g' g' ] |
      ef'2~ | ef'2~ | ef'2~ | ef'8[ g' g' g' ] |
      d'2~ | d'2 | g'2~ | g'2~ | g'8[ ef' ef' f' ] | g'2~ |
    }
    \new Staff = "viola" {
      \set Staff.instrumentName = "Viola"
      \set Staff.shortInstrumentName = "Va"
      \set Staff.midiInstrument = "viola"
      % GM 41
      \clef alto \key c \minor \time 2/4
      r8 g8\ff[ g g ] | ef2^\fermata | r8 f8[ f f ] | d2~ | d2^\fermata | R2 | r8 af'8\p[ af' af' ] |
      g'2~ | g'2~ | g'4 r4 | r8 af'8[ af' af' ] | g'2 | d'2~ | d'2 | ef'8[ ef' ef' f' ] | g'2~ |
    }
    \new Staff = "violoncello" {
      \set Staff.instrumentName = "Violoncello"
      \set Staff.shortInstrumentName = "Vc"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass \key c \minor \time 2/4
      r8 g,8\ff[ g, g, ] | ef,2^\fermata | r8 f,8[ f, f, ] | d,2~ | d,2^\fermata | R2 |
      c'2\p~ | c'2~ | c'2~ | c'2 | b2~ | b2~ | b2~ | b2 | c'2 | b2 |
    }
    \new Staff = "basso" {
      \set Staff.instrumentName = "Basso"
      \set Staff.shortInstrumentName = "Cb"
      \set Staff.midiInstrument = "contrabass"
      % GM 43
      \transposition c
      \clef bass \key c \minor \time 2/4
      r8 g8\ff[ g g ] | ef2^\fermata | r8 f8[ f f ] | d2~ | d2^\fermata | R2 | R2 |
      R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
    }
  >>
  \layout { }
  \midi { }
}
```

## 第 1 小节：六行在响，六行在等

第 1 小节是全乐队 fortissimo，但总谱上只有六行发声：第一小提琴、第二小提琴、中提琴、大提琴、低音提琴，加单簧管。长笛、双簧管、大管、圆号、小号、定音鼓六行全部休止。

这六行压在三个八度上。第一小提琴与第二小提琴同度 g′（G4）；单簧管是 B 调乐器，记谱 a′，实音也是 g′，所以最上面那个八度上站了三条声部。中提琴 g（G3）一条。大提琴 g,（G2），低音提琴记谱 g、实音 G2，两行同度。

三个八度，顶上一个挤三条，下面两个各一到两条。这不是"全员加厚"，是把音量全压在顶端——数一数同时加倍的层数，是判断这种写法值不值的第一道关，[配器分层：谁在加倍谁](orchestration-layers.md)里对此有更细的逐声部拆解。

第 2 小节发声的六行一起落到 ef′ / ef / ef,（Eb4 / Eb3 / Eb2），二分音符，带延长记号。细胞在这里说完：**三个同音，加一次下行大三度**。

## 三度：唯一能同时当动机和和声骨架的音程

三个同音只给节奏和压力，一个音高信息也不给。整个细胞里带音高的只有最后那一次跳进，所以它的全部音高内容是两个音级：G 和 Eb。

这两个音相隔三度。选三度不是修辞：

- 二度太近。级进听起来是"继续走"，不构成落点；写成 g′–g′–g′–f′，细胞就没有收尾。
- 四度、五度太空。它们给的是框架，不告诉你大调还是小调。
- 三度是唯一一个既构成明确落点、又直接给出调式的音程。

它还有第二个性质。在 c 小调里 g 是 5̂、ef 是 3̂，细胞里没有 1̂。一个缺根音的三度，正好是可以被任意低音接管的和声骨架：低音写什么，它就成为那个和弦的一部分。

这一条在同一段里立刻兑现。第 8 小节第一小提琴把细胞搬到 ef″–ef″–ef″ → c″，底下大提琴从第 7 小节起一直按着 c′，同一个三度此刻是 c 小调的三音到根音。第 12 小节第一小提琴换成 f″–f″–f″ → d″，底下大提琴从第 11 小节起按着 b（还原），同样的形状，f 与 d 落在 b 上面，是 b–d–f 减三和弦的五音与三音。

同一个三度，一次读成 3̂→1̂，一次读成 5̂→3̂。形状没变，功能全变。这就是它能既当动机又当骨架的原因：**它只说"两个音相隔三度"，不说这两个音是和弦里的第几个音。**

## 第 2 小节的延长记号：说完就停

第 2 小节那个延长记号容易被当成"这个音拖长一点"。不是。

ef′ 是二分音符，本身已经占满 2/4 的一整小节。延长记号不改写它的记谱时值，它改的是"下一小节什么时候来"。

证据在休止的那六行：第 2 小节它们写的是 `r2^\fermata`，休止符上也画了延长记号。如果延长只是某个音的时值问题，休止的声部不必标；标了，说明这是全体的停顿，不是某个声部的自由处理。

所以第 2 小节的延长记号是一条结构指令：这里是一段的结尾，下一小节从头开始。

第 3–5 小节把同一件事做第二遍：f′–f′–f′ → d′，小三度。这一次落点不是二分音符就完，而是跨两小节连线（第 4 小节 `d'2~`，第 5 小节 `d'2` 带延长记号）。同一个收尾动作，长度从 2 拍变成 4 拍再加延长。

两遍陈述的区别只有两条：三度从大变小，落点从 2 拍变 4 拍。这是"再说一遍"，不是"再写一句"。

## 停与不停：第 6 小节换的是配器

第 6 小节，第二小提琴单独进来，p，还是 g′–g′–g′ → ef′。细胞一个音都没改。

但延长记号没有了。ef′ 写成 `ef'2~`，连过第 7、8、9 三小节共六拍，第 10 小节再添一个八分音符才放手，随后是三个 g′ 八分音符。

**延长记号被换成了连线。** 同一件事，一次是"停住不动"，一次是"按住，但时间继续走"。段落边界就在这里分出来：

- 细胞说完 → 延长记号，下一小节重新开始。
- 细胞后面还要接 → 撤掉延长记号，把停的时值写进拍子。

那什么时候该重复、什么时候必须换材料？看第 1–5 小节做了什么：第二遍换掉了两个维度，音程（大三度→小三度）和落点长度（2 拍→4 拍）。第 6 小节换掉的是另外两个，配器（六行→一行）和力度（ff→p）。

规则是：**每次重复必须换掉一个维度。** 第 5 小节之后如果再来一遍 f′–f′–f′ → d′，换不掉任何东西，那句话就白说了。所以这里改的不是"说什么"，是"谁在说"。

## 同一段里的四处变形

**音区。** 第 8 小节第一小提琴 ef″–ef″–ef″ → c″，第 12 小节 f″–f″–f″ → d″。第 12 小节就是第 3 小节那一句原样高一个八度：音程、节奏、跳进方向全不变，只有绝对音高变了；第 8 小节则换了起点，但仍是三个同音加下行小三度。四次陈述的第一个音依次是 g′、f′、ef″、f″——前三次是下行级进，第四次回到 f″，落点始终在它下方三度。推动音乐往前的是那条级进，不是细胞本身。

**乐器。** 第 1–5 小节六行齐奏，第 6 小节只剩第二小提琴一行，第 8 小节换成第一小提琴。同一个细胞，三次换承载它的声部。

**和声。** 第 8 小节底下是 c 踏板，第 12 小节是 b 踏板，同一个三度读成两种和弦音，见上一节。

**停的余地。** 细胞说完之后留给"停"的空间一路缩到零。第 2 小节是延长记号，不计拍子；第 8–10 小节里落点 c″ 撑了三拍，第 10 小节后半是一个四分休止，第 11 小节整小节空着；到第 12–14 小节，落点 d″ 一松手就是 `d''8[ g'' g'' f'' ]`，新句子紧接着进来，一拍都不留。八分音符的时值从头到尾没改过一次——被压掉的是停，不是音。

## 改到什么程度就不再是同一个细胞

不变的部分只有两条：**三个等时值同音，加一次下行三度**。其余全可动——绝对音高、八度、乐器、力度、落点长短、底下是什么和声。

边界在第 7 小节的中提琴：af′–af′–af′ → g′。节奏与细胞完全相同，落点低了一个小二度。它借的是细胞的节奏，不是细胞的音程，听起来是一条下滑的半音线，不是那个细胞。二度是级进，不构成落点。

反过来，把落点写成下行五度也不成立：五度是空框架，不告诉你大调还是小调，细胞就失去了"一句话说完"的性质。

所以判据只有一条：**三个同音之后那一次跳进是不是三度**。是三度，改音区、改乐器、改和声、改长短，都还认得出；不是三度，节奏一模一样也不是。

## 可以照做的五条

一，**细胞只留一个音程。** 同音重复给节奏，一次跳进给音高。第二个音程会把细胞变成旋律，就搬不动了。

二，**让这个音程是缺根音的三度。** 只有两个音级、不含 1̂，它才能被不同的持续音接管。

三，**说完就画延长记号，而且画在休止的声部上。** 全体停顿才是段落边界；只标一个声部，那是独奏的自由处理。

四，**要接下去就把延长记号换成连线**，把停的时值写进拍子。

五，**重复时每次换一个维度**；换不掉，就换配器。
