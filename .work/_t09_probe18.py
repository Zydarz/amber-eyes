import io, json, os, re, sys
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

els = parse_file(str(ROOT/"01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))
TXT = {}
for e in els:
    if e["kind"] != "LOI": continue
    for i, s in enumerate(e["sentences"], 1):
        TXT[f"{e['id']}#{i}"] = s["text"]

print("=== CÂU NGOÀI [3,15] s THEO TỪNG NGÔN NGỮ ===")
for lang, f in [("VN","timeline_s_t09.json"), ("EN","timeline_s_EN_t09.json"), ("JA","timeline_s_JA_t09.json")]:
    tl = json.loads((ROOT/".work"/f).read_text(encoding="utf-8"))
    out = [(it["id"], round(it["end"]-it["start"],2)) for it in tl["items"]
           if not (3.0 <= it["end"]-it["start"] <= 15.0)]
    print(f"\n  {lang}: {len(out)} câu ngoài khoảng")
    for sid, d in out:
        print(f"    {sid:>8} {d:>6}s | {TXT[sid][:95]}")

print()
print("=== NHÓM CÂU NGUY HIỂM (ngắn <3s) — cần GOM với câu kế ===")
tl = json.loads((ROOT/".work/timeline_s_t09.json").read_text(encoding="utf-8"))
by_el = {}
for it in tl["items"]:
    by_el.setdefault(it["element"], []).append(it)
for el, its in by_el.items():
    short = [(i["id"], round(i["end"]-i["start"],2)) for i in its if i["end"]-i["start"] < 3.0]
    if short:
        print(f"  {el}: {[x[0] for x in short]}  (tổng element={sum(i['end']-i['start'] for i in its):.1f}s, {len(its)} câu)")
        for i in its:
            print(f"      {i['id']:>8} {i['end']-i['start']:>5.2f}s")
