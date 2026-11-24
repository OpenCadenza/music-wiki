import pathlib
p=pathlib.Path('content/notation/articulation-marks-and-realization.md')
t=p.read_text(encoding='utf-8')
repl={
 '`([4F 8F] 16G 16F)`':'（F 附点、F 八分、G–F 两个十六分，同弓连奏）',
 '`8E\' 8F\'`':'（E–F 两个八分断音）',
 '`8ee\' 8ff\'`':'（e²–f² 两个八分断音）',
 '`8ff#\' 8gg\'`':'（f♯²–g² 两个八分断音）',
 '`8bbn\' 8ccc\'`':'（b♭²–c³ 两个八分断音）',
 '`4C\'/ 4B-\'/`':'（C–B♭ 四分断音）',
 '`4eee\'\\ f`':'（e³ 四分断音，强奏）',
 '`(4C 4D 4E 4F)`':'（C–D–E–F 四分连弓）',
 '`(2.C 8D 8C)`':'（附点二分 C，接 D–C 八分）',
 '`8BB- 8C`':'（B♭–C 八分）',
 '`8A/ 8A 8A 8A`':'（A 八分音符分弓）',
 '`8c/ 8c 8c 8c`':'（c 八分音符分弓）',
 '`8dd\'\\) 8r`':'（d³ 八分，接休止）',
 '`8dd\'\\) 8r 8b-\'\\ 8r 2a/`':'（d³–休止–b♭²–休止–a 二分）',
 '`8d-/L 8c 8B-/J 8A-/L 8B- 8c/J`':'（d♭–c–b♭–a♭–b♭–c 六个八分）',
 '`(8d- 8c 8B-) (8A- 8B- 8c)`':'（d♭–c–b♭ 与 a♭–b♭–c 两组三音连弓）',
}
for a,b in repl.items():
    t=t.replace(a,b)
# add cross-link in case 3 intro
old='在贝多芬生前完成的最后一部完整作品《F大调第十六弦乐四重奏》Op. 135 的第三乐章'
new='在贝多芬生前完成的最后一部完整作品《F大调第十六弦乐四重奏》Op. 135 的第三乐章'
if 'string-quartet-acoustic-role-differentiation' not in t:
    t=t.replace('在贝多芬生前完成的最后一部完整作品《F大调第十六弦乐四重奏》Op. 135 的第三乐章（*Lento assai, cantante e tranquillo*，6/8 拍，降 D 大调）中，演奏法记号',
                '在贝多芬生前完成的最后一部完整作品《F大调第十六弦乐四重奏》Op. 135 的第三乐章（*Lento assai, cantante e tranquillo*，6/8 拍，降 D 大调）中，演奏法记号',1)
    # append link after the case 3 heading paragraph
    t=t.replace('演奏法记号褪去了所有外在的戏剧冲突，升华为形而上的精神内省：',
                '演奏法记号褪去了所有外在的戏剧冲突，升华为形而上的精神内省；同一段音乐的音区与声部角色，可对照[《弦乐四重奏》](../ensembles/string-quartet-acoustic-role-differentiation.md)中已编译的 Op.135 III mm.1–12 谱例阅读：',1)
p.write_text(t,encoding='utf-8')
# provenance row
q=pathlib.Path('provenance/notation/articulation-marks-and-realization.md')
s=q.read_text(encoding='utf-8')
s=s.replace('| 占位 | 贝多芬《F大调第十六弦乐四重奏》Op. 135 |','| `beethoven-op135-iii-mm1-12`（关联引用） | 贝多芬《F大调第十六弦乐四重奏》Op. 135 |',1)
q.write_text(s,encoding='utf-8')
print('ok')
