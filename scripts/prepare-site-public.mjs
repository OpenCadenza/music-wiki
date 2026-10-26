import { cp, mkdir, rm } from 'node:fs/promises'
import { join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = resolve(fileURLToPath(new URL('..', import.meta.url)))
const source = join(root, 'public')
const contentRoot = join(root, 'content')
const target = join(contentRoot, 'public')
const contentPrefix = `${resolve(contentRoot)}${process.platform === 'win32' ? '\\' : '/'}`

if (!resolve(target).startsWith(contentPrefix)) {
  throw new Error(`Refusing to write outside content root: ${target}`)
}

await rm(target, { recursive: true, force: true })
await mkdir(target, { recursive: true })
await cp(source, target, { recursive: true })
console.log('prepared content/public for VitePress')
