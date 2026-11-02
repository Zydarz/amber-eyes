import sys, os
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
os.environ["AE_EP"]="03"
import edition as ED
from PIL import ImageFont, ImageDraw, Image
F_LAB = ImageFont.truetype(r"C:\Windows\Fonts\bahnschrift.ttf", 24)
print("ROLE_NAME:")
for r,(n,t) in ED.ROLE_NAME.items():
    bb = ImageDraw.Draw(Image.new("RGB",(10,10))).textbbox((0,0), n, font=F_LAB)
    w = bb[2]-bb[0]
    print(f"  {r}: {n!r}  width={w}px  {'<<< TRAN 350px (badge 470 - 120) -> BI CAT' if w>350 else ''}")
    print(f"      title={t!r}")
print()
print("UI:", ED.UI)
