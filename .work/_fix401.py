import re, sys
from pathlib import Path
P = Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03\KeHoach_Video_Tap03.md")
t = P.read_text(encoding="utf-8-sig")
old = "| 4-01 | `4.02#1`–`#3` | H | T5 ngày | `t3_vacaville_1978` | **NĂM 1978 · VACAVILLE** · *Cơ sở Y tế Bang California (CMF)*"
new = "| 4-01 | `4.02#1`–`#3` | H | T5 ngày | `t3_vacaville_1978` | **1978 · VACAVILLE** · *Cơ sở Y tế Bang California (CMF)*"
assert t.count(old) == 1, t.count(old)
P.write_text(t.replace(old, new), encoding="utf-8")
print("[OK ] 4-01: 'NĂM 1978 · VACAVILLE' -> '1978 · VACAVILLE'")
