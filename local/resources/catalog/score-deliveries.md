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

**2026-11-17 编制篇四件复核**：Reicha Op.88/2、Nielsen Op.43、Beethoven Op.97、Schubert D.929 经 7 条路线穷尽溯源后确认**当前无可用机器可读源**（详见 `local/workbench/scores/score-s7/缺口报告.md`）。唯一可行路径：Zenodo 的 PDMX `mxl.tar.gz`（约 1.8 GB，内含真实 MusicXML；已备好 5 个成员的精确取件清单 `score-s7/_probe/expect_mxl.tsv`）。

| SCR-038 | 尼尔森 管乐五重奏 Op.43 第一乐章 开头 12 小节（弱起 + 印刷谱 mm.1–11） | S8 | 第 2 版核验**可放行**（5/4 恢复、速度文字、小节号、注释四处均过），已按新乐器契约回填正文 |
| SCR-039 | 舒伯特 D.929 第二乐章 mm.1–21 | S9 | 核验通过（补 13 条力度、修 m.16 连音线、隐藏节拍机后），已入正文 |

### 新增谱源：PDMX MusicXML（2026-11-17）
Zenodo 记录 15571083 的 `mxl.tar.gz`（1,894,335,797 B）已取回并解包，5 份 MusicXML 归档在 `scholar-plan-dev/local/resources/scores/pdmx/`（附 README）：Nielsen Op.43 全曲、Nielsen Kvintet 另一转录、Schubert D.929 二乐章三份转录。归档结构为 `mxl/<两位hex>/<两位hex>/<hash>.mxl`，与 `score-s7` 清单里的 `PDMX/mxl/...` 写法不同，按 `members-map.json` 的文件名前缀匹配解出。

---

## 2026-11-22 第二轮 P1 补谱（`task-4`，`score-assistant-2`）

产出目录：`local/workbench/scores/score-p1/`。**生产者不得自我认证**：下表"待独立核验"即表示本助手只完成编码+自检，未作核验结论。

| 编号 | 作品与片段 | 谱源 | 交付文件 | 状态 | 编译结果 |
| --- | --- | --- | --- | --- | --- |
| **SCR-040** | 贝多芬 第七交响曲 Op.92 **II. Allegretto mm.1–10**（10 谱表摘录：长笛/双簧管/单簧管 A/大管/圆号 E + 中提琴/大提琴/低音提琴；一、二小提琴保留空谱表；小号、定音鼓该段全休止，从略） | Mutopia Project #595（Stelios Samelis, 2005；源标 Dover/Litolff，PD）分谱，本地副本 `local/workbench/scores/score-s2/downloads/op92-2/` | `local/workbench/scores/score-p1/beethoven-op92-ii-mm1-10/beethoven-op92-ii-mm1-10.ly`（+ `.pdf`/`.mid`/`page.png` 本地预览件）<br>核对记录：同目录 `核对记录.md`；核验报告：同目录 `核验报告-verifier.md` | **已核验（verifier-4：记谱逐音一致、结构事实全对）**。已按 verifier 意见修正 D1（圆号移调 → 音乐会音高 E3/E4）与 D2（单簧管/圆号改实音记谱），重编译 0 error/0 warning。**同时证伪正文原表述**"前 26 小节木管与铜管完全沉默"：m.1–3 由双簧管、单簧管(A)、大管、圆号(E) 以 f→pp 奏 a 小调主和弦，m.3 后半拍释放；m.3–26 才是纯低弦，第二小提琴 m.27、第一小提琴 m.51 依次进入。正文已回填 `beethoven-op92-ii-mm1-10` 围栏并改写该段 |
| **SCR-038（重新登记）** | 尼尔森 管乐五重奏 Op.43 第一乐章（弱起 + 印刷谱 mm.1–11） | 见 SCR-038 原行（PDMX MXL，`local/origin_resources/downloads/2026-11-17/pdmx/extract/mxl/`） | `local/workbench/scores/score-s8/nielsen-op43-mvt1-mm1-12.ly` | **待独立核验（本轮仅登记，不做自我认证）**：本轮未重新核对内容，也未复核其既有"可放行"结论；按 P1 清单 #7 只登记状态，等 verifier 独立结论 | 沿用 S8 记录（0 error / 0 warning） |

### 缺口（本轮补谱清单 #1 / #2 / #4 / #5，如实报告）

| 清单项 | 作品/片段 | 本轮结论 |
| --- | --- | --- |
| #1 | 贝多芬 钢琴三重奏 Op.97《大公》第一乐章 mm.1–12 | **无可用机器可读源**（续 `score-s5`/`score-s7` 缺口报告：本地 kern 仅钢琴奏鸣曲+弦乐四重奏；PDMX 无 Op.97；Mutopia 无 O97；IMSLP 仅 PDF 扫描；MuseScore 唯一候选自述 WIP） |
| #2 | 雷哈 管乐五重奏 Op.88 No.2 第一乐章 mm.1–8 | **无可用机器可读源**（IMSLP 木管五重奏曲目表缺 Op.88/2；MuseScore `scores/9588706` 标 CC0 但导出需登录会话） |
| #4 | 贝多芬 第九交响曲 Op.125 第一乐章 mm.1–35 | **无可用机器可读源**（Mutopia 该项目仍在 in-progress；本机无交响曲 kern/MusicXML；IMSLP 直链被 bot check 拦） |
| #5 | 马勒 第四交响曲 第二乐章 mm.34–46 | **无可用机器可读源**（PDMX 25.4 万条 0 命中；Mutopia 无 Mahler；KernScores 503） |

**下一步建议（若主控要推进这四处）**：① 用带登录会话的浏览器导出 MuseScore CC0 MXL（Reicha Op.88/2 唯一许可干净的一条）；② Zenodo PDMX `mxl.tar.gz` 全量重取后按 `score-s7/_probe/expect_mxl.tsv` 清单精确取件（该清单已确认含 Op.97/Reicha 之外的目标）；③ **Op.125 本轮新发现可行路径**：CCARH《The Nine Symphonies of Beethoven: A Digital Edition》提供**带显式小节号的 MuseData 原始数据**（非扫描件），`sym9` = Op.125，可从 <https://wiki.ccarh.org/wiki/Ludwig_van_Beethoven> 的 Data 列或 <https://musedata.org/list/> 的 `DATA_URL` 表取 `.md2`；`sym7` 还可用来独立复核 Op.92 II 的未决项（圆号调性、Vn 进入小节）；④ Mahler 4 目前只能挂起或改换同论点例。以上均需外部下载与人工转写，**不经"从扫描目测抄谱"**。

---

## 2026-11-22 R 卡（task-10 / task-8 / task-9，`score-assistant-2`）

进度与阻断的完整说明见 `local/workbench/scores/score-p1/R卡进度与阻断.md`。

| 编号 | 作品与片段 | 谱源 | 交付文件 | 状态 | 编译结果 |
| --- | --- | --- | --- | --- | --- |
| **SCR-041** | 贝多芬 第14弦乐四重奏 Op.131 **I. Adagio ma non troppo e molto espressivo，弱起 + 印刷谱 mm.1–8**（Vn I 赋格主题、Vn II m.4 答题进入、Va m.8 末拍进入、Vc 全休止） | `local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet14-1.krn`（Kern，craigsapp 编；**文件头 OMV 误标 Mvmt.4，内容实为第一乐章**） | `local/workbench/scores/score-p1/beethoven-op131-i-mm1-8/beethoven-op131-i-mm1-8.ly`（+ `.pdf`/`.mid`/`page.png`）<br>核对记录：同目录 `核对记录.md` | **待独立核验**。八度基准已用已核验的 `beethoven-op131-i-mm6-11`（SCR-017）逐音校准（kern `c`=C4 标准约定，`es`=E♯）；力度位置与跨边界圆滑线/连音线按"片段内保留、越界删除"简化，已在核对记录 §6 逐条登记 | 0 error / 0 warning；MIDI 逐声部自查：Vn I 首音 G♯4、Vn II 首音 C♯4、Va G♯3、Vc 全休止 |
| **SCR-042** | 莫扎特 第六钢琴奏鸣曲 K.284 (205b) **I. Allegro，mm.17–24**（PianoStaff 双行；过渡段收束→三次击槌→抽空→A 大调副题起句） | `local/resources/scores/source-packages/humdrum/mozart-sonatas/0016-16-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 1.abc`（hum2abc 自 Humdrum kern `sonata06-1.krn` 转换，2021-01-14；L:1/16、M:C、K:D） | `local/workbench/scores/score-p1/mozart-k284-i-mm17-24/`（`.ly` + 核对记录 + pdf/mid/png） | **待独立核验**。事实更正两条：**三次击槌的左手和弦是 A–C♯–E（A 大调主和弦），不是 E–G♯–B**；**内聚裂隙实际是 m.21 第 4 拍双手同时休止 + m.22 左手整小节休止**（非"m.22 第 1 拍"）。详见核对记录 §2 | 0 error / 0 warning；MIDI：右手首和弦 E5/A5/C♯6、左手 A3/A4/G♯4… |
| **SCR-043** | 贝多芬 第14弦乐四重奏 Op.131 **VII. Allegro，mm.21–26** | `…/beethoven-string-quartets-main/…/kern/quartet14-7.krn` | `local/workbench/scores/score-p1/beethoven-op131-vii-mm21-26/` | **待独立核验**。Vn I C♯6–B♯5–A5–G♯5 下行 × Vc C♯3–D♯3–F♯3–E3 上行＝倒影对位；Va 为"每拍 8 分休止 + 8 分 G♯4"固定型；m.24 四声部 `p` | 0 error / 0 warning；MIDI 逐声部自查通过 |
| **SCR-044** | 贝多芬 Op.131 **VII. Allegro，mm.216–224** | 同上 `quartet14-7.krn` | `local/workbench/scores/score-p1/beethoven-op131-vii-mm216-224/` | **待独立核验**。实为 D 大调踏板华彩织体（Vc D2/A2 与 E2/A2 交替全音符、Va/Vn II 踏板、Vn I 在 F♯5–A6 间运动）；**是否为"终曲第二主题呈示"属学术判断，本助手不代认证**，建议学者按谱面确认是否换段 | 0 error / 0 warning；MIDI 含 A6(93)、F♯6(90) 等极值音 |
| R101 | 莫扎特 K.284 I mm.16–23 / 17–22 | 见 SCR-042 | — | **已交付 SCR-042**（取 mm.17–24，范围可再调） | — |
| **SCR-046** | 贝多芬 第九交响曲 Op.125 **I. Allegro ma non troppo, un poco maestoso，mm.1–35**（**13 谱表**，含 Corno 3,4；弦乐 A–E 五度 tremolo 写成重复和弦 `\tuplet 3/2 { <e' a>16 ×12 }`；A4 横向 3 页） | 同 SCR-045（CCARH MuseData `sym9-mvmt1.md2`，依 B&H 全集 / Bennion 2005；**非 CC0**）。**第二源核对**：`downloads/beethoven-op125-i/op125-i-20parts-musescore-pdmx.mxl`（CC0，source-assistant-2 提供的 `<transpose>` 证据：Cor in D −10、Cor 3,4 in B♭ basso −14、**Tr in D +2**、Cl in B −2、Basso −12）。工具 `md2_parse.py`/`md2_score.py`（per-part Q、**行首缩进=和弦音**、`P` 行忽略、移调实音、1/24 精确补足小节、`--barchecks` 逐小节定位）/`midi_events.py` | `local/workbench/scores/score-p1/beethoven-op125-i-mm1-35/`（`.ly` + 核对记录 + pdf 3 页/mid/png×3） | **待 verifier-6 核验**。入场：m.1 Vn II+Vc/圆号 → m.2 Vn I → m.4 Va+Cb → m.5 Cl → m.9 Ob → m.11 Fl → m.14 Fg → **m.15 Corno 3,4（写 E♮5/E♮4→实 D4/D3）** → **m.16 Tr+Timp 全奏**；开场并集 {A2,E3,A3,E4}＝空五度无三音。**m.21/m.23 的"第 2 声部"已按第二源改正为和弦音**（不再退为休止） | **0 error / 0 warning**（`\barNumberCheck` 逐小节核过 35 小节 × 13 声部） |
| **SCR-045** | 贝多芬 第九交响曲 Op.125 **I. mm.1–16**（早期版，**声部读法有误**：曾把前导空格当第 2 声部、小号误用 −10；仅作历史对照，**勿回填正文**） | 同上 | `local/workbench/scores/score-p1/beethoven-op125-i-mm1-16/` | 已被 SCR-046 取代 | 0/0（但读法已过时） |
| R201 | 贝多芬 Op.53 I mm.1–14 / mm.23–42 | `kern/sonata21-1.krn` | — | **已改派**（lead 改派 score-assistant-3；最小编辑方案已授权，另派 source-assistant-2 找第二谱源） | — |
| R301 第 2/3 段 | Op.131 VII mm.21–26、mm.216–224 | 同上 | — | **已交付 SCR-043 / SCR-044**（R301 三段齐） | 见上 |

---

## 2026-11-22 谱源登记：R2 资料请求（`task-14`，`source-assistant-2`）

本段**不登记交付谱例**，只登记"新入手的机器可读谱源与其许可"，供后续补谱/核验复用。汇总报告：`local/workbench/scores/score-p1/缺口报告-2-来源.md`；取件与核验脚手架：`local/workbench/scores/score-p1/downloads/_pdmx/`（含说明与日志）。每项均有独立 `来源与许可.md`（URL、抓取时间、许可、完整性、转换方式）。

| 编号 | 作品 / 片段 | 谱源（本地路径） | 类型与许可 | 用途与状态 |
| --- | --- | --- | --- | --- |
| **SRC-001** | 贝多芬 第九交响曲 Op.125 **第一乐章（全乐章 547 小节）** | `local/workbench/scores/score-p1/downloads/beethoven-op125-i/sym9-mvmt1.md2`（1,452,057 B）<br>URL：`https://bitbucket.org/musedata/beethoven/raw/master/bhl/orch/sym9/editions/public/score/mvt1.md2` | **CCARH MuseData**（`.md2` 文本，14 part，含 `measure N` 显式小节号）；文件头 `(C) 2002,2005 CCARH`，学术/教育用途，**非 CC0**；依 B&H 全集（Bennion 2005）转写 | **P1 清单 #4 主底本**（mm.1–35 可直取）；`Q:24` ⇒ 每小节 48 divisions 可作时值断言 |
| **SRC-002** | 同上（交叉核对） | `…/beethoven-op125-i/op125-i-20parts-musescore-pdmx.mxl`（541,180 B）、`…/op125-i-52parts-musescore-pdmx.mxl`（696,481 B） | **MusicXML**（MuseScore 用户转录，经 PDMX/Zenodo 15571083 取件）；**CC0 1.0**，`is_official=False` | 与 SRC-001 在"547 小节 / 2/4 / 前 16 小节每小节 2 拍"上一致；抽查音高用，不作主底本。**已用于核 SCR-046 的三处未决项**（圆号/小号移调方向、m.21/m.23 内声部性质、m.15 Corno 3,4 进入音），证据表：`local/workbench/scores/score-p1/downloads/beethoven-op125-i/第二源核对-op125.md` |
| **SRC-003** | 贝多芬 第二十一钢琴奏鸣曲 Op.53《华尔斯坦》**第一乐章** | `…/beethoven-op53/op53-waldstein-A-musescore-pdmx.mxl`（102,874 B，**小节号 0 起**）、`…/op53-waldstein-B-musescore-pdmx.mxl`（234,884 B，**整部三乐章、小节号 1 起**） | **MusicXML**（MuseScore 用户转录，PDMX）；**CC0 1.0** | **R201 第二谱源**：印刷谱 m.4/m.8/m.11 两源均为 4.0 拍，并据此判定 kern 的"4.5 拍"系解析口径问题（和弦/倚音），已通报 `score-assistant-3` |
| **SRC-004** | 贝多芬 第七交响曲 Op.92 **第二乐章（全乐章 278 小节）** | `…/beethoven-op92-ii/sym7-mvmt2.md2`（346,584 B）<br>URL：`https://bitbucket.org/musedata/beethoven/raw/master/bhl/orch/sym7/editions/public/score/mvt2.md2` | **CCARH MuseData**（13 part，`measure` 标记 3,550 个）；学术/教育用途，**非 CC0** | **Op.92 II 独立第三编码源**，供 `verifier-4` 复核未决项；该编码圆号记作 `Cor_1-2/(E)` |
| — | 贝多芬 Op.97《大公》I mm.1–12 | `…/beethoven-op97/_not-op97/beethoven-dmajor-trio-musescore-pdmx.mxl`（80,257 B，CC0） | MusicXML（PDMX） | **排除性证据**：`Allegro vivace e con brio` + 3/4 + 270 小节 ⇒ 非 Op.97，不得作底本；#1 仍为缺口 |
| — | 雷哈 Op.88 No.2 I mm.1–8 | 无机器可读源；IMSLP 仅扫描（手稿 F-Pn L.4503(1)，44 页）+ 分谱 PDF | — | **缺口**；更正上一轮"IMSLP 无扫描"的判断 |
| — | 马勒 第四 II mm.34–46 | 无总谱级机器可读源；IMSLP 仅 1 个 MXL（`#1037437`，第二乐章 **Vn1 分谱**排版文件，且下载被 JS 反爬拦截） | — | **缺口**；PDMX 无第四交响曲 |

> 取件与核对可复现说明：大归档 `PDMX.csv`（225,399,738 B）与 `mxl.tar.gz`（1,894,335,797 B）取用后已删除（腾出 ~2 GB），Zenodo 记录公开可重取；提取、扫描、逐小节核验脚本与输出全部留在 `downloads/_pdmx/`。**未绕过任何站点的人机校验/登录限制**（musescore.com 返回 Cloudflare 校验、imslp.org 文件下载走 JS 中转，均如实登记为阻塞）。


---

## 2026-11-22 R201 交付（`task-8`，`score-assistant-3`）

> **本节取代上面「R 卡」表里 R201 行的"阻断／未编码"状态。** R201 的"底本 m.4 / m.8 / m.11 各多出 0.5 拍"经独立复核**不成立**，原因是三条 kern 读法错误，**未做任何最小编辑**，按底本原样落谱。详情见两交付目录的 `核对记录.md` §0、§2。

**复核要点（三条读法坑，与 `source-assistant-2` / lead 的结论一致，本助手独立复算确认）**
1. `8qccc#` 是**倚音**（kern `q`），时值 **0**，不推进时间；
2. `([4ddd)` 是**四分**（附点会写 `4.ddd`）；
3. 同一 spine 内**空格分隔的多个 token = 同时发声的和弦**，不能相加 —— m.11 左手 `8GG] (8GL]` 是**一个八分和弦**（0.5），不是两个八分。
⇒ 统一口径"记录时间推进量 = 各 spine 剩余发声时值的最小值；`q`=0；同 spine 多 token=和弦"，mm.1–14 与 mm.23–42 **34/34 小节全部恰 4.00 拍**；LilyPond barcheck 0 警告。

| 编号 | 作品与片段 | 谱源 | 交付文件 | 状态 | 编译结果 |
| --- | --- | --- | --- | --- | --- |
| **SCR-045** | 贝多芬 第21钢琴奏鸣曲 Op.53《Waldstein》**I. Allegro con brio，mm.1–14**（主部 C 大调反复和弦 → G/B 收束 → 花彩 → **B♭ 大调下方大二度模进** → F/A → m.9 高点 → 半音下行低音 C2-B1-B♭1-A1-A♭1-G1 → m.13 延长 → m.14 新句；双行钢琴谱） | **主源**：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata21-1.krn`（`!!!OPS 53`／`*M4/4`／`*MM144`／`*k[]`）<br>**第二源 A**：`local/workbench/scores/score-p1/downloads/beethoven-op53/op53-waldstein-A-musescore-pdmx.mxl`（PDMX/Zenodo 15571083，CC0，file m.0=印刷 m.1）<br>**第二源 B**：同目录 `…-B-…mxl`（同来源，整部三乐章，小节号 1 起） | `local/workbench/scores/score-p1/beethoven-op53-i-mm1-14/beethoven-op53-i-mm1-14.ly`（+ `.pdf`/`.mid`/`page.png`）<br>核对记录：同目录 `核对记录.md` | **待独立核验**（生产者未自我认证）。三源比对：kern↔本交付 0 差异；**源 B↔本交付 14/14 完全一致**；源 A 仅 m.12 末拍左手和弦分歧（A 记 A1，kern/B/本交付记 C2）。音区三源一致：m.1 左手 36/43=C2/G2、右手 48/52=C3/E3（源 B 实测 MIDI 号）。圆滑线未转译（登记在 §4-3） | 0 error / 0 warning（LilyPond 2.26.0）；MIDI 两谱表 program=0 acoustic grand，总长 56.00 拍；右手 27 个音级 + 2 个倚音（C♯6/E6）全对，左手 16/16 全对 |
| **SCR-046** | 贝多芬 Op.53 **I. Allegro con brio，mm.23–42**（**B 大调属准备** 十六分琶音层 → m.29 收束／m.30 交接 → mm.31–34 八分对置层 → **m.35 E 大调副题进入**（底本 `dolce e molto legato`）→ mm.39–41 第二乐句＋**m.41 B1+B2 属持续音** → m.42 三连八分上行至 F♯♯5；双行钢琴谱，m.38／m.41 为两层声部） | 同 SCR-045 三源 | `local/workbench/scores/score-p1/beethoven-op53-i-mm23-42/beethoven-op53-i-mm23-42.ly`（+ `.pdf`/`.mid`/`page.png`）<br>核对记录：同目录 `核对记录.md` | **待独立核验**。三源比对：kern↔本交付 0 差异；**源 B↔本交付 20/20 完全一致**；源 A 7/20 分歧（mm.23–26 左手第二半小节音型、m.28、m.32、m.39），均以 kern+B 为准并逐条登记在 §5.2。**`dolce e molto legato` 定位印刷谱 m.35**（A 出现在其 file m.34，正是"A 从 0 起号"判据） | 0 error / 0 warning；MIDI 80.00 拍 = 20×4；右手 28/28、左手 24/24 音级与 kern 完全一致 |

**两源的许可与性质**：A、B 均为 musescore.com 用户转录经 PDMX 收录（`license: cc-zero`、`is_official=False`），**只作交叉核对，不取代 kern、不单独当原谱引用**；取得路径、许可与"两份转录的已知缺陷"见 `local/workbench/scores/score-p1/downloads/beethoven-op53/来源与许可.md`（`source-assistant-2` / `task-14`）。

**给后续 R 卡的可复用结论**：本谱集（craigsapp/beethoven-piano-sonatas 的 MuseData→kern 转写）有三条易踩的记法，核时值前必须先套：① `q` 倚音 = 0 时值；② 同一 spine 空格分隔多 token = 和弦（取最短时值，不累加）；③ `[` / `]` 是**连音线**（不是符杠），`L` / `J` 才是符杠。
