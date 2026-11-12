import io, json, os, re, sys
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

tl = json.loads((ROOT/".work/timeline_s_t09.json").read_text(encoding="utf-8"))
items = tl["items"]
acting_vn = json.loads((ROOT/".work/acting_tap09.json").read_text(encoding="utf-8"))
PAUSE_VN = acting_vn.get("_pause_after", {})

print("=== inter-item gaps (VN) vs pause_after ===")
gaps = []
for i in range(1, len(items)):
    a, b = items[i-1], items[i]
    g = round(b["start"] - a["end"], 3)
    gaps.append(g)
from collections import Counter
print("  gap distribution:", Counter(gaps).most_common(14))
print()
print("  sample: sid | gap | pause_after | role_prev->role_cur")
for i in range(1, 14):
    a, b = items[i-1], items[i]
    print(f"   {b['id']:>8} gap={b['start']-a['end']:>6.3f} pause={PAUSE_VN.get(b['id'],'?'):>5} {a['role']}->{b['role']}")

# how much silence total
speech = sum(i["end"]-i["start"] for i in items)
print()
print(f"  speech total = {speech:.2f}s ; timeline total = {tl['total']} ; sil = {tl['total']-speech:.2f}s")
print(f"  first start = {items[0]['start']} ; last end = {items[-1]['end']}")

# char counts per language
print()
print("=== char counts ===")
KB = {"vi": "01_KICH_BAN/Tap09/kichban_tap09_23102026.md",
      "en": "01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md",
      "ja": "01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md"}
CH = {}
for lang, rel in KB.items():
    els = parse_file(str(ROOT/rel))
    d = {}
    for e in els:
        if e["kind"] != "LOI": continue
        for i, s in enumerate(e["sentences"], 1):
            d[f"{e['id']}#{i}"] = s["text"]
    CH[lang] = d
    print(f"  {lang}: n={len(d)} total_chars={sum(len(v) for v in d.values())}")
print("  ids identical across langs:", list(CH['vi'])==list(CH['en'])==list(CH['ja']))

# pause_after comparison
for lang, f in [("EN","acting_tap09_EN.json"), ("JA","acting_tap09_JA.json")]:
    a = json.loads((ROOT/".work"/f).read_text(encoding="utf-8"))
    p = a.get("_pause_after", {})
    same = sum(1 for k,v in PAUSE_VN.items() if p.get(k)==v)
    print(f"  pause_after {lang}: n={len(p)} · trùng VN {same}/{len(PAUSE_VN)} · max={max(p.values()) if p else 0} · mean={sum(p.values())/len(p):.3f}")
print(f"  pause_after VN: n={len(PAUSE_VN)} · max={max(PAUSE_VN.values())} · mean={sum(PAUSE_VN.values())/len(PAUSE_VN):.3f}")
