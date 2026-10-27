# 一口气说完：序曲里没有第二乐章可以补救

序曲是单乐章体裁，舞台上只给一次机会：立调、出主题、转折、收束，全在同一口气里。没有第二乐章可以把没说清的话接着说，所以序曲的每一处结构都必须自己承重。Op.62《科里奥兰》把这件事做得极清楚：它把"立调"本身写成一个事件，让主和弦拖到第 13 小节才出现；把展开部压成"只剩节奏细胞"的调性游走；把全部结论押在最后三十九小节的尾声上。

```lilypond title="贝多芬 Op.62 序曲《科里奥兰》" location="Allegro con brio，mm.1–16"
\version "2.26.0"
\language "english"

#(set-global-staff-size 15)

\score {
  \new StaffGroup <<
    \new Staff = "flauti" {
      \set Staff.instrumentName = "Flauto I"
      \set Staff.midiInstrument = "flute"
      % GM 73
      \clef treble \key c \minor \time 4/4
      \tempo "Allegro con brio" 4 = 150
      \relative c {
        % m.1–2
        R1 *2
        % m.3
        c'''4-.\ff r r2
        % m.4–6
        R1 *3
        % m.7
        d4-. r r2
        % m.8–10
        R1 *3
        % m.11
        ef4-. r r2
        % m.12
        R1
        % m.13
        g4-. r r2
        % m.14
        b,4-. r r2
        % m.15–16
        R1*2
      }
    }
    \new Staff = "clarinetti" {
      \set Staff.instrumentName = "Clarinetto I in B"
      \set Staff.midiInstrument = "clarinet"
      % GM 71
      \transposition as
      \clef treble \key d \minor \time 4/4
      \relative c {
        R1 *2
        d''4-.\ff r r2
        R1 *3
        e4-. r r2
        R1 *3
        f4-. r r2
        R1
        f4-. r r2
        e4-. r r2
        R1*2
      }
    }
    \new Staff = "corni" {
      \set Staff.instrumentName = "Corno I in E-flat"
      \set Staff.midiInstrument = "french horn"
      % GM 60
      \transposition ds'
      \clef treble \key c \major \time 4/4
      \relative c {
        R1*2
        f''4-.\ff r r2
        R1*3
        f4-. r r2
        R1*3
        c4-. r r2
        R1
        e4-. r r2
        e4-. r r2
        R1*2
      }
    }
    \new Staff = "timpani" {
      \set Staff.instrumentName = "Timpani in C, G"
      \set Staff.midiInstrument = "timpani"
      % GM 47
      \clef bass \key c \minor \time 4/4
      \relative c {
        R1*2
        c4-.\ff r r2
        R1*3
        c4-. r r2
        R1*3
        c4-. r r2
        R1
        g4-. r r2
        g4-. r r2
        R1*2
      }
    }
    \new Staff = "violino1" {
      \set Staff.instrumentName = "Violino I"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 4/4
      \relative c {
        c'1\ff ~
        c
        <f c' af'>4-. r r2
        R1
        c1 ~
        c
        <d d' d'>4-. r r2
        R1
        c1 ~
        c
        <ef' ef'>4-. r r2
        R1
        <ef, c' g'>4-. r r2
        <g, d' b'>4-. r r2
        % m.15：主题进来
        c8[-.\p ef-.] ef[( d)] d[-. g-.] g4-"ten."
        c,8[-. ef-.] ef[( d)] d[-. g-.] g4-"ten."
      }
    }
    \new Staff = "violino2" {
      \set Staff.instrumentName = "Violino II"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 4/4
      \relative c {
        c'1\ff ~
        c
        <f c' af'>4-. r r2
        R1
        c1 ~
        c
        <d b' af'>4-. r r2
        R1
        c1 ~
        c
        <fs ef' c'>4-. r r2
        R1
        <g, ef' c'>4-. r r2
        <g d' b'>4-. r r2
        R1 *2
      }
    }
    \new Staff = "violoncello" {
      \set Staff.instrumentName = "Violoncello"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass \key c \minor \time 4/4
      \relative c {
        c1\ff ~
        c
        f,4-. r r2
        R1
        c'1 ~
        c
        f,4-. r r2
        R1
        c'1 ~
        c
        fs,4-. r r2
        R1
        g4-. r r2
        g4-. r r2
        c4\p r4 r2
        c4 r4 r2
      }
    }
    \new Staff = "contrabasso" {
      \set Staff.instrumentName = "Contrabasso"
      \set Staff.midiInstrument = "contrabass"
      % GM 43
      \transposition c
      \clef bass \key c \minor \time 4/4
      \relative c {
        c1\ff ~
        c
        f,4-. r r2
        R1
        c'1 ~
        c
        f,4-. r r2
        R1
        c'1 ~
        c
        fs,4-. r r2
        R1
        g4-. r r2
        g4-. r r2
        c4\p r4 r2
        c4 r4 r2
      }
    }
  >>
  \layout { indent = 2.4\cm }
  \midi { }
}
```

## 一、第一个和弦不是和弦

第 1 小节全奏的"和弦"里只有一个音高：c。小提琴 I 与 II 是 c′，大提琴 c，低音提琴记谱 c（实际低八度）。没有三度，没有五度。而且它不是一个和弦的瞬间，是两小节的连线——m.1 与 m.2 是同一个音，被连线绑在一起。

管乐、铜管、定音鼓在这两小节里全部空着：长笛、单簧管、圆号、定音鼓的第一个音都在第 3 小节。所以开头的两小节是纯弦乐的一个音，ff。

这不是主和弦，是主音。听者拿到的是音高位置，不是调式——c 究竟是大调还是小调、c 是不是主音，都还没有答案。

奏鸣曲可以反过来做：Op.90 第一乐章的弱起和弦在 m.1 就是 e 小三和弦的第一转位，一个完整的主和弦直接落地。奏鸣曲有整个乐章来解释这个和弦，序曲没有第二乐章，于是它把"解释"本身变成了开头。

## 二、调性在第 13 小节才成立

第 3 小节第一次击出带三度的和弦：f–a♭–c，f 小三和弦，下属。它的分布是——长笛 c‴，单簧管（in B）奏出的 c″，圆号（in E♭）奏出的 a♭″，小提琴 I 与 II 同奏 f′–c″–a♭″，大提琴 f，低音提琴 f。全组 ff，只有一个四分音符，m.4 空一小节。

m.5–6 又回到那个裸 c。第 7 小节第二次击：f–a♭–b–d，f 减七——三度仍是 a♭，但七音 b 把和弦拧成减七，小提琴 I 把 d 叠成三个八度。m.9–10 再次回到裸 c。第 11 小节第三次击：f♯–a–c–e♭，f♯ 减七，这一次连根音都不在 f 上，而是 f♯——指向 g 的半音下方。

第 13 小节才出现全曲第一个 c 小三和弦：c–e♭–g，低音是大提琴的 g。第 14 小节接 G 大三和弦：g–b–d。到这里，i–V 的功能关系第一次成立，c 才真正是"c 小调的主音"。

把数字排开看：第 1 到第 12 小节里没有一个 c 小三和弦；三次击出的和弦分别落在 f（两次）与 f♯（一次），每一次都带着 a♭、b、e♭ 这些"离开 c"的音。c 作为音高在第 1 小节就有，c 作为调性要到第 13–14 小节才成立。

与奏鸣曲比，这一步是"慢"的：奏鸣曲第 1 小节就摆出主和弦，Op.62 拖到第 13 小节。但时间账反过来——♩=150、4/4，第 1 至 14 小节只有 22.4 秒。22 秒里它做完了四件事：给出主音、击出三个非主和弦、成立 i–V、让主题开口。奏鸣曲在同样的 22 秒里通常只够把主部主题陈述一遍。

## 三、两个主题，六小节一句

主题在第 15 小节的小提琴 I 上进来，记号 p，与前面十四个小节的 ff 断然切开：c–e♭–e♭–d–d–g，全部八分音符，最后一个 g 标 *ten.*。这是一条下行的叹息，两小节一句，m.16 原样重复。

m.17 起换头：c–e♭–e♭–d，接 d–a♭–a♭–g；m.18 再换：g–c–c–b，接 b–f–f–e♭；m.19 渐强，m.20 以 f♯ 经过音收在 g 上，标 f。主题一的总长是 mm.15–20，六小节。m.21 空一小节——分句。

连接部不写新材料：m.22–27 把主题一搬到 b♭ 小调再说一遍，小提琴 I 是 b♭–d♭–d♭–c–c–f，比 m.15 低一个大二度。主题换了调，轮廓一个音没改。这就是序曲的连接部——它不是"过渡"，是把主题暂时放错地方。

m.50 是一小节 B♭ 大三和弦（f–b♭–d），标渐弱；m.51 只剩 d、b♭、a♭ 三个音，全曲最稀薄的一小节。主题二就从这片空隙里进来。

主题二在 m.52 出现，E♭ 大调，p：g–a♭–g–f–d–b♭，四分音符与二分音符连成一条下行的线，与主题一同样是"长音落下去"的轮廓，但把八分音符的锯齿换成了连线。主题二的加厚从 m.57 起：同一个音被反复击出， cresc. 一路推到 mm.61–63 的 ff。

主题的总数是两个，加一次主题一的调性变体（m.22）。没有第三主题——序曲没有时间让第三个主题成立。

## 四、展开部：只有细胞，没有主题

展开部没有被取消，但被抽干了内容。它从 m.96 开始：大提琴的半音下行八度——c、b、b♭、a♭、g、f♯、e♭、d，六小节走完，把调性甩在身后。

中段（mm.102–151）只剩主题的节奏细胞：四分音符接三个八分音符的那一下顿挫，旋律轮廓全部丢掉。这一段在 a♭、d♭、g♭/f♯、b 各级上打转，没有一次停在主调上。力度按四次涨落走：m.118 p、m.130 cresc.、m.136 回到 p、m.140 f、m.148 ff。

m.152–153 是一个 f 小三和弦（f–a♭–c）连按两小节，ff；m.154 一个 d♭ 的短击，m.155 空一小节；m.156–157 只剩一个 f——全乐队只有这一个音高。到这里，引子那个"裸主音"的手势才真正搬到了下属音上。序曲用这个手势当中介，等于告诉听者：调性还没回来。

主题在 m.158 回来，但先在 f 上：小提琴 I 是 f–a♭–a♭–g，接着 m.161 是 b–e♭–e♭–d–d–g。再现的第一次陈述落在下属调，主调的再现被推迟。

所以展开部的压缩不是删长度（它仍有六十来小节），而是删内容：只留节奏细胞，把"主题怎样在调性里行走"这件工作交给调性本身。

## 五、尾声：三十九小节，四道工序

尾声从 m.276 开始，标志是那个裸 c 原样回来：小提琴 I 是 `c1 ~ c`，两小节，ff——与 m.1–2 一模一样。

mm.276–283 把引子的前八小节原样重演：裸 c 两小节（m.276–277）、f 的短击（m.278）、空一小节（m.279）、裸 c 两小节（m.280–281）、同一个 d 的短击（m.282）、空一小节（m.283）。同一套句式，一节不差；到 m.284 的第三个裸 c 之后，句式才开始变。

mm.286 起短击加速：m.286 是 e♭+b，m.288 是 c+g，m.289 是 a♭+e——从四小节一击变成一小节一击。m.290 只剩单音（f 与 d），m.292 是 e♭ 的 p，m.294 的 d 加了 pizz.。

m.296 标 *arco* 与 *sempre più piano*，小提琴开始 c 与 b 的半音交替：m.297 与 m.299 各是两拍 c 接两拍 b（两次），之后 c 与 b 各自被按住两小节（mm.300–303）。最后十来小节只剩零散的碎片与一个 c：m.305 一个 e♭、m.306 一个 b–d–g、m.307 一个 a♭、m.309 一个 g；m.310 与 mm.312–314 只剩 c。全曲不是收在主和弦上，是收在一个还没有决定的 c 上——与第 1 小节那个裸 c 首尾相接。

尾声共三十九小节（mm.276–314），引子十四小节；尾声是引子的近三倍。它长，是因为它要一次做完四件事：把引子的手势搬回来（框架）、把短击加速（压力）、把和声拆成单音（解体）、让主音独自留下（结论）。奏鸣曲的尾声通常只做一件事——把已经成立的结论再确认一遍。

## 六、与 Op.84 差在哪

Op.84《埃格蒙特》也从一个裸主音开场：m.1 只有一个 f，同样不给三度。但它在 m.2 就补上 a♭–c–f，f 小三和弦在第 2 小节落地——比 Op.62 早了十一小节。

结尾正相反。Op.84 的最后十二小节转到 F 大调，用 F–A–C 与 e♮ 把整首曲子翻到亮面；Op.62 的最后三十九小节把小三度彻底拆掉，只剩 c 与 b 的半音。同样是一次说清一件事，Op.84 把"说清"放在结尾，Op.62 把"说清"放在开头：一个向上收，一个向下散。

## 七、可迁移的写法

第一，先决定调性什么时候成立。要做戏剧性的开场，就把主和弦往后推，用不带三度的主音占位——Op.62 用了十一小节，代价是这十一小节必须每一次都击出"离开主音"的和弦，否则占位就变成了空白。

第二，主题控制在两个。第三个主题在单乐章体裁里没有时间成立；如果材料不够，把第一个主题搬到错的调上再说一遍（m.22 的 b♭ 小调），比新写一个主题便宜。

第三，展开部可以短，但不能没有内容。留节奏细胞、丢掉旋律轮廓、让调性游走承重；力度至少要有两到三次涨落，否则游走会听成走神。

第四，尾声至少做两件事：把引子的手势搬回来，再把它拆掉。Op.62 做了四件（再现、加速、解体、留主音），所以它有三十九小节；只做"再现"的尾声，八小节就够了。

第五，单乐章里"慢"必须被压成一个姿态。Op.62 的十四小节引子里有六小节只按着一个 c（m.1–2、m.5–6、m.9–10），另有三小节全空（m.4、m.8、m.12），空本身就是它的重量；把慢写成一个段落，序曲就没有时间说正事了。
