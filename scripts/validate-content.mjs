import { readFile, readdir } from 'node:fs/promises'
import { join, relative, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = resolve(fileURLToPath(new URL('..', import.meta.url)))
const contentRoot = join(root, 'content')
const errors = []

async function walk(directory) {
  const result = []
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name)
    if (entry.isDirectory()) result.push(...(await walk(path)))
    else result.push(path)
  }
  return result
}

for (const path of await walk(contentRoot)) {
  const relativePath = relative(contentRoot, path).split('\\').join('/')
  if (path.endsWith('README.md')) {
    errors.push(`${relativePath}: use index.md for a directory entry page`)
  }
  if (!path.endsWith('.md')) continue
  const text = await readFile(path, 'utf8')
  for (const match of text.matchAll(/^\\version\s+"([^"]+)"/gm)) {
    if (match[1] !== '2.26.0') {
      errors.push(`${relativePath}: LilyPond version ${match[1]} is not 2.26.0`)
    }
  }
}

if (errors.length) {
  console.error(errors.join('\n'))
  process.exitCode = 1
} else {
  console.log('content validation passed')
}
