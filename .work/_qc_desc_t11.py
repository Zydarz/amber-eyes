#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_qc_desc_t11.py — Kiểm định chất lượng mô tả Tập 11 trên 4 ngôn ngữ (VI, EN, JA, KO).
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

INDICATORS = [
    "DƯ CHẤN XÃ HỘI",
    "VẬT HÓA NẠN NHÂN",
    "CƠ CHẾ CHIA NGĂN",
    "BẢN NGÃ ÁI KỶ SỤP ĐỔ",
    "HỆ THỐNG TỰ BÀO CHỮA",
    "NGÒI NỔ TÂM LÝ",
    "DẤU ẤN SIGNATURE",
    "QUỸ ĐẠO LEO THANG",
    "HIỆU ỨNG HÀO QUANG",
    "NẠN NHÂN HỌC",
]

INDICATORS_EN = [
    "SOCIAL IMPACT",
    "OBJECTIFICATION",
    "COGNITIVE COMPARTMENTALIZATION",
    "NARCISSISTIC COLLAPSE",
    "TECHNIQUES OF NEUTRALIZATION",
    "PSYCHOLOGICAL TRIGGER",
    "SIGNATURE VS. MODUS OPERANDI",
    "FANTASY ADDICTION",
    "HALO EFFECT",
    "VICTIMOLOGY",
]

INDICATORS_JA = [
    "社会的余波",
    "被害者の客体化",
    "心理的区画化",
    "自己愛の崩壊",
    "自己正当化",
    "心理的引き金",
    "署名（Signature）",
    "妄想への耽溺",
    "後光効果",
    "被害者学",
]

INDICATORS_KO = [
    "사회적 파장",
    "피해자의 객체화",
    "심리적 구획화",
    "나르시시즘적 붕괴",
    "자기 정당화",
    "심리적 방아쇠",
    "시그니처(Signature)",
    "환상 중독",
    "후광 효과",
    "피해자학",
]


def check_file(path: Path, indicators: list, lang: str):
    if not path.exists():
        print(f"[{lang}] LỖI: Tệp không tồn tại: {path}")
        return False
    text = path.read_text(encoding="utf-8")
    char_count = len(text.strip())
    
    # 1. Kiểm tra giới hạn 5000 ký tự
    if char_count > 5000:
        print(f"[{lang}] LỖI: Dung lượng vượt trần 5000 ký tự ({char_count:,} ký tự)")
        return False
        
    # 2. Kiểm tra 10 chỉ dấu
    matched = 0
    missing = []
    for ind in indicators:
        if ind.lower() in text.lower():
            matched += 1
        else:
            missing.append(ind)
            
    if matched < 10:
        print(f"[{lang}] LỖI: Thiếu {10 - matched}/10 chỉ dấu tâm lý ({missing})")
        return False
        
    print(f"[{lang}] {path.name}: {matched}/10 chỉ dấu | {char_count:,} ký tự (<= 5000) | Trạng thái: PASS")
    return True


def check_file_parity(p1: Path, p2: Path):
    if not p1.exists() or not p2.exists():
        return False
    t1 = p1.read_text(encoding="utf-8").strip()
    t2 = p2.read_text(encoding="utf-8").strip()
    return t1 == t2


def check_double_cr(path: Path):
    if not path.exists():
        return True
    raw = path.read_bytes()
    return b"\r\r\n" not in raw


def main():
    print("=== KIỂM ĐỊNH 10 CHỈ DẤU TÂM LÝ TRONG MÔ TẢ TẬP 11 ===")
    vi_ok = check_file(ROOT / "02_SAN_XUAT" / "Tap11" / "mo_ta.txt", INDICATORS, "VI")
    en_ok = check_file(ROOT / "02_SAN_XUAT" / "Tap11_EN" / "description.txt", INDICATORS_EN, "EN")
    ja_ok = check_file(ROOT / "02_SAN_XUAT" / "Tap11_JA" / "description.txt", INDICATORS_JA, "JA")
    ko_ok = check_file(ROOT / "02_SAN_XUAT" / "Tap11_KO" / "description.txt", INDICATORS_KO, "KO")
    
    all_ok = vi_ok and en_ok and ja_ok and ko_ok
    
    print("\n=== KIỂM ĐỊNH ĐỒNG BỘ FILE XUẤT BẢN & GỐC ===")
    pairs = [
        (ROOT / "02_SAN_XUAT" / "Tap11" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap11" / "xuat_ban" / "mo_ta.txt"),
        (ROOT / "02_SAN_XUAT" / "Tap11" / "nguon_tham_khao.md", ROOT / "02_SAN_XUAT" / "Tap11" / "xuat_ban" / "nguon_tham_khao.md"),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap11_EN" / "xuat_ban" / "description.txt"),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap11_EN" / "description.txt"),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "nguon_tham_khao_EN.md", ROOT / "02_SAN_XUAT" / "Tap11_EN" / "xuat_ban" / "nguon_tham_khao_EN.md"),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap11_JA" / "xuat_ban" / "description.txt"),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap11_JA" / "description.txt"),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "nguon_tham_khao_JA.md", ROOT / "02_SAN_XUAT" / "Tap11_JA" / "xuat_ban" / "nguon_tham_khao_JA.md"),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "description.txt", ROOT / "02_SAN_XUAT" / "Tap11_KO" / "xuat_ban" / "description.txt"),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "mo_ta.txt", ROOT / "02_SAN_XUAT" / "Tap11_KO" / "description.txt"),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "nguon_tham_khao_KO.md", ROOT / "02_SAN_XUAT" / "Tap11_KO" / "xuat_ban" / "nguon_tham_khao_KO.md"),
    ]
    
    parity_ok = True
    for p1, p2 in pairs:
        matched = check_file_parity(p1, p2)
        if not matched:
            print(f"  LỖI lệch file: {p1.relative_to(ROOT)} != {p2.relative_to(ROOT)}")
            parity_ok = False
        else:
            print(f"  OK: {p1.relative_to(ROOT)} == {p2.relative_to(ROOT)}")
            
    print("\n=== KIỂM ĐỊNH LINE ENDING (DOUBLE CR == 0) ===")
    all_files = [p for p, _ in pairs] + [p for _, p in pairs]
    unique_files = sorted(set(all_files))
    bad_cr = []
    for f in unique_files:
        if not check_double_cr(f):
            bad_cr.append(f)
            
    if bad_cr:
        print(f"  LỖI double CR tại: {[str(f.relative_to(ROOT)) for f in bad_cr]}")
    else:
        print(f"  ✅ 100% ({len(unique_files)}/{len(unique_files)}) files đạt chuẩn LF thuần (double_cr=0)")
        
    final_pass = all_ok and parity_ok and not bad_cr
    if final_pass:
        print("\n>>> TẤT CẢ CÁC CỔNG KIỂM ĐỊNH MÔ TẢ TẬP 11: 100% PASS! <<<")
        sys.exit(0)
    else:
        print("\n>>> CÓ LỖI TRONG KIỂM ĐỊNH MÔ TẢ TẬP 11! <<<")
        sys.exit(1)


if __name__ == "__main__":
    main()
