# -*- coding: utf-8 -*-
"""Tạo các tờ montage QC cho 124 ảnh nền Tập 20.
Quy chuẩn AGENTS.md (H20, A11 #172): ô >= 512px, 4 cột x 4 hàng, 16 ảnh/tờ.
"""
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work/kaggle_flux"))
from t20_jobs_124_data import JOBS_124

bg_dir = ROOT / "assets/bg"
out_dir = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap20/qc_montage"
out_dir.mkdir(parents=True, exist_ok=True)

cell_w, cell_h = 512, 288
cols, rows = 4, 4
per_sheet = cols * rows

total_sheets = math.ceil(len(JOBS_124) / per_sheet)
print(f"Bắt đầu dựng {total_sheets} tờ montage (mỗi tờ 16 ô 512x288)...")

for sheet_idx in range(total_sheets):
    sheet_jobs = JOBS_124[sheet_idx * per_sheet : (sheet_idx + 1) * per_sheet]
    montage = Image.new("RGB", (cell_w * cols, cell_h * rows), color=(15, 15, 15))
    draw = ImageDraw.Draw(montage)
    
    for idx, j in enumerate(sheet_jobs):
        c = idx % cols
        r = idx // cols
        x = c * cell_w
        y = r * cell_h
        
        p = bg_dir / f"{j['name']}.png"
        if p.exists():
            with Image.open(p) as img:
                thumb = img.resize((cell_w, cell_h), Image.Resampling.LANCZOS)
                montage.paste(thumb, (x, y))
        
        # Label bar
        num = sheet_idx * per_sheet + idx + 1
        label = f"#{num:03d} [{j['act']}] {j['name']}"
        draw.rectangle([x, y + cell_h - 26, x + cell_w, y + cell_h], fill=(0, 0, 0))
        draw.text((x + 6, y + cell_h - 20), label[:50], fill=(250, 250, 250))
        
    out_path = out_dir / f"montage_t20_sheet_{sheet_idx + 1}.png"
    montage.save(out_path, quality=90)
    print(f"  -> Đã lưu: {out_path.name}")

print("\nHoàn tất tạo 8 tờ montage QC!")
