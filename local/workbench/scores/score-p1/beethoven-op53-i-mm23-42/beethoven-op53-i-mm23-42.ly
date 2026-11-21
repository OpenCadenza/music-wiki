\version "2.26.0"
\language "english"

#(set-global-staff-size 18)

% ============================================================================
% 贝多芬 第21钢琴奏鸣曲 Op.53「Waldstein」第一乐章
% Allegro con brio，mm.23–42（B 大调属准备 → 16 分音型 → 八分对置层 → E 大调副题进入与第一乐句收束）
%
% 底本：local/resources/scores/source-packages/beethoven-score-sources/
%       beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata21-1.krn
%       （MuseData 转写 **kern；!!!OPS 53 / !!!OTP Waldstein / *M4/4 / *MM144）
%
% 记谱口径（详见同目录 核对记录.md）：
%   1. 按底本实际音高直录。**调号照底本：全乐章 *k[] 不换调号**，故 B 大调/E 大调段落
%      的升号全部以临时记号写出 —— 这是底本（及原谱）的实际写法，不是本交付的简化。
%   2. 谱号逐处照录：右手 m.30 低音谱号（下行至 B2）、m.31 起高音；
%      左手 m.35–36 高音谱号、m.37 低音、m.38 高音、m.39 起低音。
%   3. 连音线（kern '[' / ']'）照录：m.23 的 B5 四分延音入十六分。
%   4. 圆滑线（kern '(' / ')'）未转译，与 R301 口径一致；底本在 mm.35–41 有成对乐句线
%      （m.35→m.36、m.37→m.38、m.39→m.40、m.41 内），本交付未画出。
%   5. m.38、m.41 底本用 *^ 分成两层（长音＋移动声部），按两聲部排版：
%      m.38 右手 E5+G♯5 / D♯5+F♯5 ＋ B4 附点二分 → A4；左手 E4+G♯4 / D♯4+F♯4 ＋ B3 全音符。
%      m.41 左手 E3+G♯3 四分 → F♯3+A3 附点二分 ＋ B1+B2 全音符（属持续音）。
%   6. m.42 底本用 *Xtuplet 的 12 分音符（= 三连八分），按 4 组 \tuplet 3/2 排版；
%      首组第一个音是和弦 G♯3+E4（底本同记录内两个 token）。
%   7. 速度 4=144 出自底本 *MM144；m.35 的 "dolce e molto legato" 是底本
%      !LO:TX 文本记号，照录为 markup。
% ============================================================================

global = {
  \key c \major
  \time 4/4
  \tempo "Allegro con brio" 4 = 144
}

upper = {
  \global
  \clef treble
  % m.23  B5 四分延音入十六分：B 大调主和弦琶音（B2-D♯3-F♯3-B3）
  b''4 ~ b''16 a''16 g''16 fs''16 g''16 fs''16 e''16 ds''16 e''16 g''16 fs''16 e''16 |
  % m.24  换 B7 外壳（F♯-A）与 E 小三和弦，十六分音阶上行
  ds''16 cs''16 b'16 as'16 b'16 cs''16 d''16 ds''16 e''16 ds''16 e''16 fs''16 g''16 gs''16 a''16 as''16 |
  % m.25  同 m.23 音型（B 大调）
  b''16 as''16 b''16 as''16 b''16 a''16 g''16 fs''16 g''16 fs''16 e''16 ds''16 e''16 g''16 fs''16 e''16 |
  % m.26  同 m.24 音型
  ds''16 cs''16 b'16 as'16 b'16 cs''16 d''16 ds''16 e''16 ds''16 e''16 fs''16 g''16 gs''16 a''16 as''16 |
  % m.27  右手与左手交换音型：B5-D♯5-B4 / A♯5-B5-E5-G5
  b''16 fs''16 ds''16 b'16 as'16 b'16 e''16 g''16 b''16 fs''16 ds''16 b'16 as'16 b'16 e''16 g''16 |
  % m.28  每拍重音 sf（底本四个 sf）
  b''16 fs''16 ds''16 b'16 b''16 g''16 e''16 b'16 b''16 fs''16 ds''16 b'16 b''16 g''16 e''16 b'16 |
  % m.29  十六分琶音继续下行到 B3；左手改为四分和弦并转入休止（属准备收束）
  b''16 fs''16 ds''16 b'16 fs''16 ds''16 b'16 fs'16 ds''16 b'16 fs'16 ds'16 b'16 fs'16 ds'16 b16 |
  % m.30  下行至 B2（底本此处右手换低音谱号），末拍四十六分琶音交给左手
  \clef bass
  fs'16 ds'16 b16 fs16 ds'16 b16 fs16 ds16 b16 fs16 ds16 b,16 r4 |
  \clef treble
  % m.31  B 大调八分对置层起：左手 B1-B2-C♯2-C♯3-D♯2-D♯3，右手 B4-B3-C♯5-C♯4
  r2 b'8 b8 cs''8 cs'8 |
  % m.32  左手 D♯2-D♯3-E2-E3-F♯2-F♯3；右手 D♯5-D♯4（首拍）与 E5-E4（末拍）
  ds''8 ds'8 r4 ds''8 ds'8 e''8 e'8 |
  % m.33  递增：F♯5-F♯4 / G♯5-G♯4 / A5-A4 / A5-B4
  fs''8 fs'8 gs''8 gs'8 a''8 a'8 a''8 b'8 |
  % m.34  A5 持续音上：C♯5-D♯5-E5-F♯5
  a''8 cs''8 a''8 ds''8 a''8 e''8 a''8 fs''8 |
  % m.35  E 大调副题进入（底本 "dolce e molto legato"）：B4+E5+G♯5 → A4+D♯5+F♯5 → G♯4+C♯5+E5
  <b' e'' gs''>2^\markup { \italic "dolce e molto legato" }
  <a' ds'' fs''>4 <gs' cs'' e''>4 |
  % m.36  F♯4+B♯4+D♯5 → E4+C♯5
  <fs' bs' ds''>2 <e' cs''>2 |
  % m.37  A4+B4+D♯5 → B4+E5 → C♯5+E5+F♯5（底本 B 带 courtesy natural，此处强制 '!'）
  <a' b'! ds''>2 <b' e''>4 <cs'' e'' fs''>4 |
  % m.38  两层：E5+G♯5 / D♯5+F♯5 半音符 ＋ B4 附点二分 → A4 四分
  << { <e'' gs''>2 <ds'' fs''>2 } \\ { b'2. a'4 } >> |
  % m.39  B3+E4+G♯4 → A3+D♯4+F♯4 → G♯3+C♯4+E4（与 m.35 同型下移三度）
  <b e' gs'>2 <a ds' fs'>4 <gs cs' e'>4 |
  % m.40  D♯3+F♯3+B♯3+D♯4 → E3+A3+C♯4
  <ds fs bs ds'>2 <e a cs'>2 |
  % m.41  右手 B3 → C♯4 → D♯4（左手 B1+B2 属持续音下，见 lower）
  b2 cs'4 ds'4 |
  % m.42  十二分音符（三连八分）四组：首组首音为和弦 G♯3+E4，其后升序至 F♯♯5
  \tuplet 3/2 { <gs e'>8 fs'8 gs'8 } \tuplet 3/2 { a'8 b'8 cs''8 }
  \tuplet 3/2 { d''8 ds''8 e''8 } \tuplet 3/2 { es''8 fs''8 fss''8 } |
}

lower = {
  \global
  \clef bass
  % m.23  B 大调属准备：B2-D♯3-F♯3-B3 与 B2-E3-G3-B3 两种十六分琶音交替
  b,16\p ds16 fs16 b16 b,16 ds16 fs16 b16 b,16 e16 g16 b16 b,16 e16 g16 b16 |
  % m.24  B7 外壳（F♯-A）与 E 小三和弦
  b,16 fs16 a16 b16 b,16 fs16 a16 b16 b,16 e16 g16 b16 b,16 e16 g16 b16 |
  % m.25  同 m.23
  b,16 ds16 fs16 b16 b,16 ds16 fs16 b16 b,16 e16 g16 b16 b,16 e16 g16 b16 |
  % m.26  同 m.24
  b,16 fs16 a16 b16 b,16 fs16 a16 b16 b,16 e16 g16 b16 b,16 e16 g16 b16 |
  % m.27  渐强起点（底本 m.27 起 '<'）
  b,16\< ds16 fs16 b16 as16 b16 g16 e16 b,16 ds16 fs16 b16 as16 b16 g16 e16 |
  % m.28  f 起，每拍重音 sf（底本四组）
  b,16\f ds16 fs16 b16 b,16\sf e16 g16 b16 b,16\sf ds16 fs16 b16 b,16\sf e16 g16 b16 |
  % m.29  四分和弦 B2+D♯3+F♯3+B3，其后全休止
  <b, ds fs b>4 r4 r2 |
  % m.30  末拍交给左手：B1-D♯2-F♯2-B2 十六分琶音
  r2 r4 b,,16 ds,16 fs,16 b,16 |
  % m.31  八分对置层：左手低八度 B1-B2-C♯2-C♯3-D♯2-D♯3（渐弱起）
  b,,8\> b,8 cs,8 cs8 ds,8 ds8 r4 |
  % m.32  D♯2-D♯3-E2-E3-F♯2-F♯3
  ds,8 ds8 e,8 e8 fs,8 fs8 r4 |
  % m.33  F♯2-F♯3-G♯2-G♯3（底本 m.33 重新标 p，收束 m.31 起的渐弱）
  r2\p fs,8 fs8 gs,8 gs8 |
  % m.34  A2-A3-B2-B3-C♯3-C♯4-D♯3-D♯4
  a,8 a8 b,8 b8 cs8 cs'8 ds8 ds'8 |
  % m.35  副题左手上声部：E4+G♯4 → B3+D♯4+F♯4 → C♯4+E4（此两小节底本换高音谱号）
  \clef treble
  <e' gs'>2 <b ds' fs'>4 <cs' e'>4 |
  % m.36  G♯3+B♯3+D♯4 → A3+C♯4
  <gs bs ds'>2 <a cs'>2 |
  % m.37  回低音谱号：F♯3+A3+B3+D♯4 → G♯3+B3+E4 → A3+C♯4+F♯4
  \clef bass
  <fs a b ds'>2 <gs b e'>4 <a cs' fs'>4 |
  % m.38  换高音谱号，两层：E4+G♯4 / D♯4+F♯4 半音符 ＋ B3 全音符；sf 起渐弱
  \clef treble
  << { <e' gs'>2\sf\> <ds' fs'>2\! } \\ { b1 } >> |
  % m.39  回低音谱号（与 m.35 同型下移三度）：E3+G♯3 → B2+D♯3+F♯3 → C♯3+E3
  \clef bass
  <e gs>2\p <b, ds fs>4 <cs e>4 |
  % m.40  G♯2+B♯2 → A2+C♯3
  <gs, bs,>2 <a, cs>2 |
  % m.41  两层：E3+G♯3 四分 → F♯3+A3 附点二分 ＋ B1+B2 全音符属持续音
  << { <e gs>4 <fs a>2. } \\ { <b,, b,>1 } >> |
  % m.42  E2+E3 八分属和弦起句，余两拍半休止
  <e, e>4\p r4 r2 |
}

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      \upper
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % 力度统一画在下谱表下方（避免低音区挤到两谱表之间，位置忽上忽下）
      \override DynamicLineSpanner.direction = #DOWN
      \lower
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
