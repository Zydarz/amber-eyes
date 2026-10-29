import json, os
p = r"D:\TEST\Gax\Audi\provenance.json"
print("exists:", os.path.exists(p))
if os.path.exists(p):
    d = json.load(open(p, encoding="utf-8"))
    print("type:", type(d).__name__, "len:", len(d))
    if isinstance(d, list) and d:
        print("keys:", list(d[0].keys()))
        for e in d:
            if "sfx/t2" in str(e.get("file","")):
                print(json.dumps(e, ensure_ascii=False)[:400]); break
        print("--- so entry sfx:", sum(1 for e in d if "sfx" in str(e.get("file",""))))
        print("--- cac nhom file:", sorted({str(e.get("file","")).split("/")[0] for e in d}))
