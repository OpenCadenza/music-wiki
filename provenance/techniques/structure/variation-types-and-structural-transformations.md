# 变奏曲式的类型

- 文章：`content/techniques/structure/variation-types-and-structural-transformations.md`
- 许可：CCARH MuseData / Humdrum Kern 学术用途（非 CC0；详见两表）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| W. A. Mozart (1783) | A 大调第 11 钢琴奏鸣曲 K. 331 第一乐章乐谱机器可读事实 | CCARH MuseData/Humdrum Kern 转写 ABC（逐小节核验 Thema mm. 1–18 西西里两段体结构与半音化骨架，Var. 1 mm. 19–36 洛可可浮雕式十六分音符修饰与低音忠实度，Var. 3 mm. 55–72 a小调同主音小调色彩阻尼） |
| Ludwig van Beethoven (1820) | E 大调第 30 钢琴奏鸣曲 Op. 109 第三乐章乐谱机器可读事实 | CCARH Humdrum Kern `sonata30-3.krn`（逐小节核验 主题 mm. 1–16 萨拉班德圣咏原型与低音对位，Var. 1 mm. 17–32 意大利歌剧咏叹调与夜曲织体，Var. 2 mm. 33–64 点彩断奏与霍克特二重对位倒影，Var. 5 mm. 113–128 严格四部自由赋格） |
| Ludwig van Beethoven (1822) | c 小调第 32 钢琴奏鸣曲 Op. 111 第二乐章（阿里埃塔）乐谱机器可读事实 | CCARH Humdrum Kern `sonata32-2.krn`（逐小节核验 阿里埃塔主题 mm. 1–16 9/16 拍律动与三音升华动机 C-D-G，Var. 1–3 比例时值递减 9/16 $\to$ 6/16 $\to$ 12/32，Var. 4–Coda 音区两极声学真空与持续长颤音） |
| William E. Caplin | *Classical Form: A Theory of Formal Functions for the Instrumental Music of the Classical Style* (Oxford University Press, 1998) | 古典曲式中乐段、复合乐段与小两段体骨架理论支撑 |
| Charles Rosen | *The Classical Style: Haydn, Mozart, Beethoven* (W. W. Norton, 1997) & *Beethoven's Piano Sonatas: A Short Companion* (Yale University Press, 2002) | 莫扎特高雅装饰性变奏原则与贝多芬晚期奏鸣曲变奏曲式形而上时间观剖析 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `mozart-k331-i-theme-mm1-8` | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | Andante grazioso，mm. 1–8（6/8，A 大调） | CCARH Humdrum Kern（`sonata11-1a.krn` → hum2abc 转出的 ABC，`local/resources/scores/source-packages/humdrum/mozart-sonatas/0043-…mvmt. 1a.abc`）；排版为本项目自编码 LilyPond 摘录；回比对 DCMLab《莫扎特钢琴奏鸣曲》语料 `notes/K331-1.notes.tsv`（MS3 转录）：mm. 1–7 音高多重集完全一致，m. 8 底本以连线代替重复音一处 | 据 CCARH 转写，学术用途（非 CC0） |
| `mozart-k331-i-var1-mm19-26` | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | Variation I，mm. 19–26（6/8） | CCARH Humdrum Kern（`sonata11-1b.krn` → hum2abc 转出的 ABC，`local/resources/scores/source-packages/humdrum/mozart-sonatas/0044-…mvmt. 1b.abc（`%%setbarnb 19`，与刊本印刷号一致）`）；排版为本项目自编码 LilyPond 摘录；回比对 DCMLab《莫扎特钢琴奏鸣曲》语料 `notes/K331-1.notes.tsv`（MS3 转录）：6/8 小节音高多重集全部一致，另两小节仅有装饰音写法差异 | 据 CCARH 转写，学术用途（非 CC0） |
| `mozart-k331-i-var3-mm55-72` | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | Variation III（Minore），mm. 55–72（6/8，A 小调记谱无调号） | CCARH Humdrum Kern（`sonata11-1d.krn` → hum2abc 转出的 ABC，`local/resources/scores/source-packages/humdrum/mozart-sonatas/0046-…mvmt. 1d.abc（缺 `%%setbarnb`，按变奏二止于 m. 54 推算本段起于刊本 m. 55）`）；排版为本项目自编码 LilyPond 摘录；回比对 DCMLab《莫扎特钢琴奏鸣曲》语料 `notes/K331-1.notes.tsv`（MS3 转录） mn 55–72：16/18 小节音高多重集完全一致 | 据 CCARH 转写，学术用途（非 CC0） |
| `beethoven-op109-iii-mm1-8`（关联引用） | 贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章 | 主题 Gesangvoll, mit innigster Empfindung，mm. 1–8 | CCARH Humdrum Kern `sonata30-3.krn`；谱例见 `content/techniques/harmony/augmented-sixth-mechanics-and-syntactic-drift.md` | 据 CCARH MuseData 转写，学术用途 |
| `beethoven-op109-iii-mm17-32` | 贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章 | Variation I: Molto espressivo，mm.17–32（底本 kern 连续编号 mm.17–35，含反复第二结尾） | CCARH Humdrum Kern `sonata30-3.krn` | 据 CCARH MuseData 转写，学术用途 |
| `beethoven-op109-iii-mm33-48` | 贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章 | Variation II: Leggiermente，mm.33–48（底本 kern 连续编号 mm.36–51） | CCARH Humdrum Kern `sonata30-3.krn` | 据 CCARH MuseData 转写，学术用途 |
| `beethoven-op109-iii-mm113-128` | 贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章 | Variation V: Allegro, ma non troppo，mm.113–128（底本 kern 连续编号 mm.120–135） | CCARH Humdrum Kern `sonata30-3.krn` | 据 CCARH MuseData 转写，学术用途 |
| `beethoven-op111-ii-mm1-16` | 贝多芬《c小调第32钢琴奏鸣曲》Op. 111 第二乐章 | Arietta: Adagio molto semplice e cantabile，mm.1–16（底本 kern 连续编号 mm.1–18，含反复第二结尾） | CCARH Humdrum Kern `sonata32-2.krn` | 据 CCARH MuseData 转写，学术用途 |
| `beethoven-op111-ii-mm33-48` | 贝多芬《c小调第32钢琴奏鸣曲》Op. 111 第二乐章 | Variation II: L'istesso tempo，mm.33–48（底本 kern 连续编号 mm.36–54） | CCARH Humdrum Kern `sonata32-2.krn` | 据 CCARH MuseData 转写，学术用途 |
