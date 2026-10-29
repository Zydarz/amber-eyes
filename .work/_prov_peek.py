import json, pathlib
p=pathlib.Path("provenance.json")
d=json.loads(p.read_text(encoding="utf-8"))
print("type:", type(d).__name__, "| len:", len(d))
if isinstance(d, dict):
    ks=list(d.keys()); print("top keys:", ks[:12])
    for k in ks[:2]:
        v=d[k]
        print(f"\n--- {k} ({type(v).__name__}, len {len(v) if hasattr(v,'__len__') else '-'}) ---")
        print(json.dumps(v, ensure_ascii=False)[:900])
else:
    print(json.dumps(d[:2], ensure_ascii=False, indent=1)[:1500])
