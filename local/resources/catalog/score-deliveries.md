# 谱例交付履历与谱源追溯表 (Score Deliveries Registry)

> [!IMPORTANT]
> **状态更新（2026-11-16 晚，三轮核验后）**：SCR-001／002／003 的首版交付经独立核验均判【有差异】并且存在实质错误（海顿右手高八度、左手低八度；莫扎特左手莫名加音并吞休止、m.10 越界至 MIDI 19；Op.74 中提琴低八度、大提琴写出低于最低弦的 A1/Bb1）。三段已按核验结论由 `assistant-scores-a` 重编码，再由 `verifier-deepseek` 复验并最终判**「一致」**，现已回填正文（提交 `9406960` 及后续清理）。本表行内的「首版状态」保留原记录，作为质检教训。
>
> 重编码后的文件（正文所用版本）位于 `local/workbench/scores/assistant-scores-a/`，核验报告见 `local/workbench/scores/verifier/核验报告-修正版.md`（§8 修正建议、§10 改动复审）。
>
> **一个已知的源间冲突**：Op.74 m.9 第一小提琴十六分加花第 9 个音，kern 记 `16ee-`（E♭5），DCML 记 `accidentalNatural`（E♮5），两源 1:1 冲突。取 E♮5（理由：未校订 MS3 原始件即含还原号；该组是前四音 E-F-G-F 的原位八度移位）。**正文不得用这一音作半音阶立论。**

本表记录由资料与谱例协作团队向学者交付的自包含 LilyPond 2.26.0 乐谱片段，明确记录其原始数据来源、精确取音行号/小节定位、核对状态与编译验证结果。本目录纳入 Git 版本控制，确保交付谱例具备完整的版本回溯与可复现性。

---

## 交付清单

| 编号 | 作品与作品号 | 乐章与小节 | 谱源原件与精确取音定位 | 交付文件路径 | 交付助手 | 状态 | 编译结果 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCR-001** | 海顿（J. Haydn）<br>《G大调第42钢琴奏鸣曲》Hob. XVI:27 | III. Presto<br>mm. 1–8（含弱起 `\partial 8`） | **原件路径**：`local/origin_resources/corpus/lilypond/HaydnFJ/HOB-XVI-27/hob-xvi-27-iii-presto/hob-xvi-27-iii-presto.ly`<br>**精确定位**：<br>- 右手高音部 `MD`：第 34–44 行；<br>- 左手低音部 `MS`：第 256–266 行。<br>**底本说明**：C. F. Peters (1880s) / Mutopia Project 权威排版源。 | 首版：[resources/scores/haydn-hob-xvi-27/](../../resources/scores/haydn-hob-xvi-27/)<br>**现用**：`local/workbench/scores/assistant-scores-a/haydn-hob-xvi-27-mvt3-mm1-8.ly` | resource-assistant 首版 → assistant-scores-a 重编码 | 首版【有差异】（右手高八度、左手 mm.5–8 低八度）；**重编码版经复核「一致」，已入正文** | 首版编译通过但音高有误；重编码版编译 0 error/0 warning |
| **SCR-002** | 莫扎特（W. A. Mozart）<br>《G大调钢琴奏鸣曲》K. 283 (189h) | I. Allegro<br>mm. 1–10（含弱起 `\partial 4`） | **原件路径 1（ABC/Kern）**：`local/origin_resources/corpus/abc/humdrum-kern/mozart_sonatas/0013-13-Piano Sonata No. 5 in G major, K 283 (189h), mvmt. 1.abc`<br>**定位**：第 25–46 行。<br>**原件路径 2（MusicXML）**：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k283.xml`<br>**底本说明**：新莫扎特全集（NMA）与 Humdrum 数字化原谱。 | [mozart-k283-mvt1-mm1-10.ly](../../resources/scores/mozart-k283/mozart-k283-mvt1-mm1-10.ly) | resource-assistant 首版 → assistant-scores-a 重编码 | 首版【有差异】（左手凭空加三音并吞休止、m.10 出现 MIDI 19 越界）；**重编码版经复核「一致」，已入正文** | 首版编译通过但音高/节奏有误；重编码版编译 0 error/0 warning |
| **SCR-003** | 贝多芬（L. v. Beethoven）<br>《降E大调第10弦乐四重奏“竖琴”》Op. 74 | I. Poco adagio<br>mm. 1–9 | **原件路径 1（Kern）**：`local/origin_resources/corpus/abc/humdrum-kern/beethoven_quartets/0038-38-String Quartet No. 10 in E_b Major, Op. 74 mvt 1.abc`<br>**原件路径 2（DCML）**：`local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n10op74_01.mscx` 与 `local/resources/scores/dcml-abc/n10op74_01.notes.tsv` | [beethoven-op74-mvt1-mm1-9-adagio.ly](../../resources/scores/beethoven-op74/beethoven-op74-mvt1-mm1-9-adagio.ly) | 预备轮录入 → assistant-scores-a 重编码 | 首版【有差异】（中提琴低八度、大提琴低于最低弦 C2）；**重编码版经复核「一致」，已入正文**（含上文 E♮5／E♭5 源冲突登记） | 首版编译通过但音高有误；重编码版编译 0 error/0 warning |
| **SCR-004** | 贝多芬（L. v. Beethoven）<br>《F大调第16弦乐四重奏》Op. 135 | IV. Der schwer gefaßte Entschluß<br>Grave, mm. 165–172 | **原件路径（Kern）**：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet16-4.krn`<br>**定位**：第 887–960 行。 | `local/workbench/scores/assistant-scores-c/beethoven-op135-mvt4-mm165-172-grave.ly`（已交付落盘） | `assistant-scores-c` | **已独立核验：一致（D1 休止已补；D2/D3 为 Kern 与 DCML/BeLuva 源间冲突，.ly 取多数，已注明），正文待回填** | 编译通过（verifier-4 复核 0 warning） |
| **SCR-005** | 莫扎特（W. A. Mozart）<br>《C大调钢琴奏鸣曲》K. 330 (300h) | II. Andante cantabile<br>mm. 1–8（含弱起 `\partial 4.`） | **原件路径 1（OMT XML）**：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k330,ii.xml`（含完整弱起及 mm. 1–8 乐段）<br>**原件路径 2（OMT 图）**：同目录 `Graphics/form/k330-ii.png`<br>**原件路径 3（Humdrum Kern）**：`local/origin_resources/corpus/abc/humdrum-kern/mozart_sonatas/0041-41-Piano Sonata No. 10 in C major, K 330 (300h), mvmt. 2.abc`<br>**对照参照**：新莫扎特全集（NMA IX/25/1） | [mozart-k330-mvt2-mm1-8.ly](../../workbench/scores/assistant-scores-d/mozart-k330-mvt2-mm1-8.ly) | `assistant-scores-d` 编码 → `verifier-2` 独立核验 | **经 `verifier-2` 判「一致」，已入正文** | 0 error / 0 warning；95 音，F2–C6（88 键音域内） |
| **SCR-006** | 贝多芬（L. v. Beethoven）<br>《G大调第2弦乐四重奏》Op. 18 No. 2 | IV. Allegro molto quasi presto<br>mm. 1–8 | **原件路径 1（OMT XML）**：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/beethoven_18_2.xml`（全四声部）<br>**原件路径 2（OMT 图）**：同目录 `Graphics/form/beethoven_18_2.png`<br>**原件路径 3（Kern）**：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet02-4.krn`（第 16–46 行）<br>**原件路径 4（DCML）**：`local/resources/scores/source-packages/dcml/ABC-main/ABC-main/reviewed/n02op18-2_04_reviewed.mscx` 与 `local/resources/scores/dcml-abc/n02op18-2_04.notes.tsv` | [beethoven-op18-no2-mvt4-mm1-8.ly](../../workbench/scores/assistant-scores-d/beethoven-op18-no2-mvt4-mm1-8.ly) | `assistant-scores-d` 编码 → `verifier-2` 独立核验 | **经 `verifier-2` 判「一致」，已入正文** | 0 error / 0 warning；50 音，A2–B4；四声部均落在乐器物理音域内 |
| **SCR-007** | 海顿（J. Haydn）<br>《G大调弦乐四重奏》Op. 64 No. 4 (Hob. III:66) | II. Menuetto (Allegretto)<br>mm. 1–8（含弱起 `\partial 4`） | **原件路径（OpenScore 转写，主依据）**：OpenScore/StringQuartets `scores/Haydn,_Joseph/String_Quartet_in_G_major,_Hob.III66,_Op.64,_No.4/sq7249986.mxl`（据 IMSLP #06556，Eulenburg 版 Altmann 编订）；本地副本 `local/workbench/scores/assistant-scores-e/tmp/haydn_hobIII66_op64no4.mxl`；排版 PDF 本地副本 `tmp/openscore_haydnIII66.pdf`<br>**独立交叉核对**：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/haydn-III-66-ii.png`（OMT 二谱表缩编）<br>**注意**：本曲即正文占位原先误写的「Hob. III:66 (Op. 77 No. 1) 第二乐章 Adagio」；实际 Op. 77 No. 1 = Hob. III:81，本曲第二乐章为 Menuetto（详见 `assistant-scores-e/核对记录.md` §1.1，正文侧待修正） | [haydn-hobIII66-op64no4-mvt2-mm1-8.ly](../../workbench/scores/assistant-scores-e/haydn-hobIII66-op64no4-mvt2-mm1-8.ly) | `assistant-scores-e` 编码（自检：MusicXML↔MIDI 逐音一致） | **已入正文；独立核验进行中（待核验）** | 0 error / 0 warning；80 音，G2–B5；四声部音域合法（m.7 倚音 B4 为 LilyPond MIDI 附加输出，非音符错误） |
| **SCR-008** | 贝多芬（L. v. Beethoven）<br>《c小调第7小提琴奏鸣曲》Op. 30 No. 2 | III. Scherzo: Allegro<br>mm. 1–8 | **谱源盘点（均不可逐音置信，未编码）**：① 仓库内 OMT 资产 `.../Graphics/form/XML/beethovenop30.xml`（Sibelius 导出，单 part「Piano」两谱表**钢琴缩编**，无小提琴声部）与 `.../Graphics/form/beethoven_op30.png`；② 19 世纪早期版本扫描（Wikimedia Commons / Internet Archive b25709409，10 页，本地副本 `local/workbench/scores/assistant-scores-e/tmp/beeth_op30no2_earlyed.pdf`）——低质石印/铜版、老式休止符字形、三谱表无法稳定对齐到可逐音置信；③ IMSLP 直连被 bot check 拦截；Mutopia 仅第 1、4 乐章，无第三乐章；DCML / Humdrum 语料均无小提琴奏鸣曲 | **未交付（—）** | `assistant-scores-e`（定位后判定放弃，按硬约束不编造） | **未交付**：无源可逐音置信；正文保持占位（不得当已核验事实使用） | 未编码（详情见 `assistant-scores-e/核对记录.md` §2） |

---

## 规范与质量保证

1. **真实谱源溯源**：每一条谱例必须写明本地文件路径与物理行号/小节，严禁脱离谱源凭记忆复原，严禁自编织体冒充原作。
2. **独立核验必经**：所有谱例必须由独立核验人进行逐音、逐八度、乐器音域比对，不得单凭编译通过结论作为交付标准。
3. **声部完整性**：
   - 键盘作品必须双行大谱表全声部；
   - 弦乐室内乐必须全声部总谱；
   - 若只能交付声部摘录，必须在 `title` 与 `location` 中明示“摘录”与实际声部。
4. **技术要求**：
   - LilyPond 2.26.0 语法；
   - `\language "english"`；
   - GM 乐器程序号 (0–127)；
   - 速度标记、拍号与弱起对齐。

---

## 未入库下载件（2026-11-17 清点）

下列外部下载件位于 `local/workbench/scores/assistant-scores-e/tmp/`（workbench 临时目录，非 Git 登记目录）。经核对，`local/origin_resources/` 与 `local/resources/` 下**均无对应登记**（`openscore-stringquartets` 仅有整库 ZIP 级登记，与下列单曲件无关）。仅备注，不移动文件、不改动 `origin_resources`。

| 下载件（本地路径） | 内容与来源 | 用途 / 备注 |
| --- | --- | --- |
| `local/workbench/scores/assistant-scores-e/tmp/haydn_hobIII66_op64no4.mxl` | OpenScore StringQuartets `sq7249986.mxl` 的本地副本（海顿 Op. 64 No. 4 / Hob. III:66 弦乐四重奏转写，底本 IMSLP #06556，Eulenburg 版 Altmann 编订） | SCR-007 主谱源（S1），逐音编码依据；建议后续决定是否正式入库 `origin_resources` |
| `local/workbench/scores/assistant-scores-e/tmp/openscore_haydnIII66.pdf` | 上述转写的排版 PDF（OpenScore 仓库内 `sq7249986.pdf`）本地副本，页面 9 = II. Menuetto 起 | SCR-007 视觉比对与交付用 |
| `local/workbench/scores/assistant-scores-e/tmp/beeth_op30no2_earlyed.pdf` | 贝多芬 Op. 30 No. 2 早期版本扫描（10 页），Wikimedia Commons / Internet Archive `b25709409` | SCR-008 弃用谱源证据（未能逐音置信，见核对记录 §2） |

> 备注：未发现独立的 IMSLP 直连下载件——IMSLP 原谱下载被 bot check 拦截（`assistant-scores-e/核对记录.md` §2.1）；IMSLP #06556 仅作为 OpenScore 转写的底本源被引用，不构成本地原件。


## 2026-11-17 本轮补齐（谱例助手 S1–S6 + 独立核验）

| 编号 | 作品/片段 | 交付者 | 状态 |
| --- | --- | --- | --- |
| SCR-009 | 巴赫 BWV 269 mm.3–4 | S1 | 核验一致，已入正文 |
| SCR-010 | 巴赫 BWV 347 mm.3–4 | S1 | 核验一致（时值按四分+fermata 修正），已入正文 |
| SCR-011 | 巴赫 BWV 38/6 mm.12–13 | S1 | 核验一致，已入正文 |
| SCR-012 | 巴赫 BWV 153/5 mm.3–4 | S1 | 核验一致（C♮ 修正），已入正文 |
| SCR-013 | 巴赫 BWV 87/7 mm.1–3 | S1 | 核验一致，已入正文 |
| SCR-014 | 巴赫 BWV 269 mm.5–7 | S1 | 核验一致（C♮ 修正），已入正文 |
| SCR-015 | 巴赫 BWV 60/5 mm.1–4 | S1 | 核验一致，已入正文 |
| SCR-016 | 贝多芬 Op.74 I mm.18–24 | S1/S2 各一版 | 核验一致（D 版已入正文；S1 版仅存工作区） |
| SCR-017 | 贝多芬 Op.131 I mm.6–11 | S2 | 核验一致，已入正文 |
| SCR-018 | 贝多芬 Op.132 I mm.1–8 | S2 | 核验一致（G♯2），已入正文 |
| SCR-019 | 贝多芬 Op.95 I mm.1–8 / mm.19–24 | S2 | 核验一致，已入正文 |
| SCR-020 | 贝多芬 Op.135 IV mm.1–4 / mm.12–16 / mm.165–172 | S3 + assistant-scores-c | 核验一致（D1 休止已补），已入正文 |
| SCR-021 | 舒伯特 D.328 mm.1–5 / mm.72–76 | S3 | 核验一致（m.76 左手 F♯3 修正），已入正文 |
| SCR-022 | 巴赫 BWV 1050 I mm.1–9 | S3 | 核验一致（cemba2 省略已注明），已入正文 |
| SCR-023 | 海顿 Hob.I:104 I mm.17–31（弦乐）/ mm.32–39（全奏） | S3 | 核验一致（按印刷谱号重编、补力度与圆号移调后），已入正文 |
| SCR-024 | 贝多芬 Op.74 I mm.6–9 | S3 | 内容通过；m.9 花彩降号与 DCML 冲突（kern 对、DCML 疑漏），未入正文（记谱轴以链接指向前文） |
| SCR-025 | 贝多芬 Op.13 I mm.1–19 | S4 | 核验一致，已入正文 |
| SCR-026 | 贝多芬 Op.81a I mm.1–25 | S4 | 核验一致（悬空延音线待整理），已入正文 |
| SCR-027 | 贝多芬 Op.111 I mm.1–25 | S4 | 核验一致（拍号 4/4；m.7/8/13 版本差异已注），已入正文 |
| SCR-028 | 莫扎特 K.309 III mm.9–19 | S4 | 核验一致（倚音按 NMA），已入正文 |
| SCR-029 | 贝多芬 Op.2 No.3 I mm.1–13 | S4 | 核验一致（删 m.11 悬空延音线），已入正文 |
| SCR-030 | 莫扎特 K.465 IV mm.10–16 | S2 | 核验有条件通过，已修正（F♯、速度 144、编号基准）并入正文 |
| SCR-031 | 贝多芬 Op.14 No.1 I mm.1–16 | S5 | 核验一致，已入正文（Hess 34 无源未收录） |
| SCR-032 | 海顿 Op.76/3 II mm.1–20 | S1 | **待修正 6 处八度后入正文**（核验已给逐行清单） |
| SCR-033 | 贝多芬 Op.135 III mm.1–12 | S1 | **待修正 4 处音高后入正文** |
| SCR-034 | 勃拉姆斯 Op.90 III mm.1–8 | S2 | **退回返修**（m.4 后半至 m.8 大提琴仍高八度） |
| SCR-035 | 贝多芬 Op.67 II mm.205–209 | S2 | **退回返修**（只含大管声部，且降号被写成升号） |
| SCR-036 | 贝多芬 Op.109 III mm.1–8 | S6（进行中） | 编码中 |
| SCR-037 | 舒伯特 D.960 I mm.18–48 | S6（进行中） | 视源有无决定 |

### 缺口（确认无可靠机器可读源）

HWV 348 Air、K.550 III、Op.55 I、Op.67 IV、Reicha Op.88/2、Nielsen Op.43、Op.97、D.929、Hess 34、Op.125 I、Mahler 4 II、K.494。详见 `local/docs/实施记录/2026-11-16-DSH首批/批次日志.md` M19/M20 与各助手 `缺口报告.md`。

| SCR-036 | 贝多芬 Op.109 III mm.1–8 | S6 | 核验一致（m.7 左手连音线已按核验补），已入正文 |
| SCR-037 | 舒伯特 D.960 I mm.18–48 | S6 | 未交付：DCML/kern/Mutopia 均无舒伯特钢琴奏鸣曲语料，已登记缺口 |

**2026-11-17 返修与复核结果**：SCR-032（海顿 Op.76/3）与 SCR-033（Op.135 III）已返修并入正文；SCR-035（Op.67 II）已改降号拼写、改名 m205-209，以"大管声部摘录"入正文；SCR-034（勃拉姆斯）核验与返修结论冲突未决，暂不入正文。另经主控最小探针复核：核验员对 Op.135 III 三处"应改 A♮/D♮"的判定系测量脚本按调号误算，实际原文件已正确。
