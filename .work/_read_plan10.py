import os, sys
from pathlib import Path

ROOT = Path(r"d:\TEST\Gax\amber-eyes")
plan_path = ROOT / "02_SAN_XUAT/Tap10/KeHoach_Video_Tap10.md"
print(plan_path.read_text(encoding="utf-8")[:1500])
