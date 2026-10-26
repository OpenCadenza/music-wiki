<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { withBase } from 'vitepress'
import {
  Download,
  ExternalLink,
  Pause,
  Play,
  RotateCcw,
  Volume2,
  VolumeX
} from '@lucide/vue'

const props = defineProps<{
  id: string
  title: string
  language: 'abc' | 'lilypond'
  status: 'published' | 'draft'
  svg: string
  audio: string
  source: string
}>()

const audioElement = ref<HTMLAudioElement>()
const playing = ref(false)
const muted = ref(false)
const duration = ref(0)
const currentTime = ref(0)
const loadError = ref(false)

const svgUrls = computed(() =>
  props.svg
    .split('|')
    .filter(Boolean)
    .map((path) => withBase(path))
)
const audioUrl = computed(() => withBase(props.audio))
const sourceUrl = computed(() => withBase(props.source))
const progress = computed(() =>
  duration.value > 0 ? (currentTime.value / duration.value) * 100 : 0
)

function formatTime(value: number) {
  if (!Number.isFinite(value) || value < 0) return '0:00'
  const minutes = Math.floor(value / 60)
  const seconds = Math.floor(value % 60)
  return `${minutes}:${seconds.toString().padStart(2, '0')}`
}

async function togglePlayback() {
  const audio = audioElement.value
  if (!audio) return
  if (audio.paused) {
    try {
      await audio.play()
    } catch {
      loadError.value = true
    }
  } else {
    audio.pause()
  }
}

function seek(event: Event) {
  const audio = audioElement.value
  if (!audio || duration.value <= 0) return
  const value = Number((event.target as HTMLInputElement).value)
  audio.currentTime = (value / 100) * duration.value
}

function restart() {
  const audio = audioElement.value
  if (!audio) return
  audio.currentTime = 0
  void audio.play()
}

function toggleMute() {
  const audio = audioElement.value
  if (!audio) return
  audio.muted = !audio.muted
  muted.value = audio.muted
}

function syncAudioMetadata() {
  const audio = audioElement.value
  if (!audio) return
  if (Number.isFinite(audio.duration)) duration.value = audio.duration
  currentTime.value = Number.isFinite(audio.currentTime) ? audio.currentTime : 0
  loadError.value = false
}

onMounted(() => {
  const audio = audioElement.value
  if (!audio) return
  audio.addEventListener('durationchange', syncAudioMetadata)
  audio.addEventListener('loadeddata', syncAudioMetadata)
  syncAudioMetadata()
})
</script>

<template>
  <figure class="score-example" :data-score-id="id">
    <figcaption>
      <span class="score-title">{{ title }}</span>
      <span class="score-meta">
        <span v-if="status === 'draft'" class="score-status">草稿</span>
        <span class="score-format">{{ language === 'abc' ? 'ABC' : 'LilyPond 2.26.0' }}</span>
      </span>
    </figcaption>

    <div class="score-sheet">
      <a
        v-for="(svgUrl, pageIndex) in svgUrls"
        :key="svgUrl"
        class="score-page"
        :href="svgUrl"
        target="_blank"
        rel="noreferrer"
      >
        <img :src="svgUrl" :alt="`${title} 乐谱第 ${pageIndex + 1} 页`" loading="lazy" />
        <span class="score-open" aria-hidden="true"><ExternalLink :size="16" /></span>
      </a>
    </div>

    <div class="score-controls" aria-label="音频播放">
      <button class="control-button primary" type="button" :aria-label="playing ? '暂停' : '播放'" @click="togglePlayback">
        <Pause v-if="playing" :size="18" />
        <Play v-else :size="18" />
      </button>
      <button class="control-button" type="button" aria-label="从头播放" @click="restart">
        <RotateCcw :size="17" />
      </button>
      <span class="score-time">{{ formatTime(currentTime) }}</span>
      <input
        class="score-progress"
        type="range"
        min="0"
        max="100"
        step="0.1"
        :value="progress"
        aria-label="播放进度"
        @input="seek"
      />
      <span class="score-time">{{ formatTime(duration) }}</span>
      <button class="control-button" type="button" :aria-label="muted ? '取消静音' : '静音'" @click="toggleMute">
        <VolumeX v-if="muted" :size="17" />
        <Volume2 v-else :size="17" />
      </button>
      <a class="control-button" :href="audioUrl" download aria-label="下载音频">
        <Download :size="17" />
      </a>
      <a class="score-source" :href="sourceUrl" target="_blank" rel="noreferrer">源码</a>
    </div>

    <p v-if="loadError" class="score-error">音频未能载入。</p>

    <audio
      ref="audioElement"
      class="score-audio-element"
      :src="audioUrl"
      preload="metadata"
      @durationchange="syncAudioMetadata"
      @play="playing = true"
      @pause="playing = false"
      @ended="playing = false"
      @loadedmetadata="syncAudioMetadata"
      @loadeddata="syncAudioMetadata"
      @timeupdate="currentTime = $event.currentTarget.currentTime"
      @error="loadError = true"
    />
  </figure>
</template>
