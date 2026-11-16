# 新增开发分支部署

站点是「一个仓库、一次部署、多个分支页面」。主站和每个开发分支的预览在**同一次部署**中发布，
所以任何一次部署都会同时刷新所有页面。

| 页面 | 地址 | 构建来源 |
| --- | --- | --- |
| 主站 | `/music-wiki/` | `main` 的代码 + `main` 的 `content/` |
| 开发预览 | `/music-wiki/dev/<slug>/` | `main` 的代码 + 该分支的 `content/` |

「代码」指 `.vitepress/`、`scripts/`、`package.json`、`toolchains.json` 等构建相关文件。开发分支
只提供 `content/`，主题和工具链统一取自 `main`，预览不会和主站跑偏。

本文档不属于站点正文（站点只发布 `content/`），位于仓库 `docs/` 目录。

## 改动分布总览

| 要做的事 | 在哪改 | 为什么 |
| --- | --- | --- |
| 把分支加进顶栏下拉框 | **main** 的 `branches.json` | 下拉框和部署矩阵读同一份清单 |
| 允许推送该分支时自动部署 | **main** 的 `.github/workflows/deploy.yml` 的 `on.push.branches` | 触发列表是静态的；不加也能手动运行 |
| 允许该分支部署到 Pages | **仓库设置**里的 `github-pages` 环境 | 环境默认只放行 `main`，否则 deploy 作业起不来 |
| 同步构建配置 | **新分支** 的 `.github/workflows/` 两个文件 | `push` 事件执行的是被推分支里那份 workflow |
| 写内容 | **新分支** 的 `content/` | 预览构建时替换主站的 `content/` |

## 一、在 main 上做的两件事

### 1. 登记分支（同时完成「加进下拉框」）

编辑仓库根目录的 `branches.json`，追加一条：

```json
{
  "label": "agent开发分支2",
  "branch": "feature/foo",
  "slug": "feature-foo"
}
```

| 字段 | 含义 | 约束 |
| --- | --- | --- |
| `label` | 下拉框里显示的名字 | 必填，可中文 |
| `branch` | 真实分支名 | 必填，可以带 `/` |
| `slug` | 网址路径段：`/music-wiki/dev/<slug>/` | 小写字母、数字、连字符；不能重复；`main` 条目留空 |

顶栏下拉框按清单顺序渲染，当前所在分支会自动选中；改 `label` 就是改下拉框文字。主站条目
（`slug` 为空）必须保留一条。

### 2. 打开推送触发

在 `.github/workflows/deploy.yml` 的 `on.push.branches` 里加上分支名：

```yaml
    branches:
      - main
      - dsh-c6ded6ed-82bb
      - feature/foo
```

不加这一条，分支推送不会自动触发；你仍可以在 Actions 页面手动 Run workflow（手动运行会构建
清单里的所有分支）。

改完提交并推送 `main`。这一步不会立刻产生新页面，因为新分支还没有同版 workflow。

## 二、在新分支上做的事

### 3. 同步两个 workflow 文件

`push` 事件执行的是**被推分支自己的** `.github/workflows/deploy.yml`。如果新分支还是旧版，
即使 `main` 里已登记，推送也不会按新逻辑运行。在分支上执行：

```bash
git checkout main -- .github/workflows/deploy.yml .github/workflows/build-site.yml
```

提交这条改动。分支不需要复制 `branches.json`：部署流程会固定从 `main` 读取清单。

### 4. 在分支里只写 content

预览只取该分支的 `content/`，其余目录（`.vitepress/`、`scripts/`、`package.json` 等）即使改了
也不会体现。需要新主题、新脚本时，先合进 `main`，预览会随之下次部署生效。

## 三、仓库设置（一次性）

`github-pages` 环境有部署分支策略，默认只允许 `main`。新增分支如果不放行，会出现
**build 成功、deploy 作业 0 步直接失败**。维护者在仓库 Settings → Environments →
`github-pages` → Deployment branches 里添加，或用一条命令：

```bash
gh api -X POST /repos/OpenCadenza/music-wiki/environments/github-pages/deployment-branch-policies \
  -f name=feature/foo -f type=branch
```

查看当前放行列表：

```bash
gh api /repos/OpenCadenza/music-wiki/environments/github-pages/deployment-branch-policies \
  --jq '.branch_policies[].name'
```

## 四、验证

```bash
gh run list --branch feature/foo --limit 3      # 是否触发
gh run view <run-id>                            # 三个作业：Read branches.json / Build ... / Publish
```

成功后的检查点：

1. `/music-wiki/dev/feature-foo/` 可访问，标题带「（开发预览）」，页面带 `noindex`；
2. 页面里的链接、谱例资源都在 `/music-wiki/dev/feature-foo/` 前缀下；
3. 顶栏下拉框多出「agent开发分支2」，并且当前页正确选中它；
4. 主站 `/music-wiki/` 仍然正常，下拉框仍选中「主分支」。

常见问题：

| 现象 | 原因 |
| --- | --- |
| 推送后完全没有运行 | 分支里没有新版 workflow 文件，或 `on.push.branches` 没加分支 |
| build 全部成功，deploy 0 步失败 | 环境的部署分支策略没放行该分支 |
| 页面 404 | `slug` 写错，或 `branches.json` 不在 `main` 的最新提交里 |
| 下拉框没有新条目 | 只改了分支，没有改 `main` 的 `branches.json` |
| 预览内容没变化 | 分支变了但这次部署没有重建它；检查 `gh run` 里该分支作业是否走了缓存（缓存命中说明内容哈希未变） |

## 五、约束与维护

- 每次部署是整站发布：主站和所有开发预览一起更新，不会出现「只更新一个页面」。
- 未改动的分支复用上次构建产物（按内容哈希缓存），不会被重新构建。
- 单个开发分支构建失败不会阻塞主站；该分支的预览保持上次成功的内容，部署摘要里会有告警。
- 开发分支不要合并进 `main` 来发布；满足发布标准后，由维护者挑选通过的 `content/` 改动。
- 删除分支时，同时删掉 `branches.json` 里的条目；预览页会在下一次部署后消失。
- 分支数量没有硬上限，但每个分支占一个构建作业；同时保留太多分支会拉长每次部署时间。

## 六、完整示例

把 `feature/foo` 发布为「agent开发分支2」，地址 `/music-wiki/dev/feature-foo/`：

```bash
# 1. main：登记清单与触发列表
git switch main
# 编辑 branches.json，追加 {"label":"agent开发分支2","branch":"feature/foo","slug":"feature-foo"}
# 编辑 .github/workflows/deploy.yml，在 on.push.branches 里加 feature/foo
git commit -am "Publish feature/foo as a development preview"
git push origin main

# 2. 放行环境（维护者）
gh api -X POST /repos/OpenCadenza/music-wiki/environments/github-pages/deployment-branch-policies \
  -f name=feature/foo -f type=branch

# 3. 新分支：同步 workflow 后再写内容
git switch feature/foo
git checkout main -- .github/workflows/deploy.yml .github/workflows/build-site.yml
git commit -m "ci: sync deployment workflows"
git push origin feature/foo
```
