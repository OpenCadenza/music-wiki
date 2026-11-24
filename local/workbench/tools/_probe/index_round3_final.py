import pathlib
def add(path, lines):
    p=pathlib.Path(path); t=p.read_text(encoding='utf-8').rstrip()+'\n'
    for line in lines:
        slug=line.split('](')[1].split(')')[0]
        if slug not in t: t += line+'\n'
    p.write_text(t,encoding='utf-8')

add('content/techniques/structure/index.md',[
 '- [变奏曲式的类型](variation-types-and-structural-transformations.md)：装饰、性格/对位与时值递减三类变奏如何重塑骨架与时间。',
 '- [死与少女的变奏](schubert-d810-variation-movement.md)：舒伯特 D.810 第二乐章如何用织体裂变与调性明暗把歌曲原型写成室内乐全景变奏。',
 '- [浪漫套曲的结构](romantic-song-cycle-macrostructure.md)：舒曼《诗人之恋》如何用悬置属七、独立后奏与跨曲再现织成超曲式网络。',
])
add('content/techniques/rhythm/index.md',[
 '- [民族语汇与节奏](folk-idiom-and-rhythmic-vitality.md)：德沃夏克 Op.96 如何把五声骨架、苏格兰切分与持续低音注入古典四重奏。',
])
add('content/techniques/sound/index.md',[
 '- [德彪西的音响平面](debussy-vocal-planes-of-tone.md)：德彪西歌曲如何用人声朗诵调、器乐背景动型与调式色彩层拉开三维景深。',
 '- [独奏与乐队对话](mozart-concerto-solo-orchestra-dialogue.md)：K.467 第二乐章如何用弱音弦乐、拨奏低音与木管标点建立独奏—乐队三方对话。',
 '- [歌曲中的钢琴角色](schubert-lieder-piano-role.md)：舒伯特如何让钢琴从伴奏升格为造境、心理反思与叙事接管的主角。',
])
add('content/techniques/counterpoint/index.md',[
 '- [赋格在奏鸣曲中](fugue-in-the-sonata-cycle.md)：贝多芬 Op.106/Op.110 如何把严格赋格嵌入奏鸣套曲终章，完成危机与救赎。',
 '- [莫扎特四重奏对话](mozart-quartet-conversational-counterpoint.md)：K.421 如何让四件均质提琴在动机分配与对位中真正平权对话。',
])
add('content/notation/index.md',[
 '- [移调记谱与实音](transposing-instruments-notation-and-sounding-pitch.md)：K.550/Op.92/Op.21 三例拆解移调乐器的记谱—实音映射与编码陷阱。',
 '- [演奏法记号与实现](articulation-marks-and-realization.md)：贝多芬早中晚三期四重奏的连弓、断音与强弱突变如何落到运弓力学。',
])
add('content/ensembles/index.md',[
 '- [从管弦乐到四重奏](orchestra-to-string-quartet-reduction.md)：海顿《临终七言》如何把管弦乐原版压缩成四件提琴的声学代偿。',
])
p=pathlib.Path('content/index.md'); t=p.read_text(encoding='utf-8')
t=t.replace('这个实验目前已经产出了 48 篇文章','这个实验目前已经产出了 60 篇文章')
p.write_text(t,encoding='utf-8')
print('ok')
