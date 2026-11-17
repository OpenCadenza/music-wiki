import io

# 1) 日志追加 M20
log = r"local\docs\实施记录\2026-11-16-DSH首批\批次日志.md"
add = """

## 2026-11-17 M20 谱例补齐战役收官（33 → 34 块）

### 产出

正文真实谱例从 6 块增至 **34 块**（`check_notation_fences.mjs` 实测 34/34 编译通过）。新增覆盖：巴赫众赞歌 4、挂留篇 3、贝多芬四重奏 3、那不勒斯 2、动机篇 5、风格轴 3、慢引子 3、终止式延后 2、增六 2（K.465 + Op.109）、双向选择 1。

### 流程与代价

6 名谱例助手并行（S1–S6）→ 每批另派独立核验员逐音比对 DCML／Kern／MusicXML → 仅核验通过者入正文。核验共发现需修正项：S1 批次 4 段、S2 批次 2 段、S3 批次 2 段、S4 批次 2 段、S6 批次 1 段——**即"编译通过"与"音乐正确"之间的距离，靠这层核验才被量出来**。

### 核验反证出的正文事实错误（均已改）

Op.132 大提琴 G♯2（前一轮 P0 被主控错误提示改坏）、勃拉姆斯 Op.90 III 圆号层不存在（mm.1–12 全休止，首次进入 m.40 末/m.41）、海顿 I:104 全奏自印刷谱 m.32 起（Kern 多一空小节导致编号差 1）、Op.111 Allegro 为 4/4、BWV 87/7 女高音 E4、Op.2 No.3 悬空延音线。

### 未入正文（保留工作区与修正清单）

- 待修正：海顿 Op.76/3 II（6 处八度）、贝多芬 Op.135 III（4 处音高）、勃拉姆斯 Op.90 III（m.4 后半起八度）、Op.67 II 大管摘录（降号拼写）。
- 确认无可靠机器可读源：12 件（清单见 `local/resources/catalog/score-deliveries.md` SCR-009~037 与各助手 `缺口报告.md`）。

### 版本库与推送

按用户批准：本批合并为**一次提交**、排除临时产物（各助手 downloads、MusicXML 副本、编译产物、二进制），并把忽略规则修正为相对 `local/` 的路径；已推送 `scholar-agent-dev`（`c305baf..dc4d5ae`）。

## 待办（主控）"""
s = io.open(log, encoding="utf-8").read()
s = s.replace("## 待办（主控）", add, 1)
io.open(log, "w", encoding="utf-8", newline="\n").write(s)
print("log ok")

# 2) 交付登记追加
cat = r"local\resources\catalog\score-deliveries.md"
add2 = """
| SCR-036 | 贝多芬 Op.109 III mm.1–8 | S6 | 核验一致（m.7 左手连音线已按核验补），已入正文 |
| SCR-037 | 舒伯特 D.960 I mm.18–48 | S6 | 未交付：DCML/kern/Mutopia 均无舒伯特钢琴奏鸣曲语料，已登记缺口 |
"""
with io.open(cat, "a", encoding="utf-8", newline="\n") as f:
    f.write(add2)
print("catalog ok")