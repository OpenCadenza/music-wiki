#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""build_abc_fences (score-r6)：为莫扎特钢琴奏鸣曲各缺口生成 LilyPond 围栏草稿。

底本：local/resources/scores/source-packages/humdrum/mozart-sonatas/*.abc
（hum2abc，Craig Sapp，由 CCARH kern 转出；本仓库另存有 DCML 音符表用于独立回比对）
"""
import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import abc2ly

SRC = os.path.join("local", "resources", "scores", "source-packages", "humdrum", "mozart-sonatas")
OUT = os.path.join("local", "workbench", "tmp", "mozart-r6")

TARGETS = [
    dict(
        key="k331-theme",
        abc="0043-43-Piano Sonata No. 11 in A major, K 331 (300i), mvmt. 1a.abc",
        measures=(1, 8), location="Thema: Andante grazioso，mm.1–8",
        title="莫扎特 第11钢琴奏鸣曲 K.331 第一乐章", id="mozart-k331-i-theme-mm1-8",
        comments=[
            "莫扎特 A 大调第 11 钢琴奏鸣曲 K.331 第一乐章主题 mm.1-8（6/8，A 大调）。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "并用 DCML 莫扎特奏鸣曲音符表按小节做音高多重集回比对（mm.1-8 逐小节一致，",
            "m.8 底本含一处连线替代重复音，见 provenance 记录）。",
            "试听速度 1/8=144 采自底本速度标记。",
        ],
    ),
    dict(
        key="k331-var1",
        abc="0044-44-Piano Sonata No. 11 in A major, K 331 (300i), mvmt. 1b.abc",
        measures=(19, 26), location="Variation I，mm.19–26",
        title="莫扎特 第11钢琴奏鸣曲 K.331 第一乐章", id="mozart-k331-i-var1-mm19-26",
        comments=[
            "莫扎特 K.331 第一乐章变奏一 mm.19-26（6/8，A 大调）。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "DCML 音符表按小节回比对 mm.19-26：6/8 小节全部一致，另两小节仅有装饰音写法差异。",
            "底本 ABC 的 %%setbarnb 为 19，与刊本印刷号一致。",
        ],
    ),
    dict(
        key="k331-var3",
        abc="0046-46-Piano Sonata No. 11 in A major, K 331 (300i), mvmt. 1d.abc",
        measures=(1, 18), location="Variation III（Minore），mm.55–72",
        title="莫扎特 第11钢琴奏鸣曲 K.331 第一乐章", id="mozart-k331-i-var3-mm55-72",
        comments=[
            "莫扎特 K.331 第一乐章变奏三（小调变奏）mm.55-72（6/8，A 小调记谱无调号）。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "该分谱（sonata11-1d.krn）缺少 %%setbarnb，按变奏二止于 m.54 推算本段自刊本 m.55 起；",
            "DCML 音符表 mn 55-72 回比对 16/18 小节音高多重集完全一致。",
        ],
    ),
    dict(
        key="k545-cadence",
        abc="0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc",
        measures=(5, 8), location="Allegro，mm.5–8",
        title="莫扎特 第15钢琴奏鸣曲 K.545 第一乐章", id="mozart-k545-i-mm5-8",
        comments=[
            "莫扎特 C 大调第 15 钢琴奏鸣曲 K.545 第一乐章 mm.5-8（4/4，C 大调）。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "DCML 音符表 mm.5-8 逐小节音高多重集完全一致。",
            "试听速度 1/4=120 采自底本速度标记。",
        ],
    ),
    dict(
        key="k545-ic",
        abc="0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc",
        measures=(22, 26), location="Allegro，mm.22–26",
        title="莫扎特 第15钢琴奏鸣曲 K.545 第一乐章", id="mozart-k545-i-mm22-26",
        comments=[
            "莫扎特 K.545 第一乐章呈示部收束 mm.22-26（半终止前的终止准备）。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "DCML 音符表 mm.22-26 回比对：m.22/m.23 底本把回音写成显式还原 G，与 DCML 记谱的 G# 不同，",
            "此处按底本原样保留；其余小节音高一致。",
        ],
    ),
    dict(
        key="k545-dev",
        abc="0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc",
        measures=(29, 42), location="Allegro，展开部 mm.29–42",
        title="莫扎特 第15钢琴奏鸣曲 K.545 第一乐章", id="mozart-k545-i-mm29-42",
        comments=[
            "莫扎特 K.545 第一乐章展开部 mm.29-42。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "DCML 音符表 mm.29-42 逐小节音高多重集完全一致（含左手十六分音符分解音型）。",
        ],
    ),
    dict(
        key="k332-compound",
        abc="0052-52-Piano Sonata No. 12 in F major, K 332 (300k), mvmt. 1.abc",
        measures=(41, 56), location="Allegro，mm.41–56",
        title="莫扎特 第12钢琴奏鸣曲 K.332 第一乐章", id="mozart-k332-i-mm41-56",
        comments=[
            "莫扎特 F 大调第 12 钢琴奏鸣曲 K.332 第一乐章 mm.41-56（3/4，F 大调）。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "DCML 音符表 mm.41-56 回比对：11/16 小节音高多重集完全一致，",
            "其余 5 小节差异均为底本写作的倚音/装饰音（本谱例不展开装饰音）与一处连线写法。",
            "试听速度 1/4=144 采自底本速度标记。",
        ],
    ),
    dict(
        key="k545-mm1-14",
        abc="0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc",
        measures=(1, 14), location="Allegro，mm.1–14",
        title="莫扎特 第15钢琴奏鸣曲 K.545 第一乐章", id="mozart-k545-i-mm1-14",
        clefs={"2": "treble"},
        comments=[
            "莫扎特 C 大调第 15 钢琴奏鸣曲 K.545 第一乐章 mm.1-14（4/4，C 大调）：主部（mm.1–4）与补充、过渡段（mm.5–14）。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "DCML 音符表 mm.1-14 逐小节音高多重集完全一致。",
            "左手谱号按底本：mm.1–4 为高音谱号（C4–G4 一带），m.5 末拍起随底本改低音谱号，谱号换在该拍原位置。",
            "试听速度 1/4=120 采自底本速度标记。",
        ],
    ),
    dict(
        key="k284-ii",
        abc="0017-17-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 2.abc",
        measures=(1, 16), location="Rondeau en polonaise: Andante，mm.1–16",
        title="莫扎特 第6钢琴奏鸣曲 K.284 第二乐章", id="mozart-k284-ii-mm1-16",
        comments=[
            "莫扎特 D 大调第 6 钢琴奏鸣曲 K.284 第二乐章（回旋曲式波兰舞曲）mm.1-16（3/4，A 大调）。",
            "据 CCARH kern（经 hum2abc 转出的 ABC）核对后自编码摘录，学术用途；",
            "DCML 音符表 mn 1-16 回比对：12/16 小节音高多重集完全一致，其余 4 小节差异在",
            "三层叠置（&）与连音线写法上，音高集合一致。",
            "试听速度 1/4=104 采自底本速度标记。",
        ],
    ),
]


def build_one(t):
    src = os.path.join(SRC, t["abc"])
    data = abc2ly.parse_abc(src)
    first, last = t["measures"]
    out = os.path.join(OUT, t["key"] + ".md")

    class A:
        pass
    a = A()
    a.title = t["title"]
    a.location = t["location"]
    a.id = t["id"]
    a.out = out
    a.clefs = t.get("clefs")
    abc2ly.write_fence(data, first, last, a, t["comments"])
    print("wrote", out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    for t in TARGETS:
        if args.only and args.only not in t["key"]:
            continue
        build_one(t)


if __name__ == "__main__":
    main()
