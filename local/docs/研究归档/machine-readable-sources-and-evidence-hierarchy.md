# 研究归档：谱源的可信度阶梯——为什么机器可读原生语料能当证据而人工转写不能

- **学者**：scholar-b2（初稿与事故解剖），scholar-b3（第二波深化核验与收尾）
- **选题**：谱源的可信度阶梯：为什么机器可读原生语料能当证据，而人工转写不能？（Evidence Hierarchy of Musical Sources: Why Native Machine-Readable Corpora Serve as Grounds While Human Transcriptions Fail）
- **中心论证**：面对本知识库旧谱核验中 5 份人工转写 .ly 全部不合格的严峻事实，本文解构了机器可读原生语料（Kern、DCML、Mutopia）与人工转写乐谱在底层数据哲学上的根本对立。提出严肃音乐学与 Agent 知识工程的“谱源可信度四级阶梯”，明确 Level 1（机器原生语料）与 Level 2（学术校勘工程）作为定论依据的不可替代性，揭露 Level 4（人工现代转写）充斥八度漂移、调号静默错音、主观臆造与运音降级的高危属性，并为知识库沉淀了具有长效约束力的证据采信三铁律。
- **状态**：`第二波核验完成，已去除内部代号，已接入真实语料路径与本地核验报告，待 lead 验收`

---

## 1. 实际采用的资料与谱源对比样本

- **真实核验第一手报告**：
  * `local/workbench/scores/assistant-scores-c/旧谱核验报告.md`（完整解剖 5 份旧工程 .ly 文件的真实编码硬伤）。

- **底层机器可读原生谱源（Kern & DCML & Mutopia）逐音核验**：
  * **Humdrum Kern 官方总谱（本工作树真实路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/`）**：
    - `quartet16-4.krn`（第 112–146 行，=12 至 =16 小节）：m. 13 中提琴 `4C'`（C3）与大提琴 `4CC'`（C2）绝对物理音区；
    - `quartet10-1.krn`（第 23–77 行，=1 至 =9 小节）：m. 6–8 大提琴 `2.EE-/1BB-` 与 m. 9 第一小提琴花彩 `16ee-` 显式变音字符绑定；
    - `quartet15-1.krn`（第 1–60 行，=1 至 =8 小节）：mm. 1–8 四音半音卡农细胞在时间轴上的行对齐绝对音高。
  * **DCML 权威 TSV 和声标注与元数据（DCML 规范，本工作树无独立副本）**：
    - `metadata.tsv`（`annotators` 与 `reviewers` 显式记录的双重同行复审结构）；
    - `n16op135_04.harmonies.tsv`、`n10op74_01.harmonies.tsv`、`n15op132_01.harmonies.tsv`（分离和弦音 `chord_tones` 与加音 `added_tones` 的分层架构）。
  * **Mutopia 权威 Peters 版 LilyPond 源码（基于 C.F. Peters Band I 底本，本工作树无独立副本）**：
    - `SchubertF/D328/Erlkoenig/Erlkoenig.ly`：追溯 C.F. Peters Band I 历史 Plate 底本，显式记录 `re4-| sib-|` 垂直短跳音与复调全景织体。

- **对照事故样本**：
  * 早期 5 份人工转写 `.ly` 文件（`beethoven-op135-mvt4-mm1-4-grave.ly`、`beethoven-op135-mvt4-mm12-16-allegro.ly`、`beethoven-op74-mvt1-mm1-9-adagio.ly`、`schubert-d328-mm1-5-prelude.ly`、`schubert-d328-mm72-76-mein-vater.ly`）。

---

## 2. 正文位置与目录拓展

- **核心正文**：`content/notation/machine-readable-sources-and-evidence-hierarchy.md`
- **顶层导论收录**：
  * `content/notation/index.md`（收录本篇作为记谱轴关于数字音乐学方法论与证据学的收官篇章）

---

## 3. 谱例占位与交付状态

全文严格遵循工程硬规则，绝无空 `lilypond` 围栏，采用规范文本引用块界定 Level 1 原生证据与 Level 4 事故翻车的对齐标准：
1. **贝多芬：F大调第16弦乐四重奏 Op. 135，第 4 乐章 Allegro，mm. 12–16**（弦乐四重奏，GM 40/40/41/42）
   - Level 1 原生证据（`quartet16-4.krn`）与 Level 4 翻车代码的对位比较，确立绝对定论证据与伪证界限（谱例收录于同库《核心细胞的倒影变形与和声再语境化》）。

*交付状态*：正文中无独立代码围栏，跨篇关联《核心细胞》已收录谱例，文末明确指引核验报告位置。

---

## 4. 总结与后续工作重点

- **第七篇收官达成**：本篇作为记谱轴核心方法论篇章，为全库的证据采信建立四级阶梯标准；
- **全库证据链闭环**：结合各分析篇章的实际核验经历，使读者和后续研究 Agent 明确区分机器可读原生语料（Level 1）与人工现代转写谱（Level 4）的本质差异。

---

## 5. 2026-11-20 第二波逐篇深度核验与收尾记录（scholar-b3）

- **规则 A 清洗**：
  - 正文第 11 行去除 `assistant-scores-c` 与“独立核验团队”等工程内部代号，改为面向读者的“当针对早期遗留的 5 份现代人工转写 .ly 文件进行独立逐音校勘时（详见文末核验记录说明）”，并在文末标注引导读者查阅内部审计记录 `local/workbench/scores/assistant-scores-c/旧谱核验报告.md`；
- **规则 B 与 D 落实**：
  - 正文第 77 行（原 86 行）去除行号 `Lines 112–146`，改用具体小节定位 `mm. 12–16`；将正文“独立核验代理”调整为“独立核验流程”；
  - 确认本工作树中真实存在的路径：核验报告 `local/workbench/scores/assistant-scores-c/旧谱核验报告.md` 以及贝多芬弦乐四重奏 Kern 语料库 `local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/`；
  - 严格核验 `quartet16-4.krn`（m.13 中提琴 C3、大提琴 C2）、`quartet10-1.krn`（m.9 花彩 `16ee-`）、`quartet15-1.krn`（mm. 1–8 半音卡农细胞绝对物理音高），行段对应完全属实；
- **图表升级**：
  - 将原 ASCII 阶梯图替换为合规的 Mermaid `flowchart TD` 图表，节点文字全部用双引号包裹并用 `<br>` 换行，语法自查通过；
- **完善 provenance**：
  - 更新 `provenance/notation/machine-readable-sources-and-evidence-hierarchy.md`，填入本地核验报告、Kern 官方总谱、DCML 和声标注与 Mutopia 源码出处；在“谱例”表中登记关联作品，许可标为“未确认”；
- **待补与未决事项**：
  - DCML TSV 数据集与 Mutopia LilyPond 源码在本工作树中无本地独立副本，属于外部学术标准参考；
  - 谱例许可统一登记为“未确认”，待主库统一确定授权状态。

## 复读状态

- 2026-11-22：**已复读**（差异复读 + 按篇修订已落地；本条由主控按工作流 §6 回填）。

