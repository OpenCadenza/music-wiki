# 资料来源与下载方式

> 核验日期：2026-10-27
> 结论均来自本机实测（2026-10-26/27 两轮配货），不是文档推测。

知识库的硬约束是：**谱例必须是真实作品**。因此素材源的第一要求不是"全"，而是
"能拿到机器可读编码，且许可允许再分发"。按这个标准，可用性排序如下。

## 来源分级

| 级别 | 来源 | 形态 | 实测结论 |
| --- | --- | --- | --- |
| A | **Mutopia Project** | LilyPond `.ly` 源码 | **主力源，推荐**。convert-ly 迁移后直接可用，覆盖贝多芬钢琴奏鸣曲与部分四重奏 |
| B | OpenScore 四重奏/艺术歌曲 | MuseScore / MusicXML | 语料齐全（CC0），但 **MusicXML → LilyPond 转换实测失败**，见下文 |
| C | IMSLP | 公有领域扫描件 PDF | 兜底。需要人工转录，成本高，只在 A/B 都没有时考虑 |
| 不推荐 | MuseScore.com 用户谱 | MuseScore / MusicXML | 与 B 同一转换通道，同样失败；且许可逐曲不同 |

## A：Mutopia Project

站点：<https://www.mutopiaproject.org/>
贝多芬目录：<https://www.mutopiaproject.org/ftp/BeethovenLv/>
可读的作品清单：<https://www.mutopiaproject.org/cgibin/make-table.cgi?Composer=BeethovenLv>

### 目录结构

```text
https://www.mutopiaproject.org/ftp/BeethovenLv/<Opus>/<PieceFolder>/
```

`<Opus>` 形如 `O2`、`O10`、`O18`、`O131`、`WoO78`。`<PieceFolder>` 形如
`LVB_Sonate_02no1_1`、`pathetique-1`、`quartet_o131`。

每个作品目录里可能有：

| 文件 | 说明 |
| --- | --- |
| `<Name>.ly` | 单文件源码，直接下载 |
| `<Name>-lys/` | 多文件工程，主文件 `\include` 其余文件；**必须整个目录一起下** |
| `<Name>-lys.zip` | 上一条的打包版 |
| `<Name>.mid` | 参考 MIDI |
| `<Name>-a4.pdf` | 参考排版稿，人工复核时对照用 |
| `<Name>.rdf` | 元数据（部分曲目缺少有效内容） |

### 下载命令

单文件：

```powershell
$base = 'https://www.mutopiaproject.org/ftp/BeethovenLv'
Invoke-WebRequest -Uri "$base/O2/LVB_Sonate_02no1_1/LVB_Sonate_02no1_1.ly" `
  -OutFile 'op2no1-i-src.ly' -UseBasicParsing
```

多文件（先列目录再全下）：

```powershell
$dir = "$base/O111/lvb_sonate_111_1/lvb_sonate_111_1-lys/"
$files = ([regex]::Matches(
  (Invoke-WebRequest -Uri $dir -UseBasicParsing).Content,
  'href="([^"]+\.ly)"') | ForEach-Object { $_.Groups[1].Value }) | Sort-Object -Unique
New-Item -ItemType Directory -Force -Path 'op111-lys' | Out-Null
foreach ($f in $files) {
  Invoke-WebRequest -Uri "$dir$f" -OutFile "op111-lys\$f" -UseBasicParsing
}
```

**不要**按"最短的含 `\score` 的文件"自动挑主文件。Op.27 No.2 的 zip 里有 3 个乐章 ×
2 种纸张共 6 个文件，自动挑选会选到第二乐章。必须点名下载。

### 覆盖情况（实测，2026-10-27）

钢琴奏鸣曲：

| 作品 | 可得乐章 |
| --- | --- |
| Op.2 No.1 | 第一至第四乐章 |
| Op.10 No.1 | 第一、第三乐章 |
| Op.10 No.2 | 第一至第三乐章 |
| Op.13《悲怆》 | 第一至第三乐章 |
| Op.27 No.2《月光》 | 全曲（多文件） |
| Op.31 No.2《暴风雨》 | 第一、第二乐章 |
| Op.49 No.1 / No.2 | 各两个乐章 |
| Op.57《热情》 | **第二、第三乐章**（无第一乐章） |
| Op.78 / Op.79 / Op.90 | Op.78 两乐章、Op.79 三乐章、Op.90 两乐章 |
| Op.111 | 第一乐章（多文件工程，3 个 `.ly`） |

**缺失**：Op.53、Op.101、Op.106、Op.109、Op.110。晚期奏鸣曲除 Op.111 外都没有机器可读源。

弦乐四重奏：

| 作品 | 状态 |
| --- | --- |
| Op.18 No.4 | 四个乐章全部（多文件，5 个 `.ly`） |
| Op.59 No.3 | 第二乐章（多文件，5 个 `.ly`） |
| Op.131 | 全七乐章（多文件，42 个 `.ly`） |
| Op.74 / Op.95 / Op.127 / Op.130 / Op.132 / Op.133 / Op.135 | **无** |

其他可用目录：O11、O17、O30、O37、O40、O47、O50、O55、O61、O62、O66、O67、O69、O72b、
O76、O81b、O84、O92、O129、O137、WoO29/30/55/59/78/82。这些多为其他体裁，接第三轮之前
先按需确认音色与编制。

### 许可

Mutopia 逐曲标注，**必须逐曲读**，不能用"Mutopia 都是公有领域"概括。已知两类：

| 类型 | 例子 | 义务 |
| --- | --- | --- |
| Public Domain | Op.2 No.1、Op.10、Op.13、Op.31/2、Op.57、Op.111 | 无附加义务，仍建议署名排版者 |
| CC BY-SA 2.5 | Op.27 No.2（Berners 1908）、Op.131（Eulenburg 1911） | 必须署名 + 以相同许可共享改编 |

读取方式：单文件看 header 的 `copyright` 与 `footer` 字段；多文件工程里 header 常在
主文件的 `\header` 块，`footer` 形如 `Mutopia-2007/08/11-1022`，末段数字即 Mutopia 条目 ID。

## B：OpenScore（CC0 但转换失败）

- 仓库：<https://github.com/OpenScore/StringQuartets>
- 目录页（含逐曲 MusicXML 下载）：<https://fourscoreandmore.org/openscore/stringquartets/>
- 覆盖：贝多芬 Op.18 全套、Op.59/3、Op.127、Op.130、Op.131、Op.133、Op.135，**许可 CC0**

**实测结论：这条路当前不可用。** 流程与本机失败点：

1. 从 fourscoreandmore 下载 `.mxl`（本质是 zip，内含 `score.xml`，单曲 9–10 MB）。
2. `musicxml2ly.py score.xml -o out.ly` —— 能出文件（Op.131 约 340 KB）。
3. 编译**失败**。原因：MuseScore 导出的文字力度（`sempre pp`、`più p`、`più cresc.`）
   被转成畸形宏：

   ```text
   "               sempre pp" = #(make-dynamic-script ""               sempre pp"")
   ```

   内层引号未转义，LilyPond 直接语法错误；后续还会出现 `unknown command: \p '` 这类用法。
4. 预处理 MusicXML（删掉全部 `<other-dynamics>`，Op.131 共 58 处）后错误降到 3 条，
   但仍报 `Guile signaled an error` 与 `not an articulation`；继续修引号后
   **LilyPond 进程崩溃**（退出码 `0xC0000005`，访问冲突），怀疑与 10 MB 级输入规模有关。

如果将来要复活这条路，建议方向：先把 MusicXML 按乐章切小（单乐章 2–3 MB），
再逐个转换；或在转换后做一遍"宏定义块剔除 + 力度降级为 `\p`/`\f`"的后处理。
不要指望 `--nd`（`--no-articulation-directions`）能解决——实测无效。

## C：IMSLP（兜底）

<https://imslp.org/> 。贝多芬作品页有 Breitkopf & Härtel (1862–1865) 等公有领域扫描件。
只在前两级都拿不到时使用，且**不要自己转录**——转录一个乐章的工作量超过写一篇文章。
正确做法：先把选题写出来、谱例位置留占位，把 IMSLP 链接登记进 `NOTICE.md` 的待补条目。

## 许可登记规则

每个用到的谱例都要在仓库根 `NOTICE.md` 登记两处：

1. **来源清单**：来源 ID、作品、排版底本、排版者、许可、链接。
2. **按文章登记**：文章路径、谱例小节范围、来源 ID。

正文**不写**来源、版次、页码或许可。这条边界是硬规则，见
[内容规范](https://github.com/OpenCadenza/music-wiki/blob/main/README.md)。

## 找不到源时怎么办

**不要放弃选题。** 按以下顺序处理：

1. 换一个能拿到谱例的作品来说明同一个问题（同一技法通常有多部作品可证）。
2. 换同类体裁（钢琴奏鸣曲拿不到，就从四重奏取）。
3. 仍拿不到：正文照常写，谱例位置写占位行：

   ```markdown
   **贝多芬 Op.110 第三乐章，mm.1–20**

   > 谱例待补：Op.110 第三乐章 mm.1–20。
   ```

占位行保留作品、作品号、乐章、小节范围，后续补谱时不必重写正文。
占位清单与数量以[进度文档](progress.md)的汇总为准，本文不复写数字，避免两处漂移。
