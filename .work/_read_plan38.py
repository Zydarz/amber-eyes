import os, sys
from pathlib import Path

ROOT = Path(r"d:\TEST\Gax\amber-eyes")
plan_path = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap38/KeHoach_Video_Tap38.md"
if plan_path.exists():
    print(plan_path.read_text(encoding="utf-8")[:1500])
else:
    print("Tap 38 plan not found")
