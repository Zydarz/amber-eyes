import re
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path("02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md")
content = p.read_text(encoding="utf-8")
table_lines = [l for l in content.splitlines() if l.strip().startswith("|") and not l.strip().startswith("|---") and not l.strip().startswith("| Shot")]

print(f"Total shot rows in KeHoach_Video_Tap02_JA.md: {len(table_lines)}")

# Check git diff of KeHoach_Video_Tap02_JA.md between 5e9910b9 and HEAD
import subprocess
cmd = ["git", "diff", "5e9910b9..HEAD", "--", "02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print(f"Diff of KeHoach lines: {len(res.stdout.splitlines())}")
if len(res.stdout.splitlines()) < 100:
    print(res.stdout)
else:
    for l in res.stdout.splitlines()[:40]:
        print(l)
