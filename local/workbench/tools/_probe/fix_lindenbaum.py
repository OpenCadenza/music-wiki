import pathlib
p=pathlib.Path('content/techniques/sound/schubert-lieder-piano-role.md')
t=p.read_text(encoding='utf-8')
t=t.replace('在第 59 小节，狂暴的风雪平息，音乐重返平和纯净的 E 大调抒情音型','在第 59 小节，狂暴的风雪平息，主题在 E 大调上重返平和纯净的抒情音型')
p.write_text(t,encoding='utf-8')
print('ok')
