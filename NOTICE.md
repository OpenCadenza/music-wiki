# 谱例来源与许可

本文件登记 `content/` 中每段真实谱例的作品、小节、取用渠道与许可。
知识正文不重复这些信息；站点页脚提供本文件的入口。

## 许可总述

- 本项目使用的谱例一律取自**公有领域**乐谱的再排版，或 CC0 编码的乐谱。
- 贝多芬作品本身早已进入公有领域。下列条目记录的是所用**排版版本**的出处与排版者。
- 每段谱例只截取数小节用于教学分析，不构成完整乐谱的再分发。

## 来源清单

| 来源 ID | 作品 | 排版底本 | 排版者 | 许可 | 链接 |
| --- | --- | --- | --- | --- | --- |
| `mutopia-1211` | 贝多芬 Op.2 No.1 第一乐章 | Breitkopf & Härtel (1862–1865) | Stelios Samelis | Public Domain | <https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1211> |
| `mutopia-778` | 贝多芬 Op.10 No.1 第一乐章 | Breitkopf & Härtel (1862–1865) | — | Public Domain | <https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=778> |
| `mutopia-992` | 贝多芬 Op.10 No.2 第一乐章 | Breitkopf & Härtel (1862–1865) | — | Public Domain | <https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=992> |
| `mutopia-299` | 贝多芬 Op.13《悲怆》第一乐章 | G. Schirmer (1894)、Berners (1908) | — | Public Domain | <https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=299> |
| `mutopia-1509` | 贝多芬 Op.31 No.2《暴风雨》第一乐章 | Breitkopf & Härtel (1862–1865) | — | Public Domain | <https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1509> |
| `mutopia-1022` | 贝多芬 Op.111 第一乐章 | Breitkopf & Härtel (1862–1865) | Stelios Samelis | Public Domain | <https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1022> |

## 按文章登记

每篇文章所用谱例的具体小节范围。新增文章时在此追加一行。

| 文章 | 谱例小节 | 来源 ID |
| --- | --- | --- |
| `composers/beethoven/piano/sonatas/opening-gestures.md` | Op.2 No.1 i 弱起–m.10；Op.13 i Grave mm.1–10 | `mutopia-1211`、`mutopia-299` |
| `composers/beethoven/piano/sonatas/motive-tasks.md` | Op.2 No.1 i 弱起–m.14 | `mutopia-1211` |
| `composers/beethoven/piano/sonatas/transition.md` | Op.2 No.1 i mm.9–28 | `mutopia-1211` |
| `composers/beethoven/piano/sonatas/secondary-theme.md` | Op.2 No.1 i mm.20 起；Op.31 No.2 i 副部段 | `mutopia-1211`、`mutopia-1509` |
| `composers/beethoven/piano/sonatas/exposition-closure.md` | Op.10 No.1 i mm.90 起；Op.2 No.1 i mm.41–48 | `mutopia-778`、`mutopia-1211` |

## 编辑约定

- 谱例统一用 `\language "english"`、`\version "2.26.0"`，由原始编码经 `convert-ly` 迁移、
  音名转写，并逐音核对（以 MIDI 事件序列比对原始排版）后入库。
- 原始 `.ly` 编码与核对记录留在项目工作区，不进入本仓库。
