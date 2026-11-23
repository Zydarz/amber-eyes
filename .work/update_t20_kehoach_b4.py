# -*- coding: utf-8 -*-
"""Cập nhật mục B4 trong KeHoach_Video_Tap20.md với 124 ảnh nền chuẩn H25."""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work/kaggle_flux"))
from t20_jobs_124_data import JOBS_124

kh_path = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap20/KeHoach_Video_Tap20.md"
text = kh_path.read_text(encoding="utf-8")

# Tạo nội dung B4 mới
b4_lines = [
    "## B4. Danh mục 124 Ảnh Nền Liên kết (Chuẩn `assets/bg/t20_a*.png` theo H25)",
    "",
    "Toàn bộ 124 ảnh nền Dark Graphic Novel Noir được phân bổ đều cho 241 câu thoại (5 Hồi, trung bình 1.94 câu/ảnh, 0 lặp ảnh):",
    ""
]

by_act = {}
for j in JOBS_124:
    by_act.setdefault(j["act"], []).append(j)

act_titles = {
    1: "HỒI 1: CUỘC PHỎNG VẤN ĐỊNH MỆNH & TIN BÁO TỪ THÙNG RÁC",
    2: "HỒI 2: BỨC TƯỢNG ĐÁ TRONG PHÒNG HỎI CUNG & CÚ SỐC NHẬN THỨC",
    3: "HỒI 3: GIẢI MÃ TÂM LÝ: KẺ RÌNH RẬP NGẦM & PHẢN ỨNG ĐÓNG BĂNG KỲ DỊ",
    4: "HỒI 4: PHÁN QUYẾT CHUNG THÂN & SỰ TRỪNG PHẠT CỦA CÔNG LÝ",
    5: "HỒI 5: BÀI HỌC CẢNH TỈNH & 4 CẢNH BÁO ĐỎ PHÒNG NGỪA",
}

for act in sorted(by_act):
    jobs = by_act[act]
    b4_lines.append(f"### Hồi {act} ({len(jobs)} ảnh — {act_titles[act]})")
    for j in jobs:
        sids_str = "–".join(j["sids"]) if len(j["sids"]) > 1 else j["sids"][0]
        b4_lines.append(f"- `{j['name']}`: ({sids_str}) {j['desc']}")
    b4_lines.append("")

b4_new_text = "\n".join(b4_lines).strip()

# Thay thế B4 cũ
pattern = re.compile(r"## B4\. Danh mục \d+ Ảnh Nền Liên kết.*?(?=## B5\.|$)", re.DOTALL)
new_text, n = pattern.subn(b4_new_text + "\n\n", text)
assert n == 1, f"Không tìm thấy duy nhất 1 mục B4 (n={n})"

kh_path.write_text(new_text, encoding="utf-8")
print(f"Đã cập nhật mục B4 trong: {kh_path}")
