import { createContentLoader } from 'vitepress'
import type { TextureForm } from './texture-cases'

interface FormPage {
  url: string
  form: TextureForm
}

declare const data: FormPage[]
export { data }

export default createContentLoader('texture/*.md', {
  transform(pages) {
    return pages
      .filter(({ frontmatter }) => frontmatter.kind === 'form')
      .map(({ url, frontmatter }) => ({ url, form: frontmatter as TextureForm }))
  }
})
