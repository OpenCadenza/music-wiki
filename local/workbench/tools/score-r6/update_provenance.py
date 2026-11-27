#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""update_provenance (score-r6)：把 provenance 谱例表里的「占位（未出谱）」行换成真实登记。

匹配方式：该行以给定前缀开头（整行替换）。
"""
import io

KERN = "CCARH Humdrum Kern（`{krn}` → hum2abc 转出的 ABC，`local/resources/scores/source-packages/humdrum/mozart-sonatas/{abc}`）；排版为本项目自编码 LilyPond 摘录"
LIC_KERN = "据 CCARH 转写，学术用途（非 CC0）"
DCML = "DCMLab《莫扎特钢琴奏鸣曲》语料 `{tsv}`（MS3 转录）"

JOBS = [
    # (文件, 旧行前缀, 新行)
    (r"provenance/techniques/structure/cadential-prinner-and-structural-closure.md",
     "| 占位（未出谱） | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 | Allegro，mm. 5–8 |",
     "| `mozart-k545-i-mm5-8` | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 | Allegro，mm. 5–8 | "
     + KERN.format(krn="sonata15-1.krn", abc="0061-…mvmt. 1.abc")
     + "；音高多重集已与 " + DCML.format(tsv="notes/K545-1.notes.tsv") + " 逐小节回比对一致 | " + LIC_KERN + " |"),

    (r"provenance/techniques/structure/compound-period-hierarchical-syntax.md",
     "| 占位（未出谱） | 莫扎特《F大调第12钢琴奏鸣曲》K. 332 第一乐章 |",
     "| `mozart-k332-i-mm41-56` | 莫扎特《F大调第12钢琴奏鸣曲》K. 332 第一乐章 | Allegro，mm. 41–56（3/4） | "
     + KERN.format(krn="sonata12-1.krn", abc="0052-…mvmt. 1.abc")
     + "；回比对 " + DCML.format(tsv="notes/K332-1.notes.tsv")
     + "：11/16 小节音高多重集完全一致，其余 5 小节差异均为底本倚音/装饰音（谱例不展开装饰音）与一处连线写法 | "
     + LIC_KERN + " |"),

    (r"provenance/techniques/structure/compound-period-hierarchical-syntax.md",
     "| 占位（未出谱） | 莫扎特《D大调第6钢琴奏鸣曲》K. 284 第二乐章 |",
     "| `mozart-k284-ii-mm1-16` | 莫扎特《D大调第6钢琴奏鸣曲》K. 284 第二乐章 | Rondeau en polonaise: Andante，mm. 1–16（3/4，A 大调） | "
     + KERN.format(krn="sonata06-2.krn", abc="0017-…mvmt. 2.abc")
     + "；回比对 " + DCML.format(tsv="notes/K284-2.notes.tsv")
     + "：12/16 小节音高多重集完全一致，其余 4 小节差异在三层叠置（&）与连线写法，音高集合相同 | "
     + LIC_KERN + " |"),

    (r"provenance/techniques/structure/phrase-expansion-and-structural-skeleton.md",
     "| 占位（未出谱） | 莫扎特《F大调回旋曲》K. 494 |",
     "| `mozart-k494-mm1-6` | 莫扎特《F大调回旋曲》K. 494（后编为奏鸣曲 K. 533/494 末乐章） | Allegro，mm. 1–6（2/2，F 大调） | "
     + DCML.format(tsv="notes/K533-3.notes.tsv")
     + "；并与 `local/origin_resources/sources/open-music-theory/raw/openmusictheory.github.io-master.zip` 中教材谱例 `Graphics/form/XML/k494.mxl` 逐小节核对（mm. 1–4 音高集合完全一致，m. 5–6 教材写法略有简化） | "
     "底本为 DCMLab 语料（CC BY-NC-SA 4.0）转录数据，仅用于核对与自编码摘录；作品本身公有领域，谱例再发布许可待人工复核 |"),

    (r"provenance/techniques/structure/sequence-mechanics-and-syntactic-functions.md",
     "| 占位（未出谱） | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 |",
     "| `mozart-k545-i-mm29-42` | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 | Allegro，展开部 mm. 29–42（4/4） | "
     + KERN.format(krn="sonata15-1.krn", abc="0061-…mvmt. 1.abc")
     + "；音高多重集已与 " + DCML.format(tsv="notes/K545-1.notes.tsv") + " 逐小节回比对一致 | " + LIC_KERN + " |"),

    (r"provenance/techniques/harmony/cadential-six-four-and-dominant-syntax.md",
     "| 占位（未出谱） | 莫扎特《A大调第11钢琴奏鸣曲》K. 331 第一乐章 |",
     "| `mozart-k331-i-theme-mm1-8`（关联引用） | 莫扎特《A大调第11钢琴奏鸣曲》K. 331 第一乐章 | Andante grazioso，mm. 1–8 | "
     + KERN.format(krn="sonata11-1a.krn", abc="0043-…mvmt. 1a.abc")
     + "；谱例见 `content/techniques/structure/variation-types-and-structural-transformations.md` | " + LIC_KERN + " |"),

    (r"provenance/techniques/harmony/cadential-six-four-and-dominant-syntax.md",
     "| 占位（未出谱） | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 |",
     "| `mozart-k545-i-mm22-26` | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 | Allegro，mm. 22–26（4/4） | "
     + KERN.format(krn="sonata15-1.krn", abc="0061-…mvmt. 1.abc")
     + "；回比对 " + DCML.format(tsv="notes/K545-1.notes.tsv")
     + "：m. 22–23 底本把回音写成显式还原 G（`=g`），DCML 作 G♯，此处按底本原样保留；其余小节一致 | "
     + LIC_KERN + " |"),

    # 变奏曲式篇：三条占位
    (r"provenance/techniques/structure/variation-types-and-structural-transformations.md",
     "| 占位（未出谱） | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | Andante grazioso，mm. 1–8 |",
     "| `mozart-k331-i-theme-mm1-8` | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | Andante grazioso，mm. 1–8（6/8，A 大调） | "
     + KERN.format(krn="sonata11-1a.krn", abc="0043-…mvmt. 1a.abc")
     + "；回比对 " + DCML.format(tsv="notes/K331-1.notes.tsv")
     + "：mm. 1–7 音高多重集完全一致，m. 8 底本以连线代替重复音一处 | " + LIC_KERN + " |"),

    (r"provenance/techniques/structure/variation-types-and-structural-transformations.md",
     "| 占位（未出谱） | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | 第一变奏，mm. 19–26 |",
     "| `mozart-k331-i-var1-mm19-26` | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | Variation I，mm. 19–26（6/8） | "
     + KERN.format(krn="sonata11-1b.krn", abc="0044-…mvmt. 1b.abc（`%%setbarnb 19`，与刊本印刷号一致）")
     + "；回比对 " + DCML.format(tsv="notes/K331-1.notes.tsv")
     + "：6/8 小节音高多重集全部一致，另两小节仅有装饰音写法差异 | " + LIC_KERN + " |"),

    (r"provenance/techniques/structure/variation-types-and-structural-transformations.md",
     "| 占位（未出谱） | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | 第三变奏 Minore，mm. 55–72 |",
     "| `mozart-k331-i-var3-mm55-72` | 莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 | Variation III（Minore），mm. 55–72（6/8，A 小调记谱无调号） | "
     + KERN.format(krn="sonata11-1d.krn", abc="0046-…mvmt. 1d.abc（缺 `%%setbarnb`，按变奏二止于 m. 54 推算本段起于刊本 m. 55）")
     + "；回比对 " + DCML.format(tsv="notes/K331-1.notes.tsv")
     + " mn 55–72：16/18 小节音高多重集完全一致 | " + LIC_KERN + " |"),
]


def main():
    for path, prefix, newline in JOBS:
        src = io.open(path, encoding="utf-8").read()
        lines = src.split("\n")
        hits = [i for i, ln in enumerate(lines) if ln.startswith(prefix)]
        if len(hits) != 1:
            print("!! %s：命中 %d 次（%s）" % (path, len(hits), prefix[:46]))
            continue
        lines[hits[0]] = newline
        io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
        print("OK %s ← %s" % (path, prefix[:40]))


if __name__ == "__main__":
    main()
