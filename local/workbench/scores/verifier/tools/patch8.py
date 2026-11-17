p='cmp_xml.py'
s=open(p,encoding='utf-8').read()
s=s.replace("src = read_part(score, pi, start, count + 1)","src = read_part(score, pi, start, count)")
s=s.replace("b = [(m, d) for (_, m, d) in src[n]] if n < len(src) else []",
            "b = [(m, d) for (_, m, d) in src[n - 1]] if n - 1 < len(src) else []")
open(p,'w',encoding='utf-8').write(s)
print('alignment fixed')
