import pathlib
# score-board manual gaps
p=pathlib.Path('local/resources/catalog/score-board.md')
t=p.read_text(encoding='utf-8')
t=t.replace('| 贝多芬 Op.97 第一乐章 | mm.1–12 | 暂无可靠谱源 |','| 贝多芬 Op.97 第一乐章 | mm.1–12 | 无法核验：无机器可读源（IMSLP 仅 PDF；PDMX 无；CCARH 无钢琴三重奏） |')
t=t.replace('| 雷哈 Op.88 No.2 第一乐章 | mm.1–8 | 暂无可靠谱源 |','| 雷哈 Op.88 No.2 第一乐章 | mm.1–8 | 无法核验：IMSLP 有扫描/分谱 PDF，无 MXL；PDMX 无 |')
t=t.replace('| 贝多芬 Op.92 第二乐章 | mm.1–26 | 暂无可靠谱源 |','| 贝多芬 Op.92 第二乐章 | mm.1–10 | 已回填（`beethoven-op92-ii-mm1-10`，verifier-4 核验） |')
t=t.replace('| 贝多芬 Op.125 第一乐章 | mm.1–35 | 暂无可靠谱源 |','| 贝多芬 Op.125 第一乐章 | mm.1–35 | 已回填（`beethoven-op125-i-mm1-35`，verifier-6 逐音核验） |')
t=t.replace('| 马勒 第四交响曲 第二乐章 | mm.34–46 | 暂无可靠谱源 |','| 马勒 第四交响曲 第二乐章 | mm.34–46 | 无法核验：PDMX 无第四；IMSLP 仅 Vn1 分谱 MXL，非总谱 |')
t=t.replace('| 那不勒斯和弦教材模型 | 示意 | 作者决定是否保留 |','| 那不勒斯和弦教材模型 | 示意 | 不出谱：正文改为示意性表述（差异复读 #1 已处理） |')
p.write_text(t,encoding='utf-8')

# 补谱清单 statuses
p=pathlib.Path('local/docs/实施记录/2026-11-22-第二轮/补谱清单.md')
t=p.read_text(encoding='utf-8')
t=t.replace('| 1 | `ensembles/bidirectional-selection-of-musical-ideas-and-medium.md` | 贝多芬《大公三重奏》Op. 97 第一乐章 mm. 1–12 | 单行占位 | 待补 | 工作树内无该曲可靠谱源记录，先找源 |','| 1 | `ensembles/bidirectional-selection-of-musical-ideas-and-medium.md` | 贝多芬《大公三重奏》Op. 97 第一乐章 mm. 1–12 | 单行占位 | **无法核验** | 无机器可读源（IMSLP 仅 PDF；PDMX 无；CCARH 无钢琴三重奏），见 `缺口报告-2-来源.md` |')
t=t.replace('| 2 | `ensembles/wind-quintet-acoustic-balance.md` | 雷哈 Op. 88 No. 2 第一乐章 mm. 1–8 | 单行占位 | 待补 | 需与"交错排布"论证对齐（见差异复读 #7） |','| 2 | `ensembles/wind-quintet-acoustic-balance.md` | 雷哈 Op. 88 No. 2 第一乐章 mm. 1–8 | 单行占位 | **无法核验** | IMSLP 有扫描/分谱 PDF，无 MXL；PDMX 无；见 `缺口报告-2-来源.md` |')
t=t.replace('| 3 | `techniques/sound/timbral-contrast-and-formal-articulation.md` | 贝多芬 Op. 92 第二乐章 | 单行占位 | 待补 | 分谱在 `local/workbench/scores/score-s2/downloads/op92-2/`，可据此编码 |','| 3 | `techniques/sound/timbral-contrast-and-formal-articulation.md` | 贝多芬 Op. 92 第二乐章 mm.1–10 | 已回填 | **已核验** | `beethoven-op92-ii-mm1-10`，verifier-4 逐音一致；正文原「木管铜管沉默」已订正 |')
t=t.replace('| 4 | 同上 | 贝多芬 Op. 125 第一乐章 mm. 1–35 | 单行占位 | 待补 | 无本地总谱，需先找源 |','| 4 | 同上 | 贝多芬 Op. 125 第一乐章 mm. 1–35 | 已回填 | **已核验** | `beethoven-op125-i-mm1-35`，verifier-6 1,876/1,876 音通过 |')
t=t.replace('| 5 | 同上 | 马勒《第四交响曲》第二乐章 mm. 34–46 | 单行占位 | 待补 | 无本地总谱，需先找源 |','| 5 | 同上 | 马勒《第四交响曲》第二乐章 mm. 34–46 | 单行占位 | **无法核验** | PDMX 无第四；IMSLP 仅 Vn1 分谱 MXL，非总谱 |')
t=t.replace('| 6 | `techniques/harmony/neapolitan-chord-structural-mutation.md` | 那不勒斯和弦"教材式规范进行"示意 | 正文有意改成示意性表述 | 可不出谱 | 差异复读 #1 指出"是否改为示意性谱例由作者决定"这句不该进正文，随修订处理 |','| 6 | `techniques/harmony/neapolitan-chord-structural-mutation.md` | 那不勒斯和弦"教材式规范进行"示意 | 正文示意性表述 | **不出谱（已定）** | 差异复读 #1 已处理；正文不再写"是否改为示意性谱例" |')
t=t.replace('| 7 | `ensembles/wind-quintet-acoustic-balance.md` | 尼尔森 Op. 43 第一乐章（清单 #16） | 已入文 mm.1–11 谱例 | 待核验结论 | 等 verifier 结论；未到位就保持"该处核验结论未到位" |','| 7 | `ensembles/wind-quintet-acoustic-balance.md` | 尼尔森 Op. 43 第一乐章（清单 #16） | 已入文 mm.1–11 谱例 | **沿用 S8 核验（可放行）** | SCR-038 结论；本轮未重核，正文不据此新增断言 |')
p.write_text(t,encoding='utf-8')
print('ok')
