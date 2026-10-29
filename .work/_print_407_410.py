import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

s_vn = json.load(open(".work/script_tap02.json", encoding="utf-8"))
s_en = json.load(open(".work/script_tap02_EN.json", encoding="utf-8"))

for tid in ["4.07", "4.10"]:
    ev = next(e for e in s_vn if e["id"] == tid)
    ee = next(e for e in s_en if e["id"] == tid)
    print(f"\n=== ELEMENT {tid} ({ev['role']}) — {len(ev['sentences'])} sentences ===")
    for sv, se in zip(ev["sentences"], ee["sentences"]):
        print(f"[{sv['id']}]")
        print(f"  VN: {sv['text']}")
        print(f"  EN: {se['text']}")
