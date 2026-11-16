import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import BranchSwitcher from './BranchSwitcher.vue'
import ScoreExample from './ScoreExample.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // Right of the search box on desktop and tablet.
      'nav-bar-content-after': () => h(BranchSwitcher, { variant: 'navbar' }),
      // Mobile navigation screen, because the navbar has no room for it.
      'nav-screen-content-before': () => h(BranchSwitcher, { variant: 'screen' })
    })
  },
  enhanceApp({ app }) {
    app.component('ScoreExample', ScoreExample)
  }
} satisfies Theme
