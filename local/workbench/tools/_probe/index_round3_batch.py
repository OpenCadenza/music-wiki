import pathlib
def add(path, lines):
    p=pathlib.Path(path); t=p.read_text(encoding='utf-8').rstrip()+'\n'
    for line in lines:
        slug=line.split('](')[1].split(')')[0]
        if slug not in t: t += line+'\n'
    p.write_text(t,encoding='utf-8')

add('content/ensembles/index.md',[
 '- [人声、中提琴与钢琴](voice-viola-and-piano.md)：女低音、助奏中提琴与钢琴如何在同频区段化解掩蔽，形成三方复调对话。',
])
add('content/techniques/counterpoint/index.md',[
 '- [海顿的变奏对话](cantus-firmus-variation-and-conversational-counterpoint.md)：海顿 Op.76/3 第二乐章如何用定旋律声部轮换与织体加减法，把国歌变奏写成室内乐对话。',
])
add('content/techniques/sound/index.md',[
 '- [合唱式织体](brahms-string-quartet-chorale-texture.md)：勃拉姆斯 Op.51/1 如何把合唱与管风琴式声部导向嵌入弦乐四重奏。',
 '- [德彪西四重奏色调](debussy-quartet-timbre-and-harmonic-color.md)：德彪西 Op.10 如何用调式偏转、平行和弦与弱音器置换打开印象主义室内乐音响。',
 '- [K.550 句法与配器](mozart-k550-syntax-and-orchestration.md)：莫扎特 K.550 第一乐章如何用弦乐先行、木管标点与双调圆号铰接句法。',
])
add('content/techniques/structure/index.md',[
 '- [海顿104慢引子](slow-introduction-and-allegro-transition.md)：海顿 No.104 的慢引子如何用号角悬疑、小调滑移与属音制动为快板蓄能。',
 '- [自传叙事与四重奏](autobiographical-narrative-and-quartet-form.md)：斯美塔那 SQ1 如何在严格奏鸣构架里承载私密自传叙事。',
 '- [协奏原则](concertante-principle-and-double-exposition.md)：古典协奏曲如何把利都奈罗与奏鸣曲式熔成双重呈示。',
])
p=pathlib.Path('content/index.md'); t=p.read_text(encoding='utf-8')
t=t.replace('这个实验目前已经产出了 40 篇文章','这个实验目前已经产出了 48 篇文章')
p.write_text(t,encoding='utf-8')
print('ok')
