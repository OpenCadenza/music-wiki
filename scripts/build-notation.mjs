import { spawn } from 'node:child_process'
import { createHash } from 'node:crypto'
import { existsSync } from 'node:fs'
import {
  copyFile,
  mkdir,
  readFile,
  readdir,
  rm,
  stat,
  writeFile
} from 'node:fs/promises'
import { join, relative, resolve, sep } from 'node:path'
import { fileURLToPath } from 'node:url'
import { Midi } from '@tonejs/midi'
import MarkdownIt from 'markdown-it'

const root = resolve(fileURLToPath(new URL('..', import.meta.url)))
const contentRoot = join(root, 'content')
const publicRoot = join(root, 'public')
const notationRoot = join(publicRoot, 'notation')
const workRoot = join(root, '.notation-work')
const targetVersion = '2.26.0'
const cacheSchema = 1
const force = process.argv.includes('--force')

const lilypond = process.env.LILYPOND_PATH || 'lilypond'
const abc2midi = process.env.ABC2MIDI_PATH || 'abc2midi'
const fluidsynth = process.env.FLUIDSYNTH_PATH || 'fluidsynth'
const ffmpeg = process.env.FFMPEG_PATH || 'ffmpeg'
const abc2svg =
  process.env.ABC2SVG_PATH ||
  join(
    root,
    'node_modules',
    '.bin',
    process.platform === 'win32' ? 'abc2svg.cmd' : 'abc2svg'
  )

const soundfontCandidates = [
  process.env.SOUNDFONT_PATH,
  'E:/programfiles/i-score/data/soundfonts/fluidr3-gm/FluidR3_GM.sf2',
  join(root, 'soundfonts', 'FluidR3_GM.sf2')
].filter(Boolean)
const soundfont = soundfontCandidates.find((candidate) => existsSync(candidate))

if (!soundfont) {
  throw new Error(
    'FluidR3 GM soundfont not found. Set SOUNDFONT_PATH or place FluidR3_GM.sf2 in soundfonts/.'
  )
}

const markdown = new MarkdownIt({ html: true })
const instrumentPrograms = new Map(
  Object.entries({
    piano: 0,
    'acoustic grand piano': 0,
    harpsichord: 6,
    celesta: 8,
    organ: 19,
    guitar: 24,
    violin: 40,
    viola: 41,
    cello: 42,
    contrabass: 43,
    strings: 48,
    'string ensemble': 48,
    trumpet: 56,
    trombone: 57,
    tuba: 58,
    'french horn': 60,
    saxophone: 65,
    flute: 73,
    oboe: 68,
    clarinet: 71,
    bassoon: 70
  })
)

function digest(data) {
  return createHash('sha256').update(data).digest('hex')
}

function slash(path) {
  return path.split(sep).join('/')
}

function safeAssetId(value, hash) {
  const safe = value
    .toLowerCase()
    .replace(/[^a-z0-9._-]+/g, '-')
    .replace(/^-+|-+$/g, '')
  return safe || `notation-${hash.slice(0, 16)}`
}

function run(command, args, options = {}) {
  return new Promise((resolvePromise, reject) => {
    const child = spawn(command, args, {
      cwd: options.cwd || root,
      env: { ...process.env, SOURCE_DATE_EPOCH: '946684800' },
      shell: process.platform === 'win32' && command.toLowerCase().endsWith('.cmd'),
      windowsHide: true
    })
    const stdout = []
    const stderr = []
    child.stdout.on('data', (chunk) => stdout.push(chunk))
    child.stderr.on('data', (chunk) => stderr.push(chunk))
    child.on('error', reject)
    child.on('close', (code) => {
      const result = {
        code,
        stdout: Buffer.concat(stdout).toString('utf8'),
        stderr: Buffer.concat(stderr).toString('utf8')
      }
      if (code !== 0) {
        reject(
          new Error(
            `${command} exited with ${code}\n${result.stderr || result.stdout}`.trim()
          )
        )
        return
      }
      resolvePromise(result)
    })
  })
}

async function walk(directory) {
  const files = []
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name)
    if (entry.isDirectory()) {
      files.push(...(await walk(path)))
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      files.push(path)
    }
  }
  return files.sort()
}

function metadataBefore(lines, openingLine) {
  const prefix = lines.slice(Math.max(0, openingLine - 100), openingLine).join('\n')
  const matches = [
    ...prefix.matchAll(/<!--\s*(opusloom:example|music-kb:block)\s*([\s\S]*?)-->/g)
  ]
  const last = matches.at(-1)
  if (!last) return {}
  try {
    return JSON.parse(last[2].trim())
  } catch {
    return {}
  }
}

function pageHeading(text) {
  const match = text.match(/^#\s+(.+)$/m)
  return match ? match[1].trim() : '音乐谱例'
}

async function collectBlocks() {
  const blocks = []
  for (const path of await walk(contentRoot)) {
    const source = await readFile(path, 'utf8')
    const lines = source.split(/\r?\n/)
    const pageTitle = pageHeading(source)
    const tokens = markdown.parse(source, {})
    let notationIndex = 0
    for (const token of tokens) {
      if (token.type !== 'fence') continue
      const language = token.info.trim().split(/\s+/, 1)[0].toLowerCase()
      if (!['abc', 'lilypond', 'ly'].includes(language)) continue
      notationIndex += 1
      const normalizedLanguage = language === 'ly' ? 'lilypond' : language
      const hash = digest(token.content)
      const metadata = metadataBefore(lines, token.map?.[0] || 0)

      if (normalizedLanguage === 'lilypond') {
        const versions = [...token.content.matchAll(/^\\version\s+"([^"]+)"/gm)].map(
          (match) => match[1]
        )
        if (versions.length !== 1 || versions[0] !== targetVersion) {
          throw new Error(
            `${slash(relative(root, path))}:${(token.map?.[0] || 0) + 1}: ` +
              `LilyPond code must declare exactly \\version "${targetVersion}"`
          )
        }
      }

      const stableId =
        metadata.id ||
        `notation.${slash(relative(contentRoot, path)).replace(/\.md$/, '').replaceAll('/', '.')}.${notationIndex}`
      const context = String(metadata.context || metadata.title || '').trim()
      const title = context
        ? `${pageTitle}: ${context.length > 72 ? `${context.slice(0, 72)}...` : context}`
        : `${pageTitle} (${notationIndex})`
      blocks.push({
        path,
        relativePath: slash(relative(contentRoot, path)),
        line: (token.map?.[0] || 0) + 1,
        code: token.content,
        hash,
        stableId,
        language: normalizedLanguage,
        metadata,
        title
      })
    }
  }
  return blocks
}

function withoutVersion(code) {
  return code.replace(/^\\version\s+"[^"]+"\s*\r?\n?/m, '')
}

function skipQuotedAndComments(source, index) {
  const character = source[index]
  if (character === '"') {
    index += 1
    while (index < source.length) {
      if (source[index] === '\\') index += 2
      else if (source[index] === '"') return index + 1
      else index += 1
    }
  }
  if (character === '%' && source[index + 1] === '{') {
    const end = source.indexOf('%}', index + 2)
    return end < 0 ? source.length : end + 2
  }
  if (character === '%') {
    const end = source.indexOf('\n', index + 1)
    return end < 0 ? source.length : end + 1
  }
  return index
}

function matchingBrace(source, opening) {
  let depth = 0
  for (let index = opening; index < source.length; index += 1) {
    const skipped = skipQuotedAndComments(source, index)
    if (skipped !== index) {
      index = skipped - 1
      continue
    }
    if (source[index] === '{') depth += 1
    if (source[index] === '}') {
      depth -= 1
      if (depth === 0) return index
    }
  }
  throw new Error('Unbalanced LilyPond braces while adding MIDI output')
}

function withMidiOutput(code) {
  const scoreEnds = []
  const scorePattern = /\\score\b/g
  let match
  while ((match = scorePattern.exec(code))) {
    let opening = match.index + match[0].length
    while (opening < code.length && /\s/.test(code[opening])) opening += 1
    if (code[opening] !== '{') {
      throw new Error('Expected { after \\score while adding MIDI output')
    }
    const closing = matchingBrace(code, opening)
    const block = code.slice(opening, closing + 1)
    if (!/\\midi\b/.test(block)) scoreEnds.push(closing)
    scorePattern.lastIndex = closing + 1
  }

  if (scoreEnds.length === 0 && /\\score\b/.test(code)) return code
  if (scoreEnds.length === 0) {
    return [
      `\\version "${targetVersion}"`,
      '\\score {',
      `  \\new Staff { ${withoutVersion(code).trim()} }`,
      '  \\layout { }',
      '  \\midi { }',
      '}'
    ].join('\n')
  }

  let rendered = code
  for (const position of scoreEnds.sort((a, b) => b - a)) {
    rendered =
      rendered.slice(0, position) + '\n  \\midi { }\n' + rendered.slice(position)
  }
  return rendered
}

async function filesWithExtension(directory, extension) {
  return (await readdir(directory))
    .filter((name) => name.toLowerCase().endsWith(extension))
    .sort()
}

async function renderLilyPond(block, outputDirectory) {
  const workDirectory = join(workRoot, block.hash)
  await rm(workDirectory, { recursive: true, force: true })
  await mkdir(workDirectory, { recursive: true })

  const sourcePath = join(workDirectory, 'source.ly')
  const scorePath = join(workDirectory, 'score.ly')
  const audioPath = join(workDirectory, 'audio.ly')
  await writeFile(sourcePath, block.code, 'utf8')
  await writeFile(scorePath, block.code, 'utf8')
  await writeFile(audioPath, withMidiOutput(block.code), 'utf8')

  await run(
    lilypond,
    ['-dbackend=svg', '-dno-point-and-click', '-o', 'page', scorePath],
    { cwd: workDirectory }
  )
  const svgFiles = await filesWithExtension(workDirectory, '.svg')
  if (svgFiles.length === 0) {
    throw new Error(`${block.stableId}: LilyPond produced no SVG`)
  }
  const svg = []
  for (let index = 0; index < svgFiles.length; index += 1) {
    const targetName = `page-${index + 1}.svg`
    await copyFile(join(workDirectory, svgFiles[index]), join(outputDirectory, targetName))
    svg.push(targetName)
  }

  await run(lilypond, ['-dno-point-and-click', '-o', 'audio', audioPath], {
    cwd: workDirectory
  })
  const midiFiles = [
    ...(await filesWithExtension(workDirectory, '.mid')),
    ...(await filesWithExtension(workDirectory, '.midi'))
  ]
  if (midiFiles.length !== 1) {
    throw new Error(
      `${block.stableId}: expected one LilyPond MIDI file, found ${midiFiles.length}`
    )
  }
  return {
    svg,
    midi: join(workDirectory, midiFiles[0]),
    sourceName: 'source.ly'
  }
}

async function renderAbc(block, outputDirectory) {
  const workDirectory = join(workRoot, block.hash)
  await rm(workDirectory, { recursive: true, force: true })
  await mkdir(workDirectory, { recursive: true })

  const sourcePath = join(workDirectory, 'source.abc')
  const renderPath = join(workDirectory, 'render.abc')
  await writeFile(sourcePath, block.code, 'utf8')
  const renderSource = /^%%fullsvg\b/m.test(block.code)
    ? block.code
    : `%%fullsvg 1\n${block.code}`
  await writeFile(renderPath, renderSource, 'utf8')

  const rendered = await run(abc2svg, [renderPath], { cwd: workDirectory })
  const svgPages = [...rendered.stdout.matchAll(/<svg\b[\s\S]*?<\/svg>/gi)].map(
    (match) => match[0]
  )
  if (svgPages.length === 0) {
    throw new Error(`${block.stableId}: abc2svg produced no SVG`)
  }
  const svg = []
  for (let index = 0; index < svgPages.length; index += 1) {
    const targetName = `page-${index + 1}.svg`
    await writeFile(join(outputDirectory, targetName), `${svgPages[index]}\n`, 'utf8')
    svg.push(targetName)
  }

  const midiPath = join(workDirectory, 'audio.mid')
  await run(abc2midi, [sourcePath, '-o', midiPath], { cwd: workDirectory })
  if (!(await stat(midiPath)).size) {
    throw new Error(`${block.stableId}: abc2midi produced an empty MIDI file`)
  }
  return {
    svg,
    midi: midiPath,
    sourceName: 'source.abc'
  }
}

function requestedProgram(block) {
  const requested = block.metadata.instrument || block.metadata.midi_instrument
  if (requested !== undefined && requested !== null && requested !== '') {
    const numeric = Number(requested)
    if (Number.isInteger(numeric) && numeric >= 0 && numeric <= 127) return numeric
    const program = instrumentPrograms.get(String(requested).toLowerCase())
    if (program === undefined) {
      throw new Error(`${block.stableId}: unknown General MIDI instrument ${requested}`)
    }
    return program
  }

  const hasLilyInstrument =
    /midiInstrument|Staff\.midiInstrument/.test(block.code) &&
    block.language === 'lilypond'
  const hasAbcInstrument =
    /^%%MIDI\s+(?:program|voice\b.*instrument=)/im.test(block.code) &&
    block.language === 'abc'
  return hasLilyInstrument || hasAbcInstrument ? null : 0
}

async function applyProgram(block, midiPath) {
  const program = requestedProgram(block)
  if (program === null) return
  const midi = new Midi(await readFile(midiPath))
  for (const track of midi.tracks) track.instrument.number = program
  await writeFile(midiPath, Buffer.from(midi.toArray()))
}

async function renderAudio(block, midiPath, outputDirectory) {
  await applyProgram(block, midiPath)
  const wavPath = join(outputDirectory, 'audio.wav')
  const mp3Path = join(outputDirectory, 'audio.mp3')
  await run(fluidsynth, [
    '-ni',
    '-g',
    '0.85',
    '-r',
    '44100',
    '-F',
    wavPath,
    soundfont,
    midiPath
  ])
  await run(ffmpeg, [
    '-hide_banner',
    '-loglevel',
    'error',
    '-y',
    '-i',
    wavPath,
    '-codec:a',
    'libmp3lame',
    '-b:a',
    '128k',
    mp3Path
  ])
  if (!(await stat(mp3Path)).size) {
    throw new Error(`${block.stableId}: ffmpeg produced an empty MP3 file`)
  }
  await rm(wavPath, { force: true })
}

async function existingArtifactsAreUsable(block, outputDirectory) {
  if (force) return false
  const metadataPath = join(outputDirectory, 'metadata.json')
  if (!existsSync(metadataPath)) return false
  try {
    const metadata = JSON.parse(await readFile(metadataPath, 'utf8'))
    if (
      metadata.cacheSchema !== cacheSchema ||
      metadata.sourceHash !== block.hash ||
      metadata.targetVersion !== targetVersion
    ) {
      return false
    }
    for (const relativePath of [
      ...metadata.svg,
      metadata.audio,
      metadata.source
    ]) {
      const artifact = join(outputDirectory, relativePath)
      if (!existsSync(artifact) || (await stat(artifact)).size === 0) return false
    }
    return true
  } catch {
    return false
  }
}

async function main() {
  await mkdir(notationRoot, { recursive: true })
  await mkdir(workRoot, { recursive: true })
  const blocks = await collectBlocks()
  const ids = new Set()
  const manifestBlocks = []

  for (const block of blocks) {
    const assetId = safeAssetId(block.stableId, block.hash)
    if (ids.has(assetId)) {
      throw new Error(`Duplicate notation asset id ${assetId}`)
    }
    ids.add(assetId)
    const outputDirectory = join(notationRoot, assetId)
    await mkdir(outputDirectory, { recursive: true })

    let metadata
    if (await existingArtifactsAreUsable(block, outputDirectory)) {
      metadata = JSON.parse(await readFile(join(outputDirectory, 'metadata.json'), 'utf8'))
      console.log(`reuse ${assetId}`)
    } else {
      for (const name of await readdir(outputDirectory)) {
        await rm(join(outputDirectory, name), { recursive: true, force: true })
      }
      console.log(`compile ${assetId} (${block.relativePath}:${block.line})`)
      const rendered =
        block.language === 'lilypond'
          ? await renderLilyPond(block, outputDirectory)
          : await renderAbc(block, outputDirectory)
      await renderAudio(block, rendered.midi, outputDirectory)
      await writeFile(
        join(outputDirectory, rendered.sourceName),
        block.code,
        'utf8'
      )
      metadata = {
        cacheSchema,
        id: block.stableId,
        title: block.title,
        language: block.language,
        sourceHash: block.hash,
        targetVersion,
        sourcePath: block.relativePath,
        svg: rendered.svg,
        audio: 'audio.mp3',
        source: rendered.sourceName
      }
      await writeFile(
        join(outputDirectory, 'metadata.json'),
        `${JSON.stringify(metadata, null, 2)}\n`,
        'utf8'
      )
    }

    metadata.title = block.title
    manifestBlocks.push({
      hash: block.hash,
      id: block.stableId,
      language: block.language,
      title: block.title,
      svg: metadata.svg.map((name) => `/notation/${assetId}/${name}`),
      audio: `/notation/${assetId}/${metadata.audio}`,
      source: `/notation/${assetId}/${metadata.source}`,
      sourcePath: block.relativePath,
      line: block.line
    })
  }

  for (const entry of await readdir(notationRoot, { withFileTypes: true })) {
    if (entry.isDirectory() && !ids.has(entry.name)) {
      const stale = resolve(notationRoot, entry.name)
      if (!stale.startsWith(`${notationRoot}${sep}`)) {
        throw new Error(`Refusing to remove stale path outside notation root: ${stale}`)
      }
      await rm(stale, { recursive: true, force: true })
    }
  }

  const manifest = {
    schemaVersion: 1,
    targetVersion,
    blocks: manifestBlocks
  }
  await writeFile(
    join(notationRoot, 'manifest.json'),
    `${JSON.stringify(manifest, null, 2)}\n`,
    'utf8'
  )
  console.log(`notation: ${manifestBlocks.length} blocks, target ${targetVersion}`)
}

await main()
