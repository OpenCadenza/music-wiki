import { defineConfig } from 'vitepress'
import { withSidebar } from 'vitepress-sidebar'
import { createHash } from 'node:crypto'
import { existsSync, readFileSync } from 'node:fs'
import { resolve } from 'node:path'
import MarkdownIt from 'markdown-it'

const manifestPath = resolve('public/notation/manifest.json')

type NotationBlock = {
  hash: string
  id: string
  language: 'abc' | 'lilypond'
  status: 'published' | 'draft'
  title: string
  svg: string[]
  audio: string
  source: string
}

function readManifest(): Map<string, NotationBlock> {
  if (!existsSync(manifestPath)) {
    throw new Error('Notation manifest is missing. Run `pnpm notation` first.')
  }

  const manifest = JSON.parse(readFileSync(manifestPath, 'utf8')) as {
    blocks: NotationBlock[]
  }
  return new Map(manifest.blocks.map((block) => [block.hash, block]))
}

function escapeAttribute(value: string) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('"', '&quot;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
}

function notationMarkdownPlugin(md: MarkdownIt) {
  const manifest = readManifest()
  const defaultFence = md.renderer.rules.fence

  md.renderer.rules.fence = (tokens, index, options, env, self) => {
    const token = tokens[index]
    const language = token.info.trim().split(/\s+/, 1)[0].toLowerCase()
    if (!['abc', 'lilypond', 'ly'].includes(language)) {
      return defaultFence(tokens, index, options, env, self)
    }

    const hash = createHash('sha256').update(token.content).digest('hex')
    const block = manifest.get(hash)
    if (!block) {
      throw new Error(`Notation manifest does not contain ${language} block ${hash}`)
    }

    const attributes = {
      id: block.id,
      title: block.title,
      language: block.language,
      status: block.status || 'published',
      svg: block.svg.join('|'),
      audio: block.audio,
      source: block.source
    }
    const renderedAttributes = Object.entries(attributes)
      .map(([name, value]) => `${name}="${escapeAttribute(value)}"`)
      .join(' ')
    return `<ScoreExample ${renderedAttributes} />\n`
  }
}

const siteConfig = {
  title: '音乐知识库',
  titleTemplate: ':title | 音乐知识库',
  description: '面向音乐创作任务的作曲、乐理与 ABC/LilyPond 谱例知识库',
  lang: 'zh-CN',
  base: '/music-wiki/',
  srcDir: 'content',
  publicDir: 'public',
  outDir: 'dist',
  cleanUrls: false,
  appearance: false,
  lastUpdated: true,
  head: [
    ['meta', { name: 'theme-color', content: '#f5f1ec' }],
    ['link', { rel: 'icon', href: '/music-wiki/favicon.svg' }]
  ],
  markdown: {
    config: notationMarkdownPlugin,
    lineNumbers: true,
    theme: 'github-light'
  },
  themeConfig: {
    logo: '/logo.svg',
    siteTitle: '音乐知识库',
    outline: {
      level: [2, 3],
      label: '本页目录'
    },
    nav: [
      { text: '按任务查资料', link: '/' },
      { text: '作曲家', link: '/composers/' },
      { text: '贝多芬', link: '/composers/beethoven/' },
      { text: '来源与许可', link: '/knowledge/' }
    ],
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索',
            buttonAriaLabel: '搜索知识库'
          },
          modal: {
            displayDetails: '显示详细列表',
            resetButtonTitle: '清除搜索',
            backButtonTitle: '关闭搜索',
            noResultsText: '没有找到相关内容',
            footer: {
              selectText: '选择',
              navigateText: '切换',
              closeText: '关闭'
            }
          }
        }
      }
    },
    docFooter: {
      prev: '上一页',
      next: '下一页'
    },
    lastUpdated: {
      text: '最后更新'
    },
    sidebarMenuLabel: '知识树',
    returnToTopLabel: '回到顶部',
    socialLinks: [
      {
        icon: 'github',
        link: 'https://github.com/OpenCadenza/music-wiki'
      }
    ],
    footer: {
      message: '面向创作任务的音乐知识库',
      copyright: '来源许可与引用边界见来源登记表'
    }
  }
}

export default defineConfig(
  withSidebar(siteConfig, {
    documentRootPath: 'content',
    collapsed: true,
    collapseDepth: 1,
    collapseFromLevel: 1,
    useTitleFromFileHeading: true,
    useFolderTitleFromIndexFile: true,
    useFolderLinkFromIndexFile: true,
    includeRootIndexFile: false,
    includeFolderIndexFile: false,
    excludeByGlobPattern: ['**/_maintenance/**', '**/README.md'],
    hyphenToSpace: true,
    underscoreToSpace: true,
    sortFolderTo: 'top',
    sortMenusByName: true,
    manualSortFileNameByPriority: ['index.md'],
    debugPrint: false
  })
)
