# -*- coding: utf-8 -*-
"""大提琴 m.16：连音线起点改到第三个音（G2），并补回该音的断奏点。"""
import io, os

p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'schubert-d929-mvt2-mm1-21.ly')
s = io.open(p, encoding='utf-8').read()
old = "  g,4~ g,16 g,16-( a,16-. b,16-.) |"
new = "  g,4~ g,16 g,16-.( a,16-. b,16-.) |"
assert old in s, "anchor not found"
s = s.replace(old, new, 1)
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("ok")
