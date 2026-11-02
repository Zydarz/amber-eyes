import re
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]; sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
for l in sec.splitlines():
    if re.match(r"\|\s*(4-09|4-10|4-11)\s", l): print(l)
