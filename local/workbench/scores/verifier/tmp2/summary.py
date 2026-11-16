import sys
sys.path.insert(0, ".")
import lyparse

NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def nm(p):
    return f"{NAMES[p % 12]}{p // 12 - 1}"


for path, names in [
    ("display_mozart.txt", ["rightHand", "leftHand"]),
    ("display_beethoven.txt", ["violinOne", "violinTwo", "viola", "cello"]),
]:
    print(f"===== {path}")
    total = 0
    for name, tr in lyparse.load(path, names).items():
        ps = [p for _, _, p in tr.events]
        total += len(ps)
        print(f"  {name}: {len(ps)} 音  范围 {nm(min(ps))}({min(ps)}) – {nm(max(ps))}({max(ps)})"
              f"  小节线 {len(tr.barlines)} 个  装饰音组 {len(tr.ornaments)}")
        # 每小节音数
    print(f"  合计 {total} 音")
