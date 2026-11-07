# -*- coding: utf-8 -*-
"""QC script for Tap 17 descriptions."""
import sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path('.')

files = [
    ('VI', ROOT / '02_SAN_XUAT' / 'Tap17' / 'mo_ta.txt'),
    ('VI_xuatban', ROOT / '02_SAN_XUAT' / 'Tap17' / 'xuat_ban' / 'mo_ta.txt'),
    ('EN', ROOT / '02_SAN_XUAT' / 'Tap17_EN' / 'description.txt'),
    ('EN_xuatban', ROOT / '02_SAN_XUAT' / 'Tap17_EN' / 'xuat_ban' / 'description.txt'),
    ('JA', ROOT / '02_SAN_XUAT' / 'Tap17_JA' / 'description.txt'),
    ('JA_xuatban', ROOT / '02_SAN_XUAT' / 'Tap17_JA' / 'xuat_ban' / 'description.txt'),
    ('KO', ROOT / '02_SAN_XUAT' / 'Tap17_KO' / 'description.txt'),
    ('KO_xuatban', ROOT / '02_SAN_XUAT' / 'Tap17_KO' / 'xuat_ban' / 'description.txt'),
]

all_pass = True
print("=== BÁO CÁO QC MÔ TẢ TẬP 17 (TRẦN <= 5000 KÝ TỰ) ===")
for label, p in files:
    if not p.exists():
        print(f"FAIL: File not found {p}")
        all_pass = False
        continue
    content = p.read_text(encoding='utf-8').strip()
    n_chars = len(content)
    status = "PASS" if n_chars <= 5000 else "FAIL (>5000)"
    if n_chars > 5000:
        all_pass = False
    print(f"[{label:12s}] {n_chars:4d} ký tự | {status} | {p}")

print("\nKẾT QUẢ:", "TẤT CẢ ĐẠT PASS (<= 5000 ký tự)" if all_pass else "CÓ FILE LỖI FAIL")
if not all_pass:
    sys.exit(1)
