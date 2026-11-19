import io, os, re, glob

root = os.getcwd()
files = [p.replace('\\', '/') for p in glob.glob('content/**/*.md', recursive=True) if not p.endswith('index.md')]
made = []

for p in files:
    t = io.open(p, encoding='utf-8').read()
    h1 = re.search(r'^#\s+(.+)$', t, re.M)
    title = h1.group(1).strip() if h1 else p
    rel = p[len('content/'):]
    fences = []
    for m in re.finditer(r'```lilypond([^\n]*)\n', t):
        attrs = m.group(1)
        fences.append({
            'id': (re.search(r'id="([^"]*)"', attrs) or [None, ''])[1],
            'title': (re.search(r'title="([^"]*)"', attrs) or [None, ''])[1],
            'location': (re.search(r'location="([^"]*)"', attrs) or [None, ''])[1],
        })
    body = [f"# {title}", "", f"- 文章：`content/{rel}`", "- 许可：待补", ""]
    body += ["## 引用与出处", "", "| 来源 | 版本/位置 | 在本文的用途 |", "| --- | --- | --- |", "|  |  |  |", ""]
    body += ["## 谱例", ""]
    if fences:
        body += ["| 谱例 id | 作品 | 定位 | 底本 | 许可 |", "| --- | --- | --- | --- | --- |"]
        for f in fences:
            body.append(f"| `{f['id']}` | {f['title']} | {f['location']} | 待补 | 待补 |")
    else:
        body.append("（本文暂无谱例）")
    body.append("")
    out = os.path.join('provenance', rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    io.open(out, 'w', encoding='utf-8', newline='\n').write("\n".join(body))
    made.append(rel)

readme = """# 来源与许可

本目录登记每篇文章的来源、底本与许可，结构与 `content/` 一致：文章 `content/<路径>.md` 对应
`provenance/<路径>.md`。站点在文章末尾提供「来源与许可」入口（依赖 main 分支的站点改动）。

正文可以自由引用外部资料、点名作者、指出出处；版本、页码、URL、许可等**书目信息**写在这里，
不把整份参考文献表搬进正文。

## 文件格式

```md
# 文章标题
- 文章：`content/<路径>.md`
- 许可：…

## 引用与出处
| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |

## 谱例
| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
```

## 登记约定

- 学者成稿时登记自己用到的资料与谱例底本；已有「参考文献/资料索引」章节的内容搬到这里。
- 谱例助手交付新谱例时，补上作品、底本、排版者与许可。
- 没有外部来源的文章不建文件，页面不显示入口。

## 谱例底本与许可（沿用主库登记）

谱例优先采用公有领域乐谱的再排版或 CC0 编码；贝多芬等古典作品本身已进入公有领域，条目记录的是
所用**排版版本**的出处与排版者。每段谱例只截取数小节用于教学分析，不构成完整乐谱的再分发。
"""
io.open('provenance/README.md', 'w', encoding='utf-8', newline='\n').write(readme)

io.open('NOTICE.md', 'w', encoding='utf-8', newline='\n').write(
    "# 谱例来源与许可\n\n"
    "本分支的来源与许可按文章登记在 [`provenance/`](provenance/README.md)，"
    "结构与 `content/` 一致。文章 `content/<路径>.md` 对应 `provenance/<路径>.md`。\n"
)
print('provenance 文件:', len(made))
