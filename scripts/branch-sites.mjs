// Validate branches.json and print the development branches as a JSON array,
// which the deploy workflow feeds straight into its build matrix.
import { readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const entries = JSON.parse(readFileSync(resolve(root, 'branches.json'), 'utf8'))

if (!Array.isArray(entries) || entries.length === 0) {
  throw new Error('branches.json must be a non-empty array')
}
if (!entries.some((entry) => !entry.slug)) {
  throw new Error('branches.json needs one entry without a slug for the main site')
}

const seen = new Set()
const dev = []
for (const entry of entries) {
  if (typeof entry.label !== 'string' || entry.label.trim() === '') {
    throw new Error(`branches.json: every entry needs a label (${JSON.stringify(entry)})`)
  }
  if (typeof entry.branch !== 'string' || entry.branch.trim() === '') {
    throw new Error(`branches.json: ${entry.label} needs a branch name`)
  }
  if (typeof entry.slug !== 'string') {
    throw new Error(`branches.json: ${entry.label} needs a slug (empty for the main site)`)
  }
  if (!entry.slug) continue
  if (!/^[a-z0-9][a-z0-9-]*$/.test(entry.slug)) {
    throw new Error(
      `branches.json: slug "${entry.slug}" must be lowercase letters, digits or hyphens`
    )
  }
  if (seen.has(entry.slug)) {
    throw new Error(`branches.json: duplicate slug "${entry.slug}"`)
  }
  seen.add(entry.slug)
  dev.push({ label: entry.label, branch: entry.branch, slug: entry.slug })
}

console.log(JSON.stringify(dev))
