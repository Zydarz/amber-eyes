import json
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
W = ROOT / ".work"

for ep, ids in [("02", ["1.06", "1.09", "1.16"]),
                ("04", ["1.06", "1.09", "1.10", "4.05"]),
                ("03", ["1.01", "1.02", "1.10", "1.11", "1.14", "3.01", "4.01", "5.01", "5.12"])]:
    f = W / f"script_tap{ep}.json"
    if not f.exists():
        print(f"tap{ep}: KHONG CO {f.name}")
        continue
    els = json.load(open(f, encoding="utf-8"))
    byid = {e["id"]: e for e in els}
    print(f"\n--- Tap{ep} ---")
    for i in ids:
        e = byid.get(i)
        if not e:
            print(f"  {i:<6} (khong ton tai)")
            continue
        k = e["kind"]
        d = e.get("desc", "") or (e.get("sentences", [{}])[0].get("text", "") if k == "LOI" else "")
        print(f"  {i:<6} [{k:<4}] {d[:92]}")
