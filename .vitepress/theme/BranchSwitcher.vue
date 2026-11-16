<script setup lang="ts">
import branches from '../../branches.json'

type BranchEntry = { label: string; branch: string; slug: string }

withDefaults(defineProps<{ variant?: 'navbar' | 'screen' }>(), { variant: 'navbar' })

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
  <label class="branch-switcher" :class="`branch-switcher--${variant}`" title="切换分支站点">
    <svg
      v-if="variant === 'navbar'"
      class="branch-switcher-icon"
      viewBox="0 0 16 16"
      width="14"
      height="14"
      aria-hidden="true"
    >
      <g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round">
        <circle cx="4" cy="3.6" r="1.5" />
        <circle cx="4" cy="12.4" r="1.5" />
        <circle cx="12" cy="5.2" r="1.5" />
        <path d="M4 5.1v5.8" />
        <path d="M10.5 5.4c0 2.2-1.6 2.9-4.2 3.6" />
      </g>
    </svg>
    <span v-else class="branch-switcher-label">分支</span>
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
  flex-shrink: 0;
  gap: 6px;
}

.branch-switcher--navbar {
  height: 40px;
  padding: 0 8px 0 10px;
  border: 1px solid transparent;
  border-radius: 8px;
  background-color: var(--vp-c-bg-alt);
  cursor: pointer;
  transition: border-color 0.25s;
}

.branch-switcher--navbar:hover,
.branch-switcher--navbar:focus-within {
  border-color: var(--vp-c-brand-1);
}

.branch-switcher-icon {
  flex-shrink: 0;
  color: var(--vp-c-text-2);
  transition: color 0.25s;
}

.branch-switcher--navbar:hover .branch-switcher-icon,
.branch-switcher--navbar:focus-within .branch-switcher-icon {
  color: var(--vp-c-text-1);
}

.branch-switcher-select {
  appearance: none;
  -webkit-appearance: none;
  border: none;
  border-radius: 0;
  background-color: transparent;
  background-image:
    linear-gradient(45deg, transparent 50%, var(--vp-c-text-2) 50%),
    linear-gradient(135deg, var(--vp-c-text-2) 50%, transparent 50%);
  background-repeat: no-repeat;
  font-family: inherit;
  cursor: pointer;
}

.branch-switcher-select:focus {
  outline: none;
}

.branch-switcher-select option {
  color: var(--vp-c-text-1);
  background-color: var(--vp-c-bg);
}

.branch-switcher--navbar .branch-switcher-select {
  padding: 0 16px 0 0;
  background-position:
    calc(100% - 5px) calc(50% - 1px),
    calc(100% - 1px) calc(50% - 1px);
  background-size: 4px 4px, 4px 4px;
  color: var(--vp-c-text-2);
  font-size: 13px;
  font-weight: 500;
  line-height: 20px;
  transition: color 0.25s;
}

.branch-switcher--navbar:hover .branch-switcher-select,
.branch-switcher--navbar:focus-within .branch-switcher-select {
  color: var(--vp-c-text-1);
}

.branch-switcher--screen {
  margin: 12px 24px 4px;
  padding: 0;
}

.branch-switcher--screen .branch-switcher-label {
  flex-shrink: 0;
  font-size: 13px;
  color: var(--vp-c-text-2);
}

.branch-switcher--screen .branch-switcher-select {
  flex-grow: 1;
  height: 40px;
  padding: 0 28px 0 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background-color: var(--vp-c-bg-alt);
  background-position:
    calc(100% - 16px) calc(50% - 1px),
    calc(100% - 12px) calc(50% - 1px);
  background-size: 4px 4px, 4px 4px;
  color: var(--vp-c-text-1);
  font-size: 14px;
}

@media (max-width: 767px) {
  .branch-switcher--navbar {
    display: none;
  }
}

@media (min-width: 768px) {
  .branch-switcher--screen {
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
