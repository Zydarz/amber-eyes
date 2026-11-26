import json, re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
p = json.loads((ROOT/"provenance.json").read_text(encoding="utf-8"))
t36 = [r for r in p if r["file"].startswith("assets/bg/t36_")]
print("provenance t36:", len(t36))
names = re.findall(r'"(t36_a\d_\d+_[a-z0-9_]+)":', (ROOT/".work"/"_regen_t36_textfix_v3.py").read_text(encoding="utf-8"))
miss = [n for n in names if f"assets/bg/{n}.png" not in {r["file"] for r in p}]
print("thieu provenance:", miss)
W = ROOT/".work"/"qc_montage"
try: f = ImageFont.truetype("arial.ttf", 26)
except Exception: f = ImageFont.load_default()
CW, PAD, LAB = 640, 4, 26+8; CH = int(CW*9/16); ROW = CH+LAB+PAD; COLS = 3
rows = (len(names)+COLS-1)//COLS
sheet = Image.new("RGB",(COLS*(CW+PAD), rows*ROW),(8,8,10)); dr = ImageDraw.Draw(sheet)
for i,name in enumerate(names):
    c,r = i%COLS, i//COLS
    im = Image.open(ROOT/"assets"/"bg"/f"{name}.png").convert("RGB").resize((CW,CH), Image.LANCZOS)
    x,y = c*(CW+PAD), r*ROW
    sheet.paste(im,(x,y)); dr.text((x+3,y+CH+3), name[:54], font=f, fill=(235,235,240))
out = W/"regen_v3_check.jpg"; sheet.save(out, quality=90); print("ok", out, sheet.size, len(names))
