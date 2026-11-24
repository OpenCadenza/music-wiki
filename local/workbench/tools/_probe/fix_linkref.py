import pathlib
p=pathlib.Path('provenance/notation/transposing-instruments-notation-and-sounding-pitch.md')
t=p.read_text(encoding='utf-8').replace('（关联既有谱例）','（关联引用）')
p.write_text(t,encoding='utf-8')
print('ok')
