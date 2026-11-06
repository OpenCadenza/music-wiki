# beethoven-context

> 来源说明：[原始 README](../../../../../origin_resources/sources/beethoven-context/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/beethoven-context/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：15；状态计数：{"cached": 8, "failed": 7}。

## 来源说明摘要

贝多芬研究、草稿与版本依据 类型：音乐学分析、创作过程与学术版本说明；并非 ABC/LilyPond 乐谱库。来源为 Boston University Center for Beethoven Research、Beethoven-Haus、Henle、MTO 与作者官网。Werkstatt 为未取得的候选。 download.py 内逐项记录官方链接；manifest.json 记录实际下载结果、大小和哈希。raw/ 保存 HTML/PDF，仍保留作者及出版者权利，仅作为本地研究资料，不随知识库发布。下载状态不代替实际阅读记录。 目录结构：README.md（说明）、download.py（获取脚本）、manifest.json（结果）、raw/（原始资料）。 在本目录运行 python download.py，可通过 MUSICLIBRARYPROXY 设置代理。默认复用本地文件，并保留失败结果；需要重试时明确执行 python download.py --only <来源ID --retry-failed，每项仅一次有界请求。不会因重跑而无限请求已失败网址。 实际读取范围见 context-sources.md。BU 的 sketches 总页只是目录；实质内容在另取的 I/III/V 章。Henle 的 henle-sonatas-commentary.pdf 是1975/76年前言，文件名沿用早期记录，不是逐曲校勘报告。MTO两篇和Igoa资料本地下载仍失败，但所需段落已通过网页阅读工具读取；不得计为取得完整本地正文。研究项目介绍和学术分析的摘要都不能替代每部作品的原谱。

## 清单条目

- **Judith Ofcarcik: Multi-Strand Musical Narratives (MTO 2020)** — 状态：failed；目标路径未实存：raw/ofcarcik-2020.html；来源：https://www.mtosmt.org/issues/mto.20.26.2/mto.20.26.2.ofcarcik.html；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.；结果备注：<urlopen error _ssl.c:1063: The handshake operation timed out>
- **Beethoven-Haus: Beethoven and the Art of Fugue exhibition booklet** — 状态：failed；目标路径未实存：raw/haus-fugue-2022.pdf；来源：https://internet.beethoven.de/pdf-web/fuge_begleitheft_en_screen；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.；结果备注：<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)>
- **Hepokoski: Formal Process, Sonata Theory, and Tempest (MTO 2010)** — 状态：failed；目标路径未实存：raw/hepokoski-tempest.html；来源：https://www.mtosmt.org/issues/mto.10.16.2/mto.10.16.2.hepokoski.html；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.；结果备注：<urlopen error _ssl.c:1063: The handshake operation timed out>
- **Boss: Schenkerian-Schoenbergian Analysis, Beethoven Op.10 No.1 (MTO 1999)** — 状态：failed；目标路径未实存：raw/boss-op10-1.html；来源：https://www.mtosmt.org/issues/mto.99.5.1/mto.99.5.1.boss.html；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.；结果备注：<urlopen error _ssl.c:1063: The handshake operation timed out>
- **Enrique Igoa: Functional Harmony, revised 2023** — 状态：failed；目标路径未实存：raw/igoa-functional-harmony.pdf；来源：https://www.enriqueigoa.com/articulos_y_libros/Functional_Harmony.pdf；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.；结果备注：<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)>
- **Lockwood: Sources of Knowledge of Beethoven’s Compositional Procedures** — 状态：cached；原件：[raw/lockwood-procedures.html](../../../../../origin_resources/sources/beethoven-context/raw/lockwood-procedures.html)；来源：https://www.bu.edu/beethovencenter/i-sources-of-knowledge-of-beethovens-compositional-procedures/；字节：98095；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.
- **Lockwood: Stages of Knowledge of Sources** — 状态：cached；原件：[raw/lockwood-stages.html](../../../../../origin_resources/sources/beethoven-context/raw/lockwood-stages.html)；来源：https://www.bu.edu/beethovencenter/iii-stages-of-knowledge-of-sources/；字节：96649；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.
- **Lockwood: Gustav Nottebohm** — 状态：cached；原件：[raw/lockwood-nottebohm.html](../../../../../origin_resources/sources/beethoven-context/raw/lockwood-nottebohm.html)；来源：https://www.bu.edu/beethovencenter/v-gustav-nottebohm-1817-1882/；字节：97941；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.
- **Lewis Lockwood: Beethoven’s Sketches, the State of our Knowledge** — 状态：cached；原件：[raw/lockwood-sketches.html](../../../../../origin_resources/sources/beethoven-context/raw/lockwood-sketches.html)；来源：https://www.bu.edu/beethovencenter/beethovens-sketches-the-state-of-our-knowledge/；字节：96805；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.
- **Beethoven-Haus: scholarly studies, editions and sketches** — 状态：cached；原件：[raw/haus-studies.html](../../../../../origin_resources/sources/beethoven-context/raw/haus-studies.html)；来源：https://www.beethoven.de/en/studies；字节：68422；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.
- **Beethoven-Haus Digital Archive: scope and source descriptions** — 状态：cached；原件：[raw/haus-archive.html](../../../../../origin_resources/sources/beethoven-context/raw/haus-archive.html)；来源：https://www.beethoven.de/en/archive；字节：72950；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.
- **Beethovens Werkstatt: research project and modules** — 状态：failed；目标路径未实存：raw/werkstatt-project.html；来源：https://beethovens-werkstatt.de/projekt/；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.；结果备注：<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)>
- **Beethovens Werkstatt: prototype editions** — 状态：failed；目标路径未实存：raw/werkstatt-prototypes.html；来源：https://beethovens-werkstatt.de/prototypen/；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.；结果备注：<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)>
- **Henle: piano sonatas volume preface (1975/76)** — 状态：cached；原件：[raw/henle-sonatas-commentary.pdf](../../../../../origin_resources/sources/beethoven-context/raw/henle-sonatas-commentary.pdf)；来源：https://www.henle.de/media/21/33/94/1697725799/9032-1697725799-sync.pdf；字节：71123；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.
- **Henle: Op.2 sonatas preface** — 状态：cached；原件：[raw/henle-op2-preface.pdf](../../../../../origin_resources/sources/beethoven-context/raw/henle-op2-preface.pdf)；来源：https://www.henle.de/media/68/08/f4/1697725903/0832-1697725903-sync.pdf；字节：135866；权利说明：Original author/publisher rights retained; local research cache, not a redistribution license.

## 本地阅读副本

- [haus-archive.html](../../../../text/source-copies/beethoven-context/haus-archive.html)
- [haus-studies.html](../../../../text/source-copies/beethoven-context/haus-studies.html)
- [lockwood-nottebohm.html](../../../../text/source-copies/beethoven-context/lockwood-nottebohm.html)
- [lockwood-procedures.html](../../../../text/source-copies/beethoven-context/lockwood-procedures.html)
- [lockwood-sketches.html](../../../../text/source-copies/beethoven-context/lockwood-sketches.html)
- [lockwood-stages.html](../../../../text/source-copies/beethoven-context/lockwood-stages.html)

## 整理后的 HTML 正文

- [Archiv - Beethoven-Haus Bonn](../../../../text/organized-html/beethoven-context/haus-archive.md)（4055 字符）
- [Studies | Beethoven-Haus Bonn](../../../../text/organized-html/beethoven-context/haus-studies.md)（9281 字符）
- [V. Gustav Nottebohm (1817-1882) | Center for Beethoven Research](../../../../text/organized-html/beethoven-context/lockwood-nottebohm.md)（2488 字符）
- [I. Sources of knowledge of Beethoven’s compositional procedures | Center for Beethoven Research](../../../../text/organized-html/beethoven-context/lockwood-procedures.md)（2928 字符）
- [Beethoven’s Sketches: the State of our Knowledge | Center for Beethoven Research](../../../../text/organized-html/beethoven-context/lockwood-sketches.md)（1163 字符）
- [III. Stages of Knowledge of Sources | Center for Beethoven Research](../../../../text/organized-html/beethoven-context/lockwood-stages.md)（1757 字符）


## 其他清单元数据

{}

<!-- unified-ocr:start -->
## OCR 阅读副本

以下页数是PDF物理页数；转换可读不表示学者已读。原谱图像的OCR文字不能充当音符编码。

- **henle-op2-preface.pdf**（15页）— converted_readable；[1-15](../../../../text/ocr/beethoven-context/henle-op2-preface/henle-op2-preface.md)
- **henle-sonatas-commentary.pdf**（3页）— converted_readable；[1-3](../../../../text/ocr/beethoven-context/henle-sonatas-commentary/henle-sonatas-commentary.md)

<!-- unified-ocr:end -->
