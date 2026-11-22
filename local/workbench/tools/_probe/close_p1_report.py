import pathlib
p=pathlib.Path('local/docs/实施记录/2026-11-22-第二轮/完成报告.md')
t=p.read_text(encoding='utf-8')
t=t.replace('| Op.97 / Reicha Op.88-2 / Mahler 4-II | 无机器可读源，硬缺口登记，不造谱 |','| Op.97 / Reicha Op.88-2 / Mahler 4-II | 无机器可读源，记为「无法核验」并三处登记（见 `P1-收口.md`） |')
p.write_text(t,encoding='utf-8')
print('ok')
