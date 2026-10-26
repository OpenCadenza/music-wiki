<!-- music-kb:page {"id": "page.a45f2e0af55b5a9080d9c1578571e934"} -->
<!-- knowledge: composer.beethoven.songs-opera.text-melody-accompaniment -->
# 文本、旋律与伴奏：三种任务怎样分工

<!-- aliases: text setting, 词乐关系, prosody, 词重音, breath, 换气, accompaniment, 伴奏, Lied, Fidelio, recitative, 重唱 -->

声乐写作同时受语义、语法分句、词重音、音节可唱性、旋律、和声与伴奏约束。文字不是外加歌词；它决定呼吸和重音，却也不要求每个词由一枚音符直译。写作时先问：句子的主要动作落在哪个音区，关键词出现时伴奏变稀还是变密，句尾由歌者、器乐还是停顿接管。

Op.98 的证据来自 Dunlop 对六首歌、跨歌回返和钢琴伴奏的讨论。Fidelio 的证据来自 Met 对家庭场景、囚徒合唱与四重唱的导听，以及 Hastings 对莱奥诺拉咏叹调歌唱难点的录音比较。前者可支持套曲回返与伴奏关系，后两者可支持选定场景和声部实现；它们都不足以承担全剧逐号分析。

## 原创模型

模型使用原创德语短句：钢琴先奏一小节前奏，歌者随后进入，末句共同收束。它不含《致远方的爱人》或《费黛里奥》的旋律、歌词、谱例或音频。

<!-- opusloom:example {"id": "beethoven.model.lied-text-and-accompaniment", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["dunlop-an-die-ferne-geliebte-2024", "hastings-fidelio-leonore-2022", "met-fidelio-in-focus-2025"], "rights": "原创教学模型；不含《致远方的爱人》或《费黛里奥》的旋律、歌词、谱例或音频。", "source_locator": "模型仅演示钢琴前奏、歌者进入和末句共同收束三种新写操作。历史观察分别参考 Dunlop 对 Op.98 歌唱线/伴奏的论述、Hastings 对莱奥诺拉咏叹调歌唱要求的研究、Met 对囚徒合唱/重唱的场景导听。", "context": "原创德语短句与键盘模型：钢琴先奏一小节前奏，歌者随后进入，末句共同收束。不是贝多芬原作、引文或风格复原。"} -->
```lilypond
\version "2.26.0"
\language "english"
melody = {
  \key g \major \time 3/4
  R2. | g'4 a' b' | c''4 b' a' | d''4 c'' b' | a'8-> g' g'2-> |
}
words = \lyricmode {
  Mor -- gen -- licht, tra -- ge mich, lei -- se fort, weit hi -- naus.
}
right = {
  \key g \major \time 3/4
  <g b d'>2. | <g b d'>2 r4 | <c' e' g'>2 r4 |
  <d' fs' a'>2 r4 | <g b d'>2. |
}
left = {
  \key g \major \time 3/4
  g,2 d4 | g,2 d4 | c2 g4 | d2 a4 | g,2 g,4 |
}
\score {
  <<
    \new Staff << \new Voice = "singer" { \melody } >>
    \new Lyrics \lyricsto "singer" { \words }
    \new PianoStaff << \new Staff { \right } \new Staff { \clef bass \left } >>
  >>
  \layout { }
}
```

第 1 小节是钢琴前奏；第 2 小节歌者在 G4 进入，唱 G–A–B，对应“Mor / gen / licht”。第 3 小节 C5–B4–A4 对应“tra / ge / mich”；第 4 小节 D5–C5–B4 对应“lei / se / fort”。这些词的词首重读位于各小节第一拍。第 5 小节 A4、G4 八分音符对应“weit / hi”，随后 G4 二分音符对应“naus”，以时值和显式重音强调末音节。共十二个歌词起音；末句改变时值支持词重音，不能按音节数机械填四分音符。

歌者实际音域为 G4–D5，钢琴低音为 G2–A3。模型采用绝对音高，避免相对记谱中的意外八度漂移。末小节歌者与钢琴共同落到 G 大调音响，只作为本模型收束，不声称复制贝多芬的终止。

## 实际写作步骤

1. 先标出词义、重读、语法停顿与呼吸位置，再试唱；不要先用器乐动机填满音节。
2. 为每句指定一个主要旋律动作和一个伴奏动作，确认两者互补。
3. 若钢琴总与歌者同节奏同音高，文本清晰度和层次通常会下降；若伴奏持续复杂，歌者难以呼吸和传词。
4. 多角色场景先区分音区、发声节奏和句子长度，再安排重唱交叠。合唱加入时要说明它是群众、叙述者还是对照层。
5. 历史例登记作品版本、人物/声部、场景或歌曲、小节和文本出处。音像比较只支持具体表演观察。

这套模型不覆盖 Fidelio 的宣叙调、重唱和乐队动机，也不证明 Dunlop 的踏板选择具有唯一性。真实声乐编配还须检查歌者换气、辅音密集区和乐队遮蔽。
