# -*- coding: utf-8 -*-
"""补齐 pianoLH 剩余三处力度记号（m15 / m20 / m21）。"""
import io, sys, os

p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 'schubert-d929-mvt2-mm1-21.ly')
s = io.open(p, encoding='utf-8').read()
orig = s

pairs = [
    # m15：钢琴左手 pp（源 onset=24，落在第二个八分 G3 上）
    ("  r8 g8 g,4 |\n  r8 g8 g,8( f,8 |",
     "  r8 g8\\pp g,4 |\n  r8 g8 g,8( f,8 |"),
    # m20 的 p 与 m21 的 pp（m18 有同样一行，用 m19 做锚点）
    ("  af,8 af,8 ef,8 ef,8 |\n  f,8 f,8 g,8 g,8 |\n  c,8 r8 r4 |",
     "  af,8 af,8 ef,8 ef,8 |\n  f,8\\p f,8 g,8 g,8 |\n  c,8\\pp r8 r4 |"),
]
for a, b in pairs:
    if a not in s:
        print("NOT FOUND:", repr(a[:60]))
    s = s.replace(a, b, 1)

io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("changed:", orig != s)
print(s[s.index('pianoLH'):s.index('\\score')])
