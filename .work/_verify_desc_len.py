# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

langs = {
    "VN": ("02_SAN_XUAT/Tap01/mo_ta.txt", "02_SAN_XUAT/Tap01/xuat_ban/mo_ta.txt"),
    "EN": ("02_SAN_XUAT/Tap01_EN/mo_ta.txt", "02_SAN_XUAT/Tap01_EN/xuat_ban/mo_ta.txt"),
    "JA": ("02_SAN_XUAT/Tap01_JA/mo_ta.txt", "02_SAN_XUAT/Tap01_JA/xuat_ban/mo_ta.txt"),
    "KO": ("02_SAN_XUAT/Tap01_KO/mo_ta.txt", "02_SAN_XUAT/Tap01_KO/xuat_ban/mo_ta.txt"),
}

print(f"{'Ngôn ngữ':<8} | {'Đường dẫn':<45} | {'Ký tự':<8} | {'Trạng thái (<=5000)':<20}")
print("-" * 88)

all_ok = True
for lang, paths in langs.items():
    for p in paths:
        text = Path(p).read_text(encoding="utf-8")
        chars = len(text)
        ok = chars <= 5000
        if not ok:
            all_ok = False
        status = "PASS (<= 5.000)" if ok else f"FAIL (VƯỢT {chars - 5000})"
        print(f"{lang:<8} | {p:<45} | {chars:<8} | {status:<20}")

print("-" * 88)
print(f"Tổng kết: {'TẤT CẢ 8 FILE ĐẠT CHUẨN (100% PASS)' if all_ok else 'CÓ FILE VƯỢT QUÁ 5.000 KÝ TỰ'}")
