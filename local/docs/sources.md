## 整理好的资料已经打包到https://drive.google.com/file/d/18csDqCQFRM1LOUsRHQzZy98XmUS_deS2/view?usp=sharing

# 当前资料来源链接与下载方法

资料记录更新于2026-10-29；2026-11-07迁入本开发分支并调整本地相对链接。本页按现存原件、来源清单、下载脚本和专题目录整理。覆盖26个来源目录、旧corpus谱库、9批历史专题记录及专题补充线索。旧AI文章、模型、提示词和日志不是外部学术资料，不循环列为知识来源。

本地“已取得”指能定位到原件，不表示已阅读、谱例正确或可再发布。失败／仅入口／未确认候选与实存全文分开。链接是取得时登记地址；本轮核对了部分官方入口，未把所有历史URL重新下载一遍。

## 1. 资料位置与范围

- 原始库：[music-wiki/local/origin_resources](../origin_resources)，来源包在sources，旧谱库在corpus，历史专题在collections。
- 阅读库：[music-wiki/local/resources/README.md](../resources/README.md)；原件及来源关系保留，OCR／清理／转码写阅读副本。
- 每源的README、manifest及下载脚本都保留在原始库；下表提供入口。脚本是取得时的工具，不自动等于完整恢复方案。
- 部分来源同时出现在多个专题表。条目数不相加当作去重后的文献数；历史“read”标签不当作本轮学者已读。

## 2. 通用下载方法

网页：打开具体文章／教材章节，保存HTML，并按研究需要保存正文图表。论文主页和PDF examples可能是不同文件，不能只存HTML就称图文齐全。PDF：优先取作者、期刊、出版社或大学机构库的实际文件链接；直链失效时回到条目页取得新链接。

GitHub：仓库Code → Download ZIP，或使用表中的归档链接。分支快照可能随上游变化；需重现相同内容时记录commit，并改用固定commit归档。方法见[GitHub官方说明](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)。

原谱图像：保存所需馆藏数字对象的具体页，记录条目URL、图像URL与数字页序。编码谱：整段或整目录取得必要include，不把单独的主.ly文件误当完整工程。

下载脚本通常会写自身目录下的raw和manifest。不要直接运行在封存原件上；在local/workbench建立保留相对结构的下载工作副本，随后登记新原件和加工副本。以下命令均从该工作副本根运行，**本页没有执行重新采集**：

```powershell
# 单源脚本：按第3节选择具体来源；不是所有脚本都会联网下载
python sources/alan-belkin/download.py

# 多文件Mutopia源码和可选MIDI；需要requests
python corpus/tools/fetch_mutopia.py --with-midi

# 取得ABC原始包；--no-split先只保留原包；需要requests
python corpus/tools/fetch_abc.py --no-split

# PDMX固定v1原包：断点续传及字节数／MD5／SHA-256记录
python sources/pdmx/download_archive.py
```

代理沿用当前环境，不修改系统代理。不同旧脚本分别使用MKB_DOWNLOAD_PROXY、MUSIC_LIBRARY_PROXY或显式--proxy；chamber旧脚本固定本地7890端口且需要pypdf。失败记录保留，有界重试；不要把403、超时或非PDF响应写成成功。

## 3. 26个来源总表

来源列可跳转到具体文件链接。所有来源都附原始清单和脚本；“已有”范围以实际材料为准，不代表整站或全集。

| 来源／官网 | 现有范围 | 下载方式／脚本 |
| --- | --- | --- |
| [Open Music Theory](#source-open-music-theory) · [官网／上游](https://viva.pressbooks.pub/openmusictheory/) | 旧版源码ZIP已取得；OMT2整书导出未取得，另有单章缓存 | 旧版取GitHub master归档；OMT2从官网导出PDF/EPUB/XML，原请求403须单列；[download.py](../origin_resources/sources/open-music-theory/download.py) |
| [Rubin: Music Composition & Theory](#source-rubin-composition) · [官网／上游](https://open.lib.umn.edu/musiccomposition/) | PDF/EPUB导出曾403，正文未取得 | 官网阅读／导出；保留实际失败，不把目录当全书；[download.py](../origin_resources/sources/rubin-composition/download.py) |
| [MIT OCW 21M.301](#source-mit-ocw) · [官网／上游](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/) | 已存整课ZIP、8份PDF及下载页 | 课程Download页取ZIP；作业／项目PDF逐项下载；[download.py](../origin_resources/sources/mit-ocw/download.py) |
| [Alan Belkin 配器资料](#source-alan-belkin) · [官网／上游](https://alanbelkinmusic.com/orchestration/) | 已存Artistic Orchestration PDF及2个介绍页 | 作者官网PDF直链；课程介绍不等于课程媒体已取得；[download.py](../origin_resources/sources/alan-belkin/download.py) |
| [Partimenti / Solfeggi](#source-partimenti) · [官网／上游](https://partimenti.org/partimenti/collections/index.html) | 已存5份历史PDF及4个目录／说明页；另2个未确认候选 | 从collections实际链接取Basili、Sala、Doll、Lorenzini、Paisiello；不猜PDF地址；[download.py](../origin_resources/sources/partimenti/download.py) |
| [Music Theory Online](#source-music-theory-online) · [官网／上游](https://mtosmt.org/) | 已存12篇HTML；具体论文URL已从专题目录恢复 | 论文页保存HTML及所需图像／PDF examples；现有download.py仅复制旧缓存；[download.py](../origin_resources/sources/music-theory-online/download.py) |
| [Philharmonia 乐器资源](#source-philharmonia) · [官网／上游](https://philharmonia.co.uk/resources/instruments/) | 已存入口及11种乐器HTML，无影音文件 | 从乐器入口进入具体乐器页，保存正文；媒体需另外取得；[download.py](../origin_resources/sources/philharmonia/download.py) |
| [LilyPond 2.26 官方片段](#source-lilypond-snippets) · [官网／上游](https://lilypond.org/doc/v2.26/Documentation/snippets/index.html) | 已存HTML及4份.ly源码 | 官方文档及stable/2.26仓库Raw文件；这些是工具例，不冒充作品原谱；[download.py](../origin_resources/sources/lilypond-snippets/download.py) |
| [Mutopia Project](#source-mutopia) · [官网／上游](https://www.mutopiaproject.org/ftp/) | corpus原清单有1,841个作品／乐章条目 | 从作品目录取.ly、同目录include及MIDI；重新采集用corpus/tools/fetch_mutopia.py；[download.py](../origin_resources/sources/mutopia/download.py) |
| [ABC Plus](#source-abcplus) · [官网／上游](https://abcplus.sourceforge.net/) | 已有ABC合唱原始包；包含演示文件，须区分 | 官网Choral/*.abc直链；现有来源脚本主要复用corpus；[download.py](../origin_resources/sources/abcplus/download.py) |
| [Humdrum / Bach chorales](#source-humdrum) · [官网／上游](https://github.com/craigsapp/bach-370-chorales) | 已存Bach ZIP并解出370份.krn | 实际下载Bach子库main ZIP，不把元仓库当全部谱库；[download.py](../origin_resources/sources/humdrum/download.py) |
| [Josquin Research Project](#source-josquin) · [官网／上游](https://github.com/josquin-research-project/jrp-scores) | 已存main ZIP并解出1,381份.krn | 官方仓库ZIP；官网https://josquin.stanford.edu/用于检索；[download.py](../origin_resources/sources/josquin/download.py) |
| [DCML Annotated Beethoven Corpus](#source-dcml) · [官网／上游](https://github.com/DCMLab/ABC) | 已存ABC-main.zip、140份.mscx及351份表格／元数据 | 下载选定ABC子库；不是整个DCML集合；标注与原谱分开使用；[download.py](../origin_resources/sources/dcml/download.py) |
| [OpenScore Lieder](#source-openscore-lieder) · [官网／上游](https://github.com/OpenScore/Lieder) | 已存main ZIP，约183MiB；先列目录 | 仓库Code → Download ZIP；按需解出目标歌曲及相关文件；[download.py](../origin_resources/sources/openscore-lieder/download.py) |
| [OpenScore StringQuartets](#source-openscore-stringquartets) · [官网／上游](https://github.com/OpenScore/StringQuartets) | 已存main ZIP，约584MiB；先列目录 | 仓库ZIP或目标谱Raw；格式以具体文件为准；[download.py](../origin_resources/sources/openscore-stringquartets/download.py) |
| [Beethoven Kern 与原谱选页](#source-beethoven-score-sources) · [官网／上游](https://github.com/craigsapp/beethoven-piano-sonatas) | 已存奏鸣曲／四重奏ZIP及3件馆藏各3张JPG | 两个Craig Sapp仓库ZIP；Beethoven-Haus选页按馆藏条目与记录的图像直链；[download.py](../origin_resources/sources/beethoven-score-sources/download.py) |
| [PDMX 固定v1数据包](#source-pdmx) · [官网／上游](https://github.com/pnlong/PDMX) | 已存Zenodo 13763756的PDMX.tar.gz，1,588,637,145字节 | 从固定Zenodo记录取原包并校验；不是后来全部MXL/PDF/MIDI扩展包；[download.py](../origin_resources/sources/pdmx/download.py) |
| [ABC notation 标准与检索](#source-abcnotation) · [官网／上游](https://abcnotation.com/) | 已存主页、检索帮助、版权说明、ABC 2.1标准；无曲调全集 | 保存具体标准／帮助页；单曲按条目取得，不把入口脚本当曲调全站采集器；[download.py](../origin_resources/sources/abcnotation/download.py) |
| [IMSLP 乐理文献目录](#source-imslp) · [官网／上游](https://imslp.org/wiki/Category:Music_theory) | 仅存类别HTML，未取得教材PDF | 从作品／文献条目选择实际文件下载；目录页不是PDF；[download.py](../origin_resources/sources/imslp/download.py) |
| [Chopin Online](#source-chopin-online) · [官网／上游](https://chopinonline.ac.uk/) | 仅存首页说明，未存初版／手稿全集 | 从项目作品条目进入数字对象，再按实际文件入口取得所需页；[download.py](../origin_resources/sources/chopin-online/download.py) |
| [Bach Digital](#source-bach-digital) · [官网／上游](https://www.bach-digital.de/) | 旧请求仅314字节，记blocked；无有效本地正文 | 网页按作品／来源检索，具体数字对象单独取得；旧首页响应不算已下载资料；[download.py](../origin_resources/sources/bach-digital/download.py) |
| [贝多芬草稿／版本与理论背景](#source-beethoven-context) · [官网／上游](https://www.bu.edu/beethovencenter/) | BU正文、Henle导言等已存；另有失败与仅在线线索 | 具体网页／PDF见逐项表；context脚本可按ID有限重试；[download.py](../origin_resources/sources/beethoven-context/download.py) |
| [键盘／变奏／四重奏研究](#source-beethoven-analysis-keyboard) · [官网／上游](https://www.gmth.de/) | 已存部分论文PDF／HTML／原码，另有在线未缓存及失败 | 期刊全文、机构库PDF或条目下载；逐篇链接与落地页均列于下表；[download.py](../origin_resources/sources/beethoven-analysis-keyboard/download.py) |
| [室内乐研究与版本导言](#source-beethoven-analysis-chamber) · [官网／上游](https://www.bu.edu/beethovencenter/) | 已存Barry、Ross、Raiser、出版社导言等；另有失败 | 出版社／机构库直链；后补资料不一定包含在最初download.py中；[download.py](../origin_resources/sources/beethoven-analysis-chamber/download.py) |
| [交响／协奏／声乐研究](#source-beethoven-analysis-orchestral) · [官网／上游](https://www.esm.rochester.edu/beethoven/) | Eastman正文、若干论文／样章已存，部分尝试失败 | Eastman网页逐篇保存；大学机构库PDF直链；样章与全书分开登记；[download.py](../origin_resources/sources/beethoven-analysis-orchestral/download.py) |
| [The Session（排除项）](#source-the-session) · [官网／上游](https://github.com/adactio/TheSession-data) | 仅保存许可文本，未采集曲调 | 原记录将此渠道排除；脚本仅取LICENSE，不是曲调下载方法；[download.py](../origin_resources/sources/the-session/download.py) |

### 脚本的实际边界

- mutopia、abcplus的sources入口主要复用corpus；真正重新获取谱库要用corpus/tools/fetch_mutopia.py或fetch_abc.py。
- music-theory-online/download.py只把collections下已有HTML复制过来，不能重下论文。具体论文地址已恢复到第4节；需要重取时按各论文URL取得全文及所需图表。
- abcnotation入口保存标准／帮助页；the-session只保存许可依据，不能把它们说成已采集曲调库。
- Bach Digital、Chopin Online、IMSLP的简短脚本只发有限网页请求，且不会完整重建manifest；新取得结果要重新登记。
- beethoven-context支持--only <ID> --retry-failed；keyboard也支持按ID重试。chamber会跳过已有记录，部分后补论文来自专题补充脚本，不能认为重跑原download.py就恢复所有后补资料。
- 旧脚本有不同的缓存／覆盖行为；重跑前读脚本，不作“全部可无损重跑”的统一保证。

## 4. 逐源具体文献、文件与直链

本节列来源清单中的具体URL。Mutopia的1,841个逐曲目录与文件关系见第5节的完整manifest；复用的ABC文件在第5节逐包列出。未确认候选仍标未确认，下载失败项不当作实存全文。

<a id="source-open-music-theory"></a>

### Open Music Theory（open-music-theory）

[来源说明](../origin_resources/sources/open-music-theory/README.md) · [原始清单](../origin_resources/sources/open-music-theory/manifest.json) · [下载脚本](../origin_resources/sources/open-music-theory/download.py)

另有LibreTexts的OMT2 Mediants单章缓存，见第6节；不能与OMT2整书导出混称。旧版上游为[openmusictheory/openmusictheory.github.io](https://github.com/openmusictheory/openmusictheory.github.io)，本地取得master快照。OMT2是Pressbooks教材；原清单中的导出失败端点不能当作旧版ZIP已含OMT2。

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| openmusictheory.github.io-master.zip | [地址](https://api.github.com/repos/openmusictheory/openmusictheory.github.io/zipball/master) | [原件](../origin_resources/sources/open-music-theory/raw/openmusictheory.github.io-master.zip)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| open-music-theory.xml | [地址](https://viva.pressbooks.pub/openmusictheory/open/download?type=wxr) | 未定位本地原件；旧状态：failed | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| open-music-theory.pdf | [地址](https://viva.pressbooks.pub/openmusictheory/open/download?type=pdf) | 未定位本地原件；旧状态：failed | 直链保存PDF；若失败从条目页重新进入 |
| open-music-theory.epub | [地址](https://viva.pressbooks.pub/openmusictheory/open/download?type=epub) | 未定位本地原件；旧状态：failed | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-rubin-composition"></a>

### Rubin: Music Composition & Theory（rubin-composition）

[来源说明](../origin_resources/sources/rubin-composition/README.md) · [原始清单](../origin_resources/sources/rubin-composition/manifest.json) · [下载脚本](../origin_resources/sources/rubin-composition/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| music-composition.pdf | [地址](https://open.lib.umn.edu/musiccomposition/open/download?type=pdf) | 未定位本地原件；旧状态：failed | 直链保存PDF；若失败从条目页重新进入 |
| music-composition.epub | [地址](https://open.lib.umn.edu/musiccomposition/open/download?type=epub) | 未定位本地原件；旧状态：failed | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-mit-ocw"></a>

### MIT OCW 21M.301（mit-ocw）

[来源说明](../origin_resources/sources/mit-ocw/README.md) · [原始清单](../origin_resources/sources/mit-ocw/manifest.json) · [下载脚本](../origin_resources/sources/mit-ocw/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| course-download-index.html | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/download/) | [原件](../origin_resources/sources/mit-ocw/raw/course-download-index.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| 6832bc8959d3cf094daa3ff0db0dfa43_asgnmnt1_sclecon.pdf | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/6832bc8959d3cf094daa3ff0db0dfa43_asgnmnt1_sclecon.pdf) | [原件](../origin_resources/sources/mit-ocw/raw/6832bc8959d3cf094daa3ff0db0dfa43_asgnmnt1_sclecon.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| 1c211eed4e5995d42c701ee93de0a06e_asgnmnt2_continu.pdf | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/1c211eed4e5995d42c701ee93de0a06e_asgnmnt2_continu.pdf) | [原件](../origin_resources/sources/mit-ocw/raw/1c211eed4e5995d42c701ee93de0a06e_asgnmnt2_continu.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| 2aa5a9f0c064677fdb79b8becdbf2fc5_asgnmnt2_keys_in.pdf | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/2aa5a9f0c064677fdb79b8becdbf2fc5_asgnmnt2_keys_in.pdf) | [原件](../origin_resources/sources/mit-ocw/raw/2aa5a9f0c064677fdb79b8becdbf2fc5_asgnmnt2_keys_in.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| ee19a1342a38393be325ef17f64fb912_asgnmnt3_triads.pdf | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/ee19a1342a38393be325ef17f64fb912_asgnmnt3_triads.pdf) | [原件](../origin_resources/sources/mit-ocw/raw/ee19a1342a38393be325ef17f64fb912_asgnmnt3_triads.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| 63900e60a0c16bf3ba082fec7f6d1ffc_asgnmnt4_part.pdf | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/63900e60a0c16bf3ba082fec7f6d1ffc_asgnmnt4_part.pdf) | [原件](../origin_resources/sources/mit-ocw/raw/63900e60a0c16bf3ba082fec7f6d1ffc_asgnmnt4_part.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| 1e2dff536bc156dd3f2f903885c3ff4c_asgnmnt5_twopart.pdf | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/1e2dff536bc156dd3f2f903885c3ff4c_asgnmnt5_twopart.pdf) | [原件](../origin_resources/sources/mit-ocw/raw/1e2dff536bc156dd3f2f903885c3ff4c_asgnmnt5_twopart.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| 695d904f02a6015a316583ae707e7118_final_proj_force.pdf | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/695d904f02a6015a316583ae707e7118_final_proj_force.pdf) | [原件](../origin_resources/sources/mit-ocw/raw/695d904f02a6015a316583ae707e7118_final_proj_force.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| 6b1ca66c13e4844f186011fb73cee0c9_final_proj_instr.pdf | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/6b1ca66c13e4844f186011fb73cee0c9_final_proj_instr.pdf) | [原件](../origin_resources/sources/mit-ocw/raw/6b1ca66c13e4844f186011fb73cee0c9_final_proj_instr.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| 21m.301-spring-2005.zip | [地址](https://ocw.mit.edu/courses/21m-301-harmony-and-counterpoint-i-spring-2005/21m.301-spring-2005.zip) | [原件](../origin_resources/sources/mit-ocw/raw/21m.301-spring-2005.zip)；旧状态：downloaded | 直链保存压缩包，核对类型与大小后解包 |

<a id="source-alan-belkin"></a>

### Alan Belkin 配器资料（alan-belkin）

[来源说明](../origin_resources/sources/alan-belkin/README.md) · [原始清单](../origin_resources/sources/alan-belkin/manifest.json) · [下载脚本](../origin_resources/sources/alan-belkin/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| bk-O-O.pdf | [地址](https://alanbelkinmusic.com/wp-content/uploads/2024/09/bk-O-O.pdf) | [原件](../origin_resources/sources/alan-belkin/raw/bk-O-O.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| orchestration-index.html | [地址](https://alanbelkinmusic.com/orchestration/) | [原件](../origin_resources/sources/alan-belkin/raw/orchestration-index.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| mini-courses-index.html | [地址](https://alanbelkinmusic.com/two-orchestration-mini-courses/) | [原件](../origin_resources/sources/alan-belkin/raw/mini-courses-index.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-partimenti"></a>

### Partimenti / Solfeggi（partimenti）

[来源说明](../origin_resources/sources/partimenti/README.md) · [原始清单](../origin_resources/sources/partimenti/manifest.json) · [下载脚本](../origin_resources/sources/partimenti/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| partimenti-index.html | [地址](https://partimenti.org/partimenti/index.html) | [原件](../origin_resources/sources/partimenti/raw/partimenti-index.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| collections-index.html | [地址](https://partimenti.org/partimenti/collections/index.html) | [原件](../origin_resources/sources/partimenti/raw/collections-index.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| about-parti.html | [地址](https://partimenti.org/partimenti/about_parti/index.html) | [原件](../origin_resources/sources/partimenti/raw/about-parti.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| solfeggi-series.html | [地址](https://partimenti.org/solfeggi/about_series/index.html) | [原件](../origin_resources/sources/partimenti/raw/solfeggi-series.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| basili_1776_smaller.pdf | [地址](https://partimenti.org/partimenti/collections/basili_1776_smaller.pdf) | [原件](../origin_resources/sources/partimenti/raw/basili_1776_smaller.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| sala_elementi_small.pdf | [地址](https://partimenti.org/partimenti/collections/sala_elementi_small.pdf) | [原件](../origin_resources/sources/partimenti/raw/sala_elementi_small.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| doll_regole_smaller.pdf | [地址](https://partimenti.org/partimenti/collections/doll_regole_smaller.pdf) | [原件](../origin_resources/sources/partimenti/raw/doll_regole_smaller.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| lorenzini_regs.pdf | [地址](https://partimenti.org/partimenti/collections/lorenzini_regs.pdf) | [原件](../origin_resources/sources/partimenti/raw/lorenzini_regs.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| paisiello_regole_1782.pdf | [地址](https://partimenti.org/partimenti/collections/paisiello_regole_1782.pdf) | [原件](../origin_resources/sources/partimenti/raw/paisiello_regole_1782.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| rule-of-the-octave.pdf | [地址](https://partimenti.org/partimenti/Rule_of_the_Octave.pdf) | 未定位本地原件；旧状态：unconfirmed_candidate | 候选未确认：先从官网目录核实，未实际请求 |
| solfeggi-exercises.pdf | [地址](https://partimenti.org/solfeggi/solfeggi/solfeggi.pdf) | 未定位本地原件；旧状态：unconfirmed_candidate | 候选未确认：先从官网目录核实，未实际请求 |

<a id="source-music-theory-online"></a>

### Music Theory Online（music-theory-online）

[来源说明](../origin_resources/sources/music-theory-online/README.md) · [原始清单](../origin_resources/sources/music-theory-online/manifest.json) · [下载脚本](../origin_resources/sources/music-theory-online/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| The Power of Anacrusis: Engendered Feeling in Groove-Based Musics | [地址](https://mtosmt.org/issues/mto.06.12.4/mto.06.12.4.butterfield.php) | [原件](../origin_resources/sources/music-theory-online/raw/butterfield-2006-anacrusis-925fd5fd6ae18339.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Sentential Lyric-Types in the Great American Songbook | [地址](https://mtosmt.org/issues/mto.13.19.3/mto.13.19.3.callahan.html) | [原件](../origin_resources/sources/music-theory-online/raw/callahan-2013-songbook-eccb660de9096bae.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beyond Strophic: Prolonged Refrains, Choruses, and Bridges in the Blues, 1923-1966 | [地址](https://mtosmt.org/issues/mto.25.31.1/mto.25.31.1.carter.html) | [原件](../origin_resources/sources/music-theory-online/raw/carter-2025-beyond-strophic-fed87a54548fd8e6.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| A Platonic Model of Funky Rhythms | [地址](https://mtosmt.org/issues/mto.16.22.2/mto.16.22.2.cohn.php) | [原件](../origin_resources/sources/music-theory-online/raw/cohn-2016-funky-rhythms-1119934417edfd1e.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Transformations in Tonal Jazz: ii–V Space | [地址](https://mtosmt.org/issues/mto.17.23.1/mto.17.23.1.mcclimon.html) | [原件](../origin_resources/sources/music-theory-online/raw/mcclimon-2017-ii-v-space-f5e0615fd8e97111.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Form and Voice Leading in Early Beatles Songs | [地址](https://www.mtosmt.org/issues/mto.11.17.3/mto.11.17.3.nobile.html) | [原件](../origin_resources/sources/music-theory-online/raw/nobile-2011-beatles-form-896fedffc7b2d8ce.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Guide-Tone Space: Navigating Voice-Leading Syntax in Tonal Jazz | [地址](https://mtosmt.org/issues/mto.19.25.2/mto.19.25.2.smither.html) | [原件](../origin_resources/sources/music-theory-online/raw/smither-2019-guide-tone-space-7de83ed3d933d645.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Referents in the Palimpsests of Jazz: Disentangling Theme from Improvisation in Recordings of Standard Jazz Tunes | [地址](https://mtosmt.org/issues/mto.24.30.3/mto.24.30.3.smither.html) | [原件](../origin_resources/sources/music-theory-online/raw/smither-2024-referents-37cd613f85f6fad8.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Formal Functions of Drum Patterns in Post-Millennial Pop Songs, 2012–2021 | [地址](https://mtosmt.org/issues/mto.24.30.2/mto.24.30.2.geary.html) | [原件](../origin_resources/sources/music-theory-online/raw/geary-2024-drum-form-b456dd257b4adbee.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Teleology in Verse–Prechorus–Chorus Form, 1965–2020 | [地址](https://mtosmt.org/issues/mto.22.28.3/mto.22.28.3.nobile.html) | [原件](../origin_resources/sources/music-theory-online/raw/nobile-2022-teleology-8bd39cf06d0420e6.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The Functions of Continuous Processes in Contemporary Electronic Dance Music | [地址](https://mtosmt.org/issues/mto.21.27.2/mto.21.27.2.smith.html) | [原件](../origin_resources/sources/music-theory-online/raw/smith-2021-continuous-edm-e5c1cc07614f99f3.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Codetta and Anthem Postchorus Types in Top-40 Pop from 2010 to 2015 | [地址](https://www.mtosmt.org/issues/mto.22.28.2/mto.22.28.2.stroud.html) | [原件](../origin_resources/sources/music-theory-online/raw/stroud-2022-postchorus-8de2b66247c586ab.html)；旧状态：cached-copy | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-philharmonia"></a>

### Philharmonia 乐器资源（philharmonia）

[来源说明](../origin_resources/sources/philharmonia/README.md) · [原始清单](../origin_resources/sources/philharmonia/manifest.json) · [下载脚本](../origin_resources/sources/philharmonia/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| instruments.html | [地址](https://philharmonia.co.uk/resources/instruments/) | [原件](../origin_resources/sources/philharmonia/raw/instruments.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| violin.html | [地址](https://philharmonia.co.uk/resources/instruments/violin/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/violin.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| cello.html | [地址](https://philharmonia.co.uk/resources/instruments/cello/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/cello.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| flute.html | [地址](https://philharmonia.co.uk/resources/instruments/flute/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/flute.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| oboe.html | [地址](https://philharmonia.co.uk/resources/instruments/oboe/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/oboe.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| clarinet.html | [地址](https://philharmonia.co.uk/resources/instruments/clarinet/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/clarinet.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| bassoon.html | [地址](https://philharmonia.co.uk/resources/instruments/bassoon/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/bassoon.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| trumpet.html | [地址](https://philharmonia.co.uk/resources/instruments/trumpet/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/trumpet.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| trombone.html | [地址](https://philharmonia.co.uk/resources/instruments/trombone/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/trombone.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| horn.html | [地址](https://philharmonia.co.uk/resources/instruments/horn/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/horn.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| tuba.html | [地址](https://philharmonia.co.uk/resources/instruments/tuba/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/tuba.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| percussion.html | [地址](https://philharmonia.co.uk/resources/instruments/percussion/) | [原件](../origin_resources/sources/philharmonia/raw/instruments/percussion.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-lilypond-snippets"></a>

### LilyPond 2.26 官方片段（lilypond-snippets）

[来源说明](../origin_resources/sources/lilypond-snippets/README.md) · [原始清单](../origin_resources/sources/lilypond-snippets/manifest.json) · [下载脚本](../origin_resources/sources/lilypond-snippets/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| snippets-index.html | [地址](https://lilypond.org/doc/v2.26/Documentation/snippets/index.html) | [原件](../origin_resources/sources/lilypond-snippets/raw/snippets-index.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| merging-multi-measure-rests-in-a-polyphonic-part.ly | [地址](https://raw.githubusercontent.com/lilypond/lilypond/stable/2.26/Documentation/snippets/merging-multi-measure-rests-in-a-polyphonic-part.ly) | [原件](../origin_resources/sources/lilypond-snippets/raw/snippets/merging-multi-measure-rests-in-a-polyphonic-part.ly)；旧状态：downloaded | 直链保存源码，并补齐同目录include |
| creating-cross-staff-arpeggios-in-a-piano-staff.ly | [地址](https://raw.githubusercontent.com/lilypond/lilypond/stable/2.26/Documentation/snippets/creating-cross-staff-arpeggios-in-a-piano-staff.ly) | [原件](../origin_resources/sources/lilypond-snippets/raw/snippets/creating-cross-staff-arpeggios-in-a-piano-staff.ly)；旧状态：downloaded | 直链保存源码，并补齐同目录include |
| customizing-the-position-and-number-of-dots-in-repeat-sign-bar-lines.ly | [地址](https://raw.githubusercontent.com/lilypond/lilypond/stable/2.26/Documentation/snippets/customizing-the-position-and-number-of-dots-in-repeat-sign-bar-lines.ly) | [原件](../origin_resources/sources/lilypond-snippets/raw/snippets/customizing-the-position-and-number-of-dots-in-repeat-sign-bar-lines.ly)；旧状态：downloaded | 直链保存源码，并补齐同目录include |
| isolated-percent-repeats.ly | [地址](https://raw.githubusercontent.com/lilypond/lilypond/stable/2.26/Documentation/snippets/isolated-percent-repeats.ly) | [原件](../origin_resources/sources/lilypond-snippets/raw/snippets/isolated-percent-repeats.ly)；旧状态：downloaded | 直链保存源码，并补齐同目录include |

<a id="source-mutopia"></a>

### Mutopia Project（mutopia）

[来源说明](../origin_resources/sources/mutopia/README.md) · [原始清单](../origin_resources/sources/mutopia/manifest.json) · [下载脚本](../origin_resources/sources/mutopia/download.py)

本来源记录的大量条目是corpus本地文件复用，不是额外下载。逐曲目录、ly_all／ly／mid文件名及SHA在第5节完整清单中。

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| upstream-README.rst | [地址](https://raw.githubusercontent.com/MutopiaProject/MutopiaProject/master/README.rst) | [原件](../origin_resources/sources/mutopia/raw/upstream-README.rst)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-abcplus"></a>

### ABC Plus（abcplus）

[来源说明](../origin_resources/sources/abcplus/README.md) · [原始清单](../origin_resources/sources/abcplus/manifest.json) · [下载脚本](../origin_resources/sources/abcplus/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| index.html | [地址](https://abcplus.sourceforge.net/) | [原件](../origin_resources/sources/abcplus/raw/index.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-humdrum"></a>

### Humdrum / Bach chorales（humdrum）

[来源说明](../origin_resources/sources/humdrum/README.md) · [原始清单](../origin_resources/sources/humdrum/manifest.json) · [下载脚本](../origin_resources/sources/humdrum/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| bach-370-chorales-main.zip | [地址](https://codeload.github.com/craigsapp/bach-370-chorales/zip/refs/heads/main) | [原件](../origin_resources/sources/humdrum/raw/bach-370-chorales-main.zip)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-josquin"></a>

### Josquin Research Project（josquin）

[来源说明](../origin_resources/sources/josquin/README.md) · [原始清单](../origin_resources/sources/josquin/manifest.json) · [下载脚本](../origin_resources/sources/josquin/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| jrp-scores-main.zip | [地址](https://codeload.github.com/josquin-research-project/jrp-scores/zip/refs/heads/main) | [原件](../origin_resources/sources/josquin/raw/jrp-scores-main.zip)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-dcml"></a>

### DCML Annotated Beethoven Corpus（dcml）

[来源说明](../origin_resources/sources/dcml/README.md) · [原始清单](../origin_resources/sources/dcml/manifest.json) · [下载脚本](../origin_resources/sources/dcml/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| ABC-main.zip | [地址](https://codeload.github.com/DCMLab/ABC/zip/refs/heads/main) | [原件](../origin_resources/sources/dcml/raw/ABC-main.zip)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-openscore-lieder"></a>

### OpenScore Lieder（openscore-lieder）

[来源说明](../origin_resources/sources/openscore-lieder/README.md) · [原始清单](../origin_resources/sources/openscore-lieder/manifest.json) · [下载脚本](../origin_resources/sources/openscore-lieder/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| Lieder-main.zip | [地址](https://codeload.github.com/OpenScore/Lieder/zip/refs/heads/main) | [原件](../origin_resources/sources/openscore-lieder/raw/Lieder-main.zip)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-openscore-stringquartets"></a>

### OpenScore StringQuartets（openscore-stringquartets）

[来源说明](../origin_resources/sources/openscore-stringquartets/README.md) · [原始清单](../origin_resources/sources/openscore-stringquartets/manifest.json) · [下载脚本](../origin_resources/sources/openscore-stringquartets/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| StringQuartets-main.zip | [地址](https://codeload.github.com/OpenScore/StringQuartets/zip/refs/heads/main) | [原件](../origin_resources/sources/openscore-stringquartets/raw/StringQuartets-main.zip)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-beethoven-score-sources"></a>

### Beethoven Kern 与原谱选页（beethoven-score-sources）

[来源说明](../origin_resources/sources/beethoven-score-sources/README.md) · [原始清单](../origin_resources/sources/beethoven-score-sources/manifest.json) · [下载脚本](../origin_resources/sources/beethoven-score-sources/download.py)

原脚本仅取两个Kern ZIP。Beethoven-Haus三件数字对象各取前三张JPG，共9张，非完整作品；清单保留各页原始图像URL，按该URL可重取同一页，链接失效时回馆藏条目重新解析公开METS中的FLocat图像地址。

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| beethoven-piano-sonatas-main.zip | [地址](https://github.com/craigsapp/beethoven-piano-sonatas) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-piano-sonatas-main.zip)；旧状态：未声明 | 仓库Code → Download ZIP，或固定commit归档 |
| beethoven-string-quartets-main.zip | [地址](https://github.com/craigsapp/beethoven-string-quartets) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-string-quartets-main.zip)；旧状态：未声明 | 仓库Code → Download ZIP，或固定commit归档 |
| Symphony No. 5 in C minor, Op. 67 | [地址](https://www.beethoven.de/de/media/view/6535079790641152) | 未定位本地原件；旧状态：未声明 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| symphony5-page-001.jpg（数字页1） | [原图](https://lh3.googleusercontent.com/d2bnNU4xG0gF2HOQGGZA4-xaVWy4asw8wfmmdZJCI9HdWG2botub0mOTYb1vQdTNWwfpJaAxc_L24_Sg8QEfuH4lZu4QexRJ2x-zjTPA=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/symphony5-page-001.jpg) | 直链保存JPG，保留上述馆藏条目 |
| symphony5-page-002.jpg（数字页2） | [原图](https://lh3.googleusercontent.com/Bbe3f1y-00MKwFrmTvNkz5icQyYveCCNqxKGt2FmFpHSG1VEvsQP4DtDvXmPm0rx2eV41Rz2DRNpheb1xG5u2s8YUW3hFqGdWj7avPhI=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/symphony5-page-002.jpg) | 直链保存JPG，保留上述馆藏条目 |
| symphony5-page-003.jpg（数字页3） | [原图](https://lh3.googleusercontent.com/hl29uSwNLSHyZfmdxwC5j92Hi1jkqsDNN-XgBhpT_4Rdzdh4Ds8x5UQ3e2NA6LZRuOyMmsxmpG1YPCt9ecvBfyXQjmTR_m5P-9q8n5Yvwg=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/symphony5-page-003.jpg) | 直链保存JPG，保留上述馆藏条目 |
| Piano Concerto No. 3 in C minor, Op. 37 | [地址](https://www.beethoven.de/en/media/view/6288763953086464) | 未定位本地原件；旧状态：未声明 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| piano-concerto3-page-001.jpg（数字页1） | [原图](https://lh3.googleusercontent.com/UhEA8auOB7q0z6jYTmaDMj3xRHOb83Tx9w_iZXd-STrAtmwFVRItk78SNgKl05QSPmcPVW9ysJCGF6Nty82VtYGC0afZv8StR-V2qEC2Fg=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/piano-concerto3-page-001.jpg) | 直链保存JPG，保留上述馆藏条目 |
| piano-concerto3-page-002.jpg（数字页2） | [原图](https://lh3.googleusercontent.com/sewfMRAWWv827_ogTI4TXWCzpRp2_tbEMMOy0tnRmQgkyTNFsjhJ8664xdhxjER_GCGcL8rWLVX9c-fpsDDk3oOsEU0dYF05ijSQZIq3aw=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/piano-concerto3-page-002.jpg) | 直链保存JPG，保留上述馆藏条目 |
| piano-concerto3-page-003.jpg（数字页3） | [原图](https://lh3.googleusercontent.com/vczbBSeFS14zhXhLIeVh5hE7bT2qMMYh5tFI9pePg2l7JyCLVo_2IUO_lOtUMOvDbA5-LDh9cQ4qfFTcMPbmrVa0XPGLN-n3tAXmUk1d5g=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/piano-concerto3-page-003.jpg) | 直链保存JPG，保留上述馆藏条目 |
| An die ferne Geliebte, Op. 98 (song cycle) | [地址](https://www.beethoven.de/en/media/view/6507161798574080) | 未定位本地原件；旧状态：未声明 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| op98-autograph-page-001.jpg（数字页1） | [原图](https://lh3.googleusercontent.com/rVSB8ypBrMlkhcrNDXQXdkG7VDMpmixbbu6HhXwMcx9M8ymPzjwTtle_EMwwT9W3goemoVc6QOkTkOv1Tk3ckO4kFD23EKjOAMCciKIzrg=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/op98-autograph-page-001.jpg) | 直链保存JPG，保留上述馆藏条目 |
| op98-autograph-page-002.jpg（数字页2） | [原图](https://lh3.googleusercontent.com/j-2fLfuZfybzvBYhicNm-42yR3bNrilPaGnw6ecfaPFHbs8eyAqwqLl8suXAE8g_m28fbhne8UHFVEPogSURY5iLPQc0qgKGjkAVpAGs=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/op98-autograph-page-002.jpg) | 直链保存JPG，保留上述馆藏条目 |
| op98-autograph-page-003.jpg（数字页3） | [原图](https://lh3.googleusercontent.com/7TpoEp3RuXJoAsmRuV-4jXk-8y90wiOUySAiJw7Ap1Dq3YlbPVBBJvyEgc_-ECbLPErc_XElzTyouYMWNWJGnVtsC9S8dH4dLnxFm7WDcQ=s0) | [原件](../origin_resources/sources/beethoven-score-sources/raw/beethoven-house-selected/op98-autograph-page-003.jpg) | 直链保存JPG，保留上述馆藏条目 |

<a id="source-pdmx"></a>

### PDMX 固定v1数据包（pdmx）

[来源说明](../origin_resources/sources/pdmx/README.md) · [原始清单](../origin_resources/sources/pdmx/manifest.json) · [下载脚本](../origin_resources/sources/pdmx/download.py)

当前固定记录为[Zenodo 13763756／v1](https://zenodo.org/records/13763756)。该版原包内主要为MusicRender JSON、metadata和CSV；不是后来扩展的全部MXL/PDF/MIDI。原包1,588,637,145字节；download_archive.py有四路HTTP范围续传及完整字节数、MD5、SHA-256检查。

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| README.md | [地址](https://raw.githubusercontent.com/pnlong/PDMX/main/README.md) | [原件](../origin_resources/sources/pdmx/raw/README.md)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| code-LICENSE.txt | [地址](https://raw.githubusercontent.com/pnlong/PDMX/main/LICENSE) | [原件](../origin_resources/sources/pdmx/raw/code-LICENSE.txt)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| zenodo-record.json | [地址](https://zenodo.org/api/records/13763756) | [原件](../origin_resources/sources/pdmx/raw/zenodo-record.json)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| PDMX.tar.gz | [地址](https://zenodo.org/records/13763756/files/PDMX.tar.gz?download=1) | [原件](../origin_resources/sources/pdmx/raw/PDMX.tar.gz)；旧状态：downloaded | 直链保存压缩包，核对类型与大小后解包 |

<a id="source-abcnotation"></a>

### ABC notation 标准与检索（abcnotation）

[来源说明](../origin_resources/sources/abcnotation/README.md) · [原始清单](../origin_resources/sources/abcnotation/manifest.json) · [下载脚本](../origin_resources/sources/abcnotation/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| index.html | [地址](https://abcnotation.com/) | [原件](../origin_resources/sources/abcnotation/raw/index.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| search-help.html | [地址](https://abcnotation.com/searchHelp) | [原件](../origin_resources/sources/abcnotation/raw/search-help.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| copyright.html | [地址](https://abcnotation.com/searchCopyright) | [原件](../origin_resources/sources/abcnotation/raw/copyright.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| abc-2.1-standard.html | [地址](https://abcnotation.com/wiki/abc:standard:v2.1) | [原件](../origin_resources/sources/abcnotation/raw/abc-2.1-standard.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-imslp"></a>

### IMSLP 乐理文献目录（imslp）

[来源说明](../origin_resources/sources/imslp/README.md) · [原始清单](../origin_resources/sources/imslp/manifest.json) · [下载脚本](../origin_resources/sources/imslp/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| music-theory-category.html | [地址](https://imslp.org/wiki/Category:Music_theory) | [原件](../origin_resources/sources/imslp/raw/music-theory-category.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-chopin-online"></a>

### Chopin Online（chopin-online）

[来源说明](../origin_resources/sources/chopin-online/README.md) · [原始清单](../origin_resources/sources/chopin-online/manifest.json) · [下载脚本](../origin_resources/sources/chopin-online/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| homepage.html | [地址](https://chopinonline.ac.uk/) | [原件](../origin_resources/sources/chopin-online/raw/homepage.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-bach-digital"></a>

### Bach Digital（bach-digital）

[来源说明](../origin_resources/sources/bach-digital/README.md) · [原始清单](../origin_resources/sources/bach-digital/manifest.json) · [下载脚本](../origin_resources/sources/bach-digital/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| homepage.html | [地址](https://www.bach-digital.de/) | 未定位本地原件；旧状态：blocked | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-beethoven-context"></a>

### 贝多芬草稿／版本与理论背景（beethoven-context）

[来源说明](../origin_resources/sources/beethoven-context/README.md) · [原始清单](../origin_resources/sources/beethoven-context/manifest.json) · [下载脚本](../origin_resources/sources/beethoven-context/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| Judith Ofcarcik: Multi-Strand Musical Narratives (MTO 2020) | [地址](https://www.mtosmt.org/issues/mto.20.26.2/mto.20.26.2.ofcarcik.html) | 未定位本地原件；旧状态：failed | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethoven-Haus: Beethoven and the Art of Fugue exhibition booklet | [地址](https://internet.beethoven.de/pdf-web/fuge_begleitheft_en_screen) | 未定位本地原件；旧状态：failed | 直链保存PDF；若失败从条目页重新进入 |
| Hepokoski: Formal Process, Sonata Theory, and Tempest (MTO 2010) | [地址](https://www.mtosmt.org/issues/mto.10.16.2/mto.10.16.2.hepokoski.html) | 未定位本地原件；旧状态：failed | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Boss: Schenkerian-Schoenbergian Analysis, Beethoven Op.10 No.1 (MTO 1999) | [地址](https://www.mtosmt.org/issues/mto.99.5.1/mto.99.5.1.boss.html) | 未定位本地原件；旧状态：failed | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Enrique Igoa: Functional Harmony, revised 2023 | [地址](https://www.enriqueigoa.com/articulos_y_libros/Functional_Harmony.pdf) | 未定位本地原件；旧状态：failed | 直链保存PDF；若失败从条目页重新进入 |
| Lockwood: Sources of Knowledge of Beethoven’s Compositional Procedures | [地址](https://www.bu.edu/beethovencenter/i-sources-of-knowledge-of-beethovens-compositional-procedures/) | [原件](../origin_resources/sources/beethoven-context/raw/lockwood-procedures.html)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Lockwood: Stages of Knowledge of Sources | [地址](https://www.bu.edu/beethovencenter/iii-stages-of-knowledge-of-sources/) | [原件](../origin_resources/sources/beethoven-context/raw/lockwood-stages.html)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Lockwood: Gustav Nottebohm | [地址](https://www.bu.edu/beethovencenter/v-gustav-nottebohm-1817-1882/) | [原件](../origin_resources/sources/beethoven-context/raw/lockwood-nottebohm.html)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Lewis Lockwood: Beethoven’s Sketches, the State of our Knowledge | [地址](https://www.bu.edu/beethovencenter/beethovens-sketches-the-state-of-our-knowledge/) | [原件](../origin_resources/sources/beethoven-context/raw/lockwood-sketches.html)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethoven-Haus: scholarly studies, editions and sketches | [地址](https://www.beethoven.de/en/studies) | [原件](../origin_resources/sources/beethoven-context/raw/haus-studies.html)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethoven-Haus Digital Archive: scope and source descriptions | [地址](https://www.beethoven.de/en/archive) | [原件](../origin_resources/sources/beethoven-context/raw/haus-archive.html)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethovens Werkstatt: research project and modules | [地址](https://beethovens-werkstatt.de/projekt/) | 未定位本地原件；旧状态：failed | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethovens Werkstatt: prototype editions | [地址](https://beethovens-werkstatt.de/prototypen/) | 未定位本地原件；旧状态：failed | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Henle: piano sonatas volume preface (1975/76) | [地址](https://www.henle.de/media/21/33/94/1697725799/9032-1697725799-sync.pdf) | [原件](../origin_resources/sources/beethoven-context/raw/henle-sonatas-commentary.pdf)；旧状态：cached | 直链保存PDF；若失败从条目页重新进入 |
| Henle: Op.2 sonatas preface | [地址](https://www.henle.de/media/68/08/f4/1697725903/0832-1697725903-sync.pdf) | [原件](../origin_resources/sources/beethoven-context/raw/henle-op2-preface.pdf)；旧状态：cached | 直链保存PDF；若失败从条目页重新进入 |

<a id="source-beethoven-analysis-keyboard"></a>

### 键盘／变奏／四重奏研究（beethoven-analysis-keyboard）

[来源说明](../origin_resources/sources/beethoven-analysis-keyboard/README.md) · [原始清单](../origin_resources/sources/beethoven-analysis-keyboard/manifest.json) · [下载脚本](../origin_resources/sources/beethoven-analysis-keyboard/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| The Performance of Beethoven’s ‘Diabelli Variations’: Continuity, Discontinuity, Cyclic Integration, Irony | [地址](https://storage.gmth.de/zgmth/pdf/1126) · [条目页](https://www.gmth.de/zeitschrift/artikel/1126.aspx) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/kinderman-diabellicycle-2021.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| Eine Diskursgeschichte der Diabelli-Variationen: Makroform und Interpretation im Spiegel analytischer Texte aus 200 Jahren | [地址](https://storage.gmth.de/zgmth/pdf/1125) · [条目页](https://www.gmth.de/zeitschrift/artikel/1125.aspx) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/linke-diabellicycle-macroform-2021.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| A Schenkerian Analysis of Beethoven’s E Minor Piano Sonata, Opus 90 | [地址](https://digital.library.unt.edu/ark:/67531/metadc28486/m2/1/high_res_d/thesis.pdf) · [条目页](https://digital.library.unt.edu/ark:/67531/metadc28486/) | 未定位本地原件；旧状态：failed | 直链保存PDF；若失败从条目页重新进入 |
| The Genesis of Beethoven’s Piano Sonata in A-flat, Op. 110 | [地址](https://dspace.library.uvic.ca/bitstreams/5933a35b-85da-4365-82f0-4d5ce81aefb8/download) · [条目页](https://dspace.library.uvic.ca/items/c5f2c910-e0f5-4b93-be32-7e23859f7195) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/matheson-1993-op110.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| Beethoven’s Instrumental Fugal Style: An Investigation of Tonal and Thematic Characteristics in the Late-Period Fugues | [地址](https://etheses.whiterose.ac.uk/id/eprint/1894/1/DX195498_1.pdf) · [条目页](https://etheses.whiterose.ac.uk/id/eprint/1894/) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/ormesher-late-fugues-1989.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| Towards a Personal Interpretation of Beethoven’s Piano Sonata in E Major, Op. 109 | [地址](https://researchspace.ukzn.ac.za/bitstreams/6b2a6e62-c10f-4bdc-8aec-5efab5b8b86b/download) · [条目页](https://researchspace.ukzn.ac.za/items/506b2d03-5af4-453a-94b7-5d95bf9ab47c) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/warburton-op109-2018.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| Ambiguity and Paradox in Beethoven’s Late Style | [地址](https://eprints.soton.ac.uk/id/eprint/462187/1/Text387632.pdf) · [条目页](https://eprints.soton.ac.uk/462187/) | 未定位本地原件；旧状态：failed | 直链保存PDF；若失败从条目页重新进入 |
| Harmony, voice leading, and motive in Beethoven's last quartet | [地址](https://scholarsbank.uoregon.edu/bitstreams/8e8ff90f-f404-4eb7-b78b-8d6403210c7a/download) · [条目页](https://scholarsbank.uoregon.edu/items/ea62cc8f-7cb1-4690-ac07-85a40cd8e9b3/full) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/britton-2008-op135.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| Beethoven’s Opus 18 String Quartets: Selected First Movements in Consideration of the Formal Theories of Heinrich Koch | [地址](https://digital.library.unt.edu/ark:/67531/metadc5427/m2/1/high_res_d/thesis.pdf) · [条目页](https://digital.library.unt.edu/ark:/67531/metadc5427/) | 未定位本地原件；旧状态：read_online_not_cached | 直链保存PDF；若失败从条目页重新进入 |
| Beethoven’s Sonatas Op. 31: Creative Process, Formal Structures and Performance | [地址](https://omp.cini.it/public/index.php/FGCOP/catalog/download/17/12/44-1?inline=1) · [条目页](https://omp.cini.it/public/index.php/FGCOP/catalog/book/17) | 未定位本地原件；旧状态：read_online_not_cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Models and Idea in Beethoven’s Late ‘Trifles’: A Stylistic Study of the Bagatelles, Op. 126 | [地址](https://etheses.dur.ac.uk/2759/1/2759.pdf) · [条目页](https://etheses.dur.ac.uk/2759/) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/leather-2005-op126.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| Tracing Beethoven Through the Ten Sonatas for Piano and Violin | [地址](https://drum.lib.umd.edu/bitstreams/4d17d5a6-4422-4c6a-8723-e714161ff473/download) · [条目页](https://drum.lib.umd.edu/items/8e7b782f-25a9-438c-9359-f6abc9259c9d/full) | 未定位本地原件；旧状态：read_online_not_cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The Autograph of Beethoven’s ‘Archduke’ Trio, Op. 97: A New Source | [地址](https://bf.press.uillinois.edu/pdfs/BF-VOL-11.2.pdf) · [条目页](https://katalog.beethoven.de/cgi-bin/biblio/kat_en.pl?reccheck=32656) | 未定位本地原件；旧状态：read_online_not_cached | 直链保存PDF；若失败从条目页重新进入 |
| Quartet No. 4 in C Minor, Op. 18 No. 4, first movement | [地址](https://www.mutopiaproject.org/ftp/BeethovenLv/O18/QuartetOpus18_No4_1/QuartetOpus18_No4_1-lys.zip) · [条目页](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=790) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/mutopia-op18no4)；旧状态：downloaded | 直链保存压缩包，核对类型与大小后解包 |
| Piano Sonata No. 1, Op. 2 No. 1, first movement | [地址](https://www.mutopiaproject.org/ftp/BeethovenLv/O2/LVB_Sonate_02no1_1/LVB_Sonate_02no1_1.ly) · [条目页](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1211) | [原件](../origin_resources/corpus/lilypond/BeethovenLv/O2/LVB_Sonate_02no1_1/LVB_Sonate_02no1_1.ly)；旧状态：available_in_project_corpus | 直链保存源码，并补齐同目录include |
| Perceiving Irony in Music: The Problem in Beethoven’s String Quartets | [地址](https://mtosmt.org/issues/mto.16.22.3/mto.16.22.3.bourne.html) | 未定位本地原件；旧状态：read_online_not_cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Teleology and Structural Determinants in Beethoven’s C♯ Minor Quartet, Op. 131 | [地址](https://symposium.music.org/30/articles/teleology-and-structural-determinants-in-beethovens-c-minor-quartet-op-131) | [原件](../origin_resources/sources/beethoven-analysis-keyboard/raw/barry-op131-teleology-1990.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

<a id="source-beethoven-analysis-chamber"></a>

### 室内乐研究与版本导言（beethoven-analysis-chamber）

[来源说明](../origin_resources/sources/beethoven-analysis-chamber/README.md) · [原始清单](../origin_resources/sources/beethoven-analysis-chamber/manifest.json) · [下载脚本](../origin_resources/sources/beethoven-analysis-chamber/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| barenreiter-cello-sonatas-preface.pdf | [地址](https://www.barenreiter.co.uk/prefaces/9790006524228_Innenansicht.pdf) | [原件](../origin_resources/sources/beethoven-analysis-chamber/raw/barenreiter-cello-sonatas-preface.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| bonds-op95-ucpress.html | [地址](https://online.ucpress.edu/jams/article/70/2/285/92328/Irony-and-Incomprehensibility-Beethoven-s-Serioso) | 未定位本地原件；旧状态：unavailable | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| cambridge-november-theatrical-quartets-excerpt.pdf | [地址](https://assets.cambridge.org/97811070/35454/excerpt/9781107035454_excerpt.pdf) | 未定位本地原件；旧状态：unavailable_after_two_web_timeouts | 直链保存PDF；若失败从条目页重新进入 |
| Mind-games: the structure of energy and the character of structure in Beethoven’s ‘Archduke’ Trio | [地址](https://www.bu.edu/beethovencenter/files/2024/04/Beethoven-Archduke-MT-2022-autumn.pdf) | [原件](../origin_resources/sources/beethoven-analysis-chamber/raw/barry-op97-formung-2022.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| Ludwig van Beethoven, Piano Trio in B-flat major, op. 97 (‘Archduke’) | [地址](https://blogs.loc.gov/music/files/2015/10/ATOS-Trio-FINAL-Program-10.15.15.pdf) | 未定位本地原件；旧状态：unavailable | 直链保存PDF；若失败从条目页重新进入 |
| The Second Finale of Beethoven’s String Quartet Opus 130: A Study of the Composing Score and Autograph Manuscript | [地址](https://open.bu.edu/server/api/core/bitstreams/43091386-c528-451d-869d-fa5c70824348/content) | [原件](../origin_resources/sources/beethoven-analysis-chamber/raw/bu-ross-op130-second-finale-2013.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| Spiral Time and the Paradigm of Persuasion: Recontextualising Beethoven’s String Quartet op.127 | [地址](https://www.bu.edu/beethovencenter/files/2017/06/Beethovens-E-flat-major-quartet-Op.-127-and-the-Paradigm-of-Persuasion-MT-2018-corrected-proofs.pdf) | 未定位本地原件；旧状态：read_online_not_cached | 直链保存PDF；若失败从条目页重新进入 |
| ‘A New Type of Part Writing’: Notation and Performance in Beethoven’s Late String Quartets | [地址](https://api.repository.cam.ac.uk/server/api/core/bitstreams/c409333e-edb0-455c-943b-10e730446708/content) | 未定位本地原件；旧状态：read_online_not_cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Das galante Modell als kreativer Raum: Die Introduktion zum ersten Satz von Ludwig van Beethovens Streichquartett Es-Dur op. 74 | [地址](https://www.gmth.de/zeitschrift/artikel/958.aspx) | [原件](../origin_resources/sources/beethoven-analysis-chamber/raw/raiser-op74-galant-introduction-2018.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Preface to Beethoven: Streichquartett B-dur op. 130 / Grande Fugue op. 133 | [地址](https://www.henle.de/media/17/99/f3/1697725875/9741-1697725875-sync.pdf) | [原件](../origin_resources/sources/beethoven-analysis-chamber/raw/henle-op130-op133-preface-cadenbach-2007.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |

<a id="source-beethoven-analysis-orchestral"></a>

### 交响／协奏／声乐研究（beethoven-analysis-orchestral）

[来源说明](../origin_resources/sources/beethoven-analysis-orchestral/README.md) · [原始清单](../origin_resources/sources/beethoven-analysis-orchestral/manifest.json) · [下载脚本](../origin_resources/sources/beethoven-analysis-orchestral/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| eastman-home.html | [地址](https://www.esm.rochester.edu/beethoven/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-home.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-inheritance.html | [地址](https://www.esm.rochester.edu/beethoven/orchestra-discussions/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-inheritance.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-transition.html | [地址](https://www.esm.rochester.edu/beethoven/transitional-composer-and-heroic-objective/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-transition.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-1.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-1/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-1.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-2.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-2/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-2.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-3.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-3/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-3.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-4.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-4/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-4.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-5.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-5/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-5.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-6.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-6/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-6.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-7.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-7/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-7.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-8.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-8/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-8.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| eastman-symphony-9.html | [地址](https://www.esm.rochester.edu/beethoven/symphony-no-9/) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/eastman-symphony-9.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| scalfaro-piano-concerto-3.pdf | [地址](https://cris.unibo.it/retrieve/e1dcb32f-9c54-7715-e053-1705fe0a6cc9/Musica%20Docta%20Beethoven.pdf) | 未定位本地原件；旧状态：unavailable | 直链保存PDF；若失败从条目页重新进入 |
| mtholyoke-missa-credo.pdf | [地址](https://ida.mtholyoke.edu/bitstream/10166/853/1/THESIS99.pdf) | 未定位本地原件；旧状态：unavailable | 直链保存PDF；若失败从条目页重新进入 |
| waikato-an-die-ferne-geliebte.pdf | [地址](https://researchcommons.waikato.ac.nz/bitstreams/fad3fc69-5a40-4c67-acf1-364550f4b6bd/download) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/waikato-an-die-ferne-geliebte.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| fiU-fidelio-leonore-analysis.pdf | [地址](https://digitalcommons.fiu.edu/record/20056/files/04._Hastings_Ten_Portraits_in_Sound_of_Beethoven_s_Leonore.pdf) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/fiU-fidelio-leonore-analysis.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| bu-beethoven-cadenzas.pdf | [地址](https://open.bu.edu/bitstreams/2a3d42d3-faec-4ae8-a1a4-9bb19c670e5c/download) | 未定位本地原件；旧状态：unavailable | 直链保存PDF；若失败从条目页重新进入 |
| met-fidelio-program.pdf | [地址](https://www.metopera.org/globalassets/season/2024-25/fidelio/programs/031525-fidelio.pdf) | 未定位本地原件；旧状态：unavailable | 直链保存PDF；若失败从条目页重新进入 |
| rakochi-triple-concerto-orchestra.pdf | [地址](https://dspace.ut.ee/bitstreams/5d57eb2b-c3fb-4b99-bb29-d642b13f37b5/download) | 未定位本地原件；旧状态：unavailable | 直链保存PDF；若失败从条目页重新进入 |
| beethovenhaus-pc5-sketch.html | [地址](https://www.beethoven.de/en/media/view/5653332433567744/Ludwig%2Bvan%2BBeethoven%2C%2BSkizzenblatt%2Bzum%2BKlavierkonzert%2BNr.%2B5%2Bop.%2B73%2C%2B1.%2BSatz%2C%2BAutograph?fromWork=5723434050912256) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/beethovenhaus-pc5-sketch.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| bso-piano-concerto-5.html | [地址](https://www.bso.org/works/piano-concerto-no-5-emperor) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/bso-piano-concerto-5.html)；旧状态：downloaded | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| berliner-piano-concerto-5.html | [地址](https://www.berliner-philharmoniker.de/en/programme-notes/ludwig-van-beethoven-concerto-for-piano-and-orchestra-in-e-flat-major-op-73/) | 未定位本地原件；旧状态：unavailable | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| turner-leonore-overtures.pdf | [地址](https://eprints.hud.ac.uk/id/eprint/34974/1/Final%20thesis%20-%20Turner%2C%20N.pdf) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/turner-leonore-overtures.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| lin-beethoven-lieder.pdf | [地址](https://digital.library.unt.edu/ark:/67531/metadc500227/m2/1/high_res_d/1002775233-Lin.pdf) | 未定位本地原件；旧状态：unavailable | 直链保存PDF；若失败从条目页重新进入 |
| lopez-symphony-9-performance.pdf | [地址](https://scholarship.miami.edu/view/pdfCoverPage?download=true&filePid=13419057900002976&instCode=01UOML_INST) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/lopez-symphony-9-performance.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |
| stanley-periodization-sample.pdf | [地址](https://assets.cambridge.org/97805215/80748/sample/9780521580748wsc00.pdf) | [原件](../origin_resources/sources/beethoven-analysis-orchestral/raw/stanley-periodization-sample.pdf)；旧状态：downloaded | 直链保存PDF；若失败从条目页重新进入 |

<a id="source-the-session"></a>

### The Session（排除项）（the-session）

[来源说明](../origin_resources/sources/the-session/README.md) · [原始清单](../origin_resources/sources/the-session/manifest.json) · [下载脚本](../origin_resources/sources/the-session/download.py)

| 文献／文件 | 来源链接 | 当前本地状态 | 下载方法 |
| --- | --- | --- | --- |
| LICENSE.md | [地址](https://raw.githubusercontent.com/adactio/TheSession-data/main/LICENSE.md) | [原件](../origin_resources/sources/the-session/raw/LICENSE.md)；旧状态：cached | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

## 5. 旧corpus谱库：逐曲与逐包来源

### Mutopia：1,841个作品／乐章条目

完整清单：[corpus/manifest-mutopia.json](../origin_resources/corpus/manifest-mutopia.json)；[官方FTP目录](https://www.mutopiaproject.org/ftp/)；[官方仓库](https://github.com/MutopiaProject/MutopiaProject)。

manifest中每个piece的url是作品目录；files.ly_all／ly／mid是该目录中的文件名，local字段给出本地路径。逐曲来源链接全部保留在此清单，不把数千个物理文件重复抄成数千个独立来源。重取时进入对应目录下载主.ly、同目录依赖及所需MIDI；现有fetch_mutopia.py --with-midi按作品目录采集。原始文件常有旧LilyPond版本，迁移只在工作副本中进行。

### ABC：63个原始包

完整清单：[corpus/manifest-abc.json](../origin_resources/corpus/manifest-abc.json)。以下来源URL逐包取自该清单；按X:拆分产生的文件继承原包来源。ABC是既有转写，不能冒称原生Kern；需要更完整记谱时回上游原生库。

| 原始包 | 原始下载地址 | 上游／下载方法 |
| --- | --- | --- |
| GasparOnline.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/GasparOnline.abc) | [Gaspar-Online-Edition/Gaspar-Online-Edition](https://github.com/Gaspar-Online-Edition/Gaspar-Online-Edition)；保存ABC原包；需要原生谱时查上游仓库 |
| beethoven_quartets.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/beethoven_quartets.abc) | [craigsapp/beethoven-string-quartets](https://github.com/craigsapp/beethoven-string-quartets)；保存ABC原包；需要原生谱时查上游仓库 |
| beethoven_sonatas.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/beethoven_sonatas.abc) | [craigsapp/beethoven-piano-sonatas](https://github.com/craigsapp/beethoven-piano-sonatas)；保存ABC原包；需要原生谱时查上游仓库 |
| chopin_1stEdition.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/chopin_1stEdition.abc) | [pl-wnifc/humdrum-chopin-first-editions](https://github.com/pl-wnifc/humdrum-chopin-first-editions)；保存ABC原包；需要原生谱时查上游仓库 |
| chopinmazurkas.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/chopinmazurkas.abc) | [craigsapp/chopin-mazurkas](https://github.com/craigsapp/chopin-mazurkas)；保存ABC原包；需要原生谱时查上游仓库 |
| chopinpreludes.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/chopinpreludes.abc) | [craigsapp/chopin-preludes](https://github.com/craigsapp/chopin-preludes)；保存ABC原包；需要原生谱时查上游仓库 |
| haydn_sonatas.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/haydn_sonatas.abc) | [craigsapp/haydn-keyboard-sonatas](https://github.com/craigsapp/haydn-keyboard-sonatas)；保存ABC原包；需要原生谱时查上游仓库 |
| joplin.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/joplin.abc) | [craigsapp/joplin](https://github.com/craigsapp/joplin)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-agricola.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/agricola.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-anon.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/anon.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-brumel.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/brumel.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-busnoys.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/busnoys.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-compe.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/compe.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-das.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/das.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-daser.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/daser.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-dufay.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/dufay.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-feacute.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/feacute.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-isaac.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/isaac.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-japart.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/japart.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-josquin.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/josquin.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-martini.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/martini.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-moutin.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/moutin.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-obrecht.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/obrecht.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-ockeghem.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/ockeghem.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-orto.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/orto.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-pipelar.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/pipelar.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-regis.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/regis.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-rue.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/rue.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jrp-tinctoris.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jrp/tinctoris.abc) | josquin.stanford.edu (Josquin Research Project)；保存ABC原包；需要原生谱时查上游仓库 |
| jsbachchorales.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/jsbachchorales.abc) | [craigsapp/bach-370-chorales](https://github.com/craigsapp/bach-370-chorales)；保存ABC原包；需要原生谱时查上游仓库 |
| mozart_sonatas.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/mozart_sonatas.abc) | [craigsapp/mozart-piano-sonatas](https://github.com/craigsapp/mozart-piano-sonatas)；保存ABC原包；需要原生谱时查上游仓库 |
| palestrina_a.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/palestrina_a.abc) | Humdrum/ELVIS 数据库；保存ABC原包；需要原生谱时查上游仓库 |
| pl-cz.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/pl-cz.abc) | Humdrum/ELVIS 数据库；保存ABC原包；需要原生谱时查上游仓库 |
| pl-kk.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/pl-kk.abc) | Humdrum/ELVIS 数据库；保存ABC原包；需要原生谱时查上游仓库 |
| pl-kozmzk.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/pl-kozmzk.abc) | Humdrum/ELVIS 数据库；保存ABC原包；需要原生谱时查上游仓库 |
| pl-sa.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/pl-sa.abc) | Humdrum/ELVIS 数据库；保存ABC原包；需要原生谱时查上游仓库 |
| pl-stab.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/pl-stab.abc) | Humdrum/ELVIS 数据库；保存ABC原包；需要原生谱时查上游仓库 |
| pl-wn.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/pl-wn.abc) | Humdrum/ELVIS 数据库；保存ABC原包；需要原生谱时查上游仓库 |
| pl-wtm.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/pl-wtm.abc) | Humdrum/ELVIS 数据库；保存ABC原包；需要原生谱时查上游仓库 |
| scarlatti_sonatas.abc | [ABC直链](http://ifdo.ca/~seymour/kern2abc/scarlatti_sonatas.abc) | [craigsapp/scarlatti-keyboard-sonatas](https://github.com/craigsapp/scarlatti-keyboard-sonatas)；保存ABC原包；需要原生谱时查上游仓库 |
| Ave_Maria_Arcadelt.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Ave_Maria_Arcadelt.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Ave_Maria_Gombert.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Ave_Maria_Gombert.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Ave_Maria_Palestrina.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Ave_Maria_Palestrina.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Ave_Regina_Coelorum.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Ave_Regina_Coelorum.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Ave_Verum.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Ave_Verum.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Bianco_Dolce_Cigno.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Bianco_Dolce_Cigno.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Coro_Della_Notte.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Coro_Della_Notte.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Gaudeamus_Igitur.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Gaudeamus_Igitur.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Halleluja_Erlebach.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Halleluja_Erlebach.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Magnificat.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Magnificat.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| O_Sacrum_Convivium.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/O_Sacrum_Convivium.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| O_Vos_Omnes.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/O_Vos_Omnes.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Otche_Nash.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Otche_Nash.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Pater_Noster.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Pater_Noster.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Selig_Sind_Die_Toten.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Selig_Sind_Die_Toten.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Son_questi.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Son_questi.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Tourdion.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Tourdion.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| Unendliche_Freude.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/Unendliche_Freude.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| choral.abc | [ABC直链](https://abcplus.sourceforge.net/Choral/choral.abc) | abcplus.sourceforge.net；保存ABC原包；需要原生谱时查上游仓库 |
| demo-dacapo.abc | [ABC直链](https://abcplus.sourceforge.net/demo-dacapo.abc) | abcplus.sourceforge.net；语法演示，不作真实作品谱例 |
| demo-guitarchords.abc | [ABC直链](https://abcplus.sourceforge.net/demo-guitarchords.abc) | abcplus.sourceforge.net；语法演示，不作真实作品谱例 |
| demo-itachords.abc | [ABC直链](https://abcplus.sourceforge.net/demo-itachords.abc) | abcplus.sourceforge.net；语法演示，不作真实作品谱例 |
| demo-percussions.abc | [ABC直链](https://abcplus.sourceforge.net/demo-percussions.abc) | abcplus.sourceforge.net；语法演示，不作真实作品谱例 |

## 6. 9批历史专题中的全部来源记录

这里补齐未归并进26个来源目录的资源线索。下表只转录书目／网址和可定位缓存，不转录旧Agent的音乐结论，也不承接旧“已读”标签。没有定位到原件只表示此记录不足以定位，不能据此宣称整本教材或全文已取得。

历史目录中另有22个HTML缓存文件。按条目ID可找到MTO Zeller论文、OMT2 Mediants单章、部分课程／节目说明；这不等于OMT2整书已取得。VSL四个具名缓存实际是相同的3,411字节应用壳，缺正文，不能当作已取得四篇乐器资料。

### 2026-10-21-jazz-pop-exchange

[原始专题目录](../origin_resources/collections/2026-10-21-jazz-pop-exchange/sources.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| Blues | [来源](https://www.loc.gov/collections/songs-of-america/articles-and-essays/musical-styles/popular-songs-of-the-day/blues/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Ragtime | [来源](https://www.loc.gov/collections/songs-of-america/articles-and-essays/musical-styles/popular-songs-of-the-day/ragtime/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Popular Songs of the Day | [来源](https://www.loc.gov/collections/songs-of-america/articles-and-essays/musical-styles/popular-songs-of-the-day/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The Popular Song: Old and New | [来源](https://www.loc.gov/collections/american-sheet-music-1870-to-1885/articles-and-essays/music-published-in-america-1870-1885/the-popular-song-old-and-new/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Acoustical Recording | [来源](https://www.loc.gov/collections/national-jukebox/articles-and-essays/acoustical-recording/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Registry by Induction Years: 2011, Ruth Etting | [来源](https://www.loc.gov/programs/national-recording-preservation-board/recording-registry/registry-by-induction-years/2011/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Jazz Singers | [来源](https://www.loc.gov/exhibits/jazz-singers/online-exhibition.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Hot Five and Hot Seven Recordings | [来源](https://www.loc.gov/static/programs/national-recording-preservation-board/documents/Hot-5-and-Hot-7-Recordings_Anderson.pdf) | 本条未定位原件；仅作线索 | 直链保存PDF；若失败从条目页重新进入 |
| Ko Ko | [来源](https://www.loc.gov/static/programs/national-recording-preservation-board/documents/ko-ko.pdf) | 本条未定位原件；仅作线索 | 直链保存PDF；若失败从条目页重新进入 |
| Jazz and Blues | [来源](https://www.si.edu/spotlight/african-american-music/jazz-blues) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Tell It Like It Is: A History of Rhythm and Blues | [来源](https://folklife.si.edu/magazine/freedom-sounds-tell-it-like-it-is-a-history-of-rhythm-and-blues) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Roots of Rock | [来源](https://rockhall.com/exhibitions/roots-of-rock/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Scott Joplin ABC collection | [来源](http://ifdo.ca/~seymour/kern2abc/) | [本地文件](../origin_resources/corpus/abc/_sources/humdrum-kern/joplin.abc) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

### chopin-corpus

[原始专题目录](../origin_resources/collections/chopin-corpus/catalog.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| Trois Nouvelles Etudes, No. 1 F Minor | [来源](https://www.mutopiaproject.org/ftp/ChopinFF/B130/TroisNouvellesEtudes_Chopin_n1/) | [本地文件](../origin_resources/corpus/lilypond/ChopinFF/B130/TroisNouvellesEtudes_Chopin_n1/TroisNouvellesEtudes_Chopin_n1.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

### early-classical

[原始专题目录](../origin_resources/collections/early-classical/catalog.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| Carl Philipp Emanuel Bach: The Complete Works | [来源](https://cpebach.org/description) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Bach Digital | [来源](https://www.bach-digital.de/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| GluckWV-online | [来源](https://www.gluck-gesamtausgabe.de/gwv.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| J. C. Bach: Operas and Dramatic Works | [来源](https://jcbach.org/preface) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| International Joseph Haydn Private Foundation catalogue and digitals | [来源](https://joseph-haydn.art/en/catalog-digitals) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| DCML: Carl Philipp Emanuel Bach, Works for Keyboard | [来源](https://github.com/DCMLab/cpe_bach_keyboard) | 本条未定位原件；仅作线索 | 仓库Code → Download ZIP，或固定commit归档 |
| DCML: Johann Christian Bach, Keyboard Sonatas | [来源](https://github.com/DCMLab/jc_bach_sonatas) | 本条未定位原件；仅作线索 | 仓库Code → Download ZIP，或固定commit归档 |
| Haydn piano sonatas | [来源](https://github.com/craigsapp/haydn-piano-sonatas) | 本条未定位原件；仅作线索 | 仓库Code → Download ZIP，或固定commit归档 |
| OpenScore String Quartets | [来源](https://github.com/OpenScore/StringQuartets) | 本条未定位原件；仅作线索 | 仓库Code → Download ZIP，或固定commit归档 |
| Normative Wit: Haydn's Recomposed Recapitulations | [来源](https://mtosmt.org/issues/mto.15.21.2/mto.15.21.2.mastic.php) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| String Quartets, Op. 33 | [来源](https://imslp.org/wiki/String_Quartets,_Op.33_%28Haydn,_Joseph%29) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Symphony No. 5 in C minor, Op. 67 (1808) | [来源](https://www.esm.rochester.edu/beethoven/symphony-no-5/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Symphony No. 3 in E-flat, Op. 55 "Eroica" (1804) | [来源](https://www.esm.rochester.edu/beethoven/symphony-no-3/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Formal Process, Sonata Theory, and the First Movement of Beethoven's "Tempest" Sonata | [来源](https://mtosmt.org/issues/mto.10.16.2/mto.10.16.2.hepokoski.php) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Baroque Concerto | [来源](https://ocw.mit.edu/courses/21m-011-introduction-to-western-music-fall-2024/pages/week-6-recitation-6a-listening-reading-goetjen/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The Classical Concerto First-Movement Cadenza: Origins, Growth, Facilitating Factors and the Eventual Decline | [来源](https://mtosmt.org/issues/mto.25.31.3/mto.25.31.3.maliniak.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Follow the Solo: The Formal Evolution of the Concerto in the Eighteenth-Century | [来源](https://doi.org/10.1093/mts/mtac009) | 本条未定位原件；仅作线索 | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| Symphony No. 5, Op. 67, first movement, piano reduction | [来源](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=497) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| La Primavera / Spring, Op. 8 No. 1, RV 269 | [来源](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=301) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Piano Concerto No. 23 in A major, K. 488 | [来源](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2229) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

### jazz-theory

[原始专题目录](../origin_resources/collections/jazz-theory/catalog.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| Blues Harmony | [来源](https://viva.pressbooks.pub/openmusictheory/chapter/blues-harmony/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Swing Rhythms | [来源](https://viva.pressbooks.pub/openmusictheory/chapter/swing-rhythms/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| AABA Form and Strophic Form | [来源](https://viva.pressbooks.pub/openmusictheory/chapter/aaba-and-strophic-form/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Transformations in Tonal Jazz: ii–V Space | [来源](https://mtosmt.org/issues/mto.17.23.1/mto.17.23.1.mcclimon.html) | [本地文件](../origin_resources/collections/jazz-theory/raw/mcclimon-2017-ii-v-space-f5e0615fd8e97111.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Guide-Tone Space: Navigating Voice-Leading Syntax in Tonal Jazz | [来源](https://mtosmt.org/issues/mto.19.25.2/mto.19.25.2.smither.html) | [本地文件](../origin_resources/collections/jazz-theory/raw/smither-2019-guide-tone-space-7de83ed3d933d645.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beyond Strophic: Prolonged Refrains, Choruses, and Bridges in the Blues, 1923-1966 | [来源](https://mtosmt.org/issues/mto.25.31.1/mto.25.31.1.carter.html) | [本地文件](../origin_resources/collections/jazz-theory/raw/carter-2025-beyond-strophic-fed87a54548fd8e6.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| A Platonic Model of Funky Rhythms | [来源](https://mtosmt.org/issues/mto.16.22.2/mto.16.22.2.cohn.php) | [本地文件](../origin_resources/collections/jazz-theory/raw/cohn-2016-funky-rhythms-1119934417edfd1e.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The Power of Anacrusis: Engendered Feeling in Groove-Based Musics | [来源](https://mtosmt.org/issues/mto.06.12.4/mto.06.12.4.butterfield.php) | [本地文件](../origin_resources/collections/jazz-theory/raw/butterfield-2006-anacrusis-925fd5fd6ae18339.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Referents in the Palimpsests of Jazz: Disentangling Theme from Improvisation in Recordings of Standard Jazz Tunes | [来源](https://mtosmt.org/issues/mto.24.30.3/mto.24.30.3.smither.html) | [本地文件](../origin_resources/collections/jazz-theory/raw/smither-2024-referents-37cd613f85f6fad8.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Form and Voice Leading in Early Beatles Songs | [来源](https://www.mtosmt.org/issues/mto.11.17.3/mto.11.17.3.nobile.html) | [本地文件](../origin_resources/collections/jazz-theory/raw/nobile-2011-beatles-form-896fedffc7b2d8ce.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Sentential Lyric-Types in the Great American Songbook | [来源](https://mtosmt.org/issues/mto.13.19.3/mto.13.19.3.callahan.html) | [本地文件](../origin_resources/collections/jazz-theory/raw/callahan-2013-songbook-eccb660de9096bae.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

### orchestration

[原始专题目录](../origin_resources/collections/orchestration/catalog.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| Violin | [来源](https://www.vsl.co.at/academy/strings/violin) | [缓存壳（无正文）](../origin_resources/collections/orchestration/raw/vsl-violin-technique-0ad7ea564bd58522.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Clarinet in Bb | [来源](https://www.vsl.co.at/academy/woodwinds/clarinet) | [缓存壳（无正文）](../origin_resources/collections/orchestration/raw/vsl-clarinet-register-0ad7ea564bd58522.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Viennese Horn | [来源](https://www.vsl.co.at/academy/brass/horn-f) | [缓存壳（无正文）](../origin_resources/collections/orchestration/raw/vsl-horn-notation-0ad7ea564bd58522.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Timpani | [来源](https://www.vsl.co.at/academy/percussion/timpani) | [缓存壳（无正文）](../origin_resources/collections/orchestration/raw/vsl-timpani-function-0ad7ea564bd58522.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Klangfarbenmelodie, Chromophony, and Timbral Function in Arnold Schoenberg’s “Farben” | [来源](https://mtosmt.org/issues/mto.23.29.3/mto.23.29.3.zeller.html) | [本地文件](../origin_resources/collections/orchestration/raw/zeller-2023-farben.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Deepen Your Orchestral Skills as a Film Composer | [来源](https://www.berklee.edu/berklee-now/news/deepen-your-orchestral-skills-as-a-film-composer) | [本地文件](../origin_resources/collections/orchestration/raw/berklee-virtual-orchestration-guide-d356b33fcee4e059.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

### pop-contemporary

[原始专题目录](../origin_resources/collections/pop-contemporary/catalog.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| The Functions of Continuous Processes in Contemporary Electronic Dance Music | [来源](https://mtosmt.org/issues/mto.21.27.2/mto.21.27.2.smith.html) | [本地文件](../origin_resources/collections/pop-contemporary/raw/smith-2021-continuous-edm-e5c1cc07614f99f3.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Codetta and Anthem Postchorus Types in Top-40 Pop from 2010 to 2015 | [来源](https://www.mtosmt.org/issues/mto.22.28.2/mto.22.28.2.stroud.html) | [本地文件](../origin_resources/collections/pop-contemporary/raw/stroud-2022-postchorus-8de2b66247c586ab.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Teleology in Verse–Prechorus–Chorus Form, 1965–2020 | [来源](https://mtosmt.org/issues/mto.22.28.3/mto.22.28.3.nobile.html) | [本地文件](../origin_resources/collections/pop-contemporary/raw/nobile-2022-teleology-8bd39cf06d0420e6.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Formal Functions of Drum Patterns in Post-Millennial Pop Songs, 2012–2021 | [来源](https://mtosmt.org/issues/mto.24.30.2/mto.24.30.2.geary.html) | [本地文件](../origin_resources/collections/pop-contemporary/raw/geary-2024-drum-form-b456dd257b4adbee.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

### previous

[原始专题目录](../origin_resources/collections/previous/catalog.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| Classical theme types | [来源](https://openmusictheory.github.io/classicalThemes.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The sentence | [来源](https://openmusictheory.github.io/sentence.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The period | [来源](https://openmusictheory.github.io/period.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Introduction to sonata theory | [来源](https://openmusictheory.github.io/SonataTheory-intro.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Sonata form: thematic modules | [来源](https://openmusictheory.github.io/sonataThematicModules.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Sonata form: the development | [来源](https://openmusictheory.github.io/sonataDevelopment.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Sonata form: the recapitulation | [来源](https://openmusictheory.github.io/sonataRecap.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Five-part rondo | [来源](https://openmusictheory.github.io/fivePartRondo.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Minuet form | [来源](https://openmusictheory.github.io/minuet.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Introduction to strict voice-leading | [来源](https://openmusictheory.github.io/speciesIntro.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Composing a cantus firmus | [来源](https://openmusictheory.github.io/cantusFirmus.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Composing a first-species counterpoint | [来源](https://openmusictheory.github.io/firstSpecies.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Composing a second-species counterpoint | [来源](https://openmusictheory.github.io/secondSpecies.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Composing a third-species counterpoint | [来源](https://openmusictheory.github.io/thirdSpecies.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Composing a fourth-species counterpoint | [来源](https://openmusictheory.github.io/fourthSpecies.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| High Baroque fugal exposition | [来源](https://viva.pressbooks.pub/openmusictheory/chapter/high-baroque-fugal-exposition/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Composing a fugue | [来源](https://open.lib.umn.edu/musiccomposition/chapter/composing-a-fugue/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Harmonic functions | [来源](https://openmusictheory.github.io/harmonicFunctions.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Classical cadence types | [来源](https://openmusictheory.github.io/cadenceTypes) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Harmonic syntax: prolongation | [来源](https://openmusictheory.github.io/harmonicSyntax2) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Modulation | [来源](https://openmusictheory.github.io/Modulation.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The ABC music standard 2.1 | [来源](https://abcnotation.com/wiki/abc%3Astandard%3Av2.1/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| LilyPond 2.26 Notation Reference | [来源](https://lilypond.org/doc/v2.26/Documentation/notation/index.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Ravel's Sound: Timbre and Orchestration in His Late Works | [来源](https://mtosmt.org/issues/mto.21.27.1/mto.21.27.1.beavers.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Harmony in the chamber music | [来源](https://www.cambridge.org/core/books/abs/cambridge-companion-to-ravel/harmony-in-the-chamber-music/9574ADD75877F749618ED9D9F5DD075F) | 本条未定位原件；仅作线索 | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| OpenScore Lieder Corpus | [来源](https://github.com/OpenScore/Lieder) | 本条未定位原件；仅作线索 | 仓库Code → Download ZIP，或固定commit归档 |
| Composing Canons | [来源](https://open.lib.umn.edu/musiccomposition/chapter/composing-canons/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Composing a Theme and Variations | [来源](https://open.lib.umn.edu/musiccomposition/chapter/composing-a-theme-and-variations/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Instruments: violin, viola, cello | [来源](https://philharmonia.co.uk/resources/instruments/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| OpusLoom verification and admission conventions | 无外部URL；内部规范记录 | 不作为外部学术资料 | 不下载 |
| LilyPond 2.26 snippets | [来源](https://lilypond.org/doc/v2.26/Documentation/snippets/index) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Updating files with convert-ly | [来源](https://lilypond.org/doc/v2.26/Documentation/usage/updating-files-with-convert_002dly) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Bach Digital works and source database | [来源](https://www.bach-digital.de/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Invention 1, BWV 772 | [来源](https://www.mutopiaproject.org/ftp/BachJS/BWV772/bach-invention-01/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Das Wohltemperierte Clavier I, Fuga I, BWV 846 | [来源](https://www.mutopiaproject.org/ftp/BachJS/BWV846/wtk1-fugue1/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Das Wohltemperierte Clavier I, Prelude I, BWV 846 | [来源](https://www.mutopiaproject.org/ftp/BachJS/BWV846/wtk1-prelude1/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Goldberg Variations, BWV 988 | [来源](https://www.mutopiaproject.org/ftp/BachJS/BWV988/bwv-988-aria/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Wolfgang Amadeus Mozart: Thematic Catalogue, Zweig MS 63 | [来源](https://searcharchives.bl.uk/catalog/040-001945812) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Piano Sonata in C major, K. 545, first movement | [来源](https://www.mutopiaproject.org/ftp/MozartWA/KV545/K545-1/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Piano Sonata in A major, K. 331, theme | [来源](https://www.mutopiaproject.org/ftp/MozartWA/KV331/KV331_1_1_tema/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Piano Sonata in A major, K. 331, Variation 1 | [来源](https://www.mutopiaproject.org/ftp/MozartWA/KV331/KV331_1_2_var1/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Piano Sonata in C minor, K. 457, first movement | [来源](https://www.mutopiaproject.org/ftp/MozartWA/KV457/sonata1/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| OpenScore String Quartets | [来源](https://github.com/OpenScore/StringQuartets) | 本条未定位原件；仅作线索 | 仓库Code → Download ZIP，或固定commit归档 |
| A Comparative Study of the Harmonic Equipment and Formal Features in the String Quartets by Claude Debussy and Maurice Ravel | [来源](https://digital.library.unt.edu/ark:/67531/metadc663181/m2/1/high_res_d/1002603893-Jenkins.pdf) | 本条未定位原件；仅作线索 | 直链保存PDF；若失败从条目页重新进入 |
| Therein Lies a Tale: Musical and Literary Structure in Ravel's Ma mere l'Oye | [来源](https://cpb-ap-se2.wpmucdn.com/blogs.unimelb.edu.au/dist/6/184/files/2016/09/34_Kilpatrick-246zr6w.pdf) | 本条未定位原件；仅作线索 | 直链保存PDF；若失败从条目页重新进入 |
| Sonata Form in Ravel's Pre-War Chamber Music | [来源](https://www.mtosmt.org/docs/diss-index.php?id=389) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Impressionism | [来源](https://musictheory.pugetsound.edu/mt21c/Impressionism.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Quatuor en fa majeur de Maurice Ravel | [来源](https://pad.philharmoniedeparis.fr/0763695-quatuor-en-fa-majeur-de-maurice-ravel.aspx?_lg=fr-FR) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Breaking the Frame: Arabesque and Metric Complexity in the Sunrise Scene from Ravel's Daphnis et Chloe | [来源](https://www.gmth.de/zeitschrift/artikel/270.aspx) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Orchestral Tissue, Subordinate Arabesques, and Turning Inward in Maurice Ravel's Bolero | [来源](https://mtosmt.org/issues/mto.20.26.2/mto.20.26.2.bhogal.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

### ravel-encoding

[原始专题目录](../origin_resources/collections/ravel-encoding/catalog.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| Ravel, String Quartet in F major, OpenScore 8482283 MusicXML | [来源](https://github.com/OpenScore/StringQuartets/blob/main/scores/Ravel%2C_Maurice/String_Quartet_in_F_major/sq8482283.mxl) | 本条未定位原件；仅作线索 | 条目内选Raw／Download raw file；多文件谱保留依赖 |

### romantic

[原始专题目录](../origin_resources/collections/romantic/catalog.json)

| 文献／资源 | 来源链接 | 当前本地依据 | 取得方法 |
| --- | --- | --- | --- |
| Erlkönig, D. 328 (Op. 1) | [来源](https://www.mutopiaproject.org/ftp/SchubertF/D328/Erlkoenig/) | [本地文件](../origin_resources/corpus/lilypond/SchubertF/D328/Erlkoenig/Erlkoenig.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Kinderscenen: Träumerei, Op. 15 No. 7 | [来源](https://www.mutopiaproject.org/ftp/SchumannR/O15/SchumannOp15No07/) | [本地文件](../origin_resources/corpus/lilypond/SchumannR/O15/SchumannOp15No07/SchumannOp15No07.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Prelude, Op. 28 No. 4 | [来源](https://www.mutopiaproject.org/ftp/ChopinFF/O28/Chop-28-4/) | [本地文件](../origin_resources/corpus/lilypond/ChopinFF/O28/Chop-28-4/Chop-28-4.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Intermezzo, Op. 118 No. 2 | [来源](https://www.mutopiaproject.org/ftp/BrahmsJ/O118/intermezzo/) | [本地文件](../origin_resources/corpus/lilypond/BrahmsJ/O118/intermezzo/intermezzo.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| A Riddle in Chopin's Preludes, Op. 28 | [来源](https://online.ucpress.edu/ncm/article/46/3/197/196353/A-Riddle-in-Chopin-s-Preludes-Op-28) | 本条未定位原件；仅作线索 | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| Erlkönig: Goethe, Schubert, and Resurrecting the Son | [来源](https://symposium.music.org/61-1/articles/i-erlkoenig-i-goethe-schubert-and-resurrecting-the-son) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Week 9: Recitation 9A Listening and Reading | [来源](https://ocw.mit.edu/courses/21m-011-introduction-to-western-music-fall-2024/pages/week-9-recitation-9a-listening-reading-goetjen/) | [本地文件](../origin_resources/collections/romantic/raw/mit-ocw-erlkonig-2024-3e757f8ac0744123.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Piano Pieces, Op. 118, Nos. 1, 2, and 5; Intermezzo, Op. 117, No. 2 | [来源](https://www.laphil.com/works/piano-pieces-op-118-nos-1-2-and-5-intermezzo-op-117-no-2) | [本地文件](../origin_resources/collections/romantic/raw/laphil-brahms-op118-2c35b8ab7c0d672f.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Analysing musical performance through functional data analysis: rhythmic structure in Schumann's Träumerei | [来源](https://www.tandfonline.com/doi/full/10.1080/09540090902733848) | 本条未定位原件；仅作线索 | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| Open Music Theory 2e: Mediants | [来源](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_%28Gotham_et_al.%29/05%3A_Chromaticism/5.15%3A_Mediants) | [本地文件](../origin_resources/collections/romantic/raw/omt-2e-mediants-4fa7a536eed738fc.html) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Etude in A minor, Op. 10 No. 2 | [来源](https://www.mutopiaproject.org/ftp/ChopinFF/O10/10-02-i/) | [本地文件](../origin_resources/corpus/lilypond/ChopinFF/O10/10-02-i/10-02-i.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Etude in C minor, Op. 10 No. 12 | [来源](https://www.mutopiaproject.org/ftp/ChopinFF/O10/op-10-12-wfi/) | [本地文件](../origin_resources/corpus/lilypond/ChopinFF/O10/op-10-12-wfi/op-10-12-wfi.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Etude in A-flat major, Op. 25 No. 1 | [来源](https://www.mutopiaproject.org/ftp/ChopinFF/O25/chopin-op-25-01/) | [本地文件](../origin_resources/corpus/lilypond/ChopinFF/O25/chopin-op-25-01/chopin-op-25-01.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Trois Nouvelles Etudes No. 1 in F minor, B. 130 | [来源](https://www.mutopiaproject.org/ftp/ChopinFF/B130/TroisNouvellesEtudes_Chopin_n1/) | [本地文件](../origin_resources/corpus/lilypond/ChopinFF/B130/TroisNouvellesEtudes_Chopin_n1/TroisNouvellesEtudes_Chopin_n1.ly) | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Etudes, Op. 10, Nos. 1, 2, 3, 4, 12 and Etudes, Op. 25, Nos. 5, 6, 11 | [来源](https://www.laphil.com/works/etudes-op-10-nos-1-2-3-4-12-and-etudes-op-25-nos-5-6-11) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Tenuto Ties and Slurs in Chopin's Etudes | [来源](https://musicperformanceresearch.org/tenuto-ties-and-slurs-in-chopins-etudes/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Claude Debussy, Contrapuntiste Malgre Lui | [来源](https://symposium.music.org/17/articles/claude-debussy-i-contrapuntiste-malgre-lui) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Claude Debussy, La Mer | [来源](https://www.berliner-philharmoniker.de/en/programme-notes/claude-debussy-la-mer/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Enquete autour du Prelude a l'apres-midi d'un faune de Debussy | [来源](https://www.conservatoiredeparis.fr/fr/enquete-autour-du-prelude-lapres-midi-dun-faune-de-debussy) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Igor Stravinsky, Le Sacre du printemps | [来源](https://www.berliner-philharmoniker.de/en/programme-notes/igor-stravinsky-le-sacre-du-printemps-ballet/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Bela Bartok, Music for Strings, Percussion, and Celesta | [来源](https://www.laphil.com/works/music-for-strings-percussion-and-celesta) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Olivier Messiaen, Quartet for the End of Time | [来源](https://www.laphil.com/works/quartet-for-the-end-of-time) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Review of Anthony Pople, Messiaen: Quatuor pour la fin du Temps | [来源](https://mtosmt.org/issues/mto.99.5.2/mto.99.5.2.luchese.html) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Pitch-Class Sets, Normal Order, and Transformations | [来源](https://viva.pressbooks.pub/openmusictheory/chapter/pc-sets-normal-order-and-transformations/) | 本条未定位原件；仅作线索 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

## 7. 贝多芬专题记录中的其他来源／落地页

以下为专题JSON中补充登记、尚未在前表按相同URL列出的地址，包含条目页与旧线上线索；不是新增下载成果。个别www／非www形式可能指向同一资源。

| 文献／条目 | 地址 | 本地依据／记录位置 | 取得方法 |
| --- | --- | --- | --- |
| Multi-Strand Musical Narratives: An Introduction | [来源](https://mtosmt.org/issues/mto.20.26.2/mto.20.26.2.ofcarcik.html) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| “Transforming Chaos”: Modes of Ambiguity in Tchaikovsky’s Symphony No. 5 in E Minor | [来源](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=ucin1187004301&disposition=inline) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Piano Concerto No. 1 in C, Opus 15 | [来源](https://www.bso.org/works/beethoven-piano-concerto-no-1) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Lyric as Self-reflection: The Role of the Slow Movement in Beethoven’s Works | [来源](https://etheses.dur.ac.uk/3613/1/THESIS.pdf) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 直链保存PDF；若失败从条目页重新进入 |
| A Movement by Movement Analysis of the Missa Solemnis | [来源](https://www.cco.caltech.edu/~tan/BeethovenMissaSolemnis/analysis_of_missa_solemnis.html) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| The Annotated Beethoven Corpus: String Quartet Op. 59 No. 3, first movement (n09op59-3_01) | [来源](https://github.com/DCMLab/ABC) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 仓库Code → Download ZIP，或固定commit归档 |
| Beethoven: Missa Solemnis, Chapter 3 “Preliminaries to the analysis” | [来源](https://www.cambridge.org/core/books/beethoven-missa-solemnis/preliminaries-to-the-analysis/42BE39163891F7BC072EE68A8DDF9F7F) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| An Approach to Ambiguity in the Opening of Beethoven’s ‘String Quartet’, Op. 59 no. 3, I | [来源](https://www.jstor.org/stable/24044576) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| Suspended Time: The Fugue on “et vitam venturi saeculi” in the Credo of the Missa solemnis | [来源](https://www.tandfonline.com/doi/full/10.1080/01411896.2013.791805) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| Mass C major op. 86, HN 9548 | [来源](https://www.henle.de/en/Mass-C-major-op.-86/HN-9548) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Switching Colors on Beethoven’s Broadwood Fortepiano: Variation 4 of the Piano Sonata, Opus 111 | [来源](https://storage.gmth.de/proceedings/articles/28/pdf/gmth-proceedings-artikel-28.pdf) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 直链保存PDF；若失败从条目页重新进入 |
| Practical performance considerations for the Andante con moto of Beethoven’s Piano Concerto in G Major, Op. 58 | [来源](https://repository.lsu.edu/gradschool_dissertations/1348/) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethoven’s Late Style in His Last Five Piano Sonatas | [来源](https://etd.ohiolink.edu/acprod/odb_etd/r/etd/search/10?clear=10&p10_accession_num=ucin1243014360) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Piano Concerto No. 2 | [来源](https://www.laphil.com/works/piano-concerto-no-2-beethoven) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethoven Op.10 No.1, I, Mutopia 778 | [来源](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=778) | [原件](../origin_resources/corpus/lilypond/BeethovenLv/O10/LVB_Sonate_10no1_1/LVB_Sonate_10no1_1.ly)；[来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Form und Dramaturgie in Beethovens Violinkonzert | [来源](https://www.gmth.de/zeitschrift/artikel/898.aspx) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethoven: Violin Concerto, Chapter 5, ‘Structure and style I – 1. Allegro ma non troppo’ | [来源](https://www.cambridge.org/core/books/beethoven-violin-concerto/structure-and-style-i-1-allegro-ma-non-troppo/4E0813A56F26C3792868CC4723999FA4) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 进入出版／文献条目，取可访问全文或PDF；摘要须单列 |
| ‘A New Type of Part Writing’: Notation and Performance in Beethoven’s Late String Quartets | [来源](https://www.repository.cam.ac.uk/items/1ff78915-a0ae-4130-bdf1-bc7e6b10ee71) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Beethoven’s Triple Concerto | [来源](https://ton.bard.edu/beethovens-triple-concerto/) | [来源记录](../origin_resources/beethoven-project/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Symphony No. 5 in C minor, Op. 67 | [来源](https://www.beethoven.de/de/media/view/6484893366222848/scan/59) | [来源记录](../origin_resources/beethoven-project/repertoire/inventory.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |
| Seven Variations on God Save the King, WoO 78 | [来源](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1024) | [来源记录](../origin_resources/beethoven-project/integration/prepared/knowledge/sources.json)；未另外声称已缓存全文 | 打开具体条目，下载实际PDF或保存正文HTML及所需图表 |

## 8. 新资料入库、谱例交付与正文边界

预备轮使用初整角色，正式轮不再设置初整代理；资料助手亲自完成取得与初整。先查原始库和阅读库，避免重复取得。新原件保留下载URL、取得时间、实际文件、格式／页段、哈希和许可原文；正式轮资料助手亲自完成初步整理并更新共同入口，新资料与预备轮资料同等可用。PDF／图像使用已选定EverythingMarkdown；原谱OCR不等于可靠音符编码。

没有现成LilyPond或许可信息尚不齐时，仍如实记录来源与缺口，不能用自编谱例替代真实作品。资料助手负责实际交付谱例的正确性与符合要求；找不到就如实报告，音乐学者无需验谱，可使用真实定位的占位符。下载、校验与转换都不能替代学者阅读和理解文献。

原件、加工资料、来源／许可及下载过程先登记在local。正式轮对外层music-wiki仓库的改动只限content，根NOTICE的公共登记同步另行安排；资料来源表、许可和生产记录不塞进音乐正文。

本页只补全来源与取得方法，没有重新采集资料或启动正式知识库写作。
