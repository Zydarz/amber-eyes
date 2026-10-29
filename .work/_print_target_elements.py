import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

s_vn = json.load(open(".work/script_tap02.json", encoding="utf-8"))
s_en = json.load(open(".work/script_tap02_EN.json", encoding="utf-8"))

target_ids = ["2.04", "2.08", "4.05", "4.06", "4.07", "4.10", "4.11", "4.12", "5.08"]

for tid in target_ids:
    ev = next(e for e in s_vn if e["id"] == tid)
    ee = next(e for e in s_en if e["id"] == tid)
    print(f"\n=======================================================")
    print(f"=== ELEMENT {tid} ({ev['role']}) — {len(ev['sentences'])} sentences ===")
    for sv, se in zip(ev["sentences"], ee["sentences"]):
        print(f"[{sv['id']}]")
        print(f"  VN: {sv['text']}")
        print(f"  EN: {se['text']}")
