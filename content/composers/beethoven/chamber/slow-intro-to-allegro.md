# 慢引子怎样被快板吃掉：Op.69 第三乐章的一次交接

慢引子接快板，最省力的写法是让快板"冲进来"：引子渐强，快板用强奏把它打断。Op.69 第三乐章不这么做。它的引子停在属七和弦上，用两个延长记号把时间悬住，然后快板以 *pp* 起——转折不是变响，是变轻。更值得注意的是：引子的材料在快板里一次也没有回来，被吃掉的只有它的时间和它的调性。

先看引子的前八小节。

```lilypond title="贝多芬 Op.69 第三乐章" location="Adagio cantabile，mm.1–8"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "one" {
      \set Staff.instrumentName = "Violoncello"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef tenor \key e \major \time 2/4
      \tempo "Adagio cantabile" 8 = 46
      % m.1
      R2
      % m.2
      fs'4.\p e'8 ~
      % m.3
      e'8[ e'( a' gs'16 e')]
      % m.4
      fs'4 fs'8 r
      % m.5
      fs'8. fs'16 fs'16( e') ds'\staccato e'\staccato
      % m.6
      e'4._\markup { \italic "cresc." }( gs'16. e'32)
      % m.7
      ds'8\p( fs'4) fs'8
      % m.8
      fs'4 ~ fs'16[ b b b]
    }
    \new Staff = "two" {
      \set Staff.instrumentName = "Pianoforte"
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key e \major \time 2/4
      % m.1
      b'4\p( e''16 ds'' e'' gs')
      % m.2
      b'4( a'8 gs'16^\trill a'32 b')
      % m.3
      cs''8([ b' ds'' e''16 gs'])
      % m.4
      b'8.([ as'16] a'8) r
      % m.5
      a'8. a'16 a'( gs') fs'\staccato( e'\staccato)
      % m.6
      cs''4_\markup { \italic "cresc." }( b'8) e''16.( cs''32)
      % m.7
      b'4_\markup { \italic "p dolce" } as'
      % m.8
      a'!8^\trill[ ~ a'32 gs' a' fs']
      \new Voice { ds'32[ b \stemUp \change Staff = "three" as32 a gs a fs b] e8 }
    }
    \new Staff = "three" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key e \major \time 2/4
      % m.1
      e16\p( b gs b e b gs b)
      % m.2
      ds( b fs b ds b e b)
      % m.3
      a( cs' gs b <fs a> b <e gs> b)
      % m.4
      ds( b fs b ds b fs b)
      % m.5
      ds16( b fs b) ds( e) <a b>\staccato( <gs b>\staccato)
      % m.6
      a e' cs' e' <gs b> e' <e gs> cs'
      % m.7
      fs16 ds' b ds' fs e' cs' e'
      % m.8
      <b ds'>8 r r4
    }
  >>
  \layout { }
  \midi { }
}
```

## 一、引子的形状

引子是 2/4，调号四个升号，也就是 E 大调——A 大调的属调。速度标 ♪=46，一小节两拍。

第 1 小节只有钢琴：右手从 b′ 起，b′–e″–d♯″–e″–g♯′，前一半是四分音符接四个十六分音符；左手是 e–b–g♯–b 的八分音符分解，一小节走两遍（八个音）。大提琴整小节休止。

第 2 小节大提琴才进来，从 f♯′ 起：附点四分音符 f♯′，接八分音符 e′，再连到下一小节。第 3 小节是 e′–e′–a′–g♯′–e′，第 4 小节 f♯′ 两次、休止。第 5 小节六个音挤在一小节里，落点是 1.0、1.75、2.0、2.25、2.5、2.75 拍——f♯′ 附点八分、f♯′ 十六分、f♯′ 十六分、e′、d♯′、e′。第 6 小节 e′ 附点四分音符，接 g♯′ 附点十六分与 e′ 三十二分。第 7 小节 d♯′ 与 f♯′，标 *p dolce*。第 8 小节 f♯′ 连出去，十六分音符处夹进 b–b–b。

整段引子有十七小节，之后是不带小节线的散板。十七小节里，速度、调号、拍号一次都没有变。

## 二、钢琴先动，大提琴等一小节

m.1 的全部内容是钢琴的：右手一句话，左手八分音符流动。大提琴在 m.2 才开口，而且是从 f♯′ 这个不解决任何东西的音上开口——它不是主音（E 大调的主音是 e），也不是导音，是第二级。

这个分工在整段引子里没有反转：钢琴的左手一直保持每小节八个八分音符的流动（m.5 起变成十六分音符的短促音型），右手守在 b′ 附近；大提琴负责长音与邻音（m.5 的 d♯′–e′、m.6 的 g♯′ 回到 e′）。两件乐器不是一问一答，是"一件在动、一件在量"。

力度也分工：m.1 钢琴标 *p*；m.6 两件乐器同时 *cresc.*——这是引子里唯一一次两个声部朝同一个方向走；m.7 钢琴标 *p dolce*，大提琴标 *p*。到 m.7–8 为止，引子的力度一直在 *p* 这个平面上，没有一次到 *f*。

## 三、接缝：两个延长记号，一个半音

引子的最后不是小节，是一段散板：记谱上不带小节线，长度由演奏者定。大提琴从这里开始独奏：f♯′ 上一个延长记号，标 *ad libitum*；然后 f♯′–e′–d′–c♯′–b–b♯，最后落在 **b♯** 上，第二个延长记号。

同一时刻钢琴做什么？它在散板里只有一件事：把 E 七和弦（e–g♯–b–d，从 e₂ 一直铺到 d′）连击两次，第二次之后是一个带延长记号的休止。此后到快板第一拍，钢琴一个音也没有再出。

所以接缝的实况是：

- 钢琴给出属七和弦 E7，然后停住等；
- 大提琴在属七上面把旋律走到 b♯，也停住等；
- 两个延长记号之后，快板第一拍，两件乐器同时动。

```lilypond title="贝多芬 Op.69 第三乐章" location="引子末（散板）– Allegro vivace，快板 mm.1–6"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "one" {
      \set Staff.instrumentName = "Violoncello"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef tenor \key e \major \time 2/4
      \tempo "Adagio cantabile" 8 = 46
      \new Voice { \cadenzaOn
        fs'4^\fermata_\markup { \italic "ad libitum" } ~
        fs'8 e' d' cs' b4 bs4^\fermata
        \cadenzaOff }
      \bar "||"
      \key a \major \time 2/2
      \tempo "Allegro vivace" 4 = 164
      % 快板 m.1
      cs'4\pp( a gs b)
      % m.2
      a2. b8\staccato cs'\staccato
      % m.3
      e'8( d') cs'\staccato d'\staccato cs'( b) as\staccato b\staccato
      % m.4
      a!8( gs) fs\staccato gs\staccato e4 fs16( gs a b)
      % m.5
      cs'4_\markup { \italic "cresc." }( a gs b)
      % m.6
      a2. b8\staccato cs'\staccato
    }
    \new Staff = "two" {
      \set Staff.instrumentName = "Pianoforte"
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key e \major \time 2/4
      \new Voice { \cadenzaOn <e gs b d'>8 s4 s8 r8 s8 r4^\fermata s4 \cadenzaOff }
      \bar "||"
      \key a \major \time 2/2
      % m.1
      <e a cs'>8 <e a cs'> <e a cs'> <e a cs'> <e b d'> <e b d'> <e gs d'> <e gs d'>
      % m.2
      <e a cs'>4 r r2
      % m.3
      <fs b d'>8 <fs b d'> <fs b d'> <fs b d'> <fs b d'> <fs b d'> <fs b d'> <fs b d'>
      % m.4
      <e b d'>4 r r2
      % m.5
      <e a cs'>8_\markup { \italic "cresc." } <e a cs'> <e a cs'> <e a cs'> <e b d'> <e b d'> <e gs d'> <e gs d'>
      % m.6
      <e a cs'>8 <e a cs'> <e a cs'> <e a cs'> <e a cs'> <e a cs'> <e a cs'> <e a cs'>
    }
    \new Staff = "three" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key e \major \time 2/4
      \new Voice { \cadenzaOn <e, gs, b, d>8 s4 s8 r8 s8 r4^\fermata s4 \cadenzaOff }
      \bar "||"
      \key a \major \time 2/2
      % m.1
      a,,8\pp a,, a,, a,, a,, a,, a,, a,,
      % m.2
      a,,4 r r2
      % m.3
      d,8 d, d, d, d, d, d, d,
      % m.4
      e,4 r r2
      % m.5
      a,,8 a,, a,, a,, a,, a,, a,, a,,
      % m.6
      a,,8 a,, gs,, gs,, a,, a,, g,, g,,
    }
  >>
  \layout { }
  \midi { }
}
```

和声上这是一次标准的属到主：E7 里的 g♯ 上行半音到 a，d 下行半音到 c♯，e 留着不动，正好凑成 A 大三和弦（a–c♯–e）。快板第一拍钢琴敲的就是 e–a–c♯——A 大三和弦的第二转位。

但真正把两段缝起来的是大提琴自己的半音。它在散板里停在 **b♯**（实音 c），这是 c♯ 的下邻音；快板第一拍它落在 **c♯′**。b♯→c♯，一个半音，弦乐器自己把话接上，不需要钢琴给提示。

力度在这里做了一个反向：引子的最后一片是 *p*，快板第一拍标 *pp*。转折点不是"打断"，是"接走"——快板比引子更轻。

## 四、快板不吃材料，只吃调性

快板的主题从 c♯′ 进来：c♯′–a–g♯–b，四个四分音符，*pp*，接着 a 延续三个四分音符，再 b–c♯′。这条旋律和引子里大提琴那条 f♯′–e′–a′–g♯′ 起头的线没有共同的音型：一个是二度下行，一个是三度下行接上行。

引子的材料在快板里一次也没有回来。全曲只有一处散板、一处 Adagio 速度标记；乐章最后停在 A 大三和弦上（钢琴 a–c♯–e–a），没有把引子搬回来收尾。

真正被吃掉的是引子的两样东西。

第一样是**调性**。引子是 E 大调，E 是 A 的属；引子把属调唱了十七小节，快板一开口就把它兑现成 A 大调。引子的调性没有消失，它是被兑现掉了。

第二样是**和声姿态**。引子末那个 E7 并没有走远——快板第 1 小节的后半，钢琴的八分音符从 e–a–c♯ 换成 e–b–d 再换成 e–g♯–d，最后这一组就是 e–g♯–d，E7 去掉五音。同一个和弦在引子里是悬置的（延长记号、散板、不许解决），在快板里只是第 1 小节后半的一闪。**同一个和弦，一次是悬念，一次是过门。**

所以"慢引子被快板吃掉"的准确含义是：快板吃掉引子的时间（十七小节的行进压成一小节里的三次换和弦）、吃掉引子的调性（属变成主），但不吃引子的主题。主题留在引子里，不回收。

## 五、贝多芬手里的三种接法

同样是慢引子接快板，功能可以完全不同。三种写法各有各的代价。

**一、属准备型。** 引子不提供主题材料，只提供属和弦与悬念；快板另起主题。Op.69 第三乐章就是这种。代价是引子不能太长，否则听者会期待它被回收；收益是快板可以立刻用最轻的力度起，不必与前段较劲。

**二、回收型。** 引子的主题在乐章后部原样或变形回来，引子变成一个"可以回收的地址"。Op.13 第一乐章的 Grave 在展开部里回来、在结尾之前又回来一次。代价是快板必须有足够长的后半段来安置这次回收，篇幅压不下来。

**三、姿态型。** 引子短到只是一个开场姿态，不提供材料也不回收，快板直接另起炉灶。Op.78 第一乐章的四小节 Adagio 就是这种：它的分量来自"短"，而不是来自"回"。

三种写法的分界不在长度，在**引子给出的是什么**：给和声（属准备型）、给材料（回收型），还是只给一个姿态（姿态型）。Op.69 属于第一种，而且是其中最干净的一例：引子的最后一个音（b♯）与快板的第一个音（c♯′）之间只隔一个半音，其余的交接全部由属七和弦完成。

## 六、可迁移的写法

第一，先决定引子给什么。给和声，就不要在快板里回收主题——两套逻辑会打架：听者刚被延长记号悬住，又被一个熟悉的主题接走，悬念就白做了。

第二，接缝的音要算到半音。Op.69 用两个延长记号把"停"放在属七上，把"接"放在下邻音到主音的半音上；停与接不在同一件乐器上，而在同一个和声里。写的时候先定属和弦，再定旋律停在属和弦的哪个音上——停在导音（g♯）会太急，停在下邻音（b♯）才留得住。

第三，力度反向。慢引子 *p*、快板 *pp*，转折才是"接走"；慢引子 *p*、快板 *f*，转折就是"打断"。后者更常见，但前者能让快板的主题一开口就带着耳语感，后面还有 cresc. 的余地。

第四，谁先动要安排好。引子里可以让钢琴先动、旋律乐器等一小节（Op.69 的 m.1 只有钢琴）；接缝处反过来——旋律乐器说最后一句，钢琴按住和弦等。这样两件乐器在转折处各有一次"独自在场"的机会。

第五，长度按句算，不按小节凑。Op.69 的引子最后接一段散板，散板不占小节，所以小节数不必是整数。写的时候先把短句排好，剩下的交给散板与延长记号。
