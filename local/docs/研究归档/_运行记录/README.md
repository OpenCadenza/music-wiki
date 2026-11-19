# 学者运行记录（2026-11-16 首批）

这些文件是从 DSH 会话日志导出的完整运行记录，保留每位学者的提示词、回复、工具调用与思考摘要，供续任学者在原作者的判断基础上继续工作。

- 来源：`~/.dsh/sessions/<workspace>/<sessionId>/session.v4.jsonl.zstd`（zstd 流，按事件导出）。
- 处理：助手与用户正文保留；工具参数截断到约 240 字、工具结果截断到约 360 字、思考过程截断到约 240 字，并标注省略。
- 导出脚本：`local/workbench/tools/_probe/export_scholar_logs.py`（可重跑）。

## 学者与文章归属

| 学者 | 运行记录 | 负责的文章 |
| --- | --- | --- |
| scholar-a | `scholar-a.md` | `techniques/structure/galant-schemata-and-formal-functions.md` |
| scholar-a2 | `scholar-a2.md` | 增六和弦、慢引子、终止延后、海米奥拉、混合乐段（并接手加兰特图式） |
| scholar-b | `scholar-b.md` | `techniques/material/motivic-inversion-and-harmonic-recontextualization.md` |
| scholar-b2 | `scholar-b2.md` | 半音挂留、众赞歌声部时钟、挂留力学、机器可读谱源、谱号八度、那不勒斯（并接手动机构思） |
| scholar-c | `scholar-c.md` | 音响平面、音色标点、管弦乐音色、钢琴三重奏、弦乐四重奏、管乐五重奏、乐思与媒介 |
| scholar-c2 | `scholar-c2.md` | 接手 scholar-c 的七篇并完成收尾 |
| scholar-1/2/3 | `scholar-1.md` 等 | 最早一轮探索，仅作历史参考 |

文章与学者的对应也写在 `local/docs/研究归档/<slug>.md` 的“学者”字段。

## 续任学者怎么用

1. 先读你的前任那份运行记录（全文），再读对应文章的归档与正文。
2. 记录里能看到前任读过什么、怎么判断、哪些问题没解决；续作时沿用同一思路，不要另起一套。
3. 如果发现前任的结论有问题，在归档里写清依据再改，不要静默推翻。
