# 演奏法记号与实现

- 文章：`content/notation/articulation-marks-and-realization.md`
- 许可：公有领域（详见两表；据 CCARH MuseData 转写，学术用途）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| CCARH MuseData / Humdrum Kern 贝多芬弦乐四重奏原生语料 | `local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/` 下 `quartet01-1.krn`、`quartet07-1.krn`、`quartet16-3.krn` | 贝多芬弦乐四重奏 Op. 18 No. 1（第一乐章 mm. 1–30 两连两断与断音模进）、Op. 59 No. 1（第一乐章 mm. 1–24 如歌长连弓与内声部分弓异步对位）与 Op. 135（第三乐章 mm. 1–12 降 D 大调内省长连弓与三音微观连弓细分）机器可读底本核验依据 |
| 贝多芬四重奏历史初版与校勘版本文献 | Vienna: Haslinger (Op. 18), Bureau des arts et d'industrie (Op. 59), Schlesinger (Op. 135) | 连弓弧线、点音断音（Dot）、顿音楔形（Stroke）、强弱突变（sf, fp, subito p）与速度表情术语的历史记谱比对 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `beethoven-op18no1-i-mm1-4` | 贝多芬《F 大调第一弦乐四重奏》Op. 18 No. 1 第一乐章 | Allegro con brio，mm.1–4 | OpenScore StringQuartets MXL `String_Quartet_No.1,_Op.18_No.1` | CC0-1.0 / 公有领域 |
| `beethoven-op59no1-i-mm1-8` | 贝多芬《F 大调第七弦乐四重奏》Op. 59 No. 1 第一乐章 | Allegro，mm.1–8（大提琴主题与内声部八分音符分弓） | CCARH Humdrum Kern `quartet07-1.krn` | 据 CCARH MuseData 转写，学术用途 |
| `beethoven-op59no1-i-mm18-24` | 贝多芬《F 大调第七弦乐四重奏》Op. 59 No. 1 第一乐章 | Allegro，mm.18–24（ff 爆发后的断音与休止撕裂） | CCARH Humdrum Kern `quartet07-1.krn` | 据 CCARH MuseData 转写，学术用途 |
| `beethoven-op135-iii-mm1-12`（关联引用） | 贝多芬《F 大调第十六弦乐四重奏》Op. 135 第三乐章 | Lento assai, cantante e tranquillo，mm.1–12 | 已有编译谱例，见 `content/ensembles/string-quartet-acoustic-role-differentiation.md` | 公有领域（据 CCARH MuseData 转写，学术用途） |

> 谱例均由本项目从 MusicXML 或 Humdrum Kern 逐音转写为 LilyPond：MusicXML 见 `local/workbench/tools/score-r5/mxl2ly.py`，Kern 见 `local/workbench/tools/score-r5/kern2ly.py`（转换结果另以编译 MIDI 的音高集合逐谱表回比对 kern 模型）。八度映射经 MIDI 实测校准（`c'` = 中央 C）。只截取论证所需片段，不构成完整乐谱的再分发。
