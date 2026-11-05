import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
plan = Path("02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md").read_text(encoding="utf-8")
for l in plan.splitlines():
    if any(x in l for x in ['3-12', '3-13', '3-14', '3-15', '3-16']):
        print(l)
