# 谱例交付履历与谱源追溯表 (Score Deliveries Registry)

本表记录由资料与谱例协作团队向学者交付的自包含 LilyPond 2.26.0 乐谱片段，明确记录其原始数据来源、精确取音行号/小节定位、核对状态与编译验证结果。本目录纳入 Git 版本控制，确保交付谱例具备完整的版本回溯与可复现性。

---

## 交付清单

| 编号 | 作品与作品号 | 乐章与小节 | 谱源原件与精确取音定位 | 交付文件路径 | 交付助手 | 状态 | 编译结果 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCR-001** | 海顿（J. Haydn）<br>《G大调第42钢琴奏鸣曲》Hob. XVI:27 | III. Presto<br>mm. 1–8（含弱起 `\partial 8`） | **原件路径**：`local/origin_resources/corpus/lilypond/HaydnFJ/HOB-XVI-27/hob-xvi-27-iii-presto/hob-xvi-27-iii-presto.ly`<br>**精确定位**：<br>- 右手高音部 `MD`：第 34–44 行（mm. 1–8，包含弱起 `d8`、Meyer 呈示 1-7-2-1、Passo Indietro 模进与停顿）；<br>- 左手低音部 `MS`：第 256–267 行（mm. 1–8，和弦与低音声部对位）。<br>**底本说明**：C. F. Peters (1880s) / Mutopia Project 权威排版源。 | [haydn-hob-xvi-27-mvt3-mm1-8.ly](../../resources/scores/haydn-hob-xvi-27/haydn-hob-xvi-27-mvt3-mm1-8.ly) | resource-assistant | 已核对，待 `assistant-scores-a` 独立核验 | LilyPond 2.26.0 编译通过，生成 `.pdf` 与 `.mid` |
| **SCR-002** | 莫扎特（W. A. Mozart）<br>《G大调钢琴奏鸣曲》K. 283 (189h) | I. Allegro<br>mm. 1–10（含弱起 `\partial 4`） | **原件路径 1（ABC/Kern）**：`local/origin_resources/corpus/abc/humdrum-kern/mozart_sonatas/0013-13-Piano Sonata No. 5 in G major, K 283 (189h), mvmt. 1.abc`<br>**定位**：第 25–46 行（弱起 `d3B` 及 mm. 1–10 完整呈示与延续终止句）。<br>**原件路径 2（MusicXML）**：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k283.xml`<br>**定位**：Part 1（右手）与 Part 2（左手）的 Measure 1 至 Measure 10 逐音对位比对。<br>**底本说明**：新莫扎特全集（NMA）与 Humdrum 数字化原谱。 | [mozart-k283-mvt1-mm1-10.ly](../../resources/scores/mozart-k283/mozart-k283-mvt1-mm1-10.ly) | resource-assistant | 已核对，待 `assistant-scores-a` 独立核验 | LilyPond 2.26.0 编译通过，生成 `.pdf` 与 `.mid` |
| **SCR-003** | 贝多芬（L. v. Beethoven）<br>《降E大调第10弦乐四重奏“竖琴”》Op. 74 | I. Poco adagio<br>mm. 1–9 | **原件路径 1（Kern）**：`local/origin_resources/corpus/abc/humdrum-kern/beethoven_quartets/0038-38-String Quartet No. 10 in E_b Major, Op. 74 mvt 1.abc`<br>**原件路径 2（DCML）**：`local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n10op74_01.mscx` 与 `local/resources/scores/dcml-abc/n10op74_01.notes.tsv`<br>**底本说明**：全 4 声部总谱（Violin I/II, Viola, Cello），慢引子外声部骨架与加兰特模型变形。 | [beethoven-op74-mvt1-mm1-9-adagio.ly](../../resources/scores/beethoven-op74/beethoven-op74-mvt1-mm1-9-adagio.ly) | 预备轮录入 / resource-assistant 验证 | 已核对，待 `assistant-scores-a` 独立核验 | LilyPond 2.26.0 编译通过，生成 `.pdf` 与 `.mid` |
| **SCR-004** | 贝多芬（L. v. Beethoven）<br>《F大调第16弦乐四重奏》Op. 135 | IV. Der schwer gefaßte Entschluß<br>Grave, mm. 165–172 | **原件路径（Kern）**：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet16-4.krn`<br>**定位**：第 887–960 行（乐章第二次 3/2 拍处；中提琴与大提琴重现问句动机 G-E-Ab，高音声部连续震音与增三和弦）。 | 任务分配中（task-11） | 归 `assistant-scores-c` 专职编码 | 任务处理中 | 待编码与编译 |

---

## 规范与质量保证

1. **真实谱源溯源**：每一条谱例必须写明本地文件路径与物理行号/小节，严禁脱离谱源凭记忆复原，严禁自编织体冒充原作。
2. **声部完整性**：
   - 键盘作品必须双行大谱表全声部；
   - 弦乐室内乐必须全声部总谱；
   - 若只能交付声部摘录，必须在 `title` 与 `location` 中明示“摘录”与实际声部。
3. **技术要求**：
   - LilyPond 2.26.0 语法；
   - `\language "english"`；
   - GM 乐器程序号 (0–127)；
   - 速度标记、拍号与弱起对齐。
