import re
from pathlib import Path
from PIL import ImageFont
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8-sig")
print("=== tat ca dong T5 ===")
for l in plan.splitlines():
    if not re.match(r"\|\s*[1-5]-\d+", l): continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c)>3 and "T5" in c[3]:
        big = re.search(r"\*\*(.+?)\*\*", c[5])
        t = big.group(1) if big else ""
        f = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 150)
        w = f.getlength(t)
        for X,lbl in ((140,"X=140"),(560,"X=560")):
            if X + w > 1900:
                print(f"  {c[0]:6s} {lbl}  rong={w:.0f}  -> TRAN KEH {X+w:.0f}px   {t!r}")
            else:
                print(f"  {c[0]:6s} {lbl}  rong={w:.0f}  -> OK ({X+w:.0f}px)  {t!r}")
                break
