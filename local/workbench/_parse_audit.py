import json
d=json.load(open('local/workbench/_audit.json',encoding='utf-8'))
def walk(o):
    if isinstance(o,dict):
        if o.get('code')=='uncollected-article' or o.get('type')=='uncollected-article':
            print(o.get('path'), o.get('message'))
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(d)
