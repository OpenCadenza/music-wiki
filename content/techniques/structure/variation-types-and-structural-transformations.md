---
title: 变奏曲式的类型
description: 剖析古典至晚期浪漫主义变奏曲式的三大核心结构类型：以莫扎特K.331为代表的装饰性变奏、以贝多芬Op.109为代表的性格与复调变奏，以及以Op.111阿里埃塔为代表的时值递减与比例时间变奏。
---

# 变奏曲式的类型

<p class="doc-subtitle">从莫扎特K.331的装饰性织体、贝多芬Op.109的性格复调裂变，到Op.111阿里埃塔的时值递减，变奏曲式如何在维持骨架统一的同时完成时间的重塑？</p>

在西方器乐曲式的演进史中，变奏曲式（Variation Form）始终占据着一种特殊的哲学地位。与奏鸣曲式那种基于调性冲突、危机爆发与辩证综合的“黑格尔式”戏剧冲突不同，变奏曲式建立在一种关于**“变与不变”**（Permanence and Flux）的原型思考之上：在漫长的音乐时空展开中，究竟是什么被绝对守恒，又是什么被允许自由裂变？

奏鸣曲式的展开部倾向于“离心式”的解构——将主题动机粉碎、调性急剧离心并激化矛盾；而变奏曲式则展现出一种深刻的“向心式”智慧：在始终保持母体身份认同（Identity）的前提下，挖掘材料潜藏的无限形态。从类型学维度审视，变奏曲式并非单一手法的机械重复，而是由三种截然不同的结构动力学机制所主导：
1. **装饰性变奏**（Ornamental / Figurative Variation）：以固定的和声骨架与低音走向为基石，通过表面音符细分与修饰音繁衍展现古典高雅修辞；
2. **性格与复调变奏**（Character / Contrapuntal Variation）：打破统一的情感面具，通过速度、节拍、演奏法与复调对位手法的颠覆性介入，使原主题分裂为截然不同的戏剧性格；
3. **时值递减与比例时间变奏**（Metric Diminution & Proportional Variation）：依托严密的数学比例阶梯对基础拍位进行持续细分，在保持恒定大拍脉搏的同时引发微观时间意识的先验跃迁。

本文通过对三部具有断代意义的经典文献——莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章、贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章，以及贝多芬《c小调第32钢琴奏鸣曲》Op. 111 第二乐章（阿里埃塔）的谱面细读，系统解构变奏曲式的这三大核心类型学范式。

---

## 一、装饰性变奏：骨架冻结与音型繁衍（莫扎特 K. 331 第一乐章）

在18世纪后半叶的高雅风格（*Style galant*）语境中，**装饰性变奏**（Ornamental / Figurative Variation，德语称 *Verzierungs-Variation*）是最具代表性的古典曲式典范。其核心法则在于：主题的调性、和声骨架、低音走向与小节长度被严格“冻结”，作曲家的创造力主要聚焦于旋律线条的修饰、辅助音的穿插以及表面节奏密度的梯级加密。

### 1. 主题的方整结构与西西里舞曲节律（mm. 1–18）
莫扎特 K. 331 第一乐章（Andante grazioso，6/8 拍，A 大调）以一段典型的高雅双规乐段为母体：
- **两段体骨架与句法划分**：主题包含两个反复段（mm. 1–8 与 mm. 9–18），前 8 小节构成严格的平行复乐段；
- **西西里摇曳风范**：附点八分音符加十六分音符的特征节奏（$C\sharp 5 \to D5 \to C\sharp 5 \to E5 \to E5$），赋予旋律优雅而轻盈的歌唱性；
- **声部导向与线性减缩（Schenkerian Skeleton）**：
  * 高音声部：以三音 $C\sharp 5$ 为起点，经由四音 $D5$ 跃升至五音 $E5$，随后在第 4 小节下行收拢于二音 $B4$（达成半终止 HC）；
  * 低音声部：以主音 $A2$ 起步，经由第一转位属和弦低音 $G\sharp 2$ 回归 $A2$，随后下行至下属音 $D3$ 与属音 $E2$，构成坚固的三和弦支柱；
- **前乐段的功能和声级数（mm. 1–8）**：
  $$\text{I} \to \text{V}^6_5 \to \text{I} \to \text{IV} \to \text{I}^6_4 \to \text{V} \quad (\text{mm. 1–4, 半终止})$$
  $$\text{I} \to \text{V}^6_5 \to \text{I} \to \text{IV} \to \text{I}^6_4 \to \text{V}^7 \to \text{I} \quad (\text{mm. 5–8, 完全正格终止})$$
- **对比中段与扩充再现（mm. 9–18）**：第 9–12 小节展开属音上的驻留（Standing on the dominant），右手以 $E4 \to D5 \to B4 \to G\sharp 4$ 展开轻微的小调阴影模进；第 13–18 小节在主调上再现原型，并在第 17–18 小节加入 2 小节扩充终止，彻底确立 A 大调调性引力。

```lilypond title="莫扎特 第11钢琴奏鸣曲 K.331 第一乐章" location="Thema: Andante grazioso，mm.1–8" id="mozart-k331-i-theme-mm1-8"
\version "2.26.0"
\language "english"

% 莫扎特 A 大调第 11 钢琴奏鸣曲 K.331 第一乐章主题 mm.1-8（6/8，A 大调）。
% 据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；
% 并用 DCML 莫扎特奏鸣曲音符表按小节做音高多重集回比对（mm.1-8 逐小节一致，
% m.8 底本含一处连线替代重复音，见 provenance 记录）。
% 试听速度 1/8=144 采自底本速度标记。

global = {
  \key a \major
  \time 6/8
  \tempo "Thema: Andante grazioso" 8 = 144
}

upper = {
  \global
  \clef treble
  \set Staff.midiInstrument = "acoustic grand"
  cs''8. d''16 cs''8 e''4 e''8 |
  b'8. cs''16 b'8 d''4 d''8 |
  a'4 a'8 b'4 b'8 |
  << { cs''4 e''16 d''16 cs''4 b'8 } \\ { e'4 b'8 a'4 gs'8 } >> |
  cs''8. d''16 cs''8 e''4 e''8 |
  b'8. cs''16 b'8 d''4 d''8 |
  a'4 b'8 cs''4 <fs' b' d''>8 |
  <e' a' cs''>4 <d' e' gs' b'>8 <cs' e' a'>4 r8 |
}

lower = {
  \global
  \clef bass
  \set Staff.midiInstrument = "acoustic grand"
  << { e'4 e'8 e'4 e'8 } \\ { a8. b16 a8 cs'4 cs'8 } >> |
  << { e'4 e'8 e'4 e'8 } \\ { gs8. a16 gs8 b4 b8 } >> |
  << { e'4 e'8 e'4 e'8 } \\ { fs4 fs8 gs4 gs8 } >> |
  a4 d8 e4. |
  << { e'4 e'8 e'4 e'8 } \\ { a8. b16 a8 cs'4 cs'8 } >> |
  << { e'4 e'8 e'4 e'8 } \\ { gs8. a16 gs8 b4 b8 } >> |
  << { e'4 e'8 e'4 s8 } \\ { fs4 gs8 a4 d8 } >> |
  e4 e,8 a,4 r8 |
}

\score {
  \new PianoStaff <<
    \new Staff { \set Staff.midiInstrument = "acoustic grand" \upper }
    \new Staff { \set Staff.midiInstrument = "acoustic grand" \lower }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

### 2. 第一变奏中的半音化浮雕与十六分音符音流（mm. 19–36 / 变奏 mm. 1–18）
进入第一变奏，莫扎特展现了装饰性变奏的最高技艺：
- **旋律骨架的精准保留**：原主题的骨干音（$C\sharp 5 \dots E5 \dots$）并未被抹除，而是被镶嵌于连续的十六分音符织体之中；
- **半音下辅助音与倚音修饰（mm. 19–22）**：在第 1 小节，右手以带升号的下辅助音切入（$B\sharp 4 \to C\sharp 5 \to B4 \to C\sharp 5$），随后跃升至 $D\sharp 5 \to E5 \to D5 \to E5$。这种连续的半音化辅助音犹如在原本平整的古典大理石雕塑上雕琢出繁复精致的洛可可浮雕；
- **声部织体的梯级加密（mm. 23–26）**：至前乐段后半程，十六分音符音流在右手展开连续的下行级进跑动，第 24 小节在完全正格终止前达到高密度的音型华彩；
- **双手音型对换与低音忠实度**：在随后的反复段中，十六分音符跑动迅速转移至左手内声部，而右手恢复清晰的旋律线条；左手低音与内声部和弦（$[A, E] \to [C, E] \to [G, E] \dots$）维持着与主题完全一致的击弦节拍与换和弦频率，确保听众始终能够在清晰的和声导航中辨识出母体形态。

```lilypond title="莫扎特 第11钢琴奏鸣曲 K.331 第一乐章" location="Variation I，mm.19–26" id="mozart-k331-i-var1-mm19-26"
\version "2.26.0"
\language "english"

% 莫扎特 K.331 第一乐章变奏一 mm.19-26（6/8，A 大调）。
% 据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；
% DCML 音符表按小节回比对 mm.19-26：6/8 小节全部一致，另两小节仅有装饰音写法差异。
% 底本 ABC 的 %%setbarnb 为 19，与刊本印刷号一致。

global = {
  \key a \major
  \time 6/8
  \tempo "Variation I" 8 = 144
}

upper = {
  \global
  \clef treble
  \set Staff.midiInstrument = "acoustic grand"
  bs'16 cs''16 r16 cs''16 bs'16 cs''16 ds''16 e''16 r16 e''16 fs''16 e''16 |
  e''16 b'16 r16 b'16 as'16 b'16 cs''16 d''16 r16 d''16 e''16 d''16 |
  d''16 a'16 r16 a'16 gs'16 a'16 as'16 b'16 r16 b'16 as'16 b'16 |
  bs'16 cs''16 bs'16 cs''16 e''16 d''16 cs''16 b'16 a'16 gs'16 fs'16 e'16 |
  <e' a' cs''>4 <b' d''>8 <bs' ds''>8 <cs'' e''>8 r16 <a' cs''>16 |
  << { <e' gs' b'>8\staccato <e' gs' b'>8\staccato <e' a' cs''>8\staccato <as' cs''>8 <b' d''>8 r16 <gs' b'>16 } \\ { s4. e'4 s8 } >> |
  a'8\staccato a'8\staccato b'16\trill a'32 b'32 cs''8\staccato cs''8\staccato <fs' b' d''>8 |
  <e' a' cs''>8 <e' a' cs''>8 <d' e' gs' b'>8 <cs' e' a'>8 r8 r8 |
}

lower = {
  \global
  \clef bass
  \set Staff.midiInstrument = "acoustic grand"
  r8 <a e'>8 r8 r8 <cs' e'>8 r8 |
  r8 <gs e'>8 r8 r8 <b e'>8 r8 |
  r8 <fs e'>8 r8 r8 <gs e'>8 r8 |
  <a e'>4 <d fs>8 <e gs>4 r8 |
  a,16 a16 a16 a16 a16 a16 a,16 a16 a16 a16 a16 a16 |
  e,16 e16 e16 e16 e16 e16 e,16 e16 e16 e16 e16 e16 |
  fs,16 fs16 fs16 fs16 gs,16 gs16 a,16 a16 a16 a16 d,16 d16 |
  e,16 e16 e16 e16 e,16 e16 a,,8 a,8 r8 |
}

\score {
  \new PianoStaff <<
    \new Staff { \set Staff.midiInstrument = "acoustic grand" \upper }
    \new Staff { \set Staff.midiInstrument = "acoustic grand" \lower }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

### 3. 古典装饰套曲的宏观色彩阻尼（第三变奏 Minore 的对比功能，mm. 55–72）
在古典装饰性变奏套曲中，单纯的音型加密极易引发听觉疲劳。为此，莫扎特引入了古典主义的标准阻尼设计——**同主音小调变奏**（*Minore*，mm. 55–72）：
- 在第三变奏中，音乐突转为 a 小调，原本明朗的高雅风范瞬间被一层阴郁的悲剧色彩笼罩；
- 织体由断奏与轻巧跳音转为连贯沉郁的十六分音符八度与半音阶滑行，和声节奏在减七和弦的辗转中被拉长；
- 低音线条以八度击弦强化低频重量，弱化了西西里舞曲原本轻盈的摇曳感，构建出严峻的内省空间；
- 这种局部调式色彩的暂时暗转，不仅避免了装饰性音型的机械平铺，更为主调大调（*Maggiore*）在第四、五变奏中的明亮回归蓄积了强大的结构反弹力。

```lilypond title="莫扎特 第11钢琴奏鸣曲 K.331 第一乐章" location="Variation III（Minore），mm.55–72" id="mozart-k331-i-var3-mm55-72"
\version "2.26.0"
\language "english"

% 莫扎特 K.331 第一乐章变奏三（小调变奏）mm.55-72（6/8，A 小调记谱无调号）。
% 据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；
% 该分谱（sonata11-1d.krn）缺少 %%setbarnb，按变奏二止于 m.54 推算本段自刊本 m.55 起；
% DCML 音符表 mn 55-72 回比对 16/18 小节音高多重集完全一致。

global = {
  \key c \major
  \time 6/8
  \tempo "Variation III" 8 = 144
}

upper = {
  \global
  \clef treble
  \set Staff.midiInstrument = "acoustic grand"
  c''16 b'16 a'16 b'16 c''16 d''16 e''16 ds''16 f''16 e''16 d''16 c''16 |
  b'16 a'16 gs'16 a'16 b'16 c''16 d''16 cs''16 e''16 d''16 c''16 b'16 |
  a'16 e''16 ds''16 e''16 c''16 a'16 gs'16 e''16 f''16 e''16 d''16 b'16 |
  b'16 a'16 gs'16 a'16 b'16 c''16 <a' c''>4 <gs' b'>8 |
  <c'' c'''>16 <b' b''>16 <a' a''>16 <b' b''>16 <c'' c'''>16 <d'' d'''>16 <e'' e'''>16 <ds'' ds'''>16 <f'' f'''>16 <e'' e'''>16 <d'' d'''>16 <c'' c'''>16 |
  <b' b''>16 <a' a''>16 <gs' gs''>16 <a' a''>16 <b' b''>16 <c'' c'''>16 <d'' d'''>16 <cs'' cs'''>16 <e'' e'''>16 <d'' d'''>16 <c'' c'''>16 <b' b''>16 |
  <a' a''>16 <gs' gs''>16 <a' a''>16 <c'' c'''>16 <b' b''>16 <d'' d'''>16 <c'' c'''>16 <b' b''>16 <c'' c'''>16 <e'' e'''>16 <d'' d'''>16 <f'' f'''>16 |
  <e'' e'''>16 <ds'' ds'''>16 <e'' e'''>16 <e' e''>16 <fs' fs''>16 <gs' gs''>16 <a' a''>4 r8 |
  a'16 gs'16 a'16 a''16 gs''16 g''16 g''16 f''16 e''16 f''16 e''16 f''16 |
  a''16 gs''16 a''16 gs''16 a''16 f''16 f''16 e''16 ds''16 e''16 ds''16 e''16 |
  e''16 d''16 c''16 b'16 a'16 e''16 f''16 d''16 b'16 a'16 gs'16 b'16 |
  << { s4. c''4 b'8 } \\ { b'16 a'16 c''16 b'16 d''16 c''16 a'4 gs'8 } >> |
  c''16 b'16 a'16 b'16 c''16 d''16 e''16 ds''16 f''16 e''16 d''16 c''16 |
  b'16 a'16 gs'16 a'16 b'16 c''16 d''16 cs''16 e''16 d''16 c''16 b'16 |
  a'16 gs'16 a'16 c''16 b'16 d''16 c''16 b'16 c''16 e''16 d''16 f''16 |
  e''16 ds''16 e''16 e'16 fs'16 gs'16 a'16 gs'16 a'16 e'16 c'16 e'16 |
  <a' a''>16 <gs' gs''>16 <a' a''>16 <c'' c'''>16 <b' b''>16 <d'' d'''>16 <c'' c'''>16 <b' b''>16 <c'' c'''>16 <e'' e'''>16 <d'' e'''>16 <f'' f'''>16 |
  <e'' e'''>16 <ds'' ds'''>16 <e'' e'''>16 <e' e''>16 <fs' fs''>16 <gs' gs''>16 <a' a''>4 r8 |
}

lower = {
  \global
  \clef bass
  \set Staff.midiInstrument = "acoustic grand"
  a16 e'16 c'16 e'16 a16 e'16 a16 e'16 c'16 e'16 a16 e'16 |
  e16 e'16 b16 e'16 e16 e'16 e16 e'16 b16 e'16 e16 e'16 |
  a16 e'16 c'16 e'16 a16 e'16 b16 e'16 d'16 e'16 b16 e'16 |
  c'16 e'16 b16 e'16 a16 e'16 e16 e'16 ds'16 e'16 e16 e'16 |
  a16 e'16 c'16 e'16 a16 e'16 a16 e'16 c'16 e'16 a16 e'16 |
  e16 e'16 b16 e'16 e16 e'16 e16 e'16 b16 e'16 e16 e'16 |
  a16 e'16 c'16 e'16 gs16 e'16 a16 e'16 c'16 e'16 f16 d'16 |
  e16 c'16 a16 c'16 e16 b16 a,16\staccato c16\staccato e16\staccato a16\staccato a,8 |
  << { c'4 cs'8 d'4. } \\ { a4. a4. } >> |
  << { f'16 e'16 f'16 e'16 f'16 d'16 d'16 c'16 b16 c'16 b16 c'16 } \\ { a4. a4. } >> |
  << { c'16 d'16 e'16 d'16 c'8 b16 c'16 d'16 e'16 f'8 } \\ { a4. gs16 a16 b16 c'16 d'8 } >> |
  << { e'8 e'8 e'8 s4. } \\ { c'8 gs8 a8 ds4 e8 } >> |
  a16 e'16 c'16 e'16 a16 e'16 a16 e'16 c'16 e'16 a16 e'16 |
  e16 e'16 b16 e'16 e16 e'16 e16 e'16 b16 e'16 e16 e'16 |
  a16 e'16 c'16 e'16 gs16 e'16 a16 e'16 c'16 e'16 f16 d'16 |
  e16 c'16 a16 c'16 e16 b16 <a, a>4 r8 |
  a,16 e16 c16 e16 gs,16 e16 a,16 e16 c16 e16 f,16 d16 |
  e,16 c16 a,16 c16 e,16 b,16 a,,16\staccato c,16\staccato e,16\staccato a,16\staccato a,,8 |
}

\score {
  \new PianoStaff <<
    \new Staff { \set Staff.midiInstrument = "acoustic grand" \upper }
    \new Staff { \set Staff.midiInstrument = "acoustic grand" \lower }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

---

## 二、性格变奏与复调解构：人格分裂与戏剧重构（贝多芬 Op. 109 第三乐章）

进入19世纪，纯粹的表面装饰已无法满足浪漫主义对人类复杂心理状态的探索诉求。贝多芬在晚期奏鸣曲中彻底颠覆了装饰性传统，创立了**性格变奏**（Character Variation，德语称 *Charakter-Variation*）与**复调变奏**（Contrapuntal Variation）高度熔铸的全新范式。在此范式下，主题不仅被修饰，更被置入剧烈的性格冲突、速度反差与对位解构之中。

### 1. 主题的萨拉班德遗风与抒情圣咏原型（mm. 1–16）
贝多芬 Op. 109 第三乐章标记为 *Gesangvoll, mit innigster Empfindung*（如歌地，怀着最深沉的情感），3/4 拍，E 大调。该主题是一首兼具萨拉班德舞曲特征与庄严德国圣咏风范的崇高之作：
- **萨拉班德节律**：强烈的第二拍加重与附点停顿，使三拍子舞步沉潜为一种内在的冥想律动；
- **低音线与高音线的两极对位**：
  * 高音声部：$G\sharp 4 \to G\sharp 4 \to A4 \to F\sharp 4 \dots$，以质朴的四部和声织体展开；
  * 低音声部：$E2 \to G\sharp 2 \to A2 \to B2 \dots$，构建出坚如磐石的二重对位骨架；
- **乐段结构与和声向心力**：严格的 16 小节方整结构（$8 + 8$），前半段落于属调 B 大调，后半段从升 c 小调向主调 E 大调回环收拢，展示出极其纯净的德奥古典调性闭环。

贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章主题 mm.1–8 的谱例见 [《增六和弦机制与句法漂移》](../harmony/augmented-sixth-mechanics-and-syntactic-drift.md#score-beethoven-op109-iii-mm1-8)；mm.9–16 的后半段与主题终止式不在该谱例范围内，此处只作文字描述，不另复制代码块。

### 2. 第一变奏：意大利美声咏叹调与歌剧化转译（mm. 17–32）
标记为 *Molto espressivo* 的第一变奏，展示了性格变奏对于“语境置换”的惊人魔力：
- **情感面具的彻底颠覆**：原本庄严肃穆的德国圣咏瞬间化身为一出充满浪漫主义激情的意大利歌剧美声咏叹调（*Bel canto*）；
- **旋律的大跨度飞翔与花腔修饰**：第一小提琴式的右手高音线条以倚音挑起高音 $B5$（小字二组顶端的 B 音），随后在宽广的八度与十度跳进中倾泻出三十二分音符华彩（*Fioritura*）；
- **左手摇曳的舞曲伴奏**：低音第一拍落在大字一组深沉的低音基石上（大字一组的 E 音），二三拍以柔和的柱状和弦跟进，呈现出如同肖邦夜曲般的流动空间感；
- **戏剧动力的渐进升级**：原本平稳的圣咏骨架在连续的切分与渐强（*crescendo*）推动下，爆发出古典装饰性变奏所不具备的强力情感冲击。

```lilypond title="贝多芬 第30钢琴奏鸣曲 Op.109 第三乐章" location="Variation I: Molto espressivo，mm.17–32" id="beethoven-op109-iii-mm17-32"
\version "2.26.0"
\language "english"

% 据 CCARH MuseData（CCARH）转写，学术用途。
% 底本 kern 连续编号 mm.17–35（反复第二结尾另计小节）；此处按刊本印刷号 mm.17–32 标注。

global = {
  \key e \major
  \time 3/4
}

upper = {
  \clef "treble"
  \tempo "Molto espressivo" 4 = 84
  <<
    \new Voice = "rhI" {
      \voiceOne
      \grace { b'8 } ( b'' 2 -> e'' 8. fs'' 16 | % kern m.17
      e'' 4 ds'' 4 ~ ) ds'' 8. b' 16 | % kern m.18
      ( b'' 4. -> ds'' 8 \tuplet 5/4 { e'' 32 fs'' 32 e'' 32 ds'' 32 e'' 32 } fs'' 16 gs'' 16 ) | % kern m.19
      ( gs'' 4 fs'' 4. ds'' 8 ) | % kern m.20
      \grace { b'8 } ( b'' 4. -> gs'' 8 ) ( fs'' 8. -. e'' 16 -. ) | % kern m.21
      ( e'' 8 ds'' 4 ) ( cs'' 8 -. b' 8 -. a' 8 -. ) | % kern m.22
      ( a' 8 gs' 8 fs' 8 b' 8 as' 8 e'' 8 ) | % kern m.23
      ( fs'' 8 e'' 8 fs'' 8 g'' 8 ) ds'' 8. b' 16 | % kern m.24
      ( fs'' 8 e'' 8 fs'' 8 g'' 8 ) ds'' 8. b' 16 | % kern m.25
      \grace { b'8 } b'' 4. -> ( b' 8 bs' 8. cs'' 16 ) | % kern m.26
      \grace { cs''8 } a'' 4. -> ( a' 8 as' 8. b' 16 ) | % kern m.27
      \grace { b'8 } gs'' 4. ( gs' 8 a' 8. e'' 16 ) | % kern m.28
      <e' e''> 8 <ds' ds''> 8 ~ <ds' ds''> 8 <cs' fx'> 8 <b gs'> 8 <a a'> 8 | % kern m.29
      \grace { a''8 } a''' 4. ( gs'' 8 a'' 8. cs''' 16 ) | % kern m.30
      ( as'' 8. b'' 16 ) ( as'' 8. b'' 16 ) ( a'' 8. gs'' 16 ) | % kern m.31
      gs''' 8 e''' 8 ~ ( e''' 16 ds''' 16 ) cs''' 8 ~ ( cs''' 16 b'' 16 ) a'' 8 ~ | % kern m.32
      a'' 8 as'' 8 ~ as'' 16 ( b'' 16 fs'' 8 ) ( gs'' 8. fs'' 16 ) | % kern m.33
      \grace { fs''8 } b'' 4. -> ( b' 8 bs' 8. cs'' 16 ) | % kern m.34
      a'' 8 as'' 8 ~ ( as'' 16 b'' 16 fs'' 8 ) gs'' 4 | % kern m.35
    }
    \new Voice = "rhII" {
      \voiceTwo
      s2. | % kern m.17
      s2. | % kern m.18
      s2. | % kern m.19
      s2. | % kern m.20
      s2. | % kern m.21
      s2. | % kern m.22
      s 2 as' 4 | % kern m.23
      as' 2 b' 4 | % kern m.24
      as' 2 b' 4 | % kern m.25
      s2. | % kern m.26
      s2. | % kern m.27
      s 2 e' 4 | % kern m.28
      s2. | % kern m.29
      s2. | % kern m.30
      s2. | % kern m.31
      s2. | % kern m.32
      s2. | % kern m.33
      s2. | % kern m.34
      s2. | % kern m.35
    }
  >>
}

lower = {
  \clef "bass"
  <<
    \new Voice = "lhI" {
      \voiceOne
      e, 4 <b, e gs b> 4 <b, e gs b> 4 | % kern m.17
      fs, 4 <b, fs a b> 4 <b, fs a b> 4 | % kern m.18
      gs, 4 <b, e gs b> 4 <b, e gs b> 4 | % kern m.19
      a, 4 <b, ds fs b> 4 <b, ds fs b> 4 | % kern m.20
      gs, 4 <b, e gs b> 4 <b, e gs b> 4 | % kern m.21
      fs, 4 <b, ds fs a> 4 <ds, b,> 4 | % kern m.22
      b, 4 b, 4 cs, 8 fs,, 8 | % kern m.23
      ( cs, 8 g, 8 fs, 8 e, 8 ) ( <b,, fs,> 8 cs, 16 ds, 16 ) | % kern m.24
      ( cs, 8 g, 8 fs, 8 e, 8 ) ( <b,, fs,> 8 <cs, e,> 8 ) | % kern m.25
      <ds, fs,> 4 <ds fs b> 4 <es gs cs'> 4 | % kern m.26
      fs, 4 <fs a> 4 <ds fs b> 4 | % kern m.27
      e, 4 <e gs b> 4 <cs cs'> 4 | % kern m.28
      cs' 8 b 8 ~ b 8 as 8 gs 8 fs 8 | % kern m.29
      fs, 4 <fs a> 4 <cs e a> 4 | % kern m.30
      ds, 4 <ds fs a b> 4 <e gs b> 4 | % kern m.31
      b, 4 <gs b e'> 4 <fs a b ds'> 4 | % kern m.32
      e, 4 <e fs a b ds'> 4 <e gs b e'> 8 <ds fs b ds'> 8 | % kern m.33
      ds, 4 <ds fs b> 4 <es gs cs'> 4 | % kern m.34
      e, 4 <e fs a b ds'> 4 <e gs b e'> 4 | % kern m.35
    }
    \new Voice = "lhII" {
      \voiceTwo
      s2. | % kern m.17
      s2. | % kern m.18
      s2. | % kern m.19
      s2. | % kern m.20
      s2. | % kern m.21
      s2. | % kern m.22
      ( e, 4 ds, 8 d, 8 cs, 4 | % kern m.23
      fs,, 2 s 4 | % kern m.24
      fs,, 2 s 4 | % kern m.25
      s2. | % kern m.26
      s2. | % kern m.27
      s2. | % kern m.28
      ds 4 ( ds 4 gs, 8 fs, 8 ) | % kern m.29
      s2. | % kern m.30
      s2. | % kern m.31
      s2. | % kern m.32
      s2. | % kern m.33
      s2. | % kern m.34
      s2. | % kern m.35
    }
  >>
}

\score {
  \new PianoStaff <<
    \new Staff = "RH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \upper
    }
    \new Staff = "LH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \lower
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

### 3. 第二变奏：轻盈点彩断奏与严格二重对位（mm. 33–64）
紧接第一变奏的歌剧狂澜，第二变奏（*Leggiermente*）呈现出彻底的结构粉碎与复调智性游戏：
- **织体的极简粉碎**：连贯如歌的线条被彻底碎裂为点彩式的十六分音符跳音（Staccato）；
- **霍克特式交错对位（Hocket-like Dialogue）**：右手与左手相隔半拍错位进入，你呼我应；主题的原型动机在此被拆解为单音微粒，在两只手之间以极其严苛的二重对位方式相互抛掷；
- **温柔连奏的戏剧性截断（mm. 41–48）**：在第 9–12 小节，轻佻碎裂的断奏忽然被极度温柔的四部纯净连奏（*Teneramente, legato*）强行切断，形成了巨大的戏剧性格撕裂；
- **再现部的严格二重对位倒影（mm. 49–64）**：在后半程，左右手声部发生颠倒互换（Invertible Counterpoint），原先的上方高音声部翻转为低音，低音声部跃升为高音，充分彰显了贝多芬深邃的巴洛克复调功力。

```lilypond title="贝多芬 第30钢琴奏鸣曲 Op.109 第三乐章" location="Variation II: Leggiermente，mm.33–48" id="beethoven-op109-iii-mm33-48"
\version "2.26.0"
\language "english"

% 据 CCARH MuseData（CCARH）转写，学术用途。
% 底本 kern 连续编号 mm.36–51（反复第二结尾另计小节）；此处按刊本印刷号 mm.33–48 标注。

global = {
  \key e \major
  \time 3/4
}

upper = {
  \clef "treble"
  \tempo "Leggiermente" 4 = 84
  <<
    \new Voice = "rhI" {
      \voiceOne
      r 16 ( b 16 gs' 16 ) r 16 r 16 ( e' 16 b 16 ) r 16 r 16 ( cs' 16 fs' 16 ) r 16 | % kern m.36
      r 16 ( ds' 16 fs 16 ) r 16 r 16 e 16 b 16 r 16 r 16 b 16 fs 16 r 16 | % kern m.37
      r 16 gs' 16 gs'' 16 r 16 r 16 e'' 16 b' 16 r 16 r 16 cs'' 16 fs'' 16 r 16 | % kern m.38
      r 16 ds'' 16 fs'' 16 r 16 r 16 as'' 16 e'' 16 r 16 r 16 <ds'' fs''> 16 b'' 16 r 16 | % kern m.39
      r 16 b'' 16 e'' 16 r 16 r 16 gs'' 16 e''' 16 r 16 r 16 e''' 16 fs''' 16 r 16 | % kern m.40
      r 16 e''' 16 ds''' 16 r 16 r 16 ds''' 16 cs''' 16 r 16 r 16 b'' 16 a'' 16 r 16 | % kern m.41
      r 16 a'' 16 gs'' 16 r 16 r 16 gs'' 16 a'' 16 r 16 r 16 bf'' 16 e''' 16 r 16 | % kern m.42
      r 16 <bf'' e'''> 16 <a'' f'''> 16 r 16 r 16 <bf'' g'''> 16 <g'' e'''> 16 r 16 r 16 b''' 16 b'' 16 r 16 | % kern m.43
      ( gs' 8 e' 8 ) e' 8 e' 8 ( e' 8. ds' 32 e' 32 ) | % kern m.44
      ( a' 8 fs' 8 ) fs' 8 fs' 8 ( fs' 8. es' 32 fs' 32 ) | % kern m.45
      ( b' 8 gs' 8 ) gs' 8 gs' 8 ( gs' 8. fs' 32 gs' 32 ) | % kern m.46
      ( <cs' cs''> 8 <cs' a'> 8 ) <cs' a'> 8 <cs' a'> 8 ( a' 8. gs' 32 a' 32 ) | % kern m.47
      r 16 <gs' b' gs''> 16 r 16 <gs' b' e''> 16 r 16 <gs' b' ds''> 16 r 16 <gs' b' e''> 16 r 16 <gs' b' ds''> 16 r 16 <gs' b' e''> 16 | % kern m.48
      r 16 <a' ds'' fs'' a''> 16 r 16 <a' ds'' fs''> 16 r 16 <a' ds'' es''> 16 r 16 <a' ds'' fs''> 16 r 16 <a' ds'' es''> 16 r 16 <a' ds'' fs''> 16 | % kern m.49
      r 16 <b' e'' gs'' b''> 16 r 16 <b' e'' gs''> 16 r 16 <b' e'' gs''> 16 r 16 <b' e'' b''> 16 r 16 <as' e'' g'' as''> 16 r 16 <e'' as'' e'''> 16 | % kern m.50
      r 16 <e'' as'' e'''> 16 r 16 <fs'' as'' fs'''> 16 r 16 <g'' as'' g'''> 16 r 16 <e'' as'' e'''> 16 r 16 <e'' as'' e'''> 16 r 16 <ds'' b'' ds'''> 16 | % kern m.51
    }
    \new Voice = "rhII" {
      \voiceTwo
      s2. | % kern m.36
      s2. | % kern m.37
      s2. | % kern m.38
      s2. | % kern m.39
      s2. | % kern m.40
      s2. | % kern m.41
      s2. | % kern m.42
      s2. | % kern m.43
      s2. | % kern m.44
      ( e' 2 ds' 4 ) | % kern m.45
      ( fs' 2 e' 4 ) | % kern m.46
      gs' 2 fs' 4 | % kern m.47
      s2. | % kern m.48
      s2. | % kern m.49
      s2. | % kern m.50
      s2. | % kern m.51
    }
  >>
}

lower = {
  \clef "bass"
  e, 16 r 16 r 16 ( e 16 gs 16 ) r 16 r 16 ( gs, 16 a, 16 ) r 16 r 16 ( a 16 | % kern m.36
  b 16 ) r 16 r 16 b, 16 cs 16 r 16 r 16 cs' 16 ds' 16 r 16 r 16 ds 16 | % kern m.37
  e 16 r 16 r 16 e' 16 \clef "treble" gs' 16 r 16 r 16 gs 16 as 16 r 16 r 16 as' 16 | % kern m.38
  b' 16 r 16 r 16 fs' 16 fs' 16 r 16 r 16 cs'' 16 b' 16 r 16 r 16 a' 16 | % kern m.39
  gs' 16 r 16 r 16 gs'' 16 e'' 16 r 16 r 16 b' 16 cs'' 16 r 16 r 16 as' 16 | % kern m.40
  as' 16 r 16 r 16 b' 16 cs'' 16 r 16 r 16 e'' 16 ds'' 16 r 16 r 16 fs'' 16 | % kern m.41
  d'' 16 r 16 r 16 f'' 16 cs'' 16 r 16 r 16 e'' 16 c'' 16 r 16 r 16 g'' 16 | % kern m.42
  c'' 16 r 16 r 16 c''' 16 c'' 16 r 16 r 16 c''' 16 b'' 16 r 16 r 16 b' 16 | % kern m.43
  \clef "bass" r 8 <b, e gs> 8 <b, e gs> 8 <b, e gs> 8 <b, e gs> 8 <b, e gs> 8 | % kern m.44
  <b, fs a> 8 <b, fs a> 8 <b, fs a> 8 <b, fs a> 8 <b, fs a> 8 <b, fs a> 8 | % kern m.45
  <b, gs b> 8 <b, gs b> 8 <b, gs b> 8 <b, gs b> 8 <b, gs b> 8 <b, gs b> 8 | % kern m.46
  <b, a> 8 <b, a> 8 <b, a> 8 <b, a> 8 <b ds'> 8 <b ds'> 8 | % kern m.47
  b, 16 r 16 <gs b e'> 16 r 16 <gs b e'> 16 r 16 <gs b e'> 16 r 16 <gs b e'> 16 r 16 <gs b e'> 16 r 16 | % kern m.48
  b, 16 r 16 <fs a b ds'> 16 r 16 <fs a b ds'> 16 r 16 <fs a b ds'> 16 r 16 <fs a b ds'> 16 r 16 <fs a b ds'> 16 r 16 | % kern m.49
  b, 16 r 16 <gs b e'> 16 r 16 <gs b e'> 16 r 16 <gs b e'> 16 r 16 cs 16 r 16 <g as e'> 16 r 16 | % kern m.50
  c 16 r 16 <g as e'> 16 r 16 <g as e'> 16 r 16 <g as e'> 16 r 16 <c g> 16 r 16 <b, b> 16 r 16 | % kern m.51
}

\score {
  \new PianoStaff <<
    \new Staff = "RH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \upper
    }
    \new Staff = "LH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \lower
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

### 4. 节拍突变与复调织体沉思（第三、四变奏）
在进入终极高潮前，贝多芬通过节拍与复调织体的持续重组拓展性格空间：
- **第三变奏（Allegro vivace，2/4 拍，mm. 65–96）**：节拍骤然由三拍子压缩为紧凑的 2/4 拍，双手展开高速的十六分音符奔涌，以托卡塔式的机械动力爆发出充沛的戏剧动能；
- **第四变奏（9/8 拍，mm. 97–112）**：标记为稍慢于主题，拍号转为摇曳的 9/8 拍，四声部之间展开温柔的复调卡农模仿与动机重叠，构建出深邃的室内乐冥想空间。

### 5. 严密对位与主题终极消解（第五、六变奏）
贝多芬并未止步于表层的性格分裂，而是在后半程进一步引爆了对位法与音响物理维度的潜能：
- **第五变奏（Allegro, ma non troppo，mm. 113–128）**：音乐骤然化为严苛的四声部自由赋格。圣咏主题的下行级进被提炼为刚劲的对位短句，各声部展开紧凑的卡农式追逐与密接和应（Stretto），彻底抽离了舞曲外壳；
- **第六变奏（Tempo I del tema）与主题回归**：基础圣咏原型以不可思议的音符密度重新凝聚，右手在最高音区激荡起漫长的持续颤音（Trill），下方以急促的分解和弦瀑布喷薄而下。在经历了一整场精神宇宙的裂变浩劫之后，原初质朴的主题以完全未施粉黛的素颜（Da Capo）重现，达成了一种“看山还是山”的形而上顿悟。

```lilypond title="贝多芬 第30钢琴奏鸣曲 Op.109 第三乐章" location="Variation V: Allegro, ma non troppo，mm.113–128" id="beethoven-op109-iii-mm113-128"
\version "2.26.0"
\language "english"

% 据 CCARH MuseData（CCARH）转写，学术用途。
% 底本 kern 连续编号 mm.120–135（反复第二结尾另计小节）；此处按刊本印刷号 mm.113–128 标注。

global = {
  \key e \major
  \time 4/4
}

upper = {
  \clef "bass"
  \tempo "Allegro, ma non troppo" 4 = 84
  <<
    \new Voice = "rhI" {
      \voiceOne
      \clef "bass" gs 2 e 2 | % kern m.120
      a 2 fs 2 ~ | % kern m.121
      fs 4 gs 8 ds 8 e 4 d 4 | % kern m.122
      cs' 2 a 2 ~ | % kern m.123
      ( a 4 as 4 b 4 a 4 ) | % kern m.124
      gs 4 b 4 b 4 e' 4 | % kern m.125
      \clef "treble" ( e' 2. f' 4 | % kern m.126
      <e' g'> 4 <f' a'> 4 <g' bf'> 4 <ds' b'> 4 ) | % kern m.127
      \clef "bass" gs 2 e 2 | % kern m.128
      a 2 fs 2 | % kern m.129
      \clef "treble" r 8 b' 8 -. cs'' 8 -. ds'' 8 -. e'' 8 -. fs'' 8 -. gs'' 8 -. e'' 8 -. | % kern m.130
      a'' 8 cs'' 8 ds'' 8 e'' 8 fs'' 8 gs'' 8 a'' 8 fs'' 8 | % kern m.131
      b'' 8 ds'' 8 e'' 8 fs'' 8 gs'' 8 a'' 8 b'' 8 gs'' 8 | % kern m.132
      c''' 8 e'' 8 fs'' 8 gs'' 8 a'' 8 b'' 8 c''' 8 a'' 8 | % kern m.133
      d''' 8 fs'' 8 g'' 8 a'' 8 b'' 8 c''' 8 d''' 8 b'' 8 | % kern m.134
      e''' 8 d''' 8 e''' 8 f''' 8 g''' 8 as''' 8 b''' 8 ds''' 8 | % kern m.135
    }
    \new Voice = "rhII" {
      \voiceTwo
      s1 | % kern m.120
      e 4 fs 8 cs 8 ds 4 b, 4 | % kern m.121
      b 2 gs 2 | % kern m.122
      <cs gs> 4 a 8 e 8 fs 4 c 4 | % kern m.123
      r 1 | % kern m.124
      r 4 e 4 gs 2 | % kern m.125
      s1 | % kern m.126
      s1 | % kern m.127
      s1 | % kern m.128
      e 4 fs 8 cs 8 ds 4 b, 4 | % kern m.129
      \clef "treble" gs' 2 e' 2 ~ | % kern m.130
      e' 4 fs' 8 cs' 8 ds' 4 b 4 ~ | % kern m.131
      b 4 gs' 8 ds' 8 e' 4 d' 4 | % kern m.132
      c' 4 a' 8 e' 8 f' 4 e' 4 | % kern m.133
      s1 | % kern m.134
      s 2 e''' 4 ds''' 8 r 8 | % kern m.135
    }
  >>
}

lower = {
  \clef "bass"
  <<
    \new Voice = "lhI" {
      \voiceOne
      r 4 e, 4 -. gs, 2 ~ | % kern m.120
      gs, 4 fs, 4 -. a, 2 ~ | % kern m.121
      a, 4 gs, 4 -. b, 2 ~ | % kern m.122
      b, 4 a, 4 -. c 4 e, 4 | % kern m.123
      b, 2 fs, 2 ~ | % kern m.124
      fs, 4 gs, 4 r 2 | % kern m.125
      gs 4 a 4 bf 4 a 4 | % kern m.126
      ( g, 4 f, 4 e, 4 fs, 4 ) | % kern m.127
      r 8 b,, 8 -. cs, 8 -. ds, 8 -. e, 8 -. fs, 8 -. gs, 8 -. e, 8 -. | % kern m.128
      fs, 8 -. b,, 8 -. ds, 8 -. e, 8 -. fs, 8 -. gs, 8 -. a, 8 -. fs, 8 -. | % kern m.129
      b, 8 -. ds 8 -. e 8 -. fs 8 -. gs 2 | % kern m.130
      fs 2 a 2 | % kern m.131
      gs 2 b 2 | % kern m.132
      a 2 ( cs' 2 | % kern m.133
      \clef "treble" d' 4 b' 8 fs' 8 g' 4 f' 4 | % kern m.134
      e' 8 f' 8 gs' 8 f' 8 e' 4 fs' 4 | % kern m.135
    }
    \new Voice = "lhII" {
      \voiceTwo
      s1 | % kern m.120
      s1 | % kern m.121
      s1 | % kern m.122
      s1 | % kern m.123
      e, 4 fs, 8 cs, 8 ds, 4 b,, 4 ~ | % kern m.124
      b,, 4 gs, 8 ds, 8 e, 4 b,, 4 | % kern m.125
      ( bs,, 4 cs, 2 <c, c> 4 ) | % kern m.126
      c, 2. b,, 4 | % kern m.127
      s1 | % kern m.128
      s1 | % kern m.129
      s1 | % kern m.130
      s1 | % kern m.131
      s1 | % kern m.132
      s1 | % kern m.133
      \clef "treble" c' 4 b 2 g 4 | % kern m.134
      c' 2 ~ c' 4 b 4 | % kern m.135
    }
    \new Voice = "lhIII" {
      \voiceThree
      s1 | % kern m.120
      s1 | % kern m.121
      s1 | % kern m.122
      s1 | % kern m.123
      s1 | % kern m.124
      s1 | % kern m.125
      r 2 cs 4 s4 | % kern m.126
      s1 | % kern m.127
      s1 | % kern m.128
      s1 | % kern m.129
      s1 | % kern m.130
      s1 | % kern m.131
      s1 | % kern m.132
      s1 | % kern m.133
      s1 | % kern m.134
      s1 | % kern m.135
    }
  >>
}

\score {
  \new PianoStaff <<
    \new Staff = "RH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \upper
    }
    \new Staff = "LH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \lower
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

---

## 三、时值递减与比例时间变奏：微观细分与永恒感知（贝多芬 Op. 111 第二乐章）

如果说 Op. 109 展现的是性格空间维度的浩瀚，那么贝多芬《c小调第32钢琴奏鸣曲》Op. 111 第二乐章（阿里埃塔，*Arietta: Adagio molto semplice e cantabile*）则是音乐史上关于**时间维度**变奏的巅峰丰碑——**时值递减与比例变奏**（Metric Diminution & Proportional / Temporal Variation）。

### 1. 阿里埃塔主题的原初母体与三音上升动机（mm. 1–16）
- **节拍律动的天平**：全曲置于极其罕见的 9/16 拍之中。9/16 拍意味着每小节包含 3 个大拍（每个大拍为一个附点八分音符），每个大拍由 3 个十六分音符构成（三小拍九等分），形成了自然摇曳的三连音律动基准；
- **极简崇高的三音核**：弱拍起音由主音跳向属音（$C5 \to G4$），随后以级进加跳进唱出统摄全乐章的升华动机：
  $$C \to D \to G$$
- **十六小节神圣母题的骨架**：
  * 前 4 小节：弱起进入，旋律在 $G4$ 长音上呼吸，通过模进上升至 $E5 \to C5$；
  * mm. 5–8：低音走出纯朴的级进下行（$C \to B \to A \to G$），高音攀升至 $G5$ 峰值，半终止于属调 G 大调；
  * mm. 9–16：向 a 小调与下属调展开微弱的冥想暗影，最终以神圣的光辉收束于 C 大三和弦原位完全正格终止。

```lilypond title="贝多芬 第32钢琴奏鸣曲 Op.111 第二乐章" location="Arietta: Adagio molto semplice e cantabile，mm.1–16" id="beethoven-op111-ii-mm1-16"
\version "2.26.0"
\language "english"

% 据 CCARH MuseData（CCARH）转写，学术用途。
% 底本 kern 连续编号 mm.1–18（反复第二结尾另计小节）；此处按刊本印刷号 mm.1–16 标注。

global = {
  \key c \major
  \time 9/16
}

upper = {
  \clef "treble"
  \tempo "Adagio molto semplice e cantabile" 8. = 40
  <<
    \new Voice = "rhI" {
      \voiceOne
      g' 4. ( d'' 8 g' 16 ) | % kern m.1
      g' 4. g' 8. | % kern m.2
      ( g' 8. e'' 8. c'' 8. ) | % kern m.3
      c'' 8. b' 8. <g' b'> 8. | % kern m.4
      ( c'' 8. e'' 8. g'' 8. ) | % kern m.5
      ( g'' 8. f'' 8. d'' 8 <a' c''> 16 ) | % kern m.6
      ( <g' b'> 8. <g' c''> 8. <g' d''> 8 g' 16 ) | % kern m.7
      g' 4. s8. | % kern m.8
      g' 4. e' 8. | % kern m.9
      c'' 4. ( c'' 8 b' 16 ) | % kern m.10
      b' 4. ( b' 8 e'' 16 ) | % kern m.11
      <b' e''> 8. ( <c'' e''> 8. <b' d''> 8 <a' c''> 16 ) | % kern m.12
      ( <a' c''> 8. <gs' b'> 8. <e' a' c''> 8. ) | % kern m.13
      <g' b' d''> 4. <g' b' d''> 8. | % kern m.14
      <g' c'' e''> 4. <a' c'' f''> 8. | % kern m.15
      <g' b' d''> 8. <g' b' d''> 8. ( <g' b' d''> 8 <b' d'' g''> 16 ) | % kern m.16
      ( <b' d'' g''> 8 <g' c'' e''> 16 ) <g' c'' e''> 8. e' 8. | % kern m.17
      ( <b' d'' g''> 8 <g' c'' e''> 16 ) <g' c'' e''> 8. c'' 8 e' 16 | % kern m.18
    }
    \new Voice = "rhII" {
      \voiceTwo
      ( e' 8. f' 8. d' 8. ) | % kern m.1
      ( d' 8. e' 8. f' 8. ) | % kern m.2
      g' 8. e' 8. g' 8. | % kern m.3
      e' 8. d' 8. d' 8. | % kern m.4
      g' 4. g' 8. | % kern m.5
      a' 4. a' 8 d' 16 | % kern m.6
      d' 8. c' 8. d' 8 d' 16 ~ | % kern m.7
      d' 8 ( d' 16 <c' e'> 8 <b f'> 16 ) s8. | % kern m.8
      d' 8 ( <c' e'> 16 <b f'> 8 <c' e'> 16 ) s 8. | % kern m.9
      e' 4. e' 8. | % kern m.10
      e' 4. s 8. | % kern m.11
      s2 s16 | % kern m.12
      s2 s16 | % kern m.13
      s2 s16 | % kern m.14
      s2 s16 | % kern m.15
      s2 s16 | % kern m.16
      s2 s16 | % kern m.17
      s2 s16 | % kern m.18
    }
  >>
}

lower = {
  \clef "bass"
  <<
    \new Voice = "lhI" {
      \voiceOne
      <c, g,> 8. <d, g,> 8. <b,, g,> 8. | % kern m.1
      <b,, g,> 8. <c, g,> 8. <d, g,> 8. | % kern m.2
      <e, g,> 8. <c, g,> 8. <e, g,> 8. | % kern m.3
      ( g,, 8. g, 8. ) ( <g,, g,> 8 <f,, f,> 16 ) | % kern m.4
      <e,, e,> 4. <e,, e,> 8. | % kern m.5
      <d,, d,> 4. ( <f,, f,> 8 <fs,, fs,> 16 ) | % kern m.6
      ( g, 8. a, 8. b, 8 ) b, 16 ~ | % kern m.7
      b, 8 ( b, 16 c 8 s4 | % kern m.8
      b, 8 ) ( c 16 d 8 c 16 ) e 8. | % kern m.9
      a, 8. e 8. e 8. | % kern m.10
      gs, 8. e 8. e 8. | % kern m.11
      <gs, e> 8. <a, e> 8. <a, e> 8. | % kern m.12
      ( e, 8. e 8. ) <a,, a,> 8. | % kern m.13
      <g,, g,> 4. <g,, g,> 8. | % kern m.14
      <c, c> 4. <f,, f,> 8. | % kern m.15
      <g,, g,> 8. <g,, g,> 8. <g,, g,> 8 <g,, g,> 16 | % kern m.16
      ( <g,, g,> 8 <c, c> 16 ) <c, c> 8. e 8. | % kern m.17
      ( <g,, g,> 8 <c, c> 16 ) <c, c> 16 ( g 16 f 16 e 16 c 16 g 16 ) | % kern m.18
    }
    \new Voice = "lhII" {
      \voiceTwo
      s2 s16 | % kern m.1
      s2 s16 | % kern m.2
      s2 s16 | % kern m.3
      g,, 4. s 8. | % kern m.4
      s2 s16 | % kern m.5
      s2 s16 | % kern m.6
      g,, 4. s 8. | % kern m.7
      s2 s16 | % kern m.8
      s2 s16 | % kern m.9
      a, 4. a, 8. | % kern m.10
      gs, 4. gs, 8. | % kern m.11
      s2 s16 | % kern m.12
      e, 4. s 8. | % kern m.13
      s2 s16 | % kern m.14
      s2 s16 | % kern m.15
      s2 s16 | % kern m.16
      s2 s16 | % kern m.17
      s2 s16 | % kern m.18
    }
  >>
}

\score {
  \new PianoStaff <<
    \new Staff = "RH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \upper
    }
    \new Staff = "LH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \lower
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

### 2. 比例递减的数学阶梯与时间引力坍缩
在阿里埃塔主题之后，贝多芬并未改变基础脉搏的绝对时钟速度，而是通过严密的节拍乘法递增，展开了人类音乐史上最壮丽的**时值持续细分**（Progressive Metric Subdivisions）：
- **变奏一（Var. 1，9/16 拍，mm. 17–32）**：基础脉动保持 9/16 拍，但每小拍内部开始被细分为附点十六分音符与三十二分音符的交错律动，旋律流动感显著提升；
- **变奏二（Var. 2，6/16 拍，mm. 33–48）**：拍号切入 6/16 拍（*L'istesso tempo*），大拍由三等分重构为复合两等分，三连音在更密集的微观时间中翻滚，产生出轻快跃动的步调；
- **变奏三（Var. 3，12/32 拍，mm. 49–64）**：拍号切入 12/32 拍（*L'istesso tempo*），每个大拍被细分为极速的三十二分音符狂喜切分，产生出超越时代的先锋摇摆与能量喷薄；
- **变奏四与终曲（Var. 4–Coda，9/16 拍，mm. 65–177）**：时值被进一步压缩至六十四分音符甚至无法被物理计量的超高音长颤音（Trill）。在小字三组高空，密集的音符微粒不再产生速度感，而是因为振动频率达到感知极限，反向转化为一种超脱时间流逝的“永恒静止”（Eternal Stasis）。

### 3. 声学空间的极端极化与超越物理时间
在变奏四及其后的发展中，时值细分与键盘音响物理发生剧烈共振：
- **两极声学真空**：左手深陷于大字一组与大字二组的极低音持续音（Pedal point），右手则游弋在小字三组甚至小字四组的高空。中间长达三个八度的声学空洞，彻底瓦解了古典四部和声的密集肉身感；
- **高音颤音的超验光环**：在高音区长达数十小节的三重颤音中，音符运动彻底脱离了节拍重音的牵引，转化为一种纯粹的光线与泛音云团。变奏曲式在此完成了从“修辞技术”到“形而上宇宙论”的终极飞跃。

```lilypond title="贝多芬 第32钢琴奏鸣曲 Op.111 第二乐章" location="Variation II: L'istesso tempo，mm.33–48" id="beethoven-op111-ii-mm33-48"
\version "2.26.0"
\language "english"

% 据 CCARH MuseData（CCARH）转写，学术用途。
% 底本 kern 连续编号 mm.36–54（反复第二结尾另计小节）；此处按刊本印刷号 mm.33–48 标注。

global = {
  \key c \major
  \time 9/16
}

upper = {
  \clef "treble"
  \tempo "L'istesso tempo" 8. = 40
  <<
    \new Voice = "rhI" {
      \voiceOne
      c'' 8 <c' e'> 16 ) s4. | % kern m.36
      ( <d'' g''> 16 <b' f''> 16 <c'' e''> 16 <c'' f''> 16 <c'' e''> 16 <c'' e''> 16 ) s8. | % kern m.36+1
      \time 6/16 r 8 s4 | % kern m.36+2
      \tuplet 3/2 { ( e'' 16 c'' 32 b' 16 c'' 32 } \tuplet 3/2 { d'' 16 b' 32 as' 16 b' 32 ) } r 8 | % kern m.37
      \tuplet 3/2 { f 16 d 32 cs 16 d 32 } \tuplet 3/2 { g' 16 e' 32 ds' 16 e' 32 } \tuplet 3/2 { g' 16 e' 32 g' 16 f' 32 } | % kern m.38
      \tuplet 3/2 { a' 16 fs' 32 a' 16 g' 32 } <g' e''> 8 <g' c''> 8 | % kern m.39
      \tuplet 3/2 { c'' 16 b' 32 d'' 16 c'' 32 } \tuplet 3/2 { c'' 16 as' 32 c'' 16 b' 32 } <g' b'> 8 | % kern m.40
      c'' 8 \tuplet 3/2 { e'' 16 d'' 32 f'' 16 e'' 32 } g'' 8 ~ | % kern m.41
      g'' 16 g'' 16 ~ \tuplet 3/2 { g'' 16 e'' 32 g'' 16 f'' 32 } \tuplet 3/2 { e'' 16 cs'' 32 e'' 16 d'' 32 } | % kern m.42
      c'' 16 b' 16 c'' 16 cs'' 16 d'' 16 d'' 16*2/3 g' 32*2/3 | % kern m.43
      g' 16 g' 16 ~ g' 16 g' 16 s8 | % kern m.44
      g' 16 g' 16 ~ \tuplet 3/2 { g' 16 gs' 32 a' 16 b' 32 } \tuplet 3/2 { e' 16 e' 32 ~ e' 16 e' 32 } | % kern m.45
      c'' 16 ~ c'' 16*2/3 b' 32*2/3 c'' 16 ~ c'' 16*2/3 b' 32*2/3 c'' 16 ~ c'' 16*2/3 b' 32*2/3 | % kern m.46
      b' 16 ~ b' 16*2/3 c'' 32*2/3 b' 16 ~ b' 16*2/3 c'' 32*2/3 b' 16 ~ b' 16*2/3 e'' 32*2/3 | % kern m.47
      <b' e''> 16 ~ <b' e''> 16*2/3 <c'' e''> 32*2/3 <c'' e''> 16 ~ \tuplet 3/2 { <c'' e''> 16 <gs' b' d''> 32 ( <e' b' d''> 16 <f' a' c''> 32 } <fs' a' c''> 16*2/3 <gs' b'> 32*2/3 | % kern m.48
      \tuplet 3/2 { <b gs' b'> 16 <b gs' b'> 32 ~ <b gs' b'> 16 <b gs' b'> 32 ~ } \tuplet 3/2 { <b gs' b'> 16 <c' a' c''> 32 ~ <c' a' c''> 16 <c' a' c''> 32 ~ } \tuplet 3/2 { <c' a' c''> 16 <d' b' d''> 32 ~ <d' b' d''> 16 <d'' b'' d'''> 32 } | % kern m.49
      s 8 d'' 8 ~ \tuplet 3/2 { d'' 16 ds'' 32 f'' 16 e'' 32 } | % kern m.50
      e'' 8 ~ e'' 16 e'' 16 ~ \tuplet 3/2 { e'' 16 e'' 32 g'' 16 f'' 32 } | % kern m.51
      \tuplet 3/2 { d'' 16 ( fs'' 32 a'' 16 g'' 32 ~ ) } ( g'' 16 \tuplet 3/2 { a'' 16 g'' 32 ~ ) ( g'' 16 f'' 32 } a'' 16*2/3 g'' 32*2/3 ) | % kern m.52
      g'' 16 ~ g'' 16*2/3 f'' 32*2/3 e'' 16 r 16 r 16*2/3 \tuplet 3/2 { e' 32 ~ e' 16 } e' 32*2/3 | % kern m.53
      g'' 16 ~ \tuplet 3/2 { g'' 16 f'' 32 e'' 16 g'' 32 ~ } g'' 16*2/3 g'' 32*2/3 s8 | % kern m.54
    }
    \new Voice = "rhII" {
      \voiceTwo
      s2 s16 | % kern m.36
      s2 s16 | % kern m.36+1
      \time 6/16 s4. | % kern m.36+2
      \tuplet 3/2 { g' 16 e' 32 d' 16 e' 32 } \tuplet 3/2 { f' 16 d' 32 cs' 16 d' 32 } r 8 | % kern m.37
      s4. | % kern m.38
      s4. | % kern m.39
      \tuplet 3/2 { e' 16 d' 32 f' 16 e' 32 } \tuplet 3/2 { e' 16 cs' 32 e' 16 d' 32 } d' 8 | % kern m.40
      g' 8 e' 16 g' 16 \tuplet 3/2 { d'' 16 cs'' 32 e'' 16 d'' 32 } | % kern m.41
      \tuplet 3/2 { cs'' 16 b' 32 d'' 16 cs'' 32 } a' 16 a' 16 ~ a' 16 a' 16 | % kern m.42
      a' 16 d' 16 \tuplet 3/2 { g' 16 e' 32 g' 16 f' 32 ~ } \tuplet 3/2 { f' 16 d' 32 <f' af'> 16 <d' f'> 32 } | % kern m.43
      \tuplet 3/2 { <d' f'> 16 d' 32 b 16 c' 32 } \tuplet 3/2 { d' 16 c' 32 f' 16 e' 32 } s8 | % kern m.44
      \tuplet 3/2 { <d' f'> 16 d' 32 <b f'> 16 <c' e'> 32 } \tuplet 3/2 { e' 16 <d' e'> 32 <c' e'> 16 <b e'> 32 } \tuplet 3/2 { b 16 d' 32 <a c'> 16 <gs d'> 32 } | % kern m.45
      c' 16*2/3 ds' 32*2/3 e' 16 ~ e' 16*2/3 ds' 32*2/3 e' 16 ~ e' 16*2/3 ds' 32*2/3 e' 16 ~ | % kern m.46
      e' 16*2/3 f' 32*2/3 e' 16 ~ e' 16*2/3 f' 32*2/3 e' 16 ~ e' 16*2/3 f' 32*2/3 e' 16 | % kern m.47
      s4. | % kern m.48
      s4. | % kern m.49
      \tuplet 3/2 { ( <d'' b'' d'''> 16 d'' 32 cs'' 16 d'' 32 ) } \tuplet 3/2 { d'' 16 b' 32 as' 16 b' 32 } g' 16 g' 16 ~ | % kern m.50
      \tuplet 3/2 { g' 16 c'' 32 b' 16 c'' 32 } \tuplet 3/2 { c'' 16 bf' 32 a' 16 bf' 32 } bf' 16 ~ bf' 16*2/3 a' 32*2/3 | % kern m.51
      a' 16*2/3 c'' 32*2/3 d'' 16 ~ d'' 16*2/3 ds'' 32*2/3 e'' 16 ~ \tuplet 3/2 { e'' 16 f'' 32 <b' f''> 16 <b' d''> 32 } | % kern m.52
      \tuplet 3/2 { <b' d''> 16 b' 32 c'' 16 d'' 32 } \tuplet 3/2 { g' 16 b 32 c' 16 d' 32 } \tuplet 3/2 { c' 16 b 32 a 16 <gs d'> 32 } | % kern m.53
      \tuplet 3/2 { <b' d''> 16 b' 32 c'' 16 d'' 32 } \tuplet 3/2 { g' 16 d'' 32 e'' 16 f'' 32 } s8 | % kern m.54
    }
  >>
}

lower = {
  \clef "bass"
  <<
    \new Voice = "lhI" {
      \voiceOne
      e 16 a, 16 e 16 s4. | % kern m.36
      r 16 g 16 g 16 ( a 16 ) g 16 g 16 s8. | % kern m.36+1
      \time 6/16 \tuplet 3/2 { c' 16 ( g 32 fs 16 g 32 ) } s4 | % kern m.36+2
      g 16 g 16 ~ g 16 g 16 \tuplet 3/2 { ( d 16 g, 32 fs, 16 g, 32 ) } | % kern m.37
      a, 16 b, 16 ~ b, 16 c 16 cs 16 d 16 | % kern m.38
      ds 16 e 16 \tuplet 3/2 { d 16 b, 32 d 16 c 32 } \tuplet 3/2 { f 16 ds 32 f 16 e 32 } | % kern m.39
      g 8 g, 8 \tuplet 3/2 { f, 16 e, 32 g, 16 f, 32 } | % kern m.40
      \tuplet 3/2 { e, 16 d, 32 f, 16 e, 32 } \tuplet 3/2 { c, 16 b,, 32 d, 16 c, 32 } \tuplet 3/2 { bf,, 16 a,, 32 c, 16 bf,, 32 } | % kern m.41
      a,, 16 a, 16 d, 16 d 16 f, 16 fs, 16 ~ | % kern m.42
      \tuplet 3/2 { fs, 16 fs, 32 a, 16 g, 32 } a, 16 bf, 16 ~ bf, 16 b, 16 ~ | % kern m.43
      b, 16 s 8. s8 | % kern m.44
      \tuplet 3/2 { <g, b,> 16 b, 32 d 16 c 32 } \tuplet 3/2 { c 16 b, 32 a, 16 gs, 32 ~ } \tuplet 3/2 { gs, 16 gs, 32 a, 16 b, 32 } | % kern m.45
      a, 16*2/3 ds 32*2/3 e 16 ~ e 16*2/3 ds 32*2/3 e 16 ~ e 16*2/3 ds 32*2/3 e 16 ~ | % kern m.46
      e 16*2/3 f 32*2/3 e 16 ~ e 16*2/3 f 32*2/3 e 16 ~ e 16*2/3 f 32*2/3 e 16 | % kern m.47
      <gs,, gs,> 16*2/3 <gs,, gs,> 32*2/3 <a,, a,> 16 ~ <a,, a,> 16*2/3 ( <a,, a,> 32*2/3 <b,, b,> 16 \tuplet 3/2 { ( <c, c> 16 ) <d, d> 32 <ds, ds> 16 <e, e> 32 ) } | % kern m.48
      \tuplet 3/2 { <e, e> 16 <e, e> 32 ~ <e, e> 16 <e, e> 32 ~ } \tuplet 3/2 { <e, e> 16 <a,, a,> 32 ~ <a,, a,> 16 <a,, a,> 32 ~ } \tuplet 3/2 { <a,, a,> 16 <g,, g,> 32 ~ <g,, g,> 16 <g,, g,> 32 } | % kern m.49
      \tuplet 3/2 { <g,, g,> 16 f' 32 e' 16 f' 32 } \tuplet 3/2 { f' 16 d' 32 c' 16 d' 32 } b 16 d' 16*2/3 c' 32*2/3 | % kern m.50
      \tuplet 3/2 { c' 16 e' 32 ds' 16 e' 32 } \tuplet 3/2 { e' 16 g' 32 fs' 16 g' 32 } \tuplet 3/2 { g' 16 g' 32 e' 16 fs' 32 } | % kern m.51
      \tuplet 3/2 { c' 16 a 32 c' 16 b 32 ~ } b 16*2/3 b 32*2/3 c' 16 \tuplet 3/2 { cs' 16 d' 32 f' 16 <d' f'> 32 } | % kern m.52
      \tuplet 3/2 { <g d' f'> 16 <g, g> 32 ( <a, a> 16 <b, b> 32 ) } \tuplet 3/2 { <c c'> 16 ( d 32 e 16 f 32 } \tuplet 3/2 { e 16 d 32 c 16 b, 32 ) } | % kern m.53
      \tuplet 3/2 { <g d' f'> 16 ( <g, g> 32 <a, a> 16 <b, b> 32 } \tuplet 3/2 { <c c'> 16 ) \clef "treble" b' 32 c'' 16 d'' 32 } s8 | % kern m.54
    }
    \new Voice = "lhII" {
      \voiceTwo
      s2 s16 | % kern m.36
      b, 16 g, 16 c 16 ~ c 8 c 16 s8. | % kern m.36+1
      \time 6/16 s4. | % kern m.36+2
      s4. | % kern m.37
      s4. | % kern m.38
      s4. | % kern m.39
      s4. | % kern m.40
      s4. | % kern m.41
      s4. | % kern m.42
      s 8 g, 8 ~ g, 16 g, 16 ~ | % kern m.43
      \tuplet 3/2 { g, 16 ( b, 32 d 16 e 32 } \tuplet 3/2 { f 16 e 32 d 16 c 32 ) } s8 | % kern m.44
      s4. | % kern m.45
      a, 16 ~ \tuplet 3/2 { a, 16 gs, 32 a, 16 ~ a, 32 } gs, 16 a, 16 ~ a, 16*2/3 gs, 32*2/3 | % kern m.46
      gs, 16 ~ gs, 16*2/3 a, 32*2/3 gs, 16 ~ gs, 16*2/3 a, 32*2/3 gs, 16 ~ gs, 16*2/3 gs, 32*2/3 | % kern m.47
      s4. | % kern m.48
      s4. | % kern m.49
      s 16 g 16 ~ g 8 ~ g 16 g 16 ~ | % kern m.50
      g 16 c' 16 ~ c' 16 c' 16 ~ c' 16 f 16 | % kern m.51
      \tuplet 3/2 { fs 16 a 32 fs 16 g 32 ~ } g 16 g 16 ~ g 16 g 16*2/3 g 32*2/3 | % kern m.52
      s4. | % kern m.53
      s4. | % kern m.54
    }
  >>
}

\score {
  \new PianoStaff <<
    \new Staff = "RH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \upper
    }
    \new Staff = "LH" {
      \set Staff.midiInstrument = "acoustic grand"
      \global
      \lower
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

---

## 四、三大变奏曲式类型学比较与结构功能

为清晰把握变奏曲式的演进脉络，三种范式在结构守恒、表层变量与审美维度上的差异可系统总结如下：

| 变奏类型 | 代表案例 | 核心守恒维度 | 主要自由变量 | 节奏动力学机制 | 核心审美与哲学追求 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **装饰性变奏** (*Verzierung*) | 莫扎特 K. 331 I (mm. 1–36) | 和声骨架、乐句长度、低音步调、基础节拍 | 旋律走势、经过音、辅助音、表面织体 | 装饰性音符加密（八分 $\to$ 十六分） | 古典对称之美、高雅修辞与手工艺精巧性 |
| **性格与复调变奏** (*Charakter*) | 贝多芬 Op. 109 III (mm. 1–64) | 宏观两段体、低音骨架核心级数 | 情感性格、演奏法（断/连）、织体形态、对位关系 | 速度/节拍表情重置、霍克特对位错位 | 戏剧人格面具裂变、复调深沉思辨与浪漫冲突 |
| **时值递减比例变奏** (*Diminution*) | 贝多芬 Op. 111 II (mm. 1–48) | 基础脉搏、三音核心动机、16小节和声矩阵 | 节拍等分比例（9/16 $\to$ 6/16 $\to$ 12/32）、音区两极分化 | 数学比例递减、微观时值持续倍增 | 物理时间意识坍缩、超验精神升华与宇宙秩序 |

### 变奏技法在室内乐与大型器乐中的写作法则
1. **骨架的多层级分离**：在构思变奏曲时，必须区分“核心骨架”（Skeletal Invariant）与“表层音型”（Surface Figuration）。变奏越激进，越依赖底层[《和声节奏》](../harmony/harmonic-rhythm-and-syntactic-pacing.md)与[《超拍与乐句节奏》](../rhythm/hypermeter-and-phrase-rhythm.md)的隐性锚定；
2. **性格极性的辩证布局**：单一段落的变奏不宜孤立设计，应形成如 Op. 109 那样“歌唱咏叹 $\to$ 轻盈碎裂断奏 $\to$ 严密赋格”的性格阶梯，使全套变奏构成一部宏大的心理交响；
3. **时间度量的结构性赋能**：善用古典对位法中的增减时值（Augmentation & Diminution）原理，通过拍号比例的先验转换，使变奏过程成为时间张力不断凝聚与最终释放的物理过程；
4. **主题回归的形而上闭环**：无论是 Op. 109 还是《哥德堡变奏曲》，在经历浩瀚的变奏奥德赛之后，原初主题的素颜重现（Da Capo）往往不再是简单的重复，而是在听众心理空间中激荡起历经沧桑后的终极顿悟；
5. **织体层次与声学动态控制**：变奏过程中切忌各声部音量与密度的均质化，应借助声部增减与音区拉伸（从极低音基石到超高音泛音圈），保持声学空间的通透度与层次感；
6. **宏观调性与色彩张力曲线**：长篇变奏套曲应合理设置同主音大小调对比（如 Minore）或对位中段，避免单一织体音型加密导致的感官钝化，维持全曲的长程戏剧张力。

结合[《定旋律变奏》](../counterpoint/cantus-firmus-variation-and-conversational-counterpoint.md)的复调平权法则与[《复合乐段》](compound-period-hierarchical-syntax.md)的句法展开，理解变奏曲式的这三大维度，正是洞察西方器乐音乐如何在有限材料中开辟无限精神疆域的钥匙。
