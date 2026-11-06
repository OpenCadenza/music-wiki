# 文本与编码谱源入口

> 初步整理索引。来源卡、目录页、摘要、失败下载均保留状态；这些记录不代表已读完全文或已核验音乐事实。

来源数：26；raw 文本副本 76 个，关联图像 9 个；跟踪 ZIP 9 个；另有 5 个机器可读谱包已选取解包。

## 来源卡

- [abcnotation](sources/abcnotation.md)（清单条目 5）
- [abcplus](sources/abcplus.md)（清单条目 42）
- [alan-belkin](sources/alan-belkin.md)（清单条目 3）
- [bach-digital](sources/bach-digital.md)（清单条目 1）
- [beethoven-analysis-chamber](sources/beethoven-analysis-chamber.md)（清单条目 10）
- [beethoven-analysis-keyboard](sources/beethoven-analysis-keyboard.md)（清单条目 17）
- [beethoven-analysis-orchestral](sources/beethoven-analysis-orchestral.md)（清单条目 26）
- [beethoven-context](sources/beethoven-context.md)（清单条目 15）
- [beethoven-score-sources](sources/beethoven-score-sources.md)（清单条目 11）
- [chopin-online](sources/chopin-online.md)（清单条目 1）
- [dcml](sources/dcml.md)（清单条目 1）
- [humdrum](sources/humdrum.md)（清单条目 1）
- [imslp](sources/imslp.md)（清单条目 1）
- [josquin](sources/josquin.md)（清单条目 1）
- [lilypond-snippets](sources/lilypond-snippets.md)（清单条目 5）
- [mit-ocw](sources/mit-ocw.md)（清单条目 10）
- [music-theory-online](sources/music-theory-online.md)（清单条目 12）
- [mutopia](sources/mutopia.md)（清单条目 4241）
- [open-music-theory](sources/open-music-theory.md)（清单条目 4）
- [openscore-lieder](sources/openscore-lieder.md)（清单条目 1）
- [openscore-stringquartets](sources/openscore-stringquartets.md)（清单条目 1）
- [partimenti](sources/partimenti.md)（清单条目 11）
- [pdmx](sources/pdmx.md)（清单条目 4）
- [philharmonia](sources/philharmonia.md)（清单条目 12）
- [rubin-composition](sources/rubin-composition.md)（清单条目 2）
- [the-session](sources/the-session.md)（清单条目 2）

## 可读材料

- [OMT 旧版教材阅读入口](../../../text/open-music-theory/README.md)：官方 GitHub 旧版源码，非 OMT2。抽取 500 项；现有 Markdown 与官方源码同路径 SHA-256 一致 130 项；已改写 378 个可解析的站内链接，另有 1 个源链接目标未取得或未识别。
- [DCML 标注 TSV 说明](../../../scores/dcml-abc/README.md)：[阅读副本目录](../../../scores/dcml-abc/)，纳入 351 项，排除未登记来源的 `_reviewed.tsv` 70 项；需结合 ABC 原件及数据字典使用。
- [整理后的 HTML 正文阅读入口](../../../text/organized-html/README.md)：58 篇正文；原始 HTML 副本仍在 [source-copies](../../../text/source-copies/)，目录、摘要和错误页未作为正文。

- [机器可读谱包副本](../../../scores/source-packages/README.md)：从 Beethoven Kern、Bach 370 Chorales、Josquin、DCML ABC 指定原包解出 2065 个原生谱文件；不编译或转换。

- [本地可读性抽样记录](qa.json)：覆盖教材、MTO、Philharmonia、作品/版本 HTML 和 Beethoven Kern 谱。

- [既有谱源总目录](../../../../materials/scores/CATALOG.md)（811 个文件）；[第二批贝多芬奏鸣曲记录](../../../../materials/scores/BATCH2-INDEX.md)。

## 大型谱包和未处理项

- ZIP 目录数量及类型见 `index.json` 的 `archives`。MIT/OCW 与 OpenScore 大包只记目录；PDMX TAR 不展开。
- 原始 PDF/JPG 的 OCR 由专用 OCR 流程处理；本脚本不读取或转换这些文件。
- 失败、blocked、未取得、仅目录页、在线未缓存等状态见逐来源卡及原始 manifest。
- 旧生成文章、模型输出、提示词、日志和临时文件不得作为可信资料；排除项列在 `index.json`。
