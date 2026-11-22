import pathlib
p=pathlib.Path('content/techniques/harmony/diminished-seventh-enharmonic-pivot.md')
t=p.read_text(encoding='utf-8')
t=t.replace('小下统音','降六级音（♭6）')
t=t.replace('三十秒与六十四分音符','三十二分音符与六十四分音符')
t=t.replace('谱面临时取消原本的三个降号调号，快板以 p 在 E 小调低音八分音符同音脉动上正式爆发','谱面临时取消原本的三个降号调号（改为无升降号），快板主题以 E 为低音中心、在八分音符同音脉动上正式爆发')
t=t.replace('从三个降号的 C 小调/G 小调体系，到带有一个升号的 E 小调，五度循环上跨越了整整 **4 个调号单位**','从三个降号的 C 小调/G 小调体系，进入无升降号的 E 中心调域，调号差跨越了 3 个单位（若按 E 小调惯用一升记谱则为 4 个）')
p.write_text(t,encoding='utf-8')
print('ok')
