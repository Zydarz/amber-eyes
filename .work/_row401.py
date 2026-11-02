import re, json
from pathlib import Path
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8-sig")
for l in plan.splitlines():
    if re.match(r"\|\s*(4-01|4-15|5-01|1-01)\s", l): print(l)
print()
from PIL import ImageFont
f = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 150)
for s in ("NĂM 1978 · VACAVILLE CMF","24 · 4 · 1973","1978 · VACAVILLE CMF"):
    print(f"  {s!r}: {f.getlength(s):.0f}px  (khung 1920, bat dau X=140)")
