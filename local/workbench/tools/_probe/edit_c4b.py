import pathlib
p=pathlib.Path('content/techniques/harmony/lydian-mode-and-tonal-gravity.md')
t=p.read_text(encoding='utf-8')
t=t.replace('### 3.1 D 大调“新力觉醒”的体质反差','### 3.1 D 大调“新力觉醒”的音响反差')
t=t.replace('构建体质维度的戏剧对抗','构建音响层面的戏剧对抗')
p.write_text(t,encoding='utf-8')
print('ok')
