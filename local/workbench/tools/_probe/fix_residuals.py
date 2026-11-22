import pathlib
def sub(path, pairs):
    p=pathlib.Path(path); t=p.read_text(encoding='utf-8')
    for a,b in pairs:
        if a not in t: print('MISS', path, a[:30])
        t=t.replace(a,b)
    p.write_text(t,encoding='utf-8')

sub('content/techniques/sound/natural-horn-writing-and-harmonic-series.md',[
 ('作 F 需浅塞（下微调），作 F# 需深塞（或唇部微调）','作 F 需深塞（下微调约 49 音分），作 F♯ 需唇部上顶微调（手塞只能降音高）')])
sub('content/techniques/structure/compound-period-hierarchical-syntax.md',[
 ('第 8 小节低音以 $E \\to E_1$ 明确锁定属音','第 8 小节低音以 E3 明确锁定属音'),
 ('第 16 小节强拍经低音明确的属到主跳进（$E_1 \\to A_1$）','第 16 小节强拍经低音明确的属到主跳进（E3 → A2）')])
sub('content/techniques/counterpoint/parallel-fifths-and-octaves.md',[
 ('大字一组与大字组 $CC\\text{–}C$','大字组 C2 与小字组 C3'),
 ('低音突然以八度加倍击出大字一组与大字组 $CC\\text{–}C$','低音突然以八度加倍击出大字组 C2 与小字组 C3')])
sub('content/techniques/harmony/lydian-mode-and-tonal-gravity.md',[
 ('中提琴以大字组低八度形态进入','中提琴以小字组低八度形态进入'),
 ('以大字一组低音进入（$CC\\text{–}AA$）','以大字组低音进入（C2–A2）'),
 ('唱出 $2ff\\text{–}2ee\\mid 2dd\\text{–}2ee$','唱出 f3–e3 ｜ d3–e3')])
sub('content/techniques/harmony/applied-dominant-chains-and-functional-replacement.md',[
 ('（$8dd \\to 8cc\\sharp$）','（谱面写作两个八分音符：d3→c♯3）'),
 ('右手 $ee \\to ddd$ 构成','右手 e3→d3 的八度下行构成')])
sub('content/techniques/harmony/diminished-seventh-enharmonic-pivot.md',[
 ('$4f\\sharp\\text{–}4a\\text{–}4dd\\sharp$','f♯3–a3–d♯4'),
 ('category: 创作技法','category: techniques/harmony')])
sub('content/techniques/harmony/modal-mixture-and-color-syntax.md',[
 ('category: 创作技法','category: techniques/harmony')])
sub('local/docs/研究归档/woodwind-symphonic-emancipation.md',[
 ('核心音乐现象：弦乐赋格呈示中大管在 mm. 7–10 作为独立复调对位声部介入','核心音乐现象：弦乐赋格呈示中，大管于 m.10 第 3 拍起以 G2→C3→E3/G3 与低音提琴同步进入低音层（mm.10–12），m.11 圆号加入，m.12 长笛/双簧管加入')])
print('done')
