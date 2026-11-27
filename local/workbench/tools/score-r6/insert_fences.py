#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""insert_fences (score-r6)：把围栏草稿替换掉正文里的占位行。

替换规则：按「文件 + 占位行原文（去首尾空白后整行匹配）」定位，用围栏草稿整块替换该行。
link_to 提供时改为写一行跨文引用（该片段在主文文章里只保留一份）。
"""
import io
import os

TMP = os.path.join("local", "workbench", "tmp", "mozart-r6")

JOBS = [
    dict(
        target=r"content/techniques/structure/cadential-prinner-and-structural-closure.md",
        placeholder="谱例待补：莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 mm. 5–8（原型 Prinner）",
        fence="k545-cadence.md",
    ),
    dict(
        target=r"content/techniques/structure/compound-period-hierarchical-syntax.md",
        placeholder="谱例待补：莫扎特《F大调第12钢琴奏鸣曲》K. 332 第一乐章 mm. 41–56",
        fence="k332-compound.md",
    ),
    dict(
        target=r"content/techniques/structure/compound-period-hierarchical-syntax.md",
        placeholder="谱例待补：莫扎特《D大调第6钢琴奏鸣曲》K. 284 第二乐章 mm. 1–16",
        fence="k284-ii.md",
    ),
    dict(
        target=r"content/techniques/structure/concertante-principle-and-double-exposition.md",
        placeholder="谱例待补：莫扎特 K.467 第一乐章 mm. 9–28（全奏动能过渡段）——该段十六分音符跑动密集，本轮只出主部主题群，暂不嵌入。",
        fence="k467-i-9-28.fence.md",
    ),
    dict(
        target=r"content/techniques/structure/phrase-expansion-and-structural-skeleton.md",
        placeholder="谱例待补：莫扎特《F大调回旋曲》K. 494 开篇 mm. 1–6（据 OMT 教材谱例）",
        fence="k494.md",
    ),
    dict(
        target=r"content/techniques/structure/sequence-mechanics-and-syntactic-functions.md",
        placeholder="谱例待补：莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章展开部 mm. 29–42",
        fence="k545-dev.md",
    ),
    dict(
        target=r"content/techniques/structure/variation-types-and-structural-transformations.md",
        placeholder="莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 Andante grazioso，mm. 1–8。",
        fence="k331-theme.md",
    ),
    dict(
        target=r"content/techniques/structure/variation-types-and-structural-transformations.md",
        placeholder="莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 第一变奏，mm. 19–26（即变奏 mm. 1–8）。",
        fence="k331-var1.md",
    ),
    dict(
        target=r"content/techniques/structure/variation-types-and-structural-transformations.md",
        placeholder="莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 第三变奏 Minore，mm. 55–72。",
        fence="k331-var3.md",
    ),
    dict(
        target=r"content/techniques/harmony/cadential-six-four-and-dominant-syntax.md",
        placeholder="谱例待补：莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 mm. 22–26（副部 EEC）",
        fence="k545-ic.md",
    ),
    dict(
        target=r"content/techniques/harmony/cadential-six-four-and-dominant-syntax.md",
        placeholder="谱例待补：莫扎特《A大调第11钢琴奏鸣曲》K. 331 第一乐章 mm. 1–8",
        link=("本段主题与终止四六的骨架见[《变奏曲式的类型与结构转化》]"
              "(../structure/variation-types-and-structural-transformations.md"
              "#score-mozart-k331-i-theme-mm1-8)（莫扎特《A大调钢琴奏鸣曲》K. 331 第一乐章 mm. 1–8，"
              "第 4、8 小节各有一次终止四六的插入与解决；同一片段全库只保留一份）。"),
    ),
]


def main():
    for job in JOBS:
        path = job["target"]
        src = io.open(path, encoding="utf-8").read()
        lines = src.split("\n")
        placeholder = job["placeholder"].strip()
        hits = [i for i, ln in enumerate(lines) if ln.strip() == placeholder]
        if len(hits) != 1:
            print("!! %s：占位行命中 %d 次（%s）" % (path, len(hits), placeholder[:40]))
            continue
        if "fence" in job:
            block = io.open(os.path.join(TMP, job["fence"]), encoding="utf-8").read().rstrip("\n")
        else:
            block = job["link"]
        lines[hits[0]] = block
        io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
        print("OK %s ← %s" % (path, job.get("fence", "link")))


if __name__ == "__main__":
    main()
