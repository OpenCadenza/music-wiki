<!-- music-kb:page {"id": "page.e73b7f33d1c2597699283c2345bf0955"} -->
<!-- knowledge: composer.beethoven.piano.op111-rhythm -->
# Op.111 Arietta：速度不变时的节奏缩减

检索词：Beethoven、Op.111、Arietta、Husarik、Buckley、L’istesso tempo、长短节律、音值细分。

Buckley 指出，第二乐章题为 Adagio molto，第二、第三变奏仍标 *L’istesso tempo*；加速感来自音值缩短，而非速度标记变化。她据此把终乐章听作慢乐章与终曲功能的融合：抒情连续性减弱变奏段落的割裂感，节奏细分则把它推向结尾（Buckley, pp. 120–121）。

Husarik 把 Arietta 开头辨认为下降的长—短两音头部动机，并指出草稿中也保持这一节律；他把 6/16 的第二变奏与 12/32 的第三变奏解释为更细的活动层级，使头部动机密集、切分地反复出现。Husarik 把反复计入连续小节编号；这些编号不能直接套入其他版本。按其编号，第四变奏从 m.129（Henle m.65）起撤去这种可辨节律；高颤音标在 m.170（文中 Henle m.106），其后 m.171 进入作者所称 cadenza，至 m.195（Henle m.130）的最终回归才重新听到主题形态（Husarik, pp. 282–285、291–294）。“消亡—复归”是其戏剧弧线解释，不是唯一形式结论。

### 原创节奏缩减练习

下例是新写的六音轮廓 G–F–E–D–C–D（先下降，末尾上行）。三次陈述都保留“较长音—较短音”的比例和音高轮廓，逐次压短时值；每行使用不同长度的拍号，以便直接看到比例变化。音高、节拍组合、旋律和布局均为本库原创。

<!-- opusloom:example {"id": "beethoven.model.op111-trochaic-diminution", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["husarik-op111-2020", "buckley-beethoven-slow-movements-2011"], "rights": "原创节奏迁移练习；不含贝多芬原作音符或现代版谱例编码。", "source_locator": "仅迁移 Husarik 对 Op. 111/II 主题长短头部节律及前三变奏细分的观察（PDF pp. 282–285）；Buckley 对不变速度与音值缩减推进的讨论（PDF pp. 120–121）。", "context": "三次原创六音轮廓陈述，依次以 dotted-quarter/eighth、dotted-eighth/sixteenth、dotted-sixteenth/thirty-second 构成长短对；仅练习比例性节奏缩减，不代表 Op. 111 的真实音符、拍号序列、和声或曲式。"} -->
```lilypond
\version "2.26.0"
\language "english"

\score {
  \new Staff {
    \clef treble
    \key c \major
    \absolute {
      \time 6/4
      g'4. f'8 e'4. d'8 c'4. d'8 |
      \time 3/4
      g'8. f'16 e'8. d'16 c'8. d'16 |
      \time 3/8
      g'16. f'32 e'16. d'32 c'16. d'32 |
    }
  }
  \layout { }
}
```

第 1 小节有三组长短对：G–F、E–D、C–D，分别写作附点四分音符加八分音符；每组两拍，合为 6/4。第 2 小节保持相同音高次序，把每组改为附点八分音符加十六分音符；三组共 3/4。第 3 小节继续按相同比例缩短为附点十六分音符加三十二分音符，三组共 3/8。

## 迁移与边界

练习重点是辨认长短比例和六音轮廓仍在，而不是把三小节误听为同一真实速度下的原作变奏。它没有低音与和弦，不能说明原作的和声支撑或终止。若把音符总时长变短当作乐曲实际加快，或把主题轮廓保留误当成原作所有和声支点不变，就超出了模型能证明的内容。

Buckley讨论速度标记与音值细分；Husarik讨论头部节律、编号与戏剧解释。两者提供不同层面的分析，不互相替代。

来源 ID：`husarik-op111-2020`、`buckley-beethoven-slow-movements-2011`。两项为在线选页实读，未成功缓存全文。谱例 ID `beethoven.model.op111-trochaic-diminution` 保持不变。
