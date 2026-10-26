<!-- music-kb:page {"id": "page.c82aeb01ea715822abad6bae39bec525"} -->
<!-- knowledge: composer.beethoven.chamber.quartet.op133-held-note -->
# Op.133：保留音怎样因和弦变化取得新意义

<!-- aliases: Beethoven Grosse Fuge Op.133, held note, recontextualization, suspension, harmonic conflict, 贝多芬大赋格, 保留音, 和弦重释, 冲突音, 上行解决 -->

## 创作问题

一个线性音高如果跨过和弦或低音变化，它何时从和弦音变成冲突音，随后又怎样获得可听的解决？

## 来源与定位

第二种操作是让一个线性音高在和弦变化后取得新的垂直意义。Ormesher 以 Op. 133 第350小节中提琴的 C 为例：这个有节奏重音的音可被听作与降D大调周围和声冲突的预先音，三小节后上行解决；他把这种效果追溯到《序曲》中因休止而不易察觉的第二拍主题起音（《Instrumental Fugal Style》，印刷 p.168）。同一论文把全曲按其连续编号分作 Overtura、三段赋格及同音节奏的 scherzo 段，并指出主题与对题的对比从 Fugue I 到 III 逐渐减弱（pp.163、248–250）。这是 Ormesher 的组织模型，不是每个版本都印出的分部，也不意味着所有切分音都具有和声功能。迁移这一步时，必须逐项核对音符进入拍位、当时低音/和弦、后续解决；若和弦未改变或没有明确解决，只能称重音或切分，不应升格为结构性预示。

Op. 130/133 则提醒分析者先区分“作品终曲”和“单独赋格”。Ormesher 记述《大赋格》最初作为 Op. 130 终乐章，后由另一终曲替换；他认为两种结尾各有结构代价，没有完全令人满意的“哪一个才正确”的答案（pp.151–154）。所以讨论 Op. 130 的六乐章弧线时，须先说明使用原始大赋格还是替换终曲；讨论 Op. 133 时，则可把音型、切分、调性冲突和分部比例当作独立作品的问题，而不要将它无说明地并入 Op. 130 的既定终曲。

## 谱例

下例是新写的降E大调四声部小练习。它不转录 Op. 133，也不复制论文中的现代谱例编码。第一拍的降B大三和弦提供属和弦背景；第二拍上声部 D5 是和弦音，低音在第三拍转到降E后，D5 被重新听成主和弦上的大七度，持续到第四拍再上行半音解决为降E5。模型只示范“线性保留音因低音/和声变化而改变垂直功能”，不声称模拟 Op. 133 第350小节的实际音符、时值、织体或调性。

<!-- opusloom:example {"id": "beethoven.model.late-quartet-recontextualized-held-note", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["ormesher-fugues-1989"], "rights": "原创降E大调四声部教学练习；不转录、改编或模仿贝多芬原谱及现代版谱例。", "source_locator": "只迁移 Ormesher 对 Op.133/III m.350 中提琴 C 在降D大调和声中形成预先冲突、随后上行解决的分析问题（印刷 p.168）；本例改用新音高与新织体。", "context": "一小节 4/4：降B大三和弦移向降E大调主和弦；D5 跨越低音/和弦变化，从属和弦三音转为主和弦大七度，并上行半音至降E5。用于检查保留音如何改变和弦角色，不是原作片段或作品形式缩影。"} -->
```lilypond
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Vln. I" } {
      \key ef \major \time 4/4
      r4 d''2 ef''4 |
    }
    \new Staff \with { instrumentName = "Vln. II" } {
      \key ef \major \time 4/4
      f'2 g'2 |
    }
    \new Staff \with { instrumentName = "Vla." } {
      \clef alto \key ef \major \time 4/4
      d'2 bf2 |
    }
    \new Staff \with { instrumentName = "Vc." } {
      \clef bass \key ef \major \time 4/4
      bf,2 ef,2 |
    }
  >>
  \layout { }
}
```

## 逐拍解释

**逐小节核对。** 这是一小节。第1–2拍，低音 B♭2、中提琴 D4、第二小提琴 F4 构成 B♭大三和弦；第一小提琴休止后在第2拍进入 D5，仍是该属和弦的三音。第3拍低音转 E♭2，第二小提琴升至 G4、中提琴降至 B♭3，明确给出 E♭大调主和弦框架。第一小提琴 D5 仍延续到第3拍，因而相对 E♭根音成为大七度；第4拍它上行半音至 E♭5，完成局部解决。不要把这一个小节称为贝多芬的原作终止，也不要把“大七度上行”泛化为固定风格规则；若低音未转、或 D5 没有延续到新和弦上，模型的关键重新解释就消失。

## 迁移方法

先写一个保留音，再让低音或和弦在保留期间改变，使同一音高取得新的垂直角色；解决音必须由新和弦的方向支持。记录进入拍位、原和弦、改变时点、冲突音级和解决音五项。

## 来源与边界

**来源边界。** Bourne 的“讽刺”来自对期待偏离的解释框架；Barry 的全曲“teleology”是具名分析模型；Ormesher 的 Op. 133 分部及主题—和声解释有具体编号，但依赖其版本与连续计数。三者可互相比较，不能合并成一份已证明的作曲意图报告。

来源 ID：`ormesher-fugues-1989`。Op.133 第350小节的实际音高、声部与版本由该文定位；本模型只迁移问题，不复刻原作。
