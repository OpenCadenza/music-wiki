#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""compare (score-r6)：把 ABC 底本与 DCML notes.tsv 按小节做音高多重集比对。

用法：
  python compare.py --abc <file.abc> --dcml <notes.tsv> --measures 1-8 [--offset 0]
--offset：ABC 小节号 = 印刷号 + offset（应对 ABC 的连续号与刊本号的差异）。
输出每小节每声部的 MATCH / DIFF 与差异明细。
"""
import argparse
import sys

sys.path.insert(0, __file__.rsplit("\\", 1)[0].rsplit("/", 1)[0])
from abc2ly import parse_abc, measure_pitches  # noqa: E402
from dcml_dump import dump as dcml_dump  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--abc", required=True)
    ap.add_argument("--dcml", required=True)
    ap.add_argument("--measures", required=True)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--voice-map", default="1:1,2:2",
                    help="ABC声部=DCML staff")
    ap.add_argument("--combined", action="store_true",
                    help="再按两谱表合并后的音高多重集核对（容忍跨谱表记谱）")
    args = ap.parse_args()
    first, last = [int(x) for x in args.measures.split("-")]
    data = parse_abc(args.abc)
    vmap = dict(p.split(":") for p in args.voice_map.split(","))
    dml = dcml_dump(args.dcml, first, last)
    ok = bad = 0
    for vn in data["order"]:
        if vn not in vmap:
            continue
        st = vmap[vn]
        v = data["voices"][vn]
        abc = {m.number: measure_pitches(m) for m in v.measures}
        dc = {int(k): val for k, val in dml.get(st, {}).items()}
        print("== V%s ↔ staff %s" % (vn, st))
        for mn in range(first, last + 1):
            a = abc.get(mn + args.offset)
            d = dc.get(mn)
            if d is None:
                print("  m%-4d [no DCML data]" % mn)
                continue
            if a is None:
                print("  m%-4d [no ABC measure]" % mn)
                bad += 1
                continue
            if sorted(a) == sorted(d):
                print("  m%-4d MATCH (%d notes)" % (mn, len(d)))
                ok += 1
            else:
                bad += 1
                sa, sd = sorted(a), sorted(d)
                print("  m%-4d DIFF abc=%s" % (mn, sa))
                print("           dcm=%s" % (sd,))
    print("\n合计 MATCH=%d DIFF=%d" % (ok, bad))
    # 跨谱表核对：合并两行谱表后再比（钢琴谱常有左右手交叉记谱）
    if args.combined:
        print("\n== 合并两声部（跨谱表核对）")
        ok2 = bad2 = 0
        allabc = {}
        for vn in data["order"]:
            for m in data["voices"][vn].measures:
                allabc.setdefault(m.number, []).extend(measure_pitches(m))
        alldc = {}
        for st in dml:
            for k, val in dml[st].items():
                alldc.setdefault(int(k), []).extend(val)
        for mn in range(first, last + 1):
            a = sorted(allabc.get(mn + args.offset, []))
            d = sorted(alldc.get(mn, []))
            if not d and not a:
                print("  m%-4d [两侧皆空]" % mn)
                continue
            if a == d:
                print("  m%-4d MATCH (%d notes)" % (mn, len(d)))
                ok2 += 1
            else:
                bad2 += 1
                print("  m%-4d DIFF abc=%s" % (mn, a))
                print("           dcm=%s" % (d,))
        print("\n合并后 MATCH=%d DIFF=%d" % (ok2, bad2))
        return 0 if bad2 == 0 else 1
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
