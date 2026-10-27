# local：配货工作区（不进 Git）

> 这个目录已在 `.gitignore` 里，**不会被提交**。放的是可重建的中间产物：
> 原始乐谱、切片工具、验证脚本。正文与 `NOTICE.md` 才是不可再生的资产。

---

## 目录

```
local/
├── README.md                    # 本文件
└── materials/
    ├── scores/                  # 配货后的 LilyPond 源码（817 个文件，8.6 MB）
    │   ├── full/                # 钢琴奏鸣曲
    │   ├── quartets/            # 弦乐四重奏
    │   ├── symphonies/          # 交响曲
    │   ├── chamber/             # 室内乐
    │   ├── concertos/           # 协奏曲
    │   ├── overtures/           # 序曲
    │   ├── variations/          # 钢琴变奏曲
    │   ├── mutopia/             # 零散单文件
    │   ├── raw/                 # 上游原样下载（未迁移），用于追溯
    │   └── raw2/                # 同上，第二批
    └── tools/                   # 切片与转换工具
```

**先看两份索引，不要一个个翻文件：**

| 文件 | 内容 |
| --- | --- |
| `materials/scores/CATALOG.md` | **全库目录**：每个体裁下有哪些作品、有没有 english 音名版 |
| `materials/scores/INDEX.md` + `BATCH2-INDEX.md` | 钢琴奏鸣曲两批的配货记录：来源 URL、许可、小节数、复现方式 |
| `materials/scores/<体裁>/INDEX.md` | 该批配货清单（室内乐、协奏曲、序曲、变奏曲各一份） |

四重奏与交响曲那两批没有单独 INDEX，来源与许可见仓库根 `NOTICE.md` 的源表。
每个作品目录里的命名约定：

| 文件 | 是什么 |
| --- | --- |
| `<id>.ly` | 主文件，已迁到 LilyPond 2.26.0，编译 0 error |
| `<id>-en.ly` | english 音名版（全库统一用这个音名体系） |
| `<id>.pdf` / `<id>.mid` | **没有搬进来**——可由 `.ly` 重新生成 |
| `INDEX.md` | 该批的配货清单：来源 URL、Mutopia 条目号、许可、小节数、编译结果、移调乐器 |

> 只搬了源码，没搬 PDF/MIDI/PNG：那部分占 160 MB，且随时能从 `.ly` 重编。

---

## 资料从哪来

**唯一主力源是 [Mutopia Project](https://www.mutopiaproject.org/) 的贝多芬目录：**

```
https://www.mutopiaproject.org/ftp/BeethovenLv/
```

40 个作品目录（`O2/`、`O10/`、`O13/`、`O18/`、`O37/`、`O55/`、`O67/`、`O92/`、`O111/` …），
匿名可下、无配额、无需 API key。每个目录下有两种形态：

- **单文件**：直接下 `<Name>.ly`；
- **多文件工程**：下 `-lys/` 子目录里的全部 `.ly`（主文件只是 `\include` 壳，音乐在声部文件里）。

**已覆盖的作品与体裁：**

| 体裁 | 作品 |
| --- | --- |
| 钢琴奏鸣曲 | Op.2/1、Op.10/1、Op.10/2、Op.13、Op.27/2、Op.31/2、Op.47、Op.49/1、Op.49/2、Op.57、Op.78、Op.79、Op.90、Op.111 |
| 弦乐四重奏 | Op.18 No.4（四乐章）、Op.59 No.3 II、Op.131（七乐章，迁移失败） |
| 交响曲 | Op.55《英雄》、Op.67 第五、Op.92 第七 |
| 室内乐 | Op.69 大提琴奏鸣曲（三乐章）、Op.47《克罗采》、Op.30 No.2、Op.11 三重奏、Op.17 圆号奏鸣曲、Op.137 五重奏赋格 |
| 协奏曲 | Op.37 第三钢琴协奏曲、Op.61 小提琴协奏曲（三乐章） |
| 序曲 | Op.62《科里奥兰》、Op.84《埃格蒙特》 |
| 变奏曲 | Op.76 六首变奏曲、Op.129 回旋随想曲 |

**许可**：除 Op.27 No.2（Berners 1908）与 Op.131（Eulenburg 1911）是 **CC BY-SA 2.5**，
其余全部为 Public Domain。逐条登记在仓库根 `NOTICE.md`。

**拿不到源的**：Op.35《英雄变奏曲》（Mutopia 无 `O35/`）、Op.101/106/109/110（晚期钢琴奏鸣曲）、
声乐与合唱（无弥撒、无歌剧）。这几处只能用占位或换例证。

---

## 工具怎么用

| 工具 | 用途 |
| --- | --- |
| `qcut.mjs` | 从**变量体**（`name = { ... }`）按小节切；支持任意拍号、弱起、`\repeat volta` 与音符同行 |
| `split.mjs` | 从 `\new Staff = "up"` 形式按小节切（钢琴谱用这个） |
| `transcode-note-names.py` | 荷兰语音名 → english；**内置守卫**，源已声明 english 时拒绝执行 |
| `render-bars.mjs` | 渲染带小节号的 PNG，用于核对谱面 |
| `bar-trace.mjs` | 用 `\barNumberCheck` 探针查某个位置是第几小节 |
| `check-article.mjs` | 抽出文章里的 lilypond 块逐个编译并统计汉字数 |
| `midi-verify.mjs` | MIDI 逐音比对（**已停用**：本项目不做音高校验） |

切片：

```powershell
node qcut.mjs <file.ly> <变量名> <startM> <endM> <每小节拍数>     # 变量体
$env:INCLUDE_PICKUP='1'; node qcut.mjs ...                        # 保留弱起
node split.mjs <file.ly> up|down <startM> <endM>                  # \new Staff 形式
```

---

## 丢了怎么办

这个目录整体可重建：按[配货管线](../../../opencadenza-dev-doc/music-wiki-知识生产/score-pipeline.md)
从 Mutopia 重下、`convert-ly` 迁移、转 english、编译，大约半天。

**真正不可再生的只有 `content/` 与 `NOTICE.md`。**
