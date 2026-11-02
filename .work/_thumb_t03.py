import re
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8-sig")
for kw in ("THUMB", "thumbnail", "THUMBNAIL"):
    for m in re.finditer(kw, plan):
        s = max(0, m.start()-120); e = min(len(plan), m.start()+600)
        print(f"--- {kw} @ {m.start()} ---")
        print(plan[s:e])
        print()
        break
print("=== mo_ta.txt ===")
print((ROOT/"02_SAN_XUAT"/"Tap03"/"xuat_ban"/"mo_ta.txt").read_text(encoding="utf-8-sig")[:900])
