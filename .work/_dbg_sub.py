import re
from pathlib import Path
p=Path("02_SAN_XUAT/Danh_Sach_SFX_Tap03-29.md")
lines=p.read_text(encoding="utf-8").splitlines()
i0=next(i for i,l in enumerate(lines) if l.startswith("### 4.2"))
i1=next(i for i,l in enumerate(lines) if i>i0 and l.startswith("## 5."))
print("4.2 lines:", i0, i1)
print("HEADER:", lines[i0+1][:200])
for l in lines[i0:i1]:
    if "thay th" in l.lower():
        print("  ", l[:230])
