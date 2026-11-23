import pathlib
def add(path, lines):
    p=pathlib.Path(path); t=p.read_text(encoding='utf-8').rstrip()+'\n'
    for line in lines:
        if line.split('](')[1].split(')')[0] not in t:
            t += line+'\n'
    p.write_text(t,encoding='utf-8')

add('content/techniques/harmony/index.md',[
 '- [副属连锁](applied-dominant-chains-and-functional-replacement.md)：副属和弦如何五度连锁推进，以及装饰性离调与结构性功能替代的句法分界。',
 '- [终止四六和弦](cadential-six-four-and-dominant-syntax.md)：终止四六为何不是独立和弦，而是属功能区的双倚音延留，以及它何时必须出现、何时被省略。',
 '- [三度调性](chromatic-mediant-and-tonal-space.md)：大三度中音关系如何扩张奏鸣曲式的调性空间，并迫使再现部作出结构代偿。',
 '- [减七枢纽](diminished-seventh-enharmonic-pivot.md)：减七和弦的对称等音结构如何成为多向导音枢纽，触发远关系调性突变。',
 '- [和声节奏](harmonic-rhythm-and-syntactic-pacing.md)：和声变更频率如何独立于表面音符节奏，组织乐句推进、终止期待与结构制动。',
 '- [利底亚调式](lydian-mode-and-tonal-gravity.md)：贝多芬 Op.132 第三乐章如何用无调号 F 利底亚剥离功能和声的向心重力。',
 '- [调式交替](modal-mixture-and-color-syntax.md)：同主音大小调借用如何在提供色彩对比的同时维系单一调性中心。',
])
add('content/techniques/structure/index.md',[
 '- [终止图式](cadential-prinner-and-structural-closure.md)：加兰特 Prinner 如何通过低音变异与终止四六插入，从延续图式转化为结构性正格终止。',
 '- [复合乐段](compound-period-hierarchical-syntax.md)：16 小节复合乐段如何把乐句升阶为乐题，以双层终止维持宏观呼应与微观动力。',
 '- [内聚裂隙](medial-caesura-and-sonata-transition.md)：奏鸣曲式过渡段如何以能量蓄积与突变阻断，打开副部主题的句法空间。',
 '- [乐句扩展](phrase-expansion-and-structural-skeleton.md)：古典句法如何通过内部扩展、终止回避与模进追加拉长乐句，同时保持可还原的骨架。',
 '- [模进与句法](sequence-mechanics-and-syntactic-functions.md)：模进如何同时承担延续动力、调性迁移与结构标点，以及装饰性模进与结构性模进的分野。',
 '- [超乐章目的论](teleological-multimovement-integration.md)：晚期贝多芬如何让多乐章在终端回收开篇材料，完成整体目的论。',
])
add('content/techniques/sound/index.md',[
 '- [长笛写作](flute-writing-and-orchestral-acoustics.md)：长笛四阶音区的声能反差、气息消耗与掩蔽规避，如何决定其管弦乐写作。',
 '- [自然圆号写作](natural-horn-writing-and-harmonic-series.md)：自然圆号的泛音列与管身调性如何塑造古典配器的音区、调性与手塞语法。',
 '- [定音鼓写作](timpani-writing-and-classical-orchestration.md)：双鼓固定音高与机械调弦延迟如何重塑曲式标点、和声骨架与动机形态。',
 '- [中提琴写作](viola-writing-and-orchestral-voicing.md)：中提琴的形制悖论、音区特性与掩蔽矛盾如何塑造室内乐与管弦乐织体。',
])
add('content/techniques/counterpoint/index.md',[
 '- [平行五八度](parallel-fifths-and-octaves.md)：严格对位的平行五八度禁则如何在古典与浪漫实践中被功能性、织体性与音响色彩打破。',
])
add('content/techniques/rhythm/index.md',[
 '- [超拍与乐句节奏](hypermeter-and-phrase-rhythm.md)：高层超拍如何与和声终止错位，塑造古典句法的悬置、重叠与动力弹性。',
])
add('content/styles/index.md',[
 '- [管乐交响化](woodwind-symphonic-emancipation.md)：木管组如何从宫廷 Harmoniemusik 的伴宴与翻倍外壳，蜕变为管弦乐中对等的独立声部。',
])

p=pathlib.Path('content/index.md'); t=p.read_text(encoding='utf-8')
t=t.replace('这个实验目前已经产出了 20 篇文章','这个实验目前已经产出了 40 篇文章')
p.write_text(t,encoding='utf-8')
print('ok')
