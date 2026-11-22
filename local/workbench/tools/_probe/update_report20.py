import pathlib
p=pathlib.Path('local/docs/实施记录/2026-11-22-第二轮/完成报告.md')
t=p.read_text(encoding='utf-8')
t=t.replace('# 第二轮完成报告（18 篇阶段，2026-11-22 19:15）','# 第二轮完成报告（20 篇，2026-11-22 23:0x）')
t=t.replace('- 新文章 **18 篇**（计划约 20 篇）。a4《和声节奏》、c4《长笛写作》两篇因 gemini 5 小时额度在 17:5x 用尽，按用户指示 20:30 后补写。','- 新文章 **20 篇**（计划约 20 篇）。a4《和声节奏》、c4《长笛写作》在 20:30 gemini 额度恢复后补写完成，已过 reviewer-2 快速复核并修正。')
t=t.replace('- 已推送 `scholar-agent-dev`：`7ca07db..18fdcc5`（18 篇状态）。','- 已推送 `scholar-agent-dev` 快照；最终 20 篇状态在收口后推送。')
t=t.replace('1. 20:30 后唤醒 `scholar-a4`（S107 和声节奏）、`scholar-c4`（S307 长笛写作），各 150–250 行、单行占位、双门禁。\n2. 验收提交后跑全量门禁 + `pnpm build`，更新文档，最终 `git push origin HEAD:scholar-agent-dev`。\n3. 可选：请 reviewer-2 对最后两篇做一次快速复核。','1. 20 篇已全部提交，reviewer-2 已复核最后两篇并修正。\n2. 收口：全量门禁 + `pnpm notation`/`build:site`，更新文档，最终 `git push origin HEAD:scholar-agent-dev`。')
p.write_text(t,encoding='utf-8')
print('ok')
