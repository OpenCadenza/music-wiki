import { existsSync } from 'node:fs'
import { readFile, readdir } from 'node:fs/promises'
import { join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = resolve(fileURLToPath(new URL('..', import.meta.url)))
const distRoot = join(root, 'dist')
const manifestPath = join(root, 'public', 'notation', 'manifest.json')

/** Production base; the development preview overrides it in CI. */
const productionBase = '/music-wiki/'
const base = (() => {
  const configured = (process.env.MUSIC_WIKI_BASE || '').trim()
  if (!configured) return productionBase
  const path = configured.replace(/^\/+|\/+$/g, '')
  return path ? `/${path}/` : '/'
})()

// The main site asserts its known article set. The development preview is built
// from another branch's content, so it asserts whatever that branch declares.
const previewMode = process.env.MUSIC_WIKI_SMOKE === 'preview'

if (!existsSync(manifestPath)) throw new Error('Notation manifest is missing')
if (!existsSync(distRoot)) throw new Error('VitePress output dist/ is missing')

const manifest = JSON.parse(await readFile(manifestPath, 'utf8'))
if (!Number.isInteger(manifest.blocks?.length) || manifest.blocks.length === 0) {
  throw new Error(`Expected at least one notation block, found ${manifest.blocks?.length || 0}`)
}

async function collectHtml(directory) {
  const entries = await readdir(directory, { withFileTypes: true })
  const files = []
  for (const entry of entries) {
    const path = join(directory, entry.name)
    if (entry.isDirectory()) files.push(...(await collectHtml(path)))
    else if (entry.name.endsWith('.html')) files.push(path)
  }
  return files
}

const htmlFiles = await collectHtml(distRoot)
if (htmlFiles.length === 0) throw new Error('VitePress produced no HTML pages')

const mainPages = [
  ['首页', 'index.html', false],
  ['贝多芬', 'composers/beethoven/index.html', false],
  ['奏鸣曲目录', 'composers/beethoven/piano/sonatas/index.html', false],
  ['开头', 'composers/beethoven/piano/sonatas/opening-gestures.html', true],
  ['动机', 'composers/beethoven/piano/sonatas/motive-tasks.html', true],
  ['横向主调织体案例库', 'texture/index.html', false]
]

if (previewMode) {
  if (!existsSync(join(distRoot, 'index.html'))) throw new Error('preview: missing index.html')
  for (const block of manifest.blocks) {
    const page = block.sourcePath.replace(/\.md$/, '.html')
    if (!existsSync(join(distRoot, page))) {
      throw new Error(`${block.id}: declared page ${page} was not built`)
    }
  }
} else {
  for (const [name, relativePath, expectScore] of mainPages) {
    const path = join(distRoot, relativePath)
    if (!existsSync(path)) throw new Error(`${name}: missing built page ${relativePath}`)
    const html = await readFile(path, 'utf8')
    if (expectScore && !html.includes('score-example')) {
      throw new Error(`${name}: rendered page has no score player`)
    }
  }
}

for (const file of htmlFiles) {
  const html = await readFile(file, 'utf8')
  const name = file.slice(distRoot.length)
  if (html.includes('<ScoreExample')) {
    throw new Error(`${name}: ScoreExample component was not rendered`)
  }
  if (html.includes('score-example') && !html.includes(`${base}notation/`)) {
    throw new Error(`${name}: notation URL does not include the Pages base path ${base}`)
  }
}

const homeHtml = await readFile(join(distRoot, 'index.html'), 'utf8')
if (!homeHtml.includes(`${base}assets/`)) {
  throw new Error(`首页: asset URLs do not include the Pages base path ${base}`)
}

const textureCatalogPath = join(distRoot, 'texture', 'index.html')
if (!previewMode || existsSync(textureCatalogPath)) {
  if (!existsSync(textureCatalogPath)) throw new Error('missing texture catalog page')
  const textureCatalog = await readFile(textureCatalogPath, 'utf8')
  for (const block of manifest.blocks) {
    if (!block.sourcePath?.startsWith('texture/')) continue
    const page = block.sourcePath.replace(/\.md$/, '.html')
    const html = await readFile(join(distRoot, page), 'utf8')
    if (!html.includes(`data-score-id="${block.id}"`) ||
        !html.includes(`id="${block.id}" class="texture-facts"`) ||
        !textureCatalog.includes(`${base}${page}#${block.id}"`)) {
      throw new Error(`${block.id}: missing score player, case facts or catalog link`)
    }
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
    const relative = artifact.name.startsWith(base)
      ? artifact.name.slice(base.length)
      : artifact.name
    const distPath = join(distRoot, ...relative.split('/'))
    if (!existsSync(distPath)) {
      throw new Error(`${block.id}: ${artifact.kind} was not copied to dist`)
    }
  }
}

console.log(
  `site smoke test passed: ${htmlFiles.length} pages, ${manifest.blocks.length} score blocks, base ${base}`
)
