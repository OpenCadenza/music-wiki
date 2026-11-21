#!/usr/bin/env node
// 每篇文章的验收门禁（第二轮 P2 起使用）。
// 用法：
//   node local/workbench/tools/check_article_acceptance.mjs            # 全库
//   node local/workbench/tools/check_article_acceptance.mjs hemiola   # 路径片段过滤
// 退出码：0 全部通过；1 有失败项。
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const contentDir = path.join(root, 'content');
const provDir = path.join(root, 'provenance');
const archDir = path.join(root, 'local/docs/研究归档');
const filters = process.argv.slice(2);

function walk(dir) {
  const out = [];
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) out.push(...walk(p));
    else if (ent.isFile() && ent.name.endsWith('.md')) out.push(p);
  }
  return out;
}

const rel = (p) => path.relative(root, p).split(path.sep).join('/');
const articles = walk(contentDir)
  .filter((p) => path.basename(p) !== 'index.md')
  .filter((p) => filters.length === 0 || filters.some((f) => rel(p).includes(f)))
  .sort();

// 全库谱例 id 唯一性
const idOwners = new Map();
for (const p of walk(contentDir)) {
  const text = fs.readFileSync(p, 'utf8');
  for (const m of text.matchAll(/```lilypond[^\n]*?\bid="([A-Za-z0-9._-]+)"/g)) {
    const arr = idOwners.get(m[1]) ?? [];
    arr.push(rel(p));
    idOwners.set(m[1], arr);
  }
}
const dupIds = [...idOwners.entries()].filter(([, v]) => v.length > 1);

const bodyRules = [
  ['A 内部代号', /\b(?:scholar-[abc]\d?|assistant-scores(?:-[a-z])?)\b/],
  ['B 源文件行号', /(?:^|[^0-9])行 \d+|Lines? \d+[-–]\d+/],
  ['B 本地路径', /local\/(?:resources|workbench|origin_resources)/],
  ['C 交付状态', /交付状态|待后续谱例|待资料助手|待谱例助手|待谱例交付/],
  ['E GM 编号', /GM \d/],
];

function tableRows(text, heading) {
  const idx = text.indexOf(heading);
  if (idx === -1) return 0;
  const rest = text.slice(idx + heading.length);
  const stop = rest.search(/^##\s/m);
  const section = stop === -1 ? rest : rest.slice(0, stop);
  return section
    .split(/\r?\n/)
    .filter((l) => /^\|/.test(l.trim()))
    .filter((l) => !/^\|\s*-{2,}/.test(l.trim())) // 分隔行
    .filter((l) => !/^\|\s*(来源|谱例 id)\s*\|/.test(l.trim())) // 表头
    .filter((l) => l.replace(/\|/g, '').trim().length > 0).length;
}

let failures = 0;
const report = [];

for (const p of articles) {
  const relPath = rel(p);
  const text = fs.readFileSync(p, 'utf8');
  const lines = text.split(/\r?\n/);
  const problems = [];

  // 1. 标题结构
  const h1Idx = lines.findIndex((l) => /^#\s+/.test(l));
  const h1 = h1Idx >= 0 ? lines[h1Idx].replace(/^#\s+/, '').trim() : '';
  const h1Len = [...h1].length;
  if (h1Idx === -1) problems.push('缺 H1');
  else if (h1Len < 2 || h1Len > 8) problems.push(`H1 长度 ${h1Len}（需 2–8 字）：${h1}`);

  const after = lines.slice(h1Idx + 1, h1Idx + 4).filter((l) => l.trim() !== '');
  if (!after.some((l) => /^<p class="doc-subtitle">.*<\/p>$/.test(l.trim())))
    problems.push('H1 后缺单行 <p class="doc-subtitle">…</p>');

  const fm = lines.slice(0, 8).find((l) => /^title:/.test(l));
  if (!fm) problems.push('frontmatter 缺 title');
  else if (fm.replace(/^title:\s*/, '').trim().replace(/^["']|["']$/g, '') !== h1)
    problems.push(`frontmatter title 与 H1 不一致：${fm.trim()}`);

  // 2. provenance
  const provPath = path.join(provDir, path.relative(contentDir, p));
  if (!fs.existsSync(provPath)) problems.push('缺 provenance 文件');
  else {
    const prov = fs.readFileSync(provPath, 'utf8');
    if (tableRows(prov, '## 引用与出处') < 1) problems.push('provenance「引用与出处」表为空');
    if (tableRows(prov, '## 谱例') < 1) problems.push('provenance「谱例」表为空');
  }

  // 3. 归档同名
  const slug = path.basename(p, '.md');
  if (!fs.existsSync(path.join(archDir, `${slug}.md`))) problems.push(`缺同名归档 ${slug}.md`);

  // 4. 正文残留
  for (const [name, re] of bodyRules) {
    if (re.test(text)) {
      const hit = text.split(/\r?\n/).findIndex((l) => re.test(l));
      problems.push(`${name}（约第 ${hit + 1} 行）`);
    }
  }

  // 5. 内部 md 链接
  const dir = path.dirname(p);
  for (const m of text.matchAll(/\]\(([^)\s]+\.md)(?:#[^)]*)?\)/g)) {
    const target = m[1];
    if (/^https?:/.test(target)) continue;
    if (!fs.existsSync(path.join(dir, target))) problems.push(`断链 ${target}`);
  }

  // 6. 谱例 id 重复（只在全库层面报一次，挂到相关文章）
  for (const [id, owners] of dupIds) {
    if (owners.includes(relPath)) problems.push(`谱例 id 重复：${id}（${owners.join(', ')}）`);
  }

  if (problems.length) {
    failures++;
    report.push(`FAIL ${relPath}\n  - ${problems.join('\n  - ')}`);
  } else {
    report.push(`PASS ${relPath}`);
  }
}

console.log(report.join('\n'));
console.log(`\n合计 ${articles.length} 篇：通过 ${articles.length - failures}，失败 ${failures}。`);
if (dupIds.length) console.log(`全库谱例 id 重复 ${dupIds.length} 组。`);
process.exit(failures ? 1 : 0);
