#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them dong provenance cho DeXuat_Sua_Tap06.md (L7) — idempotent."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PROV = ROOT / "provenance.json"
F = "02_SAN_XUAT/Tap06/DeXuat_Sua_Tap06.md"

ROW = {
    "file": F,
    "loai": "gói đề xuất sửa (7 câu kịch bản + 11 chữ trên hình) — CHƯA ÁP DỤNG",
    "cong_cu": ".work/_gen_t06_fix_proposal.py (generator) — câu hiện tại trích tự động từ .work/script_tap06.json",
    "ngay": "2026-11-03",
    "prompt": None,
    "seed": None,
    "dieu_khoan": "Chỉ trích dẫn nguồn công khai; không sao chép nội dung có bản quyền",
    "kiem_tra_thuong_mai": "đạt",
    "ghi_chu": ("Kịch bản + bảng shot + video KHÔNG đổi. Blocker: Higgs Audio v3 chỉ chạy được trên Kaggle GPU — "
                "máy dựng không có GPU/kaggle CLI/kaggle.json/torch/mlx_audio (đo 03/11/2026) ⇒ không tạo lại được "
                "7 file WAV. Quy trình 6 bước trong §C của file. A11 #93, #94"),
}

prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
before = len(prov)
prov = [e for e in prov if e.get("file") != F]
prov.append(ROW)
PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"provenance.json: {before} -> {len(prov)} dong (them 1 dong cho {F})")
