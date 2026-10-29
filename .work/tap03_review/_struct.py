import json
p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
d = json.load(open(p, encoding="utf-8"))
print("top-level type:", type(d).__name__)
if isinstance(d, dict):
    print("keys:", list(d.keys())[:20])
    for k, v in list(d.items())[:5]:
        print("  ", k, "->", type(v).__name__, (len(v) if hasattr(v,'__len__') else ''))
        if isinstance(v, list) and v and isinstance(v[0], dict):
            print("      sample keys:", list(v[0].keys()))
            print("      sample:", json.dumps(v[0], ensure_ascii=False)[:400])
elif isinstance(d, list):
    print("len:", len(d))
    print("sample keys:", list(d[0].keys()))
    print(json.dumps(d[0], ensure_ascii=False)[:400])
