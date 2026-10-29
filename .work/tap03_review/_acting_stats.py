import json
from pathlib import Path

W = Path(r"D:\TEST\Gax\Audi\.work")
for ep in ("02", "03"):
    p = W / f"acting_tap{ep}.json"
    if not p.exists():
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    pa = d.get("_pause_after", {})
    acts = {k: v for k, v in d.items() if not k.startswith("_")}
    n = len(acts)
    tot = sum(pa.values())
    print(f"--- Tap{ep}: {n} cau, {len(pa)} nghỉ, tổng {tot:.1f} s ---")
    import collections
    c = collections.Counter(pa.values())
    print("   phan bo:", dict(sorted(c.items())))
    for thr in (0.0, 0.3, 0.4, 0.5):
        keep = {k: v for k, v in pa.items() if v >= thr}
        print(f"   >= {thr}: {len(keep)} nghỉ, {sum(keep.values()):.1f} s")
    emos = collections.Counter(v[0] for v in acts.values())
    print("   cam xuc:", dict(emos))
