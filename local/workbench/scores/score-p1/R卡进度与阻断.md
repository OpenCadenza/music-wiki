# R 卡进度与阻断说明（2026-11-22，score-assistant-2）

本文件随每次交付更新。当前：**R101 已交付、R301 三段全部交付、R201 阻断（需一次决策）**。凡"没把握"处一律不编码。

---

## R101（task-10）：莫扎特 K.284 I —— **已交付（待独立核验）**

- 文件：`local/workbench/scores/score-p1/mozart-k284-i-mm17-24/`（`.ly` + 核对记录 + pdf/mid/png）
- 取段：**mm.17–24**（说明见核对记录 §2：要覆盖"过渡段蓄积 → 三次击槌 → 抽空 → 副题起句"，23–24 不可省）
- 底本：`local/resources/scores/source-packages/humdrum/mozart-sonatas/0016-16-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 1.abc`
- 编译：**0 error / 0 warning**；MIDI 逐手自查（右手首和弦 76/81/85 = E5/A5/C♯6；左手 57/69/68/69…）
- **两条要请学者注意的事实**：① 三次击槌的左手和弦是 **A–C♯–E（A 大调主和弦）**，不是 E–G♯–B；② 内聚裂隙实际是 **m.21 第 4 拍双手同时休止 + m.22 左手整小节休止**，不是"m.22 第 1 拍"。
- 建议围栏：`title="莫扎特 第六钢琴奏鸣曲 K.284 第一乐章" location="Allegro，mm.17–24" id="mozart-k284-i-mm17-24"`

---

## R301（task-9）：贝多芬 Op.131 三段 —— **三段全部交付（待独立核验）**

| 段 | 文件 | 编译 | 备注 |
| --- | --- | --- | --- |
| ① I. Adagio，弱起 + mm.1–8 | `score-p1/beethoven-op131-i-mm1-8/` | 0/0 | Vn I 赋格主题、Vn II m.4 答题、Va m.8 末拍进入、Vc 全休止 |
| ② VII. Allegro，mm.21–26 | `score-p1/beethoven-op131-vii-mm21-26/` | 0/0 | Vn I C♯6–B♯5–A5–G♯5 下行 × Vc C♯3–D♯3–F♯3–E3 上行＝倒影；Va 为 G♯ 固定伴奏型 |
| ③ VII. Allegro，mm.216–224 | `score-p1/beethoven-op131-vii-mm216-224/` | 0/0 | D 大调踏板织体（Vc D2/A2 与 E2/A2 交替）+ Vn I 华彩；**未必是"第二主题呈示**"，见该段核对记录 §2 与 §5-3 |

- 三段均用同一份 kern 语料（`quartet14-1.krn` / `quartet14-7.krn`），八度基准已用已核验的 `beethoven-op131-i-mm6-11` 校准（kern `c`=C4 标准；english `es`=E♯ 与 kern `e#` 一致）。
- 三段共同的未决：逐音未与印刷谱比对；圆滑线（底本 `(`/`)` 多为跨小节乐句线）一律未转译；速度写 `2 = 120`（＝四分音符 240，与底本 `*MM240` 同值，底本未标计时单位）。

---

## R201（task-8）：贝多芬 Op.53 I —— **阻断：底本小节时值不闭合（需决策）**

底本：`.../beethoven-score-sources/beethoven-piano-sonatas-main/.../kern/sonata21-1.krn`（`OPS 53` / `OGP: Waldstein` / `Allegro con brio` / `*M4/4` / `*MM144`）。

**音区问题已按 lead 指示解除**：m.1–2 左手 C2+G2、右手 C3+E3，m.4 花彩 D6 属正常跨度，按 kern 原样编码，不再以此停手。

**新的阻断点（与音区无关，是时值）**：把 kern 的音符按标准读法逐小节累加，有 **3 个小节右手/左手超过 4 拍**，LilyPond 的小节校验必然报错，必须做一次编辑决定才能落谱：

| 小节 | 声部 | 底本 token 序列（kern 原文） | 累加 | 差 |
| --- | --- | --- | --- | --- |
| **m.4** | RH | 装饰 `8qccc#` + `([4ddd)`（附点四分 1.5）+ `16dddLL] 16ccc 16bb 16aaJJ`（1.0）+ `4gg')`（1.0）+ `4r`（1.0） | **4.5** | +0.5 |
| **m.8** | RH | 装饰 `8qbb` + `([4ccc)`（1.5）+ `16cccLL] 16bb- 16aa- 16ggJJ`（1.0）+ `4ff')`（1.0）+ `4r`（1.0） | **4.5** | +0.5 |
| **m.11** | LH | `4GGG 4FF`（1.0）+ `[2GGz\ [2Gz\`（2.0）+ `8GG] (8GL]`（1.0）+ `16AL 16BJJ`（0.5） | **4.5** | +0.5 |

对照：m.3 / m.7（同型花彩）恰好 4.0 拍闭合（`4.D(4.G` 1.5 + `16BLL 16AJJ` 0.5 + `8G')` 0.5 + `8r` 0.5 + `4r` 1.0），m.12 / m.14 也闭合。**所以不是我的读法整体错，而是 m.4 / m.8 / m.11 这三处底本自身多出半拍**（同一文件此前已被 verifier 查出 `\transposition` 系统性高八度，属同类转写缺陷）。

**两条可选出路（请 lead 定一条，我立即出谱）**：

- **(a) 授权最小编辑**：m.4/m.8 末尾的 `4r` 读作 `8r`（附点和弦 1.5 + 四十六分 1.0 + 四分 1.0 + 八分休止 0.5 = 4.0）；m.11 的 `16AL 16BJJ` 后移入 m.12，或把 `[2GGz` 的半音符读作附点二分减一次…（这一处更麻烦，建议三处都按"四分符 + 八分休止"或"移半拍入下小节"统一处理，并在核对记录逐条登记）。**这是编辑决定，不是音高猜测。**
- **(b) 换第二谱源**：用 MuseScore/Mutopia 的 Op.53 片段交叉核对后再定。我在本机没有第二套 Op.53 机器可读源（`source-packages` 只有这一份 kern；IMSLP Op.53 只有扫描 PDF）。

我倾向 **(b) → (a)**：先取第二源核对 m.4/m.8/m.11，若第二源也显示"附点四分 + 四分 + 其余"，就按 (a) 落谱并双源登记。请给一句话指示。

---

## 附：本轮可复用工具（`local/workbench/scores/score-p1/tools/`）

| 工具 | 用途 |
| --- | --- |
| `kern_dump.py` | kern 多谱表按小节 dump（`--ly` 输出 LilyPond 音名）；已支持时值前置休止（`8r`）、前导修饰记号、和弦 |
| `kern2ly.py` | kern → LilyPond 骨架（实验性，长于机械搬运，律动复杂处仍需人工） |
| `ly_bar_positions.py` | Mutopia 分谱逐小节"是否发声"矩阵（用于判断谁在第几小节进入） |
| `midi_probe.py` | MIDI 逐 track 音高/程序号自查 |
| `transposition_probe.ly` | 实测 LilyPond `\transposition` 语义（`a`＝下小三度、`e`＝下小六度、`e'`＝上大三度） |

---

## R201 已交付并解除阻断（2026-11-22，`score-assistant-3`）

> 上面 R201 节的"阻断／需决策"**已作废**。原文的"m.4 / m.8 / m.11 各多 0.5 拍"是**解析口径错**，不是底本缺陷（lead 与 `source-assistant-2` 的复核结论，本助手独立复算确认）。

**三条读法错误（本谱集 MuseData→kern 转写的坑）**
1. `8qccc#` 的 `q` = **倚音，零时值**，不能按八分计入（原表把它当 0.5 拍的是另一处错；原表实际是漏了这条，导致另一侧多算）；
2. `([4ddd)` 是**四分 1.0**（附点会写 `4.ddd`，原表当 1.5）；
3. 同一 spine 内**空格分隔多 token = 同时发声的和弦** —— m.11 左手 `8GG] (8GL]` 是**一个八分和弦 0.5**（原表当两个八分 = 1.0）。

**统一口径**：数据记录的时间推进量 = 各 spine **剩余发声时值的最小值**；`"."` 延续；`q`=0；同 spine 多 token = 和弦（取最短、不累加）；`[`/`]` 是**连音线**，`L`/`J` 才是符杠。
**结果**：mm.1–14 与 mm.23–42 **34/34 小节全部恰 4.00 拍**（kern 解析 + LilyPond barcheck 双证）；**未做任何最小编辑**。

**交付**
- `score-p1/beethoven-op53-i-mm1-14/`（`.ly` + `核对记录.md` + pdf/mid/png）—— SCR-045
- `score-p1/beethoven-op53-i-mm23-42/`（同上）—— SCR-046
- 第二谱源（PDMX/MuseScore CC0 两份 MusicXML）由 `source-assistant-2` 取回于 `score-p1/downloads/beethoven-op53/`；**源 B 与交付两段 34/34 小节逐音完全一致**，源 A 有 8 处独异（逐条登记在核对记录 §5）。
- 登记：`local/resources/catalog/score-deliveries.md`「2026-11-22 R201 交付」节。**待独立 verifier**。
