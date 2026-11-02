import re
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8-sig")
for l in plan.splitlines():
    if re.match(r"\|\s*(1-01|2-06)\s", l):
        print(repr(l))
