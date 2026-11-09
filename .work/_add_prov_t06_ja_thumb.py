#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 JA — ghi dòng provenance cho thumbnail.png bản Nhật (L7).

Idempotent: chạy lại không nhân bản dòng.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
PROV = ROOT / "provenance.json"

FILE = "02_SAN_XUAT/Tap06_JA/xuat_ban/thumbnail.png"
ENTRY = {
    "file": FILE,
    "loai": "ảnh đại diện 1280×720 (RGB)",
    "cong_cu": ".work/package.py thumbnail() — nền t6_clown_mirror_chiaroscuro + chữ Pillow (YuGothB.ttc)",
    "ngay": "2026-11-09",
    "prompt": None,
    "seed": None,
    "dieu_khoan": "Nền tự vẽ bằng code; không dùng tài sản tải ngoài",
    "kiem_tra_thuong_mai": "đạt",
    "ghi_chu": ("Dòng chữ: 道化師の微笑みと · 床下の29の秘密 (EPISODES[\"06\"][\"thumb\"] nhánh JA). "
                "Sinh bằng .work/_make_thumb_ja_t06.py — gọi TRỰC TIẾP package.thumbnail() "
                "(A11 #72: KHÔNG gọi CLI package.py vì CLI ghi đè thumbnail/mô tả đã xuất bản). "
                "Soi mắt: nền đúng tập, chữ Nhật không tofu, logo + 2 avatar vai đúng."),
}

data = json.loads(PROV.read_text(encoding="utf-8"))
hits = [i for i, x in enumerate(data)
        if isinstance(x, dict) and x.get("file") == FILE]
if hits:
    data[hits[0]] = ENTRY
    print(f"-> cap nhat dong da co (index {hits[0]})")
    for i in hits[1:]:
        data.pop(i)
        print(f"   xoa dong trung lap (index {i})")
else:
    data.append(ENTRY)
    print("-> them dong moi")

PROV.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"provenance.json: {len(data)} muc")
