// 谱例围栏编译检查：从 content/ 提取所有 lilypond 围栏，按 build-notation.mjs 的包装方式
// 逐块编译（仅 LilyPond，不涉及音频链），报告每块的成功/失败与错误摘要。
// 用途：在 fluidsynth/soundfont 不可用的机器上，仍能确认"代码块可编译"。
// 用法：node local/workbench/tools/check_notation_fences.mjs [--only <pathFragment>]

import { execFile } from 'node:child_process'
import { mkdtemp, readFile, readdir, rm, writeFile } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join, relative, resolve } from 'node:path'
import { promisify } from 'node:util'

const run = promisify(execFile)
const root = resolve(import.meta.dirname, '../../..')
const contentRoot = join(root, 'content')
const lilypond = process.env.LILYPOND_PATH || 'E:\\GreenSoftware\\lilypond-2.26.0\\bin\\lilypond.exe'
const targetVersion = '2.26.0'

const onlyIndex = process.argv.indexOf('--only')
const only = onlyIndex === -1 ? null : process.argv[onlyIndex + 1]

async function walk(dir) {
  const out = []
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const path = join(dir, entry.name)
    if (entry.isDirectory()) out.push(...(await walk(path)))
    else if (entry.name.endsWith('.md')) out.push(path)
  }
  return out.sort()
}

function fences(source) {
  const lines = source.split(/\r?\n/)
  const blocks = []
  let open = null
  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i]
    if (open === null) {
      const match = /^```(\w+)?(.*)$/.exec(line)
      if (match && /^(lilypond|ly)$/.test(match[1] || '')) {
        open = { line: i + 1, info: (match[2] || '').trim(), body: [] }
      }
      continue
    }
    if (/^```\s*$/.test(line)) {
      blocks.push(open)
      open = null
      continue
    }
    open.body.push(line)
  }
  return blocks
}

function attribute(info, name) {
  const match = new RegExp(`${name}\\s*=\\s*"([^"]*)"`).exec(info || '')
  return match ? match[1] : ''
}

function wrap(code) {
  const withoutVersion = code.replace(/^\\version\s+"[^"]+"\s*\r?\n?/m, '')
  const lines = withoutVersion.split(/\r?\n/)
  const directives = lines.filter((line) => /^\s*\\(?:include|language)\b/.test(line))
  const music = lines.filter((line) => !/^\s*\\(?:include|language)\b/.test(line)).join('\n').trim()
  if (/\\score\b/.test(music)) {
    return [`\\version "${targetVersion}"`, ...directives, music].join('\n')
  }
  return [
    `\\version "${targetVersion}"`,
    ...directives,
    '\\score {',
    `  \\new Staff { ${music} }`,
    '  \\layout { }',
    '}'
  ].join('\n')
}

const tempRoot = await mkdtemp(join(tmpdir(), 'fence-check-'))
const files = await walk(contentRoot)
const results = []

for (const file of files) {
  const rel = relative(contentRoot, file).replaceAll('\\', '/')
  if (only && !rel.includes(only)) continue
  const source = await readFile(file, 'utf8')
  for (const block of fences(source)) {
    const code = block.body.join('\n')
    const title = attribute(block.info, 'title')
    const location = attribute(block.info, 'location')
    const versionCount = [...code.matchAll(/^\\version\s+"([^"]+)"/gm)].length
    const workDirectory = join(tempRoot, `${results.length}`)
    await (await import('node:fs/promises')).mkdir(workDirectory, { recursive: true })
    const target = join(workDirectory, 'fragment.ly')
    await writeFile(target, wrap(code), 'utf8')
    let ok = true
    let message = ''
    try {
      await run(lilypond, ['--pdf', '-dno-point-and-click', '-o', join(workDirectory, 'out'), target], {
        cwd: workDirectory,
        maxBuffer: 32 * 1024 * 1024
      })
    } catch (error) {
      ok = false
      message = `${error.stderr || error.message}`.split(/\r?\n/).filter(Boolean).slice(0, 6).join(' | ')
    }
    results.push({ rel, line: block.line, title, location, versionCount, ok, message })
  }
}

await rm(tempRoot, { recursive: true, force: true })

const failed = results.filter((item) => !item.ok)
const missingTitle = results.filter((item) => !item.title || !item.location)
const badVersion = results.filter((item) => item.versionCount !== 1)

for (const item of results) {
  const state = item.ok ? 'OK  ' : 'FAIL'
  console.log(`${state} ${item.rel}:${item.line}  ${item.title || '(无 title)'} / ${item.location || '(无 location)'}`)
  if (!item.ok) console.log(`       ${item.message}`)
}
console.log(
  `\n合计 ${results.length} 块：编译通过 ${results.length - failed.length}，失败 ${failed.length}；` +
    `缺 title/location ${missingTitle.length}；\\version 数量异常 ${badVersion.length}`
)
if (failed.length) process.exitCode = 1
