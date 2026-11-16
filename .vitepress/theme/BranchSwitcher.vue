<script setup lang="ts">
import branches from '../../branches.json'

type BranchEntry = { label: string; branch: string; slug: string }

const base = import.meta.env.BASE_URL
// "/music-wiki/dev/<slug>/" -> "/music-wiki/"
const siteRoot = base.replace(/dev\/[^/]+\/$/, '')

const entries = (branches as BranchEntry[]).map((entry) => ({
  label: entry.label,
  url: entry.slug ? `${siteRoot}dev/${entry.slug}/` : siteRoot
}))

const current = entries.find((entry) => entry.url === base)?.url ?? entries[0]?.url ?? siteRoot

function onChange(event: Event) {
  const url = (event.target as HTMLSelectElement).value
  if (url && url !== base) window.location.href = url
}
</script>

<template>
  <label class="branch-switcher" title="切换分支站点">
    <span class="branch-switcher-label">分支</span>
    <select
      class="branch-switcher-select"
      aria-label="切换分支站点"
      :value="current"
      @change="onChange"
    >
      <option
        v-for="entry in entries"
        :key="entry.url"
        :value="entry.url"
        :selected="entry.url === current"
      >
        {{ entry.label }}
      </option>
    </select>
  </label>
</template>

<style scoped>
.branch-switcher {
  display: flex;
  align-items: center;
  gap: 6px;
  margin: 0 4px 0 12px;
}

.branch-switcher-label {
  font-size: 12px;
  color: var(--vp-c-text-2);
  white-space: nowrap;
}

.branch-switcher-select {
  appearance: none;
  -webkit-appearance: none;
  padding: 3px 22px 3px 8px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background-color: transparent;
  background-image:
    linear-gradient(45deg, transparent 50%, var(--vp-c-text-2) 50%),
    linear-gradient(135deg, var(--vp-c-text-2) 50%, transparent 50%);
  background-position:
    calc(100% - 12px) calc(50% - 1px),
    calc(100% - 8px) calc(50% - 1px);
  background-size: 4px 4px, 4px 4px;
  background-repeat: no-repeat;
  color: var(--vp-c-text-1);
  font-size: 12px;
  line-height: 20px;
  cursor: pointer;
  transition: border-color 0.2s;
}

.branch-switcher-select:hover,
.branch-switcher-select:focus-visible {
  border-color: var(--vp-c-brand-1);
  outline: none;
}

.branch-switcher-select option {
  color: var(--vp-c-text-1);
  background-color: var(--vp-c-bg);
}

@media (max-width: 768px) {
  .branch-switcher {
    margin-left: 8px;
  }

  .branch-switcher-label {
    display: none;
  }

  .branch-switcher-select {
    max-width: 122px;
  }
}
</style>
