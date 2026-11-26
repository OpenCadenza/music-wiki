// 一次性：清理 manual:gaps 中本轮已补齐的缺口行，并把 K.467 I 缺口缩到 mm.9–28
import { readFileSync, writeFileSync } from 'node:fs'

const file = 'local/resources/catalog/score-board.md'
const drop = [
  /Op\.109 第三乐章 \| 第一\/第二变奏/,
  /Op\.111 第二乐章 \| 主题/,
  /Op\.106 第四乐章 \|/,
  /Op\.110 第三乐章 \|/,
  /Op\.59 No\.1 第一乐章 \| mm\.1–8/,
  /K\.467 第一乐章 \| mm\.74–91/,
  /Op\.61 第一乐章 \|/,
  /K\.467 第二乐章 \|/
]
const lines = readFileSync(file, 'utf8').split(/\r?\n/)
const out = []
let dropped = 0
for (const line of lines) {
  if (drop.some((re) => re.test(line))) {
    dropped += 1
    continue
  }
  if (/K\.467 第一乐章 \| mm\.1–28/.test(line)) {
    out.push(
      '| 莫扎特 K.467 第一乐章 | mm.9–28 | 未完成：本轮只出了主部主题群 mm.1–8 与独奏引子 mm.74–91（据 CCARH MuseData md2 自编码）；mm.9–28 的十六分音型密集段待下一轮出谱（《协奏原则》） |'
    )
    continue
  }
  out.push(line)
}
writeFileSync(file, out.join('\n'), 'utf8')
console.log(`removed ${dropped} gap rows, rewrote K.467 I row`)
