import pathlib,re
names = ['applied-dominant-chains-and-functional-replacement','compound-period-hierarchical-syntax','flute-writing-and-orchestral-acoustics','lydian-mode-and-tonal-gravity','medial-caesura-and-sonata-transition','natural-horn-writing-and-harmonic-series','teleological-multimovement-integration','timpani-writing-and-classical-orchestration','viola-writing-and-orchestral-voicing','woodwind-symphonic-emancipation']
for n in names:
    p=pathlib.Path(f'local/docs/研究归档/{n}.md')
    t=p.read_text(encoding='utf-8')
    t=t.replace('**状态**：已成稿，待本批复读','**状态**：已复读（reviewer-2 中期复读 + 作者返修，2026-11-22）')
    t=t.replace('**当前状态**：已成稿，待本批复读','**当前状态**：已复读（reviewer-2 中期复读 + 作者返修，2026-11-22）')
    t=t.replace('**状态**：`已成稿，待本批复读`','**状态**：`已复读`（reviewer-2 中期复读 + 作者返修，2026-11-22）')
    p.write_text(t,encoding='utf-8')
print('done')
