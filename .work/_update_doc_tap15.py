import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
jobs = json.load(open(WORK / "bg_jobs_tap15.json", encoding="utf-8"))
doc_path = ROOT / "02_SAN_XUAT" / "Tap15" / "Danh_Sach_Anh_Tap15.md"

lines = [
    "# DANH SÁCH ẢNH NỀN — TẬP 15 'CƠN CUỒNG GHEN RỐI LOẠN NHÂN CÁCH RANH GIỚI'",
    "",
    "*Hồ sơ Travis Alexander & Jodi Arias — Bi kịch cuồng ghen và thao túng tâm lý tại Mesa, Arizona.*",
    "*Phiên bản tạo lại bằng Kaggle FLUX.2 theo chuẩn Deep Noir Chiaroscuro (QUY_TAC_TAO_ANH_KAGGLE_FLUX.md v1.0).*",
    "",
    "---",
    "",
    "## B1. Thông tin bộ ảnh",
    "",
    "| Mục | Nội dung |",
    "|---|---|",
    "| **Số ảnh chuẩn hóa** | **63 ảnh** phục vụ trọn vẹn 5 hồi (220 câu thoại kịch bản A2c 10 chỉ dấu) |",
    "| **Kích thước chuẩn** | `2112×1188` (16:9 2K), lưu trữ tại `assets/bg/t15_*.png` |",
    "| **Phong cách nghệ thuật** | Deep Graphic Novel Noir — Chiaroscuro tâm lý học, dìm màu tro lạnh (sat 0.65, contrast 1.15), vignette góc tối, hạt phim 35mm |",
    "| **Engine thực thi** | `black-forest-labs/FLUX.2-klein-4B` trên Kaggle GPU (Tesla T4) |",
    "| **Ràng buộc thị giác (V5/V9)** | 100% không mặt trực diện người thật, bóng lưng/chiaroscuro, không bạo lực gore, 0 chữ viết AI |",
    "| **Sổ nguồn gốc tài sản** | Đầy đủ 63 bản ghi trong `provenance.json` (Luật L7) |",
    "",
    "## B2. Phân bổ chi tiết 63 ảnh theo 5 Hồi",
    ""
]

for act in range(1, 6):
    act_jobs = [j for j in jobs if j.get("act") == act]
    lines.append(f"### Hồi {act} ({len(act_jobs)} ảnh)")
    for j in act_jobs:
        first_desc = j.get("desc", "").splitlines()[0]
        lines.append(f"- `{j['name']}`: {first_desc}")
    lines.append("")

doc_path.write_text("\n".join(lines), encoding="utf-8")
print("Updated successfully:", doc_path)
