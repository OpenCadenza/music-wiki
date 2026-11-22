import pathlib
p=pathlib.Path('local/docs/实施记录/2026-11-22-第二轮/已写选题清单.md')
t=p.read_text(encoding='utf-8')
if '和声节奏' not in t:
    t += '| 和声节奏 | 和声变更频率如何组织乐句推进、制造终止期待与结构高潮？ | `content/techniques/harmony/harmonic-rhythm-and-syntactic-pacing.md` |\n'
    t += '| 长笛写作 | 长笛的音区声能、发音力学与配器功能如何决定其管弦乐写作？ | `content/techniques/sound/flute-writing-and-orchestral-acoustics.md` |\n'
p.write_text(t,encoding='utf-8')

p2=pathlib.Path('local/docs/实施记录/2026-11-22-第二轮/中止与交接.md')
t2=p2.read_text(encoding='utf-8')
t2=t2.replace('## 4. 完成状态\n\n- 新文章：**18 篇**（计划约 20 篇；a4《和声节奏》、c4《长笛写作》两篇因 gemini 5 小时额度在 17:5x 用尽，按用户指示待 20:30 后补写）。','## 4. 完成状态\n\n- 新文章：**20 篇**（计划约 20 篇；最后两篇《和声节奏》《长笛写作》已于 22:0x–22:5x 完成、复核并提交）。')
t2=t2.replace('- 任务板：S/A 卡已关闭到 A306；剩 task-50（S107 和声节奏）待 20:30 后开工。','- 任务板：S/A 卡已关闭到 A307。')
t2=t2.replace('- 推送：尚未推送；`scholar-agent-dev` 目标分支，待 20:30 两篇补齐后再做最终推送。','- 推送：18 篇快照已推送；20 篇最终状态在收口后推送 `scholar-agent-dev`。')
t2=t2.replace('## 5. 20:30 后要做的两件事\n\n1. 唤醒 `scholar-a4` 写 S107《和声节奏》、`scholar-c4` 写 S307《长笛写作》（提示词已发过，重发即可），各 150–250 行、单行占位、双门禁。\n2. 两篇验收提交后：跑全量门禁、`pnpm build`、更新本文件与进度日志、`git push origin HEAD:scholar-agent-dev`。','## 5. 收口清单\n\n1. 20 篇已全部验收；reviewer-2 已对最后两篇出快速复核并修正。\n2. 全量门禁 + `pnpm notation` / `build:site`，更新本文件与进度日志。\n3. 最终 `git push origin HEAD:scholar-agent-dev`。')
p2.write_text(t2,encoding='utf-8')
print('ok')
