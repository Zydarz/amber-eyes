import sys, json
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
from parse_kichban import parse_file
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
vers = {
 "BAN_GOC_10/22": ROOT/"01_KICH_BAN"/"Tap03"/"kichban_tap03_22102026_ban_goc.md",
 "TRUOC_V9_10/31_11h": ROOT/".work"/"_cu"/"kichban_tap03_22102026_truoc_V9_20261031.md",
 "HIEN_TAI_10/31_20h": ROOT/"01_KICH_BAN"/"Tap03"/"kichban_tap03_22102026.md",
}
res = {}
for name, p in vers.items():
    if not p.exists():
        print("MISSING", p); continue
    els = parse_file(p)
    n = sum(len(e.get("sentences",[])) for e in els if e["kind"]=="LOI")
    res[name] = {e["id"]: [s["text"] for s in e.get("sentences",[])] for e in els if e["kind"]=="LOI"}
    print(f"{name}: {n} cau")
print()
for el in ("2.07","5.02"):
    print("="*80)
    print("ELEMENT", el)
    for name in res:
        s = res[name].get(el, [])
        print(f"  {name}: {len(s)} cau")
        for i,t in enumerate(s,1):
            print(f"     #{i:<2} {t[:120]}")
        print()
