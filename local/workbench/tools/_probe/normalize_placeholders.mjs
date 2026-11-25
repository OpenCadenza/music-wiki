// 占位规范化（一次性脚本）：把 10 篇里的三种旧写法改成规范单行占位
// 旧写法：  > 谱例占位：…  /  *【谱例说明：…（本段未收录内联图片谱例）】*  /  *【谱例 N：…】*
// 新写法：  谱例待补：作品 乐章，mm.x–y（说明）
import { readFileSync, writeFileSync } from 'node:fs'

const FILES = [
  'content/styles/woodwind-symphonic-emancipation.md',
  'content/techniques/harmony/cadential-six-four-and-dominant-syntax.md',
  'content/techniques/harmony/lydian-mode-and-tonal-gravity.md',
  'content/techniques/sound/natural-horn-writing-and-harmonic-series.md',
  'content/techniques/sound/timpani-writing-and-classical-orchestration.md',
  'content/techniques/sound/viola-writing-and-orchestral-voicing.md',
  'content/techniques/structure/cadential-prinner-and-structural-closure.md',
  'content/techniques/structure/compound-period-hierarchical-syntax.md',
  'content/techniques/structure/phrase-expansion-and-structural-skeleton.md',
  'content/techniques/structure/sequence-mechanics-and-syntactic-functions.md'
]

const apply = process.argv.includes('--apply')
let changed = 0

function normalizeBracket(line) {
  // *【谱例说明：……】*  或  *【谱例 1：……】*
  const m = line.match(/^\*【谱例(?:说明| ?\d+)?[：:]\s*(.+?)】\*$/)
  if (!m) return null
  let body = m[1].trim()
  // 去掉「本段未收录内联图片谱例」以及它所在的空括号
  body = body.replace(/（\s*本段未收录内联图片谱例\s*）/, '')
  body = body.replace(/，?\s*本段未收录内联图片谱例/, '')
  body = body.replace(/（\s*）$/, '')
  return `谱例待补：${body}`
}

function normalizeQuote(line) {
  const m = line.match(/^>\s*谱例占位[：:]\s*(.+)$/)
  if (m) return `谱例待补：${m[1].trim()}`
  // 裸引用块占位：单行 >，含小节定位、无链接、不是元数据列表
  if (/^>\s*\S/.test(line) && /mm?\.\s*\d/.test(line) && !/\]\(/.test(line) && !/-\s*\*\*/.test(line)) {
    return `谱例待补：${line.replace(/^>\s*/, '').trim()}`
  }
  return null
}

for (const file of FILES) {
  const raw = readFileSync(file, 'utf8')
  const lines = raw.split(/\r?\n/)
  const out = []
  let fileChanged = 0
  for (const line of lines) {
    const trimmed = line.trim()
    let next = normalizeBracket(trimmed) || normalizeQuote(trimmed)
    if (next) {
      out.push(next)
      fileChanged++
      changed++
      if (!apply) console.log(`[${file}] ${trimmed}\n   → ${next}`)
    } else {
      out.push(line)
    }
  }
  if (apply && fileChanged) writeFileSync(file, out.join('\n'), 'utf8')
  if (fileChanged) console.log(`${file}: ${fileChanged} 行（${apply ? '已写入' : '预览'}）`)
}
console.log(`\n合计 ${changed} 行${apply ? '' : '（预览，未写入；加 --apply 落盘）'}`)
