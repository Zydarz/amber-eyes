import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path("02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md")
lines = p.read_text(encoding="utf-8").splitlines()
print(f"Total lines: {len(lines)}")
for l in lines[:50]:
    print(l)
