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
import midiPackage from '@tonejs/midi'
import MarkdownIt from 'markdown-it'

const { Midi } = midiPackage

const root = resolve(fileURLToPath(new URL('..', import.meta.url)))
const contentRoot = join(root, 'content')
const notationRoot = join(root, 'public', 'notation')
const workRoot = join(root, '.notation-work')
const toolchain = JSON.parse(await readFile(join(root, 'toolchains.json'), 'utf8'))
const targetVersion = toolchain.lilypond.version
const generatorVersion = '4'
const cacheSchema = 4
const checkOnly = process.argv.includes('--check')
const force = process.argv.includes('--force')

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

async function digestFile(path) {
  return digest(await readFile(path))
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
      shell: false,
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
        stdout: Buffer.concat(stdout).toString('utf8').trim(),
        stderr: Buffer.concat(stderr).toString('utf8').trim()
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

function executable(environmentName, candidates) {
  const fromEnvironment = process.env[environmentName]
  if (fromEnvironment) return fromEnvironment
  return candidates.find((candidate) => existsSync(candidate)) || candidates.at(-1)
}

const executables = {
  lilypond: executable('LILYPOND_PATH', [
    join(root, '.tools', 'lilypond-2.26.0', 'bin', 'lilypond.exe'),
    join(root, '.tools', 'lilypond-2.26.0', 'bin', 'lilypond'),
    'lilypond'
  ]),
  abc2midi: executable('ABC2MIDI_PATH', [
    join(root, '.tools', 'abcmidi-20261016', 'abc2midi.exe'),
    join(root, '.tools', 'abcmidi-20261016', 'abc2midi'),
    'abc2midi'
  ]),
  fluidsynth: executable('FLUIDSYNTH_PATH', [
    join(
      root,
      '.tools',
      'fluidsynth-v2.6.1-win10-x64-cpp11',
      'bin',
      'fluidsynth.exe'
    ),
    'fluidsynth'
  ]),
  ffmpeg: executable('FFMPEG_PATH', ['ffmpeg']),
  ffprobe: executable(
    'FFPROBE_PATH',
    process.env.FFMPEG_PATH
      ? [process.env.FFMPEG_PATH.replace(/ffmpeg(?:\.exe)?$/i, (match) =>
          match.replace(/ffmpeg/i, 'ffprobe')
        )]
      : ['ffprobe']
  ),
  abc2svg:
    process.env.ABC2SVG_PATH ||
    join(root, 'node_modules', 'abc2svg', 'abc2svg')
}

const soundfontCandidates = [
  process.env.SOUNDFONT_PATH,
  join(root, '.tools', 'soundfonts', toolchain.soundfont.filename),
  'E:/programfiles/i-score/data/soundfonts/fluidr3-gm/FluidR3_GM.sf2',
  join(root, 'soundfonts', toolchain.soundfont.filename)
].filter(Boolean)
const soundfont = soundfontCandidates.find((candidate) => existsSync(candidate))

function firstLine(text) {
  return text.split(/\r?\n/, 1)[0].trim()
}

async function probeTools() {
  const [
    lilypondOutput,
    abc2midiOutput,
    fluidsynthOutput,
    ffmpegOutput,
    ffprobeOutput
  ] = await Promise.all([
    run(executables.lilypond, ['--version']),
    run(executables.abc2midi, ['-ver']),
    run(executables.fluidsynth, ['--version']),
    run(executables.ffmpeg, ['-version']),
    run(executables.ffprobe, ['-version'])
  ])
  const lilyVersion = firstLine(lilypondOutput.stdout)
  if (!new RegExp(`\\b${targetVersion.replaceAll('.', '\\.')}\\b`).test(lilyVersion)) {
    throw new Error(
      `LilyPond ${targetVersion} is required; version probe returned: ${lilyVersion}`
    )
  }
  const abc2svgPackage = JSON.parse(
    await readFile(join(root, 'node_modules', 'abc2svg', 'package.json'), 'utf8')
  )
  if (abc2svgPackage.version !== toolchain.abc2svg) {
    throw new Error(
      `abc2svg ${toolchain.abc2svg} is required; installed version is ${abc2svgPackage.version}`
    )
  }
  if (!soundfont) {
    throw new Error(
      'FluidR3 GM soundfont not found. Run scripts/install-toolchain.ps1 or set SOUNDFONT_PATH.'
    )
  }
  const soundfontHash = await digestFile(soundfont)
  if (soundfontHash !== toolchain.soundfont.sha256) {
    throw new Error(
      `Soundfont hash mismatch: expected ${toolchain.soundfont.sha256}, found ${soundfontHash}`
    )
  }
  return {
    versions: {
      lilypond: lilyVersion,
      abc2midi: firstLine(abc2midiOutput.stdout || abc2midiOutput.stderr),
      abc2svg: abc2svgPackage.version,
      fluidsynth: firstLine(fluidsynthOutput.stdout),
      ffmpeg: firstLine(ffmpegOutput.stdout),
      ffprobe: firstLine(ffprobeOutput.stdout)
    },
    soundfont: {
      name: toolchain.soundfont.filename,
      sha256: soundfontHash,
      license: toolchain.soundfont.license
    }
  }
}

async function walk(directory) {
  const files = []
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name)
    if (entry.isDirectory()) files.push(...(await walk(path)))
    else if (entry.isFile() && entry.name.endsWith('.md')) files.push(path)
  }
  return files.sort()
}

function metadataBefore(lines, openingLine) {
  const prefix = lines.slice(Math.max(0, openingLine - 100), openingLine).join('\n').trimEnd()
  const matches = [
    ...prefix.matchAll(
      /<!--\s*(opusloom:example|music-kb:block)\s*([\s\S]*?)-->/g
    )
  ]
  const match = matches.at(-1)
  if (!match || prefix.slice(match.index + match[0].length).trim()) return {}
  try {
    return JSON.parse(match[2].trim())
  } catch {
    throw new Error('Invalid notation metadata JSON')
  }
}

function pageHeading(text) {
  const match = text.match(/^#\s+(.+)$/m)
  return match ? match[1].replaceAll(/[*_`]/g, '').trim() : '音乐谱例'
}

async function collectBlocks() {
  const blocks = []
  const hashes = new Map()
  const ids = new Map()
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
      const line = (token.map?.[0] || 0) + 1
      const relativePath = slash(relative(contentRoot, path))
      const hash = digest(token.content)
      const previousHash = hashes.get(hash)
      if (previousHash) {
        throw new Error(
          `Identical notation blocks are not supported: ${relativePath}:${line} and ${previousHash}`
        )
      }
      hashes.set(hash, `${relativePath}:${line}`)
      const metadata = metadataBefore(lines, token.map?.[0] || 0)
      if (normalizedLanguage === 'lilypond') {
        const versions = [...token.content.matchAll(/^\\version\s+"([^"]+)"/gm)].map(
          (match) => match[1]
        )
        if (versions.length !== 1 || versions[0] !== targetVersion) {
          throw new Error(
            `${relativePath}:${line}: LilyPond code must declare exactly ` +
              `\\version "${targetVersion}"`
          )
        }
      }
      const stableId =
        metadata.id ||
        `notation.${relativePath.replace(/\.md$/, '').replaceAll('/', '.')}.${notationIndex}`
      if (ids.has(stableId)) {
        throw new Error(
          `Duplicate notation id ${stableId}: ${relativePath}:${line} and ${ids.get(stableId)}`
        )
      }
      ids.set(stableId, `${relativePath}:${line}`)
      const context = String(metadata.context || metadata.title || '').trim()
      const title = context
        ? `${pageTitle}: ${context.length > 72 ? `${context.slice(0, 72)}...` : context}`
        : `${pageTitle} (${notationIndex})`
      blocks.push({
        path,
        relativePath,
        line,
        code: token.content,
        hash,
        stableId,
        language: normalizedLanguage,
        status: metadata.status || 'published',
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

function splitTopLevelDirectives(code) {
  const directives = []
  const music = []
  for (const line of withoutVersion(code).split(/\r?\n/)) {
    if (/^\s*\\(?:include|language)\b/.test(line)) directives.push(line)
    else music.push(line)
  }
  return { directives, music: music.join('\n').trim() }
}

function wrappedFragment(code, midi) {
  const { directives, music } = splitTopLevelDirectives(code)
  return [
    `\\version "${targetVersion}"`,
    ...directives,
    '\\score {',
    `  \\new Staff { ${music} }`,
    '  \\layout { }',
    ...(midi ? ['  \\midi { }'] : []),
    '}'
  ].join('\n')
}

function withLayoutOutput(code) {
  return /\\score\b/.test(code) ? code : wrappedFragment(code, false)
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
  if (scoreEnds.length === 0) return wrappedFragment(code, true)

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
    .sort((a, b) => a.localeCompare(b, 'en', { numeric: true }))
}

async function mergeMidiFiles(paths, outputPath) {
  if (paths.length === 1) return paths[0]
  const merged = new Midi()
  let offset = 0
  for (const path of paths) {
    const source = new Midi(await readFile(path))
    for (const sourceTrack of source.tracks) {
      const track = merged.addTrack()
      track.name = sourceTrack.name
      track.channel = sourceTrack.channel
      track.instrument.number = sourceTrack.instrument.number
      for (const note of sourceTrack.notes) {
        track.addNote({
          midi: note.midi,
          time: note.time + offset,
          duration: note.duration,
          velocity: note.velocity
        })
      }
    }
    offset += source.duration + 0.1
  }
  await writeFile(outputPath, Buffer.from(merged.toArray()))
  return outputPath
}

async function renderLilyPond(block, workDirectory, outputDirectory) {
  const layoutDirectory = join(workDirectory, 'layout')
  const audioDirectory = join(workDirectory, 'audio')
  await Promise.all([
    mkdir(layoutDirectory, { recursive: true }),
    mkdir(audioDirectory, { recursive: true })
  ])
  const scorePath = join(layoutDirectory, 'score.ly')
  const audioPath = join(audioDirectory, 'score.ly')
  await writeFile(scorePath, withLayoutOutput(block.code), 'utf8')
  await writeFile(audioPath, withMidiOutput(block.code), 'utf8')

  await run(
    executables.lilypond,
    ['-dcrop', '-dbackend=svg', '-dno-point-and-click', '-o', 'page', 'score.ly'],
    { cwd: layoutDirectory }
  )
  const svgFiles = await filesWithExtension(layoutDirectory, '.svg')
  if (svgFiles.length === 0) {
    throw new Error(`${block.stableId}: LilyPond produced no SVG`)
  }
  const croppedSvgFiles = []
  for (const name of svgFiles) {
    const head = (await readFile(join(layoutDirectory, name), 'utf8')).slice(0, 512)
    if (!/width="210\.00mm"\s+height="297\.00mm"/.test(head)) {
      croppedSvgFiles.push(name)
    }
  }
  if (croppedSvgFiles.length === 0) {
    throw new Error(`${block.stableId}: LilyPond produced no cropped SVG`)
  }
  const svg = []
  for (const [index, sourceName] of croppedSvgFiles.entries()) {
    const targetName = `page-${index + 1}.svg`
    await copyFile(join(layoutDirectory, sourceName), join(outputDirectory, targetName))
    svg.push(targetName)
  }

  await run(
    executables.lilypond,
    ['-dno-point-and-click', '-o', 'score', 'score.ly'],
    { cwd: audioDirectory }
  )
  const midiFiles = [
    ...(await filesWithExtension(audioDirectory, '.mid')),
    ...(await filesWithExtension(audioDirectory, '.midi'))
  ]
  if (midiFiles.length === 0) {
    throw new Error(`${block.stableId}: LilyPond produced no MIDI`)
  }
  const midi = await mergeMidiFiles(
    midiFiles.map((name) => join(audioDirectory, name)),
    join(audioDirectory, 'merged.mid')
  )
  return { svg, midi, sourceName: 'source.ly' }
}

async function renderAbc(block, workDirectory, outputDirectory) {
  const sourcePath = join(workDirectory, 'source.abc')
  const renderPath = join(workDirectory, 'render.abc')
  await writeFile(sourcePath, block.code, 'utf8')
  const renderSource = /^%%fullsvg\b/m.test(block.code)
    ? block.code
    : `%%fullsvg 1\n${block.code}`
  await writeFile(renderPath, renderSource, 'utf8')

  const rendered = await run(process.execPath, [executables.abc2svg, renderPath], {
    cwd: workDirectory
  })
  const svgPages = [...rendered.stdout.matchAll(/<svg\b[\s\S]*?<\/svg>/gi)].map(
    (match) => match[0]
  )
  if (svgPages.length === 0) {
    throw new Error(`${block.stableId}: abc2svg produced no SVG`)
  }
  const svg = []
  for (const [index, source] of svgPages.entries()) {
    const targetName = `page-${index + 1}.svg`
    await writeFile(join(outputDirectory, targetName), `${source}\n`, 'utf8')
    svg.push(targetName)
  }

  await run(
    executables.abc2midi,
    [sourcePath, '-o', join(workDirectory, 'audio.mid')],
    { cwd: workDirectory }
  )
  const midiFiles = [
    ...(await filesWithExtension(workDirectory, '.mid')),
    ...(await filesWithExtension(workDirectory, '.midi'))
  ]
  if (midiFiles.length === 0) {
    throw new Error(`${block.stableId}: abc2midi produced no MIDI`)
  }
  const midi = await mergeMidiFiles(
    midiFiles.map((name) => join(workDirectory, name)),
    join(workDirectory, 'merged.mid')
  )
  return { svg, midi, sourceName: 'source.abc' }
}

function requestedInstrument(block) {
  const requested = block.metadata.instrument || block.metadata.midi_instrument
  if (requested !== undefined && requested !== null && requested !== '') {
    const numeric = Number(requested)
    if (Number.isInteger(numeric) && numeric >= 0 && numeric <= 127) {
      return { strategy: 'metadata', label: String(requested), program: numeric }
    }
    const program = instrumentPrograms.get(String(requested).toLowerCase())
    if (program === undefined) {
      throw new Error(`${block.stableId}: unknown General MIDI instrument ${requested}`)
    }
    return { strategy: 'metadata', label: String(requested), program }
  }
  const embedded =
    block.language === 'lilypond'
      ? /midiInstrument|Staff\.midiInstrument/.test(block.code)
      : /^%%MIDI\s+(?:program|voice\b.*instrument=)/im.test(block.code)
  return embedded
    ? { strategy: 'score', label: 'score MIDI program', program: null }
    : { strategy: 'default', label: 'acoustic grand piano', program: 0 }
}

async function readMidi(path) {
  const midi = new Midi(await readFile(path))
  const notes = midi.tracks.flatMap((track) => track.notes)
  return {
    midi,
    noteCount: notes.length,
    duration: midi.duration,
    contentDuration: notes.reduce(
      (maximum, note) => Math.max(maximum, note.time + note.duration),
      0
    )
  }
}

async function applyInstrument(block, midiPath, instrument) {
  if (instrument.program === null) {
    const midiMetadata = await readMidi(midiPath)
    return midiMetadata
  }
  const midiMetadata = await readMidi(midiPath)
  for (const track of midiMetadata.midi.tracks) {
    track.instrument.number = instrument.program
  }
  await writeFile(midiPath, Buffer.from(midiMetadata.midi.toArray()))
  return readMidi(midiPath)
}

async function mediaDuration(path) {
  const result = await run(executables.ffprobe, [
    '-v',
    'error',
    '-show_entries',
    'format=duration',
    '-of',
    'default=noprint_wrappers=1:nokey=1',
    path
  ])
  const duration = Number(result.stdout)
  if (!Number.isFinite(duration) || duration <= 0) {
    throw new Error(`ffprobe returned invalid duration for ${path}`)
  }
  return duration
}

async function assertAudible(path) {
  const result = await run(executables.ffmpeg, [
    '-hide_banner',
    '-i',
    path,
    '-af',
    'volumedetect',
    '-f',
    'null',
    '-'
  ])
  const match = `${result.stderr}\n${result.stdout}`.match(
    /max_volume:\s+(-?[\d.]+|-inf)\s+dB/i
  )
  if (!match || match[1].toLowerCase() === '-inf' || Number(match[1]) < -50) {
    throw new Error(`${path}: rendered audio is silent or too quiet`)
  }
}

async function renderAudio(block, midiPath, outputDirectory, instrument) {
  const midiMetadata = await applyInstrument(block, midiPath, instrument)
  if (midiMetadata.noteCount === 0 || midiMetadata.contentDuration <= 0) {
    throw new Error(`${block.stableId}: MIDI contains no playable notes`)
  }
  const wavPath = join(outputDirectory, 'audio.wav')
  const mp3Path = join(outputDirectory, 'audio.mp3')
  await run(executables.fluidsynth, [
    '-ni',
    '-g',
    toolchain.audio.gain,
    '-r',
    toolchain.audio.sampleRate,
    '-o',
    'synth.reverb.active=0',
    '-o',
    'synth.chorus.active=0',
    '-F',
    wavPath,
    soundfont,
    midiPath
  ])
  await run(executables.ffmpeg, [
    '-hide_banner',
    '-loglevel',
    'error',
    '-y',
    '-i',
    wavPath,
    '-af',
    'areverse,silenceremove=start_periods=1:start_duration=0.15:start_threshold=-50dB,areverse',
    '-codec:a',
    'libmp3lame',
    '-b:a',
    toolchain.audio.bitrate,
    mp3Path
  ])
  await rm(wavPath, { force: true })
  if (!(await stat(mp3Path)).size) {
    throw new Error(`${block.stableId}: ffmpeg produced an empty MP3 file`)
  }
  const audioDuration = await mediaDuration(mp3Path)
  await assertAudible(mp3Path)
  const minimumDuration = Math.max(0.5, midiMetadata.contentDuration * 0.6)
  if (
    audioDuration < minimumDuration ||
    audioDuration > Math.max(midiMetadata.duration, midiMetadata.contentDuration) + 10
  ) {
    throw new Error(
      `${block.stableId}: audio duration ${audioDuration}s is not compatible with MIDI ` +
        `duration ${midiMetadata.contentDuration}s`
    )
  }
  return {
    noteCount: midiMetadata.noteCount,
    midiDuration: midiMetadata.duration,
    midiContentDuration: midiMetadata.contentDuration,
    audioDuration
  }
}

async function artifactRecord(path, kind, publicName) {
  const info = await stat(path)
  if (!info.isFile() || info.size === 0) {
    throw new Error(`${path}: expected a non-empty ${kind} artifact`)
  }
  return {
    kind,
    name: publicName,
    size: info.size,
    sha256: await digestFile(path)
  }
}

async function existingArtifactsAreUsable(metadata, cacheKey, outputDirectory) {
  if (force || !metadata || metadata.cacheSchema !== cacheSchema) return false
  if (metadata.cacheKey !== cacheKey || metadata.targetVersion !== targetVersion) return false
  for (const artifact of metadata.artifacts || []) {
    const path = join(outputDirectory, artifact.name)
    if (!existsSync(path)) return false
    if ((await stat(path)).size !== artifact.size) return false
    if ((await digestFile(path)) !== artifact.sha256) return false
  }
  return true
}

function cacheKeyFor(block, toolInfo) {
  return digest(
    JSON.stringify({
      generatorVersion,
      targetVersion,
      language: block.language,
      sourceHash: block.hash,
      instrument: requestedInstrument(block),
      tools: toolInfo.versions,
      soundfont: toolInfo.soundfont.sha256,
      audio: toolchain.audio
    })
  )
}

async function validateManifest(blocks) {
  const manifestPath = join(notationRoot, 'manifest.json')
  if (!existsSync(manifestPath)) throw new Error('Notation manifest is missing')
  const manifest = JSON.parse(await readFile(manifestPath, 'utf8'))
  if (manifest.generatorVersion !== generatorVersion) {
    throw new Error('Notation manifest generator version is stale')
  }
  if (manifest.targetVersion !== targetVersion) {
    throw new Error('Notation manifest target version is stale')
  }
  if (manifest.blocks?.length !== blocks.length) {
    throw new Error(
      `Notation manifest has ${manifest.blocks?.length || 0} blocks; expected ${blocks.length}`
    )
  }
  const expected = new Map(blocks.map((block) => [block.hash, block]))
  const seen = new Set()
  for (const item of manifest.blocks) {
    const block = expected.get(item.hash)
    if (!block || seen.has(item.hash)) {
      throw new Error(`Notation manifest has an unknown or duplicate block ${item.hash}`)
    }
    seen.add(item.hash)
    if (item.id !== block.stableId || item.sourcePath !== block.relativePath) {
      throw new Error(`Notation manifest metadata mismatch for ${block.stableId}`)
    }
    for (const artifact of item.artifacts || []) {
      const path = join(root, 'public', artifact.name)
      if (!existsSync(path) || (await digestFile(path)) !== artifact.sha256) {
        throw new Error(`Notation artifact is missing or stale: ${artifact.name}`)
      }
    }
  }
  console.log(`notation manifest validated: ${blocks.length} blocks`)
}

async function main() {
  const blocks = await collectBlocks()
  if (checkOnly) {
    await validateManifest(blocks)
    return
  }
  const toolInfo = await probeTools()
  await mkdir(notationRoot, { recursive: true })
  await mkdir(workRoot, { recursive: true })
  const ids = new Set()
  const manifestBlocks = []

  for (const block of blocks) {
    const assetId = safeAssetId(block.stableId, block.hash)
    if (ids.has(assetId)) throw new Error(`Duplicate notation asset id ${assetId}`)
    ids.add(assetId)
    const outputDirectory = join(notationRoot, assetId)
    await mkdir(outputDirectory, { recursive: true })
    const cacheKey = cacheKeyFor(block, toolInfo)
    const metadataPath = join(outputDirectory, 'metadata.json')
    let metadata = null
    if (existsSync(metadataPath)) {
      try {
        metadata = JSON.parse(await readFile(metadataPath, 'utf8'))
      } catch {}
    }

    if (await existingArtifactsAreUsable(metadata, cacheKey, outputDirectory)) {
      console.log(`reuse ${assetId}`)
    } else {
      for (const name of await readdir(outputDirectory)) {
        await rm(join(outputDirectory, name), { recursive: true, force: true })
      }
      console.log(`compile ${assetId} (${block.relativePath}:${block.line})`)
      const workDirectory = join(workRoot, cacheKey)
      await rm(workDirectory, { recursive: true, force: true })
      await mkdir(workDirectory, { recursive: true })
      try {
        const rendered =
          block.language === 'lilypond'
            ? await renderLilyPond(block, workDirectory, outputDirectory)
            : await renderAbc(block, workDirectory, outputDirectory)
        const instrument = requestedInstrument(block)
        const audio = await renderAudio(
          block,
          rendered.midi,
          outputDirectory,
          instrument
        )
        const sourcePath = join(outputDirectory, rendered.sourceName)
        await writeFile(sourcePath, block.code, 'utf8')
        const artifacts = [
          ...(await Promise.all(
            rendered.svg.map((name) =>
              artifactRecord(join(outputDirectory, name), 'score-svg', name)
            )
          )),
          await artifactRecord(
            join(outputDirectory, 'audio.mp3'),
            'audio-mp3',
            'audio.mp3'
          ),
          await artifactRecord(sourcePath, 'score-source', rendered.sourceName)
        ]
        metadata = {
          schemaVersion: 4,
          cacheSchema,
          generatorVersion,
          cacheKey,
          id: block.stableId,
          title: block.title,
          status: block.status,
          language: block.language,
          sourceHash: block.hash,
          targetVersion,
          sourcePath: block.relativePath,
          line: block.line,
          instrument,
          tools: toolInfo.versions,
          soundfont: toolInfo.soundfont,
          audio: { ...toolchain.audio, ...audio },
          svg: rendered.svg,
          audioFile: 'audio.mp3',
          sourceFile: rendered.sourceName,
          artifacts
        }
        await writeFile(metadataPath, `${JSON.stringify(metadata, null, 2)}\n`, 'utf8')
      } finally {
        await rm(workDirectory, { recursive: true, force: true })
      }
    }

    metadata.title = block.title
    metadata.status = block.status
    await writeFile(metadataPath, `${JSON.stringify(metadata, null, 2)}\n`, 'utf8')
    const url = (name) => `/notation/${assetId}/${name}`
    manifestBlocks.push({
      hash: block.hash,
      id: block.stableId,
      language: block.language,
      status: block.status,
      title: block.title,
      svg: metadata.svg.map(url),
      audio: url(metadata.audioFile),
      source: url(metadata.sourceFile),
      sourcePath: block.relativePath,
      line: block.line,
      instrument: metadata.instrument,
      audioMetadata: metadata.audio,
      artifacts: metadata.artifacts.map((artifact) => ({
        ...artifact,
        name: url(artifact.name)
      }))
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
    schemaVersion: 4,
    generatorVersion,
    targetVersion,
    contentHash: digest(
      blocks.map((block) => `${block.relativePath}\0${block.line}\0${block.hash}`).join('\n')
    ),
    tools: toolInfo.versions,
    soundfont: toolInfo.soundfont,
    audio: toolchain.audio,
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
