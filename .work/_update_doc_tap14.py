import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

jobs = json.load(open(WORK / "bg_jobs_tap14.json", encoding="utf-8"))
doc_path = ROOT / "02_SAN_XUAT" / "Tap14" / "Danh_Sach_Anh_Tap14.md"

lines = [
    "# DANH SÁCH ẢNH NỀN — TẬP 14 'KHI NẠN NHÂN GASLIGHTING BƯỚC QUA RANH GIỚI TỘI ÁC'",
    "",
    "*Hồ sơ Betty Broderick & Thao túng thực tại (Gaslighting) — Bi kịch hôn nhân triệu đô tại San Diego.*",
    "*Phiên bản mở rộng hoàn chỉnh: 77 ảnh nền 2K (tránh lặp nền theo quy chuẩn H10 & Deep Noir Kaggle FLUX).*",
    "",
    "---",
    "",
    "## B1. Thông tin bộ ảnh",
    "",
    "| Mục | Nội dung |",
    "|---|---|",
    "| **Số ảnh chuẩn hóa** | **77 ảnh** phục vụ trọn vẹn 5 hồi (210 câu thoại kịch bản A2c) |",
    "| **Kích thước chuẩn** | `2112×1188` (16:9 2K), lưu trữ tại `assets/bg/t14_*.png` |",
    "| **Tỷ lệ bao phủ** | ~2.7 shot/ảnh (triệt tiêu hoàn toàn nguy cơ lặp ảnh > 4 shot theo luật H10) |",
    "| **Phong cách nghệ thuật** | Deep Graphic Novel Noir — Chiaroscuro tâm lý học, dìm màu tro lạnh, hạt phim 35mm |",
    "| **Engine thực thi** | `black-forest-labs/FLUX.2-klein-4B` trên Kaggle GPU (Tesla T4) |",
    "| **Sổ nguồn gốc tài sản** | Đầy đủ 77 bản ghi trong `provenance.json` (Luật L7) |",
    "",
    "## B2. Phân bổ chi tiết 77 ảnh theo 5 Hồi",
    ""
]

for act in range(1, 6):
    act_jobs = [j for j in jobs if j.get("act") == act]
    lines.append(f"### Hồi {act} ({len(act_jobs)} ảnh)")
    for j in act_jobs:
        lines.append(f"- `{j['name']}`: {j.get('desc', '')}")
    lines.append("")

doc_path.write_text("\n".join(lines), encoding="utf-8")
print("Updated successfully:", doc_path)
