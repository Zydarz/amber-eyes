import re
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path("02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md")
content = p.read_text(encoding="utf-8")

for sid in ['1-33', '1-34', '1-35', '2-25', '3-31', '5-29', '5-30', '5-36']:
    found = re.findall(rf"\|?\s*{sid}\s*\|", content)
    print(f"Shot {sid} in KeHoach: {found}")
