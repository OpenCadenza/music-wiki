import io

cat = r"local\resources\catalog\score-deliveries.md"
add = """

## 2026-11-17 本轮补齐（谱例助手 S1–S6 + 独立核验）

| 编号 | 作品/片段 | 交付者 | 状态 |
| --- | --- | --- | --- |
| SCR-009 | 巴赫 BWV 269 mm.3–4 | S1 | 核验一致，已入正文 |
| SCR-010 | 巴赫 BWV 347 mm.3–4 | S1 | 核验一致（时值按四分+fermata 修正），已入正文 |
| SCR-011 | 巴赫 BWV 38/6 mm.12–13 | S1 | 核验一致，已入正文 |
| SCR-012 | 巴赫 BWV 153/5 mm.3–4 | S1 | 核验一致（C♮ 修正），已入正文 |
| SCR-013 | 巴赫 BWV 87/7 mm.1–3 | S1 | 核验一致，已入正文 |
| SCR-014 | 巴赫 BWV 269 mm.5–7 | S1 | 核验一致（C♮ 修正），已入正文 |
| SCR-015 | 巴赫 BWV 60/5 mm.1–4 | S1 | 核验一致，已入正文 |
| SCR-016 | 贝多芬 Op.74 I mm.18–24 | S1/S2 各一版 | 核验一致（D 版已入正文；S1 版仅存工作区） |
| SCR-017 | 贝多芬 Op.131 I mm.6–11 | S2 | 核验一致，已入正文 |
| SCR-018 | 贝多芬 Op.132 I mm.1–8 | S2 | 核验一致（G♯2），已入正文 |
| SCR-019 | 贝多芬 Op.95 I mm.1–8 / mm.19–24 | S2 | 核验一致，已入正文 |
| SCR-020 | 贝多芬 Op.135 IV mm.1–4 / mm.12–16 / mm.165–172 | S3 + assistant-scores-c | 核验一致（D1 休止已补），已入正文 |
| SCR-021 | 舒伯特 D.328 mm.1–5 / mm.72–76 | S3 | 核验一致（m.76 左手 F♯3 修正），已入正文 |
| SCR-022 | 巴赫 BWV 1050 I mm.1–9 | S3 | 核验一致（cemba2 省略已注明），已入正文 |
| SCR-023 | 海顿 Hob.I:104 I mm.17–31（弦乐）/ mm.32–39（全奏） | S3 | 核验一致（按印刷谱号重编、补力度与圆号移调后），已入正文 |
| SCR-024 | 贝多芬 Op.74 I mm.6–9 | S3 | 内容通过；m.9 花彩降号与 DCML 冲突（kern 对、DCML 疑漏），未入正文（记谱轴以链接指向前文） |
| SCR-025 | 贝多芬 Op.13 I mm.1–19 | S4 | 核验一致，已入正文 |
| SCR-026 | 贝多芬 Op.81a I mm.1–25 | S4 | 核验一致（悬空延音线待整理），已入正文 |
| SCR-027 | 贝多芬 Op.111 I mm.1–25 | S4 | 核验一致（拍号 4/4；m.7/8/13 版本差异已注），已入正文 |
| SCR-028 | 莫扎特 K.309 III mm.9–19 | S4 | 核验一致（倚音按 NMA），已入正文 |
| SCR-029 | 贝多芬 Op.2 No.3 I mm.1–13 | S4 | 核验一致（删 m.11 悬空延音线），已入正文 |
| SCR-030 | 莫扎特 K.465 IV mm.10–16 | S2 | 核验有条件通过，已修正（F♯、速度 144、编号基准）并入正文 |
| SCR-031 | 贝多芬 Op.14 No.1 I mm.1–16 | S5 | 核验一致，已入正文（Hess 34 无源未收录） |
| SCR-032 | 海顿 Op.76/3 II mm.1–20 | S1 | **待修正 6 处八度后入正文**（核验已给逐行清单） |
| SCR-033 | 贝多芬 Op.135 III mm.1–12 | S1 | **待修正 4 处音高后入正文** |
| SCR-034 | 勃拉姆斯 Op.90 III mm.1–8 | S2 | **退回返修**（m.4 后半至 m.8 大提琴仍高八度） |
| SCR-035 | 贝多芬 Op.67 II mm.205–209 | S2 | **退回返修**（只含大管声部，且降号被写成升号） |
| SCR-036 | 贝多芬 Op.109 III mm.1–8 | S6（进行中） | 编码中 |
| SCR-037 | 舒伯特 D.960 I mm.18–48 | S6（进行中） | 视源有无决定 |

### 缺口（确认无可靠机器可读源）

HWV 348 Air、K.550 III、Op.55 I、Op.67 IV、Reicha Op.88/2、Nielsen Op.43、Op.97、D.929、Hess 34、Op.125 I、Mahler 4 II、K.494。详见 `local/docs/实施记录/2026-11-16-DSH首批/批次日志.md` M19/M20 与各助手 `缺口报告.md`。
"""
with io.open(cat, "a", encoding="utf-8", newline="\n") as f:
    f.write(add)
print("catalog ok")

chk = r"local\docs\实施记录\2026-11-16-DSH首批\待作者修订清单.md"
add2 = """

## 本轮补齐谱例时新增的正文事实修正（已完成，作者复核用）

7. `composers/beethoven/piano-sonatas/slow-introduction-integration.md`：Op.111 的"Allegro 2/2"已改为 **4/4**（DCML 与 kern 全乐章只有一个拍号，速度加快而拍号不变）。
8. `techniques/sound/planes-of-tone-layering.md` 案例二：圆号进入位置已改为 **m.40 末弱起、m.41 起陈述主题**（此前误写 m.78）；并存疑处：圆号在本段 m.1–12 全休止，正文已如实改述。

## 待作者复核的谱例相关表述

9. `techniques/harmony/augmented-sixth-…`：K.465 谱例的小节编号按 OpenScore 零基（弱起=0）计，正文若采用"弱起算第 1 小节"计法需相应改为 mm.11–17。
10. `composers/beethoven/quartets/chromatic-…` 与 `techniques/counterpoint/suspension-…`：Op.74 m.9 花彩的 E♭/E♮ 在 kern 与 DCML 之间存在源间冲突（kern 记 E♭、DCML 记 E♮，和声逻辑支持 E♭）；正文若断言"旧谱漏降号"，建议补一句源间异读说明。
"""
with io.open(chk, "a", encoding="utf-8", newline="\n") as f:
    f.write(add2)
print("checklist ok")