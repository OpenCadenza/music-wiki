<script setup lang="ts">
import { useData } from 'vitepress'

const { frontmatter } = useData()
</script>

<template>
  <p v-if="frontmatter.provenanceUrl" class="provenance-link">
    <a :href="frontmatter.provenanceUrl" target="_blank" rel="noreferrer">来源与许可 →</a>
  </p>
</template>
