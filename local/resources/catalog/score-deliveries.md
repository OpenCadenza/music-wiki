# 谱例交付履历与谱源追溯表 (Score Deliveries Registry)

> [!CAUTION]
> **核验预警（2026-11-16 独立核验结论）**：
> 经谱例专职助手 `assistant-scores-a` 独立逐音比对原谱核验（详见 [核验报告](../../workbench/scores/assistant-scores-a/核验报告.md)），此前交付的 **SCR-001、SCR-002、SCR-003 三段谱例均判定为【有差异】且存在实质错误**（海顿右手整体高八度/左手低八度；莫扎特左手凭空加音吞休止符/m.10 越界至 MIDI 19 超出 88 键钢琴物理下限；贝多芬 Op.74 中提琴低八度/大提琴越界至 C2 以下）。
> **上述三段已从正文撤出并禁止直接引用，正由谱例专职助手重新独立对谱编码**。本记录完整保留作为溯源与质检教训。

本表记录由资料与谱例协作团队向学者交付的自包含 LilyPond 2.26.0 乐谱片段，明确记录其原始数据来源、精确取音行号/小节定位、核对状态与编译验证结果。本目录纳入 Git 版本控制，确保交付谱例具备完整的版本回溯与可复现性。

---

## 交付清单

| 编号 | 作品与作品号 | 乐章与小节 | 谱源原件与精确取音定位 | 交付文件路径 | 交付助手 | 状态 | 编译结果 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCR-001** | 海顿（J. Haydn）<br>《G大调第42钢琴奏鸣曲》Hob. XVI:27 | III. Presto<br>mm. 1–8（含弱起 `\partial 8`） | **原件路径**：`local/origin_resources/corpus/lilypond/HaydnFJ/HOB-XVI-27/hob-xvi-27-iii-presto/hob-xvi-27-iii-presto.ly`<br>**精确定位**：<br>- 右手高音部 `MD`：第 34–44 行；<br>- 左手低音部 `MS`：第 256–267 行。<br>**底本说明**：C. F. Peters (1880s) / Mutopia Project 权威排版源。 | [haydn-hob-xvi-27-mvt3-mm1-8.ly](../../resources/scores/haydn-hob-xvi-27/haydn-hob-xvi-27-mvt3-mm1-8.ly) | resource-assistant | **独立核验未通过【有差异】**<br>右手高八度、左手低八度。已撤出正文，待专职重编。 | LilyPond 编译通过，但音高有误 |
| **SCR-002** | 莫扎特（W. A. Mozart）<br>《G大调钢琴奏鸣曲》K. 283 (189h) | I. Allegro<br>mm. 1–10（含弱起 `\partial 4`） | **原件路径 1（ABC/Kern）**：`local/origin_resources/corpus/abc/humdrum-kern/mozart_sonatas/0013-13-Piano Sonata No. 5 in G major, K 283 (189h), mvmt. 1.abc`<br>**定位**：第 25–46 行。<br>**原件路径 2（MusicXML）**：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/XML/mozart, k283.xml`<br>**底本说明**：新莫扎特全集（NMA）与 Humdrum 数字化原谱。 | [mozart-k283-mvt1-mm1-10.ly](../../resources/scores/mozart-k283/mozart-k283-mvt1-mm1-10.ly) | resource-assistant | **独立核验未通过【有差异】**<br>左手加音吞休止符、m.10 出现 MIDI 19 越界。已撤出正文，待专职重编。 | LilyPond 编译通过，但音高/节奏有误 |
| **SCR-003** | 贝多芬（L. v. Beethoven）<br>《降E大调第10弦乐四重奏“竖琴”》Op. 74 | I. Poco adagio<br>mm. 1–9 | **原件路径 1（Kern）**：`local/origin_resources/corpus/abc/humdrum-kern/beethoven_quartets/0038-38-String Quartet No. 10 in E_b Major, Op. 74 mvt 1.abc`<br>**原件路径 2（DCML）**：`local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n10op74_01.mscx` 与 `local/resources/scores/dcml-abc/n10op74_01.notes.tsv` | [beethoven-op74-mvt1-mm1-9-adagio.ly](../../resources/scores/beethoven-op74/beethoven-op74-mvt1-mm1-9-adagio.ly) | 预备轮录入 / resource-assistant 验证 | **独立核验未通过【有差异】**<br>中提琴低八度、大提琴低于最低弦 C2。已撤出正文，待专职重编。 | LilyPond 编译通过，但音高有误 |
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
