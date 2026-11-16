"""莫扎特：按手（声部）分别比对，检查谱表分配与八度。"""
import sys
sys.path.insert(0, ".")
import compare as C

BASE = "E:/github/music-wiki/.agents/worktrees/dsh-c6ded6ed-82bb/"
MOZ_ABC = BASE + "local/origin_resources/corpus/abc/humdrum-kern/mozart_sonatas/0041-41-Piano Sonata No. 10 in C major, K 330 (300h), mvmt. 2.abc"

ly_all = C.ly_per_measure("display_mozart.txt", ["rightHand", "leftHand"], 3.0, 1.5)
ly_rh = {m: [e for e in v if e[3] == "rightHand"] for m, v in ly_all.items()}
ly_lh = {m: [e for e in v if e[3] == "leftHand"] for m, v in ly_all.items()}
abc1 = C.abc_per_measure(MOZ_ABC, 25, 42, unit=0.5, key_alters={"B": -1}, only_v=1)
abc2 = C.abc_per_measure(MOZ_ABC, 25, 42, unit=0.5, key_alters={"B": -1}, only_v=2)
ms = list(range(0, 9))
C.show(ly_rh, ms, "被测件 右手")
C.show(abc1, ms, "ABC V1（右手）")
C.show(ly_lh, ms, "被测件 左手")
C.show(abc2, ms, "ABC V2（左手）")
print()
C.diff(ly_rh, abc1, "右手 vs ABC V1（音高）", ms)
C.diff(ly_rh, abc1, "右手 vs ABC V1（音高+时值）", ms, with_dur=True)
C.diff(ly_lh, abc2, "左手 vs ABC V2（音高）", ms)
C.diff(ly_lh, abc2, "左手 vs ABC V2（音高+时值）", ms, with_dur=True)
