# 配货管线

> 核验日期：2026-10-27
> 全部命令在 Windows + LilyPond 2.26.0 下实测通过；Linux/CI 只需替换路径。

配货指把公开乐谱变成"可切片、可编译、english 音名"的 LilyPond 源码。
**这一步不做音高校验**——编译通过即可入库，准确性交人工复核。

## 流程

```mermaid
flowchart LR
  A[下载 .ly / -lys 目录] --> B[convert-ly 迁到 2.26.0]
  B --> C[编译 0 error]
  C --> D[音名转 english]
  D --> E[编译 0 error]
  E --> F[按小节切片]
  F --> G[嵌入文章 + 编译]
```

## 工具位置

| 工具 | 说明 |
| --- | --- |
| LilyPond 2.26.0 | 自带 `bin\python.exe`、`bin\convert-ly.py`、`bin\musicxml2ly.py` |
| `convert-ly.py` | 语法迁移。**结果打到 stdout**，不是原地改 |
| `transcode-note-names.py` | 荷兰语音名 → english，见下文 |
| `split.mjs` | 按小节切分 LilyPond 声部体（写手侧自建工具，可按需重写） |
| `qcut.mjs` | 支持**变量体**（`name = { ... }`）、任意拍号、弱起、`\repeat volta` 与音符同行的情况；四重奏切片用它 |

本机曾把远端源码放在工作区的 `.work/scores/`（不入 Git）。**该目录不是权威资产**，
丢失后按本文重跑即可；真正要保留的是最终嵌进文章的谱例块与 `NOTICE.md` 登记。

## 步骤 1：下载

见[资料来源](sources.md)。单文件下一份，多文件下整个 `-lys/` 目录。

**下载后必须校验文件大小。** 这一步踩过大坑：一次多文件下载静默失败，五个 `.ly` 全部变成
0 字节，转换器给空输入加上 `\language "english"` 行，产出 20 字节的文件；后续编译
"0 error" 通过（空谱表当然不报错），整条链路看起来是绿的，实际没有任何音符。

```powershell
Get-ChildItem *.ly | Select-Object Name, Length |
  Where-Object { $_.Length -lt 500 }        # 有输出就说明下载坏了
```

经验阈值：单声部文件通常 4–10 KB，主文件（多文件工程的 `\include` 壳）1–3 KB。
低于 500 字节一律视为失败，重下。

## 步骤 2：convert-ly 迁移

```powershell
$lp   = '<lilypond-2.26.0 安装目录>'
$src  = 'op2no1-i-src.ly'
$out  = 'op2no1-i.ly'

$ver = (Select-String -Path $src -Pattern '^\\version\s+"([^"]+)"' |
        Select-Object -First 1).Matches[0].Groups[1].Value

& "$lp\bin\python.exe" "$lp\bin\convert-ly.py" --from=$ver --to=2.26.0 $src > $out 2>$null
```

要点：

- **必须重定向 stdout**。`convert-ly` 没有 `--output` 选项；直接传文件名不会原地生效，
  结果会打到标准输出。踩过一次，文件头仍是旧版本号，白欢喜。
- `--from` 用文件里实际的版本（见过 2.8.0、2.10.3、2.12.0），不要一律写 2.10.3。
- 迁移后 `\version` 必须是 `"2.26.0"`，且全块只能出现一次。

## 步骤 3：编译

```powershell
& "$lp\bin\lilypond.exe" -dno-point-and-click -o op2no1-i op2no1-i.ly *> op2no1-i.log
Select-String -Path op2no1-i.log -Pattern ': error:|fatal'
```

判定标准：**0 error**。warning 可以接受（`decrescendo too small` 之类很常见），
但出现 `fatal error` 或退出码非 0 必须修。

## 步骤 4：音名转 english

全库统一 `\language "english"`，否则 agent 抄代码会踩音名不匹配。

```powershell
& python transcode-note-names.py in.ly out.ly
```

映射表（荷兰语 → english）：

```text
aes→af  bes→bf  ces→cf  des→df  ees→ef  fes→ff  ges→gf
ais→as  bis→bs  cis→cs  dis→ds  eis→es  fis→fs  gis→gs
aeses→aff  beses→bff  ceses→cff  deses→dff  eeses→eff  feses→fff  geses→gff
aisis→ass  bisis→bss  cisis→css  disis→dss  eisis→ess  fisis→fss  gisis→gss
```

三个易错点，都是实测踩出来的：

1. **必须处理重升重降**。Op.111 里出现 `eeses`，漏了会报 `not a note name`。
2. **前瞻不能排除数字**。音名后紧跟时值（`ees4`、`aes8.`），前瞻若写成
   `(?![A-Za-z0-9_])` 会漏掉这些；正确写法只排除字母：`(?![A-Za-z])`。
3. **只处理代码区**。跳过 `"..."` 字符串、`%` 行注释、`%{ %}` 块注释；
   `\markup { \italic "con espressione" }` 里的词不能被当成音名。

迁移后 `\language` 若原本是 `"nederlands"` 要改成 `"english"`；没有该行时补在 `\version` 之后。

多文件工程：对每个 `.ly` 各转一份，输出到新目录并**保持原文件名**，再编译主文件。
注意 include 的文件名大小写（Op.111 主文件写的是 `LVB_Sonate_111_1_1.ly`，下载到的是小写，
Windows 不报错但 Linux CI 会挂，按 include 的字面大小写重命名）。

### 音名转换：不要用手抄映射表

`transcode-note-names.py` 早期版本用手抄的映射表，**漏了 nederlands 的 `es`、`eses`、`as`**。
nederlands 里 `es` = 降 E（`ees` 的别名），english 里 `es` = 升 E——漏掉之后降 E 会变成升 E，
整首差一个半音，**而编译依然 0 error**。Op.62 上游有大量裸 `es`，
旧表产出 base 与 `-en` 的 PDF 差 47 KB（`\key es \major` 成了升 E 大调）。

现行做法：映射表**直接从 LilyPond 自带的
`share/lilypond/2.26.0/scm/lily/define-note-names.scm` 解析**（67 条），不手抄。
自检方法：同一份源码转前转后各编一次 MIDI，`SHA256` 应完全相同。

另一个偶发故障：LilyPond 2.26.0 偶尔以 `0xC0000005` 崩溃，日志里没有任何 error 行。
这是进程级偶发，与源码无关（同一文件重跑通常即过）。批处理脚本应对非 0 退出码自动重试
（≤3 次）并在日志里记 `attempt N`，不要把崩溃当成源码错误去改谱。
## 步骤 5：切片

目标：从整乐章里取 8–20 小节，双手/全声部，拼成自包含 `\score`。

**转码前必须先判源语言。** 有些上游源本来就是 english 音名（`\include "english.ly"` 或
`\language "english"`）。对这类源套 nederlands→english 映射会把 `as`（升 A）改成 `af`（降 A）、
`es`（升 E）改成 `ef`（降 E）——每音差一个半音，**编译依然 0 error**。
现行脚本已内置守卫：检测到源声明 english 就拒绝执行并退出（不产出文件），
确认真是 nederlands 时加 `--force` 覆盖。

另外两个不在 convert-ly 覆盖范围内的坑：

- `\applyMusic #unfold-repeats` 在 2.26 里签名变成 `(types music)`，convert-ly 不处理，
  报 `Wrong number of arguments` 且**退出码非 0 但日志里没有 `: error:` 行**。手工改成
  `\unfoldRepeats \theScore`。
- 取小节号的探针必须在**剥掉 `\midi` 输出**的副本里编译。用了 `\unfoldRepeats` 的谱表，
  第二遍解释会把 `currentBarNumber` 抬到展开反复之后的号（实测把某段起点从 83 报成 97）。
### 定位小节号

最可靠的办法是让 LilyPond 自己报：

```lilypond
\barNumberCheck #49
```

插到候选位置，编译时若实际不是第 49 小节，报错信息会告诉你"实际在第几小节"。
比数行、比从 MIDI 推都准。**注意 `\cadenzaOn` 段落会让小节号与通行版脱节**
（Op.111 的 Maestoso 就是这样），这类段落不要写"第 X 小节"，直接用占位。

### 切分

- 每个 `\new Staff` 的声部体可以独立切；四重奏要四处一起取。
- 切完后必须补上下文：`\clef`、`\key`、`\time`、`\tempo`、`\language`。
- 去掉 `\repeat volta`、`\header`、`\tagline`。
- 保留力度、连音线、倚音、延长记号——它们是论证的一部分。

### 编译

切片本身也要 0 error。四声部谱例的常见错误是漏了某个声部的 `\set Staff.midiInstrument`。

## 嵌入文章：三个必填项

| 项 | 写法 | 缺失后果 |
| --- | --- | --- |
| 标题与定位 | 围栏属性 `title="贝多芬 Op.2 No.1 第一乐章" location="mm.1–10"` | 播放器标题退化成"页面标题 (1)"，且没有位置副标题 |
| 速度 | `\tempo 4 = 190`，照抄来源乐章 | 默认 60 bpm，播放明显偏慢 |
| 乐器 | `\set Staff.midiInstrument = "acoustic grand"` + `% GM 0` | 退回钢琴音色 |

乐器名要写 LilyPond 认可的写法：钢琴 `"acoustic grand"`（**不是** `"acoustic grand piano"`，
后者会警告并静默退回钢琴）、`"violin"`、`"viola"`、`"cello"`。GM 编号：钢琴 0、
小提琴 40、中提琴 41、大提琴 42。

## 已知故障

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| `.ly` 只有几十字节，编译却"0 error" | 下载静默失败，得到空输入 | 校验文件大小，低于 500 字节重下 |
| 迁移后文件仍是旧版本号 | convert-ly 结果打到 stdout | 重定向到新文件，别指望原地改 |
| `not a note name: eeses` | 未处理重升重降 | 补 `eeses→eff` 一类映射 |
| `not a note name: bes`（转换后） | 前瞻排除了数字，`bes4` 漏转 | 前瞻只排除字母 |
| 播放比预期慢一倍以上 | 缺 `\tempo` | 补速度标记 |
| 音色是钢琴但作品不是 | 缺 `% GM` 或乐器名拼错 | 补注释，改正名字 |
| `unknown command: \p '` | MuseScore → musicxml2ly 的畸形力度 | 见[资料来源](sources.md)，该路线暂不可用 |
| LilyPond 退出码 `0xC0000005` | 10 MB 级 MusicXML 转换产物 | 按乐章切小再转；当前放弃该路线 |
| 小节号与通行版不符 | `\cadenzaOn` 段落 | 不写小节号，改占位 |
| Linux CI 找不到 include 文件 | 文件名大小写不一致 | 按 include 的字面大小写重命名 |

## 管弦乐总谱的特殊处理

总谱比钢琴谱多三件事，缺一件就会得到"看起来对、听起来错"的谱例：

1. **移调乐器要写 `\transposition`。** 源文件的 `\key c \major` 是**记谱调**，
   不是实际音高。Op.92 引子里单簧管 in A、圆号 in A、小号 in D，
   对应 `\transposition a`、`\transposition a`、`\transposition d`。不写的话播放会整体移调。
   判断方法：读 `\set Staff.instrumentName`，里面通常写着 "in A" / "in D"。
2. **GM 编号按乐器组分配。** 长笛 73、双簧管 68、单簧管 71、大管 70、圆号 60、
   小号 56、定音鼓 47、小提琴 40、中提琴 41、大提琴 42、低音提琴 43。
3. **`\compressFullBarRests` 在 2.26 已移除。** 老总谱源会报 `unknown command`；
   `convert-ly` 会自动换成 `\compressEmptyMeasures`，所以**先跑 convert-ly 再编译**，
   不要手工删这一行。

另外两条实测结论：

- Mutopia 的 `O92/Symphony7_1` 标 4/4，看着像错版——它其实是第七交响曲的 **Poco sostenuto 引子**
  （引子确实是 4/4，后面的 Vivace 才是 6/8）。切片前先看 `\tempo`/`\markup` 里的段落名，
  不要凭"我记得是 6/8"就判它错。
- `O67/beethoven_fifth_op67` 是**钢琴缩编**，`O67/Symphony5_1` 才是总谱。
  同一个作品在 Mutopia 可能同时存在缩编与总谱，目录名里的 `Symphony`/`sonate` 字样可以初步区分，
  最终以文件里是否有 `flauti`/`oboi`/`corni` 等分谱判断。

## 配货完成的标准

一个乐章算配货完成，当且仅当：

1. `<id>.ly` 是 2.26.0，编译 0 error。
2. `<id>-en.ly` 是 english 音名，编译 0 error。
3. 来源、版次、许可、Mutopia 条目号已登记进 `NOTICE.md`。

满足这三条就可以交给写手切片，不再做进一步校验。
