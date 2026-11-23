import os, sys
from pathlib import Path

ROOT = Path(r"d:\TEST\Gax\amber-eyes")
plan_path = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap39/KeHoach_Video_Tap39.md"
print(plan_path.read_text(encoding="utf-8"))
