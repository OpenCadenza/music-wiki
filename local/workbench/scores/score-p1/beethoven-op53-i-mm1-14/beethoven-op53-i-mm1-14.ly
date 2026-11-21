\version "2.26.0"
\language "english"

#(set-global-staff-size 18)

% ============================================================================
% 贝多芬 第21钢琴奏鸣曲 Op.53「Waldstein」第一乐章
% Allegro con brio，mm.1–14（主部 + 下方大二度模进 + 半音下行低音 + 半音准备）
%
% 底本：local/resources/scores/source-packages/beethoven-score-sources/
%       beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata21-1.krn
%       （MuseData 转写 **kern，均分岭谱集；!!!OPS 53 / !!!OTP Waldstein /
%         *M4/4 / *MM144 / *k[] 全乐章不换调号）
%
% 记谱口径（详见同目录 核对记录.md）：
%   1. 一律按底本实际音高直录，不作移调、不改八度；底本 mm.1–3 右手写在低音谱号，
%      m.4 起换高音谱号，m.5–7 又回低音谱号，m.8 起高音谱号 —— 谱号逐处照录
%      （kern 行 51 / 64 / 94 的 `*clef`，均在小节末、对下一小节生效）。
%   2. 连音线（kern '[' / ']'）照录为 '~'：m.4 的 D6、m.8 的 C6、m.11 的 G 八度。
%   3. 圆滑线（kern '(' / ')'）**全部照录**，共 6 条（均在单声部内、无跨 Voice 问题）：
%      m.3 附点和弦→八分 G；m.4 D6→G5（与连音线并存）；m.7 同 m.3；m.8 C6→F5；
%      m.9 倚音 E6→附点二分 F6；m.11 左手 G 八度八分→m.12 的 C4（跨小节）。
%   4. 装饰音（kern '8q…'）记作 \grace 十六分；m.4/m.8/m.9 的装饰音分别为
%      C♯6→D6、B♮5→C6、E6→F6（均为下方半音倚音）。
%   5. 力度与速度照录：m.1/5 pp、m.9 渐强、m.11 f、m.12 渐弱、m.13 p、m.14 pp；
%      速度 4=144 出自底本 *MM144，非推定值。
%   6. 底本 courtesy natural（kern '…n'）只在 m.14 第一音强制打印还原号 '!'，
%      以还原 m.12 的 E♭；其余 courtesy natural 不强制打印（C 大调调号下本不需要）。
% ============================================================================

global = {
  \key c \major
  \time 4/4
  \tempo "Allegro con brio" 4 = 144
}

upper = {
  \global
  \clef bass
  % m.1  右手写在低音谱号：C3+E3 的反复八分和弦（首拍右手休止，左手单音 C2 起拍）
  r8 <c e>8 <c e>8 <c e>8 <c e>8 <c e>8 <c e>8 <c e>8 |
  % m.2  第六拍后换 D3+F♯3，为 m.3 的 G 作导音准备
  <c e>8 <c e>8 <c e>8 <c e>8 <c e>8 <c e>8 <d fs>8 <d fs>8 |
  % m.3  G/B：附点四分和弦 → 十六分经过音 B-A → 八分 G 收束
  <d g>4.( b16 a16 g8) r8 r4 |
  % m.4  花彩：装饰 C♯6 → D6（延音入十六分）→ 十六分下行 C6-B♭5-A5 → 四分 G5
  \clef treble
  \grace { cs'''16 } d'''4 ~( d'''16 c'''16 b''16 a''16 g''4) r4 |
  % m.5  B♭ 大调（对 m.1 作下方大二度模进）：B♭2+D3。底本 m.4 末 `*clefF4` ⇒ 右手 m.5–7 回低音谱号
  \clef bass
  <bf, d>8 <bf, d>8 <bf, d>8 <bf, d>8 <bf, d>8 <bf, d>8 <bf, d>8 <bf, d>8 |
  % m.6  末两拍换 C3+E3
  <bf, d>8 <bf, d>8 <bf, d>8 <bf, d>8 <bf, d>8 <bf, d>8 <c e>8 <c e>8 |
  % m.7  F/A：附点四分和弦 → 十六分 A-G → 八分 F 收束（与 m.3 同型）；底本 m.7 起渐强
  <c f>4.( a16 g16 f8) r8 r4 |
  % m.8  花彩（与 m.4 同型，下移大二度）：装饰 B♮5 → C6 延音 → 下行至 F5。
  %      底本 m.7 末 `*clefG2` ⇒ 右手 m.8 起回高音谱号
  \clef treble
  \grace { b''16 } c'''4 ~( c'''16 bf''16 af''16 g''16 f''4) r4 |
  % m.9  高点：装饰 E6 → 附点二分 F6，末拍十六分下行 F6-E♭6-D6-C6
  \grace { e'''16( } f'''2.) f'''16 ef'''16 d'''16 c'''16 |
  % m.10 十六分音型两次上行（B♭5 起，至 F6 折回）
  b''16 c'''16 d'''16 ef'''16 f'''16 ef'''16 d'''16 c'''16
  b''16 c'''16 d'''16 ef'''16 f'''16 ef'''16 d'''16 c'''16 |
  % m.11 连续十六分下行至 B4，与 m.12 的 C5 接续（半音准备）
  b''16 c'''16 d'''16 ef'''16 f'''16 ef'''16 d'''16 c'''16
  b''16 af''16 g''16 f''16 ef''16 d''16 c''16 b'16 |
  % m.12 与左手同步的八分柱式和弦（C5-G4-E♭4-C4 下行）
  c''8 r8 g'8 r8 ef'8 r8 c'8 r8 |
  % m.13 G 上的延长（与左手 G1+G2 合成三个八度的 G）
  g1\fermata |
  % m.14 新句：E4-C4 十六分交替（首音强制还原号，还原 m.12 的 E♭）
  e'!16 c'16 e'16 c'16 e'16 c'16 e'16 c'16 e'16 c'16 e'16 c'16 e'16 c'16 e'16 c'16 |
}

lower = {
  \global
  \clef bass
  % m.1  首拍单音 C2，其后 C2+G2 反复八分
  c,8\pp <c, g,>8 <c, g,>8 <c, g,>8 <c, g,>8 <c, g,>8 <c, g,>8 <c, g,>8 |
  % m.2  末两拍 G2→A2
  <c, g,>8 <c, g,>8 <c, g,>8 <c, g,>8 <c, g,>8 <c, g,>8 <c, a,>8 <c, a,>8 |
  % m.3  低音半音下行 C2→B1，上声部保持 G2
  <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 |
  % m.4  B1+G2 保持
  <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 <b,, g,>8 |
  % m.5  低音继续下行 B1→B♭1，上声部 G2→F2
  <bf,, f,>8\pp <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 |
  % m.6  末两拍 F2→G2
  <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 <bf,, f,>8 <bf,, g,>8 <bf,, g,>8 |
  % m.7  A1+F2（F 大调第一转位）；底本自 m.7 起渐强（m.7 的 '<' 与 '['、m.9 的 '<' 三段连写）
  <a,, f,>8\< <a,, f,>8 <a,, f,>8 <a,, f,>8 <a,, f,>8 <a,, f,>8 <a,, f,>8 <a,, f,>8 |
  % m.8  A♭1+F2
  <af,, f,>8 <af,, f,>8 <af,, f,>8 <af,, f,>8 <af,, f,>8 <af,, f,>8 <af,, f,>8 <af,, f,>8 |
  % m.9  G1+F2（属七外壳），末两拍 A♭1+F2；渐强延续（底本 m.9 的 '<'）
  <g,, f,>8 <g,, f,>8 <g,, f,>8 <g,, f,>8 <g,, f,>8 <g,, f,>8 <af,, f,>8 <af,, f,>8 |
  % m.10 G/A♭ 交替
  <g,, f,>8 <g,, f,>8 <af,, f,>8 <af,, f,>8 <g,, f,>8 <g,, f,>8 <af,, f,>8 <af,, f,>8 |
  % m.11 四分 G1+F2 → 二分 G2+G3（延音入八分）→ 十六分 A3-B3 接到 m.12 的 C4
  <g,, f,>4\f <g, g>2 ~ <g, g>8( a16 b16 |
  % m.12 八分柱式和弦下行：C4 / G2+G3 / E♭2+E♭3 / C2+C3，每拍后半为休止
  c'8) r8 <g, g>8 r8\> <ef, ef>8 r8 <c, c>8 r8 |
  % m.13 G1+G2 延长（与右手 G3 合成三个八度）
  <g,, g,>1\fermata\p |
  % m.14 C2+C3 八分起句，其后 C3-G3 十六分交替
  <c, c>8\pp c16 g16 c16 g16 c16 g16 c16 g16 c16 g16 c16 g16 c16 g16 |
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
