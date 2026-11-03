#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xác minh toàn diện 29 file mo_ta.txt, nguon_mo_ta.txt, nguon_tham_khao.md."""
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")
all_pass = True

print(f"{'Tập':<6} | {'mo_ta':<6} | {'xuat_ban':<8} | {'nguon_txt':<9} | {'nguon_md':<8} | {'Ký tự':<6} | {'Dòng nguồn':<10} | Trạng thái")
print("-" * 75)

for i in range(1, 30):
    k = f"{i:02d}"
    ep_dir = ROOT / "02_SAN_XUAT" / f"Tap{k}"
    xb_dir = ep_dir / "xuat_ban"

    mota1 = ep_dir / "mo_ta.txt"
    mota2 = xb_dir / "mo_ta.txt"
    nguon_txt = ep_dir / "nguon_mo_ta.txt"
    nguon_md = ep_dir / "nguon_tham_khao.md"

    f_mota1 = mota1.exists()
    f_mota2 = mota2.exists()
    f_nguon_txt = nguon_txt.exists()
    f_nguon_md = nguon_md.exists()

    if not (f_mota1 and f_mota2 and f_nguon_txt and f_nguon_md):
        print(f"Tap {k:<2} | {str(f_mota1):<6} | {str(f_mota2):<8} | {str(f_nguon_txt):<9} | {str(f_nguon_md):<8} | THIẾU FILE")
        all_pass = False
        continue

    content = mota1.read_text(encoding="utf-8")
    has_chua_co = ("[CHƯA CÓ" in content or "[CHUA CO" in content)
    has_chap = "⏱ MỐC CHƯƠNG" in content
    has_luuy = "⚠️ LƯU Ý" in content
    has_nguon = "📚 NGUỒN THAM KHẢO" in content
    has_hotline = "🆘 Nếu bạn biết một trẻ em" in content
    has_hash = "#" in content

    # Đo độ dài phần nguồn
    src_lines = 0
    if has_nguon and has_hotline:
        part = content.split("📚 NGUỒN THAM KHẢO")[1].split("🆘")[0].strip()
        src_lines = len(part.splitlines())

    if has_chua_co or not (has_chap and has_luuy and has_nguon and has_hotline and has_hash):
        print(f"Tap {k:<2} | {str(f_mota1):<6} | {str(f_mota2):<8} | {str(f_nguon_txt):<9} | {str(f_nguon_md):<8} | {len(content):<6} | {src_lines:<10} | LỖI NỘI DUNG")
        all_pass = False
    else:
        print(f"Tap {k:<2} | {str(f_mota1):<6} | {str(f_mota2):<8} | {str(f_nguon_txt):<9} | {str(f_nguon_md):<8} | {len(content):<6} | {src_lines:<10} | ✅ ĐẠT CHUẨN")

print("-" * 75)
print("KẾT LUẬN TOÀN BỘ 29 TẬP:", "100% ĐẠT CHUẨN" if all_pass else "CÓ LỖI CẦN XỬ LÝ")
