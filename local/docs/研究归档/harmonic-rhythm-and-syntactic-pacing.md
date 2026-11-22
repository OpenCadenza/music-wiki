# 选题研究归档：和声节奏与句法推进

## 1. 选题基本信息

- **短标题**：和声节奏
- **长问题**：和声变更频率如何组织乐句推进、制造终止期待与结构高潮？古典作品中和声节奏与表面音符时值、超拍节拍有何本质区分，加速与减速机制又如何在曲式关键节点协同运作？
- **对应任务卡**：S107 (task-50)
- **当前状态**：已成稿，待本批复读

---

## 2. 正文与索引位置

- **正文文件**：`content/techniques/harmony/harmonic-rhythm-and-syntactic-pacing.md`（短标题：和声节奏）
- **来源与许可**：`provenance/techniques/harmony/harmonic-rhythm-and-syntactic-pacing.md`

---

## 3. 谱例状态与案例核验

1. **贝多芬：F小调第1钢琴奏鸣曲 Op. 2 No. 1，第 1 乐章 Allegro，mm. 1–8**
   - 证明：标准句型中呈示句到延续句的指数级和声加速阶梯（2小节 → 1小节 → 半小节）；
   - 谱面核验：
     - mm. 1–2：低音 F2–A♭2–c3 支撑曼海姆火箭上行琶音，保持在 F 小调主功能区（i），和声步长整整 2 小节；
     - mm. 3–4：移位至属功能区，低音 E2 支撑属七和弦（V6/5），和声步长同样为 2 小节；
     - mm. 5–6：进入延续句，动机断片化为 1 小节单元，m. 5 驻留于 i，m. 6 模进上移至 vii°6/V，和声更迭速率加速为 1 小节；
     - m. 7：终止功能区，第 1 拍特强（ff）第一转位主和弦（i6），第 3 拍旋律下行切入前属和弦（ii°6），和声节奏成倍紧缩为半小节（2拍）一换；
     - m. 8：汇聚于属和弦（V）并以冠音延长记号达成半终止（HC）；
   - 底本来源：本地 Humdrum 贝多芬奏鸣曲库 `beethoven-piano-sonatas-main/kern/sonata01-1.krn`；
   - 状态：**规范单行文本占位**。

2. **莫扎特：C大调第15钢琴奏鸣曲 K. 545，第 1 乐章 Allegro，mm. 1–14**
   - 证明：表面节奏（十六分音符阿尔贝蒂低音）与深层和声节奏的解耦推进；
   - 谱面核验：
     - mm. 1–4：左手为持续十六分音符 C–G–E–G 阿尔贝蒂低音，表面流动极快，但宏观和声节奏处于宽广主功能延留状态（m. 1: I, m. 2: V4/3-I6, mm. 3–4: IV6-I6/V6/5-I）；
     - mm. 5–8：右手十六分音符下行跑动，低音和声节奏开始以 1 小节为步长稳健更迭（IV → I6 → ii6 → V）；
     - mm. 9–14：进入过渡段，两手表面十六分音符不减，但和声节奏在 mm. 9–11 突然提速至每两拍（半小节）更迭一个和弦（ii → V/V → V），驱动全曲冲刺撞击至 m. 12 属半终止三拍长休止的内聚裂隙；
   - 底本来源：本地 Humdrum 莫扎特奏鸣曲库 `0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc`；
   - 状态：**规范单行文本占位**。

3. **贝多芬：F小调第1钢琴奏鸣曲 Op. 2 No. 1，第 1 乐章 Allegro，mm. 81–101**
   - 证明：展开部再现准备段属音驻留（Standing on the Dominant）的减速制动与张力蓄积；
   - 谱面核验：
     - mm. 81–94：低音声部筑起八分音符脉动的属音 C 踏板，整整 14 小节固定在属功能区，深层和声节奏骤降归零；
     - mm. 85–92：右上声部先后在 c²（m. 85）与 c³（m. 87）爆发出带装饰音的长颤音与突强跳进，表面激化与和声冻结形成强烈势能反差；
     - mm. 93–100：动态降至 pp，踏板撤去，单线条半音下行叹息逐步融解织体；
     - m. 101：曼海姆火箭在原调 F 小调以特强（ff）爆发再现；
   - 底本来源：本地 Humdrum 贝多芬奏鸣曲库 `beethoven-piano-sonatas-main/kern/sonata01-1.krn`；
   - 状态：**规范单行文本占位**。

---

## 4. 理论脉络与主要文献依据

- **Open Music Theory (OMT)**：
  - `sentence.md`：句型呈示句与延续句的定义，明确将和声加速（Harmonic Acceleration）列为延续功能的五大关键标志；
  - `harmonicSyntax1.md` / `harmonicSyntax2.md`：和声功能区（T/S/D Zone）的建立与延留机制；
  - `themeFunctions.md`：主题功能界定与和声变更速率在呈示、延续与终止区的配置；
- **William Caplin**：《古典曲式》（*Classical Form*, 1998）与《古典曲式分析》（*Analyzing Classical Form*, 2013），系统阐述句型结构内部的几何级数和声加速阶梯，以及曲式关键节点处属音驻留（Standing on the Dominant）的制动力学；
- **与首批 20 篇及本轮选题的关系与边界**：
  - 与《超拍与乐句节奏》（专论宏观多小节重音层级与超小节划分）严格区分，本文专论和弦变更速率与时间句法推进力学；
  - 与《模进与句法》（专论音高移位模型与导向线条）严格区分，模进是和声节奏的一种载体，但和声节奏独立统摄所有句型、终止与踏板；
  - 与《终止四六和弦》（专论微观对位延留与解决）严格区分，本文聚焦宏观和声密度的压缩与释放；
  - 正文中精准关联 short title 链接：`[《超拍与乐句节奏》](../rhythm/hypermeter-and-phrase-rhythm.md)`、`[《模进与句法》](../structure/sequence-mechanics-and-syntactic-functions.md)`、`[《内聚裂隙》](../structure/medial-caesura-and-sonata-transition.md)`、`[《复合乐段》](../structure/compound-period-hierarchical-syntax.md)`、`[《乐句扩展》](../structure/phrase-expansion-and-structural-skeleton.md)`、`[《终止四六和弦》](cadential-six-four-and-dominant-syntax.md)`、`[《终止式延后》](../structure/cadential-evasion-and-temporal-expansion.md)`。

---

## 5. 未解决的缺口与可接受的局限

- **当前缺口**：正文谱例按规范采用单行普通文本占位，待后续集中排谱统一处理；
- **局限**：本文主要以古典乐派键盘奏鸣曲与弦乐四重奏核心例证为主，未深入展开十九世纪后浪漫派（如瓦格纳、李斯特）中通过高度半音化调性游离导致和声节奏完全解构的极端形态。
