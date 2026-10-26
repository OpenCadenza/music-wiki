import { existsSync } from 'node:fs'
import { readFile } from 'node:fs/promises'
import { join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = resolve(fileURLToPath(new URL('..', import.meta.url)))
const distRoot = join(root, 'dist')
const manifestPath = join(root, 'public', 'notation', 'manifest.json')

if (!existsSync(manifestPath)) throw new Error('Notation manifest is missing')
if (!existsSync(distRoot)) throw new Error('VitePress output dist/ is missing')

const manifest = JSON.parse(await readFile(manifestPath, 'utf8'))
if (manifest.blocks?.length !== 66) {
  throw new Error(`Expected 66 notation blocks, found ${manifest.blocks?.length || 0}`)
}

const pages = [
  ['首页', 'index.html', false],
  ['贝多芬', 'composers/beethoven/index.html', false],
  ['Op.110', 'composers/beethoven/piano/sonatas/op110-fugue.html', true],
  ['Op.74', 'composers/beethoven/chamber/quartets/op74-model-reinterpretation.html', true],
  ['Op.127/132', 'composers/beethoven/chamber/quartets/op127-op132-return-meter.html', true],
  ['ABC', 'abc.html', true]
]

for (const [name, relativePath, expectScore] of pages) {
  const path = join(distRoot, relativePath)
  if (!existsSync(path)) throw new Error(`${name}: missing built page ${relativePath}`)
  const html = await readFile(path, 'utf8')
  if (html.includes('<ScoreExample')) {
    throw new Error(`${name}: ScoreExample component was not rendered`)
  }
  if (expectScore && !html.includes('score-example')) {
    throw new Error(`${name}: rendered page has no score player`)
  }
  if (expectScore && !html.includes('/music-wiki/notation/')) {
    throw new Error(`${name}: notation URL does not include the Pages base path`)
  }
}

for (const block of manifest.blocks) {
  const artifacts =
    block.artifacts ||
    [...block.svg, block.audio, block.source].map((name) => ({
      name,
      kind: 'legacy-manifest'
    }))
  for (const artifact of artifacts) {
    const distPath = join(distRoot, ...artifact.name.replace(/^\/music-wiki\//, '').split('/'))
    if (!existsSync(distPath)) {
      throw new Error(`${block.id}: ${artifact.kind} was not copied to dist`)
    }
  }
}

console.log(
  `site smoke test passed: ${pages.length} representative pages, ${manifest.blocks.length} score blocks`
)
