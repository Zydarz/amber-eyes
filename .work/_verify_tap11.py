#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
BG_DIR = ROOT / "assets" / "bg"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap11"
PROV_FILE = ROOT / "provenance.json"

jobs = json.loads((WORK / "bg_jobs_tap11.json").read_text(encoding="utf-8"))
print(f"=== KIỂM TRA TẬP 11 ===")
print(f"Tổng số jobs định nghĩa: {len(jobs)}")

missing = []
wrong_size = []
for j in jobs:
    f = BG_DIR / f"{j['name']}.png"
    if not f.exists():
        missing.append(j["name"])
    else:
        with Image.open(f) as im:
            if im.size != (2112, 1188):
                wrong_size.append((j["name"], im.size))

print(f"Ảnh đã tạo: {len(jobs) - len(missing)} / {len(jobs)}")
if missing:
    print(f"Thiếu ({len(missing)}): {missing[:5]}...")
if wrong_size:
    print(f"Sai kích thước ({len(wrong_size)}): {wrong_size[:5]}")

prov = json.loads(PROV_FILE.read_text(encoding="utf-8")) if PROV_FILE.exists() else []
t11_prov = [p for p in prov if "assets/bg/t11_" in p.get("file", "")]
print(f"Bản ghi provenance cho t11: {len(t11_prov)} / {len(jobs)}")

danh_sach = OUT_DIR / "Danh_Sach_Anh_Tap11.md"
review = OUT_DIR / "REVIEW_Bo_Anh_Tap11.md"
contact_sheet = OUT_DIR / "contact_sheet_t11.png"

print(f"Danh_Sach_Anh_Tap11.md: {'CÓ' if danh_sach.exists() else 'CHƯA'}")
print(f"REVIEW_Bo_Anh_Tap11.md: {'CÓ' if review.exists() else 'CHƯA'}")
print(f"contact_sheet_t11.png: {'CÓ' if contact_sheet.exists() else 'CHƯA'}")

if not missing and not wrong_size and len(t11_prov) == len(jobs) and danh_sach.exists() and review.exists() and contact_sheet.exists():
    print(">>> TẤT CẢ TIÊU CHUẨN HOÀN TOÀN ĐẠT CHUẨN 100%! <<<")
else:
    print(">>> ĐANG CHỜ HOÀN TẤT CÁC BƯỚC CÒN LẠI <<<")
