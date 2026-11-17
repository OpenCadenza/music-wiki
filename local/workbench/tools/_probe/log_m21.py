import io

log = r"local\docs\实施记录\2026-11-16-DSH首批\批次日志.md"
add = """

## 2026-11-17 M21 四段返修：两处核验结论被推翻

返修助手按核验清单改完四段，其中**两处它拒绝照改并由主控复核确认**：

1. **Op.135 III 的 `an4./dn4/dn,4.`**：核验员主张"裸写 `a` 在 D♭ 调下渲染为 A♭"，据此要求改音名。返修助手指出 `an`/`dn` 在 `\\language "english"` 下不是合法音名（实编译报 `not a note name: an`），且 LilyPond 的音名是绝对音高、`\\key` 只影响谱面记号。主控用最小探针验证：`\\key df \\major a'4 d'4 g'4 c'4` 的 MIDI 为 C4–A4 全还原音——**核验员错，返修助手对**；该处原本就发 A♮3/D♮3/D♮2。核验员的偏差来自其 `cmp_staff.py` 把调号套用到 `.ly` 侧音高的测量端 bug。
2. **Brahms Op.90 III 的"m.4 末–m.8 整体高八度"**：返修助手按底本的 `\\relative c'` 重新解析，认为除 5 个音外本来就在 C4 八度；核验员则据印刷谱"旋律压在谱表顶线、高于中提琴伴奏"主张整段在 C3。**双方证据都指向不同结论，主控暂不定案**——该段暂不入正文（`planes-of-tone` 案例二保留占位），待有印刷谱目视结论再定。

### 已入正文（本轮）

- 海顿 Op.76/3 II mm.1–20（返修 6 处八度后）、贝多芬 Op.135 III mm.1–12（返修 1 处八度后）→ `ensembles/string-quartet-…`
- 贝多芬 Op.67 II mm.205–209 大管声部摘录（重拼写为降号后）→ `techniques/sound/planes-of-tone-layering…`，明确标注"只含大管、弦乐层未收录"

围栏 34 → **37 块**，全部编译通过。

## 待办（主控）"""
s = io.open(log, encoding="utf-8").read()
s = s.replace("## 待办（主控）", add, 1)
io.open(log, "w", encoding="utf-8", newline="\n").write(s)
print("log ok")

cat = r"local\resources\catalog\score-deliveries.md"
add2 = """
**2026-11-17 返修与复核结果**：SCR-032（海顿 Op.76/3）与 SCR-033（Op.135 III）已返修并入正文；SCR-035（Op.67 II）已改降号拼写、改名 m205-209，以"大管声部摘录"入正文；SCR-034（勃拉姆斯）核验与返修结论冲突未决，暂不入正文。另经主控最小探针复核：核验员对 Op.135 III 三处"应改 A♮/D♮"的判定系测量脚本按调号误算，实际原文件已正确。
"""
with io.open(cat, "a", encoding="utf-8", newline="\n") as f:
    f.write(add2)
print("catalog ok")