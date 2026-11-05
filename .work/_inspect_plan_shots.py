import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

plan = Path("02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
lines = [l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]

for l in lines[:15]:
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    print(f"{cells[0]:5s} | {cells[1]:20s} | {cells[2]:5s} | {cells[3]:10s} | {cells[4]:20s}")
