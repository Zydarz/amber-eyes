import sys
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work/kaggle_flux"))
import t19_jobs_61_data

ds_path = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap19/Danh_Sach_Anh_Tap19.md"
lines = ds_path.read_text(encoding="utf-8")

if "## ẢNH BỔ SUNG THEO QUY CHUẨN MỚI (H22 & H25)" not in lines:
    md_out = lines.rstrip() + "\n\n## ẢNH BỔ SUNG THEO QUY CHUẨN MỚI (H22 & H25)\n\n"
    md_out += "| STT | Tên file | Hồi | Câu thoại | Mô tả bối cảnh noir |\n|---|---|:---:|---|---|\n"
    for i, j in enumerate(t19_jobs_61_data.JOBS_61, 85):
        s_range = ", ".join(j["sids"])
        md_out += f"| {i} | `{j['name']}.png` | Hồi {j['act']} | {s_range} | {j['desc']} |\n"
    ds_path.write_text(md_out, encoding="utf-8")
    print("Đã cập nhật Danh_Sach_Anh_Tap19.md thành công!")
else:
    print("Danh_Sach_Anh_Tap19.md đã có phần bổ sung.")
