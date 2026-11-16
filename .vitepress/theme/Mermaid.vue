<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useData } from 'vitepress'

const props = defineProps<{ code: string }>()

const { isDark } = useData()

const host = ref<HTMLElement | null>(null)
const copied = ref(false)

let instanceSeq = 0
let copyTimer: ReturnType<typeof setTimeout> | undefined

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

async function renderDiagram() {
  if (!host.value) return
  try {
    const mermaid = (await import('mermaid')).default
    mermaid.initialize({
      startOnLoad: false,
      securityLevel: 'strict',
      // Keep each diagram at its natural size; the block scrolls horizontally
      // when a figure is wider than the content area, like a code block. Tall
      // figures are not clipped: the page scrolls, as it does for code.
      useMaxWidth: false,
      theme: isDark.value ? 'dark' : 'default',
      themeVariables: {
        fontSize: '15px',
        actorFontSize: '15px',
        messageFontSize: '15px',
        fontFamily: 'var(--vp-font-family-base)'
      }
    })
    const { svg } = await mermaid.render(nextRenderId(), props.code)
    if (host.value) {
      host.value.innerHTML = svg
      // Pin each SVG to its natural size (from the viewBox) so figures keep
      // their own proportions instead of collapsing to the container width.
      const svgEl = host.value.querySelector('svg')
      if (svgEl) {
        const box = svgEl.viewBox?.baseVal
        if (box && box.width > 0 && box.height > 0) {
          svgEl.removeAttribute('style')
          svgEl.setAttribute('width', String(box.width))
          svgEl.setAttribute('height', String(box.height))
        }
      }
    }
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

onMounted(() => {
  showFallback()
  void renderDiagram()
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
  font-family: var(--vp-font-family-base);
}

.mermaid-scroll :deep(.nodeLabel),
.mermaid-scroll :deep(.edgeLabel) {
  font-family: var(--vp-font-family-base);
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