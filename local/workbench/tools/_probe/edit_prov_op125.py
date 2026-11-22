import pathlib
p=pathlib.Path('provenance/techniques/sound/timbral-contrast-and-formal-articulation.md')
t=p.read_text(encoding='utf-8')
t=t.replace('| `beethoven-op125-i-mm1-35`（待回填） | 贝多芬 第九交响曲 Op.125 第一乐章 | Allegro ma non troppo, un poco maestoso，mm.1–35 | CCARH MuseData sym9（依 Breitkopf & Härtel 转写） | 学术/教育用途（非 CC0） |','| `beethoven-op125-i-mm1-35` | 贝多芬 第九交响曲 Op.125 第一乐章 | Allegro ma non troppo, un poco maestoso，mm.1–35 | CCARH MuseData sym9（依 Breitkopf & Härtel 转写） | 学术/教育用途（非 CC0） |')
p.write_text(t,encoding='utf-8')
print('ok')
