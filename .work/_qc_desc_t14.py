# -*- coding: utf-8 -*-
"""QC kiểm tra tính toàn vẹn và độ dài tất cả các file mô tả của Tập 14."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

desc_files = [
    # Tiếng Việt
    ROOT / "02_SAN_XUAT" / "Tap14" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap14" / "xuat_ban" / "mo_ta.txt",
    
    # Tiếng Anh
    ROOT / "02_SAN_XUAT" / "Tap14_EN" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_EN" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_EN" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_EN" / "xuat_ban" / "mo_ta.txt",
    
    # Tiếng Nhật
    ROOT / "02_SAN_XUAT" / "Tap14_JA" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_JA" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_JA" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_JA" / "xuat_ban" / "mo_ta.txt",
    
    # Tiếng Hàn
    ROOT / "02_SAN_XUAT" / "Tap14_KO" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_KO" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_KO" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap14_KO" / "xuat_ban" / "mo_ta.txt",
]

all_pass = True
print("================================================================")
print("KIỂM THỬ QC ĐỘ DÀI MÔ TẢ YOUTUBE TẬP 14 (TRẦN <= 5000 KÝ TỰ)")
print("================================================================")

for p in desc_files:
    if not p.exists():
        print(f"FAIL File not found: {p.relative_to(ROOT)}")
        all_pass = False
        continue
    content = p.read_text(encoding="utf-8").strip()
    char_len = len(content)
    status = "PASS" if char_len <= 5000 else "FAIL (> 5000)"
    if char_len > 5000:
        all_pass = False
    print(f"[{status}] {p.relative_to(ROOT)} -> {char_len:,} ký tự")

print(f"\n>>> KẾT QUẢ QC MÔ TẢ TẬP 14: {'ALL GREEN - PASSED' if all_pass else 'FAILED'} <<<")
