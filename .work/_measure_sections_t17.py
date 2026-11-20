# -*- coding: utf-8 -*-
"""Đo chiều dài từng khối của mô tả Tập 17 để rút gọn chính xác."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_descriptions_t17 as M  # noqa: E402

for lang in ["VI", "EN"]:
    chap, _ = M.chapters(lang)
    body = {"VI": M.BODY_VI, "EN": M.BODY_EN}[lang]
    short = {"VI": M.SHORT_VI, "EN": M.SHORT_EN}[lang]
    parts = [
        ("tiêu đề + brand", len(M.TITLES[lang]) + len(" | Amber eyes")),
        ("thân bài (mở đầu + 10 chỉ dấu)", len(body)),
        ("đầu chương", len(M.HEADS[lang]) + 1 + len("\n".join(chap))),
        ("cảnh báo", len(M.ADVISORY[lang])),
        ("nguồn", len(M.SRC_HEADS[lang]) + 1 + len(short)),
        ("hotline", len(M.SOS[lang])),
        ("hashtag", len(M.TAGS[lang])),
        ("dòng trống", 14),
    ]
    print(f"--- {lang} (tổng {sum(v for _, v in parts)}) ---")
    for name, v in parts:
        print(f"   {name:38s} {v:5d}")
    print(f"   {'MỤC TIÊU':38s} {5000 - sum(v for _, v in parts):5d}  (cần cắt thêm)")
