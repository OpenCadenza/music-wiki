# 研究归档：增六和弦

- **学者**：scholar-a2（原创），scholar-a3（续作对齐）
- **选题**：增六和弦（Augmented-Sixth Chords）
- **中心论证**：批判将增六和弦按地理标签（意大利、法国、德国、瑞士）机械割裂的传统教学法，立足对位物理学揭示其本质为外声部“反向半音向心钳夹（Inward/Outward Symmetrical Voice-Leading Wedge）”——低音降六音（le）向下与上音声部升四音（fi）向上，以严苛的增六度张力双向收束于属音八度；四大变体的分化源自内声部填充所决定的声学密度与微积分（意六纯骨架双主音、法六超主音注入全音阶对称双三全音、德六降中音垂直与属七等音但引发莫扎特五度危机并依赖终止四六和弦、瑞六大调对位自洽）；实证考察其在古典乐派中作为前属功能（Predominant / [S6]）终极加压制动器的规范运用（莫扎特 K. 465 IV 阶梯式加压、贝多芬 Op. 109 III 沉思中的半音高压突进）；最终揭示浪漫主义时期（舒伯特 D. 960 I）如何利用德六和弦与属七和弦在十二平均律中的绝对声学等同性，发生深刻的“语法漂移”，将其由局部前属跳板异化为跨越半音远关系调性的“等音转调虫洞枢纽（Enharmonic Pivot）”。
- **状态**：`已完成第一波审查与对齐（H1 短标题、副标题、frontmatter、无行号与伪路径、消除内部代号、统一小节口径、压平谱例占位、补齐 provenance 表）`

---

## 1. 实际采用的资料范围

- **Open Music Theory (OMT) 教学文献源码（工作树真实存在）**：
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/alteredSubdominants.md`（变化下属和弦体系、那不勒斯和弦、意/法/德/瑞增六和弦构成、功能低音 [S6] 标记、莫扎特五度规避与终止四六和弦衔接）；
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/harmonicFunctions.md` 与 `harmonicSyntax1.md`（T-S-D-T 功能等级与和声语法模型）；
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/cadenceTypes.md`（正格终止与半终止的和声动力学要求）；
- **实证总谱研读**：
  * 沃尔夫冈·阿玛多伊斯·莫扎特《C大调第19弦乐四重奏“不协和”》K. 465 第四乐章（Allegro molto，mm. 10–16；此处遵循 OpenScore 与 OMT 零基记谱口径，即弱起小节计为 m. 0，对应传统印本 mm. 11–17：m. 13 自然下属 IV6，m. 14 第 2 拍爆发法国六和弦 Fr.，mm. 15–16 经 Cad6/4 达成完全正格终止 PAC）；
  * 路德维希·凡·贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章（Andante molto cantabile ed espressivo，mm. 1–8：如歌萨拉班德变奏主题，m. 7 拍尾至 m. 8 拍头引入德国六和弦 Ger. 强力加压，释放于半终止 HC；经查工作树内 `local/resources/scores/source-packages/beethoven-score-sources/.../kern/sonata30-3.krn` 真实存在并逐音核实一致）；
  * 弗朗茨·舒伯特《降B大调第21钢琴奏鸣曲》D. 960 第一乐章（Molto moderato，mm. 18–48，本工作树无数字谱副本：主部主题呈示与神秘低音震音，德六和弦向属七和弦的等音重拼与半音大三度远关系调区跃迁）；
- **引证与推论纪律说明**：
  * 本文严格立足于上述实际阅读的 OMT 章节与实证总谱，严禁虚构文献页码与行号；
  * 增六和弦的四大形态构成、声部导向与功能低音标记严格依据 OMT 体系；
  * 关于外声部“反向半音向心钳夹”的物理力学模型、声学色彩微积分以及等音转调枢纽的语法漂移分析，在正文中明确注明为笔者的归纳推导。

---

## 2. 谱例与占位现状

1. **莫扎特《C大调第19弦乐四重奏“不协和”》K. 465，第四乐章 Allegro molto，mm. 10–16**
   - 谱例 id：`mozart-k465-iv-mm10-16`
   - 定位：`Allegro，mm.10–16`
   - 现况：已完成自包含 LilyPond 围栏嵌入并校验通过。小节编号口径说明已写入正文。
2. **贝多芬《E大调第30钢琴奏鸣曲》Op. 109，第三乐章 Andante molto cantabile ed espressivo，mm. 1–8**
   - 谱例 id：`beethoven-op109-iii-mm1-8`
   - 定位：`Andante molto cantabile ed espressivo，mm.1–8`
   - 现况：已完成自包含 LilyPond 围栏嵌入并校验通过。
3. **舒伯特《降B大调第21钢琴奏鸣曲》D. 960，第一乐章 Molto moderato，mm. 18–48**
   - 现况：正文已压为单行纯文本占位（`舒伯特《降B大调第21钢琴奏鸣曲》D. 960 第一乐章 Molto moderato，mm. 18–48`），无 GM 编号与内部交付状态。待后续有可靠数字化谱源再行增补。

---

## 3. 待解决缺口与后续

- 正文内跨篇引用已规范为短标题链接，消除对内部角色代号 `scholar-b2` 的提及；
- K. 465 小节编号口径（零基计法 vs 传统印本）已在正文中阐明，避免歧义；
- 舒伯特 D. 960 待后续获取高质数字化谱源后再评估制作独立谱例。
