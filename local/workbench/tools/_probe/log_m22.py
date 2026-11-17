import io

log = r"local\docs\实施记录\2026-11-16-DSH首批\批次日志.md"
add = """

## 2026-11-17 M22 编制篇四件溯源：全部确认无可用源，但找到一条夜间可解的路径

`score-s7` 走完 7 条路线（本地语料、OpenScore 各仓库、GitHub 代码搜索、IMSLP 作品页、MuseScore、Kunst der Fuge、DCML/Humdrum/MuseData），四件均未编成，证据已入 `缺口报告.md`：

| 作品 | 结论 | 关键证据 |
| --- | --- | --- |
| Reicha Op.88/2 I | 无源 | IMSLP 页 31 个 PDF/PNG 中 `mxl`/`MusicXML` 字面为 0；Mutopia `ftp/ReichaA/` 404；PDMX 里 reicha 命中 56 行全是 Reichardt 误命中 |
| Nielsen Op.43 I | 有源但损坏 | PDMX 副本声明 4/4，但强拍间距 480,480,480,480,1920（mm.1–4 每小节只 1 拍），声部小节号错位 |
| Beethoven Op.97 I | 无源 | P DMX 9 条 trio 候选无 Op.97；IMSLP 31 PDF 中 mxl 0；Mutopia `ftp/BeethovenLv/` 41 个 opus 目录无 O97 |
| Schubert D.929 II | 有源但损坏 | PDMX 副本 mm.1–20 每小节 1920 tick（4/4）、m.21 起才 960（2/4），冲突恰在小提琴进入处；大提琴小节号偏 +2、小提琴偏 +20 |

**新发现（下轮可直接用）**：Zenodo 上 PDMX 除本地那个 JSON 包外，另有 **`mxl.tar.gz`（约 1.8 GB）**，其中是真正的 MusicXML。本次会话未取回（单连接 186 KB/s，全程约 2.7 h；12 路并行被限速到约 40 KB/s）。**取件清单已备**：`score-s7/_probe/expect_mxl.tsv` 与 `members-map.json` 给出 5 个成员的精确归档路径，取下后可直接 `tar -xzf` 指定成员，不必解全档。

**其它结论**：IMSLP 已不用 `Special:IMSLPDisclaimerAccept`，`/images/` 直链返回 MTCaptcha 页；`imslp.eu` 与 `petruccimusiclibrary.ca` 对 `/images/` 均 404。Kunst der Fuge 只有 D.929 的 MIDI（按项目口径不作谱源）。

## 待办（主控）"""
s = io.open(log, encoding="utf-8").read()
s = s.replace("## 待办（主控）", add, 1)
io.open(log, "w", encoding="utf-8", newline="\n").write(s)
print("log ok")

cat = r"local\resources\catalog\score-deliveries.md"
add2 = """
**2026-11-17 编制篇四件复核**：Reicha Op.88/2、Nielsen Op.43、Beethoven Op.97、Schubert D.929 经 7 条路线穷尽溯源后确认**当前无可用机器可读源**（详见 `local/workbench/scores/score-s7/缺口报告.md`）。唯一可行路径：Zenodo 的 PDMX `mxl.tar.gz`（约 1.8 GB，内含真实 MusicXML；已备好 5 个成员的精确取件清单 `score-s7/_probe/expect_mxl.tsv`）。
"""
with io.open(cat, "a", encoding="utf-8", newline="\n") as f:
    f.write(add2)
print("catalog ok")