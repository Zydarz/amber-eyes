# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work/kaggle_flux"))
import t18_jobs_61_data
from PIL import Image, ImageDraw
import os, math

jobs = t18_jobs_61_data.JOBS_61
acts = {}
for j in jobs:
    acts.setdefault(j['act'], []).append(j)

out_dir = ROOT / ".work/qc_montage_t18"
out_dir.mkdir(parents=True, exist_ok=True)

for act, act_jobs in acts.items():
    n = len(act_jobs)
    cols = 4
    rows = math.ceil(n / cols)
    w_thumb, h_thumb = 528, 297
    montage = Image.new('RGB', (cols * w_thumb, rows * h_thumb), (20, 20, 20))
    draw = ImageDraw.Draw(montage)
    
    for idx, j in enumerate(act_jobs):
        r = idx // cols
        c = idx % cols
        x = c * w_thumb
        y = r * h_thumb
        fpath = ROOT / "assets/bg" / (j['name'] + ".png")
        im = Image.open(fpath).resize((w_thumb, h_thumb), Image.Resampling.LANCZOS)
        montage.paste(im, (x, y))
        draw.rectangle([x, y, x + w_thumb, y + 25], fill=(0, 0, 0))
        label = f"{idx+1}. {j['name']}"
        draw.text((x + 8, y + 5), label, fill=(255, 255, 255))
    
    out_p = out_dir / f"montage_t18_new61_act{act}.png"
    montage.save(out_p)
    print(f"Da luu: {out_p} ({n} anh)")
