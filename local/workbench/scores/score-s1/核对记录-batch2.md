# 谱例交付核对记录 —— 第二批（编制轴）

批次：2026-11-17（第二批）。目标：四篇"编制"文章的全部谱例占位（8 个目标片段）。
工具：LilyPond 2.26.0；`midi_pitch_check.py` 自查。
输出目录：`local/workbench/scores/score-s1/`（新文件名，未覆盖第一批 8 个片段）。

---

## 0. 本批结果总览

| # | 目标片段 | 状态 | 交付文件 |
|---|----------|------|----------|
| 1 | Reicha Op.88 No.2 第一乐章 mm.1–8（管乐五重奏） | **缺口**（无机器可读谱源） | — |
| 2 | Nielsen Op.43 第一乐章 mm.1–12（管乐五重奏） | **缺口**（无机器可读谱源） | — |
| 3 | Beethoven Op.97《大公》第一乐章 mm.1–12（钢琴三重奏） | **缺口**（无机器可读谱源） | — |
| 4 | Schubert D.929 第二乐章 mm.1–21（钢琴三重奏） | **缺口**（无机器可读谱源） | — |
| 5 | Haydn Op.76 No.3《皇帝》第二乐章 mm.1–20（弦乐四重奏） | **完成**（mm.1–20 主题，含弱起） | `haydn-op76-3-mvt2-mm01-20-emperor.{ly,pdf,mid}` |
| 6 | Beethoven Op.135 第三乐章 mm.1–12（弦乐四重奏） | **完成** | `beethoven-op135-mvt3-mm01-12.{ly,pdf,mid}` |
| 7 | Beethoven Op.14 No.1 第一乐章 mm.1–16（钢琴独奏） | **部分完成**（摘录 mm.1–4；mm.5–16 未编码） | `beethoven-op14-1-mvt1-mm01-04-excerpt.{ly,pdf,mid}` |
| 8 | Beethoven Hess 34（Op.14 No.1 弦乐四重奏改编）对应片段 | **缺口**（无机器可读谱源，且与原作对照未成） | — |
| — | 文章 4 的 Op.97 mm.1–12（复用） | **缺口**（同 #3） | — |

> 缺口原因统一说明见 §4：五件作品在本地资源（`scholar-plan-dev/local/resources/scores` 与 `origin_resources/corpus`）、OpenScore 语料、hfm-weimar MusicXML 库、Mutopia、IMSLP、ScoreSynth 中均无**可用的 MusicXML/Kern 谱源**；IMSLP 仅有 PDF 扫描件。按"绝不编造音高或小节号"的边界，不从扫描件强行转写。

---

## 1. 已交付片段：来源与核对

### 1.1 Haydn Op.76 No.3「皇帝」第二乐章 mm.1–20（`haydn-op76-3-mvt2-mm01-20-emperor.ly`）

- **来源**：OpenScore String Quartets 语料（CC0）`sq20428156.mxl`
  - `github.com/OpenScore/StringQuartets` → `scores/Haydn,_Joseph/String_Quartet_in_C_major,_Hob.III77,_Op.76_No.3/sq20428156.mxl`
  - 下载件：`E:\...\scholar-plan-dev\local\origin_resources\downloads\2026-11-17\s1\haydn-op76-3.mxl`（197,968 bytes）
  - 转写者：mozbadel（MuseScore 4.7.4），据 IMSLP #28079 转写；CC0。
- **转换与核对方式**：`Expand-Archive` 解包 → `musicxml2ly` 转换 → **并用 Python 直接解析 score.xml 的 `<note>/<rest>/<backup>/<chord>/<tie>` 逐小节提取**（每声部、每音高、每时值、连音线、和弦）作为编码依据。
- **小节定位**：MusicXML 中第二乐章以 `measure number="0"`（前导弱起）开始，键 `1` 个升号（G 大调）、拍号 2/2；据此定位 mm.0–20。**实际范围 = 弱起 + mm.1–20（主题呈示段）**；变奏一（mm.21 起）未含。第四拍（= 末小节）为主题收束的短小节（弱起互补），以隐藏休止补齐编译小节。
- **逐小节核对结论**（与 MusicXML 提取一致）：

| 小节 | Vn1（主旋律） | Vn2 | Va | Vc |
|------|--------------|-----|----|----|
| 弱起 | G4· A4(8) | B3· D4(8) | G3(4) r4 | G3(4) r4 |
| 1 | B4 A4 C5 B4 | G4 F#4 A4 G4 | r2 D4 D4 | r2 F#3 G3 |
| 2 | A4(8) F#4(8) G4 E5 D5 | C4 B3 C5 B4 | F#3(8) A3(8) G3 r2 | D3 G2 r2 |
| 3 | C5 B4 A4 B4(8) G4(8) | F#4 G4 E4(2) | A3 B3 E4 G3 | D3 G3 C3 C#3 |
| 4 | D5(2) G4· A4(8) | D4(2) B3· D4(8) | F#3(2) G3 r4 | D3(2) G3 r4 |
| 5–8 | 与 1–4 构成重复加大（m.8 收 D5(2) A4 B4） | 平行三度声部 | 内声部轮转 | 低音进行 |
| 9–10 | A4(8) F#4(8) D4 C5 B4 ／ A4 F#4 D4 D5 C5 | F#4 r F#4 G4 ／ F#4 r B4 A4 | D4 r A3 G3(8) B3(8) ／ D4 r D4 E4(8) F#4(8) | D3 r D3 D3 ／ D3 r B2 C3(8) D3(8) |
| 11 | B4· B4(8) C#5 C#5(8) D5(8) | G4· G4(8) F#4(8) | G4 G3 E4 E4(8) D4(8) | E3(2) A2 A2 |
| 12 | D5(2,♩fermata) G5· F#5(8) | F#4(2) [G3+G4]· G4(8) | D4(2) [G3+D4](2) | D3(2) B3· B3(8) |
| 13–15 | 半音装饰句（F#5 E5 D5 …） | 同型声部 | 内声部 | 低音支持 |
| 16–19 | 与 12–15 同型高八度/变奏 | 同型 | 同型 | 同型 |
| 20 | G4(2) | G4(2) | B3(2) | G2(2) |

  说明：m.12 女高音 D5 带延长记号（源 `d2 ^\fermata`）✓；m.12/m.16 的 G5 带 `fz`（源 `_\\fz`）✓；m.14 的 A4 处 `p`（源 `_\\p`）✓；开头 `p dolce` ✓。
- **已知取舍**：MusicXML 的 P1（小提琴 I）内部另有一个仅含休止与一个重复 A4 的残留第二声部（转录瑕疵），**未纳入**；vln1 m.15/m.19 的 B4 为**倚音**（MusicXML 中时值为 0），按 `\grace` 记写。

### 1.2 Beethoven Op.135 第三乐章 mm.1–12（`beethoven-op135-mvt3-mm01-12.ly`）

- **来源（三源交叉）**：
  1. 本地 Kern `quartet16-3.krn`（文件头：Mvmt. 3；Lento assai, cantante e tranquillo；*D-:；*M6/8；*MM40）
  2. 本地 DCML `n16op135_03.notes.tsv`（逐音 midi/duration_qb 核对）
  3. OpenScore String Quartets `sq12397213.mxl`（CC0；下载件 `downloads\2026-11-17\s1\beethoven-op135.mxl`）——用于裁定 m.7 次中音时值
- **逐小节核对结论**：

| 小节 | Vn1 | Vn2 | Va | Vc |
|------|-----|-----|----|----|
| 1 | （全小节休止） | 前 3/8 休止 → A♭3·（连至 m.2） | F3（全小节，连至 m.2） | 全小节休止 |
| 2 | D♭4·（连）→ [D♭4+F4]· | A♭3·（中）→ A♭3·（收） | F3·（中）→ F3·（收） | 前 3/8 休止 → [D♭2+D♭3]· |
| 3 | D♭4 C4 B♭3 A♭3 B♭3 C4（六八分，一弧） | A♭3（整小节，起连） | F3·→G♭3·（连弓） | 上：A♭2（整小节）；下：D♭2·（连弓）→E♭2· |
| 4 | D♭4 E♭4 F4（弧）→ E♭4· | A♭3（整小节，收连） | F3· G♭3· | 上：A♭2；下：D♭2·→C2· |
| 5 | D♭4 C4 B♭3 A♭3 B♭3 C4（弧） | A♭3（整小节，起连） | F3·→G♭3·（弧） | 上：A♭2；下：D♭2·→E♭2· |
| 6 | D♭4 E♭4 F4（弧）F4(8)→E♭4(4) | A♭3·（收连）→A♭3 C4 B♭3（三连八分弧） | F3(4) D♭3(8) C3(4) E♭3(8，连至 m.7) | [D♭2+A♭2]· → A♭2(4) G♭2(8) |
| 7 | F4 F4(8) F4(8)→D♭4 B♭3（弧） | A3·（附点四分）→B♭3·（附点四分） | E♭3(4，收连) C3(8) D♭3· | F2· B♭2· |
| 8 | B♭4 B♭4(8) B♭4(8)→G♭4 E♭4（弧） | F4(4) B♭3(8，起连)→B♭3·（收连） | D3(4) F3(8) G♭3· | D2· E♭2· |
| 9 | A♭4 A♭4(8) A♭4(8)→F4 D♭4（弧） | E♭4(4) [A♭3+E♭4](8，A♭3 连)→A♭3·（收连） | G♭3(4) E♭3(8) F3· | C2· D♭2(4) F2(8) |
| 10 | A♭3(8) F4 E♭4（弧）→D♭4· | D♭4(4) C4(8) A♭3·（起连） | F3(4) G♭3(8) F3· | A♭2· D♭3(8) F2(8) G♭2(8) |
| 11 | D♭4(4) C4(8)（弧）→D♭4(8) F4 G♭4（弧） | A♭3·（收连）A♭3(8) D♭4(4) | F3(4) G♭3(8) F3(4) D♭3(8) | A♭2(8) F3(8) E♭3(8) D♭3(4) B♭2(8) |
| 12 | A♭4 F5 E♭5（弧）→D♭5 B♭4 G♭4（弧） | F4 A♭4 G♭4 F4 D♭4 D♭4（六八分） | D♭3(4) C3(8) F3(8) G♭3(8) E♭3(8) | A♭2· D♭3(8) D♭3 D♭3 |

- **源间裁定**：
  1. **m.7 次中音**：Kern/DCML 均记 `4.An/ + 4.B-/]`（2/8+3/8=5/8，小节时值不足）；OpenScore 记 **A3 附点四分 + B♭3 附点四分**（3/8+3/8=6/8）。本谱取 OpenScore 读法（自洽完整），备注 Kern 此处缺附点。
  2. **m.8 次中音**：三源一致为 F4(4)+B♭3(8,连)+B♭3·(收连) = 6/8 ✓。
  3. 大提琴 mm.3–5 为**双声部**（上声部持续 A♭2 附点二分，下声部为进行低音 D♭2→E♭2/C2），以 `<< \voiceOne … \\ \voiceTwo … >>` 记写。
  4. 大提琴 m.6 的 A♭2 记为四分（Kern `(4AA-/` 无附点；与 DCML duration_qb=1.0 一致）。
- **力度**：Kern 无 dynam 层，本谱不添加力度记号（文章"pp/sotto voce"为叙述性描述，非谱面标记）。

### 1.3 Beethoven Op.14 No.1 第一乐章 mm.1–4（摘录，`beethoven-op14-1-mvt1-mm01-04-excerpt.ly`）

- **来源**：本地 Kern `sonata09-1.krn`（OPS 14；ONM 1；OMV 1；Allegro；*E:；*M4/4；*MM132），行 20–53（`=1-` 至 `=4`）
- **核对结论**：
  - m.1：右手 B4（二分）＋[E4+E5]（二分）；左手 8 分休止 + (E3,G♯3,B3) 八分和弦×3 + 八分休止 + ×3
  - m.2：右手 C♯5 ＋[F♯4+F♯5]；左手同型 A 大三和弦 (E,A,C♯)
  - m.3：右手 D♯5 ＋[B4+B5]；左手同型 (E,F♯,A,D♯)
  - m.4：左手附点二分和弦 (E3,G♯3,B3,E4) + 四分休止；右手 B4· + C♯6(16) D♯6(16) + E6(4) + 四分休止
  - 全部音高/时值与 Kern 一致；左手记作**同时发声的八分和弦**（Kern 用空格子记号表示和弦；文章称"分解和弦"为叙述性措辞，谱面按 Kern）。
- **实际范围**：**mm.1–4（摘录）**，未含 mm.5–16。

---

## 2. 缺口清单（五件作品 + 两处依赖）

| 工作 | 已查证的无源情况 |
|------|------------------|
| **Reicha Op.88 No.2** | 本地资源、OpenScore、hfm-weimar（Beethoven/Schubert 等在前，无 Reicha）、Mutopia、GitHub 均无可读 MusicXML/Kern；IMSLP 仅 PDF 扫描（1818 年版） |
| **Nielsen Op.43** | 同上；IMSLP 仅 PDF（1922 年版扫描 + 分谱），无 MusicXML/MXL/MSCZ |
| **Beethoven Op.97《大公》** | 本地无钢琴三重奏谱源；OpenScore StringQuartets 仅四重奏；hfm-weimar 无三重奏；IMSLP 仅 PDF 分谱/总谱 |
| **Schubert D.929** | 同上；IMSLP 仅 PDF |
| **Beethoven Hess 34** | 无任何机器可读谱源；IMSLP 无对应页（检索标题未命中） |
| 文章 4 的 Op.97 复用 | 同 Op.97 缺口 |

> 处理原则：不从扫描件强行逐音转写（无法达到"经核对"标准）；如需这些片段，建议下一轮以"人工读取权威扫描并双人复核"或购买/获取 urtext MusicXML 后再做。

## 3. 编译与 MIDI 自查

| 文件 | 编译 | MIDI 自查（midi_pitch_check.py） |
|------|------|----------------------------------|
| haydn-op76-3-mvt2-mm01-20-emperor | ✓ Success，零 warning/barcheck | 311 音；声部音域 Vn1 D4–G5、Vn2 G3–C5、Va D3–B4、Vc C2–C4 ✓；全部 88 键内 |
| beethoven-op135-mvt3-mm01-12 | ✓ Success，零 warning/barcheck | 144 音；Vn1 A♭3–F5、Vn2 A♭3–A♭4、Va C3–G♭3、Vc C2–F3 ✓；全部 88 键内 |
| beethoven-op14-1-mvt1-mm01-04-excerpt | ✓ Success，零 warning/barcheck | 77 音；RH E4–E6、LH E3–E4 ✓；全部 88 键内 |

## 4. 交付文件与来源清单

```
local/workbench/scores/score-s1/
├── haydn-op76-3-mvt2-mm01-20-emperor.{ly,pdf,mid}
├── beethoven-op135-mvt3-mm01-12.{ly,pdf,mid}
├── beethoven-op14-1-mvt1-mm01-04-excerpt.{ly,pdf,mid}
└── 核对记录-batch2.md（本文件）
```

下载件（按约定存 `scholar-plan-dev\local\origin_resources\downloads\2026-11-17\s1\`）：
- `haydn-op76-3.mxl`（OpenScore StringQuartets，CC0，197,968 B）
- `beethoven-op135.mxl`（OpenScore StringQuartets，CC0，235,822 B）
