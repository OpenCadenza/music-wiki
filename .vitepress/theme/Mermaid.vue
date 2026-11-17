<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useData } from 'vitepress'

const props = defineProps<{ code: string }>()

const { isDark } = useData()

const host = ref<HTMLElement | null>(null)
const copied = ref(false)

let instanceSeq = 0
let copyTimer: ReturnType<typeof setTimeout> | undefined
let renderedOnce = false

// Must match the site font stack literally: mermaid measures label widths with
// this stack, and a CSS variable resolves to the fallback font in its detached
// measuring element, which produced boxes smaller than the painted text.
const fontStack =
  '"Inter", "Noto Sans SC", "Source Han Sans SC", "Microsoft YaHei", sans-serif'

/** Mermaid keys its styles and temporary DOM by id, so every render needs a unique one. */
function nextRenderId() {
  instanceSeq += 1
  return `mermaid-${Date.now().toString(36)}-${instanceSeq}-${Math.random()
    .toString(36)
    .slice(2, 7)}`
}

function escapeHtml(text: string) {
  return text
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
}

function showFallback() {
  if (!host.value) return
  host.value.innerHTML = `<pre class="mermaid-fallback">${escapeHtml(props.code)}</pre>`
}

function fitViewBox(svgEl: SVGSVGElement) {
  const box = svgEl.viewBox.baseVal
  let minX = box.x
  let minY = box.y
  let maxX = box.x + box.width
  let maxY = box.y + box.height
  try {
    const content = svgEl.getBBox()
    minX = Math.min(minX, content.x)
    minY = Math.min(minY, content.y)
    maxX = Math.max(maxX, content.x + content.width)
    maxY = Math.max(maxY, content.y + content.height)
  } catch {
    // getBBox can fail on detached/hidden SVG; the mermaid viewBox still works.
  }
  const pad = 4
  minX -= pad
  minY -= pad
  maxX += pad
  maxY += pad
  svgEl.setAttribute('viewBox', `${minX} ${minY} ${maxX - minX} ${maxY - minY}`)
  svgEl.setAttribute('width', String(Math.ceil(maxX - minX)))
  svgEl.setAttribute('height', String(Math.ceil(maxY - minY)))
}

async function renderDiagram() {
  if (!host.value) return
  try {
    const mermaid = (await import('mermaid')).default
    // Wait for webfonts before mermaid measures label sizes.
    await document.fonts.ready
    mermaid.initialize({
      startOnLoad: false,
      securityLevel: 'strict',
      // Natural size; the block scrolls horizontally when wider than the column.
      useMaxWidth: false,
      theme: isDark.value ? 'dark' : 'default',
      themeVariables: {
        fontSize: '15px',
        actorFontSize: '15px',
        messageFontSize: '15px',
        fontFamily: fontStack,
        // Opaque background so long edge labels do not let arrows show through.
        edgeLabelBackground: isDark.value ? '#1b1b1f' : '#ffffff'
      },
      flowchart: {
        htmlLabels: true,
        nodeSpacing: 40,
        rankSpacing: 64,
        padding: 8
      }
    })
    const { svg } = await mermaid.render(nextRenderId(), props.code)
    if (!host.value) return
    host.value.innerHTML = svg
    const svgEl = host.value.querySelector('svg')
    if (svgEl) {
      svgEl.removeAttribute('style')
      fitViewBox(svgEl as SVGSVGElement)
    }
    renderedOnce = true
  } catch (error) {
    console.error('mermaid render failed:', error)
    showFallback()
  }
}

async function copySource() {
  try {
    await navigator.clipboard.writeText(props.code)
    copied.value = true
    if (copyTimer) clearTimeout(copyTimer)
    copyTimer = setTimeout(() => {
      copied.value = false
    }, 1600)
  } catch (error) {
    console.error('mermaid copy failed:', error)
  }
}

onMounted(async () => {
  showFallback()
  await renderDiagram()
  // A font that finishes loading after the first pass changes label widths.
  if (!renderedOnce) return
  if (document.fonts?.addEventListener) {
    document.fonts.addEventListener(
      'loadingdone',
      () => void renderDiagram(),
      { once: true }
    )
  }
})

watch(isDark, () => void renderDiagram())
watch(() => props.code, () => void renderDiagram())

onBeforeUnmount(() => {
  if (copyTimer) clearTimeout(copyTimer)
  if (host.value) host.value.innerHTML = ''
})
</script>

<template>
  <figure class="mermaid-block">
    <figcaption class="mermaid-header">
      <span class="mermaid-lang">mermaid</span>
      <button
        class="mermaid-copy"
        type="button"
        :aria-label="copied ? '已复制 Mermaid 源码' : '复制 Mermaid 源码'"
        @click="copySource"
      >
        {{ copied ? '已复制' : '复制' }}
      </button>
    </figcaption>
    <div ref="host" class="mermaid-scroll" role="img" aria-label="Mermaid 图" tabindex="0"></div>
  </figure>
</template>

<style scoped>
.mermaid-block {
  margin: 16px 0;
  border-radius: 8px;
  background-color: var(--vp-code-block-bg);
  overflow: hidden;
}

.mermaid-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px 0 16px;
  font-size: 12px;
  line-height: 20px;
  color: var(--vp-c-text-2);
}

.mermaid-lang {
  font-family: var(--vp-font-family-mono);
}

.mermaid-copy {
  padding: 2px 8px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  font-family: inherit;
  font-size: 12px;
  line-height: 18px;
  cursor: pointer;
  transition:
    color 0.2s,
    border-color 0.2s;
}

.mermaid-copy:hover {
  color: var(--vp-c-text-1);
  border-color: var(--vp-c-brand-1);
}

.mermaid-scroll {
  padding: 8px 16px 12px;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--vp-c-divider) transparent;
}

.mermaid-scroll::-webkit-scrollbar {
  height: 10px;
}

.mermaid-scroll::-webkit-scrollbar-track {
  background: transparent;
}

.mermaid-scroll::-webkit-scrollbar-thumb {
  background: var(--vp-c-divider);
  border: 2px solid transparent;
  border-radius: 5px;
  background-clip: content-box;
}

.mermaid-scroll :deep(svg) {
  display: block;
  margin: 0 auto;
  max-width: none;
  height: auto;
}

/* VitePress styles every <p> inside .vp-doc (line-height 28px, vertical
   margins), and mermaid labels are <p> inside foreignObject. Those styles make
   rendered labels taller than mermaid measured them, which clips the text, so
   restore mermaid's own metrics inside diagrams. */
.mermaid-scroll :deep(foreignObject p) {
  margin: 0;
  padding: 0;
  font-size: inherit;
  line-height: 1.5;
}

.mermaid-fallback {
  margin: 0;
  padding: 0;
  color: var(--vp-c-text-2);
  font-family: var(--vp-font-mono);
  font-size: 12px;
  overflow: auto;
}
</style>