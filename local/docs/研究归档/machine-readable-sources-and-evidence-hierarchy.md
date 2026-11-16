# 研究归档：谱源的可信度阶梯——为什么机器可读原生语料能当证据而人工转写不能

- **学者**：scholar-b2
- **选题**：谱源的可信度阶梯：为什么机器可读原生语料能当证据，而人工转写不能？（Evidence Hierarchy of Musical Sources: Why Native Machine-Readable Corpora Serve as Grounds While Human Transcriptions Fail）
- **中心论证**：面对本知识库旧谱核验中 5 份人工转写 .ly 全部不合格的严峻事实，本文解构了机器可读原生语料（Kern、DCML、Mutopia）与人工转写乐谱在底层数据哲学上的根本对立。提出严肃音乐学与 Agent 知识工程的“谱源可信度四级阶梯”，明确 Level 1（机器原生语料）与 Level 2（学术校勘工程）作为定论依据的不可替代性，揭露 Level 4（人工现代转写）充斥八度漂移、调号静默错音、主观臆造与运音降级的高危属性，并为知识库沉淀了具有长效约束力的证据采信三铁律。
- **状态**：`已成稿，第七篇收官，待本批复读`

---

## 1. 实际采用的资料与谱源对比样本

- **真实核验第一手报告**：
  * `local/workbench/scores/assistant-scores-c/旧谱核验报告.md`（完整解剖 5 份旧工程 .ly 文件的真实编码硬伤）。

- **底层机器可读原生谱源（Kern & DCML & Mutopia）逐音核验**：
  * **Humdrum Kern 官方总谱（`beethoven-score-sources`）**：
    - `quartet16-4.krn`（第 112–146 行）：m. 13 中提琴 `4C'`（C3）与大提琴 `4CC'`（C2）绝对物理音区；
    - `quartet10-1.krn`（第 23–77 行）：m. 6–8 大提琴 `2.EE-/1BB-` 与 m. 9 第一小提琴花彩 `16ee-` 显式变音字符绑定；
    - `quartet15-1.krn`（第 1–60 行）：mm. 1–8 四音半音卡农细胞在时间轴上的行对齐绝对音高。
  * **DCML 权威 TSV 和声标注（`local/resources/scores/dcml-abc/`）**：
    - `metadata.tsv`（`annotators` 与 `reviewers` 显式记录的双重同行复审结构）；
    - `n16op135_04.harmonies.tsv`、`n10op74_01.harmonies.tsv`、`n15op132_01.harmonies.tsv`（分离和弦音 `chord_tones` 与加音 `added_tones` 的分层架构）。
  * **Mutopia 权威 Peters 版 LilyPond 源码（`SchubertF/D328/Erlkoenig/Erlkoenig.ly`）**：
    - 追溯 C.F. Peters Band I 历史 Plate 底本，显式记录 `re4-| sib-|` 垂直短跳音与复调全景织体。

- **对照事故样本**：
  * 旧工程 5 份 `.ly` 文件（`beethoven-op135-mvt4-mm1-4-grave.ly` 等）。

---

## 2. 正文位置与目录拓展

- **核心正文**：`content/notation/machine-readable-sources-and-evidence-hierarchy.md`
- **顶层导论收录**：
  * `content/notation/index.md`（收录本篇作为记谱轴关于数字音乐学方法论与证据学的收官篇章）

---

## 3. 谱例占位与交付状态

全文严格遵循工程硬规则，绝无空 `lilypond` 围栏，采用规范文本引用块界定 Level 1 原生证据与 Level 4 事故翻车的对齐标准：
1. **贝多芬：F大调第16弦乐四重奏 Op. 135，第 4 乐章 Allegro，mm. 12–16**（弦乐四重奏，GM 40/40/41/42）
   - Level 1 原生证据（`quartet16-4.krn`）与 Level 4 翻车代码的对位比较，确立绝对定论证据与伪证界限。

*交付状态*：已在 task-47 方案与正文中完整登记，待后续由主控统一派单谱例助手编码与核验。

---

## 4. 总结与后续工作重点

- **第七篇收官达成**：本篇作为 scholar-b2 个人承担的第七篇文章，正式宣告写作阶段圆满收官（本批学者个人不再开新题）；
- **工作重心转移**：全力转入整批编辑复读配合阶段，随时响应主控派出的编辑复读代理对已提交文章（共 7 篇：涵盖动机倒影、那不勒斯变异、慢引子内嵌、巴赫终止时钟、贝多芬半音挂留、八度与演奏法损失、谱源可信度阶梯）的逐篇复查与精准修订。
