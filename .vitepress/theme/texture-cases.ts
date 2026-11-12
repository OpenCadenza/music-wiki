export type Tension = 'low' | 'medium' | 'high'

export interface TextureCase {
  id: string
  question: string
  composer: string
  work: string
  section?: string
  measures: { start: number; end: number }
  meter: string
  tempo: { marking: string; unit: string; bpm: number; source: 'score' | 'playback' }
  observed_accent: string
  feel: string[]
  tension: { level: Tension; evidence: string }
  notation: { format: 'lilypond' | 'abc'; id: string }
}

export interface TextureForm {
  form_id: string
  category: 'texture' | 'dance'
  topic_name: string
  question: string
  description: string
  aliases: string[]
  accent: {
    typical_meters?: string[]
    downbeat: string
    emphasis: string
    grouping: string
  }
  pattern: Record<string, string>
  cases: TextureCase[]
}

export const categoryLabels = { texture: '织体', dance: '舞曲' } as const
export const tensionLabels = { low: '低', medium: '中', high: '高' } as const

export function caseLocation(entry: TextureCase) {
  return [entry.composer, entry.work, entry.section,
    `第 ${entry.measures.start}–${entry.measures.end} 小节`].filter(Boolean).join(' · ')
}
