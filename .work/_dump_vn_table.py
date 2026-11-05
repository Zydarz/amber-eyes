# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
p = ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md"
lines = p.read_text(encoding="utf-8").splitlines()
i0 = None
for i, l in enumerate(lines):
    if "DANH S" in l and "SHOT" in l:
        i0 = i
        break
print("i0 =", i0, repr(lines[i0]) if i0 is not None else "")
if i0 is None:
    for i, l in enumerate(lines):
        if l.startswith("#"):
            print(i, repr(l))
    sys.exit(1)
i1 = next(i for i, l in enumerate(lines) if i > i0 and l.startswith("**T"))
out = lines[i0:i1 + 1]
(ROOT / ".work/_vn_table_dump.md").write_text("\n".join(out), encoding="utf-8")
print("rows written:", len(out))
print("\n".join(out[:6]))
