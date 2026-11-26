import json, re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT/".work"/"qc_montage"
src = (ROOT/".work"/"_regen_t36_textfix_v2.py").read_text(encoding="utf-8")
names = re.findall(r'"(t36_a\d_\d+_[a-z0-9_]+)":', src)
print("so anh:", len(names))
try: f = ImageFont.truetype("arial.ttf", 26)
except Exception: f = ImageFont.load_default()
CW, PAD, LAB = 640, 4, 26+8
CH = int(CW*9/16); ROW = CH+LAB+PAD; COLS = 4
rows = (len(names)+COLS-1)//COLS
sheet = Image.new("RGB",(COLS*(CW+PAD), rows*ROW),(8,8,10)); dr = ImageDraw.Draw(sheet)
for i,name in enumerate(names):
    c,r = i%COLS, i//COLS
    im = Image.open(ROOT/"assets"/"bg"/f"{name}.png").convert("RGB").resize((CW,CH), Image.LANCZOS)
    x,y = c*(CW+PAD), r*ROW
    sheet.paste(im,(x,y)); dr.text((x+3,y+CH+3), name[:54], font=f, fill=(235,235,240))
out = W/"regen_v2_check.jpg"; sheet.save(out, quality=90); print("ok", out, sheet.size)
