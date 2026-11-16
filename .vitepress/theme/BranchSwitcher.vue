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
    <svg
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
  height: 40px;
  padding: 0 8px 0 10px;
  border: 1px solid transparent;
  border-radius: 8px;
  background-color: var(--vp-c-bg-alt);
  cursor: pointer;
  transition: border-color 0.25s;
}

.branch-switcher:hover,
.branch-switcher:focus-within {
  border-color: var(--vp-c-brand-1);
}

.branch-switcher-icon {
  flex-shrink: 0;
  color: var(--vp-c-text-2);
  transition: color 0.25s;
}

.branch-switcher:hover .branch-switcher-icon,
.branch-switcher:focus-within .branch-switcher-icon {
  color: var(--vp-c-text-1);
}

.branch-switcher-select {
  appearance: none;
  -webkit-appearance: none;
  padding: 0 16px 0 0;
  border: none;
  background-color: transparent;
  background-image:
    linear-gradient(45deg, transparent 50%, var(--vp-c-text-2) 50%),
    linear-gradient(135deg, var(--vp-c-text-2) 50%, transparent 50%);
  background-position:
    calc(100% - 5px) calc(50% - 1px),
    calc(100% - 1px) calc(50% - 1px);
  background-size: 4px 4px, 4px 4px;
  background-repeat: no-repeat;
  color: var(--vp-c-text-2);
  font-family: inherit;
  font-size: 13px;
  font-weight: 500;
  line-height: 20px;
  cursor: pointer;
  transition: color 0.25s;
}

.branch-switcher:hover .branch-switcher-select,
.branch-switcher:focus-within .branch-switcher-select {
  color: var(--vp-c-text-1);
}

.branch-switcher-select:focus {
  outline: none;
}

.branch-switcher-select option {
  color: var(--vp-c-text-1);
  background-color: var(--vp-c-bg);
}

@media (max-width: 767px) {
  .branch-switcher {
    height: 34px;
    padding: 0 6px 0 8px;
    gap: 4px;
  }

  .branch-switcher-select {
    max-width: 96px;
    font-size: 12px;
  }
}
</style>

<!-- Placed right after the search box, before the nav menu. -->
<style>
.VPNavBar .content-body > .search {
  order: 1;
}

.VPNavBar .content-body > .branch-switcher {
  order: 2;
  margin-left: 12px;
}

.VPNavBar .content-body > .menu {
  order: 3;
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

@media (max-width: 767px) {
  .VPNavBar .content-body > .branch-switcher {
    margin-left: 8px;
  }
}
</style>
