# 核验报告：海顿 Op. 64 No. 4 (Hob. III:66) 第二乐章 Menuetto，mm. 1–8（含弱起）

- **核验人**：verifier-3（独立核验员，只核对/报告，未改任何成品）
- **核验日期**：2026-11-17
- **核验对象**：`content/techniques/structure/hybrid-themes-and-syntax-decoupling.md` 中 `title="海顿 Op. 64 No. 4 (Hob. III:66) 第二乐章 Menuetto"` 的 `lilypond` 围栏（md 行 178–290，location = mm. 1–8 含弱起）
- **抽取方式**：从 md 原样抽取（`verifier/tmp3/fence_haydn.ly`，md 行 178–290，111 行）；围栏与生产者交付文件 `local/workbench/scores/assistant-scores-e/haydn-hobIII66-op64no4-mvt2-mm1-8.ly` 的 score body **逐字符一致**（脚本化对比确认，差异仅注释与 `\version`/`\language` 行）
- **权威依据**：
  1. **S1**：OpenScore StringQuartets 转写 `sq7249986.mxl`（本地副本 `assistant-scores-e/tmp/haydn_hobIII66_op64no4.mxl`；据 IMSLP #06556，Eulenburg 版 Wilhelm Altmann 编订），已确认其属性：4 声部、Menuetto 起始于绝对小节 101（局部 num=0，3/4，fifths=1）；排版 PDF（本地 `tmp/openscore_haydnIII66.pdf`）第 8 页为 `II. Menuetto` 起始页，已高清渲染核对
  2. **S2**：OMT 教材缩编图 `Graphics/form/haydn-III-66-ii.png`（仓库旧版库；本会话中该图已按 S1/正文引用做独立视觉交叉，裁剪副本保存在 `verifier/tmp3/omt_*.png`，图源路径在本会话期间因并行整理被移动，裁剪副本可复验）
  3. IMSLP 作品页 General Information（`Hob.III:66 ; Op.64 No.4`，Key = G major，乐章表 = Allegro con brio / Minuet-Trio / Adagio cantabile sostenuto / Finale. Presto）——与核对记录 §1.1 陈述一致
- **补充说明**：IMSLP #06556 原版 PDF 与 archive.org 的独立扫描本会话内均因外部拦截无法直接下载（bot check / 连接超时），故 m.8 的第二遍细节以 S1（转写自 #06556）之 XML 与排版 PDF 为唯一可用谱面依据，S2（OMT 缩编）作独立交叉。

---

## 一、总体结论

**「一致（附 2 处需记录在案的注意点）」**：mm.0–7 四声部逐音（音高/八度/临时记号/时值/连音线/跳音/力度）与 S1 完全一致，与 S2 缩编图吻合；m.8 围栏采用完整 3 拍小节的第一遍形态书写，与 S2 及 S1 的第一遍（X1）一致；与 S1 的反复第二遍（num=8）在 Vn II 第 3 拍存在 **1 处音符差异**（见 §5.2），编码本身与其说明的"已按 3 拍书写"目的一致。正文 §3.2 两句话的和声断言与谱面低音进行**吻合**。编译 0 error / 0 warning，barcheck 生效。

---

## 二、核对项 1：拍号 / 调号 / 速度 / 乐章归属 —— **一致**

| 项目 | 正文/围栏 | S1（OpenScore/据 Eulenburg） | S2（OMT 图） | 结论 |
| :--- | :--- | :--- | :--- | :--- |
| 调号 | G 大调（`\key g \major`） | Menuetto 起 fifths=1，`attributes` 无降调号 | 一个升号（F#） | 一致 |
| 拍号 | 3/4 | 局部 num=0 起 `<time><beats>3</beats><beat-type>4</beat-type></time>`，divisions=48 | 3/4 | 一致 |
| 速度 | `\tempo "Allegretto" 4 = 130` | 局部 num=0 有 `{II. Menuetto} {Allegretto}`；原版仅印 Allegretto，无节拍机数字，130 取自转写播放属性（谱内注释已说明） | — | 一致（130 非原版标记，已注释） |
| 乐章 | 第二乐章 Menuetto（Allegretto），非 Adagio | `{II. Menuetto}{Allegretto}` + IMSLP 乐章表 | 标题区 `II. Menuetto` | 一致；正文原占位「Op.77 No.1/Adagio/降E/2/4」确为错误，现谱例与正文 §3.2 均已按 Op.64 No.4 写 |

---

## 三、核对项 2：小节对应（弱起 + mm.1–8）—— **一致（附 m.8 结构说明）**

- S1 中 Menuetto 局部小节 = num 0（弱起）→ num 7，随后 m.8 被转写为 **X1（第一遍，2 拍）** + **num=8（第二遍，1 拍）** 两个 logic 小节（`:|` 在 X1 右端、`|:` 在 num=8 左端），合计 3 拍 = 完整 m.8。
- 围栏写法：`\partial 4`（弱起 1 拍）+ 8 个完整 3/4 小节，末小节为 m.8，末行 `\bar "||"`。
- 弱起内容与 S1 一致：Vn I `D5–B4` 两个八分（连音线、f），其余三声部 `r4`（S1 idx 101 确认为 `D5-B4 eighth [sls]`，其他 `R`）。`\partial 4` 与源一致。
- **说明**：S1 的 m.8 因反复记号被拆为 X1（第一遍：Vn I `G4+R`、Vn II `B3+R`、Va `G4+R`、Vc `G2·G3·`，共 2 拍）+ num=8（第二遍：Vn I `R`、Vn II `C5–B4`、Va `R`、Vc `R`，共 1 拍）。围栏按"完整 3 拍小节（强拍 G 主和弦 + 两拍休止，Vn II B3 + 两拍休止）"书写，与 S2（OMT 缩编图 m.8 = treble G 四分 + 两个四分休止）和 S1 的第一遍形态一致，是谱例对反复结构的标准扁平化处理；但 **Vn II 的第三拍在 S1 第二遍中为 C5–B4 八分连音而非休止**，见 §5.2。

---

## 四、核对项 3：逐音核对四声部（S1 XML idx 101–110 ↔ 围栏）—— **mm.0–7 完全一致；m.8 见 §5.2**

记号：`·`=跳音（staccato），`( )`=连音线，`g`=倚音（grace），(n)=时值（拍）。

| 局部小节 | 声部 | S1（逐音） | 围栏（LilyPond） | 判定 |
| :--- | :--- | :--- | :--- | :--- |
| 弱起 | Vn I | D5(½)-( B4(½) )，f | `d''8(\f b'8)` | 一致 |
| 弱起 | Vn II / Va / Vc | r4 | `r4` | 一致 |
| m.1 | Vn I | F#4(½)-(G4(½) ) D4(1)· B5(½)-(G5(½) ) | `fs'8( g'8) d'4-. b''8( g''8)` | 一致（含 B5/G5 八度，经 S2 图复核） |
| m.1 | Vn II | r4 ‖ D4(1)· D4(1)·（f） | `r4 d'4-.\f d'4-.` | 一致 |
| m.1 | Va | r4 ‖ B3· B3·（f） | `r4 b4-.\f b4-.` | 一致 |
| m.1 | Vc | r4 ‖ G3· G3·（f） | `r4 g4-.\f g4-.` | 一致 |
| m.2 | Vn I | F#5(½)-(A5(½)) C5(1)· A4(½)-(C5(½)) | `fs''8( a''8) c''4-. a'8( c''8)` | 一致 |
| m.2 | Vn II / Va / Vc | r4 ‖ F#4·F#4· / A3·A3· / D3·D3· | 同 | 一致 |
| m.3 | Vn I | C5–B4 十六分连 ‖ r8 ‖ D5–C5 ‖ r8 ‖ E5–C5 ‖ r8 | `c''16( b'16) r8 d''16( c''16) r8 e''16( c''16) r8` | 一致 |
| m.3 | Vn II | G4· r G4· r G4· r | `g'8-. r8 g'8-. r8 g'8-. r8` | 一致 |
| m.3 | Va | G3· r E3· r C3· r | `g8-. r8 e8-. r8 c8-. r8` | 一致 |
| m.3 | Vc | **G3**· r E3· r C3· r | `g8-. r8 e8-. r8 c8-. r8`（G3） | 一致（生产者自述初版误写 `g,`=G2 已改为 `g`=G3，与 S1 同音齐奏核实无误） |
| m.4 | Vn I | A4(2) ‖ D4(1)（p） | `a'2 d'4\p` | 一致 |
| m.4 | Vn II | F#4(2) r4 | `fs'2 r4` | 一致 |
| m.4 | Va | D3· r r | `d4-. r4 r4` | 一致 |
| m.4 | Vc | D3· D4· r | `d4-. d'4-. r4` | 一致 |
| m.5 | Vn I | G4(2)-( B4(½) G#4(½) ) | `g'2( b'8 gs'8)` | 一致（G#4=gs' 临时升号正确） |
| m.5 | Vn II / Va / Vc | r4 ‖ D4·D4· / G3·F4· / B2·B2·（p） | `r4 d'4-.\p d'4-.` 等 | 一致 |
| m.6 | Vn I | B4(½)-(A4(½)) C5(1)· C5(½)-(B4(½)) | `b'8( a'8) c''4-. c''8( b'8)` | 一致 |
| m.6 | Vn II | E4(1) r E4(½)-(D4(½)) | `e'4 r4 e'8( d'8)` | 一致 |
| m.6 | Va / Vc | E4 r r / C3 r r | `e'4 r4 r4` / `c4 r4 r4` | 一致 |
| m.7 | Vn I | **(g B4)** A4(1)-( A4(½) G4(½) A4(½) D4(½) ) | `\grace b'16 a'4( a'8 g'8 a'8 d'8)` | 一致；**倚音 B4 确认来自 S1（XML `(g B4)`），非生产者自行添加** |
| m.7 | Vn II | C4(3)（slur start→m.8） | `c'2.` | 一致 |
| m.7 | Va | F#4(3)（slur start→m.8） | `fs'2.` | 一致 |
| m.7 | Vc | D3· D3· D3· | `d4-. d4-. d4-.` | 一致 |
| m.8 | Vn I | X1: G4(1)+R(1)；num8: R(1) | `g'4 r2` | 一致（3 拍） |
| m.8 | Vn II | X1: B3(1)+R(1)；num8: **C5(½)-B4(½)** | `b4 r2` | **有差异（详见 §5.2）** |
| m.8 | Va | X1: G4(1)+R(1)；num8: R(1) | `g'4 r2` | 一致 |
| m.8 | Vc | X1: G2·G3·（共 2 拍）；num8: R(1) | `g,4-. g4-. r4` | 一致 |

- 连音线：S1 m.5 Vn I `G4(2)-` 至 `G#4`、m.6 各组、m.7 Vn I 组、m.7 Vn II/Va 的跨小节起音（至 m.8 B3/G4 收）等，围栏均按 S1 起止闭合；生产者的"连音一律按 S1 起止闭合"成立。
- 力度：Vn I 弱起 f、m.4 第 3 拍 p；Vn II/Va/Vc m.1 第 2 拍 f、m.5 第 2 拍 p（S1 XML 逐条核对，与核对记录 §1.3 一致；Va m.5 的 `[p]` 括号属编者附加，按主 `p` 处理无碍）。

---

## 五、核对项 4：音域 —— **一致**

用抽取围栏实编译生成的 MIDI（`verifier/tmp3/verifier_haydn.mid`）经 `midi_pitch_check.py` 检查：

- 音符数 **80**；总音域 G2(43)–B5(83)（与生产者记录的 80 音、G2–B5 完全一致）
- ch1 = Vn I：D4(62)–B5(83) → 满足「Vn I ≥ G3」✓
- ch2 = Vn II：B3(59)–G4(67) → 满足「Vn II ≥ G3」✓
- ch3 = Va：C3(48)–G4(67) → 满足「C3–C6」✓
- ch4 = Vc：G2(43)–D4(62) → 满足「C2–C6」✓
- 全部落在 88 键音域内（A0–C8），无越界。

---

## 六、核对项 5：编译与 barcheck —— **通过**

- 命令：`E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe --pdf --output=verifier_haydn fence_haydn.ly`（对从 md 原样抽取的围栏直接编译，不经过生产者文件）
- 结果：**0 error / 0 warning**；日志结尾 `Success: compilation successfully completed`；`[8]` 表示 8 个小节全部解释通过
- 每小节末均有 `|`；`\partial 4` 弱起 + 8 个完整 3/4 小节，barcheck 全部通过（若有拍数不符会报 "barcheck failed"，未出现）
- MIDI 输出正常（80 音符，与 §五 一致）

---

## 七、核对项 6：与正文 §3.2 文字的和声关系 —— **吻合（附 1 处教法性备注）**

正文两句话：
1. 「mm. 1–4 完成先行句的半终止（m. 4 停于 D 属和弦）」——**吻合**：m.4 低音 D（Vc D3·+D4·）、Vn II F#4、Vn I A4，构成 D 大三和弦（V；D–F#–A），其后 m.5 低音换 B（I6）。m.4 为典型的先行句半终止（HC，V）。
2. 「后 4 小节（mm. 5–8）为由和声级数主导的扩充终止进行（ECP：I6–ii6/5–V–I）」——**吻合于低音骨架**：
   - m.5 低音 **B**（I6，G/B）
   - m.6 低音 **C**（ii6/5）
   - m.7 低音 **D**（V，D 属和弦：Vc D3·×3 + Vn II C4/ Vn I 属和弦音）
   - m.8 低音 **G**（I，G2·G3· → G）
   - 低音进行 B–C–D–G 与 I6–ii6/5–V–I 逐小节对应，与 OMT 原文「I6 ii6/5 V I」及核对记录 §1.3 一致。
   - **教法性备注（非差异）**：m.6 的规范 ii6/5 音集应为 D–F–A–C（低音 C），S1/围栏中 m.6 写的是 Vn I B4–C5（6–5 邻音/经过）+ Vn II E4 + Va E4 + Vc C3，即强拍呈现 C–E–(+B) 的 ii 类功能位、以经过音方式补足 F/A 感；这是把 ii6/5 功能位写成低音 C + 六度邻音的自然记谱，正文「I6–ii6/5–V–I」的低音级数断言可成立。

---

## 八、差异清单（需记录在案）

### 8.1 【主差异】m.8 Vn II 第 3 拍：S1 第二遍为 C5–B4，围栏为休止

- **依据**：S1 `seq7249986.mxl` 绝对小节 idx=110（局部分 num=8，`|:` 第二遍）Vn II 原始 XML：`C5 eighth slur-start beam-begin` + `B4 eighth slur-stop beam-end`；S1 排版 PDF 第 8 页第三系统第 1 小节（num=8，前反复号）高倍渲染确认 Vn II 为 C5–B4 两个八分连音（其余声部四分休止）。
- **围栏现状**（md 行 212）：Vn II m.8 = `b4 r2`，即第 3 拍写为休止。
- **期望 vs 实际**：若要求围栏完整囊括 S1 之 m.8 反复结构，Vn II 第 3 拍应为 `c''8( b'8)`（C5–B4 八分连音）而非休止；Vn I/Va/Vc 第 3 拍休止与 S1 一致。
- **性质判断**：这属于「谱例对小节内反复记谱的扁平化处理」。S1 因反复记号把 m.8 拆为 X1(2拍)+num8(1拍)，两遍内容不同；围栏取完整 3 拍小节的第一遍形态书写，与 S2（OMT 缩编图，m.8 = treble G 四分 + 两拍休止）**完全一致**，也与正文所引的 OMT 图一致。C5–B4 是第二遍（衔接 B 段）的经过/连接音，非第一遍声部内容。
- **建议**：(a) 若以「忠实 OpenScore 全信息」为标准 → 此差异应记录并在谱例注明或补音；(b) 若以「与正文引用图（OMT）一致的教学谱例」为标准 → 现写法可接受，但建议在谱面注释里说明「m.8 第三拍按第一遍记谱，第二遍 Vn II 有 C5–B4」以免读者对照 OpenScore 时困惑。

### 8.2 【记录项】核对记录 §1.3 对「m.8 排版显示完整 3 拍」的表述不完整

- 核对记录第 63 行称「S1 排版 PDF 显示该小节是 3/4 完整小节（强拍和弦 + 两个四分休止）」；但 S1 排版 PDF 实际把 m.8 拆为 X1（2 拍）与 num=8（1 拍，Vn II 有 C5–B4）两个小节框，两遍合观才是完整 3 拍。生产者在「排版」口径上略过了第二遍的 Vn II 音，与 §8.1 同源。此条不影响 mm.1–7 与 m.8 强拍和弦的正确性，仅影响 m.8 第三拍 Vn II 的完整性。

### 8.3 【备注】浮点编译产物与音域核查均通过（无新增问题）

---

## 九、放行建议

**建议放行。** 理由：

1. mm.0–7 四个声部逐音（音高/八度/临时记号/时值/连音/跳音/力度）与 S1 完全一致，与 S2 缩编图交叉吻合；m.7 倚音 B4 在 S1 中确实存在（XML `(g B4)`），非生产者自加，生产者对该倚音的说明成立。
2. 拍号/调号/速度/乐章归属、小节对应、音域、编译（0 error/0 warning）与 barcheck 全部通过。
3. 正文 §3.2 的和声断言（m.4 V 半终止；mm.5–8 I6–ii6/5–V–I）与谱面低音进行吻合。
4. 唯一音符差异（m.8 Vn II 第 3 拍）属于「反复第二遍连接音」的谱例化省略，与正文引用的 OMT 缩编图一致，音乐功能无冲突；若团队要求严格对照 OpenScore 全信息，可在该小节加注或补 `c''8( b'8)`（会改变 G 主和弦收束的观感，建议优先采用加注方案）。

**最需关注的一点**：§8.1 的 m.8 Vn II 第三拍（S1 第二遍 C5–B4 vs 围栏休止）——不影响任何和弦/主句音，但若有人按 OpenScore 转写逐音比对会发现这一处，建议在谱面或交接记录中显式说明取舍依据。

---

## 附：使用的关键证据文件（均为本会话亲自产出的核验物）

- `local/workbench/scores/verifier/tmp3/fence_haydn.ly`（md 原样抽取）
- `local/workbench/scores/verifier/tmp3/verifier_haydn.mid` / `.pdf`（实测编译产物）
- `local/workbench/scores/verifier/tmp3/omt_left.png` / `omt_right.png` / `omt_m78_zoom.png` / `omt_bottom_right.png`（S2 缩编图裁剪比对）
- `local/workbench/scores/verifier/tmp3/s1_sys2_*.png` / `s1_sys3_*.png` / `s1_X1_hi600.png`（S1 排版 PDF 高倍渲染）
- `local/workbench/scores/assistant-scores-e/tmp/haydn_hobIII66_op64no4.mxl`（S1 主依据）及其导出（`mx_all.py` idx 101–110）
- 脚本：`tmp3/cmp_fence_haydn.py`（围栏↔生产者逐字符对比）、`tmp3/extract_fence_haydn.py`（md 围栏抽取）