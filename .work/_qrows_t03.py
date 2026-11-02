import re
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]; sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
want = {"1-08","1-09","1-12","1-13","1-14","1-15","2-20","2-21","2-22","4-08","4-09","5-14","5-15"}
for l in sec.splitlines():
    if not re.match(r"\|\s*[1-5]-\d+", l): continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if c[0] in want: print(l)
