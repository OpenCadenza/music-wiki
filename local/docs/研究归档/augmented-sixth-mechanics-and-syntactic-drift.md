# 研究归档：增六和弦的力学本质与语法漂移：从古典半音下属加压到浪漫等音枢纽

- **学者**：scholar-a2
- **选题**：增六和弦的力学本质与语法漂移：从古典半音下属加压到浪漫等音枢纽（The Mechanics and Syntactic Drift of Augmented-Sixth Chords: From Classical Chromatic Subdominant Pressurization to Romantic Enharmonic Pivots）
- **中心论证**：批判将增六和弦按地理标签（意大利、法国、德国、瑞士）机械割裂的传统教学法，立足对位物理学揭示其本质为外声部“反向半音向心钳夹（Inward/Outward Symmetrical Voice-Leading Wedge）”——低音降六音（le）向下与上音声部升四音（fi）向上，以严苛的增六度张力双向收束于属音八度；四大变体的分化源自内声部填充所决定的声学密度与微积分（意六纯骨架双主音、法六超主音注入全音阶对称双三全音、德六降中音垂直与属七等音但引发莫扎特五度危机并依赖终止四六和弦、瑞六大调对位自洽）；实证考察其在古典乐派中作为前属功能（Predominant / [S6]）终极加压制动器的规范运用（莫扎特 K. 465 IV 阶梯式加压、贝多芬 Op. 109 III 沉思中的半音高压突进）；最终揭示浪漫主义时期（舒伯特 D. 960 I）如何利用德六和弦与属七和弦在十二平均律中的绝对声学等同性，发生深刻的“语法漂移”，将其由局部前属跳板异化为跨越半音远关系调性的“等音转调虫洞枢纽（Enharmonic Pivot）”。
- **状态**：`已成稿，待本批复读`

---

## 1. 实际采用的资料范围

- **Open Music Theory (OMT) 教学文献源码**：
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/alteredSubdominants.md`（变化下属和弦体系、那不勒斯和弦、意/法/德/瑞增六和弦构成、功能低音 [S6] 标记、莫扎特五度规避与终止四六和弦衔接）；
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/harmonicFunctions.md` 与 `harmonicSyntax1.md`（T-S-D-T 功能等级与和声语法模型）；
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/cadenceTypes.md`（正格终止与半终止的和声动力学要求）；
- **实证总谱研读**：
  * 沃尔夫冈·阿玛多伊斯·莫扎特《C大调第19弦乐四重奏“不协和”》K. 465 第四乐章（Allegro molto，mm. 10–16：m. 13 自然下属 IV6，m. 14 第 2 拍爆发法国六和弦 Fr.，mm. 15–16 经 Cad6/4 达成完全正格终止 PAC）；
  * 路德维希·凡·贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章（Andante molto cantabile ed espressivo，mm. 1–8：如歌萨拉班德变奏主题，m. 7 拍尾至 m. 8 拍头引入德国六和弦 Ger. 强力加压，释放于半终止 HC）；
  * 弗朗茨·舒伯特《降B大调第21钢琴奏鸣曲》D. 960 第一乐章（Molto moderato，mm. 18–48：主部主题呈示与神秘低音震音，德六和弦向属七和弦的等音重拼与半音大三度远关系调区跃迁）；
- **引证与推论纪律说明**：
  * 本文严格立足于上述实际阅读的 OMT 章节与实证总谱，严禁虚构文献页码；
  * 增六和弦的四大形态构成、声部导向与功能低音标记严格依据 OMT 体系；
  * 关于外声部“反向半音向心钳夹”的物理力学模型、声学色彩微积分以及等音转调枢纽的语法漂移分析，在正文中明确注明为笔者的归纳推导。

---

## 2. 谱例占位清单

本篇正文规划 3 处核心例证，严格按照工程硬规则采用标准文本引用块规范占位，绝无空 lilypond 围栏，确保构建通过：

1. **莫扎特《C大调第19弦乐四重奏“不协和”》K. 465，第四乐章 Allegro molto，mm. 10–16**
   - 编制与 GM 编号：第一小提琴（GM 40）、第二小提琴（GM 40）、中提琴（GM 41）、大提琴（GM 42）
   - 调性与拍号：C 大调，2/4 拍
   - 结构特征：mm. 10–12 呈示推进；m. 13 温和下属 IV6；m. 14 第 2 拍法国六和弦（Fr.）；mm. 15–16 经 Cad6/4 达成完全正格终止 PAC
   - 交付状态：文本引用块占位，待后续向谱例助手提 R 卡制作真实 LilyPond 围栏并独立核验；
2. **贝多芬《E大调第30钢琴奏鸣曲》Op. 109，第三乐章 Andante molto cantabile ed espressivo，mm. 1–8**
   - 编制与 GM 编号：钢琴双手（GM 0: Acoustic Grand Piano）
   - 调性与拍号：E 大调，3/4 拍
   - 结构特征：mm. 1–6 萨拉班德风格如歌先行句；m. 7 拍尾至 m. 8 拍头引入德国六和弦（Ger.）跨小节线强力加压，释放于半终止 HC
   - 交付状态：文本引用块占位，待后续向谱例助手提 R 卡制作真实 LilyPond 围栏并独立核验；
3. **舒伯特《降B大调第21钢琴奏鸣曲》D. 960，第一乐章 Molto moderato，mm. 18–48**
   - 编制与 GM 编号：钢琴双手（GM 0: Acoustic Grand Piano）
   - 调性与拍号：降 B 大调，4/4 拍
   - 结构特征：主部呈示与神秘低音升 F 震音，德六和弦与属七和弦等音重释机制，实现向半音/大三度远关系调区的等音转调跃迁
   - 交付状态：文本引用块占位，待后续向谱例助手提 R 卡制作真实 LilyPond 围栏并独立核验。

---

## 3. 待解决缺口

- 当前全库编译环境与内容结构校验 100% 正常；
- 3 处核心例证待在后续轮次中由主控统筹资料助手与谱例助手制作自包含 LilyPond 代码并进行音域与对位核验。
