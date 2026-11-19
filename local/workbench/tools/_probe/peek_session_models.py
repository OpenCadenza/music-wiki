import json, glob, os

files = sorted(glob.glob(r"C:\Users\ThinkBook\.dsh\storages\session_projcache\sessions\*.json"),
               key=os.path.getmtime, reverse=True)
path = files[0]
print("session file:", os.path.basename(path))
data = json.load(open(path, encoding="utf-8"))

def walk(obj, prefix="", depth=0):
    if depth > 3:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            kl = k.lower()
            if "model" in kl or "provider" in kl or "allowed" in kl:
                s = json.dumps(v, ensure_ascii=False)[:300]
                print(prefix + k, "=", s)
            walk(v, prefix + k + ".", depth + 1)
    elif isinstance(obj, list):
        for i, v in enumerate(obj[:5]):
            walk(v, prefix + f"[{i}].", depth + 1)

walk(data)
