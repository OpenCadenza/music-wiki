# 写给移调乐器：记谱调与实际音高之间那层翻译

移调乐器不是"音高写错"，是同时存在两层谱面：演奏者读的那一层，听众听到的那一层。写给圆号 in F 的每一个音，都要在作曲这一步过一次减法——写出来的音，实际响出来低一个纯五度。这件事在纸上完全看不出来：谱面本身是干净的、正确的，错的只有"你以为你听到的"。Op.17 圆号奏鸣曲把这一层翻译的代价摆得很清楚：调号、音区、可用音级、以及两件乐器谁先开口，全都被这五度牵着走。

## 一、`\transposition f` 管的是什么

LilyPond 里写圆号声部，必须加一行 `\transposition f`。它不改变任何一个印刷出来的音符，只改 MIDI 回放时的音高：让整条声部在出声时下移纯五度。

漏写的后果很具体：谱面看起来完全正常，演奏者照着拉也完全正常，只有回放错——整个声部的音高比实音高五度，而且听上去"不和谐"却找不出哪个音写错了。这是移调乐器最典型的一类错误：错误不在谱面上，在谱面与声音之间的那层翻译里。

```lilypond title="贝多芬 Op.17 圆号奏鸣曲第一乐章" location="Allegro moderato，mm.1–8"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "horn" \relative c'' {
      \set Staff.midiInstrument = "french horn"
      % GM 60
      \transposition f
      \clef treble \time 4/4 \tempo 4 = 120
      \partial 4 g8.\f g16^\markup { \bold "Allegro moderato" }
      c2 g4-. e-. |
      c-.
      \clef bass
      \set Staff.middleCPosition = #-1
      c,-. r2 |
      R1 R1 R1 R1 R1 R1
    }
    \new PianoStaff <<
      \new Staff = "pianoRH" \relative c'' {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \clef treble \key f \major \time 4/4
        \partial 4 r4
        R1 |
        r2 r8 c\p( a' g) |
        g( f) f-. f-. f( g16 f) e8-. f-. |
        fs2( g8) c,( bf' a) |
        a( g) g-. g-. g8( a16 g) f8-. g-. |
        <gs e>2( <a f>8) f( c' bf) |
        \override Script.avoid-slur = #'outside
        bf\prall( a) a\prall( g) g\prall( f) f\prall( e)
        e\prall( d) d\prall( c) c\prall( bf) bf\prall( a)
        \revert Script.avoid-slur
      }
      \new Staff = "pianoLH" \relative c'' {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \clef bass \key f \major \time 4/4
        \partial 4 r4
        R1 R1 |
        r4 <c a f> <c a f> <c a f> |
        <c bf e,>2~ <c bf e,>8 r r4 |
        r4 <c bf e,> <c bf e,> <c bf e,> |
        <c bf f>2~ <c bf f>8 r r4 |
        r8 f,( c' bf) bf( a) <c a>( <bf g>) |
        <bf g>( <a f>) <a f>( <g e>) <g e>( <f d>) <f d>( <e c>) |
      }
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

看第一行谱的调号：**圆号那行是空的，钢琴那两行有一个降号**。这不是抄谱漏了。曲子是 F 大调，钢琴照实音写，调号一个降；圆号的谱面整体上移五度，写出来就是 C 大调，没有升降号。同一首曲子，三种调号观感——因为写在纸上的调名不同。

## 二、五度差在音符上是什么样

第 1 小节圆号吹的是 `c''2 g'4-. e'-.`。把每个音下移纯五度：

- 写的 c″ 响 f′
- 写的 g′ 响 c′
- 写的 e′ 响 a

听起来是 f′–c′–a——F 大三和弦的分解，和钢琴的 F 大调对上了。第 2 小节写 `c'' c'`，实音 `f′ f`，落在低音区，所以这一小节换了低音谱号。

这就是移调乐器在纸上的样子：**音程关系不变，调号不变，只有绝对高度变了**。写 c–g–e 还是 c–g–e，落到耳朵里成了 f–c–a。所以判断圆号写得好不好，不能看谱面有多高，要先把每个音减掉五度再看。

方向也要记牢：实音永远比记谱低。看着很高的音（写 c‴）实音只是 f″，没那么高；看着很低的音（低音谱号的 c′）实音是 f，比看到的还要再低五度。两头都要减，不要只在"听起来不对"的时候才减。

## 三、能被吹出来的音只有一条泛音列

自然圆号没有活塞，只能吹基音的泛音列。F 调圆号在记谱上的可用音是：

c、g、c′、e′、g′、b♭′、c″、d″、e″、f″、g″、a″、b♭″、b″、c‴

一共十五个音，跨三个八度。列外的音（写 c♯、d♯、e♭、f♯、a♭ 之类）要靠右手伸进喇叭口把管长改掉（bouché，塞音），音色会变闷、音量会掉一档。

这条限制直接决定了两个乐章的写法差异。

第一乐章第 1 小节那三个音 c″、g′、e′ 全在泛音列上（第 8、6、5 泛音），所以那个开头是敞开的、亮的，力度 f 也撑得住。整段号角式的分解和弦都建在骨干泛音上。

第二乐章正好相反。圆号的写谱线是 `ef8[( c16) r32 c]-.`、`b8-. d-.` 这一串——`ef`、`b`、`d` 全在泛音列之外，每一个都要塞。所以这个乐章圆号听起来是蒙住的、带鼻音的，力度标 p 与 pp，不是客气，是物理上就吹不响。

```lilypond title="贝多芬 Op.17 圆号奏鸣曲第二乐章" location="Poco Adagio, quasi Andante，mm.1–8"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "horn" \relative c'' {
      \set Staff.midiInstrument = "french horn"
      % GM 60
      \transposition f
      \clef treble \time 2/4 \tempo 4 = 42
      \partial 8 c16.\p c32^\markup { \bold "Poco Adagio, quasi Andante" }
      \repeat unfold 2 { ef8[( c16) r32 c]-. } |
      b8-. d-. r4 |
      R2 |
      r4 r8 d16.\pp d32 |
      \repeat unfold 2 { ef8[-. ef16.-. ef32]-. } |
      ef8-. d-. r4 |
      R2 |
      r4 r8 bf16.\p bf32
    }
    \new PianoStaff <<
      \new Staff = "pianoRH" \relative c' {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \key f \minor \time 2/4
        \clef bass
        \partial 8 r8
        <c af f>8-. r <c af f>-. r |
        <c g e>-. <c g e>-. \clef treble r8 f'16. f32 |
        << { \repeat unfold 2 { af8[( f16) r32 f] } }
        \\ { \repeat unfold 2 { b,8. r32 b } } >> |
        <e c'>8-. <c g>-. r4 |
        \repeat unfold 2 { <f, c>8-. <f c>16.-. <f c>32-. } |
        <f bf,>8-. <ef bf>-. r <c' f>16.-. <c f>32-. |
        <ef bf'>8-. <ef bf'>16.-. <ef bf'>32-. <d af>8-. <d af>16.-. <d af>32-. |
        <ef g,>8 r r4 |
      }
      \new Staff = "pianoLH" \relative c, {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \key f \minor \time 2/4
        \clef bass
        \partial 8 r8
        f8-. r f-. r |
        <c' c,>-. <c c,>-. r4 |
        \clef treble
        << { \repeat unfold 2 { f'8[( af16) r32 af] } }
        \\ { \repeat unfold 2 { df,8. r32 df } } >> |
        <g c,>8-. <e c>-. r4 |
        \clef bass
        f,8-. f16.-. f32-. ef8-. ef16.-. ef32-. |
        d8 ef r <af ef'>16.-. <af ef'>32-. |
        <bf g'>8-. <bf g'>16.-. <bf g'>32-. <bf f'>8-. <bf f'>16.-. <bf f'>32-. |
        <ef, ef'>8-. r r4 |
      }
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

第 2 小节是这篇文章最想做的一张"翻译样本"。圆号写 `b8-. d-.`，实音是 e、g；同一小节钢琴写 `<c g e>`，是一个 C 大三和弦。三行谱摆在一起看：圆号那行是 `b`、`d`，钢琴那行是 `c`、`g`、`e`——纸面上完全不像同一个和弦，听起来严丝合缝。

## 四、写不出来的音怎么办：换八度、换手、换乐器

泛音列是稀疏的：相邻两个可用音之间常常隔着一个三度、一个四度甚至一个五度。所以圆号写不出级进的半音，只能跳。

第三乐章第 6 小节有一句 `b f''`——从写的 b 直接跳到 f″，将近两个八度。不是因为作曲家想跳，是因为中间那一大段半音根本不存在于泛音列里，跳过去是唯一能落地的方式。

遇到必须半音进行的地方，一般有三条路：

一，把它交给钢琴。Op.17 慢乐章里，需要长音与和声变化的地方都在钢琴那边（`<c af f>`、`<c g e>` 一拍一个和弦），圆号的半音全部写成短音——十六分、三十二分，一闪就过去。

二，换八度。同一个音名在泛音列的上八度里往往可用（写 c 不可用时改用 c″），代价是整句跳进。

三，塞音。这是最贵的一种：音准难控、音色发闷、音量下降，只适合短音或经过音，不适合长音旋律。

Op.17 慢乐章的做法是第一和第三条混用：圆号的长音全部落在泛音列上，短的装饰句用塞音。

## 五、三个乐章：谁先开口

同一个编制，三个乐章的分工完全不同，差别集中在"谁先开口"这一件事上。

第一乐章：圆号先。第 1 小节圆号一个人吹出号角动机的前三个音（`c''2 g'4-. e'-.`，实音 f′–c′–a），第 2 小节第一拍才落回 `c'`（实音 f）；钢琴整小节是 `R1`。钢琴第 2 小节第 3 拍才进，力度 p——而且进的位置正好是圆号休止的那两拍。之后第 3 到第 9 小节圆号连续休止七小节，钢琴一个人把动机接过去展开。

第二乐章：同时。钢琴从第 1 小节起就在，但它给的是和弦（`<c af f>`、`<c g e>`），一拍一个，不构成旋律；圆号在上方唱。这是"伴奏 + 独奏"的分工，和第一乐章"轮流"完全不同。

第三乐章：钢琴先。钢琴第 1 小节就把回旋主题说出来，圆号的谱面是 `r2` 加三小节 `R1`——前三个整小节不响，第 4 小节才用 `g4-.\p g-.` 进来。

三个乐章放在一起看，就是三种合作的模板：轮流说（I）、一个唱一个铺（II）、一个起头一个接（III）。写法上的差别不在音符，在休止符写在哪一行。

## 六、钢琴在这首里和小提琴奏鸣曲里不一样

同为两件乐器的奏鸣曲，Op.17 的钢琴和小提琴奏鸣曲里的钢琴不是同一个角色。

音量。自然圆号比现代钢琴轻得多，所以这里钢琴的第一个力度记号是 p，而且钢琴的织体是稀疏的：慢乐章右手一拍一个和弦，左手两拍一个八度，中间大量留白。小提琴奏鸣曲里不需要这样让——小提琴的穿透力足够和钢琴正面抗，Op.47 的钢琴一进来就是 fp 的四音和弦。

音区。圆号的实音集中在中低音区（f–f″），钢琴在这里往两头跑：右手走高音区的十六分音符，左手用 `<f f,>`、`<c c,>` 这样的八度顶住低音，中间那一层留给圆号。小提琴奏鸣曲里中间层是钢琴的地盘（Op.47 的钢琴右手和弦正好压在 c′–e″）。

留白。第一乐章第 1 小节钢琴整小节空着，第 3–9 小节圆号整段空着。这种"整小节整小节地让"在小提琴奏鸣曲里很少见——那里更常见的是两件乐器同时在说话，靠音区和节奏错开，而不是靠一方完全闭嘴。让位的单位不一样：一首是拍，一首是小节。

## 三条可以带走的规则

一，先写 `\transposition`，再写音符。移调标记是这一层翻译的开关，写了它，谱面写的是演奏者读的，出声是听众听的；两个都对，谱子才成立。

二，判断移调声部的音区，要先把每个音减五度再判断。写在纸上的 c″ 不是 c″，是 f′。装配弦乐、木管与钢琴时，"谁在中间"这个问题必须用实音回答。

三，写自然圆号（或任何受泛音列限制的乐器）时，先排骨干音。把旋律的骨架音挑出来，确认它们在泛音列上；其余的经过音再决定是交给钢琴、换八度，还是塞音。骨架音落在列外，整句就废了。

同体裁里两件乐器如何分工，见[两件乐器的平等不是各写一半，是谁在什么时候让位](violin-sonata-equality.md)；钢琴写作的一般问题见[钢琴奏鸣曲](../piano/sonatas/index.md)。
