# 第二遍不能只是再说一遍：Op.37 的双呈示部改了什么

双呈示部常被讲成"乐队先弹一遍，独奏再弹一遍"。照字面做，第二遍就是浪费三分钟。Op.37 第一乐章的乐队呈示部有 111 小节，钢琴在这三分多钟里一个音都不出；它一旦开口，就必须让听者听见"这一遍和上一遍不一样"。它改的是四件事：前面加了两小节音阶、主题升了八度并加倍、乐队的答句被删掉、结尾的调换了。

## 一、两遍的长度与分界

乐队呈示部是 mm.1–111，111 小节。最后一小节（m.111）只有一件事：全奏在 C 上停住，标延长记号——小提琴 I 是 c′ 二分音符加延长记号，后半小节休止。

独奏呈示部从 m.112 起，到 m.248，137 小节。其中 mm.227–248 这二十二小节是乐队收尾，钢琴整段休止。所以两遍的长度是 111 比 137，第二遍长二十六小节。

分界落在 m.111 与 m.112 之间，而且是硬分界：m.111 的延长记号之后，第 112 小节的强拍就是钢琴的第一拍。

按 ♩=132 算，111 小节是三分二十二秒。这是双呈示部最贵的一笔账——独奏在三分半钟里不出声。

## 二、乐队第一遍建立了什么

```lilypond title="贝多芬 Op.37 第一乐章" location="Allegro con brio，mm.1–8"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "v1" {
      \set Staff.instrumentName = "Violino I"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 4/4
      \tempo "Allegro con brio" 4 = 132
      % m.1
      c'2\p ef'
      % m.2
      g'4. f'8\staccato ef'4\staccato d'\staccato
      % m.3
      c'4\staccato r8 g\staccato c'4\staccato r8 g\staccato
      % m.4
      c'4 r4 r2
      % m.5–8
      R1*4
    }
    \new Staff = "ob" {
      \set Staff.instrumentName = "Oboi"
      \set Staff.midiInstrument = "oboe"
      % GM 68
      \clef treble \key c \minor \time 4/4
      % m.1–4
      R1*4
      % m.5
      << { d''2\p f'' } \\ { r2 b'\p } >>
      % m.6
      <b' af''>4.\sf <c'' g''>8\staccato <b' f''>4\staccato <c'' ef''>\staccato
      % m.7
      <b' d''>4\staccato r8 <c'' ef''>8\staccato <b' d''>4\staccato r8 <c'' ef''>8\staccato
      % m.8
      <b' d''>4\staccato r4 r2
    }
    \new Staff = "fg" {
      \set Staff.instrumentName = "Fagotti"
      \set Staff.midiInstrument = "bassoon"
      % GM 70
      \clef bass \key c \minor \time 4/4
      % m.1–4
      R1*4
      % m.5
      <g b>2\p <g d'>
      % m.6
      <g f'>4.\sf <g ef'>8\staccato <g d'>4\staccato <g c'>\staccato
      % m.7
      << { g'4\staccato g'8\rest fs'\staccato g'4\staccato g'8\rest fs'\staccato g'4\staccato }
         \\ { g4 r g r g } >>
      % m.8
      r4 r2
    }
    \new Staff = "co" {
      \set Staff.instrumentName = "Corni in E-flat"
      \set Staff.midiInstrument = "french horn"
      % GM 60
      \transposition ef
      \clef treble \key c \major \time 4/4
      % m.1–4
      R1*4
      % m.5
      <e' e''>2\p <e' e''>
      % m.6
      <e' e''>4.\sf <e' e''>8\staccato <e' e''>4\staccato <e' e''>\staccato
      % m.7
      <e' e''>4\staccato r <e' e''>\staccato r
      % m.8
      <e' e''>\staccato r4 r2
    }
    \new Staff = "bs" {
      \set Staff.instrumentName = "Bassi"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass \key c \minor \time 4/4
      % m.1
      c2\p ef
      % m.2
      g4. f8\staccato ef4\staccato d\staccato
      % m.3
      c4\staccato r8 g,\staccato c4\staccato r8 g,\staccato
      % m.4
      c4 r4 r2
      % m.5–8
      R1*4
    }
  >>
  \layout { }
  \midi { }
}
```

主题一在 mm.1–4，只由弦乐奏：c′ 二分音符接 e♭′（上行小三度），然后 g′ 附点四分音符下行经 f′、e♭′ 到 d′，再是敲击式的 c′–g–c′–g，最后 c′ 收住。低音声部把同一条线低八度重述一遍（c–e♭、g–f–e♭–d、c–g–c–g），所以这四小节是**一条单线的齐奏**，没有和弦，没有分层。

mm.5–8 弦乐停住，木管与圆号接：双簧管把同一条轮廓**提高一级**（d″–f″，下面挂 b′，m.6 起是 b′–a♭″、c″–g″ 这样的两音和弦），大管落在 G 上（g–b、g–d′），圆号（in E♭ 记谱，实奏 g）持续同一个音。

所以乐队的第一遍把话说得很干净：四小节齐奏主题、四小节移级答句。八小节之后主题已经完整成立，后面的九十几小节都在这个基础上铺开——m.9 起小提琴 I 换到高音区，g″ 上停一个二分音符，再接回音式下行（g″–f″–e♭″，m.10 落到 d″–c″），这是主题的延续而不是新主题。乐队的这一遍靠“主题、答句、延续”三段把 111 小节撑起来，全程没有独奏参与。

## 三、独奏第一遍改了什么

```lilypond title="贝多芬 Op.37 第一乐章" location="mm.110–118"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "v1" {
      \set Staff.instrumentName = "Violino I"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 4/4
      \tempo "Allegro con brio" 4 = 132
      \set Score.currentBarNumber = #110
      % m.110：乐队最后一次敲主音
      c'4\staccato\ff r c'\staccato r
      % m.111：延长记号，乐队停住
      c'2^\fermata r2
      % m.112–118：弦乐休止，钢琴独奏
      R1*7
    }
    \new Staff = "p+rh" {
      \set Staff.instrumentName = "Pianoforte"
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key c \minor \time 4/4
      % m.110–111
      R1
      r2^\fermata s2
      % m.112
      c'4\sf\staccato r4 r16 c'( d' ef' f' g' a' b')
      % m.113
      c''4\sf\staccato r4 r16 c''( d'' ef'' f'' g'' a'' b'')
      % m.114
      <c'' c'''>2\f <ef'' ef'''>
      % m.115
      <g'' g'''>4.\sf <f'' f'''>8\staccato <ef'' ef'''>4\staccato <d'' d'''>\staccato
      % m.116
      <c'' c'''>4\staccato r8 <g' g''>8\staccato <c'' c'''>4\staccato r8 <g' g''>8\staccato
      % m.117
      <c'' c'''>4 r4 r2
      % m.118
      << { <b' d''>2 <d'' f''> } \\ { g'2\p g' } >>
    }
    \new Staff = "p-lh" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key c \minor \time 4/4
      % m.110
      R1
      % m.111：延长记号的空隙里，左手先奏上行的音阶
      r2^\fermata << { c16\rest^\f c( d ef f g a b) }
                     \\ { c,16\rest c,( d, ef, f, g, a, b,) } >>
      % m.112
      c4\sf\staccato r4 r16 c( d ef f g a b)
      % m.113
      c'4\sf\staccato r4 r16 c( d ef f g a b)
      % m.114
      <c c'>2\f <ef ef'>
      % m.115
      <g g'>4.\sf <f f'>8\staccato <ef ef'>4\staccato <d d'>\staccato
      % m.116
      <c c'>4\staccato r8 <g, g>8\staccato <c c'>4\staccato r8 <g, g>8\staccato
      % m.117
      <c c'>4 r4 r2
      % m.118
      <g b d'>2\p <g d' f'>
    }
  >>
  \layout { }
  \midi { }
}
```

**第一件改动：钢琴的第一个音提前到了延长记号的空隙里。** m.110 乐队最后一次敲 C（fortissimo，两次），m.111 全奏停在 C 上标延长记号。钢琴右手在 m.111 是空的，左手却不空——在延长记号的后半小节，左手奏一条上行音阶 c–d–e♭–f–g–a–b（十六分音符），从低八度一直铺到高八度。乐队的句号还没收干净，独奏已经把下一句的起拍塞进来了。

**第二件改动：加了两小节引子。** m.112 右手是 c′ 上的 sforzando 加同一条音阶（到 b′），m.113 整体提高八度再来一遍（c″ 加音阶到 b″）。这两小节在乐队的第一遍里完全不存在——主题一的第一句就是 c′–e♭′，没有前置。

**第三件改动：主题升八度并加倍。** m.114 起才是主题一：c″+c‴ 同时响，e♭″+e♭‴ 同时响；m.115 是 g″+g‴ 附点四分音符下行到 f″、e♭″、d″；m.116 的敲击 c″–g′ 也各加一个八度。乐队的第一遍是一条单线（c′–e♭′），这一遍是**两个八度同时响**。

**第四件改动：乐队的答句被删掉了。** 第一遍的 mm.5–8 是木管与圆号的移级答句；第二遍到 m.117 为止主题一就结束了，紧接着 m.118 起钢琴换成自己的句子（<b′ d″> 二分音符接 <d″ f″>，后面跟颤音），木管的答句整段没有出现。

四件事合起来：**加（引子）、升（八度）、删（答句）、换（后面接什么）**。第二遍没有新主题，但每一处都有新信息。

## 四、从"合奏块"到"独奏加伴奏"

乐队的第一遍是块状的：一条线由全组弦乐齐奏（m.1 起），换了音色也是整组换（m.5 起木管与圆号整组接）。第二遍不是。

主题一说完之后，钢琴继续走了四小节自己的句子（mm.118–121）。到 m.122 弦乐才进来，而且进来以后不奏主题：小提琴 I 持 e♭′ 全音符，然后用脉动重复（e♭′–e♭′–e♭′–e♭′），m.124 起换成 a♭′ 的长音与脉动；钢琴在高处奏旋律（g″ 长音，接 g″–f♯″–g″–a♭″–g″–f″–e♭″ 的回音式加花）。

这就是"合奏块"被改写成"独奏加伴奏"的具体做法：**乐队从"齐奏一条线"退成"长音加脉动"**，把旋律的位置整个让出来。齐奏的时候，乐队说的是"这条线是这样"；长音加脉动的时候，乐队说的是"这条线在什么和声上"。

## 五、与 Op.61 差在哪

Op.61 的独奏第一次进来时给的是**新主题**，和乐队的主题没有关系；Op.37 的独奏给的是**乐队主题本身**，只是换了八度、加了倍、前面挂了两小节音阶。同样是双呈示部，Op.61 用新材料区分两遍，Op.37 用新织体区分两遍：前者把第二遍变成一个新的开始，后者把第二遍变成对第一遍的一次重读。

## 六、双呈示部的用处与代价

用处是**独奏不必自我介绍**。主题已经由乐队立好，独奏一开口就是在改写已知的东西，听者听的是差异——八度、加倍、伴奏的分层——而不是又一段陌生材料。这也解释了为什么 Op.37 的第二遍能比第一遍长二十六小节却仍然没有新主题：它把长度花在"改写"上，不花在"新材料"上。

代价是**时间和风险**。111 小节、三分二十二秒，钢琴一个音不出；如果第二遍只是重复，这三分半就是白花的。所以第二遍必须有一张改动清单，而且清单上不能只有一项。Op.37 的清单是四项：加引子、升八度、删答句、换结尾。

结尾的换法值得单独说。乐队的第一遍以主音 C 上的延长记号收住（m.111），完全闭合；独奏这一遍结束时（mm.232–248）离开 C 与 E♭，落到 D–F♯–A 上，不回主音。第一遍可以闭合，因为它要给独奏留一个"接下去"的口子；第二遍不能闭合，因为它要把听者推进展开部。

## 七、可迁移的写法

第一，先把第一遍写成"完整但单色"的。Op.37 的主题一只有弦乐、只有一条线、只有一个调（mm.1–4）；单色不是简陋，是给第二遍留出改写的余地。

第二，第二遍的改动列成清单，四项里至少做三项：加（前置引子）、升（八度或音区）、删（第一遍里的某一段整段不出现）、换（结尾的调或和声走向）。只做"升八度"一项，听者会觉得只是换了个音区。

第三，让独奏在"上一段的空隙"里进来，而不是在强拍上等。Op.37 的左手音阶起于 m.111 的后半——延长记号还没完，新的起拍已经在了。

第四，主题一进来之后，乐队必须降级。齐奏、答句、整组换音色，都是第一遍的做法；第二遍里乐队要做的是长音、脉动、分解，把旋律让出来（m.122 起）。

第五，第二遍的结尾不要闭合。第一遍可以停在主音的延长记号上（m.111），第二遍要往远处走（D–F♯–A），因为它的下一站是展开部，不是终点。
