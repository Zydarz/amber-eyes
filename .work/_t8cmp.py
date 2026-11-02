import re
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
for ep, f in (("02","02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md"), ("03","02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md")):
    plan = (ROOT/f).read_text(encoding="utf-8-sig")
    print(f"===== TAP {ep}: cac dong T8 =====")
    n=0
    for l in plan.splitlines():
        if not re.match(r"\|\s*[1-5]-\d+", l): continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c)>3 and "T8" in c[3]:
            print(f"  {c[0]:6s} | {c[3]:22s} | {c[5][:105]}")
            n+=1
    print(f"  ({n} dong)\n")
