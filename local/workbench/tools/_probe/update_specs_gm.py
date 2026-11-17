import io

# README：表格行 + 乐器章节
p = r"README.md"
t = io.open(p, encoding="utf-8").read()

t = t.replace("| 乐器 | 每个 `\\new Staff` 写 `midiInstrument` + `% GM <编号>` |",
              "| 乐器 | 每个 `\\new Staff` 写标准 General MIDI 乐器名的 `midiInstrument` |")

old = """### 乐器与 GM 编号（必填）

每个 `\\new Staff` 都要声明 MIDI 乐器，并在紧邻的一行写出 General MIDI 编号：

```lilypond
\\new Staff = "up" {
  \\set Staff.midiInstrument = "violin"
  % GM 40
  ...
}
```

`midiInstrument` 决定 LilyPond 的名字映射，`% GM <编号>` 是给构建脚本的权威值：脚本按注释
里的 0–127 程序号设置该声部，两者不一致时以编号为准。不要混用 1–128 的编号表。
乐器名称无效时可能回落到钢琴，非钢琴作品尤其要明确 GM 编号。

移调乐器的 `\\transposition` 也按 `\\language "english"` 的音名写：B♭ 调写 `\\transposition bf`、
E♭ 调写 `ef`、D 调写 `d`。写成 `bes` 会在 english 下报 `Expecting pitch, found bes`。
乐器名要写 LilyPond 认可的写法：钢琴 `"acoustic grand"`（**不是** `"acoustic grand piano"`），
小提琴 `"violin"`，中提琴 `"viola"`，大提琴 `"cello"`。名字写错会有 `no such MIDI instrument`
警告，并静默退回钢琴。"""

new = """### 乐器（必填）

每个 `\\new Staff` 都要声明 MIDI 乐器，`midiInstrument` 必须使用标准 General MIDI 乐器名：

```lilypond
\\new Staff = "up" {
  \\set Staff.midiInstrument = "violin"
  ...
}
```

构建脚本按乐器名解析 General MIDI 程序号，名字就是唯一的权威值；`pnpm validate` 会拒绝
非标准名称。非标准乐器请取最接近的标准名称（例如民族乐器取音色相近的管弦乐器），
不要自造名字。

乐器名要写 LilyPond 认可的写法（与 LilyPond `scm/lily/midi.scm` 的 128 个 GM 名称一致）：
钢琴 `"acoustic grand"`（**不是** `"acoustic grand piano"`），小提琴 `"violin"`，
中提琴 `"viola"`，大提琴 `"cello"`，圆号 `"french horn"`，竖琴 `"orchestral harp"`。
名字写错会有 `no such MIDI instrument` 警告，并静默退回钢琴。

移调乐器的 `\\transposition` 也按 `\\language "english"` 的音名写：B♭ 调写 `\\transposition bf`、
E♭ 调写 `ef`、D 调写 `d`。写成 `bes` 会在 english 下报 `Expecting pitch, found bes`。"""

if old in t:
    t = t.replace(old, new, 1)
    print("README 章节已替换")
else:
    print("README 章节未匹配")
io.open(p, "w", encoding="utf-8", newline="\n").write(t)

# 偏好文档：替换 GM bullet
p2 = r"local\docs\偏好-知识库写作.md"
t2 = io.open(p2, encoding="utf-8").read()
old2 = "- **每个 `\\new Staff` 声明乐器**：`\\set Staff.midiInstrument = \"…\"`，紧邻一行写 `% GM <编号>`。**2026-11-17 决定暂缓统一**：现有围栏仍用旧写法（`instrumentName` + `midiInstrument`），后续迁移时以上述写法为准。"
new2 = "- **每个 `\\new Staff` 声明乐器**：`\\set Staff.midiInstrument = \"标准 General MIDI 乐器名\"`。**不写 GM 编号，也不写 `instrumentName`**（谱面不显示乐器名）；乐器名就是唯一权威值，非标准名会被 `pnpm validate` 拒绝。名字写法见 README（钢琴 `\"acoustic grand\"`、圆号 `\"french horn\"` 等）。"
if old2 in t2:
    t2 = t2.replace(old2, new2, 1)
    print("偏好文档 bullet 已替换")
else:
    print("偏好文档 bullet 未匹配")
io.open(p2, "w", encoding="utf-8", newline="\n").write(t2)

# 角色提示词
p3 = r"local\docs\实施记录\2026-11-16-DSH首批\角色提示词.md"
t3 = io.open(p3, encoding="utf-8").read()
old3 = "> - 每个 `\\new Staff` 声明乐器与 0–127 的 GM 编号（格式见 README：`\\set Staff.midiInstrument` + 紧邻 `% GM <编号>`；本分支现有围栏暂用旧写法，新写一律按 README）。"
new3 = "> - 每个 `\\new Staff` 用 `\\set Staff.midiInstrument = \"标准 General MIDI 乐器名\"` 声明乐器（不写 GM 编号，也不写 `instrumentName`）；乐器名写法见 README 的《乐器》一节。"
if old3 in t3:
    t3 = t3.replace(old3, new3, 1)
    print("角色提示词 已替换")
else:
    print("角色提示词 未匹配")
io.open(p3, "w", encoding="utf-8", newline="\n").write(t3)