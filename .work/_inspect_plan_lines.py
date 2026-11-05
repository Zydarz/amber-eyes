import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
plan = open("02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md", encoding="utf-8").read()

shot_ids = ["1-07", "1-08", "1-09", "1-14", "1-15", "2-16", "2-17", "2-18", "2-19",
            "2-20", "2-21", "2-22", "2-23", "2-24", "3-20", "3-21", "3-22", "3-23",
            "5-13", "5-14", "5-15", "5-16", "5-19", "5-20", "5-23", "5-24"]

for l in plan.splitlines():
    for sid in shot_ids:
        if re.match(rf"\|\s*{sid}\s*\|", l):
            print(l)
