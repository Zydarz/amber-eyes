import io, json, os, re, sys
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

print("=== sentence count: CURRENT vs PRE-REWRITE backup ===")
for label, rel in [
    ("CURRENT  01_KICH_BAN/Tap09", "01_KICH_BAN/Tap09/kichban_tap09_23102026.md"),
    ("BACKUP   _cu/kichban_tap09_23102026_truoc_soat_20261101", ".work/_cu/kichban_tap09_23102026_truoc_soat_20261101.md"),
    ("BACKUP   _cu/tap09_pre_10chiau_20261105", ".work/_cu/tap09_pre_10chiau_20261105/kichban_tap09_23102026.md"),
]:
    p = ROOT/rel
    if not p.exists():
        print(f"  {label}: MISSING"); continue
    els = parse_file(str(p))
    n = sum(len(e.get("sentences", [])) for e in els if e["kind"]=="LOI")
    nel = sum(1 for e in els if e["kind"]=="LOI")
    print(f"  {label}: sentences={n} LOI_elements={nel} all_elements={len(els)}")

print()
print("=== VN timeline per-sentence durations (H10: 3-15 s) ===")
tl = json.loads((ROOT/".work/timeline_s_t09.json").read_text(encoding="utf-8"))
d = [round(i["end"]-i["start"],2) for i in tl["items"]]
d_sorted = sorted(d)
print(f"  n={len(d)} min={min(d)} max={max(d)} median={d_sorted[len(d)//2]}")
out = [x for x in d if x < 3.0 or x > 15.0]
print(f"  ngoài [3,15]: {len(out)} -> {sorted(out)[:15]}")
print(f"  total={tl['total']} intro={tl['intro']} last_end={tl['items'][-1]['end']}")

print()
print("=== FORBIDDEN WORD scan (A9.2) on current VN script ===")
els = parse_file(str(ROOT/"01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))
texts = [(f"{e['id']}#{i}", s["text"]) for e in els if e["kind"]=="LOI"
         for i,s in enumerate(e.get("sentences",[]),1)]
VI = ["sát hại","thi thể","máu","đòn","trói","bầm","đập","đầu độc","diệt cỏ","bỏ đói",
      "móc áo","đồ lót","quan hệ tình dục","hiếp","cưỡng ép","giết","xác chết","nạn nhân bị giết"]
hits = []
for sid, t in texts:
    low = t.lower()
    for w in VI:
        if w in low:
            hits.append((sid, w, t[:90]))
print(f"  câu chứa từ cấm: {len(hits)}")
for h in hits[:25]: print("   ", h)
