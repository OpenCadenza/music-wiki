# 团队接手：音乐学者子代理方案开发分支

状态：2026-11-07迁移与交接准备；资料预备已完成，尚未启动第一批正式写作。

## 1. 取得正确的代码与资料包

由维护者先推送 `音乐学者子代理方案-开发分支`。接手成员在自己机器上克隆该分支；以下命令可在 Git 终端执行：

```powershell
git clone --branch 音乐学者子代理方案-开发分支 https://github.com/OpenCadenza/music-wiki.git
cd music-wiki
```

已有克隆则先处理自己的未提交改动，再 fetch 并切换这个分支。一个仓库同时维护多个方案时，使用独立工作目录，不覆盖其他分支的研究资料。

向维护者取得 `music-wiki-resources-2026-11-07.zip`。文件名、字节数、SHA-256、目录数量和基线提交见[资料包.json](资料包.json)。压缩包使用 ZIP64；推荐下面的 Python 脚本处理，不依赖各平台解压软件对长路径和大ZIP的支持。

## 2. 校验并解压，然后接手工作

需要 Python 3.10+，此步骤只用标准库。在仓库根目录运行：

```powershell
python local/workbench/tools/handoff_bundle.py restore --archive "D:/收到的资料/music-wiki-resources-2026-11-07.zip"
```

把路径换成自己的资料包位置。脚本校验整包及内置清单的 SHA-256，检查全部目标路径和已有文件冲突，然后恢复缺失资料。相同文件跳过，不同文件停止；请先处理真实冲突，不能用覆盖解压掩盖团队改动。成功结果应为19,973个已验证文件；首次在干净克隆中，35份已由Git提供的入口／索引会被识别为相同文件，其他资料解压到本机。

解压目标是**仓库根目录**，最终必须是：

```text
music-wiki/
├── .git/                         唯一Git仓库
├── content/
└── local/
    ├── docs/
    ├── workbench/tools/
    ├── origin_resources/         12,945文件，原始资料
    └── resources/                7,028文件，阅读资料与索引
```

需要约4.34GB空间保存解压资料，另需存放收到的压缩包。请预留合计至少9GB可用空间。不要得到 `local/local/resources`，不要在local里建立第二个Git仓库。原始资料是研究输入，不会成为网站公开内容。

只检查压缩包完整性而不解压，可运行：

```powershell
python local/workbench/tools/handoff_bundle.py verify --archive "D:/收到的资料/music-wiki-resources-2026-11-07.zip"
```

成功解压后运行 `git status --short`，资料正文和原件应继续忽略，入口和索引不应因解压发生变化。打开[资料总入口](../../resources/README.md)，确认实际文献、OCR图像和谱源可读。

## 3. 主控必读与工作阶段

按顺序阅读[文档入口](../README.md)、[写作偏好](../偏好-知识库写作.md)、[子代理工作流](../子代理工作流.md)、[纠偏重建计划](../纠偏重建计划.md)、[看板说明](../公共看板/README.md)、[预备轮验收](../实施记录/2026-10-28-预备轮/预备轮验收.md)，并读[原始用户提示词](../上一轮用户提示词.md)理解历史要求。以最新明确要求及本分支现行文档为准。

资料助手按需查[来源与下载方法](../sources.md)。音乐学者必须进一步实际阅读资料，不以入口、资料卡、助手概述或旧AI文章替代阅读。

本次交接不自动授权首批写作。由用户明确启动后，音乐学者gpt-6.1-terra / high自由选题，资料助手gpt-6-luna / medium查找并整理资料、负责谱例正确性与要求；找不到如实报告，学者可留占位且无需验谱。第一批约20篇，整批结束由gpt-6.1-terra / medium复读。原生消息协作，看板记录实际研究状态。正式轮没有初整代理。

## 4. 一个仓库的版本与发布边界

- `local/` 是主仓库的普通目录。每篇成稿后归档对应看板记录，由主控在根目录串行提交 `content/` 和 `local/` 的全部非忽略改动；不并发操作Git index，不自动推送。
- 正式轮允许维护正文与本地研究区；其余站点代码、配置、CI、根NOTICE和根README仍不在写作改动范围。此次迁移更新README和忽略规则是独立准备任务。
- `local/README.md` 的“请勿合并到main分支”适用于整个研究目录。本开发分支不整体合入main。发布时单独选取审核后的正文改动，根NOTICE等公共登记另行处理。
- 旧local历史以subtree合入，不能再对local单独init、commit或push。历史文档中旧的双仓库说明只解释旧阶段，不覆盖当前规则。
- `local/origin_resources/`及阅读正文继续忽略；`local/resources/README.md`与`local/resources/catalog/`纳入Git。分支推送不携带大型资料，更新资料包时同步更新资料包描述；旧包与新描述不匹配应停止。

## 5. 工具和已知缺口

现有阅读材料无需重新OCR。Python脚本可直接完成资料包恢复；构建站点时再依根README、package.json及pnpm锁文件配置工具链和LilyPond。

预备轮OCR、导入验收和团队文档回写脚本保存的是原机器流程，其中有EverythingMarkdown、Poppler、Python依赖和旧源路径等机器配置。接手后不要盲目重跑。需要新OCR时，安装并按EverythingMarkdown原工具说明配置本机环境与服务凭据，调整工具路径后使用；凭据和云端上传授权不会随资料包转移。本包没有运行缓存和服务密钥。

旧 `local/materials/`、`local/archive/` 和OCR运行日志不在本资料包中。新研究应使用原始库和阅读库，旧AI正文不能当作学术输入。原机器仍保留旧归档，历史旧正文与NOTICE也可从资料包描述中的main基线提交查看；若要处理完整旧发布产物归档，请单独向维护者取得，不要冒称本包包含它。

原有资料缺口仍见预备轮验收：OMT2完整导出、部分HTML图像等尚未补齐；op98手稿封面仅原图可读。资料齐备与学者已读是两件事。机器绝对路径保留在部分历史收据中用于追溯，当前资料位置以仓库内相对路径为准。

## 6. 维护者同步分支

本次由维护者自行推送，命令在本分支工作目录执行：

```powershell
git push -u origin 音乐学者子代理方案-开发分支
```

将资料包单独发送给有权访问资料的团队成员，同时指向本分支此版本的资料包描述。GitHub只同步文档、研究记录、工具、轻量索引和正文。

当前一份版本化压缩包适合首次交接。后续多人频繁新增资料时，可以把资料包放到团队共享存储，固定文件名版本与SHA-256并提供稳定下载链接；仅同步新增资料或定期出新包。资料库再持续增长时再考虑DVC／对象存储，不必现在把4.34GB资料及每次变动都放进普通Git历史。


已核对的GitHub限制：普通Git拒绝大于100MiB的文件（[官方说明](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)）；Release每个附件必须小于2GiB（[官方说明](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)）。本包约3.85GB，不提交Git，也不能作为单个Release附件上传。当前直接发送或共享存储即可；确需Release时先分卷并提供重组与校验说明。
