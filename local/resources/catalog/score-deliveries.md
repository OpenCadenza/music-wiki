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
| **SCR-004** | 贝多芬（L. v. Beethoven）<br>《F大调第16弦乐四重奏》Op. 135 | IV. Der schwer gefaßte Entschluß<br>Grave, mm. 165–172 | **原件路径（Kern）**：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet16-4.krn`<br>**定位**：第 887–960 行。 | 任务处理中（task-11） | 归 `assistant-scores-c` 专职编码 | 任务处理中 | 待专职助手编码与核验 |

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
