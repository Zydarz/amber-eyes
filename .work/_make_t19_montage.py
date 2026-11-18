import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
OUT_MONTAGE = ROOT / ".work/qc_montage_t19"
OUT_MONTAGE.mkdir(parents=True, exist_ok=True)

jobs_61 = json.loads((ROOT / ".work/bg_jobs_tap19_new61.json").read_text(encoding="utf-8"))

for act in range(1, 6):
    act_jobs = [j for j in jobs_61 if j["act"] == act]
    if not act_jobs:
        continue
    
    cell_w, cell_h = 528, 297  # Tỷ lệ 16:9 (1/4 kích thước 2112x1188)
    cols = 3
    rows = (len(act_jobs) + cols - 1) // cols
    
    montage = Image.new("RGB", (cols * cell_w, rows * (cell_h + 30)), (15, 15, 15))
    draw = ImageDraw.Draw(montage)
    
    for idx, j in enumerate(act_jobs):
        c = idx % cols
        r = idx // cols
        x = c * cell_w
        y = r * (cell_h + 30)
        
        img_path = ROOT / f"assets/bg/{j['name']}.png"
        if img_path.exists():
            with Image.open(img_path) as im:
                im_thumb = im.resize((cell_w, cell_h), Image.Resampling.LANCZOS)
                montage.paste(im_thumb, (x, y))
        else:
            draw.rectangle([x, y, x + cell_w, y + cell_h], fill=(50, 0, 0))
            
        label = f"[{act}] {j['name'][:35]}"
        draw.text((x + 10, y + cell_h + 6), label, fill=(220, 220, 220))
        
    out_file = OUT_MONTAGE / f"montage_t19_new61_act{act}.png"
    montage.save(out_file, quality=92)
    print(f"Đã tạo montage Hồi {act}: {out_file}")
