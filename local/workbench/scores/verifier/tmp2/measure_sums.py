import sys
sys.path.insert(0, ".")
import lyparse

def sums(path, names, bar_len, partial):
    print(f"===== {path}  每小节总时值（四分拍）")
    tracks = lyparse.load(path, names)
    for name, tr in tracks.items():
        per = {}
        for t, d, p in tr.events:
            if t < partial - 1e-9:
                m = 0
            else:
                m = int((t - partial) / bar_len + 1e-9) + 1
            per[m] = per.get(m, 0.0) + d
        # 用事件终点更稳妥
        end = {}
        for t, d, p in tr.events:
            if t < partial - 1e-9:
                m = 0
            else:
                m = int((t - partial) / bar_len + 1e-9) + 1
            end[m] = max(end.get(m, 0.0), t + d - (0 if m == 0 else partial + (m - 1) * bar_len))
        txt = "  ".join(f"m{m}:{end[m]:.3f}" for m in sorted(end))
        print(f"  {name}: {txt}")
        print(f"    小节线时间: {[round(b, 3) for b in tr.barlines]}")

sums("display_mozart.txt", ["rightHand", "leftHand"], 3.0, 1.5)
sums("display_beethoven.txt", ["violinOne", "violinTwo", "viola", "cello"], 2.0, 0.0)
