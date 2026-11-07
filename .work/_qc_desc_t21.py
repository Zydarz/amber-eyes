# -*- coding: utf-8 -*-
"""Comprehensive QC for Episode 21 descriptions across all 4 languages."""

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\amber-eyes")

desc_files = {
    "VN": [
        ROOT / "02_SAN_XUAT" / "Tap21" / "mo_ta.txt",
        ROOT / "02_SAN_XUAT" / "Tap21" / "xuat_ban" / "mo_ta.txt",
    ],
    "EN": [
        ROOT / "02_SAN_XUAT" / "Tap21_EN" / "description.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_EN" / "mo_ta.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_EN" / "xuat_ban" / "description.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_EN" / "xuat_ban" / "mo_ta.txt",
    ],
    "JA": [
        ROOT / "02_SAN_XUAT" / "Tap21_JA" / "description.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_JA" / "mo_ta.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_JA" / "xuat_ban" / "description.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_JA" / "xuat_ban" / "mo_ta.txt",
    ],
    "KO": [
        ROOT / "02_SAN_XUAT" / "Tap21_KO" / "description.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_KO" / "mo_ta.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_KO" / "xuat_ban" / "description.txt",
        ROOT / "02_SAN_XUAT" / "Tap21_KO" / "xuat_ban" / "mo_ta.txt",
    ],
}

all_green = True
print("=" * 70)
print("QC AUDIT: EPISODE 21 YOUTUBE DESCRIPTIONS (STRICTLY <= 5000 CHARS)")
print("=" * 70)

for lang, paths in desc_files.items():
    print(f"\n--- CHECKING {lang} ---")
    for p in paths:
        if not p.exists():
            print(f"FAIL: File not found: {p.relative_to(ROOT)}")
            all_green = False
            continue
        text = p.read_text(encoding="utf-8")
        raw = p.read_bytes()
        d_cr = raw.count(b"\r\r\n")
        cnt = len(text)
        
        # Check required sections
        has_10_indicators = (
            "1." in text and "2." in text and "3." in text and "4." in text and "5." in text
            and "6." in text and "7." in text and "8." in text and "9." in text and "10." in text
        )
        has_timestamps = "00:00" in text and "00:23" in text
        has_disclaimer = "Amber eyes" in text
        has_hotline = "111" in text or "988" in text or "189" in text or "109" in text
        has_hashtags = "#AmberEyes" in text
        
        status = cnt <= 5000 and d_cr == 0 and has_10_indicators and has_timestamps and has_hotline and has_hashtags
        print(f"File: {p.relative_to(ROOT)}")
        print(f"  Length: {cnt} chars ({'PASS <= 5000' if cnt <= 5000 else 'FAIL > 5000'})")
        print(f"  Double CR: {d_cr}")
        print(f"  10 Indicators: {'PASS' if has_10_indicators else 'FAIL'}")
        print(f"  Timestamps: {'PASS' if has_timestamps else 'FAIL'}")
        print(f"  Hotline: {'PASS' if has_hotline else 'FAIL'}")
        print(f"  Overall: {'PASS' if status else 'FAIL'}")
        all_green = all_green and status

print("\n" + "=" * 70)
print(f"FINAL RESULT: {'>>> ALL DESCRIPTIONS PASSED QC (100% GREEN) <<<' if all_green else '>>> QC FAILED <<<'}")
print("=" * 70)
