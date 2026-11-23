# -*- coding: utf-8 -*-
"""Cập nhật danh sách 124 ảnh nền Tập 20 vào Danh_Sach_Anh_Tap20.md"""
import json
import sys
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work/kaggle_flux"))
from t20_jobs_124_data import JOBS_124

lines = [
    "# DANH SÁCH 124 ẢNH NỀN TẬP 20 (CHUẨN FLUX.2 DEEP NOIR 2K)",
    "",
    "> **Hồ sơ:** Stephen McDaniel (Án mạng Trường Luật Mercer - Macon, Georgia)",
    "> **Kịch bản:** 241 câu thoại (Hệ sinh thái 10 chỉ dấu tâm lý A2c & Luật K10)",
    "> **Quy chuẩn kỹ thuật:** `QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` v1.0 (2112×1188, dìm màu Sat 0.65, Contrast 1.15, Vignette 45%, Film Grain 35mm)",
    "> **Trạng thái:** 124/124 ảnh đã được sinh và trích xuất 100% vào `assets/bg/`",
    "",
    "| STT | Tên file | Hồi | Phân đoạn câu | Mô tả bối cảnh & Ẩn dụ noir |",
    "|---|---|:---:|:---:|---|",
]

for idx, j in enumerate(JOBS_124, 1):
    sids_str = "–".join(j["sids"]) if len(j["sids"]) > 1 else j["sids"][0]
    lines.append(f"| {idx:03d} | `{j['name']}.png` | Hồi {j['act']} | {sids_str} | {j['desc']} |")

out_file = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap20/Danh_Sach_Anh_Tap20.md"
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Đã cập nhật thành công {len(JOBS_124)} dòng vào: {out_file}")
