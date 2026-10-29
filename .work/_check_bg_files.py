import json, re, sys
from pathlib import Path

bg_dir = Path("assets/bg")
ds = open("02_SAN_XUAT/Tap05/Danh_Sach_Anh_Tap05.md", encoding="utf-8").read()
names = re.findall(r'`(t5_[a-z0-9_]+)`', ds)
print(f"Found {len(set(names))} unique background names in Danh_Sach_Anh")

missing = [n for n in set(names) if not (bg_dir / f"{n}.png").exists()]
print(f"Missing background files: {missing}")
