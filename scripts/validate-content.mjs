import { existsSync } from 'node:fs'
import { createHash } from 'node:crypto'
import { readFile, readdir, stat } from 'node:fs/promises'
import { dirname, extname, join, relative, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import MarkdownIt from 'markdown-it'

const root = resolve(fileURLToPath(new URL('..', import.meta.url)))
const contentRoot = join(root, 'content')
const targetVersion = '2.26.0'
const errors = []
const markdown = new MarkdownIt({ html: true })
const sourceIds = new Map()
const fenceHashes = new Map()

async function walk(directory) {
  const files = []
  const directories = []
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name)
    if (resolve(directory) === resolve(contentRoot) && entry.name === 'public') {
      continue
    }
    if (entry.isDirectory()) {
      directories.push(path)
      const nested = await walk(path)
      files.push(...nested.files)
      directories.push(...nested.directories)
    } else if (entry.isFile()) {
      files.push(path)
    }
  }
  return { files, directories }
}

function relativePath(path) {
  return relative(contentRoot, path).split('\\').join('/')
}

function metadataBefore(text, openingLine) {
  const lines = text.split(/\r?\n/)
  const prefix = lines.slice(Math.max(0, openingLine - 100), openingLine).join('\n').trimEnd()
  const matches = [
    ...prefix.matchAll(/<!--\s*(?:opusloom:example|music-kb:block)\s*([\s\S]*?)-->/g)
  ]
  const match = matches.at(-1)
  if (!match || prefix.slice(match.index + match[0].length).trim()) return null
  return match[1]
}

function localTarget(raw) {
  let target = raw.trim()
  if (target.startsWith('<') && target.includes('>')) {
    target = target.slice(1, target.indexOf('>'))
  } else {
    target = target.split(/\s+/, 1)[0]
  }
  if (
    !target ||
    target.startsWith('#') ||
    /^(?:https?:|mailto:|tel:|data:)/i.test(target)
  ) {
    return null
  }
  return decodeURIComponent(target.split('#', 1)[0].split('?', 1)[0])
}

const { files, directories } = await walk(contentRoot)
for (const directory of directories) {
  if (directory.split(/[\\/]/).includes('_maintenance')) continue
  if (!existsSync(join(directory, 'index.md'))) {
    errors.push(`${relativePath(directory)}: directory needs index.md`)
  }
}

let notationBlocks = 0
for (const path of files) {
  const rel = relativePath(path)
  if (path.endsWith('README.md')) {
    errors.push(`${rel}: use index.md for a directory entry page`)
  }
  if (!path.endsWith('.md')) continue
  const text = await readFile(path, 'utf8')
  if (rel !== 'index.md') {
    const directoryIndex = join(dirname(path), 'index.md')
    if (!existsSync(directoryIndex) && resolve(dirname(path)) !== resolve(contentRoot)) {
      errors.push(`${rel}: parent directory needs index.md`)
    }
  }
  if ((rel === 'index.md' || path.endsWith('index.md')) && !/^#\s+.+$/m.test(text)) {
    errors.push(`${rel}: index.md needs a level-one heading`)
  }

  const tokens = markdown.parse(text, {})
  let pageFenceIndex = 0
  const codeLines = new Set()
  for (const token of tokens) {
    if (token.type !== 'fence') continue
    for (let line = token.map?.[0] || 0; line < (token.map?.[1] || 0); line += 1) {
      codeLines.add(line)
    }
    const language = token.info.trim().split(/\s+/, 1)[0].toLowerCase()
    if (!['abc', 'lilypond', 'ly'].includes(language)) continue
    notationBlocks += 1
    pageFenceIndex += 1
    const line = (token.map?.[0] || 0) + 1
    const hash = createHash('sha256').update(token.content).digest('hex')
    if (fenceHashes.has(hash)) {
      errors.push(`${rel}:${line}: duplicate notation content also used by ${fenceHashes.get(hash)}`)
    } else {
      fenceHashes.set(hash, `${rel}:${line}`)
    }

    // 谱例元数据是可选的：正文不再写来源、许可或定位字段。
    // 若作者仍写了注释块，只校验它是合法 JSON。
    const rawMetadata = metadataBefore(text, token.map?.[0] || 0)
    let metadata = {}
    if (rawMetadata) {
      try {
        metadata = JSON.parse(rawMetadata.trim())
      } catch {
        errors.push(`${rel}:${line}: invalid notation metadata JSON`)
      }
    }
    const id =
      metadata.id || `notation.${rel.replace(/\.md$/, '').replaceAll('/', '.')}.${pageFenceIndex}`
    if (sourceIds.has(id)) {
      errors.push(`${rel}:${line}: duplicate notation id ${id}; first used at ${sourceIds.get(id)}`)
    } else {
      sourceIds.set(id, `${rel}:${line}`)
    }

    if (language === 'lilypond' || language === 'ly') {
      const versions = [...token.content.matchAll(/^\\version\s+"([^"]+)"/gm)].map(
        (match) => match[1]
      )
      if (versions.length !== 1) {
        errors.push(`${rel}:${line}: LilyPond needs exactly one version declaration`)
      } else if (versions[0] !== targetVersion) {
        errors.push(
          `${rel}:${line}: LilyPond version ${versions[0]} is not ${targetVersion}`
        )
      }
    }
  }

  const lines = text.split(/\r?\n/)
  for (let index = 0; index < lines.length; index += 1) {
    if (codeLines.has(index)) continue
    const line = lines[index]
    for (const match of line.matchAll(/(?<!!)\[[^\]]*\]\(([^)]+)\)/g)) {
      const target = localTarget(match[1])
      if (!target) continue
      const normalizedTarget = target.replace(/\.html$/, '.md')
      const resolved = normalizedTarget.startsWith('/')
        ? resolve(contentRoot, normalizedTarget.slice(1))
        : resolve(dirname(path), normalizedTarget)
      const resolvedRoot = resolve(contentRoot)
      const rootPrefix = `${resolvedRoot}${process.platform === 'win32' ? '\\' : '/'}`
      if (resolved !== resolvedRoot && !resolved.startsWith(rootPrefix)) {
        errors.push(`${rel}:${index + 1}: link escapes content root: ${target}`)
      } else if (!existsSync(resolved) && !existsSync(`${resolved}.md`)) {
        errors.push(`${rel}:${index + 1}: missing link target ${target}`)
      }
    }
  }
}

if (notationBlocks === 0) {
  errors.push('expected at least one ABC/LilyPond block')
}

// 来源与许可不再登记在 content/ 内，改为仓库根 NOTICE.md。
if (!existsSync(join(root, 'NOTICE.md'))) {
  errors.push('NOTICE.md is missing at repository root')
}
if (existsSync(join(contentRoot, 'knowledge', 'sources.json'))) {
  errors.push('content/knowledge/sources.json: source registry belongs in NOTICE.md')
}

if (errors.length) {
  console.error([...new Set(errors)].join('\n'))
  process.exitCode = 1
} else {
  console.log(
    `content validation passed: ${files.filter((path) => path.endsWith('.md')).length} Markdown files, ` +
      `${directories.length} directories, ${notationBlocks} notation blocks`
  )
}
