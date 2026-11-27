p = r'local/docs/研究归档/fugue-in-the-sonata-cycle.md'
s = open(p, encoding='utf-8').read()
repls = [
    ('1. **贝多芬《降B大调第29钢琴奏鸣曲“槌子键琴”》Op. 106 第四乐章 引子**',
     '1. **贝多芬《降B大调第29钢琴奏鸣曲“槌子键琴”》Op. 106 第四乐章 引子**（围栏 `beethoven-op106-iv-mm1-14`）'),
    ('2. **贝多芬《降B大调第29钢琴奏鸣曲“槌子键琴”》Op. 106 第四乐章 赋格呈示部**',
     '2. **贝多芬《降B大调第29钢琴奏鸣曲“槌子键琴”》Op. 106 第四乐章 赋格呈示部**（围栏 `beethoven-op106-iv-mm15-48`）'),
    ('3. **贝多芬《降A大调第31钢琴奏鸣曲》Op. 110 第三乐章 宣叙调与哀歌**',
     '3. **贝多芬《降A大调第31钢琴奏鸣曲》Op. 110 第三乐章 宣叙调与哀歌**（围栏 `beethoven-op110-iii-mm1-26`）'),
    ('4. **贝多芬《降A大调第31钢琴奏鸣曲》Op. 110 第三乐章 赋格呈示部**',
     '4. **贝多芬《降A大调第31钢琴奏鸣曲》Op. 110 第三乐章 赋格呈示部**（围栏 `beethoven-op110-iii-mm27-56`）'),
]
for a, b in repls:
    assert a in s, a
    s = s.replace(a, b, 1)
n = s.count('状态：单行普通文本占位')
s = s.replace('状态：单行普通文本占位', '状态：已成文围栏并编译通过')
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('statuses replaced:', n)
