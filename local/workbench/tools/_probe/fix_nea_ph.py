import io

p = r"content\techniques\harmony\neapolitan-chord-structural-mutation.md"
t = io.open(p, encoding="utf-8").read()
old = "****\n\n> 谱例待补： 。"
new = """> **教科书规范模型：g 小调／f 小调 i → N⁶ → V⁷ → i（非真实作品原谱）**

> 谱例待补：这是教材式规范句法，不是任何一部作品的原谱；是否改为示意性谱例由作者决定。"""
if old in t:
    t = t.replace(old, new, 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)
    print("已修复")
else:
    print("未匹配")