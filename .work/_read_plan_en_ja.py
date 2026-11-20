import os, sys
from pathlib import Path

ROOT = Path(r"d:\TEST\Gax\amber-eyes")
plan_en = ROOT / "02_SAN_XUAT/Tap39_EN/Production_Plan_Tap39_EN.md"
plan_ja = ROOT / "02_SAN_XUAT/Tap39_JA/Production_Plan_Tap39_JA.md"

print("--- EN ---")
print(plan_en.read_text(encoding="utf-8"))
print("--- JA ---")
print(plan_ja.read_text(encoding="utf-8"))
