import io, json, os, re, sys
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

tl = json.loads((ROOT/".work/timeline_s_t09.json").read_text(encoding="utf-8"))
items = tl["items"]
print("=== timeline items sample (first 3 of each act) ===")
seen = {}
for it in items:
    a = it["act"]
    seen.setdefault(a, []).append(it)
for a in sorted(seen):
    for it in seen[a][:2]:
        print(f"  {it['id']:>8} act={a} role={it['role']} {it['start']:>8.2f}-{it['end']:>8.2f} len={it['end']-it['start']:>5.2f} | {it['text'][:55]}")

print()
print("=== markers sample ===")
for m in tl["markers"][:14]:
    print("  ", json.dumps(m, ensure_ascii=False)[:150])

print()
print("=== acts ===")
print(" ", tl["acts"])

print()
print("=== element -> sentences in script vs timeline ===")
els = parse_file(str(ROOT/"01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))
tl_ids = [i["id"] for i in items]
sc_ids = [f"{e['id']}#{k}" for e in els if e["kind"]=="LOI" for k in range(1, len(e.get("sentences",[]))+1)]
print("  timeline ids:", len(tl_ids), "script ids:", len(sc_ids), "IDENTICAL ORDER:", tl_ids == sc_ids)

print()
print("=== role sequence ===")
from collections import Counter
print(" ", Counter(i["role"] for i in items))

print()
print("=== element roles in script (for N1/N2) ===")
for e in els:
    if e["kind"]=="LOI":
        print(f"  {e['id']:>6} role={e['role']:>4} n={len(e.get('sentences',[]))}")
