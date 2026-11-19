import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import BranchSwitcher from './BranchSwitcher.vue'
import Mermaid from './Mermaid.vue'
import ProvenanceLink from './ProvenanceLink.vue'
import ScoreExample from './ScoreExample.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      // Right of the search box; icon-only on portrait screens.
      'nav-bar-content-after': () => h(BranchSwitcher),
      // Footer link to this article's entry in provenance/.
      'doc-footer-before': () => h(ProvenanceLink)
    })
  },
  enhanceApp({ app }) {
    app.component('Mermaid', Mermaid)
    app.component('ScoreExample', ScoreExample)
  }
} satisfies Theme
