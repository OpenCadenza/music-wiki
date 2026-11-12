<script setup lang="ts">
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import { data } from './texture-cases.data'
import { categoryLabels, caseLocation, tensionLabels } from './texture-cases'

const query = ref('')
const category = ref('')
const meter = ref('')
const tension = ref('')
const meters = [...new Set(data.flatMap(({ form }) => form.cases.map((entry) => entry.meter)))].sort()

const normalize = (value: string) => value.normalize('NFKC').toLowerCase().replace(/[.\s]/g, '')
const results = computed(() => {
  const needle = normalize(query.value)
  return data.flatMap(({ url, form }) => {
    if (category.value && form.category !== category.value) return []
    const matchesForm = normalize([form.topic_name, ...form.aliases].join(' ')).includes(needle)
    const cases = form.cases.filter((entry) =>
      (!meter.value || entry.meter === meter.value) &&
      (!tension.value || entry.tension.level === tension.value) &&
      (matchesForm || normalize([entry.composer, entry.work, entry.section].join(' ')).includes(needle))
    )
    return cases.length ? [{ url, form, cases }] : []
  })
})
const caseCount = computed(() => results.value.reduce((total, item) => total + item.cases.length, 0))

function clearFilters() {
  query.value = category.value = meter.value = tension.value = ''
}
</script>

<template>
  <div class="texture-catalog">
    <div class="texture-filters" role="group" aria-label="案例筛选">
      <label>形式或作品
        <input v-model="query" type="search" placeholder="例如：震音、Op. 53">
      </label>
      <label>类别
        <select v-model="category">
          <option value="">全部</option>
          <option v-for="(label, key) in categoryLabels" :key="key" :value="key">{{ label }}</option>
        </select>
      </label>
      <label>拍号
        <select v-model="meter">
          <option value="">全部</option>
          <option v-for="value in meters" :key="value" :value="value">{{ value }}</option>
        </select>
      </label>
      <label>案例紧张度
        <select v-model="tension">
          <option value="">全部</option>
          <option v-for="(label, key) in tensionLabels" :key="key" :value="key">{{ label }}</option>
        </select>
      </label>
    </div>
    <div class="texture-results-bar">
      <span role="status">{{ results.length }} 种形式 · {{ caseCount }} 条案例</span>
      <button type="button" :disabled="!query && !category && !meter && !tension" @click="clearFilters">清空筛选</button>
    </div>
    <p v-if="!results.length">没有案例符合这些条件。</p>
    <article v-for="{ url, form, cases } in results" :key="form.form_id" class="texture-result">
      <div class="texture-category">{{ categoryLabels[form.category] }}</div>
      <a class="texture-title" :href="withBase(url)">{{ form.topic_name }}｜{{ form.question }}</a>
      <p>{{ form.description }}</p>
      <ul>
        <li v-for="entry in cases" :key="entry.id">
          <a :href="withBase(url) + '#' + entry.id">{{ caseLocation(entry) }}</a>
          <span>{{ entry.meter }} · 紧张度{{ tensionLabels[entry.tension.level] }}</span>
        </li>
      </ul>
    </article>
  </div>
</template>

<style scoped>
.texture-catalog { margin: 1.25rem 0 2rem; }
.texture-filters {
  display: grid;
  grid-template-columns: 2fr repeat(3, 1fr);
  gap: 0.75rem;
  padding: 1rem;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
}
.texture-filters label { display: grid; gap: 0.3rem; font-size: 0.85rem; font-weight: 600; }
.texture-filters input, .texture-filters select {
  min-width: 0;
  width: 100%;
  height: 2.25rem;
  padding: 0 0.5rem;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 4px;
}
.texture-results-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.8rem 0;
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
}
.texture-results-bar button { color: var(--vp-c-brand-1); text-decoration: underline; }
.texture-results-bar button:disabled { opacity: 0.65; color: var(--vp-c-text-2); text-decoration: none; }
.texture-result { padding: 0.85rem 0; border-top: 1px solid var(--vp-c-divider); }
.texture-category { color: var(--vp-c-text-2); font-size: 0.8rem; }
.texture-title { font-size: 1.06rem; font-weight: 650; }
.texture-result p, .texture-result ul { margin: 0.4rem 0; }
.texture-result li span { margin-inline-start: 0.65rem; font-size: 0.8rem; color: var(--vp-c-text-2); }
@media (max-width: 639px) {
  .texture-filters { grid-template-columns: 1fr 1fr; }
}
</style>
