import sys, json, re
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
from parse_kichban import parse_file
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
old_els = parse_file(ROOT/".work"/"_cu"/"kichban_tap03_22102026_truoc_V9_20261031.md")
new_els = parse_file(ROOT/"01_KICH_BAN"/"Tap03"/"kichban_tap03_22102026.md")
def byel(els):
    return {e["id"]: [s["text"] for s in e.get("sentences",[])] for e in els if e["kind"]=="LOI"}
O, N = byel(old_els), byel(new_els)
print("=== SO CAU THAY DOI THEO ELEMENT ===")
for el in sorted(set(O)|set(N)):
    a,b = len(O.get(el,[])), len(N.get(el,[]))
    flag = "  <<< THAY DOI" if a!=b else ""
    if flag: print(f"  {el}: old {a} -> new {b}{flag}")
print()
print("=== ELEMENT THAY DOI: so sanh text ===")
for el in sorted(set(O)|set(N)):
    if len(O.get(el,[]))==len(N.get(el,[])): continue
    print(f"--- {el} (old {len(O[el])} -> new {len(N[el])}) ---")
    for i in range(max(len(O[el]),len(N[el]))):
        o = O[el][i][:95] if i<len(O[el]) else ""
        n = N[el][i][:95] if i<len(N[el]) else ""
        mark = "  " if o==n else " *"
        print(f"{mark} old#{i+1:<2} {o}")
        print(f"   new#{i+1:<2} {n}")
