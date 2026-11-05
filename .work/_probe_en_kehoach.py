import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path("02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md")
content = p.read_text(encoding="utf-8")
table_rows = [l for l in content.splitlines() if l.strip().startswith("|") and not l.strip().startswith("|---") and not l.strip().startswith("| Shot")]
print(f"Table rows in KeHoach_Video_Tap02_EN.md: {len(table_rows)}")
print(f"First row: {table_rows[0] if table_rows else ''}")
print(f"Last row: {table_rows[-1] if table_rows else ''}")
