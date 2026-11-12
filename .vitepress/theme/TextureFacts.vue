<script setup lang="ts">
import { computed } from 'vue'
import { useData } from 'vitepress'
import { categoryLabels, caseLocation, tensionLabels } from './texture-cases'
import type { TextureForm } from './texture-cases'

const props = defineProps<{ caseId?: string }>()
const { frontmatter } = useData<TextureForm>()
const form = computed(() => frontmatter.value)
const entry = computed(() => form.value.cases?.find((item) => item.id === props.caseId))
</script>

<template>
  <dl v-if="entry" :id="entry.id" class="texture-facts" aria-label="案例资料">
    <div><dt>谱例</dt><dd>{{ caseLocation(entry) }}</dd></div>
    <div><dt>拍号与速度</dt><dd>{{ entry.meter }} · {{ entry.tempo.marking }} · {{ entry.tempo.unit }} = {{ entry.tempo.bpm }}（{{ entry.tempo.source === 'score' ? '谱面' : '播放' }}）</dd></div>
    <div><dt>实际重音</dt><dd>{{ entry.observed_accent }}</dd></div>
    <div><dt>听感</dt><dd>{{ entry.feel.join('、') }}</dd></div>
    <div><dt>节奏紧张度</dt><dd><strong>{{ tensionLabels[entry.tension.level] }}</strong> · {{ entry.tension.evidence }}</dd></div>
  </dl>
  <dl v-else-if="form.accent" class="texture-facts" aria-label="形式资料">
    <div><dt>类别</dt><dd>{{ categoryLabels[form.category] }}<template v-if="form.aliases.length"> · {{ form.aliases.join('、') }}</template></dd></div>
    <div v-if="form.accent.typical_meters?.length"><dt>典型拍号</dt><dd>{{ form.accent.typical_meters.join('、') }}</dd></div>
    <div><dt>重拍</dt><dd>{{ form.accent.downbeat }}</dd></div>
    <div><dt>典型强调</dt><dd>{{ form.accent.emphasis }}</dd></div>
    <div><dt>分组依据</dt><dd>{{ form.accent.grouping }}</dd></div>
    <div v-for="(value, label) in form.pattern" :key="label"><dt>{{ label }}</dt><dd>{{ value }}</dd></div>
  </dl>
</template>

<style scoped>
.texture-facts {
  margin: 1rem 0 1.4rem;
  scroll-margin-top: calc(var(--vp-nav-height) + 1rem);
  padding: 0.45rem 0.9rem;
  border-inline-start: 3px solid var(--vp-c-brand-1);
  background: var(--vp-c-bg-soft);
  border-radius: 0 6px 6px 0;
}
.texture-facts > div {
  display: grid;
  grid-template-columns: minmax(5.5rem, 23%) 1fr;
  gap: 0.6rem;
  padding: 0.25rem 0;
}
.texture-facts dt { font-weight: 600; color: var(--vp-c-text-2); }
.texture-facts dd { margin: 0; }
</style>
