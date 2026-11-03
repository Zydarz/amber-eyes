#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat provenance.json cho lop nguon Tap06 (L7).

- mo_ta.txt / nguon_tham_khao.md (thanh pham) -> cap nhat mo ta + trang thai
- them 2 dong moi cho file GENERATOR trong 02_SAN_XUAT/Tap06/
"""
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PROV = ROOT / "provenance.json"
NGAY = "2026-11-02"

NEW = [
    {
        "file": "02_SAN_XUAT/Tap06/nguon_mo_ta.txt",
        "loai": "KHỐI nguồn chèn vào mục '📚 NGUỒN THAM KHẢO' của mô tả YouTube (20 nguồn, 2503 ký tự)",
        "cong_cu": ".work/_gen_t06_sources.py (generator) — có validator chặn nếu URL chưa kiểm chứng HTTP 200",
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Chỉ trích dẫn nguồn công khai; không sao chép nội dung có bản quyền",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "Sinh từ bảng nguồn; KHÔNG sửa tay file thành phẩm (A11 #70)",
    },
    {
        "file": "02_SAN_XUAT/Tap06/nguon_tham_khao.md",
        "loai": "BẢNG đối chiếu 58 mốc dữ kiện × 20 nguồn công khai (mỗi URL đã kiểm chứng HTTP 200 ngày 02/11/2026)",
        "cong_cu": ".work/_gen_t06_sources.py (generator) — validator 4 cổng: URL 200 + nội dung khác rỗng · mã câu tồn tại trong script_tap06.json · khoá nguồn hợp lệ & mọi nguồn đều được dùng · không trùng mã câu",
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Chỉ trích dẫn nguồn công khai; không sao chép nội dung có bản quyền",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "58 mốc: 51 mức ✅ · 7 mức ⚠ (1.08#1, 2.06#3, 2.11#2, 2.11#3, 3.06#1, 3.11#1, 5.02#3) — cần người dùng duyệt lại câu chữ trong kịch bản",
    },
]

prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
before = len(prov)

# L5: sao lưu bản cũ trước khi ghi đè
import shutil
CU = ROOT / ".work" / "_cu"
CU.mkdir(parents=True, exist_ok=True)
shutil.copy2(PROV, CU / "provenance_truoc_nguon_t06.json")
print(f"backup -> {CU / 'provenance_truoc_nguon_t06.json'}")

UPD = {
    "02_SAN_XUAT/Tap06/xuat_ban/mo_ta.txt": {
        "loai": "mô tả YouTube (sinh ra, KHÔNG sửa tay — sửa ở package.py + edition.py) — 4067 ký tự",
        "ghi_chu": ("Có dòng ghi công Higgs Audio (voice_credit) + dòng hashtag; mốc chương lấy từ timeline_s_t06.json; "
                    "mục '📚 NGUỒN THAM KHẢO' lấp đầy 20 nguồn công khai đã kiểm chứng HTTP 200 (02/11/2026). "
                    "Sinh lại bằng .work/_regen_desc_t06.py — gọi description() trực tiếp, KHÔNG gọi CLI nên thumbnail.png và Tap06_master.mp4 giữ nguyên hash (A11 #72)"),
    },
    "02_SAN_XUAT/Tap06/xuat_ban/nguon_tham_khao.md": {
        "loai": "bảng đối chiếu 58 mốc dữ kiện × 20 nguồn công khai — mỗi URL đã kiểm chứng HTTP 200",
        "cong_cu": ".work/package.py description() (chép từ 02_SAN_XUAT/Tap06/nguon_tham_khao.md)",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": ("Trước đó rỗng ⇒ package.py ghi bảng 'cần bổ sung' rỗng và mô tả thiếu mục NGUỒN THAM KHẢO. "
                    "Nay đã điền 58 dòng có link thật; 7 dòng mức ⚠ chờ người dùng duyệt câu chữ kịch bản"),
    },
}

for e in prov:
    f = e.get("file")
    if f in UPD:
        e.update(UPD[f])

prov = [e for e in prov if e.get("file") not in
        ("02_SAN_XUAT/Tap06/nguon_mo_ta.txt", "02_SAN_XUAT/Tap06/nguon_tham_khao.md")]
prov.extend(NEW)

PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"provenance.json: {before} -> {len(prov)} dong")
