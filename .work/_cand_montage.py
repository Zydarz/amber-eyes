import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT/".work"/"qc_montage"
det = json.loads((ROOT/".work"/"_text_detect_t36.json").read_text(encoding="utf-8"))
done = {"t36_a1_05_small_fiat_leaving_florence_night","t36_a3_29_quantico_profile_1989_loner_manual_laborer_map",
        "t36_a4_06_postman_bicycle_and_slow_lonely_silhouette","t36_a2_23_man_turned_away_from_police_station_door",
        "t36_a2_32_patrol_car_hill_road_exhausted_vigil","t36_a3_09_envelope_cut_out_letters_blank_collage",
        "t36_a3_20_detective_timeline_gaps_calendar_wall"}
cand = [d["name"] for d in det if d["n"] > 0 and d["name"] not in done]
cand = [c for c in cand if (ROOT/"assets"/"bg"/f"{c}.png").exists()]
print("ung vien:", len(cand))
try: f = ImageFont.truetype("arial.ttf", 26)
except Exception: f = ImageFont.load_default()
CW, PAD, LAB = 640, 4, 26+8
CH = int(CW*9/16); ROW = CH+LAB+PAD
COLS = 4
for part in range(0, len(cand), 32):
    chunk = cand[part:part+32]
    rows = (len(chunk)+COLS-1)//COLS
    sheet = Image.new("RGB",(COLS*(CW+PAD), rows*ROW),(8,8,10)); dr = ImageDraw.Draw(sheet)
    for i,name in enumerate(chunk):
        c,r = i%COLS, i//COLS
        im = Image.open(ROOT/"assets"/"bg"/f"{name}.png").convert("RGB").resize((CW,CH), Image.LANCZOS)
        x,y = c*(CW+PAD), r*ROW
        sheet.paste(im,(x,y)); dr.text((x+3,y+CH+3), name[:52], font=f, fill=(235,235,240))
    out = W/f"cand_{part//32}.jpg"; sheet.save(out, quality=90)
    print("ok", out.name, sheet.size, len(chunk))
