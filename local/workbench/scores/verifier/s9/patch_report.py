# -*- coding: utf-8 -*-
import io
p = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\verifier\核验报告-D929.md"
s = io.open(p, encoding="utf-8").read()
old = '建议改为"c 小调的行板/葬礼进行曲式乐章"。'
new = ('建议改为"c 小调的行板/葬礼进行曲式乐章"。'
       '**注意文章自身第 143 行已经写了"规整的丧葬进行曲节奏"**——"稍快板"与"丧葬进行曲"在同一个案例里互相矛盾，'
       '删掉"稍快板"即可自洽。')
print("found:", old in s)
if old in s:
    s = s.replace(old, new)
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    print("written, bytes", len(s.encode("utf-8")))
