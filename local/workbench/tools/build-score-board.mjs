import { existsSync, readdirSync, readFileSync, writeFileSync, statSync } from 'node:fs'
import { join, relative } from 'node:path'

const root = process.argv[2] || process.cwd()
const contentRoot = join(root, 'content')
const out = join(root, 'local', 'resources', 'catalog', 'score-board.md')

function walk(dir) {
  const acc = []
  for (const name of readdirSync(dir)) {
    const p = join(dir, name)
    const st = statSync(p)
    if (st.isDirectory()) acc.push(...walk(p))
    else if (name.endsWith('.md')) acc.push(p)
  }
  return acc
}

const rows = []
const refs = new Map()
const files = walk(contentRoot)

for (const file of files) {
  const text = readFileSync(file, 'utf8')
  const rel = relative(contentRoot, file).replaceAll('\\', '/')
  for (const m of text.matchAll(/```lilypond([^\n]*)\n/g)) {
    const attrs = m[1]
    const id = /id="([^"]*)"/.exec(attrs)?.[1]
    if (!id) continue
    const title = /title="([^"]*)"/.exec(attrs)?.[1] ?? ''
    const location = /location="([^"]*)"/.exec(attrs)?.[1] ?? ''
    rows.push({ id, title, location, rel })
  }
  for (const m of text.matchAll(/#score-([a-z0-9.-]+)/g)) {
    const list = refs.get(m[1]) || []
    if (!list.includes(rel)) list.push(rel)
    refs.set(m[1], list)
  }
}

rows.sort((a, b) => a.id.localeCompare(b.id))

const lines = [
  '# 谱例公共看板（自动生成）',
  '',
  '> 谱例助手出谱前先读本表：id 命中的谱例不再重复出谱，直接把占位替换成 `文章#score-<id>` 链接。',
  '> 本表由 `node local/workbench/tools/build-score-board.mjs` 从 `content/` 生成，勿手改。',
  '',
  '| 谱例 id | 作品 | 定位 | 所在文章 | 直达链接 | 被引用文章 |',
  '| --- | --- | --- | --- | --- | --- |'
]

for (const r of rows) {
  const link = `${r.rel}#score-${r.id}`
  const used = (refs.get(r.id) || []).join('<br>')
  lines.push(`| \`${r.id}\` | ${r.title} | ${r.location} | ${r.rel} | \`${link}\` | ${used} |`)
}

lines.push('')

// manual:gaps 由人维护：优先沿用现有看板里的缺口块，没有才回退到初始模板。
const GAP_START = '<!-- manual:gaps -->'
const GAP_END = '<!-- /manual:gaps -->'
const fallbackGapBlock = [
  GAP_START,
  '## 缺口（手工维护）',
  '',
  '| 作品 | 需要的片段 | 状态 |',
  '| --- | --- | --- |',
  '| 贝多芬 Op.97 第一乐章 | mm.1–12 | 暂无可靠谱源 |',
  '| 雷哈 Op.88 No.2 第一乐章 | mm.1–8 | 暂无可靠谱源 |',
  '| 马勒 第四交响曲 第二乐章 | mm.34–46 | 暂无可靠谱源 |',
  '| 那不勒斯和弦教材模型 | 示意 | 作者决定是否保留 |',
  GAP_END
]
let gapBlock = fallbackGapBlock
if (existsSync(out)) {
  const previous = readFileSync(out, 'utf8')
  const start = previous.indexOf(GAP_START)
  const end = previous.indexOf(GAP_END)
  if (start !== -1 && end > start) {
    gapBlock = previous.slice(start, end + GAP_END.length).split(/\r?\n/)
  }
}
lines.push(...gapBlock, '')

writeFileSync(out, lines.join('\n'))
console.log(`score-board: ${rows.length} entries -> ${relative(root, out)}（manual:gaps ${gapBlock.length > fallbackGapBlock.length ? '沿用现有块' : '使用初始模板'}）`)
