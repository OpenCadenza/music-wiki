# 四小节之内：开头怎样交代调性、音区与性格

开头不是"气氛"，是一张预算表。四小节之内有四个变量必须同时定下来：主调用哪几个音级亮相、第一个强拍（downbeat）落在和弦的哪个音上、两只手各占哪一层音区、第一处力度落差留到第几拍。这四个变量互相牵制——把主音推给第一个强拍，琶音就必须从别的音起；让左手空一整小节，音区就天然分成两层；把力度落差压进第一次触键，后面的四小节就没有第二档可用了。

Op.2 No.1 和 Op.13 给出两种相反的预算方案。前者用一条上行琶音把主和弦"数"出来，把力度落差推到第 5 小节；后者把落差压进第一个和弦的第一次触键，用三小节把同一手势搭成一道减七和弦的梯子。同样的四小节，两种算法。

还有第三种算法：把开口本身让给休止。Op.111 的 Maestoso 在第一个和弦之前先空出一段，让那个和弦从一个缝里挤进来——同一张预算表，换了一种花法，那是另一个题目。

## 五个音，第三个音才决定大小调

Op.2 No.1 第一乐章（f 小调，4/4）的开头不是和弦，是一条单声部琶音（arpeggio）。弱起（anacrusis）的一拍只有一个 c′，力度是 p，断奏（staccato）；随后第 1 小节是 f′–a♭′–c″–f″ 四个断奏四分音符，全在右手，左手整小节不发声。弱起那一拍不计入小节号。

把这五个音连起来看：c′–f′–a♭′–c″–f″。这是 f 小调主和弦从五音往上数的排列，五个音里 f 出现两次（f′、f″）、c 出现两次（c′、c″）、a♭ 只出现一次。真正决定信息量的是顺序——第一个音是五音 c′，不是主音；主音 f′ 迟半拍；"小调"这个信息要等第三个音 a♭′ 才落地。在 a♭′ 响起之前，c′–f′ 完全可以是 f 大调。

也就是说，这条琶音不是"陈述主和弦"，而是按 5–1–♭3–5–1 的顺序把和弦成员逐个点亮，让调式在第三个音上被确定。它同时办了两件事：把主音放在第一个强拍（第 1 小节第 1 拍落在 f′ 上），又把"大调还是小调"的悬念拖到第 3 拍。

## 第一个强拍落在主音上，左手故意不进

音区（register）的第一层也在第 1 小节定下：五个音跨 c′ 到 f″，一个十一度，全部落在高音谱表里，左手不参与。

这不是省略。第 1 小节如果左手垫一个 F，琶音的"空"就没有了；让低音缺席，第 2 小节左手的进入才成为一次真正的事件。第 2 小节左手在四分休止之后进来，给 f–a♭–c′ 三个断奏和弦，落在第 2、3、4 拍——它不抢第 1 拍，只在右手的空档里补三下。

这时两手的距离值得量一下：右手这一小节最低的音是 e″（回音里最后一个音的落点），左手最高是 c′，中间整整空出十六个半音，没有任何音落在这条带子里。右手因此听起来是"悬"的，左手只是回声。

第 3 小节把同一个琶音搬到属和弦上：g′–c″–e″–g″，即 C 大三和弦，右手仍是断奏四分音符。左手这一小节给的是 e–g–b♭–c′。注意那个 b♭：右手的 C–E–G 加上它，合起来是 C 属七和弦，也就是 f 小调的属。同一个形状、同一种节奏，调性功能从主翻到属，只用了左手一个音。

四小节的结构因此是两组两小节：第 1–2 小节是问句（主和弦琶音 + 收束），第 3–4 小节是答句（属和弦琶音 + 收束）。收束的公式固定：附点四分音符、用三连音写出来的回音（turn）、一个断奏四分音符、四分休止。第 1–2 小节的收束落在 a♭″，第 3–4 小节落在 b♭″。

## 第 5 小节的 sf，第 7 小节的唯一和弦

前四小节的力度（dynamics）只有一档 p。第一次力度事件出现在第 5 小节第 1 拍：一个倚音 c″ 把 a♭″ 顶进去，sf。第 6 小节同一位置再来一次，音高换成 b♭″。两次重音（sforzando）都落在强拍，用的都是"倚音顶上去 + 附点音重击"这同一个手段，连左手的和弦都跟着换（第 5 小节是 f–a♭–c′，第 6 小节是 g–b♭–e′）。

第一次整体的力度变化要等到第 7 小节：c″–f″–a♭″–c‴ 四音和弦，f 小调原位、顶上加八度，ff，带琶音记号，紧接着四个八分音符 b♭″–a♭″–g″–f″ 一路渐弱。这是前七小节里唯一一个右手和弦，前面全是单声部。

它同时改了音区：左手这一小节抬到 f′（第 2 拍 a♭–c′–f′），右手从 c″ 起，第 2 小节那道十六个半音的空档缩到七个半音，也就是一个五度。

第 8 小节是这套安排的收口：装饰音 e″–f″–g″ 顶到 f″，p，然后退半步到 e″（导音），断奏，延长记号，休止。开头不是靠更响结束的，是靠一个半音的下行加一次停顿结束。

```lilypond
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \clef treble
      \key f \minor
      \time 4/4
      \override Score.MetronomeMark.transparent = ##t
      \tempo 4 = 190
      \partial 4 c'4\p\staccato^\markup { \large \bold "Allegro" }_"弱起只有一拍"
      f'\staccato^"第一个强拍落在主音" af'\staccato c''\staccato f''\staccato
      af''4.( \tuplet 3/2 { g''16[ f'' e''] } f''4\staccato) r4
      g'\staccato^"同一个琶音换到属和弦" c''\staccato e''\staccato g''\staccato
      bf''4.( \tuplet 3/2 { af''16[ g'' f''] } g''4\staccato) r4
      \acciaccatura c''16 af''4.\sf^"第一个 sf" ( \tuplet 3/2 { g''16[ f'' e''] } f''4\staccato) r4
      \acciaccatura c''16 bf''4.\sf ( \tuplet 3/2 { af''16[ g'' f''] } g''4\staccato) r4
      <c'' f'' af'' c'''>2\ff^"这里才出现和弦"\arpeggio\> bf''8([ af'' g'' f''\!])
      \grace { e''16[ f'' g''] } f''4\p^"退回半音" ( e''\staccato) r4^\fermata r4
      R1
      R1
    }
    \new Staff = "down" {
      \clef bass
      \key f \minor
      \time 4/4
      \partial 4 r4
      R1
      r4 <f af c'>4\staccato <f af c'>\staccato <f af c'>\staccato
      <e g bf c'>4\staccato r4 r2 r4 <e g bf c'>\staccato <e g bf c'>\staccato <e g bf c'>\staccato
      r4 <f af c'>\staccato <f af c'>\staccato <f af c'>\staccato
      r <g bf e'>\staccato <g bf e'>\staccato <g bf e'>\staccato
      r4 <af c' f'>\staccato r <bf df' g'>\staccato
      r4 <c' g'>4\staccato r4^\fermata g,4\staccato^\p
      c\staccato^"右手空两小节" ef!\staccato g\staccato c'\staccato
      ef'!4.( \tuplet 3/2 { d'16[ c' b] } c'4\staccato) c'4\staccato
    }
  >>
  \layout { }
  \midi { }
}
```

## 第 8 小节的半步，第 9 小节的换手

第 9、10 两小节右手整小节不发声。左手独自继续：第 9 小节 c–e♭–g–c′（主和弦琶音，p），第 10 小节 e♭′ 附点四分音符、回音 d′–c′–b、c′–c′。

两件事需要记下来。第一，旋律搬到左手，音区掉了一个八度以上，力度回到 p——这是全曲第一次由另一只手说话。第二，左手弹的还是琶音，和开头那条同一种句法，只是从右手的高音区搬到了中音区。

所以开头四小节真正立起来的东西不是"主题"，是一种说话方式：主和弦可以拆成琶音说，也可以交给另一只手说。

## 慢引子：把落差放进第一次触键

Op.13 第一乐章的 Grave 走相反的路：落差不在第 5 小节，而在第一个和弦的第一次触键上。

第 1 小节第 1 拍，右手 c′–g–e♭，左手在低八度上叠同一个和弦，最低音落到 C2，标记 fp：强起，立刻收回。全小节最高的音只到 D4——中央 C 上方一个全音。整个第 1 小节没有一个音进入高音区。

和弦不是被"保持"，而是被拆开：第 2 拍它分裂成三组十六分音符（c–g–e♭、d–b–g、e♭–c–g），第 3 拍换成减三和弦 a–c–e♭，第 4 拍只剩 b–d 两个音，然后休止。音区在同一小节里靠十六分音符铺开，不靠旋律。

第 2 小节把同一手势整个上移半音：b–d–f–a♭，导音上的减七和弦（diminished seventh），同样 fp、同样拆成十六分音符。第 3 小节再上移：f♯–a–c–e♭，升四度上的减七和弦。

三小节连起来是一条梯子：主和弦，导音减七，升四度减七。性格不是靠某个动机的表情定下来的，是靠这道梯子的材质——每一级都是减七和弦，每一级都在同一个位置被 fp 咬一口。

力度落差的分工也不一样。第一个 sf 在第 3 小节，第一个 ff 在第 5 小节（低音区的 f–b–a♭–f 四个音），第 8 小节出现 sfp。Op.13 在前八小节用完了 fp、sf、ff、sfp 四档，而 Op.2 No.1 前四小节只有一档 p。

第 10 小节收在延长记号上：右手是一串十六分、六十四分、一百二十八分音符的下行跑句，停在 a♭′ 与 b 上；左手 G–C–E♭ 加延长记号，标着"紧接快板，不停顿"。

```lilypond
\version "2.26.0"
\language "english"

graveRH = \relative c' {
  \clef treble \key c \minor \time 4/4
  <c g ef>4^\markup {\large "Grave"}^"fp：强起，立刻收回"
    ~ <c g ef>16.[ <c g>32 <d b g>16. <ef c g>32]
    <ef c a>4( <d b>8) r
  <f d b>4\fp^"上移半音：导音减七" ~ <f d b>16.[ <f d b>32 <g d b>16. <af d, b>32]
    <af d, b>4( <g ef c>8) r

  <c a fs>4 \fp^"再上移：升四度减七" ~ <c a fs>16.[ <c a fs>32 <d a fs>16. <ef a, fs>32]
    <ef a, fs>4( \sf <d g, d>16[)-. r32 <c a fs>32 <d a fs>16. <ef a, fs>32]
  <ef a, fs>4( \sf <d g, d>8[ \p <e c g>8_\markup {\italic "cresc."}]
    <f c af>[)-. af] \sf ~
    \override Slur.positions = #'(5 . 5)
    af32[( g64 af bf af g f] ef[ d c bf] \tuplet 9/8 { af128[ g f ef d f af f d]}

   ef8)-. \p <ef' ef,>8 ~ <ef ef,>16.[ <ef ef,>32 <f f,>16. <g g,>32]
    \revert Slur.positions
    <g g,>8[( <f f,>16)] r32 \clef bass f, \ff^"第一个 ff"
    <f b, af f>16.[ <f b, af f>32 <f c af f>16. <f c af f>32]
  <f d af f>8 \clef treble <f' f,>8 ~ <f f,>16.[ <f f,>32 <g g,>16. <af af,>32]
    <af af,>8[( <g g,>16)] r32 <g, e cs g>32 \ff <a e cs a>16.[ <a e cs a>32
    <bf e, cs bf>16. <bf e, cs bf>32]

  <a fs d a>8 <a' a,!>8 ~ <a a,>16.[ <a a,>32 <b b,>16. <c c,>32]
    <c c,>8[( <b b,>16)] r r8 <b b,>16.[ <c c,>32]
  <cs cs,>8[(_\markup {\italic "cresc."} <d d,>)] r <d d,>16.[ <ef ef,>32]
    <e e,>8( <f f,>4) <f f,>8

  <f f,>8 \sfp ~ <f f,>32[ ef!64 d f ef d c!]
     b16[-.( b-. <b f>-. <b f>)-.] <c ef,>8 r r4

    c8[ \p ~ c32 b64( c] \tuplet 6/4 { d[ c bf af g bf)]} af16[-.( af-. af-. af)-.]
    g16[( ef')] ~ \tuplet 6/4{ ef64[ d df c b bf]} \tuplet 7/8{ a128[ af g fs f e ef]}
    d[( df c b bf a af g fs f e ef d df c b)] af'16.[^\fermata b,32]
}

graveLH = \relative c {
  \clef bass \key c \minor \time 4/4
  <c g ef c>4 ~ <c g ef c>16.[ ef32 d16. c32] fs4( g8) r16. af,!32 |
  af'4 ~ af16.[ af32 g16. f!32] ef4 ~ ef8 r16. ef32-. |

  ef'4 ~ ef16.[ ef32 d16. c32] c4( b16)[-. r32 ef32 d16. c32]
  c4( b8 <bf c e> <af c f!>)-. r <bf, bf,>4^\sf

  <ef ef,>16 <ef g bf>[ <ef g bf> <ef g bf>] <ef g bf>[ <ef g bf> <ef g bf> <ef g bf>]
    <ef af c>[ <ef af c> <ef af c> <ef af c>] <d d,>[ <d d,> <c c,> <c c,>]
  <b b,> <b d f af>[^\p <b d f af> <b d f af>] <bf d f af>[ <bf d f af> <bf d f af> <bf d f af>]
    <bf cs e g>[ <bf cs e g> <bf cs e g> <bf cs e g>] <a a,>[ <a a,> <g g,> <g g,>]

  <fs fs,> <d'' a fs>[^\p <d a fs> <d a fs>] <d a fs>[ <d a fs> <d a fs> <d a fs>]
    <d af f>[ <d af f> <d af f> <d af f>] <b f d>[ <b f d> <b f d> <b f d>]
  <af d, b>[ <af d, b> <af d, b> <af d, b>] <f b, af>[ <f b, af> <f b, af> <f b, af>]
    <f b, g>[ <f b, g> <f b, g> <f b, g>] <f c af>[ <f c af> <f c af> <f c af>]

  <f b, g>8-. r r \clef treble <g' d'>16[(-. <g d'>)-.]
    <af c>8 r r4 \clef bass
  r4 r8 <f, c' d>16[(-. <f c' d>)-.]
    <g c ef>8 r <f d g,>8*1/2 s16_ \markup {\italic "紧接快板，不停顿"} r8^\fermata
}

\score {
  \new PianoStaff <<
    \new Staff = "up" { \graveRH }
    \new Staff = "down" { \graveLH }
  >>
  \layout { }
  \midi { }
}
```

## 同一材料，第二次出场

Op.13 的快板主题在第 11 小节进入，第一拍就把引子建立的材质接了过去：左手 C2 与 C3 交替的八分音符脉冲，右手 c′ 持三拍，第 4 拍落 E–B♭ 的三全音。引子用减七和弦建立起来的"低音区 + 三全音"的性格，在这里换成了"三全音 + 律动"。

Op.2 No.1 的对照更干净。第 101 小节，同一条琶音原样回来：f′–a♭′–c″–f″ 四个断奏四分音符。变化全在左手——第 1 小节那里是整小节休止，第 101 小节左手给 f–a♭–c 并持满一拍；第 102 小节左手同样三个和弦，每个从八分音符延长到持满一拍。

音高一个没改，配重全改了。这就是开头四小节真正的用处：它给后面的每一次重复预设了一个"空"的基准，让第二次出场不需要新素材就成立。

## 两条可以带走的规则

一，先决定第一个强拍落在和弦的哪个音上。落在主音（Op.2 No.1 第 1 小节第 1 拍的 f′）是宣告；从五音起（弱起的 c′）是悬置。这个选择决定了后面四小节要不要"补上"主音。

二，把第一处力度落差放在一个能被记住的位置，而且只能放一次。Op.2 No.1 放在第 5 小节的强拍，用前面四小节的 p 把它养出来；Op.13 放在第 1 小节的第一次触键，让落差变成音色而不是事件。两种都成立，但不能两头都要——若第一小节已经 ff，第五小节的 sf 就没有对比对象了。
