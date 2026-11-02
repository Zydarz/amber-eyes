import sys, re, difflib
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
from parse_kichban import parse_file
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
old_els = parse_file(ROOT/".work"/"_cu"/"kichban_tap03_22102026_truoc_V9_20261031.md")
new_els = parse_file(ROOT/"01_KICH_BAN"/"Tap03"/"kichban_tap03_22102026.md")
def byel(els):
    return {e["id"]: [s["text"] for s in e.get("sentences",[])] for e in els if e["kind"]=="LOI"}
O, N = byel(old_els), byel(new_els)
def norm(s): return re.sub(r"\s+"," ", s).strip()
diffs = 0
for el in sorted(set(O)|set(N)):
    o, n = O.get(el,[]), N.get(el,[])
    if len(o)==len(n):
        for i,(a,b) in enumerate(zip(o,n)):
            if norm(a)!=norm(b):
                diffs += 1
                print(f"* {el}#{i+1} TEXT DOI:")
                print(f"    old: {norm(a)[:160]}")
                print(f"    new: {norm(b)[:160]}")
print(f"\nTong so cau DOI CHU (cung so luong): {diffs}")
