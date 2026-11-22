#!/usr/bin/env node
/**
 * 第四轮整合检查工具（只读）
 *
 * 检查 content/ ↔ provenance/ ↔ local/docs/研究归档/ 三件套、index 收录、
 * 幻影谱例 id、score-board 缺口表与正文占位的差异、标题与术语口径。
 *
 * 用法：
 *   node local/workbench/tools/audit_integration.mjs              # 写入报告，打印摘要
 *   node local/workbench/tools/audit_integration.mjs --check      # 只检查不写文件（门禁用）
 *   node local/workbench/tools/audit_integration.mjs --json       # 额外把 JSON 打到 stdout
 *   node local/workbench/tools/audit_integration.mjs --quiet      # 只打印一行结果
 *   node local/workbench/tools/audit_integration.mjs --out-dir=<dir>  # 覆盖输出目录
 *   node local/workbench/tools/audit_integration.mjs --root=<dir>     # 覆盖仓库根
 *
 * 输出（默认）：
 *   local/docs/实施记录/2026-11-23-第四轮/整合检查-最新.md
 *   local/docs/实施记录/2026-11-23-第四轮/integration-audit.json
 *
 * 退出码：0 = 无 P0；1 = 存在 P0。
 * 本工具只读输入，只写上述两个输出文件；不修改 content/、provenance/、研究归档/、score-board，不执行 git。
 */
import { readdirSync, readFileSync, existsSync, statSync, mkdirSync, writeFileSync } from 'node:fs'
import { join, relative, resolve, basename } from 'node:path'
import { posix } from 'node:path'
import { fileURLToPath } from 'node:url'

// ---------------------------------------------------------------- 配置

const DEFAULT_ROOT = resolve(fileURLToPath(new URL('../../..', import.meta.url)))
const DEFAULT_OUT_DIR = 'local/docs/实施记录/2026-11-23-第四轮'
const SCOREBOARD = 'local/resources/catalog/score-board.md'
const ARCHIVE_DIR = 'local/docs/研究归档'
const BATCH_DOC = 'local/docs/实施记录/2026-11-22-第二轮/已写选题清单.md'

/** 每个违规类别的严重度；P0 决定退出码。集中在此处，便于第四轮按需调整。 */
const SEVERITY = {
  'missing-index': 'P0',
  'index-no-h1': 'P0',
  'uncollected-article': 'P0',
  'missing-provenance': 'P0',
  'missing-archive': 'P0',
  'prov-table-empty': 'P0',
  'fence-id-not-in-scoreboard': 'P0',
  'dead-link': 'P1',
  'missing-h1': 'P1',
  'title-duplicate': 'P1',
  'phantom-id': 'P1',
  'fence-id-missing-in-provenance': 'P1',
  'prov-path-mismatch': 'P1',
  'prov-license-pending': 'P1',
  'archive-path-missing': 'P1',
  'archive-status-missing': 'P1',
  'manual-gaps-stale': 'P1',
  'manual-gaps-missing': 'P1',
  'scoreboard-missing': 'P1',
  'title-mismatch': 'P2',
  'index-only-dir': 'P2',
  'axis-index-coverage': 'P2',
  'id-near-collision': 'P2',
  'archive-status-placeholder-only': 'P2',
  'placeholder-nonconforming': 'P2',
  'term-inconsistency': 'P2'
}

const SEVERITY_ORDER = ['P0', 'P1', 'P2']
const MD_ROW_CAP = 40

const CHECKS = [
  { id: 'index-presence', title: '目录索引存在与实质导览', categories: ['missing-index', 'index-no-h1', 'index-only-dir', 'axis-index-coverage'] },
  { id: 'index-coverage', title: 'index 收录本目录文章', categories: ['uncollected-article'] },
  { id: 'links', title: '相对链接可达', categories: ['dead-link'] },
  { id: 'triplet', title: '三件套（正文 / provenance / 归档）', categories: ['missing-provenance', 'missing-archive', 'prov-path-mismatch', 'archive-path-missing', 'archive-status-missing', 'archive-status-placeholder-only'] },
  { id: 'provenance-tables', title: 'provenance 两表非空与许可登记', categories: ['prov-table-empty', 'prov-license-pending'] },
  { id: 'score-ids', title: '谱例 id 对账（围栏 / provenance / score-board）', categories: ['phantom-id', 'fence-id-missing-in-provenance', 'fence-id-not-in-scoreboard', 'id-near-collision', 'scoreboard-missing'] },
  { id: 'manual-gaps', title: 'score-board 缺口表与正文占位差异', categories: ['manual-gaps-stale', 'manual-gaps-missing', 'placeholder-nonconforming'] },
  { id: 'titles', title: '标题唯一性与元数据一致', categories: ['missing-h1', 'title-duplicate', 'title-mismatch'] },
  { id: 'terms', title: '术语口径统计', categories: ['term-inconsistency'] }
]

const TERM_PAIRS = [
  { id: 'idea-motif', name: '乐思 / 乐念', variants: ['乐思', '乐念'] },
  { id: 'suspension', name: '挂留 / 悬置', variants: ['挂留', '悬置'] },
  { id: 'sequence', name: '模进 / 序列', variants: ['模进', '序列'] },
  { id: 'prinner', name: 'Prinner / 普林纳', variants: ['Prinner', '普林纳'] }
]

const ROMAN = { 一: 'i', 二: 'ii', 三: 'iii', 四: 'iv', 五: 'v', 六: 'vi', 七: 'vii', 八: 'viii', 九: 'ix', 十: 'x' }

// ---------------------------------------------------------------- 工具函数

function walkFiles(dir, { skipDirs = new Set(), ext = '.md' } = {}) {
  const acc = []
  if (!existsSync(dir)) return acc
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory() && skipDirs.has(entry.name)) continue
    const full = join(dir, entry.name)
    if (entry.isDirectory()) acc.push(...walkFiles(full, { skipDirs, ext }))
    else if (entry.name.endsWith(ext)) acc.push(full)
  }
  return acc
}

const toPosix = (p) => p.split('\\').join('/')

/** 以 content/ 为基准的相对 posix 路径 */
function contentRel(root, absPath) {
  return toPosix(relative(join(root, 'content'), absPath))
}

/** 去掉围栏代码，返回 { clean, fences }；clean 保留行数便于报行号 */
function parseFences(text) {
  const lines = text.split(/\r?\n/)
  const clean = lines.slice()
  const fences = []
  let i = 0
  while (i < lines.length) {
    const open = /^(\s*)(`{3,}|~{3,})\s*([^\s`~]*)(.*)$/.exec(lines[i])
    if (!open) {
      i += 1
      continue
    }
    const marker = open[2][0]
    const length = open[2].length
    const closeRe = new RegExp('^\\s*' + (marker === '`' ? '`' : '~') + '{' + length + ',}\\s*$')
    const body = []
    let j = i + 1
    for (; j < lines.length; j += 1) {
      if (closeRe.test(lines[j])) break
      body.push(lines[j])
    }
    const attributes = {}
    for (const attr of `${open[3]} ${open[4]}`.matchAll(/(\w+)="([^"]*)"/g)) attributes[attr[1]] = attr[2]
    fences.push({
      startLine: i + 1,
      language: (open[3] || '').toLowerCase(),
      info: `${open[3] || ''}${open[4] || ''}`.trim(),
      attributes,
      body: body.join('\n')
    })
    for (let k = i; k <= Math.min(j, lines.length - 1); k += 1) clean[k] = ''
    i = j + 1
  }
  return { clean: clean.join('\n'), fences }
}

const NOTATION_LANGS = new Set(['lilypond', 'ly', 'abc'])

function extractLinks(cleanText) {
  const links = []
  for (const m of cleanText.matchAll(/(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g)) {
    links.push({ text: m[1], target: m[2] })
  }
  return links
}

function localTarget(raw) {
  let target = raw.trim()
  if (target.startsWith('<') && target.includes('>')) target = target.slice(1, target.indexOf('>'))
  else target = target.split(/\s+/, 1)[0]
  if (!target || target.startsWith('#') || /^(?:https?:|mailto:|tel:|data:)/i.test(target)) return null
  let decoded = target
  try {
    decoded = decodeURIComponent(target)
  } catch {
    /* 保留原样 */
  }
  return decoded.split('#', 1)[0].split('?', 1)[0]
}

/** 把链接解析成 content/ 下的 posix 相对路径；越界返回 null 并标记 */
function resolveContentLink(fromRel, target) {
  const local = localTarget(target)
  if (!local) return null
  const normalized = local.replace(/\.html$/, '.md')
  const resolved = posix.normalize(normalized.startsWith('/') ? normalized.slice(1) : posix.join(posix.dirname(fromRel), normalized))
  if (resolved.startsWith('..')) return { rel: resolved, escapes: true }
  return { rel: resolved, escapes: false }
}

function resolveExists(contentRootAbs, rel) {
  const abs = join(contentRootAbs, rel)
  if (existsSync(abs) && statSync(abs).isFile()) return true
  if (existsSync(`${abs}.md`)) return true
  if (existsSync(join(abs, 'index.md'))) return true
  return false
}

/** 解析谱例 id：<work>-<movement>-mm<from>-<to>，work 归一去掉连字符 */
function parseScoreId(id) {
  const m = /^(.+?)-([ivxl]+)-mm(\d+)-(\d+)$/i.exec(id)
  if (!m) return null
  return {
    work: m[1].toLowerCase().replaceAll('-', ''),
    movement: m[2].toLowerCase(),
    from: Number(m[3]),
    to: Number(m[4])
  }
}

function rangesOverlap(a, b) {
  return Math.max(a.from, b.from) <= Math.min(a.to, b.to)
}

function workTokens(text) {
  const tokens = new Set()
  for (const m of text.matchAll(/\bop(?:us)?\.?\s*(\d+)(?:\s*(?:no|nr)\.?\s*(\d+))?/gi)) {
    tokens.add(m[2] ? `op${m[1]}no${m[2]}` : `op${m[1]}`)
  }
  for (const m of text.matchAll(/\bK\.?\s*(\d+)/g)) tokens.add(`k${m[1]}`)
  for (const m of text.matchAll(/\bD\.?\s*(\d+)/g)) tokens.add(`d${m[1]}`)
  for (const m of text.matchAll(/\bBWV\s*(\d+)/gi)) tokens.add(`bwv${m[1]}`)
  for (const m of text.matchAll(/\bHob\.?\s*([IVX]+)\s*:\s*(\d+)/gi)) tokens.add(`hob${m[1].toLowerCase()}${m[2]}`)
  return tokens
}

function romanFromChinese(text) {
  const m = /第\s*([一二三四五六七八九十])\s*乐章/.exec(text)
  return m ? ROMAN[m[1]] : null
}

function rangesIn(text) {
  return [...text.matchAll(/mm?\.?\s*(\d+)\s*[–—\-~]\s*(\d+)/g)].map((m) => ({ from: Number(m[1]), to: Number(m[2]) }))
}

function posixNormId(id) {
  return id.toLowerCase().replaceAll('-', '')
}

/** 解析 markdown 表格：返回每个数据行的单元格数组（自动跳过表格前的空行与说明行） */
function tableRows(lines, startIndex) {
  const rows = []
  let sawSeparator = false
  let started = false
  for (let i = startIndex; i < lines.length; i += 1) {
    const line = lines[i].trim()
    if (!line.startsWith('|')) {
      if (!started) continue
      break
    }
    started = true
    if (/^\|[\s:|-]+\|$/.test(line)) {
      sawSeparator = true
      continue
    }
    if (!sawSeparator) continue
    const cells = line.replace(/^\|/, '').replace(/\|$/, '').split('|').map((c) => c.trim())
    rows.push({ cells, line: i + 1 })
  }
  return rows
}

function sectionLines(text, headingPattern) {
  const lines = text.split(/\r?\n/)
  const index = lines.findIndex((l) => headingPattern.test(l))
  if (index === -1) return { found: false, lines: [], start: -1 }
  return { found: true, lines: lines.slice(index + 1), start: index }
}

function cleanIdCell(cell) {
  let value = cell.replaceAll('`', '').trim()
  value = value.replace(/（[^）]*）/g, '').replace(/\([^)]*\)/g, '').trim()
  return value
}

function isPlaceholderId(value) {
  return !value || /^(占位|暂无|无|—|–|-|待补|待定)$/.test(value) || /^（?暂无）?$/.test(value)
}

const ID_SHAPE = /^[a-z0-9][a-z0-9._-]*$/

// ---------------------------------------------------------------- CLI

const argv = process.argv.slice(2)
const flags = new Set(argv.filter((a) => a.startsWith('-')))
const optValue = (name) => {
  const hit = argv.find((a) => a.startsWith(`--${name}=`))
  return hit ? hit.slice(name.length + 3) : null
}
if (flags.has('--help') || flags.has('-h')) {
  console.log(readFileSync(fileURLToPath(import.meta.url), 'utf8').split('*/')[0].replace(/^#!.*\n/, ''))
  process.exit(0)
}

const ROOT = resolve(optValue('root') || DEFAULT_ROOT)
const OUT_DIR = resolve(ROOT, optValue('out-dir') || DEFAULT_OUT_DIR)
const CHECK_ONLY = flags.has('--check') || flags.has('--no-write')
const PRINT_JSON = flags.has('--json')
const QUIET = flags.has('--quiet')

const contentRoot = join(ROOT, 'content')
const provenanceRoot = join(ROOT, 'provenance')
const archiveRoot = join(ROOT, ARCHIVE_DIR)

// ---------------------------------------------------------------- 收集数据

const violations = []
const advisories = []
const add = (category, path, detail, extra = {}) => {
  violations.push({ category, severity: SEVERITY[category] || 'P1', path, detail, ...extra })
}
const advise = (id, detail, extra = {}) => advisories.push({ id, detail, ...extra })

if (!existsSync(contentRoot)) {
  console.error(`找不到 content/：${contentRoot}`)
  process.exit(1)
}

const allContentMd = walkFiles(contentRoot, { skipDirs: new Set(['public']) })
const indexFiles = allContentMd.filter((f) => basename(f) === 'index.md')
const articleFiles = allContentMd.filter((f) => basename(f) !== 'index.md')

const articles = articleFiles.map((abs) => {
  const rel = contentRel(ROOT, abs)
  const text = readFileSync(abs, 'utf8')
  const { clean, fences } = parseFences(text)
  const notation = fences.filter((f) => NOTATION_LANGS.has(f.language))
  const h1 = (/^#\s+(.+)$/m.exec(clean) || [])[1]?.trim() || ''
  const fmBlock = /^---\r?\n([\s\S]*?)\r?\n---/.exec(text)
  const fmTitle = fmBlock ? (/^title:\s*(.+)$/m.exec(fmBlock[1]) || [])[1]?.trim() : null
  return {
    rel,
    abs,
    text,
    clean,
    fences,
    notation,
    fenceIds: notation.map((f) => f.attributes.id).filter(Boolean),
    untaggedFences: notation.filter((f) => !f.attributes.id).length,
    h1,
    fmTitle: fmTitle || null,
    links: extractLinks(clean),
    chars: clean.replace(/\s/g, '').length
  }
})
const articleByRel = new Map(articles.map((a) => [a.rel, a]))
const allFenceIds = new Set()
for (const a of articles) for (const id of a.fenceIds) allFenceIds.add(id)

// 批次（首批 / 第二轮）映射：按选题清单出现顺序前 20 / 后 20
const batchBySlug = new Map()
let batchSource = 'unavailable'
if (existsSync(join(ROOT, BATCH_DOC))) {
  const doc = readFileSync(join(ROOT, BATCH_DOC), 'utf8')
  const paths = [...doc.matchAll(/`content\/([^`]+\.md)`/g)].map((m) => m[1])
  if (paths.length >= 40) {
    paths.forEach((p, i) => batchBySlug.set(basename(p, '.md'), i < 20 ? '首批' : '第二轮'))
    batchSource = BATCH_DOC
  }
}
const batchOf = (article) => batchBySlug.get(basename(article.rel, '.md')) || '未知'

// ---------------------------------------------------------------- 1. 目录与索引

const dirsWithArticles = new Map() // dirRel -> article rels
for (const a of articles) {
  const dir = posix.dirname(a.rel)
  if (!dirsWithArticles.has(dir)) dirsWithArticles.set(dir, [])
  dirsWithArticles.get(dir).push(a.rel)
}
const dirsWithIndex = new Set(indexFiles.map((f) => posix.dirname(contentRel(ROOT, f))))
const allDirs = new Set([...dirsWithArticles.keys(), ...dirsWithIndex])

for (const dir of [...allDirs].sort()) {
  if (dir !== '.' && !dirsWithIndex.has(dir)) add('missing-index', dir, '目录有文章但没有 index.md')
  if (dir === '.' || dirsWithArticles.has(dir)) continue
  // 只有 index.md、且子树里也没有任何文章，才算空壳目录
  const subtree = articles.some((a) => a.rel.startsWith(`${dir}/`))
  if (!subtree) add('index-only-dir', dir, '目录只有 index.md，子树没有文章（空壳目录）')
}

const indexCoverage = []
for (const indexAbs of indexFiles.sort()) {
  const rel = contentRel(ROOT, indexAbs)
  const dir = posix.dirname(rel)
  const text = readFileSync(indexAbs, 'utf8')
  const { clean } = parseFences(text)
  if (!/^#\s+.+$/m.test(clean)) add('index-no-h1', rel, 'index.md 缺少一级标题')
  const linkedRels = new Set()
  const linkedDirs = new Set()
  for (const link of extractLinks(clean)) {
    const resolved = resolveContentLink(rel, link.target)
    if (!resolved) continue
    if (resolved.escapes) {
      add('dead-link', rel, `链接越出 content/：${link.target}`)
      continue
    }
    linkedRels.add(resolved.rel)
    if (link.target.endsWith('/') || resolveExists(contentRoot, resolved.rel) === false) linkedDirs.add(resolved.rel)
    if (!resolveExists(contentRoot, resolved.rel)) add('dead-link', rel, `链接目标不存在：${link.target}`)
  }
  const own = (dirsWithArticles.get(dir) || []).filter((r) => r !== rel).sort()
  const uncollected = own.filter((r) => !linkedRels.has(r))
  for (const r of uncollected) {
    add('uncollected-article', r, `${dir}/index.md 未收录本文`, { index: `${dir}/index.md` })
  }
  indexCoverage.push({ dir: dir === '.' ? '' : dir, index: rel, articles: own.length, linked: own.length - uncollected.length, uncollected })
}

// 轴根导览覆盖率（P2 信息项）：只有含二级子目录的轴（techniques / composers）才检查，
// 平铺轴（ensembles / styles / notation）的收录问题已由 uncollected-article 覆盖。
const AXES = ['techniques', 'composers']
for (const axis of AXES) {
  const indexRel = `${axis}/index.md`
  if (!existsSync(join(contentRoot, indexRel))) continue
  const hasSubdirs = articles.some((a) => a.rel.startsWith(`${axis}/`) && a.rel.split('/').length > 2)
  if (!hasSubdirs) continue
  const { clean } = parseFences(readFileSync(join(contentRoot, indexRel), 'utf8'))
  const linkedRels = new Set()
  const linkedDirs = new Set()
  for (const link of extractLinks(clean)) {
    const resolved = resolveContentLink(indexRel, link.target)
    if (!resolved || resolved.escapes) continue
    linkedRels.add(resolved.rel)
    if (link.target.endsWith('/')) linkedDirs.add(resolved.rel.replace(/\/$/, ''))
  }
  const subtree = articles.filter((a) => a.rel.startsWith(`${axis}/`))
  const missing = subtree.filter((a) => {
    if (linkedRels.has(a.rel)) return false
    const parts = a.rel.split('/')
    for (let i = 1; i < parts.length; i += 1) {
      if (linkedDirs.has(parts.slice(0, i).join('/'))) return false
    }
    return true
  })
  if (missing.length) {
    add('axis-index-coverage', indexRel, `轴根导览未覆盖 ${missing.length}/${subtree.length} 篇子树文章`, { missing: missing.map((a) => a.rel) })
  }
}

// ---------------------------------------------------------------- 2. 相对链接可达（正文）

for (const a of articles) {
  for (const link of a.links) {
    const resolved = resolveContentLink(a.rel, link.target)
    if (!resolved) continue
    if (resolved.escapes) {
      add('dead-link', a.rel, `链接越出 content/：${link.target}`)
      continue
    }
    if (!resolveExists(contentRoot, resolved.rel)) add('dead-link', a.rel, `链接目标不存在：${link.target}`)
  }
}

// ---------------------------------------------------------------- 3. 三件套

function findArchive(slug) {
  const abs = join(archiveRoot, `${slug}.md`)
  return existsSync(abs) ? abs : null
}

const provenanceByRel = new Map()
for (const a of articles) {
  const slug = basename(a.rel, '.md')
  const provAbs = join(provenanceRoot, a.rel)
  const archiveAbs = findArchive(slug)

  if (!existsSync(provAbs)) add('missing-provenance', a.rel, '缺少同名 provenance 文件')
  else {
    const provText = readFileSync(provAbs, 'utf8')
    const articleLine = /文章[：:]\s*`([^`]+)`/.exec(provText)?.[1] || ''
    if (articleLine && articleLine !== `content/${a.rel}`) {
      add('prov-path-mismatch', a.rel, `provenance 登记的正文路径不符：${articleLine}`, { expected: `content/${a.rel}` })
    }
    const license = (/^-\s*许可[：:]\s*(.+)$/m.exec(provText) || [])[1]?.trim() || ''
    if (!license || /^(待补|未确认|待确认|—|-|无)$/.test(license)) {
      add('prov-license-pending', a.rel, `文件头许可未落实：「${license || '缺失'}」`)
    }
    const citeSection = sectionLines(provText, /^##\s*引用与出处\s*$/)
    const scoreSection = sectionLines(provText, /^##\s*谱例\s*$/)
    const citeRows = citeSection.found ? tableRows(citeSection.lines, 0) : []
    const scoreRows = scoreSection.found ? tableRows(scoreSection.lines, 0) : []
    if (!citeSection.found || citeRows.length === 0) add('prov-table-empty', a.rel, '「引用与出处」表缺失或没有数据行')
    if (!scoreSection.found || scoreRows.length === 0) add('prov-table-empty', a.rel, '「谱例」表缺失或没有数据行')
    const scoreIds = scoreRows.map((r) => cleanIdCell(r.cells[0] || '')).filter((v) => !isPlaceholderId(v))
    provenanceByRel.set(a.rel, { abs: provAbs, text: provText, scoreRows, scoreIds, citeRows })
  }

  if (!archiveAbs) add('missing-archive', a.rel, `缺少研究归档（${ARCHIVE_DIR}/${slug}.md）`)
  else {
    const archiveText = readFileSync(archiveAbs, 'utf8')
    if (!archiveText.includes(`content/${a.rel}`)) {
      add('archive-path-missing', a.rel, '归档未写明正文路径', { archive: `${ARCHIVE_DIR}/${slug}.md` })
    }
    const statusField = /^-\s*\*\*(?:当前)?状态\*\*\s*[：:]\s*(.+)$/m.exec(archiveText)
    const statusSection = /^##\s*复读状态/m.test(archiveText)
    if (!statusField && !statusSection) {
      add('archive-status-missing', a.rel, '归档没有状态字段或「复读状态」小节')
    } else {
      const statusValue = statusField ? statusField[1] : ''
      if (
        statusField &&
        /占位|待补|待核验|待后续/.test(statusValue) &&
        !/复读|整合|已完成|已定稿|已核验|已交付/.test(statusValue)
      ) {
        add('archive-status-placeholder-only', a.rel, `归档状态只描述谱例占位：「${statusValue.slice(0, 60)}」`)
      }
    }
  }
}

// ---------------------------------------------------------------- 4. 谱例 id 对账

// 4.1 score-board
let boardIds = []
let boardExists = existsSync(join(ROOT, SCOREBOARD))
let gaps = { found: false, rows: [] }
let scoreRefsTotal = 0
if (!boardExists) add('scoreboard-missing', SCOREBOARD, '找不到 score-board.md')
else {
  const boardText = readFileSync(join(ROOT, SCOREBOARD), 'utf8')
  boardIds = [...boardText.matchAll(/^\|\s*`([^`]+)`\s*\|/gm)].map((m) => m[1])
  const boardIdSet = new Set(boardIds)
  const dupBoard = boardIds.filter((id, i) => boardIds.indexOf(id) !== i)
  if (dupBoard.length) add('fence-id-not-in-scoreboard', SCOREBOARD, `score-board 有重复 id：${[...new Set(dupBoard)].join(', ')}`)

  const gapBlock = /<!--\s*manual:gaps\s*-->([\s\S]*?)<!--\s*\/manual:gaps\s*-->/.exec(boardText)
  if (!gapBlock) add('manual-gaps-missing', SCOREBOARD, '缺少 <!-- manual:gaps --> 手工缺口区')
  else {
    const gapLines = gapBlock[1].split(/\r?\n/)
    const rows = tableRows(gapLines, 0)
    gaps = { found: true, rows: rows.map((r) => ({ work: r.cells[0] || '', span: r.cells[1] || '', status: r.cells[2] || '', line: r.line })) }
  }

  // 4.2 围栏 id ↔ score-board
  for (const a of articles) {
    for (const id of a.fenceIds) {
      if (!boardIdSet.has(id)) add('fence-id-not-in-scoreboard', a.rel, `围栏 id 不在 score-board：${id}`, { id })
    }
  }
  // 4.3 围栏 id ↔ 本篇 provenance
  for (const a of articles) {
    const prov = provenanceByRel.get(a.rel)
    if (!prov) continue
    const set = new Set(prov.scoreIds)
    for (const id of a.fenceIds) {
      if (!set.has(id)) add('fence-id-missing-in-provenance', a.rel, `围栏 id 未登记在本篇 provenance 谱例表：${id}`, { id })
    }
    // 4.4 幻影 id：provenance 有、正文围栏无
    for (const id of prov.scoreIds) {
      if (allFenceIds.has(id)) continue
      if (!ID_SHAPE.test(id)) {
        add('phantom-id', a.rel, `谱例表 id 列不是合法 id：「${id}」`, { id })
        continue
      }
      add('phantom-id', a.rel, `谱例表登记了 id 但正文没有对应围栏：${id}`, { id })
    }
  }
  // 4.5 近似 id：幻影 id 与真实围栏同作品同乐章且区间重叠
  const realParsed = [...allFenceIds].map((id) => ({ id, parsed: parseScoreId(id) })).filter((x) => x.parsed)
  for (const a of articles) {
    const prov = provenanceByRel.get(a.rel)
    if (!prov) continue
    for (const id of prov.scoreIds) {
      if (allFenceIds.has(id)) continue
      const p = parseScoreId(id)
      if (!p) continue
      for (const real of realParsed) {
        if (real.parsed.work !== p.work || real.parsed.movement !== p.movement) continue
        if (!rangesOverlap(p, real.parsed)) continue
        add('id-near-collision', a.rel, `计划 id ${id} 与既有围栏 ${real.id} 同作品同乐章且小节重叠（补谱会重复）`, { id, existing: real.id })
      }
    }
  }
}
// score-board 里出现但全库没有围栏的 id
if (boardExists) {
  const fenceSet = allFenceIds
  for (const id of boardIds) if (!fenceSet.has(id)) add('fence-id-not-in-scoreboard', SCOREBOARD, `score-board 有 id 但全库没有对应围栏：${id}`, { id })
}

// 4.6 正文里的 #score- 引用（信息项）
for (const a of articles) scoreRefsTotal += [...a.clean.matchAll(/#score-[a-z0-9.-]+/g)].length

// ---------------------------------------------------------------- 5. 缺口表 vs 正文占位

function placeholderStats(article) {
  const standard = (article.clean.match(/谱例待补/g) || []).length
  const bracket = (article.clean.match(/【谱例说明/g) || []).length
  const noInline = (article.clean.match(/未收录内联图片谱例/g) || []).length
  // 裸引用块占位：只认「单行引用块 + 作品号 + mm 区间 + 没有链接 + 不是元数据列表」
  // 多行引用块通常是跨篇导航/谱例元数据说明，不算占位。
  const blocks = []
  let current = []
  for (const line of article.clean.split(/\r?\n/)) {
    if (/^\s*>/.test(line)) current.push(line.trim())
    else if (current.length) {
      blocks.push(current)
      current = []
    }
  }
  if (current.length) blocks.push(current)
  const quoteLines = blocks
    .filter((block) => {
      if (block.length !== 1) return false
      const line = block[0]
      if (/\]\(/.test(line)) return false
      if (/-\s*\*\*[^*]+\*\*\s*[：:]/.test(line)) return false
      if (!/mm\.?\s*\d/.test(line)) return false
      return workTokens(line).size > 0
    })
    .map((block) => block[0])
  const quotePlaceholder = quoteLines.length
  const placeholderTokens = new Set()
  for (const line of article.clean.split(/\r?\n/)) {
    if (!/【谱例说明|未收录内联图片谱例|谱例待补/.test(line) && !quoteLines.includes(line.trim())) continue
    for (const token of workTokens(line)) placeholderTokens.add(token)
  }
  const provPlaceholderRows = (provenanceByRel.get(article.rel)?.scoreRows || []).filter((r) => isPlaceholderId(cleanIdCell(r.cells[0] || ''))).length
  return {
    standard,
    bracket,
    noInline,
    quotePlaceholder,
    provPlaceholderRows,
    placeholderTokens: [...placeholderTokens],
    nonconforming: bracket + noInline + quotePlaceholder,
    hasGapSignal: standard + bracket + noInline + quotePlaceholder > 0
  }
}

const placeholders = new Map(articles.map((a) => [a.rel, placeholderStats(a)]))
for (const [rel, stats] of placeholders) {
  if (stats.nonconforming > 0) {
    add('placeholder-nonconforming', rel, `占位不是规范「谱例待补」写法：括号说明 ${stats.bracket}、未收录内联 ${stats.noInline}、裸引用块 ${stats.quotePlaceholder}`)
  }
}

if (gaps.found) {
  for (const row of gaps.rows) {
    const tokens = workTokens(`${row.work} ${row.span}`)
    const movement = romanFromChinese(row.work) || null
    const rowRanges = rangesIn(row.span)
    const mentionedIds = [...row.status.matchAll(/`([a-z0-9][a-z0-9._-]+)`/g)].map((m) => m[1])
    const filledId = mentionedIds.find((id) => allFenceIds.has(id))
    let staleReason = null
    if (filledId) staleReason = `状态里提到的 ${filledId} 已存在于正文围栏`
    else if (/已(回填|补|交付|完成)/.test(row.status)) staleReason = '状态显示已完成但仍在缺口表'
    else {
      for (const a of articles) {
        const p = a.fenceIds.map(parseScoreId).filter(Boolean)
        for (const parsed of p) {
          const idTokens = workTokens(parsed.work)
          const tokenMatch = [...tokens].some((t) => idTokens.has(t))
          if (!tokenMatch) continue
          if (movement && parsed.movement !== movement) continue
          if (rowRanges.length === 0 || rowRanges.some((r) => rangesOverlap(r, parsed))) {
            staleReason = `正文已有同作品${movement ? `同乐章` : ''}重叠围栏（${a.fenceIds.find((f) => parseScoreId(f))}）`
            break
          }
        }
        if (staleReason) break
      }
    }
    if (staleReason) {
      add('manual-gaps-stale', SCOREBOARD, `缺口行疑似过期：${row.work} ${row.span}｜${row.status}（${staleReason}）`, { work: row.work, span: row.span, status: row.status })
    }
  }
}

// 信息项：有明确占位写法但没有缺口登记（只按强信号判断，避免把 provenance 计划行算进来）
const gapWorksText = gaps.rows.map((r) => `${r.work} ${r.span}`).join('\n')
const gapTokens = workTokens(gapWorksText)
const placeholderNoGap = []
for (const [rel, stats] of placeholders) {
  if (stats.standard + stats.bracket + stats.noInline + stats.quotePlaceholder === 0) continue
  const covered = stats.placeholderTokens.some((t) => gapTokens.has(t))
  if (!covered) placeholderNoGap.push(rel)
}
if (placeholderNoGap.length) {
  advise('placeholder-without-gap', `${placeholderNoGap.length} 篇有谱例占位/计划但没有登记到 score-board manual:gaps`, { files: placeholderNoGap })
}

// ---------------------------------------------------------------- 6. 标题与术语

const titleStats = { total: articles.length, duplicates: [], missingH1: [], mismatch: [] }
const byH1 = new Map()
for (const a of articles) {
  if (!a.h1) titleStats.missingH1.push(a.rel)
  if (a.h1) {
    if (!byH1.has(a.h1)) byH1.set(a.h1, [])
    byH1.get(a.h1).push(a.rel)
  }
  if (a.fmTitle && a.h1 && a.fmTitle !== a.h1) titleStats.mismatch.push({ rel: a.rel, h1: a.h1, fmTitle: a.fmTitle })
}
for (const [title, rels] of byH1) {
  if (rels.length > 1) {
    titleStats.duplicates.push({ title, rels })
    add('title-duplicate', rels[0], `标题重复：「${title}」出现在 ${rels.length} 篇`, { rels })
  }
}
for (const rel of titleStats.missingH1) add('missing-h1', rel, '正文缺少一级标题')
for (const item of titleStats.mismatch) add('title-mismatch', item.rel, `frontmatter title「${item.fmTitle}」≠ 一级标题「${item.h1}」`)

const termStats = {}
for (const pair of TERM_PAIRS) {
  const variants = {}
  for (const variant of pair.variants) {
    const files = []
    let occurrences = 0
    const byBatch = { 首批: 0, 第二轮: 0, 未知: 0 }
    for (const a of articles) {
      const count = a.clean.split(variant).length - 1
      if (!count) continue
      occurrences += count
      files.push({ rel: a.rel, count, batch: batchOf(a) })
      byBatch[batchOf(a)] += 1
    }
    variants[variant] = { articles: files.length, occurrences, byBatch, files }
  }
  termStats[pair.id] = { name: pair.name, variants }
  const used = Object.values(variants).filter((v) => v.articles > 0)
  if (used.length > 1) {
    add('term-inconsistency', 'content/', `${pair.name} 两种写法并存：${Object.entries(variants).map(([k, v]) => `${k} ${v.articles} 篇`).join(' / ')}`)
  }
}

// ---------------------------------------------------------------- 输出

const severityCounts = { P0: 0, P1: 0, P2: 0 }
for (const v of violations) severityCounts[v.severity] = (severityCounts[v.severity] || 0) + 1

const checksOut = CHECKS.map((check) => {
  const own = violations.filter((v) => check.categories.includes(v.category))
  const bySeverity = { P0: 0, P1: 0, P2: 0 }
  for (const v of own) bySeverity[v.severity] += 1
  return {
    id: check.id,
    title: check.title,
    violations: own.length,
    bySeverity,
    status: own.some((v) => v.severity === 'P0') ? 'fail' : own.length ? 'warn' : 'pass'
  }
})

const fenceCount = articles.reduce((n, a) => n + a.fenceIds.length, 0)
const summary = {
  articles: articles.length,
  contentDirs: [...allDirs].filter((d) => d !== '.').length,
  indexFiles: indexFiles.length,
  notationBlocks: fenceCount,
  notationBlocksWithoutId: articles.reduce((n, a) => n + a.untaggedFences, 0),
  provenance: [...provenanceByRel.keys()].length,
  archives: articles.filter((a) => findArchive(basename(a.rel, '.md'))).length,
  scoreboardIds: boardIds.length,
  manualGaps: gaps.rows.length,
  scoreRefs: scoreRefsTotal,
  batchSource,
  severityCounts,
  exitCode: severityCounts.P0 > 0 ? 1 : 0,
  passed: severityCounts.P0 === 0
}

const json = {
  tool: 'local/workbench/tools/audit_integration.mjs',
  schemaVersion: 1,
  generatedAt: new Date().toISOString(),
  root: ROOT,
  summary,
  checks: checksOut,
  violations: violations.sort(
    (a, b) =>
      SEVERITY_ORDER.indexOf(a.severity) - SEVERITY_ORDER.indexOf(b.severity) ||
      a.category.localeCompare(b.category) ||
      a.path.localeCompare(b.path)
  ),
  advisories,
  indexCoverage,
  termStats,
  titleStats,
  scoreBoard: { exists: boardExists, ids: boardIds.length, gaps },
  placeholders: Object.fromEntries([...placeholders].map(([rel, stats]) => [rel, stats]))
}

// --- 人读摘要
const categoryTitle = (category) => {
  const map = {
    'missing-index': '目录缺 index.md',
    'index-no-h1': 'index 缺一级标题',
    'index-only-dir': '空壳目录（只有 index）',
    'axis-index-coverage': '轴根导览未覆盖子树',
    'uncollected-article': '文章未被本目录 index 收录',
    'dead-link': '相对链接不可达',
    'missing-provenance': '缺 provenance',
    'missing-archive': '缺研究归档',
    'prov-path-mismatch': 'provenance 正文路径不符',
    'archive-path-missing': '归档未写正文路径',
    'archive-status-missing': '归档缺状态',
    'archive-status-placeholder-only': '归档状态只写占位',
    'prov-table-empty': 'provenance 表为空',
    'prov-license-pending': '许可未落实',
    'phantom-id': '幻影谱例 id（有登记无围栏）',
    'fence-id-missing-in-provenance': '围栏 id 未进 provenance',
    'fence-id-not-in-scoreboard': '围栏 id 与 score-board 不一致',
    'id-near-collision': '计划 id 与既有围栏同段冲突',
    'scoreboard-missing': 'score-board 缺失',
    'manual-gaps-stale': '缺口表疑似过期',
    'manual-gaps-missing': '缺口区缺失',
    'placeholder-nonconforming': '占位写法不规范',
    'missing-h1': '正文缺一级标题',
    'title-duplicate': '标题重复',
    'title-mismatch': 'frontmatter 标题与 H1 不一致',
    'term-inconsistency': '术语两种写法并存'
  }
  return map[category] || category
}

const mdRows = (items, render) => {
  const rows = items.slice(0, MD_ROW_CAP).map(render)
  if (items.length > MD_ROW_CAP) rows.push(`| … | 其余 ${items.length - MD_ROW_CAP} 条见 JSON |`)
  return rows
}

const esc = (s) => String(s).replaceAll('|', '\\|').replace(/\r?\n/g, ' ')
const md = []
md.push('# 整合检查（自动生成）', '')
md.push(`- 生成时间：${new Date().toISOString()}（UTC）`)
md.push('- 运行命令：`node local/workbench/tools/audit_integration.mjs`（只读；`--check` 只检查不写文件）')
md.push(`- 结论：**P0 = ${severityCounts.P0}，P1 = ${severityCounts.P1}，P2 = ${severityCounts.P2}** → ${summary.passed ? '通过（exit 0）' : '未通过（exit 1）'}`)
md.push(`- 输入快照：正文 ${summary.articles} 篇 / 内容目录 ${summary.contentDirs} / index ${summary.indexFiles} / 谱例块 ${summary.notationBlocks} / provenance ${summary.provenance} / 归档 ${summary.archives} / score-board id ${summary.scoreboardIds} 行 / manual:gaps ${summary.manualGaps} 条`)
md.push(`- 批次映射来源：${batchSource === 'unavailable' ? '未找到选题清单，按「未知」处理' : `\`${batchSource}\``}`)
md.push('')
md.push('## 总表', '')
md.push('| 检查项 | 结果 | P0 | P1 | P2 |')
md.push('| --- | --- | --- | --- | --- |')
for (const check of checksOut) {
  const label = check.status === 'fail' ? '未通过' : check.status === 'warn' ? '告警' : '通过'
  md.push(`| ${check.title}（\`${check.id}\`） | ${label} | ${check.bySeverity.P0} | ${check.bySeverity.P1} | ${check.bySeverity.P2} |`)
}
md.push('')

for (const severity of SEVERITY_ORDER) {
  const own = violations.filter((v) => v.severity === severity)
  if (!own.length) continue
  md.push(`## ${severity} 明细（${own.length} 条）`, '')
  const byCategory = new Map()
  for (const v of own) {
    if (!byCategory.has(v.category)) byCategory.set(v.category, [])
    byCategory.get(v.category).push(v)
  }
  for (const [category, items] of [...byCategory].sort((a, b) => b[1].length - a[1].length)) {
    md.push(`### ${categoryTitle(category)}（${category}，${items.length} 条）`, '')
    md.push('| 位置 | 问题 |')
    md.push('| --- | --- |')
    md.push(...mdRows(items, (v) => `| \`${esc(v.path)}\` | ${esc(v.detail)} |`))
    md.push('')
  }
}

md.push('## 目录收录明细', '')
md.push('| 目录 | index | 本目录文章 | 已收录 | 未收录 |')
md.push('| --- | --- | --- | --- | --- |')
for (const row of indexCoverage.sort((a, b) => a.dir.localeCompare(b.dir))) {
  md.push(`| ${row.dir || '(根)'} | \`${row.index}\` | ${row.articles} | ${row.linked} | ${row.uncollected.length ? row.uncollected.map((r) => `\`${r.split('/').pop()}\``).join('<br>') : '—'} |`)
}
md.push('')

md.push('## 谱例 id 对账', '')
md.push(`- 围栏 id：${allFenceIds.size} 个（无 id 围栏 ${summary.notationBlocksWithoutId} 个）`)
md.push(`- score-board id：${boardIds.length} 行`)
md.push(`- 幻影 id（provenance 有、正文无）：${violations.filter((v) => v.category === 'phantom-id').length} 条`)
md.push(`- 围栏 id 未进 score-board：${violations.filter((v) => v.category === 'fence-id-not-in-scoreboard').length} 条`)
md.push(`- 围栏 id 未进本篇 provenance：${violations.filter((v) => v.category === 'fence-id-missing-in-provenance').length} 条`)
md.push(`- 正文 \`#score-<id>\` 锚点引用：${summary.scoreRefs} 处`)
md.push('')

if (gaps.rows.length) {
  md.push('## manual:gaps 现状', '')
  md.push('| 作品 | 片段 | 状态 | 判定 |')
  md.push('| --- | --- | --- | --- |')
  const staleKeys = new Set(violations.filter((v) => v.category === 'manual-gaps-stale').map((v) => `${v.work}||${v.span}`))
  for (const row of gaps.rows) {
    md.push(`| ${esc(row.work)} | ${esc(row.span)} | ${esc(row.status)} | ${staleKeys.has(`${row.work}||${row.span}`) ? '**疑似过期**' : '有效/待核'} |`)
  }
  md.push('')
}

md.push('## 术语统计', '')
md.push('| 术语对 | 写法 A（篇数/次数） | 写法 B（篇数/次数） | 判定 |')
md.push('| --- | --- | --- | --- |')
for (const pair of TERM_PAIRS) {
  const stat = termStats[pair.id]
  const [a, b] = pair.variants
  const va = stat.variants[a]
  const vb = stat.variants[b]
  md.push(`| ${pair.name} | ${a}：${va.articles} 篇 / ${va.occurrences} 次 | ${b}：${vb.articles} 篇 / ${vb.occurrences} 次 | ${va.articles && vb.articles ? '**混用**' : '单一'} |`)
}
md.push('')
md.push('## 标题与元数据', '')
md.push(`- 正文 ${titleStats.total} 篇；缺 H1：${titleStats.missingH1.length}；标题重复：${titleStats.duplicates.length} 组；frontmatter≠H1：${titleStats.mismatch.length}`)
if (titleStats.mismatch.length) {
  md.push('')
  md.push('| 文章 | frontmatter | H1 |')
  md.push('| --- | --- | --- |')
  for (const item of titleStats.mismatch) md.push(`| \`${item.rel}\` | ${esc(item.fmTitle)} | ${esc(item.h1)} |`)
}
md.push('')

if (advisories.length) {
  md.push('## 信息项（不计入违规）', '')
  for (const item of advisories) {
    md.push(`- **${item.id}**：${item.detail}`)
    if (item.files) for (const f of item.files.slice(0, 20)) md.push(`  - \`${f}\``)
    if (item.files && item.files.length > 20) md.push(`  - …其余 ${item.files.length - 20} 篇见 JSON`)
  }
  md.push('')
}

md.push('## 说明', '')
md.push('- 本工具只读 `content/`、`provenance/`、`local/docs/研究归档/`、`local/resources/catalog/score-board.md`，只写本报告与 `integration-audit.json`；不改正文、不改归档、不执行 git。')
md.push('- 严重度映射集中在脚本顶部 `SEVERITY`；P0 决定退出码，供第四轮收口当门禁。')
md.push('- `score-board.md` 的 `manual:gaps` 为手工维护区，`local/workbench/tools/build-score-board.mjs` 重新生成整表时会用硬编码模板覆盖该区——重新生成前请先备份手工缺口表。')
md.push('')

const mdText = md.join('\n')

// ---------------------------------------------------------------- 落盘与输出

if (!QUIET) {
  console.log(`整合检查：正文 ${summary.articles} 篇，内容目录 ${summary.contentDirs}，谱例 ${summary.notationBlocks} 块`)
  for (const check of checksOut) {
    const label = check.status === 'fail' ? 'FAIL' : check.status === 'warn' ? 'WARN' : 'PASS'
    console.log(`  [${label}] ${check.id.padEnd(18)} P0=${check.bySeverity.P0} P1=${check.bySeverity.P1} P2=${check.bySeverity.P2}`)
  }
  console.log(`P0=${severityCounts.P0} P1=${severityCounts.P1} P2=${severityCounts.P2} → ${summary.passed ? '通过' : '未通过'}`)
}

if (!CHECK_ONLY) {
  mkdirSync(OUT_DIR, { recursive: true })
  const mdPath = join(OUT_DIR, '整合检查-最新.md')
  const jsonPath = join(OUT_DIR, 'integration-audit.json')
  writeFileSync(mdPath, mdText)
  writeFileSync(jsonPath, `${JSON.stringify(json, null, 2)}\n`)
  if (!QUIET) console.log(`报告：${toPosix(relative(ROOT, mdPath))}\n数据：${toPosix(relative(ROOT, jsonPath))}`)
} else if (!QUIET) {
  console.log('（--check：未写文件）')
}

if (PRINT_JSON) console.log(JSON.stringify(json, null, 2))

process.exitCode = summary.exitCode
