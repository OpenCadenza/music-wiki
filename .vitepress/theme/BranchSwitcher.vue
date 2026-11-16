<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import branches from '../../branches.json'

type BranchEntry = { label: string; branch: string; slug: string }

const base = import.meta.env.BASE_URL
// "/music-wiki/dev/<slug>/" -> "/music-wiki/"
const siteRoot = base.replace(/dev\/[^/]+\/$/, '')

const entries = (branches as BranchEntry[]).map((entry) => ({
  label: entry.label,
  url: entry.slug ? `${siteRoot}dev/${entry.slug}/` : siteRoot
}))

const currentUrl = entries.find((entry) => entry.url === base)?.url ?? siteRoot
const currentLabel = computed(
  () => entries.find((entry) => entry.url === currentUrl)?.label ?? '分支'
)

const open = ref(false)
const rootEl = ref<HTMLElement | null>(null)

function onDocumentClick(event: MouseEvent) {
  if (rootEl.value && !rootEl.value.contains(event.target as Node)) open.value = false
}

function onKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape') open.value = false
}

onMounted(() => {
  document.addEventListener('click', onDocumentClick)
  document.addEventListener('keydown', onKeydown)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', onDocumentClick)
  document.removeEventListener('keydown', onKeydown)
})

function toggle() {
  open.value = !open.value
}

function choose(url: string) {
  open.value = false
  if (url !== base) window.location.href = url
}
</script>

<template>
  <div ref="rootEl" class="branch-switcher">
    <button
      type="button"
      class="branch-switcher-trigger"
      :aria-expanded="open"
      aria-haspopup="listbox"
      :title="`切换分支站点（当前：${currentLabel}）`"
      @click="toggle"
    >
      <svg class="branch-switcher-icon" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true">
        <g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round">
          <circle cx="4" cy="3.6" r="1.5" />
          <circle cx="4" cy="12.4" r="1.5" />
          <circle cx="12" cy="5.2" r="1.5" />
          <path d="M4 5.1v5.8" />
          <path d="M10.5 5.4c0 2.2-1.6 2.9-4.2 3.6" />
        </g>
      </svg>
      <span class="branch-switcher-label">{{ currentLabel }}</span>
      <span class="branch-switcher-caret" aria-hidden="true"></span>
    </button>

    <div v-if="open" class="branch-switcher-menu" role="listbox">
      <button
        v-for="entry in entries"
        :key="entry.url"
        type="button"
        class="branch-switcher-item"
        :class="{ active: entry.url === currentUrl }"
        role="option"
        :aria-selected="entry.url === currentUrl"
        @click="choose(entry.url)"
      >
        {{ entry.label }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.branch-switcher {
  position: relative;
  flex-shrink: 0;
}

.branch-switcher-trigger {
  display: flex;
  align-items: center;
  gap: 6px;
  height: 40px;
  padding: 0 8px 0 10px;
  border: 1px solid transparent;
  border-radius: 8px;
  background-color: var(--vp-c-bg-alt);
  color: var(--vp-c-text-2);
  font-family: inherit;
  cursor: pointer;
  transition: border-color 0.25s;
}

.branch-switcher-trigger:hover,
.branch-switcher-trigger:focus-visible,
.branch-switcher-trigger[aria-expanded='true'] {
  border-color: var(--vp-c-brand-1);
  outline: none;
}

.branch-switcher-icon {
  flex-shrink: 0;
}

.branch-switcher-label {
  font-size: 13px;
  font-weight: 500;
  line-height: 20px;
  color: var(--vp-c-text-1);
  transition: color 0.25s;
}

.branch-switcher-caret {
  width: 6px;
  height: 6px;
  border-right: 1.5px solid var(--vp-c-text-2);
  border-bottom: 1.5px solid var(--vp-c-text-2);
  transform: rotate(45deg) translateY(-2px);
}

.branch-switcher-menu {
  position: absolute;
  top: calc(100% + 6px);
  right: 0;
  z-index: 60;
  min-width: 150px;
  max-height: 60vh;
  overflow-y: auto;
  padding: 6px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background-color: var(--vp-c-bg-elv);
  box-shadow: var(--vp-shadow-3);
}

.branch-switcher-item {
  display: block;
  width: 100%;
  border: 0;
  border-radius: 6px;
  padding: 0 12px;
  line-height: 32px;
  font-size: 14px;
  font-weight: 500;
  text-align: left;
  color: var(--vp-c-text-1);
  background-color: transparent;
  white-space: nowrap;
  cursor: pointer;
  transition:
    background-color 0.25s,
    color 0.25s;
}

.branch-switcher-item:hover {
  color: var(--vp-c-brand-1);
  background-color: var(--vp-c-default-soft);
}

.branch-switcher-item.active {
  color: var(--vp-c-brand-1);
}

.branch-switcher-item.active::after {
  content: '';
  display: inline-block;
  margin-left: 12px;
  width: 10px;
  height: 6px;
  border-left: 2px solid currentColor;
  border-bottom: 2px solid currentColor;
  transform: rotate(-45deg) translateY(-1px);
}

@media (max-width: 767px) {
  .branch-switcher-trigger {
    width: 40px;
    padding: 0;
    justify-content: center;
  }

  .branch-switcher-label,
  .branch-switcher-caret {
    display: none;
  }
}
</style>

<!-- Placed right after the search box, before the nav menu. -->
<style>
.VPNavBar .content-body > .search {
  order: 1;
  flex-grow: 0;
}

.VPNavBar .content-body > .branch-switcher {
  order: 2;
  margin-left: 8px;
}

.VPNavBar .content-body > .menu {
  order: 3;
  margin-left: auto;
}

.VPNavBar .content-body > .translations {
  order: 4;
}

.VPNavBar .content-body > .appearance {
  order: 5;
}

.VPNavBar .content-body > .social-links {
  order: 6;
}

.VPNavBar .content-body > .extra {
  order: 7;
}

.VPNavBar .content-body > .hamburger {
  order: 8;
}
</style>