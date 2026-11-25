// 盘点：无编译谱例的正文，以及其中的占位候选行
import { readdirSync, readFileSync, statSync } from 'node:fs'
import { join, relative } from 'node:path'

const root = process.argv[2] || 'content'
const files = []
;(function walk(dir) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name)
    if (statSync(p).isDirectory()) walk(p)
    else if (name.endsWith('.md')) files.push(p)
  }
})(root)

const rows = []
for (const p of files) {
  if (p.endsWith('index.md')) continue
  const text = readFileSync(p, 'utf8')
  const fences = (text.match(/```lilypond/g) || []).length
  const rel = relative(root, p).replaceAll('\\', '/')
  if (fences > 0) continue
  // 候选占位行：非围栏、非链接行、含 mm. 或 m. 或 Op./K./D. 的独立短行
  const lines = text.split(/\r?\n/)
  const cands = []
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim()
    if (!line) continue
    if (line.startsWith('#') || line.startsWith('|') || line.startsWith('```')) continue
    if (/\]\(/.test(line)) continue
    if (!/(mm\.|m\.\s?\d|Op\.|K\.|D\.\s?\d)/.test(line)) continue
    if (line.length > 200) continue
    cands.push(`L${i + 1}: ${line.slice(0, 120)}`)
  }
  rows.push({ rel, fences, cands })
}

rows.sort((a, b) => b.cands.length - a.cands.length)
console.log(`无编译谱例正文：${rows.length} 篇`)
let total = 0
for (const r of rows) {
  total += r.cands.length
  console.log(`\n## ${r.rel}  (候选行 ${r.cands.length})`)
  for (const c of r.cands) console.log(`  ${c}`)
}
console.log(`\n候选行合计：${total}`)
