import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
jobs = json.load(open(ROOT / ".work/bg_jobs_tap18.json", encoding="utf-8"))

md_lines = [
    "# DANH SÁCH 80 ẢNH NỀN TẬP 18 (CHUẨN FLUX.2 DEEP NOIR 2K)",
    "",
    "> **Hồ sơ:** Lori Vallow & Chad Daybell (Thảm kịch Rexburg, Idaho)  ",
    "> **Kịch bản:** 240 câu thoại (Hệ sinh thái 10 chỉ dấu tâm lý A2c & Luật K10)  ",
    "> **Quy chuẩn kỹ thuật:** `QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` v1.0 (2112×1188, dìm màu Sat 0.65, Contrast 1.15, Vignette 45%, Film Grain 35mm)  ",
    "> **Trạng thái:** 80/80 ảnh đã được render và đồng bộ 100% vào `assets/bg/`  ",
    "",
    "| STT | Tên file | Hồi | Phân đoạn câu | Mô tả bối cảnh & Ẩn dụ noir |",
    "|---|---|:---:|:---:|---|"
]

for idx, j in enumerate(jobs, 1):
    md_lines.append(f"| {idx:02d} | `{j['name']}.png` | Hồi {j['act']} | {j.get('sentences', '')} | {j.get('desc', '')} |")

out_md = ROOT / "02_SAN_XUAT/Tap18/Danh_Sach_Anh_Tap18.md"
out_md.write_text("\n".join(md_lines), encoding="utf-8")
print(f"Đã cập nhật: {out_md}")
