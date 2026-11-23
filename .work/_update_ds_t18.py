# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work/kaggle_flux"))
import t18_jobs_61_data

ds_path = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap18/Danh_Sach_Anh_Tap18.md"
lines = ds_path.read_text(encoding="utf-8")

if "## ẢNH BỔ SUNG THEO QUY CHUẨN MỚI (H22 & H25)" not in lines:
    md_out = lines.rstrip() + "\n\n## ẢNH BỔ SUNG THEO QUY CHUẨN MỚI (H22 & H25)\n\n"
    md_out += "| STT | Tên file | Hồi | Mô tả bối cảnh noir |\n|---|---|:---:|---|\n"
    for i, j in enumerate(t18_jobs_61_data.JOBS_61, 81):
        md_out += f"| {i} | `{j['name']}.png` | Hồi {j['act']} | {j['desc']} |\n"
    ds_path.write_text(md_out, encoding="utf-8")
    print("Da cap nhat Danh_Sach_Anh_Tap18.md thanh cong!")
else:
    print("Danh_Sach_Anh_Tap18.md da co phan bo sung.")
