# R 卡进度与阻断说明（2026-11-22，score-assistant-2）

本轮 `task-4`（P1 补谱六处）已完成并 complete；以下为 R101/R201/R301 三张卡的**进度与阻断**。
凡是"没把握"的地方一律不编码、不猜（宁可交缺口说明，也不交可能错八度的谱）。

---

## R101（task-10）：莫扎特 K.284 I mm.16–23 或 17–22 —— **无源，未编码**

| 检查 | 结果 |
| --- | --- |
| 本地 `local/resources/scores/source-packages/` | 只有 `beethoven-score-sources`（钢琴奏鸣曲 kern + 弦乐四重奏 kern）与 `humdrum/bach-370-chorales`；**无莫扎特奏鸣曲 kern/ABC** |
| 本地 `local/resources/text/open-music-theory/.../Graphics/form/XML/` | 14 个 XML 里莫扎特只有 `mozart, k283.xml`、`mozart, k330,ii.xml`、**`k284-ii.xml`（第二乐章）**——**没有 K.284 第一乐章** |
| 本地 `local/origin_resources/` | 本工作树与主检出均**不存在**该目录（此前的 `humdrum-kern/mozart_sonatas/*.abc` 记录不在当前机器可读范围内） |
| Mutopia | `ftp/MozartWA/` 目录清单无 `KV284`（本轮实抓，见下） |
| IMSLP | 该曲只有扫描 PDF，无 MusicXML |

Mutopia 莫扎特目录实抓（节选，证明无 KV284）：
`Anh41 AveverumM K6deest KV2 KV130 KV137 KV153 KV154 KV158 KV183 KV191 KV229 KV250 KV265 KV299 KV309 KV315 KV331 KV349 KV351 KV379 KV387 KV397 KV401 KV407 KV412 KV417 KV421 KV428 KV447 KV453a KV457 KV458 KV464 KV465 KV477 KV478 KV487 KV488 KV495 KV498 KV517 KV518 KV519 KV520 KV522 KV523 KV525 KV527 KV545 KV546 KV560b KV574 KV581 KV594 KV620 KV622 KV626`（<https://www.mutopiaproject.org/ftp/MozartWA/>）

**下一步（任一即可）**：① 由资料助手取 Humdrum `mozart/sonatas` 语料的 K.284 第一乐章 kern（KernScores/kern.humdrum.org 或 GitHub 镜像），我即可编码；② 或用登录会话从 MuseScore 导出 MXL；③ 或学者指定改用有源可查的同类例子。

---

## R201（task-8）：贝多芬 Op.53 I mm.1–14 与 mm.23–42 —— **源已定位，但底本存在八度不自洽，未定稿**

底本：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata21-1.krn`
（`!!!OPS: 53`、`!!!OTP: Waldstein`、`!!!OMV: 1`、`!!!OMD: Allegro con brio`、`*M4/4`、`*MM144`、`*C:`、`!!!ENC: Craig Stuart Sapp (2023-03-19 修订)`；**kern 八度约定已用另一份已核验片段校准，见下**。）

**问题**：同一条右手声部里，m.3 的和弦写作 `D`+`G`（kern 标准 = D3+G3），而 m.4 的花彩写作 `ddd`（= D6），两者相差 **3 个八度**，不可能是同一乐句的真实音区：

```
=3  RH: 4.D (4.G      % D3 + G3（1.5 拍）→ 16B 16A → 8G'   （右手此时仍是低音谱号）
=4  RH: (8qccc# ([4ddd) 16ddd 16ccc 16bb 16aa 4gg')        % C♯6→D6→…→G5（已换高音谱号）
```

同样地，m.1–2 的右手和弦 `C`+`E`（= C3+E3）、m.5–6 的 `BB-`+`D`（= B♭2+D3）与 m.4 的 D6 花彩也不在同一音区。两种可能：**(a)** 底本 mm.1–3（及 5–6）的和弦整体记低了 1–2 个八度；**(b)** 花彩整体记高了。二者相差一个八度还是两个八度，只有看印刷谱（Durand/Dukas 参考版或 Bärenreiter）第 1 页才能定。

**为什么不能自己定**：这不是"音高抄错"而是"八度归属"问题，猜错就是整段高/低一个八度——正是前几轮交付被退回的典型缺陷（SCR-003/SCR-034 都栽在八度上）。按"不造谱、不硬猜"，此处停下等一次人工对照。

**下一步（30 秒可定）**：请有谱面的一方看一眼 Op.53 第一乐章第 1–4 小节，回答两个问题：① m.1–2 两手的重复和弦是否在**中央 C 附近**（RH 约 C4+E4、LH 约 C3+G3）？② m.4 花彩的顶点是 **D5 还是 D6**？答案一到，我按同一个八度基准编码 mm.1–14 与 mm.23–42（结构已解析完毕，随时可出谱）。
另：学者请求里的"mm.1–14 主部主题…半音下行到属音 G"与"mm.23–42 B 大调属准备 → E 大调副题"两处的**小节边界我也需要核一遍**（kern 的调号/`*>` 段落标记可给，但"属音 G 出现在 m.14"这类断言应由谱面确认，我不替学者认证音乐分析）。

---

## 附：kern 八度约定校准（本轮做成的工具与结论，供所有后续 kern 任务复用）

- 工具：`local/workbench/scores/score-p1/tools/kern_dump.py`（**kern 双/多谱表按小节 dump，`--ly` 输出 LilyPond 音名**）。
- 校准方法：拿**已入正文且经独立核验**的 `content` 片段 `beethoven-op131-i-mm6-11`（底本 `S2-D2-beethoven-op131-m6-11.ly`）与同语料的 `quartet14-1.krn` 逐音比对：
  - kern `a` → .ly `a'`（A4）；kern `ee` → `e''`（E5）；kern `dd#` → `ds''`（D♯5）；kern `cc#` → `cs''`（C♯5）；kern `e#` → `es'`（english 下 `es` = E**♯**）——**逐项吻合，无冲突**。
  - 结论：该语料 **kern 八度约定 = 标准（`c` = 中央 C，`cc` = C5，`C` = C3）**，可放心用于绝对音高。
- 附带记录：`quartet14-1.krn` 文件头 `!!!OMV: Mvmt. 4` / `!!!OMD: Adagio ma non troppo e molto cantabile` 与实际内容（第一乐章 C♯ 小调赋格，2/2，MM69）**不符**，属文件头元数据错误；引用该文件时勿以文件头乐章号为准。
- 这套校准直接用于 **R301 第 1 段**（已交付，见 §R301）。

---

## R301（task-9）：贝多芬 Op.131 三段 —— 第 1 段已交付，第 2/3 段未做

| 学者请求 | 状态 |
| --- | --- |
| ① 第一乐章 mm.1–8（Vn I 赋格主题 + Vn II 答题） | **已交付**：`local/workbench/scores/score-p1/beethoven-op131-i-mm1-8/`（`.ly` + 核对记录 + pdf/mid/png）。0 error / 0 warning；底本 `quartet14-1.krn`；八度已按 §附 校准；MIDI 逐声部自查通过。**待独立核验** |
| ② 第七乐章 Allegro mm.21–26（Vn I 与大提琴倒影对位） | **未做**：需先定位 `quartet14-7.krn` 的乐章块并核小节号（该语料文件头乐章号不可靠，见 §附） |
| ③ 第七乐章 Allegro mm.216–224（D 大调/那不勒斯音级的终曲第二主题） | **未做**：同上 |

第 2/3 段可直接沿用本轮的工具与校准（`kern_dump.py`），下一轮约一段 15–20 分钟即可出谱。
